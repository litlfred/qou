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
