# 风格索引

每种风格一个文件夹，结构相同：

| 文件 | 给谁看 | 内容 |
|---|---|---|
| `README.md` | 所有人 | prompt 全文（①风格 ②内容 ③随机项 ④文字约束 ⑤反向提示词）、请求参数、图片参考 |
| `style.json` | 程序 | 与 README 内容一致的机器可读配置 |
| `samples.json` | 排查用 | 每张样图的完整 prompt、seed、task_id、链接 |

| 风格 | 文件夹 | 状态 |
|---|---|---|
| 风格1：小红书贴纸字 | [style1-sticker](style1-sticker/README.md) | 已定稿 |
| 风格2：杂志手账拼贴 | [style2-collage](style2-collage/README.md) | 调试中 |
| 风格3 | [style3](style3/README.md) | 待定 |

新增风格：复制 [`_template/`](_template/) 并按 [开发对接说明 §5](../docs/开发对接说明.md#5-新增或修改风格) 修改。
