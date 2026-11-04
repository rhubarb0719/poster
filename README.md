# poster · 小红书家电种草封面生成

用 `qwen-image-3.0-pro`（CR 统一接口）按「固定风格 + 每次替换的内容 + 随机版式」生成竖版 3:4 家电封面海报。
同一风格下画风一致，标题、产品、卖点的位置和样式每张不同。

## 目录

```
poster/
├── README.md                    ← 你在这里：总览
├── docs/
│   ├── 开发对接说明.md           ← 开发先读：调用流程、参数、注意事项
│   ├── 替换最终内容清单.md       ← 换成品牌方最终文字和产品图的步骤
│   └── qwen-image-3.0-pro接入文档.md   ← CR 官方接入文档原文
├── styles/                      ← 每种风格一个文件夹（prompt + 图片参考）
│   ├── README.md                ← 风格索引
│   ├── style1-sticker/          ← 风格1：小红书贴纸字（已定稿）
│   │   ├── README.md            ← prompt 全文、随机项、样图
│   │   ├── style.json           ← 程序读取的风格配置
│   │   ├── samples.json         ← v2 样图的完整 prompt / seed / task_id
│   │   └── samples_v1.json      ← v1（调整前）样图记录
│   ├── style2-collage/          ← 风格2：杂志手账拼贴（调试中）
│   ├── style3/                  ← 风格3（待定）
│   └── _template/               ← 新建风格时复制这个
├── src/poster/                  ← 代码（仅 Python 3 标准库，无第三方依赖）
│   ├── prompt.py                ← 读取 style.json，拼 prompt / 请求体
│   ├── check.py                 ← 内容检查（字段、长度、段数、引号、产品图）
│   ├── client.py                ← CR 接口：提交、等待、下载
│   └── cli.py                   ← 命令行
├── assets/products/             ← 品牌方产品图（默认不入库）
├── examples/
│   ├── keywords/冰箱.json        ← 冰箱关键词库（产品 / 主标题 / 副标题 / 卖点，按长度分组）
│   └── content/                 ← 内容示例：简单.json / 中等.json / 压力.json
└── tests/
    └── text-stress/             ← 文字压力测试记录（inputs/ 为当时实际使用的内容）
```

> ⚠️ **当前文字和样图均为测试内容**，品牌方最终内容替换步骤见 [docs/替换最终内容清单.md](docs/替换最终内容清单.md)。

## 快速开始

```bash
export CR_API_KEY=你的完整密钥
export PYTHONPATH=src
```

```bash
python3 -m poster styles
```

只看拼出来的 prompt（不调用接口、不扣费）：

```bash
python3 -m poster prompt --style style1-sticker --content examples/content/简单.json --random 7
```

出图（随机 6 种版式，每种 1 张）：

```bash
python3 -m poster generate --style style1-sticker --content examples/content/简单.json --count 6
```

结果写在 `output/<时间>/`（已加入 .gitignore）：图片文件 + `result.json`（prompt、参数、task_id、图片链接）。

## 风格

| 风格 | 状态 | 说明 |
|---|---|---|
| [风格1：小红书贴纸字](styles/style1-sticker/README.md) | 已定稿（v2） | 白/黑/柠檬黄 + 强调色，超粗黑体贴纸字标题；颜色、标题位置与字号、产品位置/大小/角度、卖点排布与字号随机组合 |
| [风格2：杂志手账拼贴](styles/style2-collage/README.md) | 调试中 | 奶黄 + 米灰 + 黑的杂志手账拼贴（v2），网格纸、撕边纸、胶带、手绘箭头、圆形色块 |
| [风格3](styles/style3/README.md) | 待定 | — |
