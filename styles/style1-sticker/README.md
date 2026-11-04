# 风格1：小红书贴纸字

**状态：已定稿（v2）** · 配置文件：[`style.json`](style.json)

白 / 黑 / 柠檬黄 + 一个强调色的扁平电商封面，超粗黑体“贴纸字”标题。**画风固定**；颜色、标题位置与字号、产品位置/大小/角度、卖点排布与字号、装饰**随机组合**，每张图版式不同。

## 请求参数

| 参数 | 值 |
|---|---|
| model | `qwen-image-3.0-pro` |
| 接口 | 生成图片 `/unified/v1/images/tasks`；带产品参考图时用编辑图片 `/unified/v1/images/edit-tasks` |
| aspect_ratio / quality | `3:4` / `2K` |
| provider_options.prompt_extend | `false`（开启会改写 prompt，效果不可控） |
| seed | 每张随机并记录，便于复现 |
| negative_prompt | 见 ⑤ |

## Prompt 结构

拼接顺序（每段一行）：① 风格 → ③ 背景 → 标题（② 内容 + 位置、大小、字效）→ 产品（内容 + 角度、位置、大小）→ 卖点（内容 + 排布、字号）→ 强调色、装饰 → ④ 文字约束。⑤ 单独放 `negative_prompt`。

### ① 固定风格（每张都一样）

```
小红书竖版家电种草封面海报，3:4。视觉风格：扁平电商排版；主标题使用超粗黑体，白色粗描边加黑色硬投影的"贴纸字"效果；配色只用白、黑、柠檬黄，加一个强调色；辅助文字为黑色粗体白描边；产品为高清抠图，棚拍质感，边缘干净；整体对比强烈、排版饱满、信息层级清晰，文字清晰准确无错字，高清。
```

### ② 内容（每次替换）

| 字段 | 说明 | 示例 |
|---|---|---|
| 主标题 | 建议 ≤8 字 | 博世新品冰箱 |
| 副标题 | 建议 ≤6 字 | 上海首发 |
| 产品 | 产品外观描述，**不写英文和型号** | 一台博世 slot in 全嵌入式冰箱，十字对开门，白色玻璃门板，简约无把手设计 |
| 卖点 | **3 个**，短卖点 2–4 字 | 全嵌 / 隐嵌 / 零缝嵌入 |
| 产品名（可选） | 有产品参考图时填。产品描述自动换成：`参考图中的{产品名}，保持外观、颜色、门体结构和细节完全不变`，产品角度固定为：`保持参考图中的产品角度` | 冰箱 |

文字共 5 段（主标题 + 副标题 + 3 个卖点），**不要再加**，文字越多越容易出乱码。

可选词：[冰箱关键词库](../../examples/keywords/冰箱.json)；三档内容示例：[`examples/content/`](../../examples/content/)。下方 v1、v2 样图使用的卖点是“全嵌 / 隐嵌 / 高品质”（调整词库前的版本）。

### ③ 随机项（每类抽一项；序号即 `--pick` 用的数字，按下列类别顺序）

#### 颜色

**背景**（第 1 位）

1. 纯白背景
2. 米白背景，带极淡的点阵纹理
3. 纯白内容区，外圈淡薰衣草紫粗圆角边框
4. 纯白内容区，外圈天蓝色粗圆角边框
5. 米灰色网格纸背景，边缘点缀几片空白撕边纸片（纸片上无任何文字）

**强调色**（第 10 位）

1. 红色
2. 荧光绿
3. 橙色
4. 天蓝色

#### 标题：位置 / 字号 / 字效

**标题位置**（第 2 位）

1. 主标题和副标题在画面顶部居中，占画面上方约25%
2. 主标题在画面顶部左对齐，副标题在其右下方略倾斜
3. 主标题竖排在画面右侧，副标题在画面顶部左侧
4. 主标题在画面顶部，副标题做成倾斜的贴纸标签压在产品右上角
5. 主标题在画面顶部，副标题写在一个手绘白色对话气泡里，气泡尾巴指向产品

**标题大小**（第 3 位）

