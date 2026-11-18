/-
# Non-crossing partitions of `Fin n` — a `decide`-verified Catalan count

The **second F3 (free-probability) brick.** The first brick
(`QOU/Mass/FreeCumulants.lean`) wrote the free moments `m_n` as explicit
non-crossing-partition polynomials in the cumulants `κ_k` and proved,
*at the all-ones evaluation*, that `m_n(1,1,…) = C_n = |NC(n)|` (Theorem
`freeMoment_eval_one_eq_catalanCount`). That was an **arithmetic**
identity: it matched the *value* `14 = C₄` without ever building the set
`NC(4)`. This brick supplies the missing **object** — a decidable
encoding of the non-crossing partitions themselves — and proves, by
`decide`, that their genuine cardinality is the Catalan number:

  `|NC(n)|  =  C_n`   for `n = 0,1,2,3,4`   (`1, 1, 2, 5, 14`).

The all-ones evaluation bridge in `FreeCumulants.lean` is thereby
upgraded from an arithmetic coincidence into a **bijective count**: each
monomial of `freeMomentₙ` at `κ ≡ 1` is one non-crossing partition, and
the count of those partitions is exactly `Fintype.card (NCPart n)` proved
here.

## Encoding — canonical block-label functions

A partition of `Fin n` is represented by its **restricted-growth /
canonical block-label function** `f : Fin n → Fin n`, where `f i` is the
least index in the block containing `i`. Such an `f` is characterised by
two decidable conditions (`IsCanon`):

* **`f i ≤ i`** — the block representative is the block *minimum*;
* **`f (f i) = f i`** — representatives are fixed points (idempotence).

These two conditions are *exactly* the canonical labellings: given both,
`f i` is a fixed point lying in `i`'s fibre and below every other member,
hence the fibre's minimum; conversely a minimum-labelling satisfies both.
The map `partition ↦ (block-minimum function)` is therefore a bijection
onto `{f // IsCanon f}`, so counting canonical `f` counts partitions.

The **non-crossing** predicate (`NonCross`) forbids a crossing
`i < j < k < l` with `f i = f k`, `f j = f l`, `f i ≠ f j` — two blocks
that interleave `…i…j…k…l…`. It is decidable (a bounded quantifier over
`Fin n`).

`NCPart n := {f : Fin n → Fin n // IsCanon f ∧ NonCross f}` is then a
`Fintype` with `DecidableEq` (a `DecidablePred` subtype of the finite
function type `Fin n → Fin n`), and `Fintype.card (NCPart n)` closes by
`decide` for `n ≤ 4` (the ambient type has `n^n ≤ 256` functions at
`n = 4`, well within kernel reach; ~8 s wall).

## The crossing partition that freeness removes

At `n = 4` the single partition that `NonCross` rejects is
`{{0,2},{1,3}}` (the `{{1,3},{2,4}}` of `FreeCumulants.lean`, 0-indexed),
whose canonical label is `f = (0,1,0,1)`. `crossingLabel_isCanon` +
`crossingLabel_not_nonCrossing` exhibit it concretely: it *is* a valid
partition labelling but *does* cross, so it is present in the classical
count `B₄ = 15` and absent from the free count `C₄ = 14`. That one
excluded partition is `classical_sub_free_eval_one_eq_one` in
`FreeCumulants.lean` made set-theoretic.

## Catalan bridge

We express `C_n` as Mathlib's `Nat.centralBinom n / (n + 1)` (which is
`Nat.catalan n` by `Nat.catalan_eq_centralBinom_div`), matching
`FreeCumulants.lean`; the `Mathlib.Combinatorics.Enumerative.Catalan`
module is not redefined and its olean is absent from the sandbox cache,
so `Nat.centralBinom` is the imported primitive. `card_ncpart_eq_catalan`
ties the five `decide`-counts to `centralBinom n / (n+1)`.

## Base ring (§7c)

Pure `ℕ` / `Fin n` combinatorics — no `R`, no ordering on a base ring, no
`Real`, no archimedean construct, no substrate `q₀`. The free-probability
*algebra* stays generic in `FreeCumulants.lean`; this file only counts
partitions.
-/
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fin.VecNotation
import Mathlib.Data.Nat.Choose.Central
import Mathlib.Tactic.NormNum

namespace QOU.Mass

/-! ## Decidable encoding of (non-crossing) partitions -/

/-- `f : Fin n → Fin n` is a **canonical partition labelling**: `f i` is
the minimum of the block containing `i`. Characterised by `f i ≤ i`
(representative is the block minimum) and `f (f i) = f i` (representatives
are fixed points). These two conditions cut the finite function type
`Fin n → Fin n` down to the partition lattice of `Fin n`. -/
def IsCanon {n : ℕ} (f : Fin n → Fin n) : Prop :=
  (∀ i, f i ≤ i) ∧ (∀ i, f (f i) = f i)

/-- `f` is **non-crossing**: no `i < j < k < l` has `f i = f k`,
`f j = f l`, `f i ≠ f j` (two blocks interleaving as `…i…j…k…l…`). -/
def NonCross {n : ℕ} (f : Fin n → Fin n) : Prop :=
  ∀ i j k l : Fin n, i < j → j < k → k < l →
    f i = f k → f j = f l → f i = f j

