# Initial Diagnostic Report: Lean Compilation, Vacuity Audit, and Discharge Queue Status

**Date:** 2026-06-20
**Explorer Working Directory:** `/Users/litlfred/space_cats/qou/.agents/teamwork_preview_explorer_phase1_diag`
**Project Workspace:** `/Users/litlfred/space_cats/qou`

---

## 1. Lean Compilation Status

The workspace targets are structured under a root Lake-workspace. Direct execution of the build commands in this sandbox encountered permission timeouts; however, current status has been extracted from verified build logs and audit reports.

### Build Target Status Summary
- **fred2005-formal-groups (`Fred2005`)**: ✅ Passed (6s elapsed)
- **unital-groebner-bases (`UGB`)**: ✅ Passed (7s elapsed)
- **quantum-observable-universe (`QOU`)**: ❌ Failed (6052s elapsed during full cache-less build)

### Key Files with Compilation Errors in `QOU`
A total of **70+ modules** failed to compile. The primary files and error signatures include:

1. **Foundational & Linear Algebra Extensions**:
   - `QOU/MathlibExt/PosSemidefTraceZero.lean`:
     - Line 82: `Invalid field sqrt: The environment does not contain And.sqrt`
     - Line 70: `unsolved goals`
   - `QOU/MathlibExt/RpowAlgebra.lean`:
     - Line 51: `unsolved goals`

2. **Hecke Algebra Representations & Formalisms**:
   - `QOU/HeckeAlgebra/Formal.lean`:
     - Lines 83 & 87: Depends on `LaurentPolynomial.T` (no executable code); needs marking as `noncomputable`.
     - Lines 108 & 122: `Unknown constant LaurentPolynomial.mapRingHom` / `mapRingHom_T`.
     - Line 218: `unexpected token 'end'; expected 'lemma'` (syntax error).
   - `QOU/HeckeAlgebra/QSubstrate.lean`:
     - Lines 64, 72, & 97: Depends on `Real.instDivInvMonoid`; needs marking as `noncomputable`.
   - `QOU/HeckeAlgebra/Wedderburn.lean`:
     - Lines 60, 67, 73, 79, & 87: `unexpected token 'λ'; expected '_' or identifier`. (Lean 4 toolchain regression where `λ` cannot be used as an identifier prefix like `λ_Z`).

3. **Archimedean & Interaction Structures**:
   - `QOU/Archimedean/EmCouplingProjection.lean`:
     - Line 32: `unexpected token 'section'; expected 'lemma'`
     - Lines 34 & 35: Depends on `LaurentPolynomial.T`; needs `noncomputable`.
     - Line 95: `Unknown identifier em_coupling_classical_limit_axiom`
   - `QOU/Interactions/AlgebraicPrimality.lean`:
     - Line 47: `invalid declaration, it uses unsafe declaration Real.instRepr`
     - Line 223: `type of theorem magicEqualsEmpirical_of_perNAxioms is not a proposition`
   - `QOU/Interactions/BringShellBinding.lean`:
     - Lines 93, 154, & 215: `Tactic rcases failed: 2 is not a free variable`
   - `QOU/Interactions/HeckeEngine.lean`:
     - Line 112: `(deterministic) timeout at whnf, maximum number of heartbeats (200000) has been reached`

4. **Pauli Witness Core (Acoustic Spectrum & Nuclear Combinatorics)**:
   - `Witness12B.lean`, `Witness11C.lean`, `Witness12C.lean`, `Witness11B.lean`, `Witness10Be.lean`, `Witness9Be.lean`, `Witness10B.lean`, `Witness9B.lean`, `Witness8Li.lean`:
     - All exit with `maximum recursion depth has been reached` on large formula elaboration.

