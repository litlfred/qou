import QOU.Nuclear.BraneTowerExponentialDecayAndCPTClosure

/-!
# `prop:cpt-d6-d7-d8-closure` — CPT Markov-Trace Closure

Companion Lean module for `prop:cpt-d6-d7-d8-closure`, retaining the parametric `CPTClosure`
predicate and componentwise composition theorem `cptClosure_of_components` over generic
commutative rings `R`, together with an unconditional `CPTClosure` realization on
flavor-decorated 3-strand closed braids via `QOU.Nuclear.BraneTowerExponentialDecayAndCPTClosure`.
-/

namespace QOU.ParticleInteractions

open QOU.Nuclear.BraneTowerExponentialDecayAndCPTClosure

-- Ref: [jones1987] V. Jones, Hecke algebra representations of braid groups
/-- A symmetry action `f : B → B` preserves the trace functional `tr : B → R`. -/
def PreservesMarkovTrace {B R : Type*} (tr : B → R) (f : B → B) : Prop :=
  ∀ b : B, tr (f b) = tr b

-- Ref: [leitner2026] prop:cpt-d6-d7-d8-closure
-- Ref: [wigner1937], [jones1987], [kassel1995]
/-- Trace preservation predicate for a composite CPT action. -/
def cpt_closure {B R : Type*} (markovTrace : B → R) (cptComposite : B → B) : Prop :=
  PreservesMarkovTrace markovTrace cptComposite

-- Ref: [leitner2026] prop:cpt-d6-d7-d8-closure
-- Ref: [wigner1937], [jones1987], [kassel1995]
/-- Parametric typeclass packaging trace invariance of `cptComposite` under `markovTrace`. -/
class CPTClosure (R : Type*) [CommRing R] (B : Type*)
    (markovTrace : B → R) (cptComposite : B → B) : Prop where
  cpt_trace_preserved : cpt_closure markovTrace cptComposite

/-- Componentwise closure: if `C`, `P`, and `T` individually preserve `tr`, then `C ∘ P ∘ T`
preserves `tr`. -/
theorem cptClosure_of_components {B R : Type*} (tr : B → R) (C P T : B → B)
    (hC : PreservesMarkovTrace tr C)
    (hP : PreservesMarkovTrace tr P)
    (hT : PreservesMarkovTrace tr T) :
    cpt_closure tr (C ∘ P ∘ T) := by
  intro b
  show tr (C (P (T b))) = tr b
  rw [hC (P (T b)), hP (T b), hT b]

/-- Unconditional realization of `CPTClosure` on `FlavorBraid3` equipped with the bar-symmetrized
`H_3(q)` Markov trace `tauMSymH3 W z h` over any commutative ring `R` and conjugation-symmetric
color-sheet weight `W`. -/
theorem cptClosure_flavorBraid3_barSym {R : Type*} [CommRing R]
    (W : (Fin 3 → QuarkFlavor) → R) (hW : ∀ fl, W (QuarkFlavor.conj ∘ fl) = W fl)
    (z h : R) :
    CPTClosure R FlavorBraid3 (tauMSymH3 W z h) actionCPT :=
  ⟨fun b => (cpt_preserves_barSym_markov_trace_H3 W hW z h b).2.2.2⟩

end QOU.ParticleInteractions
