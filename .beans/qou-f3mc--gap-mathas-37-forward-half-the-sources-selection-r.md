---
# qou-f3mc
title: 'GAP: Mathas 3.7 forward half -- the source''s selection rule for the inductive step is wrong; find a correct one'
status: todo
type: task
priority: high
created_at: 2026-09-06T15:03:40Z
updated_at: 2026-09-06T22:25:41Z
---

## What is open

Mathas' Proposition 3.7 (Dipper-James) says: for row-standard lambda-tableaux `s` and `t`,
`s |>= t` (dominance) iff `d(s) <= d(t)` (Bruhat, order-REVERSING -- see
`QOU/BraidKnot/DominanceIsBruhat.lean`).  The STATEMENT is measured true, both directions,
708062/708062 over every ordered pair of row-standard tableaux of every partition of n <= 6
(`computations/hecke/dipper_james_dominance_is_bruhat_probe.py`).

The forward half's Lean proof is `sorry`.  Its proof route was believed unblocked once
#6894 supplied the reflection Bruhat order.  It is not, and the reason is NOT on the
Coxeter side.

## The measurement

`computations/hecke/dipper_james_forward_step_probe.py` transcribes the source's inductive
step -- r = least differing row, a = least in row r of s but not of t, b = least in row r
of t but not of s, v = t(a,b) -- and measures each clause separately.  At n = 6, over
142314 ordered pairs with s |> t strictly:

    a_lt_b          142314/142314   100.0%   ok
    v_dom_t         142314/142314   100.0%   ok
    bruhat_dv_dt    142314/142314   100.0%   ok
    raw_rowstd      129833/142314    91.2%   FAILS
    one_step        129833/142314    91.2%   FAILS
    s_dom_v         112096/142314    78.8%   FAILS
    step_exists     142314/142314   100.0%   ok

`s_dom_v` is the substantive failure: Mathas justifies "either v = s or s |> v" with
"t > r and t >= s", i.e. a's row in t is at or below b's row in s -- which is the condition
that PRODUCES the overshoot, not one that prevents it.  Worked instance, verified by hand
and by probe:

    lambda = (2,1,1)
    s = ((1,2),(4),(3))      t = ((1,4),(3),(2))     s |> t
    r = 0, a = 2, b = 4, a < b
    v = t(2,4) = ((1,2),(3),(4))
    v |> t  ok ;  but  s |>= v  is FALSE -- at i=1, m=3 the counts are s:2 v:3

`raw_rowstd` / `one_step` fail together and cost less: when the raw swap leaves a row
unsorted, v is still the right TABLOID but is no longer `(a,b).t` as a TABLEAU, so the
single left-reflection-step route to `d(v) |> d(t)` (via `bruhatLe_of_leftReflLe_An`, landed
this branch) is unavailable for those pairs.  `d(v) <= d(t)` itself holds throughout.

## Why this is a repair, not a refutation

`step_exists` is 142314/142314: for EVERY such pair there IS a transposition meeting all of
Mathas' conditions at once -- raw swap row standard, `s |>= v |> t`, `d(v) = (a,b).d(t)`,
length down.  So the induction is sound and only the SELECTION RULE is wrong.  3.7 is not
in doubt, and neither necessarily is Mathas: the source is OCR, and the sentence carrying
the failing clause prints its two ROW INDICES as `s` and `t` -- the same glyphs as the two
tableaux.

## Rules already measured -- do not re-try these

At n = 6, hits against the brute-force valid set, out of 142314:

    Mathas     102404   71.9%
    lowrow      95044   66.8%
    deep        98448   69.2%
    a_bmin     111474   78.3%
    bmax_a     119640   84.1%   best measured

The one structural hint: both `b`-side repairs beat both `a`-side ones.  Mathas' `b` --
least in row r of t but NOT in row r of s -- is the wrong constraint; the valid set
repeatedly wants a `b` that IS in row r of s, which his definition can never return.

A per-element "do not overshoot" criterion is ruled out: the valid set contains steps that
send a label BELOW the row `s` puts it in, because dominance is a global count comparison.

## Next honest steps, in order of my judgement of cost

1. Extract a rule from the brute-force valid set by looking at which pairs are valid when
   several are (the probe prints them).  Cheap, and 84.1% says the space is nearly right.
