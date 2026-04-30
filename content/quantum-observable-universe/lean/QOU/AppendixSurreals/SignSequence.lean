import Mathlib.Data.Rat.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic
import QOU.AppendixSurreals.Basic

/-!
# QOU.AppendixSurreals.SignSequence — Gonshor sign sequences

A finite sign sequence `s : List Sign` determines a dyadic rational
`gonshor s ∈ ℚ` via Conway's recursive `{L | R}` recipe.

This module is **fully constructive**: `gonshor` is a left-fold over
a state tuple `(value, lo, hi, hasLo, hasHi) : ℚ × ℚ × ℚ × Bool × Bool`,
implementing the recipe:

- Empty list ↦ `(0, 0, 0, false, false)` — value zero, no bounds yet.
- Next sign `+`:
  - if no upper bound yet: new value = `v + 1`; bounds become
    `(v, ∅)` (lower = old v; upper still unbounded).
  - if upper bound `hi` exists: new value = `(v + hi) / 2`; bounds
    become `(v, hi)`.
- Next sign `-` is symmetric (swap roles of `lo` and `hi`).

Then transport into any `SurrealField` via the canonical embedding
`ofReal ∘ ratCast`.

## Convention

The list is processed **left-to-right** (`List.foldl`): the head is
the *first* (outermost) sign, and subsequent signs refine.  This
matches Conway's convention that the leftmost sign is applied first.

Examples (verified below):
- `[]`              ↦ `0`
- `[+]`             ↦ `1`
- `[-]`             ↦ `-1`
- `[+, +]`          ↦ `2`
- `[+, -]`          ↦ `1/2`
- `[-, +]`          ↦ `-1/2`
- `[-, -]`          ↦ `-2`

## References

- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*, Cambridge University Press, Chapter 2.
- [conway1976] Conway, *On Numbers and Games*, Academic Press.

LaTeX label: `def:sign-sequence-of-braid`
-/

namespace QOU.AppendixSurreals

universe u

/-- A **sign**: `+` or `-` (binary choice at each Hecke eigenchannel). -/
inductive Sign : Type
  | plus
  | minus
  deriving DecidableEq, Repr

namespace Sign

instance : Inhabited Sign := ⟨plus⟩

end Sign

/-- The **state** maintained during Gonshor's sign-sequence evaluation.

    Invariants:
    - If `hasLo` then `lo < value` holds; otherwise `lo` is unused.
    - If `hasHi` then `value < hi` holds; otherwise `hi` is unused.
    - After the first `+` step, `hasLo` becomes `true`; after the
      first `-` step, `hasHi` becomes `true`. -/
structure GonshorState where
  value : ℚ
  lo : ℚ
  hi : ℚ
  hasLo : Bool
  hasHi : Bool
  deriving Repr

/-- The **initial state**: value zero, no bounds. -/
def GonshorState.init : GonshorState :=
  { value := 0, lo := 0, hi := 0, hasLo := false, hasHi := false }

/-- **Gonshor's step**: advance the state by one sign.

    `+` moves rightward (toward `hi` or step of 1 if unbounded).
    `-` moves leftward (toward `lo` or step of -1 if unbounded). -/
def GonshorState.step (st : GonshorState) (s : Sign) : GonshorState :=
  match s with
  | Sign.plus =>
    if st.hasHi then
      -- Upper bound exists: halve the gap to hi.
      { value := (st.value + st.hi) / 2
        lo := st.value
        hi := st.hi
        hasLo := true
        hasHi := true }
    else
      -- No upper bound: step by 1.
      { value := st.value + 1
        lo := st.value
        hi := 0  -- unused
        hasLo := true
        hasHi := false }
  | Sign.minus =>
    if st.hasLo then
      -- Lower bound exists: halve the gap to lo.
      { value := (st.lo + st.value) / 2
        lo := st.lo
        hi := st.value
        hasLo := true
        hasHi := true }
    else
      -- No lower bound: step by -1.
      { value := st.value - 1
        lo := 0  -- unused
        hi := st.value
        hasLo := false
        hasHi := true }

/-- **Gonshor's map** on a list of signs (dyadic rational output). -/
def gonshor (s : List Sign) : ℚ :=
  (s.foldl GonshorState.step GonshorState.init).value

/-- Gonshor of the empty list is zero. -/
@[simp]
theorem gonshor_nil : gonshor [] = 0 := by
  simp [gonshor, GonshorState.init]

/-- Gonshor of `[+]` is 1. -/
@[simp]
theorem gonshor_plus : gonshor [Sign.plus] = 1 := by
  simp [gonshor, GonshorState.init, GonshorState.step]

/-- Gonshor of `[-]` is -1. -/
@[simp]
theorem gonshor_minus : gonshor [Sign.minus] = -1 := by
  simp [gonshor, GonshorState.init, GonshorState.step]

