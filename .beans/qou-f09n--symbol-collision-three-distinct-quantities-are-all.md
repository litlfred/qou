---
# qou-f09n
title: 'SYMBOL COLLISION: three distinct quantities are all called c_2, and AGENTS.md calls the wrong one Taylor-exact'
status: todo
type: task
created_at: 2026-08-16T11:48:34Z
updated_at: 2026-08-16T11:48:34Z
---


## Not a contradiction — a collision. Retracting my own call.

I reported on PR #5210 that `qbeta_alpha_eff_ladder_reconciliation_probe`'s
`c_2 = -9/8` and the committed extraction's `c_2 = -1` were "two different
ladders" and "a live contradiction". **That was wrong.** They are the same
model, expanded two ways. Symbolically, `cos(alpha - u/2)*(1 - u^2)` divided
by its own `u^0` value `cos(alpha)`:

    u^0 coefficient = 1
    u^1 coefficient = tan(alpha)/2
    u^2 coefficient = -9/8          <-- = -1  +  (-1/8)

The `-1` is the coefficient of the **explicit multiplicative factor**
`(1 + c_2 u^2)`. The `-1/8` falls out of expanding the cosine. Their sum is
the total `u^2` coefficient of the normalised series. No number is wrong.

The `c_1 = tan(alpha)/2 != 0` vs the #1887 reframe's `c_1 = 0` is the SAME
issue, not a second one: the two parameterisations do not share a base point
(`Phi(0) = cos(alpha) != 1`), so their `c_k` are not the same coefficients.

## Three live meanings of `c_2`

| value | what it is | where |
|---|---|---|
| `-1` | coefficient of the explicit factor `(1 + c_2 u^2)` | `qbeta_utils.c3_target_at`, hardcoded |
| `-9/8` | total `u^2` coefficient of the normalised committed model | `qbeta_alpha_eff_ladder_reconciliation_probe` |
| `-8.00641` | bar-even part, exact in Q[sqrt 3] | `qbeta_c3even_exact_sseries_probe`, bean `8we6` |

Registry §2 already warns that attributes do not transfer across overloaded
symbols. This is that, three ways, in one channel.

## The actionable defect: AGENTS.md's "PROVED Taylor-exact"

AGENTS.md line 1062 (the `c_k` truncation-order banner) says:

> `c_2 = -1` is PROVED Taylor-exact

Under the natural reading of "Taylor" — the Taylor coefficient of the ladder
series — **the `u^2` coefficient is `-9/8`, not `-1`**. `-1` is the
coefficient of the explicit factor, which is *hardcoded* in the extractor
(`qbeta_utils.py`: `Q_N2 = Q_N1 * (1 + c_2 u^2)`, `c_2 = -1`), i.e.
definitional rather than derived. And per PR #5187 the Lean lemma about it is
a renaming: `1 - b^2 hbar^4 = 1 - (b hbar^2)^2` is `ring`-true, with the
substantive identification `asserted`, proved nowhere.

So the phrase is wrong on both halves: not "Taylor" (wrong coefficient) and
not "PROVED" (tautological lemma + hardcoded value).

**The irony is the point.** That same banner exists to stop a four-session
flip-flop caused by *"conflating 'N=3 beats 100x experimental' (true) with
'c_3 = -2 is Taylor-exact' (false)"*. It warns against this exact error class
for `c_3` while committing a version of it for `c_2`.

## What to do

1. **Do NOT change any number.** Nothing computes wrongly. This is naming.
2. **Register the three meanings** in the `ck-dk-canonical-registry` §2
   overloaded-symbol table, with distinct names — e.g. `c_2^factor = -1`,
   `c_2^series = -9/8`, `c_2^even = -8.00641`.
3. **Re-word AGENTS.md line 1062.** Proposed, for owner sign-off rather than
   unilateral edit (it is a STRICT banner and a contested channel):
   *"`c_2^factor = -1` is the explicit ladder factor's coefficient, fixed by
   construction, not derived; the normalised series' `u^2` coefficient is
   `-9/8`."*
4. **Withdraw the "contradiction" framing** wherever I put it — done here;
   also stated on #5210.

## Scope

No fit, nothing wired, no value changed. This is a naming/provenance defect,
not a numerical one — which is exactly why it survived: every consumer
computes correctly with its own `c_2`, and only a reader comparing two of
them sees a problem.
