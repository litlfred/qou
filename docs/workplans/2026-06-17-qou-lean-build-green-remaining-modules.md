# Green-ify `lake build QOU` — remaining broken modules (warm-start workplan)

**Date:** 2026-06-17
**Context:** `lake build QOU` was red on `main` far beyond the two modules
repaired in #2443. This session cleared the **mechanically-fixable** ones
(PRs #2443 + #2450, 7 modules total); this doc captures the diagnosis of the
**remaining hard tail** so a focused session (with a live LSP for goal states)
starts warm.

## Status (2026-06-20): all five hard-tail modules GREEN ✅

Every module in the "remaining hard tail" below has since been repaired and
verified `lean`-direct EXIT 0 (sorry-free):

| Module | Landed via | Verified |
|--------|-----------|----------|
| `Archimedean/AxialCoupling` | `eff26583` (on `main`) | lean-direct |
| `FeynmanPathIntegrals` | `4c29034c` (on `main`) | lean-direct |
| `BraidKnot/NucleusEmptySDPUniqueness` | `244508f0` (on `main`) | lean-direct |
| `Archimedean/PauliWitness/Witness12B` | `32af0018` (on `main`) | lean-direct (>400s → 21s) |
| `Molecular/ShellClosureNfTermCount` | already on `main` (normalize-then-extract proofs in place) | lean-direct EXIT 0, 2026-06-20 |

The first four were cleared by a build-green session whose commits merged to
`main` (a parallel session produced an equivalent set; the duplicate PR #2484
was closed as superseded). `ShellClosureNfTermCount` — the one module this doc
flagged as needing real proof work — was found **already repaired on `main`**:
`helium_slot2_nonzero` uses the recommended `helium_nf 2 = 4·(HA²+1)` normalize-
then-`mul_ne_zero` strategy, `helium_slot3_nonzero` reduces to `−(4·HA)`, and
`HA_ne_zero` factors as `T(−1)·(T 2 − 1)` — no nonexistent `coeff`/`T_ne_zero`
API and no `linarith`-on-`≠` remain. Confirmed EXIT 0 via lean-direct against
the restored `lake-cache/qou-v4-24-0` olean cache on 2026-06-20.

**Whole-library status is NOT confirmed green** — see the sandbox caveat at the
end of this doc. The five *named* hard modules are done; whether anything past
them in build order is red requires a CI build, which the sandbox cannot run.

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

## Completion record (2026-06-20)

All five hard-tail modules listed above are repaired and verified `lean`-direct
EXIT 0 (sorry-free). The recommended order this doc proposed for "the next
session" was overtaken by events: four modules landed on `main` via build-green
sessions, and `ShellClosureNfTermCount` was found already repaired. Nothing in
the named tail remains.

## Sandbox caveat — `lake build QOU` wipes the restored cache (do NOT use it here)

The closing advice above ("re-run `lake build QOU` after each batch") **cannot be
followed in the web/cloud sandbox**, and attempting it is destructive. Confirmed
2026-06-20: running `lake build QOU` against a tree that has the
`lake-cache/qou-v4-24-0` oleans restored triggers

```
info: mathlib: URL has changed; deleting '…/.lake/packages/mathlib' and cloning again
info: mathlib: cloning https://github.com/leanprover-community/mathlib4
```

i.e. lake **deletes the restored Mathlib oleans** (2951 → a handful) and starts a
from-source rebuild (~40 min, network-flaky). The "URL has changed" is lake
comparing the manifest's Mathlib remote against the cache's clone origin.

**Consequences for whole-library verification:**
- Determining whether any of the 778 QOU modules *past* the five named ones is
  red is **not tractable in-sandbox** — there is no cache-preserving full build.
- Use **CI** (`lean_ci.yml` does the authoritative `lake build`) for the
  whole-library green/red answer, or a dedicated from-source build session.
- For single-file checks, keep using **lean-direct** against the restored cache
  (`LEAN_PATH=… ~/.elan/toolchains/lean-v4.24.0/bin/lean <file>`), invoking the
  **toolchain binary directly** to bypass the elan proxy (the proxy hits the
  firewalled `release.lean-lang.org` and fails — see `lean-environment-setup.md`).
- To stop a runaway build use `pkill -x lake` / `pkill -x lean` (exact name).
  Do **not** `pkill -f <pattern>` with a string that appears in your own shell
  command line — it self-kills (exit 144).
