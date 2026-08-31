---
# qou-4idm
title: No general detector for a consumer witness older than the upstream witness it READS
status: todo
type: task
created_at: 2026-08-31T04:15:24Z
updated_at: 2026-08-31T04:15:24Z
---


Found 2026-08-31 by accident, while excising one file for `qou-wsfl`.

## The concrete instance

`low_isotope_binding_model_comparison.py` does not compute `B_depth`. It READS
it from another witness:

    depth = _load("binding-depth-stratified.witness.json").get("per_atom", {})
    bdep  = mp.mpf(str(bval))

That upstream was regenerated on **2026-08-29** by `drain(qou-p77d)` and holds
`D: B_MeV = 0.709992911…`. The consumer's own witness dated from **2026-08-23**
and had never been re-run, so it still published `0.606879` — **17% wrong**, for
six days, with `allPassed: true`.

Nothing flagged it. It surfaced only because an unrelated excision happened to
re-run the producer.

## Why the existing gates miss it

There are several staleness tools and each is scoped to one CAUSE:

    codata_2022_downstream_staleness_scan.py   a constants change
    mpmath_version_staleness_probe.py          an engine version change
    q0_muon_witness_staleness_triage.py        an anchor change
    stale_probe_audit.py                       probe-specific

None asks the general, cause-free question: **is any witness older than a
witness it reads?** That is a pure DAG + mtime/commit comparison and it catches
every cause at once, including causes nobody has thought of yet.

## Shape of the fix

The dependency edges already exist — producers `_load(...)` named witness files,
and `computations/audits/witness_dependency_residue_*.py` already walks
something like this graph. A detector needs:

1. for each producer, the witness files it reads (string literals are enough to
   start; `_load("x.witness.json")` is the dominant idiom);
2. for each witness, the commit that last changed it;
3. report any consumer whose witness commit is OLDER than an upstream's.

Ordering by commit date, not mtime — a fresh clone has uniform mtimes, which is
exactly the situation this session started in.

## Caution

Expect a large first result set, and expect it to overlap the q0/anchor
migrations that have been re-running producers all week. The value is in the
ones that are stale for NO tracked reason — like this one, which was collateral
from a float64 drain of something it depends on.
