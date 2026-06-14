# Lean build-drain beans (2026-06-14) — one bean per lean file

**Goal:** drain the Lean QA report so blocks move to `proved`. The
build-verified `proof-objects.json` shows the QOU library does not cleanly
compile: **28 erroring library files + 6 library sorries**. Each erroring
file → its content block(s) flip `error`/`has_sorry` → `proved` once it
compiles. One bean per lean file below (30 = 28 error + 2 sorry-only).

Context: [`2026-06-14-lean-two-layer-drift-triage.md`](2026-06-14-lean-two-layer-drift-triage.md).
Live queue mirror: `todos/lean-discharge-queue.json`.

## Fast per-file verification recipe (lean-direct, no full rebuild)

`lake build QOU` rebuilds Mathlib from source (~20 min) and one module
(`Archimedean/PauliWitness/Witness12B.lean`) hangs. To verify ONE fixed
file against the restored oleans (oleans live under `build/lib/lean/`, the
v4.24 layout — NOT `build/lib`):

```bash
export PATH="$HOME/.elan/bin:$PATH" ELAN_NO_OVERRIDE_NOTICE=1
LP=$(find . -type d -path '*/.lake/build/lib/lean' | tr '\n' ':')
LEAN_PATH="$LP" lean <path/to/file.lean>   # exit 0 = compiles, sorry-free
```

(Mathlib-only-import files verify in seconds; files importing other QOU
modules need those QOU oleans built first.)

## Status legend
✅ drained (lean-direct EXIT0) · 🟡 partial (one bug fixed, more remain) · ⬜ open

## Tier 1 — mechanical (syntax / identifier / import / noncomputable)

- [x] ✅ `AlgebraicSubstrate/TwoFiltrationBridgeGeneral.lean` — `λ` used as a
  variable (`conj lam = λ → …`); `λ`→`lam`. → `prop:two-filtration-bridge-general`
- [x] ✅ `AlgebraicSubstrate/TwoFiltrationBridgeSmallCases.lean` — same; `λ`→`lam`.
  → `prop:two-filtration-bridge-small-cases`
- [x] ✅ `BraidKnot/KnotFactorSpectralDerivation.lean` — `Unknown identifier ℝ`
  (add `import Mathlib.Data.Real.Basic`) + `λ`→`lam`. → `prop:knot-factor-spectral-form`
- [x] ✅ `BraidKnot/GramSeminormalBlock.lean` — `noncomputable instance` (Real
  div). → gram-seminormal block
- [ ] 🟡 `BraidKnot/PlancherelWeightBoundedness.lean` — `λ`-binder fixed (`λ`→`lam`);
  **remaining**: 46 `typeclass instance stuck (LE)`, 57 `abs '|' parse` — needs
  an order/abs import + small proof repair. → `prop:plancherel-weight-boundedness`
- [ ] ⬜ `Observations/TraceLocalityMeetsGsNonLocality.lean:36` — `[LinearOrderedField R]`
  is not a class (Mathlib 2025 order refactor deprecated it); replace with
  `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` idiom. **Do not guess
  the exact spelling — confirm against the pinned Mathlib rev.**

## Tier 2 — local semantic (extra tactic / wrong lemma name / structure)

- [ ] ⬜ `AppendixSurreals/KComplex.lean:103` — `No goals to be solved` (remove extra tactic).
- [ ] ⬜ `Interactions/QIntegerMassFormula.lean:89` — `No goals` + sorry at `:172`.
- [ ] ⬜ `FlavorDressing/FlavorMassSplittingBound.lean:78` — `No goals`.
- [ ] ⬜ `Information/HeckeLogDecomposition.lean:53` — `Unknown constant Real.log_one_div`
  (Mathlib rename → find current name, e.g. `Real.log_inv`/`Real.log_div`).
- [ ] ⬜ `Archimedean/BorromeanQuark.lean:35` — `Unknown constant Finset.univ.sum`
  → `∑ x, …` / `Finset.sum Finset.univ` (+ downstream type mismatches).
- [ ] ⬜ `Archimedean/EmCouplingBringZeroMode.lean:103` — `unexpected '/--' expected 'lemma'`
  (malformed lemma/docstring) + sorry at `:193`.
- [ ] ⬜ `CategoricalDqSquared.lean:43` — `unexpected 'section' expected 'lemma'`
  (incomplete lemma before `section`).
- [ ] ⬜ `LiftingDescent/CosimplicialCrossedGroupoid.lean:33` — same incomplete-lemma.
- [ ] ⬜ `su2_emergence_volume_determinant.lean:58` — `Unknown identifier SU2EmergenceContext`
  (missing def/import).
- [ ] ⬜ `BraidKnot/WitnessR5Full.lean:67` — Prop-valued struct field `min_block_eig`
  must be a proof (fix the field type).
- [ ] ⬜ `Braiding/HeckeGenPolyReduction.lean:86` — `unknown tactic`.
- [ ] ⬜ `MassEndomorphism/MassEndomorphismConjecture.lean:75,93` — `unknown tactic`.
- [ ] ⬜ `PhiQJSJ.lean:44` — `unknown tactic`.
- [ ] ⬜ `MathlibExt/RpowAlgebra.lean:51` — `unsolved goals`.
- [ ] ⬜ `Molecular/PalindromicityOrbitalType.lean:42` — `Type mismatch`.
- [ ] ⬜ `Molecular/ShellClosureNfTermCount.lean:92` — `typeclass instance stuck`.

## Tier 3 — bigger / cascade

- [ ] ⬜ `AtomicMass.lean:118` — `rw [ElementDatum.codata_minus_ame_eq_Z_offset]` on an
  **undefined** constant → cascades to ~101 errors. Define the lemma (the comment
  says "refactored via … (PR #1548)" — the refactor dropped the decl) or revert the `rw`.
- [ ] ⬜ `AppendixSurreals/PolynomialEval.lean:156` — `Invalid field 'pow' (Exists.pow)`
  ×38 + sorries at `:357,:453`.
- [ ] ⬜ `Archimedean/HeckeH3.lean:89` — `simp` nested failure (×11).
- [ ] ⬜ `BraidKnot/NucleusEmptySDPUniqueness.lean:105` — `failed to synthesize` (×9).
- [ ] ⬜ `FeynmanPathIntegrals.lean:300` — `Application type mismatch` (×2).
- [ ] ⬜ `QGeometricLanglands.lean:271` — `Application type mismatch` (×7).
- [ ] ⬜ `AppendixSurreals/KComplex.lean` — (see Tier 2; 3 errors total).

## Sorry-only (file compiles; discharge the sorry to reach `proved`)

- [ ] ⬜ `BraidKnot/GSReductionOrder.lean:123` — discharge `sorry`.
- [ ] ⬜ `Archimedean/HyperbolicVolumeIndependence.lean:39` — discharge `sorry`.

## Progress

| | count |
|---|--:|
| ✅ drained (verified clean) | 4 |
| 🟡 partial | 1 (Plancherel) |
| ⬜ open | 25 |

Next pass: Tier 2 "No goals / unknown tactic" quick wins, then the
Mathlib-rename beans (HeckeLogDecomposition, TraceLocality), then the
Tier-3 cascades (AtomicMass root unblocks ~101). Each fix verified with
the lean-direct recipe above; a full `lake build QOU` + `proof-objects.json`
regen at the end of the campaign reconciles the dashboard.
