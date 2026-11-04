# qwen-image-3.0-pro 接入文档

# qwen-image-3.0-pro 接入文档

<a id="overview"></a>

## 模型用途与调用 ID

官方模型 ID：`qwen-image-3.0-pro`

可用操作：生成图片 / 编辑图片。

新接入请使用下表推荐的调用 ID，并将完整 ID 填入请求的 model 字段。不同任务的参数要求见对应章节。

<a id="invocation-ids"></a>

### 推荐调用 ID 与用途

| 请求 model | 用途与参数 |
| --- | --- |
| `qwen-image-3.0-pro` | [生成图片](#operation-1) / [编辑图片](#operation-2) |

同一章节对应的调用 ID 可以使用该章节的请求结构；复制示例后，只在切换这些入口时替换 model。跨章节切换时需同时核对参数。费用按实际调用 ID 的报价与账单结算。

参数表按当前 CR 调用契约列出。省略可选字段时使用表内默认值；未注明固定默认值时，省略该字段使用模型默认行为。更换模型时重新核对输入与限制。

<a id="authentication"></a>

## 调用前准备

登录 [CR 控制台](https://creative-reasoning.com/console/keys)，在 API Key 页面创建或复制完整密钥。将示例中的 `API_KEY` 替换为你的完整 API Key；请求使用 `Authorization: Bearer API_KEY`。API Key ID 是资源标识，不能代替密钥认证。

所有调用示例使用生产地址 `https://api.creative-reasoning.com`。示例已填写本模型的公开名称。更换模型时，需要重新核对参数、输入类型和限制。

cURL 示例在 Bash 或 Zsh 中运行，需要 cURL 和 Python 3（用于解析 JSON）。先确认 `curl --version` 和 `python3 --version` 可用。Python 示例还需要 requests，使用 `python3 -m pip install requests` 安装。

将 `https://media.example.com/...` 替换为你自己的素材 URL，确保 CR 能直接读取且在任务期间有效。本地路径或需登录的网页不能作为素材 URL；格式、数量和尺寸见本页参数表。

<a id="quickstart"></a>

## 最小可运行示例

cURL 和 Python 是同一操作的两种写法，选择一种运行即可。示例中的可选取值不代表模型默认值；可通过后面的参数表调整。

<a id="operation-1"></a>

### 生成图片

```http
POST https://api.creative-reasoning.com/unified/v1/images/tasks
```

model: `qwen-image-3.0-pro`

[常用参数](#operation-1-common) · [完整参数](#operation-1-parameters)

<a id="operation-1-curl"></a>

#### cURL

先运行一次提交命令。命令将完整响应保存在 `response.json`、响应头保存在 `response-headers.txt`，成功后从 `response.id` 取得 `TASK_ID`。保存这个 ID；等待结果时查询原任务，不要再次提交生成。本地解析报错时先检查 `response.json`；若已有任务 `id`，继续查询该任务。

```bash
python3 --version >/dev/null && \
curl --fail-with-body --silent --show-error \
  --request POST "https://api.creative-reasoning.com/unified/v1/images/tasks" \
  --header "Authorization: Bearer API_KEY" \
  --header "Content-Type: application/json" \
  --dump-header response-headers.txt \
  --output response.json \
  --data '{
  "model": "qwen-image-3.0-pro",
  "prompt": "A blue ceramic cup on a wooden table, soft daylight.",
  "n": 1,
  "size": "1024x1024"
}' && \
TASK_ID=$(python3 -c 'import json; print(json.load(open("response.json"))["id"])') && \
printf '%s\n' "$TASK_ID"
```

<a id="operation-1-python"></a>

#### Python

下面的 Python 示例是同一次操作的另一种调用方式。选择 cURL 或 Python 其中一种运行；分别运行会发起两次调用。

```python
import json
import time
import requests

api_key = "API_KEY"
headers = {"Authorization": f"Bearer {api_key}"}
payload = {
    "model": "qwen-image-3.0-pro",
    "prompt": "A blue ceramic cup on a wooden table, soft daylight.",
    "n": 1,
    "size": "1024x1024",
}
response = requests.post(
    "https://api.creative-reasoning.com/unified/v1/images/tasks",
    headers=headers, json=payload, timeout=120,
)
if not response.ok:
    print(response.status_code, response.text)
response.raise_for_status()
print("x-cr-usage-id:", response.headers.get("x-cr-usage-id"))
print("x-cr-request-id:", response.headers.get("x-cr-request-id"))
result = response.json()
task_id = result["id"]
print("task_id:", task_id)
with open("cr-task-id.txt", "w", encoding="utf-8") as saved:
    saved.write(task_id)

deadline = time.monotonic() + 600
while result["status"] in ("pending", "processing"):
    if time.monotonic() >= deadline:
        raise TimeoutError("本地等待结束；任务 ID 已保存到 cr-task-id.txt，稍后查询原任务。")
    response = requests.get(
        f"https://api.creative-reasoning.com/unified/v1/tasks/{task_id}/wait",
        headers=headers, timeout=40,
    )
    if response.status_code == 429:
        time.sleep(2)
        response = requests.get(
            f"https://api.creative-reasoning.com/unified/v1/tasks/{task_id}",
            headers=headers, timeout=40,
        )
    if not response.ok:
        print(response.status_code, response.text)
    response.raise_for_status()
    result = response.json()
    if result["status"] in ("pending", "processing"):
        time.sleep(1)

if result["status"] == "failed":
    raise RuntimeError(result.get("error", {}))
if result["status"] != "completed":
    raise RuntimeError(result)
with open("cr-task-result.json", "w", encoding="utf-8") as saved:
    json.dump(result, saved, ensure_ascii=False, indent=2)
for item in result.get("data", []):
    if item.get("url"):
        print("result_url:", item["url"])
print("Saved result: cr-task-result.json")
```

Python 会保存任务 ID 到 cr-task-id.txt、完成结果到 cr-task-result.json，并输出结果 URL。若等待超时，继续查询保存的任务 ID，不要重新运行提交部分。

<a id="operation-1-response"></a>

#### 读取响应

首次受理返回 `202 Accepted`，正文的 `id` 是本次任务 ID；`status` 表示当前状态，`model` 是公开模型名称，`created_at` 是创建时间的 Unix 秒数，`poll_url` 是查询相对路径。`Location` 响应头也提供查询路径。将 `poll_url` 拼在 `https://api.creative-reasoning.com` 后可得到完整地址。受理不代表生成完成；按本页的任务查询步骤读取结果。

以下为响应结构示意，仅保留读取结果需要的字段。标识、URL、生成内容和错误信息必须从实际响应读取；所有大写占位值都不能复制为请求参数。示意内容不能用于推算实际耗时或费用。

提交被受理时，保存实际返回的 `id`。示意中的 `TASK_ID_FROM_RESPONSE` 只表示该响应字段，不是可查询的任务 ID。

```json
{
  "id": "TASK_ID_FROM_RESPONSE",
  "status": "pending",
  "model": "qwen-image-3.0-pro",
  "poll_url": "/unified/v1/tasks/TASK_ID_FROM_RESPONSE"
}
```

图片生成完成后，从 data\[\].url 读取下载地址。

```json
{
  "id": "TASK_ID_FROM_RESPONSE",
  "status": "completed",
  "model": "qwen-image-3.0-pro",
  "data": [
    {
      "url": "IMAGE_URL_FROM_RESPONSE"
    }
  ]
}
```

任务执行失败时，查询仍可返回 HTTP `200`，正文结构如下。先检查 `status`，再读取错误原因；失败结构不包含成功的 `data`。

```json
{
  "id": "TASK_ID_FROM_RESPONSE",
  "status": "failed",
  "model": "qwen-image-3.0-pro",
  "error": {
    "code": "task_failed",
    "message": "ERROR_MESSAGE_FROM_RESPONSE"
  }
}
```

<a id="operation-2"></a>

### 编辑图片

```http
POST https://api.creative-reasoning.com/unified/v1/images/edit-tasks
```

model: `qwen-image-3.0-pro`

[常用参数](#operation-2-common) · [完整参数](#operation-2-parameters)

<a id="operation-2-curl"></a>

#### cURL

先运行一次提交命令。命令将完整响应保存在 `response.json`、响应头保存在 `response-headers.txt`，成功后从 `response.id` 取得 `TASK_ID`。保存这个 ID；等待结果时查询原任务，不要再次提交生成。本地解析报错时先检查 `response.json`；若已有任务 `id`，继续查询该任务。

```bash
python3 --version >/dev/null && \
curl --fail-with-body --silent --show-error \
  --request POST "https://api.creative-reasoning.com/unified/v1/images/edit-tasks" \
  --header "Authorization: Bearer API_KEY" \
  --header "Content-Type: application/json" \
  --dump-header response-headers.txt \
  --output response.json \
  --data '{
  "model": "qwen-image-3.0-pro",
  "prompt": "Keep the person'"'"'s facial features and change the background to a softly lit studio.",
  "image": "https://media.example.com/portrait.png",
  "n": 1,
  "size": "1024x1024"
}' && \
TASK_ID=$(python3 -c 'import json; print(json.load(open("response.json"))["id"])') && \
printf '%s\n' "$TASK_ID"
```

<a id="operation-2-python"></a>

#### Python

下面的 Python 示例是同一次操作的另一种调用方式。选择 cURL 或 Python 其中一种运行；分别运行会发起两次调用。

```python
import json
import time
import requests

api_key = "API_KEY"
headers = {"Authorization": f"Bearer {api_key}"}
payload = {
    "model": "qwen-image-3.0-pro",
    "prompt": "Keep the person's facial features and change the background to a softly lit studio.",
    "image": "https://media.example.com/portrait.png",
    "n": 1,
    "size": "1024x1024",
}
response = requests.post(
    "https://api.creative-reasoning.com/unified/v1/images/edit-tasks",
    headers=headers, json=payload, timeout=120,
)
if not response.ok:
    print(response.status_code, response.text)
response.raise_for_status()
print("x-cr-usage-id:", response.headers.get("x-cr-usage-id"))
print("x-cr-request-id:", response.headers.get("x-cr-request-id"))
result = response.json()
task_id = result["id"]
print("task_id:", task_id)
with open("cr-task-id.txt", "w", encoding="utf-8") as saved:
    saved.write(task_id)

deadline = time.monotonic() + 600
while result["status"] in ("pending", "processing"):
    if time.monotonic() >= deadline:
        raise TimeoutError("本地等待结束；任务 ID 已保存到 cr-task-id.txt，稍后查询原任务。")
    response = requests.get(
        f"https://api.creative-reasoning.com/unified/v1/tasks/{task_id}/wait",
        headers=headers, timeout=40,
    )
    if response.status_code == 429:
        time.sleep(2)
        response = requests.get(
            f"https://api.creative-reasoning.com/unified/v1/tasks/{task_id}",
            headers=headers, timeout=40,
        )
    if not response.ok:
        print(response.status_code, response.text)
    response.raise_for_status()
    result = response.json()
    if result["status"] in ("pending", "processing"):
        time.sleep(1)

if result["status"] == "failed":
    raise RuntimeError(result.get("error", {}))
if result["status"] != "completed":
    raise RuntimeError(result)
with open("cr-task-result.json", "w", encoding="utf-8") as saved:
    json.dump(result, saved, ensure_ascii=False, indent=2)
for item in result.get("data", []):
    if item.get("url"):
        print("result_url:", item["url"])
print("Saved result: cr-task-result.json")
```

Python 会保存任务 ID 到 cr-task-id.txt、完成结果到 cr-task-result.json，并输出结果 URL。若等待超时，继续查询保存的任务 ID，不要重新运行提交部分。

<a id="operation-2-response"></a>

#### 读取响应

首次受理返回 `202 Accepted`，正文的 `id` 是本次任务 ID；`status` 表示当前状态，`model` 是公开模型名称，`created_at` 是创建时间的 Unix 秒数，`poll_url` 是查询相对路径。`Location` 响应头也提供查询路径。将 `poll_url` 拼在 `https://api.creative-reasoning.com` 后可得到完整地址。受理不代表生成完成；按本页的任务查询步骤读取结果。

以下为响应结构示意，仅保留读取结果需要的字段。标识、URL、生成内容和错误信息必须从实际响应读取；所有大写占位值都不能复制为请求参数。示意内容不能用于推算实际耗时或费用。

提交被受理时，保存实际返回的 `id`。示意中的 `TASK_ID_FROM_RESPONSE` 只表示该响应字段，不是可查询的任务 ID。

```json
{
  "id": "TASK_ID_FROM_RESPONSE",
  "status": "pending",
  "model": "qwen-image-3.0-pro",
  "poll_url": "/unified/v1/tasks/TASK_ID_FROM_RESPONSE"
}
```

图片生成完成后，从 data\[\].url 读取下载地址。

```json
{
  "id": "TASK_ID_FROM_RESPONSE",
  "status": "completed",
  "model": "qwen-image-3.0-pro",
  "data": [
    {
      "url": "IMAGE_URL_FROM_RESPONSE"
    }
  ]
}
```

任务执行失败时，查询仍可返回 HTTP `200`，正文结构如下。先检查 `status`，再读取错误原因；失败结构不包含成功的 `data`。

```json
{
  "id": "TASK_ID_FROM_RESPONSE",
  "status": "failed",
  "model": "qwen-image-3.0-pro",
  "error": {
    "code": "task_failed",
    "message": "ERROR_MESSAGE_FROM_RESPONSE"
  }
}
```

<a id="task-results"></a>

## 查询任务与保存结果

使用提交任务时的同一把 API Key。前面的 cURL 命令已从提交响应提取 `TASK_ID`；如果在新终端继续，请从保存的 `response.json` 再次读取该 `id`。不要使用示例 UUID、请求 ID 或其他任务的 ID。换一把 API Key 查询会返回 `404`，即使它们属于同一团队。

```bash
TASK_ID=$(python3 -c 'import json; print(json.load(open("response.json"))["id"])') && \
curl --fail-with-body --silent --show-error \
  "https://api.creative-reasoning.com/unified/v1/tasks/${TASK_ID}" \
  --header "Authorization: Bearer API_KEY"
```

普通 GET 返回当前状态。`/wait` 最多等待 30 秒；仍在执行时返回当前状态，可以继续等待同一个 ID。等待超时或断开连接不会取消任务。Python 示例最多在本地等待 10 分钟；本地等待结束或网络异常后，使用已保存的任务 ID 继续查询。

```bash
curl --fail-with-body --silent --show-error \
  "https://api.creative-reasoning.com/unified/v1/tasks/${TASK_ID}/wait" \
  --header "Authorization: Bearer API_KEY"
```

| status | 处理方式 |
| --- | --- |
| `pending` / `processing` | 任务尚未完成，继续查询原 ID，不重新 POST。 |
| `completed` | 生成完成，从 data 数组读取结果。 |
| `failed` | 生成失败，读取 error.code 与 error.message，再决定是否修改输入后重新发起。 |

任务查询返回 HTTP `200` 时仍可能是 `failed`，必须检查正文 `status`。错误码 `task_cancelled` 表示任务取消，`task_failed` 表示未进一步分类的失败。失败响应没有成功结果；不要只凭 HTTP 状态确认生成成功。

| 结果字段 | 含义 |
| --- | --- |
| `data[].url` | 生成结果的下载地址，直接使用完整 URL，不自行拼接。 |

上述字段只在相应产物中出现，不代表本模型支持所有产物。及时下载到自己的存储；图片链接可能过期。视频链接最多有效 24 小时，源文件更早失效时可能提前过期。任务终态正文自完成起保留 24 小时，之后查询返回 `410 task_expired`。重复查询不会延长链接或正文有效期。

<a id="idempotency"></a>

### 提交重试与幂等

异步任务提交支持可选的 `Idempotency-Key` 请求头。它是由调用方生成并保存在业务记录中的操作唯一标识，不是 API Key，也不用于认证。需要安全重试时，在第一次 POST 前生成它；同一操作重试复用相同值、API Key、接口和完全相同的请求正文。新操作使用新值。

```http
Idempotency-Key: YOUR_UNIQUE_OPERATION_ID
```

将 `YOUR_UNIQUE_OPERATION_ID` 替换为你为本次操作生成的唯一编号，例如 UUID。长度为 1–256 个不含空白的可打印 ASCII 字符。相同键与相同请求返回原任务；同键不同请求返回 `409 idempotency_conflict`。任务已完成时，幂等重试可返回 `200`。拿到任务 ID 后直接查询，不再重试提交。没有设置幂等头的 POST 超时后，不要盲目重发。

<a id="common-parameters"></a>

## 常用参数

<a id="operation-1-common"></a>

### 生成图片

| 字段 | 类型 | 字段来源 | 参数类别 | 必填 | 取值、默认值与限制 |
| --- | --- | --- | --- | --- | --- |
| `model` | string | CR 接口 | 请求参数 | 必填 | 使用本页示例中的精确模型 ID。 |
| `prompt` | string | CR 接口 | 请求参数 | 必填 | 生成或编辑描述。 |
| `aspect_ratio` | string | CR 接口 | 请求参数 | 可选 | 1:1、16:9、9:16、4:3、3:4、3:2、2:3、21:9、9:21。配合 quality 选择尺寸；省略不指定比例。 |
| `n` | integer | CR 接口 | 请求参数 | 可选 | 输出张数 1–6，默认 1。 |
| `quality` | string | CR 接口 | 请求参数 | 可选 | CR 分辨率档位：1K 或 2K；省略不指定档位。与 size 同时设置时必须匹配像素面积。 |
| `size` | string | CR 接口 | 请求参数 | 可选 | auto 或宽x高，例如 1024x1024；面积 262144–4194304 像素，宽高比 1:8–8:1。省略时模型自动选择。与 aspect\_ratio 不同时设置。 |

<a id="operation-2-common"></a>

### 编辑图片

| 字段 | 类型 | 字段来源 | 参数类别 | 必填 | 取值、默认值与限制 |
| --- | --- | --- | --- | --- | --- |
| `model` | string | CR 接口 | 请求参数 | 必填 | 使用本页示例中的精确模型 ID。 |
| `prompt` | string | CR 接口 | 请求参数 | 必填 | 生成或编辑描述。 |
| `image` | string \| string\[\] | CR 接口 | 请求参数 | 必填 | 提供时使用 1–3 张参考图片的 HTTPS URL 或 data URL；顺序对应提示词中的图片编号。不支持蒙版。 |
| `aspect_ratio` | string | CR 接口 | 请求参数 | 可选 | 1:1、16:9、9:16、4:3、3:4、3:2、2:3、21:9、9:21。配合 quality 选择尺寸；省略不指定比例。 |
| `n` | integer | CR 接口 | 请求参数 | 可选 | 输出张数 1–6，默认 1。 |
| `quality` | string | CR 接口 | 请求参数 | 可选 | CR 分辨率档位：1K 或 2K；省略不指定档位。与 size 同时设置时必须匹配像素面积。 |
| `size` | string | CR 接口 | 请求参数 | 可选 | auto 或宽x高，例如 1024x1024；面积 262144–4194304 像素，宽高比 1:8–8:1。省略时模型自动选择。与 aspect\_ratio 不同时设置。 |

<a id="parameters"></a>

## 完整参数

字段来源分为 CR 接口和模型原厂。图片和视频的原厂扩展使用 provider\_options；顶层请求参数不要重复放入该对象。

字段来源说明由谁定义字段，不表示所有模型都支持它。参数类别区分请求参数、操作参数和模型选项；取值、默认值及限制适用于本页列出的模型，换模型前需查阅目标模型的参数表。

必填：每次请求都要提供。条件必填：仅在使用对应输入类型、父对象或功能时必填，条件见说明。可选：可以省略；没有明确默认值的字段不应自行假定默认值。

<a id="operation-1-parameters"></a>

### 生成图片

| 字段 | 类型 | 字段来源 | 参数类别 | 必填 | 取值、默认值与限制 |
| --- | --- | --- | --- | --- | --- |
| `model` | string | CR 接口 | 请求参数 | 必填 | 使用本页示例中的精确模型 ID。 |
| `prompt` | string | CR 接口 | 请求参数 | 必填 | 生成或编辑描述。 |
| `aspect_ratio` | string | CR 接口 | 请求参数 | 可选 | 1:1、16:9、9:16、4:3、3:4、3:2、2:3、21:9、9:21。配合 quality 选择尺寸；省略不指定比例。 |
| `image` | string \| string\[\] | CR 接口 | 请求参数 | 可选 | 提供时使用 1–3 张参考图片的 HTTPS URL 或 data URL；顺序对应提示词中的图片编号。不支持蒙版。 |
| `n` | integer | CR 接口 | 请求参数 | 可选 | 输出张数 1–6，默认 1。 |
| `negative_prompt` | string | CR 接口 | 请求参数 | 可选 | 不希望出现的内容；省略表示不设置。 |
| `output_format` | string | CR 接口 | 请求参数 | 可选 | 仅 png；省略也返回 PNG。 |
| `quality` | string | CR 接口 | 请求参数 | 可选 | CR 分辨率档位：1K 或 2K；省略不指定档位。与 size 同时设置时必须匹配像素面积。 |
| `response_format` | string | CR 接口 | 请求参数 | 可选 | 仅 url；省略也返回图片 URL。 |
| `seed` | integer | CR 接口 | 请求参数 | 可选 | 0–2147483647；省略随机选择，固定种子不保证完全相同的结果。 |
| `size` | string | CR 接口 | 请求参数 | 可选 | auto 或宽x高，例如 1024x1024；面积 262144–4194304 像素，宽高比 1:8–8:1。省略时模型自动选择。与 aspect\_ratio 不同时设置。 |
| `callback_url` | string | CR 接口 | 请求参数 | 可选 | 调用方自己的 HTTPS 终态通知地址；省略时通过任务查询获取结果。 |
| `provider_options` | object | CR 接口 | 请求参数 | 可选 | 本模型的可选设置；仅填写本表列出的子字段。省略表示不附加设置。不要重复填写顶层统一参数。 |
| `provider_options.prompt_extend` | boolean | 模型原厂 | 模型选项 | 可选 | 自动优化提示词，默认 true。 |
| `provider_options.prompt_extend_mode` | string | 模型原厂 | 模型选项 | 可选 | direct 或 agent，默认 direct。agent 仅适用于文生图。 |
| `provider_options.enable_thinking` | boolean | 模型原厂 | 模型选项 | 可选 | 默认 true；仅 prompt\_extend=true 时生效。 |
| `provider_options.watermark` | boolean | 模型原厂 | 模型选项 | 可选 | 是否添加水印，默认 false。 |

<a id="operation-2-parameters"></a>

### 编辑图片

| 字段 | 类型 | 字段来源 | 参数类别 | 必填 | 取值、默认值与限制 |
| --- | --- | --- | --- | --- | --- |
| `model` | string | CR 接口 | 请求参数 | 必填 | 使用本页示例中的精确模型 ID。 |
| `prompt` | string | CR 接口 | 请求参数 | 必填 | 生成或编辑描述。 |
| `image` | string \| string\[\] | CR 接口 | 请求参数 | 必填 | 提供时使用 1–3 张参考图片的 HTTPS URL 或 data URL；顺序对应提示词中的图片编号。不支持蒙版。 |
| `aspect_ratio` | string | CR 接口 | 请求参数 | 可选 | 1:1、16:9、9:16、4:3、3:4、3:2、2:3、21:9、9:21。配合 quality 选择尺寸；省略不指定比例。 |
| `n` | integer | CR 接口 | 请求参数 | 可选 | 输出张数 1–6，默认 1。 |
| `negative_prompt` | string | CR 接口 | 请求参数 | 可选 | 不希望出现的内容；省略表示不设置。 |
| `output_format` | string | CR 接口 | 请求参数 | 可选 | 仅 png；省略也返回 PNG。 |
| `quality` | string | CR 接口 | 请求参数 | 可选 | CR 分辨率档位：1K 或 2K；省略不指定档位。与 size 同时设置时必须匹配像素面积。 |
| `response_format` | string | CR 接口 | 请求参数 | 可选 | 仅 url；省略也返回图片 URL。 |
| `seed` | integer | CR 接口 | 请求参数 | 可选 | 0–2147483647；省略随机选择，固定种子不保证完全相同的结果。 |
| `size` | string | CR 接口 | 请求参数 | 可选 | auto 或宽x高，例如 1024x1024；面积 262144–4194304 像素，宽高比 1:8–8:1。省略时模型自动选择。与 aspect\_ratio 不同时设置。 |
| `callback_url` | string | CR 接口 | 请求参数 | 可选 | 调用方自己的 HTTPS 终态通知地址；省略时通过任务查询获取结果。 |
| `provider_options` | object | CR 接口 | 请求参数 | 可选 | 本模型的可选设置；仅填写本表列出的子字段。省略表示不附加设置。不要重复填写顶层统一参数。 |
| `provider_options.prompt_extend` | boolean | 模型原厂 | 模型选项 | 可选 | 自动优化提示词，默认 true。 |
| `provider_options.prompt_extend_mode` | string | 模型原厂 | 模型选项 | 可选 | 仅 direct，默认 direct。 |
| `provider_options.enable_thinking` | boolean | 模型原厂 | 模型选项 | 可选 | 默认 true；仅 prompt\_extend=true 时生效。 |
| `provider_options.watermark` | boolean | 模型原厂 | 模型选项 | 可选 | 是否添加水印，默认 false。 |

<a id="callbacks"></a>

## 接收完成通知

需要通知时，在提交请求顶层加入 `callback_url`，值为你自己提供的 HTTPS 接收地址。它必须能接收 POST、全部 DNS 地址均为公网地址，且不依赖跳转；不得使用 localhost、内网地址或 CR API 地址。URL 的 UTF-8 长度最多 2048 字节，不能包含 userinfo 或 fragment。不要把该字段放入 provider\_options。

CR 发送 `completed` 或 `failed` 终态，正文与该任务的终态 GET 响应一致，不增加事件外层。使用正文 `id` 去重：先保存结果，再返回任意 `2xx`。处理时间较长时，先持久化或入队，再异步处理。可以使用 URL query 中由你生成的随机 token 校验通知；不要在公开日志中记录完整回调地址。

单次通知最多等待 10 秒。非 `2xx`、连接异常或超时会重试，首次失败后最多再试 3 次，分别等待 1、2、4 秒；`3xx` 不会自动跳转。重复通知使用同一正文，不重新生成。通知失败不改变任务状态；仍可使用原任务 ID 查询结果。

<a id="errors"></a>

## 常见错误与恢复

请求被拒绝时，读取响应中的 `error.type`、`error.code` 和 `error.message`，同时保存 `x-cr-request-id` 以便排查。错误对象说明原因，不是生成结果。不要依赖错误文案的固定措辞。

| 错误 | 恢复方式 |
| --- | --- |
| `400` | 核对必填字段、JSON 类型、参数组合和素材限制；修正后再发送。 |
| `401` / `403` | 检查完整 API Key 是否有效，以及该 Key 是否有权调用本模型。 |
| `402` | 查看调用明细与可用额度，处理余额或额度限制后再调用。 |
| `429` | 降低频率或并发；有 Retry-After 时遵循该等待时间。 |
| `5xx` / timeout | 暂时异常或连接超时不证明操作未被受理。先保存请求 ID，按是否已有任务 ID 和幂等标识决定恢复方式。 |
| `404 task_not_found` | 检查是否使用提交响应的 id 和同一把 API Key。 |
| `410 task_expired` | 结果正文已过期；使用此前保存的结果，不通过重试查询恢复正文。 |
| `429 task_wait_capacity_exceeded` | 等待连接过多，改用普通 GET 查询原任务并设置查询间隔。 |

<a id="billing"></a>

## 用量与费用核对

保留模型调用响应头中的 `x-cr-usage-id`，其值就是查询本次账单的 `usage_id`。`x-cr-request-id` 标识一次 HTTP 请求尝试，包括任务查询和幂等重试，不能代替用量 ID 查询账单。Python 示例输出这两个响应头；cURL 示例将它们保存到 `response-headers.txt`。

通过 `GET https://creative-reasoning.com/api/v1/management/usage/{usage_id}` 查询单条账单，批量查询使用 `POST https://creative-reasoning.com/api/v1/management/usage/batch`。其中 `{usage_id}` 必须替换为响应头取得的值。管理请求需要具有 `usage:read` 权限且覆盖该用量所属团队的 Management Token，模型 API Key 不能用于此操作。可在 CR 控制台取得获授权的 Management Token；没有该权限时，请由团队管理员核对调用明细。

费用以最终账单为准，金额单位为 Credits（ℂ）。响应中的 `usage` 是用量信息，不应直接当作扣费金额。新账单可能短暂返回 `404`；`billing_status: pending` 表示仍在结算，金额为空不表示免费。`billing_status: final` 时以 `credits.after_discount` 核对实际费用；账单完成不等于模型生成成功。

