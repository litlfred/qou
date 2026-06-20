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

## Bucket-B is the SAME cluster (folded in)

The "bucket-B" set (9–10 `lean-infrastructure` remark-blocks with real `.lean`
decls but **no `lean:` field**) is **not a separate task** — every one is a
member of this same out-of-build cluster, and several are *providers* the
item-A files import (e.g. `braid-group-n-strand`, `markov-axioms-primitive`,
`typed-b3-sub-braid-extraction`). They are:

- `braids-and-knots/{braid-group-n-strand,markov-trace-inductive-limit}`
- `mass-endomorphism/{multi-link-jones-q1-extension,u-coordinate-discharges}`
- `mass-theory/{ck-extraction-from-algebraic-rules,mass-tower-deeper-fillers,typed-b3-sub-braid-extraction}`
- `predicted-spectra/{bloch-wigner-mathlib-filler,three-substantive-mathlib-fillers}`
- `stochastic-mechanics/markov-closure-map-axiomatic`

All are `kind: remark` with **no `lean:` field** (only the `"lean-infrastructure"`
tag). Per AGENTS.md §3 a `remark` does not *require* a `.lean` sibling, so
"wiring in" here is a **decision**, made during the same toolchain session:

- **If the block's `.lean` becomes a real in-build module** (because item-A
  importers depend on it): add a `lean: { ref: "qou:QOU.<Path>" }` to the
  `.ts` once the module compiles, promoting the remark to a referenced block.
- **If it stays narrative infrastructure** (no downstream importer needs it
  as a module): leave it as a `remark` with no `lean.ref`; the `.lean` is
  grep-resolved scaffolding. Add it to the broken-import scanner's documented
  exclusion so it stops being re-flagged.

Because the providers (bucket-B) and consumers (bucket-A) are the same
connected component, **wire the whole component in one toolchain session** —
moving a provider also satisfies the consumers that import it, and the
`lean.ref` promotion (bucket-B) happens as each provider's module goes green.

## Corrections (Gemini review of PR #1653)

**1. `em-coupling-projection.lean` is ONE module, not two.** An earlier draft
double-mapped it (the spurious `QOU.ArchimedeanUniverse.EmCouplingProjection`
row, removed). The provider declares `namespace QOU.Archimedean`, so the
canonical target is **`QOU.Archimedean.EmCouplingProjection`** (single row
above). The `import QOU.ArchimedeanUniverse.EmCouplingProjection` in
`predicted-spectra/em-coupling-chern-simons.lean` is a **wrong import in the
consumer** (stale `ArchimedeanUniverse` namespace) — fix it during the
migration to `import QOU.Archimedean.EmCouplingProjection`, not by creating a
second module.

**2. Lean 4 module-name casing — UpperCamelCase, BUT update importers too.**
Six targets currently use snake_case file/module names matching how their
importers reference them today:

| current (snake) | Lean-4 CamelCase |
|---|---|
| `QOU.BraidKnot.braid_group_n_strand` | `QOU.BraidKnot.BraidGroupNStrand` |
| `QOU.BraidKnot.braid_link_types` | `QOU.BraidKnot.BraidLinkTypes` |
| `QOU.BraidKnot.h3_hecke_idempotents` | `QOU.BraidKnot.H3HeckeIdempotents` |
| `QOU.BraidKnot.hoefsmit_V21_cos_symmetrization` | `QOU.BraidKnot.HoefsmitV21CosSymmetrization` |
| `QOU.BraidKnot.markov_axioms_primitive` | `QOU.BraidKnot.MarkovAxiomsPrimitive` |
| `QOU.BraidKnot.q_beta_categorical_precision_ladder` | `QOU.BraidKnot.QBetaCategoricalPrecisionLadder` |

Renaming to CamelCase is the right Lean-4 idiom, **but it is not free**: every
`import QOU.BraidKnot.braid_group_n_strand` in the consumer files must be
updated in lock-step (otherwise the rename re-breaks them). Do the rename +
all importer updates in the same commit during the toolchain session. (The
already-CamelCase targets — `TwoRowStratum`, `KnotFactorAmphicheiral`, etc. —
need no rename, only the move.)
