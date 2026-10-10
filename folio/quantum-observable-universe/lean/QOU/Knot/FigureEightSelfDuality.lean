/-
  Self-duality kills the imaginary face — the keystone CS(4_1)=0, formalized
  over a generic commutative ring with a bar-involution σ (NOT ℂ; §7c).

  Context (vpug / keystone). The QOU complex volume splits a substrate element
  V into a bar-EVEN (cosh / Vol / binding / Re) part and a bar-ODD (sinh /
  Chern–Simons / Q_β / Im) part — the archimedean (ℂ) instance being
  Re/Im under complex conjugation. The figure-eight 4_1 (the Higgs) is
  AMPHICHIRAL (self-dual: 4_1 = mirror 4_1), so its colored Jones is σ-fixed
  (J_N(q)=J_N(q^-1), verified exactly in figure_eight_aj_operator.py). The
  consequence — Im V(4_1) = CS(4_1) = 0, so the Higgs knot contributes ONLY the
  real (mass) face m_μ/m_e = Vol(4_1)/ℏ_q² — is here PROVED algebraically over
  any (R, σ): a σ-fixed element has zero bar-odd part.

  This is the (R,σ)-generalization the literature's ℂ-results need (owner's
  "not just ℂ"): bar-involution σ replaces complex conjugation; the elementary
  self-duality argument is ring algebra. The hard saddle asymptotics
  (Vol(4_1) limit) stay conditional — see QOU/Knot/FigureEightVolume.lean.

  Complements the bar-parity descent in
  mass-endomorphism/binding-qbeta-complex-volume.lean (invol_descent); the NEW
  content here is the self-dual ⇒ Im-vanishes theorem.

  -- Ref: [kashaev1997] https://doi.org/10.1007/BF01239527
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Tactic

namespace QOU.Knot.SelfDuality

variable {R : Type*} [CommRing R] (σ : R →+* R)

/-- bar-EVEN part: `V + σV` (cosh / Vol / binding / Re face). -/
def barEven (V : R) : R := V + σ V

/-- bar-ODD part: `V − σV` (sinh / Chern–Simons / Q_β / Im face). -/
def barOdd (V : R) : R := V - σ V

/-- The two parities reconstruct `2V`. -/
theorem barEven_add_barOdd (V : R) : barEven σ V + barOdd σ V = 2 * V := by
  simp only [barEven, barOdd]; ring

/-- **Self-duality kills the imaginary face.** A σ-fixed (amphichiral /
    self-dual) element — the figure-eight 4_1 / Higgs — has zero bar-ODD part.
    This is CS(4_1) = 0 = Im V(4_1), proved over any `(R, σ)`. -/
theorem selfDual_barOdd_zero (V : R) (hV : σ V = V) : barOdd σ V = 0 := by
  simp only [barOdd, hV, sub_self]

/-- For a self-dual element only the bar-EVEN (Vol / mass) face survives:
    `barEven σ V = 2V`. -/
theorem selfDual_barEven_two (V : R) (hV : σ V = V) : barEven σ V = 2 * V := by
  simp only [barEven, hV]; ring

/-- **Recurrence descent (the c_k ladder).** A three-term recurrence
    `Vp = c·Vk − Vm` with a σ-fixed (bar-even) multiplier `c` descends to BOTH
    parity recurrences at once — the algebraic engine of the c_k ladder
    (bar-even binding `c₂=−8` and bar-odd Q_β `c₂=−1` from one relation). -/
theorem recurrence_descent {Vp Vk Vm c : R} (hc : σ c = c)
    (h : Vp = c * Vk - Vm) :
    barEven σ Vp = c * barEven σ Vk - barEven σ Vm ∧
    barOdd σ Vp = c * barOdd σ Vk - barOdd σ Vm := by
  have hσ : σ Vp = c * σ Vk - σ Vm := by
    rw [h, map_sub, map_mul, hc]
  refine ⟨?_, ?_⟩
  · simp only [barEven]; rw [hσ, h]; ring
  · simp only [barOdd]; rw [hσ, h]; ring

/-- **Keystone corollary.** For the self-dual Higgs knot, the complex volume is
    purely real: its bar-odd (CS / Q_β / Im) face is 0 and its bar-even
    (Vol / mass / Re) face is `2V`. Hence `Q_β` cannot be the figure-eight's own
    imaginary face — it must live in the many-body binding defect (see the
    CAL-123 reanalysis audit). -/
theorem higgs_complex_volume_real (V : R) (hSelfDual : σ V = V) :
    barOdd σ V = 0 ∧ barEven σ V = 2 * V :=
  ⟨selfDual_barOdd_zero σ V hSelfDual, selfDual_barEven_two σ V hSelfDual⟩

end QOU.Knot.SelfDuality
