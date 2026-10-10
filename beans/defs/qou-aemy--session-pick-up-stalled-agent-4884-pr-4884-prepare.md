---
# qou-aemy
title: 'Session: pick up stalled agent 4884 (PR #4884) — prepare-merge + merge'
status: completed
type: epic
priority: normal
created_at: 2026-08-10T07:07:51Z
updated_at: 2026-08-10T08:20:04Z
---

Merged as `5cc389cfe5` (rebase-merge, 25 commits, branch preserved).

The authoring session stalled after the `qou-frch` commit with everything
pushed, so the science needed no change. The pickup found two genuine
defects; both are recorded here because both are recurring classes, not
one-offs.

**1. A new library module was orphaned from the build graph.**
`QOU.Archimedean.TowerHeightAttack` — 316 lines, 9 declarations, the whole
of the PR's §2 — was imported by *nothing*. `lake build QOU` would never
have compiled it, so no later break in it could be caught. It type-checks
standalone, which is exactly why per-file `lean`-direct exit 0 hid the gap.

Generalisable lesson: **a per-file `lean`-direct pass does not prove a
module is reachable.** Grep for importers as a separate step. This same
directory-scoped-`git add` slip is recorded three times in that branch's
own commit messages, and PR #4846 is triaging 795 unbuilt modules — so the
check belongs in the routine, not in one agent's habits.

**2. The stale-olean trap fires again after any rebase.**
The `lake-cache` branch was seeded 2026-08-07; `HyperbolicVolumeTranscendence`
changed 08-09 and the rebase moved across 381 further commits. Verifying
against that cache would have repeated the exact error the authoring session
had already caught and documented mid-run.

What worked: rebuild the import cone **from source** into a fresh olean dir.
The 118-module aggregator cone built clean, which additionally closed the
one verification checkbox the authoring session had left open (`QOU.Archimedean`
was only ever blocked by the cache predating `PauliWitness.lean`).

Cost note for whoever does this next: `PauliWitness/Witness12B` alone takes
~30 min at 99% CPU, and the SessionStart `lean-build-bg.sh` hook races you
for cores — it respawns after `pkill`. It writes to a *different* mathlib
tree (`content/.../lean/.lake/packages/mathlib`) than `lean-verify.sh` reads
(`/home/user/qou/.lake/packages/mathlib`), so it does not corrupt results,
only slows them. That hook also errors on main: `lean-build-bg.sh: line 177:
mathlib_local_available: command not found`.

**Left open deliberately** (named in the PR, not absorbed): `qou-5wuz`
(neither new witness records `q0Anchor`; `Q0_ANCHOR_MISSING` +2),
`check-sidecars` P30 (both new producers bypass `WitnessBuilder` ⇒
`PROV_MISSING`), and `qou-oflu` (the inherited `kappa-shell8` float64
offender, still the only thing holding §4b red repo-wide).

**Not obtained:** a Copilot review. Requested, nothing within the 15-minute
cap. Merged on agent verification per the skill's timeout rule — stated
rather than implied, since CI is `workflow_dispatch`-only and this PR
carried zero check runs.
