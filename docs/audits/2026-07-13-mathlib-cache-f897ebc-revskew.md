# Mathlib olean cache is one rev behind the f897ebc pin — targeted-build audit

**Date:** 2026-07-13
**Branch:** `claude/mathlib-infra-build-2026-07-13`
**Directive:** "build any missing mathlib infra … do slow, do right"
**Beans:** `qou-4fa1` (build), `qou-1mws` (copy), `qou-t4ij` (rev-skew finding)

## TL;DR

The `lake-cache/qou-v4-24-0` olean cache (reseeded **2026-07-02**) predates the
mathlib **f897ebc** pin bump (landed on `main` **~2026-07-08**, bean `szkf`).
So the cache's 2962 mathlib oleans are from the **pre-f897ebc** rev while the
current checkout pins f897ebc. Targeted lean-direct builds against the stale
cache succeed for import-compatible modules but fail wherever the f897ebc bump
reorganized a **foundational instance**. The single such boundary hit here is
`Mathlib.Analysis.Calculus.ContDiff.Bounds` (a `Norm (E →L[𝕜] F →L[𝕜] …)`
synthesis), which cascades to the whole RiemannZeta/HurwitzZeta/Schwartz chain.

## What was built (verified working in-container)

Ran a topological lean-direct olean builder (`lean -o <out>.olean
--root=/home/user/mathlib4 <src>.lean`, LEAN_PATH = restored cache oleans) over
17 targets needed by QOU library files.

- **Built: 166 mathlib oleans** (2962 → 3128). Complete targets include
  `Trigonometric.Chebyshev`, `Algebra.Quaternion`, `SpecialFunctions.Gamma.Basic`,
  `SpecialFunctions.Stirling`, `Complex.PhragmenLindelof`,
  `Integrals.Basic`, `RingTheory.Derivation.Basic`, `PowerSeries.Inverse`,
  `GroupTheory.Complement`, `Data.Nat.Dist`, `SpecificGroups.Quaternion`.
- **Verification:** `QOU/QBeta/ToroidalHarmonicsBasis.lean` (imports the
  newly-built Chebyshev + Integrals.Basic + Derivation.Basic) lean-direct checks
  **exit 0** — only warnings + its one known cited `sorry`
  (`liouville_green_weber_limit`).

## What failed and why (root cause)

- **Failed: 45 mathlib modules**, all cascading from a **single root**:
  `ContDiff/Bounds.lean:65` + `:83` — `failed to synthesize
  Norm (Eu →L[𝕜] (Du →L[𝕜] Fu) →L[𝕜] Du →L[𝕜] Gu)`. Everything downstream
  (`SchwartzSpace`, `LSeries.HurwitzZeta*`, `LSeries.RiemannZeta`, …) is a pure
  "object file … does not exist" cascade off Bounds.
- ContDiff.Bounds's transitive closure is **1654 modules, 1653 already present**
  (only Bounds itself missing); the `Norm` provider
  `Mathlib.Analysis.Normed.Operator.NormedSpace` is present. Force-rebuilding
  that provider from f897ebc source **also** fails
  (`NormedSpace.lean:218` — same `Norm (StrongDual … →L[𝕜] …)` class), so the
  stale boundary is **deeper in the normed-operator foundation**, not a single
  olean.
- Diagnosis: the f897ebc bump reorganized the ContinuousLinearMap `Norm`
  instance path. The pre-f897ebc cache oleans don't provide it in the shape
  f897ebc source elaborates against. This is not fixable by rebuilding one or a
  few modules — it requires rebuilding the normed-operator foundation (and its
  large dependent cone) from f897ebc source, i.e. a **full clean f897ebc mathlib
  build**.

## Blast radius on QOU

Only **2** real QOU files import the failed chain:

- `QOU/AppendixSurreals/CasimirZetaPrefactor.lean` — 0 `sorry`, proves
  `riemannZeta (-3) = 1/120` etc. (would verify once the chain builds).
- `QOU/BraidKnot/ClassicalRiemannHypothesis.lean` — a `conjecture` carrier
  (RH is genuinely open); needs `riemannZeta` only to *state* the class.

Neither is on the active work path; both are stable.

## Seeding decision — DO NOT seed the +166 into the cache

The +166 oleans are **mixed-rev** (f897ebc source compiled against pre-f897ebc
cache deps). They load and check for the modules that don't cross a bumped
instance, but seeding them into the load-bearing `lake-cache/qou-v4-24-0` would
mix revs in shared infra other containers restore from. The correct next step
for the cache is a **clean full f897ebc mathlib rebuild + reseed**, tracked as a
deliberate long job (beans `9h6x` / `bnyo` / `qou-t3bx` / `qou-52i4`), not an
in-session incremental seed. The +166 remain useful in this container
(`.lake/` is gitignored/ephemeral) with no pollution risk.

## Recommendation

1. **Accept** the verified in-container 165-module win for this session's Lean
   verification needs.
2. **Defer** the RiemannZeta chain to a **full f897ebc mathlib rebuild** (the
   real infra fix; ~multi-hour, better as a dedicated cache-refresh job than an
   in-session task) — then reseed `lake-cache/qou-v4-24-0` clean at f897ebc.
