# Lean Content Block Audit — Quantum Observable Universe

**Generated:** 2026-04-06  
**Commit:** See `proof-objects.json` for current SHA  
**Paper:** quantum-observable-universe

---

## Executive Summary

| Metric | Value | Status |
|--------|-------|--------|
| Total `.lean` files (sibling + build) | 374 | — |
| Sibling `.lean` files (in chapter dirs) | 316 | — |
| Build system `.lean` files (lean/) | 58 | — |
| **Total actual `sorry` terms** | **55** | 🟡 |
| Sorry with citations | 47 | ✅ |
| **Sorry WITHOUT citations** | **8** | 🔴 |
| **Trivial truths** (`True := by trivial`) | **3** | 🔴 |
| Axiom declarations | 75+ | 📎 All cited |
| Python computation scripts | 73 | — |
| Python witness JSONs | 52 | — |
| Python witnesses with structured format | 1 | 🔴 |
| Python scripts without witnesses | 21 | ⚠️ |

---

## Chapter-by-Chapter Lean Status

### ✅ Ch 0 — Introduction
- **Files:** 0 lean | **Sorries:** 0 | No Lean required (prose only)

### ✅ Ch 1 — Quantum Observable Universe (`ch1-quantum-observable-universe`)
- **Sibling files:** 17 | **Sorries:** 0 | **Axioms:** 0
- **Status:** Complete. All definitions and propositions proved.
- Includes: rigid-monoidal-category, quantum-universe, snake-identity,
  frobenius-relation, categorical-jet, involutive-structure, hodge-su2, etc.

### 🟡 Ch 2 — Quantum Geometry (`ch2-quantum-geometry`)
- **Sibling files:** 68 | **Sorries:** 1 | **Axioms:** 20
- **Sorry detail:**
  - `q-codifferential-formula-prop.lean:127` — Ref: [manuscript] Ch. 2 ✅
- **Axiom strategy:** 20 axioms encoding differential form algebra (Webster
  inner product, adjoint operators, Reeb field) — all standard mathematical
  infrastructure not yet in Mathlib.
- **Status:** Essentially complete. Single sorry is in the q-codifferential
  adjoint relation which depends on axiomatized differential form machinery.

### ✅ Ch 3 — Lifting of Quantum Torsion (`ch3-lifting-of-quantum-torsion`)
- **Sibling files:** 28 | **Sorries:** 0 | **Axioms:** 5
- **Status:** Complete. All descent and torsion theorems proved.

### 🟡 Ch 4 — Path Integrals and Braiding (`ch4-path-integrals-and-braiding`)
- **Sibling files:** 50 | **Sorries:** 14 | **Axioms:** 30
- **Sorry detail (all cited ✅):**
  - `vertex-algebra-relations.lean` — 4 sorries (Ref: [jones1987], [kassel1995])
  - `vertex-is-exceptional-divisor.lean` — 3 sorries (Ref: [kassel1995], [manuscript])
  - `markov-trace-product.lean` — 2 sorries (Ref: [jones1987], [kassel1995])
  - `transfer-matrix-level-independence.lean` — 2 sorries (Ref: [jones1987], [manuscript])
  - `knot-particle-correspondence.lean` — 1 sorry (Ref: [jones1987])
  - `reeb-bundle.lean` — 1 sorry (Ref: [manuscript] Ch 6 §2)
  - `q-momentum.lean` — 1 sorry (Ref: [jones1987])
- **Assessment:** All sorries reference peer-reviewed sources (Jones 1987,
  Kassel 1995). These encode deep mathematical results (Markov trace theory,
  braid group representations) that require substantial Mathlib infrastructure
  to formalize.

### 🔴 Ch 5 — Brings Surface (`ch5-brings-surface`)
- **Sibling files:** 61 | **Sorries:** 16 | **Axioms:** 17
- **Sorry detail (all cited ✅):**
  - `skein-finiteness-bound.lean` — 3 sorries (Ref: [manuscript] §6)
  - `spectral-decomposition-qvalue.lean` — 3 sorries (Ref: [manuscript] §5)
  - `descartes-elliptic-curve.lean` — 2 sorries (Ref: [manuscript] §5)
  - `weierstrass-projection.lean` — 2 sorries (Ref: [manuscript] §5, Silverman VI.3.6)
  - `categorical-proton.lean` — 1 sorry (Ref: [manuscript] Ch. 5)
  - `categorical-neutron.lean` — 1 sorry (Ref: [manuscript] Ch. 5)
  - `shell-closure-normal-form.lean` — 1 sorry (Ref: [kazhdan-lusztig1979])
  - `descartes-knot-eigenbasis.lean` — 1 sorry (Ref: [chari1994guide] Ch. 10)
  - `torus-hopf-stability.lean` — 1 sorry (Ref: [manuscript] Ch. 5)
  - `em-coupling-projection.lean` — 1 sorry (Ref: [manuscript] §5)
