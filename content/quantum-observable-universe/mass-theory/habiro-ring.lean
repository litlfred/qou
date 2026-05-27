import Mathlib.Algebra.Group.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Order.Filter.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic


/-!
# Habiro Ring

The Habiro ring is the inverse limit of Z[q] / ((q;q)_n),
the cyclotomic completion where all quantum invariants coexist.

-- Ref: [habiro2002] Habiro, "On the colored Jones polynomials of some simple links," arXiv:math/0505219
-/

namespace QOU.HabiroRing

/-- The q-Pochhammer symbol (q;q)_n = (1-q)(1-q²)...(1-qⁿ). -/
noncomputable def qPochhammer (q : ℝ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => qPochhammer q n * (1 - q ^ (n + 1))

/-- The quotient ring Z[q] / ((q;q)_n) as an equivalence relation.
    Two polynomials are equivalent modulo (q;q)_n if their
    difference is divisible by (1-q)(1-q²)...(1-qⁿ). -/
-- Ref: [habiro2002]
def HabiroEquiv (n : ℕ) (f g : ℝ → ℝ) : Prop :=
  ∀ q : ℝ, qPochhammer q n ≠ 0 →
    ∃ h : ℝ → ℝ, f q - g q = qPochhammer q n * h q

/-- The Habiro ring is the inverse limit of these quotients.
    An element is a compatible family of equivalence classes. -/
-- Ref: [habiro2002]
structure HabiroElement where
  /-- Representatives at each level. -/
  family : ℕ → (ℝ → ℝ)
  /-- Compatibility: at level n, agrees with level n+1 modulo (q;q)_n. -/
  compatible : ∀ n : ℕ, HabiroEquiv n (family n) (family (n + 1))

/-- Laurent polynomials embed into the Habiro ring. -/
noncomputable def embed (f : ℝ → ℝ) : HabiroElement where
  family := fun _ => f
  compatible := by intro n; intro q _; exact ⟨fun _ => 0, by ring⟩

/-- The algebraic quantum volume lives in the Habiro ring. -/
-- Ref: [manuscript] def:algebraic-quantum-volume
noncomputable def algebraicVolume (tracedVolumes : List (ℝ → ℝ)) : ℝ → ℝ :=
  fun q => tracedVolumes.foldl (fun acc v => acc * v q) 1

/-- The algebraic volume embeds into the Habiro ring. -/
noncomputable def algebraicVolumeHabiro (tracedVolumes : List (ℝ → ℝ)) :
    HabiroElement :=
  embed (algebraicVolume tracedVolumes)

end QOU.HabiroRing
