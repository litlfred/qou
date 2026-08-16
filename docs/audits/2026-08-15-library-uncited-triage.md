# Uncited library documents — triage queue

**Generated** 2026-08-15 by `scripts/library-relevance-rank.py --write-triage`.
Regenerate rather than edit.

134 of 341 library documents carry no `library:` back-reference from
`content/schema/references.ts` — nothing in the bibliography points at them.
That is the backlog [`local/paper-relevance-triage`](../../.claude/skills/local/paper-relevance-triage.md)
exists to work; it was invisible until the sources were sectioned.

## How this is ranked

By **topical overlap with the qou corpus**, not by volume of extracted
material. An earlier pass ranked by formalizable-candidate count and put a
whole journal issue first — that measures how much formal content a document
*offers*, which is not the same question.

The vocabulary is derived from this corpus, not hand-supplied: every content-block
`title:` and `defines:` entry plus the notation register, yielding 2137 terms,
of which 1213 discriminate within the library. Weighting is library IDF times
corpus frequency: a term must be both rare in the library and central here, so
neither a ubiquitous word nor a rare-but-alien one scores. Scoring reads each
document's extracted *claims*
(`candidates.json`) plus its title and section titles — not its prose — so a
passing mention in a bibliography does not inflate a score.

**The score is a prior, not a verdict.** It says "this document is written in our
vocabulary", which is where triage should start, not where it should end.

## Bound volumes (0 flagged)

Marked `!` below. A single paper has one Introduction and one References;
these have three or more. Two different things produce that, and they want
different handling:

* **A bound journal issue** (`ant-v14-n7-s`, 19) really is several unrelated
  papers in one file. Its score mixes them, so it is close to meaningless.
  Split before triaging.
* **A thesis** (`klein-…`, `malkin-…`) is one coherent work whose chapters each
  carry their own furniture. The score is fine; only the section-count signal
  is misleading. No split needed.

The detector cannot tell them apart — it counts furniture, not authorship —
so the flag means *check which of these it is*, not *split it*.

**Classified 2026-08-15: every currently flagged document was checked and
none needs splitting.** `scripts/split-bound-volume.py` was dry-run against
all of them and refused each one for want of a repeating masthead, which is
the mark of a published issue. Spot-checked the largest,
`arxiv-math-0203194v1` (256pp, 6 flags): it is the André–Baldassarri
Tôhoku-Hokkaido lecture volume — one coherent work whose chapters restart
their numbering, exactly the thesis-shaped false positive. `ant-v14-n7-s`
was the only genuine bound issue and is already split into its 10 papers.

## Ranking