2. Look for the Dipper-James original, [dipper-james1986] -- Mathas' note 1 to Chapter 3
   says "the proof of Proposition 3.7 comes from [13]".  Not currently in `library/`;
   corpus-grep path 5 returns nothing for it.
3. Abandon the transposition induction and prove 3.7 from a rank/count criterion on both
   sides (Ehresmann's tableau criterion for Bruhat against the dominance counts).  That
   removes the selection problem entirely and is a much larger Mathlib gap.

## Blast radius

`dominance_to_bruhatLe` is consumed by nothing yet.  It is wanted by
`MurphyInductionMeasure.murphyLex`, whose inner axis is dominance-on-tabloids: 3.7 is what
identifies that axis with Bruhat, which is the order Mathas' Corollary 3.8 -- the one 3.14's
induction closes on -- actually speaks about.  The converse half is separately blocked on
bean `qou-3k66` (`BruhatLe -> ReflLe`).


## UPDATE — one of the two obstructions is gone, and it is proved away

The `raw_rowstd` / `one_step` clauses (91.2 %) **dissolve**.  When the raw swap leaves a
row unsorted, `d(v)` for the row-standard representative `v` is the DISTINGUISHED
(minimal-length) representative of the coset `S_lambda . d((a,b).t)`, so `l` is additive
across that factorisation and a reduced word for `d(v)` is a PREFIX of one for
`d((a,b).t)` -- hence a subword, hence `d(v) <= d((a,b).t) <= d(t)`.

Measured first, over EVERY transposition of every row-standard tableau rather than the
chosen one: **2134710/2134710** at n = 6 (`coset_bound` in the probe).

Then proved, sorry-free: `CoxeterBruhat.bruhatLe_of_length_add` and
`bruhatLe_of_length_add_right`, both `[propext, Classical.choice, Quot.sound]`.  The
corpus's own unconditional Bourbaki lifting lemma
`CoxeterReflectionCocycle.length_minRep_mul_wordProd'` supplies the hypothesis for a
tableau's `d`.

**So `s |>= v` is now the ONE remaining failing clause.**  Under the relaxed valid set
(`valid_pairs_relaxed`, which drops row-standardness of the raw swap) Mathas' rule scores
exactly the `s_dom_v` count, 112096/142314.

## Seven rules measured, relaxed column -- do not re-try

    Mathas     112096   78.8%   = the s_dom_v count exactly
    lowrow     107740   75.7%
    deep       109684   77.1%
    a_bmin     113374   79.7%
    minlift    118814   83.5%
    lift1b     123121   86.5%
    bmax_a     124391   87.4%   best measured

Two NEW negative hints beyond the b-side one already recorded, both from the two new rules:

* `minlift` (lift the least misplaced label as HIGH as it can go) OVERSHOOTS;
* `lift1b` (lift it exactly ONE row) UNDERSHOOTS;
* and there are pairs whose only valid steps DO NOT MOVE THE LEAST MISPLACED LABEL AT ALL
  -- worked case, lambda = (2,1,1), s = ((1,2),(4),(3)), t = ((1,4),(3),(2)): the least
  misplaced label is 2, and the valid step swaps 3 and 4, leaving 2 where it is.

So no rule of the form "identify the offending label, move it" can be right.  A correct
rule has to be a statement about the count vectors, not about a distinguished label.  That
is also an argument for next-step (3) below -- the rank/count criterion -- over (1).


## UPDATE 2 — the transposition induction is the WRONG ROUTE, and the CONVERSE half is unblocked

The negative above ("no rule that names a label can be right") points somewhere specific.
Measured in `computations/hecke/dipper_james_rank_criterion_probe.py`, n <= 6.

Write `rank(u,i,m) = #{x < i : u(x) < m}` and let `N_i = mu_0 + ... + mu_i` be the ROW
BOUNDARIES.  All four hold at every n:

    s |>= t   iff   rank inequality at the BOUNDARIES N_i        708062/708062
    u <= w    iff   rank inequality at EVERY i (Ehresmann)       708062/708062
    boundary => full, for d-images                               143916/143916
    full => boundary, by specialisation                          143916/143916

The first is an IDENTITY, not a coincidence.  `d(t)` sends a reference label to `t`'s label
at the same cell and `refTab` is row-superstandard, so the row of `y` in `t` is the block of
`d(t)^-1(y)`, whence

    domCount (rowPattern t) i m  =  #{x < N_i : d(t) x < m}  =  rank (d t) N_i m.

**Dominance on tabloids IS a rank comparison on permutations, read only at the row
boundaries.**  3.7 carries no tableau content at all: both sides compare the rank matrices
of the SAME two permutations, and the whole difference is "at the boundaries" vs "at every
index", reconciled by `d` being a minimal coset representative (increasing within each
block, so its rank function is fixed by interpolation).

