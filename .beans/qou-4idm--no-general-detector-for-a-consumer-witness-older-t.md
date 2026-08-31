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

## 2026-08-31 — DETECTOR BUILT (`aa85401ac`). 248 stale consumers.

`computations/audits/witness_upstream_staleness_audit.py [--strict] [--limit N]`

    witnesses with a commit date : 3605
    producers referencing one    : 1313
    STALE consumers              : 248

Ordering is by COMMIT DATE, not mtime — a fresh clone gives every file the same
mtime, so an mtime comparison reports nothing in exactly the environment this
runs in. This session started on such a clone.

### Validated, not assumed

Both directions against the known-true case: it reports **0** occurrences of
`low-isotope-binding-model-comparison` now, and the commit dates confirm it
would have fired before the fix (consumer 08-23 < upstream 08-29; now 08-31 >
08-29). A reported hit was spot-checked too — `qbeta_singularity_type_probe`
genuinely `json.load`s the upstream it is 27.7 days behind.

### The backlog is CONCENTRATED — this is the actionable part

248 stale consumers, but they hang off very few upstreams:

    16 each  atom-chi-rust-t / -d / -4he / -3he .witness.json   = 64 consumers
    14       y-lambda-at-q0.witness.json
    12       qbeta-decay-sdp-extended-ck.witness.json
     7       habiro-coefficients-atomic.witness.json
     6       wenzl-y-lambda-h9.witness.json
     4       q-pinning-50-digit.witness.json
     4       joint-tower-sdp-rust.witness.json

Re-running the consumers of the four `atom-chi-rust-*` witnesses alone clears
**64 of 248 (26%)**.

Two of these upstreams are already known-problematic elsewhere, which raises the
stakes rather than lowering them:

- `qbeta-decay-sdp-extended-ck` is the ALL-NULLS witness of `qou-s2no`. Its 12
  consumers are publishing results derived from `c_k` values the upstream no
  longer contains.
- `y-lambda-at-q0.witness.json` is the cache
  `_y_lambda_at_convention_C_HISTORICAL` reads — marked "DEAD — convention C,
  excised 2026-08-09". 14 consumers sit behind a convention-C artifact.

### Not gated yet

No baseline: the backlog is 248 and the numbers shift with every commit, so a
must-only-shrink file would churn. `--strict` exists for when it is drained
enough to gate in CI.

## 2026-08-31 — TWO limits on the detector, and on regeneration generally

### 🛑 The detector OVER-REPORTS: commit date ≠ value change

It flags an upstream as newer by the commit that last TOUCHED it. Some of those
commits change no values at all. Proven on the largest cluster:

    y-lambda-at-q0.witness.json, last touched by
    09340b94f "vendor: re-sync qou-mass mirror after the merge"
        non-ephemeral content identical?  TRUE
        changed non-ephemeral keys:       []

So its 7 flagged consumers are **false positives** — the upstream's values never
moved. The fix is to walk each upstream's history back to the last commit that
changed non-ephemeral content and compare against THAT, not the last touch.
Until then, treat the 208 as an upper bound.

### 🛑 Regeneration is not free: the corpus spans HETEROGENEOUS environments

This container is NEWER than some witnesses (mpmath 1.3.0 → 1.4.1) and **OLDER
than others**. Regenerating one of the latter silently downgrades its provenance
record. I did exactly that, in `e3ccfc9a4`:

    binding-reeb-phase-decomposition
        python 3.13.12 -> 3.11.15;  numpy 2.5.0 -> 2.4.6;  scipy 1.18.0 -> 1.17.1

Reverted in `6fe9c71fc`. The other 9 of that batch are fine (mpmath UP, or the
pyhecke_native_build hash from the wheel rebuild).

The witness tooling already warns about this and was right to:

    "the environment block records LESS than the witness on disk ... install it
     and re-run rather than committing the weaker record; the numbers can be
     identical while the provenance silently degrades."

**Check the environment delta before committing any regeneration**, not just the
values. A staleness drain performed in the wrong container trades a stale number
for a degraded record.

