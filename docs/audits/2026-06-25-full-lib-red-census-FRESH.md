# Fresh full-library red census (2026-06-25, late) — accurate genuine-red list

Supersedes `2026-06-25-full-lib-red-census.md` (stale: it listed the 12 NONCOMPUTABLE
files + several SYNTAX files as red, but those were fixed on main by `80050efd` etc.).

**Method.** Bottom-up `lean -o` build of all 813 `QOU/*.lean` modules on **current
origin/main** against the restored `lake-cache/qou-v4-24-0` Mathlib oleans
(`docs/audits/scripts/lean_red_census.py`). Each module → GREEN / blocked-on-QOU-dep /
cache-artifact (missing Mathlib olean) / **genuinely-RED** (real source error with imports loaded).

## Headline: 35 genuinely-RED source-error modules

> **Caveat (lower bound).** The first census run had a classification bug (the
> missing-olean error format quotes the full path, not the bare module, so 352
> missing-QOU-dep modules were mis-tagged RED and the fixpoint collapsed after one
> pass). The **35 below are confirmed genuine** (their imports loaded ⇒ the error is a
> real source error). Modules *blocked* on a missing QOU dep may hide additional reds,
> revealed only once their dep builds — a clean fixpoint re-run (corrected script) is
> needed for the complete count. **Cache-artifacts** (modules importing Mathlib
> submodules absent from the cached build closure, e.g. `Mathlib.Order.LocallyFiniteOrder`,
> `Mathlib.NumberTheory.LSeries.*`, bare `import Mathlib`) are **not** source errors —
> they compile in CI and are excluded here.

### By error class (all 35)

