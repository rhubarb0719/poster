# poster · 小红书冰箱种草封面

用 `qwen-image-3.0-pro` 生成 3:4 竖版封面：**风格固定，版式随机**（标题、产品、卖点的位置和样式每张不同）。

> ⚠️ 当前文字（`examples/`）和样图均为**测试内容**，品牌方最终文字和产品图确认后替换。

## 目录

```
docs/开发对接说明.md      开发先读：流程、参数、注意事项
docs/qwen-image-3.0-pro接入文档.md   接口官方文档
styles/style1-sticker/   风格1：小红书贴纸字（prompt + 样图）
styles/style2-collage/   风格2：杂志手账拼贴（prompt + 样图）
styles/style3/           风格3（待定）
styles/_template/        新建风格时复制
src/poster/              代码（仅 Python 标准库）
examples/content/中等.json   内容示例（标准格式）
examples/keywords/冰箱.json  关键词库（待品牌方确认后修改）
assets/products/         品牌产品图（默认不入库）
tests/difficulty/        难度分档测试记录（gallery.html 一页看全部）
```

## 用法

```bash
export CR_API_KEY=你的完整密钥 PYTHONPATH=src
```

```bash
python3 -m poster check examples/content/中等.json
```

```bash
python3 -m poster prompt --style style1-sticker --content examples/content/中等.json --random 1
```

```bash
python3 -m poster generate --style style1-sticker --content examples/content/中等.json --count 6
```

`check` 检查内容，`prompt` 只看拼好的 prompt（都不扣费）；`generate` 出图，结果在 `output/<时间>/result.json`。

## 规则

| 项 | 规则 |
|---|---|
| 文字 | 统一用**中等难度**：主标题约 7–12 字，副标题 ≤10 字，**3 个卖点**（最多 1 个超过 8 字），共 5 段。依据：中等档乱码 1/12 |
| 产品大小 | 占画面高度 **55%–75%**，每张随机 |
| 产品描述 | 只写中文外观，不写英文、型号（会被印到产品上）；型号要展示就放进卖点 |
| 引号 | 文字里用中文引号“”，不用英文 `"` |
| 并发 | ≤3，遇到 `upstream_rate_limited` 等待后重新提交（代码已处理） |
| 图片链接 | 会过期，出图后立即转存 |
