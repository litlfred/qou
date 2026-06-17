# Green-ify `lake build QOU` — remaining broken modules (warm-start workplan)

**Date:** 2026-06-17
**Context:** `lake build QOU` was red on `main` far beyond the two modules
repaired in #2443. This session cleared the **mechanically-fixable** ones
(PRs #2443 + #2450, 7 modules total); this doc captures the diagnosis of the
**remaining hard tail** so a focused session (with a live LSP for goal states)
starts warm.

## Already fixed (verified lean-direct EXIT 0)
- #2443 (merged): `PlancherelWeightBoundedness`, `KnotFactorSpectralDerivation`
- #2450: `EmCouplingBringZeroMode`, `GramSeminormalBlock`, `QIntegerMassFormula`,
  `PhiQJSJ`, `Braiding/HeckeGenPolyReduction`

## Environment recipe (proven this session)
- Restore the toolchain cache from the orphan branch
  `lake-cache/qou-v4-24-0` (≈2 min, 2946+ Mathlib oleans) — see
  `lean-environment-setup.md`. Do **not** run a bare `lake build` against a
  cache-less tree: it re-resolves deps and wipes the oleans, forcing a
  ~hour from-source rebuild (it *did* complete from source this session,
  3658 oleans, but that's slow + flaky).
- **Verify single files with lean-direct**, not `lake build <Module>`:
  ```bash
  LP=""; for d in .lake/packages/*/.lake/build/lib/lean .lake/build/lib/lean \
      content/quantum-observable-universe/lean/.lake/build/lib/lean; do
    [ -d "$d" ] && LP="$LP:$d"; done; LP="${LP#:}"
  LEAN_PATH="$LP" lean <file.lean>
  ```
- **`pkill -x lake` / `pkill -x lean`** (exact name) to stop builds — NOT
  `pkill -f "lake build"`, which matches the agent's own shell command line
  and self-kills it (exit 144).
- Grep lean output for `error` (not `error:`) — unknown-constant errors are
  formatted `error(lean.unknownIdentifier):`.

## Common mechanical bugs (the patterns that worked)
- `λ` used as an identifier (`∀ λ ∈ …`, `intro λ`, `fun λ =>`) — `λ` is the
  reserved lambda token; rename the partition binder `λ`→`p` (leave docstring
  math `w_λ`/`Σ_λ` intact).
- Missing imports for the symbols used: `Mathlib.Data.Real.Basic` (ℝ order +
  `|·|`), `Mathlib.Algebra.Order.BigOperators.Group.Finset`
  (`single_le_sum`/`sum_le_sum`/`abs_sum_le_sum_abs`),
  `Mathlib.Algebra.BigOperators.Ring.Finset` (`Finset.sum_mul`),
  `Mathlib.Tactic.Module` (`module`), `Mathlib.Tactic.Linarith` (`linarith`).
- Real-arithmetic `def`/`instance` (zpow `10^(-k:ℤ)`, `1/100`) ⇒ add
  `noncomputable`.
- Orphaned `/-- -/` doc-comment of a removed decl (parse error
  `unexpected token '/--'`) ⇒ demote to `/- -/`.
- Class index not inferable from a field's type ⇒ pin it: `Foo.field (q := q) …`.

## Remaining hard modules (real proof/API work)

### `Molecular/ShellClosureNfTermCount`
- `LaurentPolynomial.T_injective` and `LaurentPolynomial.T_ne_zero` **do not
  exist** in this Mathlib. Available primitives: `LaurentPolynomial.T_apply`
  `(T n) m = if n = m then 1 else 0`; `Finsupp.single_left_injective (h : b ≠ 0)`;
  `Finsupp.single_ne_zero : single a b ≠ 0 ↔ b ≠ 0`. (`T n = Finsupp.single n 1`.)
- `HA_ne_zero` (:88) and `helium_slot3_nonzero` (:222) are single-`T`-difference
  nonzero proofs — tractable by coefficient extraction
  (`DFunLike.congr_fun h k; simp [LaurentPolynomial.T_apply, Finsupp.sub_apply]`).
- `helium_slot2_nonzero` (:207): a `simp`-based coefficient extraction on the
  **unfolded product** `helium_nf 2` **TIMES OUT** (>200 s) — the expression is
  a big product of `T`s. Needs a normalize-first strategy: rewrite to the
  `4·T(2) − 4·T(0) + 4·T(−2)` form (via `LaurentPolynomial.T_add`/`T_mul`/`ring`
  on the *polynomial*, or `LaurentPolynomial.ext`) **then** extract the index-2
  coefficient — not a blind `simp`. Two `linarith [T_ne_zero …]` calls (:217,
  :230) also pass a `≠` fact to `linarith` (impossible) — replace with the
  coefficient-contradiction.

### `Archimedean/AxialCoupling`
- `std_trace_braid_dependent` (:182) extracts a `T²` coefficient via
  `LaurentPolynomial.coeff` + `coeff_add`/`coeff_mul`/`coeff_T` — **none of which
  exist** (LaurentPolynomial has no `coeff` API). Rewrite using `DFunLike`
  application + `LaurentPolynomial.T_apply`; the product coefficient
  (`markov_denom * stdRep…`) is an `AddMonoidAlgebra.mul_apply` convolution —
  evaluate it explicitly rather than via a (nonexistent) `coeff_mul` simp set.

### `FeynmanPathIntegrals`
- Application type mismatches at :300 — needs LSP `lean_goal`/`lean_hover_info`
  to see the expected-vs-actual types; likely an API-signature drift.

### `BraidKnot/NucleusEmptySDPUniqueness`
- Instance-synthesis failures + a "Not a definitional equality" + type mismatch
  at :105/:112/:129/:132/:152. Hardest; needs careful LSP-driven diagnosis of
  the SDP/PSD typeclass setup.

### `Archimedean/PauliWitness/Witness12B`
- Compile **timeout** (>150 s) — a performance problem, not a clear bug.
  Try `set_option maxHeartbeats`, profile with `lean_profile_proof`, or
  restructure the slow proof/`decide`.

## Recommended order for the next session
1. `ShellClosure` `HA_ne_zero` + `slot3` (tractable coeff extraction) → then the
   `slot2` normalize-then-extract.
2. `AxialCoupling` (same coeff-extraction technique, plus the convolution).
3. `FeynmanPathIntegrals` (LSP type diagnosis).
4. `NucleusEmptySDPUniqueness` (hard).
5. `Witness12B` (perf).

Re-run `lake build QOU` after each batch — fixing earlier modules unblocks the
build to reveal any further breakage past module ~3360.
