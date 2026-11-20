---
# qou-q3f7
title: 'mass-table-comprehensive.witness.json is stale: B_qCLT is off by a constant -7.92e-4 MeV vs its own producer on main'
status: todo
pr: 8336
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-28T20:01:37Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

## The measurement

Found while draining this witness's float64 (PR #5918). The drain itself is
NOT the cause — that was established by running the pristine `origin/main`
producer and the drained one **in the same process** on the same isotopes,
rather than comparing either to the committed artifact.

Committed witness (`computedAt 2026-08-26T04:01:07Z`, `commitSha 3ea8e82193`)
vs what `main`'s own producer emits today:

| isotope | A | committed `B_qCLT_MeV` | producer today | delta |
|---|---|---|---|---|
| D    |  2 | 4.401529   | 4.400737   | -0.000792 |
| T    |  3 | 10.263414  | 10.262622  | -0.000792 |
| 37Cl | 37 | 162.993882 | 162.993090 | -0.000792 |
| 38Cl | 38 | 168.855767 | 168.854975 | -0.000792 |
| 39Cl | 39 | 174.717652 | 174.716860 | -0.000792 |
| 40Cl | 40 | 180.579537 | 180.578745 | -0.000792 |

`m_approx_MeV` moves by exactly +0.000792 on the same rows, which is just
`m_unbound - B_qCLT`.

## Why this cannot be float64 rounding, and cannot be alpha

**Constant in ABSOLUTE terms across a column spanning 4.4 -> 180.6 MeV.**
Float64 error would scale with the value (and would be ~1e-14 here, which is
in fact exactly what the PR #5918 drain moves these numbers by: 2.8e-16 at D
to 5.5e-14 at 40Cl).

`B_qCLT = -alpha * sum_log_V` with `alpha = m_e * 8 * Catalan` constant per
row. A change in `alpha` of relative size d gives `dB = d * B`, which scales
with B. It does not. So `alpha` is not the mover.

Therefore `sum_log_V` rose by a CONSTANT

    dS = 7.92e-4 / alpha = 7.92e-4 / 3.7443 = 2.115e-4

independent of A -- i.e. **a single multiplicative factor in the product of
per-generator Wedderburn volumes changed by a ratio of exp(2.115e-4) =
1.00021**, and that factor is present exactly once per atom regardless of A.
That is 2.1e-4 relative: five orders above float64, so it is a real upstream
change, not noise.

## Hypothesis (NOT tested)

The term that appears once per atom irrespective of A is the **inter-nucleon**
contribution -- `atom_per_generator_volumes(Z, N, include_inter=True)`. A
change in the inter-nucleon volume, or in the convention it is computed under,
would produce exactly this signature. Given the window (witness computed
2026-08-26; `main` has advanced heavily since), the convention-D / colour-
weighting / q0 landings are the obvious places to look first.

Stated as a hypothesis because it was not run down: the signature is
consistent with it and I did not verify which commit moved the value.

## Next step

1. Bisect `atom_per_generator_volumes(1, 1, include_inter=True)` across the
   window to name the commit.
2. Decide whether the new value is the intended one (then the witness was
   simply never regenerated) or a regression (then the producer is wrong and
   the witness was right).

PR #5918 regenerates this witness for the float64 drain, so **the -7.92e-4
will land in that regeneration**. It is called out in that PR's Attribution
section so the movement is not misread as the drain's doing. Whichever way
step 2 goes, the number in the witness after #5918 is what `main`'s producer
currently computes.


## CAUSE IDENTIFIED — and it is not staleness-by-neglect, it is a DEFERRED
## regeneration that this witness was always going to take

The hypothesis above (inter-nucleon term) is confirmed as to *mechanism*, and
the commit is named. `git log --since=2026-08-25 -- tools/pyhecke/.../atom.py
computations/hecke_core*.py` returns exactly two commits, and the first is:

**`543e30adfd` "flip: route the p-n bond through one canonical colour-weighted
offset"** (2026-08-26 13:35Z, bean `qou-cblw`) — the R3 colour-weighting
ruling. Its own message states:

    f_pn  before   0.5081578877486455981370624
    f_pn  after    0.5082297893767389669218554
    gap            7.190163e-05,  relative 1.415e-04

and names `atom_per_generator_volumes` as one of its three `pyhecke/atom.py`
sites — the exact function the q-CLT proxy calls. The p-n bond enters once per
atom irrespective of A, which is the constant-offset signature.

It also says, explicitly:

    Witness regeneration is NOT in this commit. The affected set is large
    (<= 1027 producers ...) and some single producers run for tens of minutes.
    It is metered separately.

So `mass-table-comprehensive` is one of those deferred regenerations, and
PR #5918's re-run is that meter arriving. The new number is the INTENDED one.

## What is NOT reconciled

The naive prediction does not match, and this is recorded rather than
smoothed over. `B = -alpha * sum_log_V` with `alpha = m_e*8*Catalan =
3.74417`, so the observed `dB = 7.92e-4` implies

    dS = 2.1153e-4  (+/- 1.3e-7, from the witness's 6-dp resolution)

against the commit's single-crossing `1.41497e-4`. The ratio is **1.4949**,
which is close to 3/2 but is NOT 3/2 — exact 3/2 would need `2.12246e-4`,
7.2e-7 above the measured value and far outside the 6-dp error bar.

Candidate explanations, none tested:
  - the p-n factor enters the volume product with a multiplicity, and the
    `f_pn` gap quoted in the commit is not the same quantity that enters;
  - the second commit in the window, `879419b0ac` (`hecke_core_legacy.py`,
    "migrate the bridge, defaults and legacy branches"), also contributes.

Do not quote 3/2. Either measure it, or leave it open.

## Disposition

The value in the witness after PR #5918 is what `main`'s producer computes
under the canonical colour-weighted convention. Cross-referenced on
`qou-cblw`. This bean can close once the 1.4949 is reconciled or judged not
worth reconciling.


## Progress Update (PR #8336)
- Formalized in Lean 4.24.0 (`0` sorries, `0` advisories across all 6 static audit scripts in directory mode) and wired into `QOU.lean`.
- Verified at `mp.dps = 50` with 2-commit witness stamp (`03d44f353473173a3c5099bb1c73d25e13571021` -> `ece176bc167f5646b3158b046f0540fa97d681a7`) in PR #8336.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8336, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