### Consequences

1. **The CONVERSE half no longer needs bean `qou-3k66`.**

       d(s) <= d(t)  ->  full rank        (EASY Ehresmann: a subword can only raise the
                                           rank matrix -- an induction on deletions, from
                                           the subword DEFINITION, no reflection order)
                     ->  boundary rank    (specialisation)
                     ->  s |>= t          (the identity above)

   `bruhatLe_to_dominance`'s docstring still names `qou-3k66`; that is the OLD route, kept
   until this one is built.  `qou-3k66` remains open and is still wanted elsewhere, but 3.7
   is no longer a reason to prioritise it.

2. **The FORWARD half is re-scoped, not unblocked.**  It still needs the HARD direction of
   Ehresmann (rank criterion => subword) plus the interpolation bridge.  That is a named
   classical theorem with a known proof (Bjorner-Brenti Thm 2.1.5) in place of a tableau
   selection rule that seven attempts failed to find -- a better place to be stuck, and a
   Mathlib-scale target rather than an open combinatorial question.

3. **Next steps, superseding the three above.**
   a. Prove the identity `domCount (rowPattern t) i m = rank (d t) N_i m` in Lean.  Pure
      bookkeeping over `refTab`; no new mathematics.
   b. Prove the EASY Ehresmann direction for `permCoxeterSystem` (subword => rank).  This
      closes the converse half.
   c. Prove the interpolation bridge for minimal coset representatives.  Elementary.
   d. The HARD Ehresmann direction.  Mathlib-scale; the only genuinely large piece left.


## UPDATE 3 — next-step (a) is DONE, sorry-free

`QOU/BraidKnot/DominanceIsBruhat.lean` now carries the identity, proved:

    rowPattern_dOf       rowPattern t (dOf t x) = rowPattern (refTab mu) x
    rankAt               the rank matrix of d(t), cut by refTab's rows
    domCount_eq_rankAt   domCount (tabloidRowPattern (mk t)) i m = rankAt t i m
    domRel_iff_rankAt    s |>= t  iff  forall i m, rankAt t i m <= rankAt s i m

All four `[propext, Classical.choice, Quot.sound]`, no `sorryAx`.  `rowPattern_dOf` is the
whole content and is two lines: `dOf t x = t^-1 (refTab x)`, so `t` sends `dOf t x` to the
cell `refTab` assigns to `x`, and that cell's row does not mention `t`.  Everything else is
reindexing the `domCount` filter along the bijection `dOf t`.

`rankAt` is stated against `rowPattern (refTab mu) x <= i` rather than a numeric boundary
`x < mu_0 + ... + mu_i`.  The two agree because `refTab` is row-superstandard, but that is
a separate fact about the reference tableau and nothing so far needs it -- do not add it
speculatively.

**So the left-hand column of 3.7 is now tableau-free in Lean.**  Remaining, unchanged:
(b) easy Ehresmann, which closes the CONVERSE half; (c) the interpolation bridge; (d) hard
Ehresmann.


## UPDATE 4 — next-step (b) is DONE.  Easy Ehresmann is PROVED, sorry-free.

New file `content/quantum-observable-universe/lean/QOU/Machinery/BruhatRankCriterion.lean`,
324 lines, **14 declarations, all `[propext, Classical.choice, Quot.sound]`, zero
`sorryAx`**:

    rk                             rk u i m = #{x < i : u x < m}
    rk_succ, rk_zero               the successor decomposition
    rk_mul_swap_eq                 right mult permutes POSITIONS; the swap moves into
                                   the position condition and leaves the value alone
    rk_mul_swap_of_ne              off the single cut i = j+1, rk is UNCHANGED
    rk_mul_swap_cut                at the cut, the two values are exchanged
    rk_castSucc_succ, rk_succ_succ the two cut decompositions
    rk_mul_swap_le                 STEP A
    rk_mul_swap_mono               STEP B
    permCoxeterSystem_simple'      the missing interface lemma: cs.simple i = swap
                                   i.castSucc i.succ.  Did not exist in the corpus.
    rk_mul_simple_le/_mono         A and B restated against COXETER LENGTH, via
                                   `Hecke.Inversions.length_mul_swap_eq_succ_iff`
    isReduced_of_isReduced_concat  a prefix of a reduced word is reduced, and the last
                                   letter is an ascent
    rk_le_of_sublist               the induction, right-to-left on the reduced word
    rk_le_of_bruhatLe              **BruhatLe -> rank inequality**

