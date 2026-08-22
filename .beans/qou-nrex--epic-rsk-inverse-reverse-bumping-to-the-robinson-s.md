---
# qou-nrex
title: 'EPIC: RSK inverse — reverse bumping to the Robinson-Schensted bijection (taken over from the Schensted programme)'
status: in-progress
type: milestone
priority: normal
created_at: 2026-08-16T02:46:29Z
updated_at: 2026-08-22T12:26:05Z
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
