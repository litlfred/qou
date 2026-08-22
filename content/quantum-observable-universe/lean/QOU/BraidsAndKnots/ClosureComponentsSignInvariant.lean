import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.GroupTheory.GroupAction.Quotient

/-!
# Braid-closure component count is a crossing-sign invariant

The number of components of a braid closure is determined by the
permutation the braid induces on its strands, and `σᵢ` and `σᵢ⁻¹` induce
the **same** transposition. So the component count cannot see a crossing's
sign, and is therefore invariant under every resolution of an unsigned or
averaged crossing.

## Why this is worth proving

This is the invariant that adjudicates the deuteron's knot assignment
(bean `qou-e5jf`,
`docs/audits/2026-08-21-deuteron-knot-assignment-adjudication.md`). The
canonical deuteron mass word `atom_braid_word_3A(1,1)` is a `23`-letter
element of `H₆(q)` whose five *averaged* crossings `σ − h/2` and
`σ − h(½ − δ/4)` are ℂ-linear combinations, not braid-group elements, so
the word has no single closure — it has one closure per resolution, and
there are `2⁵ = 32` of them.

Enumeration found all `32` resolutions give a `3`-component link while
`6₂` and the trefoil are knots (`1` component) and the Hopf link has `2`.
This file replaces that enumeration with a proof: the count is the same
for **every** resolution because it never depended on the signs, so no
knot and no `2`-component link can be the closure of that word under any
crossing convention. That is a **scope-(b) structural exclusion** in the
sense of `AGENTS.md §"Before declaring refuted"` — the invariant is named
and proved here rather than asserted.

It is also the formalize-first prune of
`docs/audits/…-adjudication.md §5` step 2: it rules out the entire
knot-valued hypothesis class *before* any census search is run, so a
search that does run can be pointed at the right slice.

## What is proved

* `wordPerm_eq_of_indices_eq` — the induced permutation depends only on
  the sequence of crossing *indices*, never on their signs. This is the
  whole content; everything else is a specialisation of it.
* `wordPerm_resolve` — consequently, resolving each unsigned crossing by
  an arbitrary rule `f` (a function of the letter's position, so distinct
  crossings may resolve differently) leaves the permutation unchanged.
* `closureComponents_resolve` — hence the component count of the closure,
  defined as the number of orbits of the induced permutation acting on
  the strands, is likewise unchanged.
* `closureComponents_ne_of_perm_ne` — the contrapositive, which is the
  form the adjudication uses: differing component counts exclude a
  candidate outright.

## Scope — what is proved, and what is cited

The new content is the **sign-invariance**. What is *not* proved here, and
must not be read as proved, is the identification underneath it:

* that `wordPerm adjacentPerm` is the image of the braid word under the
  standard surjection `Bₙ ↠ Sₙ`, and
* that the closure's components correspond to that permutation's orbits.

Both are standard (Birman §1.2 and §2.2) and are **cited, not derived** —
deriving them needs a formalisation of `Bₙ` with its relations, which this
file deliberately does not build. So `wordPerm adjacentPerm` is *defined*
to send each crossing to the adjacent transposition regardless of sign,
rather than being shown to do so from the braid relations.

That definitional choice is where a reader should aim their scepticism,
so it is worth being explicit about why it is not circular. The claim
being formalised is *"the map `Bₙ → Sₙ` cannot see a crossing's sign"*,
and the reason it cannot is that `σᵢ` and `σᵢ⁻¹` have the *same* image
there. `wordPerm` encodes exactly that by giving `g` the index and
withholding the `Bool`. Had the definition instead read
`if letter.2 then g letter.1 else (g letter.1)⁻¹`, every theorem below
would be **false** — which is what makes them falsifiable statements
about the definition rather than restatements of it.

Purely combinatorial otherwise: `Equiv.Perm (Fin n)` and lists. No ring,
no `ℝ`, no archimedean construct, so §7c's base-ring wall is not
approached. The statements are generic in the index type where possible.

