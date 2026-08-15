# Uncited library documents — triage queue

**Generated** 2026-08-15 by `scripts/library-relevance-rank.py --write-triage`.
Regenerate rather than edit.

248 of 341 library documents carry no `library:` back-reference from
`content/schema/references.ts` — nothing in the bibliography points at them.
That is the backlog [`local/paper-relevance-triage`](../../.claude/skills/local/paper-relevance-triage.md)
exists to work; it was invisible until the sources were sectioned.

## How this is ranked

By **topical overlap with the qou corpus**, not by volume of extracted
material. An earlier pass ranked by formalizable-candidate count and put a
whole journal issue first — that measures how much formal content a document
*offers*, which is not the same question.

The vocabulary is derived from this corpus, not hand-supplied: every content-block
`title:` and `defines:` entry plus the notation register, yielding 2094 terms,
of which 1175 discriminate within the library. Weighting is library IDF times
corpus frequency: a term must be both rare in the library and central here, so
neither a ubiquitous word nor a rare-but-alien one scores. Scoring reads each
document's extracted *claims*
(`candidates.json`) plus its title and section titles — not its prose — so a
passing mention in a bibliography does not inflate a score.

**The score is a prior, not a verdict.** It says "this document is written in our
vocabulary", which is where triage should start, not where it should end.

## Bound volumes (6 flagged)

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

| doc-id | Intro/Ref sections | pp | title |
|---|---|---|---|
| [`arxiv-math-0203194v1`](../../library/arxiv-math-0203194v1/) | 6 | 256 | Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkai |
| [`klein-few-body-systems-in-lattice-effective-field-theory-the`](../../library/klein-few-body-systems-in-lattice-effective-field-theory-the/) | 5 | 111 | Few-Body Systems in Lattice Eﬀective Field Theory Dissertation zur Erl |
| [`malkin-2021-galois-action-on-motivic-fundamental-groups-thes`](../../library/malkin-2021-galois-action-on-motivic-fundamental-groups-thes/) | 4 | 123 |  |
| [`arxiv-1206.6004v2`](../../library/arxiv-1206.6004v2/) | 3 | 20 | Symmetry, Integrability and Geometry: Methods and Applications SIGMA 8 |
| [`di-cairano-2022-j-phys-commun-6-015002`](../../library/di-cairano-2022-j-phys-commun-6-015002/) | 3 | 12 | Journal of Physics Communications PAPER • OPEN ACCESS On the derivatio |
| [`phys-rep09`](../../library/phys-rep09/) | 3 | 88 | PhysicsReports470(2009)151–238 Contents lists available at ScienceDire |

## Ranking

