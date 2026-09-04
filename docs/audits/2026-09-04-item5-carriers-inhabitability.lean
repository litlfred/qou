import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-! Replicate-and-inhabit test (the `qou-7yj0` method) applied to the classes
    behind this session's confirmed §3b-cond item-5 violations. -/

-- (1) GBResidueSpectralSum: chooses mass/descended/residue itself.
class GBRes (R : Type*) [CommRing R] [LinearOrder R] where
  descended : R
  levelBound : ℕ
  residue : Fin levelBound → R
  mass : R
  spectral_decomposition : mass = |descended| + ∑ ℓ : Fin levelBound, residue ℓ

instance : GBRes ℤ where
  descended := 0; levelBound := 0; residue := fun i => i.elim0; mass := 0
  spectral_decomposition := by simp

-- (2) MarkovTraceRecursiveReducerContext: chooses Braid/reduce/correct itself.
class MTRRC where
  Braid : Type
  reduce : Braid → Braid
  terminates : Braid → Prop
  correct : Braid → Braid → Prop
  disjointProduct : Braid → Braid → Braid
  symMul : Braid → Braid → Braid
  claim : ∀ β : Braid, terminates β ∧ correct β (reduce β) ∧
    (∀ α : Braid, reduce (disjointProduct α β) = symMul (reduce α) (reduce β))

instance : MTRRC where
  Braid := Unit; reduce := id; terminates := fun _ => True; correct := fun _ _ => True
  disjointProduct := fun _ _ => (); symMul := fun _ _ => ()
  claim := fun _ => ⟨trivial, trivial, fun _ => rfl⟩

-- (3) NEGATIVE CONTROL — BrunnianDecoupling takes its subject as PARAMETERS,
--     which is the parametrised form `qou-7yj0` recommends.  If the method is
--     sound this must NOT be inhabitable at arbitrary values.
structure BrunnianDecoupling (k : ℕ) (component_factor composite_factor : ℝ) : Prop where
  decouples : composite_factor = component_factor ^ k

example : ¬ BrunnianDecoupling 2 (3 : ℝ) 5 := by
  rintro ⟨h⟩; norm_num at h