1. 主标题字号很大，横向约占画面宽度85%
2. 主标题字号大，横向约占画面宽度70%，四周留白更多
3. 主标题字号中等，横向约占画面宽度60%，副标题明显小一号

**标题字效**（第 4 位）

1. 主标题柠檬黄填充带细斜线纹理，黑色粗描边和硬投影
2. 主标题黑字，压在一条柠檬黄高亮笔刷底上
3. 主标题黑字白色粗描边加黑色硬投影，重点字用强调色

#### 产品：位置 / 大小 / 角度

**产品位置**（第 5 位）

1. 产品居中
2. 产品偏左
3. 产品偏右
4. 产品居中偏下，底部略微出画

**产品大小**（第 6 位）

1. 产品约占画面高度50%
2. 产品约占画面高度60%
3. 产品约占画面高度70%

**产品角度**（第 7 位）

1. 正面平视
2. 正面略向左转约15度，能看到一点右侧面
3. 正面略向右转约15度，能看到一点左侧面
4. 正面略微俯视

#### 卖点：排布 / 字号

**卖点排布**（第 8 位）

1. 卖点标签散落在产品两侧，略微倾斜
2. 卖点竖排成清单，每行前面一个绿色✅图标，放在产品旁的空白处
3. 每个卖点放在一个圆形柠檬黄色块里，用手绘黑色箭头指向产品
4. 每个卖点写在一条半透明纸胶带上，斜贴在产品周围
5. 卖点做成底部一排横向标签，用竖线分隔

**卖点字号**（第 9 位）

1. 卖点字号统一，约为主标题的三分之一
2. 卖点字号略大，约为主标题的二分之一

#### 装饰

**装饰**（第 11 位）

1. 左上角几道手绘强调短线
2. 黄色小星星和手绘弧形箭头
3. 几个小圆点和波浪线
4. 无额外装饰，保持干净

`--pick` 的类别顺序：1.背景 → 2.标题位置 → 3.标题大小 → 4.标题字效 → 5.产品位置 → 6.产品大小 → 7.产品角度 → 8.卖点排布 → 9.卖点字号 → 10.强调色 → 11.装饰

**冲突规则**（同时命中即跳过，避免重叠或拥挤）：

- 标题位置3（主标题竖排在画面右侧，副标题在画面顶部左侧） + 产品位置3（产品偏右）
- 标题位置3（主标题竖排在画面右侧，副标题在画面顶部左侧） + 标题大小1（主标题字号很大，横向约占画面宽度85%）
- 卖点排布5（卖点做成底部一排横向标签，用竖线分隔） + 产品位置4（产品居中偏下，底部略微出画）
- 标题位置1（主标题和副标题在画面顶部居中，占画面上方约25%） + 产品大小3（产品约占画面高度70%） + 标题大小1（主标题字号很大，横向约占画面宽度85%）

### ④ 文字约束（必加，放最后）

```
画面中只允许出现以下文字：主标题、副标题和卖点，每段文字只出现一次，字形清晰、完全准确，其中的英文、数字和型号按原样逐字写出。除这些指定文字外，不要出现任何其他文字、字母、数字、英文、型号、logo或符号文字。没有内容的区域保持留白，或只用纯图形装饰，不要任何填充文字或伪文字。
```

### ⑤ 反向提示词

```
乱码, 伪文字, 无意义文字, 多余文字, 重复文字, 英文小字, 报纸文字, 错别字, 模糊文字, 水印, logo, 产品变形, 透视歪斜, 卡通人物, 杂乱背景, 低分辨率
```

### 完整 prompt 示例（`--pick 1,2,3,3,1,1,3,1,2,2,1`）

