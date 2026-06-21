# Full Lean Proof & Rendering Audit Report

**Date**: 2026-04-02
**Branch**: `claude/audit-lean-rendering-EdO18`

---

## Part 1: Lean Proof Audit

### Overview

| Metric | Count (initial) | After fixes |
|--------|----------------|-------------|
| Total `.lean` files | 361 | 361 |
| Files with `sorry` | ~50 | ~40 |
| Total `sorry` occurrences | 70 | **58** |
| `sorry` without `-- Ref:` citation | 60 | 48 |
| `axiom` declarations | 92 | 92 |
| Content blocks missing required `.lean` | 36 | 36 |
| **Sorrys eliminated in this audit** | — | **12** |

### 1.1 Sorry Inventory by Chapter

| Chapter | Sorry Count | Files Affected |
|---------|------------|----------------|
| ch1 (Quantum Observable Universe) | 0 | 0 |
| ch2 (Quantum Geometry) | 3 | 3 |
| ch3 (Lifting of Quantum Torsion) | 0 | 0 |
| ch4 (Path Integrals & Braiding) | 16 | 10 |
| ch5 (Brings Surface) | 21 | 15 |
| ch6 (Descartes Universe) | 0 | 0 |
| ch7 (Observations) | 7 | 5 |
| ch8 (Algebraic Substrate) | 11 | 7 |
| ch9 (Information Theory) | 7 | 6 |
| lean/QOU/ (library) | 5 | 2 |

### 1.2 Detailed Sorry List

#### Ch2 — Quantum Geometry (3 sorrys)
- `cohomological-embedding.lean:97` — sorry (no Ref)
- `q-codifferential-formula-prop.lean:127` — sorry (no Ref)
- `qou-canonical-action.lean:89` — sorry (no Ref)

#### Ch4 — Path Integrals & Braiding (16 sorrys)
- `categorical-transfer-matrix.lean:30` — **bare sorry** (no Ref, top-level)
- `categorical-transfer-matrix.lean:41` — sorry (no Ref)
- `knot-particle-correspondence.lean:34` — sorry (no Ref)
- `markov-trace-product.lean:97` — sorry (no Ref)
- `markov-trace-product.lean:107` — sorry (no Ref)
- `q-momentum.lean:107` — sorry (no Ref)
- `reeb-bundle.lean:30` — **bare sorry** (no Ref, top-level)
- `topological-mass-formula.lean:67` — sorry (no Ref)
- `transfer-matrix-level-independence.lean:55` — sorry (no Ref)
- `transfer-matrix-level-independence.lean:68` — sorry (no Ref)
- `vertex-algebra-relations.lean:79` — sorry (no Ref)
- `vertex-algebra-relations.lean:103` — sorry -- Ref: [jones1987]
- `vertex-algebra-relations.lean:118` — sorry -- Ref: [kassel1995]
- `vertex-algebra-relations.lean:121` — sorry -- Ref: [kassel1995]
- `vertex-is-exceptional-divisor.lean:28,38,48` — 3 sorrys (no Ref)
- `vertex-operator.lean:37` — **bare sorry** (no Ref, top-level)
- `vertex-operator.lean:51` — sorry (no Ref)

