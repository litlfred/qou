# Analysis Report: mass-theory Directory Placeholders, TODOs, and Sorries

This report details the findings from scanning the `content/quantum-observable-universe/mass-theory/` directory for placeholders, `TODO`s, `FIXME`s, and `sorry`s, cross-referencing them with the vacuity audit results, and analyzing the current branch status.

---

## 1. Executive Summary

- **Total `TODO`s / `FIXME`s:** 8 occurrences. 0 `FIXME`s. All `TODO`s are either metadata tags (`todo-html` tags in TS files) or documentation-level roadmap markers (in `.md` and `.lean` files).
- **Total `sorry`s:** Found in 19 files. **Zero bare/unreferenced `sorry`s.** Every active `sorry` carries a citation: either a literature reference (e.g. `[kashaev1997]`, `[wenzl1988b]`) or a manuscript-internal reference (e.g. `[manuscript] prop:confinement-sdp`). One occurrence (`delta-q-decoration.lean`) is inside a block comment.
- **Vacuity / Shadow Stubs:** 22 local sibling `.lean` files are flagged as redundant "shadow stubs" in the vacuity audit. The real formalizations exist in the library tree (`content/quantum-observable-universe/lean/QOU/...`), meaning these stubs are unnecessary and cause trivial-true vacuity audit failures.
- **Non-Exempt Defects:** 
  - 2 files (`bring-residue-resolvent.lean`, `reidemeister-mass-invariance.lean`) contain `native_decide` calls.
  - 2 files (`magic-A-binding-formula.lean`, `q-pochhammer-partial-product.lean`) are flagged as false-premise defects (but are actually scanner false positives on induction/by-cases bases).
  - 1 file (`symbolic-character-table.lean`) is flagged as a `proof-no-trivial-true` placeholder-true defect, but is actually a redundant shadow stub.
- **Branch status:** The `claude/placeholder-beans-2026-06-21` branch contains sidecar `.qa.json` updates recording the results of the `proof-no-placeholder-stub` audit run. No source code changes in `mass-theory/` have been made yet.

---

## 2. Scan Results & Remediation Strategies

### A. TODOs & FIXMEs
No `FIXME`s were found. The `TODO`s found are classified below:

| File | Line | Context | Type | Remediation Strategy |
|---|---|---|---|---|
| `descent-rate-probe-sim.ts` | 13 | `tags: ["todo-html", ...]` | Metadata tag | Keep tag; no change required. |
| `multi-level-jet-sum-sim.ts` | 12 | `tags: ["todo-html", ...]` | Metadata tag | Keep tag; no change required. |
| `q-beta-radius-of-convergence-gate.md` | 30 | `q = 1 shadow ... TODO` | Roadmap checklist | Keep as documentation; no code changes. |
| `q-beta-radius-of-convergence-gate.md` | 31 | `Direction sanity ... TODO` | Roadmap checklist | Keep as documentation; no code changes. |
| `q-beta-radius-of-convergence-gate.md` | 96 | `q=1 shadow → TODO` | Roadmap checklist | Keep as documentation; no code changes. |
| `q-beta-radius-of-convergence-gate.md` | 97 | `Direction sanity → TODO` | Roadmap checklist | Keep as documentation; no code changes. |
| `q-beta-radius-of-convergence-gate.md` | 100 | `steps 4–5 are TODO` | Roadmap checklist | Keep as documentation; no code changes. |
| `reeb-bundle.lean` | 35 | `tracked as a TodoItem` | Roadmap note | Keep as documentation; no code changes. |

---

### B. Sorries Analysis
Active `sorry` occurrences were audited for compliance with the bibliographic citation rule (AGENTS.md §1).

