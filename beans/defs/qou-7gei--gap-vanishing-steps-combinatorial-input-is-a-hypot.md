---
# qou-7gei
title: 'GAP: vanishing_step''s combinatorial input is a HYPOTHESIS, not a proved Young-diagram fact -- discharge it with the repo''s own eraseCorner'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T16:48:48Z
updated_at: 2026-11-17T12:41:36Z
parent: qou-0cyu
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

## UPDATE 2 -- ITEM 4 DONE, ITEM 3 MOSTLY DONE. Three of four hypotheses discharged.

All sorry-free, lake build exit 0 no warnings, axioms clean;
traceRadical_star_eq needs only [propext, Quot.sound].

  [x] 4. hnn NONNEGATIVITY -- DONE, and it turned out nearly free once the
         weights were actually DEFINED. Until now `qint` and `yw` existed only
         in docstrings: the file reasoned through the abstracted numerators X, Y
         of qint_three_term_pair, so nothing in it was named y_lambda and
         nothing could carry a sign. Two definitions later:

             qint q m := (q^m - (q^-1)^m)/(q - q^-1)
             yw q n m := qint q m / (q + q^-1)^n

             qint_pos    0 < [m]_q for m >= 1 and q > 1
             yw_pos      EVERY SURVIVING WEIGHT IS STRICTLY POSITIVE, at every
                         n simultaneously
             yw_nonneg   and every weight is >= 0

         yw_pos is doing double duty: it is hnn, and it is also the only new
         input T4 needed.

  [~] 3. hbranch -- the MATHEMATICAL half is done. qint_three_term proves
         [m+2] + [m] = [2][m+1] on the DEFINED qint, and yw_branching proves
             yw q (n+1) (m+2) + yw q (n+1) m = yw q n (m+1)
         at every level. What remains is pure INDEXING: relating those two
         summands to "the two ways of adding a box to a two-row diagram", i.e.
         connecting m = n - 2k + 1 to the covers Finset. Bookkeeping, not a new
         fact. I over-estimated this item twice; it was the smallest of the
         three, not the largest.

  [ ] 2. Instantiate hpred. Still open, and now the ONLY substantive item.

## SNAG WORTH RECORDING -- field_simp is WRONG under a variable exponent

`yw_branching` first attempt used `field_simp; ring` and failed: field_simp
rewrote the BASE of `(q + q^-1)^n` into `(q^2 q^-1 + q^-1)^n`, after which ring
cannot reconcile two different bases under the same variable exponent `n`. The
fix is to cancel the single factor by hand:

    rw [pow_succ, mul_comm ((q + q^-1)^n) (q + q^-1)]
    exact mul_div_mul_left _ _ hs

This will recur anywhere the tower is indexed by n. Reach for mul_div_mul_left,
not field_simp, when a variable exponent is present.

## CORRECTIONS TO MY OWN ESTIMATES IN THIS BEAN

Twice now the estimate was wrong in the same direction -- I priced the algebraic
items high and the combinatorial item low, and the reverse was true. Item 1 fell
to the (2,0) reduction, items 3 and 4 fell to simply defining the weights. Item
2, which I listed as routine, is the one still standing. Do not carry the
original ordering into planning.

## UPDATE 3 -- ITEM 2 DONE. All four hypotheses discharged.

  [x] 2. hpred INSTANTIATED on real Young diagrams. QOU.Mathlib.youngPred and
         QOU.Mathlib.threeRow_vanishing_all_levels, sorry-free, axioms clean.
         vanishing_step_dom and vanishing_all_levels_dom depend on NO AXIOMS.

### THE OBSTACLE, and how it was dissolved rather than solved

The blocker was NOT the combinatorics. It was that `vanishing_step` summed over
a `Finset (Shape (n+1))`, and instantiating that on Young diagrams needs
`Fintype {mu : YoungDiagram // mu.cells.card = n}` -- which Mathlib does not
have and which is a genuine piece of work.

