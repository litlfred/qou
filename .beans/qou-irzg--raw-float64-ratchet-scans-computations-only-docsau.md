---
# qou-irzg
title: raw-float64 ratchet scans computations/ only — docs/audits/scripts/ witnesses are ungated (5 carry raw floats)
status: todo
type: task
created_at: 2026-08-15T02:49:47Z
updated_at: 2026-08-15T02:49:47Z
---


## Evidence

`scripts/precision-gates.sh --changed` on a branch touching only
`docs/audits/scripts/` reports:

    precision-gates: no witness or computations/ script touched — skipped.

That is correct behaviour for the script as written, and it is the problem: the
raw-float64 ratchet's scan root is `computations/`, so every witness under
`docs/audits/scripts/` is outside the NO-FLOAT64 discipline. Audit probes emit
witnesses there routinely — this session alone added three.

Scanning that directory by hand (JSON walk for Python `float` instances) found
**5 witnesses carrying raw float64**, none of them from this arc:

| witness | raw floats |
|---|---|
| `qbeta-action-qsqrt3-saddle-probe` | 8 |
| `qbeta-ohtsuki-deformed-meridian-rungs` | 6 |
| `keystone-wlambda-unitarity-normalization-gate` | 4 |
| `qbeta-ohtsuki-deformed-kappa5-phase-test` | 1 |
| `qbeta-ohtsuki-deformed-kappa3-tall-ladder` | 1 |

Several are `max_loss_digits` / `c_ratios` — diagnostic magnitudes rather than
physical predictions, so the *harm* may be low. The *gap* is not: nothing stops
a q₀-bearing prediction landing there ungated, and the directory is where
audit probes naturally write.

## Two separable pieces

1. **Widen the ratchet's scan root** to include `docs/audits/scripts/`. Cheap.
   Expect it to go red immediately on the five above — which is the point, but
   means it needs a baseline decision, not a one-line patch.
2. **Drain the five.** Belongs to whichever arc owns those probes, per the
   prepare-merge rule that inherited red is not the current branch's regression.

Found while running `/prepare-merge` step 4b on PR #5060. Not fixed there: the
branch introduced no red, and widening a ratchet mid-merge would have made the
gate's first run red on someone else's witnesses.

## Still open, and it grew — re-measured 2026-08-19

Piece 1 (widen the scan) shipped: `witness_raw_float64_audit.py` takes
`--scan-root`, and `scripts/precision-gates.sh` runs the audits tree as an
ADVISORY gate. `--rebaseline` is refused alongside `--scan-root`, so the
tempting shortcut is closed.

Piece 2 (drain the five) is **not** done, and is now **six**:

|  n | witness |
|---:|---|
| 8 | `qbeta-action-qsqrt3-saddle-probe` |
| 6 | `qbeta-ohtsuki-deformed-meridian-rungs` |
| 6 | `wlambda_normalisation_census`  **<- NEW since this bean was filed** |
| 4 | `keystone-wlambda-unitarity-normalization-gate` |
| 1 | `qbeta-ohtsuki-deformed-kappa3-tall-ladder` |
| 1 | `qbeta-ohtsuki-deformed-kappa5-phase-test` |

That the count went 5 -> 6 while the tree was advisory is the argument for
flipping it blocking: advisory reports a gap, it does not hold one. The gate
comment already states the flip condition ("once the five are drained"); the
condition should now read six, and the drain still belongs to the arcs owning
those probes rather than to this bean.

Note the newcomer is a `.py`-named witness in a tree of `-`-named ones, so a
drain sweep keyed on the `qbeta-*` prefix would miss it.

## Piece 1 CLOSED — the gate is BLOCKING and green (2026-08-19)

The blocker was never that the six were undrained. It was that the ratchet had
**no memory for this tree**: `raw-float64-baseline.json`'s 1572 entries are all
`computations/` paths, so every witness under `docs/audits/scripts/` read as
NEW on every run, forever. A ratchet with no memory is red on arrival, and a
gate red on arrival gets skipped — the rule `precision-gates.sh` states at the
top.

That is the **`_output_name` defect (qou-pgdw) one step removed**. When that
bug was fixed the OUTPUT name was scoped to the scan root; the BASELINE was
left global. `_baseline_path()` now derives it the same way, so this tree gets
`raw-float64-baseline--docs-audits-scripts.json` (6 files / 26 fields) and the
corpus baseline is untouched.

This is **establishing coverage where there was none**, not silencing a
regression in a tree that already had it — the distinction the drains-never-grow
rule turns on. `--rebaseline` with `--scan-root` was refused before precisely
because it would have written into the corpus baseline; that is now
unreachable from a non-default root, so the refusal was relaxed to permit a
root's own file.

Verified before flipping, because a gate that cannot be shown to fire is a
no-op:

| check | result |
|---|---|
| audits tree green now | exit **0** |
| planted dirty witness | exit **1**, names it |
| after removing it | exit **0** |
| corpus run unaffected | 1572 baseline, NEW 0, REGRESSED 0 |
| whole gate family | **all blocking gates green** |

Why flip rather than wait for the drain: the count grew **5 -> 6** while the
tree was advisory. Advisory REPORTS a gap; it does not HOLD one. The next
`wlambda_normalisation_census` now fails on arrival.

## Piece 2 still open, and still not mine

The six baselined witnesses (26 fields) belong to the arcs owning those probes:

- 8 `max_loss_digits` (3 qbeta-ohtsuki probes) — precision *diagnostics*, the
  same class as the `compute_wall_sec` telemetry drained in qou-5qwb, so
  cheap: serialize at the producer.
- 6 `sum_classical = 1.0` (`wlambda_normalisation_census`) — an exact value
  stored as a float; cheapest of all.
- 8 `c_ratios` + 4 `Z_at_q0` — genuine computed values; these want real mpmath
  treatment, not serialization, and that is a judgement for their owners.

The gate now holds the line at six. It does not drain it.

## QUEUED — kappa3 / kappa5 witnesses, and exactly how to finish

Four of the six drained and pushed (`669adce8a1b`); the audits tree is at **2**
raw float64, one field in each of:

- `qbeta-ohtsuki-deformed-kappa3-tall-ladder.witness.json`
- `qbeta-ohtsuki-deformed-kappa5-phase-test.witness.json`

**Both producers are ALREADY FIXED and committed.** Nothing remains to edit —
the only thing outstanding is that each witness must be regenerated by a
completed run. Re-running is the whole task.

    cd docs/audits/scripts
    python3 -u qbeta_ohtsuki_deformed_kappa3_tall_ladder.py 2>&1 | tee /tmp/kappa3.log
    python3 -u qbeta_ohtsuki_deformed_kappa5_phase_test.py  2>&1 | tee /tmp/kappa5.log

Cost, measured this session rather than guessed: kappa3 reached rung 9/11
(N=131072) at 765 s, kappa5 rung 8/11 (N=65536) at 428 s. Cost grows ~2.4x per
rung doubling, so kappa3 projects to roughly **2 h** end to end. `dps = 980` and
`N` runs to 524288.

### Do NOT trust `pgrep -f` to tell you it is still running

`pgrep -f qbeta_ohtsuki...` MATCHES ITS OWN COMMAND LINE when the pattern
appears in the monitoring command. It reported "still running" for a job that
had already written its witness and exited, this session — the same trap
`qou-9br4` records for rho-k, hit independently here. Use

    pgrep -af "python3 .*kappa3_tall" | grep -v "bash -c"

and cross-check the log's mtime.

### Finish checklist

1. `python3 computations/witness_shape_guard.py` — 0 collapsed. A partial
   write scores **zero raw floats** and reads as a perfect drain; this is the
   gate that separates the two.
2. `git diff -- <witness> | grep -iE '^-.*"(numpy|mpmath|sympy|pyhecke)"'` —
   any `-` line means the container is poorer than the one that wrote the
   committed copy; install and re-run rather than commit the stripped one
   (compute-author §0.1).
3. `python3 computations/witness_raw_float64_audit.py --scan-root docs/audits/scripts --strict`
   — expect **0** dirty.
4. **Then tighten the baseline**, which is the step that makes this stick:

       python3 computations/witness_raw_float64_audit.py \
           --scan-root docs/audits/scripts --rebaseline

   Baselines drain, never grow — leaving it at 6 files / 26 fields after the
   tree reaches 0 would let a future regression back in silently, which is the
   whole failure this bean was opened about.

## The gated tree was the SMALLER half — widen it to all of `docs/audits`

Measured after the flip: I scoped the gate to `docs/audits/scripts` (26 fields),
because that is where the bean's original evidence came from. The rest of
`docs/audits/` was never in scope and is far bigger:

    docs/audits (whole tree, excl. _deprecated and self-outputs):
      34 dirty witnesses, 1,277 raw float64 fields

That is ~50x the subtree I gated. Most are dated 2026-05-02 — historical
one-off audit artifacts, e.g. `2026-05-02-per-braid-hybrid-jet` (249 fields),
`-gs-filtration-E2-probe` (157), `-per-braid-wigner` (91).

**Plan: one gate for `docs/audits`, superseding the `scripts` one.** The
`_baseline_path()` mechanism already generalises to any scan root, so this is a
baseline file and a one-word change to the gate's `--scan-root`, not new
machinery. Two baselines for nested trees would double-count the subtree and
confuse the drain accounting; a single superset baseline does not.

Sequenced AFTER the kappa3/kappa5 witnesses land, so the new baseline starts at
the true floor rather than recording 2 fields that are about to become 0.

Not a drain: these 1,277 stay exactly as they are. The point is that nothing
NEW may join them — which is the same argument the 5 -> 6 growth made for the
subtree, only fifty times larger.