```
小红书竖版家电种草封面海报，3:4。视觉风格：扁平电商排版；主标题使用超粗黑体，白色粗描边加黑色硬投影的"贴纸字"效果；配色只用白、黑、柠檬黄，加一个强调色；辅助文字为黑色粗体白描边；产品为高清抠图，棚拍质感，边缘干净；整体对比强烈、排版饱满、信息层级清晰，文字清晰准确无错字，高清。
背景：纯白背景。
标题：主标题"博世新品冰箱"，副标题"上海首发"；主标题在画面顶部左对齐，副标题在其右下方略倾斜；主标题字号中等，横向约占画面宽度60%，副标题明显小一号；主标题黑字白色粗描边加黑色硬投影，重点字用强调色。
产品：一台博世 slot in 全嵌入式冰箱，十字对开门，白色玻璃门板，简约无把手设计；正面略向右转约15度，能看到一点左侧面；产品居中，产品约占画面高度50%。
卖点："全嵌""隐嵌""高品质"；卖点标签散落在产品两侧，略微倾斜；卖点字号略大，约为主标题的二分之一，每个卖点只出现一次。
强调色：荧光绿。装饰：左上角几道手绘强调短线（纯图形，不含文字）。
画面中只允许出现以下文字：主标题、副标题和卖点，每段文字只出现一次，字形清晰、完全准确。除此之外不要出现任何其他文字、字母、数字、英文、型号、logo或符号文字。没有内容的区域保持留白，或只用纯图形装饰，不要任何填充文字或伪文字。
```

## 图片参考（v2，当前版本）

> ⚠️ 以下样图使用的是**测试文字**，品牌方最终内容确认后需重新出图替换。

> 链接是生成服务的临时地址，**可能过期**，满意的图请另存到团队素材库后替换这里的链接。完整 prompt 与 task_id 见 [`samples.json`](samples.json)。

| 编号 | 背景 · 强调色 | 标题 | 产品 | 卖点 | `--pick` | seed | 图 |
|---|---|---|---|---|---|---|---|
| v2-1 | 纯白背景 · 荧光绿 | 主标题在画面顶部左对齐 · 主标题字号中等 | 产品居中 · 占高50% · 正面略向右转约15度 | 卖点标签散落在产品两侧 | `1,2,3,3,1,1,3,1,2,2,1` | 1855407656 | [1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/fa/20261104/ed759433/b5338559-a4b2-48be-b35b-d9439b4573bb_qwen_image3_serving_output_0.png?Expires=1793879075&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=H4WLEHSN465zyoIjW344G44wxpA%3D) |
| v2-2 | 米灰色网格纸背景 · 红色 | 主标题在画面顶部 · 主标题字号大 | 产品居中偏下 · 占高50% · 正面略向左转约15度 | 卖点竖排成清单 | `5,5,2,1,4,1,2,2,1,1,3` | 866914210 | [1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/36/20261104/ed759433/8c1e4a28-f8e6-4205-8eeb-b8f3c0975241_qwen_image3_serving_output_0.png?Expires=1793879076&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=2to1rFmb8XgfdjwOI4kZCYmXxJQ%3D) |
| v2-3 | 纯白内容区 · 天蓝色 | 主标题在画面顶部 · 主标题字号大 | 产品偏左 · 占高70% · 正面略微俯视 | 卖点标签散落在产品两侧 | `4,4,2,1,2,3,4,1,2,4,4` | 1356692527 | [1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/58/20261104/ed759433/42ce6d9a-5f45-46fb-9e9a-ddf7851ed752_qwen_image3_serving_output_0.png?Expires=1793879076&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=i9E6c2gyC8HaLmf9%2BbCrJvG98Ac%3D) |
| v2-4 | 纯白内容区 · 荧光绿 | 主标题和副标题在画面顶部居中 · 主标题字号中等 | 产品偏左 · 占高60% · 正面略微俯视 | 每个卖点放在一个圆形柠檬黄色块里 | `4,1,3,1,2,2,4,3,1,2,3` | 298264976 | [1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/ec/20261104/ed759433/b0107d5e-e969-4bd6-9390-709a9a18d805_qwen_image3_serving_output_0.png?Expires=1793879101&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=f2pyOTDOiFsuUzbe44KsTdHa%2B%2F4%3D) |
| v2-5 | 米白背景 · 橙色 | 主标题在画面顶部左对齐 · 主标题字号中等 | 产品偏左 · 占高70% · 正面略向右转约15度 | 卖点标签散落在产品两侧 | `2,2,3,3,2,3,3,1,2,3,3` | 2124511382 | [1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/6a/20261104/ed759433/e40f0eab-ff5a-4936-8e50-018d13b2d1cb_qwen_image3_serving_output_0.png?Expires=1793879101&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=WA%2FGryf3Irkmmd%2BEGQzum6vYoOk%3D) |
| v2-6 | 纯白背景 · 红色 | 主标题和副标题在画面顶部居中 · 主标题字号大 | 产品偏左 · 占高50% · 正面略向右转约15度 | 卖点做成底部一排横向标签 | `1,1,2,3,2,1,3,5,1,1,2` | 1392101199 | [1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/cb/20261104/ed759433/7f2ee1c5-0ec7-4af9-bcbd-44b31b5b7264_qwen_image3_serving_output_0.png?Expires=1793879135&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=5%2Bxftfqkh3hQ1HmcAvQ3H54VKfM%3D) |