| File | Line | Type | Reference Citation | Remediation Strategy |
|---|---|---|---|---|
| `alpha-k-categorical-closure.lean` | 78 | Conjecture Instance | `[manuscript] conj:alpha-k-categorical-closure` | **KEEP** — Valid §3b-cond conjecture class instance representation. |
| `chi-lambda-w0-sign-weighting.lean` | 146 | Theorem Proof | `[manuscript] prop:chi-lambda-w0-sign-weighting` | **KEEP** — Cited manuscript theorem. |
| `confinement-sdp.lean` | 29 | Theorem Proof | `[manuscript] prop:confinement-sdp` | **KEEP** — Cited manuscript theorem. |
| `content-scaling-correspondence.lean` | 11 | Def/Proof | `[manuscript] §5.6, prop:content-scaling-correspondence` | **KEEP** — Cited manuscript theorem. |
| `crystal-basis-resolves-mass-tower-open-problems.lean` | 11 | Theorem Proof | `[manuscript] prop:crystal-basis-resolves-mass-tower-open-problems` | **KEEP** — Cited manuscript theorem. |
| `delta-q-decoration.lean` | 34 | Comment | `[wenzl1988b] Wenzl 1988, DOI 10.1007/BF01393839` | **KEEP** — Inside a block comment; serves as a doc note. |
| `descended-level-zero.lean` | 11 | Theorem Proof | `[manuscript] prop:descended-level-zero` | **KEEP** — Cited manuscript theorem. |
| `interface-knot-markov-z.lean` | 143 | Theorem Proof | `[manuscript] prop:interface-knot-markov-z` | **KEEP** — Cited manuscript theorem. |
| `jucys-murphy-central-elements-qou.lean` | 72, 81 | Theorem Proofs | `[manuscript] jucys-murphy-central-elements-qou.ts` | **KEEP** — Cited manuscript theorems. |
| `kashaev-volume-conjecture.lean` | 94 | Theorem Proof | `[manuscript] kashaev-volume-conjecture` | **KEEP** — Cited manuscript theorem. |
| `knot-operator-transition.lean` | 15 | Theorem Proof | `[manuscript]` (shadow stub) | **DELETE FILE** — Duplicate shadow stub (see Section C). |
| `lepton-mass-tower-canonical.lean` | 55, 58 | Def Case | `[manuscript] conj:lepton-mass-tower-canonical` | **KEEP** — Cited conjectural definition cases. |
| `lepton-mass-tower-canonical.lean` | 146 | Theorem Proof | `[manuscript] — deferred to non-comm setting` | **KEEP** — Cited manuscript theorem (deferred proof). |
| `lr-tensor-character-bridge.lean` | 113 | Theorem Proof | `[manuscript] cor:lr-tensor-character-bridge` | **KEEP** — Cited manuscript theorem. |
| `mass-endomorphism-tower.lean` | 82 | Theorem Proof | `[manuscript] prop:mass-endomorphism-tower` | **KEEP** — Cited manuscript theorem. |
| `partition-sum-proton-residual.lean` | 89 | Existential proof | `[manuscript] computations/frobenius_partition_sum.py` | **KEEP** — Cited witness-bound computation. |
| `phi-q-tower-jsj-bridge.lean` | 136 | Instance field | `[kashaev1997] Kashaev, Lett. Math. Phys. 39` | **KEEP** — Cited conjecture class instance. |
| `symbolic-character-table.lean` | 29 | Theorem Proof | `[manuscript]` (shadow stub) | **DELETE FILE** — Duplicate shadow stub (see Section C). |
| `vol-through-tau.lean` | 48 | Existential proof | `[manuscript]` | **KEEP** — Cited manuscript theorem. |
| `volume-perturbation-formula.lean` | 13 | Theorem Proof | `[manuscript]` | **KEEP** — Cited manuscript theorem. |

---

### C. Redundant Shadow Stubs (Trivial-True stubs)
The following 22 files in `content/quantum-observable-universe/mass-theory/` are flagged as "shadow stubs" in the vacuity audit. The real formalizations exist in the library path under `content/quantum-observable-universe/lean/QOU/`. 

According to **AGENTS.md §0a**, these local siblings are redundant and should be deleted to prevent them from shadowing the real declarations:

1. `bring-trilog-imaginary-tate-rational.lean` 
   *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/BringTrilogImaginaryTateRational.lean`)*
2. `chirality-writhe-ribbon-derivation.lean` 
   *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/ChiralityWritheRibbon.lean`)*
3. `cl3-zeta5-orbit-sum-identity.lean` 
   *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/Cl3Zeta5OrbitSum.lean`)*
4. `cl3-zeta5-pslq-independence.lean` 
   *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/Cl3Zeta5PslqIndependence.lean`)*
