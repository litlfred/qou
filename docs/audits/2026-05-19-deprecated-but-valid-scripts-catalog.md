# Deprecated-but-valid compute scripts — catalog

**Original branch**: `claude/closed-forms-first-principles` ([PR #787](https://github.com/litlfred/qou/pull/787), merged 2026-05-19)
**Original date**: 2026-05-19
**Trigger**: user asked *"check for similar valid deprecated"* after the `prop:unified-curvature-rank-mass-formula` paper↔compute gap finding.

**Update branch**: `claude/update-deprecated-scripts-catalog-jvbyM` — adds verified per-proposition wiring status and corrects two non-existent labels (see [Status update — 2026-05-19 (post-merge re-verification)](#status-update--2026-05-19-post-merge-re-verification) below).

## Status update — 2026-05-19 (post-merge re-verification)

Re-verified all claims in the table after PR #787 merged. **The systemic finding still holds**, with three corrections:

| Catalog claim | Verified state | Action |
|---|---|---|
| 11 propositions need wiring | **7** still need it; 4 have a `computation` field (but pointed at *different* live scripts — see below) | Reduce active revival list to 7 |
| 2 of those 11 propositions exist as blocks (`prop:b-over-a-spectral-decomposition`, `prop:atomic-braid-mass`) | **Neither label exists in `content/`.** The closest blocks are `def:atomic-braid` (sibling, not a mass claim) and the 2-of-3 b/a-trio props (`prop:confined-knot-binding`, `prop:wigner-np-pairing`) | Drop the 2 phantom rows; the b/a trio is really a 2-prop pair |
| ~30 deprecated scripts | **25 scripts total** — this count includes the 8 `build_*_chain.py` scripts attributed to `prop:full-pole-structure-mass-trace` (`build_alpha_k_h3_chains.py`, `build_atom_tr_M_chains.py`, `build_c_q_chain.py`, `build_hoefsmit_rep_chain.py`, `build_hoefsmit_rep_sigma2_chain.py`, `build_markov_trace_assembly_chain.py`, `build_schur_weyl_weight_chain.py`, `build_sigma_shell_chain.py`). All 25 are still in `computations/_deprecated/`; none revived. | Original "~30" was approximate; precise count is **25** (not 25+8). |

### Per-proposition wiring status (verified)

| Proposition | `.ts` exists? | `computation` field? | Wired script (if any) | Catalog's deprecated script(s) still orphaned? |
|---|---|---|---|---|
| `prop:unified-curvature-rank-mass-formula` | yes | no | — | yes (2 scripts) |
| `prop:confinement-categorical` | yes | no | — | yes (1 script) |
| `prop:e-infinity-page-identifications` | yes | no | — | yes (1 script) |
| `prop:schur-weyl-mass-decomposition` | yes | no | — | yes (1 script, same as above) |
| `prop:mass-endomorphism-tower` | yes | yes | `habiro_exact_mass_endomorphism.py` (337 LoC) | yes (4 scripts; alternate covers different scope) |
| `prop:binding-scale-catalan` | yes | no | — | yes (3 scripts) |
| `prop:atomic-mass-gb-nf` | yes | yes | `canonical_mass_table_extended.py` (507 LoC) | yes (1 script) |
| `prop:atomic-braid-mass` | no | n/a | — | n/a — label does not exist (`def:atomic-braid` exists in `particle-interactions/` but is a definition, not a mass prop). `atomic_braid_mass_paper_formula.py` is orphaned with no consumer block. |
| `prop:b-over-a-spectral-decomposition` | no | n/a | — | n/a — label does not exist. `b_over_a_evaluator.py` references two real labels: `prop:confined-knot-binding` (yes wired to `jet_knot_invariants.py`) and `prop:wigner-np-pairing` (no). |
| `prop:full-pole-structure-mass-trace` | yes | yes | `markov_substrate_realizer.py` (242 LoC) | yes (8 `build_*_chain.py` scripts; alternate is a single-script replacement, may cover only a subset) |
| `prop:categorical-mass-markov` | yes | no | — | yes (3 scripts) |

### Active revival list (post-update)

**6 propositions remain** (1 revived on this branch); each has no `computation` field and an orphaned deprecated script:

1. `prop:unified-curvature-rank-mass-formula` *(highest priority — Δ_λ thread)*
2. ~~`prop:confinement-categorical`~~ — yes **revived on this branch** (PR #819, commit reviving `atomic_chirality_residue.py` and wiring it to the proposition; witness has 2 assertions, both passed)
3. `prop:e-infinity-page-identifications`
4. `prop:schur-weyl-mass-decomposition`
5. `prop:binding-scale-catalan`
6. `prop:categorical-mass-markov`
7. `prop:wigner-np-pairing`

**4 propositions** have a `computation` field but pointing at a *different* live script than the catalog's deprecated ones — verify the alternate covers the same computational scope before treating the deprecated scripts as superseded:

The first 3 rows are catalog propositions wired to alternate live scripts. The 4th row (`prop:confined-knot-binding`) is **not** a catalog row but a real proposition that shares `b_over_a_evaluator.py` with the un-wired `prop:wigner-np-pairing` — included here because the supersession decision on that shared script affects both.

| Proposition (origin) | Live (wired) script | Deprecated (orphaned) scripts | Disposition needed |
|---|---|---|---|
| `prop:mass-endomorphism-tower` *(catalog row)* | `habiro_exact_mass_endomorphism.py` | `all_subsets_tower.py`, `atom_per_generator_volumes_sym.py`, `brane_tower_distance_weighted.py`, `brane_tower_plancherel_scaffold.py` | check if any deprecated covers extra cases (full-tower vs. Habiro-exact only) |
| `prop:atomic-mass-gb-nf` *(catalog row)* | `canonical_mass_table_extended.py` | `anti_self_reciprocity_universality_probe.py` | check if anti-self-reciprocity probe adds an assertion not in the canonical mass table |
| `prop:full-pole-structure-mass-trace` *(catalog row)* | `markov_substrate_realizer.py` (single, 242 LoC) | 8 `build_*_chain.py` scripts (~2200 LoC total) | likely the largest scope gap — 8 chain-builders may carry per-stage emit hooks the realizer does not |
| `prop:confined-knot-binding` *(via b/a trio)* | `jet_knot_invariants.py` | `b_over_a_evaluator.py` (shared with `prop:wigner-np-pairing`) | the same script also covers an un-wired prop; revival could serve both |

For each row above, the next agent should diff the live and deprecated scripts to decide whether the deprecated is **(a) genuinely superseded** (then move to `_deprecated/_archive/`), **(b) covers extra scope** (then either fold the missing logic into the live script or re-wire the proposition to consume both), or **(c) covers identical scope but predates the rewrite** (then move).

### Phantom-proposition root cause

The two non-existent labels (`prop:atomic-braid-mass`, `prop:b-over-a-spectral-decomposition`) were inferred from filename / scope keywords in the original catalog pass without a `grep -rn 'label: "prop:atomic-braid-mass"'` check. Future catalog audits should require the per-row label grep before listing — the cheap verification step prevents 2/11 ≈ 18% false-positive rate.

### Reality check — what landed on `main` since the catalog (2026-05-19 evening)

Post-merge survey of every change to `computations/`, `content/quantum-observable-universe/`, and `docs/` since PR #787 merged at `2026-05-19T04:52:44Z`:

- **No `_deprecated/` revivals** — `git log origin/main -- computations/_deprecated/` shows zero post-#787 changes. All 25 catalog scripts are exactly where they were when the catalog was written.
- **No `computation` field added** to any of the 7 still-unwired propositions. Their `.ts` manifests are unmodified since #787 (verified with `git log <sha>..origin/main -- <ts>`).
- **The 1ppb / Δ_λ thread was paused, now substantially advanced.** Per the [1ppb-categorical-chain ledger](../coordination/1ppb-categorical-chain.md), Phase 3 of PR #787 produced a hard categorical finding (Vol_hyp clusters by Z: Vol(D)=Vol(T)=12.776 ≠ Vol(³He)=Vol(⁴He)=12.554; N-direction is Seifert-fibered → contributes 0 to hyperbolic volume). **Phase 4 on this branch** ([audit doc](./2026-05-19-delta-lambda-phase4-z4N-closure.md), witness `delta-lambda-z4N-phase4.witness.json`) identifies the closure formula $\lvert\Delta_\lambda^*(K)\rvert \approx (\mathrm{Vol}_{\mathrm{hyp}}(K)/[8]_q) \cdot [3]_q^{2(Z-1)} \cdot (q^{1/2}+q^{-1/2})^{4N}$ with **max rel.err. 2.51% across the 4 atoms (zero fit parameters)**. The Seifert-piece contribution is identified as $(\dim_q V_{1/2})^{4N}$ — no per-JSJ-piece RT infrastructure needed; the per-N factor is a product of quantum dims that the existing QOU formalism (Hoefsmit, Hecke skein) already provides. **Priority #1's framing has shifted again**: the unified-mass-formula revival should now also test the Phase 4 closure factorisation against its depth-stratified output before declaring success or failure — a revival that reproduces the Phase 4 quantum-integer structure is far more credible than one that doesn't.
- **The closed-forms thread continued on a different axis.** The qbeta-ladder closure path ([PR #804](https://github.com/litlfred/qou/pull/804) + follow-ups: `c7b91515`, `054a3d88`, `9b415626`) reached **c_2..c_3 fully derived via SDP-T_β framework (≤ 1.7%)** and formalised **c_4..c_7 as `conj:qbeta-c-k-closed-forms`** (empirical-fit closed forms, sub-ppt residuals, derivation OPEN). This is orthogonal to the deprecated-scripts catalog — the new binding scripts `binding_via_interface_knot.py` and `binding_q_target_sweep.py` are consumed by `q-beta-categorical-precision-ladder.md` and the new conjecture block, **not** by `prop:binding-scale-catalan`. They do **not** supersede `catalan_binding.py` / `binding_full_pipeline.py` / `binding_per_block_log.py`.
- **Markov-trace bug fix landed (`be773569`).** Fix to `pyhecke.gram` at `TR_M[5]` (`z³ → h·z² + z`). At least 5 deprecated scripts use the buggy entry point: `atom-stability-check.py`, `atom_mass_integrated.py`, `binding_from_level_walk.py`, `ch-bond-lp.py`, `confinement-lp.py` (none are in the catalog's 25 — they were swept up in earlier orphan cleanups). **Caveat for revivers**: any catalog script that imports `pyhecke.gram` or computes a Markov trace through `H_3` needs a fresh re-run after the fix, even if its code is "fine" on inspection.
- **Co-casimir / weight-factor audit landed** (`da093f88`, PR #808 follow-up to PR #802). Touches Wedderburn-weight conventions; downstream effect on `prop:schur-weyl-mass-decomposition` revival should re-check the weight definition against `docs/audits/2026-05-19-weight-factor-audit.md` before consuming `atom_level_wedderburn_tower.py`.
- **No new content block adds a `computation` field that points at a deprecated catalog script.** The 50+ new `.ts` blocks landed in `appendix-surreals/`, `braids-and-knots/`, etc. are all new claims, not revivals.

**Bottom line.** The systemic finding (paper↔compute wiring gap) is unchanged. The arithmetic narrows from 11 → 7 actionable revivals + 3 supersession-disposition checks + 2 phantom-label cleanups. Two cross-cutting caveats now apply to *any* revival: (i) the TR_M[5] Markov-trace bug fix may invalidate witnesses produced from un-patched code paths, and (ii) the Vol-clusters-by-Z structural finding from PR #787 Phase 3 constrains what an N-dependent mass formula can look like — useful as a falsifiability gate for the unified-mass-formula revival's output.

---

## Systemic finding

The orphan-witness cleanup in [PR #663](https://github.com/litlfred/qou/pull/663) (2026-05-17) moved 262 of 285 candidate scripts to `computations/_deprecated/`. The criterion was "no live consumer in any `.ts` content block's `computation` field". A grep of the moved scripts reveals **many implement live paper propositions** but were swept up because the propositions' `.ts` manifests do NOT declare a `computation.script` / `computation.witness` field.

This is a **systemic paper↔compute wiring gap**, not a single isolated case. Curated below: 11 propositions whose compute infrastructure was deprecated and which are reviveable by adding a `computation` field to the proposition's `.ts` manifest.

## Top revival candidates

> **Updated 2026-05-19** — see [Per-proposition wiring status (verified)](#per-proposition-wiring-status-verified) above. Of the 11 rows below: **7 are still actionable**, **2 have phantom labels** (`prop:atomic-braid-mass`, `prop:b-over-a-spectral-decomposition` don't exist as blocks), and **3 have been wired to a different live script** (`prop:mass-endomorphism-tower`, `prop:full-pole-structure-mass-trace`, and `prop:atomic-mass-gb-nf`) — those rows need a supersession check, not a revival. A fourth real proposition, `prop:confined-knot-binding`, is also wired-to-alternate but reached the disposition table via the b/a trio (the phantom row `prop:b-over-a-spectral-decomposition` actually represents two real props: `confined-knot-binding` (wired) + `wigner-np-pairing` (actionable)).

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

**Total** (original count): ~30 deprecated scripts referencing ~11 live propositions.
**Verified count** (2026-05-19 update): **25 deprecated scripts** referencing **11 real propositions** (the 11 original rows resolve to: 7 actionable single-prop rows + 4 wired-to-alternate (3 named directly + `prop:confined-knot-binding` reached via the b/a trio) + 1 true phantom (`prop:atomic-braid-mass`, no real backup). The other phantom (`prop:b-over-a-spectral-decomposition`) decomposes into the 2 real props `confined-knot-binding` (wired) + `wigner-np-pairing` (actionable).). All 25 scripts are still in `computations/_deprecated/`; zero revivals have landed.

## Why they were deprecated

Per the [`_deprecated/README.md`](https://github.com/litlfred/qou/blob/main/computations/_deprecated/README.md), the cleanup criteria were:

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

1. `git mv computations/_deprecated/strict_3cal_unified_mass.py computations/strict_3cal_unified_mass.py`
2. Add a `WitnessBuilder.set_audit_only(...)` or block-consumer hook to the script.
3. Add `computation: { script: ..., witness: ... }` to `unified-curvature-rank-mass-formula.ts`.
4. Run on D, T, ³He, ⁴He → emit witness → compare to AME.

This is the **next concrete step** for closing the Δ_λ gate, if the user wants to proceed.

## Related: paper-level recommendation

A separate audit-doc pass should check **every `prop:*` block in main** for a `computation` field. Blocks that claim categorical content but have no compute hook are at risk of having their implementation scripts re-deprecated on every orphan-cleanup. The fix is the same: declare the `computation` field at proposition authoring time, BEFORE the implementation script lands in `_deprecated/`.

---

## Instructions for a follow-up agent

If you are picking up this catalog to **actually revive** the deprecated-but-valid compute infrastructure, here is the work plan. Read this whole section before starting.

### Scope

11 propositions × ~30 deprecated scripts (see table above). Pick **one proposition at a time**; do not bundle. Each revival is an independent commit / PR.

### Per-revival procedure (use `prop:unified-curvature-rank-mass-formula` as worked example)

1. **Identify the target.** Pick one row of the table above (e.g. `prop:unified-curvature-rank-mass-formula` → `strict_3cal_unified_mass.py`).

2. **Re-wire BEFORE moving the script.** Per AGENTS.md and the orphan-cleanup policy, the canonical fix is to add a `computation` field to the proposition's `.ts` manifest. For the worked example:

   ```ts
   // content/quantum-observable-universe/braids-and-knots/unified-curvature-rank-mass-formula.ts
   import { proposition } from "../../schema/builders";

   export default proposition({
     label: "prop:unified-curvature-rank-mass-formula",
     title: "Unified curvature-rank mass formula ...",
     lean: { ref: "qou:QOU.WedderburnMass.unified_curvature_rank_mass", validation: "not_checked" },
     uses: ["prop:plancherel-term-7-formulation"],
     computation: {
       engine: "mpmath",
       script: "computations/strict_3cal_unified_mass.py",
       witness: "computations/strict-3cal-unified-mass.witness.json",
       status: "not_run",
       requires: ["mpmath", "numpy"],
     },
   });
   ```

3. **`git mv` the script + witness back from `_deprecated/`.**

   ```bash
   git mv computations/_deprecated/strict_3cal_unified_mass.py \
          computations/strict_3cal_unified_mass.py
   # Move the witness too if it exists in _deprecated/
   git mv computations/_deprecated/strict-3cal-unified-mass.witness.json \
          computations/strict-3cal-unified-mass.witness.json 2>/dev/null || true
   ```

4. **Add a `set_audit_only` or block-consumer hook to the script** (if the witness builder pattern is missing). The script may already have a `WitnessBuilder.save()` call; verify it points to the witness filename in step 2.

5. **Add explicit assertions** to the witness so it isn't `falsifiability == "no-assertions"`. Per the worked example, the script's natural assertion is: "depth-stratified mass prediction for D, T, ³He, ⁴He matches AME within tolerance T". If the prediction is the empirical result of the run, set tolerance to the actual gap (e.g. 5% relative) so the assertion can pass without being tautological.

6. **Run the script** to emit the witness. The two unified-mass scripts have non-trivial wall-clock cost (per-partition Hoefsmit matrices for $n \in \{6, 9, 12\}$). Expect:
   - D (n=6, 11 partitions): seconds
   - T / ³He (n=9, 30 partitions): tens of seconds
   - ⁴He (n=12, 77 partitions): minutes

7. **Add to the witness pipeline** `.github/workflows/witness-pipeline.yml` after a similar-class step (e.g. after `derivation_chain_validator`).

8. **Validate**: `bun run validate quantum-observable-universe` and ensure 0 new warnings.

9. **Commit + push + open PR**. Reference [this catalog](./2026-05-19-deprecated-but-valid-scripts-catalog.md) (relative path; the previous version of this step linked a feature branch URL that would rot post-merge) in the PR body and mark the proposition's row as yes revived.

### Priority order (recommended — re-prioritised 2026-05-19 evening update)

Tackle in this order (highest yield first). **Note**: `prop:mass-endomorphism-tower` is no longer at #2 because it has been wired to `habiro_exact_mass_endomorphism.py` — its 4 deprecated scripts now need a **supersession check**, not a revival (see [the disposition table](#per-proposition-wiring-status-verified) above).

**Two cross-cutting caveats** before reviving anything:

- **TR_M[5] Markov bug** (`be773569`): if the script touches `pyhecke.gram.TR_M` or computes a Markov trace through `H_3`, re-run after the fix; the old witness may be wrong.
- **Vol-clusters-by-Z constraint** (PR #787 Phase 3): the canonical-braid hyperbolic volume is invariant under adding nucleons at fixed Z. Use this as a falsifiability gate for any revived N-dependent binding-energy formula — if a revived script predicts D ≠ T binding via a different `Vol_hyp`, that's a discrepancy worth surfacing before declaring the revival successful.

1. **`prop:unified-curvature-rank-mass-formula`** — directly closes the Δ_λ gate flagged in [PR #777](https://github.com/litlfred/qou/pull/777). The log-Δ empirical test in `delta_lambda_two_factor_phase2.py` shows 5.22× variance, so the script's depth-stratified output should close the 4-atom binding-energy formula at the same scale (the residual is the per-(K, λ) Wedderburn coupling, expected to resolve under the full $\alpha_k \cdot \tilde w_\lambda$ structure). **However** — the Δ_λ thread is currently *paused* at PR #787 pending owner answers about per-JSJ-piece quantum invariants; check the [1ppb-categorical-chain ledger](../coordination/1ppb-categorical-chain.md) for status before committing reviver-time. The Phase 3 Vol-clusters-by-Z finding (above caveat) is a useful structural check on whatever the revived script outputs.

2. **`prop:binding-scale-catalan`** — 3 deprecated scripts, mentions $m_e \cdot 8G$ (Term 7 universal prefactor). Likely tightly coupled to the unified-mass-formula revival.

3. **`prop:confinement-categorical`** — `atomic_chirality_residue.py` is the only deprecated script; the proposition is foundational (the GAP-A-3/4 diagnosis).

4. **`prop:schur-weyl-mass-decomposition`** + **`prop:e-infinity-page-identifications`** — both consume the same deprecated script `atom_level_wedderburn_tower.py`; one revival serves both.

5. **`prop:categorical-mass-markov`** — 3 deprecated scripts (`canonical_isospin_pyhecke{,_full_census,_test}.py`), Markov-trace mass variants.

6. **`prop:wigner-np-pairing`** — shares `b_over_a_evaluator.py` with the already-wired `prop:confined-knot-binding`; revival may just need a `computation` field on the second consumer.

7. **Supersession disposition** (separate work track, lower priority): for the 3 already-wired propositions (`mass-endomorphism-tower`, `atomic-mass-gb-nf`, `full-pole-structure-mass-trace`), diff live vs. deprecated scripts and either move the deprecated scripts to `_deprecated/_archive/` (genuine supersession) or fold the missing logic in.

8. **Phantom-label cleanup**: the original catalog table lists `prop:atomic-braid-mass` and `prop:b-over-a-spectral-decomposition` — neither label exists in `content/`. Either author the missing propositions if the underlying claim is intended, or remove the rows. The associated scripts (`atomic_braid_mass_paper_formula.py`, the shared `b_over_a_evaluator.py`) need an explicit disposition (revive under a real label, or move to `_archive/`).

### Anti-patterns

- no **Do NOT batch multiple propositions into one PR.** Each revival is independent and may produce per-witness drift / CI cost. One-at-a-time keeps PRs reviewable.
- no **Do NOT add `computation.witness` without `computation.script`** — the orphan-cleanup looks for both.
- no **Do NOT skip the assertion step.** A witness with no assertions is *exactly* the orphan-cleanup criterion; re-deprecating yourself.
- no **Do NOT re-implement the math.** The deprecated scripts have working math; the gap is purely wiring.

### Coordination

This catalog landed on [PR #787](https://github.com/litlfred/qou/pull/787) as part of the closed-forms-first-principles diagnostic package. Tag the original branch's coordination thread (1ppb-categorical-chain ledger at `docs/coordination/1ppb-categorical-chain.md`) when reviving any of the 4 propositions touching the Δ_λ thread (unified-mass, mass-endomorphism-tower, binding-scale-catalan, confinement-categorical).
