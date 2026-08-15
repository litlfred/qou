# Uncited library documents — triage queue

**Generated** 2026-08-15 by `scripts/library-relevance-rank.py --write-triage`.
Regenerate rather than edit.

169 of 341 library documents carry no `library:` back-reference from
`content/schema/references.ts` — nothing in the bibliography points at them.
That is the backlog [`local/paper-relevance-triage`](../../.claude/skills/local/paper-relevance-triage.md)
exists to work; it was invisible until the sources were sectioned.

## How this is ranked

By **topical overlap with the qou corpus**, not by volume of extracted
material. An earlier pass ranked by formalizable-candidate count and put a
whole journal issue first — that measures how much formal content a document
*offers*, which is not the same question.

The vocabulary is derived from this corpus, not hand-supplied: every content-block
`title:` and `defines:` entry plus the notation register, yielding 2122 terms,
of which 1199 discriminate within the library. Weighting is library IDF times
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
| [`arxiv-math-0203194v1`](../../library/arxiv-math-0203194v1/) | 5 | 256 | Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkai |
| [`klein-few-body-systems-in-lattice-effective-field-theory-the`](../../library/klein-few-body-systems-in-lattice-effective-field-theory-the/) | 5 | 111 | Bonn, November 2018 |
| [`malkin-2021-galois-action-on-motivic-fundamental-groups-thes`](../../library/malkin-2021-galois-action-on-motivic-fundamental-groups-thes/) | 4 | 123 | ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponth |
| [`di-cairano-2022-j-phys-commun-6-015002`](../../library/di-cairano-2022-j-phys-commun-6-015002/) | 3 | 12 | Langevin equation in systems with also negative temperatures |

## Ranking

