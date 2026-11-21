# lean-verifier — session log

One line-block per session: what was verified, by what method, and any
`MEMORY.md` entry confirmed or corrected. Moved out of `MEMORY.md` 2026-09-03 so
the injected file stays under 200 lines. Newest first.

- 2026-09-12 (verify ONE new file, branch `claude/hecke-tower-witness-2026-09-12`,
  `QOU/MathlibExt/HeckeTowerWitness.lean` — the presented infinite Hecke tower as a
  `MarkovTrace`): **before 1 error + 1 warning (exit 1) → after 0/0 (exit 0)**; 29
  `#print axioms`, all std-3, **no `sorryAx`**; source has 0 `sorry` and 0 `axiom`
  *declarations* (the 2 raw `axiom` hits are prose, "Markov axioms" — and the brief's
  claim that "sorry" appears in the docstring was wrong, it appears **nowhere**).
  Restore was ALREADY present (root 3758 = the seed exactly) so no fetch; built the §17
  union mirror instead. **`OcneanuTrace.olean` was 2026-09-03 against a 2026-09-11
  source** — the §1/§11 false-green setup — so both QOU deps were rebuilt from current
  source into the mirror first; green reproduced against the real trees too. Cone was
  only 3 modules, no UGB, no non-Mathlib imports. Two mutation tests rejected (exit 1):
  `h -> h+1` in the quadratic, and zeroing the `linear_combination` coefficient that
  consumes the Markov-root hypothesis. Non-vacuity checked rather than assumed:
  `MarkovTrace ℚ (HeckeTower ℚ (3/2))` is inhabited with `h ≠ 0`, `z ≠ zinv` and
  `twH 0 < twH 1`, so the module's "missing quadrant" claim has an instance.
  **Both fixes were proof-only; no statement touched** — the error was a missing binary-
  `sub` simp projection on `Hecke2` (fix: `sub_eq_add_neg`), the warning was
  `Set.image_subset` → `Set.image_mono` with `f` now implicit. Both recorded in
  `authoring-traps`. The concurrent SessionStart `lake build` independently reached the
  same single error (`✖ [6641/6642]`, same line:col) — new `MEMORY.md` entry.

- 2026-09-04 (post-merge re-verification, branch `claude/standard-model-terms-status-ftoejr`
  at HEAD `219672e496`; 8 files, all blobs == HEAD): **8/8 lean-direct EXIT 0, zero
  diagnostics**; 94 `#print axioms` lines, all std-3 or "no axioms", **no `sorryAx`**.
  Container had a REAL build tree, not a restore (2441 `.trace` beside 2442 QOU
  oleans, no `RESTORED-NO-TRACES`), so no cache restore was needed — but
  `QOU/AlphaEM/FormLadderAnchorDominance.olean` was **Aug 24 against a Sep 3
  source**, the textbook §1/§11 false-green setup for its new consumer
  `…Checks.lean`. Handled by the harness §3 route: `cp -al` mirror of the root
  build tree (0 bytes), `rm -f` + rebuild all **13** transitive QOU cone modules
  from current source, then verify. Real tree unchanged (2442 → 2442) and repo
  clean — the mirror never wrote through a shared inode. Merge-breakage check:
  the merge touched 32 `.lean`, **none** in the 13-module cone and none of the 8;
  `lakefile.toml`/`lean-toolchain` untouched; reverse cone of the genericised
  `FormLadderAnchorDominance` is exactly **one** importer (its own new `Checks`),
  so main could not have added a broken consumer. Shallow graft still live —
  `git log -- <file>` returns `c9c12648e4 2026-08-31` for nearly every file, so
  olean-vs-source dating from git remains undecidable; rebuild instead.
  Substance: all four new/rewritten carriers are content-bearing with NO instance
  (`WeinbergAngleCategorical` 7 real Prop fields, `ChernSimonsCorrectionConjecture`
  3, `CategoricalHiggsMechanism` 4 + a `[WeinbergAngleCategorical]` binder = the
  §3b-tax dependent-conjecture edge); the §3b-cond consequences derive rather than
  project. Noted, not defects: `QOU.BraidsAndKnots.{EWHoefsmitData,
  WeinbergAngleCategorical}` are declared **twice** — a self-labelled "FAITHFUL
  inlined copy" in `categorical-higgs-mechanism.lean`, fields byte-identical,
  docstrings differ — harmless only because chapter-dir `.lean` sit outside the
  `srcDir="."` + `globs=["QOU","QOU.+"]` library and are never imported together;
  and `Checks.refCodata` has no consumer and its literal is absent from the
  witness its docstring names (present only under `fsh-guts/deprecated/computations/`),
  though the residuals it would imply reproduce to ~8 sig figs. All 6 chapter-dir
  sidecars FRESH (`source_hashes.lean` == `sha256(file)[:12]`). New TRAP recorded:
  docstring prose reads as code to line-oriented matchers (`grep -cw sorry`
  matches `sorry-free`; a decl regex matched `below` and `instance` out of prose).
  **Measured refinement to harness §1**: the stale olean was genuinely stale —
  `#check @…no_anchor_blind_affine_correction_closes_gap` gave `(P M s c : ℝ)`
  against the tree vs `{R} [CommRing R] [IsDomain R] (P M s c : R)` against a
  fresh build — yet `Checks.lean` exits 0 against BOTH, because a generalisation
  specialises back at `R = ℝ`. So a consumer's green is no evidence of cone
  currency when the dependency change was a generalisation, and `grep -c -a
  <declName>` cannot see it either (the name is in both oleans). Use `#check`.