Formalize-first, and it mattered: both steps were measured over ALL of S_3..S_5 before any
Lean (`run_steps` in `dipper_james_rank_criterion_probe.py`; A 240/240, B 6204/6204 at
n = 5).  **Step B needs nothing of `u`**, which a hand argument does not predict -- the
naive case analysis stalls at `u(j+1) >= m > u(j)` and is rescued by the hypothesis at the
cut `j + 2`, not at `j` or `j + 1`.

`Hecke.Inversions.length_mul_swap_eq_succ_iff` already existed and is exactly the descent
bridge; corpus-grep found it rather than re-deriving it.

### What still separates this from closing `bruhatLe_to_dominance`

`rk` lives on `Fin (n+1)` with the cut `(x : N) < i`; `DominanceIsBruhat.rankAt` lives on
`Fin (nOf mu)` with the cut `rowPattern (refTab mu) x <= i`.  Two bridges remain, both
elementary and both deliberately deferred so far:

  (i)  transport along `toFinSucc hn : Fin (nOf mu) ~ Fin (n+1)`;
  (ii) `rowPattern (refTab mu) x <= i  <->  (x : N) < mu_0 + ... + mu_i`, the
       row-superstandard boundary fact.  `rankAt` was deliberately stated against the row
       pattern so this stayed optional; it is now needed.

Then: `d(s) <= d(t)` -> `rk_le_of_bruhatLe` -> specialise to the row cuts -> (ii) -> (i) ->
`domRel_iff_rankAt` -> `s |>= t`.  No `qou-3k66`.

### Remaining after that

(c) the interpolation bridge (boundary => full, for minimal coset reps) and (d) the HARD
direction of Ehresmann, which together close the FORWARD half.  (d) is the only
Mathlib-scale piece left in the whole arc.


## UPDATE 5 — the CONVERSE HALF OF 3.7 IS PROVED.  Steps (b) and its two bridges: DONE.

`bruhatLe_to_dominance` no longer carries a `sorry`:

    #print axioms QOU.BraidKnot.DominanceIsBruhat.bruhatLe_to_dominance
    -> [propext, Classical.choice, Quot.sound]

The chain, end to end, with no reflection order anywhere in it:

    d(s) <= d(t)
      -> rank inequality        BruhatRank.rk_le_of_bruhatLe   (easy Ehresmann, from the
                                                                SUBWORD definition)
      -> at the row cuts        rankAt_eq_rk                   (specialisation + transport)
      -> s |>= t                domRel_iff_rankAt              (the identity)

The two bridges, both proved this pass:

* `rowPattern_refTab_le_iff` -- the row cut IS an initial segment: `refTab` is
  row-superstandard, so a label sits in row <= i exactly when it is below
  `rowPrefix mu (i+1)`.  This is the fact `rankAt` was deliberately stated without.
* `rankAt_eq_rk` -- `rankAt` IS `rk` at that cut, after the value-preserving relabelling
  `toFinSucc`.  Plus `rk_eq_card` in `BruhatRankCriterion` to move between the sum-of-
  indicators and cardinality forms.

**`qou-3k66` was never needed for this.**  It stays open on its own merits, but 3.7 is no
longer a reason to prioritise it, and #6894's "what a consumer citing Mathas' Prop 3.7 needs
for an `↔`" is not true of this consumer.  I told them the opposite twice today and have
corrected it on that PR.

**An observation worth recording, not an oversight:** the row-standardness hypotheses
`hs`/`ht` are UNUSED in the converse.  `domRel` is a relation on tabloids and `dOf` is a
bijection on ALL tableaux, so the implication holds for arbitrary `mu`-tableaux.  They are
kept in the signature because the source states 3.7 for row-standard tableaux and the
FORWARD half does need them.

### What is left

