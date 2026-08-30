---
# qou-xbsk
title: Three committed audit witnesses on main are stale (substantive field moved)
status: todo
type: task
priority: normal
created_at: 2026-08-30T03:38:49Z
updated_at: 2026-08-30T03:39:23Z
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
