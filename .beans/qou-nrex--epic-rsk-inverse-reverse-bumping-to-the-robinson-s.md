---
# qou-nrex
title: 'EPIC: RSK inverse — reverse bumping to the Robinson-Schensted bijection (taken over from the Schensted programme)'
status: in-progress
type: milestone
priority: normal
created_at: 2026-08-16T02:46:29Z
updated_at: 2026-08-22T19:52:50Z
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

## Brick 10 — cascade right inverse, non-deleting branch (PR #5374, 2026-08-21)

`insert (uninsert T i).1 z = T` under `2 ≤ (T.getD i []).length`. lean-direct exit 0;
`#print axioms insert_uninsert` = [propext, Classical.choice, Quot.sound], no sorryAx.

**The predicted hypothesis was wrong and is corrected in-file.** Brick 9's PR body predicted a
corner condition (row i+1 strictly shorter than row i). It is not that: the row-kept branch works
for *any* sorted row, corner or not, and the row-deleted branch fails on a genuine counterexample
(#eval-checked): uninsert [[1],[2,4]] 0 = ([[2,4]], some 1) but insert [[2,4]] 1 = [[1,4],[2]].
That T has row lengths (1,2) — a non-Young shape. So the deleting branch needs a **shape**
hypothesis (weakly decreasing row lengths), which is the next brick, not a corner one.

### Remaining
- brick 11: the deleting branch, under a Young-shape hypothesis on T.
- word-level surjectivity (iterate brick 10+11 the way brick 3 iterates brick 2).
- RSKBurnsideHolds for general n → feeds spechtEquiv_of_sum_sq for the general Wedderburn split.


### Brick 10 generalized (same PR #5374, 2026-08-21)

The `2 ≤ length` side condition is GONE. `insert_uninsert` now holds at every row of a
row-sorted, column-strict tableau with no empty rows — the full cascade right inverse.

**Correction to the note above:** I wrote that the deleting branch 'needs a shape hypothesis
(weakly decreasing row lengths), which is the next brick'. It did not need a new brick.
`ColStrict` / `StrictBelow` were already in SchenstedInsertion.lean, and `StrictBelow` bundles
BOTH halves — `lower.length ≤ upper.length` (the Young-shape half I was about to invent) and
`upper[j] < lower[j]` — with the bumping lemma `insert_colStrict` already proved. One corpus grep
for ColStrict before writing that note would have saved the round trip. Recorded in the file
docstring and the PR body, not quietly dropped.

axioms: insert_uninsert = [propext, Quot.sound] (Classical.choice dropped with the length omega).

### Remaining after brick 10
- word-level surjectivity: iterate insert_uninsert the way brick 3 iterates brick 2.

### Brick 11 — uninsert invariants (PR #5383, 2026-08-21, branch claude/schensted-uninsert-invariants-2026-08-21)

uninsert_rowsSorted + uninsert_noEmptyRows, unconditional at every row index. Both needed to
ITERATE brick 10 (the IH re-applies insert_uninsert at each intermediate tableau).

**The corner condition finally located.** I looked for it in the wrong place across two bricks.
StrictBelow bundles a LENGTH half; the keeping branch at row 0 turns 'row1.length <= r.length' into
'row1.length <= r.length - 1', which fails exactly when row 1 is as long as row 0 — i.e. when the
removed cell is not a corner. So:
  - right-inverse identity (brick 10): needs NO corner condition
  - ColStrict preservation: CANNOT hold without one
Machine-checked on T = [[1,3],[2,4]]: cornerWitness_colStrict / cornerWitness_not_colStrict, plus
cornerWitness_{rowsSorted,noEmptyRows}_survives showing the split is real on that same witness.

Not a gap: the cascade is always run at the largest recording-tableau entry, which IS a corner.
The condition is supplied by Q one level up and belongs in the statement that consumes it.

### Remaining after brick 11
- ColStrict preservation under an explicit corner hypothesis (needs the corner predicate defined,
  and the i+1 case is the reverse bumping lemma proper).
- word-level surjectivity: iterate insert_uninsert the way brick 3 iterates brick 2, consuming the
  three preservation lemmas.
- RSKBurnsideHolds for general n -> spechtEquiv_of_sum_sq gives the general Wedderburn split.

### Brick 12a — rowUninsert index characterization (PR #5390, branch claude/schensted-rowuninsert-index-2026-08-21)

rowUninsert_spec: the reverse mirror of the corpus's rowInsert_bump_eq_set. Existential form
(k < length, getD k = z, .1 = r.set k y, z < y, and nothing right of k eligible). The maximality
clause is the content.

Two findings:
- lt_of_index_lt needs NO sortedness. I expected weak-sorted + rightmost chaining; the maximality
  clause gives y <= r[m] directly and z < y chains through. One line.
- THIRD duplication caught this arc: getD_set_self / getD_set_ne / getD_eq_getElem_mem already
  exist at SchenstedInsertion.lean:551,556,561. Pattern: that file is 1300+ lines and carries far
  more than its section headings advertise. GREP IT BEFORE ADDING ANY List/getD/index helper.

Machine-checked rightmost witness: rowUninsert [1,2,4] 3 = ([1,3,4], some 2) — two eligible
entries, takes the right-hand one; leftmost would give [3,2,4], not weakly increasing.

### Three PRs open simultaneously on this epic, no file overlap
- #5374 brick 10  SchenstedCascadeRightInverse.lean
- #5383 brick 11  SchenstedUninsertInvariants.lean
- #5390 brick 12a SchenstedReverseRowIndex.lean
All three add one import line to QOU.lean in the same region; 2nd and 3rd to land need a one-line
rebase there.

- brick 12b: reverse bump monotonicity (write index weakly INCREASES going up, mirror of
  bump_findIdx_mono). May need a named uninsertIdx; rowUninsert_spec is the bridge.
- brick 12c: uninsert preserves ColStrict, under the corner hypothesis located in #5383.
- word-level surjectivity; RSKBurnsideHolds for general n.


## MERGED 2026-08-21 — bricks 10-15 all on main

All six landed via /prepare-merge-auto, rebase-merge, branches preserved:
  #5374 b10 bd39e875e0 | #5383 b11 fce013fecc | #5390 b12 715db19cfc
  #5398 b13 53286a5b6c | #5400 b14 3cd8bed694 | #5410 b15 87252c0d20

Verified ON MAIN (not just per-branch): all six lean-direct exit 0 together; six imports registered
in QOU.lean; zero sorryAx across every declaration. The one 'sorry' grep hit is the phrase
'sorry-free' in a docstring.

### Merge-mechanics lesson worth keeping
The stacked branches could NOT be plain-rebased once their parents landed: rebase replays the
parent's commits, which are already on main, giving 'both added' conflicts — and worse, the
REBASE_HEAD version was the SUPERSEDED intermediate (pre-correction docstring) while main had the
final one. Blindly resolving would have REVERTED the brick-12 correction.
Fix: rebuild each stacked branch on fresh origin/main and cherry-pick ONLY its unique commits
(git log --oneline origin/main..BR, drop the ones already landed). Also: a stacked PR's BASE must be
retargeted to main (#5398 failed to merge with '405 merge conflicts' until its base was changed off
the parent branch).

### What the epic now has on main
P side complete at the word level. insert/uninsert mutually inverse on column-strict tableaux
(both composites); all three invariants preserved (two unconditionally, ColStrict at a corner);
the run-level statement foldl_insert_uninsertSteps + insertWord_uninsertSteps; and brick 15 showing
their hypotheses are inhabited.

### Next: the Q-side, which is the actual gate on surjectivity
CornersAlong P is for an ARBITRARY standard pair (P,Q) with positions read off Q — NOT off an
insertion history. Different argument: the cell carrying the largest remaining entry of a standard
tableau is a corner, because a cell below it would carry a larger entry. Brick 15 does NOT cover
this and its docstring says so.


### Brick 16 — Q-side keystone (PR #5426, based on main)

isCorner_of_max_in_row : ColStrict T -> NoEmptyRows T -> i < T.length ->
  (last cell of row i >= every entry of T) -> IsCorner T i

Classical one-line contradiction: not-a-corner + ColStrict's length half pins rows i and i+1 EQUAL
in length, putting a cell directly below the maximum, which column-strictness makes strictly larger.

**It needs LESS than standardness.** I had this queued as 'needs a standardness predicate on
List (List N)' and the corpus has none, so the obvious move was to write one. Checking what the
argument actually consumes: no strict-row hypothesis, no standardness predicate — ColStrict plus the
position of the maximum is the whole input. Writing that predicate would have been a fifth
unnecessary addition on an arc that already caught four duplications.

Also le_getD_last_of_sorted (+ isCorner_of_max_in_row_sorted) so a caller who knows the max is
SOMEWHERE in row i can reach the keystone, which is stated about the last cell.

### Remaining
- brick 17: wire the keystone along a run — read positions off Q, show each step removes the largest
  REMAINING entry, assemble CornersAlong for an arbitrary standard (P,Q).
- rskPair bijective.
- RSKBurnsideHolds general n -> spechtEquiv_of_sum_sq gives the general Wedderburn split.


### Brick 17 — the cascade IS shape-level corner removal (same PR #5426)

tableauShape_uninsert : ColStrict T -> NoEmptyRows T -> IsCorner T i ->
  tableauShape (uninsert T i).1 = SYTEnum.removeCorner (tableauShape T) i

uninsert changes exactly ONE row length (rows above the target are rewritten by rowUninsert, which
preserves length), so on shapes it decrements entry i and drops the row if that empties it — exactly
removeCorner.

**This is how the arbitrary-(P,Q) argument crosses from Q to P.** IsCorner is determined by the
shape (isCorner_iff_shape, brick 13), so once the shape is tracked, a corner of Q's shape is a
corner of P's.

Connects to EXISTING infra rather than duplicating: SYTEnum.removeCorner is the GNW corner-removal
op in SYTListCorner.lean, and its sz_removeCorner / sorted_removeCorner / removeCorner_pos now apply
to the reverse cascade for free. (Fifth potential duplication avoided — I checked before writing a
parallel shape operation.)

### Remaining for surjectivity — now assembly, not new mathematics
- read the positions off Q (bricks 4-6 machinery: qRowOf / qAppendSteps);
- show each step removes the largest REMAINING entry of Q;
- induct with the shape carried alongside, using brick 16 + brick 17 at each step
  -> CornersAlong P is for arbitrary standard (P,Q).
Then rskPair bijective; then RSKBurnsideHolds general n -> spechtEquiv_of_sum_sq gives the general
Wedderburn split (currently n <= 12 only, via the unrelated rskBurnsideHolds_le12).


### Brick 18 — CornersAlong reduces to SHAPES ALONE (same PR #5426)

uninsertSteps_shape_and_corners : ShapeCornersAlong (tableauShape T) is ->
  CornersAlong T is  AND  tableauShape (uninsertSteps T is).1 = removeCornerSteps (tableauShape T) is

**The decoupling is the result.** CornersAlong T is mentions the tableau at EVERY step, so
discharging it looked like it needed P and Q reasoned about together. It does not: IsCorner is
determined by the shape (isCorner_iff_shape, brick 13) and brick 17 makes the cascade act on shapes
as removeCorner, so the run-level corner condition FACTORS THROUGH tableauShape T.

Headline consequence — insertWord_uninsertSteps_of_shape: every hypothesis is about T's SHAPE and
the position list; P appears only in the conclusion.

Four conclusions in one induction because they are mutually dependent: the shape at step k needs the
corner condition at every LATER step (else the cascade may not have succeeded), and the corner at
step k needs the shape at step k. Brick 14's uninsertSteps_invariants does NOT break the circle — it
TAKES CornersAlong as a hypothesis, which is what we are producing.

### Epic status
P side: DONE, and now reduced to shapes. Bricks 10-15 on main; 16-18 open in #5426.
Remaining for surjectivity is ONE statement about Q's shape alone:
  produce ShapeCornersAlong (tableauShape P) is + removeCornerSteps ... = []
  from Q standard, by reading positions off Q (bricks 4-6: qRowOf / qAppendSteps) and showing each
  step peels the corner carrying the largest REMAINING entry (brick 16 supplies that corner).
Then rskPair bijective; then RSKBurnsideHolds general n -> spechtEquiv_of_sum_sq gives the general
Wedderburn split.


### Brick 19 — the two run conditions COINCIDE (same PR #5426)

cornersAlong_iff_shape : CornersAlong T is <-> ShapeCornersAlong (tableauShape T) is
(under RowsSorted + ColStrict + NoEmptyRows)

Brick 18 gave shape -> tableau; this adds the converse. No circularity: the induction's own
hypothesis supplies ShapeCornersAlong for the LATER steps, and tableauShape_uninsertSteps turns that
into the shape at that point, so the shape is in hand before the current step's corner is checked.

Immediately buys: brick 15's insertion-built CornersAlong now reads at shape level, so BOTH
hypotheses of insertWord_uninsertSteps_of_shape are inhabited (shapeCornersAlong_insertWord,
removeCornerSteps_insertWord). Same anti-vacuity check brick 15 made, one level up — a reduction to
a condition nothing satisfies is no reduction.

### #5426 now carries bricks 16-19, all sorry-free and axiom-clean
16 isCorner_of_max_in_row | 17 tableauShape_uninsert | 18 the reduction | 19 the iff + inhabitation


### Brick 20 — addable-cell sequences peel back as corners (same PR #5426)

shapeCornersAlong_addCellSteps : YoungShape l -> AddableAlong l is ->
  ShapeCornersAlong (addCellSteps l is) is  AND  removeCornerSteps (addCellSteps l is) is = l

A standard tableau IS a sequence of addable cells. This proves such a sequence, peeled in reverse,
is exactly a corner sequence — and lands back on the starting shape.

Purely shape-level: no tableau, no Q, no insertion. Isolates the combinatorial content so brick 21
only has to supply the bridge 'standard Q -> addable sequence'.

Three single-step facts: youngShape_addCell, isCorner_addCell (shape mirror of brick 15's
insert_isCorner, same reason), removeCorner_addCell (the exact-inverse half — why
removeCornerSteps ... = l falls out of the same induction).

Slip worth recording: I first routed sortedness through an invented List.sorted_ge_iff_getD_le.
Replaced with sorted_of_getD_step, proved here — a shape is weakly decreasing as soon as each
adjacent step is, which is the form the addCell case analysis actually produces.

### The chain is now complete except one bridge
  addable sequence --brick 20--> ShapeCornersAlong --brick 18/19--> CornersAlong
    --brick 14--> insertWord (uninsertSteps P is).2 = P
Brick 21 = the only gap: standard Q gives an AddableAlong sequence whose addCellSteps [] is the
shape of P. Everything downstream of that is proved.


### Brick 21 — insertion acts on shapes as addCell (same PR #5426)

tableauShape_insert : tableauShape (insert T x) = addCell (tableauShape T) (newRowIndex T x)

The MIRROR of brick 17 (tableauShape_uninsert = removeCorner). Corpus had neither this nor any
newRowIndex lemma.

isAddable_newRowIndex — NOT from the bumping-column argument. Read off insert_colStrict (already in
corpus): the inserted tableau is column-strict, so its shape is weakly decreasing, and spelling that
out at the added index IS addability. I expected to need bump_findIdx_mono; I did not.

addableAlong_rowIndices closes the insertion-built case by a route INDEPENDENT of brick 19's iff —
brick 20's machinery reaches the same conclusion brick 15 + 19 did. The forward and reverse shape
pictures AGREE, not merely compose.

### #5426 now carries bricks 16-21, four files, all sorry-free and axiom-clean
16 isCorner_of_max_in_row | 17 tableauShape_uninsert | 18 the reduction | 19 the iff
20 addable sequences peel as corners | 21 the forward shape law

### The ONE remaining gap for surjectivity
An ARBITRARY standard Q gives an AddableAlong sequence. Everything else is proved:
  Q standard --GAP--> AddableAlong --20--> ShapeCornersAlong --18/19--> CornersAlong
    --14--> insertWord (uninsertSteps P is).2 = P
The gap needs a standardness predicate on List (List N) (corpus has none) plus the fact that reading
positions off Q in timestamp order yields addable cells. Brick 16 already supplies the corner half.


### Brick 22 — the built shape is the COUNT shape (same PR #5426)

getD_addCellSteps : AddableAlong l is -> (addCellSteps l is).getD i 0 = l.getD i 0 + is.count i

addCell increments one entry, so row i of the built shape holds exactly the cells whose position was
i. No tableau appears. This is the tool the Q-bridge needs: it identifies addCellSteps [] is with
tableauShape Q by COUNTING entries per row, rather than by constructing a truncation of Q.

**A design attempt that failed, recorded so it is not retried.** I tried to state the remaining gap
as a self-contained counting condition on the position list —
  forall k, is[k] = 0 or (is.take k).count is[k] < (is.take k).count (is[k] - 1)
— hoping to prove AddableAlong from it and drop AddableAlong entirely. Circular: the count
characterisation itself needs each step's index to be within the CURRENT shape, which is part of
what AddableAlong asserts. AddableAlong stays the primitive; the count form is its consequence, and
that is the direction that composes.

This also means the Q-bridge will NOT need a qTrunc construction — counting per row is enough.


### Brick 23 — the counting bridge (same PR #5426)

countLt_above : ColStrict Q -> rows strictly increasing -> entry at column c of row r+1 =>
  countLt (row r+1) k < countLt (row r) k

Brick 22 made the built shape a COUNT shape, so IsAddable reduces to a count comparison. This is it,
from column-strictness alone: the entry directly above is smaller, and StrictBelow's LENGTH half
guarantees that cell exists — so row r has its first c+1 entries below the threshold against exactly
c in row r+1.

**Two constructions avoided, both of which I had queued:**
1. qTrunc (restrict Q to entries < s, prove ColStrict survives the filter, show emptied rows form a
   suffix) — estimated 250+ lines. Counting per row replaces it entirely.
2. A standardness predicate on List (List N). Corpus has none; I queued writing one twice. The
   hypotheses actually consumed are 'rows strictly increasing' + ColStrict, written inline.

Third time on this arc that checking what the argument consumes shrank the machinery.

### Remaining gap is now narrow
Assemble: read rows off Q in timestamp order (qRowOf, brick 5) into a position list, and combine
brick 23's count comparison with brick 22's count shape to get AddableAlong. Everything downstream
is proved.


### Brick 23b — the bridge fact keyed on MEMBERSHIP (same PR #5426)

countLt_above_mem : ColStrict Q -> rows strictly increasing -> k in row r+1 =>
  countLt (row r+1) k < countLt (row r) k

**Answers the open question from last turn.** I flagged not knowing whether qRowOf's lemmas give the
COLUMN as well as the row. Checked: qRowOf returns only the row, and nothing in bricks 4-6 records a
column — so brick 23's column-indexed form was not reachable by the assembly.

The fix is recovery, not a new qRowOf lemma: in a strictly increasing row the column of an entry IS
its countLt.
  countLt_lt_length_and_getD : k in row -> countLt row k < row.length
                                        AND row.getD (countLt row k) 0 = k
Both halves in one induction (shared case analysis). countLt_above then restates on membership.

### #5426 carries bricks 16-23b, five files, all sorry-free and axiom-clean
### Remaining: pure plumbing
Build the position list from qRowOf over the timestamp range, match (is.take k).count i against
countLt (row i) k, apply 23b. Everything else proved.


### Brick 24 — qRowOf correctness (same PR #5426)

mem_of_qRowOf    : qRowOf Q t = some r -> t in Q.getD r []
qRowOf_lt_length : qRowOf Q t = some r -> r < Q.length
countLt_above_qRowOf : qRowOf Q k = some (r+1) -> countLt (row r+1) k < countLt (row r) k

**Answers the question I flagged last turn, and it was a real gap.** Every existing qRowOf lemma is
about how qAppend / qAppendSteps MOVE things (qRowOf_qAppend_self, qRowOf_qAppend_of_ne,
qRowOf_qAppendSteps). None says the located row is correct on its own terms. For a Q that is simply
GIVEN rather than built by appending, there was nothing to appeal to. Two short inductions.

That is now three flagged-then-confirmed gaps in a row (qRowOf gives no column; no standardness
predicate needed; no qRowOf correctness lemma). Checking the input before building on it has been
worth the minutes each time.

### #5426 carries bricks 16-24, five files, all sorry-free and axiom-clean

### The ONE remaining step, and it is a counting bijection not plumbing
  (is.take k).count i  =  countLt (Q.getD i []) k
LHS counts timestamps t < k whose qRowOf row is i; RHS counts entries of row i below k. Equal when
Q's entries are exactly 0..n-1 with no repeats. That needs a 'Q holds exactly the range' hypothesis
(corpus has insertWordRec_snd_content / _nodup for the built case) plus the counting argument.
Everything else in the chain is proved.


### Brick 25 — qRowOf total and exact (same PR #5426)

qRowOf_isSome_of_mem_flatten : t in Q.flatten -> exists r, qRowOf Q t = some r
qRowOf_eq_some_iff_mem : Q.flatten.Nodup -> i < Q.length -> (qRowOf Q t = some i <-> t in row i)

Brick 24 gave one direction; this is the converse, and it is where cross-row DISTINCTNESS finally
matters — qRowOf returns the FIRST row containing t, so a repeated entry would be located in the
wrong row. Nodup on the flattened tableau is the weakest hypothesis ruling that out, and the corpus
already tracks it for the built case (insertWordRec_snd_content_nodup).

**Totality is separate and needs no distinctness — and it is a trap-blocker.** qRowOf returns an
Option; a counting argument reading it with .getD 0 would silently score every ABSENT timestamp as
row 0. Stating totality makes that visible instead of latent. Worth having found before writing the
count, not after.

### #5426 carries bricks 16-25, five files, all sorry-free and axiom-clean
### Remaining: the count equality itself
  (is.take k).count i = countLt (Q.getD i []) k
Both sides now have their ingredients: exactness turns 'row of t is i' into 't in row i', totality
rules out the none-trap, and the two sides then count the same set. Needs a 'Q holds exactly
0..n-1' hypothesis to know every t < k is present.


### Brick 26 — THE COUNT EQUALITY (same PR #5426)

count_qPositions : Q.flatten.Nodup -> i < Q.length -> (all t below k are in Q) ->
  (qPositions Q k).count i = countLt (Q.getD i []) k

The step the whole Q-side reduces to. Brick 22 phrased the built shape as a count over the POSITION
LIST; countLt counts over the ROWS of Q. Same number.

Genuinely a bijection, not a rewrite — timestamps on the left, entries on the right. Both filtered
lists are duplicate-free with the same members; proof goes through toFinset rather than building the
bijection by hand.

Each hypothesis does distinct work:
- Nodup -> exactness (brick 25); without it qRowOf locates a repeated entry in the WRONG row, and
  rows are not duplicate-free either.
- i < Q.length -> the row exists.
- all t below k present -> totality (brick 25). qPositions reads qRowOf with .getD 0, so an ABSENT
  timestamp reads as row 0 and is counted there. This is exactly the none-trap totality was stated
  to block. Predicting it one brick early is what made this one compile first try.

### #5426 carries bricks 16-26, five files, all sorry-free and axiom-clean
### Remaining: assemble AddableAlong from the pieces
All ingredients now proved. IsAddable at step k = (count comparison), which is brick 23b via
countLt_above_qRowOf, transported across brick 26 to the position-list side, with brick 22 supplying
the shape. What is left is threading them through the AddableAlong recursion.


### Brick 27 — THE CHAIN CLOSES (same PR #5426)

addableAlong_qPositions : Q column-strict + rows strictly increasing + flatten Nodup +
  all t below n present  ->  AddableAlong [] (qPositions Q n)

insertWord_uninsertSteps_of_standard : P row-sorted/col-strict/no-empty-rows, Q standard, SAME SHAPE
  ->  insertWord (uninsertSteps P (qPositions Q n)).2 = P

**The gap named back at brick 15 is closed.**
  Q standard --26--> AddableAlong --20--> ShapeCornersAlong --18--> insertWord . uninsertSteps = id

Each ingredient was already proved; brick 27 threads them through the AddableAlong recursion,
inducting on the HORIZON not the list. That is why the append-at-end forms were needed:
List.range (n+1) = List.range n ++ [n] grows at the END while the recursion consumes from the FRONT.

Only hypothesis tying P to Q is EQUAL SHAPE — which is what 'a pair of tableaux of the same shape'
means.

### SCOPE — what this is NOT
Word-level surjectivity on the P side. NOT bijectivity of rskPair: nothing says the recovered word's
RECORDING tableau is Q. RSKBurnsideHolds for general n STILL OPEN, still only n <= 12 via the
unrelated rskBurnsideHolds_le12 (no RSK in it).

### #5426 carries bricks 16-27, five files, zero sorries, axiom-clean throughout
### Next
- recovered word's recording tableau is Q (the other half of bijectivity);
- then rskPair bijective; then RSKBurnsideHolds general n -> spechtEquiv_of_sum_sq gives the general
  Wedderburn split.

### Bricks 28-32 — THE Q SIDE CLOSES (same PR #5426)

The gap named in brick 27's SCOPE note is closed. The recovered word's RECORDING tableau is Q.

Brick 28-29 (SchenstedReinsertRow.lean) — the missing link:
  addCell_removeCorner   : adding a cell back at a corner returns the shape (two-case anatomy of
                           removeCorner: above length one the zero-filter is inert and it is a
                           `set`; at length one the corner is the final row and the filter deletes)
  newRowIndex_uninsert   : newRowIndex (uninsert T i).1 z = i — the re-inserted letter goes back to
                           the row it was peeled from. Brick 10 proved the tableau is rebuilt; it
                           never said WHERE. Argued at the level of shapes: addCell moves exactly
                           one entry, so one index only can land back on the shape you started from.
  rowIndices_uninsertSteps : along a run, the recovered word's row-index record IS the position
                           list it was recovered from.

Brick 30-31 (SchenstedRecordingTrunc.lean) — the replay:
  qTrunc Q n             : the horizon truncation — timestamps below n, emptied rows dropped.
                           The induction is stated HERE, not at Q. After n steps the replay is not
                           Q, so the direct statement has nothing to induct on. Same move as
                           brick 27's induct-on-the-horizon.
  qAppend_qTrunc         : one replay step. Two facts do it, both from column strictness, NOT from
                           the appends:
                             - non-empty rows of a truncation are an INITIAL SEGMENT
                               (exists_le_head: any entry has a strictly smaller entry in the top
                               row) => a row index means the same thing in qTrunc Q t as in Q,
                               nothing has shifted;
                             - a timestamp joins its row at the END (filter_lt_succ_mem: the row is
                               strictly increasing and every smaller entry is already there) =>
                               qAppend, which only writes at a row's end, is the right operation.
  qAppendSteps_qPositions_self : qAppendSteps [] (qPositions Q n) 0 = Q.

Brick 32 (SchenstedRSKSurjective.lean) — P and Q meet:
  insertWordRec_uninsertSteps_of_standard :
    P row-sorted/col-strict/no-empty-rows, Q standard, SAME SHAPE
      ->  insertWordRec (uninsertSteps P (qPositions Q n)).2 = (P, Q)
  = brick 27 (insertion tableau is P) + brick 29 (record is the position list) + brick 31 (replay
    rebuilds Q), tied by brick 4 (recording tableau IS the record of rowIndices).
  Brick 29 was the load-bearing one: without it "the insertion tableau came out right" constrains
  nothing about Q.

### SCOPE — what this is NOT
Surjectivity onto standard pairs **in the List (List ℕ) representation**. NOT rskPair bijectivity.
rskPair lands in `Σ μ : YoungDiagram, StandardYoungTableau μ × StandardYoungTableau μ` — Mathlib's
type — so what remains is a REPRESENTATION BRIDGE (List (List ℕ) <-> StandardYoungTableau μ, plus
the +1 value shift wordOfPerm applies), not more combinatorics on the correspondence itself.
RSKBurnsideHolds for general n STILL OPEN, still only n <= 12 via rskBurnsideHolds_le12 (no RSK).

### #5426 now carries bricks 16-32, eight files, zero sorries, axiom-clean throughout
### Next
- the representation bridge to Mathlib's StandardYoungTableau (check SchenstedCellsBridge first);
- then rskPair bijective; then RSKBurnsideHolds general n -> spechtEquiv_of_sum_sq gives the general
  Wedderburn split.

### Bricks 33-34 — the representation bridge, other direction (same PR #5426)

listStandardYT (brick 10) already crossed List (List ℕ) -> StandardYoungTableau. These start back.

Brick 33 (SchenstedListOfSYT.lean):
  toListTableau S        : rows of S read off its cells, (List.range rowLens.length).map ...
  + tableauShape_toListTableau = μ.rowLens ON THE NOSE
  + rows_strict / rowsSorted / colStrict / noEmptyRows / nodup_flatten

  Where the two notions differ is SHAPE, not content: StrictBelow BUNDLES the Young-shape length
  condition with the entry comparison; SemistandardYoungTableau keeps them apart (lengths in the
  diagram, entries in col_strict). rowLen_anti is the half with no counterpart in the tableau's
  own data — the bridge has to supply it.

Brick 34 (SchenstedRecordingOfSYT.lean) — the +1 convention, paid:
  mem_flatten_toListTableau_iff_Icc : entries are exactly 1..|μ| (mapsTo one way, surjOn the other)
  unshiftT Q := Q.map (·.map (· - 1))  -- inverse of the existing shiftT on positive entries
  toRecordingTableau S := unshiftT (toListTableau S)
  + the full bundle brick 32 takes: ColStrict, rows strictly increasing, flatten Nodup,
    NoEmptyRows, shape = μ.rowLens, content EXACTLY {0..|μ|-1}.

  Brick 32's Q counts from 0 (insertWordRec starts at 0); a StandardYoungTableau counts from 1
  (bijOn onto Set.Icc 1 |μ|). insertWordSYT already pays this in the other direction via shiftT.
  Positivity of every entry — the hypothesis the down-shift needs — FALLS OUT of the content fact,
  so no extra input. Past the end nothing is needed: the default 0 is a fixed point of (· - 1).

### SCOPE — what 33+34 are NOT
The Q ARGUMENT of brick 32, assembled. NOT brick 32 run on it.

### What is actually left before rskPair surjectivity (measured, not guessed)
Given a target ⟨μ, S_P, S_Q⟩ one needs a PERMUTATION σ with rskPair σ = it. Brick 32 gives a WORD w
with insertWordRec w = (P₀, Q₀) in list form. Three gaps remain, all bridge, none combinatorics:
  1. ROUND TRIP: listStandardYT (toListTableau S) = S — needed to turn the list-level equality into
     insertWordPSYT … = S_P and insertWordSYT w = S_Q. This is the real remaining work.
  2. SIGMA/SHAPE COERCION: ofRowLens μ.rowLens _ = μ is ofRowLens_to_rowLens_eq_self (exists), but
     the Sigma equality still has to be threaded through it.
  3. w MUST COME FROM A PERMUTATION: wordOfPerm has content {1..n}; brick 32's w is whatever the
     cascade recovered. Need w's content = {1..n} => ∃ σ, wordOfPerm σ = w.
RSKBurnsideHolds for general n STILL OPEN, still only n <= 12 via rskBurnsideHolds_le12 (no RSK).

### #5426 now carries bricks 16-34, ten files, zero sorries, axiom-clean throughout

### Bricks 35-37 — two of the three remaining gaps closed (same PR #5426)

Brick 35 (SchenstedSYTRoundTrip.lean) — THE ROUND TRIP, which I had flagged as the one gap whose
proof shape I did not know:
  sigma_listStandardYT_toListTableau : ⟨_, listStandardYT (toListTableau S) …⟩ = ⟨μ, S⟩

  The statement MUST be a Sigma: listStandardYT lands on ofRowLens (tableauShape T) _, only
  PROPOSITIONALLY equal to μ, so the two tableaux do not share a type. Packing the diagram with the
  tableau is what makes the equation statable — and is the form rskPair's codomain already takes.

  I expected the dependent-type work to be the hard part. It is TWO LEMMAS:
    ofRowLens_congr  (equal row-length lists -> equal diagrams, by subst; sortedness proofs are
                      irrelevant)
    sigma_ext_entry  (subst the diagram, then compare entries)
  Everything else is entrywise on ℕ with NO cast. getD_getD_toListTableau_all is load-bearing: the
  list tableau reads back every entry, ON the diagram and OFF it — off it both sides are 0, one
  because the list runs out, the other by the SSYT's own `zeros`.

  Also added StandardYoungTableau.ext_entry — a genuine gap in that type's API (bijOn is a proof, so
  entries determine the tableau). content_toListTableau supplies listStandardYT's content argument
  in the multiset form it wants (both sides nodup, same members).

