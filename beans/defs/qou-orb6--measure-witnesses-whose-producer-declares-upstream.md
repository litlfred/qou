---
# qou-orb6
title: 'MEASURE: witnesses whose producer declares upstreams but that record no edge are invisible to witness_dependency_drift'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T16:15:24Z
updated_at: 2026-10-04T15:21:32Z
parent: qou-5vkl
---

## Not a new class — a RECURRENCE of the one `producer_upstream_edge_gap_audit`
## retracted to, with the cost measured

That audit's RETRACTION (2026-08-23) narrowed its finding to: *"the previously
committed witness was generated a month BEFORE its producer learned to record
edges, so that witness had no edge and the drift detector could not walk to
it ... narrower and self-closing."*

Correct about the mechanism. **"Self-closing" says nothing about how long, or
how wrong, before it closes** — and this is the measurement of that.

### The worked instance (PR #5671, bean `qou-nmza`)

`averaged-block-swap-binding.witness.json`, committed state before the fix:

    computedAt                 2026-06-11T02:21:28
    upstream_witness_hashes    ABSENT
    data.atom_traces.id        0.055358425349822354

Its producer DOES declare the edge (`add_upstream(HERE /
"binding-canonical.witness.json")`), but the committed witness predates that
instrumentation, so `witness_dependency_drift` could not walk to it. Meanwhile
`binding-canonical` was recomputed 2026-08-22 under convention D to
`0.16097414544240738…`.

**Result: 2.5 months at rel 0.6561 — 65.6 % wrong — while carrying
`id_trace_matches_binding_canonical` at tolerance 1e-9 marked PASSED.**
Post-re-run the same assertion holds at 2.96e-31.

That compounding is the point: the missing edge hides the staleness, and the
frozen assertion actively asserts the opposite. Documented as a mechanism in
`witness_failed_assertion_audit.py` (§"A second way a PASSING assertion lies").

## Measurement — and its LIMITS, which are not yet bounded

Name-based mapping (producer that calls `add_upstream`/`record_upstream` ->
its `WitnessBuilder("<stem>")`), over the tracked tree:

    witnesses whose producer declares upstreams : 165
      edge recorded (drift detector can walk)   : 113
      NO edge recorded -> invisible to drift    :  52   (32 %)

    by witness computedAt:  2026-05: 8   06: 24   07: 2   08: 18

**DO NOT QUOTE 52 AS A FINDING.** At least one confirmed false positive:
`path-b-evacuation.witness.json` was attributed to
`tools/qou-substrate/python/qou_substrate/witness.py` — the WitnessBuilder
LIBRARY, whose line 1094 contains `WitnessBuilder("path-b-evacuation", …)`.
A name-based map cannot tell a producer from an example inside the library.
The false-positive rate is unbounded because I stopped here.

## The part that is NOT explained, and matters most

18 of the 52 have `computedAt` in 2026-08 — **after** the 2026-08-08
`record_upstream` port, several on 2026-08-23/24. "Self-closing" does not
cover those. Three were spot-checked and their producers genuinely do declare:

    delta_lambda_categorical_verification.py  record_upstream:80, add_upstream_records:248
    binding_block_multiplicative.py           record_upstream:142, add_upstream_records:312
    l2_row_independence_probe.py              record_upstream:86

yet e.g. `delta-lambda-categorical-verification.witness.json` has NO
`upstream_witness_hashes` under any spelling (checked `upstream`, `upstreams`,
`provenance` too). So either `_UPSTREAM_RECORDS` is empty on the path taken,
or the `record_upstream` call sites are in branches not executed. **Resolve
this before drawing any conclusion from the 52** — if declared-but-unwritten
is the common case, the fix is in the producers' control flow, not a
regeneration wave, and the two framings imply completely different work.

## Next steps, in order

1. Explain the 18 post-port cases. That determines everything else.
2. Rebuild the mapping AST-side (a `WitnessBuilder(...)` in the module that
   also has the `add_upstream` call), not by name, and exclude
   `qou_substrate/witness.py` itself.
3. Only then decide between "regenerate the pre-port backlog" and "fix
   producer control flow".

## Coordination

This axis is owned by `computations/audits/producer_upstream_edge_gap_audit.py`
and `computations/witness_upstream_declaration_audit.py`. **Do not build a
third detector** — extend one of those. This bean exists to carry the measured
cost (65.6 %, 2.5 months) that the existing retraction's "self-closing" framing
leaves out, plus the unresolved post-port count.


---

## STEP 1 ANSWERED — it is a live bug, not an aging backlog

And the "52" above is **superseded**. Do not use it.

`witness_upstream_declaration_audit.py` now carries
`declaration_reaches_witness`, which answers the question the name-based count
could not: the producer declares — does the declaration REACH the witness?

    declares, but the declaration CANNOT REACH the witness:  21
        ATTACHED_TOO_EARLY  19
        NEVER_ATTACHED       2