### Bycatch: `habiro_pochhammer_bridge` could not run at all

Its eval namespace bound the substrate value to `check_q` while the upstream's
`a_m` expressions are polynomials in `u` (`-172*u - 172`), so everything past
m=0 raised `NameError`. `check_q` appears nowhere else — a rename leftover, and
NOT a contract that moved: the upstream uses `u` on both sides of its last
regeneration. Fixed; it now runs. Its witness is not committed (this container
would downgrade it, and it reports a real assertion failure at 81596 ppm that
deserves its own look).

## 2026-08-31 (later) — 🛑 I MUST CORRECT THE PREVIOUS ENTRY

The section above claims `y-lambda-at-q0`'s 7 consumers are false positives,
"proven" by showing that `09340b94f vendor: re-sync qou-mass mirror` changed no
non-ephemeral content. **That proof used the wrong file.**

I checked with the glob `'*y-lambda-at-q0.witness.json'`, which matched a
VENDORED copy under `qou-mass/`. The copy in `computations/` was last changed on
2026-08-22 by `410190979 q0: label 229 witnesses from their own payload`, and
that IS a real value change. Those consumers were not false positives.

    ./computations/y-lambda-at-q0.witness.json                       <- the real one
    ./qou-mass/src/qou_mass/y-lambda-at-q0.witness.json              <- mirror
    ./qou-mass/src/qou_mass/data/_deprecated/y-lambda-at-q0.witness.json

**194 witness basenames are duplicated** across 3462 files, almost all via the
`qou-mass` mirror. A glob over basenames is unsafe anywhere in this repo.

### Both fixes are still right, for the reasons found afterwards

1. **Value-change comparison** — still correct as a principle, and it does
   suppress **8** pairs whose upstream was touched without its values moving. It
   just does not suppress the y-lambda ones.

2. **Vendored-copy exclusion** — needed for a reason I had not seen: with
   duplicates present, `_resolve` finds two basename matches, returns None, and
   silently DROPS the pair. Excluding `qou-mass/` and `_deprecated/` made real
   pairs resolve that were being skipped.

### Corrected numbers

    witnesses with a commit date   3605 -> 3095   (510 vendored/deprecated dropped)
    suppressed (values unchanged)                 8
    STALE consumers                248 -> 251

The count went UP, not down. The original 248 was wrong in both directions at
once: it counted mirror churn as upstream change AND dropped real pairs as
ambiguous. 251 is the honest figure.

### The duplicate-basename hazard is NOT a new finding — `qou-kcii` owns it

Before filing "194 duplicated basenames" as a discovery: the corpus already has
`computations/audits/duplicate_witness_stem_audit.py` (bean `qou-kcii`), and it
is a better analysis than mine. It reports TWO numbers because raw duplication
over-reports — 25 duplicated stems, of which **7 are consumer-splitting** — and
it names the mechanism I had not identified:

    `_path_bridge.witness_path()` searches `prefer_dir` first, typically the
    CALLING SCRIPT'S OWN directory, then `computations/`, then each cluster
    subdir. So when one stem exists at two paths, WHICH FILE A CONSUMER GETS
    DEPENDS ON WHERE THE CONSUMER LIVES — two scripts can read "the same
    witness" and receive different numbers.

My 194 is that same phenomenon counted coarsely, inflated by the `qou-mass`
vendor mirror, which is the "corner nothing reads" that audit deliberately
discounts. So:

- the exclusion in THIS audit is still required (ambiguous basenames were
  silently dropping real pairs);
- but there is no new corpus-wide defect to file, and I am not filing one.

I also measured that 76 of 81 witness-globbing audits do not exclude
`qou-mass/`, 44 of them scanning from a root-like base. That is a heuristic
count from a regex, NOT a verified defect list — and given `qou-kcii`'s framing
(a mirror nothing reads is untidy, not dangerous) it is probably mostly
harmless. Recorded as an observation, not a claim.
