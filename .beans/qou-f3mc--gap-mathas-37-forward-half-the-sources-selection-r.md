---
# qou-f3mc
title: 'GAP: Mathas 3.7 forward half -- the source''s selection rule for the inductive step is wrong; find a correct one'
status: todo
type: task
priority: high
created_at: 2026-09-06T15:03:40Z
updated_at: 2026-09-06T15:04:39Z
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