Braid words are modelled exactly as the corpus already models them —
`QOU.Archimedean.BraidWord n` is by definition `List (Fin (n - 1) × Bool)`
with the `Bool` recording the sign — so these lemmas apply to it without a
conversion. That type is *not* imported here, to keep the import cone off
the matrix/Hecke machinery this argument does not use.

## References

- [birman1974] J. Birman, *Braids, Links, and Mapping Class Groups*,
  Annals of Mathematics Studies 82, Princeton (1974) — §1.2 for the
  natural surjection `Bₙ ↠ Sₙ` and §2.2 for the closure.
- [manuscript] `docs/audits/2026-08-21-deuteron-knot-assignment-adjudication.md`
-/

namespace QOU.BraidsAndKnots

open Equiv

variable {ι : Type*} {n : ℕ}

/-! ## §1  The permutation induced by a signed word -/

/-- The permutation a signed word induces, given an assignment `g` of a
permutation to each crossing index.

The `Bool` component of each letter is the crossing's sign, and `g` is not
given it: that omission *is* the mathematical content, since `σᵢ` and
`σᵢ⁻¹` project to the same transposition in `Sₙ`. -/
def wordPerm (g : ι → Perm (Fin n)) (w : List (ι × Bool)) : Perm (Fin n) :=
  (w.map fun letter => g letter.1).prod

@[simp] theorem wordPerm_nil (g : ι → Perm (Fin n)) :
    wordPerm g ([] : List (ι × Bool)) = 1 := rfl

@[simp] theorem wordPerm_cons (g : ι → Perm (Fin n)) (letter : ι × Bool)
    (w : List (ι × Bool)) :
    wordPerm g (letter :: w) = g letter.1 * wordPerm g w := rfl

/-- **The induced permutation depends only on the crossing indices.**

Two signed words with the same index sequence induce the same
permutation, whatever their signs. Every other statement in this file is
a specialisation of this one. -/
theorem wordPerm_eq_of_indices_eq (g : ι → Perm (Fin n))
    {v w : List (ι × Bool)} (h : v.map Prod.fst = w.map Prod.fst) :
    wordPerm g v = wordPerm g w := by
  have hv : v.map (fun letter => g letter.1) = (v.map Prod.fst).map g := by
    simp [List.map_map, Function.comp_def]
  have hw : w.map (fun letter => g letter.1) = (w.map Prod.fst).map g := by
    simp [List.map_map, Function.comp_def]
  unfold wordPerm
  rw [hv, hw, h]

/-! ## §2  Resolving unsigned crossings

An *unsigned* word is a bare list of indices; a **resolution** chooses a
sign for each crossing. The rule `f : ℕ → Bool` is indexed by position, so
different crossings may be resolved differently — the `2⁵` resolutions of
the deuteron mass word are exactly the `f`s on its five averaged letters. -/

/-- Resolve an unsigned word, assigning the crossing at position `k` the
sign `f k`, counting from `k₀`. -/
def resolveFrom (f : ℕ → Bool) : List ι → ℕ → List (ι × Bool)
  | [], _ => []
  | i :: rest, k => (i, f k) :: resolveFrom f rest (k + 1)

/-- Resolve an unsigned word, counting positions from `0`. -/
def resolve (f : ℕ → Bool) (idx : List ι) : List (ι × Bool) :=
  resolveFrom f idx 0

/-- Resolving changes only the signs: the index sequence is preserved. -/
@[simp] theorem resolveFrom_indices (f : ℕ → Bool) (idx : List ι) (k : ℕ) :
    (resolveFrom f idx k).map Prod.fst = idx := by
  induction idx generalizing k with
  | nil => rfl
  | cons i rest ih => simp [resolveFrom, ih]

@[simp] theorem resolve_indices (f : ℕ → Bool) (idx : List ι) :
    (resolve f idx).map Prod.fst = idx :=
  resolveFrom_indices f idx 0

/-- **Every resolution induces the same permutation.**