## 图片参考（v1，调整前版本）

v1 没有产品大小/角度、卖点字号等随机项，选项序号与 v2 不同，仅作画风参考。完整记录见 [`samples_v1.json`](samples_v1.json)。

- 第一种_全取第1项（seed 42）：[1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/06/20261104/ed759433/a4a9252d-35ea-43a5-913c-4edd53bad080_qwen_image3_serving_output_0.png?Expires=1793877376&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=AWy5rG7xeQp2jpoyuy0ZYEF7AWo%3D) [2](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/7f/20261104/ed759433/a4a9252d-35ea-43a5-913c-4edd53bad080_qwen_image3_serving_output_1.png?Expires=1793877376&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=g000rEy1STJ8l7CdU3DEcDw%2BS3w%3D) [3](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/d0/20261104/ed759433/a4a9252d-35ea-43a5-913c-4edd53bad080_qwen_image3_serving_output_2.png?Expires=1793877376&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=tNs4LKUCDKd6k1qao9CPNB21G84%3D) [4](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/ee/20261104/ed759433/a4a9252d-35ea-43a5-913c-4edd53bad080_qwen_image3_serving_output_3.png?Expires=1793877376&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=3lQiNtrYInNKHupuwmvHmYGx2aU%3D)
- 随机1（seed 1001）：[1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/15/20261104/ed759433/8bea5b77-9fbc-4a6c-94c7-f9eb65274d0b_qwen_image3_serving_output_0.png?Expires=1793877553&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=A58yS%2F9%2F3Tl7%2Fm0P6DaqaKEZmZw%3D)
- 随机2（seed 1002）：[1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/17/20261104/ed759433/295c1db5-70b8-4bb3-b45e-ab29afb1222f_qwen_image3_serving_output_0.png?Expires=1793877553&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=8MZjIvQzxMssmqjPuAvr6gwmdyo%3D)
- 随机3（seed 1003）：[1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/b9/20261104/ed759433/366d05e5-840d-431f-af3f-9c5e96aef4f6_qwen_image3_serving_output_0.png?Expires=1793877554&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=VLxVCoyYx81cmTVl8d1VC4ah5Y8%3D)
- 随机5（seed 1005）：[1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/4c/20261104/ed759433/6ed61c47-78b7-4eca-915d-a3eb1030a6ad_qwen_image3_serving_output_0.png?Expires=1793877553&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=jbmgxG0u9QoXnM4Pesaadf9qelg%3D)
- 随机6（seed 1006）：[1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/28/20261104/ed759433/a39714cb-8a43-49f0-958a-3ab8214c383e_qwen_image3_serving_output_0.png?Expires=1793877554&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=mFjf9S8KwYMJVc9xk8gfhqxeSKY%3D)
- 随机4（seed 1004）：[1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/39/20261104/ed759433/4cfb56cc-4b94-4032-9fc7-625720854226_qwen_image3_serving_output_0.png?Expires=1793877583&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=E5U%2FwECl0oQf9rmiXvnsW2bq4sk%3D)
