import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-! Round two of the conjecture-carrier audit: the carriers named in the
    "conditional on" population beyond `BorromeanQuark`.  Each is replicated
    faithfully, with externals stubbed, and handed either a trivial instance
    (self-satisfying) or a refutation (uninhabitable). -/

-- stubs
def confinementLevel (_T : ℕ) : ℕ := 0
def KLRTopDegree (_m : ℕ) : ℕ := 0
noncomputable def binding_energy_bw (_q _me : ℝ) (_Z _N : ℕ) (_fZ _fN : ℝ) : ℝ := 0

namespace C1 -- lean/QOU/BraidKnot/CrystalGraphRealization.lean:45  (= mass-theory/crystal-r-matrix-sub-lemma.lean:60)
class CrystalGraphRealization (R : Type) [CommRing R] (q : R) where
  NormalForm : Type
  CrystalNode : Type
  nodeOf : NormalForm → CrystalNode
  raising : ℕ → CrystalNode → Option CrystalNode
  lowering : ℕ → CrystalNode → Option CrystalNode
  crystal_realises : ∀ (T : NormalForm) (i : ℕ), raising i (nodeOf T) = none
/-- `raising := fun _ _ => none` satisfies "every normal form is a
    highest-weight vector" for free.  The docstring calls this field
    "the conjecture itself ... plays the role of `sorry`"; it does not. -/
instance triv : CrystalGraphRealization ℤ 0 :=
  ⟨PUnit, PUnit, id, fun _ _ => none, fun _ _ => none, fun _ _ => rfl⟩
end C1

namespace C2 -- mass-theory/transfer-matrix-level-independence.lean:120
class CrystalGraphRealization : Prop where
  highest_weight : ∃ raise : ℕ → ℤ, ∀ i : ℕ, raise i = 0
instance triv : CrystalGraphRealization := ⟨⟨fun _ => 0, fun _ => rfl⟩⟩
end C2

namespace C3 -- lean/QOU/BraidKnot/QBetaPerBlockChiClosedForms.lean:1075
          -- (= mass-endomorphism/qbeta-per-block-chi-closed-forms.lean:399, identical)
class CanonicalMarkovWeightsH3 where
  y3 : ℝ → ℝ
  y21 : ℝ → ℝ
  y111 : ℝ → ℝ
  sum_dim_normalised : ∀ q > 0, y3 q + 2 * y21 q + y111 q = 1
instance triv : CanonicalMarkovWeightsH3 :=
  ⟨fun _ => 1, fun _ => 0, fun _ => 0, by intro q _; norm_num⟩
end C3

namespace C4 -- mass-theory/wigner-coefficient-derivation.lean:70
class QIntegerMassFormula : Prop where
  coeffs_are_q_rational :
    ∀ (m_e : ℝ), 0 ≤ m_e → ∀ _c : ℕ, ∃ r : ℝ, 0 ≤ r ∧ ∃ value : ℝ, value = r * m_e
/-- `value` is existentially bound and constrained only by the equation that
    defines it, so the whole field reduces to `True`. -/
instance triv : QIntegerMassFormula :=
  ⟨fun _ _ _ => ⟨0, le_refl 0, 0, by ring⟩⟩
end C4

namespace C5 -- mass-theory/q-integer-mass-formula.lean:150 — the UNRESTRICTED copy
class QIntegerMassFormula where
  f_magic : ℕ → ℝ
  tolerance : ℝ
  tolerance_bound : 0 < tolerance ∧ tolerance ≤ (1 : ℝ) / 100
  /-- NOTE `(B_AME : ℝ)` with NO `[IsAMEValue Z N B_AME]` restriction — the
      sibling copy in `lean/QOU/Interactions/QIntegerMassFormula.lean:178` has
      that instance binder and this one does not. -/
  fits_AME :
    ∀ (q m_e : ℝ) (Z N : ℕ) (B_AME : ℝ),
      ∃ δ : ℝ, |δ| ≤ tolerance ∧
        B_AME = (1 + δ) * binding_energy_bw q m_e Z N (f_magic Z) (f_magic N)

/-- **This carrier is UNINHABITABLE**, and not because of any physics: the
    quantifier ranges over EVERY real `B_AME`, while `{(1+δ)X : |δ| ≤ t}` is a
    bounded interval for the single fixed `X`.  Taking `B_AME = 0` forces
    `X = 0` (since `t ≤ 1/100 < 1` keeps `1 + δ` positive); taking
    `B_AME = 1` then demands `1 = 0`.

    So every `[QIntegerMassFormula]`-conditional theorem in that file is
    vacuously true.  The proof holds for ANY `binding_energy_bw`. -/
theorem not_inhabited : ¬ Nonempty QIntegerMassFormula := by
  rintro ⟨inst⟩
  obtain ⟨ht0, ht1⟩ := inst.tolerance_bound
  obtain ⟨δ₀, hδ₀, h0⟩ := inst.fits_AME 1 1 0 0 0
  obtain ⟨δ₁, hδ₁, h1⟩ := inst.fits_AME 1 1 0 0 1
  set X := binding_energy_bw 1 1 0 0 (inst.f_magic 0) (inst.f_magic 0) with hX
  have hb0 : |δ₀| ≤ (1:ℝ)/100 := le_trans hδ₀ ht1
  have hlo : (0:ℝ) < 1 + δ₀ := by
    have := abs_le.mp hb0
    linarith [this.1]
  have hXz : X = 0 := by
    have : (1 + δ₀) * X = 0 := h0.symm
    rcases mul_eq_zero.mp this with h | h
    · linarith
    · exact h
  rw [hXz, mul_zero] at h1
  exact one_ne_zero h1
end C5

#print axioms C1.triv
#print axioms C2.triv
#print axioms C3.triv
#print axioms C4.triv
#print axioms C5.not_inhabited