`f` and `f'` may disagree at every position; the permutation does not
move. This is the statement the deuteron adjudication needs: the mass
word's `32` resolutions cannot differ in their induced permutation. -/
theorem wordPerm_resolve (g : ι → Perm (Fin n)) (f f' : ℕ → Bool)
    (idx : List ι) :
    wordPerm g (resolve f idx) = wordPerm g (resolve f' idx) :=
  wordPerm_eq_of_indices_eq g (by simp)

/-! ## §3  Component count of the closure -/

/-- The number of components of the closure of a braid whose induced
permutation is `π`: the strands `Fin n` fall into components exactly as
they fall into orbits of `⟨π⟩`, since the closure joins strand `i` to
strand `π i`. -/
noncomputable def closureComponents (π : Perm (Fin n)) : ℕ :=
  Nat.card (MulAction.orbitRel.Quotient (Subgroup.zpowers π) (Fin n))

/-- **The component count of a braid closure is a crossing-sign
invariant.**

The count is the same for every resolution of the unsigned word, because
by `wordPerm_resolve` the permutation it is computed from is the same. -/
theorem closureComponents_resolve (g : ι → Perm (Fin n)) (f f' : ℕ → Bool)
    (idx : List ι) :
    closureComponents (wordPerm g (resolve f idx))
      = closureComponents (wordPerm g (resolve f' idx)) := by
  rw [wordPerm_resolve g f f' idx]

/-- The same statement for two signed words sharing an index sequence. -/
theorem closureComponents_eq_of_indices_eq (g : ι → Perm (Fin n))
    {v w : List (ι × Bool)} (h : v.map Prod.fst = w.map Prod.fst) :
    closureComponents (wordPerm g v) = closureComponents (wordPerm g w) := by
  rw [wordPerm_eq_of_indices_eq g h]

/-- **The exclusion form.** Distinct component counts force distinct
induced permutations.

This is how the invariant is used in adjudication: a candidate link whose
component count differs from the word's is excluded, and by
`closureComponents_resolve` that exclusion survives every choice of
crossing sign — so it needs no crossing convention to be fixed first. -/
theorem closureComponents_ne_of_perm_ne {π π' : Perm (Fin n)}
    (h : closureComponents π ≠ closureComponents π') : π ≠ π' := by
  intro hEq
  exact h (by rw [hEq])

/-! ## §4  The adjacent-transposition assignment

The braid group's own map to `Sₙ`: the crossing at index `i` swaps
strands `i` and `i + 1`. Instantiating `g` at this recovers the
statements above for genuine braid words. -/

/-- Strand `i + 1`, as an element of `Fin n`, for a crossing index
`i : Fin (n - 1)`. -/
def succStrand (i : Fin (n - 1)) : Fin n :=
  ⟨i.val + 1, by have := i.isLt; omega⟩

/-- Strand `i`, as an element of `Fin n`. -/
def strand (i : Fin (n - 1)) : Fin n :=
  ⟨i.val, by have := i.isLt; omega⟩

/-- The transposition the crossing at index `i` induces on strands. The
sign of the crossing is absent by construction, which is the point. -/
def adjacentPerm (i : Fin (n - 1)) : Perm (Fin n) :=
  Equiv.swap (strand i) (succStrand i)

/-- **The braid-closure statement.** For genuine braid words — the
corpus's `BraidWord n = List (Fin (n - 1) × Bool)` — the number of
components of the closure is unchanged by resolving the crossings any way
at all. -/
theorem braidClosureComponents_resolve (f f' : ℕ → Bool)
    (idx : List (Fin (n - 1))) :
    closureComponents (wordPerm adjacentPerm (resolve f idx))
      = closureComponents (wordPerm adjacentPerm (resolve f' idx)) :=
  closureComponents_resolve adjacentPerm f f' idx

/-- Two braid words differing only in their crossing signs have closures
with the same number of components. -/
theorem braidClosureComponents_eq_of_indices_eq
    {v w : List (Fin (n - 1) × Bool)} (h : v.map Prod.fst = w.map Prod.fst) :
    closureComponents (wordPerm adjacentPerm v)
      = closureComponents (wordPerm adjacentPerm w) :=
  closureComponents_eq_of_indices_eq adjacentPerm h

end QOU.BraidsAndKnots
