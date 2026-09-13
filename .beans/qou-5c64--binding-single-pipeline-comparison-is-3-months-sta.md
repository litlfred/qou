---
# qou-5c64
title: binding-single-pipeline-comparison is 3 months stale and RED when re-run — 2 assertions flip, one column moves 69x, and the float64 drain is blocked behind it
status: todo
type: bug
priority: high
created_at: 2026-09-13T09:23:58Z
updated_at: 2026-09-13T09:31:09Z
---

Found 2026-09-13 while screening `binding-single-pipeline-comparison` (299 raw
float64 fields) as a drain target. The reproducibility check that precedes every
drain is what turned it up: run the **unmodified** producer from `HEAD` and the
committed witness does not reproduce.

## The measurement

`computations/binding-single-pipeline-comparison.witness.json` was computed
**2026-06-15T17:27:53Z**. Re-run today on `main` `53e088bc03d`, unmodified
producer, no edits of mine:

    allPassed:  True  ->  FALSE

| assertion | computed | passed |
|---|---|---|
| `B_sym_E0_within_1p25x_T_3He` | 1.136 -> **1.58** | True -> **FALSE** |
| `B_qCLT_fac_chain_within_1p25x_T_3He` | 1.083 -> **1.5** | True -> **FALSE** |
| `E0_beats_deuteron_pin_generic` | 0.8807 -> 0.7849 | True -> True |
| `B_magic_He4_within_10pct` | 0.945 -> 0.945 | True -> True |
| `B_qCLT_fac_resolves_T_3He_ordering` | 1.0 -> 1.0 | True -> True |

**262 numeric fields moved.** The largest are all one column,
`B_lin_raw__*__miss_x`, and they grow with A:

| row | field | committed | live | move |
|---|---|---:|---:|---:|
| 5 | `B_lin_raw__E0_derived__miss_x` | 10.699 | **747.44** | 69× |
| 5 | `B_lin_raw__alpha_D_pinned__miss_x` | 18.708 | **951.92** | 51× |
| 4 | `B_lin_raw__E0_derived__miss_x` | 8.101 | 295.06 | 36× |
| 3 | `B_lin_raw__E0_derived__miss_x` | 7.412 | 86.47 | 12× |
| 1 | `B_lin_raw__E0_derived__miss_x` | 2.520 | 17.94 | 7× |
| 0 | `B_lin_raw__E0_derived__miss_x` | 0.893 | 3.614 | 4× |

Headline fields move too: `He4_miss_x` 7.17 -> 7.731,
`miss_range_generic_x` `'0.88-2.30x'` -> `'1.08-2.68x'`,
`B_qCLT_chain_uniform_E0` 7.7794 -> **5.6663** (-27 %). And the wall time went
`durationMs` 4591 -> 46014, a 10x slowdown.

## The scriptHash moved, but that is NOT the cause — I checked

    recorded scriptHash  dc752e6dffd2
    live     scriptHash  fa8cd41874f1

The producer's own source did change, so `witness_staleness_triage.py` would
class this `substantive` rather than `cosmetic`. **That classification would be
misleading here.** I read the June version at its recorded
`scriptCommitSha 32f3f7314e11c8beb610f8d3972bbf1ab4f0ec50` (via the GitHub API —
the clone is shallow, so `git log -- <producer>` returns only the boundary
commit) and diffed it. The only change to the compute path is that
`_constants()` dropped a `try/except` fallback around the `codata_constants`
import. That cannot move a number by 69x.

**So this is import-cone drift, and the trap AGENTS.md names for it applies
exactly: a file-local `git diff` on the producer cannot see it.**

## Cause: the UPSTREAM TRACES moved, by a clean per-nucleon factor

Every `tr_M` this producer reads changed, and the change is structured:

| atom | A | tr_free old -> new | ratio | **ratio^(1/A)** |
|---|--:|---|--:|--:|
| D   | 2 | 0.983526 -> 0.299015 |  3.289 | **1.81362** |
| ⁴He | 4 | 0.967324 -> 0.089410 | 10.819 | **1.81362** |
| ⁶Li | 6 | 0.951388 -> 0.026735 | 35.586 | **1.81362** |
| T   | 3 | 0.908024 -> 0.142072 |  6.391 | 1.85579 |
| ³He | 3 | 1.047757 -> 0.188179 |  5.568 | 1.77241 |
| ⁷Li | 7 | 0.878353 -> 0.012703 | 69.145 | 1.83157 |

**The three N = Z nuclei agree to all six significant figures** — a uniform
per-nucleon factor of `1.81362` — while the three N ≠ Z ones split above and
below it (n-rich high, p-rich low). That is a per-nucleon change that also
touches the p/n weighting, which is the shape of the 2026-08-15 ruling's **R3**
(`bring_color_weighted` canonical as the p/n convention) as much as of R1's
C -> D `z` swap.

It is **not** a pure rescale: the log-ratios moved too
(`ell_bond_deuteron 0.929219 -> 0.676822`, `L_pp 0.694507 -> 0.489899`,
`L_nn 1.236978 -> 0.907262`), so free and atom words moved by different amounts
— which is what a change in `z` does, since `z` enters the atom word's
inter-nucleon crossings and not the free word's.

The producer's own scale parameters did **not** move: `E_0_MeV 4.185981`,
`q_0 1.109979`, `m_e_MeV 0.51099895` are identical across the two runs. Only
`alpha_D_pinned_MeV` moved (2.394018 -> 3.286784), and that is derived from the
deuteron trace, so it is downstream of the same change.

