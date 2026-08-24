---
# qou-p8lx
title: main is RED on staleness-gates.sh — 3 gates, invisible because --changed was skipping
status: in-progress
type: bug
priority: normal
created_at: 2026-08-22T21:04:36Z
updated_at: 2026-08-23T07:54:23Z
---

Found on PR #5474 immediately after fixing the `--changed` predicate
(qou-s2gm defect 1) so the script actually examines committed work.

MEASURED on a pristine origin/main worktree, full run (not --changed):

  git worktree add --detach /tmp/mainwt origin/main
  (cd /tmp/mainwt && bash scripts/staleness-gates.sh)   -> exit 1

  RED: scriptHash + upstream drift
       q0 constant staleness
       qou-mass vendor mirror
  ADVISORY: dependency coverage

Identical set on the #5474 branch, so these are INHERITED, not caused by
that branch. Attribution is by measurement on a clean worktree, not by
assertion.

## Why this was invisible

`scripts/staleness-gates.sh --changed` collected its relevant-file set from
`git diff --name-only HEAD` + `--cached` + `ls-files --others` — the working
tree only. Once a change is committed the set is empty, so it printed
"no witness or computations/ script touched — skipped" and exited 0.
AGENTS.md tells every agent to commit early and often, so that is the
common case. The gate has been red for an unknown length of time with
nothing reporting it.

DISTINCT FROM qou-mnrd, which tracks main being red on the raw-float64
ratchet (a precision-gates gate). These three are staleness-gates gates
and were not previously recorded.

## Do not

* do not narrow the `--changed` predicate again to make this quiet — that
  re-opens the hole #5474 closed;
* do not baseline the offenders — the ratchets drain and never grow
  (AGENTS.md).

## Next step

Triage the three separately; they are unrelated backlogs.
`qou-mass vendor mirror` is `scripts/sync-qou-mass-vendor.py --check` and
may be a one-command `--apply` (the mirror is GENERATED — see AGENTS.md,
all 14 copies had drifted when the sync script was written), so start
there. The other two are corpus-scale.


## RE-MEASURED 2026-08-23 — this bean OVER-CLAIMED one of its three

`qou-mass vendor mirror` was NOT a backlog. It was a TRANSIENT mid-arc state.

Reproduced the original red to confirm it was real: at e9fd81a633,
`sync-qou-mass-vendor.py --check` exits 1 on three drifted witness JSONs
(atomic-tr-m-mpfr-50dps, canonical-mass-table-extended,
m-p-borromean-verification-50dps). So the measurement was correct.

But it belonged to the qou-ishr float64 drain, mid-flight: 945b2edf2f
("m_p_borromean 17 -> 0") and e005856e18 ("canonical_isotope_witness ...
43,901 float64 -> 0") rewrote the SOURCE witnesses, drifting the vendored
mirror; that same arc's follow-ups re-synced it (09571f1b3f, c1c8f34bfa).
On current main the checker exits 0 — "42 modules, 18 witness JSON, 122
package-data witness JSON in sync".

THE LESSON: a red measured once on main may be MID-ARC, not persistent. A
sibling landing a source change in one commit and its derived artifact in
the next is red in between, and a snapshot taken there is indistinguishable
from a standing backlog. Re-measure before treating a red here as work.
Recorded in the script's own header so the next reader gets it for free.

## The two that remain, characterised

`q0 constant staleness` — 6 witnesses, and they are TWO different things:
2 are self-consistent muon-declared (the gated qou-1c4y migration, not to be
drained here); 4 declare one anchor and carry another. The 4 are split out
as bean qou-bdkx and are actionable without the gated migration.

`scriptHash + upstream drift` — dominated by sha256_mismatch against
q-pinning-50-digit.witness.json, i.e. the same q0 migration root. Per
AGENTS.md §4 the self-stale class is ~0% safe to refresh, so this one is red
BY DESIGN and cannot be drained.

## Consequence worth the owner's attention

Two of staleness-gates.sh's BLOCKING gates measure backlogs that policy says
not to drain. So the array cannot go green on main until qou-1c4y runs — a
permanently-red blocking gate, which is precisely the "a gate red on arrival
gets skipped" failure precision-gates.sh warns about at its top. Visible to
every agent now that #5474/#5495 made the gate actually run.