5. `cyclotomic-cl3-orbit-sum-general.lean` 
   *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/CyclotomicCl3OrbitSum.lean`)*
6. `cyclotomic-depth3-dimension-synthesis.lean` 
   *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/CyclotomicDepth3DimensionSynthesis.lean`)*
7. `cyclotomic-dimension-synthesis-all-depths.lean` 
   *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/CyclotomicDimensionSynthesisAllDepths.lean`)*
8. `cyclotomic-orbit-sum-all-depths.lean` 
   *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/CyclotomicOrbitSumAllDepths.lean`)*
9. `cyclotomic-trilog-imaginary-closed-form.lean` 
   *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/CyclotomicTrilogImaginary.lean`)*
10. `delta-max-uniform-bound.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/MassEndomorphism/DeltaMaxUniformBound.lean`)*
11. `feynman-categorical-trace.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/FeynmanPathIntegrals.lean`)*
12. `feynman-eigenbasis-decomposition.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/FeynmanPathIntegrals.lean`)*
13. `feynman-trace-collapse.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/FeynmanPathIntegrals.lean`)*
14. `jonquiere-cyclotomic-tate-rationality.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/JonquiereCyclotomicTateRationality.lean`)*
15. `knot-operator-transition.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/knot_operator_transition.lean`)*
16. `markov-pair-z2.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/Interactions/MarkovPeel.lean`)*
17. `phi-q-tower-algebraic-stratification.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/PhiQTowerAlgebraicStratification.lean`)*
18. `staircase-corner-hook.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/StaircaseCornerHook.lean`)*
19. `term6-binding-density.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/Term6BindingDensity.lean`)*
20. `three-calibration-inputs.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/ThreeCalibrationInputs.lean`)*
21. `two-filtration-bridge-general.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/TwoFiltrationBridgeGeneral.lean`)*
22. `wigner-np-pairing.lean` 
    *(real formalization: `content/quantum-observable-universe/lean/QOU/Archimedean/ConfinedKnotBinding.lean`)*
23. `symbolic-character-table.lean`
    *(real formalization: `content/quantum-observable-universe/lean/QOU/BraidKnot/symbolic_character_table.lean`)*

**Remediation:** **DELETE** these 23 redundant `.lean` sibling files in `content/quantum-observable-universe/mass-theory/`. The `lean.ref` fields in the metadata `.ts` files already correctly resolve to the `QOU` namespace declarations compiled in the main package, making these stubs obsolete.

---

### D. Non-Exempt Vacuity Defects

#### 1. `native_decide` Masking (`proof-no-decide-masking`)
The use of `native_decide` adds `Lean.ofReduceBool` to the axiom set, which violates `proof-no-decide-masking` rules.

- **Files affected:**
  - `bring-residue-resolvent.lean` (Lines 198, 204, 210, 217):
    Evaluating concrete non-zero denominators, e.g.:
    `theorem bring_residue_q_eq_2_pole_nonzero_at_3 : 1 - hShift (2 : ℚ) * (2 : ℚ)^3 ≠ 0 := by unfold hShift; native_decide`
  - `reidemeister-mass-invariance.lean` (Lines 113, 116):
    Evaluating simple shell numbers, e.g.:
    `theorem ground_state_shell : shellNumber 3 = 1 := by native_decide`

- **Remediation:** Replace `native_decide` with `rfl` or `decide`. Since these are simple evaluation checks on integers/rationals, the compiler can resolve them decidably and cleanly without using `native_decide`, thereby dropping the extra axiom dependency.

#### 2. False Premise Scanner Hits (`proof-no-false-premise`)
The scanner flags standard mathematical proof patterns as false-premise defects because they contain contradictory rcases or impossible eliminations.

- **Files affected:**
  - `magic-A-binding-formula.lean` (Lines 170, 179):
    Uses `absurd hc (by decide)` on a by-cases branch to eliminate an impossible equality (e.g. `AlphaShift = DoublyMagic`).
  - `q-pochhammer-partial-product.lean` (Line 67):
    Uses `(Nat.not_lt_zero k hk).elim` to discharge the impossible induction base case where `k < 0`.

- **Remediation:** **None.** These are scanner false positives / heuristic over-matches. The overall theorems are not vacuously true; they only use standard contradiction/base-case reasoning. These should be marked as exempt in the `.qa.json` files or ignored.
