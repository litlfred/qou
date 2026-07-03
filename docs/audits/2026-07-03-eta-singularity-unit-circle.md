# The η-descent singularity lies on the unit q-circle (0zr0 follow-up)

**Date:** 2026-07-03
**Producer:**
[`computations/qbeta/qbeta_eta_singularity_probe.py`](../../computations/qbeta/qbeta_eta_singularity_probe.py)
(witness `qbeta-eta-singularity.witness.json`; mpmath dps 40 + exact rungs)
**Lineage:**
[`2026-07-03-0zr0-eta-descent-invariant-theory-prune.md`](2026-07-03-0zr0-eta-descent-invariant-theory-prune.md)
left one sharpened datum — the descent function E(t), t = η², has a finite
radius of convergence with the nearest singularity on the negative t-axis.
This probe identifies where, and by what mechanism.

## LEG 1 — the singularity location from the exact rungs

| method | t_c |
|---|---|
| Domb–Sykes (3-point, crude) | −0.04269, exponent γ ≈ −0.20 |
| Padé [3/3] nearest pole | −0.05404 |
| Padé [3/4] nearest pole | −0.05151 |
| Padé [4/4] nearest pole (adopted) | **−0.04805** |

Consistent with the rung-ratio bound (≈ −1/20.5 = −0.0488). Estimates
agree at the ~10% level — 8 rungs is a short series; the location is
robust, the exponent is not.

## LEG 2 — the mechanism, from the closed-form net route

The net route is closed-form, so candidate singular points are locatable
directly in the complex s-plane (s = q−1). Scan results (upper
half-annulus 0.10 < |s| < 0.45; conjugates implied):

| mechanism | s | \|q\| = \|1+s\| | \|t-image\| / \|t_c\| |
|---|---|---|---|
| zero of O (cube-root branch of η) | −0.0663 + 0.3581i | **1.0** | 0.13 |
| zero of O′ (critical point of s ↦ t) | −0.0397 + 0.2789i | **1.0** | **0.87** |
| zero of net route (log branch) | none found in annulus | — | — |
| cos α = 0 | none in annulus (needs \|α\| ≈ π/2) | — | — |

**Finding 1 (structural, with a one-line proof): the bar-odd channel's
zeros are confined to the unit q-circle.** On |q| = 1 the bar involution
σ: q ↦ 1/q coincides with complex conjugation (1/q = q̄), so for the
real-coefficient bar-odd series O: conj(O) = O∘σ = −O there — **O is
purely imaginary on the unit circle**, and its zeros are the zeros of the
single real function Im O(θ), generically isolated points ON the circle.
Both numerically located candidates indeed sit at |q| = 1 to working
precision (|q|−1 = 0.0 at 40 dps). The unit q-circle — the closure of the
root-of-unity locus — is thus the natural singular locus of the
ζ₄-channel descent.

**Finding 2 (numeric identification, suggestive not clinched): the
nearest t-singularity is the critical point of the descent map** (zero of
O′, where the inverse of s ↦ t(s) branches — consistent with a
square-root-type singularity of E(t)) at

    q* = e^{iθ*},  θ* ≈ 0.28270 rad,  θ*/2π ≈ 0.044993.

Its principal-branch |t|-image reproduces 87% of |t_c|; the 13% gap is
attributed to branch/edge-of-convergence effects in evaluating t(s) near
the circle (recorded as a caveat, not resolved). The rational-angle scan
flags θ*/2π ≈ 1/22 within 5×10⁻⁴ (1/22 = 0.045455, i.e. a 1% miss) — a
**borderline** match: q* being a 22nd root of unity is not established;
at face value θ*/2π is non-rational to the resolution available.

## What this sharpens

- The refuted odd-sector functional forms (h·D+h³·F, cosh/sinh V₀ family)
  are replaced by a **located obstruction**: the descent variable's
  domain is bounded by the unit q-circle, where the bar-odd channel
  degenerates (O purely imaginary, zeros on the circle).
- Physically suggestive reading (not a claim): the ζ₄/complex-volume
  channel "sees" the root-of-unity boundary — the locus where q-series
  become quantum invariants at roots of unity — at a specific
  non-small-order angle θ* ≈ 0.2827. Any future ζ₄-route proposal should
  predict θ*.

Scope (a) throughout: ORD-17 truncation, net route, numeric
identification at the ~10% level; no wiring.