Brick 36 (SchenstedWordOfPermSurj.lean):
  exists_wordOfPerm_eq : content w = {1..n}  ->  ∃ σ : Equiv.Perm (Fin n), wordOfPerm σ = w
  σ i = w[i] - 1; nodup gives injective; injective = bijective on a finite type, which is the only
  reason no inverse has to be built by hand.

Brick 37 (SchenstedShapeOfPositions.lean):
  addCellSteps_qPositions : addCellSteps [] (qPositions Q n) = tableauShape Q
  Brick 32 relates P and Q by "P's shape is what Q's positions BUILD"; what one has about a pair is
  that they SHARE a shape. This identifies the two. Row i gains one cell per position = i (brick 22)
  = the count of row-i entries below the horizon (brick 26) = the row's length once the horizon
  clears everything. eq_of_getD_eq closes it: lists of POSITIVE naturals agreeing at every index are
  equal — positivity is what supplies the LENGTHS (past the shorter list getD reads 0, which the
  longer cannot).

### ONE gap left before rskPair surjectivity
Thread brick 35's Σ-equality through rskPair's DEFINITION:
  rskPairWord hw = ⟨pShape w, insertWordPSYT hw, recordingShape_eq_pShape w ▸ insertWordSYT w⟩
The `▸` transport plus the PAIR-valued sigma make this messier than the single-tableau case of
brick 35 — sigma_ext_entry handles one tableau, not two under a shared diagram cast. Expect a
pair-valued analogue plus lemmas identifying pShape w and recordingShape w with μ.
RSKBurnsideHolds for general n STILL OPEN, still only n <= 12 via rskBurnsideHolds_le12 (no RSK).

