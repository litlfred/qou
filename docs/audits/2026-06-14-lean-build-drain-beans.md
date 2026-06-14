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

- [ ] 🟡 `AppendixSurreals/KComplex.lean:103` — `No goals to be solved` (remove extra tactic).
- [x] ✅ `Interactions/QIntegerMassFormula.lean:89` — `No goals`@89 + orphan-docstring@134
  + noncomputable@172 fixed; residual `sorry`@172 is the §3b-cond conjecture-class
  instance (file moves error → has_sorry). lean-direct EXIT 0.
- [x] ✅ `FlavorDressing/FlavorMassSplittingBound.lean:78` — 8 errors (No-goals ×4 +
  `inv_lt_one₀`/`div_lt_iff₀`/`sq_pos_of_ne_zero`→`pow_pos`/`positivity`→`pow_pos`).
  lean-direct EXIT 0.
- [x] ✅ `Information/HeckeLogDecomposition.lean:53` — `Real.log_one_div` → `one_div` +
  `Real.log_inv`. lean-direct EXIT 0.
- [x] ✅ `Archimedean/BorromeanQuark.lean:35` — `Finset.univ.sum`→`∑ i, …` + import
  `Algebra.BigOperators.Fin` & `Fin.VecNotation` (for `![..]`). lean-direct EXIT 0.
- [ ] ⬜ `Archimedean/EmCouplingBringZeroMode.lean:103` — `unexpected '/--' expected 'lemma'`
  (malformed lemma/docstring) + sorry at `:193`.
- [ ] ⬜ `CategoricalDqSquared.lean:43` — SKIPPED. Section/docstring structure fixed locally
  but file references `CategoricalQExtDeriv` with NO local def; only Instanton defines it
  as `Linear ℝ C` while the local theorem declares `Linear R_q C` — reconciling is a §7c
  base-ring design decision, not mechanical. Reverted to HEAD.
- [x] ✅ `LiftingDescent/CosimplicialCrossedGroupoid.lean:33` — docstring orphaned the
  `noncomputable section` + unclosed section; moved docstring + added bare `end`.
  lean-direct EXIT 0.
- [x] ✅ `su2_emergence_volume_determinant.lean:58` — `Unknown identifier SU2EmergenceContext`
  → `import QOU.su2_emergence_dagger_unitarity`. lean-direct EXIT 0.
- [x] ✅ `BraidKnot/WitnessR5Full.lean:67` — Prop-valued struct with ℝ data field →
  dropped `: Prop`. lean-direct EXIT 0.
- [x] ✅ `Braiding/HeckeGenPolyReduction.lean:86` — `module` unknown tactic →
  `import Mathlib.Tactic.Module`. lean-direct EXIT 0.
- [x] ✅ `MassEndomorphism/MassEndomorphismConjecture.lean:75,93` — `ring` unknown tactic →
  `import Mathlib.Tactic.Ring`. lean-direct EXIT 0.
- [x] ✅ `PhiQJSJ.lean:44` — `linarith` unknown tactic → `import Mathlib.Tactic.Linarith`;
  + `TowerSummandRealization.realisation (q := q) β S` named-arg. lean-direct EXIT 0.
- [x] ✅ `MathlibExt/RpowAlgebra.lean:51` — `unsolved goals` (q=0 case) → explicit
  `Real.zero_rpow`. lean-direct EXIT 0.
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
| ✅ drained (verified clean) | 13 |
| 🟡 partial | 2 (Plancherel, KComplex) |
| ⬜ open | 13 |
| ⏭ skipped (needs design decision) | 1 (CategoricalDqSquared) |

Session 2 (2026-06-14, branch `claude/gallant-volta-olmlar`, PR #2295)
drained 9 more: HeckeLogDecomposition, QIntegerMassFormula,
RpowAlgebra, CosimplicialCrossedGroupoid, MassEndomorphismConjecture,
BorromeanQuark, HeckeGenPolyReduction, PhiQJSJ,
su2_emergence_volume_determinant, WitnessR5Full, FlavorMassSplittingBound
(11 commits; all lean-direct EXIT 0). The common roots were missing
tactic imports (`Tactic.Ring`/`.Linarith`/`.Module`),
`field_simp; ring`→"No goals", and the GroupWithZero order refactor
(`inv_lt_one₀`/`div_lt_iff₀`).

Next pass: Tier 2 "No goals / unknown tactic" quick wins, then the
Mathlib-rename beans (HeckeLogDecomposition, TraceLocality), then the
Tier-3 cascades (AtomicMass root unblocks ~101). Each fix verified with
the lean-direct recipe above; a full `lake build QOU` + `proof-objects.json`
regen at the end of the campaign reconciles the dashboard.