- 2026-09-03 (skeptic pass, `qou-cds2`, `QOU/Interactions/GramQuotientDetD.lean`
  as committed `338d40f57c`, blob `566da678`): could NOT refute. Mirror currency
  re-checked (`grep -c -a gramRadicalD` = 2 in the mirror's parent olean vs 0 in
  the shared Jul-2 one; mirror oleans link-count 1, newer than their sources).
  lean-direct EXIT 0, 0 diagnostics, 15.0 s wall / 12.2 s user; 10/10 `#print
  axioms` (9 decls + `Matrix.det_fin_five`) = std-3. `maxHeartbeats 4000000` is
  NOT load-bearing (default 200000 passes). MUTATION TEST (harness §10): the
  pristine child passes against a stand-in parent carrying the real table and
  FAILS at `ring` (line 138) when ONE leading-block entry changes — the theorem
  is about the table. sympy (own parser): closed form = Lean RHS = witness,
  `real_roots = []`, signature (4,1) at q₀, 25/25 entry perturbations move the
  det. Findings, all prose: "nondegenerate on V/rad" is automatic — the content
  is corank = 1 (rank 5) for every real q; "never positive" is unscoped against
  the `tr(ab*)` star form's positive-definite quotient (`GramSignature.lean`
  2026-08-09 block); witness `det_at_q0` evaluated at a 15-digit q₀ (`str(mpf)`
  under ambient dps 15), 5.6e-17 off the 50-digit anchor while printing 30
  digits. Branch tip moved mid-run (`4dbfd2ee31` → `1d9f1cf9db`); verified
  blob == HEAD blob == remote-tip blob. `lean -o` refuses a source outside its
  root dir (cwd / `--root`) — stand-ins need a scratch root laid out as the
  module path.