- **Assessment:** Highest sorry count. Most reference the manuscript itself
  (§5, §6), indicating these are proofs that need to be written, not external
  results. Priority for formalization work.

### ✅ Ch 6 — Descartes Universe (`ch6-descartes-universe`)
- **Sibling files:** 12 | **Sorries:** 0 | **Axioms:** 0
- **Status:** Complete.

### 🟡 Ch 7 — Observations (`ch7-observations`)
- **Sibling files:** 25 | **Sorries:** 7 | **Axioms:** 0
- **Sorry detail (all cited ✅):**
  - `w-boson-mass-discrepancy.lean` — 2 sorries (Ref: [manuscript] §7, [jones1985])
  - `building-block-knots.lean` — 2 sorries (Ref: [jones1987], [manuscript] §7)
  - `double-slit-massive-pattern.lean` — 1 sorry (Ref: [manuscript] §7)
  - `trace-ratio-observable.lean` — 1 sorry (Ref: [manuscript] §7)
  - `neutron-prediction-comparison.lean` — 1 sorry (Ref: [manuscript] §7)
- **Assessment:** All cited. These encode numerical predictions that need
  connection to the formal Hecke algebra infrastructure.

### 🔴 Ch 8 — Algebraic Substrate (`ch8-algebraic-substrate`)
- **Sibling files:** 24 | **Sorries:** 10 | **Axioms:** 2
- **Sorry detail:**
  - `hasse-weil-bound.lean` — 3 sorries ❌ **NO CITATIONS**
  - `macroscopic-stability-equivalence.lean` — 2 sorries ❌ **NO CITATIONS**
  - `explicit-formula.lean` — 2 sorries ❌ **NO CITATIONS**
  - `substrate-self-duality.lean` — 1 sorry (Ref: [kock2004] §2.3) ✅
  - `tannaka-krein-isomorphism.lean` — 1 sorry (Ref: [reshetikhin1991]) ✅
  - `rigid-dualizing-complex.lean` — 1 sorry (Ref: [yekutieli2015]) ✅
- **⚠️ ACTION REQUIRED:** 8 sorries in `hasse-weil-bound.lean`,
  `macroscopic-stability-equivalence.lean`, and `explicit-formula.lean` lack
  `-- Ref:` citations. These need citations added (likely [weil1949],
  [connes1999], or [montgomery-vaughan2007]).

### ✅ Ch 8 — Glossary (`ch8-glossary`)
- **Sibling files:** 8 | **Sorries:** 0 | **Axioms:** 0
- **Status:** Complete. Glossary blocks (remark wrappers for Mathlib types).

### ✅ Ch 9 — Information Theory (`ch9-information-theory`)
- **Sibling files:** 16 | **Sorries:** 0 | **Axioms:** 1
- **Status:** Complete. Single axiom (`aeon_recycling`) is a conjecture.

### ✅ Ch 10 — Fluid Dynamics (`ch10-fluid-dynamics`)
- **Sibling files:** 0 | No Lean formalization yet.

### 🟡 Ch 11 — q-Geometric Langlands (`ch11-q-geometric-langlands`)
- **Sibling files:** 7 | **Sorries:** 0 (documented as conjecture)
- **Note:** File header says "sorry = conjecture (not missing proof)".
  This is correct — the chapter axiomatizes the q-Geometric Langlands
  conjecture as a class.

---

## Lean Build System (`lean/QOU/`)

### 🟡 QOU/Descartes/ — 6 sorries, 3 trivial truths

| File | Sorries | Citations | Notes |
|------|---------|-----------|-------|
| `AxialCoupling.lean` | 3 | ✅ [manuscript] | Blocked on multi-generator Hecke→matrix |
| `OrderingIndependence.lean` | 2 | ✅ [murphy1992] | Blocked on Young idempotent formalization |
| `TMCorrespondence.lean` | 1 | ✅ documented | Scaling discrepancy + foldl bridge |

### 🔴 Trivial Truth Placeholders (AxialCoupling.lean)

These are NOT real proofs — they prove `True` (always provable), not the
actual mathematical claims:

```lean
-- Line 106: theorem sym_trace_ordering_independent : True := by trivial
-- Line 114: theorem std_trace_braid_dependent : True := by trivial
-- Line 125: theorem color_avg_essential : True := by trivial
```

