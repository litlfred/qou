---
# qou-xbsk
title: Three committed audit witnesses on main are stale (substantive field moved)
status: completed
type: task
priority: normal
created_at: 2026-08-30T03:38:49Z
updated_at: 2026-08-30T14:30:26Z
---

Surfaced by `scripts/precision-gates.sh --changed` run on 2026-08-30 from a branch
rebased to `behind = 0`, on a diff that touches **zero** files under `computations/`
(seven `.lean` files and six `.beans/` files only). So the movement is **main's, not
the branch's** — the regeneration compares main's producers against main's committed
witnesses.

The script's own report:

```
STALE COMMITTED AUDIT WITNESSES — a substantive field moved:
  computations/audits/witness-provenance-audit.witness.json
  computations/witness-raw-float64--docs-audits-audit.witness.json
  computations/witness-raw-float64--qou-mass-src-audit.witness.json
```

"Substantive" means the script's own drift classifier found a moved field that is
**not** in the ephemeral set (`computedAt` / `commitSha` / `durationMs` /
`environment` / `invocation`) — two other witnesses moved on ephemeral fields only
and were auto-reverted, so the classifier is discriminating, not blanket.

## Not fixed here, deliberately

The gates run dirties nine audit witnesses as a side effect. Committing the three
regenerated ones from a **Lean-only** PR is exactly the error AGENTS.md records as
made-and-reverted in `8176c82707` — "never commit unrelated audit witnesses the
resolution sweeps in". All nine were discarded (`git checkout -- computations/`,
tree back to 0 modified).

## What the next agent needs to do

1. **Say which count changed.** The script asks for this explicitly and it was not
   determined here — I discarded before diffing the payloads. Re-run and diff the
   regenerated witness against the committed one, field by field.
2. **Confirm the movement is main's**, per the script's own instruction: `git log`
   the newly-listed entries. My evidence for that is indirect (my diff touches no
   `computations/` path, so it cannot be mine) — which rules out one cause without
   identifying the real one.
3. Then commit the regenerated witnesses **on a branch whose scope is the audit**,
   not bundled into unrelated work.

## Separately: the four standing REDs are still main's

Same run, verified at `behind = 0`: `q0-anchor flip`, `q0-anchor refill ratchet`,
`float64-padding ratchet`, `q0-value drift ratchet`. Unchanged from the earlier
measurement, and owned by `qou-k6b3` / `qou-hhm3` / `qou-cds3`. Not this bean's scope
— noted so a reader does not mistake the three stale witnesses above for the cause of
those four.


## Items 1 and 2 ANSWERED 2026-08-30 — and item 3 is superseded, do NOT do it

This bean asked the next agent for three things. Two are now measured; the third
turns out to be the wrong action.

### 1. Which counts changed

Measured on a tree at **0 behind** `origin/main` (`5dc5727d80`), from a branch
whose diff touches zero `computations/` paths. Four witnesses moved, not three —
the set is not stable across runs because it tracks main's own churn:

    witness-provenance-audit    total_scanned      2939 -> 2948
                                prov_ok            2515 -> 2521
                                prov_missing         85 -> 103
                                prov_exempt_no_reader 258 -> 242
    q0-anchor-consistency       Q0_OK              1125 -> 1126
                                Q0_ANCHOR_MISSING  1637 -> 1645
    mpf-float-source-audit      benign               12 -> 15
    q0-value-drift              proton-pin         1997 -> 1998

### 2. The movement is main's — by name, not by inference

This bean's own evidence was indirect ("my diff touches no `computations/`
path, so it cannot be mine"), which rules out one cause without identifying
the real one. The direct evidence is in the newly-listed **entries**:

    milnor-recursion-forall-A-proof.witness.json
    aggregator-family-exclusion.witness.json
    computations/probes/pairing_delta_overdetermination_probe.py
    computations/probes/casimir-q-factorial-probe.witness.json

None is mine; `total_scanned` rising 2939 -> 2948 is main landing nine new
witnesses. Note the `pyhecke_native_build` hash also moved
(`e186e42e6d8dd38a` -> `110b330d42788fa0`) — that one is **this container's
environment stamp**, not corpus movement, and is a second reason not to commit.

### 3. "Commit them on an audit-scoped branch" — SUPERSEDED

Do not. Bean `qou-v0t8`'s later sections carry a stronger revised rule reached
after this bean was written: **never commit a tree-measuring audit witness from
a feature branch, regardless of ratchet direction or how current the tree is.**
These are *contended* files — main regenerates them on its own cadence, so a
branch that commits one acquires a conflict that recurs on every subsequent
main landing. Measured there: PR #5805 went `mergeable_state: dirty` within
twenty minutes, on exactly the file the gate told it to commit, from a tree
that was 0 behind.

The four here were reverted. `precision-gates.sh` now says so itself — the
banner's "commit the regenerated one" is gated to `main` only, and on any other
branch it prints "DO NOT COMMIT THESE. Revert them" with both failure modes
(guard landed 2026-08-30, `qou-v0t8` closed).

Nothing is lost by reverting: the movement is main's, which main carries anyway.
