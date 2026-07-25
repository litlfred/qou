---
# qou-4wl1
title: 'A3 (leg 2): bound remainder |R|<|g''(0)| via mixed-cumulant (Sniady genus) scaling'
status: todo
type: task
priority: high
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T03:31:40Z
parent: qou-v8t7
---

## A3 — leg 2: remainder domination |R| < |g'(0)|
IDEA. g(θ)=E_{2+θ}[ω₃]; g(1)=kernel, g'(0)=Cov(ln f,ω₃). R=g(1)−g'(0)=Σ_{m≥2}g^{(m)}(0)/m!, and
g^{(m)}(0)=κ_{m+1}(ln f;…;ln f;ω₃) (mixed Plancherel cumulants). Need Σ_{m≥2}|κ_{m+1}|/m! < |κ_2|.
HARD PART (framework note): Var(ln f)=O(1) bounded ⇒ the tilt is fixed-scale, so the higher cumulants
do NOT vanish asymptotically (transfer ratio ~0.65 ~const, not →1). So this is NOT 'Gaussian ⇒ done';
need a genuine bound on the cumulant series, e.g. via Śniady's genus grading of the joint cumulants.
FIRST STEP. Compute κ_2..κ_6 exactly (higher θ-derivatives of g at 0, 40dps) for n≤16; fit their
n-scaling; test whether the genus grading gives a geometric/summable bound with margin < κ_2. Currently
|R|/|κ_2|=|r−1|∈(0.13,0.46).
SUCCESS. Rigorous |R|<|g'(0)|.
KILL. Cumulant series has no controllable structure. THE genuinely hard leg (couples to A5).
