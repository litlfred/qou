---
# qou-97on
title: 'phi: the per-nucleon f1/f0 contribution as a function of an 11-letter two-generator word'
status: todo
type: task
priority: normal
created_at: 2026-09-06T07:13:59Z
updated_at: 2026-09-06T07:14:27Z
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
