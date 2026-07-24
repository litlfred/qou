---
# qou-jbd5
title: 'Brick 4: Part A uniform Tauberian convergence (1-q)logPhi_n(x;q) -> Li2(x) via hasSum_pow_div_log'
status: in-progress
type: task
priority: normal
created_at: 2026-07-18T14:57:00Z
updated_at: 2026-07-18T19:52:32Z
---

## 2026-07-24 reconciliation (main is +1077 commits since this bean was opened)

The **algebraic** half of Part A is fully landed sorry-free on `main`; the **one
load-bearing open item is the DCT/Tauberian exchange itself.**

LANDED sorry-free (main):
- `partialProduct_log_eq` / `_tsum` / `_mseries` — log Φ_n → the closed
  `m`-series (`DilogarithmArchimedeanLimit.lean`).
- `DilogPartARiemannSum.lean`: `log_partialProduct_eq_neg_sum` (Brick 1),
  `riemann_sum_form` (Brick 2) — identifies `(1−q)·Σ` as the left-endpoint
  Riemann sum of `−log(1−xu)/u`.
- Dilog algebra complete: `LiTwo_one`, `LiTwo_neg_one`, `LiTwo_duplication`,
  `LiTwo_half`, `LiTwo_eq_integral`, the reflection `LiTwo_reflection'`, the
  derivative `hasDerivAt_LiTwo` (`DilogReflection.lean`), and `Knot/Clausen.lean`.

STILL OPEN — the actual convergence:
- `ArchimedeanLimit` typeclass (`DilogarithmArchimedeanLimit.lean:108`) is
  inhabited ONLY at `x=0` (`archimedeanLimit_zero`). The uniform / dominated-
  convergence exchange that turns the Riemann-sum form into `→ Li₂(x)` for
  `x∈(0,1)` is **not proved**. No `sorry` carries it — the openness is the class
  being uninhabited off `x=0`.
- The DCT step is **in-flight (not landed)** on sibling branch
  `claude/dilog-litwo-neg-one-2026-07-18` ("interchange+geom landed; DCT open").
  COORDINATE before attacking — do not duplicate the mechanical interchange;
  an independent DCT derivation is permitted (open-outcome research) but state
  the distinct angle on that branch's PR first.
- Downstream consumer: `claude/alpha-em-zeta-anomaly-b1-2026-07-17` reduces the
  1/π per-mode-weight question to this same open dilog convergence.

Next concrete step: prove `HasSum`/`Tendsto` domination for
`(1−q)·Σ_{m} x^{m+1}/(m+1)·(q^{(m+1)n}−1)/(q^{m+1}−1) → Σ x^{m+1}/(m+1)²`
(each factor `→ 1/(m+1)`, dominated by `|x|^{m+1}/(m+1)` — summable), i.e. a
`tendsto_tsum_of_dominated_convergence` application, then inhabit
`ArchimedeanLimit x` for `x∈(0,1)`.