**ATTACHED_TOO_EARLY.** `add_upstream_records(_UPSTREAM_RECORDS)` sits
immediately after `WitnessBuilder(...)` — the natural place, and wrong,
because the records are gathered LATER by the loaders and
`add_upstream_records` COPIES (`for r in records or []`):

    builder = WitnessBuilder("delta-lambda-categorical-verification")
    builder.add_upstream_records(_UPSTREAM_RECORDS)   # 248 — list is EMPTY
    ...
    tr_M, partitions = load_chi_deuteron()            # 256 — populates it

The comment on that line reads *"declare upstreams read **before** this
builder existed"*. It states the correct use while the placement contradicts
it, which is presumably how it survived review 19 times.

**NEVER_ATTACHED.** `record_upstream` fills a list no `add_upstream_records`
consumes: `l2_row_independence_probe`, `codata_registry_triangulation_probe`.

## The false positive that halved it — 40 -> 21

The first run said 40. A function that populates the list is **not** a "later
populator" when it is the very function CONTAINING the
`add_upstream_records` call: a module-level `raise SystemExit(main())` is
trivially after every line inside `main`. Without excluding the owner, every
producer whose `main` does both is flagged — **including `q_weighted_block_swap`,
which I had verified as correct an hour earlier.**

Validated 6/6 against WITNESS ground truth rather than against the detector:
the four spot-checked flagged producers carry no `data.upstream_witness_hashes`;
both controls do. Guard case is in the self-tests (18/18), not only in a commit
message — third detector of mine to over-fire this session, and the first two
lessons lived only in commit messages.

## What this does and does not supersede

* **Superseded**: the 52 name-based count for the *declared-but-unreachable*
  half. Use the audit's 21.
* **Still open**: the *never-declared* half — the same audit's long-standing
  `undeclared (invisible to drift): 211 (270 edges)`. Different defect, same
  consequence.
* **Step 2** (rebuild the mapping AST-side) is therefore mostly moot for the
  declared half and unnecessary for the undeclared half, which the audit
  already measures correctly.

## Remaining work, re-scoped

1. Fix the 21. Each fix moves `add_upstream_records` after the loaders, which
   **changes witness content** (it records the upstream hash) — 21
   regenerations, sequenced, never a sweep. That is the whole remaining task
   for this half.
2. Consider making `add_upstream_records` on an empty list a WARNING at the
   library level. It is almost never intentional, and it would have caught all
   19 at authoring time instead of two months later. (Owner call — it touches
   `qou_substrate/witness.py`, which every producer imports.)


## CORRECTION to step 1's own result: NEVER_ATTACHED was 2, it is 0

Caught by starting the fix instead of trusting my own label.
`l2_row_independence_probe` and `codata_registry_triangulation_probe` both do:

    w.save(extra={"upstream": _UPSTREAM} if _UPSTREAM else None)

and their committed witnesses carry a **top-level `upstream`** list with real
`path` + `sha256`. They declared their edge correctly. The defect is one level
over: `witness_dependency_drift` reads
`derivation_inputs.upstream_witness_hashes` or `data.upstream_witness_hashes`
(source L129-130, L283-284) **and nothing else**, so a good edge sits where
nothing walks it.

New tier `RECORDED_OFF_PATH`. Counts:

    ATTACHED_TOO_EARLY  19      (unchanged — that finding stands)
    RECORDED_OFF_PATH    2      (was mislabelled NEVER_ATTACHED)
    NEVER_ATTACHED       0

Total 21 unchanged.

**Why the relabel matters for the work, not just the wording.** "Never
attached" blames a producer that did the job, and points the fix at the
producer. `RECORDED_OFF_PATH` opens a cheaper option: widen the drift
detector's read to include top-level `upstream` — **one reader instead of two
producers**, and it needs no regeneration at all, since the edges are already
on disk. That is the opposite trade from the 19, each of which needs a
producer re-run.

Recommend: fix the 2 at the READER (one change, zero regenerations), and the
19 at the PRODUCER (19 sequenced regenerations). Do not do all 21 the same way.

**Third correction of my own count on this axis** — 40 -> 21, the name-based
"52" retracted, and now this. The pattern in all three: a detector that
encodes what I expected the code to look like rather than what it does. Guard
cases now in the self-tests (19/19) rather than in commit messages.


## BLOCKER for the 19 regenerations: this container's native build does not match