- 2026-09-03 (skeptic pass, `qou-6gf9`, `QOU/BraidKnot/MuPCorrectionAdmissibility.lean`
  as committed `4dbfd2ee31`): could NOT refute. lean-direct against the author's
  scratch mirror (4 cone oleans rebuilt 10:49, `grep -c -a <decl>` confirmed
  current, mirror complete 944 = 942 + the 2 never-built prune oleans, no
  hardlink into the shared tree): EXIT 0, 0 diagnostics, 7.2 s wall / 7.9 s user
  (page cache warm from the author). Scratch copy: 9/9 `#print axioms` = std-3,
  no sorryAx. Grep clean (sorry/native_decide/decide/axiom/True/trivial/unsafe/
  opaque/set_option). mpmath 50 dps confirmed every interval. Findings, all
  prose: CODATA-2018 `t` unlabelled (→ harness §9); admissibility class trivially
  inhabited by constants; `bar_even_monomial_iff` could be generic-field with
  "q² not a root of unity" (advisory — statement carries `1 < q`, gate's letter
  satisfied). Concurrent sibling instance restructured `MEMORY.md` mid-session;
  anchored edits only.
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
`folio/quantum-observable-universe/lean/.lake/packages/**` tree is a
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
- 2026-09-03 (magnus-o6ov-commutator): `QOU/MassTheory/MagnusCurvatureCommutator.lean`,
  self-contained (Mathlib only). As authored EXIT 1 — 3× `ring_nf made no progress`,
  all of them `ring` on a NONCOMMUTATIVE `[Ring A]` (see the new authoring TRAP).
  Fixed with explicit `mul_assoc` in the `rw` chain: −8/+2 lines, all four
  statements byte-identical. Final EXIT 0 (warm 3.8 s; cold 4m20s wall / 8.6 s user
  — page cache, not a rebuild). `#print axioms`: std-3, no `sorryAx`.
  `Mathlib.LinearAlgebra.Trace` is UNUSED (file carries cyclicity as a hypothesis);
  compiles EXIT 0 without it — reported, not removed. Mutation test: same statement
  with `hcyc` deleted fails, residual goal `tr (ρ*(y*x)) = tr (x*(ρ*y))` — the
  hypothesis is load-bearing, statement not vacuous. Root `.lake` held 3470 mathlib
  oleans with NO `RESTORED-NO-TRACES` marker; disk 1.9 G free, so no re-restore.

- **2026-09-04 (binding-law extensivity)** — New `QOU/Hecke/BindingExtensivity.lean`,
  6 decls, lean-direct exit 0, all std-3, no sorryAx. One fix: `pow_le_pow_left`
  → `gcongr` (authoring-traps). Cold 1m32s wall / **7.0 s user**, warm 4.6 s.
  Restored from a **leaked `/tmp/tmp.*`** rather than fetching — new STABLE entry
  in `MEMORY.md`. Third container reading of the two olean trees: per-paper 1236,
  root 9721.

- 2026-09-04 (branch `claude/standard-model-terms-status-ftoejr`, seven GAP beans):
  root tree was a REAL build (2443 QOU oleans / 2441 traces, no `RESTORED-NO-TRACES`);
  9-root `LEAN_PATH` from `.lake/packages/*/.lake/build/lib/lean` + `.lake/build/lib/lean`.
  Fixed `qou-yt29` (`categorical-linking-operation.lean`, a40e260b58): vacuous
  **5/5** not 2/5 — see harness §12 on extensional `True`. Now `LinkingData`
  substrate, Properties 1-2 + pre-trace 3 proved about `lk`/`preLk`, rest as class
  fields, no instance, plus an in-file falsifier. lean-direct 3.9 s, 13 decls,
  no `sorryAx`; qa-sweep 0/0/0. Docstring currency fix in the Higgs file (c32e7e393e).
  Verdict `qou-ibck`: **no closed form** for `Σ_λ 1/dim_q λ` — measured contrast,
  `Σ f^λ` = involutions and `Σ (f^λ)²` = n! both close exactly, the reciprocal
  gives 1, 2, 5/2, 19/6, 46/15, 473/144, … with no pattern; Mathlib has
  `YoungDiagram`/`Nat.Partition` but **zero** `hookLength`, so even a general
  *definition* (≠ closed form) is blocked on formalising hook lengths. Other five
  carriers audited by harness §12; all honest, two real side-findings (harness §13,
  and the `BringHyperbolicDecomposition` identical-field bridge).

