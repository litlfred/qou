---
# qou-rok2
title: 'PR #4884: verification gate — precision-gates, check-sidecars, lean-direct'
status: completed
type: task
priority: normal
created_at: 2026-08-10T07:07:53Z
updated_at: 2026-08-10T12:53:10Z
parent: qou-aemy
---

The Phase-4 gate for #4884. CI could not supply it — `build.yml` is
`workflow_dispatch`-only under the 2026-06-30 Actions-billing directive and the
PR carried **0 check runs** — so per AGENTS.md §"QA is agent-owned" this
verification *was* the gate, and each line below was stated in the PR rather
than summarised as "verified".

**Lean.** Everything was checked against a **118-module import cone rebuilt
from source** post-rebase (`rc=0`, 0 failures), *not* against the restored
`lake-cache` oleans — see `qou-hz0e` for why that cache was untrustworthy here.

- 12 of 12 changed `.lean` files at `lean`-direct **exit 0, no warnings**
  (⇒ sorry-free).
- 51 new declarations, `#print axioms` = `[propext, Classical.choice,
  Quot.sound]` on all of them, **zero `sorryAx`**.
- Both aggregators (`QOU.AlgebraicSubstrate`, `QOU.Archimedean`) exit 0 —
  including the newly-wired `TowerHeightAttack` import. This **closed the one
  verification checkbox the authoring session had left open**: it had been
  blocked only by the cache predating `PauliWitness.lean`, and building from
  source removes that blocker rather than working around it.
- §7c checked by hand: `ℝ` in `SurrealGradingPrune` is load-bearing, not
  gratuitous — the archimedean property of `ℝ` *is* the invariant being proved.

**Precision gates** (`scripts/precision-gates.sh`). The raw-float64 ratchet was
red with 2 NEW dirty witnesses. One was attributable to this branch —
`jet-algebraic-independence.witness.json`, 3 raw float64 fields, all
`runs[i].elapsed_sec` emitted as `round(elapsed, 2)`. Drained **at the
producer** (`0516ca508`): not a baseline entry, not `--rebaseline`, not a
hand-edit. `elapsed_sec` is diagnostic wall-clock, so it is now an int, which
also makes the probe's own docstring claim ("exact, no floats anywhere") true.
Ratchet after: NEW dirty 2 → 1, REGRESSED 0. The survivor
(`kappa-shell8-excess-convention`, 25 fields) is inherited from main and
untouched — `qou-oflu`.

The regeneration was a re-run of the producer, so it doubles as an
**independent reproduction of the PR's §3**: `minimal_relation_degree 7`,
`algebraically_independent_up_to 6`, d=7 nullspace dim 3 stable at 421
equations, positive control PASS — all bit-identical. Witness diff: 3 lines,
all timings.

**Stale committed audit witnesses** (`73090b045`). All three had moved *counts*,
not just provenance, so the gate's own rule says commit the regenerated witness
and name the count. raw-float64: `new_not_baselined 2→1`, `drained_files
19→20`, `dirty_witnesses 1578→1577`. q0-value-drift: proton-pin `697→699`,
NEW drift 0. q0-anchor-consistency: `Q0_OK 582→583`, `Q0_ANCHOR_MISSING
1892→1894`.

That last `+2` is the branch's own defect (`qou-5wuz`), and committing the
regenerated audit is precisely what keeps it visible — leaving the witness
stale would have read as if the count had never moved.

**Sidecars** (`scripts/check-sidecars.sh`). Actioned: authors-note Lean-coverage
stats refreshed via `scripts/refresh-authors-note.ts` (`5c7cac6fc`) — inherited
drift from main, stated as such. Left tracked and advisory, not silently
absorbed: P30, both new producers write witnesses without `WitnessBuilder` and
so emit `PROV_MISSING`.

**Transferable.** Two gate outputs here were red *because the base moved*, not
because of the branch. Attribute every red before draining it; a red you did
not cause still has to be either fixed, or named with its owner.
