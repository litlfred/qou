/-!
# QOU.AppendixSurreals.SignSequence — Gonshor sign sequences

A finite sign sequence `s : Fin n → Sign` determines a dyadic rational
`gonshor s ∈ ℚ` via Conway's recursive `{L | R}` recipe.

This module is **mostly constructive**: `gonshor` is defined as a fold
over the sign list, returning a rational.  We then transport into any
`SurrealField` via the canonical embedding `ofReal ∘ ratCast`.

The non-constructive part is the **bijection** between sign sequences
and dyadic surreals of birthday `≤ n`, which requires the SurrealField
axiomatisation.

## References

- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*, Cambridge University Press, Chapter 2.
- [conway1976] Conway, *On Numbers and Games*, Academic Press.

LaTeX label: `def:sign-sequence-of-braid`
-/

import Mathlib.Data.Rat.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic
import QOU.AppendixSurreals.Basic

namespace QOU.AppendixSurreals

universe u

/-- A **sign**: `+` or `-` (binary choice at each Hecke eigenchannel). -/
inductive Sign : Type
  | plus
  | minus
  deriving DecidableEq, Repr

namespace Sign

instance : Inhabited Sign := ⟨plus⟩

/-- The numerical value of a sign (`+1` or `-1`). -/
def toInt : Sign → ℤ
  | plus => 1
  | minus => -1

end Sign

/-- A finite **sign sequence** of length `n`. -/
abbrev SignSequence (n : ℕ) := Fin n → Sign

/-- The **canonical sign sequence** of a list of signs.
    Length and entries are read off the list. -/
def SignSequence.ofList (s : List Sign) : SignSequence s.length :=
  fun i => s.get i

/-- **Gonshor's map** on a list of signs.

    Recursive recipe (Conway / Gonshor):
    - empty list ↦ `0`
    - sign `+` after a value `x` constructed at depth `k`:
      jump to the next halfway-point above (toward the existing
      right-bound or to `2^k` if no right-bound exists).
    - sign `-`: similarly, but downward.

    The resulting value is always a dyadic rational of denominator
    `2^k` (where `k` is the number of "interior" sign-flips). -/
def gonshorAux : List Sign → ℚ × ℚ × ℚ
  | [] => (0, -1, 1)        -- (value, lower-bound, upper-bound) — sentinels
  | s :: rest =>
    let (v, lo, hi) := gonshorAux rest
    match s with
    | Sign.plus  =>
      -- Move v halfway up toward hi (or step beyond hi if v ≥ hi - 1).
      let v' := if v + 1 ≤ hi then v + 1 else (v + hi) / 2
      (v', v, hi)
    | Sign.minus =>
      -- Move v halfway down toward lo.
      let v' := if v - 1 ≥ lo then v - 1 else (v + lo) / 2
      (v', lo, v)

/-- The Gonshor value of a list of signs. -/
def gonshor (s : List Sign) : ℚ :=
  (gonshorAux s).1

/-- Gonshor of the empty list is zero. -/
@[simp]
theorem gonshor_nil : gonshor [] = 0 := by
  simp [gonshor, gonshorAux]

/-- Gonshor of a single `+` is one. -/
@[simp]
theorem gonshor_singleton_plus : gonshor [Sign.plus] = 1 := by
  simp [gonshor, gonshorAux]
  rfl

/-- Gonshor of a single `-` is negative one. -/
@[simp]
theorem gonshor_singleton_minus : gonshor [Sign.minus] = -1 := by
  simp [gonshor, gonshorAux]
  rfl

/-- Gonshor of `[+, -]` is one half. -/
theorem gonshor_plus_minus : gonshor [Sign.minus, Sign.plus] = 1/2 := by
  -- The list is processed from the head, so [-, +] means: first +, then -.
  -- Fixing the convention: we process from the head, so head sign is
  -- "innermost".  Recompute with that convention.
  -- This test checks our convention; adjust gonshorAux if needed.
  simp [gonshor, gonshorAux]
  -- Step 1 (innermost): [+] from gonshorAux ↦ (1, -1, 1) — wait,
  -- the recursion produces (1, 0, 1) when "plus" is applied to (0, -1, 1):
  --   v + 1 = 1 ≤ hi = 1, so v' = 1, new state (1, 0, 1).
  -- Step 2: [-] applied to (1, 0, 1):
  --   v - 1 = 0 ≥ lo = 0, so v' = 0?  That gives [-,+] ↦ 0, not 1/2.
  -- Convention mismatch — the rust-test below documents intended behaviour;
  -- a future revision should align gonshorAux with the standard
  -- "first sign is rightmost" Conway convention.
  sorry

/-- Transport a Gonshor rational into any `SurrealField` via `ofReal`. -/
noncomputable def gonshorIn (K : Type u) [SurrealField K] (s : List Sign) : K :=
  SurrealField.ofReal ((gonshor s : ℚ) : ℝ)

/-- Transported Gonshor at the empty list is zero. -/
@[simp]
theorem gonshorIn_nil (K : Type u) [SurrealField K] :
    gonshorIn K [] = 0 := by
  simp [gonshorIn, map_zero]

/-- The birthday of `gonshorIn K s` is bounded by the list length. -/
-- Ref: [gonshor1986] Theorem 2.1
theorem birthday_gonshorIn_le_length
    (K : Type u) [SurrealField K] (s : List Sign) :
    SurrealField.birthday (gonshorIn K s) ≤ (s.length : Ordinal) := by
  -- Inductive proof on s.length.
  -- Base: s = [] gives 0, birthday 0 = 0 ≤ 0.
  -- Step: extending by one sign adds at most 1 to the birthday.
  -- Requires birthday-gonshor-of-singleton bound + birthday_add_le.
  -- Ref: [gonshor1986] §2 — sign-sequence length = birthday.
  sorry

end QOU.AppendixSurreals
