import QOU.MassTheory.DeltaNPMatrixIdentity

/-!
# At `q = 1` the u ↔ d flip makes proton and neutron identical; charges must then be mirror

Working assumption (owner, 2026-11-22): `m_p = m_n` at `q = 1`. This file tests whether it
falls out of upstream structure.

- The flip `u ↔ d` sends the proton weight basis to the neutron one in reverse order, i.e. it is
  the permutation `Π` reversing `Fin 3`. At `q = 1`, `Π A_i(1) Π = B_i(1)` for both generators
  and their inverses (`flip_A₁_one`, …). So every braid word acts on `W_n` exactly as on `W_p`
  after relabelling, and every trace of a word (with any polynomial `F`, hence any `∇ = F(hol)`)
  is equal on n and p at `q = 1` (`trace_word_flip`). At `q ≠ 1` the same `Π` fails (the
  `q − q⁻¹` corner moves); the conjugator there is the non-permutation `P(q)`.
- So `m_p = m_n` at `q = 1` holds for every functional built from the braid action. It can only
  be broken by an inserted operator that is not flip-covariant.
- Charge-quadratic insertions are flip-covariant exactly when `q_u² = q_d²`
  (`self_charge_equal_iff`, `pair_charge_equal_iff`). The Standard Model values (`4/9 ≠ 1/9`)
  break it; a mirror pair `q_d = −q_u` (the corpus crossing charge) keeps it.
-/

namespace QOU.MassTheory.QOneFlipSymmetry

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

variable {R : Type*} [Field R]

/-- The flip `u ↔ d` as a matrix: reversal of `Fin 3`. -/
def Flip : Matrix (Fin 3) (Fin 3) R := !![0, 0, 1; 0, 1, 0; 1, 0, 0]

theorem Flip_sq : (Flip : Matrix (Fin 3) (Fin 3) R) * Flip = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [Flip, Matrix.mul_apply, Fin.sum_univ_three]

theorem flip_A₁_one : Flip * A₁ (1 : R) * Flip = B₁ 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Flip, A₁, B₁, Matrix.mul_apply, Fin.sum_univ_three]

theorem flip_A₂_one : Flip * A₂ (1 : R) * Flip = B₂ 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Flip, A₂, B₂, Matrix.mul_apply, Fin.sum_univ_three]

theorem flip_A₁Inv_one : Flip * A₁Inv (1 : R) * Flip = B₁Inv 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Flip, A₁Inv, B₁Inv, Matrix.mul_apply, Fin.sum_univ_three]

theorem flip_A₂Inv_one : Flip * A₂Inv (1 : R) * Flip = B₂Inv 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Flip, A₂Inv, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three]

/-- At `q = 2` the flip does NOT intertwine `σ₀` (characteristic ≠ 2, 3 suffices; here `CharZero`). -/
theorem flip_A₁_two_ne [CharZero R] : Flip * A₁ (2 : R) * Flip ≠ B₁ 2 := by
  intro h
  have := congrFun (congrFun h 0) 0
  simp [Flip, A₁, B₁, Matrix.mul_apply, Fin.sum_univ_three] at this
  norm_num at this

/-- Conjugation by the involution `Flip` is multiplicative, so it carries any product of
generators on `W_p` to the same product on `W_n`. -/
theorem flip_mul (X Y : Matrix (Fin 3) (Fin 3) R) :
    Flip * (X * Y) * Flip = (Flip * X * Flip) * (Flip * Y * Flip) := by
  have h := (Flip_sq : (Flip : Matrix (Fin 3) (Fin 3) R) * Flip = 1)
  calc Flip * (X * Y) * Flip = Flip * X * (Flip * Flip) * Y * Flip := by rw [h]; simp [Matrix.mul_assoc]
    _ = (Flip * X * Flip) * (Flip * Y * Flip) := by simp [Matrix.mul_assoc]

/-- Traces are flip-invariant: `tr (Π X Π) = tr X`. -/
theorem trace_flip (X : Matrix (Fin 3) (Fin 3) R) : trace (Flip * X * Flip) = trace X := by
  rw [Matrix.trace_mul_comm, ← Matrix.mul_assoc, Flip_sq, Matrix.one_mul]

/-- So for any word `w_p` on `W_p` whose flip is the corresponding neutron word `w_n`
(`Π w_p Π = w_n`), the traces agree at `q = 1`. -/
theorem trace_word_flip (wp wn : Matrix (Fin 3) (Fin 3) R) (h : Flip * wp * Flip = wn) :
    trace wn = trace wp := by
  rw [← h, trace_flip]

/-- The Borromean holonomy at `q = 1`: the flip carries `V_p(1)` to `V_n(1)`. -/
theorem flip_V_one :
    Flip * QOU.MassTheory.HolonomyConnectionSplit.Vp (1 : R) * Flip =
      QOU.MassTheory.HolonomyConnectionSplit.Vn 1 := by
  unfold QOU.MassTheory.HolonomyConnectionSplit.Vp QOU.MassTheory.HolonomyConnectionSplit.Vn
  rw [flip_mul, flip_A₁_one, flip_A₂Inv_one]

/-- Self charge `Σ qᵢ²`: proton `2u²+d²`, neutron `u²+2d²`; equal iff `u² = d²`. -/
theorem self_charge_equal_iff (u d : R) :
    2 * u ^ 2 + d ^ 2 = u ^ 2 + 2 * d ^ 2 ↔ u ^ 2 = d ^ 2 := by
  constructor <;> intro h <;> linear_combination h

/-- Pair charge `Σ_{i<j} qᵢqⱼ`: proton `u²+2ud`, neutron `2ud+d²`; equal iff `u² = d²`. -/
theorem pair_charge_equal_iff (u d : R) :
    u ^ 2 + 2 * u * d = 2 * u * d + d ^ 2 ↔ u ^ 2 = d ^ 2 := by
  constructor <;> intro h <;> linear_combination h

/-- The Standard Model values break it. -/
theorem sm_charges_not_mirror [CharZero R] : (2 / 3 : R) ^ 2 ≠ (-1 / 3) ^ 2 := by norm_num

end QOU.MassTheory.QOneFlipSymmetry
