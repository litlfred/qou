# Uncited library documents — triage queue

**Generated** by `scripts/library-relevance-rank.py --write-triage`.
Regenerate rather than edit — the numbers below move whenever a source is
cited or a document is added, and a stamped date here just goes stale (this
line used to read "Generated 2026-08-15" long after it was not).

278 of 351 library documents are **held and registered but
cited by nothing** — no content block references their `references.ts`
entry, by `\cite{}` in a `.md`, by `cites: []` in a `.ts`, or by a Lean
`-- Ref: [key]`. That is the backlog
[`local/paper-relevance-triage`](../../.claude/skills/local/paper-relevance-triage.md)
exists to work.

**This measures something different than it used to.** It counted documents
with no `library:` back-reference from the bibliography — i.e. unregistered.
That backlog is drained: every library document now has an entry, so the
count went to zero and this page became an empty table under prose
describing a queue that no longer existed. Registered is not cited, and the
gap between them is the whole of this list.

## How this is ranked

By **topical overlap with the qou corpus**, not by volume of extracted
material. An earlier pass ranked by formalizable-candidate count and put a
whole journal issue first — that measures how much formal content a document
*offers*, which is not the same question.

The vocabulary is derived from this corpus, not hand-supplied: every content-block
`title:` and `defines:` entry plus the notation register, yielding 2187 terms,
of which 1296 discriminate within the library. Weighting is library IDF times
corpus frequency: a term must be both rare in the library and central here, so
neither a ubiquitous word nor a rare-but-alien one scores. Scoring reads each
document's extracted *claims*
(`candidates.json`) plus its title and section titles — not its prose — so a
passing mention in a bibliography does not inflate a score.

**The score is a prior, not a verdict.** It says "this document is written in our
vocabulary", which is where triage should start, not where it should end.

## Bound volumes (9 flagged)

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
| [`arxiv-math-0203194v1`](../../library/arxiv-math-0203194v1/) | 5 | 256 | Period mappings and differential equations. From C to Cp |
| [`klein-few-body-systems-in-lattice-effective-field-theory-the`](../../library/klein-few-body-systems-in-lattice-effective-field-theory-the/) | 5 | 111 | Few-body systems in lattice effective field theory |
| [`disssubmission`](../../library/disssubmission/) | 4 | 181 | Tannakian categories of perverse sheaves on abelian varieties |
| [`malkin-2021-galois-action-on-motivic-fundamental-groups-thes`](../../library/malkin-2021-galois-action-on-motivic-fundamental-groups-thes/) | 4 | 123 | On the Galois action on motivic fundamental groups of punctured ellipt |
| [`symmetry-04-00039-v3`](../../library/symmetry-04-00039-v3/) | 4 | 77 | Knots on a Torus: A Model of the Elementary Particles |
| [`arxiv-1611.09182v1`](../../library/arxiv-1611.09182v1/) | 4 | 97 | Standard model physics from an algebra? |
| [`kondev-2021-chinese-phys-c-45-030001`](../../library/kondev-2021-chinese-phys-c-45-030001/) | 3 | 181 | The NUBASE2020 evaluation of nuclear physics properties |
| [`di-cairano-2022-j-phys-commun-6-015002`](../../library/di-cairano-2022-j-phys-commun-6-015002/) | 3 | 12 | On the derivation of a nonlinear generalized Langevin equation |
| [`phys-rep09`](../../library/phys-rep09/) | 3 | 88 | The Magnus expansion and some of its applications |

## Ranking

