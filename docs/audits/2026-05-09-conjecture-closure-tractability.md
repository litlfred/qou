# Conjecture closure-tractability triage (2026-05-09)

Per AGENTS.md §3b-cond, the QOU paper has **65 class-axiomatized
conjectures** (down from 258 §3b violators in the original
2026-05-08 audit). Each is a Lean `class` whose `sorry`-bearing
instance encodes the conjectural content; downstream theorems take
the class as an explicit `[Instance]` hypothesis to remain
rigorous-conditional under §3b-cond.

This document triages each conjecture by **closure tractability** —
how achievable promotion from `class` to a proven `theorem` is.

## Tiers

- **Tier A — Mostly-mechanical Lean work**: structure exists; proof
  is direct application of existing Mathlib API. Achievable in a
  single follow-up PR with lake-build access (~hours per conjecture).
- **Tier B — Requires Mathlib upstream**: proof depends on a
  Mathlib feature that doesn't yet exist (Lie-valued forms, Iwahori-
  Hecke representation theory, partition-Fintype, etc). Achievable
  once the upstream lands; per-conjecture work moderate (~days).
- **Tier C — Genuine open math**: famous unsolved problems or active
  research. Not closable by code edits alone. Class-axiomatization
  is the *correct* end state.

## By chapter

### algebraic-substrate (2)

| Conjecture | Tier | Notes |
|---|---|---|
| `magic-numbers-bring` | B | Bring-radical roots of unity in Lean awaits Mathlib's `Polynomial.IsCyclotomic` extension. |
| `p-vs-np-qou` | C | P vs NP — Clay Millennium Problem. |

### appendix-surreals (1)

| Conjecture | Tier | Notes |
|---|---|---|
| `classical-limit-stpart` | A | Standard-part operator on `Surreal`; once the reduction is type-correct, the proof is ε-δ algebra. |

### braids-and-knots (30)

| Conjecture | Tier | Notes |
|---|---|---|
| `algebraic-geometric-dilog-equivalence` | B | Needs Mathlib's `Polylogarithm` / `MotivicCohomology`. |
| `archimedean-remainder-exponential-decay` | B | Tail-bound on q-Pochhammer; standard analysis once `qPochhammerSymbol` is wired. |
| `brane-level-selection` | A | Discrete choice from a finite set; mostly Lean plumbing. |
| `brane-tower-z-habiro` | B | Habiro ring needs Mathlib upstream. |
| `canonical-knot-id-sdp` | A | LP/SDP solver wiring; runs through `lp_dual_solver.py` → Lean. |
| `categorical-higgs-mechanism` | B | Categorical Higgs — needs symmetric-monoidal-with-trace upstream. |
| `categorical-linking-operation` | A | Mostly diagrammatic; `aesop_cat` should close most cases. |
| `categorical-neutrality-saturated-shells` | A | Discrete combinatorics; `decide` on partition tables. |
| `cemetery-group-emergence` | B | Symmetric-crystal Type B folding; KLR upstream. |
| `chirality-ribbon-frobenius` | A | Frobenius-Hopf ribbon equation; CategoryTheory.Monoidal. |
| `confinement-grading-correspondence` | A | Filtration-grading bijection; structural. |
| `crystal-graph-realization` | B | Kashiwara crystal API; needs Mathlib upstream. |
| `dilogarithm-archimedean-limit` | B | Same as `algebraic-geometric-dilog-equivalence`. |
| `hecke-anyonic-substrate` | B | Anyonic / modular-tensor-category upstream. |
| `hoefsmit-ew-cell-content` | A | Hoefsmit seminormal form is in QOU's MarkovTrace.lean; just needs algebraic identity proofs. |
| `jet-tower-uniform-delta-max` | A | Existence of bounded family; standard analysis. |
| **`kashaev-volume-conjecture`** | **C** | **Open famous (since 1995).** |
| `kazhdan-lusztig-classical-limit` | B | KL-basis decategorification; needs upstream. |
| `knot-factor-frobenius-pairing` | A | Frobenius pairing equation; structural. |
| `mass-element-nf` | A | Normal-form existence; constructive. |
| `mass-endomorphism` | A | Endomorphism-tower mass formula; mostly arithmetic. |
| `phi-q-tower-jsj-bridge` | B | JSJ decomposition needs `Topology.JSJ` (not in Mathlib). |
| `rho-prefactor-structural` | A | Rounding-to-integer Lean proof; tedious but mechanical. |
| `root-of-unity-mtc-truncation` | B | MTC truncation needs Mathlib's modular-tensor-category. |
| `shared-denominator-cusp-holonomy` | A | Algebraic identity over `ℚ(q)`; field arithmetic. |
| `shell-correction-term-seven` | A | Numerical witness pinned; just structural identity. |
| `symmetric-crystal-pair-production` | B | Type B folding upstream. |
| `weak-spectral-completeness` | B | Needs Mathlib's spectral theorem for self-adjoint operators on the Hecke representation. |
| `weinberg-angle-categorical` | A | Categorical mixing-angle formula; trigonometric identity. |
| `z-eq-n-rho-correction` | A | Arithmetic identity in the substrate. |

### descartes-universe (12)

