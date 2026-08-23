---
# qou-7e1t
title: 'low_isotope_mass_table clobbers its own canonical upstream: default re-runs it at target-dps 11 over a committed 60-dps table'
status: todo
type: bug
priority: normal
created_at: 2026-08-22T15:29:23Z
updated_at: 2026-08-23T08:27:15Z
---

## What

`computations/low_isotope_mass_table.py` describes itself as a "thin
projection" of `canonical-mass-table-extended.witness.json`. It is not
only that: **by default it re-runs the canonical producer first**, as a
subprocess, with its own arguments —

    if not args.no_rerun_canonical:
        run_canonical(args.method, args.target_dps)

    parser.add_argument("--target-dps", type=int, default=11)
    parser.add_argument("--method", ... default "auto")

— and those defaults are NARROWER than the committed canonical artifact.
Measured by running it with defaults over the committed table:

| field | committed canonical | after the wrapper's default run |
|---|---|---|
| `parameters.target_dps` | **60** | **11** |
| `parameters.method` | `branching` | `auto` |
| `parameters.dps` | 0 | 50 |
| rows | 7 | 9 (`p`, `n` now compute) |

So running the LOW-ISOTOPE wrapper silently rewrites the CANONICAL
upstream table, dropping its target precision from 60 dps to 11. The
canonical witness is a different, coarser computation afterwards, and
nothing in the wrapper's output says a canonical artifact was replaced.

## Why it bites

