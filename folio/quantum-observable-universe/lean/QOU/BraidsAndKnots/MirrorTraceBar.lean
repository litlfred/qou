import QOU.BraidsAndKnots.NucleonIsospinExclusions

/-!
# Bar is the mirror on the nucleon weight spaces

Setting as in `NucleonWeightSpaceTraces` and `NucleonIsospinExclusions`: level-2 Jimbo braiding on
`(C²)^{⊗3}`, `h = q - q⁻¹`, proton-type weight space `(2,1)` and neutron-type weight space `(1,2)`.

The bar involution `q ↦ q⁻¹` is semilinear, so it is not an operator in the commutant of the total
lowering operator `F₃`, and `commutant_trace_eq` says nothing about it directly. Its linear form is
conjugation by the `u ↔ d` swap `S^{⊗3}`, which on the weight spaces is the order-reversing
permutation `J` (it sends `e₁e₁e₂, e₁e₂e₁, e₂e₁e₁` to `e₂e₂e₁, e₂e₁e₂, e₁e₂e₂`). The letter-level
fact is `J · Aᵢ(q⁻¹) · J = Bᵢ(q) - h`, the inverse letter: bar of a braid generator is the
conjugate of its inverse (`conj_A₁`, `conj_A₂`).

Consequences, for every signed braid word `β` and its mirror `β̄` (every letter inverted):

* `trace_bar_eq_mirror`: `Tr_p(β)(q⁻¹) = Tr_p(β̄)(q)` — on the weight-space trace, **bar is the
  mirror**.
* `Tp_mirror_eq_Tn_bar`: `T_p(β̄)(q) = T_n(β)(q⁻¹)` — with the pivot, bar exchanges the proton and
  neutron sectors while mirroring.

So bar supplies no `u ↔ d` breaker beyond the pivot: the mirror is again a signed word, inside the
`F₃` commutant, where `restrictedTrace_ratio` already applies. This is the Lean form of the
pre-registered probe `qou-crossing-energy/probes/f3-bar/` (bean `qou-078y`, all checks passed,
exact sympy). Scope (a) for the n–p question: it excludes bar, not every non-equivariant datum.

Base ring (§7c): generic `[Field R]`. No numerical value enters.
-/

namespace QOU.BraidsAndKnots.MirrorTraceBar

open Matrix QOU.BraidsAndKnots.NucleonWeightSpaceTraces
  QOU.BraidsAndKnots.NucleonIsospinExclusions

variable {R : Type*} [Field R]

/-- The order-reversing permutation: the `u ↔ d` swap `S^{⊗3}` read between the two weight spaces. -/
def J : Matrix (Fin 3) (Fin 3) R := !![0, 0, 1; 0, 1, 0; 1, 0, 0]

theorem J_mul_J : (J : Matrix (Fin 3) (Fin 3) R) * J = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [J, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply]

/-- Mirror of a letter: same generator, opposite sign. -/
def mirror (l : Letter) : Letter := (l.1, !l.2)

/-- `J` conjugation turns a product into the product of the conjugates. -/
theorem J_conj_mul (X Y : Matrix (Fin 3) (Fin 3) R) :
    J * (X * Y) * J = (J * X * J) * (J * Y * J) := by
  simp only [mul_assoc]
  rw [← mul_assoc J J (Y * J), J_mul_J, one_mul]

theorem conj_A₁ (q : R) (hq : q ≠ 0) : J * A₁ q⁻¹ * J = inv q (B₁ q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [J, A₁, B₁, inv, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;>
    field_simp <;> ring

theorem conj_A₂ (q : R) (hq : q ≠ 0) : J * A₂ q⁻¹ * J = inv q (B₂ q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [J, A₂, B₂, inv, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;>
    field_simp <;> ring

theorem conj_B₁ (q : R) (hq : q ≠ 0) : J * B₁ q⁻¹ * J = inv q (A₁ q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [J, A₁, B₁, inv, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;>
    field_simp <;> ring

theorem conj_B₂ (q : R) (hq : q ≠ 0) : J * B₂ q⁻¹ * J = inv q (A₂ q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [J, A₂, B₂, inv, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;>
    field_simp <;> ring

/-- If `J X(q⁻¹) J` is the inverse letter `inv q X'`, then `J · inv_{q⁻¹} X(q⁻¹) · J = X'`. -/
theorem conj_inv_of_conj (q : R) {X X' : Matrix (Fin 3) (Fin 3) R}
    (h : J * X * J = inv q X') : J * inv q⁻¹ X * J = X' := by
  have e : J * inv q⁻¹ X * J = J * X * J + (q - q⁻¹) • (J * J) := by
    simp only [inv, inv_inv, Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_smul, Matrix.smul_mul,
      Matrix.mul_one]
    rw [sub_eq_add_neg, ← neg_smul, neg_sub]
  rw [e, h, J_mul_J]
  simp [inv]

/-- Letter level: bar conjugated by `J` is the mirrored letter. -/
theorem conj_letter (q : R) {X Y X' Y' : Matrix (Fin 3) (Fin 3) R}
    (hX : J * X * J = inv q X') (hY : J * Y * J = inv q Y') (l : Letter) :
    J * letter q⁻¹ X Y l * J = letter q X' Y' (mirror l) := by
  obtain ⟨g, s⟩ := l
  cases g <;> cases s <;> simp only [letter, mirror, Bool.false_eq_true, if_false, if_true,
    Bool.not_true, Bool.not_false]
  · exact conj_inv_of_conj q hY
  · exact hY
  · exact conj_inv_of_conj q hX
  · exact hX

/-- Word level: `J · β(q⁻¹) · J = β̄(q)`. -/
theorem conj_sword (q : R) {X Y X' Y' : Matrix (Fin 3) (Fin 3) R}
    (hX : J * X * J = inv q X') (hY : J * Y * J = inv q Y') (w : List Letter) :
    J * sword q⁻¹ X Y w * J = sword q X' Y' (w.map mirror) := by
  induction w with
  | nil => simp [sword, J_mul_J]
  | cons l w ih =>
    simp only [sword, List.map_cons]
    rw [J_conj_mul, conj_letter q hX hY l, ih]

theorem trace_J_conj (X : Matrix (Fin 3) (Fin 3) R) : trace (J * X * J) = trace X := by
  rw [Matrix.trace_mul_cycle, J_mul_J, one_mul]

/-- **Bar is the mirror on the proton-type trace.** For every signed braid word `β`,
`Tr_p(β)(q⁻¹) = Tr_p(β̄)(q)`. -/
theorem trace_bar_eq_mirror (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Letter) :
    trace (sword q⁻¹ (A₁ q⁻¹) (A₂ q⁻¹) w) = trace (sword q (A₁ q) (A₂ q) (w.map mirror)) := by
  rw [← trace_J_conj, conj_sword q (conj_A₁ q hq) (conj_A₂ q hq),
    trace_sword_eq q hq hq2]

/-- **With the pivot, bar exchanges the sectors.** `T_p(β̄)(q) = T_n(β)(q⁻¹)`. -/
theorem Tp_mirror_eq_Tn_bar (q : R) (hq : q ≠ 0) (w : List Letter) :
    Tp q (w.map mirror) = Tn q⁻¹ w := by
  simp only [Tp, Tn, inv_inv]
  rw [← trace_J_conj (sword q⁻¹ (B₁ q⁻¹) (B₂ q⁻¹) w),
    conj_sword q (conj_B₁ q hq) (conj_B₂ q hq)]

end QOU.BraidsAndKnots.MirrorTraceBar