### #5426 now carries bricks 16-37, thirteen files, zero sorries, axiom-clean throughout

### Brick 38 — rskPair IS SURJECTIVE (same PR #5426). The arc from brick 10 ends here.

exists_rskPair_eq : ∀ (μ : YoungDiagram) (SP SQ : StandardYoungTableau μ),
                      ∃ σ : Equiv.Perm (Fin μ.cells.card), rskPair σ = ⟨μ, SP, SQ⟩

Every ingredient was already proved. What was left was PLUMBING, and the plumbing is
dependent-type work: rskPairWord is a Σ whose SECOND component has ALREADY been transported along
recordingShape_eq_pShape, so comparing it with ⟨μ, SP, SQ⟩ moves three things at once.
  sigma_pair_ext_entry : subst the diagram equality, then compare entries (the only honest route)
  entry_cast           : the ▸ transport moves NO entry — this is what makes the second component
                         comparable at all
  shiftT_unshiftT      : under the transport the recording tableau is shiftT of the 0-based one, so
                         brick 34's down-shift has to be undone; the content fact already knows the
                         entries are positive, which is the whole hypothesis.

Assembly inside exists_rskPair_eq:
  P := toListTableau SP ; Q := toRecordingTableau SQ ; n := μ.cells.card
  hrange/hlt  <- mem_flatten_toRecordingTableau (brick 34)
  hshape      <- addCellSteps_qPositions (brick 37) + both shapes = μ.rowLens
  hpair       <- insertWordRec_uninsertSteps_of_standard (brick 32)
  word content<- insertWord_content + content_toListTableau (brick 35)
  σ           <- exists_wordOfPerm_eq (brick 36)

