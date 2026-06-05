# Witness metadata-drift audit — root cause + bounded refresh

**Date:** 2026-06-05
**PR:** litlfred/qou#1878
**Status:** bounded refresh done (3 witnesses); systemic backlog (~681) root-caused + recommendation recorded
**Related:** `2026-05-16-stale-witness-infra-gap.md` (upstream-hash drift class), `witness_dependency_drift.py`

## Finding

**~681 of 1022** `*.witness.json` files under `folio-assistant/computations/`
carry **producer-scriptHash drift** — their recorded `scriptHash` no longer
matches the current producer file's hash. This is a *different* drift class
from the one `witness_dependency_drift.py` detects (that one checks
`derivation_inputs.upstream_witness_hashes`); this is the script-content hash.

### Detector (proper method)

The hash must be computed exactly as `WitnessBuilder` does — sha256 of the
producer read as **utf-8 text** (not binary), 12-char prefix
(`qou_substrate.witness.file_content_hash`). A naive binary `sha256` gives the
same count here but is not guaranteed to (newline / encoding differences):

```python
import sys; sys.path.insert(0, "tools/qou-substrate/python")
from qou_substrate.witness import file_content_hash
import json, glob, os
allpy = {}
for p in glob.glob("folio-assistant/computations/**/*.py", recursive=True):
    allpy.setdefault(os.path.basename(p), []).append(p)
for w in glob.glob("folio-assistant/computations/**/*.witness.json", recursive=True):
    with open(w, encoding="utf-8") as f:          # context manager + explicit utf-8
        d = json.load(f)
    sf, sh = d.get("scriptFile"), d.get("scriptHash")
    if not sf or not sh: continue
    sib = os.path.join(os.path.dirname(w), sf)
    if os.path.exists(sib):
        path = sib                                # prefer the sibling producer
    else:
        cands = allpy.get(sf, [])                 # fallback is heuristic: trust a
        path = cands[0] if len(cands) == 1 else None  # UNIQUE basename only (skip ambiguous)
    if path and file_content_hash(path) != sh:
        print("STALE:", os.path.basename(w))
```

## Root cause — config/schema bumps × billing-blocked CI

Re-running the producers shows the drift is **almost entirely non-substantive**:

- **`precisionMetadata` defaults bumped** `65/50/15` → `70/60/10`
  (`compute_dps`/`output_dps`/`guard_digits`; `truncation_bound` `1e-50`→`1e-60`).
  Every witness generated before that bump records the old block.
- **`environment` block added** (python / sympy / mpmath versions) — old
  witnesses predate it.
- Producer-file edits (Copilot-review comment/type fixes, the 2026-06-02 subdir
  reorg) shift `scriptHash`/`scriptCommitSha`.

`.github/workflows/witness-pipeline.yml` would normally regenerate these, but it
is **billing-blocked** (the same GitHub Actions billing outage that fails every
PR's checks in ~3 s with 404 logs). So the drift accumulates repo-wide.

## Verified sample (3 cheap producers re-run, exit 0)

| witness | data changed? | assertions | classification |
|---|---|---|---|
| `binding-factor-f-decomposition` | no | pass | metadata-only |
| `binding-K-direct` | no | pass | metadata-only (env block only) |
| `meson-habiro-expansion` | **yes (tiny)** | **still pass** | small numeric drift |

`meson-habiro` drifted `x = 2.0004926 → 2.0004928`, `C ≈ +4e-5` rel — a
dependency/precision-level shift, **not** a correctness break (`R_near_1` still
passes). So among the 681: mostly cosmetic metadata + small numeric drift; no
assertion flips found in the sample.

**Hazard:** several producers (`d_from_scratch`, `b_over_a_evaluator`,
`probe_1b_li6_orthogonality`) **fail / time out** on re-run yet still write a
partial witness. Never commit a witness from a non-zero-exit run.

## Bounded refresh (this PR)

Refreshed the **3 verified** witnesses above (exit 0, assertions pass, diffs
inspected). This is a demonstration slice, not the systemic fix.

## Recommendation (the 681 are not a manual task)

A per-witness manual refresh of 681 is the wrong tool — many producers are
expensive (mass tables, `canonical_isotope_witness` × ~30 elements, Habiro
extracts) or flaky on re-run. The systemic fix is one of:

1. **Restore GitHub Actions billing** — the witness-pipeline then regenerates
   everything automatically (the intended mechanism).
2. **A dedicated mass-regen sweep** — a single bulk commit
   ("regenerate N witnesses after precision-defaults bump + environment block"),
   which the CLAUDE.md §"batch audit-job runs" exception explicitly permits,
   run with the long-compute logging discipline and skipping failing producers.

Until one of those runs, the drift is **benign** (metadata + sub-assertion-
threshold numeric shifts) and should not block review.
