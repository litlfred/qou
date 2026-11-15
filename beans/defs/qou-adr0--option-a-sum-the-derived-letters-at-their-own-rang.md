---
# qou-adr0
title: 'Option (a): sum the derived letters at their own range instead of truncating at first contact'
status: completed
type: task
priority: normal
created_at: 2026-09-05T09:04:32Z
updated_at: 2026-09-05T09:09:23Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. Option (a) of
`qou-556v`, on the owner's instruction. **Result: NOT ADOPTED**, with two real
findings and one clean refutation.

## The law tested

A pair at chain distance `d` gets weight `L_type . b_type^(d-1)`, so `d = 1`
reproduces the contact law exactly and longer pairs decay at that letter's own
rate. **No new parameter.**

⚠ The identification `mu = -ln b` -- that the same `b` suppressing the trace per
bond also sets the range -- is a MODELLING CHOICE, not derived. Labelled in the
probe, the witness and here.

Control: the closed-form pair census `min(Z,d,N,A-d)` for p-n was checked
against a brute-force enumeration over all 49 `(Z,N)` layouts with `Z,N <= 7`
and every distance -- 0 mismatches. That step was the one that could quietly be
wrong.

## Finding 1 — it FIXES THE LIGHT END, which is where the contact law is worst

Scale-normalised median `B_AME/S` by mass bin, 2548 nuclides:

| A | n | contact | full range | shift |
|---|---:|---:|---:|---:|
| **2-20** | 101 | **0.827248** | **0.884621** | **+6.94 %** |
| 21-60 | 334 | 1.070252 | 1.067485 | -0.26 % |
| 61-120 | 667 | 1.059157 | 1.048899 | -0.97 % |
| 121-180 | 764 | 0.997911 | 0.993040 | -0.49 % |
| 181-300 | 682 | 0.940301 | 0.935169 | -0.55 % |

Light nuclei have few bonds, so a contact law under-counts them most, and the
missing pairs are exactly what the range restores. Everything else drifts under
1 %.

## Finding 2 — it WASHES OUT THE LAYOUT

The segregated-vs-alternating p5-p95 gap goes **0.4589 % -> -0.03037 %**, 15x
smaller. Once every pair contributes, the ORDER of the nucleons stops mattering.
An independent route to `qou-48is`'s "the layout is nearly irrelevant to B".

## Finding 3 — but it does NOT repair the law

| law | p25-p75 | p5-p95 | full |
|---|---:|---:|---:|
| segregated chain, contact | 1.09530 | 1.22497 | 10.1815 |
| segregated chain, FULL RANGE | 1.09512 | **1.20727** | **10.7082** |
| alternating chain, contact | 1.09688 | 1.23059 | 10.3997 |
| alternating chain, FULL RANGE | 1.09420 | 1.20690 | 10.9511 |
| **layout-free (A-1)** | **1.08425** | **1.18085** | **8.17344** |

p5-p95 improves ~1.4 % while the FULL spread worsens 5.2 %, and p25-p75 is
unchanged to four figures. **Layout-free `(A-1)` still beats full range on BOTH
measures**, with no isospin structure at all. Scale: full range over-binds by a
further **1.904x** (median `B_AME/S` 11.242 -> 5.904), as predicted from
`1/(1-b)` = 2.58 / 2.03 / 1.68.

## What this establishes

The 14.4x truncation self-inconsistency measured in `qou-556v` is real and worth
recording -- **but the truncation is not what the residual is made of.** By the
brief's own falsifier that indicts the LETTERS, or the identification
`mu = -ln b`, not the range treatment. Consistent with `qou-q7ga`: the
isospin-resolved letters cost more than any range treatment recovers, which is
why the isospin-blind `(A-1)` keeps winning.

**Live successor:** the light-end gain is the one piece worth keeping. If a
future letter set is found that does not lose to `(A-1)`, re-run this probe
against it -- the range extension costs nothing and demonstrably helps exactly
the regime (`A <= 20`) where the contact law is furthest off.

Artifact: `computations/qbeta/qbeta_full_range_bond_sum_probe.py` (6/6, 30 dps,
float64-guard clean).
