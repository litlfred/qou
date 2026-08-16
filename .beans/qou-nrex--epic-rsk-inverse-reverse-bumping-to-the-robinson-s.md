---
# qou-nrex
title: 'EPIC: RSK inverse — reverse bumping to the Robinson-Schensted bijection (taken over from the Schensted programme)'
status: todo
type: milestone
created_at: 2026-08-16T02:46:29Z
updated_at: 2026-08-16T02:46:29Z
---


## Why this epic exists, and what it is NOT for

The Schensted programme in `QOU/Mathlib/Schensted*.lean` is further along than its own brick-1
docstring says: the forward map is built through **brick 11**,
`SchenstedPairingMap.rskPair : Equiv.Perm (Fin n) → Σ_λ SYT(λ) × SYT(λ)`. Taking it over means
continuing from there, not restarting.

**Do not spend a session proving `rskPair` injective.** That yields `n! ≤ Σ_λ (f^λ)²`, and that
inequality is *already proved by an unrelated route*:
`BraidKnot.SpechtActionInjective.factorial_le_sum_sq` (injectivity of the Specht action map,
merged as PR #5189). Both programmes deliver the same direction. The non-redundant content is the
**inverse map** — reverse bumping — which is what gives surjectivity and hence the identity.

## Bricks

1. **DONE** — `SchenstedReverseRow.lean`: `rowUninsert` (reverse row insertion), the inversion
   law `rowUninsert_rowInsert`, plus `_length` / `_sorted` invariants and the three helper
   lemmas (`mem_rowUninsert`, `forall_le_of_rowUninsert_none`,
   `exists_lt_of_rowUninsert_some`). Sorry-free; `#print axioms` reports **`propext` alone** —
   no `Classical.choice`, no `Quot.sound`. Pure constructive combinatorics.
2. the cascade: undo `insertRec` across rows, driven by the recording tableau's largest timestamp;
3. recover the word: iterate the cascade to invert `insertWordRec`;
4. `rskPair` is bijective;
5. the cardinality count: `RSKBurnsideHolds n` for general `n`.

## What lands when brick 5 does

`BraidKnot.SpechtWedderburnCriterion.spechtEquiv_of_sum_sq` turns it straight into the general
Wedderburn split `k[S_n] ≃ₐ[k] ∏_μ End_k(S^μ)`, which is `sn_isotypic_specht_split` — the last
open gap of the OV cone, and hence the `sorryAx` on `RSKBurnsideHolds`'s two downstream keystones.
The `n ≤ 12` case of that split is already unconditional (PR #5197) via
`PartitionsOfBridge.rskBurnsideHolds_le12`, which uses **no** RSK at all.

Also note `RSKBridge.RSK_substrate_axiom` is a real `axiom` asserting brick 5's statement. Closing
brick 5 lets it be deleted; until then, check `#print axioms` on anything claiming the identity.

## Brick 2 DONE — the reverse cascade

`QOU/Mathlib/SchenstedReverseCascade.lean`, sorry-free (`uninsert_insert` axioms: `propext`,
`Quot.sound`; the two helpers: `propext` alone):

- `newRowIndex T x` — which row `insert T x` appends to, by the same recursion `insert` uses, so
  it records rather than searches;
- `uninsert T i` — remove the last cell of row `i`, push the displaced value up through rows
  `i-1 … 0` by `rowUninsert`;
- **`uninsert_insert`** — `uninsert (insert T x) (newRowIndex T x) = (T, some x)`.

**Two side conditions, both needed and both preserved.** `RowsSorted` is what brick 1's
`rowUninsert_rowInsert` consumes on each undone row. `NoEmptyRows` is what lets `uninsert` decide
at the target row between *shortening* a row and *deleting* it — a row that had one cell and loses
it must go, or the tableau grows a spurious empty row and shapes stop matching. `insert` preserves
both (`insert_rowsSorted` upstream; `insert_noEmptyRows` added here), so the cascade composes and
brick 3 can iterate it without re-establishing them.

Also proved on the way: `rowInsert_eq_append_of_none` — a no-bump insertion is literally
`r ++ [x]`, which is what makes `dropLast`/`getLast?` the right inverse at the target row.

**Next (brick 3):** iterate `uninsert` to invert `insertWordRec`. The row index to undo at is not
free — it is where the *largest* recording timestamp sits, and `SchenstedRecording`'s
`insertWordRec_snd_content` (content is exactly `range |w|`, each timestamp once) is what makes
"the largest" well-defined. Expect the work to be locating that cell, not the undoing.

## Brick 3 DONE — word recovery

`QOU/Mathlib/SchenstedWordRecovery.lean`, sorry-free (`propext`, `Classical.choice`,
`Quot.sound`):

- `rowIndices T w` — the row where each step appended its cell, recorded along the same fold
  `insertWord` runs;
- `uninsertSteps T is` — peel the steps of `is` off the final tableau;
- **`uninsertSteps_foldl`** / **`uninsertSteps_insertWord`** — the inversion law:
  `uninsertSteps (insertWord w) (rowIndices [] w) = ([], w)`;
- `word_eq_of_insertWord_eq` — equal insertion tableau + equal index record ⇒ equal word.

**The ordering trick that made it a one-liner induction.** `uninsertSteps T (i :: rest)` undoes
`rest` — the *later* steps — before `i`. That keeps it a plain structural recursion on the
**forward** index list, so the induction on `w` lines up with `insertWord`'s fold: the IH applies
to the inner fold unchanged and brick 2 closes the outer step. Defining it over a reversed list
instead would have forced an induction from the right; the file compiled first try because it
does not.

**So the `P` side of the RSK inverse is complete**, conditional on being handed the index list.

**Next (brick 4): the recording tableau supplies `rowIndices`.** `Q(w)`'s cell holding timestamp
`s` sits in the row that step `s` appended to — that is the definitional content of `insertRec`'s
Q-branches. `SchenstedRecording.insertWordRec_snd_content` (content is exactly `range |w|`, each
timestamp once) is what makes "the row holding `s`" a function. With that,
`word_eq_of_insertWord_eq` upgrades to injectivity of `rskPair`, and the same machinery run
forwards gives surjectivity.

## Brick 4 DONE — the recording tableau IS the row-index record

`QOU/Mathlib/SchenstedRecordingIndex.lean`, sorry-free (`propext`, `Quot.sound`):

- `qAppend Q i s` — write timestamp `s` at the end of `Q`'s row `i`, with the same `headD`/`tail`
  reading `insertRec` uses;
- **`insertRec_snd_eq_qAppend`** — one step: `(insertRec P Q x s).2 = qAppend Q (newRowIndex P x) s`;
- `qAppendSteps` + **`insertWordRecAux_snd_eq_qAppendSteps`** / `insertWordRec_snd_eq_qAppendSteps`
  — the whole fold, and its form at the empty tableau.

**The finding worth keeping:** the row `insertRec` writes the timestamp into is *literally*
`newRowIndex P x`, the index brick 2 defined from `insert`'s own recursion. There are not two
notions of "which row grew" needing reconciliation — the `Q`-branches of `insertRec` and the
branches of `newRowIndex` are the same case split, so the identification is a rewrite, not an
argument. Brick 3's index list was never side information.

Consequence: brick 3's `word_eq_of_insertWord_eq` wanted equal `P` **and** equal index records;
the index record is now a function of the construction of `Q`.

**Next:** invert `qAppendSteps` — read `rowIndices` back off a given `Q`. This is where
`SchenstedRecording`'s timestamp content (`insertWordRec_snd_content`: exactly `range |w|`, each
once) finally earns its keep: it is what makes "the row holding `s`" well defined, so the read-back
is a function rather than a search. After that, `rskPair` injectivity, then surjectivity, then the
count.

## Brick 5 DONE — the single-step read-back

`QOU/Mathlib/SchenstedReadback.lean`, sorry-free (`propext`, `Quot.sound`), first-try compile:

- `qRowOf Q t` — the index of the first row of `Q` holding `t`;
- **`qRowOf_qAppend_self`** — a *fresh* timestamp lands in the row it was written to;
- **`qRowOf_qAppend_of_ne`** — appending disturbs no other timestamp's row;
- `qRowOf_eq_none` — absent everywhere ⇒ not located.

**The freshness hypothesis is load-bearing, not bookkeeping.** `qRowOf` returns the *first* row
containing `t`, so a pre-existing copy of `t` would shadow the append and the read-back would
locate the wrong row. Freshness is what makes it a function rather than a search with ties.

In the RSK setting freshness is supplied by `SchenstedRecording.insertWordRec_snd_content` — the
recording content is exactly `range |w|` with each timestamp occurring **once**. That theorem has
been sitting in the corpus with no consumer; this is what it was for. Worth noting because it is
the second time in this epic that an apparently-idle earlier result turned out to be precisely the
missing hypothesis (the first: brick 2's `NoEmptyRows`).

**Next (brick 6):** thread the two lemmas along `qAppendSteps` under the freshness invariant
(timestamps strictly increase, so every step is fresh for what came before) to recover the whole
index list from `Q`. Then `rskPair` injectivity follows from brick 3's
`word_eq_of_insertWord_eq`.

## Brick 6 DONE — the whole index list is a function of `Q`

`QOU/Mathlib/SchenstedReadbackFold.lean`, sorry-free (`propext`, `Quot.sound`):

- `AllLt Q s` — every entry of `Q` is `< s`, the freshness invariant *in the form that
  propagates*;
- `mem_qAppend` / `allLt_qAppend` — an append adds only `s`, so the invariant survives with `s+1`;
- `qRowOf_qAppendSteps_of_lt` — later appends never move an earlier timestamp;
- **`qRowOf_qAppendSteps`** — `qRowOf (qAppendSteps Q is s) (s + k) = some (is.getD k 0)`, plus
  `qRowOf_qAppendSteps_zero` at the empty tableau.

**Why the invariant had to be `AllLt` rather than plain freshness.** "s ∉ Q" is what brick 5's
lemma consumes, but it does not propagate: after writing `s` you need `s+1 ∉ qAppend Q i s`, which
needs to know the *old* entries were below `s`, not merely `≠ s`. Stating the invariant as a bound
rather than a non-membership is what makes the induction go through in one pass — and it is true
for free, because timestamps are `0, 1, 2, …` by construction.

With brick 4 (`Q(w)` **is** `qAppendSteps [] (rowIndices [] w) 0`), the index list is now a
function of `Q(w)`. Brick 3's `word_eq_of_insertWord_eq` wanted exactly that.

**Next:** assemble — equal `(P, Q)` ⇒ equal `rowIndices` (brick 6) ⇒ equal word (brick 3), i.e.
`rskPair` injective. Then surjectivity, then the count.

## Brick 7 DONE — the RSK map is injective on words

`QOU/Mathlib/SchenstedRSKInjective.lean`, sorry-free:

- `rowIndices_length` — one row index per letter (**depends on no axioms at all**);
- `rowIndices_eq_of_recording_eq` — equal recording tableaux (at equal length) force equal index
  records;
- **`word_eq_of_insertWordRec_eq`** — `(P(w), Q(w))` determines `w`;
- `insertWordRec_ne_of_ne` — the contrapositive.

Pure assembly: brick 4 (`Q` *is* the fold) → brick 6 (the fold is readable) → equal `rowIndices`
→ brick 3 (equal `P` + equal indices ⇒ equal word). No new machinery, which is what the six
previous bricks were for.

**The length hypothesis is real, not decorative.** `qRowOf` constrains only timestamps
`0 … |w|-1`, so two words of *different* lengths can agree on every timestamp the shorter one
has. It costs nothing at the use site (`|w| = n` for a permutation of `Fin n`) but it is stated
rather than hidden.

**Next:** lift to `SchenstedPairingMap.rskPair`, which is typed in `StandardYoungTableau` rather
than raw `List (List ℕ)`. Expect the work to be the typed wrapper — `wordOfPerm` injectivity and
the `SYT` casts — not the combinatorics, which is now finished on the raw layer. Then
surjectivity, then the count.

## Brick 8 DONE — RSK separates permutations

`QOU/Mathlib/SchenstedPermInjective.lean`, sorry-free:

- `wordOfPerm_length` — `|wordOfPerm σ| = n`, which is exactly the length hypothesis brick 7 needs;
- `wordOfPerm_injective`;
- **`insertWordRec_wordOfPerm_injective`** — distinct permutations of `Fin n` have distinct
  `(P, Q)` pairs.

**The injectivity half of Robinson–Schensted is now proved**, at the raw `List (List ℕ)` level.

**Deliberately NOT the typed `rskPair`.** `SchenstedPairingMap.rskPair` is typed in
`StandardYoungTableau` and built from the raw tableaux by `listStandardYT`; lifting brick 7 through
it needs a typed→raw retraction the corpus does not carry, and the *content* would be identical —
the wrapper repackages the same data. Measured the typed layer first (`SchenstedStandardGeneric`
has three declarations, `SchenstedStandardTableau` four; no retraction among them) rather than
starting the lift and discovering it midway. The typed corollary can follow whenever a retraction
appears; nothing here claims it.

**Remaining: surjectivity.** That is now the *whole* residue of the epic — and note it is also the
only part not already implied by the algebra side, since `n! ≤ Σ (f^λ)²` is proved twice over
(here by injectivity, and independently by `SpechtActionInjective.factorial_le_sum_sq`). Whoever
takes it should start from `uninsertSteps` + `uninsert_insert`: the inverse machinery is built, so
surjectivity is "every `(P, Q)` of the right shape arises", i.e. that running the inverse on an
arbitrary standard pair produces a word whose forward image is that pair.

## Brick 9 DONE — the row-level RIGHT inverse

`QOU/Mathlib/SchenstedRowRightInverse.lean`, sorry-free (**`propext` alone** on both):

- `mem_of_rowUninsert_some` — the displaced value came from the row;
- **`rowInsert_rowUninsert`** — `rowUninsert r y = (r', some z)` ⇒ `rowInsert r' z = (r, some y)`.

Brick 1 gave `rowUninsert ∘ rowInsert = id`; this gives the other composite. The two rules are
mutually inverse on their bumping branches — and the reason is worth stating: `rowUninsert` takes
the **rightmost** entry `< y`, and after the swap everything strictly left of that position is
`≤ z` while the position holds `y > z`, so `rowInsert`'s search for the **leftmost** entry `> z`
lands on exactly that cell. The two searches come at the same cell from opposite ends. That is why
the composite is the identity rather than merely close to it.

**Why this is the surjectivity entry point.** Surjectivity is "every valid `(P, Q)` arises", and
the induction runs the inverse and then checks the forward map reproduces the pair. Brick 2's
`uninsert_insert` cannot do that — it is the wrong composite. This is the row-level half of the
one that can.

**Next:** the cascade-level right inverse, `insert (uninsert T i).1 x = T`. Expect a **corner
condition** on `i` (row `i+1` strictly shorter than row `i`): removing the last cell of a
non-corner row breaks column-strictness, so the statement is false without it. That hypothesis is
the thing to get right before writing the proof.
