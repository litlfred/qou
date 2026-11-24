import Mathlib.Data.Matrix.Mul
import Mathlib.Data.Fintype.Prod
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination

/-!
# A U(1) charge phase on the strands breaks Yang–Baxter for the Hecke braiding

Audit `docs/audits/2026-11-21-neutron-heavier-sign.md` §31. Put the most general strand-symmetric,
weight-diagonal phase on the Jimbo braiding of `V = ⟨u, d⟩`:
`Ř' = Ř · diag(a, b, b, c)` on the basis `uu, ud, du, dd`, with
`Ř = [[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]]`, `h = q − q⁻¹`.

`ybe_entry` computes one diagonal entry of `Ř'₁₂Ř'₂₃Ř'₁₂ − Ř'₂₃Ř'₁₂Ř'₂₃` on three strands:
`−b(a − b)(q² − 1)(aq² + b)/q`. So Yang–Baxter forces `a = b` or `a = −b/q²` whenever
`q² ≠ 1` and `b ≠ 0` (`ybe_forces`). The U(1)_em charge line coupling `t^{9QQ'}` with
`Q_u = 2/3`, `Q_d = −1/3` has `a = t⁴`, `b = t⁻²`; over the positive reals with `q > 1` this forces
`t = 1`, i.e. zero coupling (`charge_phase_trivial`).

The obstruction is the Hecke term `h`: it maps `du` to itself rather than swapping, which a braiding
between two different U(1) objects cannot do. So a continuous Coulomb coupling cannot sit on the
strands while the Hecke relation holds. No empirical input.
-/

namespace QOU.QBeta.ChargePhaseYangBaxterObstruction

open Matrix

variable {K : Type*} [Field K]

/-- Two-site braiding `Ř · diag(a,b,b,c)`, entries `(out₁ out₂) (in₁ in₂)`; `0 = u`, `1 = d`. -/
def Rd (q a b c : K) : Fin 2 → Fin 2 → Fin 2 → Fin 2 → K
  | 0, 0, 0, 0 => q * a
  | 0, 1, 1, 0 => b
  | 1, 0, 0, 1 => b
  | 1, 0, 1, 0 => (q - q⁻¹) * b
  | 1, 1, 1, 1 => q * c
  | _, _, _, _ => 0

/-- Three-strand index. -/
abbrev ι := Fin 2 × Fin 2 × Fin 2

/-- `Ř'` on strands 1,2. -/
def R12 (q a b c : K) : Matrix ι ι K := fun i j =>
  Rd q a b c i.1 i.2.1 j.1 j.2.1 * (if i.2.2 = j.2.2 then 1 else 0)

/-- `Ř'` on strands 2,3. -/
def R23 (q a b c : K) : Matrix ι ι K := fun i j =>
  (if i.1 = j.1 then 1 else 0) * Rd q a b c i.2.1 i.2.2 j.2.1 j.2.2

/-- The `(duu, duu)` entry of the Yang–Baxter defect. -/
theorem ybe_entry (q a b c : K) (hq : q ≠ 0) :
    (R12 q a b c * R23 q a b c * R12 q a b c - R23 q a b c * R12 q a b c * R23 q a b c)
      (1, 0, 0) (1, 0, 0) = -b * (a - b) * (q ^ 2 - 1) * (a * q ^ 2 + b) / q := by
  simp only [Matrix.sub_apply, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
    R12, R23, Rd]
  simp
  field_simp
  ring

/-- Yang–Baxter forces `a = b` or `a·q² = −b`. -/
theorem ybe_forces (q a b c : K) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hb : b ≠ 0)
    (hybe : R12 q a b c * R23 q a b c * R12 q a b c = R23 q a b c * R12 q a b c * R23 q a b c) :
    a = b ∨ a * q ^ 2 = -b := by
  have h := ybe_entry q a b c hq
  rw [hybe, sub_self] at h
  have h0 : (a - b) * (a * q ^ 2 + b) = 0 := by
    have hq2' : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hq2
    have : -b * (a - b) * (q ^ 2 - 1) * (a * q ^ 2 + b) / q = 0 := by
      simpa using h.symm
    have h1 : -b * (a - b) * (q ^ 2 - 1) * (a * q ^ 2 + b) = 0 := by
      rcases div_eq_zero_iff.mp this with h | h
      · exact h
      · exact absurd h hq
    have : (-b * (q ^ 2 - 1)) * ((a - b) * (a * q ^ 2 + b)) = 0 := by linear_combination h1
    rcases mul_eq_zero.mp this with h | h
    · exact absurd h (mul_ne_zero (neg_ne_zero.mpr hb) hq2')
    · exact h
  rcases mul_eq_zero.mp h0 with h | h
  · exact Or.inl (sub_eq_zero.mp h)
  · exact Or.inr (eq_neg_of_add_eq_zero_left h)

/-- Archimedean specialisation: the U(1)_em phase `a = t⁴`, `b = t⁻²`, `c = t` on the Hecke
braiding at `q > 1` satisfies Yang–Baxter only at `t = 1`, i.e. zero charge coupling. -/
theorem charge_phase_trivial (q t : ℝ) (hq : 1 < q) (ht : 0 < t)
    (hybe : R12 q (t ^ 4) (t ^ 2)⁻¹ t * R23 q (t ^ 4) (t ^ 2)⁻¹ t * R12 q (t ^ 4) (t ^ 2)⁻¹ t
      = R23 q (t ^ 4) (t ^ 2)⁻¹ t * R12 q (t ^ 4) (t ^ 2)⁻¹ t * R23 q (t ^ 4) (t ^ 2)⁻¹ t) :
    t = 1 := by
  have hq0 : q ≠ 0 := by positivity
  have hq2 : q ^ 2 ≠ 1 := by nlinarith
  have hb : (t ^ 2)⁻¹ ≠ 0 := by positivity
  rcases ybe_forces q _ _ _ hq0 hq2 hb hybe with h | h
  · have ht6 : t ^ 6 = 1 := by
      have h2 : t ^ 2 ≠ 0 := by positivity
      field_simp at h
      linear_combination h
    have : (t - 1) * (t ^ 5 + t ^ 4 + t ^ 3 + t ^ 2 + t + 1) = 0 := by linear_combination ht6
    rcases mul_eq_zero.mp this with h' | h'
    · linarith
    · nlinarith [pow_pos ht 5, pow_pos ht 4, pow_pos ht 3, pow_pos ht 2]
  · have : 0 < t ^ 4 * q ^ 2 := by positivity
    have : 0 < (t ^ 2)⁻¹ := by positivity
    linarith

end QOU.QBeta.ChargePhaseYangBaxterObstruction