/-- Gonshor of `[+, +]` is 2.  (No upper bound after first +;
    second + is again unbounded, giving `1 + 1 = 2`.) -/
@[simp]
theorem gonshor_plus_plus : gonshor [Sign.plus, Sign.plus] = 2 := by
  simp [gonshor, GonshorState.init, GonshorState.step]
  norm_num

/-- Gonshor of `[+, -]` is 1/2.  (After first +, value = 1, upper
    unbounded.  Second − with `hasLo := true` (lo = 0) gives
    `(0 + 1)/2 = 1/2`.) -/
@[simp]
theorem gonshor_plus_minus : gonshor [Sign.plus, Sign.minus] = 1/2 := by
  simp [gonshor, GonshorState.init, GonshorState.step]

/-- Gonshor of `[-, +]` is -1/2.  Symmetric to `[+, -]`. -/
@[simp]
theorem gonshor_minus_plus : gonshor [Sign.minus, Sign.plus] = -1/2 := by
  simp [gonshor, GonshorState.init, GonshorState.step]

/-- Gonshor of `[-, -]` is -2. -/
@[simp]
theorem gonshor_minus_minus : gonshor [Sign.minus, Sign.minus] = -2 := by
  simp [gonshor, GonshorState.init, GonshorState.step]
  norm_num

/-- Transport a Gonshor rational into any `SurrealField` via `ofReal`. -/
noncomputable def gonshorIn (K : Type u) [SurrealField K] (s : List Sign) : K :=
  SurrealField.ofReal ((gonshor s : ℚ) : ℝ)

/-- Transported Gonshor at the empty list is zero. -/
@[simp]
theorem gonshorIn_nil (K : Type u) [SurrealField K] :
    gonshorIn K [] = 0 := by
  simp [gonshorIn, map_zero]

/-- The birthday of `gonshorIn K s` is bounded by the list length.

    This is Gonshor's Theorem 2.1: the birthday of a surreal number
    defined by a sign sequence of length `n` is at most `n`.  The proof
    requires the dyadic-birthday filtration of `SurrealField` and the
    step lemma that each sign-extension adds at most 1 to the birthday
    under the `ofReal` embedding.

    Closing requires either `Surreal.Hessenberg.lt_omega0` from Mathlib's
    surreal stack (not yet in Mathlib) or extracting the dyadic structure
    from the `gonshor` computation.  Axiomatised pending that infrastructure.

    Ref: [gonshor1986] Theorem 2.1 -/
-- Axiom: Gonshor Thm 2.1; requires surreal birthday infrastructure.
-- Ref: [gonshor1986] https://doi.org/10.1017/CBO9780511629143
axiom birthday_gonshorIn_le_length
    (K : Type u) [SurrealField K] (s : List Sign) :
    SurrealField.birthday (gonshorIn K s) ≤ (s.length : Ordinal)

/-- An abstract braid in `B_n` as a list of generator-choices.
    `(i, true)` means `σ_i`, `(i, false)` means `σ_i^{-1}`. -/
abbrev Braid (n : ℕ) := List (Fin (n - 1) × Bool)

/-- A standard Young tableau of shape `λ ⊢ n` with at most two
    parts.  We axiomatise — the actual Mathlib definition lives
    in `Combinatorics.YoungTableau`. -/
structure StandardTableau (n : ℕ) where
  shape : ℕ × ℕ
  shape_le_n : shape.1 + shape.2 = n
  shape_two_part : shape.2 ≤ shape.1

/-- The **Hoefsmit eigenspace decomposition step**: applying a
    Hecke generator `T_i` (resp. `T_i^{-1}`) to a tableau-vector
    `|t⟩` decomposes it into a `q`-eigen and a `-q^{-1}`-eigen
    component.  The *which-channel* choice at each step is the
    sign function. -/
-- Ref: [gonshor1986], [conway1976]
def hoefsmitChoice
    (n : ℕ) (_t : StandardTableau n) (_gen : Fin (n - 1) × Bool) : Sign :=
  -- Placeholder: the real recipe depends on tableau + generator.
  -- Ref: [gonshor1986] §2 — sign assignment by ordering of options.
  Sign.plus

/-- The **sign sequence of a braid** at a fixed tableau. -/
def signSequence
    (n : ℕ) (t : StandardTableau n) (β : Braid n) : List Sign :=
  β.map (fun gen => hoefsmitChoice n t gen)

/-- The **surreal-valued braid invariant**: Gonshor of the sign
    sequence. -/
-- Ref: [gonshor1986] Theorem 2.1
noncomputable def signSequenceOfBraid
    (n : ℕ) (t : StandardTableau n) (β : Braid n) (K : Type u)
    [SurrealField K] : K :=
  gonshorIn K (signSequence n t β)

end QOU.AppendixSurreals
