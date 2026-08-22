---
# qou-cdj8
title: sync-qou-mass-vendor checks 42 .py and ignores 157 .witness.json — 122 disagree with source on the q0 pin
status: in-progress
type: task
priority: normal
created_at: 2026-08-21T21:44:29Z
updated_at: 2026-08-22T09:22:04Z
---

Split from `qou-hp3g`, whose sync-drift half turned out already fixed
(`e4906af5a4c`) and whose title I had to retract. This is the half that is real.

## The defect

`scripts/sync-qou-mass-vendor.py` `--check`/`--apply` iterate `cone` and
compare `VENDOR / f"{mod}.py"` — **Python modules only**. It reports

    vendored copies are in sync (42 modules)

while **157 tracked `*.witness.json` under `qou-mass/src` are compared to
nothing.** A gate that reports success without examining the thing that drifted.

`required_witnesses()` (line ~195) already computes which witnesses the
vendored modules load at runtime; its result feeds a `--list` report, not the
comparison. So the design anticipated the data files — the check just never
consumed it.

## Measured (current main, 157/157 have a computations/ twin)

| | count |
|---|---|
| identical raw-float64 count | 34 |
| differing | 123 |
| mirror dirtier than source | 17 |
| **mirror/source disagree on q₀ pin** | **122** |

Worked case — `canonical-mass-table-extended.witness.json`:

    mirror  1af7d4b7a04  2026-08-15  "qou-mass v1.0.0"          33 f64   MUON
    source  da2968cc335  2026-08-19  "first witnesses at the    0 f64    PROTON
                                       proton pin"

Four days stale, and on the anchor the 2026-08-07 owner directive superseded
(reaffirmed R2, 2026-08-15). The float64 gap is a CONSEQUENCE of the staleness,
not the sync introducing error — the sync never writes these files at all.

## Blast radius — narrow, and must stay stated that way

`qou-mass` is **not published** (AGENTS.md: 404 on PyPI, no dist/, no publish
step). No external consumers. Exposure is the **5 in-repo importers**. Do not
write this up as researchers receiving wrong numbers.

## Plan

1. Extend `--check` to compare the witness JSONs `required_witnesses()`
   already identifies, so the gate covers what it ships.
2. Show it fires (plant/detect/restore), as with the .py half.
3. Re-sync the data and confirm the q₀ disagreement goes to 0.
4. Precision preflight on the result — re-syncing changes what the package
   carries, so the raw-float64 posture must be measured after, not assumed.



---

## CORRECTED after reading the script properly

Two of my own claims above were wrong and are retracted:

1. **"157 witness JSONs are compared to nothing" — FALSE.** There IS a witness
   loop (line ~246, `for name, src in wits.items()`). The check covers the 18
   witnesses `required_witnesses()` scrapes from cone-module source. The
   uncovered count is **122**, not 157 and not 139.

   139 would be 157 − 18. It is 122 because **17 names exist in both the
   package root and `data/`**, so a name-based match credits the `data/` twin
   with the root copy's check. That collapse turned out to be the sharper
   finding.

2. **"122 disagree on the q₀ pin" — true but overstated.** Split by class:

   | | n |
   |---|---|
   | mirror ABSENT / source proton — predates the #4020 anchor convention | 120 |
   | ambiguous / absent — noise | 1 |
   | **actively contradicting (both record a pin, they differ)** | **1** |

   Exactly one file contradicts its source: `canonical-mass-table-extended`,
   mirror **muon**, source **proton**. The 120 are stale and unlabelled, not
   wrong. The isotope shards are 2026-05-19 copies from the same producer,
   predating both anchor recording and the `environment` block.

## The finding that survives

**Duplicate shadows.** 17 witnesses exist in both the package root and `data/`.
The script's own header explains witnesses MUST sit in the root because the
vendored modules resolve there, and that a `data/` placement "makes every one
of them FileNotFoundError" — so these copies are unreachable at runtime. They
cannot fail loudly; they just sit there being read by humans. **2 of the 17 are
divergent:**

    q-pinning-50-digit.witness.json      root 2026-08-21  data/ 2026-07-18
    atomic-tr-m-mpfr-50dps.witness.json  root 2026-08-19  data/ 2026-08-10

