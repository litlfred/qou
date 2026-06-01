# Migration plan — wire the out-of-build sibling-import cluster into the Lake build

**Status: PLAN ONLY (not executed).** Requires a Lean toolchain to run iteratively
(move a batch → `lake build QOU` → fix errors → repeat). Executing blind would
orphan content-block triples and likely break main's build.

## Why a blind move is unsafe (the trap this plan avoids)

- Each provider `.lean` has `.md`/`.ts`/`.qa.json` siblings (the content-object triple).
  Moving only the `.lean` into `lean/QOU/` orphans it from its block.
- Importers use the **CamelCase module** name (`QOU.Archimedean.EmCouplingProjection`);
  the block's `lean.ref` uses the **snake_case decl** name
  (`qou:QOU.Archimedean.em_coupling_projection`). These are different identifiers;
  a file move alone reconciles neither.

## Provider files → target module path (24 imports, 23 providers)

| Provider (.lean, +md/ts/qa siblings) | Target module | Block lean.ref |
|---|---|---|
| `predicted-spectra/bloch-wigner-mathlib-filler.lean` | `lean/QOU/Archimedean/BlochWignerMathlibFiller.lean` (module `QOU.Archimedean.BlochWignerMathlibFiller`) | `(none)` |
| `predicted-spectra/clausen-function-mathlib-filler.lean` | `lean/QOU/Archimedean/ClausenFunctionMathlibFiller.lean` (module `QOU.Archimedean.ClausenFunctionMathlibFiller`) | `(none)` |
| `predicted-spectra/em-coupling-bring-zero-mode.lean` | `lean/QOU/Archimedean/EmCouplingBringZeroMode.lean` (module `QOU.Archimedean.EmCouplingBringZeroMode`) | `qou:QOU.Archimedean.bring_zero_mode_additive_form` |
| `predicted-spectra/em-coupling-projection.lean` | `lean/QOU/Archimedean/EmCouplingProjection.lean` (module `QOU.Archimedean.EmCouplingProjection`) | `qou:QOU.Archimedean.em_coupling_projection` |
| `mass-theory/em-spectral-completeness.lean` | `lean/QOU/Archimedean/EmSpectralCompleteness.lean` (module `QOU.Archimedean.EmSpectralCompleteness`) | `qou:QOU.Archimedean.em_spectral_completeness` |
| `predicted-spectra/force-carrier-bring-uniqueness.lean` | `lean/QOU/Archimedean/ForceCarrierBringUniqueness.lean` (module `QOU.Archimedean.ForceCarrierBringUniqueness`) | `qou:QOU.Archimedean.force_carrier_bring_uniqueness` |
| `mass-theory/mass-tower-open-problems-classes.lean` | `lean/QOU/Archimedean/MassTowerOpenProblemsClasses.lean` (module `QOU.Archimedean.MassTowerOpenProblemsClasses`) | `(none)` |
| `predicted-spectra/three-substantive-mathlib-fillers.lean` | `lean/QOU/Archimedean/ThreeSubstantiveMathlibFillers.lean` (module `QOU.Archimedean.ThreeSubstantiveMathlibFillers`) | `(none)` |
| `predicted-spectra/torus-knot-genus-four-unique.lean` | `lean/QOU/Archimedean/TorusKnotGenusFourUnique.lean` (module `QOU.Archimedean.TorusKnotGenusFourUnique`) | `qou:QOU.Archimedean.torus_knot_genus_four_unique` |
| `predicted-spectra/type-b-folded-crystal-combinatorics.lean` | `lean/QOU/Archimedean/TypeBFoldedCrystalCombinatorics.lean` (module `QOU.Archimedean.TypeBFoldedCrystalCombinatorics`) | `qou:QOU.Archimedean.TypeBCrystal.PartitionWithCells.content_sum_plus_transpose_content_sum_eq_zero` |
| `predicted-spectra/em-coupling-projection.lean` | `lean/QOU/ArchimedeanUniverse/EmCouplingProjection.lean` (module `QOU.ArchimedeanUniverse.EmCouplingProjection`) | `qou:QOU.Archimedean.em_coupling_projection` |
| `mass-theory/alpha-shift-torus-knot.lean` | `lean/QOU/BraidKnot/AlphaShiftTorus/AlphaShiftTorusKnot.lean` (module `QOU.BraidKnot.AlphaShiftTorus.AlphaShiftTorusKnot`) | `qou:QOU.BraidKnot.AlphaShiftTorus.alpha_shift_torus_knot` |
| `stochastic-mechanics/F3-eps6-leading-eq-neg-2b-cubed.lean` | `lean/QOU/BraidKnot/F3_eps6_leading_eq_neg_2b_cubed.lean` (module `QOU.BraidKnot.F3_eps6_leading_eq_neg_2b_cubed`) | `(none)` |
| `mass-theory/knot-factor-amphicheiral.lean` | `lean/QOU/BraidKnot/KnotFactorAmphicheiral.lean` (module `QOU.BraidKnot.KnotFactorAmphicheiral`) | `qou:QOU.BraidKnot.knot_factor_amphicheiral` |
| `mass-theory/knot-factor-spectral-derivation.lean` | `lean/QOU/BraidKnot/KnotFactorSpectralDerivation.lean` (module `QOU.BraidKnot.KnotFactorSpectralDerivation`) | `qou:QOU.BraidKnot.knot_factor_spectral_derivation` |
| `mass-theory/plancherel-weight-boundedness.lean` | `lean/QOU/BraidKnot/PlancherelWeightBoundedness.lean` (module `QOU.BraidKnot.PlancherelWeightBoundedness`) | `qou:QOU.BraidKnot.plancherel_weight_boundedness` |
| `mass-theory/two-row-stratum.lean` | `lean/QOU/BraidKnot/TwoRowStratum.lean` (module `QOU.BraidKnot.TwoRowStratum`) | `qou:QOU.BraidKnot.TwoRowStratum.TwoRowStratum` |
| `braids-and-knots/braid-group-n-strand.lean` | `lean/QOU/BraidKnot/braid_group_n_strand.lean` (module `QOU.BraidKnot.braid_group_n_strand`) | `(none)` |
| `braids-and-knots/braid-link-types.lean` | `lean/QOU/BraidKnot/braid_link_types.lean` (module `QOU.BraidKnot.braid_link_types`) | `(none)` |
| `braids-and-knots/h3-hecke-idempotents.lean` | `lean/QOU/BraidKnot/h3_hecke_idempotents.lean` (module `QOU.BraidKnot.h3_hecke_idempotents`) | `(none)` |
| `mass-theory/hoefsmit-V21-cos-symmetrization.lean` | `lean/QOU/BraidKnot/hoefsmit_V21_cos_symmetrization.lean` (module `QOU.BraidKnot.hoefsmit_V21_cos_symmetrization`) | `qou:QOU.BraidKnot.hoefsmit_V21_cos_symmetrization` |
| `braids-and-knots/markov-axioms-primitive.lean` | `lean/QOU/BraidKnot/markov_axioms_primitive.lean` (module `QOU.BraidKnot.markov_axioms_primitive`) | `(none)` |
| `mass-theory/q-beta-categorical-precision-ladder.lean` | `lean/QOU/BraidKnot/q_beta_categorical_precision_ladder.lean` (module `QOU.BraidKnot.q_beta_categorical_precision_ladder`) | `qou:QOU.BraidKnot.q_beta_categorical_precision_ladder` |
| `mass-theory/hecke-mass-element.lean` | `lean/QOU/Torsion/HeckeMassElement.lean` (module `QOU.Torsion.HeckeMassElement`) | `qou:QOU.Braiding.HeckeMassElement` |