| Conjecture | Tier | Notes |
|---|---|---|
| `abelianisation-at-algebraic-poles` | B | Needs MI / non-abelian Stokes upstream (R8 partial). |
| `baryon-period-ratio` | A | Period-ratio equation; field arithmetic on `ℝ`. |
| `bring-hyperbolic-knot-bloch-decomposition` | B | Bloch group + Bring radical upstream. |
| `denominator-zeros-as-sw-critical-points` | A | Polynomial-zero correspondence; closed by `polyrith` after the algebraic setup. |
| `e-hartree-categorical-derivation` | A | Mostly numerical witness pin + arithmetic identity. |
| `electroweak-higgs-torus-link-triplet` | A | Discrete classification result; `decide` over the link table. |
| `electroweak-mass-eigenstate-count` | A | Combinatorial count; decide. |
| `em-coupling-chern-simons` | B | Chern-Simons level upstream. |
| `force-carrier-knot-vs-link-dichotomy` | A | Discrete classification. |
| `gb-reduction-pl-thimble-bijection` | B | Picard-Lefschetz upstream needed (R8 partial). |
| **`hyperbolic-volume-transcendence`** | **C** | **Open transcendence problem.** |
| `pl-jsj-mass-integration-equivalence` | B | JSJ + Picard-Lefschetz upstream. |

### fluid-dynamics (6)

The five-conjecture **q-NS cone** — all famous open / Clay-adjacent:

| Conjecture | Tier | Notes |
|---|---|---|
| `levi-degeneracy` | B | Real-parameter projection works (R6); full ℂ-version needs Mathlib's root-of-unity machinery. |
| **`q-aubin-lions`** | **C** | q-deformed Aubin-Lions lemma — open. |
| **`ns-counterexample`** | **C** | NS-regularity counterexample — Clay-related. |
| **`critical-exponent`** | **C** | Critical-exponent universality — open. |
| **`blowup-yekutieli`** | **C** | Blow-up rate at criticality — open. |
| **`regularity-breakdown`** | **C** | Regularity breakdown structure — open. |

### information-theory (1)

| Conjecture | Tier | Notes |
|---|---|---|
| **`p-vs-np-boundary`** | **C** | P vs NP variant. |

### lifting-and-descent (2)

| Conjecture | Tier | Notes |
|---|---|---|
| `homological-shell-condensation` | A | Spectral-sequence collapse argument; uses R8 SS infrastructure. |
| `topological-decomposition-mass` | A | Mass-decomposition identity over closed knot. |

### molecular-construction (2)

| Conjecture | Tier | Notes |
|---|---|---|
| `palindromicity-orbital-type` | A | Combinatorial identity; `decide` on small orbital types. |
| `shell-closure-nf-term-count` | A | Term-count identity; arithmetic. |

### observations (4)

| Conjecture | Tier | Notes |
|---|---|---|
| `borromean-quark` | A | Discrete identification. |
| `cp-violation-spectral-form` | B | Spectral-form upstream needed. |
| `diagrammatic-double-magic-lr-fusion` | A | LR fusion combinatorics; `decide` / fin-cases. |
| `n-v-bring-action` | B | Bring action on N/V tower — same as `magic-numbers-bring`. |

### particle-interactions (4)

| Conjecture | Tier | Notes |
|---|---|---|
| `crossing-graded-mass-expansion` | A | Term-by-term mass expansion; algebraic identity. |
| `lifted-crossing-locality` | A | Locality property; structural. |
| `mass-volume-factorization` | A | Factorization identity; field arithmetic. |
| `q-integer-mass-formula` | A | q-integer arithmetic. |

### q-geometric-langlands (1)

| Conjecture | Tier | Notes |
|---|---|---|
| **`q-geometric-langlands`** | **C** | **Open famous (Frenkel-Gaitsgory program).** |

## Summary

| Tier | Count | % |
|---|---|---|
| **A — Mostly-mechanical** | **34** | **52 %** |
| **B — Awaits Mathlib upstream** | **22** | **34 %** |
| **C — Open famous math** | **9** | **14 %** |
| **Total** | **65** | 100 % |

## Recommendations

1. **Tier A (34 conjectures)** are the natural targets for follow-up
   PRs. Each is a few hours of Lean work with lake-build access; no
   new mathematics required. The categorical and algebraic identity
   conjectures dominate this tier.
2. **Tier B (22 conjectures)** should be tracked alongside the
   upstream Mathlib roadmap. As the upstream lands (Lie-valued
   forms → Yekutieli; partition-Fintype → Wedderburn; modular-
   tensor-category → MTC truncation; etc), each can be closed.
3. **Tier C (9 conjectures)** are open mathematical problems and
   should remain class-axiomatized. The §3b-cond pattern is the
   correct end-state for these.

## Tractability witness file

For each conjecture, the corresponding `.lean` sibling in
`content/quantum-observable-universe/<chapter>/<conj-slug>.lean`
already contains the class declaration, a canonical (trivially-
discharged) instance, and the conditional dependent theorem(s).
The sharpened versions of the most-shared classes
(`SingleVolumeIrrational`, `PLCorrectnessHypotheses`,
`QAubinLions`, `NSCounterexample`, `CriticalExponent`,
`BlowupYekutieli`, `RegularityBreakdown`) live in:

- [`QOU/BraidKnot/ConditionalClasses.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/ConditionalClasses.lean) — sharpened in R10
- [`QOU/AlgebraicSubstrate/ConditionalClasses.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/ConditionalClasses.lean) — sharpened in R10

with downstream corollaries in:

- [`QOU/BraidKnot/ConditionalCorollaries.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/ConditionalCorollaries.lean) — added in R10
- [`QOU/AlgebraicSubstrate/ConditionalCorollaries.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/ConditionalCorollaries.lean) — added in R10