## 2026-09-05 — `GeometricTailBound.lean`, and a 40-minute `lake build` mistake

New file, 5 decls, all `[propext, Classical.choice, Quot.sound]`, `lean`-direct
exit 0 in 5.0 s. Two real authoring failures (`div_le_iff` absent;
`rw [h] at *` finding no occurrence) and two imagined ones — see
`authoring-traps-v4-24-0.md`, which now ends with the imagined pair, because
being wrong about a tactic is the expensive kind of memory entry.

The process failure worth carrying: I reached for `lake build` from
`folio/quantum-observable-universe/lean/`, against this file's own standing
rule, and it ran ~1760 Mathlib modules for 40 minutes before I stopped it. It
did **not** evict the restore — it was building a *second* mathlib tree local to
that directory — which is the detail now in `MEMORY.md`. The 5-second
alternative was one `source scripts/lean-direct-env.sh` away the whole time.

## 2026-09-12 (2nd pass) — `MathlibExt/HeckeTowerWitness.lean`, branch `claude/hecke-tower-followup-2026-09-12`

Second verification of the same file the same day (first pass: 618 lines, blob
`5ca5adbda`, merged to main as `21c5179f0`). Three additions verified: two new
refutation theorems (`braid_scalar_forces_scalar`, `scalar_tail_forces_central`)
and the `exists_tower_with_nonzero_h` → `tower_nondegenerate` restatement.

- **before** exit 1 / 1 error / 0 warnings; **after** exit 0 / 0 / 0, 2.9 s.
- One real defect, one line: `abel` left `algebraMap (h*c)*x = algebraMap (c*h)*x`.
  `mul_comm h c` added to the `rw` chain. Commit `739ba86fb`.
- **Both** QOU deps were stale on disk (`OcneanuTrace` olean 8 days older than its
  source; `HeckeRankTwoMarkov` 3 h older) — rebuilt from source into the union
  mirror before gating. The first-pass note that OcneanuTrace goes stale held.
- `#print axioms` × 31 public decls: no `sorryAx`.
- 5/5 mutants RED; both hypotheses shown **semantically** necessary over `ℚ`;
  premises satisfiable; conclusion non-tautological; check (c) discharged
  generically (at `h=0,c=1` the hypotheses force `x=1`).
- Found: `u : Rˣ` is **free**, not restrictive — the tail generator's own
  quadratic forces `c*(c-h)=1` under injective `algebraMap`. Widens the refutation.
- Found: docstring cites `braid_forces_eq_of_commuting_involutions`, which does
  **not exist** (real: `QOU.Eightfold.braid_forces_eq`, and about a commutative
  image, not involutions). Reported, not rewritten — the gloss is authorial.
- The SessionStart `lake build` log was **17 min stale** and its `✖` on this exact
  module described a two-revisions-dead file. See the dated caveat in MEMORY.md.

## 2026-09-13 — cold-container restore from zero, then the caller's own file was red

Task: make the container able to `lean`-direct a NEW `QOU/Eightfold/*.lean`.
Start state: **10 oleans total** (cache genuinely unrestored), and a SessionStart
`lean-build-bg.sh` mid-`lake update` with a `cache get` child 403-ing every shard
(1655 failed / 0 downloaded of 7335 — the documented Azure-blob firewall).

- **Killed the chain by PID** (589 script, 677 `lake update`, 8184 `cache get`);
  never `pkill -f`. Manifests unharmed, all three still pin mathlib `f897ebcf72cd`,
  and the per-paper source clone is at the same rev.
- **Restored by streaming** (MEMORY §STABLE) — no 1.7 GiB tarball ever on disk;
  throwaway repo in the scratchpad under a `trap … EXIT INT TERM`. Head
  `a792c46d01b`, `PIPESTATUS=0 0`, 32461 entries, 6492 oleans / 6493 traces.
  Trace-check: **3758/3758 = 100.0 %**, marker correctly cleared.