This is the mechanism behind a narrowing I hit and reverted earlier in
this arc without identifying the cause (recorded then as "ran the extended
producer with the low-isotope atom list", 7 rows -> 5, 60 -> 11 dps). It is
not the atom list; it is the wrapper's own `--target-dps 11` default
reaching a producer whose committed output is 60.

Note the row count moves the OTHER way (7 -> 9): `--method auto` routes
`p`/`n` through the direct H_3 path, while the committed `branching` table
records them as ERROR rows. So the clobbered table is simultaneously
*wider* in coverage and *coarser* in precision than the committed one —
which is exactly why the damage is easy to miss by eyeballing a row count.

## Second, separate defect: the projection's upstream is stale

The committed `low-isotope-mass-table.witness.json` records

    derived_from.scriptHash:  b6c20f1b6e02
    derived_from.computedAt:  2026-08-15T21:36:25Z

while the canonical witness actually in the tree is `dfcd6d57966b`,
computed 2026-08-22. The projection describes a canonical witness that is
7 days old and no longer present. To its credit `derived_from` makes this
*detectable* — but nothing enforces it, and the two witnesses disagree on
their face: the projection carries `method: auto, target_dps: 11, 5 atoms`
against a committed canonical of `method: branching, target_dps: 60,
7 rows`. They cannot both describe the same computation.

Regenerating honestly with `--no-rerun-canonical` against the CURRENT
canonical yields **3 atoms**, not 5, because the current canonical has no
`p`/`n` rows. So the wrapper's two modes give materially different
witnesses, and the destructive one is the default.

## Lineage

`qou-5h7z` (completed) documented an earlier staleness in this same file —
pre-convention-D `tr_M` values and collapsed ctypes — and explicitly
declined to commit its regeneration. That bean's C->D deltas
(`2H 0.38828647 -> 0.57509096`) are the FIRST of three steps for the
deuteron; the colour-blind -> colour-weighted move landed on PR #5427 is
the third (`0.575090872 -> 0.575172244`). Different axis, same file.

## What was and was not done on PR #5427

**Done:** the anchor gap. `builder.save()` was called bare, so the emitted
witness carried `q0Anchor: null` / `q0Value: null` — it could not say which
layer its numbers belonged to, which is the enabling condition for the
cross-layer comparison retracted in `qou-4e5k`. It now inherits both from
the witness it projects (inherited, not read from `q_parameter`: this
producer computes nothing, and reading the live pin would declare the pin
this PROCESS imports rather than the pin the NUMBERS were computed at).

**Not done — deliberately:** the witness is not regenerated. Regenerating
correctly narrows it 5 -> 3 atoms, which is a visible loss that is really a
symptom of this bean, not of the anchor fix; and regenerating with defaults
would clobber the canonical table. The source fix is inert until someone
regenerates, which is the same posture used for the producer fixes earlier
in that PR.

## Next honest step

Decide what the wrapper should be. Candidates, roughly increasing cost:

1. **Make `--no-rerun-canonical` the default** and require an explicit flag
   to re-run. A projection should not have a destructive default.
2. **Refuse to re-run at settings coarser than the existing artifact** —
   compare `target_dps` and abort rather than downgrade.
3. **Reconcile method.** Decide whether the canonical table should be
   `auto` (covers `p`/`n`) or `branching` (errors on them), and make both
   producers agree, so a projection cannot be wider than its source.


---

## PARTIALLY RESOLVED (2026-08-22, PR #5460) — the silent downgrade is closed

Landed the narrow half: `canonical_mass_table_extended.py` now **refuses**
to overwrite the canonical witness at a lower `--target-dps`, with
`--allow-precision-downgrade` as the deliberate escape hatch. Sibling to the
existing `--allow-partial-canonical` guard, same idiom, same place.

Verified end to end (5/5):

| # | scenario | result |
|---|---|---|
| 1 | `--target-dps 11` over committed 60 | REFUSED, exit 2 |
| 2 | canonical after the refusal | untouched |
| 3 | bare default (60 == 60) | exit 0, writes |
| 4 | `--allow-precision-downgrade` | exit 0, downgrades to 11 / 9 rows |
| 5 | `low_isotope_mass_table.py` defaults | exit 2, canonical untouched |

## Why the qou-xwet guard could not catch this

Worth recording, because it is the generalisable part. `qou-xwet` guards
the ROW axis — it refuses a row-SUBSET write. The precision downgrade
arrives with the row count moving the **other way**: `--method auto`
computes `p`/`n`, which `branching` errors on, so the coarser replacement
is **wider** in coverage. A guard phrased as "is the new table smaller" is
structurally blind to it. Any future fixed-output-path guard should ask
which axis it protects, and whether a caller moving a different axis can
push the guarded one favourably.

## Still open — NOT done, by design

Options 1 and 3 above remain: making `--no-rerun-canonical` the default,
and reconciling `auto` vs `branching` so a projection cannot be wider than
its source.

I originally recommended option 1 as "small and clearly right". **That was
wrong, and the corpus already said so.** The 2026-06-14 audit
`docs/audits/2026-06-14-qclt-delta-lambda-lowisotope-triage.md` hit this
exact tension and recorded it as *"an architecturally significant change to
shared state ... for an explicit decision rather than done unilaterally"*,
and it measured that a light reproject **drops the p/n rows**. So flipping
the default does not remove the problem — it trades silent precision loss
for silently missing atoms. Neither default is clean while `auto` and
`branching` disagree about whether `p`/`n` are computable; that
reconciliation (option 3) is the real fix and needs an owner decision.

Related, still standing: the projection's `derived_from` names a canonical
computed 2026-08-15 (`b6c20f1b6e02`) while the tree holds `dfcd6d57966b`
from 2026-08-22, and the two disagree on their face (`auto/11dps/5 atoms`
vs `branching/60dps/7 rows`). The anchor-declaration fix for that witness
is on PR #5427, landed inert (not regenerated) for the same reason.


--------

## 2026-08-23 — MEASUREMENT that reframes option 3 (and unblocks option 1)

I wrote above that option 3 needs to *reconcile* auto vs branching so a
projection cannot be wider than its source, and treated that as the hard part
needing an owner decision. **Measured, there is nothing to reconcile.**

`compute_tr_m_canonical(..., method='auto')` dispatches to `branching`
VERBATIM for A >= 2 (canonical_mass_table_extended.py:190,
`eff = 'laurent_q_rust' if (Z+N) < 2 else 'branching'`). Run over the full
DEFAULT_ATOMS set at 60 dps:

  atom   A  auto route       branching route   identical
  p      1  laurent_q_rust   ERR               auto=ok  branch=ERR
  n      1  laurent_q_rust   ERR               auto=ok  branch=ERR
  D      2  branching        branching         YES (==, not 'agrees to')
  T      3  branching        branching         YES
  3He    3  branching        branching         YES
  4He    4  branching        branching         YES
  5Li    5  branching        branching         YES
  6Li    6  branching        branching         YES
  7Li    7  branching        branching         YES

Python `==` on the mpf, not a tolerance. So on this table

    auto  is a STRICT SUPERSET of  branching

with zero numerical disagreement anywhere the two overlap. Option 3 is not a
reconciliation; it is a one-token default change
(`--method` default `branching` -> `auto`), after which the canonical table
is 9 rows and a projection can no longer be wider than its source.

Cost: 4.5 s for all nine atoms (7Li, the worst, is 3.94 s). No pruning change
— `--target-dps` stays 60.

### Consequence for option 1

The 2026-06-14 audit's objection to flipping `--no-rerun-canonical` to the
default was that a light reproject *drops the p/n rows*. That objection is
**caused by** the canonical being `branching`. Do option 3 first and it
evaporates: reprojecting a 9-row canonical yields the 5-atom paper set
INCLUDING p and n. So the two are not alternatives — **3 unblocks 1**, and the
order is 3 then 1.

### The real remaining question is not a compute question

What p/n rows carry is `prediction_MeV`, an ABSOLUTE nucleon mass. Two things
changed under this bean since I last wrote:

* `qou-7loj` is FIXED (2026-08-08). `lookup_nucleon_mass_canonical` no longer
  reads the deprecated Vol·rho witness (+2.89 %); it routes through
  `canonical_mass.nucleon_mass_mev()`. So restoring p/n no longer restores a
  27 MeV/nucleon error.
* The owner ruling of 2026-08-11 (`qou-exam`) EXCISED absolute mass as a
  claim. So the column those rows would restore is precisely the one that is
  no longer a prediction — while `tr_M(p) = 1.1457596924573008696890` and
  `tr_M(n) = 0.9877436881158095716340` are dimensionless categorical
  quantities the table is otherwise entirely about.

That is a labelling decision (`qou-exsw`'s remaining content work), not a
method decision, and it does not gate option 3.
