# α_EM per-loop measure: the continuum ζ-determinant routes to 8π are excluded — the derivation is state-sum

**Date:** 2026-07-17 · **Axis:** α_EM 2-loop / 1ppQ (#3612) · **Tier:** numerical
(scope-(a) exclusion of two derivation routes) · **Discipline:** no fit (D=8 is
NOT read from CODATA here — the opposite), no c_k, no tier change. Follow-up to
the merged forcedness result
([`2026-07-17-alpha-em-perloop-integer-forcedness.md`](2026-07-17-alpha-em-perloop-integer-forcedness.md):
`D* = 8 = dim H¹(Bring)` is data-selected, *not derived*).

## Question

The α_EM ladder's per-loop-measure denominator is `D = π·b₁ = 8π` (b₁ = 2g = 8,
Jac(Bring) ≅ E⁴). Forcedness proved 8 is the uniquely data-selected integer; the
*derivation* — why the photon 1-loop measure on the flat Jacobian
`J = H¹(M;ℝ)/H¹(M;ℤ)` carries a **bare** `π·b₁` — is open. The recon lead was
that the flat-torus scale anomaly `ζ_Λ(0)` is the canonical home of a bare
b₁-count. This note tests that decisively.

## Result — both continuum routes excluded (scope-(a))

[`alpha_em_bring_jacobian_zeta_determinant_probe.py`](../../computations/alpha_em_bring_jacobian_zeta_determinant_probe.py):

1. **Scalar ζ-anomaly route — REFUTED.** The Epstein `ζ_Λ(0)` of a rank-n flat
   lattice is `−1` for **all** n (n = 2, 4, 8 verified; rank-1 closed form
   `2ζ(0) = −1` anchors it). The scale anomaly `det(Δ/μ²) → μ^{2ζ_Λ(0)}` therefore
   contributes `−1`, **not** `−b₁`. The bare integer b₁ = 8 does **not** originate
   in the scalar-determinant scale anomaly. (This is Terras 1973: the
   `Vol/(4πt)^{n/2}` leading heat term feeds only the pole at `s = n/2`; the
   `s = 0` constant is `−dim ker = −1`, rank-independently.)

2. **Naive Gaussian-moduli-product route — also excluded.** The b₁-fold flat-
   modulus measure `∏_{i=1}^{b₁} ∫dc_i/√(2πμ²) = (2π)^{−b₁/2}` supplies a
   `π^{b₁}` **power**, not the required single `π·b₁`. So the naive per-mode
   Gaussian product does not give `8π` either.

## Consequence — the derivation target is the discrete state-sum normalization

Both *continuum* measure routes to `π·b₁` are excluded. The surviving mechanism
is the **Reshetikhin–Turaev / shadow-world handle normalization**: in a state-sum
TQFT each handle (genus generator) carries a single global factor `1/𝒟²`,
`𝒟² = Σ_λ dim(λ)²` — a *single global count*, structurally the right shape for a
bare `b₁` in the denominator (b₁ = 2g handle-generators of the genus-g Bring
surface). This is now the sharpened, single derivation target; the two continuum
red herrings are closed.

## Honest scope (anti-laundering)

This is a *negative* that **narrows** the derivation — it does not derive D = 8.
The forcedness result (D* = 8 data-selected) stands unchanged. Nothing is read
from CODATA here (the probe asks whether geometry *forces* 8, and finds the two
naive continuum routes cannot). No fit; no c_k; nothing wired; no tier change.
The working `1/(8π)` must still be *forced* by the state-sum computation, never
reverse-engineered from the CODATA-selected value.

## Cross-references

- Forcedness (merged): [`2026-07-17-alpha-em-perloop-integer-forcedness.md`](2026-07-17-alpha-em-perloop-integer-forcedness.md)
- Derivability map + zero-mode template: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md), [`../../content/quantum-observable-universe/lean/QOU/Archimedean/PhotonIRZeroMode.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/PhotonIRZeroMode.lean)
- Bring Jacobian ≅ E⁴: [`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md)
- Three-front spec: [`2026-07-17-three-front-attack-specs.md`](2026-07-17-three-front-attack-specs.md)