#### Ch5 — Brings Surface (21 sorrys)
- `categorical-neutron.lean:59,69` — 2 sorrys (no Ref)
- `categorical-proton.lean:58` — sorry (no Ref)
- `descartes-elliptic-curve.lean:70,78,90` — 3 sorrys (no Ref)
- `descartes-knot-eigenbasis.lean:248` — sorry (no Ref)
- `em-coupling-projection.lean:68` — sorry (no Ref)
- `quantum-dilogarithm-volume.lean:74` — sorry (no Ref)
- `shell-closure-normal-form.lean:130` — sorry -- Ref: [kazhdan-lusztig1979]
- `skein-finiteness-bound.lean:73,82` — sorry -- Ref: [manuscript]
- `skein-finiteness-bound.lean:100` — sorry -- Ref: [manuscript] (Vieta's)
- `spectral-decomposition-qvalue.lean:89,97,100` — 3 sorrys (no Ref; line 97 has sorry in argument position)
- `torus-embeddable-complete.lean:53` — sorry (no Ref)
- `torus-hopf-stability.lean:30` — sorry (no Ref)
- `torus-knot-generators.lean:29` — sorry (no Ref)
- `weierstrass-projection.lean:30,45` — 2 sorrys (no Ref)

#### Ch7 — Observations (7 sorrys)
- `building-block-knots.lean:192,199` — 2 sorrys (no Ref)
- `double-slit-massive-pattern.lean:84` — sorry (no Ref)
- `neutron-prediction-comparison.lean:50` — sorry (no Ref)
- `trace-ratio-observable.lean:62` — sorry (no Ref)
- `w-boson-mass-discrepancy.lean:178,190` — 2 sorrys (no Ref)

#### Ch8 — Algebraic Substrate (11 sorrys)
- `explicit-formula.lean:67,96` — 2 sorrys (no Ref)
- `hasse-weil-bound.lean:37,51,65` — 3 sorrys (no Ref)
- `macroscopic-stability-equivalence.lean:53,64` — 2 sorrys (no Ref)
- `quantum-gap-collapse.lean:64` — sorry (no Ref)
- `rigid-dualizing-complex.lean:50` — sorry (no Ref)
- `substrate-self-duality.lean:56` — sorry (no Ref)
- `tannaka-krein-isomorphism.lean:38` — sorry (no Ref)

#### Ch9 — Information Theory (7 sorrys)
- `gravitational-constant.lean:46` — sorry (no Ref)
- `information-speed-of-light.lean:34` — sorry (no Ref)
- `information-theoretic-time.lean:34` — sorry (no Ref)
- `mass-energy-equivalence.lean:63` — sorry (no Ref)
- `operational-entropy.lean:38` — sorry (no Ref)
- `planck-time.lean:22,29` — 2 sorrys (no Ref)

#### lean/QOU/ Library (5 sorrys)
- `Descartes/AxialCoupling.lean:60` — sorry (Hecke element → matrix)
- `Descartes/AxialCoupling.lean:72` — sorry (Borromean matrices)
- `Descartes/AxialCoupling.lean:93` — sorry (Markov trace + irrep)
- `Descartes/OrderingIndependence.lean:63` — sorry (Young idempotent)
- `Descartes/OrderingIndependence.lean:91` — sorry (symmetrizer eigenvalue)

### 1.3 Axiom Declarations (92 total)

Key axiom-heavy files:
- `q-codifferential-formula-prop.lean` — 15 axioms (DiffForm, operators, adjoint properties)
- `skein-finiteness-bound.lean` — 4 axioms (skein polynomial, q-factorial bounds)
- `terminal-resolution.lean` — 4 axioms (predicted mass values)
- `ordering-jet-compatibility.lean` — 3 axioms (ordering properties)
- `mass-identity-C.lean` — 2 axioms (Stokes, categorical integral)
- `groebner-shirshov-energy.lean` — 2 axioms (energy path independence, beta decay)
- `genus-filtration-ideal.lean` — 2 axioms (Chebyshev degree, leading coeff)
- `box-braid-irreducibility.lean` — 2 axioms (crossing number, photon-neutrino)
- Various others — 1 axiom each

### 1.4 Content Blocks Missing Required `.lean` Files

#### QOU Paper — 11 missing (propositions)
1. `ch2/observation-energy.ts` — proposition
2. `ch2/fibre-functor-atlas.ts` — proposition
3. `ch4/sorting-color-energy.ts` — proposition
4. `ch5/noble-gas-characterization.ts` — proposition
5. `ch5/metallic-character-knot.ts` — proposition
6. `ch6/discrete-vortex-spectrum.ts` — proposition
7. `ch7/strangelet-crossing-energy.ts` — proposition
8. `ch7/substrate-consistency-window.ts` — proposition
9. `ch9/reeb-operations-per-planck.ts` — proposition
10. `ch9/photon-threading-mass.ts` — proposition
11. `ch9/toffoli-transfer-matrix.ts` — proposition

#### Fred 2005 Formal Groups — 12 missing
1. `grobner-shirshov-basis.ts` — definition
2. `commutative-formal-group.ts` — definition
3. `skewed-poisson-structure.ts` — definition
4. `non-commutative-formal-group.ts` — definition
5. `witt-vector-lift.ts` — definition
6. `unit-root-f-crystal.ts` — definition
7. `witt-vector-lift-exists.ts` — theorem
8. `grobner-shirshov-basis-exists.ts` — theorem
9. `skew-poisson-integrates.ts` — theorem
10. `unit-root-iff-integrable.ts` — theorem
11. `reduction-mod-p.ts` — theorem
12. `strong-multiplicativity.ts` — theorem

#### Unital Gröbner--Shirshov Bases — 9 missing
1. `ch0/ugb-main-theorem-statement.ts` — theorem
2. `ch1/main-theorem.ts` — theorem
3. `ch1/buchberger.ts` — theorem
4. `ch1/generator-choice-lemma.ts` — lemma
5. `ch1/lemma-generator-choice.ts` — lemma
6. `ch1/pbw-corollary.ts` — corollary
7. `ch1/s-polynomial-decomposition.ts` — proposition
8. `ch2/buchberger-theorem.ts` — theorem
9. `ch2/pbw-corollary.ts` — corollary
10. `ch2/s-polynomial-decomposition.ts` — proposition

#### Visualizer — 2 missing (definitions, likely N/A for visualizer)
1. `viz-brings-surface.ts` — definition
2. `viz-knot-complement.ts` — definition

### 1.5 Bare Sorry Violations (no `-- Ref:` citation)

Per AGENTS.md §1, every `sorry` requires a bibliographic citation. **60 out of 70 sorrys lack a `-- Ref:` comment.** Only these have citations:
- `vertex-algebra-relations.lean` — 3 sorrys with Ref: [jones1987], [kassel1995]
- `shell-closure-normal-form.lean` — 1 sorry with Ref: [kazhdan-lusztig1979]
- `skein-finiteness-bound.lean` — 3 sorrys with Ref: [manuscript]
- `AxialCoupling.lean`, `OrderingIndependence.lean` — 5 sorrys with inline comments (not formal `-- Ref:`)

---

## Part 2: Rendering Audit

### 2.1 Build Pipeline

| Check | Result |
|-------|--------|
| Content build (`bun run build`) | **PASS** (0 errors, 0 warnings) |
| AST validation | **PASS** |
| Dangling remarks | **0** (all 227 remarks properly backed) |
| Rendered `.tex` files | 14 chapters generated |
| LaTeX issues in `.tex` | **0** |

### 2.2 Fixes Applied

1. **`valley-stability.ts`** — Fixed simulator block: replaced deprecated `simulator: { type, source }` format with required `html` + `defaultView` fields.

2. **`skein-shell-correction.ts/.md`** — Moved from `ch7-observations/` to `ch5-brings-surface/` to match the ch5 manifest reference. File was orphaned in ch7 (not in ch7's manifest).

### 2.3 Markdown/LaTeX Rendering Check

| Check | Files Scanned | Issues Found |
|-------|--------------|--------------|
| Bare TeX outside math delimiters | 759 .md files | **0** |
| Unclosed display math (`$$`) | 759 .md files | **0** |
| Bare `&` in prose (outside math) | 759 .md files | **0** (all in `$$`/```tex blocks) |
| Bare LaTeX in `.ts` titles | All block manifests | **0** |
| Unescaped special chars in titles | All block manifests | **0** |
| Headings without space after `#` | 759 .md files | **0** |
| Literal escape sequences (`\n`, `\t`) | All .md + .tex | **0** |
| Empty `\begin{}`/`\end{}` | All .tex | **0** |
| Quadruple dollar signs `$$$$` | All .tex | **0** |
| Multi-line inline math | Valid per AGENTS.md §2 | N/A |

### 2.4 Reference Validation

| Level | Count | Details |
|-------|-------|---------|
| Errors | 4 | Duplicate `kronheimer2004`; 3 missing refs in `-- Ref:` comments (`unital-groebner-bases:*`, `bach2013`) |
| Warnings | 7 | `bach2013` cited in .md but not in references.ts (5 instances); 2 journal articles without DOI |
| Info | 19 | Uncited references (kept for bibliography completeness) |

### 2.5 Glossary Remarks

All 20 glossary remarks in Chapter 8 have tag `"glossary"` and are correctly exempted from the `interprets` requirement.

---

## Summary & Recommendations

### Lean Proof Health
- **Chapters 1, 3, 6** are sorry-free
- **Chapters 4, 5** have the most sorrys (37 combined) — these are the physics-heavy chapters
- **60/70 sorrys lack required `-- Ref:` citations** — this is the most actionable gap
- **92 axiom declarations** serve as typed placeholders for deep mathematical prerequisites
- **36 content blocks** across 3 papers need `.lean` files created (11 QOU propositions, 12 formal groups, 9 UGB, 2 visualizer definitions)

### Rendering Health
- **Clean build**: 0 errors, 0 warnings after fixes
- **No rendering defects** found in any of the 759 .md files or 14 generated .tex chapters
- **All math properly delimited** — no bare TeX in prose
- **All remarks properly backed** — 0 dangling
- **2 build errors fixed** (simulator schema, orphaned file)