### SCOPE — SURJECTIVITY, NOT BIJECTIVITY
Injectivity is SchenstedRSKInjective, stated FOR WORDS. Combining the two into an Equiv
Perm (Fin n) ≃ Σ_{|μ|=n} SYT(μ)² is NOT done, and it is what RSKBurnsideHolds needs.
RSKBurnsideHolds for general n STILL OPEN, still only n <= 12 via rskBurnsideHolds_le12 (no RSK).
Then SpechtWedderburnCriterion.spechtEquiv_of_sum_sq converts it to the general Wedderburn split.

### #5426 now carries bricks 16-38, fourteen files, zero sorries, axiom-clean throughout
### Next
- assemble the Equiv from injectivity (words) + surjectivity (this): the mismatch to bridge is that
  injectivity is stated for words and surjectivity for permutations;
- then RSKBurnsideHolds general n -> spechtEquiv_of_sum_sq -> general Wedderburn split.

### Bricks 39-40 — THE CORRESPONDENCE IS AN EQUIV (same PR #5426)

Brick 39 (SchenstedRSKPairInjective.lean) — rskPair_injective.
  SchenstedRSKInjective proved injectivity ON WORDS, for LIST tableaux. rskPair is on PERMUTATIONS
  and valued in a Σ of Mathlib SYTs. That mismatch was the entire distance.

  KEY TRICK, worth remembering: NO HEq, NO subst needed. Extracting the second component of a
  Σ-equality normally needs a transport because its type depends on the first — BUT
      fun X => X.2.1.entry i j
  is a perfectly good NON-DEPENDENT function on the Σ type (dependent projection, ℕ-valued field),
  so congrArg hands over entry equalities directly. Everything after that is ordinary list work:
    eq_of_shape_and_entries  (same shape + same entries -> same list tableau)
    shiftT_injective         (strip the 0->1 relabel; map of an injective map)
    word_eq_of_insertWordRec_eq (existing, word level)
    wordOfPerm_injective     (back to permutations)

