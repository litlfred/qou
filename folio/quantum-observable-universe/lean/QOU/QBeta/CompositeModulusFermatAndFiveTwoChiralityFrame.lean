/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

# Composite-Modulus Fermat Inversion Failure vs Self-Inverse Face Pivots and `5₂` Chirality-Frame Boundary Slopes (`qou-b5h9`, `qou-lrvc`)

Formalizes the exact arithmetic and algebraic theorems for:
1. **Bean `qou-b5h9` (`8_11 KVC / kashaev_link_statesum._solve_mod composite modulus analysis`)**:
   - At composite modulus `N = 9` (where Euler's totient is `φ(9) = 6`), the Fermat
     exponent `a^(N - 2) mod N = a^7 mod 9` equals `a^(6 + 1) mod 9 = a mod 9` for every
     unit `a ∈ {1, 2, 4, 5, 7, 8}`, returning the pivot `a` itself rather than its
     multiplicative inverse `a⁻¹ mod 9`. Consequently, for every non-self-inverse unit
     `a ∈ {2, 4, 5, 7}`, `(a * a^7) mod 9 = a² mod 9 ≠ 1`, while on the zero divisors
     `a ∈ {3, 6}`, `a^7 mod 9 = 0`.
   - At the same time, for the two boundary units `a = 1` and `a = N - 1` (the `±1`
     pivots produced by `0/1` face-incidence elimination on the Whitehead system),
     `a² ≡ 1 (mod N)` holds for every modulus `N ≥ 2` (`(N - 1)² = N*(N - 2) + 1`),
     and `(N - 1)^(N - 2) mod N = N - 1` holds for every odd composite modulus `N = 9, 15`,
     explaining structurally why Fermat's formula coincided with the true inverse on
     all `±1` face-incidence pivots.
2. **Bean `qou-lrvc` (`which chirality is the Rolfsen 5₂ in the derived (μ, λ, Im τ > 0) frame`)**:
   - The derived Farey-word `RL` triangulation of `K(7, 3)` has normal boundary slopes
     `[-10, -4, 0]`, whereas the SnapPy `Manifold('5_2')` (`m015 = K3_2`) and Dunfield /
     Hatcher–Oertel table `K(3/7)` have boundary slopes `[0, 4, 10]`, related by the
     exact mirror involution `s ↦ -s` (`mirrorSlopes [-10, -4, 0] = [10, 4, 0]`, sorting
     to `[0, 4, 10]`) while leaving the sum of absolute boundary slopes `|-10| + |-4| + |0| = 14`
     (the `M`-span of the `A`-polynomial `A_{5₂}`) mirror-invariant.
   - At `M = 1`, the `L`-coefficients `[c_3(M), c_2(M), c_1(M), c_0(M)]` of the derived
     `A`-polynomial `A_{5₂}(L, M) = L³ + L²(M¹⁰ - M⁸ + 2M⁴ + 2M² - 1) + L(-M¹⁴ + 2M¹² + 2M¹⁰ - M⁶ + M⁴) + M¹⁴`
     specialize to `[1, 3, 3, 1]` (the binomial coefficients of `(L + 1)³`, summing to
     `1 + 3 + 3 + 1 = 8 = 2³`), and for general `M` the reciprocal transformation
     `L³ · A_{5₂}(L⁻¹, M)` reverses `[c_3, c_2, c_1, c_0]` to `[c_0, c_1, c_2, c_3]`.
-/

import Init.Data.Int.Basic
import Init.Data.List.Basic
import Init.Omega

namespace QOU.QBeta.CompositeModulusFermatAndFiveTwoChiralityFrame

/-! ## 1. Composite-Modulus Fermat Inversion Failure vs `±1` Self-Inverse Pivots (`qou-b5h9`) -/

/-- Fermat pseudo-inverse candidate `a^(N - 2) mod N` over `Nat`. -/
def fermatCandidate (a N : Nat) : Nat := (a ^ (N - 2)) % N

/-- **Fermat Formula Returns the Identity on Units Modulo `9` (`qou-b5h9`).**
Because `φ(9) = 6` and `N - 2 = 7 = 6 + 1`, for every unit `a ∈ [1, 2, 4, 5, 7, 8]`
modulo `9`, `fermatCandidate a 9 = a` (returning the pivot itself rather than `a⁻¹`),
and on the zero divisors `3` and `6` it returns `0`. -/
theorem fermat_mod_nine_returns_pivot_on_units_and_zero_on_divisors :
    ([1, 2, 4, 5, 7, 8].map (fun a => fermatCandidate a 9) = [1, 2, 4, 5, 7, 8]) ∧
    fermatCandidate 3 9 = 0 ∧
    fermatCandidate 6 9 = 0 := by
  decide

/-- **Fermat Formula Fails Inverse Property on Non-Self-Inverse Units Modulo `9` and `15` (`qou-b5h9`).**
For each non-self-inverse unit `a ∈ [2, 4, 5, 7]` modulo `9`, `(a * fermatCandidate a 9) % 9 ≠ 1`,
and at `N = 15` (`a = 2`), `fermatCandidate 2 15 = 2` so `(2 * fermatCandidate 2 15) % 15 = 4 ≠ 1`,
whereas the true extended-Euclid inverses `[1, 5, 7, 2, 4, 8]` modulo `9` satisfy
`(a * a_inv) % 9 = 1`. -/
theorem fermat_fails_on_non_pm_one_units_mod_nine_and_fifteen :
    ([2, 4, 5, 7].all (fun a => (a * fermatCandidate a 9) % 9 != 1) = true) ∧
    fermatCandidate 2 15 = 2 ∧
    (2 * fermatCandidate 2 15) % 15 = 4 ∧
    (List.zipWith (fun a inv => (a * inv) % 9) [1, 2, 4, 5, 7, 8] [1, 5, 7, 2, 4, 8] =
      [1, 1, 1, 1, 1, 1]) := by
  decide

/-- **Self-Inverse Property of the Boundary Unit `N - 1` (`qou-b5h9`).**
For every integer modulus `N ≥ 2`, `(N - 1) * (N - 1) = N * (N - 2) + 1`, and for the
composite odd moduli `N = 9` and `N = 15`, `fermatCandidate (N - 1) N = N - 1` coincides
with the true multiplicative inverse `N - 1`. -/
theorem boundary_unit_self_inverse_identity (N : Int) :
    (N - 1) * (N - 1) = N * (N - 2) + 1 ∧
    fermatCandidate 8 9 = 8 ∧
    (8 * 8) % 9 = 1 ∧
    fermatCandidate 14 15 = 14 ∧
    (14 * 14) % 15 = 1 := by
  refine ⟨?_, by decide, by decide, by decide, by decide⟩
  calc
    (N - 1) * (N - 1) = (N - 1) * N - (N - 1) * 1 := Int.mul_sub (N - 1) N 1
    _ = (N * N - 1 * N) - (N - 1) := by rw [Int.sub_mul, Int.mul_one]
    _ = (N * N - N * 2) + 1 := by omega
    _ = N * (N - 2) + 1 := by rw [← Int.mul_sub]

/-! ## 2. `5₂ = K(7,3)` Boundary Slope Mirror Involution and `A`-Polynomial Reciprocity (`qou-lrvc`) -/

/-- Normal boundary slopes of the derived Farey-word `RL` triangulation of `K(7, 3)` (`qou-lrvc`). -/
def derivedSlopes52 : List Int := [-10, -4, 0]

/-- Normal boundary slopes of SnapPy `Manifold('5_2')` (`m015 = K3_2`) and Dunfield `K(3/7)` (`qou-lrvc`). -/
def snappySlopes52 : List Int := [0, 4, 10]

/-- Mirror map `s ↦ -s` on a list of boundary slopes. -/
def mirrorSlopes (S : List Int) : List Int := S.map (fun s => -s)

/-- Sum of absolute boundary slopes `Σ |sᵢ|` (a mirror-invariant topological quantity). -/
def absSlopeSum : List Int → Nat
  | [] => 0
  | s :: t => Int.natAbs s + absSlopeSum t

/-- **Derived `K(7, 3)` vs SnapPy/Dunfield `5₂` Boundary Slope Mirror Equivalence (`qou-lrvc`).**
Negating and reversing the derived slope list `[-10, -4, 0]` reproduces the SnapPy /
Dunfield slope list `[0, 4, 10]` exactly, and both chirality frames share the same
absolute slope sum `|-10| + |-4| + |0| = 14` (matching the `M¹⁴` degree of `A_{5₂}`). -/
theorem fivetwo_boundary_slopes_mirror_equivalence :
    (mirrorSlopes derivedSlopes52).reverse = snappySlopes52 ∧
    absSlopeSum derivedSlopes52 = 14 ∧
    absSlopeSum snappySlopes52 = 14 ∧
    derivedSlopes52 ≠ snappySlopes52 := by
  decide

/-- The four `L`-coefficients `[c_3(M), c_2(M), c_1(M), c_0(M)]` of the derived `5₂`
`A`-polynomial `A_{5₂}(L, M) = c_3(M) L³ + c_2(M) L² + c_1(M) L + c_0(M)` evaluated at
an integer `M`-power argument `m = M²` (since all exponents of `M` in `A_{5₂}` are even:
`M¹⁰ - M⁸ + 2M⁴ + 2M² - 1 = m⁵ - m⁴ + 2m² + 2m - 1`,
`-M¹⁴ + 2M¹² + 2M¹⁰ - M⁶ + M⁴ = -m⁷ + 2m⁶ + 2m⁵ - m³ + m²`, and `M¹⁴ = m⁷`). -/
def aPoly52CoeffsAtMSq (m : Int) : List Int :=
  [ 1,
    m ^ 5 - m ^ 4 + 2 * (m ^ 2) + 2 * m - 1,
    -(m ^ 7) + 2 * (m ^ 6) + 2 * (m ^ 5) - (m ^ 3) + (m ^ 2),
    m ^ 7 ]

/-- **`A_{5₂}(L, M)` Specialization at `M = ±1` and Reciprocal Symmetry (`qou-lrvc`).**
At `m = M² = 1`, the `L`-coefficient list of `A_{5₂}(L, M)` specializes to `[1, 3, 3, 1]`
(the binomial coefficients of `(L + 1)³`, which are palindromic and sum to `8`), while
at `m = M² = 2` (`[1, 27, 60, 128]`), its reversal `[128, 60, 27, 1]` (corresponding to
`L ↦ L⁻¹`, i.e. Culler's printed orientation vs the derived frame) is distinct, pinning
the `L ↦ L⁻¹` orientation convention. -/
theorem apoly_52_specialization_and_reciprocal_asymmetry :
    aPoly52CoeffsAtMSq 1 = [1, 3, 3, 1] ∧
    (aPoly52CoeffsAtMSq 1).reverse = aPoly52CoeffsAtMSq 1 ∧
    (aPoly52CoeffsAtMSq 1).foldl (· + ·) 0 = 8 ∧
    aPoly52CoeffsAtMSq 2 = [1, 27, 60, 128] ∧
    (aPoly52CoeffsAtMSq 2).reverse = [128, 60, 27, 1] ∧
    (aPoly52CoeffsAtMSq 2).reverse ≠ aPoly52CoeffsAtMSq 2 := by
  decide

end QOU.QBeta.CompositeModulusFermatAndFiveTwoChiralityFrame
