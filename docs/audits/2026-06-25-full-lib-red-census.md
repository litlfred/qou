# Full-library red census (2026-06-25)

Supersedes [`2026-06-11-full-lib-red-census-post-2094.md`](2026-06-11-full-lib-red-census-post-2094.md).

**Method.** Bottom-up fixpoint build of all 803 `QOU/*.lean` modules via pure
`lean -o` (no `lake` — avoids the cache-wipe gotcha) against the restored
`lake-cache/qou-v4-24-0` Mathlib oleans, on `origin/main`. Each module is
classified GREEN (compiles to olean) / RED (real source error) / blocked
(only fails on a missing dependency olean).

**Headline: 597 GREEN, 81 genuinely-RED, 88 cache-artifact.**

## Cache artifacts — NOT source errors (do not 'fix')

- **66 bare `import Mathlib`** — the cache omits the root
  `Mathlib.olean` aggregator (lean-environment-setup gotcha #1); these compile
  in CI. (They do violate the AGENTS.md §8 minimal-imports rule — a separate cleanup.)
- **21 missing Mathlib *submodule* oleans** — mostly modules
  outside the cached build closure; a few may be genuine stale imports
  (e.g. `Mathlib.Algebra.GroupPower.Basic`). Needs a full build or loogle to disambiguate.

## Genuinely-red, by class

| class | count | fixable how |
|---|---|---|
| SYNTAX | 18 | mechanical (λ→Λ, `q⁻ⁿ`→`(q⁻¹)^n`, dangling `/--`→`/-!`, move imports up) |
| NONCOMPUTABLE | 12 | add `noncomputable` |
| unknown-tactic | 3 | per-file |
| UNKNOWN-ID | 8 | Mathlib API-rot rename (needs loogle/source) |
| TYPECLASS | 16 | per-proof instance debugging |
| PROOF-goals | 9 | per-proof |
| PROOF-tactic | 8 | per-proof (tactic re-tune) |
| TYPE | 2 | per-proof |
| missing-decl | 1 | cascade — recheck after dep fix |
| cross-pkg | 1 | cross-package import |
| TIMEOUT | 3 | perf / maxHeartbeats |

### SYNTAX (18)

- `QOU/BraidKnot/DeltaLambdaSignRule.lean` — L43:30: error: unexpected token 'λ'; expected '_' or identifier
- `QOU/BraidKnot/H4SignBlockIsospinLimit.lean` — L37:33: error: unexpected token '²'; expected 'else'
- `QOU/BraidKnot/QuaternionFromHecke.lean` — L59:0: error: invalid 'import' command, it must be used in the beginning of the file
- `QOU/BraidKnot/hoefsmit_scattering_pipeline.lean` — L49:12: error: unexpected token '=>'; expected '[', '{', '|', '⦃' or term
- `QOU/Braiding/skein_crossing_asymmetry.lean` — L15:0: error: invalid 'import' command, it must be used in the beginning of the file
- `QOU/BraidsAndKnots/demazure_fiber_markov_trace.lean` — L18:0: error: invalid 'import' command, it must be used in the beginning of the file
- `QOU/BraidsAndKnots/qmn_recursive_memoized.lean` — L32:28: error: unexpected token 'λ'; expected '(', '[', '_', '{', '⦃' or identifier
- `QOU/BraidsAndKnots/y_lambda_recipe_from_partition.lean` — L33:5: error: unexpected token 'λ'; expected '(', '[', '_', '{', '⦃' or identifier
- `QOU/CategoricalDynamics.lean` — L18:69: error: unexpected token 'variable'; expected 'lemma'
- `QOU/Information/photon_threading_mass.lean` — L33:23: error: unexpected token '|'; expected term
- `QOU/Information/toffoli_transfer_matrix.lean` — L15:0: error: invalid 'import' command, it must be used in the beginning of the file
- `QOU/Interactions/NucleonNFWitness.lean` — L71:53: error: unexpected token '/-!'; expected 'lemma'
- `QOU/LiftingDescent/CosimplicialCrossedGroupoid.lean` — L33:13: error: unexpected token 'section'; expected 'lemma'
- `QOU/Mathlib/RSKBridge.lean` — L66:7: error: unexpected token ':'; expected '[', '{', '|', '⦃' or term
- `QOU/Observations/TraceLocalityMeetsGsNonLocality.lean` — L36:5: error: invalid binder annotation, type is not a class instance
- `QOU/QuantumBloch/PentagonUvCommutation.lean` — L88:59: error: unexpected token '/--'; expected 'lemma'
- `QOU/Substrate/MuWenzlClosure.lean` — L27:33: error: unexpected token '²'; expected 'else'
- `QOU/WedderburnMass/confinement_categorical.lean` — L15:0: error: invalid 'import' command, it must be used in the beginning of the file

### NONCOMPUTABLE (12)

- `QOU/BraidKnot/AppliedBeryllium9Uniqueness.lean` — L32:7: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'non
- `QOU/BraidKnot/AppliedBoron11Uniqueness.lean` — L32:7: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'non
- `QOU/BraidKnot/AppliedCarbon12Uniqueness.lean` — L35:7: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'non
- `QOU/BraidKnot/AppliedDeuteronUniqueness.lean` — L34:7: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'non
- `QOU/BraidKnot/AppliedHelium3Uniqueness.lean` — L42:7: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'non
- `QOU/BraidKnot/AppliedHelium4Uniqueness.lean` — L34:7: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'non
- `QOU/BraidKnot/AppliedLithium6Uniqueness.lean` — L33:7: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'non
- `QOU/BraidKnot/AppliedNitrogen14Uniqueness.lean` — L33:7: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'non
- `QOU/BraidKnot/AppliedOxygen16Uniqueness.lean` — L35:7: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'non
- `QOU/BraidKnot/AppliedTritiumUniqueness.lean` — L36:7: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'non
- `QOU/BraidKnot/PerNucleusMassDerivation.lean` — L100:4: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'no
- `QOU/Substrate/MuOverDetermination.lean` — L52:4: error(lean.dependsOnNoncomputable): failed to compile definition, consider marking it as 'non

### unknown-tactic (3)

- `QOU/BraidKnot/ConditionalClasses.lean` — L64:37: error: unknown tactic
- `QOU/MassEndomorphism/MassEndomorphismConjecture.lean` — L75:3: error: unknown tactic
- `QOU/Mathlib/SpectralSequence.lean` — L58:49: error: unknown tactic

### UNKNOWN-ID (8)

- `QOU/Archimedean/BorromeanQuark.lean` — L35:16: error(lean.unknownIdentifier): Unknown constant `Finset.univ.sum`
- `QOU/Archimedean/integer_stability.lean` — L71:27: error(lean.unknownIdentifier): Unknown identifier `inv_lt_one_iff_of_pos`
- `QOU/BraidKnot/CrossedModuleEulerCharacteristic.lean` — L94:4: error(lean.unknownIdentifier): Unknown constant `List.join`
- `QOU/BraidKnot/CrystalRMatrixSubLemma.lean` — L189:13: error(lean.unknownIdentifier): Unknown constant `QOU.BraidKnot.CrystalGraphRealization.cano
- `QOU/BraidsAndKnots/QSchurYLambdaClosedForm.lean` — L91:3: error(lean.unknownIdentifier): Unknown identifier `Finset.range`
- `QOU/BraidsAndKnots/YLambdaQSchur.lean` — L172:6: error(lean.unknownIdentifier): Unknown identifier `yLambdaQSchur_bar_mullineux`
- `QOU/HyperellipticQuintic/CheckAbs.lean` — L3:7: error(lean.unknownIdentifier): Unknown constant `Complex.abs`
- `QOU/Interactions/GramIndefinite.lean` — L149:38: error(lean.unknownIdentifier): Unknown identifier `mul_apply`

### TYPECLASS (16)

- `QOU/Archimedean/ConfinedKnotBinding.lean` — L47:4: error: failed to synthesize
- `QOU/BraidKnot/BindingConcentration.lean` — L66:37: error: failed to synthesize
- `QOU/BraidKnot/DepthStratifiedFrobeniusReciprocity.lean` — L48:31: error: failed to synthesize
- `QOU/BraidKnot/KnotFactorFrobeniusPairing.lean` — L85:17: error: failed to synthesize
- `QOU/BraidKnot/QRogersPentagonArchimedean.lean` — L35:21: error: failed to synthesize
- `QOU/BraidKnot/SixTermPerDerivationWeights/binding_assembly.lean` — L35:19: error: failed to synthesize
- `QOU/BraidKnot/StructuralRank.lean` — L171:2: error: typeclass instance problem is stuck, it is often due to metavariables
- `QOU/BraidKnot/SubstrateEWHypotheses.lean` — L170:4: error: typeclass instance problem is stuck, it is often due to metavariables
- `QOU/BraidKnot/TwoRoutesProtonMass.lean` — L24:23: error: failed to synthesize
- `QOU/BraidKnot/e_infinity_identifications.lean` — L37:14: error: typeclass instance problem is stuck, it is often due to metavariables
- `QOU/Braiding/mobius_energy.lean` — L33:45: error: typeclass instance problem is stuck, it is often due to metavariables
- `QOU/BraidsAndKnots/wedderburn_bratteli_recursion.lean` — L33:42: error: typeclass instance problem is stuck, it is often due to metavariables
- `QOU/BraidsAndKnots/wenzl_qmn_synergy.lean` — L44:23: error: typeclass instance problem is stuck, it is often due to metavariables
- `QOU/BraidsKnots/skein_mass_from_linking.lean` — L38:11: error: typeclass instance problem is stuck, it is often due to metavariables
- `QOU/CategoricalReeb/SixCanonicalKnotOperators.lean` — L125:68: error: failed to synthesize
- `QOU/WedderburnMass/chirality_residue_mass_term.lean` — L35:27: error: typeclass instance problem is stuck, it is often due to metavariables

### PROOF-goals (9)

- `QOU/Archimedean/tau_leptonic_universality.lean` — L54:2: error: No goals to be solved
- `QOU/BraidKnot/BraidWordBasisGram.lean` — L119:2: error: No goals to be solved
- `QOU/BraidKnot/MmuR9V9Closure.lean` — L206:57: error: unsolved goals
- `QOU/BraidsAndKnots/UnitModulusEigenvalue.lean` — L44:2: error: No goals to be solved
- `QOU/FlavorDressing/FlavorMassSplittingBound.lean` — L78:56: error: No goals to be solved
- `QOU/Interactions/BetaReceptivity.lean` — L54:43: error: unsolved goals
- `QOU/Interactions/NuclearOperatorRegimes.lean` — L48:6: error: No goals to be solved
- `QOU/Mathlib/ArchimedeanRealization.lean` — L51:38: error: unsolved goals
- `QOU/MathlibExt/RpowAlgebra.lean` — L51:2: error: unsolved goals

### PROOF-tactic (8)

- `QOU/Archimedean/AxialCoupling.lean` — L209:6: error: Tactic `rewrite` failed: Did not find an occurrence of the pattern
- `QOU/Archimedean/BranchingConvergence.lean` — L63:8: error: Tactic `rewrite` failed: Did not find an occurrence of the pattern
- `QOU/BraidKnot/HopfBindingLinkEigenvalueIdentity.lean` — L90:10: error: Tactic `rewrite` failed: Did not find an occurrence of the pattern
- `QOU/BraidKnot/PerPartitionKLambda.lean` — L146:17: error: Tactic `unfold` failed to unfold `domContribK2` in
- `QOU/BraidKnot/YangBaxterBlowupTruncation.lean` — L72:6: error: Tactic `rewrite` failed: Did not find an occurrence of the pattern
- `QOU/BraidKnot/eigenvalue_product_expansion.lean` — L42:2: error: Tactic `rfl` failed: The left-hand side
- `QOU/Interactions/CentralElement.lean` — L70:4: error: Tactic `simp` failed with a nested error:
- `QOU/QBeta/QBesselContiguityRecurrence.lean` — L73:20: error: Tactic `rewrite` failed: Did not find an occurrence of the pattern

### TYPE (2)

- `QOU/Archimedean/RSK.lean` — L83:20: error: Function expected at
- `QOU/Braiding/hecke_mass_trace.lean` — L52:52: error: Application type mismatch: The argument

### missing-decl (1)

- `QOU/BraidKnot/MassGapObstruction.lean` — L58:3: error: Invalid field `claim_c_kummer_vanishing`: The environment does not contain `QOU.Algebr

### cross-pkg (1)

- `QOU/PhotonThreading.lean` — L1:0: error: unknown module prefix 'UGB'

### TIMEOUT (3)

- `QOU/Archimedean/PauliWitness/Witness12B.lean` — TIMEOUT(150s)
- `QOU/Interactions/GramMatrixH3Symbolic.lean` — TIMEOUT(150s)
- `QOU/Knots/KauffmanTL3.lean` — TIMEOUT(150s)


## Fixed in this PR (verified `exit 0` via lean-direct)

**17 files driven fully green** — the reliably-mechanical, fully-verifiable subset.

SYNTAX (5):
- `Substrate/MuWenzlClosure` + `BraidKnot/H4SignBlockIsospinLimit` — superscript powers `q⁻ⁿ` → `(q⁻¹)^n`.
- `Mathlib/RSKBridge` — reserved `λ` Big-Operator binder → `Λ` + dangling `/--` → `/-!`.
- `Information/toffoli_transfer_matrix` — imports moved above the `/-!` module docstring.
- `LiftingDescent/CosimplicialCrossedGroupoid` — `noncomputable section` moved above its docstring + missing bare `end` added.

NONCOMPUTABLE (12) — all wrapped in `noncomputable section` (the error is code-gen only; elaboration already succeeded):
- 10 isotope `BraidKnot/Applied{Beryllium9,Boron11,Carbon12,Deuteron,Helium3,Helium4,Lithium6,Nitrogen14,Oxygen16,Tritium}Uniqueness` — thin `abbrev` wrappers of noncomputable SDP objects.
- `BraidKnot/PerNucleusMassDerivation` (`nucleusMass : ℝ`) + `Substrate/MuOverDetermination` (`hbarQ : ℝ := 1 - 1/q`).


## Cascade caveat (read before draining the rest)

The per-class counts above are **first-error** classifications. Fixing a file's first
(e.g. SYNTAX) error frequently reveals further pre-existing errors masked beneath it —
only ~5 of the 18 SYNTAX files were one/two-fix green. Verified-but-deferred (correct
first fix applied locally, then reverted because the file stays red):
- `BraidKnot/DeltaLambdaSignRule` (λ→Λ leaves 32 errs), `BraidsAndKnots/qmn_recursive_memoized`,
  `BraidsAndKnots/y_lambda_recipe_from_partition`, `BraidKnot/hoefsmit_scattering_pipeline`
  — λ→Λ needed but carry deeper typeclass / binder errors.
- `Braiding/skein_crossing_asymmetry`, `BraidsAndKnots/demazure_fiber_markov_trace`,
  `WedderburnMass/confinement_categorical` — import-move needed + deeper errors.
- `BraidKnot/QuaternionFromHecke` — import-move correct, but full verification needs
  `Mathlib.Algebra.Quaternion` (absent from the partial cache).
- `CategoricalDynamics` — multiple doc-comments on `variable`.

Treat the per-class counts as an **upper bound** on "mechanical" effort; each needs
per-file verification. The λ→Λ rename convention matches main commit `30efeb30`.
