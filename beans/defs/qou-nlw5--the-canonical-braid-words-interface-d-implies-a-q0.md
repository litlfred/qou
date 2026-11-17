---
# qou-nlw5
title: The canonical braid word's interface d implies a q0 matching NEITHER pin — 7.2e-5 off both
status: in-progress
pr: 8268
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T04:15:44Z
updated_at: 2026-10-04T15:14:09Z
parent: qou-v2om
---

MEASURED 2026-08-26, found while triaging CRASH verdicts in the `qou-wlaf`
residue sweep.

## The guard is NOT buggy — my first hypothesis was wrong

`probe_canonical_braid_interface_composition` fails with

    ValueError: Unrecognised interface d=-0.104458247769726;
                expected one of {0, -h/2=-0.1045, -h=-0.2091}

I initially flagged this as a probable tolerance bug: the rejected value and
the expected `-h/2` agree to four decimals, which reads like an exact
comparison where a tolerance was meant. **That was wrong.** The guard at
`computations/interface_composition.py:145-152` already has one:

    elif abs(d - (-h_val / 2)) < 1e-9:

It rejects because the value really is outside it, by **7.19e-5** — five
orders of magnitude past the tolerance. The guard is working exactly as
designed, and the four-decimal agreement in its own error message is a
formatting artifact of `:.4f`, which is what made it look like a near-miss.

## The real finding: the implied anchor is neither pin

Solving `h = q - 1/q` for the `d` the word actually carries:

    canonical h  (q0 - 1/q0)   = 0.20906029879563937
    implied   h  (-2 * d)      = 0.208916495539452
    canonical q0               = 1.1099785827513808
    implied   q0               = 1.1098992085064177

    |implied - proton pin|     = 7.937e-05
    |implied - muon   pin|     = 7.939e-05      relative 7.15e-05

**It matches neither anchor.** The two pins differ from each other by ~1e-8;
this sits ~7.9e-5 from both, four orders of magnitude further out. So it is
not a muon/proton layer straddle — that hypothesis is excluded by the
arithmetic, not merely unsupported.

## What is NOT established

  * **Where the third value comes from.** Not investigated. It could be a
    hard-coded `h`, a stale constant, a differently-derived interface, or a
    genuine fourth interface class the classifier does not know about.
  * **Whether the word or the guard is wrong.** If the word is right, the
    classifier needs a fourth case; if the guard is right, something upstream
    is building an interface at the wrong anchor. Both are live.
  * **Blast radius.** `interface_composition_from_word` has other callers;
    none checked. Only this probe was observed failing, and only because the
    residue sweep ran it.

## Why it matters

`(n_pp, n_pn, n_nn)` is the proton/neutron interface census the binding
channel consumes. If a word carries an interface the classifier cannot place,
the census is either wrong or unobtainable for that word — and the failure is
loud here only because a guard exists. A caller that classified by nearest
match instead of raising would have absorbed a 7e-5 anchor discrepancy
silently.

Filed rather than fixed: deciding between "add a fourth case" and "fix the
upstream anchor" needs someone who owns the interface convention.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
