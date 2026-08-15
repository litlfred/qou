# Uncited library documents — triage queue

**Generated** 2026-08-15 by `scripts/library-relevance-rank.py --write-triage`.
Regenerate rather than edit.

202 of 341 library documents carry no `library:` back-reference from
`content/schema/references.ts` — nothing in the bibliography points at them.
That is the backlog [`local/paper-relevance-triage`](../../.claude/skills/local/paper-relevance-triage.md)
exists to work; it was invisible until the sources were sectioned.

## How this is ranked

By **topical overlap with the qou corpus**, not by volume of extracted
material. An earlier pass ranked by formalizable-candidate count and put a
whole journal issue first — that measures how much formal content a document
*offers*, which is not the same question.

The vocabulary is derived from this corpus, not hand-supplied: every content-block
`title:` and `defines:` entry plus the notation register, yielding 2110 terms,
of which 1190 discriminate within the library. Weighting is library IDF times
corpus frequency: a term must be both rare in the library and central here, so
neither a ubiquitous word nor a rare-but-alien one scores. Scoring reads each
document's extracted *claims*
(`candidates.json`) plus its title and section titles — not its prose — so a
passing mention in a bibliography does not inflate a score.

**The score is a prior, not a verdict.** It says "this document is written in our
vocabulary", which is where triage should start, not where it should end.

## Bound volumes (4 flagged)

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

| doc-id | Intro/Ref sections | pp | title |
|---|---|---|---|
| [`arxiv-math-0203194v1`](../../library/arxiv-math-0203194v1/) | 6 | 256 | Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkai |
| [`klein-few-body-systems-in-lattice-effective-field-theory-the`](../../library/klein-few-body-systems-in-lattice-effective-field-theory-the/) | 5 | 111 | Few-Body Systems in Lattice Eﬀective Field Theory Dissertation zur Erl |
| [`malkin-2021-galois-action-on-motivic-fundamental-groups-thes`](../../library/malkin-2021-galois-action-on-motivic-fundamental-groups-thes/) | 4 | 123 |  |
| [`di-cairano-2022-j-phys-commun-6-015002`](../../library/di-cairano-2022-j-phys-commun-6-015002/) | 3 | 12 | Journal of Physics Communications PAPER • OPEN ACCESS On the derivatio |

## Ranking