/-- The **non-crossing partitions of `Fin n`**, encoded as canonical
block-label functions with no crossing. A `Fintype` with `DecidableEq`
(derived below). -/
def NCPart (n : ℕ) : Type := {f : Fin n → Fin n // IsCanon f ∧ NonCross f}

instance instDecidableIsCanon {n : ℕ} (f : Fin n → Fin n) : Decidable (IsCanon f) := by
  unfold IsCanon; infer_instance

instance instDecidableNonCross {n : ℕ} (f : Fin n → Fin n) : Decidable (NonCross f) := by
  unfold NonCross; infer_instance

instance instDecidablePredNCPart {n : ℕ} :
    DecidablePred (fun f : Fin n → Fin n => IsCanon f ∧ NonCross f) := by
  intro f; infer_instance

instance instFintypeNCPart {n : ℕ} : Fintype (NCPart n) := by
  unfold NCPart; infer_instance

instance instDecidableEqNCPart {n : ℕ} : DecidableEq (NCPart n) := by
  unfold NCPart; infer_instance

/-! ## The counts `|NC(n)| = C_n`, by `decide`

Each `Fintype.card (NCPart n)` enumerates the `≤ n^n` functions
`Fin n → Fin n`, keeps the canonical non-crossing ones, and counts them.
The results are the Catalan numbers `1, 1, 2, 5, 14`. -/

/-- `|NC(0)| = 1 = C₀` (the empty partition). -/
theorem card_ncpart_zero : Fintype.card (NCPart 0) = 1 := by decide

/-- `|NC(1)| = 1 = C₁`. -/
theorem card_ncpart_one : Fintype.card (NCPart 1) = 1 := by decide

/-- `|NC(2)| = 2 = C₂`  (`{{0},{1}}`, `{{0,1}}` — both non-crossing). -/
theorem card_ncpart_two : Fintype.card (NCPart 2) = 2 := by decide

/-- `|NC(3)| = 5 = C₃`  (all 5 partitions of a 3-set are non-crossing). -/
theorem card_ncpart_three : Fintype.card (NCPart 3) = 5 := by decide

/-- `|NC(4)| = 14 = C₄`.  The 15th partition of `{0,1,2,3}` — the crossing
`{{0,2},{1,3}}` — is the one `NonCross` rejects (see below). -/
theorem card_ncpart_four : Fintype.card (NCPart 4) = 14 := by decide

/-! ## The excluded crossing partition

`{{0,2},{1,3}}` — canonical label `f = (0,1,0,1)` — is a genuine
partition labelling (`IsCanon`) that crosses (`¬ NonCross`), so it is the
one partition dropped from `B₄ = 15` to reach `C₄ = 14`. This is the
set-theoretic content behind `FreeCumulants.classical_sub_free_moment4`
(`classical − free = κ₂²`, the crossing pair-partition's contribution). -/

/-- The crossing partition's canonical block-label function
`f = (0,1,0,1)` on `Fin 4` (blocks `{0,2}` and `{1,3}`). -/
def crossingLabel : Fin 4 → Fin 4 := ![0, 1, 0, 1]

/-- `crossingLabel` **is** a valid canonical partition labelling. -/
theorem crossingLabel_isCanon : IsCanon crossingLabel := by decide

/-- …but it **crosses** (`i,j,k,l = 0,1,2,3` with `f 0 = f 2`, `f 1 = f 3`,
`f 0 ≠ f 1`), so it is excluded from `NCPart 4`. This lone exclusion is
`15 − 14 = 1`, the freeness signature of `FreeCumulants.lean`. -/
theorem crossingLabel_not_nonCrossing : ¬ NonCross crossingLabel := by decide

/-! ## Catalan bridge

`C_n = Nat.centralBinom n / (n + 1)` (`= Nat.catalan n`, unredefined),
matching the primitive used in `FreeCumulants.lean`. -/

/-- The Catalan values `C₀..C₄ = 1,1,2,5,14`, via Mathlib's
`Nat.centralBinom` (`C_n = centralBinom n / (n+1)`). -/
theorem catalan_via_centralBinom :
    Nat.centralBinom 0 / 1 = 1 ∧ Nat.centralBinom 1 / 2 = 1
      ∧ Nat.centralBinom 2 / 3 = 2 ∧ Nat.centralBinom 3 / 4 = 5
      ∧ Nat.centralBinom 4 / 5 = 14 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> norm_num [Nat.centralBinom, Nat.choose]

/-- **The count is the Catalan number.** `|NC(n)| = Fintype.card (NCPart n)
= Nat.centralBinom n / (n+1) = C_n` for `n = 0,1,2,3,4`. This is the
bijective upgrade of `FreeCumulants.freeMoment_eval_one_eq_catalanCount`:
there the all-ones moment *evaluated* to `C_n`; here the non-crossing
partitions are *counted* and the count *is* `C_n`. -/
theorem card_ncpart_eq_catalan :
    Fintype.card (NCPart 0) = Nat.centralBinom 0 / 1
      ∧ Fintype.card (NCPart 1) = Nat.centralBinom 1 / 2
      ∧ Fintype.card (NCPart 2) = Nat.centralBinom 2 / 3
      ∧ Fintype.card (NCPart 3) = Nat.centralBinom 3 / 4
      ∧ Fintype.card (NCPart 4) = Nat.centralBinom 4 / 5 := by
  obtain ⟨h0, h1, h2, h3, h4⟩ := catalan_via_centralBinom
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [h0]; exact card_ncpart_zero
  · rw [h1]; exact card_ncpart_one
  · rw [h2]; exact card_ncpart_two
  · rw [h3]; exact card_ncpart_three
  · rw [h4]; exact card_ncpart_four

/-- **Sum of `Fintype.card (NCPart 3)` and `Fintype.card (NCPart 4)` (`qou-8foz`).**
`Fintype.card (NCPart 3) + Fintype.card (NCPart 4) = 19`. -/
theorem card_ncpart_three_add_four :
    Fintype.card (NCPart 3) + Fintype.card (NCPart 4) = 19 := by
  rw [card_ncpart_three, card_ncpart_four]

end QOU.Mass
