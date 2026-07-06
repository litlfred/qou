# Orphan witness characterization (post-deprecation sweep)

**Date:** 2026-05-06
**Audit baseline:** HEAD `bd3fe56d` (after `audit-wiring.ts` registry-aware
patch and the bulk move of 328 dead-exploratory probes into
`computations/_deprecated/`).

```
                 baseline    after registry/auditOnly patch    after deprecation move    after unwrap chains (this PR)
total:           547         547                                219                        189
wired:            95          98                                 98                         98
audit-only:       90          91                                 91                         91
orphan:          362         358                                 30                          0
stale-claims:      0           0                                  3                          0
```

At the **2026-05-06 snapshot**, the remaining 30 orphan witnesses were
the actionable backlog.  This document characterizes those 30 by
failure mode, content-block claim status, and suggested next action.

In the subsequent **unwrap chains** pass (this PR), those 30 were moved
to `_deprecated/`, bringing live orphan count to **0**.

The intermediate `stale-claims: 3` entry is the C.1 subset below:
three witnesses whose `contentBlock` labels were stale at the snapshot;
after unwrap they are no longer in the live audit set, so the live
`stale-claims` count is 0.

## A. FAILING (4) — assertions present and red

These witnesses run, but at least one assertion fails.  They are the
most important backlog items: every FAILING orphan represents a
prediction the substrate is currently violating with no consumer
acknowledging the failure.

| Witness | Assertion summary | Suggested action |
|---|---|---|
| [`chi-inter-and-nchir-rank`](../../computations/_deprecated/chi-inter-and-nchir-rank.witness.json) | 3 assertions, 1 failed: "D: dominant-block rank vs paper n_chir" | Wire to a `prop:` for `n_chir`; if no such prop exists, demote to `audit-only` with a probe-report MD |
| [`level-k-binding`](../../computations/_deprecated/level-k-binding.witness.json) | 1/1 failed: "N≡N triple bond at k=3" | Likely paired with `molecular-binding-level-k`; investigate `level_k_binding.py` source |
| [`molecular-binding-level-k`](../../computations/_deprecated/molecular-binding-level-k.witness.json) | 1/1 failed: "k=3 single bond" | See above — both target the level-k molecular-binding prediction |
| [`proton-neutron-mass-error`](../../computations/_deprecated/proton-neutron-mass-error.witness.json) | 1/1 failed: "tower ratio m_n/m_p matches CODATA within 10%" | Cross-link to `categorical-proton g_A` audit (memory: borromean-axial-coupling.py:30-65); investigate if this is the same y_λ-weighted Markov-trace gap |

## B. malformed (15) — body fails `JSON.parse`

The body of each witness fails strict JSON parsing, almost always
because the producing Python script emitted `-Infinity` or `NaN`
literals via `json.dumps(..., default=str)` (Python-valid, JSON-invalid).
The auditor's intentional `auditOnly` flag is now honored even on
malformed bodies (regex fallback added in this PR), but these witnesses
do not declare `auditOnly`.

| Witness |
|---|
| `alpha-cs-s-eigenvalue-and-cyflq-deltam` |
| `binding-per-block-log` |
| `breakthrough-from-hecke-engine-knot-tracker` |
| `derived-e0-tower-correction-attempt` |
| `explore-1ppb-items-1-and-2` |
| `fresh-tower-gamma-gamma-chirality` |
| `inter-nucleon-crossing-sweep` |
| `next-partition-levels` |
| `nuclear-markov-trace` |
| `probe-proton-crossing-budget` |
| `qbeta-gb-filtration-residues` |
| `qbeta-jet-order-pyhecke` |
| `rho-census-wedderburn-experiment` |
| `shell-level-qvalues` |
| `t35-exact-halflife` |

**Suggested action**: each producer should be patched to (a) replace
`-Infinity` / `NaN` literals with `null` before serialisation, **or**
(b) call `WitnessBuilder.set_audit_only(<report>.md)` if the witness
is exploratory.  Without one of these fixes the bucket-1 / bucket-2
classification cannot run on the body.

## C. passing (11) — green assertions, no consumer

These witnesses run cleanly with passing assertions, but no content
block, `:val[…]` registry entry, or audit report consumes them.

### C.1 — Self-claim a content block that does not exist (3)

The `contentBlock` field on the witness names a label, but **no
content block carries that label** in `content/**/*.ts`.  Either the
witness was authored against an obsolete label or the producing
content block was renamed without updating the witness.

| Witness | Self-claimed `contentBlock` | Real label (closest match) |
|---|---|---|
| `chi-sym-alt-closed-form` | `rem:chi-sym-alt-closed-form` | (no match — likely intended to be a new `remark` block) |
| `qvalue-representation-theory` | `prop:spectral-decomposition-qvalue` | `cor:spectral-decomposition-qvalue` (`content/quantum-observable-universe/descartes-universe/spectral-decomposition-qvalue.ts:4`) — wrong prefix |
| `rosso-jones-qvalues` | `prop:spectral-decomposition-qvalue` | same as above; both witnesses target the same corollary |
| `topological-mass-table` | `rem:amc-calculations` | `prose:amc-calculations` (`content/quantum-observable-universe/appendix-atomic-mass-calculations/amc-calculations.ts:4`) — wrong kind prefix |

**Suggested action**: either fix the `contentBlock` field on the
witness to match the real label, *and* add `computation.witness:
"computations/<name>.witness.json"` to the consumer
block; or drop the `contentBlock` claim and convert to `auditOnly`.

### C.2 — No content-block self-claim (8)

These pass quietly with no declared consumer.  All are likely
exploratory but produce green assertions, so they should not go to
`_deprecated/` without a deliberate decision.

| Witness | Producer script |
|---|---|
| `benzene-resonance` | `benzene_resonance.py` |
| `certificate-to-mass` | `certificate-to-mass.py` |
| `d-inter-correction-test` | `d_inter_correction_test.py` |
| `free-neutrino-groebner-nf` | (script not auto-resolved) |
| `mass-table-combined` | `mass_table_combined.py` |
| `nuclear-ilp` | `nuclear_ilp.py` |
| `proton-mass-tower-derivation` | `proton_mass_tower_derivation.py` |
| `qvalue-representation-theory` | `qvalue-representation-theory.py` (also in C.1) |

**Suggested action per witness**: review whether the result feeds an
existing chapter prediction.  If yes → wire it.  If no but the probe
documents a methodological choice → `auditOnly` with a short report
under `docs/audits/`.  If neither → `_deprecated/`.

## Disposition map

| Bucket | Count | Owner action |
|---|---|---|
| A — FAILING | 4 | Investigate, then wire-to-`prop:` (preferred) or `auditOnly` |
| B — malformed | 15 | Patch producer JSON serialisation **or** mark `auditOnly` |
| C.1 — stale `contentBlock` claim | 3 (4 entries; one overlaps C.2) | Fix label and wire consumer |
| C.2 — silent passing | 8 | Per-item review (wire / `auditOnly` / deprecate) |

## Reproducing the audit

```bash
bun run scripts/audit-wiring.ts --out-dir /tmp/audit-out
column -t -s$'\t' /tmp/audit-out/orphans.tsv
```

Witnesses moved to `computations/_deprecated/` are
intentionally excluded from the audit glob (`*.witness.json` without
`**/`); see `_deprecated/README.md` for the revival procedure.