**Action required:** These must be either:
1. Replaced with correct statement + proof (or sorry with citation)
2. Converted to comments/documentation
3. Removed entirely

### ✅ QOU/Torsion/ — 0 sorries
### ✅ QOU/QuantumObservableUniverse/ — 0 sorries
### ✅ All other QOU modules — 0 sorries (in build system)

---

## Witness Infrastructure Status

### Lean Witnesses
- **Current system:** `scripts/lean-witness.ts` manages `.lean.<hash>.witness` files
- **Enhancement:** Now includes `commitSha` and `fileCommitSha` for staleness detection
- **Staleness check:** `bun run scripts/lean-witness.ts status`

### Python Computation Witnesses

| Category | Count | Notes |
|----------|-------|-------|
| Total `.py` scripts | 73 | in `folio-assistant/computations/` |
| Witness JSONs | 52 | `.witness.json` sibling files |
| **Structured format** | **1** | Only `knot-volumes.witness.json` |
| With commit SHA | 4 | `git_sha` field |
| With assertions | 2 | Structured pass/fail checks |
| Legacy (ad-hoc) | 51 | Need migration to `witness_base.py` |
| Scripts without witnesses | 21 | Need to be run |

### New Infrastructure

- **`folio-assistant/computations/witness_base.py`** — Unified `WitnessBuilder`
  class for Python computations. Auto-captures commitSha, scriptHash, and
  provides structured assertions with tolerances.
- **`scripts/witness-audit.ts`** — Unified staleness checker for both Lean
  and Python witnesses.
- **`scripts/lean-audit.ts`** — Deep chapter-by-chapter audit with sorry
  classification, trivial truth detection, and axiom inventory.

---

## Action Items

### Immediate (blocking quality)

1. **Add citations to 8 uncited sorries in ch8-algebraic-substrate:**
   - `hasse-weil-bound.lean:37,51,65` — Add `-- Ref: [weil1949]` or appropriate
   - `macroscopic-stability-equivalence.lean:53,64` — Add `-- Ref:` citation
   - `explicit-formula.lean:67,96` — Add `-- Ref:` citation

2. **Remove or replace 3 trivial truth placeholders in AxialCoupling.lean:**
   - Lines 106, 114, 125: `True := by trivial` is meaningless

### Short-term (formalization priorities)

3. **Ch 5 (16 sorries):** Highest sorry count, many self-referencing [manuscript].
   Prioritize: `skein-finiteness-bound`, `spectral-decomposition-qvalue`,
   `descartes-elliptic-curve`.

4. **Ch 8 (10 sorries):** Deep algebraic results (Hasse-Weil, RH equivalence,
   explicit formula). These may remain as axioms with proper citations.

5. **Lean build system (6 sorries):** The Descartes module sorries are
   well-documented and blocked on specific infrastructure.

### Medium-term (witness infrastructure)

6. **Migrate 51 legacy Python witnesses to `witness_base.py`:**
   Do this incrementally as scripts are modified.

7. **Run 21 Python scripts that lack witnesses:**
   Generate witness JSONs for completeness.

8. **Stamp Lean witnesses after successful builds:**
   Use `bun run scripts/lean-witness.ts stamp <file>` after `lake build`.

---

## Sorry Summary Table

| Chapter | Sibling | Build | Total | Cited | Uncited | Axioms |
|---------|---------|-------|-------|-------|---------|--------|
| Ch 1 QOU | 0 | 0 | 0 | — | — | 0 |
| Ch 2 Geometry | 1 | 0 | 1 | 1 | 0 | 20 |
| Ch 3 Torsion | 0 | 0 | 0 | — | — | 5 |
| Ch 4 Braiding | 14 | 0 | 14 | 14 | 0 | 30 |
| Ch 5 Brings | 16 | 0 | 16 | 16 | 0 | 17 |
| Ch 6 Descartes | 0 | 6 | 6 | 6 | 0 | 0 |
| Ch 7 Observations | 7 | 0 | 7 | 7 | 0 | 0 |
| Ch 8 Substrate | 10 | 0 | 10 | 2 | **8** | 2 |
| Ch 8 Glossary | 0 | 0 | 0 | — | — | 0 |
| Ch 9 Info Theory | 0 | 0 | 0 | — | — | 1 |
| Ch 11 Langlands | 0 | 0 | 0 | — | — | 0 |
| **TOTAL** | **48** | **6** | **54** | **46** | **8** | **75** |

Plus: 3 trivial truths (AxialCoupling.lean), 1 sorry in UGB/NormalForms.lean