5. **Braid and Knot Invariants**:
   - `QOU/BraidKnot/ShellNeutrality.lean`:
     - Line 60: `Unknown identifier Multiset`
     - Multiple lines (65, 68, 75, 80, 91, 109, 143, 154, 160, 164, 177, 244, 259, 273, 284, 292, 308, 326, 336, 345): `unexpected token 'λ'`
   - `QOU/BraidKnot/Cl3Zeta5PslqIndependence.lean` & `KnotIndexedConvolutionGrid.lean`:
     - Unknown identifier `ℕ` (character encoding issue).
   - `QOU/BraidKnot/ChiralityWritheRibbon.lean`:
     - Stuck typeclass instance problem (metavariables).
   - `QOU/BraidKnot/MassFormulaCategorical.lean`:
     - Missing `noncomputable` markings.
   - `QOU/BraidKnot/CommutativeCrossingEnergy.lean`:
     - Line 40: `invalid 'import' command, it must be used in the beginning of the file`
   - `QOU/BraidKnot/HoefsmitV21CosSymmetrization.lean`:
     - Unsolved goals and `unfold` failures.
   - `QOU/BraidKnot/TwoRowStratum.lean`:
     - `Expected type must not contain free variables` / stuck rewrites.

6. **Missing Mathlib Imports (Cascading Failure)**:
   - `MarkovAxiomsPrimitive.lean`: Bad import `Mathlib.Algebra.Order.Ring.Lemmas` (file does not exist in cached mathlib package).
   - `KnotFactorSpectralDerivation.lean` & `PlancherelWeightBoundedness.lean`: Bad import `Mathlib.Algebra.BigOperators.Basic`.
   - `StandardPart.lean` & `Blowup.lean`: Bad import `Mathlib.RingTheory.Subring.Basic`.
   - `DeltaMaxUniformBound.lean`: Bad import `Mathlib.Algebra.Order.AbsoluteValue`.
   - `LiftingDescent/CosimplicialCrossedGroupoid.lean`: Bad import `Mathlib.CategoryTheory.Monoidal.Basic`.
   - These bad imports cascade up and prevent compilation of the root `QOU.lean`.

### Status of Fixes (Audit of 2026-06-10)
An audit and patch tranche on 2026-06-10 successfully resolved the syntax errors and SDP cascading errors in **10 in-closure files**:
- Fixed SDP variable binding and class instantiation in `SDPRealUniqueness` and `SDPEmptyConstraints`.
- Replaced `λ`-prefixed identifiers (`λ_Z/N/A` -> `ydZ/N/A` or `lam_*`) in `GaugeFieldFluidDynamics`, `LRFusion`, `Hoefsmit`, etc.
- These specific targets were verified as compilation-clean (`exit 0`). Deeper logical issues (such as metavariables in `HeckeH3`) remain.

---

## 2. Lean Vacuity Audit Findings

The vacuity audit was conducted using the TS scanner script (`content/pipeline/lean-vacuity-axiom-audit.ts`). The refreshed scan on the `main` line of history (incorporating the `splitDecls` parser fix on 2026-06-18) yielded the following results.

### Summary Metrics (1755 `.lean` files scanned)
- **Total defects / candidates**: 366
- **Total exempt stubs / shadows**: 48
- **Files flagged**: 353

### Category Breakdown
1. **`proof-no-self-assuming-projection`**: **199 candidates**
   - *Verdicts*: 199 classified as **degenerate**, 2 classified as **legitimate** (scanner false positives).
   - *Nature of Degeneracy*: Occurs when a theorem merely projects a class field of conclusion type verbatim (`:= ctx.claim_foo` where `claim_foo : P` and conclusion is `P`). The proof is vacuous since the context instance assumes the conclusion directly.
   - *Remediation*: Restructure class to carry *hypotheses* and derive the conclusion via composition, or demote the `theorem` to a `conjecture`/`remark`.
2. **`proof-no-trivial-true` / `placeholder-true`**: **111 candidates**
   - *Nature*: Theorems stated as `: True := trivial` or `: True := sorry` with no corresponding real library declaration.
   - *Remediation*: Demote to `conjecture` or formalize actual propositions with `sorry` + `-- Ref:`.
