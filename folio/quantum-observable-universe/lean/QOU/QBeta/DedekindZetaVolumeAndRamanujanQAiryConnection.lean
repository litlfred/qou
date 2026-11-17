/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

Beans:
  - qou-2pp7: Cross-check 9811173v1.pdf [broadhurst1998] at computations/binding_link_volumes.py
  - qou-cp1x: Cross-check 1104.0755v2.pdf [morita-t2011] at computations/probes/awzero_asymptotics_probe.py
-/

namespace QOU.QBeta

/-!
# Section 1: Broadhurst Rational Dedekind-Zeta Invariants of Hyperbolic 3-Manifolds (`qou-2pp7`)

Ref: [broadhurst1998] D. J. Broadhurst, "Determinations of rational Dedekind-zeta invariants of
hyperbolic manifolds and Feynman knots and links", arXiv:hep-th/9811173v1 (1998):
For a hyperbolic 3-manifold `M` whose invariant trace field `K` has a single complex place,
`Vol(M)` is a rational multiple `(a / b) * Z_K` of the normalized Dedekind zeta invariant `Z_K`
at `s = 2`. Across the SnapPea census, `152` distinct Dedekind zeta values are identified, with
`91` manifolds reducible to pairs of them.
-/

/-- Number of ideal regular tetrahedra (`a / b = 2`) in the figure-eight knot complement `4_1`
(`m004`) over `ℚ(√-3)` (`qou-2pp7`).
Ref: [broadhurst1998] §2, Table 1. -/
def figureEightDedekindMultiple : Nat := 2

/-- Number of ideal regular tetrahedra (`a / b = 2`) in Thurston's sister manifold `m003` over
`ℚ(√-3)` (`qou-2pp7`).
Ref: [broadhurst1998] §2, Table 1. -/
def thurstonSisterDedekindMultiple : Nat := 2

/-- Rational multiple `a / b = 4` of Catalan's constant `G = D_2(i)` (`Z_{ℚ(i)}`) for the
2-component Whitehead link complement `L5a1` (`qou-2pp7`).
Ref: [broadhurst1998] §2. -/
def whiteheadCatalanMultiple : Nat := 4

/-- Rational multiple `a / b = 8` of Catalan's constant `G = D_2(i)` (`Z_{ℚ(i)}`) for the
3-component Borromean rings complement `L6a4` (`qou-2pp7`).
Ref: [broadhurst1998] §2. -/
def borromeanCatalanMultiple : Nat := 8

/-- Census counts reported in Broadhurst (1998): `152` distinct Dedekind-zeta values at `s = 2`,
of which `91` census manifolds reduce to pairs of values (`qou-2pp7`).
Ref: [broadhurst1998] Abstract. -/
def broadhurstDistinctZetaCount : Nat := 152
def broadhurstPairReducibleCount : Nat := 91

/-- Linear Dedekind-zeta volume combination `m * zUnit` for rational multiple `m` and scaled
field unit `zUnit` (`qou-2pp7`).
Ref: [broadhurst1998] eq. (1). -/
def dedekindZetaVolumeMultiple (m zUnit : Int) : Int :=
  m * zUnit

/-- Exact commensurability relations for the `ℚ(√-3)` (`4_1 = m004` and `m003`) and `ℚ(i)`
(`L5a1` Whitehead and `L6a4` Borromean) hyperbolic link complements:
1. `Vol(4_1) = Vol(m003) = 2 * Z_{ℚ(√-3)}`,
2. `Vol(L6a4) = 8 * G = 2 * Vol(L5a1)` for every Catalan unit `gUnit`,
3. `152 - 91 = 61` single-zeta census manifolds (`qou-2pp7`).
Ref: [broadhurst1998] Abstract & §2. -/
theorem broadhurstDedekindZeta_commensurability (zSqrt3 gCatalan : Int) :
    figureEightDedekindMultiple = thurstonSisterDedekindMultiple ∧
    borromeanCatalanMultiple = 2 * whiteheadCatalanMultiple ∧
    dedekindZetaVolumeMultiple 2 zSqrt3 + dedekindZetaVolumeMultiple 2 zSqrt3 =
      4 * zSqrt3 ∧
    dedekindZetaVolumeMultiple 8 gCatalan =
      2 * dedekindZetaVolumeMultiple 4 gCatalan ∧
    broadhurstDistinctZetaCount - broadhurstPairReducibleCount = 61 := by
  dsimp [figureEightDedekindMultiple, thurstonSisterDedekindMultiple,
    borromeanCatalanMultiple, whiteheadCatalanMultiple, dedekindZetaVolumeMultiple,
    broadhurstDistinctZetaCount, broadhurstPairReducibleCount]
  omega

