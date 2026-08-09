---
# qou-7gei
title: 'GAP: vanishing_step''s combinatorial input is a HYPOTHESIS, not a proved Young-diagram fact -- discharge it with the repo''s own eraseCorner'
status: todo
type: task
created_at: 2026-08-09T16:48:48Z
updated_at: 2026-08-09T16:48:48Z
---


Branch: claude/anchor-followups-2026-08-08. Blocks the honesty of qou-u2jg T5.
Parent result: QOU/QBeta/TemperleyLiebTower.lean, section Propagation.

## THE GAP, stated exactly

`vanishing_step` / `vanishing_all_levels` derive the >= 3-row weight vanishing at
all n >= 3 from the n = 3 pinning -- so Wenzl's theorem is a corollary, not a
citation. But they take THREE hypotheses, and only one of them is proved:

  hbranch  branching coherence, sum over lambda covering mu of y_lambda[n+1]
           = y_mu[n].
           STATUS: proved in closed form as markov_branching_general, but NOT
           connected to the abstract `covers` in vanishing_step. Two statements
           of the same fact, not yet identified.
  hnn      nonnegativity, y_lambda >= 0.
           STATUS: MEASURED -- zero negative weights at n = 2..7 at 50 dps.
           Not proved. It should follow from positivity of the trace.
  hpred    THE ONE THIS BEAN IS ABOUT. Every partition of n+1 with >= 3 rows
           covers some partition of n with >= 3 rows, for n+1 >= 4.
           STATUS: verified by EXHAUSTION at n+1 = 4,5,6,7 -- no exceptions --
           and stated as a hypothesis in the Lean signature so the dependency is
           visible rather than buried in a sorry. NOT PROVED.

A hypothesis in the signature is honest. It is not finished.

## WHY IT IS TRUE, and the proof is short

Let lambda = (l_1 >= l_2 >= ... >= l_r) with r >= 3 and |lambda| = n+1 >= 4.
Claim: some removable corner of lambda can be deleted leaving >= 3 rows.

  CASE r >= 4. Delete any removable corner. Removing a box drops the row count
    only when it is the last box of the last row, so at worst r -> r-1 >= 3.
  CASE r = 3, l_3 >= 2. Delete the corner at the end of row 3. Still 3 rows
    because l_3 - 1 >= 1.
  CASE r = 3, l_3 = 1, l_1 > l_2. Delete the corner at the end of row 1. Valid
    since l_1 - 1 >= l_2. Still 3 rows.
  CASE r = 3, l_3 = 1, l_1 = l_2, l_2 >= 2. Delete the corner at the end of row
    2. Valid since l_2 - 1 >= 1 = l_3. Still 3 rows.
  CASE r = 3, l_3 = 1, l_1 = l_2 = 1. Then lambda = (1,1,1) and |lambda| = 3.
    EXCLUDED by |lambda| >= 4.

The |lambda| >= 4 hypothesis is used EXACTLY ONCE, in the final case, and that
single case is precisely why n = 3 is the base of the induction rather than a
step: (1^3) covers only (1^2), which has two rows. Do not lose that when
formalising -- it is the content, not an edge case.

## THE MACHINERY ALREADY EXISTS IN THIS REPO -- do not rebuild it

`QOU/Mathlib/YoungDiagramCorner.lean`:

    IsCornerCell mu c  :=  c in mu  /\  (c.1+1, c.2) not in mu
                                    /\  (c.1, c.2+1) not in mu     (:27)
    eraseCorner mu c hc : YoungDiagram                             (:33)
    mem_eraseCorner                                                (:54)
    card_eraseCorner : (eraseCorner mu c hc).cells.card + 1
                         = mu.cells.card                           (:61)

Mathlib supplies `YoungDiagram`, `rowLen`, `colLen`, `rowLen_anti`,
`colLen_anti`, `mem_iff_lt_rowLen`, `mem_iff_lt_colLen`, `transpose`,
`YoungDiagram.card`. Mathlib has NO corner API -- the repo's is the one to use.

Downstream users of the same machinery, worth reading for idiom before writing
anything: `SYTInsertMax`, `SYTEraseMax`, `SYTBranchingRule`,
`SYTBranchingBijection`, `SYTCornerListConnection`, `SYTMaxCorner`.

KEY ENCODING NOTE: "number of rows" is `mu.colLen 0`. So ">= 3 rows" is
`3 <= mu.colLen 0`, and the target statement is

    theorem exists_threeRow_corner (mu : YoungDiagram)
        (hrows : 3 <= mu.colLen 0) (hcard : 4 <= mu.cells.card) :
        exists c, exists hc : IsCornerCell mu c,
          3 <= (eraseCorner mu c hc).colLen 0

## THE PLAN

  [ ] 1. Prove `exists_threeRow_corner` as above, by the five-case analysis, in
         a NEW file QOU/Mathlib/YoungDiagramThreeRowCorner.lean (do not enlarge
         YoungDiagramCorner.lean -- it is shared with the SYT cluster).
         The likely-fiddly part is turning "l_1 > l_2" style row comparisons
         into corner-cell membership facts; `mem_iff_lt_rowLen` and
         `rowLen_anti` are the bridge. Consider whether the transpose trick
         (">= 3 rows for mu" = ">= 3 in rowLen 0 of mu^T") shortens any case.
  [ ] 2. Instantiate `vanishing_step`'s `hpred` with it -- Shape n := partitions
         of n, covers := the corner-addition Finset, rows := colLen 0. That
         needs a Finset of covers; check whether SYTBranchingRule already builds
         it (`branchInv` takes a sigma over corner cells, so something close
         exists).
  [ ] 3. Discharge `hbranch` by identifying markov_branching_general's closed
         form with the abstract `covers` sum. This is the real remaining work of
         the three and may be larger than 1 and 2 together.
  [ ] 4. Discharge `hnn` from positivity of the Markov trace. Check first
         whether the corpus already has a positivity statement to cite --
         GramSignature.starform_M2_nonneg and markov_star_nonneg are adjacent
         but are about the STAR FORM, not the weights, so do not assume they
         transfer.

