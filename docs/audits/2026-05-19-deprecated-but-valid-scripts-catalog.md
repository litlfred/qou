# Deprecated-but-valid compute scripts — catalog

**Branch**: `claude/closed-forms-first-principles` ([PR #787](https://github.com/litlfred/qou/pull/787))
**Date**: 2026-05-19
**Trigger**: user asked *"check for similar valid deprecated"* after the `prop:unified-curvature-rank-mass-formula` paper↔compute gap finding.

## Systemic finding

The orphan-witness cleanup in [PR #663](https://github.com/litlfred/qou/pull/663) (2026-05-17) moved 262 of 285 candidate scripts to `folio-assistant/computations/_deprecated/`. The criterion was "no live consumer in any `.ts` content block's `computation` field". A grep of the moved scripts reveals **many implement live paper propositions** but were swept up because the propositions' `.ts` manifests do NOT declare a `computation.script` / `computation.witness` field.

This is a **systemic paper↔compute wiring gap**, not a single isolated case. Curated below: 11 propositions whose compute infrastructure was deprecated and which are reviveable by adding a `computation` field to the proposition's `.ts` manifest.

## Top revival candidates

| Proposition | Deprecated script(s) | Why interesting |
|---|---|---|
| `prop:unified-curvature-rank-mass-formula` | `iterative_tower_unified_mass.py`, `strict_3cal_unified_mass.py` | The depth-stratified mass formula — directly relevant to Δ_λ closure (this PR's thread) |
| `prop:confinement-categorical` | `atomic_chirality_residue.py` | "Confinement = spectral-sequence collapse" — core categorical claim |
| `prop:e-infinity-page-identifications` | `atom_level_wedderburn_tower.py` | The E_∞ page → mass-formula bridge |
| `prop:schur-weyl-mass-decomposition` | `atom_level_wedderburn_tower.py` (same script, second prop) | Schur–Weyl-based mass decomposition |
| `prop:mass-endomorphism-tower` | `all_subsets_tower.py`, `atom_per_generator_volumes_sym.py`, `brane_tower_distance_weighted.py`, `brane_tower_plancherel_scaffold.py` (4 scripts!) | Mass-endomorphism tower — many independent implementations all deprecated |
| `prop:binding-scale-catalan` | `binding_full_pipeline.py`, `binding_per_block_log.py`, `catalan_binding.py` (3) | Catalan-constant-scaled binding (Term 7 universal prefactor m_e · 8G) |
| `prop:atomic-mass-gb-nf` | `anti_self_reciprocity_universality_probe.py` | GB normal-form mass formula |
| `prop:atomic-braid-mass` | `atomic_braid_mass_paper_formula.py` | Direct "paper formula" implementation |
| `prop:b-over-a-spectral-decomposition` | `b_over_a_evaluator.py` (3 props in one script: also `prop:confined-knot-binding`, `prop:wigner-np-pairing`) | b/a spectral decomposition |
| `prop:full-pole-structure-mass-trace` | `build_alpha_k_h3_chains.py`, `build_atom_tr_M_chains.py`, `build_c_q_chain.py`, ... (8 build_*_chain.py scripts) | Major build infrastructure for the full pole structure |
| `prop:categorical-mass-markov` | `canonical_isospin_pyhecke.py`, `canonical_isospin_pyhecke_full_census.py`, `canonical_isospin_test.py` (3) | Markov-trace mass — multiple variants |

**Total**: ~30 deprecated scripts referencing ~11 live propositions.

## Why they were deprecated

Per the [`_deprecated/README.md`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/_deprecated/README.md), the cleanup criteria were:

1. no content block consumes the witness (via `computation.witness` / `:val[...]` registry / `witness:` array)
2. no audit doc cites the witness
3. the witness itself has no assertions (`falsifiability == "no-assertions"`)

The 30 scripts above all satisfied (1) — because their corresponding **propositions' `.ts` manifests have no `computation` field**. The root cause is upstream of the cleanup: when these propositions were authored, their categorical statement was committed but the compute hook was not wired.

## Pattern: "narrative-only propositions"

A grep for content-block `.ts` files with `computation` fields shows the wiring rate. Many `prop:*` blocks (especially in `braids-and-knots/` and `descartes-universe/`) are pure narrative, with the implementation expected to be done "downstream" — but downstream never wired it because the proposition didn't claim the script.

This creates a **fragility**: the orphan-cleanup pass correctly identifies dangling scripts and moves them; but the upstream proposition never gets the missing `computation` field added, so the compute gap perpetuates.

## Recommendation

**Add `computation` fields systematically** to the 11 propositions above, pointing to the relevant deprecated script (and its witness). This:

1. Re-wires the paper↔compute connection that was lost.
2. Saves the deprecated scripts from being re-deprecated on the next orphan-cleanup pass.
3. Provides cross-references for downstream consumers (audits, validators).

The fix is **structural** (10-20 `.ts` manifest updates) not **methodological** (the math in the deprecated scripts is fine).

## Priority for revival (closed-forms thread context)

For the current `claude/closed-forms-first-principles` work, the most relevant revival is **`prop:unified-curvature-rank-mass-formula`** + its two scripts (`iterative_tower_unified_mass.py`, `strict_3cal_unified_mass.py`). The log-Δ empirical test (5.22× cross-atom variance) shows this is the right framework for the Δ_λ closure. A full revival requires:

1. `git mv folio-assistant/computations/_deprecated/strict_3cal_unified_mass.py folio-assistant/computations/strict_3cal_unified_mass.py`
2. Add a `WitnessBuilder.set_audit_only(...)` or block-consumer hook to the script.
3. Add `computation: { script: ..., witness: ... }` to `unified-curvature-rank-mass-formula.ts`.
4. Run on D, T, ³He, ⁴He → emit witness → compare to AME.

This is the **next concrete step** for closing the Δ_λ gate, if the user wants to proceed.

## Related: paper-level recommendation

A separate audit-doc pass should check **every `prop:*` block in main** for a `computation` field. Blocks that claim categorical content but have no compute hook are at risk of having their implementation scripts re-deprecated on every orphan-cleanup. The fix is the same: declare the `computation` field at proposition authoring time, BEFORE the implementation script lands in `_deprecated/`.
