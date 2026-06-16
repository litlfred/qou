# L2 100× dashboard refresh — post-#942 / #944 / cheat-sheet §5 close-out

> **Status (2026-05-23).** The L2 100× per-observable dashboard
> witness has been refreshed against current main (post-#942
> flavor-split wire-up + post-#944 H_12 Phase-1 extract + post-
> cheat-sheet §5 close-out). Headline: **2 of 6 observables beat
> the 100× experimental target**; the 4 misses are all dominated
> by a single 2.89% absolute-mass-scale residual on `VolDensity(𝓑₃)`
> for the proton/neutron. Closing that residual would close 3 of
> the 4 misses simultaneously.
>
> **Framing update (2026-05-24).** The 2.89% residual is **not**
> a separate "λ_scale closure" task — `λ_scale` was absorbed into
> the per-knot `VolDensity(K)` evaluation (per `prop:geom-universality`
> and the 2026-05-23 algebraic→geometric→observable consistency
> coord doc). The residual is the gap between the framework's
> current categorical `VolDensity(𝓑₃)` computation and its
> categorically-exact value. Refining the `VolDensity` evaluation
> (research-grade) is the remaining open piece.

## Before / after (refresh delta)

| obs | err_ppb before | err_ppb after | Δ | notes |
|---|---:|---:|---:|---|
| m_p | 2.960e+7 | 2.890e+7 | −2% | m_p split off m_avg by −Δm/2 |
| m_n | 2.819e+7 | 2.890e+7 | +3% | m_n split off m_avg by +Δm/2 |
| **Δ_pn** | **1.000e+9** | **2.858e+7** | **−35×** | flavor-split wire-up (#942) now reflected |
| m_mu | 0.05965 | 0.05965 | — | CAL-2 self-consistency check ✅ |
| Q_beta | 11.13 | 11.13 | — | CAL-3 anchor ✅ (just 1.43× from passing 100×) |
| m_e | 0 | 0 | — | CAL-1 anchor ✅ |

**Largest delta**: Δ_pn improved 35× from the stale-witness value of `1e9 ppb` (which reflected pre-#942 `m_p = m_n` baryon-class uniformity from the per-baryon `VolDensity` evaluation that was the same for both nucleons before the flavor-split layer landed). After flavor-split, predicted Δ_pn = 1.330 MeV vs CODATA 1.293 MeV → 28600 ppm residual.

## Current status

```
Observable  role                      pred err (ppb)     σ_exp (ppb)     100× target (ppb)     miss factor  1×?  100×?
m_p         validation                      2.890e+7          0.3091              0.003091        9.349e+9    N    N
m_n         validation                      2.890e+7          0.5747              0.005747        5.028e+9    N    N
m_mu        validation                       0.05965           21.77                0.2177          0.2740    Y    Y
Delta_pn    validation (derived)            2.858e+7           473.9                 4.739        6.031e+6    N    N
Q_beta      CAL-3 anchor                       11.13           779.7                 7.797           1.428    Y    N
m_e         CAL-1 anchor                           0          0.2935              0.002935    N/A (anchor)    Y    Y

Summary: 2/6 beat 100×, 3/6 beat 1×.
```

## Diagnostic — what's blocking each observable

| Observable | Blocker | Status |
|---|---|---|
| **m_p, m_n, Δ_pn** | 2.89% gap on the per-nucleon `VolDensity(𝓑₃)` evaluation vs. its categorically-exact value | Open (refinement of `VolDensity` itself; alternative derivation routes tested so far refuted — Bring-Bloch tier 0-5, V_7, q^10 pentagon, unit-circle Bloch class, Yekutieli per-cell purged 2026-05-24) |
| **Q_beta** (1.43× over 100×) | CAL-3 𝔇_π categorical formula |
| m_mu, m_e | CAL-2, CAL-1 anchors | ✅ trivially met |

## Implications

1. **Three observables (m_p, m_n, Δ_pn) share a single closure target**: the 2.89% per-nucleon `VolDensity(𝓑₃)` residual. A categorical refinement that closes this residual would close all three simultaneously. This is high-leverage but research-grade (alternative `VolDensity` derivation routes — Bring-Bloch, Yekutieli per-cell, V_7, q^10 pentagon, unit-circle Bloch class — have all been refuted or purged).

2. **Q_beta is the closest "easy win"** — just 1.43× from passing 100×. The categorical N=3 prediction `c_3 = -2 = J_Hopf(q=1)` (`q-beta-operator-valued-N3.witness.json`) already passes 1× experimental; a small substrate refinement could close it.

3. **Subgoal-1 (≥ CAL-2 floor) status**: m_mu PASSES 100× by 3.65× margin; m_e is the anchor; Q_beta just 1.43× away. **The achievable subset of L2 is essentially achieved or one refinement step away.**

4. **Subgoal-2 (sub-CAL-2 floor absolute m_p)**: research-grade, owner-declined 2026-05-08. The 9.3e9 miss factor reflects this; the gap is the `VolDensity(𝓑₃)` refinement that the CAL-4 cluster has been systematically working through.

## What's NOT visible in this dashboard

- **L1 internal cross-method precision** (`onepb-status-dashboard.witness.json`): separately GREEN.
- **Per-isotope binding energies B(K)** (D, T, ³He, ⁴He, ⁶Li, etc.): tracked by other witnesses (`atomic-mass-via-rho-k.witness.json`, etc.); not in this 6-observable dashboard.
- **Cross-derivation gaps** (e.g. m_⁴He vs CODATA): would need a 100×-against-AME dashboard variant.

## Cross-references

- [`docs/precision-goals.md`](../precision-goals.md) — L1 vs L2 definitions
- [`computations/per-observable-100x-status.witness.json`](../../computations/per-observable-100x-status.witness.json) — refreshed witness (this PR)
- [PR #942](https://github.com/litlfred/qou/pull/942) — flavor-split wire-up (the Δ_pn 35× improvement source)
- [PR #944](https://github.com/litlfred/qou/pull/944) — H_12 Phase-1 (unblocks A=4 mass-tower)
- [PR #966](https://github.com/litlfred/qou/pull/966) — cheat-sheet §5 close-out (all 5 items closed)
- [PR #952](https://github.com/litlfred/qou/pull/952) — Bring-Bloch unit-circle refutation
- [PR #951](https://github.com/litlfred/qou/pull/951) — q^10 + h²·G q-locality non-smoothness
- [PR #916](https://github.com/litlfred/qou/pull/916) — λ_scale strategies F/G/H/V_7 + brief
