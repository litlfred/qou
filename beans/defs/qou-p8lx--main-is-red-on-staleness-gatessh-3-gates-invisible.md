---
# qou-p8lx
title: main is RED on staleness-gates.sh — 3 gates, invisible because --changed was skipping
status: completed
type: bug
priority: normal
created_at: 2026-08-22T21:04:36Z
updated_at: 2026-08-28T15:06:58Z
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


## CLOSED 2026-08-28 — all three dispositioned, and this bean over-claimed twice

Re-measured on main cdbdc84af1. Final state of the three reds this bean
opened on:

  qou-mass vendor mirror   GREEN. Went red TWICE from unrelated causes.
      2026-08-22 was TRANSIENT (the qou-ishr drain mid-flight; that arc's own
      follow-ups re-synced it). 2026-08-23 was STANDING and REAL: char_fast
      moved to computations/substrate/ and gained a q-pinning guard in
      6a8d41bf89 while the mirror sat 8 days stale, so the packaged qou-mass
      shipped a char_fast WITHOUT it. Re-synced via --apply in PR #5511.

  q0 constant staleness    6 -> 2, and the 2 are not defects. Four closed:
      three by bean qou-bdkx / PR #5532 (producers that hardcoded the muon
      literal under a proton declaration), and knot-volumes by a SIBLING's
      derived-output exemption (53aafb7795) -- the disposition I had diagnosed
      but not implemented. The 2 survivors declare `q0Anchor: muon` AND carry
      a muon q0Value: self-consistent, valid as recorded, owned by qou-1c4y.

  scriptHash + upstream drift  492 self-stale of 3170 (was 624/3031),
      dominated by sha256_mismatch against q-pinning-50-digit.witness.json --
      the same q0-migration root. AGENTS.md §4 measures this class as ~0% safe
      to refresh: red by design.

## The permanently-red-blocking-gate concern is RESOLVED (owner, 2026-08-28)

This bean's one live owner-facing question -- two BLOCKING gates measuring
backlogs policy forbids draining, so the array could never go green -- was
answered: demote both to advisory until qou-1c4y lands. Done; the array now
exits 0 with both still running and still reporting. Flip-back condition and
the demotion-time measurements are recorded in the GATES array itself.

## Two things this bean got wrong, both worth keeping

1. It recorded three STANDING reds. One was a photograph of a sibling's
   work-in-progress. A red measured once on main may be mid-arc.
2. It treated the q0 gate's 6 as one backlog. They were three dispositions:
   2 consistent-and-gated, 3 declaration/payload contradictions, 1 derived
   output that was never a pin at all.

Both errors were of the same shape -- a single measurement generalised into
a standing category without checking whether its members differed.

---

## 2026-08-28 (later) — a third thing this bean got wrong, and it was in the demotion itself

The demotion note recorded, of the q0 gate's two survivors:

> Both survivors declare `q0Anchor: muon` AND carry a muon q0Value —
> self-consistent and valid as recorded; they are the migration, not defects.

**That is true of one of them.** `lever1-binding-core-characterization` did *not*
carry a muon `q0Value` in the sense that matters: its `params.q0` held the
**PROTON** pin while `q0Anchor`/`q0Value` declared **muon**. The declaration and
the payload disagreed — a provenance stamp asserting a layer its numbers do not
belong to, which AGENTS.md forbids "regardless of size". That is a defect, not
the migration.

Root cause was the `qou-7vm4` shape in a second file: `try:` the proton constant
/ `except:` a hardcoded muon literal, so the physics layer depended on whether an
import succeeded. Fixed at the producer (fallback removed — this producer's whole
output is an evaluation *at* the pin, so a run that cannot read it has nothing to
say), manifest re-tagged `ambiguous → physical_proton`, re-run: all three fields
agree on proton and **no number moved**.

The other survivor, `lever1_binding_habiro_single_element_test`, genuinely IS the
migration — and is now exempted **structurally** rather than incidentally. The
gate hardcodes "live q₀" as proton, but `q_parameter` resolves a
manifest-declared `ideal_muon` stem *to muon*, so it was reading a correct
ideal-layer witness as a stale physical-layer one, and its prescribed remedy
(re-run) would have destroyed the declared pin — the regeneration reverted in
PR #5436. `declared_ideal_muon_exempt` requires both the witness declaring muon
and the manifest declaring the producer `ideal_muon`, fails closed, and
deliberately does not accept `ambiguous`.

### Consequence, and what is NOT being done about it

`q0 constant staleness` now reports **q₀-stale: 0 on its own merits**, not by
demotion. It is tempting to flip it back to blocking on that basis. **I have not,
and the gate's own note is why**: *"FLIP BOTH BACK TO BLOCKING when qou-1c4y
completes. That is the whole condition — not 'when the counts look better'."*
That rule is right and a green count is exactly the argument it pre-empts.

What HAS changed is the demotion's *premise* for this one gate — "both are the
migration" no longer describes it. Recorded in the GATES array beside the
original measurement so whoever holds `qou-1c4y` can see it may be promotable
ahead of `scriptHash + upstream drift`. Owner call.

### The pattern this bean is tracking, one more time

Its own closing lesson — *"a single measurement generalised into a standing
category without checking whether its members differed"* — describes the
demotion note too. Two witnesses were called one thing; they were two.

### Correction to my reporting

I told the author twice that the third red "needs your decision". It did not: the
decision was made and shipped the same day in `8df1883353`, and the array already
exited 0. I was reading a stale measurement of my own and repeating it.
