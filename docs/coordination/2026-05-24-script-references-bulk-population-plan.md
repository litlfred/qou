# Coordination — script `references` metadata bulk-population workplan

**Date:** 2026-05-24
**Status:** Workplan / triage — proposes batches but does NOT populate sidecars (per author direction: human-authored only, no source grep).
**Trigger:** PR [#1091](https://github.com/litlfred/qou/pull/1091) introduced `ScriptQaReport.references: string[]` as the metadata-only model for the `has_references_to_paper` criterion. 545 scripts now fail the criterion because no sidecar has the field populated yet. The metadata is **human-authored only** (no source-grep allowed); populating it is a manual triage.

## Classification (filename heuristics)

Heuristics applied to 541 active Python scripts under `computations/`:

| bucket | count | naming pattern | sidecar action |
|---|---:|---|---|
| **infra** | 22 | starts with `_`, contains `cache`/`util`/`helper`/`adapter`/`registry`/`convention`/`test_`, ends `_cache.py`/`_helper.py`/`_test.py`/etc. | `references: []` (no paper backing) |
| **probe** | 86 | starts with `probe_`/`audit_`/`experiment_`, ends `_probe.py`/`_audit.py` | `references: []` (n/a after [#1110](https://github.com/litlfred/qou/pull/1110)'s exemption merges, but explicit `[]` is good practice) |
| **paper** | 85 | starts with `derive_`/`markov_`/`hecke_`/`mass_`/`atomic_`/`wedderburn_`/`braid_`/`borromean_`/`categorical_`/etc., or ends `_mass_table.py`/`_witness.py`/`_predict.py`/`_derivation.py` | **human review** — set `references: [...]` with actual paper / Mathlib / block citations |
| **ambiguous** | 351 | none of the above patterns match | **needs deeper triage** — read each script's module docstring and module-level constants; classify into paper or infra |
| **total** | 541 | | |

(Numbers reflect a current run; will drift as scripts are added/removed.)

## Per-bucket workplan

### Bucket 1 — INFRA (22 files, batch as a single PR)

These are pure infrastructure modules — caches, utilities, schema adapters, tests. They have no paper math content; their references are correctly the empty array.

**Action:** set `references: []` on each script's sidecar.

```
_li_2_q_util.py                       _prefix_cache.py
_phi_q_util.py                        canonical_tr_m_via_chi_cache.py
_precision.py                         chi_lambda_at_q0_cache.py
constit_factor_and_volhyp_test.py     fr_pullback_cosh_h_test.py
fr_pullback_k1_k2_test.py             fr_pullback_k3_test.py
lp_dual_cache.py                      lr_fusion_self_conj_test.py
ordering_cache.py                     syt_prefix_cache.py
test_bar_involution.py                test_det_pair_law.py
test_engine_equivalence.py            test_lp_dual_cache.py
wenzl_lr_convention_adapter.py        witness_base.py
y_lambda_at_q0_cache.py               y_lambda_pole_order_cache.py
```

**Edit shape (per file):**

```jsonc
// computations/script-qa/<name>.script-qa.json
{
  "$schema": "script-qa/v1",
  "script_path": "...",
  "references": [],          // ← add this line
  // ...rest unchanged
}
```

**Estimated effort:** ~10 min one-pass (22 small JSON edits). 1 PR.

### Bucket 2 — PROBE (86 files, batch as a single PR)

These match the probe/audit naming convention. PR #1110 (in flight) exempts them from `respects_archimedean_wall` via filename pattern, and PR #1091 should be extended similarly for `has_references_to_paper` — OR these can be uniformly tagged `references: []`.

**Recommendation:** uniform `references: []`. Explicit metadata > implicit exemption for audit-clarity.

**Estimated effort:** ~20 min one-pass (86 JSON edits, all identical addition). 1 PR.

### Bucket 3 — PAPER (85 files, needs per-file review)

These have explicit paper-compute naming. For each, the author should:

1. Read the module docstring + early section comments
2. Identify which content blocks (`prop:foo`, `def:bar`, `thm:foo`) the script computes
3. Identify which bibliography keys (`wenzl1988`, `hoefsmit1974`, etc.) the script implements
4. Set `references: [...]` accordingly

**Estimated effort:** ~5 min per file × 85 ≈ 7 hours of focused work. Batch as **3 PRs of ~30 files each**.

**Suggested PR slicing:**

- **PR-A:** mass-table + nuclide compute (~30 files): `applied_uniqueness_mass_table.py`, `atomic_mass_*.py`, `mass_at_3A_proper.py`, `markov_trace_*.py`, etc.
- **PR-B:** Hecke / Wedderburn / Hoefsmit (~30 files): `hecke_*.py`, `wedderburn_*.py`, `hoefsmit_*.py`, `wenzl_*.py`
- **PR-C:** braid / borromean / categorical (~25 files): `braid_*.py`, `borromean_*.py`, `categorical_*.py`, `frobenius_*.py`

### Bucket 4 — AMBIGUOUS (351 files, deeper triage)

Filename doesn't match any pattern. Each needs a manual look at the module docstring to determine whether it's paper-compute (→ Bucket 3 path) or utility/infra (→ Bucket 1 path).

**Recommendation:** do this triage AFTER PRs from Buckets 1/2/3 have landed (so the easier wins are banked first). Run a second classification pass with a `grep -l "prop:\|def:\|thm:"` over the 351 ambiguous scripts; positive matches are paper-compute, negatives are infra.

(But note: per author direction, the grep is a **classification heuristic for THIS workplan**, not for the production checker. The checker still reads only sidecar metadata.)

**Estimated effort:** 1-2 hours of focused triage to split 351 into paper/infra sub-buckets. Then 1-2 more PRs for the bulk metadata.

## Total scope estimate

| bucket | files | PRs | author effort |
|---|---:|---:|---|
| 1 — infra `[]` | 22 | 1 | ~10 min |
| 2 — probe `[]` | 86 | 1 | ~20 min |
| 3 — paper `[...]` | 85 | 3 | ~7 hours |
| 4 — ambiguous triage | 351 | 4-5 | ~10 hours |
| **total** | 544 | 9-10 | ~17 hours focused work |

## What this doc does NOT do

- Does NOT touch any sidecar `references` field. Sidecars are human-authored per [PR #1091](https://github.com/litlfred/qou/pull/1091) + author direction (2026-05-24).
- Does NOT grep scripts for citation patterns to auto-populate. Per author direction: "no citation grepped from content; only proper metadata".
- Does NOT promise specific PR scopes — author chooses pace + slicing.
- Does NOT include the ambiguous-bucket script names (351 entries; see classification pass output).

## Related

- [PR #1091](https://github.com/litlfred/qou/pull/1091) — `references` metadata schema (merged 2026-05-24)
- [PR #1110](https://github.com/litlfred/qou/pull/1110) — `respects_archimedean_wall` probe/audit exemption (parallel pattern)
- AGENTS.md §7c — substrate-vs-archimedean wall (informs the infra bucket criteria)
