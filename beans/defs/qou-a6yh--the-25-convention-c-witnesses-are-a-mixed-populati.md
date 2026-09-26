---
# qou-a6yh
title: 'The 25 convention-C witnesses are a mixed population: 7 real weights, 4 audit mentions, 14 needing judgement'
status: todo
type: task
created_at: 2026-08-24T05:02:08Z
updated_at: 2026-08-24T05:02:08Z
---

<!-- Recovered from PR #5168 (branch claude/conv-c-shared-root-2026-08-16), where
     this body was written as `qou-pvem`. It never reached main: a later commit in
     the same arc, 0ab493a49a, wrote a DIFFERENT bean (the DEAD_TOL float64-noise
     sub-class) into the same file under the same id, keeping this filename. That
     DEAD_TOL bean is the one on main today, at
     .beans/qou-pvem--the-25-convention-c-witnesses-are-a-mixed-populati.md — its
     name still describes this bean, not its own contents. Landing #5168 as-is
     would have restored this body by deleting that one, so it is re-filed here
     under a fresh id and both survive. Body below is verbatim from #5168. -->

## The finding

The 25-witness convention-C work list is **not homogeneous**. It conflates
witnesses that *compute with* C against witnesses that *report* C on purpose.
Classified by which detector fires and, for fingerprint-only hits, whether the
C decimal sits in an audit/check context:

| class | n | meaning |
|---|---|---|
| structural / symbolic | **7** | a real nonzero `y_λ` on a 3+-row block — genuine convention-C weights |
| fingerprint, audit/check context | **4** | the witness *reports* C as a named check |
| fingerprint, working value | **14** | the C decimal appears as a value the run used — needs per-file judgement |

The clearest case in the middle class is
`computations/audits/weight-factor-audit.witness.json`:

    "check": "C8",
    "name":  "Markov parameter z = 1/(q^0.5 + q^-0.5) at q_0",
    "computed_z": "0.4993203341836944524134426802…"

That is an audit verifying the C value as check **C8**. Re-running it will
always re-emit C — that is its job. Contrast `entanglement-orders.witness.json`,
which records `"z": 0.4993203341836945` as its own working parameter and is
genuinely on C.

## Why this matters

It explains the sweep result that had looked like a contradiction: 11/41
producers re-run, `cleared 0/N` on every one, against a registry
(`trace-convention-registry.md`) saying production is D. An audit that checks C
cannot be "migrated" by re-running it, and neither can a convention-comparison
probe. They are not defects; they are the control arms.

So the earlier reading — "re-running migrates nothing, therefore C lives in
producer code" — was drawn from a sample that included witnesses which are
*supposed* to carry C.

## The heuristic's limits, stated

The audit-context test is a keyword window (`check` / `name` / `label` /
`description` / `assert` / `criterion` within ±260 chars of the decimal). It is
a triage aid, not authority. **Known false positive: it puts
`qbeta-decay-channel-convention-status.witness.json` in the working-value
bucket, and that is a convention-comparison probe** — it carries both C and D
by design and belongs with the mentions. So the 14 is an upper bound on genuine
uses, and at least one is already known to be wrong.

The 7 structural/symbolic hits need no heuristic: a nonzero `y_λ` on a 3+-row
block is convention C by a Lean-proved invariant
(`TemperleyLiebTower.conventionD_kills_antisymmetriser` +
`YoungDiagramThreeRowCorner.threeRow_vanishing_all_levels`). Those are the
defensible work list.

## To close

1. Work the **7** structural hits — they are unambiguous and Lean-backed.
2. Hand-classify the **14**, starting by excluding the convention-comparison
   probes the heuristic mis-sorted.
3. Consider teaching the detector to exclude audit/check contexts, so
   `weight-factor-audit` and its kind stop appearing as work. A detector that
   flags its own control arm trains the reader to ignore it.
