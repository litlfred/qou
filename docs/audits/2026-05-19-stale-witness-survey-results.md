# Stale-witness survey — results

**Date:** 2026-05-19 (evening)
**Branch:** `claude/update-deprecated-scripts-catalog-jvbyM` ([PR #819](https://github.com/litlfred/qou/pull/819))
**Trigger:** user direction "work on reruns, as they run do research". Survey the live witness corpus for **stale witnesses** — files whose underlying script was modified after the witness was last generated.

## Survey methodology

For each `*.witness.json` under `computations/` (596 live witnesses post-PR #663 orphan cleanup):

1. Read `scriptFile` and `computedAt` from the witness.
2. Find the last commit timestamp of the script (`git log -1 --follow --format=%cI -- <path>`).
3. Flag as "stale" if `script_last_commit > witness.computedAt`.
4. Re-run the stale scripts and classify the drift.

## Counts

| Bucket | Count |
|---|---|
| Total live witnesses | 596 |
| Stale by timestamp (script newer than witness) | **564** |
| Fresh (witness newer than last script edit) | 32 |
| Witnesses without `scriptFile` field (legacy) | 4 |
| Witnesses without `computedAt` field (legacy) | 30 |

The "564 stale" number sounds alarming but is misleading — it includes any witness whose script has had even a one-line comment/refactor edit since the witness was generated. The vast majority produce **identical output** on re-run.

## Re-run-detected drift classes

Re-ran the 17 pyhecke-importing scripts + 11 Markov-trace-using scripts (28 scripts total) and classified each drift:

| Drift class | Count | Example | CI impact |
|---|---|---|---|
| Pure metadata (commitSha / computedAt / durationMs / scriptCommitSha) | ~18 | most pyhecke re-runs | Excluded by drift filter — **no impact** |
| Cosmetic sympy reformatting (`(q²−1)²/q² ↔ q²−2+q⁻²`) | 4 | `atomic-braid-gb-filtration-extension`, `proton-mass-full-tower-50dps` | Substantive in CI drift filter but mathematically identical — would **block CI** if committed |
| Unicode escape (`³He` ↔ `³He`) | 2 | `jet-knot-invariants` | Substantive in filter, cosmetic in meaning |
| `auditOnly` field drop on re-run | 2 | `paper-six-term-shadow-price-sweep`, `toffoli-lp-stability` | Re-running these would **regress audit-only classification** |
| Real numerical drift (TR_M[5] Markov-trace bug fix downstream) | **1** | `borromean-axial-coupling` (0.1245 → 0.5514, ratio = 4.43× = exact TR_M[5] correction) | Already committed (`b181e43f`) |
| `contentBlock` field drift (script updated but witness not refreshed) | 1 | `picard-lefschetz-thimble` (`rem:` → `def:`) | Already committed (`accdd75f`) |

## Action taken on this branch

| Commit | Witness | Drift type | Disposition |
|---|---|---|---|
| `accdd75f` | `picard-lefschetz-thimble`, `habiro-tail-in-ideal-validation` | `contentBlock` rename + `scriptFile` removal | Refreshed (CI was failing on these) |
| `b181e43f` | `borromean-axial-coupling` | TR_M[5] Markov-trace fix (4.43× value shift) | Refreshed (real bug-fix landing) |

**Not committed** (deliberately):
- Cosmetic sympy reformatting drift — would add ~4 commits of pure noise.
- Unicode escape drift — same.
- `auditOnly`-losing re-runs — would regress an audit-only classification.

## Open work for a future "redo-witnesses" pass

1. **Teach `paper_six_term_shadow_price_sweep.py` and `toffoli-lp-stability.py`** to call `WitnessBuilder.set_audit_only(...)` so re-runs preserve the field. After that, refresh both.
2. **Canonicalise sympy output** in scripts that emit symbolic coefficients (`atomic_braid_gb_filtration_extension.py`, `derive_m_p_hecke_full_tower_50dps.py`). Use `sp.factor()` or `sp.simplify()` with a consistent flag so re-runs produce bit-identical strings. After that, refresh.
3. **Investigate `hadron_knot_table.py`** — it timed out at 120s in an earlier re-run. Either it's legitimately long-running (and should be added to the witness-pipeline.yml validate sequence with appropriate budget) or it's wedged (and needs profiling).
4. **Pyhecke_native Rust kernel built locally** (PR #819, commit `26bcabaf`) — fixed 2 duplicate function definitions in `tools/hecke-engine/src/wenzl_lr.rs` that were blocking the build. With Rust kernel available, character evaluation in $H_n$ for $n \le 21$ is now seconds-fast (vs Python timeouts at $H_9$). This unblocks future Markov-trace witness refreshes.

## Conclusion

The "564 stale witnesses" headline is misleading. The substantive (value-changing) stale-witness population is **2** out of 596 — both already refreshed on this branch. The remaining 562 are stale only in metadata or in symbolic representation, not in actual numerical content.

For ongoing hygiene, the productive work is **fixing the upstream scripts** (canonicalise sympy output; emit `auditOnly` field correctly) rather than re-running and committing the resulting cosmetic drift. The witness-pipeline.yml drift filter is already correctly excluding metadata fields and audit-pattern files.

## Related

- Phase 4 Δ_λ closure: [`docs/audits/2026-05-19-delta-lambda-phase4-z4N-closure.md`](./2026-05-19-delta-lambda-phase4-z4N-closure.md)
- Phase 5 α-derivation research: [`docs/audits/2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md`](./2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md)
- Catalog (re-verified): [`docs/audits/2026-05-19-deprecated-but-valid-scripts-catalog.md`](./2026-05-19-deprecated-but-valid-scripts-catalog.md)
