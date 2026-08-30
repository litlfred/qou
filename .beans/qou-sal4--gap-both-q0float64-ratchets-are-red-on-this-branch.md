---
# qou-sal4
title: 'GAP: both q0/float64 ratchets are RED on this branch — 3 unstamped + iterative-lp-dual 96->99'
status: todo
type: task
created_at: 2026-08-30T18:10:19Z
updated_at: 2026-08-30T18:10:19Z
---


Surfaced 2026-08-30 while closing `qou-l2we`. **Neither red is caused by that
change** — both predate it and neither file is in that commit.

## `q0_anchor_ratchet.py --strict` — FAIL, 3 newly unstamped

    computations/deltalambda/c-knot-tau-transfer-artifact.witness.json
        73567a64e  witness(takeover): regenerate c-knot tau-transfer witness
    computations/probes/toffoli-published-vs-construction.witness.json
        2f3e5b2f8  audit: universality fails under the block's OWN indexing too
    computations/probes/toffoli-trio-rederivation.witness.json
        04f14b7c2  derive(qou-3j5m): the Toffoli trio is RESOLVED

Each is a regenerate/derive commit whose producer does not stamp `q0Anchor`.
Fix at the PRODUCER (`save(extra=...)`, never `add_data` — bean `qou-kx04`), not
by widening `q0-anchor-missing-baseline.json`. If a producer genuinely never
reads q0 the correct stamp is `'independent'` + `q0AnchorReason`, NOT silence.

## `witness_raw_float64_audit.py --strict` — FAIL, 1 regressed

    96 -> 99   computations/iterative-lp-dual-h6-deuteron.witness.json
        ac6310b31  fix(qou-mjcd): a declared-proton producer was multiplying...

That one is **mine** (qou-mjcd). The fix was correct; the re-run re-added three
raw f64 the drain had removed. Same mechanism as the one just fixed in
`qbeta_ck_basis_constrained_pslq.py`.

## The general defect this is an instance of

`bc8131bd5` ("drain(float64): 1232 declared tolerances in 499 witnesses")
drained the **artifacts** but left the **producers** emitting floats. So every
drained witness silently un-drains the next time anything re-runs its producer,
and the ratchet only notices later, attributing it to whoever re-ran it.

`qbeta_ck_basis_constrained_pslq.py` is now fixed at the producer (emits
`"tolerance"` as a string, 18 -> 17). **The other 498 are not.** Estimating that
population and fixing the producers is the real work here — a drain that any
re-run reverses is not a drain.

Do not widen either baseline. `raw-float64-baseline.json` says so itself:
"Adding a file here to silence a failure defeats the gate — fix at the producer
instead."