Found while running the gates for the correction PR (#5683).
`witness_provenance_audit.py --strict` refused to write:

    this container would record LESS than the witness on disk — downgraded
    pyhecke_native_build 30fd920c241a54fa -> b843d058d29dcec6. The file was NOT
    modified and its stronger environment block was kept. ... but any OTHER
    witness you regenerate here will carry the weaker record, so install the
    missing libraries before a batch run.

The guard worked — nothing weaker was committed. But its warning is the
operative fact for this bean's remaining work: **the 19 `ATTACHED_TOO_EARLY`
fixes each require a producer re-run, and a re-run in this container stamps
the weaker `pyhecke_native_build`.** Do not start that batch until the
extension is rebuilt to match, or every one of the 19 trades an upstream-edge
fix for an environment-provenance regression.

The container was recycled on session resume, which is when the hash changed.
Worth checking whether `maturin build --release` from `tools/pyhecke-native/`
reproduces `30fd920c241a54fa` or yields a third hash — if the build is not
reproducible, this guard will fire on every fresh container and the corpus's
recorded value is unreachable rather than merely missing. That is a different
problem and would need its own decision.

Separately, a process note from the same run: my first regeneration attempt
ran the audit **without `--strict`** while the committed copy was produced
with it, which degraded the `invocation` block (`reproduce` lost the flag).
Reverted and re-run correctly. **Match the committed invocation, not just the
environment** — the witness records how it was produced, and a weaker command
line is a weaker record even when every number is identical.


## RETRACTION of the blocker above — the 19 regenerations are NOT blocked

The section immediately above says the 19 `ATTACHED_TOO_EARLY` regenerations
are blocked on a `pyhecke_native_build` mismatch. **That is wrong.** The defect
was in the guard, and it is now fixed.

`pyhecke_native_build` is `sha256(<compiled .so>)[:16]` — a content hash of the
binary, not a version. `_environment_delta` was ordering it with
`_version_tuple`:

    _version_tuple("30fd920c241a54fa") == (30,)    # leading "30" parsed
    _version_tuple("b843d058d29dcec6") == ()       # starts with a letter
    () < (30,)  ->  reported as a DOWNGRADE

The verdict depends on whether the hash begins with a digit. On real corpus
pairs it is a coin flip: `b9cd89fd -> 0aaae203` "upgraded",
`0aaae203 -> e114ae83` "downgraded", `fe19077e -> 30fd920c` "upgraded".

There was never a corpus constant to be downgraded from: **five distinct
values across 811 committed witnesses**, all within 2026-08-22..24. A Rust
release build is not byte-reproducible across containers, so this changes on
every rebuild by design.

**The guard was corrupting the thing it protects.** A false "downgraded" sends
`save()` down the preserve path, keeping the OLD environment block — so a
freshly computed witness silently carries the previous container's build hash,
about half the time.

Fixed with `_NON_ORDINAL_ENV_KEYS`; a *missing* key still reports `stripped`,
and real version moves still report. Verified in both directions.

**So: proceed with the 19.** No rebuild needed, no batch-run precondition. The
"install the missing libraries before a batch run" advice in the warning was
itself a product of the false verdict.

The process note from that section still stands and is unaffected: **match the
committed invocation** (`--strict`), not just the environment.

### Why this one mattered more than the earlier corrections

40 -> 21, "52" retracted, `NEVER_ATTACHED` -> `RECORDED_OFF_PATH` were all
miscounts. This one would have **stopped legitimate work** — it told the next
agent that 19 fixes were unavailable until a rebuild that would not have
helped. The claim came from reading the guard's message; one measurement of
the corpus falsified it. Test the blocker before recording it.


## The 2 RECORDED_OFF_PATH are CLOSED — at the reader, as recommended

`witness_dependency_drift` now reads a third location, top-level `upstream`,
at both sites (`check_witness` and `_upstream_edges`; the second feeds
transitive propagation, and omitting it there would leave an edge visible to
direct checks but invisible to staleness travelling along it).

One change, zero regenerations — the trade the `RECORDED_OFF_PATH` relabel
predicted.

Blast radius measured BEFORE changing anything: exactly 2 witnesses carry a
top-level `upstream` that went unread, one edge each, and ZERO carry both
spellings, so no existing edge changed meaning.

    declaring witnesses  244 -> 246
    drift records        290 -> 292
    self-stale           490 -> 490   (untouched)
    transitive            41 ->  41   (untouched)

**Both new records are real staleness.** `l2-row-independence` and
`codata-registry-triangulation` each declare
`per-observable-100x-status.witness.json` at sha `eea3d26d…` recorded
2026-08-09; the file on disk is `334ebf17…`. Two weeks stale against a moved
upstream, invisible the whole time. The fix paid for itself on the first run.

Not a blocking gate — `witness_dependency_drift` runs only in
`witness-staleness.yml`, which is `workflow_dispatch`-only and invokes it with
`|| true`. The two added records cannot turn anything red.

### Remaining on this bean

1. **19 `ATTACHED_TOO_EARLY`** — move `add_upstream_records` after the
   loaders. Each changes witness content, so 19 sequenced producer re-runs.
   NOT blocked (the native-build blocker above is retracted).
2. **Clear the 2 drifts just surfaced** — re-run those two producers against
   the current `per-observable-100x-status`. Deliberately not done in the
   reader fix; it is a witness change and belongs with (1).
3. **The undeclared half** — 211 producers / 270 edges that declare nothing at
   all. Much larger than everything above, and measured by the same audit.