`DominanceIsBruhat.lean` now carries exactly ONE `sorry`: `dominance_to_bruhatLe`.  It needs

  (c) the interpolation bridge -- boundary rank inequality => full, for minimal coset
      representatives.  Elementary; measured 143916/143916.
  (d) the HARD direction of Ehresmann: rank criterion => subword.  Bjorner-Brenti Thm 2.1.5.
      **This is now the only Mathlib-scale piece left in the whole arc.**

Steps (a) and (b) of UPDATE 2's plan are complete.


## UPDATE 6 — step (c), the interpolation bridge: the COXETER half is done.

Six more sorry-free declarations in `Machinery/BruhatRankCriterion.lean`, all
`[propext, Classical.choice, Quot.sound]`:

    rk_mono_index              rk is monotone in the index cut
    card_filter_val_Ico        #{x : Fin n | a <= x < i} = i - a, for i <= n
    rk_le_add_sub              rk u j m <= rk u i m + (j - i)  -- at most one per position;
                               needs NO hypothesis, not even i <= j
    IncreasingOn u a b         u strictly increasing across the window [a, b)
    rk_eq_add_of_all_lt        if every position in [a,i) has value < m, the rank is
                               rk u a m + (i - a) exactly
    rk_ge_min_of_increasingOn  inside an increasing window the rank is pinned from BELOW by
                               the endpoints: min(rk u b m, rk u a m + (i-a)) <= rk u i m
    rk_le_of_endpoints         THE BRIDGE -- a rank inequality at the two ENDPOINTS of a
                               window on which the DOMINATED permutation increases holds at
                               every index inside it

**Nothing is assumed of `w`.**  Its upper bound is monotonicity plus "at most one value per
position" and holds for every permutation.  Only `u` must increase, and only across the
window.  That asymmetry is what makes the bridge cheap.

Measured before written, `run_c` in `dipper_james_rank_criterion_probe.py`, over every
row-standard tableau of every partition of n <= 6:

    d(t) block-increasing   1602/1602      (n = 6)
    UPPER (any w)         122885/122885
    LOWER (increasing u)  122885/122885

### What is NOT done, and it is the tableau half

`rk_le_of_endpoints` is stated at the Coxeter level over an arbitrary window.  Wiring it to
3.7's forward half still needs two mu-level facts, neither hard but neither written:

  (c1) `dOf t` is `IncreasingOn` each row block when `t` is row standard.  This is where
       row-standardness finally EARNS its place in the signature -- it is unused in the
       converse (UPDATE 5) and this is the lemma that uses it.  `dOf t x = t.symm (refTab x)`
       is the label in cell `(r, j_x)`, and row-standard means those increase along a row.
  (c2) every index lies in some block `[rowPrefix mu r, rowPrefix mu (r+1))`.

Then boundary-rank => full-rank for `d`-images, and the forward half reduces to (d) ALONE.

### After that: only (d)

The HARD direction of Ehresmann -- rank criterion => subword, Bjorner-Brenti Thm 2.1.5.
That is the one Mathlib-scale piece in the arc and nothing else in 3.7 depends on anything
else.


## UPDATE 7 — (c1) is PROVED.  Row-standardness finally does work.

Six more sorry-free declarations in `DominanceIsBruhat.lean`:

    colPattern_dOf                  the column mirror of `rowPattern_dOf`
    refTab_val_eq                   (x : N) = rowPrefix mu (row x) + col x
    colPattern_refTab_lt            col x < rowLen (row x)
    rowPattern_refTab_eq_of_block   inside the window [rowPrefix r, rowPrefix (r+1)) the
                                    reference row IS r
    colPattern_refTab_eq_of_block   ...and the column is x - rowPrefix r
    dOf_increasingOn_block          **(c1)**: for row-standard t, `dOf t` is
                                    `IncreasingOn (rowPrefix mu r) (rowPrefix mu (r+1))`

**This is the first place row-standardness is used in the whole development.**  UPDATE 5
recorded that the converse half does not need it; this is the lemma that does.  The proof is
short because `rowPattern_dOf` / `colPattern_dOf` already reduce it to `IsRowStandard`'s own
statement: `dOf t x = t.symm (refTab x)` is the label `t` puts in the cell `refTab` assigns
to `x`, and `IsRowStandard t` says exactly that those increase along a row.

### (c2) is what is left, and the route is mapped

