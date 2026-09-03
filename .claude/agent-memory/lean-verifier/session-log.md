# lean-verifier — session log

One line-block per session: what was verified, by what method, and any
`MEMORY.md` entry confirmed or corrected. Moved out of `MEMORY.md` 2026-09-03 so
the injected file stays under 200 lines. Newest first.

- 2026-09-03 (tender-keller, lane L1 GramQuotientDetD): authored + verified NEW
  `QOU/Interactions/GramQuotientDetD.lean` (convention-D successor to
  `gramMatrix_det_ne_zero`: `det(gramQuotientD q) = -(q⁴+1)(q²-q+1)⁴(q²+q+1)⁴/(q²+1)¹⁰`,
  `< 0`, `≠ 0`, no hypothesis on q). Parent olean `GramMatrixH3Symbolic.olean`
  was STALE (Jul 2, zero D decls) and `HeckeH3GramNondegeneracy.olean` ABSENT, so
  the 4-module QOU cone was rebuilt from current source into a `cp -al` mirror:
  MarkovTraceOnHecke 245 s, DetFin 330 s (cold-cache inflated), HeckeH3Gram-
  Nondegeneracy 69 s, parent — see MEMORY BASELINE. Tactic route validated on a
  scratch stand-in first (exit 0, 29 s user). sympy cross-check (entries parsed
  from the `.lean`, not transcribed) matched Lean RHS, witness `quotient_form.*`
  and `det_at_q0` to 3.7e-31.
- 2026-09-03 (tender-keller L4, `qou-6gf9`, sibling instance): authored+verified
  NEW `QOU/BraidKnot/MuPCorrectionAdmissibility.lean` (imports MuPCarrierBarParity
  + MuPCarrierOrderWindow → MmuR9V9Closure → QBetaCategoricalPrecisionLadder).
  lean-direct EXIT 0 first compile, 0 diagnostics; all 9 decls std-3 axioms, no
  sorryAx. Lessons (now in MEMORY TRAPs): the clone is SHALLOW, so `git log --
  <file>` cannot date a source against its olean ⇒ rebuilt its own 4-module QOU
  cone into a `cp -al` mirror (~4 min, only pre-existing linter warnings); the
  orchestrator's `LEAN_PATH.txt` carried RELATIVE entries (valid only with cwd =
  repo root); root `.lake/packages/mathlib/` is OLEANS ONLY — grep oleans with
  `grep -rl --binary-files=text -F <name>` for single-component names, then
  confirm with a `#check` scratch (dotted names like `Even.neg_one_pow` are stored
  as components, NOT greppable as one string). Cold-cache TRAP again (3m34 / 10 s).
- 2026-09-03 (braid-twist-flip): verified two changed content-block `.lean`
  files realizing trefoil monodromy S₃≅D₃, both lean-direct EXIT 0, no sorryAx.
  File 2 (`lean/QOU/BraidTwistFlip.lean`, `α×α×α`, all `rfl`, Mathlib.Tactic):
  6 decls "do not depend on any axioms". File 1 (`braids-and-knots/
  braid-twist-flip.lean`, `Fin 3`, imports `QOU.Basic`): built `QOU.Basic.olean`
  lean-direct first (5 s), then elaborated against it — std-3 axioms;
  `rotation_ne_id` (via `decide`) = `[propext, Quot.sound]`. Cold-cache TRAP
  confirmed (warm 1m45s wall / 11 s user). ELAN_TOOLCHAIN note added.
- 2026-09-02 (qtr-kron-consolidation): verified edited
  `QOU/MassTheory/QuantumTraceTower.lean` (new import
  `QOU.MathlibExt.MarkovTraceMultiplicative`, `qtr_kron` rerouted through
  `trace_kron (D₁ * X₁) (D₂ * X₂)`). `MarkovTraceMultiplicative.olean` was absent
  from the restore; built it lean-direct first, then the target fresh from
  current source (no false green). EXIT 0, zero diagnostics, std-3 axioms. A
  background process committed+pushed the edit as `398f760001` (not me);
  committed bytes == verified bytes. `/usr/bin/time` is NOT installed — use the
  bash `time` builtin.
