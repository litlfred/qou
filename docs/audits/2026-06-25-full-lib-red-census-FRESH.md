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
- `QOU/Information/photon_threading_mass.lean:33` — `|q − q⁻¹|` abs notation unparsed (needed `import Real.Basic`) — **DRAINED (#2787)**
- (+ 3 more in the prior census's SYNTAX list still pending verification on this run)

**unknown-identifier / unknown-constant (7)** — Mathlib API rot (loogle the new name):
- `QOU/Archimedean/BorromeanQuark.lean:35` — `Finset.univ.sum` (root cause was missing `Fintype.Fin`/`VecNotation` imports, NOT API rot) — **DRAINED (#2787)**
- `QOU/Archimedean/integer_stability.lean:71` — `inv_lt_one_iff_of_pos` → `inv_lt_one_of_one_lt₀` — **DRAINED (#2787)**
- `QOU/BraidKnot/CrossedModuleEulerCharacteristic.lean:94` — `List.join` → `List.flatten` — **DRAINED (#2787)**
- `QOU/BraidsAndKnots/QSchurYLambdaClosedForm.lean:91` — `Finset.range`
- `QOU/BraidsAndKnots/YLambdaQSchur.lean:172` — `yLambdaQSchur_bar_mullineux` (local decl)
- `QOU/HyperellipticQuintic/CheckAbs.lean:3` — `Complex.abs` (removed dead `#check`) — **DRAINED (#2787)**
- `QOU/Archimedean/RSK.lean:83` — `Function expected at`

**No-goals (4)** — remove a redundant tactic:
- `QOU/Archimedean/tau_leptonic_universality.lean:54` — **DRAINED** (this PR; see below)
- `QOU/BraidKnot/BraidWordBasisGram.lean:119` — **DRAINED (#2787)** (drop `decide`)
- `QOU/BraidsAndKnots/UnitModulusEigenvalue.lean:44` — **DRAINED (#2787)** (drop `ring`)

**unknown-tactic (3):** `QOU/BraidKnot/ConditionalClasses.lean:64` — **DRAINED (#2787)** (missing tactic import; layered with lemma-rename + div_self),
`QOU/MassEndomorphism/MassEndomorphismConjecture.lean:75` — **DRAINED (#2787)** (missing `Tactic.Ring`),
`QOU/Mathlib/SpectralSequence.lean:58` (still red — multi-error, deferred)

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

## Drained in this PR — 13 of 35 → GREEN (22 remaining)

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
9. **`photon_threading_mass.lean`** — added `import Mathlib.Data.Real.Basic` to register the
   `|·|` abs notation (was a parse error `unexpected token '|'`, not elaboration).
10. **`MassEndomorphismConjecture.lean`** — added `import Mathlib.Tactic.Ring` (`ring` was an
    unknown tactic; the file imported only `Algebra.Ring.Basic`). Pre-existing dupNamespace
    warnings remain (class name = namespace), not errors.
11. **`CrossedModuleEulerCharacteristic.lean`** — `List.join` → `List.flatten` (v4.24); the two
    downstream `native_decide` trace checks `(-12, 0)` now evaluate cleanly (genuine finite
    computation the `List.join` error had poisoned — not a vacuity-dodge).
12. **`ConditionalClasses.lean`** — 3 layered errors: added `import Mathlib.Tactic`
    (`linarith`/`field_simp` unknown); `div_lt_one_of_lt` → `(div_lt_one _).mpr`; closed the
    residual `(q-1)/(q-1) = 1` via `div_self (sub_ne_zero.mpr (ne_of_gt hq))`.
13. **`demazure_fiber_markov_trace.lean`** — 4 reserved-`λ` binders → `lam`; then a pre-existing
    structural bug (hidden behind the parse error): class field `claim_ii_bruhat_order_structural
    : Prop` carried no witness, yet the def used the Prop as its own proof. Added the `_holds`
    witness field (§3b-cond; verified no downstream instance to cascade) and projected it.

**Layering confirmed.** 7 of these 13 had a 2nd (or 3rd) error behind the first
(CategoricalDynamics: docstrings → noncomputable; BorromeanQuark: import → unused-var; hoefsmit:
λ → Real import; tau_leptonic: ring → trivial; CrossedModule: List.join → poisoned native_decide;
ConditionalClasses: tactic-import → lemma-rename → unsolved div_self; demazure: λ → missing
Prop-witness). Per-file lean-direct verification caught each before commit. Two initial
class-guesses were wrong: BorromeanQuark (`Finset.univ.sum` was a missing-import, not API rot)
and hoefsmit (a missing `ℝ` import).

### Batch-3 triage refinement (stale-census reclassification, NOT new drains)

A standalone lean-direct sweep over the **old**-census SYNTAX-18 + 9 typeclass-stuck entries
(many of which the FRESH list inherited) reclassified them — the old census was stale and
double-counts files main already fixed:

- **7 already GREEN on main** (stale false-positives): `DeltaLambdaSignRule`,
  `H4SignBlockIsospinLimit`, `CosimplicialCrossedGroupoid`, `RSKBridge`, `MuWenzlClosure`,
  `SixTermPerDerivationWeights`, `WedderburnMassFormula`. No action needed.
- **8 BLOCKED-on-dep** (error at `1:0` = a missing dep olean such as `QOU.Shared.MarkovTraceClaim`
  / `QOU.Hecke` / `Mathlib.Algebra.Quaternion`, NOT a source error; the old import-position bug is
  already fixed since parsing reaches line 1 cleanly): `QuaternionFromHecke`,
  `skein_crossing_asymmetry`, `qmn_recursive_memoized`, `y_lambda_recipe_from_partition`,
  `toffoli_transfer_matrix`, `NucleonNFWitness`, `PentagonUvCommutation`, `confinement_categorical`.
  Unverifiable standalone in this sandbox; need their dep oleans built (a corrected fixpoint run).
- **Genuinely red but NOT mechanical** (deferred — real authoring): `BindingConcentration` &
  `interface_asymmetry_maximal` (malformed `theorem … : trivial := by trivial` vacuous
  placeholders — need a §1a honest disposition); `TwoRoutesProtonMass` (`Real.arccos` +
  proof-breakage); `DepthStratifiedFrobeniusReciprocity` (syntax + unsolved/no-goals);
  `KnotFactorFrobeniusPairing` (`Inhabited (ClosedBraid n)` instance); `TraceLocalityMeetsGsNonLocality`
  (`LinearOrderedField` is no longer a class in v4.24 — hierarchy migration);
  `StructuralRank` / `e_infinity_identifications` / `skein_mass_from_linking` (metavariable-stuck
  instances). NB: `BindingConcentration`/`TwoRoutes`/`DepthStratified` each needed a *correct*
  `import Real.Basic` too, but that alone leaves them red — reverted to avoid half-fixed files.

**Conclusion: the cheap mechanical seam is exhausted.** The genuinely-remaining reds need real
per-file authoring (honest §1a dispositions, v4.24 hierarchy migration, instance derivation) or a
corrected fixpoint census to unblock the 8 dep-blocked files.

## Corrected fixpoint census (2026-06-25, DEFINITIVE — supersedes the "35 lower bound")

Ran the corrected `lean_red_census.py` (proper bottom-up fixpoint: wipe QOU oleans, rebuild,
re-try blocked modules until no new green). On HEAD with this PR's drains applied:

| class | count | meaning |
|---|---|---|
| **GREEN** | 633 | compiles (all 17 of this PR's drains are here) |
| **RED** | **50** | genuine source error — the TRUE count (the "35" was the lower bound the caveat warned of) |
| cache-artifact | 90 | missing *Mathlib* submodule olean (compiles in CI; not a source error) |
| blocked-by-red | 31 | downstream of a RED/cache dep; indeterminate until the dep builds |

The fixpoint **unblocked** the 3 dep-blocked λ files from the batch-3 list (their
`MarkovTraceClaim`/`Hecke` deps now build), letting them be drained — entries 14–17.

### Drained 14–17 (post-census, GREEN via lean-direct) → 17 total, 46 RED remaining

14. **`TraceLocalityMeetsGsNonLocality.lean`** — `[LinearOrderedField R]` is no longer a class in
    v4.24; body uses R only for `*`/`∏`, so per §7c → `[CommMonoid R]` (drop unused order/field).
15. **`y_lambda_recipe_from_partition.lean`** — ∀λ→∀lam (×2) + `import Real.Basic` (ℝ `Div`).
16. **`qmn_recursive_memoized.lean`** — λ→lam (×4) + missing-witness field
    `claim_ii_miss_computes_via_holds` (§3b-cond, the demazure pattern) + `import Real.Basic`.
17. **`confinement_categorical.lean`** — fun λ→fun lam (×2) + `import Real.Basic` (ℝ `AddCommMonoid`).

### Still-RED docstring trio (census-unblocked but layered → deferred)

The census also unblocked 3 dangling-docstring files, but each carries a non-mechanical 2nd
error, so they are **deferred** not drained: `PentagonUvCommutation` (`/--` at 88 + `unknown
tactic` at 123), `WenzlBridgeConcrete` (`/-!` at 117 + `QOU.qFactorial`/`QOU.qInteger` unknown
identifiers), `NucleonNFWitness` (multiple dangling `/-!`/`/--` + dangling `end`).

### The 46 remaining RED — class profile

Dominated by genuine proof/authoring work, NOT mechanical: ~11 `typeclass-stuck (metavariables)`,
~9 `failed-to-synthesize`, ~6 `rewrite failed`, ~5 `unsolved/No goals`, ~4 `Function expected`,
plus malformed `: trivial` placeholders, `unknown identifier` API-rot, a stack-overflow
(`AllKnownIsotopesUniqueness`), and the 1 timeout (`Witness12B`). Re-run `lean_red_census.py`
for the live annotated breakdown.

## Lesson + next step

Reds are **layered** (tau_leptonic had 2 distinct errors; ConditionalClasses had 3). Draining
the remaining 23 is careful per-file work — the easy mechanical classes (SYNTAX, missing-import,
clear renames, redundant-tactic) are now largely drained; what remains skews toward genuine
proof-breakage (`ring`/`unsolved goals`, multi-`Function expected`, `rewrite failed`, 1 timeout).
A clean fixpoint re-run with the corrected `lean_red_census.py` will (a) build the
missing-dep chains and (b) surface any hidden reds behind them, for the complete count.
