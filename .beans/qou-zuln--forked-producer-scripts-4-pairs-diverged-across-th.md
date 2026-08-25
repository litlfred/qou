---
# qou-zuln
title: 'Forked producer scripts: 4 pairs diverged across the reorg, each writing its own witness copy'
status: todo
type: task
created_at: 2026-08-15T23:17:41Z
updated_at: 2026-08-15T23:17:41Z
---


## Found while closing qou-zdz5 (PR #5170)

#5170 fixed `computations/knot-volumes.py`, whose witness was frozen because
the producer wrote beside itself while consumers cited a different directory.
Fixed with the `output_dir=` argument `WitnessBuilder.wrap_legacy` already
had. I then swept the other 24 duplicate-basename witnesses for the same
shape and found something different — and worse.

## The measurement

**4 producer scripts exist in two directories each, and ALL FOUR have
diverged.** (`__init__.py` also appears 12 times; those legitimately differ
per package and are excluded.)

| script | locations | note |
|---|---|---|
| `qbeta_phib_2loop_bdictionary_probe.py` | `computations/probes/` + `computations/qbeta/` | **560-line diff** |
| `probe_qbeta_form.py` | `computations/` + `computations/probes/` | |
| `witness_provenance_audit.py` | `computations/` + `computations/audits/` | an AUDIT script — two versions of a checker |
| `mn_dpn_xq_habiro_element_probe.py` | `computations/` + `computations/probes/` | |

Identical copies: **0**. Every pair has drifted.

Each writes its witness beside itself (`caller_file.parent`), so each fork
maintains a SEPARATE witness copy, and consumers cite one or the other.
Measured on the qbeta pair: the cited copy
(`computations/probes/qbeta-phib-2loop-bdictionary.witness.json`,
`computedAt 2026-07-18T14:10`) is the newer one, produced by the `probes/`
fork; the `qbeta/` fork's copy sits at `2026-07-17T22:06`.

## Why this is not the knot-volumes bug

knot-volumes had ONE producer whose output path drifted away from its
consumers. These have TWO producers. The cited witness is being maintained —
just by only one of the two forks, while the other drifts unobserved. So
there is no frozen-witness symptom to notice, which is why it survived.

The `habiro-coefficients-extended` pair is a third shape again: both
producers (`habiro_coefficients_extended.py` and `..._parallel.py`) live in
`computations/habiro/`, yet the cited copy is at top level and is NEWER than
the one in `habiro/`. Worth understanding before touching it.

## Why I did not fix it

Choosing which fork survives is a per-script judgement, not mechanical:
- a 560-line divergence is a different program, not a stale copy;
- `witness_provenance_audit.py` is a CHECKER — two versions means the repo
  may be auditing itself with either, and they disagree;
- deleting the losing fork changes which witness is canonical, which moves
  `raw-float64-baseline.json` keys.

Needs an owner per pair. The `probe_*` naming suggests `probes/` is the
intended home for three of them, but that is a guess, not evidence.

## Reproduce

```python
# script basenames in >1 directory under computations/, hashed
import os, collections, hashlib
py = collections.defaultdict(list)
for dp, _, fns in os.walk("computations"):
    if "_deprecated" in dp or "__pycache__" in dp: continue
    for fn in fns:
        if fn.endswith(".py"): py[fn].append(os.path.join(dp, fn))
for n, paths in ((n, p) for n, p in py.items() if len(p) > 1):
    hs = {hashlib.sha256(open(p, "rb").read()).hexdigest() for p in paths}
    print("DIVERGED" if len(hs) > 1 else "identical", n, paths)
```
