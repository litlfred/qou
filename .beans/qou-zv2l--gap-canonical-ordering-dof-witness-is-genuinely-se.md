---
# qou-zv2l
title: 'GAP: canonical-ordering-dof witness is genuinely self-stale on scriptHash (producer re-run needed)'
status: todo
type: task
created_at: 2026-08-10T12:56:59Z
updated_at: 2026-08-10T12:56:59Z
---


Found incidentally while auditing `qou-wsha` (the `scriptCommitSha`
staleness re-key), not by a targeted sweep.

`computations/probes/canonical-ordering-dof.witness.json` is **genuinely
self-stale**: its recorded `scriptHash` does not match the current bytes of
its producer, so the producer was edited after the witness was generated.

    witness  computations/probes/canonical-ordering-dof.witness.json
    producer computations/probes/canonical_ordering_dof_probe.py
    scriptHash  recorded=87418d646ff1  current=894cafe018ee   -> STALE

This is the real thing, distinct from the `scriptCommitSha` false positives
in `qou-wsha` — `witness_dependency_drift.py --self-strict` would flag it,
and it is exactly the class of drift the idle-pass witness budget exists to
drain.

**Not fixed here.** Refreshing it means re-running the producer, which is a
compute action outside the scope of a docs-currency PR, and the witness
budget rule (≤ 3 per idle pass) wants it claimed deliberately rather than
ridden along. Next agent: re-run the producer per the compute-audit
long-compute logging discipline (`2>&1 | tee /tmp/<script>.log`) and commit
the refreshed witness with a `chore(witness)` message naming the producer.

Scope note: this is one witness, from the n=3 reliably-measurable sample of a
shallow clone — **not** a claim about the corpus-wide self-staleness backlog,
which was not measured.
