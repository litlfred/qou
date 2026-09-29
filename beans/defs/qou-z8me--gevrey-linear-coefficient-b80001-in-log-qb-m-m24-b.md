---
# qou-z8me
title: 'Gevrey linear coefficient B=8.0001 in -log_q|b_m| = m^2/4 + Bm + C — exactly 8, or a log-correction artifact? (do NOT read as the self-linking 8 until derived)'
status: todo
type: task
priority: low
created_at: 2026-08-07T01:00:00Z
updated_at: 2026-08-07T01:00:00Z
---

## Observation (PR #4647, `c3_w2_c1_qborel_singularity.py`)

Solutions of the C1 recurrence `[m+2]_q·b_{m+2} = b_{m+1} + b_m` decay as

    -log_q|b_m| = A·m² + B·m + C

Fitting on `m ∈ {600,700,800}` at 500 dps gives

    A = 0.25            (exact; q-Gevrey order ½ = the Newton slope ½)
    B = 8.00010424
    C = -60.52580304

`A = 1/4` is solid and structurally confirmed. **`B` is the open question.**

## Why it is suspicious in both directions

- A crude two-step asymptotic predicts `B ≈ 7.5`, not 8. From
  `b_{m+2} ≈ (q−q⁻¹)q^{−(m+2)}b_m` one gets `ΔL ≈ −(m+2) − 15` per two steps
  (since `log_q(q−q⁻¹) ≈ −15`), summing to `−m²/4 − 7.5m`. So 8 is *not* what
  the leading asymptotic gives.
- The fit's large `C = −60.5` suggests it is absorbing higher-order terms.
  A genuine `m·log_q(m)` term would make a pure quadratic fit drift, and `B`
  would not be a constant at all.

## The trap to avoid

`8` is also the self-linking `(m−1)(n−1)` of **both** force-carrier torus
knots `T₂,₉` and `T₃,₅` — it appears as `_sl = 8` in the α_em Gram
computation. **Do not read the coincidence as meaningful.** This is exactly
the pattern the anti-numerology discipline exists for: an integer that shows
up in two places is a prompt to derive, never evidence on its own.

## Task

1. Refit with an `m·log m` term included and see whether `B` stabilises or
   the log coefficient absorbs it.
2. Fit at several disjoint `m`-windows (e.g. 400/500/600 vs 700/800/900) and
   check whether `B` is window-independent. Drift ⇒ not a constant.
3. If `B` is genuinely a constant, derive it from the recurrence rather than
   fitting it — the two-step asymptotic above is the natural starting point,
   and the gap between its 7.5 and the measured 8.0001 is the thing to explain.

Low priority: `B` shifts the q-Borel radius (`q^{1/4+B}`) but the singularity
*structure* — which is what carries the Stokes data — is established
independently by the branch-dependence result.
