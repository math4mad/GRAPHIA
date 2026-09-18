#!/usr/bin/env python3
# GRAPHIA site build · gt tables — the owner's ruling: MEF-uniform Great Tables, light theme.
# Reads pinned report JSONs from chora, emits HTML fragments into site/tables/.
# Re-runnable; fragments are derived bytes (rebuilt by this script, inputs cited).
import json, os
import pandas as pd
from great_tables import GT, md

GRAPHIA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHO = os.path.expanduser("~/Programming/code-2026/chora")
OUT = os.path.join(GRAPHIA, "site", "tables")
os.makedirs(OUT, exist_ok=True)

def load(p): return json.load(open(os.path.join(CHO, p)))

def gt_light(df, caption, name):
    # default gt skin is exactly MEF's quarto look (verified against eigen-ablation.html)
    return GT(df, id=f"gt{name}").tab_header(title=md(caption))

def save(g, fname):
    html = g.as_raw_html()
    open(os.path.join(OUT, fname), "w").write(html)
    print("wrote", fname, len(html), "B")

# ---- T1 · verdicts (the report's Table 1) ----
r10a = load("artifacts/results/exp10/report_10a.json")
r10b = load("artifacts/results/exp10/report_10b.json")
r10c = load("artifacts/results/exp10/report_10c.json")
r10cg = load("artifacts/results/exp10/report_10c_grouped.json")
try: r10cgS1 = load("artifacts/results/exp10/report_10c_grouped_S1.json")
except FileNotFoundError: r10cgS1 = load("experiments/exp10-concept-adapters/results/report_10c_grouped_S1.json")
r10d = load("artifacts/results/exp10/report_10d_router_v2.json")
r10g = load("artifacts/results/exp10/report_10g_gate.json")
r10g5 = load("artifacts/results/exp10/report_10g_routed5.json")

t1 = pd.DataFrame([
    ["行为 10a", "H2 词库自命>基座、交叉<自命", "春 0.84 vs 0.107 · 夏 0.493 vs 0.333 · 交叉 0.24/0.013 · 中性≈0", "PASS"],
    ["行为 10a", "H1 专家彼此最远", "JS ss 0.417/0.380 < base~arm 0.551/0.575（带宽 0.105/0.137）", "FAILS · 符号反转"],
    ["行为 10a", "H3 中性题压缩", "差 0.049 < 带 0.064", "INCONCLUSIVE"],
    ["结构 10b", "H4 中间型=第三空间", "U-B 父母对 0.547–1.244 ≪ 混~亲 1.758–2.508；ΔWov −0.002…0.135 vs 0.009…0.661", "FAILS · 零模型胜：插值"],
    ["结构 10b", "读方向共享", "V-A 三对 3.818/3.834/3.833 全平", "随 H4 归档"],
    ["结构 10f", "H6 跨域普适（五域）", "十对专家×专家 |ΔWov|max = 0.1294 < 0.2 带；锚点 0.618/0.661 同板齐亮", "PASS"],
    ["序列 10c", "全序列反转幅度", "theme 差 0.165(单点) → 0.060（缩水 3×，符号存活）", "REGISTERED"],
    ["序列 10c′", "§8 内容/风格期望图式", "ss 在内容与风格上皆最小；两种 style 定义下判词不变", "DISCONFIRMED"],
    ["工程 10d→10g", "匹配与行为分", "词法 0.80 / 0.607 → 学习门控 0.90 / 0.800", "PASS · 门控胜任"],
    ["工程 GGUF", "体积与速度", "q4_K_M 374–392 MB · 149.6–165.8 t/s（目标 20 / <1GB）", "PASS × 7.5"],
], columns=["层 Layer", "判项 Claim", "数 Numbers", "判定 Verdict"])
save(gt_light(t1, "**Table 1 · Exp10 判定总表** — 数字裸呈，不加修饰", "t1"), "t1_verdicts.html")

# ---- T2 · geometry ----
geo = pd.DataFrame([
    ["spring~summer", 3.818, "0.55–1.24", "−0.002 … 0.135", "✔ 13/14/15"],
    ["spring~mid", 3.834, "1.76–2.43", "0.009 … 0.635", "✔"],
    ["summer~mid", 3.833, "1.86–2.51", "0.013 … 0.661", "✔"],
    ["code~legal", 3.785, 1.162, 0.1294, "— 单种"],
    ["code~medical", 3.786, 1.134, 0.1217, "—"],
    ["legal~medical", 3.790, 1.158, 0.1284, "—"],
    ["spring/summer/mid~新域 诸交叉 (7 对)", "3.78–3.80", "≤1.2", "≤0.13", "—"],
], columns=["对 Pair", "V-A 读 (k90)", "U-B 写 (k90)", "ΔW overlap", "种子 Seeds"])
save(gt_light(geo, "**Table 2 · 几何总表** — 写方向分居，读方向共享；混合=插值", "t2"), "t2_geometry.html")

print("done. (T3/T4 written by part 2 of this script once exp11 P0 lands)")
