---
# qou-30vo
title: The import-cone staleness audit's 1473 is dominated by the witness-WRITING module
status: todo
type: task
created_at: 2026-08-23T23:34:15Z
updated_at: 2026-08-23T23:34:15Z
---

computations/witness_import_cone_staleness_audit.py is well-designed and targets a real class -- the third staleness direction, where a producer stays byte-identical (SELF green) while a module it imports moves. My peel finding today is a CONFIRMED instance of exactly that (qou-3zby): markov-peel-atomic-tr-m-muon, producer not self-stale, numbers move up to 2.9x on re-run.

But its headline count cannot be used as a work list.

MEASURED on origin/main 2026-08-23:
  witnesses scanned                3052
  SELF-stale (excluded)             626
  IMPORT-CONE STALE                1473

  tools/qou-substrate/python/qou_substrate/witness.py   last commit 2026-08-23 (today)
  producers importing WitnessBuilder / qou_substrate.witness   2077
  witnesses with computedAt BEFORE 2026-08-23                  1972

1972 >= 1473. So that ONE module -- the witness-WRITING infrastructure -- is
sufficient on its own to explain the entire flagged set. The reported count is
not distinguishable from 'was this witness computed before the last time
anyone touched WitnessBuilder'.

A change to witness.py CANNOT move a mathematical result; it serializes JSON.
The corpus already holds this exact judgement about the same module one field
over: AGENTS.md records that witness.py masks scriptCommitSha in
_EPHEMERAL_META_FIELDS, and that witness_dependency_drift.py keys
self-staleness on scriptHash alone, precisely because that field is provenance
rather than mathematics. The same reasoning applies to the module itself when
it appears in a cone.

THE RANKING IS WORSE THAN THE COUNT. The audit sorts by lag, and all four
visible entries in its 'Worst 25 by lag' name witness.py as the newest
dependency. So the presentation puts the false positives at the top and buries
confirmed cases like peel below them.

PROPOSED FIX, not implemented here: exclude witness-writing / provenance
modules from the cone (qou_substrate/witness.py, computations/witness_base.py,
and the _precision serialization surface), or class them separately and report
both numbers so nothing is hidden. The audit already computes a by-newest-module
breakdown, so the data to do this is present; it just is not applied to the
headline.

SCOPE -- this is an UPPER-BOUND argument, and I am not claiming all 1473 are
false. It shows the infra module is SUFFICIENT to explain the count, so the
count carries no information; it does not show every flagged witness is clean.
Some are genuinely stale for mathematical reasons -- peel is one, confirmed by
re-run rather than by the detector. Deciding which needs the same 're-run to
decide' discipline AGENTS.md already prescribes for witness_staleness_triage,
where 72 substantive producers actually re-run yielded only 28 moved fields
(39%). Do not treat a corrected count as a work order either.