3. **`proof-no-decide-masking`**: **31 candidates**
   - *Nature*: Proofs closed via `native_decide` (meaning they rely on external computations and inject `Lean.ofReduceBool` into the axioms).
   - *Remediation*: Replace with standard `decide` where termination is provable.
4. **`proof-no-false-premise`**: **13 candidates**
   - *Nature*: Vacuum proofs where one of the hypotheses is impossible (e.g. `False`).
5. **`proof-no-provable-axiom`**: **0 remaining**
   - *Nature*: Axioms declared without a bibliography reference.
   - *Resolution*: 5 uncited axioms in `LinearJSJVolume.lean` (such as `AtomicKnot`, `Vol`, `Vol_p`, `Vol_n`, and `JSJ_volume_additivity`) were resolved by applying proper manuscript citations (`[lewin1981]`, etc.).

---

## 3. Discharge Queue Status

An audit of `todos/lean-discharge-queue.json` shows that the queue contains **8 items** plus 1 metadata registry. Of these, only **3 items are active/open**, while the rest are closed.

### Active/Open Discharge Items
1. **`lean-catalan-G-numerical-bound`** (Priority: Medium)
   - *Summary*: Prove `catalan_G_numerical_bounds : G > 0.915 ∧ G < 0.916` (currently an axiom).
   - *Target File*: `content/quantum-observable-universe/lean/QOU/Archimedean/BorromeanVolumeCatalan.lean`
   - *Sketch*: Use Leibniz alternating series error bound `|G - S_N| <= a_{N+1}` from `Mathlib.Analysis.SpecificLimits.Normed`. At `N=22`, compute `S_22` and evaluate via `norm_num`.
   - *Blockers*: Network policy blocks olean cache download from `release.lean-lang.org`. Workaround: Restore `lake-cache/qou-v4-24-0` branch locally.
2. **`lean-discharge-triage-pass`** (Priority: High)
   - *Summary*: Triage 272 non-class sorries across the repository into `TRACTABLE` / `PROBLEMATIC` / `RESEARCH-GRADE`.
   - *Status*: Blocked on Lean LSP availability. Requires a fully built local target and then running `lean_diagnostic_messages` per file.
3. **`lean-compile-diagnostics-regen`** (Priority: High)
   - *Summary*: Regenerate `docs/audits/lean-compile-diagnostics.json` to resolve stale sidecar check failures (629 stale fails).
   - *Status*: A partial regeneration was run on 2026-06-13, but full registry update is gated on a completely green `lake build QOU`.

### Closed/Stale Queue Items
The remaining 5 items were batch-closed by the repository owner on 2026-06-09:
- `lean-q-schur-h3-y-lambda-extension` (Resolved: H_3 proofs landed in `QSchurYLambdaClosedForm.lean` via `af3316bf`).
- `lean-bar-involution-extension` (Wontfix: candidate files do not exist on `main`).
- `lean-mathlibext-sdp-rank-equality` (Resolved: file is sorry-free on `main`).
- `lean-staircase-corner-hook` (Resolved: sorry-free on `main`).
- `lean-tractable-fluid-dynamics` (Resolved: sorry-free on `main`).
- `lean-g-action-on-substrate` (Wontfix: re-scoped to `§3b-cond` permanent class registry).
- `lean-section-3b-cond-classes-permanent` (Resolved: catalog landed in `docs/audits/2026-06-03-lean-3b-cond-class-sorries-catalog.md`).
- `infra-lean-cache-host-bypass` (Resolved: Tier-2 cache-restore script `lake-cache-fetch.sh` successfully wired to bypass firewalled CDN).
- `lean-phi-q-at-zero`, `lean-li2-q-at-zero`, `lean-ord-u-zero-trm-eq` (Resolved: restructured definitions on `main` to make boundary values theorems rather than axioms).