| # | score | doc-id | fml | pp | title | strongest shared terms |
|---|---|---|---|---|---|---|
| 1 | 439.0 | [`arxiv-2604.16077v1`](../../library/arxiv-2604.16077v1/) | 31 | 66 | VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT | factor, weights, classical, parameter, limits |
| 2 | 429.5 | [`arxiv-1611.03697v5`](../../library/arxiv-1611.03697v5/) | 19 | 51 | RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND | uniqueness, data, symbols, sector, topological |
| 3 | 417.4 | [`arxiv-2208.13692v1`](../../library/arxiv-2208.13692v1/) | 30 | 38 | BRING’S CURVE: OLD AND NEW | data, bring, decomposition, parity, divisor |
| 4 | 411.4 | [`arxiv-1204.4824v2`](../../library/arxiv-1204.4824v2/) | 1 | 87 | Prepared for submission to JHEP Spectral networks | categorical, spectral, crossing, content, lifting |
| 5 | 409.5 | [`arxiv-0706.2213v3`](../../library/arxiv-0706.2213v3/) | 10 | 36 | NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS | table, trace, bridge, regularity, trefoil |
| 6 | 404.8 | [`arxiv-2008.09788v2`](../../library/arxiv-2008.09788v2/) | 29 | 31 | NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECT | eigenvalue, rigidity, field, reduction, residue |
| 7 | 388.6 | [`arxiv-1303.5278v1`](../../library/arxiv-1303.5278v1/) | 21 | 60 | 1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANI | decomposition, normal, trefoil, invariance, dual |
| 8 | 387.8 | [`arxiv-hep-th-0306165v1`](../../library/arxiv-hep-th-0306165v1/) | 0 | 67 | which has many interesting connections with three-dimensi onal quantum | physical, gravity, gauge, interpretation, field |
| 9 | 384.4 | [`arxiv-2301.02038v1`](../../library/arxiv-2301.02038v1/) | 22 | 26 | Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partia | prolongation, derivation, regularity, shift, cohomological |
| 10 | 377.7 | [`arxiv-2402.04839v2`](../../library/arxiv-2402.04839v2/) | 24 | 28 | On a volume invariant of 3–manifolds | table, borromean, surface, finiteness, topological |
| 11 | 372.7 | [`arxiv-1507.03238v3`](../../library/arxiv-1507.03238v3/) | 33 | 26 | TRIANGULATION INDEPENDENT PTOLEMY VARIETIES | obstruction, degeneracy, correspondence, coordinates, action |
| 12 | 344.2 | [`arxiv-1203.2182v1`](../../library/arxiv-1203.2182v1/) | 0 | 92 | Volume Conjecture: Reﬁned and Categoriﬁed | mass, gamma, braid, recursion, trefoil |
| 13 | 343.3 | [`arxiv-math-0506456v1`](../../library/arxiv-math-0506456v1/) | 29 | 70 | Journal of Knot Theory and Its Ramiﬁcations c© W orld Scientiﬁc Publis | bridge, classical, dilogarithm, leading, pair |
| 14 | 339.9 | [`arxiv-2203.17029v1`](../../library/arxiv-2203.17029v1/) | 22 | 65 | MODULAR q-HOLONOMIC MODULES | categorical, residue, operator, duality, identity |
| 15 | 338.3 | [`ihpmay2025`](../../library/ihpmay2025/) | 41 | 41 | IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY | stability, classification, density, cosh, conformal |
| 16 | 331.3 | [`arxiv-math-9907032v1`](../../library/arxiv-math-9907032v1/) | 33 | 27 | Mathematics Department, California Institute of Technolog y | flow, surface, computational, geometry, curvature |
| 17 | 314.1 | [`arxiv-1511.05628v1`](../../library/arxiv-1511.05628v1/) | 3 | 41 | QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY | data, derivation, feynman, level, invariance |
| 18 | 313.0 | [`arxiv-1512.04993v2`](../../library/arxiv-1512.04993v2/) | 0 | 70 | Complexity, action, and black holes | energy, shells, gate, equals, times |
| 19 | 301.3 | [`arxiv-2209.06973v1`](../../library/arxiv-2209.06973v1/) | 6 | 66 | On the geometry of two state models for the colored Jones polynomial | braid, ordering, correspondence, classical, geometry |
| 20 | 279.1 | [`arxiv-2111.04763v2`](../../library/arxiv-2111.04763v2/) | 5 | 59 | RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION | equals, habiro, block, connection, resummation |
| 21 | 275.2 | [`zagier-the-dilogarithm-function-copy-b`](../../library/zagier-the-dilogarithm-function-copy-b/) | 9 | 63 | The Dilogarithm Function Don Zagier | geometry, dilogarithm, information, functional, volumes |
| 22 | 254.5 | [`arxiv-2305.14884v2`](../../library/arxiv-2305.14884v2/) | 14 | 48 | PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS | data, fourier, integration, transform, invariance |
| 23 | 251.2 | [`arxiv-1203.6551v1`](../../library/arxiv-1203.6551v1/) | 19 | 25 | On the number of hyperbolic 3-manifolds of a given volume | crossing, volume, pair, primitive, shape |
| 24 | 245.6 | [`arxiv-2311.02632v2`](../../library/arxiv-2311.02632v2/) | 20 | 40 | SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE CHUL-HEE LEE | trace, eigenvalue, normal, surface, algebraic |
| 25 | 244.9 | [`arxiv-2410.14661v1`](../../library/arxiv-2410.14661v1/) | 33 | 62 | (r is odd). Contents 1. Introduction 2 2. Preliminaries 4 2.1. Definti | surface, geometry, identity, dilogarithm, volume |
| 26 | 233.1 | [`alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari`](../../library/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari/) | 1 | 40 | Communications in | observation, conformal, integration, dirac, derived |
| 27 | 223.0 | [`arxiv-0808.1533v1`](../../library/arxiv-0808.1533v1/) | 14 | 31 | On the third order helicity of magnetic ﬁelds on invariant domains in  | energy, factor, dual, always, bound |
| 28 | 222.6 | [`ki6c`](../../library/ki6c/) | 32 | 72 | On the asymptotic expansions of the Kashaev invariant of the knots wit | dilogarithm, crossings, symmetric, boundary, matrices |
| 29 | 216.0 | [`arxiv-hep-ph-0103325v4`](../../library/arxiv-hep-ph-0103325v4/) | 0 | 8 | Quantum algebras in phenomenological description of parti cle properti | mass, baryon, quark, realization, geometry |
| 30 | 214.3 | [`arxiv-2605.28781v1`](../../library/arxiv-2605.28781v1/) | 31 | 25 | THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS | field, fixed, fields, role, bound |
| 31 | 205.1 | [`arxiv-2109.04664v4`](../../library/arxiv-2109.04664v4/) | 13 | 27 | ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FI | integration, topological, figure-eight, boundary, jones |
| 32 | 201.7 | [`arxiv-1910.09966v1`](../../library/arxiv-1910.09966v1/) | 0 | 37 | Braids, 3-manifolds, elementary particles: number theory and symmetry  | particle, gauge, fields, bundle, charge |
| 33 | 201.6 | [`gt-v10-n3-p07-p`](../../library/gt-v10-n3-p07-p/) | 11 | 28 | Stabilization in the braid groups II: Transversal simplicity of knots  | braid, braids, full, problems, pair |
| 34 | 200.8 | [`arxiv-hep-th-0206161v1`](../../library/arxiv-hep-th-0206161v1/) | 0 | 31 | SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING Nikita A. Nekrasov | data, brane, field, reduction, instanton |
| 35 | 199.7 | [`arxiv-2412.02281v1`](../../library/arxiv-2412.02281v1/) | 43 | 28 | u + A | parameter, evaluation, convergence, limit, connection |
| 36 | 198.6 | [`arxiv-1810.11563v1`](../../library/arxiv-1810.11563v1/) | 0 | 84 | Three Lectures on Complexity and Black Holes Leonard Susskind | interpretation, time, correspondence, dual, role |
| 37 | 186.2 | [`arxiv-1301.4504v4`](../../library/arxiv-1301.4504v4/) | 0 | 66 | Prepared for submission to JHEP DEDICATED TO JOHN PRESKILL ON THE OCCA | brane, correction, transition, time, computational |
| 38 | 177.6 | [`arxiv-2302.05903v2`](../../library/arxiv-2302.05903v2/) | 0 | 15 | On combinatorial generalization(s) of Borel transform: Averaging metho | derivation, integration, transform, coefficients, strong |
| 39 | 177.2 | [`arxiv-2312.00624v1`](../../library/arxiv-2312.00624v1/) | 0 | 43 | On the structure of wave functions in complex Chern–Simons theory | classical, evaluation, factorization, quantum, q-difference |
| 40 | 176.1 | [`invariant-eigendistributions-2`](../../library/invariant-eigendistributions-2/) | 3 | 33 | REPRESENTATIONS OF WEYL GROUPS 1 Invariant eigendistributions on a sem | character, harmonic, orbital, dimension, groups |
| 41 | 170.3 | [`arxiv-1908.07065v3`](../../library/arxiv-1908.07065v3/) | 0 | 47 | Prepared for submission to JHEP Non-perturbative approaches to the qua | derivation, coupling, topological, instanton, calculus |
| 42 | 170.2 | [`arxiv-2208.14188v2`](../../library/arxiv-2208.14188v2/) | 0 | 46 | Prepared for submission to JHEP KIAS-P22064 Resurgence in complex Cher | level, limit, levels, zeros, invariants |
| 43 | 168.7 | [`9-81`](../../library/9-81/) | 15 | 7 | Singular Euclidean Structures on a Simplicial Complex with Weighted Ed | surface, dual, weight, parallel, program |
| 44 | 168.5 | [`arxiv-1101.1563v1`](../../library/arxiv-1101.1563v1/) | 7 | 20 | Gr¨ obner-Shirshov bases for categories∗ L. A. Bokut † | uniqueness, object, shirshov, bases, algebras |
| 45 | 166.1 | [`arxiv-2601.15862v1`](../../library/arxiv-2601.15862v1/) | 18 | 16 | SYNTHETIC DIFFERENTIAL JET BUNDLES ARE REDUCED | plain, functor, differential, limit, full |
| 46 | 164.3 | [`arxiv-1809.08419v1`](../../library/arxiv-1809.08419v1/) | 24 | 14 | GR ¨OBNER-SHIRSHOV BASES FOR NON-CRYST ALLOGRAPHIC COXETER GROUPS | table, bases, normal, coxeter, term |
| 47 | 161.3 | [`arxiv-1504.07260v3`](../../library/arxiv-1504.07260v3/) | 0 | 56 | Prepared for submission to JHEP Fricke S-duality in CHL models Daniel  | self-duality, level, topological, duality, connection |
| 48 | 159.9 | [`arxiv-2302.08363v2`](../../library/arxiv-2302.08363v2/) | 0 | 35 | Prepared for submission to JHEP On the structure of trans-series in qu | sigma, energy, field, recursive, problems |
| 49 | 155.4 | [`1172-5`](../../library/1172-5/) | 0 | 10 | OPTIMISTIC CALCULATIONS ABOUT THE $\mathrm{W}\mathrm{I}\mathrm{T}\math | mathrm, tilde, ldots, infty, algebraic |
| 50 | 154.9 | [`0306345v1`](../../library/0306345v1/) | 5 | 20 | Published: 16 June 2003 Skein-theoretical derivation of some formulas  | skein, derivation, habiro, recursion, calculus |
| 51 | 151.1 | [`arxiv-hep-th-0001202v2`](../../library/arxiv-hep-th-0001202v2/) | 1 | 21 | Towards cohomology of renormalization: bigrading the combinatorial Hop | table, hopf, weight, grading, full |
| 52 | 149.1 | [`arxiv-0901.1612v1`](../../library/arxiv-0901.1612v1/) | 4 | 23 | TRIPLE LINKING NUMBERS, AMBIGUOUS HOPF INV ARIANTS | hopf, scalar, linking, laplacian, characteristic |
| 53 | 147.4 | [`bsmf-2002-130-3-457-0`](../../library/bsmf-2002-130-3-457-0/) | 28 | 35 | 3 .W e c l a s s i f y h y p e r i d e a l p o l y h e d r a , u p t o | rigidity, dual, convergence, limit, local |
| 54 | 144.9 | [`arxiv-1704.01735v4`](../../library/arxiv-1704.01735v4/) | 15 | 39 | Modular curves, invariant theory and E8 Lei Yang | bring, level, surface, modular, polynomials |
| 55 | 144.9 | [`arxiv-math-ph-0105039v1`](../../library/arxiv-math-ph-0105039v1/) | 0 | 31 | December 23, 2000 (Revised Edition) Hyperbolic Structure Arising from  | braid, classical, surface, operator, dilogarithm |
| 56 | 142.9 | [`stateintegralsqseries`](../../library/stateintegralsqseries/) | 2 | 16 | FROM STATE INTEGRALS TO q-SERIES | residue, computation, state, knots, knot |
| 57 | 139.3 | [`s40687-023-00400-3`](../../library/s40687-023-00400-3/) | 3 | 23 | bonn.mpg.de/stavros 2MaxPlanckInstitutefor Mathematics,Bonn,Germany Fu | loop, matrices, polynomials, twisted, matrix |
| 58 | 139.2 | [`arxiv-2002.07369v2`](../../library/arxiv-2002.07369v2/) | 17 | 14 | GR¨OBNER-SHIRSHOV BASES FOR THE COXETER GROUPS OF THE TYPESG 2,F 4,E 6 | endomorphism, shirshov, bases, coxeter, finite |
| 59 | 137.4 | [`1-s20-s009731651830061x-main`](../../library/1-s20-s009731651830061x-main/) | 21 | 45 | Journal of Combinatorial Theory, Series A 158 (2018) 560–604 Contents  | weight, term, symmetric, numbers, strictly |
| 60 | 136.7 | [`arxiv-2109.00379v1`](../../library/arxiv-2109.00379v1/) | 4 | 23 | TWISTED NEUMANN–ZAGIER MATRICES | loop, matrices, polynomials, twisted, matrix |
| 61 | 135.9 | [`arxiv-2401.04019v1`](../../library/arxiv-2401.04019v1/) | 7 | 21 | TRUNCA TED THET A SERIES RELA TED TO THE JACOBI TRIPLE PRODUCT IDENTIT | theta, identity, product, distinct, states |
| 62 | 135.5 | [`cor-ma1`](../../library/cor-ma1/) | 19 | 26 | HAL is a multi-disciplinary open access archive for the deposit and di | operations, correspondence, frob, distinct, pair |
| 63 | 132.8 | [`arxiv-2605.15740v1`](../../library/arxiv-2605.15740v1/) | 22 | 26 | BAILEY P AIRS, EICHLER INTEGRALS AND UNIFIED WITTEN-RESHETIKHIN-TURAEV | unified, difference, limit, pair, primitive |
| 64 | 132.4 | [`1172-4`](../../library/1172-4/) | 0 | 26 | Notes on Construction of the Knot Invariant from $\mathrm{O}\mathrm{u} | mathrm, braid, dilogarithm, momentum, quantum |
| 65 | 127.6 | [`arxiv-1304.2705v1`](../../library/arxiv-1304.2705v1/) | 2 | 16 | FROM STATE INTEGRALS TO q-SERIES | residue, computation, state, knots, knot |
| 66 | 127.4 | [`arxiv-2302.04022v1`](../../library/arxiv-2302.04022v1/) | 32 | 27 | The second largest eigenvalue of normal Cayley graphs on symmetric gro | table, eigenvalue, normal, eigenvalues, groups |
| 67 | 123.4 | [`arxiv-2211.08164v2`](../../library/arxiv-2211.08164v2/) | 4 | 10 | INFINITELY MANY RIEMANN SURF ACES WITH A TRANSITIVE ACTION ON THE WEIE | surface, action, genus, characteristic, riemann |
| 68 | 122.3 | [`arxiv-1808.05026v1`](../../library/arxiv-1808.05026v1/) | 10 | 9 | GR ¨OBNER-SHIRSHOV BASES FOR TEMPERLEY-LIEB ALGEBRAS OF | bases, normal, algebras, product, term |
| 69 | 120.5 | [`arxiv-1909.06744v1`](../../library/arxiv-1909.06744v1/) | 7 | 25 | Springer correspondence for symmetric spaces Toshiaki Shoji | correspondence, stable, lusztig, pair, levi |
| 70 | 119.6 | [`arxiv-hep-th-9308100v1`](../../library/arxiv-hep-th-9308100v1/) | 0 | 22 | Department of Physics | horizon, entropy, time, information, reversal |
| 71 | 119.3 | [`arxiv-math-0502543v2`](../../library/arxiv-math-0502543v2/) | 13 | 12 | CONTINUITY OF VOLUMES – ON A GENERALIZATION OF A CONJECTURE OF J.W.MIL | decomposition, volume, volumes, cell, angle |
| 72 | 119.0 | [`ds15v1-2008`](../../library/ds15v1-2008/) | 2 | 59 | Mathematics Subject Classi cation: 33D15, 05A17, 05A19, 11B65, 11P81 | duality, theta, identity, product, euler |
| 73 | 117.0 | [`arxiv-2507.13873v1`](../../library/arxiv-2507.13873v1/) | 0 | 44 | Probing the singularity at the holographic screen via q-holography And | regime, gravity, sinh, classical, quantum |
| 74 | 116.0 | [`arxiv-2009.03688v6`](../../library/arxiv-2009.03688v6/) | 17 | 48 | E8-singularity, invariant theory and modular forms Lei Yang | decomposition, distinct, modular, forms, polynomials |
| 75 | 113.6 | [`arxiv-2402.08782v1`](../../library/arxiv-2402.08782v1/) | 4 | 12 | Hecke–Farey coordinates for Bring’s surface | hecke, bring, surface, coordinates, universal |
| 76 | 107.1 | [`arxiv-2607.29018v1`](../../library/arxiv-2607.29018v1/) | 17 | 23 | The Aldous property for normal Cayley graphs on symmetric groups | spectral, normal, groups, symmetric, strictly |
| 77 | 105.8 | [`resur-and-mld-calc-d-sauzin-hal`](../../library/resur-and-mld-calc-d-sauzin-hal/) | 1 | 16 | HAL is a multi-disciplinary open access archive for the deposit and di | operator, mathematical, calculus, physics, operators |
| 78 | 104.5 | [`arxiv-1404.0331v1`](../../library/arxiv-1404.0331v1/) | 8 | 9 | THE STRONG AJ CONJECTURE FOR CABLES OF TORUS KNOTS ANH T. TRAN | recurrence, strong, jones, torus, knots |
| 79 | 101.2 | [`arxiv-q-alg-9608020v2`](../../library/arxiv-q-alg-9608020v2/) | 1 | 9 | ∂x i + (n −j)θ +u 1≤i,j ≤n D(u;θ)Pλ (x;θ) = ( ∏ (λ i + (n −i)θ +u) Pλ  | parameter, dimension, polynomials, skew, partition |
| 80 | 99.5 | [`arxiv-1803.04009v2`](../../library/arxiv-1803.04009v2/) | 0 | 59 | Prepared for submission to JHEP IPMU-18-0045 | topological, global, symmetry, knot, manifolds |

_Showing 80 of 134. Full data: `library/*/candidates.json`._