It is not needed. The induction never uses the SUM; it uses only the
consequence that each cover's weight is at most its parent's:

    Cov n m l  ->  y[n+1] l <= y[n] m

which follows from branching plus nonnegativity in one line
(`dominates_of_branching`, via Finset.single_le_sum) and which makes `Cov` a
bare Prop. No finiteness, no Finset, no decidability, same conclusion. New
theorems vanishing_step_dom / vanishing_all_levels_dom.

WEAKER HYPOTHESES PROVING THE SAME THING was the whole trick. Worth remembering:
when an abstraction demands machinery, check whether the proof actually uses the
part that demands it.

Shapes are written INLINE as {mu : YoungDiagram // mu.cells.card = n} rather
than behind a def, so subtype projections stay definitionally transparent and no
unfolding lemmas are needed.

### WHERE THE FOUR HYPOTHESES NOW COME FROM

  hpred    QOU.Mathlib.youngPred                    (this bean, items 1 + 2)
  hnn      TemperleyLiebTower.yw_nonneg             (item 4)
  hdom     TemperleyLiebTower.dominates_of_branching applied to yw_branching
                                                    (item 3)
  base     TemperleyLiebTower.conventionD_kills_antisymmetriser  (qou-u2jg)

### WHAT IS STILL NOT DONE -- do not overstate this

threeRow_vanishing_all_levels is stated FOR AN ARBITRARY weight function y
satisfying the four hypotheses. Wiring the framework's ACTUAL y_lambda into it
requires indexing the closed form yw q n m by Young diagrams rather than by the
integer m = n - 2k + 1, i.e. a map from two-row shapes to m. That is the last
piece of glue and it is not written. So:

  * the ARGUMENT is complete and every step of it is machine-checked;
  * the CHAIN from conventionD_kills_antisymmetriser to "y_lambda = 0 for all
    >= 3-row lambda at all n" is not yet a single Lean term.

Say it that way in exposition. "Wenzl is a corollary, not a citation" is now
true of the argument AND of every individual step, but the steps are not yet
composed into one theorem about the framework's own weights.

### A PROCESS NOTE

I hit the `omit ... in` placement trap AGAIN -- it must precede the DOCSTRING,
not sit between docstring and theorem. That is twice in one session on a rule I
had already written down. The comment is now in the source at both sites.

## UPDATE 4 -- the base case collapses to ONE SCALAR. Boundary of this layer reached.

  card_three_threeRow_unique        at 3 cells there is exactly ONE three-row
                                    shape, namely (1^3): three rows forces
                                    (0,0),(1,0),(2,0) in mu, that is already
                                    three cells, and card = 3 leaves no room.
  threeRow_size_three_subsingleton  hence any two such shapes are EQUAL
  threeRow_vanishing_of_pinning     so `base` stops being a quantified statement
                                    and becomes a SINGLE SCALAR INPUT -- exactly
                                    what conventionD_kills_antisymmetriser gives

All sorry-free, axioms clean, lake build exit 0 no warnings.

## THE BOUNDARY, named rather than papered over

This is as far as THIS LAYER can honestly go. Going further means asserting that
the framework's y_lambda IS the Wedderburn weight of the Markov trace, i.e.
tr_M = sum_lambda y_lambda chi_lambda. That is a statement about CHARACTERS and
the WEDDERBURN DECOMPOSITION -- representation theory this module deliberately
does not carry, and which the Hecke-instance layer (QOU.Hecke, PR #4857) is
building. The seam is recorded in
docs/coordination/hecke-tower-and-trace-parameter.md.

WHY THE RESULT IS STILL NON-VACUOUS, and this matters: nothing here DEFINES y to
be zero anywhere. y is any function satisfying the four hypotheses, and the
theorem is a genuine implication -- a single zero at n = 3 propagates to every
level. The one place a reader could be misled is `hpin`, which is an INPUT, not
a conclusion. What is proved is the propagation, not the zero.

I considered defining y as "yw on two-row shapes, 0 on >= 3-row shapes" to force
a composition. That would have been VACUOUS -- the base case would hold by
definition rather than by the pinning -- and it is exactly the failure mode this
repo's vacuity-audit skill exists to catch. Rejected deliberately; recorded so
nobody tries it later thinking it closes the gap.

## STATUS OF THE BEAN

  [x] 1. exists_threeRow_corner
  [x] 2. hpred instantiated on Young diagrams (youngPred)
  [x] 3. hbranch -- mathematical half (qint_three_term, yw_branching); the
         remaining half is the same indexing question as the boundary above
  [x] 4. hnn (yw_nonneg)
  [x] 5. NEW -- base collapsed to one scalar (threeRow_vanishing_of_pinning)
  [ ] 6. BLOCKED ON THE HECKE LAYER: identify y with the Wedderburn weights, so
         the chain becomes one theorem about the framework's own y_lambda rather
         than about an arbitrary y. Coordinate with PR #4857; do not build a
         second Wedderburn apparatus here.

Exposition wording, unchanged and still required: "Wenzl is a corollary, not a
citation" is true of the ARGUMENT and of every individual step, and is NOT yet
true of a single Lean term about the framework's weights.


---

## 2026-09-08 — NOT closeable: item 6 of this bean's own checklist is open. Read for the completion-candidate queue.

`scripts/bean-completion-candidates.py` flags this bean on `4c62d30af32`,
*"lean: close qou-7gei **item 2** — all four propagation hypotheses discharged"*.
That is cause 1 in the tool's own taxonomy (partial completion), and the bean's
own STATUS block confirms it:

    [x] 1 exists_threeRow_corner
    [x] 2 hpred instantiated on Young diagrams (youngPred)
    [x] 3 hbranch — mathematical half
    [x] 4 hnn (yw_nonneg)
    [x] 5 base collapsed to one scalar (threeRow_vanishing_of_pinning)
    [ ] 6 BLOCKED ON THE HECKE LAYER

Item 6 — identifying `y` with the Wedderburn weights so the chain becomes one
theorem about the framework's own `y_λ` rather than about an arbitrary `y` —
requires representation theory this module deliberately does not carry, and is
being built in the Hecke-instance layer (PR #4857). The seam is recorded in
`docs/coordination/hecke-tower-and-trace-parameter.md`.

**Do not close and do not re-attack item 6 here.** The bean's own instruction is
*"Coordinate with PR #4857; do not build a second Wedderburn apparatus here."*
It also records a rejected shortcut worth keeping visible: defining `y` as *"yw
on two-row shapes, 0 on ≥3-row shapes"* would make the base case hold **by
definition** rather than by the pinning — vacuous, and exactly what the
vacuity-audit skill exists to catch.

### Progress Update (Round 67 — PR litlfred/qou#8346)
- **PR:** https://github.com/litlfred/qou/pull/8346 (`2c3a7bfb0c79ccd01acb2c398dcf5d428cbb2d13`)
- **Lean 4 Module:** `QOU.Foundations.ProjectorBranchingThreeRowCornerDeletionGenerictyEquivalenceQuotientPairingDiagonalTrace` (`LEAN_EXIT=0`, `0` warnings, `0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 major, 0 advisory` across all 6 directory-mode static vacuity & borrowed-name audits)
- **Numerical Probe & Witness:** `computations/probes/projector_branching_three_row_corner_deletion_genericity_equivalence_quotient_pairing_diagonal_trace_probe.py` & `computations/probes/projector-branching-three-row-corner-deletion-genericity-equivalence-quotient-pairing-diagonal-trace.witness.json` (`COMMIT1 = cb6750d2375a33fa0ecc4e3b1af425657b51686d`, `scriptHash = fc06654c2e67`, `allPassed = True`, `dps = 80`)
