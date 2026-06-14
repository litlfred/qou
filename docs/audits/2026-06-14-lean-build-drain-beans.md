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
- [x] ✅ `Observations/TraceLocalityMeetsGsNonLocality.lean:36` — `[LinearOrderedField R]`
  removed by Mathlib 2025 order refactor → `[Field R] [LinearOrder R]
  [IsStrictOrderedRing R]` (verified spelling against pinned Mathlib).
  lean-direct EXIT 0.

## Tier 2 — local semantic (extra tactic / wrong lemma name / structure)

- [x] ✅ `AppendixSurreals/KComplex.lean:103` — No-goals @103 (I_mul_I `<;> simp`)
  + @117 (mul_conj `<;> · simp; try ring`). lean-direct EXIT 0.
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
- [x] ✅ `Archimedean/EmCouplingBringZeroMode.lean:103` — orphaned docstring (documented a
  since-removed axiom) → non-doc `/- … -/` comment. File compiles EXIT 0 (error →
  has_sorry); residual `sorry`@191 is a permanent §3b-cond research conjecture
  (Bloch-Wigner range, PR #952) — NOT discharged.
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
- [x] ✅ `Molecular/PalindromicityOrbitalType.lean:42` — filter Prop→Bool (classical decide)
  + simp-loop@63 (`decide`) + malformed `canonical` instance@95 (→ `inferInstance` on the
  verified Z=2, drops a sorry). lean-direct EXIT 0.
- [ ] ⬜ `Molecular/ShellClosureNfTermCount.lean:92` — SKIPPED. `linarith@92` on a
  LaurentPolynomial (Semiring metavar stuck) → could be `sub_eq_zero.mp h`, BUT
  `LaurentPolynomial.T_ne_zero`/`T_injective`@94,217,230 do NOT exist in pinned Mathlib
  and the `ring_nf … linarith [T_ne_zero …]` proofs need genuine reconstruction
  (extract degree-2 coeff via `Finsupp.single_ne_zero`/`single_left_injective`) — not a
  mechanical rename. Left for a focused session.

## Tier 3 — bigger / cascade

- [ ] ⬜ `AtomicMass.lean:118` — `rw [ElementDatum.codata_minus_ame_eq_Z_offset]` on an
  **undefined** constant → cascades to ~101 errors. Define the lemma (the comment
  says "refactored via … (PR #1548)" — the refactor dropped the decl) or revert the `rw`.
- [ ] ⬜ `AppendixSurreals/PolynomialEval.lean:156` — `Invalid field 'pow' (Exists.pow)`
  ×38 + sorries at `:357,:453`.
- [ ] ⬜ `Archimedean/HeckeH3.lean:89` — `simp` nested failure (×11).
- [ ] ⬜ `BraidKnot/NucleusEmptySDPUniqueness.lean:105` — `failed to synthesize` (×9).
- [x] ✅ `FeynmanPathIntegrals.lean:300` — `Fin (n-1)` binder vs `Fin (hecke_q.n-1)`
  expected by `hecke_q.T i`; structure carries `n_eq : hecke_q.n = n`, so changed the
  binder to `Fin (hecke_q.n - 1)`. (Not a real cascade — single index-type fix.)
  lean-direct EXIT 0.
- [ ] ⬜ `QGeometricLanglands.lean:271` — SKIPPED. Mixed errors needing structural
  understanding, not mechanical: universe mismatch `QLocalSystem.{u_1,u_4}` vs `{u_1,u_2}`
  @271; `⟨…⟩` type-inference @306; `introN` on a `Prop` goal @308; `Int.mul_emod_right`
  orientation @329. The universe-polymorphism + anonymous-constructor issues need the
  author's intent on `QLocalSystem`'s universe variables.
- [ ] ⬜ `AppendixSurreals/KComplex.lean` — (see Tier 2; 3 errors total).

## Sorry-only (file compiles; discharge the sorry to reach `proved`)

- [x] ✅ `BraidKnot/GSReductionOrder.lean:123` — sorry discharged via `rfl`: the `canonical`
  instance's trivial `PUnit`/`0`/`0` model makes `order_match : ∀ T, 0 = 0` true by `rfl`
  (does NOT prove the general conjecture, which stays in `[GSOrderMatch]`). lean-direct
  EXIT 0, sorry-free → `proved`.
- [ ] ⬜ `Archimedean/HyperbolicVolumeIndependence.lean:39` — SKIPPED. The `sorry`@42 IS the
  open conjecture by design (algebraic independence of Vol(4₁)/Vol(5₂)/Vol(𝓑₃) over ℚ,
  cited [zagier1986]); §3b conjectural witness, NOT a gap. File already compiles. Discharging
  it would mean proving a Borel-Zagier open problem — out of scope.

## Progress

| | count |
|---|--:|
| ✅ drained / compiles (lean-direct EXIT 0, committed) | 21 |
| 🟡 partial (Plancherel — only file not yet EXIT 0) | 1 |
| ⏭ skipped (needs proof reconstruction / design decision / open conjecture) | 5 |
| ⬜ open (Tier-3 cascades not yet attempted) | 3 |

**Of the 20 EXIT-0 files**: 17 are sorry-free `proved`; 2 (QIntegerMassFormula,
EmCouplingBringZeroMode) compile with a permanent §3b-cond conjecture-class
sorry (error → has_sorry, the legitimate state); 1 (GSReductionOrder) had its
trivial-model sorry discharged via `rfl`.

Session 2 (2026-06-14, branch `claude/gallant-volta-olmlar`, PR #2295)
drained 16 beans across 16 commits — all verified lean-direct EXIT 0:
HeckeLogDecomposition, QIntegerMassFormula, RpowAlgebra,
CosimplicialCrossedGroupoid, MassEndomorphismConjecture, BorromeanQuark,
HeckeGenPolyReduction, PhiQJSJ, su2_emergence_volume_determinant,
WitnessR5Full, FlavorMassSplittingBound, KComplex,
PalindromicityOrbitalType, GSReductionOrder, EmCouplingBringZeroMode,
TraceLocalityMeetsGsNonLocality.

**Root-cause taxonomy** (this session): (a) missing tactic imports —
`ring`/`linarith`/`module` live in `Mathlib.Tactic.*`, not in the
`Mathlib.Algebra.*` data modules (4 files); (b) `field_simp; ring`
→ "No goals" when field_simp already closes (5 files); (c) GroupWithZero
order refactor — `inv_lt_one₀`, `div_lt_iff₀`, drop `LinearOrderedField`
(2 files); (d) orphaned docstrings after a removed axiom/inserted decl,
and unclosed `noncomputable section` (3 files); (e) missing
sibling/notation imports — `Fin.VecNotation` `![..]`, `BigOperators.Fin`
`∑`, sibling `su2_emergence_dagger_unitarity` (3 files); (f) Prop-valued
struct with ℝ data field (1 file).

**Skipped (4), with reasons**: `CategoricalDqSquared` (references
`CategoricalQExtDeriv` with no consistent base ring — §7c design
decision); `ShellClosureNfTermCount` (`T_ne_zero`/`T_injective` don't
exist + `linarith`-on-polynomial proofs need real reconstruction);
`HyperbolicVolumeIndependence` (`sorry` IS the open Borel-Zagier
conjecture, by design — already compiles); `PlancherelWeightBoundedness`
(prior session's partial — LE-stuck + abs-parse, still open).

Remaining open Tier-3 cascades (5): AtomicMass (~101-error cascade),
PolynomialEval (Exists.pow ×38), HeckeH3 (simp ×11),
NucleusEmptySDPUniqueness (synth ×9), FeynmanPathIntegrals +
QGeometricLanglands (app type mismatch).

Next pass: Tier 2 "No goals / unknown tactic" quick wins, then the
Mathlib-rename beans (HeckeLogDecomposition, TraceLocality), then the
Tier-3 cascades (AtomicMass root unblocks ~101). Each fix verified with
the lean-direct recipe above; a full `lake build QOU` + `proof-objects.json`
regen at the end of the campaign reconciles the dashboard.