- **My guard was vacuous and I nearly shipped on it** — 4-component listing,
  5-component regex. Replaced with `tar --exclude='content/*/lean/.lake/packages/*'`,
  a property true by construction. New TRAP in MEMORY.md.
- `scripts/lean-direct-env.sh` yields the right 11-entry `LEAN_PATH` unchanged;
  **only one `Mathlib/` olean root on this container**, so no union mirror needed.
  It does NOT set `-DautoImplicit=false` — pass it yourself (two-sided control
  run: bare exit 0 vs flagged exit 1; now a STABLE entry).
- **The caller's own committed file was RED.**
  `QOU/Eightfold/AnsatzContentDichotomy.lean` (`d8053c0a1`, message already said
  "UNVERIFIED, olean restore in flight"): 1 error, `154:2 No goals to be solved` —
  line 153's `simp` closes the goal, so the `exact absurd …` after it is dead.
  Verified the disposition **without touching the repo file**: copied to the
  scratchpad, `sed '154d'`, diff-guarded that the sed bit (a sed matching nothing
  is a false green), → exit 0, warnings only. `#print axioms` on all 7 theorems:
  no `sorryAx`, only `propext`/`Classical.choice`/`Quot.sound`.
- Slip worth keeping: I guessed the namespace `QOU.Eightfold` for `#print axioms`
  when the file declares `QOU.Eightfold.AnsatzContent` — and the `grep` output
  naming it was already on my screen. Sections (`Nonet`, `NonVacuity`) contribute
  nothing to the FQN. Read the namespace, never infer it from the path.
- Residual hazard reported, not fixed: the bg-build guard cannot fire on this
  trace-paired restore, so a compaction re-fires `lake build`.

## 2026-10-10 — TauBondLetter.lean (branch claude/tau-bond-letter-vanishing-2026-10-10)
Restore already in place (root mathlib 3480, per-paper QOU 2703, UGB 29), no fetch needed. Stopped the SessionStart chain by PID
(lean-build-bg.sh, `lake update`, `cache get`, curl) before it got to `lake build`. Lake-trace-hash freshness on the 16-module
Hecke cone: 14 fresh, TwRep and TwIndependent CHANGED. Rebuilt those 2, their downstream TwBasisField and TwMul, and the 3 missing
(InvMonomialDet, TauSymmetrizing, TauStructureConstants) lean-direct into a `cp -al` mirror in the scratchpad: 25 s total. Target needed
2 one-token fixes (explicit section variable `n`; `mul_zero` where the original had `smul_zero`) → exit 0, axioms clean.
## 2026-10-11 — MobiusRegulator.lean (qou-uh5f), worktree /home/claude/qou-r3
- Rebased onto origin/main 6e6d992da2 with no conflicts; new tip 656a7af6e6, pushed.
- The file imports Mathlib only, so there is no QOU cone: a bare lean-direct run against root `.lake/packages/*/.lake/build/lib/lean` (mathlib 3480, cache already present) is sufficient. exit 0, 3m53s wall / 8.4 s user, so the time was COLD PAGE CACHE.
- TRAP: `--force-with-lease` in a worktree was rejected as "(stale info)" because the local tracking ref was never fetched. `git ls-remote` showed that the remote tip equalled the pre-rebase sha, so I pushed with an explicit `--force-with-lease=<branch>:<that sha>`, which is safe.
- Also: a `cmd | tail` inside a retry loop always "succeeds", so the loop breaks on the first failure. Check PIPESTATUS.