| # | score | doc-id | fml | pp | title | strongest shared terms |
|---|---|---|---|---|---|---|
| 1 | 656.0 | [`arxiv-math-0203194v1`](../../library/arxiv-math-0203194v1/) `!` | 91 | 256 | Period mappings and differential equations. From C to Cp | table, tower, frobenius, archimedean, data |
| 2 | 545.6 | [`on-the-garoufalidis-kashaev-state-integral-invariant`](../../library/on-the-garoufalidis-kashaev-state-integral-invariant/) | 17 | 61 | On the Garoufalidis-Kashaev state-integral invariant | table, archimedean, physical, coefficient, gauge |
| 3 | 521.1 | [`2018sorus020`](../../library/2018sorus020/) | 92 | 110 | Reidemeister torsion on character varieties | skein, trace, residual, generator, convention |
| 4 | 506.7 | [`arxiv-1601.02479v5`](../../library/arxiv-1601.02479v5/) | 41 | 64 | Cohomological Donaldson-Thomas theory of a quiver with potential and q | stability, structural, crossing, shift, functor |
| 5 | 499.1 | [`bn`](../../library/bn/) | 44 | 64 | Braid groups and Hodge theory | braid, factor, weights, decomposition, cyclotomic |
| 6 | 497.2 | [`210811825v1`](../../library/210811825v1/) | 40 | 163 | Properties of eigenvalues on Riemann surfaces with large symmetry grou | table, subscript, involution, resolvent, eigenvalue |
| 7 | 489.1 | [`arxiv-1511.00400v2`](../../library/arxiv-1511.00400v2/) | 71 | 55 | Reidemeister torsion, hyperbolic three-manifolds, and character variet | chain, trace, exceptional, correspondence, surface |
| 8 | 484.2 | [`arxiv-1207.6711v1`](../../library/arxiv-1207.6711v1/) | 47 | 47 | GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS | ratio, trace, equals, pairing, parity |
| 9 | 484.0 | [`motivicperiodsandp1minus3pointsv3`](../../library/motivicperiodsandp1minus3pointsv3/) | 20 | 25 | Motivic periods and P^1 minus 3 points | hecke, realisation, depth, zeta, realisations |
| 10 | 466.4 | [`arxiv-1402.4615v3`](../../library/arxiv-1402.4615v3/) | 53 | 71 | GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JAC | plancherel, close, transition, classical, character |
| 11 | 463.8 | [`agt-v7-n2-p13-s`](../../library/agt-v7-n2-p13-s/) | 31 | 73 | Quantum hyperbolic geometry | ratio, trace, functor, amplitude, parameter |
| 12 | 463.2 | [`klein-few-body-systems-in-lattice-effective-field-theory-the`](../../library/klein-few-body-systems-in-lattice-effective-field-theory-the/) `!` | 0 | 111 | Few-body systems in lattice effective field theory | nuclear, coulomb, status, particle, density |
| 13 | 457.3 | [`0310279v5`](../../library/0310279v5/) | 44 | 128 | Stabilization in the braid groups I: MTWS | existence, braid, across, decomposition, normal |
| 14 | 457.1 | [`arxiv-2412.04241v2`](../../library/arxiv-2412.04241v2/) | 50 | 73 | THE HABIRO RING OF A NUMBER FIELD | habiro, residue, trefoil, field, integration |
| 15 | 456.7 | [`arxiv-2604.16077v1`](../../library/arxiv-2604.16077v1/) | 31 | 66 | VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT  | factor, weights, limits, classical, parameter |
| 16 | 454.7 | [`deligne-mostow-1986`](../../library/deligne-mostow-1986/) | 73 | 86 | Monodromy of hypergeometric functions and non-lattice integral monodro | normal, locus, kernel, bundle, stable |
| 17 | 453.5 | [`ant-v14-n7-s-p05`](../../library/ant-v14-n7-s-p05/) | 26 | 52 | Motivic Gauss–Bonnet formulas | trace, functor, object, interpretation, motivic |
| 18 | 453.2 | [`ant-v14-n7-s-p01`](../../library/ant-v14-n7-s-p01/) | 33 | 42 | p-adic Asai L-functions of Bianchi modular forms | realisation, involution, generator, factor, weights |
| 19 | 452.0 | [`arxiv-1604.02688v1`](../../library/arxiv-1604.02688v1/) | 40 | 57 | THE 3D-INDEX AND NORMAL SURFACES | normal, trefoil, surface, linking, duality |
| 20 | 449.1 | [`disssubmission`](../../library/disssubmission/) `!` | 0 | 181 | Tannakian categories of perverse sheaves on abelian varieties | difference, theta, period, character, spectrum |
| 21 | 448.1 | [`arxiv-0906.1500v4`](../../library/arxiv-0906.1500v4/) | 15 | 29 | Twisted Alexander invariant and non-abelian Reidemeister torsion for h | never, involution, bridge, topological, dual |
| 22 | 447.1 | [`arxiv-2509.02354v2`](../../library/arxiv-2509.02354v2/) | 33 | 41 | The holonomy braiding for U_xi(sl2) in terms of geometric quantum dilo | crossing, braiding, interpretation, fourier, experimental |
| 23 | 445.0 | [`arxiv-0905.0591v3`](../../library/arxiv-0905.0591v3/) | 37 | 42 | A SURVEY OF TWISTED ALEXANDER POLYNOMIALS | bridge, hopf, factor, duality, commutative |
| 24 | 437.3 | [`arxiv-1611.03697v5`](../../library/arxiv-1611.03697v5/) | 19 | 51 | RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY | uniqueness, data, symbols, sector, topological |
| 25 | 434.0 | [`arxiv-1712.04887v3`](../../library/arxiv-1712.04887v3/) | 39 | 43 | Bloch groups, algebraic K-theory, units, and Nahm's conjecture | closure, divisor, reduction, kernel, commutative |
| 26 | 427.7 | [`reshetikhin-turaev`](../../library/reshetikhin-turaev/) | 2 | 26 | Ribbon graphs and their invariants derived from quantum groups | uniqueness, functor, hopf, field, operator |
| 27 | 426.6 | [`arxiv-0706.2213v3`](../../library/arxiv-0706.2213v3/) | 10 | 36 | NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS | table, trace, bridge, regularity, trefoil |
| 28 | 425.5 | [`0309214v3`](../../library/0309214v3/) | 31 | 41 | The colored Jones function is q-holonomic | braiding, braid, recursion, ordering, cyclotomic |
| 29 | 424.0 | [`arxiv-1204.4824v2`](../../library/arxiv-1204.4824v2/) | 1 | 87 | Spectral networks | categorical, spectral, crossing, content, convention |
| 30 | 419.5 | [`arxiv-hep-th-0306165v1`](../../library/arxiv-hep-th-0306165v1/) | 0 | 67 | Three-Dimensional Quantum Gravity, Chern-Simons Theory, and the A-Poly | physical, gravity, gauge, interpretation, field |
| 31 | 416.8 | [`arxiv-2008.09788v2`](../../library/arxiv-2008.09788v2/) | 29 | 31 | NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECT | eigenvalue, residue, rigidity, divisor, field |
| 32 | 415.2 | [`malkin-2021-galois-action-on-motivic-fundamental-groups-thes`](../../library/malkin-2021-galois-action-on-motivic-fundamental-groups-thes/) `!` | 58 | 123 | On the Galois action on motivic fundamental groups of punctured ellipt | depth, interpretation, motivic, base, weight |
| 33 | 414.8 | [`zhao-standard-2010`](../../library/zhao-standard-2010/) | 22 | 34 | Standard Relations of Multiple Polylogarithm Values at Roots of Unity | prop, table, data, weights, divisor |
| 34 | 413.0 | [`arxiv-hep-th-0006156v1`](../../library/arxiv-hep-th-0006156v1/) | 0 | 20 | Strongly coupled quantum discrete Liouville theory I: algebraic approa | data, involution, shift, factor, fourier |
| 35 | 402.0 | [`arxiv-math-0604057v2`](../../library/arxiv-math-0604057v2/) | 29 | 19 | VOLUME CONJECTURE, REGULATOR AND SL2(C)-CHARACTER VARIETY OF A KNOT | exceptional, surface, bundle, instance, volume |
| 36 | 400.8 | [`nrarith`](../../library/nrarith/) | 29 | 38 | Arithmetic of Hyperbolic Manifolds | chain, trace, parameter, derived, volume |
| 37 | 399.9 | [`arxiv-2301.02038v1`](../../library/arxiv-2301.02038v1/) | 22 | 26 | Vinogradov's Cohomological Geometry of Partial Differential Equations | derivation, prolongation, regularity, shift, cohomological |
| 38 | 398.4 | [`ant-v14-n7-s-p02`](../../library/ant-v14-n7-s-p02/) | 22 | 36 | Pro-unipotent harmonic actions and dynamical properties of p-adic cycl | frobenius, depth, zeta, cyclotomic, times |
| 39 | 394.1 | [`arxiv-2402.04839v2`](../../library/arxiv-2402.04839v2/) | 24 | 28 | On a volume invariant of 3–manifolds | table, borromean, surface, topological, finiteness |
| 40 | 393.2 | [`topologicalinvariance3dindex`](../../library/topologicalinvariance3dindex/) | 19 | 60 | 1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANI | normal, trefoil, invariance, pentagon, topological |
| 41 | 392.3 | [`afst-2007-6-16-3-665-0`](../../library/afst-2007-6-16-3-665-0/) | 31 | 55 | Galois theory of q-difference equations | data, descent, observation, functor, topological |
| 42 | 385.4 | [`arxiv-1507.03238v3`](../../library/arxiv-1507.03238v3/) | 33 | 26 | TRIANGULATION INDEPENDENT PTOLEMY VARIETIES | obstruction, degeneracy, correspondence, coordinates, action |
| 43 | 383.8 | [`0504116v2`](../../library/0504116v2/) | 31 | 24 | On deformations of hyperbolic 3-manifolds with geodesic boundary | completeness, pairing, exceptional, lifting, rigidity |
| 44 | 382.3 | [`modularqholonomicmodules`](../../library/modularqholonomicmodules/) | 23 | 66 | MODULAR q-HOLONOMIC MODULES | categorical, residue, operator, information, duality |
| 45 | 371.6 | [`monodromyhitchiny`](../../library/monodromyhitchiny/) | 9 | 14 | On the monodromy of the Hitchin connection | trace, braid, decomposition, conformal, base |
| 46 | 370.8 | [`arxiv-1203.2182v1`](../../library/arxiv-1203.2182v1/) | 0 | 92 | Volume Conjecture: Refined and Categorified | mass, gamma, braid, recursion, trefoil |
| 47 | 370.8 | [`arxiv-math-0305275v1`](../../library/arxiv-math-0305275v1/) | 52 | 38 | Hyperbolic volume of representations of fundamental groups of cusped 3 | chain, rigidity, classical, operator, topological |
| 48 | 366.7 | [`arxiv-1704.02352v2`](../../library/arxiv-1704.02352v2/) | 18 | 43 | GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS | content, conditional, plancherel, check, identity |
| 49 | 359.5 | [`gambaudo-ghys-braids-signatures-2005`](../../library/gambaudo-ghys-braids-signatures-2005/) | 15 | 40 | Braids and signatures | braid, convention, signatures, surface, braids |
| 50 | 353.7 | [`ihpmay2025`](../../library/ihpmay2025/) | 41 | 41 | IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS | stability, classification, density, cosh, conformal |
| 51 | 340.3 | [`arxiv-1002.0126v1`](../../library/arxiv-1002.0126v1/) | 9 | 39 | An introduction to the volume conjecture | skein, descent, closure, braid, interpretation |
| 52 | 338.2 | [`arxiv-1511.05628v1`](../../library/arxiv-1511.05628v1/) | 3 | 41 | QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY | data, derivation, feynman, level, invariance |
| 53 | 335.1 | [`arxiv-2510.04782v2`](../../library/arxiv-2510.04782v2/) | 15 | 82 | q-Hodge complexes over the Habiro ring | fibre, filtration, descent, observation, habiro |
| 54 | 334.8 | [`helicity03mmj`](../../library/helicity03mmj/) | 12 | 23 | Geometry of higher helicities | energy, hopf, interpretation, rotation, field |
| 55 | 332.0 | [`arxiv-1108.4389v1`](../../library/arxiv-1108.4389v1/) | 0 | 58 | Gauge Theories Labelled by Three-Manifolds | chain, gauge, operations, operator, geometry |
| 56 | 331.7 | [`arxiv-1106.6298v1`](../../library/arxiv-1106.6298v1/) | 11 | 18 | ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS | frobenius, habiro, endomorphism, cyclotomic, laplace |
| 57 | 330.9 | [`arxiv-math-0304010v1`](../../library/arxiv-math-0304010v1/) | 38 | 49 | KEROV’S CENTRAL LIMIT THEOREM FOR THE PLANCHEREL MEASURE ON YOUNG DIAG | mass, equals, plancherel, transition, correspondence |
| 58 | 326.8 | [`arxiv-2205.01282v2`](../../library/arxiv-2205.01282v2/) | 27 | 18 | Witten-Reshetikhin-Turaev invariants and homological blocks for plumbe | decay, theta, linking, refinement, block |
| 59 | 324.1 | [`lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3`](../../library/lin-wang-1999-on-ohtsukis-invariants-of-integral-homology-3/) | 35 | 24 | On Ohtsuki's invariants of integral homology 3-spheres | residue, fixed, limits, limit, unit |
| 60 | 322.8 | [`arxiv-1512.04993v2`](../../library/arxiv-1512.04993v2/) | 0 | 70 | Complexity, action, and black holes | energy, shells, gate, equals, locality |
| 61 | 318.7 | [`arxiv-hep-th-9408099v1`](../../library/arxiv-hep-th-9408099v1/) | 0 | 88 | Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric  | mass, energy, scale, classical, coupling |
| 62 | 315.9 | [`arxiv-math-0410233v4`](../../library/arxiv-math-0410233v4/) | 31 | 46 | Cusp shapes under cone deformation | tube, bridge, time, bound, local |
| 63 | 314.5 | [`arxiv-math-0203273v3`](../../library/arxiv-math-0203273v3/) | 0 | 146 | Nilpotence, radicaux et structures monoïdales | prop, wedderburn, existence, trace, stable |
| 64 | 312.3 | [`arxiv-1202.4698v3`](../../library/arxiv-1202.4698v3/) | 0 | 32 | 6j symbols for the modular double, quantum hyperbolic geometry, and su | gamma, symbols, gauge, kernel, classical |
| 65 | 312.1 | [`arxiv-2209.06973v1`](../../library/arxiv-2209.06973v1/) | 6 | 66 | On the geometry of two state models for the colored Jones polynomial | braid, ordering, correspondence, classical, braids |
| 66 | 306.9 | [`arxiv-2505.00799v2`](../../library/arxiv-2505.00799v2/) | 27 | 32 | QUANTUM MODULAR FORMS AND RESURGENCE | obstruction, spectral, shift, decomposition, transform |
| 67 | 304.4 | [`symmetry-04-00039-v3`](../../library/symmetry-04-00039-v3/) `!` | 0 | 77 | Knots on a Torus: A Model of the Elementary Particles | beta, delta, decay, particle, hopf |
| 68 | 302.9 | [`arxiv-math-0411647v2`](../../library/arxiv-math-0411647v2/) | 32 | 60 | Asymptotics of characters of symmetric groups, genus expansion and fre | crossing, probability, connection, product, expansion |
| 69 | 300.2 | [`angled-survey`](../../library/angled-survey/) | 30 | 24 | From angled triangulations to hyperbolic structures | close, normal, rigidity, surface, volume |
| 70 | 299.3 | [`arxiv-2111.04763v2`](../../library/arxiv-2111.04763v2/) | 5 | 59 | RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION | equals, habiro, connection, block, jones |
| 71 | 297.1 | [`arxiv-0808.1533v3`](../../library/arxiv-0808.1533v3/) | 15 | 30 | On the third order helicity of magnetic fields on invariant domains in | energy, existence, borromean, factor, time |
| 72 | 296.1 | [`arxiv-0707.3682v2`](../../library/arxiv-0707.3682v2/) | 12 | 44 | ON THE p-ADIC BEILINSON CONJECTURE FOR NUMBER FIELDS | cyclotomic, residue, motivic, role, galois |
| 73 | 294.7 | [`arxiv-1611.09182v1`](../../library/arxiv-1611.09182v1/) `!` | 0 | 97 | Standard model physics from an algebra? | chain, ladder, particle, generation, time |
| 74 | 291.5 | [`maximal-hoermander-q-var-revised-v03`](../../library/maximal-hoermander-q-var-revised-v03/) | 41 | 43 | q-variational Hormander functional calculus and Schrodinger and wave m | spectral, time, operator, calculus, harmonic |
| 75 | 291.0 | [`zagier-the-dilogarithm-function`](../../library/zagier-the-dilogarithm-function/) | 9 | 63 | The dilogarithm function | information, dilogarithm, geometry, volumes, functional |
| 76 | 288.9 | [`arxiv-1906.12122v2`](../../library/arxiv-1906.12122v2/) | 0 | 76 | Nuclear effective field theory: status and perspectives | neutron, nuclear, status, quark, amplitude |
| 77 | 288.3 | [`4geo-dedi-rev`](../../library/4geo-dedi-rev/) | 15 | 26 | On the quantum Teichmüller invariants of fibred cusped 3-manifolds | factor, classical, parameter, dual, geometry |
| 78 | 287.9 | [`poincare-proof-outline`](../../library/poincare-proof-outline/) | 0 | 175 | Formalization of the Poincare disc model of hyperbolic geometry | uniqueness, existence, axiom, interpretation, axioms |
| 79 | 286.8 | [`arxiv-1811.05376v4`](../../library/arxiv-1811.05376v4/) | 10 | 40 | Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology  | decay, decomposition, transform, invariance, coefficients |
| 80 | 285.5 | [`104171-owr-2018-52`](../../library/104171-owr-2018-52/) | 0 | 66 | Enveloping Algebras and Geometric Representation Theory (Oberwolfach R | crystal, object, enveloping, ring, geometric |

_Showing 80 of 278. Full data: `library/*/candidates.json`._
