---
# qou-97on
title: 'phi: the per-nucleon f1/f0 contribution as a function of an 11-letter two-generator word'
status: completed
type: task
priority: normal
created_at: 2026-09-06T07:13:59Z
updated_at: 2026-09-06T09:58:13Z
---

## Why this is now a well-posed question (2026-09-06)

`f1/f0` on the `pn` atom word is **exactly additive** across the two nucleons —
they occupy generators {0,1} and {3,4}, every cross pair has |i-j| >= 2, so they
act on disjoint strand sets and `tr_M` factorises. Measured 6/6 exact in
`Fraction` by
`computations/probes/word_order_commutation_and_additivity_probe.py` (4/4), with
the canonical split

    v(pp) = 21    v(pn) = 37/2    v(nn) = 16    ->    phi(p) = 21/2, phi(n) = 8

reproducing the per-letter counts (proton 21, neutron 16) that
`c1_leading_coefficient_derived_probe.py` carries.

**This factorisation is NOT new** — it is derived in
`braids-and-knots/markov-axioms-primitive.md`, its consequence is named in
`mass-theory/subset-cumulant-recursion.md`, and it was measured at 40 dps by
`computations/qbeta/qbeta_disjoint_support_factorisation_probe.py` (7/7, bean
`qou-ib3g`). What is new is only the consequence below.

## The question

By additivity, the whole 22-letter problem reduces to a function `phi` of an
**11-letter word on two adjacent generators alone**. Find it.

Known constraints:

- `phi(canonical proton, grouped) = 21/2`; `phi(canonical neutron) = 8`.
- The grouped word is a **1-swap local maximum** and the Borromean word is not
  (110/196 neighbours beat it) — bean `qou-hu1f` / #6905.
- `phi` is **not** determined by contiguity at either level. Global contiguity is
  refuted outright (0.238 and 0.857 both give the ceiling value). Intra-nucleon
  contiguity fails too and is not even monotone: three proton orders at
  intra-contiguity 0.400 give `phi` = 15/2, 0 and 6, while 0.600 gives 3.

## What would settle it

The proton word is 7 letters on gen 0 (6 sigma + 1 averaged) and 4 on gen 1
(3 sigma_inv + 1 averaged); the neutron is 7 on gen 3 (5 sigma + 2 averaged) and
4 on gen 4 (4 sigma_inv). Counting distinct orderings by multinomial:

    proton   11!/(6!.1!.3!.1!) = 9240
    neutron  11!/(5!.2!.4!)    = 6930

Both are **small enough to EXHAUST** — 16170 words total at ~1.5 s each is about
7 h of compute, and the two halves are independent so they parallelise. That
would turn the maximisation into a PROVED statement over the whole orbit rather
than a sampled or 1-swap-local one, settling the local-vs-global extremality
question of `qou-hu1f` at the same time, and it would hand `phi` over as a
complete table to fit a closed form against.

(Both counts computed, not estimated: an earlier draft of this bean said 4620 and
~2 h, which was 11!/(6!.1!.3!.1!) miscomputed by a factor of 2 and stated for the
proton alone.)

Refs: `docs/audits/2026-09-06-contiguity-does-not-drive-f1-the-split-link-factorisation-does.md`.


## COMPLETED 2026-09-06 — both orbits exhausted, both global maxima

    proton    9240/9240 words   42.6 min   canonical 21/2: 1232 attain, 0 EXCEED
    neutron   6930/6930 words   32.2 min   canonical 8   :  990 attain, 0 EXCEED

Ran at n=3, not n=6, which is the whole reason this took ~75 min rather than the
~7 h estimated above. Two invariances licensed it and BOTH are gated in the probe
rather than assumed: phi is strand-count independent (21/2 at n = 3, 4, 6 alike)
and translation-invariant in the generator index.

**phi IS QUANTISED IN UNITS OF 3/2.** Every consecutive gap in both spectra is
exactly 3/2, no gaps in either ladder and nothing off it:

    proton  : 21/2  9  15/2  6  9/2  3  3/2  0  -3/2      (9 values, 9240 words)
    neutron :    8  13/2  5  7/2  2  1/2   -1  -5/2       (8 values, 6930 words)

The lattices are OFFSET: proton on (3/2)Z, neutron on (3/2)Z + 1/2. Quantum
shared, offset not. Neither is explained here.

**The two canonical words are the extremes of that ladder.** Grouped is the
global max of both orbits; borromean — the word made canonical by the 2026-09-05
ruling — is one rung above the bottom of each (proton 3/2, neutron -1). That is a
MEASUREMENT and NOT an argument against the ruling, which was made on grounds
this does not address. It does explain why so much downstream moved when the
default changed: c1 by a factor of 37, and #6559's crossover finding entirely.

**The refinement that cuts against the extremality reading:** the canonical word
is NOT unique. 1232 proton words (13.3 %) and 990 neutron words (14.3 %) attain
the maximum. So "canonical maximises phi" is true, and "canonical is picked out
by maximising phi" is FALSE — the maximum is a large plateau, not a point.
Anyone reaching for extremality as a SELECTION PRINCIPLE should read that number
first.

Upgrades qou-hu1f / #6905 (1-swap local max, 196 of 9240) and #6714 (largest of
40, p ~ 1/41) to exhaustive statements.

Audit: docs/audits/2026-09-06-phi-is-quantised-in-units-of-three-halves.md
