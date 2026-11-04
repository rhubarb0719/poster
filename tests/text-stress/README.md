# 文字压力测试

测试模型在文字量大时的准确率，按难度分三档：

| 档位 | 规则 | 状态 |
|---|---|---|
| 简单 | 短标题 + 3 个短卖点 | 待测 |
| 中等 | 中等标题 + 中英混排 + 1 个长卖点 | 待测 |
| 压力 | 长标题 + 长副标题 + 5 个卖点 + 型号 KCG89AA21C | **已出图，待人工检查** |

## 压力档：测试内容

当时实际使用的内容在 [`inputs/`](inputs/)。这批测试早于冰箱关键词库，C 组是洗烘套装，后续测试请用 [`examples/content/压力.json`](../../examples/content/压力.json)。

| 组 | 主标题（字数） | 副标题 | 卖点 |
|---|---|---|---|
| A_冰箱讲解 | 博世slot in冰箱系列全讲解（16） | 什么区别？到底怎么选？ | 全嵌入设计，与橱柜齐平 / 新工艺，有陶瓷质感 / 抗指纹处理玻璃 / 0 缝隙 Slot-in / 润玉白 / KCG89AA21C |
| B_冰箱怎么选 | 一篇看懂博世冰箱怎么选（11） | 教你如何选择“梦中情机” | 全嵌 / 隐嵌 / 新工艺，有陶瓷质感 / 百搭，浅白，纯净，纯洁 / 全嵌入设计，与橱柜齐平 / KCG89AA21C |
| C_洗烘对比 | Bosch slot in VS 进口8系 到底差在哪（27） | 外观 | 程序 | 功能 对比 | Napoli 深层净洗 / Monza 蒸汽除皱 / 阳光烘/暖衣 / 开门方向可改 / 隐藏式连接 |

说明：
- A、B 组把型号 KCG89AA21C 作为第 6 个卖点放入（冰箱型号）。C 组是洗烘套装，型号不匹配，没有放。
- C 组原关键词 `Bosch slot in VS XXX 到底差在哪` 中的 XXX 替换为“进口8系”。
- B 组副标题中的引号用中文引号“”，避免和 prompt 的英文引号冲突。

## 压力档：结果（请人工填写检查结果）

> 链接可能过期，完整 prompt 见 [`results.json`](results.json)。

| 编号 | 风格 | 内容 | 图 | 文字全对？ | 乱码/错字 | 备注 |
|---|---|---|---|---|---|---|
| P1 | style1-sticker | A_冰箱讲解 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/29/20261104/ed759433/a7206619-7623-48fa-99de-18381602d98b_qwen_image3_serving_output_0.png?Expires=1793879966&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=KFpsenSb8sNYzewZzMIeWbLcbHo%3D) |  |  |  |
| P2 | style1-sticker | A_冰箱讲解 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/78/20261104/ed759433/541dc18c-4c39-4eae-a433-b0eac7128995_qwen_image3_serving_output_0.png?Expires=1793879961&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=ME%2BXjV7b8K6bzfxbovzQKs%2FpZ%2Bc%3D) |  |  |  |
| P3 | style2-collage | A_冰箱讲解 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/82/20261104/ed759433/8e79b71c-c9ae-4bc3-b44b-42b51beaad72_qwen_image3_serving_output_0.png?Expires=1793879995&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=c3A%2B4JNUIw7nU0%2BNVG2ZKSfK6dg%3D) |  |  |  |
| P4 | style1-sticker | B_冰箱怎么选 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/8c/20261104/ed759433/14ec4632-cae5-4d9f-9abe-7cbc78df382d_qwen_image3_serving_output_0.png?Expires=1793880028&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=GRCTOQAqJwg8aw3hBfCVkqsEGN0%3D) |  |  |  |
| P5 | style1-sticker | B_冰箱怎么选 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/d9/20261104/ed759433/2f13fb72-3d41-4cc6-83bb-41daf0b0881b_qwen_image3_serving_output_0.png?Expires=1793880028&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=Ot2%2FJcNH8hy8XjGwrJ5%2BKa7cZ1U%3D) |  |  |  |
| P6 | style2-collage | B_冰箱怎么选 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/d4/20261104/ed759433/636325fd-3616-44b2-a8c7-4643ee21b032_qwen_image3_serving_output_0.png?Expires=1793880060&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=pbEKu0%2B26TuHaqpjvcU6APiLWQw%3D) |  |  |  |
| P7 | style1-sticker | C_洗烘对比 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/dd/20261104/ed759433/19dba0d6-6602-44e9-b474-93b154fdf0fd_qwen_image3_serving_output_0.png?Expires=1793880084&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=LCJgmOulbj6lqCeHED%2F2u8lYGhM%3D) |  |  |  |
| P8 | style1-sticker | C_洗烘对比 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/43/20261104/ed759433/064a1fb6-3be1-4db8-9038-5fce5715a056_qwen_image3_serving_output_0.png?Expires=1793880084&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=5thyCgTR8otRp2dobMPApOAjS4M%3D) |  |  |  |
| P9 | style2-collage | C_洗烘对比 | [看图](https://dashscope-a717.oss-accelerate.aliyuncs.com/1d/a2/20261104/ed759433/aba58758-7e36-4082-a15d-9f2e57044938_qwen_image3_serving_output_0.png?Expires=1793880106&OSSAccessKeyId=LTAI5tPxpiCM2hjmWrFXrym1&Signature=vHxQUNEcjcsH6ET%2B7WPhO6GsBRc%3D) |  |  |  |