`q-pinning-50-digit` is the substrate modulus record, present in two versions a
month apart.

**And nothing runs the gate.** Grepped every `.sh`/`.yml`: no workflow, no gate
array invokes `sync-qou-mass-vendor.py`, while AGENTS.md calls `--check` "the
gate". Fourth instance of the qou-j6gb pattern. This is why `qou-wpp2` saw it
go red again four days after the ratchet was built.

## Done

`--check` now reports its own coverage instead of implying completeness:
module + witness counts, the uncovered count, and the shadowed/divergent pairs.
Shown to track reality, not print constants: resolving one shadow moved
divergent 2→1, removing one moved pairs 17→16, both restored.

Reported rather than deleted, following the script's existing `orphans`
convention — removing a shipped file is an API decision this script should not
make silently.

## NOT done — needs a decision, not a sweep

Re-syncing the 122 or deleting the 17 shadows changes what the package carries
and is a package-design call (the script header already tracks a separate item
about a package-aware resolver so vendored data could live under `data/`).
Wiring `--check` into a gate array is likewise a decision — `precision-gates.sh`
is the NO-FLOAT64 family and this is not that.


---

## ALL THREE DONE (owner directed both decisions, 2026-08-22) — c8661cc6edd

**1. Wired into `scripts/staleness-gates.sh`, BLOCKING.** That array, not
`precision-gates.sh`: this is a copy whose source moved and was never
regenerated, which is exactly the staleness family's stated purpose, and nothing
about it is float64. Blocking from the start rather than advisory because it is
GREEN on arrival — the red-on-arrival objection does not apply.

**2. Re-synced the 122.** `extra_witnesses()` covers `data/` + `data/isotopes/`,
which had no sync path at all. Synced IN PLACE, not into the package root: these
are not resolved by the modules, so the root placement constraint does not apply
and moving them would change import paths for nothing.

**3. Deprecated the 17 shadows** to `data/_deprecated/` with a README, via
`git mv`. Not deleted — removing a shipped file is an API decision, matching the
script's `orphans` posture. `_deprecated` is the existing repo convention and
the sync already skipped it.

### Measured effect, BOTH directions

    q0Anchor recorded    8 -> 128 of 140 witnesses
    raw float64 fields   32,883 -> 44,937

**The float64 count went UP by 12,054 and that is not a regression introduced
here.** The three-month-old copies were *smaller than the sources they mirror*,
so syncing to truth imports float64 those sources already carry — a backlog
owned by the producing arcs and already tolerated at source by the corpus
baseline. The alternative was keeping copies that looked cleaner only because
they were stale. Recorded rather than buried: a naive reading of the ratchet
would score this as a 12k-field regression.

### Verification

- Coverage: 42 modules + 18 cone + 122 package-data, **0 uncovered**.
- **Fires through the runner, on both halves** — planted drift in a vendored
  module → RED naming the gate; planted drift in `data/isotopes/` (the half
  that had no coverage at all) → RED naming
  `canonical-isotope-witness-Z01.witness.json`; clean before and after.
- `precision-gates.sh`: all blocking gates green.
- `staleness-gates.sh` exits 1 at baseline on **two pre-existing reds**
  (`scriptHash + upstream drift`, `q0 constant staleness`). Verified on clean
  `origin/main`: identical two reds, so neither is mine — in particular the
  re-sync did NOT cause the q0 one, which was the obvious suspicion given it
  changed 122 anchors.

### One artifact caught before it landed

`git add -A` swept in `witness-raw-float64--qou-mass-src-audit.witness.json`,
a byproduct of my own before/after measurement on a scan root no gate runs. It
had already bumped `Q0_AUDIT_EXEMPT` 75 → 76 in the anchor audit. Removed from
the commit and the audit reverted to 75. Same class as the `docs-audits`
byproduct caught earlier in this arc.
