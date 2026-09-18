# GRAPHIA · bench V (CHORA workspace)

**Why this bench exists:** Exp10 found that concepts live in the **write direction** of ΔW —
domain LoRA adapters are near-orthogonal writers (five domains, |ΔWov|max = 0.129; three seeds)
on shared reads, and a data-mixture adapter interpolates rather than composing.
The composable law `W = W₀ + Σ pᵢΔWᵢ` therefore needs a gate, not distinguishable outputs —
shown by the learned gate (0.90 / 0.800) beating the lexical router (0.80 / 0.607).

**Holds:** the Exp10 note (six-section Qwen framework, gt tables, confession included),
the short paper (`paper/exp10-paper.pdf`, tectonic-typeset), and the Exp11 horizontal-matrix
rows as they land (P0 @ 1.5B already green).

**Site:** Quarto 1.9.38 (MEF's loom), rendered by CI, served at
https://math4mad.github.io/GRAPHIA/ — light theme on warm paper (#faf8f2), great_tables
matching `math4mad.github.io/Middle-Eigen-function`.

**Bytes discipline:** every number cites `(path, sha256)` into chora `artifacts/results/exp10|11/`;
this bench shares inputs, never histories.
