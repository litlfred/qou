---
# qou-q6yr
title: 'Regenerate canonical-mass-table-extended: braid_word_canonical carries the pre-split ctype vocabulary'
status: completed
type: task
priority: normal
created_at: 2026-08-15T00:12:16Z
updated_at: 2026-08-15T00:19:27Z
---

DONE (in-repo half). Re-ran canonical_mass_table_extended.py; all 7 rows now split correctly:

  Z N     OLD                              NEW
  1 1  avg 5              ->  avg 4 + avgW 1
  1 2  avg 7              ->  avg 6 + avgW 1
  2 1  avg 7              ->  avg 6 + avgW 1
  2 2  avg 9              ->  avg 8 + avgW 1
  3 2  avg 11             ->  avg 10 + avgW 1
  3 3  avg 13             ->  avg 12 + avgW 1
  3 4  avg 15             ->  avg 14 + avgW 1

|tr_M| UNCHANGED on all 7 rows, as predicted: the label split never moved a d value, so the numeric payload could not move. Producer wall ~6 s (method=branching, Rust path), so this was cheap, not a long compute.

precision-gates.sh --changed is RED, and it is NOT this change: raw-float64 for this witness is 24 -> 24 (unchanged). The regression is rho-k-co-casimir-extended (3->4) plus two NEW qns-* probe witnesses, all untouched here and all landed on main earlier tonight by other work.

Reverted three audit witnesses the gate incidentally regenerated (q0-anchor-consistency, q0-value-drift, witness-raw-float64). Their COUNTS moved, which the gate's rule reads as 'committed copy was stale, commit the regenerated one' -- but that rule assumes a faithful environment and this sandbox lacks scipy and clarabel and runs mpmath 1.3.0 vs 1.4.1 (visible in the witness's own engineVersions). The counts moved because of missing dependencies, not staleness. Committing them would have written sandbox-specific numbers to main.

NOT DONE: the qou-mass package shard. See qou-hy6q -- it is a hand-copied 2026-05-19 vintage (scriptHash 9c80f63797ce, engine markov_peel+mpmath) with a DIFFERENT row set (has p and n, lacks 7Li) and no sync script. Copying today's witness over it is not a refresh, it is a coverage + method + vintage change to published API output. Needs an owner decision, not a copy.
