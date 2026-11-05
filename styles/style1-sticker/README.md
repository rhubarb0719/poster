# 风格1：小红书贴纸字

版本 v2 · 配置 [`style.json`](style.json) · 参数：3:4、2K、`prompt_extend=false`

拼接顺序见 `style.json` 的 `template`；② 内容（主标题、副标题、产品、卖点）按根目录 README「规则」填写。

## ① 固定风格

```
小红书竖版冰箱种草封面海报，3:4。视觉风格：扁平电商排版；主标题使用超粗黑体，白色粗描边加黑色硬投影的"贴纸字"效果；配色只用白、黑、柠檬黄，加一个强调色；辅助文字为黑色粗体白描边；产品为高清抠图，棚拍质感，边缘干净；整体对比强烈、排版饱满、信息层级清晰，文字清晰准确无错字，高清。
```

## ③ 随机项（每类抽一项）

| 类别 | 选项 |
|---|---|
| 背景 | 1. 纯白背景<br>2. 米白背景，带极淡的点阵纹理<br>3. 纯白内容区，外圈淡薰衣草紫粗圆角边框<br>4. 纯白内容区，外圈天蓝色粗圆角边框<br>5. 米灰色网格纸背景，边缘点缀几片空白撕边纸片（纸片上无任何文字） |
| 标题位置 | 1. 主标题和副标题在画面顶部居中，占画面上方约25%<br>2. 主标题在画面顶部左对齐，副标题在其右下方略倾斜<br>3. 主标题竖排在画面右侧，副标题在画面顶部左侧<br>4. 主标题在画面顶部，副标题做成倾斜的贴纸标签压在产品右上角<br>5. 主标题在画面顶部，副标题写在一个手绘白色对话气泡里，气泡尾巴指向产品 |
| 标题大小 | 1. 主标题字号很大，横向约占画面宽度85%<br>2. 主标题字号大，横向约占画面宽度70%，四周留白更多<br>3. 主标题字号中等，横向约占画面宽度60%，副标题明显小一号 |
| 标题字效 | 1. 主标题柠檬黄填充带细斜线纹理，黑色粗描边和硬投影<br>2. 主标题黑字，压在一条柠檬黄高亮笔刷底上<br>3. 主标题黑字白色粗描边加黑色硬投影，重点字用强调色 |
| 产品位置 | 1. 产品居中<br>2. 产品偏左<br>3. 产品偏右<br>4. 产品居中偏下，底部略微出画 |
| 产品大小 | 1. 产品约占画面高度55%<br>2. 产品约占画面高度65%<br>3. 产品约占画面高度75% |
| 产品角度 | 1. 正面平视<br>2. 正面略向左转约15度，能看到一点右侧面<br>3. 正面略向右转约15度，能看到一点左侧面<br>4. 正面略微俯视 |
| 卖点排布 | 1. 卖点标签散落在产品两侧，略微倾斜<br>2. 卖点竖排成清单，每行前面一个绿色✅图标，放在产品旁的空白处<br>3. 每个卖点放在一个圆形柠檬黄色块里，用手绘黑色箭头指向产品<br>4. 每个卖点写在一条半透明纸胶带上，斜贴在产品周围<br>5. 卖点做成底部一排横向标签，用竖线分隔 |
| 卖点字号 | 1. 卖点字号统一，约为主标题的三分之一<br>2. 卖点字号略大，约为主标题的二分之一 |
| 强调色 | 1. 红色<br>2. 荧光绿<br>3. 橙色<br>4. 天蓝色 |
| 装饰 | 1. 左上角几道手绘强调短线<br>2. 黄色小星星和手绘弧形箭头<br>3. 几个小圆点和波浪线<br>4. 无额外装饰，保持干净 |

冲突（不同时出现）：标题位置3 + 产品位置3；标题位置3 + 标题大小1；卖点排布5 + 产品位置4；标题位置1 + 产品大小3 + 标题大小1

## ④ 文字约束

```
画面中只允许出现以下文字：主标题、副标题和卖点，每段文字只出现一次，字形清晰、完全准确，其中的英文、数字和型号按原样逐字写出。不要把卖点拆开、拼接或重新组合成新的文字。除这些指定文字外，不要出现任何其他文字、字母、数字、英文、型号、logo或符号文字。没有内容的区域保持留白，或只用纯图形装饰，不要任何填充文字或伪文字。
```

## ⑤ 反向提示词

```
乱码, 伪文字, 无意义文字, 多余文字, 重复文字, 英文小字, 报纸文字, 错别字, 模糊文字, 水印, logo, 产品变形, 透视歪斜, 卡通人物, 杂乱背景, 低分辨率
```

## 样图

测试文字，链接可能过期；完整 prompt 和 seed 见 [`samples.json`](samples.json)。更多对比见 [tests/difficulty](../../tests/difficulty/README.md)。

[v2-1](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/fa/20261104/ed759433/b5338559-a4b2-48be-b35b-d9439b4573bb_qwen_image3_serving_output_0.png?Expires=1793879075&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=H4WLEHSN465zyoIjW344G44wxpA%3D) · [v2-2](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/36/20261104/ed759433/8c1e4a28-f8e6-4205-8eeb-b8f3c0975241_qwen_image3_serving_output_0.png?Expires=1793879076&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=2to1rFmb8XgfdjwOI4kZCYmXxJQ%3D) · [v2-3](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/58/20261104/ed759433/42ce6d9a-5f45-46fb-9e9a-ddf7851ed752_qwen_image3_serving_output_0.png?Expires=1793879076&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=i9E6c2gyC8HaLmf9%2BbCrJvG98Ac%3D) · [v2-4](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/ec/20261104/ed759433/b0107d5e-e969-4bd6-9390-709a9a18d805_qwen_image3_serving_output_0.png?Expires=1793879101&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=f2pyOTDOiFsuUzbe44KsTdHa%2B%2F4%3D) · [v2-5](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/6a/20261104/ed759433/e40f0eab-ff5a-4936-8e50-018d13b2d1cb_qwen_image3_serving_output_0.png?Expires=1793879101&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=WA%2FGryf3Irkmmd%2BEGQzum6vYoOk%3D) · [v2-6](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/cb/20261104/ed759433/7f2ee1c5-0ec7-4af9-bcbd-44b31b5b7264_qwen_image3_serving_output_0.png?Expires=1793879135&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=5%2Bxftfqkh3hQ1HmcAvQ3H54VKfM%3D)