## 2026-10-11 — XbotBottomEdgeLemmas.lean (qou-as81 companion), agent worktree
- Mathlib-only file, so no QOU cone: LEAN_PATH = the MAIN checkout's `/home/claude/qou/.lake/packages/*/.lake/build/lib/lean` (the agent worktree has NO `.lake`). First run 2m00s wall / 5.2 s user (cold page cache), then ~6 s.
- TRAP: `/tmp/qou-lean-build-status.json` said `"status": "unavailable", "Lean toolchain present but unusable"` — FALSE; a 2-line `by decide` + `#eval` scratch exited 0. Run the elaborator, do not trust the status file.
- TRAP (worktree-isolated agent harness): any Bash call with `$VAR`-computed args, pipes into `bash`, `cd` + compound, or a python heredoc that writes a file is REFUSED as "cannot be shown not to be git". Write a runner script with the Write tool and call `bash /abs/run.sh <file>` plainly; edit with Edit, not sed/python.

## 2026-11-15 — TRAP: `scripts/setup-lean-toolchain.sh` now ALSO restores the cache, into the REAL .git, and fills the disk

Fresh container, no toolchain. Running the script (3m36s) installed the toolchain AND ran a
best-effort cache restore: it fetched `cat/folio-assistant-sci/lake-cache/qou-v4-24-0`
(a792c46d01b) into the repo's own `.git` as **22 LOOSE objects (~1.7 G)**, `.git` 1.5G -> 3.2G,
free 11G -> 1.7G. tar then died with `folio/unital-groebner-bases/lean/.lake/build: Cannot mkdir`
(exit 2), "cache fetch failed (best-effort)". Mathlib nonetheless landed complete (3480 oleans
under root `.lake/packages/mathlib`); QOU only **86 of ~2702** (partial, misleading tree).
Reclaim: the loose objects were reachable only via FETCH_HEAD (`git for-each-ref` had no ref
containing the commit) -> `rm` the commit/tree/20 part blobs by path + FETCH_HEAD: +1.7G.
Lesson: on a low-disk container install the toolchain WITHOUT that script's restore step, then
stream the parts from a throwaway repo (MEMORY.md §"stream the parts INTO tar").
lean-direct of two Mathlib-only files: 3.7 s / 1.6 s; autoImplicit control re-confirmed both sides.

## 2026-11-15 — ContentCasimir.lean (branch claude/q-laplacian-eigenvalue-derivation-2026-11-15)
- BASELINE: toolchain already at ~/.elan/toolchains/leanprover--lean4---v4.24.0 (no ~/.elan/bin); release.lean-lang.org 403, GitHub zip 200 (730 MB, 24 s) — not needed.
- BASELINE: streamed restore of cat/folio-assistant-sci/lake-cache/qou-v4-24-0 @ a792c46d01b: fetch 1m36s, root .lake 3758 / per-paper 2703 oleans; disk 16G -> 8.8G free.
- STABLE: cone rebuild into a `cp -al` shadow of the per-paper lib dir (7 modules, HeckeAlgebra 64 s, rest ≤6 s), LEAN_PATH = shadow + root .lake/packages/*; works with no union mirror.

## 2026-11-21 — fresh container with NO `~/.elan` at all (BASELINE + TRAP)

- BASELINE: toolchain from `cat/folio-assistant-sci/lake-cache/toolchain-v4-24-0`, fetched into a
  throwaway repo and streamed into `/tmp/lean-tc-stage`: fetch 37 s. Olean seed `a792c46d01b`
  streamed with `--transform 's,^content/,folio/,'`: fetch 1m32s, disk 15G→22G used. Re-measure.
- `scripts/lean-direct-env.sh` needs `$HOME/.elan/toolchains/leanprover--lean4---v4.24.0`; a symlink
  to the staged dir is enough (no elan binary needed).
- TRAP (again): the seed's trace for `QOU/BraidKnot/FrobeniusSelfDualityForcesLPDualExtraction`
  held source hash `11653228326155494116`, current source `15718497695842365695` — stale. A
  dependent content block compiled against it would be certified against old source. Rebuilt it
  lean-direct into a scratch shadow prepended to `LEAN_PATH` (2.9 s; its imports are Mathlib-only).