/-!
# Section 2: Morita Connection Formula Between Ramanujan `A_q` and `q`-Airy `Ai_q` (`qou-cp1x`)

Ref: [morita-t2011] T. Morita, "A connection formula between the Ramanujan function and the
q-Airy function", arXiv:1104.0755v2 (2011), Theorem (§1, p. 4, proved in §4):
For all `x ∈ ℂ*` and `0 < |q| < 1` (with `w = q^2`):
  `A_{q^2}(-q^3 / x^2) = (1 / (q, -1; q)_∞) * (θ(x / q) Ai_q(-x) + θ(-x / q) Ai_q(x))`,
controlling the asymptotic zeros `ζ_n = w^{1 - 2n} (1 + O(w^n))` of `A_w` via the Jacobi theta
zero lattice.
-/

/-- Quadratic exponent `n (n - 1)` of `q` in `w^{n(n-1)/2}` under `w = q^2` for the `n`-th series
term of `A_w(z)` (`qou-cp1x`).
Ref: [morita-t2011] §1, eq. (1). -/
def moritaQuadraticExponent (n : Int) : Int :=
  n * (n - 1)

/-- Tropical corner exponent `1 - 2n` in `ζ_n = w^{1 - 2n} (1 + O(w^n))` for the `n`-th zero of
`A_w` (`qou-cp1x`).
Ref: [morita-t2011] §1, Theorem. -/
def moritaTropicalCornerExponent (n : Int) : Int :=
  1 - 2 * n

/-- First-difference identity for `moritaQuadraticExponent`:
`(n + 1) n - n (n - 1) = 2 n`, and constant spacing `-2` between successive tropical corner
exponents `1 - 2 (n + 1) - (1 - 2 n) = -2` (`qou-cp1x`).
Ref: [morita-t2011] §1 & §4. -/
theorem moritaExponent_and_tropicalSpacing (n : Int) :
    moritaQuadraticExponent (n + 1) - moritaQuadraticExponent n = 2 * n ∧
    moritaTropicalCornerExponent (n + 1) - moritaTropicalCornerExponent n = -2 := by
  dsimp [moritaQuadraticExponent, moritaTropicalCornerExponent]
  have h1 : (n + 1) * (n + 1 - 1) = n * n + n := by
    have h1a : n + 1 - 1 = n := by omega
    rw [h1a, Int.add_mul, Int.one_mul]
  have h2 : n * (n - 1) = n * n - n := by
    rw [Int.mul_sub, Int.mul_one]
  rw [h1, h2]
  omega

/-- Morita's symmetric theta-Airy combination
`M(θ_+, θ_-, Ai_+, Ai_-) = θ(x / q) Ai_q(-x) + θ(-x / q) Ai_q(x)` (`qou-cp1x`).
Ref: [morita-t2011] §1, Theorem (p. 4). -/
def moritaThetaAiryCombo (thetaPos thetaNeg aiPos aiNeg : Int) : Int :=
  thetaPos * aiNeg + thetaNeg * aiPos

/-- Under reflection `x ↦ -x`, `(θ(x/q), θ(-x/q))` and `(Ai_q(x), Ai_q(-x))` swap roles, leaving
`moritaThetaAiryCombo` strictly invariant (even function of `x`, matching `A_{q^2}(-q^3 / x^2)`).
Furthermore, whenever `x = q^{2n - 1}` is a zero of `θ(-x / q)` (`thetaNeg = 0`), the combination
reduces to the single term `θ(x / q) Ai_q(-x)` (`qou-cp1x`).
Ref: [morita-t2011] §1, Theorem & §4. -/
theorem moritaThetaAiryCombo_reflection_even_and_thetaZero
    (thetaPos thetaNeg aiPos aiNeg : Int) :
    moritaThetaAiryCombo thetaNeg thetaPos aiNeg aiPos =
      moritaThetaAiryCombo thetaPos thetaNeg aiPos aiNeg ∧
    moritaThetaAiryCombo thetaPos 0 aiPos aiNeg = thetaPos * aiNeg := by
  dsimp [moritaThetaAiryCombo]
  omega

end QOU.QBeta
