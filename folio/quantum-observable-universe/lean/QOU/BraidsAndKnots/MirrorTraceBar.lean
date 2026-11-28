import QOU.BraidsAndKnots.NucleonIsospinExclusions

/-!
# Bar is the mirror on the nucleon weight spaces

Setting as in `NucleonWeightSpaceTraces` and `NucleonIsospinExclusions`: level-2 Jimbo braiding on
`(C²)^{⊗3}`, `h = q - q⁻¹`, proton-type weight space `(2,1)` and neutron-type weight space `(1,2)`.

The bar involution `q ↦ q⁻¹` is semilinear, so it is not an operator in the commutant of the total
lowering operator `F₃`, and `commutant_trace_eq` says nothing about it directly. Its linear form is
conjugation by the `u ↔ d` swap `S^{⊗3}`, which on the weight spaces is the order-reversing
permutation `Jrev` (it sends `e₁e₁e₂, e₁e₂e₁, e₂e₁e₁` to `e₂e₂e₁, e₂e₁e₂, e₁e₂e₂`). The letter-level
fact is `Jrev · Aᵢ(q⁻¹) · Jrev = Bᵢ(q) - h`, the inverse letter: bar of a braid generator is the
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
def Jrev : Matrix (Fin 3) (Fin 3) R := !![0, 0, 1; 0, 1, 0; 1, 0, 0]

theorem J_mul_J : (Jrev : Matrix (Fin 3) (Fin 3) R) * Jrev = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Jrev, Matrix.mul_apply, Fin.sum_univ_three]

/-- Mirror of a letter: same generator, opposite sign. -/
def mirror (l : Letter) : Letter := (l.1, !l.2)

/-- `Jrev` conjugation turns a product into the product of the conjugates. -/
theorem J_conj_mul (X Y : Matrix (Fin 3) (Fin 3) R) :
    Jrev * (X * Y) * Jrev = (Jrev * X * Jrev) * (Jrev * Y * Jrev) := by
  simp only [mul_assoc]
  rw [← mul_assoc Jrev Jrev (Y * Jrev), J_mul_J, one_mul]

theorem conj_A₁ (q : R) : Jrev * A₁ q⁻¹ * Jrev = NucleonIsospinExclusions.inv q (B₁ q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Jrev, A₁, B₁, NucleonIsospinExclusions.inv, Matrix.mul_apply, Fin.sum_univ_three]

theorem conj_A₂ (q : R) : Jrev * A₂ q⁻¹ * Jrev = NucleonIsospinExclusions.inv q (B₂ q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Jrev, A₂, B₂, NucleonIsospinExclusions.inv, Matrix.mul_apply, Fin.sum_univ_three]

theorem conj_B₁ (q : R) : Jrev * B₁ q⁻¹ * Jrev = NucleonIsospinExclusions.inv q (A₁ q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Jrev, A₁, B₁, NucleonIsospinExclusions.inv, Matrix.mul_apply, Fin.sum_univ_three]

theorem conj_B₂ (q : R) : Jrev * B₂ q⁻¹ * Jrev = NucleonIsospinExclusions.inv q (A₂ q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Jrev, A₂, B₂, NucleonIsospinExclusions.inv, Matrix.mul_apply, Fin.sum_univ_three]

/-- If `Jrev X(q⁻¹) Jrev` is the inverse letter `NucleonIsospinExclusions.inv q X'`, then `Jrev · inv_{q⁻¹} X(q⁻¹) · Jrev = X'`. -/
theorem conj_inv_of_conj (q : R) {X X' : Matrix (Fin 3) (Fin 3) R}
    (h : Jrev * X * Jrev = NucleonIsospinExclusions.inv q X') : Jrev * NucleonIsospinExclusions.inv q⁻¹ X * Jrev = X' := by
  have e : Jrev * NucleonIsospinExclusions.inv q⁻¹ X * Jrev = Jrev * X * Jrev + (q - q⁻¹) • (Jrev * Jrev) := by
    simp only [NucleonIsospinExclusions.inv, inv_inv, Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_smul, Matrix.smul_mul,
      Matrix.mul_one]
    rw [sub_eq_add_neg, ← neg_smul, neg_sub]
  rw [e, h, J_mul_J]
  simp [NucleonIsospinExclusions.inv]

/-- Letter level: bar conjugated by `Jrev` is the mirrored letter. -/
theorem conj_letter (q : R) {X Y X' Y' : Matrix (Fin 3) (Fin 3) R}
    (hX : Jrev * X * Jrev = NucleonIsospinExclusions.inv q X') (hY : Jrev * Y * Jrev = NucleonIsospinExclusions.inv q Y') (l : Letter) :
    Jrev * letter q⁻¹ X Y l * Jrev = letter q X' Y' (mirror l) := by
  obtain ⟨g, s⟩ := l
  cases g <;> cases s <;> simp only [letter, mirror, Bool.false_eq_true, if_false, if_true,
    Bool.not_true, Bool.not_false]
  · exact conj_inv_of_conj q hY
  · exact hY
  · exact conj_inv_of_conj q hX
  · exact hX

/-- Word level: `Jrev · β(q⁻¹) · Jrev = β̄(q)`. -/
theorem conj_sword (q : R) {X Y X' Y' : Matrix (Fin 3) (Fin 3) R}
    (hX : Jrev * X * Jrev = NucleonIsospinExclusions.inv q X') (hY : Jrev * Y * Jrev = NucleonIsospinExclusions.inv q Y') (w : List Letter) :
    Jrev * sword q⁻¹ X Y w * Jrev = sword q X' Y' (w.map mirror) := by
  induction w with
  | nil => simp [sword, J_mul_J]
  | cons l w ih =>
    simp only [sword, List.map_cons]
    rw [J_conj_mul, conj_letter q hX hY l, ih]

theorem trace_J_conj (X : Matrix (Fin 3) (Fin 3) R) : trace (Jrev * X * Jrev) = trace X := by
  rw [Matrix.trace_mul_cycle, J_mul_J, one_mul]

/-- **Bar is the mirror on the proton-type trace.** For every signed braid word `β`,
`Tr_p(β)(q⁻¹) = Tr_p(β̄)(q)`. -/
theorem trace_bar_eq_mirror (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Letter) :
    trace (sword q⁻¹ (A₁ q⁻¹) (A₂ q⁻¹) w) = trace (sword q (A₁ q) (A₂ q) (w.map mirror)) := by
  rw [← trace_J_conj, conj_sword q (conj_A₁ q) (conj_A₂ q),
    trace_sword_eq q hq hq2]

/-- **With the pivot, bar exchanges the sectors.** `T_p(β̄)(q) = T_n(β)(q⁻¹)`. -/
theorem Tp_mirror_eq_Tn_bar (q : R) (w : List Letter) :
    Tp q (w.map mirror) = Tn q⁻¹ w := by
  simp only [Tp, Tn, inv_inv]
  rw [← trace_J_conj (sword q⁻¹ (B₁ q⁻¹) (B₂ q⁻¹) w),
    conj_sword q (conj_B₁ q) (conj_B₂ q)]

end QOU.BraidsAndKnots.MirrorTraceBar
