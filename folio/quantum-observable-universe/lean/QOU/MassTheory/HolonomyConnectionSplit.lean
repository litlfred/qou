import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

/-!
# The holonomy connection on the nucleon weight spaces

Setting of `NucleonWeightSpaceTraces` / `NucleonWeightSpaceTwoTerm`: `A₁, A₂` (and inverses) are
`σ₀, σ₁` on the proton-type weight space `(2,1)`, `B₁, B₂` on the neutron-type `(1,2)`, and `P q`
intertwines them. The nucleon holonomy is `B₃ = (σ₀σ₁⁻¹)³`, here `Vp q ^ 3` and `Vn q ^ 3`.

* `intertwine_V3` / `Vn3_conj`: `P Vp³ = Vn³ P`, so `Vn³ = P Vp³ P⁻¹`: the two holonomies are
  similar and have the same spectrum.
* `eigen_transfer`: an eigenvector `ψ` of `Vp³` with eigenvalue `λ` gives the eigenvector `P ψ`
  of `Vn³` with the same `λ`. So under the identification `∇ = hol − 1` (not a corpus ruling,
  see `LITERATURE-COMPARISON.md` §21), `μ = λ − 1` is the same for proton and neutron, and the
  Cartan weights `q` / `q⁻¹` with the horizontal `q⁻¹` give the neutron exactly `q⁻²` times the
  proton (`TwoTermMatterOwnSector`).
* `trace_Vp3_sub_three`: the sum of `μ` over the weight space, `tr(Vp³) − 3`, equals
  `−(q² − 1)⁴(q⁴ + q² + 1)/q⁶`.
* `two_add_c1_eq` / `c1_sub_two_eq`: with `c₁` the middle coefficient of the non-trivial
  quadratic factor, `2 + c₁ = h⁴ [3]_q` (`h = q − q⁻¹`, `[3]_q = q² + 1 + q⁻²`), which is
  `|μ|²` when the pair is on the unit circle, and `c₁ − 2 = (q⁴ + 1)²(q² − q − 1)(q² + q − 1)/q⁶`,
  which vanishes at the golden ratio and its inverse: the boundary between the elliptic range
  (eigenvalues `e^{±iθ}`) and the loxodromic one.

No numerical value enters.
-/

namespace QOU.MassTheory.HolonomyConnectionSplit

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

variable {R : Type*} [Field R]

/-- `σ₀σ₁⁻¹` on the proton-type weight space. -/
def Vp (q : R) : Matrix (Fin 3) (Fin 3) R := A₁ q * A₂Inv q

/-- `σ₀σ₁⁻¹` on the neutron-type weight space. -/
def Vn (q : R) : Matrix (Fin 3) (Fin 3) R := B₁ q * B₂Inv q

theorem intertwine_V (q : R) (hq : q ≠ 0) : P q * Vp q = Vn q * P q := by
  unfold Vp Vn
  rw [← mul_assoc, intertwine₁ q hq, mul_assoc, intertwine₂Inv q hq, mul_assoc]

theorem intertwine_Vpow (q : R) (hq : q ≠ 0) (n : ℕ) : P q * Vp q ^ n = Vn q ^ n * P q := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, pow_succ, ← mul_assoc, ih, mul_assoc, intertwine_V q hq, ← mul_assoc]

theorem intertwine_V3 (q : R) (hq : q ≠ 0) : P q * Vp q ^ 3 = Vn q ^ 3 * P q :=
  intertwine_Vpow q hq 3

/-- The neutron holonomy is conjugate to the proton holonomy. -/
theorem Vn3_conj (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    Vn q ^ 3 = P q * Vp q ^ 3 * (P q)⁻¹ := by
  have hdet : IsUnit (P q).det := by
    rw [det_P q hq]
    exact isUnit_iff_ne_zero.mpr (div_ne_zero (neg_ne_zero.mpr hq2) (pow_ne_zero 4 hq))
  rw [intertwine_V3 q hq, mul_assoc, Matrix.mul_nonsing_inv _ hdet, mul_one]

/-- Eigenvectors transfer from proton to neutron with the same eigenvalue. -/
theorem eigen_transfer (q : R) (hq : q ≠ 0) (ψ : Matrix (Fin 3) (Fin 1) R) (lam : R)
    (h : Vp q ^ 3 * ψ = lam • ψ) : Vn q ^ 3 * (P q * ψ) = lam • (P q * ψ) := by
  rw [← Matrix.mul_assoc, ← intertwine_V3 q hq, Matrix.mul_assoc, h, Matrix.mul_smul]

/-- Sum of `μ = λ − 1` over the proton weight space. -/
theorem trace_Vp3_sub_three (q : R) (hq : q ≠ 0) :
    trace (Vp q ^ 3) - 3 = -((q ^ 2 - 1) ^ 4 * (q ^ 4 + q ^ 2 + 1)) / q ^ 6 := by
  simp only [Vp, A₁, A₂Inv, pow_succ, pow_zero, one_mul, Matrix.trace, Matrix.diag,
    Fin.sum_univ_three, Matrix.mul_apply, Matrix.of_apply, Matrix.cons_val',
    Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.head_cons,
    Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.tail_cons, Matrix.head_fin_const]
  field_simp
  ring

/-- `2 + c₁ = h⁴ [3]_q`. -/
theorem two_add_c1_eq (q : R) (hq : q ≠ 0) :
    2 + (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 4 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6 =
      (q - q⁻¹) ^ 4 * (q ^ 2 + 1 + q⁻¹ ^ 2) := by
  field_simp
  ring

/-- `c₁ − 2` factors through `q² ± q − 1`. -/
theorem c1_sub_two_eq (q : R) (hq : q ≠ 0) :
    (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 4 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6 - 2 =
      (q ^ 4 + 1) ^ 2 * (q ^ 2 - q - 1) * (q ^ 2 + q - 1) / q ^ 6 := by
  field_simp
  ring

end QOU.MassTheory.HolonomyConnectionSplit
