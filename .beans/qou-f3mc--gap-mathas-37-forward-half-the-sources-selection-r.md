---
# qou-f3mc
title: 'GAP: Mathas 3.7 forward half -- the source''s selection rule for the inductive step is wrong; find a correct one'
status: todo
type: task
priority: high
created_at: 2026-09-06T15:03:40Z
updated_at: 2026-09-06T15:48:50Z
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