**The factor 1.81362 is NOT identified.** I tested ~14 natural substrate
combinations at the proton `q₀`; the closest is `(q²+1)/q² = 1.811654`, which is
**0.11 % off** — far too large, since D's ratio comes from two values recorded to
six decimals and is good to ~1e-6. Identifying it would pin the exact upstream
change and is the cheapest way to finish this diagnosis.

**Also present and separately real, but far too small to matter:** the AME
inputs refreshed (`7.718043 -> 7.71804132`, `8.481798 -> 8.4817962`), i.e.
canonical `codata_constants` values replacing literals — a ~2e-6 move.

**Upstreams to look at:** `binding-canonical.witness.json` (D–⁴He) and
`tr_m_atom_via_transfer.tr_m_atom_zn` (⁶Li/⁷Li live, and the bond-type
sub-braids). Both moved the same way, so whatever changed is in or below
`tr_m_atom_zn`.

## Why nothing was regenerated

Three reasons, and the third is decisive.

1. **It turns a green record red.** Landing the regeneration publishes
   `allPassed: False` with two failing assertions. That is the honest state and
   it is the right end point, but it is a visible corpus-state change.
2. **It has a consumer.** `qou-y313` records
   `qbeta/qlommel_delta_lambda_lin_vs_sym_ladder.py` reading this witness (74
   fields), so the numbers propagate.
3. **It belongs to someone else's arc.** `qou-gjkv` — *"wave5: post-C-to-D
   corpus-wide witness regen (162 producers)"*, status **in-progress**, branch
   `claude/anchor-followups-2026-08-08` — lists
   `binding-single-pipeline-comparison (763)` by name in its own target list.
   AGENTS.md's 2026-09-07 ASK-THE-OWNER directive names *"regenerating a
   derived artifact that belongs to someone else's arc"* as explicitly NOT
   exempt.

That claim is **35 days stale**, so the stalled-claim takeover policy (>3 h with
no commit) would permit taking it over. But a takeover of a 162-producer sweep
is not a drive-by, and the branch is not fetched in this container, so its tip
was not verified — the age is from the bean's `updated_at`, not from a commit.

## Consequence for the float64 backlog

**The 299-field drain of this producer is BLOCKED behind this decision**, and
not incidentally: draining requires re-running the producer, and re-running it
IS the regeneration. There is no way to fix the float64 without also landing
the three-month regeneration.

This generalises. Any producer in `qou-gjkv`'s 162 is in the same position, so
the drain queue and the regen sweep are coupled wherever they overlap — a fact
neither bean records.

## Options (recommendation marked as judgement)

1. **Do nothing.** The witness keeps reading green while its producer's own
   assertions fail. Cost: zero now; the corpus keeps a false green on a
   binding-comparison result that content may cite. This is the default.
2. **Regenerate this one witness alone, publishing the red**, and drain the
   float64 in the same commit. Cost: ~1 min compute, 262 fields move, two
   assertions go red, one downstream consumer's inputs change. Risk: it
   pre-empts `qou-gjkv`'s ordering, and if the C->D hypothesis is wrong the red
   is unexplained. Reversible via git. Buys: an honest record and a 299-field
   drain.
3. **Take over `qou-gjkv` and run the whole 162-producer sweep.** Cost: large,
   hours of compute, a wide diff. Risk: highest, and it is the sweep class the
   ASK-THE-OWNER directive exists to gate.
4. **Finish the diagnosis first** — identify the `1.81362` per-nucleon factor
   and the commit in `tr_m_atom_zn`'s cone that introduced it, then choose.
   Cost: one read of that producer's history plus an algebra check; the
   producer-side half of this is already done (see above). Buys: option 2
   becomes a documented regeneration ("the traces moved to convention X on
   date Y") instead of an unexplained red.

I would take **4 then 2**: the finding is only worth landing once the red can be
explained in the commit message, and the remaining step is small — the producer
half is settled, only the upstream commit and the constant are open. Marked as
my judgement, not a finding.

**If nothing is decided, nothing changes** — the witness stays green, the
producer stays red when run, and its 299 float64 fields stay in the backlog.


---

## `qou-gjkv` ALREADY CLASSIFIED this witness as a C→D mover — on 2026-08-09

Read after writing the above, and it corroborates the cause independently and
with a date. That bean's own report names
`binding-single-pipeline-comparison (763)` in its results, and states its
posture explicitly:

> ACCEPTANCE IS NOT DONE AND IS NOT MINE TO DO. The driver's
> KEEP = {DECLARED, ANCHOR_MIGRATION, SUBFLOAT_MOVE} deliberately excludes
> VALUES, so this wave CLASSIFIES; it does not accept.

So the regeneration was **deliberately deferred pending a review pass**, not
forgotten. That settles the ownership question in the section above: this is not
an abandoned claim to take over, it is a completed classification waiting on an
acceptance decision that the wave's author declined to make on their own
authority — the same call the ASK-THE-OWNER directive would require today.

**One characterisation to reconcile.** `qou-gjkv` lists this witness under
*"largest non-numeric movers … assertion/string churn at scale"*. Measured here
a month later, **262 NUMERIC fields moved and two assertions flip to FAIL** —
materially more than "string churn". Two readings, and I have not separated
them: either the wave's field counter classified differently, or more moved in
the intervening month. Either way, do not read that line as "cosmetic" when
deciding acceptance.