Brick 40 (SchenstedRSKEquiv.lean):
  rskEquiv n : Equiv.Perm (Fin n) ≃ {X : Σ μ, SYT μ × SYT μ // X.1.cells.card = n}

  The SUBTYPE IS FORCED: rskPair lands in the Σ over ALL diagrams, image is exactly those with n
  cells (rskPair_card, via recordingCells_card ∘ recordingShape_eq_pShape). Cutting the codomain is
  what makes it a bijection and not merely injective.
  exists_rskPair_eq_of_card substitutes |μ| = n — legitimate because n IS A VARIABLE. Contrast
  brick 35, where the diagram equality had NO variable side and ofRowLens_congr had to be proved.

### SCOPE — NOT RSKBurnsideHolds
RSKBurnsideHolds n := ∑ p : Nat.Partition n, (dimSYT p)^2 = n! — indexed by Nat.Partition, NOT by
YoungDiagram. Getting there from rskEquiv additionally needs:
  Nat.card (Perm (Fin n)) = n!                                    (Fintype.card_perm, easy)
  Nat.card {X // X.1.cells.card = n} = ∑ p, (dimSYT p)^2          (THE WORK)
and the second needs partitionShape : Nat.Partition n -> YoungDiagram to be a BIJECTION onto the
diagrams with n cells, plus a Σ-card decomposition over that index. None of it is done.
RSKBurnsideHolds general n STILL OPEN, still only n <= 12 via rskBurnsideHolds_le12 (no RSK in it).

### #5426 now carries bricks 16-40, sixteen files, zero sorries, axiom-clean throughout
### Next
- partitionShape bijective onto {μ // μ.cells.card = n}  (the remaining obstacle)
- then the Σ-card decomposition -> RSKBurnsideHolds general n -> spechtEquiv_of_sum_sq -> general
  Wedderburn split.