## SCOPE DISCIPLINE

Items 1 and 2 are in MY territory. Item 3 touches the trace layer, also mine.
Item 4 may touch the Hecke layer -- the sibling owns QOU/Hecke/** and
QOU/Machinery/MarkovTraceH4* (see docs/coordination/hecke-tower-and-trace-parameter.md
and litlfred/qou#4857). Coordinate before writing there.

## DEFINITION OF DONE

`vanishing_step` and `vanishing_all_levels` take no unproved combinatorial
hypothesis, and the >= 3-row vanishing at all n >= 3 rests only on the n = 3
pinning plus proved facts. Until then, qou-u2jg's claim that "Wenzl is a
corollary, not a citation" is true of the ARGUMENT and not yet of the LEAN.
Say it that way in any exposition.

## UPDATE -- ITEM 1 DONE. The Young-diagram fact is PROVED.

QOU/Mathlib/YoungDiagramThreeRowCorner.lean (NEW), sorry-free, lake build exit 0
no warnings, axioms [propext, Classical.choice, Quot.sound]. Imported from
QOU.lean so it is not another orphan.

    theorem exists_threeRow_corner (mu : YoungDiagram)
        (hrows : 3 <= mu.colLen 0) (hcard : 4 <= mu.cells.card) :
        exists c, exists hc : IsCornerCell mu c,
          3 <= (eraseCorner mu c hc).colLen 0

TWO ENCODING FACTS collapsed the work far below the estimate:

  * "at least three rows" IS `(2,0) in mu`. Via mem_iff_lt_colLen, and then via
    mem_eraseCorner the GOAL becomes `(2,0) in mu AND (2,0) != c` -- whose first
    conjunct is the hypothesis. So the whole theorem is just "there exists a
    corner other than (2,0)". That is the trick; without it this is a slog.
  * The LAST CELL OF THE LAST ROW IS ALWAYS A CORNER, in closed form with no
    search: (colLen 0 - 1, rowLen (colLen 0 - 1) - 1). Lemma isCorner_lastRow.

Then three cases, each exhibiting an explicit corner: the last-row corner if it
is not (2,0); the row-0 corner if row 1 is shorter than row 0; the row-1 corner
otherwise. Supporting lemmas isCorner_rowEnd, rowLen_pos_of_lt_colLen,
rowLen_eq_zero_of_colLen_le, card_le_three_of_rowLen_zero_le_one.

THE CARDINALITY HYPOTHESIS IS USED EXACTLY ONCE, as predicted -- three rows plus
a one-cell third row plus rowLen 0 = 1 forces mu = (1,1,1), three cells. The
docstring says in terms so it cannot be "simplified" away by a later reader: it
is what makes n = 3 the BASE CASE rather than a step.

TWO SNAGS WORTH RECORDING for whoever does items 2-4:
  * `interval_cases` needs `import Mathlib.Tactic.IntervalCases` explicitly; it
    is not pulled in by the corner file's existing imports.
  * omega treats `mu.rowLen (1 + 1)` and `mu.rowLen 2` as DISTINCT ATOMS. Two
    `norm_num` bridging hypotheses fix it. This will recur in item 2.

## CORRECTION TO AN EARLIER CLAIM IN THIS BEAN

I wrote that the corner machinery "already exists, do not rebuild it" -- true --
but also implied the cost was mostly in fighting rowLen/colLen. It was not; the
(2,0) reduction removed nearly all of it. The remaining items should be
re-estimated rather than inheriting that guess.

## REMAINING

  [x] 1. exists_threeRow_corner -- DONE.
  [ ] 2. Instantiate vanishing_step's hpred with it. Needs Shape n := partitions
         of n, covers := the corner-ADDITION Finset (this file gives corner
         REMOVAL; the covering relation is its converse), rows := colLen 0.
         Check SYTBranchingRule.branchInv first -- it takes a sigma over corner
         cells, so the Finset may already exist.
  [ ] 3. Discharge hbranch: identify markov_branching_general's closed form with
         the abstract `covers` sum. STILL the largest of the four.
  [ ] 4. Discharge hnn from positivity of the Markov trace. May touch the
         sibling's territory -- coordinate first, see
         docs/coordination/hecke-tower-and-trace-parameter.md.

Until 2-4 land, qou-u2jg's "Wenzl is a corollary, not a citation" remains true
of the ARGUMENT and not yet of the LEAN.

## ALSO CONFIRMED WHILE HERE: the orphan diagnosis was right

The lakefile has `[[lean_lib]] name = "QOU"` with srcDir = "." and NO `globs`
field, so the default `globs = [.one "QOU"]` applies: only QOU.lean's import
closure is built. #4857's PR body describes a widened glob `["QOU", "QOU.+"]`,
which is NOT present on this branch's lakefile -- so on main today, a module not
imported from QOU.lean is genuinely never compiled. If their glob change merges
the problem disappears; importing explicitly is correct and harmless either way.