## Two true missing-deps (no provider — author or cross-package)

- `QOU.GrobnerShirshov.HeckeGS` — real module is `UGB.GrobnerShirshov.HeckeGS` (the **ugb**
  package). Consumers: `climax-volume-mass/vertex-algebra-{relations,jet-relations}.lean`.
  Fix = cross-package import (verify `lakefile` requires ugb) or author a qou shim.
- `QOU.Information` — a **namespace**, not a module; real modules are `QOU.Information.*`.
  Consumers: `information-theory/{q-game-of-life,toffoli-lp-stability}.lean`. Fix = repoint
  to the specific `QOU.Information.<Decl>` module each consumer uses.

## Per-file execution recipe (for the toolchain session)

For each provider row, in dependency order (leaf modules first):
1. `git mv` the `.lean` (and decide: keep `.md`/`.ts`/`.qa` beside the block, or move the
   triple — recommend keeping the block in place and pointing its `lean.ref` at the new
   in-build module path, since the block is narrative).
2. Reconcile the module decl name with importer expectation: importers want the CamelCase
   *module* path; ensure the file declares the namespace and the `lean.ref` decl resolves
   under it. Update the block's `.ts` `lean.ref` to the new `qou:QOU.<Path>` if the decl moved.
3. Add the module to the relevant aggregator (`lean/QOU/BraidKnot.lean`,
   `lean/QOU/Archimedean.lean`, etc.).
4. `lake build QOU` → fix errors (these files have NEVER compiled; expect real errors,
   missing imports, sorry-without-Ref, etc.) → commit the batch.
5. Repeat until the broken-import scan is 0 and the build is green.

## Verification (followup, with toolchain)

- `lake build QOU` exits 0.
- The broken-import scan (this PR's method) reports 0.
- `bun run validate quantum-observable-universe` passes (lean.ref all resolve).
