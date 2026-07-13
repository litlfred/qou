# residue-A kernel deepening — combined verdict (tasks 3 · 1 · 2)

**Date:** 2026-06-04
**PR:** [#1839](https://github.com/litlfred/qou/pull/1839)
**Status:** DONE
**Plan:** [2026-06-04-residue-a-kernel-deepening-plan.md](2026-06-04-residue-a-kernel-deepening-plan.md)

## 3 — Lean engine (verified sorry-free)

[`RationalCoeffRecurrence.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/RationalCoeffRecurrence.lean)
gained, against the bootstrapped toolchain (mathlib `f897ebcf`, lean v4.24.0):

- **`CFinite d q c`** — the order-`d` constant-coefficient recurrence (the
  coefficients of a proper rational `P/Q`).
- **`CFinite.recurrence_step`** — the recurrence *solves for the leading term*:
  `c n = -(q 0)⁻¹·∑_{j<d} q(j+1)·c(n-(j+1))` for `n ≥ d`. The "kernel produces
  `c_k` from the seed" engine, in math form.

`lake build` → *"Build completed successfully (875 jobs)"*, 0 errors / 0 sorries.

## 1 — recurrence re-run on consistent-precision c_k (cross-check)

Sibling **#1824** bias-corrected the c_k (probe 6.a: c_2 → −0.99999, c_3 →
−1.99999, toward the canonical values) and found (probe 6.c) the depth-2 kernel
**unstable** on the corrected c_k (`α_mean ≈ −59081`). The cross-check
[`qbeta_ck_recurrence_on_corrected_crosscheck.py`](../../folio-assistant/computations/qbeta/qbeta_ck_recurrence_on_corrected_crosscheck.py)
applies the Step-2 **Hankel-rank + over-determined** method to the SAME corrected
c_k: **no Hankel collapse, no constant-coeff recurrence ≤ d=4** (residuals ~2–3%,
*worse* than the raw ~1e-5 — de-biasing makes c_8/c_9 erratic).

**Two independent methods agree** ⇒ the no-low-order-kernel result is **robust to
de-biasing**, not an extraction-noise artifact. This **resolves the Step-2
caveat**: the kernel `R` is genuinely higher-order; `F` is not a low-degree
rational (the verified contrapositive of `pole_reciprocal_is_char_root`).

## 2 — SDP-normalization zero (synthesis refuted in literal form)

The #1823 interpretive synthesis (flagged *not-yet-derived*) read the
`u_substrate` pole as a zero of the SDP normalization `Q_A·cos α_eff`. The probe
[`qbeta_sdp_normalization_zero_probe.py`](../../folio-assistant/computations/qbeta/qbeta_sdp_normalization_zero_probe.py)
tests it on the documented closed form `Q_A·cos α_eff = Q_N2/(1-u²)`:

- `Q_A·cos α_eff(u_substrate) = 0.78239 ≠ 0` (smooth, nonzero).
- Its only singularity (`N2 = 1-u² = 0` ⇒ `u = ±1`) is **~116× farther** than
  `u_substrate`.

**Verdict: REFUTED in literal form.** The pole is **not** the cos-correction
factor's zero — it is **intrinsic to the c_k Habiro ladder** (radius of
convergence = `u_substrate`, i.e. `c_{k+1}/c_k → 1/u_substrate`, PR #1713). The
keystone lives in `Q_N2`'s deeper Habiro structure / the canonical `c_11+`
extraction, not the documented normalization factor.

## Net (the kernel is now sharply localised)

Three converging results pin the keystone:
1. (Lean) `F` rational ⇔ `c_k` low-order C-finite — proved grounding.
2. (compute, robust to de-biasing) the `c_k` are **not** low-order C-finite ⇒
   `F` not low-degree rational ⇒ kernel genuinely higher-order.
3. (compute) the pole is **not** the SDP cos-factor zero ⇒ intrinsic to the
   Habiro ladder.

⇒ the productive direction is **canonical `c_11+` extraction** (the only way to
pin a higher-order kernel / push residue-A precision past ~4 sig figs) **or** a
categorical derivation of `Q_N2`'s deeper structure — **not** low-order fits,
real-q forms, root-of-unity evaluations, or the cos-factor. All four of those
are now refuted.

## Guards

TIERED; no fitting; Lean verified sorry-free; `ℏ_q`/`q₀` from canonical
witnesses; diagnostic-only; tiers governed by the
[c_k/d_k registry](../coordination/ck-dk-canonical-registry.md).
