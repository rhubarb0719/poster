"""按风格配置（styles/<id>/style.json）拼接 prompt。

拼接逻辑全部由 style.json 的 template 决定，代码不含任何风格内容；
新增风格只需新建 styles/<id>/style.json。
"""
import json
import random
from pathlib import Path

STYLES_DIR = Path(__file__).resolve().parents[2] / "styles"


def list_styles():
    return sorted(p.parent.name for p in STYLES_DIR.glob("*/style.json") if not p.parent.name.startswith("_"))


def load_style(style_id):
    path = STYLES_DIR / style_id / "style.json"
    if not path.exists():
        raise FileNotFoundError(f"没有风格 {style_id}，可选：{list_styles()}")
    return json.loads(path.read_text(encoding="utf-8"))


def _conflicts(style, idx):
    """idx: 类别 → 选项序号（1 起）。命中任一冲突规则返回 True。"""
    return any(all(idx.get(k) == v for k, v in rule.items()) for rule in style.get("conflicts", []))


def pick(style, mode="first", seed=None, indices=None):
    """选随机项。mode: first（每类第 1 项）/ random（按 seed 随机，自动跳过冲突组合）/ index（indices 手动指定，1 起）。
    返回 {类别: 选项序号}。"""
    cats = list(style["options"])
    if mode == "first":
        return {c: 1 for c in cats}
    if mode == "index":
        return dict(zip(cats, indices))
    rng = random.Random(seed)
    while True:
        idx = {c: rng.randint(1, len(style["options"][c])) for c in cats}
        if not _conflicts(style, idx):
            return idx


def build(style, content, idx):
    """content: {"主标题", "副标题", "产品", "卖点": [..]}，可选 "产品名"（有参考图时用）。
    返回 (prompt, negative_prompt)。"""
    product = content["产品"]
    if content.get("产品名"):  # 有产品参考图：产品描述改为“保持参考图不变”
        product = style["产品来自参考图"].format(产品名=content["产品名"])
    values = {
        "风格": style["风格"],
        "文字约束": style["文字约束"],
        "主标题": content["主标题"],
        "副标题": content["副标题"],
        "产品": product,
        "卖点": "".join(f'"{p}"' for p in content["卖点"]),
        **{c: style["options"][c][i - 1] for c, i in idx.items()},
    }
    if content.get("产品名"):  # 有参考图时，部分类别（如产品角度）固定为跟随参考图
        values.update(style.get("参考图时固定", {}))
    return "".join(seg.format(**values) for seg in style["template"]), style["negative_prompt"]


def build_request(style, content, idx, n=1, seed=None, images=None):
    """拼出完整请求体。images 为参考图（HTTPS URL 或 data URL，1–3 张）。"""
    prompt, negative = build(style, content, idx)
    body = json.loads(json.dumps(style["params"]))
    body.update(prompt=prompt, negative_prompt=negative, n=n)
    if seed is not None:
        body["seed"] = seed
    if images:
        body["image"] = images if len(images) > 1 else images[0]
    return body