| # | score | doc-id | fml | pp | title | strongest shared terms |
|---|---|---|---|---|---|---|
| 1 | 650.1 | [`arxiv-math-0203194v1`](../../library/arxiv-math-0203194v1/) `!` | 91 | 256 | Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkai | table, tower, frobenius, archimedean, data |
| 2 | 432.7 | [`klein-few-body-systems-in-lattice-effective-field-theory-the`](../../library/klein-few-body-systems-in-lattice-effective-field-theory-the/) `!` | 0 | 111 | Few-Body Systems in Lattice Eﬀective Field Theory Dissertation zur Erl | nuclear, coulomb, particle, status, nuclei |
| 3 | 431.8 | [`arxiv-2604.16077v1`](../../library/arxiv-2604.16077v1/) | 31 | 66 | VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT | factor, weights, classical, parameter, limits |
| 4 | 431.2 | [`arxiv-math-0611504v1`](../../library/arxiv-math-0611504v1/) | 28 | 40 | QUANTUM HYPERBOLIC GEOMETRY | trace, ratio, branching, functor, weights |
| 5 | 421.4 | [`arxiv-0906.1500v4`](../../library/arxiv-0906.1500v4/) | 15 | 29 | TWISTED ALEXANDER INV ARIANT AND NON–ABELIAN REIDEMEISTER TORSION FOR  | never, involution, bridge, dual, topological |
| 6 | 420.9 | [`arxiv-1611.03697v5`](../../library/arxiv-1611.03697v5/) | 19 | 51 | RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND | uniqueness, data, symbols, sector, topological |
| 7 | 420.7 | [`arxiv-0905.0591v3`](../../library/arxiv-0905.0591v3/) | 37 | 42 | A SUR VEY OF TWISTED ALEXANDER POL YNOMIALS | bridge, hopf, factor, commutative, period |
| 8 | 420.2 | [`reshetikhin-turaev`](../../library/reshetikhin-turaev/) | 2 | 26 | Commun. Math. Phys. 127, 1-26 (1990) Communications in Mathematical Ph | uniqueness, hopf, functor, enveloping, monoidal |
| 9 | 412.4 | [`arxiv-2208.13692v1`](../../library/arxiv-2208.13692v1/) | 30 | 38 | BRING’S CURVE: OLD AND NEW | data, bring, decomposition, parity, divisor |
| 10 | 408.7 | [`arxiv-1204.4824v2`](../../library/arxiv-1204.4824v2/) | 1 | 87 | Prepared for submission to JHEP Spectral networks | categorical, spectral, crossing, content, lifting |
| 11 | 402.0 | [`arxiv-0706.2213v3`](../../library/arxiv-0706.2213v3/) | 10 | 36 | NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS | table, trace, bridge, regularity, trefoil |
| 12 | 397.2 | [`arxiv-2008.09788v2`](../../library/arxiv-2008.09788v2/) | 29 | 31 | NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECT | eigenvalue, rigidity, reduction, field, residue |
| 13 | 385.0 | [`arxiv-1303.5278v1`](../../library/arxiv-1303.5278v1/) | 21 | 60 | 1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANI | decomposition, normal, trefoil, dual, invariance |
| 14 | 383.6 | [`malkin-2021-galois-action-on-motivic-fundamental-groups-thes`](../../library/malkin-2021-galois-action-on-motivic-fundamental-groups-thes/) `!` | 58 | 123 | _(none extracted)_ | depth, interpretation, motivic, base, weight |
| 15 | 379.1 | [`arxiv-math-0604057v2`](../../library/arxiv-math-0604057v2/) | 29 | 19 | VOLUME CONJECTURE, REGULA TOR AND SL2(C)-CHARACTER V ARIETY OF A KNOT | exceptional, surface, bundle, character, instance |
| 16 | 378.2 | [`nrarith`](../../library/nrarith/) | 29 | 38 | Arithmetic of Hyperbolic Manifolds | chain, trace, parameter, derived, algebras |
| 17 | 374.0 | [`arxiv-2301.02038v1`](../../library/arxiv-2301.02038v1/) | 22 | 26 | Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partia | derivation, prolongation, regularity, shift, cohomological |
| 18 | 373.2 | [`arxiv-hep-th-0306165v1`](../../library/arxiv-hep-th-0306165v1/) | 0 | 67 | Three-Dimensional Quantum Gravity | physical, gravity, gauge, interpretation, field |
| 19 | 371.6 | [`afst-2007-6-16-3-665-0`](../../library/afst-2007-6-16-3-665-0/) | 31 | 55 | ANNALES DE LA FACULTÉ DES SCIENCES Mathématiques | data, observation, descent, functor, topological |
| 20 | 369.7 | [`arxiv-2402.04839v2`](../../library/arxiv-2402.04839v2/) | 24 | 28 | On a volume invariant of 3–manifolds | table, borromean, surface, finiteness, topological |
| 21 | 368.9 | [`arxiv-1507.03238v3`](../../library/arxiv-1507.03238v3/) | 33 | 26 | TRIANGULATION INDEPENDENT PTOLEMY VARIETIES | obstruction, degeneracy, correspondence, coordinates, action |
| 22 | 353.0 | [`arxiv-hep-th-0006156v1`](../../library/arxiv-hep-th-0006156v1/) | 0 | 20 | STRONGL Y COUPLED QUANTUM DISCRETE LIOUVILLE | data, involution, shift, factor, fourier |
| 23 | 352.5 | [`0504116v2`](../../library/0504116v2/) | 31 | 24 | On deformations of hyperbolic 3–manifolds with geodesic boundary ROBER | completeness, lifting, pairing, exceptional, rigidity |
| 24 | 349.0 | [`modularqholonomicmodules`](../../library/modularqholonomicmodules/) | 23 | 66 | MODULAR q-HOLONOMIC MODULES | categorical, residue, operator, duality, identity |
| 25 | 343.1 | [`arxiv-1704.02352v2`](../../library/arxiv-1704.02352v2/) | 18 | 43 | GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS | content, plancherel, conditional, probability, check |
| 26 | 342.5 | [`arxiv-1203.2182v1`](../../library/arxiv-1203.2182v1/) | 0 | 92 | Volume Conjecture: Reﬁned and Categoriﬁed | mass, gamma, braid, recursion, trefoil |
| 27 | 336.4 | [`arxiv-math-0506456v1`](../../library/arxiv-math-0506456v1/) | 29 | 70 | Journal of Knot Theory and Its Ramiﬁcations c© W orld Scientiﬁc Publis | bridge, classical, dilogarithm, leading, pair |
| 28 | 334.4 | [`arxiv-math-0305275v1`](../../library/arxiv-math-0305275v1/) | 52 | 38 | Hyperbolic volume of representations of fundamental groups of cusped 3 | chain, rigidity, classical, operator, topological |
| 29 | 331.1 | [`arxiv-2203.17029v1`](../../library/arxiv-2203.17029v1/) | 22 | 65 | MODULAR q-HOLONOMIC MODULES | categorical, residue, operator, duality, identity |
| 30 | 326.7 | [`arxiv-2510.04782v2`](../../library/arxiv-2510.04782v2/) | 15 | 82 | q-Hodge complexes over the Habiro ring Ferdinand Wagner | fibre, filtration, observation, descent, convention |
| 31 | 325.3 | [`arxiv-math-9907032v1`](../../library/arxiv-math-9907032v1/) | 33 | 27 | Combinatorial optimization in geometry 1 | flow, surface, computational, vertex, curvature |
| 32 | 319.6 | [`ihpmay2025`](../../library/ihpmay2025/) | 41 | 41 | IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY | stability, classification, density, cosh, conformal |
| 33 | 318.2 | [`arxiv-1002.0126v1`](../../library/arxiv-1002.0126v1/) | 9 | 39 | AN INTRODUCTION TO THE VOLUME CONJECTURE HITOSHI MURAKAMI | skein, descent, closure, braid, interpretation |
| 34 | 315.7 | [`arxiv-math-0304010v1`](../../library/arxiv-math-0304010v1/) | 38 | 49 | KEROV’S CENTRAL LIMIT THEOREM FOR THE PLANCHEREL MEASURE ON YOUNG DIAG | mass, equals, plancherel, transition, correspondence |
| 35 | 311.3 | [`lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3`](../../library/lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3/) | 35 | 24 | Acta Mathematica Sinica, English Series 1999, July, Vol.15, No.3, p. 2 | fixed, residue, limits, coefficients, recursive |
| 36 | 308.1 | [`arxiv-1512.04993v2`](../../library/arxiv-1512.04993v2/) | 0 | 70 | Complexity, action, and black holes | energy, shells, gate, equals, times |
| 37 | 307.3 | [`arxiv-1106.6298v1`](../../library/arxiv-1106.6298v1/) | 11 | 18 | ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INV ARIANTS | frobenius, endomorphism, cyclotomic, habiro, laplace |
| 38 | 307.2 | [`arxiv-hep-th-9408099v1`](../../library/arxiv-hep-th-9408099v1/) | 0 | 88 | Monopoles, Duality and Chiral Symmetry Breaking in N=2 Supersymmetric  | mass, energy, scale, classical, coupling |
| 39 | 305.2 | [`arxiv-1511.05628v1`](../../library/arxiv-1511.05628v1/) | 3 | 41 | QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY | data, derivation, feynman, level, invariance |
| 40 | 297.1 | [`arxiv-2209.06973v1`](../../library/arxiv-2209.06973v1/) | 6 | 66 | On the geometry of two state models for the colored Jones polynomial | braid, ordering, correspondence, classical, evaluation |
| 41 | 290.5 | [`arxiv-1108.4389v1`](../../library/arxiv-1108.4389v1/) | 0 | 58 | Gauge Theories Labelled by Three-Manifolds | chain, gauge, operations, operator, interaction |
| 42 | 285.1 | [`arxiv-1202.4698v3`](../../library/arxiv-1202.4698v3/) | 0 | 32 | 6j symbols for the modular double, quantum hyperbolic geometry, and su | gamma, symbols, gauge, kernel, classical |
| 43 | 276.5 | [`angled-survey`](../../library/angled-survey/) | 30 | 24 | Contemporary Mathematics From angled triangulations to hyperbolic stru | close, rigidity, normal, surface, volume |
| 44 | 272.0 | [`arxiv-2111.04763v2`](../../library/arxiv-2111.04763v2/) | 5 | 59 | RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION | equals, habiro, block, connection, resummation |
| 45 | 267.3 | [`zagier-the-dilogarithm-function-copy-b`](../../library/zagier-the-dilogarithm-function-copy-b/) | 9 | 63 | The Dilogarithm Function Don Zagier | dilogarithm, information, functional, geometry, volumes |
| 46 | 265.9 | [`arxiv-1811.05376v4`](../../library/arxiv-1811.05376v4/) | 10 | 40 | Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology  | decay, decomposition, transform, invariance, coefficients |
| 47 | 263.0 | [`4geo-dedi-rev`](../../library/4geo-dedi-rev/) | 15 | 26 | HAL is a multi-disciplinary open access archive for the deposit and di | factor, classical, parameter, dual, coordinate |
| 48 | 259.8 | [`arxiv-2605.22763v1`](../../library/arxiv-2605.22763v1/) | 19 | 59 | 2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof S | selection, text, lean, count, light |
| 49 | 256.7 | [`cspaper`](../../library/cspaper/) | 11 | 29 | Combinatorics of Triangulations and the Chern-Simons Invariant for Hyp | cohomological, interpretation, parity, topological, check |
| 50 | 256.5 | [`maximal-hoermander-q-var-revised-v03`](../../library/maximal-hoermander-q-var-revised-v03/) | 41 | 43 | HAL is a multi-disciplinary open access archive for the deposit and di | spectral, time, operator, harmonic, functional |
| 51 | 252.7 | [`poincare-proof-outline`](../../library/poincare-proof-outline/) | 0 | 175 | Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry | uniqueness, existence, axiom, interpretation, axioms |
| 52 | 247.3 | [`arxiv-1203.6551v1`](../../library/arxiv-1203.6551v1/) | 19 | 25 | On the number of hyperbolic 3-manifolds of a given volume | crossing, volume, pair, primitive, shape |
| 53 | 246.1 | [`arxiv-2305.14884v2`](../../library/arxiv-2305.14884v2/) | 14 | 48 | PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS | data, fourier, integration, transform, invariance |
| 54 | 243.3 | [`arxiv-1906.12122v2`](../../library/arxiv-1906.12122v2/) | 0 | 76 | Nuclear eﬀective ﬁeld theory: status and perspectives H.-W. Hammer∗ In | neutron, nuclear, status, quark, amplitude |
| 55 | 242.1 | [`arxiv-2311.02632v2`](../../library/arxiv-2311.02632v2/) | 20 | 40 | SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE CHUL-HEE LEE | trace, eigenvalue, normal, surface, action |
| 56 | 240.7 | [`arxiv-2410.14661v1`](../../library/arxiv-2410.14661v1/) | 33 | 62 | ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RES | surface, identity, dilogarithm, volume, canonical |
| 57 | 229.6 | [`alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari`](../../library/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari/) | 1 | 40 | Communications in | observation, conformal, integration, dirac, finiteness |
| 58 | 229.0 | [`arxiv-hep-th-9811173v1`](../../library/arxiv-hep-th-9811173v1/) | 0 | 54 | Determinations of rational Dedekind-zeta invariants of hyperbolic mani | crossing, zeta, feynman, precision, figure-8 |
| 59 | 228.3 | [`arxiv-math-0411505v2`](../../library/arxiv-math-0411505v2/) | 26 | 22 | A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION | zeta, rotation, correspondence, computational, quantum |
| 60 | 221.9 | [`arxiv-0808.1533v1`](../../library/arxiv-0808.1533v1/) | 14 | 31 | On the third order helicity of magnetic ﬁelds on invariant domains in  | energy, factor, dual, always, bound |
| 61 | 221.1 | [`ki6c`](../../library/ki6c/) | 32 | 72 | On the asymptotic expansions of the Kashaev invariant of the knots wit | dilogarithm, crossings, symmetric, boundary, matrices |
| 62 | 216.2 | [`arxiv-1012.1039v2`](../../library/arxiv-1012.1039v2/) | 28 | 22 | SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS | chain, topological, duality, identity, bound |
| 63 | 212.1 | [`arxiv-hep-ph-0103325v4`](../../library/arxiv-hep-ph-0103325v4/) | 0 | 8 | Quantum algebras in phenomenological description of parti cle properti | mass, baryon, quark, realization, algebras |
| 64 | 211.2 | [`arxiv-math-0305423v3`](../../library/arxiv-math-0305423v3/) | 16 | 19 | Stein’s Method and Plancherel Measure of the Symmetric Group | plancherel, operator, character, bound, harmonic |
| 65 | 209.2 | [`arxiv-math-0006111v2`](../../library/arxiv-math-0006111v2/) | 8 | 12 | APPROXIMA TE F ACTORIZA TION AND CONCENTRA TION FOR CHARACTERS OF SYMM | markov, trace, weight, factorization, action |
| 66 | 208.7 | [`arxiv-q-alg-9504015v2`](../../library/arxiv-q-alg-9504015v2/) | 15 | 33 | Witten’s Invariants of Rational Homology Spheres at Prime | cyclotomic, ring, bound, loop, link |
| 67 | 208.2 | [`18`](../../library/18/) | 13 | 10 | Mathematical Research Letters3, 51–60 (1996) COMBINATORIAL SCALAR CURV | deformed, scale, conformal, scalar, mathematical |
| 68 | 207.1 | [`arxiv-2412.02281v1`](../../library/arxiv-2412.02281v1/) | 43 | 28 | Explicit evaluation of the q-Stokes matrices for certain conﬂuent hype | parameter, evaluation, limit, convergence, connection |
| 69 | 206.9 | [`arxiv-2605.28781v1`](../../library/arxiv-2605.28781v1/) | 31 | 25 | THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS | fixed, field, fields, role, bound |
| 70 | 201.9 | [`gt-v10-n3-p07-p`](../../library/gt-v10-n3-p07-p/) | 11 | 28 | Geometry & Topology 10 (2006) 1425–1452 1425 Stabilization in the brai | braid, braids, problems, pair, geometry |
| 71 | 201.3 | [`arxiv-2109.04664v4`](../../library/arxiv-2109.04664v4/) | 13 | 27 | ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FI | integration, topological, figure-eight, boundary, torus |
| 72 | 198.2 | [`arxiv-1910.09966v1`](../../library/arxiv-1910.09966v1/) | 0 | 37 | Braids, 3-manifolds, elementary particles: number theory and symmetry  | particle, gauge, fields, bundle, charge |
| 73 | 196.2 | [`arxiv-1810.11563v1`](../../library/arxiv-1810.11563v1/) | 0 | 84 | Three Lectures on Complexity and Black Holes Leonard Susskind | interpretation, time, correspondence, dual, role |
| 74 | 196.2 | [`arxiv-hep-th-0206161v1`](../../library/arxiv-hep-th-0206161v1/) | 0 | 31 | SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING Nikita A. Nekrasov | data, brane, reduction, field, instanton |
| 75 | 193.8 | [`arxiv-2402.01890v4`](../../library/arxiv-2402.01890v4/) | 21 | 27 | On the spherical partition algebra | decomposition, truncation, duality, pair, schur-weyl |
| 76 | 191.1 | [`0310280v4`](../../library/0310280v4/) | 11 | 28 | Stabilization in the braid groups II: Transversal simplicity of knots  | braid, braids, problems, pair, full |
| 77 | 190.3 | [`gn2`](../../library/gn2/) | 11 | 11 | SOME RESULTS ABOUT THE KAUFFMAN BRACKET SKEIN MODULE OF THE TWIST KNOT | skein, character, ring, factorization, action |
| 78 | 184.5 | [`arxiv-1301.4504v4`](../../library/arxiv-1301.4504v4/) | 0 | 66 | Prepared for submission to JHEP DEDICATED TO JOHN PRESKILL ON THE OCCA | brane, correction, transition, time, computational |
| 79 | 183.4 | [`agt-v12-n2-p04-s`](../../library/agt-v12-n2-p04-s/) | 3 | 14 | Algebraic & Geometric Topology 12 (2012) 791–804 791 The twisted Alexa | chain, decomposition, bases, observed, algebraic |
| 80 | 180.5 | [`arxiv-1108.5286v3`](../../library/arxiv-1108.5286v3/) | 19 | 39 | Hochschild homology of aﬃne Hecke algebras Maarten Solleveld Radboud U | hecke, fourier, reduction, parameter, transform |

_Showing 80 of 202. Full data: `library/*/candidates.json`._
