---
# qou-4wl1
title: 'A3 (leg 2): bound remainder |R|<|g''(0)| via mixed-cumulant (Sniady genus) scaling'
status: in-progress
type: task
priority: high
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T11:14:07Z
parent: qou-v8t7
---

## A3 — leg 2: remainder |R|<|g'(0)|. Complete-monotonicity route TESTED and REFUTED (2026-07-25).
SIGNATURE (real): Taylor coeffs a_m=g^{(m)}(0)/m! of g(θ)=E_{2+θ}[ω₃] follow sign(a_m)=(−1)^m for
n=8..17 to order 10 (60dps); Σ_{m≥2}|a_m|<|a_1| all n. This is the NECESSARY part of −g' being
completely monotone.
REFUTED (decisive): −g' CM ⇔ moments m_k=(k+1)!|a_{k+1}| Stieltjes ⇔ Hankel H0,H1 PSD. They are NOT
(negative min-eigs, robust at 3×3 high-precision and 4×4; PSD only ~5/12, no pattern). So −g' is NOT
completely monotone; the Bernstein route (−g'=∫e^{−θs}dμ) is ELIMINATED (route #10). Sign-alternation
is necessary but not sufficient; it just re-expresses the Phase-7 bound |R|<|g'(0)|.
STATUS: remainder-domination target stands but WITHOUT the CM/Bernstein shortcut. Next: the genus
grading (Śniady 0411647) as an effective (not exact) bound on the mixed cumulants — the harder route.
Audit: 2026-07-25-covariance-kernel-complete-monotonicity-target.md.
