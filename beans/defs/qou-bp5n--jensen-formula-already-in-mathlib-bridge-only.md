---
# qou-bp5n
title: 'BRIDGE(lean): Jensen formula + Nevanlinna counting are ALREADY in Mathlib — wire, do not rebuild'
status: todo
type: task
priority: normal
tags:
    - lean
    - hadamard
    - correction
    - paper-qou
    - reorg-2026-10-04
created_at: 2026-08-08T03:30:00Z
updated_at: 2026-10-04T15:16:44Z
parent: qou-c8p8
---

## Why this bean exists at all — a correction to my own claim

On 2026-08-08 I wrote, in a commit message and to the user, that PI-5 "needs
Jensen's formula, zero-counting, and Borel-Carathéodory machinery, none of which
Mathlib v4.24.0 has in usable form."

**That is wrong for two of the three.** Enumerating the environment (not
grepping filenames) turns up:

    MeromorphicOn.circleAverage_log_norm                     -- Jensen's formula
    AnalyticOnNhd.circleAverage_log_norm_of_ne_zero          -- the nonvanishing case
    ValueDistribution.logCounting                            -- N(r, a), via
                                                             -- MeromorphicOn.divisor
    ValueDistribution.proximity, .characteristic             -- m(r,a), T(r,f)
    ValueDistribution.first main theorem lemmas

Worse: `QOU/Mathlib/HadamardFactorization.lean`'s own module docstring said so
all along — "Mathlib has Jensen's formula, the Nevanlinna value-distribution
cone (`Analysis/Complex/ValueDistribution/`)". I contradicted a correct
statement sitting in the file I was editing.

Only **Borel-Carathéodory** was genuinely absent, and it is now done
(bean qou-8cwi).

## Do

Not "add Jensen". Find out how much of the bridge is already free:

1. Read `ValueDistribution.logCounting`'s definition. It is
   `Function.locallyFinsuppWithin.logCounting (MeromorphicOn.divisor ...)`.
   Determine whether it already equals the classical `N(r) = sum_{|a_n|<r} log(r/|a_n|)`
   or needs an unfolding lemma.
2. If it does, the Hadamard step "exponent of convergence <= order" (bean
   qou-c3if) may be a short derivation rather than a build.
3. Only then write anything.

## ROAST

**"So is there any work in this bean at all?"** Possibly very little, and that is
the honest answer until step 1 is done. This bean may close as
"already-in-Mathlib, no code needed". That would be a good outcome, and it is
the reason the bean says READ FIRST rather than WRITE FIRST.

**"You are beaning your own error as if it were work."** Partly fair. The
deliverable here is a correction plus a scoping check, not a theorem. It is
beaned because the wrong claim is in a pushed commit message and would otherwise
send the next agent to rebuild machinery that already exists — the same failure
mode as the qou-fl4t "DG Section 4.5" misread, twice in one session.

**"Why did you get it wrong?"** Same root cause both times: I asserted a
structural fact about a source (DG's paper; Mathlib) without running the
one-line check. The check here is `run_cmd` over `env.constants`, and it takes
under a minute. It should precede any "Mathlib lacks X" claim, and any such
claim in this corpus that was not made that way should be treated as unverified.
