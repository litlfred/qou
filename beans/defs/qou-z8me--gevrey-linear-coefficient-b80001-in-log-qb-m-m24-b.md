---
# qou-z8me
title: Gevrey linear coefficient B=8.0001 in -log_q|b_m| = m^2/4 + Bm + C — exactly 8, or a log-correction artifact? (do NOT read as the self-linking 8 until derived)
status: todo
type: task
priority: low
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-07T01:00:00Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-frzo
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


## 2026-11-21T12:40:00Z — alien-calculus drain (thread "Build the q-native alien calculus")

**Answered: B is not 8. B = (1 − log_q(q − q⁻¹))/2, a function of q.** Lean `QOU/Mathlib/C1GevreyLinearCoeff.lean` (`c1_linear_coeff_of_nonneg_init`, `linear_coeff_tendsto`, `two_step_increment_tendsto`, `quad_coeff_tendsto`): for q > 1 and every solution of [m+k]_q b_{m+2} = b_{m+1} + b_m with b₁ ≥ 0, b₀ + b₁ > 0, (−log_q b_m − m²/4)/m → (k − 1 − log_q(q − q⁻¹))/2. Sorry-free, axioms [propext, Classical.choice, Quot.sound], lean-direct exit 0 (lean 4.24.0, restored cache).

At the probe q the closed form is 8.000104239513764 (the fit gave 8.00010424); at q = 2 it is 0.2075. The self-linking 8 of T(2,9)/T(3,5) is a coincidence of evaluation: log_q(q − q⁻¹) ≈ −15.0002 at that q. The '7.5' heuristic above took β = λ/2; the increment of m²/4 + βm is m + 1 + 2β, so β = (1 + λ)/2. Parity-free q-Borel radius ξ_s = q^{B+1/4} = q^{3/4}/√(q − q⁻¹).

Probe pre-registered: docs/audits/2026-11-21-c1-gevrey-linear-coefficient.md; computations/probes/c1_gevrey_linear_coeff_probe.py (300 dps). P3 pass; P1/P2 fail their 1e-15 thresholds at q≈1.11 only (correction q^{-300} ≈ 2.5e-14 exceeds the threshold I set); fail criterion 1e-10 not met. Branch claude/alien-calculus-c1-gevrey-2026-11-21 (local commit 8ce0789da, PR pending owner card).

Scope: positive solutions only; sign-changing / complex data not proved. Superseded-premise check (owner 2026-11-21): none — pure q-difference object, q free, no photon/convention/trace/fit input.