- 2026-09-02 (magnus-o6ov): verified `QOU/MassTheory/MagnusHookExteriorPower.lean`
  — as written FAILED on the nonexistent `Finset.sum_powerset_card` + an
  `rw [esymm]` under a binder; fix recorded in `authoring-traps-v4-24-0.md`.
  EXIT 0 after fix, std-3 axioms. Cold-cache TRAP confirmed (2m6s / 6 s user).
- 2026-08-29 … 2026-08-31 (condensed): orphan-branch restore works (blocked host
  is Azure blob, unused); `omit [inst] in` precedes the docstring; imports must
  precede a `/-!` module doc; `WedderburnRankDegeneracy` red 6 days behind a
  FALSE GREEN → `verification-harness.md` (PR #6097); `Data.Matrix.Kronecker` →
  `LinearAlgebra.Matrix.Kronecker`; a partial 3407-olean mathlib cone sufficed
  for Mathlib-only files; `BrunnianIsotypeExclusion`, `EmCouplingBarParity`,
  `QuantumTraceTower` (new) all verified lean-direct EXIT 0, std-3 axioms.

- 2026-09-03 (magnus-o6ov gauge-hook): verified committed
  `QOU/MassTheory/MagnusGaugeCurvatureHookColumn.lean` (HEAD 11e80b8a39; def
  `curvatureSum` + 2 thms over generic CommRing/Algebra, `tr : A →ₗ[R] R`).
  All 4 imports (`BigOperators.Ring.Finset`, `Module.LinearMap.Defs`,
  `Algebra.Algebra.Defs`, `Tactic`) have BOTH olean and source in v4.24.0 — the
  LinearMap/Algebra module names are real. lean-direct EXIT 0, zero diagnostics,
  AS AUTHORED (no fix). Both thms `#print axioms` = `[propext, Classical.choice,
  Quot.sound]`, no sorryAx. Cold-cache TRAP again: 3m52s wall / 10s user, warm
  4.0s. Cache was already present in root `.lake` (3470 mathlib oleans) WITHOUT
  the `RESTORED-NO-TRACES` marker — absence of the marker ≠ absence of the
  restore; check the olean count. Disk was 2.1G free: too little for a
  re-restore tarball (~1.6–2.3G), so a "restore first" reflex would have failed.

## TRAP — v4.24.0 module moves + subscript ± are notation tokens

Two authoring mistakes that block a NEW file but are trivial, correct fixes
(no statement/witness change) — seen 2026-08-29 on
`QOU/MassTheory/MagnusPairingSignStructure.lean`:

- `import Mathlib.Data.Matrix.Notation` **does not exist** in mathlib
  v4.24.0. The `!![a,b;c,d]` matrix literal notation lives in
  `Mathlib.LinearAlgebra.Matrix.Notation`. (`Mathlib.Data.Matrix.Notation`
  has neither olean nor source in the tree; the olean error is a red
  herring for "cache is partial" — the module is gone, not uncached.)
- **`import Mathlib.Data.Matrix.Kronecker` ALSO does not exist in v4.24.0**
  (confirmed 2026-08-31). The Kronecker content — `⊗ₖ` notation (`open scoped
  Kronecker`), `Matrix.mul_kronecker_mul`, `Matrix.trace_kronecker`,
  `Matrix.one_kronecker_one` — lives in `Mathlib.LinearAlgebra.Matrix.Kronecker`.
  Decisive discriminator vs "uncached": the mathlib **source** tree is present
  under `.lake/packages/mathlib/Mathlib/...`, and `Data/Matrix/Kronecker.lean`
  is absent while `LinearAlgebra/Matrix/Kronecker.lean` exists and the
  `Data/Matrix/` dir is otherwise full. So: `object file … does not exist` for a
  `Data.Matrix.*` import in v4.24.0 → check the source tree; several `Data.Matrix`
  modules moved to `LinearAlgebra.Matrix`.
- Under a full `import Mathlib.Tactic`, `₊`/`₋` (U+208A/U+208B subscript
  plus/minus) are **notation tokens** (PosPart etc.), so a bound-variable
  name like `ρ₊` fails to lex: `unexpected token '₊'; expected ','`. Rename
  the binder (`ρ₊`→`ρp`) — pure alpha-renaming, the proposition is
  identical. Fine in comments/docstrings, not in identifiers.
- `import Mathlib.Algebra.BigOperators.Ring` **is not a module** in v4.24.0.
  It is a *directory* `Ring/` (`Finset.lean`, `List.lean`, `Multiset.lean`,
  `Nat.lean`) with no `Ring.lean` aggregator; zero mathlib files import the
  bare path. `Finset.mul_sum` lives in `Mathlib.Algebra.BigOperators.Ring.Finset`
  — the correct import. Symptom is identical to a cache miss (`object file
  …/BigOperators/Ring.olean … does not exist`), so distinguish source-bug
  from cache-gap by checking the mathlib *source* tree for a `.lean` and
  grepping whether any mathlib file imports the exact path. Seen 2026-08-31
  on `QOU/MassTheory/MagnusOmega2LocalDecomposition.lean`.

## TRAP — v4.24.0 renames seen on a 4×4 complex-matrix file (2026-09-03)

Four mechanical, statement-preserving fixes, all on
`QOU/QBeta/TensorCouplingCannotUnbindSinglet.lean`:

- **`Matrix.dotProduct` does not exist** — it is root-namespace `dotProduct`
  (`Mathlib/Data/Matrix/Mul.lean:66`). Symptom: `Unknown constant` printed 4×
  (once per `fin_cases` branch) and the simp set silently loses the unfold.
- **`Matrix.smul_mulVec_assoc` is a deprecated alias** (since 2025-08-14) of
  `Matrix.smul_mulVec`, identical statement `(b • M) *ᵥ v = b • M *ᵥ v`.
- **A `def` of a `Matrix _ _ ℂ` built with `*` must be `noncomputable`** —
  `Finset.sum` over ℂ hits `Complex.instNormedAddCommGroup` (no executable
  code). `!![…]` literals and `•`/`+` alone did not need it; `*` did.
- **`Complex.I ^ 2` is created by `ring_nf`, not by `simp`.** After `simp`
  the `I`s sit as `n₂ * I * (n₂ * I)`, so `Complex.I_mul_I` AND `Complex.I_sq`
  both report "unused" and `ring` fails with `I ^ 2` in the goal. Working
  chain: `simp [...] <;> ring_nf <;> simp [Complex.I_sq] <;> ring`.
  **Do not obey the `unnecessarySeqFocus` linter here** — rewriting the tail
  as `(simp [Complex.I_sq]; ring)` fails `No goals to be solved` because
  `simp` closes some branches outright. Keep `<;>`; the lint is cosmetic.
- `vecHead (vecTail …)` residue after `!![…]`/`![…]` simp: add
  `Matrix.vecHead, Matrix.vecTail` to the simp set.

## TRAP — this cache branch restores to ROOT `.lake`, and the per-paper tree is a stale decoy

`lake-cache/qou-v4-24-0` (25 parts) extracts to `$ROOT/.lake/` (root
workspace layout: `.lake/packages/*/.lake/build/lib/lean` + `.lake/build/lib/lean`).
Measured 2026-08-29: **3407 mathlib oleans** + 2275 QOU-library oleans,
`Mathlib.Tactic.olean` and `Matrix/Trace.olean` present. The pre-existing
`content/quantum-observable-universe/lean/.lake/packages/**` tree is a
**partial decoy** (~726 mathlib, QOU lib = 0) — do NOT point LEAN_PATH at
it. Build LEAN_PATH from the ROOT `.lake` package `build/lib/lean` dirs.
(The prior log's "6990 mathlib" was not what THIS restore produced; 3407 is
the QOU-cone partial and it is sufficient for QOU + Mathlib.Tactic files.)

---

prune the log, never the TRAPs. (Pruned 2026-09-03: entries 08-29 → 09-03
collapsed; every distinct lesson from them lives in a TRAP above.)

- 2026-09-03 (magnus-o6ov decay-bound): NEW `QOU/MassTheory/MagnusHookDecayBound.lean`
  (imports sibling `MagnusHookExteriorPower` for `esymm`; 3 thms over
  `[CommRing R] [LinearOrder R] [IsStrictOrderedRing R]`). EXIT 0 AS AUTHORED, no
  fix. v4.24.0 facts confirmed live: `Finset.abs_prod` takes exactly those three
  binders + explicit `(s) (f)`; `Finset.abs_sum_le_sum_abs (f) (s)` needs
  `[IsOrderedAddMonoid]` which IsStrictOrderedRing supplies; `abs_sub` (`|a-b| ≤
  |a|+|b|`) exists, no deprecation; `Mathlib.Algebra.Order.BigOperators.{Group,
  Ring}.Finset` are real modules with oleans in the partial restore. Dep olean was
  ABSENT → built lean-direct into `$ROOT/.lake/build/lib/lean/QOU/MassTheory/`
  (4m48s wall / 11s user, cold TRAP), then target 6s. All 3 thms std-3 axioms,
  no sorryAx. Only diagnostic: `unusedSectionVars` warning on thm 1 (`[DecidableEq
  ι]` inherited from the file's `variable` line; the sibling's `esymm` does not
  need it either) — a warning, not an error; left untouched per "statements
  unchanged". Disk 1.9G free, 3470 mathlib oleans, no marker — as last session.
- 2026-09-03 (two-nucleon-sign-defect): NEW `QOU/QBeta/TensorCouplingCannotUnbindSinglet.lean`
  (Mathlib-only). As authored exit 1 — 4 mechanical fixes, see the "4×4
  complex-matrix" TRAP; no statement touched, no sorry. Final: lean-direct EXIT 0,
  8/8 decls std-3 axioms, 0 sorryAx. Part (B) `Real.sqrt` lemmas compiled as
  authored. Cold 3m29s wall / 25s user; warm 8s. Cache already restored.
- 2026-09-03 (braid-twist-flip): two content-block `.lean` (S₃≅D₃ trefoil
  monodromy) EXIT 0, no sorryAx; one needed `QOU.Basic.olean` built lean-direct
  first. Found the `/tmp` → `ELAN_TOOLCHAIN` trap (top of file).
- 2026-09-02 (qtr-kron / magnus-o6ov): `QuantumTraceTower.lean` (first QOU import;
  rebuilt the dep olean from CURRENT source first to avoid a false green) and
  `MagnusHookExteriorPower.lean` (`Finset.sum_powerset_card` does not exist →
  `Finset.sum_powerset`; aggregator `Mathlib.olean` ABSENT from this partial
  restore, so a literal `import Mathlib` errors — verify via a temp copy with
  narrowed imports). Both EXIT 0, std-3 axioms. `/usr/bin/time` not installed;
  use the bash builtin.
- 2026-08-29 → 08-31: orphan-branch restore works (blocked host is Azure blob,
  never used); this seed = 3407 mathlib oleans, sufficient for QOU + Mathlib.Tactic;
  `BrunnianIsotypeExclusion` / `EmCouplingBarParity` / `QuantumTraceTower` verified
  std-3; `/-!` before `import` is rejected; `omit [inst] in` precedes the docstring;
  `WedderburnRankDegeneracy` red on main 6 days behind a false green → PR #6097 and
  `verification-harness.md`.