| # | score | doc-id | fml | pp | title | strongest shared terms |
|---|---|---|---|---|---|---|
| 1 | 650.7 | [`arxiv-math-0203194v1`](../../library/arxiv-math-0203194v1/) `!` | 91 | 256 | Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkai | table, tower, frobenius, archimedean, data |
| 2 | 436.7 | [`arxiv-2604.16077v1`](../../library/arxiv-2604.16077v1/) | 31 | 66 | VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT | factor, weights, classical, parameter, limits |
| 3 | 435.1 | [`arxiv-math-0611504v1`](../../library/arxiv-math-0611504v1/) | 28 | 40 | QUANTUM HYPERBOLIC GEOMETRY | ratio, trace, branching, functor, weights |
| 4 | 434.7 | [`klein-few-body-systems-in-lattice-effective-field-theory-the`](../../library/klein-few-body-systems-in-lattice-effective-field-theory-the/) `!` | 0 | 111 | Bonn, November 2018 | nuclear, coulomb, particle, status, nuclei |
| 5 | 427.6 | [`arxiv-1611.03697v5`](../../library/arxiv-1611.03697v5/) | 19 | 51 | RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND | uniqueness, data, symbols, sector, topological |
| 6 | 421.6 | [`reshetikhin-turaev`](../../library/reshetikhin-turaev/) | 2 | 26 | Commun. Math. Phys. 127, 1-26 (1990) Communications in Mathematical Ph | uniqueness, functor, hopf, enveloping, monoidal |
| 7 | 415.2 | [`arxiv-2208.13692v1`](../../library/arxiv-2208.13692v1/) | 30 | 38 | BRING’S CURVE: OLD AND NEW | data, bring, decomposition, parity, divisor |
| 8 | 410.1 | [`arxiv-1204.4824v2`](../../library/arxiv-1204.4824v2/) | 1 | 87 | Prepared for submission to JHEP Spectral networks | categorical, spectral, crossing, content, lifting |
| 9 | 405.7 | [`arxiv-0706.2213v3`](../../library/arxiv-0706.2213v3/) | 10 | 36 | NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS | table, trace, bridge, regularity, trefoil |
| 10 | 400.1 | [`arxiv-2008.09788v2`](../../library/arxiv-2008.09788v2/) | 29 | 31 | NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECT | eigenvalue, rigidity, reduction, field, residue |
| 11 | 387.9 | [`malkin-2021-galois-action-on-motivic-fundamental-groups-thes`](../../library/malkin-2021-galois-action-on-motivic-fundamental-groups-thes/) `!` | 58 | 123 | ThemainmotiveofthisthesisistostudytheactionofthemotivicGaloisgrouponth | depth, interpretation, motivic, base, weight |
| 12 | 386.6 | [`arxiv-1303.5278v1`](../../library/arxiv-1303.5278v1/) | 21 | 60 | 1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANI | decomposition, normal, trefoil, invariance, dual |
| 13 | 383.0 | [`nrarith`](../../library/nrarith/) | 29 | 38 | Arithmetic of Hyperbolic Manifolds | chain, trace, parameter, derived, algebras |
| 14 | 382.3 | [`arxiv-math-0604057v2`](../../library/arxiv-math-0604057v2/) | 29 | 19 | VOLUME CONJECTURE, REGULA TOR AND SL2(C)-CHARACTER V ARIETY OF A KNOT | exceptional, surface, bundle, character, instance |
| 15 | 381.3 | [`arxiv-hep-th-0306165v1`](../../library/arxiv-hep-th-0306165v1/) | 0 | 67 | which has many interesting connections with three-dimensi onal quantum | physical, gravity, gauge, interpretation, field |
| 16 | 379.8 | [`arxiv-2301.02038v1`](../../library/arxiv-2301.02038v1/) | 22 | 26 | Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partia | prolongation, derivation, regularity, shift, cohomological |
| 17 | 373.7 | [`arxiv-2402.04839v2`](../../library/arxiv-2402.04839v2/) | 24 | 28 | On a volume invariant of 3–manifolds | table, borromean, surface, finiteness, topological |
| 18 | 370.3 | [`arxiv-1507.03238v3`](../../library/arxiv-1507.03238v3/) | 33 | 26 | TRIANGULATION INDEPENDENT PTOLEMY VARIETIES | obstruction, degeneracy, correspondence, coordinates, action |
| 19 | 356.3 | [`arxiv-hep-th-0006156v1`](../../library/arxiv-hep-th-0006156v1/) | 0 | 20 | STRONGL Y COUPLED QUANTUM DISCRETE LIOUVILLE | data, involution, shift, factor, fourier |
| 20 | 351.1 | [`modularqholonomicmodules`](../../library/modularqholonomicmodules/) | 23 | 66 | MODULAR q-HOLONOMIC MODULES | categorical, residue, operator, duality, identity |
| 21 | 347.1 | [`arxiv-math-0305275v1`](../../library/arxiv-math-0305275v1/) | 52 | 38 | Hyperbolic volume of representations of fundamental groups of cusped 3 | chain, rigidity, classical, operator, topological |
| 22 | 343.9 | [`arxiv-1704.02352v2`](../../library/arxiv-1704.02352v2/) | 18 | 43 | GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS | content, plancherel, conditional, probability, check |
| 23 | 340.3 | [`arxiv-1203.2182v1`](../../library/arxiv-1203.2182v1/) | 0 | 92 | Volume Conjecture: Reﬁned and Categoriﬁed | mass, gamma, braid, recursion, trefoil |
| 24 | 340.2 | [`arxiv-math-0506456v1`](../../library/arxiv-math-0506456v1/) | 29 | 70 | Journal of Knot Theory and Its Ramiﬁcations c© W orld Scientiﬁc Publis | bridge, classical, dilogarithm, leading, pair |
| 25 | 333.0 | [`arxiv-2203.17029v1`](../../library/arxiv-2203.17029v1/) | 22 | 65 | MODULAR q-HOLONOMIC MODULES | categorical, residue, operator, duality, identity |
| 26 | 331.3 | [`ihpmay2025`](../../library/ihpmay2025/) | 41 | 41 | IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY | stability, classification, density, cosh, conformal |
| 27 | 328.0 | [`arxiv-2510.04782v2`](../../library/arxiv-2510.04782v2/) | 15 | 82 | q-Hodge complexes over the Habiro ring Ferdinand Wagner | fibre, filtration, observation, descent, convention |
| 28 | 327.2 | [`arxiv-math-9907032v1`](../../library/arxiv-math-9907032v1/) | 33 | 27 | Mathematics Department, California Institute of Technolog y | flow, surface, computational, geometry, curvature |
| 29 | 316.2 | [`arxiv-math-0304010v1`](../../library/arxiv-math-0304010v1/) | 38 | 49 | KEROV’S CENTRAL LIMIT THEOREM FOR THE PLANCHEREL MEASURE ON YOUNG DIAG | mass, equals, plancherel, transition, correspondence |
| 30 | 312.3 | [`lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3`](../../library/lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3/) | 35 | 24 | Acta Mathematica Sinica, English Series 1999, July, Vol.15, No.3, p. 2 | fixed, residue, limits, coefficients, recursive |
| 31 | 311.8 | [`arxiv-1512.04993v2`](../../library/arxiv-1512.04993v2/) | 0 | 70 | Complexity, action, and black holes | energy, shells, gate, equals, times |
| 32 | 310.6 | [`arxiv-1511.05628v1`](../../library/arxiv-1511.05628v1/) | 3 | 41 | QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY | data, derivation, feynman, level, invariance |
| 33 | 299.1 | [`arxiv-2209.06973v1`](../../library/arxiv-2209.06973v1/) | 6 | 66 | On the geometry of two state models for the colored Jones polynomial | braid, ordering, correspondence, classical, evaluation |
| 34 | 292.6 | [`arxiv-hep-th-9408099v1`](../../library/arxiv-hep-th-9408099v1/) | 0 | 88 | E. Witten Institute for Advanced Study | mass, energy, scale, classical, coupling |
| 35 | 274.2 | [`arxiv-2111.04763v2`](../../library/arxiv-2111.04763v2/) | 5 | 59 | RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION | equals, habiro, block, connection, resummation |
| 36 | 271.0 | [`zagier-the-dilogarithm-function-copy-b`](../../library/zagier-the-dilogarithm-function-copy-b/) | 9 | 63 | The Dilogarithm Function Don Zagier | geometry, dilogarithm, information, functional, volumes |
| 37 | 268.0 | [`arxiv-1811.05376v4`](../../library/arxiv-1811.05376v4/) | 10 | 40 | Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology  | decay, decomposition, transform, invariance, coefficients |
| 38 | 263.2 | [`cspaper`](../../library/cspaper/) | 11 | 29 | Combinatorics of Triangulations and the Chern-Simons Invariant for Hyp | cohomological, interpretation, parity, topological, check |
| 39 | 260.8 | [`arxiv-2605.22763v1`](../../library/arxiv-2605.22763v1/) | 19 | 59 | 2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof S | selection, text, lean, count, light |
| 40 | 260.4 | [`arxiv-hep-th-9811173v1`](../../library/arxiv-hep-th-9811173v1/) | 0 | 54 | b vol(M) = (−D)3/ 2 (2π)2n− 4 ζK(2) 2ζ(2) for a manifold M whose invar | crossing, zeta, trace, feynman, precision |
| 41 | 257.9 | [`maximal-hoermander-q-var-revised-v03`](../../library/maximal-hoermander-q-var-revised-v03/) | 41 | 43 | HAL is a multi-disciplinary open access archive for the deposit and di | spectral, time, operator, harmonic, functional |
| 42 | 254.2 | [`poincare-proof-outline`](../../library/poincare-proof-outline/) | 0 | 175 | Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry | uniqueness, existence, axiom, interpretation, axioms |
| 43 | 252.1 | [`arxiv-2305.14884v2`](../../library/arxiv-2305.14884v2/) | 14 | 48 | PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS | data, fourier, integration, transform, invariance |
| 44 | 248.4 | [`arxiv-1203.6551v1`](../../library/arxiv-1203.6551v1/) | 19 | 25 | On the number of hyperbolic 3-manifolds of a given volume | crossing, volume, pair, primitive, shape |
| 45 | 244.4 | [`arxiv-2311.02632v2`](../../library/arxiv-2311.02632v2/) | 20 | 40 | SPECTRUM OF THE LAPLACIAN ON THE FRICKE-MACBEATH SURFACE CHUL-HEE LEE | trace, eigenvalue, normal, surface, algebraic |
| 46 | 243.8 | [`arxiv-1906.12122v2`](../../library/arxiv-1906.12122v2/) | 0 | 76 | Nuclear eﬀective ﬁeld theory: status and perspectives H.-W. Hammer∗ In | neutron, nuclear, status, quark, amplitude |
| 47 | 243.3 | [`arxiv-2410.14661v1`](../../library/arxiv-2410.14661v1/) | 33 | 62 | (r is odd). Contents 1. Introduction 2 2. Preliminaries 4 2.1. Definti | surface, geometry, identity, dilogarithm, volume |
| 48 | 231.5 | [`alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari`](../../library/alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari/) | 1 | 40 | Communications in | observation, conformal, integration, dirac, invariance |
| 49 | 230.3 | [`arxiv-math-0411505v2`](../../library/arxiv-math-0411505v2/) | 26 | 22 | A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION | zeta, rotation, correspondence, computational, quantum |
| 50 | 222.7 | [`arxiv-0808.1533v1`](../../library/arxiv-0808.1533v1/) | 14 | 31 | On the third order helicity of magnetic ﬁelds on invariant domains in  | energy, factor, dual, always, bound |
| 51 | 221.6 | [`ki6c`](../../library/ki6c/) | 32 | 72 | On the asymptotic expansions of the Kashaev invariant of the knots wit | dilogarithm, crossings, symmetric, boundary, matrices |
| 52 | 213.5 | [`arxiv-hep-ph-0103325v4`](../../library/arxiv-hep-ph-0103325v4/) | 0 | 8 | Quantum algebras in phenomenological description of parti cle properti | mass, baryon, quark, realization, algebras |
| 53 | 211.5 | [`arxiv-math-0305423v3`](../../library/arxiv-math-0305423v3/) | 16 | 19 | Stein’s Method and Plancherel Measure of the Symmetric Group | plancherel, operator, character, bound, harmonic |
| 54 | 210.3 | [`arxiv-q-alg-9504015v2`](../../library/arxiv-q-alg-9504015v2/) | 15 | 33 | Witten’s Invariants of Rational Homology Spheres at Prime | cyclotomic, ring, bound, loop, link |
| 55 | 209.1 | [`arxiv-math-0006111v2`](../../library/arxiv-math-0006111v2/) | 8 | 12 | APPROXIMA TE F ACTORIZA TION AND CONCENTRA TION FOR CHARACTERS OF SYMM | markov, trace, weight, factorization, action |
| 56 | 208.6 | [`arxiv-2605.28781v1`](../../library/arxiv-2605.28781v1/) | 31 | 25 | THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS | fixed, field, fields, role, bound |
| 57 | 203.6 | [`arxiv-2109.04664v4`](../../library/arxiv-2109.04664v4/) | 13 | 27 | ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FI | integration, topological, figure-eight, boundary, torus |
| 58 | 199.9 | [`arxiv-1910.09966v1`](../../library/arxiv-1910.09966v1/) | 0 | 37 | Braids, 3-manifolds, elementary particles: number theory and symmetry  | particle, gauge, fields, bundle, charge |
| 59 | 198.5 | [`arxiv-hep-th-0206161v1`](../../library/arxiv-hep-th-0206161v1/) | 0 | 31 | SEIBERG-WITTEN PREPOTENTIAL FROM INSTANTON COUNTING Nikita A. Nekrasov | data, brane, reduction, field, instanton |
| 60 | 197.8 | [`arxiv-1810.11563v1`](../../library/arxiv-1810.11563v1/) | 0 | 84 | Three Lectures on Complexity and Black Holes Leonard Susskind | interpretation, time, correspondence, dual, role |
| 61 | 196.6 | [`gt-v10-n3-p07-p`](../../library/gt-v10-n3-p07-p/) | 11 | 28 | Stabilization in the braid groups II: Transversal simplicity of knots  | braid, braids, full, problems, pair |
| 62 | 195.0 | [`arxiv-2412.02281v1`](../../library/arxiv-2412.02281v1/) | 43 | 28 | u + A | parameter, evaluation, convergence, limit, connection |
| 63 | 194.0 | [`arxiv-2402.01890v4`](../../library/arxiv-2402.01890v4/) | 21 | 27 | On the spherical partition algebra | decomposition, truncation, duality, pair, schur-weyl |
| 64 | 185.0 | [`arxiv-1301.4504v4`](../../library/arxiv-1301.4504v4/) | 0 | 66 | Prepared for submission to JHEP DEDICATED TO JOHN PRESKILL ON THE OCCA | brane, correction, transition, time, computational |
| 65 | 175.5 | [`arxiv-2302.05903v2`](../../library/arxiv-2302.05903v2/) | 0 | 15 | On combinatorial generalization(s) of Borel transform: Averaging metho | derivation, integration, transform, coefficients, strong |
| 66 | 175.4 | [`arxiv-hep-th-9306069v2`](../../library/arxiv-hep-th-9306069v2/) | 0 | 48 | Department of Physics | gravity, horizon, entropy, classical, information |
| 67 | 174.6 | [`arxiv-2312.00624v1`](../../library/arxiv-2312.00624v1/) | 0 | 43 | On the structure of wave functions in complex Chern–Simons theory | classical, evaluation, factorization, quantum, q-difference |
| 68 | 172.6 | [`arxiv-math-0104249v1`](../../library/arxiv-math-0104249v1/) | 21 | 16 | IRRA TIONALITY OF V ALUES OF ZET A-FUNCTION W. Zudilin 1. Introduction | independence, forms, construction, condition, linear |
| 69 | 171.5 | [`invariant-eigendistributions-2`](../../library/invariant-eigendistributions-2/) | 3 | 33 | REPRESENTATIONS OF WEYL GROUPS 1 Invariant eigendistributions on a sem | character, harmonic, orbital, dimension, groups |
| 70 | 169.7 | [`arxiv-1908.07065v3`](../../library/arxiv-1908.07065v3/) | 0 | 47 | Prepared for submission to JHEP Non-perturbative approaches to the qua | derivation, coupling, topological, instanton, strong |
| 71 | 168.7 | [`9-81`](../../library/9-81/) | 15 | 7 | Singular Euclidean Structures on a Simplicial Complex with Weighted Ed | surface, dual, weight, parallel, program |
| 72 | 167.7 | [`arxiv-1101.1563v1`](../../library/arxiv-1101.1563v1/) | 7 | 20 | Gr¨ obner-Shirshov bases for categories∗ L. A. Bokut † | uniqueness, object, shirshov, bases, algebras |
| 73 | 167.6 | [`arxiv-2208.14188v2`](../../library/arxiv-2208.14188v2/) | 0 | 46 | Prepared for submission to JHEP KIAS-P22064 Resurgence in complex Cher | level, limit, levels, zeros, stokes |
| 74 | 165.2 | [`arxiv-2601.15862v1`](../../library/arxiv-2601.15862v1/) | 18 | 16 | SYNTHETIC DIFFERENTIAL JET BUNDLES ARE REDUCED | plain, functor, differential, limit, full |
| 75 | 163.9 | [`arxiv-1809.08419v1`](../../library/arxiv-1809.08419v1/) | 24 | 14 | GR ¨OBNER-SHIRSHOV BASES FOR NON-CRYST ALLOGRAPHIC COXETER GROUPS | table, bases, normal, coxeter, term |
| 76 | 163.5 | [`gn2`](../../library/gn2/) | 11 | 11 | ning polynomial of the SL(2;C)-character variety of the twist knot. 1. | character, ring, factorization, action, genus |
| 77 | 159.4 | [`arxiv-1504.07260v3`](../../library/arxiv-1504.07260v3/) | 0 | 56 | Prepared for submission to JHEP Fricke S-duality in CHL models Daniel  | self-duality, level, topological, duality, connection |
| 78 | 159.1 | [`arxiv-2302.08363v2`](../../library/arxiv-2302.08363v2/) | 0 | 35 | Prepared for submission to JHEP On the structure of trans-series in qu | sigma, energy, field, recursive, problems |
| 79 | 154.3 | [`1172-5`](../../library/1172-5/) | 0 | 10 | OPTIMISTIC CALCULATIONS ABOUT THE $\mathrm{W}\mathrm{I}\mathrm{T}\math | mathrm, tilde, ldots, infty, algebraic |
| 80 | 152.0 | [`0306345v1`](../../library/0306345v1/) | 5 | 20 | Published: 16 June 2003 Skein-theoretical derivation of some formulas  | skein, derivation, habiro, recursion, calculus |

_Showing 80 of 169. Full data: `library/*/candidates.json`._
