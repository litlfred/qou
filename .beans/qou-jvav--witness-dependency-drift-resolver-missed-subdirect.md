---
# qou-jvav
title: witness_dependency_drift resolver missed subdirectory upstreams — 357 of 688 drift records were false
status: completed
type: task
priority: normal
created_at: 2026-08-23T17:11:30Z
updated_at: 2026-08-23T22:14:41Z
---

`staleness-gates.sh` is red on `scriptHash + upstream drift`. Two findings, one
fixed here.

## 1. FIXED — the resolver reported 358 files as missing while they sat in the repo

`witness_dependency_drift.py` resolved a recorded upstream by trying exactly two
locations:

    ups_path = witness_path.parent / ups_name   # a sibling
    if not ups_path.exists():
        ups_path = HERE / ups_name              # computations/ root

That was the entire layout before the Phase-6 refactor moved clusters into
subdirectories. Upstreams that landed in `data/`, `alpha/`, `sweeps/` resolve to
neither and were reported `upstream_missing` — while present:

    ame2020.json                          -> computations/data/
    alpha-cluster-recursion.witness.json  -> computations/alpha/
    low-isotope-binding-sweep.witness.json-> computations/sweeps/

119 records each, **357 of 688 drift records, all false**. Added a third step that
searches the tree, skips `_deprecated`, sorts for determinism, and records any
bare-name matching more than one path in `_AMBIGUOUS_UPSTREAMS` so a wrong pick is
visible rather than silent.

    drift records: 688 -> 330

Checked the two names that do resolve ambiguously
(`canonical-mass-table-extended`, `m-p-borromean-verification-50dps`, each in
`computations/` and `qou-mass/src/qou_mass/data/`): the copies are byte-identical,
so the ambiguity is currently harmless.

## 2. NOT fixed — the remaining 330 are real, and have one dominant cause

242 of them are two upstreams that genuinely changed and whose consumers were never
regenerated. 122 `canonical-isotope-witness-Z*` witnesses all record

    recorded ed68106158faf521b4f0   current 184d7e1287bdbc155834

for `canonical-mass-table-extended.witness.json`. One regeneration, 122 stale
consumers. Same shape for `m-p-borromean-verification-50dps` (121).

## 3. Also found: the per-Z renderer has been dead since witnesses went to strings

`atlas_render_per_z.py` died on its first row with

    TypeError: can't multiply sequence by non-int of type 'float'

because `err_ppm` is now a full-precision STRING (`_precision.fmt`) and the
renderer still did `value * 1000.0`. Fixed by coercing through **mpf, not float** —
the coercion should not be where a 28-digit value gets truncated.

**Its output is deliberately NOT committed.** Running it inserts a 4399-line
`AUTO:per-z-sections` block into
`content/.../recursive-atom-knot-atlas.md`, and those markers have **never** been
in the committed file. That is not restoring lost content, it is publishing a new
appendix section — an author's call, not a side effect of fixing a crash.

## What would actually close the gate

`fail = bool(all_drifts) or (bool(n_self_stale) and args.strict)`, and the gate
passes `--strict`, so BOTH must reach zero:

- 330 upstream drift records — mostly regenerating the 122 + 121 consumers above
- 580 self-stale — the full qou-zymu backlog, still blocked on the stale
  `pyhecke_native` wheel (qou-nm6y) for any producer touching native code

Worth noting the tool's own comment: self-staleness is designed WARN-only
"because self-staleness is widespread until adoption + regeneration catch up, and
we don't want to red-wall every PR on day one" — and the gate runs it in the mode
that red-walls anyway.



---

## Drift now 688 -> 92

The 122 stale consumers named above are regenerated:
`canonical_isotope_witness.py --max-z 118` (119 shards + index). It does not touch
`pyhecke_native`, so it was safe to run even before the wheel rebuild.

    drift records   688 (start)  ->  330 (resolver fix)  ->  92 (this)

Verified with the discipline that earlier cost a commit: **0 assertions flipped
PASS -> FAIL, 0 witnesses collapsed** across all 120.

Self-staleness is unchanged at 580 — a separate axis, and the qou-zymu backlog.
The vendor mirror went red on the regeneration (qou-mass ships 122 package-data
witnesses, these among them) and was re-synced.



---

## Drift 92 -> 69: the q-pin consumers

Regenerated 21 of the 23 witnesses recording a superseded hash for
`q-pinning-50-digit.witness.json` (20 ok, 1 timeout at the 600s cap,
0 errors). Verified: **0 assertions flipped, 0 witnesses collapsed.**

    drift records   688 -> 330 (resolver) -> 92 (isotopes) -> 69 (q-pin)

This is the first regeneration run **after the pyhecke_native rebuild**, so
native-backed producers computed against code matching the source rather than the
two-week-stale wheel.

### Producer lookup by stem is unreliable

Matching witness name to producer by stem found only **8 of 23**. Grepping the
tree for the witness FILENAME found 14 more. Worth knowing for any future drain:
the naming convention between a witness and its producer is not dependable, so
stem-matching silently under-covers.

### One witness has no producer at all

`inter-knot-decoupling.witness.json` is referenced by nothing in the tree — no
`.py` file writes it or names it. It is in the corpus, it is recorded as an
upstream by a consumer, and **it cannot be regenerated**, so its drift is
permanent until someone identifies or rewrites the producer. That is a different
category from 'stale', and no gate distinguishes them.

