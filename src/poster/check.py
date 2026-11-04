"""内容检查：替换为品牌方最终内容后，出图前先跑一遍。

只检查格式和已知的乱码风险，不判断文案好坏。
ERROR 必须修改；WARN 可以出图，但乱码或排版风险更高。
"""
import re
from pathlib import Path

FIELDS = {"主标题", "副标题", "产品", "卖点", "产品名"}
LIMITS = {"主标题": 12, "副标题": 10, "卖点": 8}  # 超过即提示（不含空格）
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}


def _len(s):
    """中文按 1 字、英文和数字按半字计，不含空格。"""
    s = s.replace(" ", "")
    return sum(0.5 if ch.isascii() else 1 for ch in s)


def check_content(content, images=None):
    out = []
    err = lambda m: out.append(("ERROR", m))
    warn = lambda m: out.append(("WARN", m))

    for k in ("主标题", "副标题", "产品", "卖点"):
        if k not in content:
            err(f"缺少字段：{k}")
    for k in set(content) - FIELDS:
        warn(f"未知字段 {k}，不会进入 prompt")
    points = content.get("卖点", [])
    if not isinstance(points, list) or not all(isinstance(p, str) for p in points):
        err("卖点必须是文字列表，例如 [\"全嵌\", \"隐嵌\", \"零缝嵌入\"]")
        points = []

    texts = [("主标题", content.get("主标题", "")), ("副标题", content.get("副标题", ""))] + \
            [(f"卖点{i}", p) for i, p in enumerate(points, 1)]
    for name, t in texts:
        if not isinstance(t, str) or not t.strip():
            err(f"{name} 为空")
            continue
        if '"' in t:
            err(f"{name}「{t}」含英文双引号，会打乱 prompt；请改用中文引号“”")
        limit = LIMITS.get(re.sub(r"\d+$", "", name))
        if limit and _len(t) > limit:
            warn(f"{name}「{t}」约 {_len(t):g} 字，超过建议的 {limit} 字（英文按半字计），错字风险更高")
    seen = [t for _, t in texts]
    for t in {t for t in seen if seen.count(t) > 1}:
        warn(f"文字「{t}」重复出现")

    n = 2 + len(points)
    if n > 5:
        warn(f"图上文字共 {n} 段（主标题 + 副标题 + {len(points)} 个卖点），超过建议的 5 段，乱码风险高")
    if 0 < len(points) < 3:
        warn(f"卖点只有 {len(points)} 个，版式按 3 个设计，画面可能偏空")

    product = content.get("产品", "")
    risky = re.findall(r"\b[A-Za-z]*\d[A-Za-z0-9-]*\b|\bbosch\b", product, re.I)  # 型号、英文品牌名
    if risky and not content.get("产品名"):
        warn(f"产品描述含型号或英文品牌名 {risky}，模型可能把它画到图上；产品描述只写外观，型号请放进卖点")

    if content.get("产品名") and not images:
        warn("填写了产品名（参考图模式），但没有提供产品图，出图时请加 --image")
    for src in images or []:
        if src.startswith(("https://", "data:")):
            continue
        p = Path(src)
        if not p.exists():
            err(f"产品图不存在：{src}")
        elif p.suffix.lower() not in IMAGE_EXT:
            warn(f"产品图格式 {p.suffix} 未验证过，建议用 PNG / JPG")
    if images and len(images) > 3:
        err(f"产品图 {len(images)} 张，接口最多 3 张")
    return out
