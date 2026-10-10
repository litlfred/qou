---
# qou-4hq0
title: 'A1 (deep bet): exact/semi-exact evaluation of T3=Sum(f)^2 chi(3-cyc) via content-sum formulas'
status: completed
type: task
priority: normal
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-09-07T10:25:25Z
parent: qou-v8t7
---

A1 — exact T3 evaluation: ELIMINATED (route #12, 2026-07-25 agent). No closed form for T3=Σ(dim)²χ(σ₃) / cov=Σ(dim)³ω₃ (OEIS-absent, not P-recursive, no product/hypergeometric hit; no manifestly-negative form). PRECISE REASON = the dim²→dim³ threshold: Σ(dim)²·ω₃=0 EXACTLY (closed, Plancherel expectation of shifted-symmetric ω₃, IO Prop 5.1) but Σ(dim)³·ω₃=cov carries one extra dim (=χ(e), NOT shifted-symmetric) ⇒ non-holonomic; even envelope Σdim³=10,64,596,… has no closed form. UNIFIES with A5 (genus): both fail because the extra dim ∉ shifted-symmetric algebra A. Missing tool = non-shifted-symmetric dimension-functional expansion (dim/ln-dim vs Plancherel: Vershik-Kerov ln-dim, Schur-measure, hook-content) — NOT character machinery. This also sharpens A2 (leading term Cov(ln f,ω₃) needs ln-dim expansion). Audit: 2026-07-25-covariance-kernel-A1-eliminated-dim-threshold.md



---

## 2026-09-07 cross-ref (`qou-igjo`, merged #7046)

This bean names the missing tool as a *non-shifted-symmetric dimension-functional
(ln-dim) expansion*. The obvious candidate — expanding `ln f` in the Kerov modes
`Σ_p` — is now measured and **will not terminate**: the share of `Var_P(ln f)`
carried by the low single-cycle modes falls from 20.8% (k=12) to 12.4% (k=52).
The class basis explains it: the single-cycle classes are k−1 of the p(k)
orthonormal directions of L²(Plancherel_k). Detail and the two related exact
facts are on `qou-r91v`.

Also: the dim²→dim³ threshold recorded here was re-derived independently in that
PR's probe docstring (`Σf` involutions / `Σf²` = k! via RSK / `Σf³` no closed
form) without crediting this bean, because I did not find it first. The finding
is this bean's, dated 2026-07-25.
