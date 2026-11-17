---
# qou-im4m
title: 'Nucleon crossing counts: the corpus derives a 13-crossing neutron, hecke_core implements 11'
status: in-progress
pr: 8260
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T01:37:42Z
updated_at: 2026-10-04T15:13:23Z
parent: qou-v2om
---

## Measured (scope-(a)), `qbeta_nucleon_crossing_count_contradiction_probe.py`, 7/7

`Delta_L = neutron_word - proton_word`, both from `hecke_core`, so the crossing
content of those words is load-bearing for the Delta fork (`qou-bg3w`).

| source | proton | neutron |
|---|---|---|
| `categorical-proton-properties.md:10` — bare 9 (6 B_3 + 3 quark) + one Hopf link | **11** | — |
| `categorical-neutron-properties.md:11` — "**a total of 13 crossings** (6 from B_3, 3 from quarks, 4 from gluons)" | — | **13** |
| `q-beta-gamma-gamma-canonical-derivation.md:33` — "B_p and B_n have 11 typed crossings **each**" | 11 | **11** |
| `hecke_core._PROTON_G0/G1`, `_NEUTRON_G0/G1` | **11** | **11** |

**The proton is consistent everywhere at 11.** The neutron is not: the corpus
DERIVES 13 — the LP dual "selects L_+ -> L_- (two Hopf links, 4 gluon
crossings)... the neutron requires more gluon crossings than the proton (4
versus 2) because the dd crossing creates a deeper instability (tr_M = -0.132
versus -0.006)" — while the code implements 11.

**And the citation does not say what it is cited for.**
`q-beta-gamma-gamma-canonical-derivation.md:33` names `def:categorical-proton`
and `def:categorical-neutron` as its authority for "11 typed crossings each".
Right for the proton, wrong for the neutron: that definition's own properties
block derives 13. Same stale-citation class as the convention-C citations
drained in PR #5892.

## Two corrections to my own earlier claims (PR #5892)

1. **"The 11-crossing count is asserted at three prose sites, derived at
   none."** Wrong on both halves. It IS derived — bare 9-crossing element plus
   the LP-selected Hopf stabiliser — and the derivation yields **13 for the
   neutron**, not 11.

2. **"One prose count is wrong regardless:
   `c5-...-interpretation.md:18` gives the proton two averaged crossings while
   its own proof sibling gives it one; the arithmetic settles it, since a
   two-averaged proton would carry an h^2 term and net(p) = 1 - h/2 has
   none."** Also wrong. Measured, `hecke_core`'s proton has **exactly** the
   decomposition that block states — 7 gen-0 (6 pure + 1 averaged), 4 gen-1
   (3 inverted + 1 averaged), i.e. 6 pure / 3 inverted / **2 averaged**. The
   block describes the **long** model faithfully; `net(p) = 1 - h/2` is the
   **short** model. Two different objects, not a contradiction — the
   object-conflation failure AGENTS.md §"Grep the claim SHAPE" warns about,
   committed while cataloguing other people's detector errors.

## Not adjudicated

Whether the neutron should carry 13 crossings or 11 moves every number
`Delta_L` enters. That is an owner call of the same class as the fork itself
(`qou-bg3w`). `hecke_core` is untouched.

Measurement note worth keeping: the stored shifts are full-precision `mpf`.
A first pass compared them via `str(d)`, which round-trips through a 17-digit
repr and put all 22 crossings in "other". Compare the `mpf` directly.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-29 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
