# 风格3：双产品对比图

版本 v1（调试中）· 配置 [`style.json`](style.json) · 参数：3:4、2K、`prompt_extend=false`

内容格式与风格1、2不同，见 [`examples/content/对比.json`](../../examples/content/对比.json)：`主标题`（≤6 字）、`副标题`（≤4 字）、`产品1`、`产品2`（只写外观）、`场景`（可选，仅布局 1 用）。用产品实拍图时加 `"参考图": true`，并按 左、右 顺序传 2 张图（`--image 图1 图2`）。

## 固定风格

```
小红书家电种草封面，双产品对比图风格，竖版3:4构图。排版简洁、对称平衡、留白充足，画面只分三个区域：顶部标题区、中部双产品区、底部细色带；配色以黑、白、柠檬黄为主，红色只用于副标题和对比符号；摄影级写实产品搭配扁平贴纸元素，高清。
```

拼接顺序见 `style.json` 的 `template`：风格 → 背景 → 标题 → 产品 → 徽章 → 底部色带 → 文字约束。

## 随机项（每类抽一项）

| 类别 | 选项 |
|---|---|
| 背景 | 1. 浅暖灰色纯色背景<br>2. 纯白背景<br>3. 米白色背景，带极淡的纸张纹理 |
| 布局 | 1. 两款产品各放在一张等宽的浅色圆角卡片里，两张卡片左右并排，中间留一条白色细缝，卡片内背景为{场景}<br>2. 两款产品为纯白底抠图左右并排，每款产品外加一圈手绘粗黑描边，两款产品正中间是一个红色粗体"VS"<br>3. 左右两列对比，每列外围一个手绘黑色细边框，框内背景留白 |
| 产品大小 | 1. 每款产品高度约占画面高度40%<br>2. 每款产品高度约占画面高度45%<br>3. 每款产品高度约占画面高度50% |
| 徽章样式 | 1. 黄色实心圆形，黑色粗体数字，细黑描边，贴纸感<br>2. 黑色圆角方块，白色粗体数字，带轻微纸张投影<br>3. 红色实心圆形，白色粗体数字，外圈白色描边<br>4. 柠檬黄五瓣花朵形，中心白色圆，黑色粗体数字<br>5. 橙色圆形，外围一圈放射状小短线，白色粗体数字 |

布局 2 抽中时，文字约束自动加上“VS”。

## 文字约束

```
画面中只允许出现以下文字：主标题"{主标题}"、副标题"{副标题}"、徽章数字"1"和"2"{额外文字}，每段文字只出现一次，字体粗大清晰、笔画完整，中文为简体。除这些指定文字外，不要出现任何其他文字、字母、数字、型号、logo、水印、气泡文字或标签；没有内容的区域保持留白。
```

## 反向提示词

```
乱码, 错别字, 多余文字, 小字, 英文小字, 手写字, 型号, 产品铭牌文字, 控制面板文字, 显示屏数字, 价格, 水印, logo, 对话气泡, 漫画气泡, 多余的空白标签, 产品变形, 两款产品大小不一, 产品重叠, 画面拥挤, 低分辨率
```

## 样图

测试文字，链接可能过期；完整 prompt 和 seed 见 [`samples.json`](samples.json)。

| 编号 | 背景 | 布局 | 产品大小 | 徽章 | 图 |
|---|---|---|---|---|---|
| s3-1 | 浅暖灰色纯色背景 | 两款产品各放在一张等宽的浅色圆角卡片里 | 40% | 黄色实心圆形 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/30/20261105/ed759433/f148aa4e-d5b0-4fa0-9f2f-7cffdb4755a9_qwen_image3_serving_output_0.png?Expires=1793933384&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=4dnlqrGe7x10CAG1r40L6VWOOgg%3D) |
| s3-2 | 米白色背景 | 两款产品各放在一张等宽的浅色圆角卡片里 | 45% | 黄色实心圆形 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/c2/20261105/ed759433/91e7e4a8-34f8-4650-bbbc-ccaceab74ded_qwen_image3_serving_output_0.png?Expires=1793933409&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=hqdPWJ5xgtlEBAXJ0Zombt1hplo%3D) |
| s3-3 | 纯白背景 | 左右两列对比 | 45% | 黑色圆角方块 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/e9/20261105/ed759433/3f7f3915-7627-4ca4-9ec9-1a2fc8295721_qwen_image3_serving_output_0.png?Expires=1793933409&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=kGA4TSsUgmgAlQ2RMnHVI4Z7AQM%3D) |
| s3-4 | 浅暖灰色纯色背景 | 左右两列对比 | 50% | 柠檬黄五瓣花朵形 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/6e/20261105/ed759433/8ee17cc4-5159-49ce-8840-0cdb61a36145_qwen_image3_serving_output_0.png?Expires=1793933409&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=kLiFTKAZ%2Fexde7lpkSkQWjq5bVU%3D) |
| s3-5 | 米白色背景 | 两款产品为纯白底抠图左右并排 | 50% | 黑色圆角方块 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/3e/20261105/ed759433/15f5f769-b384-4283-8d20-146b9a8b2565_qwen_image3_serving_output_0.png?Expires=1793933435&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=ShyPWZuotCGsppt2pVUoCXo7weA%3D) |
| s3-6 | 纯白背景 | 两款产品为纯白底抠图左右并排 | 40% | 黄色实心圆形 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/c7/20261105/ed759433/93b083db-8239-4b8e-a354-8368c796bd5d_qwen_image3_serving_output_0.png?Expires=1793933434&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=zTlN5xlVb3dG%2BtQu7clC%2BWU79sA%3D) |