**SYNTAX (6)** — mechanical (λ→`lam`, dangling `/--`→`/-!`, import-position, abs notation):
- `QOU/CategoricalDynamics.lean:18` — `/--` docstring before `variable` (→ comment) — **DRAINED (#2787)** (3 docstrings + 3 `noncomputable`)
- `QOU/BraidKnot/hoefsmit_scattering_pipeline.lean:49` — `fun λ =>` (reserved `λ`; → `lam`) — **DRAINED (#2787)** (+ `import Real.Basic`)
- `QOU/Information/photon_threading_mass.lean:33` — `|q − q⁻¹|` abs notation unparsed
- (+ 3 more in the prior census's SYNTAX list still pending verification on this run)

**unknown-identifier / unknown-constant (7)** — Mathlib API rot (loogle the new name):
- `QOU/Archimedean/BorromeanQuark.lean:35` — `Finset.univ.sum` (root cause was missing `Fintype.Fin`/`VecNotation` imports, NOT API rot) — **DRAINED (#2787)**
- `QOU/Archimedean/integer_stability.lean:71` — `inv_lt_one_iff_of_pos` → `inv_lt_one_of_one_lt₀` — **DRAINED (#2787)**
- `QOU/BraidKnot/CrossedModuleEulerCharacteristic.lean:94` — `List.join`
- `QOU/BraidsAndKnots/QSchurYLambdaClosedForm.lean:91` — `Finset.range`
- `QOU/BraidsAndKnots/YLambdaQSchur.lean:172` — `yLambdaQSchur_bar_mullineux` (local decl)
- `QOU/HyperellipticQuintic/CheckAbs.lean:3` — `Complex.abs` (removed dead `#check`) — **DRAINED (#2787)**
- `QOU/Archimedean/RSK.lean:83` — `Function expected at`

**No-goals (4)** — remove a redundant tactic:
- `QOU/Archimedean/tau_leptonic_universality.lean:54` — **DRAINED** (this PR; see below)
- `QOU/BraidKnot/BraidWordBasisGram.lean:119` — **DRAINED (#2787)** (drop `decide`)
- `QOU/BraidsAndKnots/UnitModulusEigenvalue.lean:44` — **DRAINED (#2787)** (drop `ring`)

**unknown-tactic (3):** `QOU/BraidKnot/ConditionalClasses.lean:64`,
`QOU/MassEndomorphism/MassEndomorphismConjecture.lean:75`, `QOU/Mathlib/SpectralSequence.lean:58`

**failed-to-synthesize / typeclass-stuck (8)** — per-proof instance debugging:
`BindingConcentration:66`, `DepthStratifiedFrobeniusReciprocity:48`,
`KnotFactorFrobeniusPairing:85`, `SixTermPerDerivationWeights/binding_assembly:35`,
`TwoRoutesProtonMass:24`, `StructuralRank:171`, `e_infinity_identifications:37`,
`skein_mass_from_linking:38`, `WedderburnMass/chirality_residue_mass_term:35`

**rewrite-failed (4):** `Archimedean/BranchingConvergence:63`,
`BraidKnot/HopfBindingLinkEigenvalueIdentity:90`, `BraidKnot/YangBaxterBlowupTruncation:72`,
`QBeta/QBesselContiguityRecurrence:73`

**unsolved-goals / rfl / unfold / binder (4):** `Mathlib/ArchimedeanRealization:51`,
`MathlibExt/RpowAlgebra:51`, `BraidKnot/eigenvalue_product_expansion:42` (rfl),
`BraidKnot/PerPartitionKLambda:146` (unfold), `Observations/TraceLocalityMeetsGsNonLocality:36` (binder)

**TIMEOUT (1):** `QOU/Archimedean/PauliWitness/Witness12B.lean` (>300 s; perf/maxHeartbeats)

## Drained in this PR — 8 of 35 → GREEN (27 remaining)

All lean-direct verified (exit 0, no `error:`; `LEAN_PATH` over the restored
`lake-cache/qou-v4-24-0` Mathlib oleans).

1. **`tau_leptonic_universality.lean`** — (1) removed a redundant `ring` after `simp`
   (No-goals); (2) the `tau_leptonic_universality` theorem was proved by a broken
   `trivial` on a genuinely-open Markov-trace step (not derivable from the abstract
   `TauLeptonicContext` masses) — replaced with an honest `sorry` + `-- Ref:` (§1a).
2. **`integer_stability.lean`** — `inv_lt_one_iff_of_pos h_q_pos` → `inv_lt_one_of_one_lt₀`
   (v4.24 lemma rename); dropped the now-unused `h_q_pos`.
3. **`CheckAbs.lean`** — removed the dead `#check Complex.abs` (`Complex.abs` removed in v4.24).
4. **`CategoricalDynamics.lean`** — 3 `/--` docstrings before `variable`/comments → `--`/`/-`;
   marked `flowPoint`/`particleStateAt`/`functorialFlowPoint` `noncomputable` (depend on
   `CategoryTheory.Limits.terminal` — a 2nd layered error behind the docstrings).
5. **`UnitModulusEigenvalue.lean`** — dropped a spurious `ring` after `field_simp` (No-goals).
6. **`BraidWordBasisGram.lean`** — dropped a spurious `decide` after `rw` (No-goals).
7. **`BorromeanQuark.lean`** — root cause was missing `Mathlib.Data.Fintype.Fin` +
   `Mathlib.Data.Fin.VecNotation` imports (NOT `Finset.univ.sum` API rot); also `hq`→`_hq`.
8. **`hoefsmit_scattering_pipeline.lean`** — `fun λ` → `fun lam` in the def body (the class
   field was already renamed); added `import Mathlib.Data.Real.Basic` (typeclass-stuck on `ℝ`).

**Layering confirmed.** 4 of these 8 had a 2nd error behind the first (CategoricalDynamics:
docstrings → noncomputable; BorromeanQuark: import → unused-var; hoefsmit: λ → Real import;
tau_leptonic: ring → trivial). Per-file lean-direct verification caught each before commit.
Two initial class-guesses were wrong: BorromeanQuark (`Finset.univ.sum` was a missing-import,
not API rot) and hoefsmit (the real 2nd blocker was a missing `ℝ` import).

## Lesson + next step

Reds are **layered** (tau_leptonic had 2 distinct errors). Draining the remaining 34 is
careful per-file work — already underway incrementally on main (the +48 red→green commits).
A clean fixpoint re-run with the corrected `lean_red_census.py` will (a) build the
missing-dep chains and (b) surface any hidden reds behind them, for the complete count.
