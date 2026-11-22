/-
# QOU.QBeta.A3BranchingModulusReflection — the branching reduction and the modulus lift are a Pythagorean pair, and the branching's own asymmetry is too small

`A3OffBlockDerivation` derives, from the `H₃(q)` Wedderburn branching with **no** freedom
(the `(3)↔(1,1,1)` bar-swap), the super-matrix blocks `A = D = (a+b)/2`, `B = C = (a−b)/2`
(bar-odd, `σB = −B`), and proves the self-adjoint even-face factor is the **reduction**
`factor_sa = 1 − x²`, `x = (a−b)/(a+b)`, with `factor_sa ≤ 1` (`magnitudeFactor_le_one`).

`BirkhoffBarOddPythagorasBridge` proves that the bar-odd unit-modulus carrier `E = χ(P)`
squares to `−1`, so the physical lift read as the modulus of the affine carrier is the
**quadrature** `factor_sa² + s²`. This file composes the two: it identifies the transverse
leg `s` with `2x` under the unit-trace normalization and records the exact Pythagorean
identity, then names the scope-(a) numerical wall.

**The Pythagorean structure (proved).** The branching reduction `1 − x²`, the transverse leg
`2x`, and the modulus lift `1 + x²` form a Pythagorean triple:

  `(1 + x²)² = (1 − x²)² + (2x)²`.

So the modulus lift is the **reflection of the self-adjoint reduction about `1`**:
`lift = 1 + x² = 2 − factor_sa`. This is the concrete `A=3` form of the bridge: the reduction
is a leg, the transverse datum `2x` is the other leg, the lift is the hypotenuse.

**The scope-(a) wall (numeric, recorded in the audit/probe, NOT here).** The observed lift is
`r* = μ₃/c₃ ≈ 1.585`, i.e. it needs `x² ≈ 0.585` (`x ≈ 0.765`). The **branching's own**
bar-asymmetry is far smaller: the symmetric Wedderburn weight gives `x = 0` (the two 1-dim
blocks are bar-even, equal); the content weight `q^{±3}` gives `x² ≈ 0.09` (`r* ≈ 1.09`); the
raw content-weighted branching gives `r* ≈ 0.96`. No clean topological content reproduces
`x = 0.765`. Hence the **transverse leg `2x` is NOT the branching slope** `B·D⁻¹/A` — it is a
genuinely transverse (Birkhoff/Stokes surface-curvature, bean `qou-prjo`) datum ~6× larger in
`x²` than the fixed `H₃` branching supplies. This is the honest negative on "derive `s` from
the branching": the branching cannot.

**Honesty (STRICT).** Generic-field algebra, sorry-free, no `native_decide`, no trivial-true,
no axiom. `r*`/`μ₃`/`c₃`/`x` are never inverted to fit; the numbers live only in the Python
witness. This file adds no closure — it proves the Pythagorean structure and names the wall.

## References
- [leitner2026] `QOU.QBeta.A3OffBlockDerivation` (`magnitudeFactor_eq`, `magnitudeFactor_le_one`,
  the branching blocks `A=D=(a+b)/2`, `B=(a−b)/2`); `QOU.QBeta.BirkhoffBarOddPythagorasBridge`
  (`barOdd_unitModulus_sq_eq_neg_one`, `affine_modulus_quadrature`); beans `qou-wiub`,
  `qou-jqof`, `qou-prjo`.
-/
import Mathlib.Tactic

namespace QOU.QBeta.A3BranchingModulusReflection

/-- The branching asymmetry `x = (a−b)/(a+b)` (the single scale-free datum of the
`(3)↔(1,1,1)` bar-swap; `a = m₍₃₎`, `b = m₍₁,₁,₁₎`). -/
noncomputable def asymmetry {K : Type*} [Field K] (a b : K) : K := (a - b) / (a + b)

/-- The self-adjoint even-face **reduction** `factor_sa = 1 − x²` (amplitude form of
`A3OffBlockDerivation.magnitudeFactor_eq`). -/
noncomputable def reduction {K : Type*} [Field K] (a b : K) : K := 1 - (asymmetry a b) ^ 2

/-- The modulus **lift** `1 + x²` (the bar-odd unit-modulus quadrature reading). -/
noncomputable def lift {K : Type*} [Field K] (a b : K) : K := 1 + (asymmetry a b) ^ 2

/-- **Pythagorean identity (sorry-free).** The reduction `1 − x²`, the transverse leg `2x`, and
the lift `1 + x²` form a Pythagorean triple. This is the concrete `A=3` bridge: the modulus of
the affine carrier `factor_sa − s·E` (with `E² = −1`, `s ↦ 2x`) is the hypotenuse of the leg
`factor_sa` and the transverse leg `2x`. -/
theorem pythagorean_triple {K : Type*} [Field K] (x : K) :
    (1 + x ^ 2) ^ 2 = (1 - x ^ 2) ^ 2 + (2 * x) ^ 2 := by ring

/-- **Reflection about `1` (sorry-free).** The modulus lift is `2` minus the self-adjoint
reduction: `lift = 2 − factor_sa`. The bar-odd unit-modulus reading reflects the branching
reduction (`≤ 1`) into a lift (`≥ 1`) across `1`. -/
theorem lift_eq_two_sub_reduction {K : Type*} [Field K] (a b : K) :
    lift a b = 2 - reduction a b := by
  simp only [lift, reduction]; ring

/-- **The lift is the modulus quadrature of the reduction and the transverse leg (sorry-free).**
`lift² = reduction² + (2x)²` — the Pythagorean identity in the branching variables. -/
theorem lift_sq_eq_reduction_sq_add_transverse {K : Type*} [Field K] (a b : K) :
    (lift a b) ^ 2 = (reduction a b) ^ 2 + (2 * asymmetry a b) ^ 2 := by
  simp only [lift, reduction]; ring

/-- **The reduction never exceeds `1` for a real branching (sorry-free)** — the amplitude form
of `A3OffBlockDerivation.magnitudeFactor_le_one`: `factor_sa = 1 − x² ≤ 1`, so the self-adjoint
branching is a reduction. The lift `2 − factor_sa ≥ 1` is therefore the *reflected* value, and
requires the transverse leg `2x` — which the branching's own small `x` cannot make large
enough (scope-(a), see the audit). -/
theorem reduction_le_one {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (a b : K) : reduction a b ≤ 1 := by
  simp only [reduction]
  have : (0 : K) ≤ (asymmetry a b) ^ 2 := sq_nonneg _
  linarith

end QOU.QBeta.A3BranchingModulusReflection
