# α_EM per-loop measure: flat-torus Maxwell 1-loop partition function — deriving the π and the reciprocal

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure · **Tier:** measurement
(scope-(a); no `α_k` wired; no fit; `1/(8π)` stays an identification until
genuinely derived) · **Branch:** `claude/alpha-em-perloop-flat-torus-maxwell-2026-07-18`.

## The residual wall (post-Front-3)

The Front-3 lead landed (#3834): `ζ_{Δ₁}(0) = −b₁ = −8`, exactly and **area-free**
— the canonical home of the bare mode-count. And `D = 8` is uniquely
data-selected to ~3500σ (`2026-07-17-alpha-em-perloop-integer-forcedness.md`).
Two pieces of the per-loop measure `1/(π·b₁) = 1/(8π)` remain **OPEN** (the
ζ(0) probe's own "not derived" list):

1. the **bare π**, and
2. the **reciprocal** form `1/(π·b₁)` — the full determinant + per-mode weight,
   not `ζ(0)` alone.

Both live on the photon target `J(M) = H¹/H¹(ℤ) = T^{b₁}` (`Jac(Bring) ~ E⁴`,
`b₁ = 8`). The derived surface zero-mode measure `1/(12π) = b₁/Area`
(Lean `PhotonIRZeroMode`, Gauss–Bonnet) is the template.

## Approach (STRICT — anti-laundering)

Compute the **flat-torus Maxwell 1-loop partition function** `Z_Maxwell(T^{b₁})`
independently — the harmonic-1-form moduli Gaussian measure × `det'Δ₁^{-1/2}`,
ζ-regularized (reusing the Epstein-zeta machinery of the #3834 probe) — and
**measure** which power of π and which b₁-dependence the standard photon path
integral produces. Then **compare** to `1/(π·b₁)`. The value is never solved
from CODATA; `D = 8` is not tuned.

*(results + verdict land here)*

<!-- RESULTS -->

## Kill criteria (pre-stated)

- **Negative** if the partition-function measure carries area / covolume
  dependence, or a π-power ≠ 1, or a b₁-dependence that is not the reciprocal —
  report scope-(a) negative, do NOT stretch normalization conventions to
  manufacture `8π` (the spec's fitting trap).
- **Positive-partial** only if the `π^{-1}` and the reciprocal-in-b₁ emerge
  from the path-integral normalization independently of CODATA.

## Cross-references

- Front-3 lead: [`2026-07-17-alpha-em-zeta-anomaly-b1-count.md`](2026-07-17-alpha-em-zeta-anomaly-b1-count.md)
- Forcedness: [`2026-07-17-alpha-em-perloop-integer-forcedness.md`](2026-07-17-alpha-em-perloop-integer-forcedness.md)
- Wall map: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md)
- Ledger: [`alpha-em.md`](../coordination/alpha-em.md)
