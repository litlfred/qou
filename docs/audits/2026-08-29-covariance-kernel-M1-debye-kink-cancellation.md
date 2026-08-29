# Covariance-kernel epic (`qou-x631`) — M₁>0 Debye constant-tracking: sub-leading exponent is indeterminate (kink-cancellation claim RETRACTED)

**Date:** 2026-08-29 · **Branch:** `claude/m1-debye-constant-tracking-2026-08-29` · **Tier:**
asymptotic-structure measurement + **self-correction** · **Discipline:** no fit; nothing wired; no
`c_k`; L2 unchanged; honest-negative. **Epic:** `qou-x631`; gap `qou-k5r5`; machinery `qou-h315`.

## 🛑 RETRACTION (of this file's first draft)

The first version of this audit claimed: *"the `|u|`-kink term vanishes; the rigorous rate is `θ^{−1}`
(smooth Euler–Maclaurin), by transpose symmetry."* **That is retracted — over-stated on two counts:**

1. **The transpose-symmetry argument does not prove `c_{1/2}=0`.** The reflection `k ↦ −1−k` sends the
   weight `g_A ↦ −g_A` and the kernel `J² ↦ J²`, so `V_A = ½Σ(g_A(x)−g_A(y))²J²` is **automatically**
   invariant — the symmetry is a relabelling of the summation, satisfied by construction, and it does
   **not** isolate or annihilate the `θ^{−1/2}` coefficient. "Even statistic under a symmetric law ⟹
   the half-power cancels" is a heuristic about *distributional* (Edgeworth/skewness) expansions, not
   about the *variance*'s asymptotic expansion; it was applied without justification.

2. **The numerics do not resolve the sub-leading exponent.** Re-tested on the same 6 points
   (`θ = 256…8192`, `V_A/θ²` good to ~1e-6): the bases `θ^{−1/2}`, `θ^{−2/3}`, `θ^{−5/6}`, `θ^{−1}` all
   fit with **comparable residual** (3.4, 3.2, 3.0, 2.3 ×10⁻⁶); the best *single* power is `p ≈ 0.94`.
   The `c_{1/2}` estimate is small (`|·|<1e-3`) and sign-unstable — consistent with 0, but **also**
   consistent with a `θ^{−5/6}` Airy-**edge** term I had ignored. Six points at this precision cannot
   tell these apart, so `c_{1/2}=0` is **not** established numerically either.

## What is actually true (robust)

- `V_A/θ² → v_A = 0.810568`, monotone from below, no oscillation.
- The correction is **small** — coefficient magnitude `~0.05`, effective single-power exponent
  `≈ 0.9` over `θ ∈ [256, 8192]`.
- That is all that the **(CS) closure** needs: any rate `≥ θ^{−1/2}` with a small constant traps the
  margin (30–300× headroom, PR #5937). **The closure feasibility is unaffected by this retraction** —
  what changes is only the *claimed mechanism/exponent*, not the prospect.

## Consequence for the machinery plan

- **`qou-8quz` ("prove `c_{1/2}=0` by transpose symmetry") is refuted as posed.** The symmetry does
  not do it. Whether the half-power vanishes (or is a `θ^{−5/6}` edge term) is entangled with the
  Airy-edge contribution and can only be settled by the **actual Euler–Maclaurin + edge analysis**
  (`qou-tvok`), not a symmetry one-liner. `qou-8quz` should be closed as *refuted*, folding its
  question into `qou-tvok`.
- The Route-1 decision (Kerov limit-shape + `CompositeEulerMaclaurin`) stands, but `qou-tvok` must now
  **include the edge (`θ^{−5/6}`) contribution explicitly** rather than assume a clean `θ^{−1}` bulk.

## Why record the negative

The retracted claim was a plausible-sounding symmetry shortcut that the measurement seemed to confirm.
It failed both tests — the symmetry is automatic, and the "confirmation" was an artifact of an
ill-conditioned power-basis fit that cannot discriminate the candidate exponents. Recording it
prevents a future agent (or me) from re-deriving the same wrong shortcut, and keeps the honest state:
the correction is small and closure-compatible, but its exponent is open.

## Compute

- [`wlambda_covariance_epic_M1_debye_expansion_fit.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_debye_expansion_fit.py)
  (exit 0; dps 60; exact Bessel sums; NO float64) — now reports the discriminancy test and the
  corrected verdict.

## Cross-references

- Debye investigation: [`2026-08-29-covariance-kernel-M1-debye-CA-investigation-verdict.md`](2026-08-29-covariance-kernel-M1-debye-CA-investigation-verdict.md)
- Machinery inventory + route: [`2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md`](2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md)
- Gap bean `qou-k5r5`; machinery epic `qou-h315`; task `qou-tvok` (now inherits the edge term).