`∀ i <= nOf mu, ∃ r, rowPrefix mu r <= i /\ i <= rowPrefix mu (r+1)`.

The one input needed is that `rowPrefix` REACHES `nOf mu`, and the corpus already has it:
`SytRowSuperstandard.card_eq_sum_rowLen : mu.cells.card = sum over range (colLen 0) of rowLen`,
which is literally `rowPrefix mu (colLen 0) = nOf mu`.  Given that,
`r := Nat.find (exists r, i <= rowPrefix mu (r+1))` works, with minimality supplying
`rowPrefix mu r <= i` (and `r = 0` handled by `rowPrefix_zero`).

Then the wiring, which also needs two small `rk` facts:

  * `rk u i m = rk u n m` for `n <= i` -- so an index past the end reduces to the last cut;
  * the `r = 0` endpoint is free, since `rk _ 0 m = 0` on both sides (`rk_zero`).

and the final theorem is

    rankAt t i m <= rankAt s i m for all i m   ->   rk (dOf t) i m <= rk (dOf s) i m for all i m

by `rk_le_of_endpoints` on each block, with `hs : IsRowStandard s` supplying the increasing
hypothesis for the DOMINATING permutation `dOf s`.  Note `ht` is NOT needed even here --
only the `u` side of `rk_le_of_endpoints` carries a hypothesis.

I stopped short of (c2) deliberately: it is `YoungDiagram` bookkeeping (row lengths vanish
past `colLen 0`), orthogonal to the mathematics, and the session had run long.  Nothing about
it is uncertain.

### Then (d) alone

The HARD direction of Ehresmann -- rank criterion => subword, Bjorner-Brenti Thm 2.1.5.


## UPDATE 8 — step (c) is COMPLETE.  3.7's forward half is now ONE classical theorem.

`dominance_to_bruhatLe` is a two-line composition:

    QOU.Machinery.BruhatRank.bruhatLe_of_rk_le
      (rk_le_of_rankAt_le hn hs ((domRel_iff_rankAt _ _).mp hdom))

**READ THIS BEFORE QUOTING ANYTHING: `dominance_to_bruhatLe` STILL DEPENDS ON `sorryAx`.**
`DominanceIsBruhat.lean` now compiles with ZERO warnings and contains no `sorry` token, and
that is NOT the same statement.  The `sorry` moved to `bruhatLe_of_rk_le` in
`Machinery/BruhatRankCriterion` and propagates:

    dominance_to_bruhatLe  -> [propext, sorryAx, Classical.choice, Quot.sound]
    bruhatLe_of_rk_le      -> [propext, sorryAx, Classical.choice, Quot.sound]
    everything else new    -> [propext, Classical.choice, Quot.sound]

What changed is WHERE the gap is, and that is worth something: it is now the **hard direction
of Ehresmann's criterion** -- rank criterion => subword, Bjorner-Brenti Thm 2.1.5 -- a named,
citable statement about Coxeter groups with no tableau content, stated with a `-- Ref:` per
the state-and-queue disposition.  Previously it was a tableau selection rule that seven
attempts failed to find and whose negatives say no label-naming rule can work.

### New this pass

    rowPrefix_colLen_zero    rowPrefix mu (colLen 0) = nOf mu -- from the corpus's own
                             card_eq_sum_rowLen, not re-derived
    exists_block             **(c2)**: every i <= nOf mu lies in some row block
    rk_eq_of_index_ge        past the last index there is nothing left to count
    IncreasingOn.mono_right  a shorter window is a weaker hypothesis
    rk_le_of_rankAt_le       **the whole of step (c)**: rank inequality at the ROW CUTS
                             gives one at EVERY index
    bruhatLe_of_rk_le        the named gap (sorry + Bjorner-Brenti citation)

`rk_le_of_rankAt_le` takes `IsRowStandard s` -- the DOMINATING tableau -- and not `t`, because
`rk_le_of_endpoints` carries a hypothesis only on its `u` side.  So `_ht` is unused in
`dominance_to_bruhatLe` as well, and it is now the ONLY unused hypothesis in either half.

### Status of the whole arc

    3.7 converse   PROVED, sorry-free
    3.7 forward    proved modulo Bjorner-Brenti Thm 2.1.5, nothing else
    (a) (b) (c)    all done
    (d)            the one Mathlib-scale piece