### What is left

69 records across a long tail — 7 on `habiro-coefficients-atomic`, 6 on
`q-beta-operator-valued-N3`, then 3s and 2s. No single dominant cause remains,
so the rest is per-upstream work rather than one sweep.


---

## The 12 assertion flips are stale passes, not regressions — bisected

Draining the drift tail flipped 12 assertions across 6 witnesses. Applying the
bisect that settled this question once already, rather than assuming either way.

The alarming one first: `m-p-substrate-identity-50dps`,
`m_n_matches_codata_within_10ppb`, **2.389 ppb -> 501.43 ppb** against a 10 ppb
tolerance. A 200x degradation in the neutron-mass prediction.

**Precision is exonerated.** Re-running the producer at
`QOU_COMPUTE_DPS` = 50, 60, 70 gives **501.43180043143343 at every one** — the
same value at the original precision as at the new one. The dps sweep did not
cause it.

**The producer is untouched** by this branch (last changed 2026-08-08) and uses
no native code, so neither the sweep nor the wheel rebuild explains it.

**An input changed.** The witness was last regenerated **2026-08-08**. Its
constants were corrected after that:

    codata_constants.py        2026-08-19  "fix(AME): the canonical binding
                                            reference was hand-typed and 7 of 11
                                            were wrong"
    experimental_constants.py  2026-08-22  CODATA drain (qou-7ot6)

So the 2.4 ppb agreement was computed against **hand-typed constants that were
wrong**, and 501 ppb is the honest number against corrected ones. The flattering
value was an artifact.

All six flipped witnesses were last regenerated **2026-08-08 or 2026-08-02** —
every one predates those fixes. The whole set is the same shape: stale witnesses
recording passes their own inputs no longer support.

This is the second time in this branch that PASS -> FAIL turned out to be the
corpus ceasing to lie rather than breaking. The first time I reverted on
suspicion and put 15 stale passes back for a commit.

## The one shape-guard flag is also benign

`a-K-via-lp-dual-hecke-basis`, `durationMs 6,950 -> 384`. Not a partial write:
206 of 211 data leaves are unchanged and all 4 assertions still pass. The 5 that
moved are all inside `upstream_witness_hashes[0]` — the recorded upstream hash
being refreshed, which is the entire point of the drain. The 18x speedup is
qou-rug0's path fix making `tools/pyhecke/python` actually resolve.


---

## RESOLVED — drift 688 -> 11, and the tool no longer audits retired artifacts

Landed across 93e24e23d (resolver) and de80c6b6b (scan scope + a new kind).

**The resolver** (93e24e23d). `load_and_hash_upstream` records a BARE
FILENAME, and the lookup only tried a sibling directory and the flat
`computations/` root — the whole layout before the Phase-6 refactor moved
clusters into subdirectories. Upstreams that landed in `data/`, `alpha/`,
`sweeps/` matched neither and were reported `upstream_missing` while sitting in
the repo. `ame2020.json`, `alpha-cluster-recursion.witness.json` and
`low-isotope-binding-sweep.witness.json` accounted for **357 of 688 records on
their own, all false**. A third tree-search fallback resolves them;
`_AMBIGUOUS_UPSTREAMS` records any bare name matching more than one path, so a
wrong pick is visible rather than silent.

**The scan scope** (de80c6b6b). The walk included `_deprecated/`, though the
tool already excluded it when resolving an upstream and when locating a
producer. One of those retired artifacts could never be cleared by any
regeneration: `computations/_deprecated/qbeta-gb-filtration-residues.witness.json`
is hand-written and not valid JSON — `"rel_error_pct": +20.27`, and JSON
forbids a leading `+` — so it sat as a permanent `unreadable` record. Scan now
skips `_deprecated`: 14 -> 12 records, 2717 witnesses checked, unverifiable
766 -> 442. `flavor-dressed-mass-from-substrate-split` cleared with it, its
only downstream being deprecated too.

**New `upstream_deprecated` kind** (de80c6b6b), because one live producer
depends on a retired anchor ON PURPOSE:
`probes/he4_sdp_compositional_probe.py` carries its own two-path resolver and
a comment saying the .md cites the anchor at `computations/` but it "currently
lives under computations/_deprecated/ (which _path_bridge.witness_path skips by
convention) — check both explicitly." Calling that `upstream_missing` was
false; passing it silently would hide a live result resting on a retired
artifact. It resolves, and the record says which kind it is.

**Also drained:** isotope consumers (122) and q-pin consumers (21).

Final: **235 witnesses declare `upstream_witness_hashes` (8.6% adoption), 11
drift records** — 10 held by producers under active repair, plus one genuinely
absent upstream, `probe-wedderburn-weight-scheme.witness.json`. That last one
was untracked with its producer in `0763606e4` ("untrack the five root-level
agent-scratch dirs"); recovered from history it carries `"assertions": []` and
is a diagnostic comparing two weight schemes, and the sweep only ever hashed
it without reading its data — so the declaration is being dropped with a
comment recording where it went, not restored.

The 8.6% adoption figure is the real remaining exposure and is a separate
concern from this bean: the `dependency coverage` gate in `staleness-gates.sh`
already tracks it (advisory).