| # | score | doc-id | fml | pp | title | strongest shared terms |
|---|---|---|---|---|---|---|
| 1 | 648.6 | [`arxiv-math-0203194v1`](../../library/arxiv-math-0203194v1/) `!` | 91 | 256 | Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkai | table, tower, frobenius, archimedean, data |
| 2 | 535.0 | [`on-the-garoufalidis-kashaev-state-integral-invariant`](../../library/on-the-garoufalidis-kashaev-state-integral-invariant/) | 17 | 61 | of the requirements for the degree of Master of Science in Mathematics | table, archimedean, physical, coefficient, pairing |
| 3 | 511.1 | [`2018sorus020`](../../library/2018sorus020/) | 92 | 110 | HAL is a multi-disciplinary open access archive for the deposit and di | skein, trace, residual, generator, interpretation |
| 4 | 489.4 | [`arxiv-1601.02479v5`](../../library/arxiv-1601.02479v5/) | 41 | 64 | COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A | stability, structural, crossing, shift, hopf |
| 5 | 478.3 | [`bn`](../../library/bn/) | 44 | 64 | Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009 | braid, lifting, decomposition, cyclotomic, factor |
| 6 | 475.1 | [`210811825v1`](../../library/210811825v1/) | 40 | 163 | for the award of Doctor of Philosophy of Loughborough University | table, subscript, involution, resolvent, eigenvalue |
| 7 | 468.1 | [`arxiv-1207.6711v1`](../../library/arxiv-1207.6711v1/) | 47 | 47 | GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS | trace, ratio, equals, pairing, parity |
| 8 | 463.7 | [`arxiv-1511.00400v2`](../../library/arxiv-1511.00400v2/) | 71 | 55 | Reidemeister torsion, hyperbolic three-manifolds, and character variet | chain, trace, exceptional, correspondence, surface |
| 9 | 445.9 | [`agt-v7-n2-p13-s`](../../library/agt-v7-n2-p13-s/) | 31 | 73 | Algebraic & Geometric Topology 7 (2007) 845–917 845 Quantum hyperbolic | trace, ratio, functor, amplitude, parameter |
| 10 | 445.9 | [`arxiv-1402.4615v3`](../../library/arxiv-1402.4615v3/) | 53 | 71 | GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JAC | plancherel, close, transition, classical, probability |
| 11 | 443.8 | [`ant-v14-n7-s-p01`](../../library/ant-v14-n7-s-p01/) | 33 | 42 | p-adic Asai L-functions of Bianchi modular forms David Loeﬄerand Chris | realisation, involution, generator, factor, weights |
| 12 | 439.1 | [`ant-v14-n7-s-p05`](../../library/ant-v14-n7-s-p05/) | 30 | 52 | Motivic Gauss–Bonnet formulas | trace, object, functor, interpretation, monoidal |
| 13 | 436.8 | [`deligne-mostow-1986`](../../library/deligne-mostow-1986/) | 73 | 86 | P UBLICATIONS MATHÉMATIQUES DE L ’I.H.É.S. PIERRE DELIGNE G. D. MOSTOW | locus, kernel, normal, stable, bundle |
| 14 | 434.3 | [`0310279v5`](../../library/0310279v5/) | 44 | 128 | Stabilization in the braid groups I: MTWS JOAN S BIRMAN WILLIAM W MENA | existence, braid, across, decomposition, observations |
| 15 | 434.0 | [`arxiv-2509.02354v2`](../../library/arxiv-2509.02354v2/) | 33 | 41 | THE HOLONOMY BRAIDING FORUξ(sl2) IN TERMS OF GEOMETRIC QUANTUM DILOGAR | crossing, braiding, interpretation, fourier, experimental |
| 16 | 431.7 | [`klein-few-body-systems-in-lattice-effective-field-theory-the`](../../library/klein-few-body-systems-in-lattice-effective-field-theory-the/) `!` | 0 | 111 | Few-Body Systems in Lattice Eﬀective Field Theory Dissertation zur Erl | nuclear, coulomb, particle, status, nuclei |
| 17 | 430.6 | [`arxiv-2412.04241v2`](../../library/arxiv-2412.04241v2/) | 50 | 73 | THE HABIRO RING OF A NUMBER FIELD | habiro, integration, residue, field, trefoil |
| 18 | 428.7 | [`arxiv-math-0611504v1`](../../library/arxiv-math-0611504v1/) | 28 | 40 | QUANTUM HYPERBOLIC GEOMETRY | trace, ratio, branching, functor, weights |
| 19 | 425.7 | [`arxiv-2604.16077v1`](../../library/arxiv-2604.16077v1/) | 31 | 66 | VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT | factor, weights, classical, parameter, limits |
| 20 | 422.4 | [`arxiv-1604.02688v1`](../../library/arxiv-1604.02688v1/) | 40 | 57 | THE 3D-INDEX AND NORMAL SURFACES | normal, trefoil, surface, independence, duality |
| 21 | 417.6 | [`reshetikhin-turaev`](../../library/reshetikhin-turaev/) | 2 | 26 | Commun. Math. Phys. 127, 1-26 (1990) Communications in Mathematical Ph | uniqueness, hopf, functor, monoidal, field |
| 22 | 417.4 | [`arxiv-0906.1500v4`](../../library/arxiv-0906.1500v4/) | 15 | 29 | TWISTED ALEXANDER INV ARIANT AND NON–ABELIAN REIDEMEISTER TORSION FOR  | never, involution, bridge, dual, topological |
| 23 | 416.3 | [`arxiv-0905.0591v3`](../../library/arxiv-0905.0591v3/) | 37 | 42 | A SUR VEY OF TWISTED ALEXANDER POL YNOMIALS | bridge, hopf, factor, commutative, period |
| 24 | 416.1 | [`arxiv-1611.03697v5`](../../library/arxiv-1611.03697v5/) | 19 | 51 | RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND | uniqueness, data, symbols, sector, topological |
| 25 | 414.4 | [`arxiv-1712.04887v3`](../../library/arxiv-1712.04887v3/) | 39 | 43 | BLOCH GROUPS, ALGEBRAIC K-THEORY | closure, reduction, kernel, divisor, commutative |
| 26 | 408.3 | [`arxiv-2208.13692v1`](../../library/arxiv-2208.13692v1/) | 30 | 38 | BRING’S CURVE: OLD AND NEW | data, bring, decomposition, parity, divisor |
| 27 | 407.8 | [`arxiv-1204.4824v2`](../../library/arxiv-1204.4824v2/) | 1 | 87 | Prepared for submission to JHEP Spectral networks | categorical, spectral, crossing, content, lifting |
| 28 | 395.6 | [`arxiv-0706.2213v3`](../../library/arxiv-0706.2213v3/) | 10 | 36 | NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS | table, trace, regularity, bridge, trefoil |
| 29 | 390.3 | [`arxiv-2008.09788v2`](../../library/arxiv-2008.09788v2/) | 29 | 31 | NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECT | eigenvalue, rigidity, reduction, residue, field |
| 30 | 382.8 | [`arxiv-1303.5278v1`](../../library/arxiv-1303.5278v1/) | 21 | 60 | 1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANI | decomposition, normal, trefoil, dual, invariance |
| 31 | 376.6 | [`malkin-2021-galois-action-on-motivic-fundamental-groups-thes`](../../library/malkin-2021-galois-action-on-motivic-fundamental-groups-thes/) `!` | 58 | 123 | _(none extracted)_ | depth, interpretation, base, motivic, weight |
| 32 | 374.7 | [`arxiv-math-0604057v2`](../../library/arxiv-math-0604057v2/) | 29 | 19 | VOLUME CONJECTURE, REGULA TOR AND SL2(C)-CHARACTER V ARIETY OF A KNOT | exceptional, surface, bundle, instance, character |
| 33 | 372.7 | [`arxiv-2301.02038v1`](../../library/arxiv-2301.02038v1/) | 22 | 26 | Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partia | derivation, prolongation, regularity, shift, cohomological |
| 34 | 372.5 | [`nrarith`](../../library/nrarith/) | 29 | 38 | Arithmetic of Hyperbolic Manifolds | chain, trace, parameter, derived, algebras |
| 35 | 370.6 | [`arxiv-hep-th-0306165v1`](../../library/arxiv-hep-th-0306165v1/) | 0 | 67 | Three-Dimensional Quantum Gravity | physical, gravity, gauge, interpretation, field |
| 36 | 369.3 | [`ant-v14-n7-s-p02`](../../library/ant-v14-n7-s-p02/) | 22 | 36 | Pro-unipotent harmonic actions and dynamical properties of p -adic cyc | frobenius, depth, zeta, cyclotomic, times |
| 37 | 366.4 | [`arxiv-1507.03238v3`](../../library/arxiv-1507.03238v3/) | 33 | 26 | TRIANGULATION INDEPENDENT PTOLEMY VARIETIES | obstruction, degeneracy, correspondence, coordinates, action |
| 38 | 364.8 | [`arxiv-2402.04839v2`](../../library/arxiv-2402.04839v2/) | 24 | 28 | On a volume invariant of 3–manifolds | table, borromean, surface, finiteness, topological |
| 39 | 364.6 | [`afst-2007-6-16-3-665-0`](../../library/afst-2007-6-16-3-665-0/) | 31 | 55 | ANNALES DE LA FACULTÉ DES SCIENCES Mathématiques | data, observation, descent, functor, topological |
| 40 | 361.5 | [`monodromyhitchiny`](../../library/monodromyhitchiny/) | 9 | 14 | HAL is a multi-disciplinary open access archive for the deposit and di | trace, braid, decomposition, conformal, base |
| 41 | 349.7 | [`0504116v2`](../../library/0504116v2/) | 31 | 24 | On deformations of hyperbolic 3–manifolds with geodesic boundary ROBER | completeness, lifting, pairing, exceptional, rigidity |
| 42 | 346.8 | [`arxiv-hep-th-0006156v1`](../../library/arxiv-hep-th-0006156v1/) | 0 | 20 | STRONGL Y COUPLED QUANTUM DISCRETE LIOUVILLE | data, involution, shift, factor, fourier |
| 43 | 339.8 | [`modularqholonomicmodules`](../../library/modularqholonomicmodules/) | 23 | 66 | MODULAR q-HOLONOMIC MODULES | categorical, residue, operator, duality, identity |
| 44 | 336.3 | [`arxiv-1704.02352v2`](../../library/arxiv-1704.02352v2/) | 18 | 43 | GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS | content, plancherel, conditional, probability, check |
| 45 | 335.4 | [`arxiv-1203.2182v1`](../../library/arxiv-1203.2182v1/) | 0 | 92 | Volume Conjecture: Reﬁned and Categoriﬁed | mass, gamma, braid, recursion, trefoil |
| 46 | 333.0 | [`arxiv-math-0305275v1`](../../library/arxiv-math-0305275v1/) | 52 | 38 | Hyperbolic volume of representations of fundamental groups of cusped 3 | chain, rigidity, classical, operator, topological |
| 47 | 332.7 | [`gambaudo-ghys-braids-signatures-2005`](../../library/gambaudo-ghys-braids-signatures-2005/) | 15 | 40 | Bull. Soc. math. France 133 (4), 2005, p. 541–579 | braid, convention, surface, signatures, braids |
| 48 | 326.7 | [`arxiv-math-0506456v1`](../../library/arxiv-math-0506456v1/) | 29 | 70 | Journal of Knot Theory and Its Ramiﬁcations c© W orld Scientiﬁc Publis | bridge, classical, dilogarithm, leading, pair |
| 49 | 323.5 | [`0307092v2`](../../library/0307092v2/) | 44 | 62 | ISSN 1364-0380 (on line) 1465-3060 (printed) 413 | star, ordering, normal, commutative, instance |
| 50 | 323.0 | [`arxiv-math-9907032v1`](../../library/arxiv-math-9907032v1/) | 33 | 27 | Combinatorial optimization in geometry 1 | flow, surface, computational, vertex, curvature |
| 51 | 322.4 | [`arxiv-2510.04782v2`](../../library/arxiv-2510.04782v2/) | 15 | 82 | q-Hodge complexes over the Habiro ring Ferdinand Wagner | fibre, filtration, observation, descent, convention |
| 52 | 321.9 | [`arxiv-2203.17029v1`](../../library/arxiv-2203.17029v1/) | 22 | 65 | MODULAR q-HOLONOMIC MODULES | categorical, residue, operator, duality, identity |
| 53 | 316.8 | [`arxiv-1002.0126v1`](../../library/arxiv-1002.0126v1/) | 9 | 39 | AN INTRODUCTION TO THE VOLUME CONJECTURE HITOSHI MURAKAMI | skein, descent, closure, braid, interpretation |
| 54 | 310.7 | [`ihpmay2025`](../../library/ihpmay2025/) | 41 | 41 | IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY | stability, classification, density, cosh, conformal |
| 55 | 309.7 | [`arxiv-math-0304010v1`](../../library/arxiv-math-0304010v1/) | 38 | 49 | KEROV’S CENTRAL LIMIT THEOREM FOR THE PLANCHEREL MEASURE ON YOUNG DIAG | mass, equals, plancherel, transition, correspondence |
| 56 | 308.4 | [`lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3`](../../library/lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3/) | 35 | 24 | Acta Mathematica Sinica, English Series 1999, July, Vol.15, No.3, p. 2 | fixed, residue, limits, recursive, coefficients |
| 57 | 305.8 | [`arxiv-1512.04993v2`](../../library/arxiv-1512.04993v2/) | 0 | 70 | Complexity, action, and black holes | energy, shells, gate, equals, times |
| 58 | 304.7 | [`arxiv-1106.6298v1`](../../library/arxiv-1106.6298v1/) | 11 | 18 | ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INV ARIANTS | frobenius, endomorphism, cyclotomic, habiro, laplace |
| 59 | 302.2 | [`arxiv-hep-th-9408099v1`](../../library/arxiv-hep-th-9408099v1/) | 0 | 88 | Monopoles, Duality and Chiral Symmetry Breaking in N=2 Supersymmetric  | mass, energy, scale, classical, coupling |
| 60 | 300.3 | [`arxiv-1511.05628v1`](../../library/arxiv-1511.05628v1/) | 3 | 41 | QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY | data, derivation, feynman, level, invariance |
| 61 | 295.3 | [`arxiv-2209.06973v1`](../../library/arxiv-2209.06973v1/) | 6 | 66 | On the geometry of two state models for the colored Jones polynomial | braid, ordering, correspondence, classical, evaluation |
| 62 | 295.0 | [`arxiv-2205.01282v2`](../../library/arxiv-2205.01282v2/) | 27 | 18 | WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBE | decay, theta, refinement, linking, block |
| 63 | 285.2 | [`arxiv-1108.4389v1`](../../library/arxiv-1108.4389v1/) | 0 | 58 | Gauge Theories Labelled by Three-Manifolds | chain, gauge, operations, operator, interaction |
| 64 | 284.9 | [`arxiv-math-0410233v4`](../../library/arxiv-math-0410233v4/) | 31 | 46 | CUSP SHAPES UNDER CONE DEFORMA TION JESSICA S. PURCELL | tube, bridge, time, bound, local |
| 65 | 282.2 | [`arxiv-1202.4698v3`](../../library/arxiv-1202.4698v3/) | 0 | 32 | 6j symbols for the modular double, quantum hyperbolic geometry, and su | gamma, symbols, gauge, kernel, classical |
| 66 | 268.1 | [`angled-survey`](../../library/angled-survey/) | 30 | 24 | Contemporary Mathematics From angled triangulations to hyperbolic stru | close, rigidity, normal, surface, volume |
| 67 | 263.3 | [`arxiv-2111.04763v2`](../../library/arxiv-2111.04763v2/) | 5 | 59 | RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION | equals, habiro, block, connection, resummation |
| 68 | 262.4 | [`4geo-dedi-rev`](../../library/4geo-dedi-rev/) | 15 | 26 | HAL is a multi-disciplinary open access archive for the deposit and di | factor, classical, parameter, dual, coordinate |
| 69 | 260.9 | [`zagier-the-dilogarithm-function`](../../library/zagier-the-dilogarithm-function/) | 9 | 63 | The Dilogarithm Function Don Zagier | quotient, information, dilogarithm, functional, volumes |
| 70 | 259.1 | [`arxiv-2605.22763v1`](../../library/arxiv-2605.22763v1/) | 19 | 59 | 2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof S | selection, text, lean, count, light |
| 71 | 258.3 | [`arxiv-1811.05376v4`](../../library/arxiv-1811.05376v4/) | 10 | 40 | Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology  | decay, decomposition, transform, invariance, coefficients |
| 72 | 255.7 | [`zagier-the-dilogarithm-function-copy-b`](../../library/zagier-the-dilogarithm-function-copy-b/) | 9 | 63 | The Dilogarithm Function Don Zagier | information, dilogarithm, functional, volumes, geometry |
| 73 | 255.3 | [`maximal-hoermander-q-var-revised-v03`](../../library/maximal-hoermander-q-var-revised-v03/) | 41 | 43 | HAL is a multi-disciplinary open access archive for the deposit and di | spectral, time, operator, harmonic, functional |
| 74 | 253.0 | [`arxiv-0707.3682v2`](../../library/arxiv-0707.3682v2/) | 12 | 44 | ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS | cyclotomic, motivic, residue, role, fields |
| 75 | 253.0 | [`cspaper`](../../library/cspaper/) | 11 | 29 | Combinatorics of Triangulations and the Chern-Simons Invariant for Hyp | interpretation, cohomological, parity, topological, check |
| 76 | 251.3 | [`poincare-proof-outline`](../../library/poincare-proof-outline/) | 0 | 175 | Poincaré Disc Model Danijela Simić Filip Marić Pierre Boutry | uniqueness, existence, axiom, interpretation, axioms |
| 77 | 247.1 | [`s0025-5718-07-02027-3`](../../library/s0025-5718-07-02027-3/) | 28 | 30 | MA THEMA TICS OF COMPUT A TION | times, residue, precision, characterisation, rigid |
| 78 | 244.2 | [`arxiv-2305.14884v2`](../../library/arxiv-2305.14884v2/) | 14 | 48 | PERTURBATIVE INV ARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS | data, fourier, integration, transform, invariance |
| 79 | 242.8 | [`arxiv-1203.6551v1`](../../library/arxiv-1203.6551v1/) | 19 | 25 | On the number of hyperbolic 3-manifolds of a given volume | crossing, volume, pair, primitive, torus |
| 80 | 242.1 | [`arxiv-math-ph-0012035v3`](../../library/arxiv-math-ph-0012035v3/) | 0 | 46 | Non-Abelian Stokes theorem in action Bogus/suppress law Broda1 Departm | trace, decomposition, ordering, operator, topological |

_Showing 80 of 248. Full data: `library/*/candidates.json`._
