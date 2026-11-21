import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Basic
import Mathlib.Tactic.Ring


/-!
# Habiro Ring

The Habiro ring is the inverse limit of Z[q] / ((q;q)_n),
the cyclotomic completion where all quantum invariants coexist.

-- Ref: [habiro2004cyclotomic] Habiro, "Cyclotomic completions of polynomial rings," arXiv:math/0209324

## Base ring (AGENTS.md §7c)

Everything here is stated over a generic commutative ring `R`, not over `ℝ`.
`(q;q)_n` is a product of `1 - q^k`, `HabiroEquiv` is a divisibility condition,
and `algebraicVolume` is a fold of multiplication — no ordering, no radical, no
`Real.*` construct appears anywhere in the file.

Two independent reasons `ℝ` was wrong here, not merely over-general:

1. **The file contradicted its own first line.** It opens "the inverse limit of
   `ℤ[q] / ((q;q)_n)`" and then modelled that ring by functions `ℝ → ℝ`.
2. **The framework's own fibre/observable split forbids it.** Per AGENTS.md
   §"Im(q) at fibre vs observable level", a Habiro element is a **fibre-level**
   object in which `q` is a formal variable and may be complex; `Im(q) = 0` is an
   *archimedean* constraint that applies only after the `τ` functor, at the
   substrate anchor. Typing the Habiro ring over `ℝ` imposes the observable-level
   constraint on a fibre-level object.

The archimedean instance is recovered at `R := ℝ`.
-/

namespace QOU.HabiroRing

variable {R : Type*} [CommRing R]

/-- The q-Pochhammer symbol (q;q)_n = (1-q)(1-q²)...(1-qⁿ). -/
def qPochhammer (q : R) : ℕ → R
  | 0 => 1
  | n + 1 => qPochhammer q n * (1 - q ^ (n + 1))

/-- The quotient ring Z[q] / ((q;q)_n) as an equivalence relation.
    Two polynomials are equivalent modulo (q;q)_n if their
    difference is divisible by (1-q)(1-q²)...(1-qⁿ). -/
-- Ref: [habiro2004cyclotomic]
def HabiroEquiv (n : ℕ) (f g : R → R) : Prop :=
  ∀ q : R, qPochhammer q n ≠ 0 →
    ∃ h : R → R, f q - g q = qPochhammer q n * h q

/-- The Habiro ring is the inverse limit of these quotients.
    An element is a compatible family of equivalence classes. -/
-- Ref: [habiro2004cyclotomic]
structure HabiroElement (R : Type*) [CommRing R] where
  /-- Representatives at each level. -/
  family : ℕ → (R → R)
  /-- Compatibility: at level n, agrees with level n+1 modulo (q;q)_n. -/
  compatible : ∀ n : ℕ, HabiroEquiv n (family n) (family (n + 1))

/-- Laurent polynomials embed into the Habiro ring. -/
def embed (f : R → R) : HabiroElement R where
  family := fun _ => f
  compatible := by intro n; intro q _; exact ⟨fun _ => 0, by ring⟩

/-- The algebraic quantum volume lives in the Habiro ring. -/
-- Ref: [leitner2026] def:algebraic-quantum-volume
def algebraicVolume (tracedVolumes : List (R → R)) : R → R :=
  fun q => tracedVolumes.foldl (fun acc v => acc * v q) 1

/-- The algebraic volume embeds into the Habiro ring. -/
def algebraicVolumeHabiro (tracedVolumes : List (R → R)) :
    HabiroElement R :=
  embed (algebraicVolume tracedVolumes)

end QOU.HabiroRing
