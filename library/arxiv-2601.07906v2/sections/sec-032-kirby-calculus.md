---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-032-kirby-calculus
section_title: "Kirby calculus"
section_number: null
pages: 106-117
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
Kirby calculus
We can think of many of the above VTQFT identities as arising from a homeomor-
phism of 3-manifolds M ∼= M ′, since ZVir is a topological invariant. The main tool
that is used in topology to find homeomorphisms between 3-manifolds is known as
‘Kirby calculus’. Here, we present some basic aspects of Kirby calculus relevant to
the Virasoro TQFT. For a more detailed review of this topic, we recommend the
following literature [145–147].
The Lickorish–Wallace theorem [148, 149] states that any closed, connected,
orientable 3-manifold can be obtained by integer Dehn surgery on the components
of a link inside S3.48 Integer Dehn surgery means that the coefficient p/q associated
to each link component can be chosen to be an integer, i.e. with q = 1. This result
allows for the representation of any 3-manifold as a link with a framing. For example,
from left to right, the following diagrams represent the manifolds S2 ×S1, the 3-torus
T 3, and the Lens space L(7, 5):
0 ,
0
0
0
,
−1
3
2
.
(C.42)
The framing determines which Dehn filling to perform on the corresponding link
component.
There are several standard conventions for indicating the framing. In the integer
framing, each link component is assigned an integer. In the annular framing, the link
is thickened into a ribbon which keeps track of these coefficients. The blackboard
framing uses the diagram itself to record the framing.
These three conventions
(integer, annular, and blackboard) are illustrated below:
−1
=
=
.
(C.43)
The representation of closed 3-manifolds in terms of framed links is not unique,
and the role of Kirby calculus is to determine when two framed links correspond
to the same topology. For example, two links that are related via a sequence of
framed Reidemeister moves yield homeomorphic 3-manifolds. There are three framed
48There is also an extension to manifolds with boundary, see e.g. appendix B.3 of [145].
– 106 –
Reidemeister moves, with only the first differing from its classical version:
R1:
←→
←→
,
R2:
←→
,
R3:
←→
.
(C.44)
The need for framed moves instead of the standard Reidemeister moves is because
the framed version preserves the blackboard framing. Kirby [150] introduced two
additional moves (K1 and K2) and proved that the surgery on a pair of framed links
correspond to the same 3-manifold if and only if they are related by a finite sequence
of R and K moves. The first Kirby move adds or deletes a disjoint unknot with
framing +1 or −1 from the link L,
K1:
L
←→
L ⊔
±1 .
(C.45)
The second Kirby move, also known as a handle slide, is more involved and is better
explained with an example:
K2:
←→
.
(C.46)
This move involves two link components drawn in the blackboard frame. It slides
one of the links along the framing of the other.
From K1 and K2, one can build composite moves which make it easier to identify
whenever two links correspond to the same manifold. Two of such operations are
the blow up FR+ and the blow down FR−:
FR+
←→
,
FR−
←→
. (C.47)
– 107 –
These operation allow for the twisting (or untwisting) of n strands via the deletion (or
inclusion) of a ±1-framed unknot. The case where n = 0 is equivalent to the Kirby
move K1. These operations are also known in the literature as the Fenn-Rourke
(FR) moves. Fenn and Rourke [151] showed that two links in S3 give homeomophic
manifolds if and only if they are related by a sequence of blow ups and blow downs.
Below, we show that these moves are naturally realized within the Virasoro TQFT
and follow directly from basic properties of the PSL(2, Z) crossing kernels.
Blow ups and blow downs.
One can exploit the fact that framed links related by
Kirby moves yield homeomorphic manifolds to derive useful VTQFT identities. How-
ever, care is required when manipulating VTQFT diagrams, as only those moves that
do not involve cutting along non-hyperbolic manifolds are meaningful in VTQFT.
In what follows, we show that blow-ups and blow-downs FR± are valid in VTQFT
when the number of strands satisfies n > 0.
Using the PSL(2, Z) relation
e2πih2SP2P1[P0]e2πih1 =
Z
dP3 SP2P3[P0]e−2πih3SP3P1[P0],
(C.48)
one can show that the FR+ move is satisfied for a single strand:
Z
dPρ0(P)
P ′
P
=
Z
dP S1P[1]e2πihSPP ′[1]
P ′
=
P ′
.
(C.49)
A similar result holds for FR−. Using the result for n = 1, the result for any n
follows directly. For example, the case where n = 2 is given by:
Z
dPρ0(P)
P
=
Z
dP ′ F1,P ′
Z
dPρ0(P)
P ′
P
(C.50)
=
Z
dP ′ F1,P ′
P ′
=
,
and so on for n > 2.
– 108 –
References
[1] E. Witten, (2+1)-Dimensional Gravity as an Exactly Soluble System, Nucl. Phys.
B 311 (1988) 46.
[2] A. Belin and J. de Boer, Random statistics of OPE coefficients and Euclidean
wormholes, Class. Quant. Grav. 38 (2021) 164001 [2006.05499].
[3] J. Chandra, S. Collier, T. Hartman and A. Maloney, Semiclassical 3D gravity as an
average of large-c CFTs, 2203.06511.
[4] J. Cotler and K. Jensen, AdS3 gravity and random CFT, JHEP 04 (2021) 033
[2006.08648].
[5] T. G. Mertens, J. Sim´on and G. Wong, A proposal for 3d quantum gravity and its
bulk factorization, JHEP 06 (2023) 134 [2210.14196].
[6] G. Di Ubaldo and E. Perlmutter, AdS3/RMT2 Duality, 2307.03707.
[7] A. Belin, J. de Boer, D. L. Jafferis, P. Nayak and J. Sonner, Approximate CFTs
and Random Tensor Models, 2308.03829.
[8] D. L. Jafferis, L. Rozenberg and G. Wong, 3d gravity as a random ensemble, JHEP
02 (2025) 208 [2407.02649].
[9] J.-M. Schlenker and E. Witten, No ensemble averaging below the black hole
threshold, JHEP 07 (2022) 143 [2202.01372].
[10] J. de Boer, D. Liska, B. Post and M. Sasieta, A principle of maximum ignorance
for semiclassical gravity, 2311.08132.
[11] S. Collier, L. Eberhardt and M. Zhang, Solving 3d Gravity with Virasoro TQFT,
2304.13650.
[12] S. Collier, L. Eberhardt and M. Zhang, 3d gravity from Virasoro TQFT:
Holography, wormholes and knots, SciPost Phys. 17 (2024) 134 [2401.13900].
[13] J. de Boer, D. Liska and B. Post, Multiboundary wormholes and OPE statistics,
JHEP 10 (2024) 207 [2405.13111].
[14] J. de Boer, J. Kames-King and B. Post, Surgery and statistics in 3d gravity,
2506.04151.
[15] T. Hartman, Triangulating quantum gravity in AdS3, 2507.12696.
[16] T. Hartman, Conformal Turaev-Viro Theory, 2507.11652.
[17] J. Chandra, Statistics in 3d gravity from knots and links, JHEP 12 (2025) 139
[2508.10864].
[18] C. Yan, More on torus wormholes in 3d gravity, JHEP 11 (2023) 039 [2305.10494].
[19] J. Chandra, T. Hartman and V. Meruliya, Statistics of three-dimensional black
holes from Liouville line defects, JHEP 11 (2024) 090 [2404.15183].
– 109 –
[20] L. Eberhardt, Notes on crossing transformations of Virasoro conformal blocks,
2309.11540.
[21] A. Maloney and E. Witten, Quantum Gravity Partition Functions in Three
Dimensions, JHEP 02 (2010) 029 [0712.0155].
[22] C. A. Keller and A. Maloney, Poincare Series, 3D Gravity and CFT Spectroscopy,
JHEP 02 (2015) 080 [1407.6008].
[23] N. Benjamin, H. Ooguri, S.-H. Shao and Y. Wang, Light-cone modular bootstrap
and pure gravity, Phys. Rev. D 100 (2019) 066029 [1906.04184].
[24] A. Ghosh, H. Maxfield and G. J. Turiaci, A universal Schwarzian sector in
two-dimensional conformal field theories, JHEP 05 (2020) 104 [1912.07654].
[25] H. Maxfield and G. J. Turiaci, The path integral of 3D gravity near extremality; or,
JT gravity with defects as a matrix integral, JHEP 01 (2021) 118 [2006.11317].
[26] N. Benjamin, S. Collier and A. Maloney, Pure Gravity and Conical Defects, JHEP
09 (2020) 034 [2004.14428].
[27] G. Di Ubaldo and E. Perlmutter, AdS3 Pure Gravity and Stringy Unitarity, Phys.
Rev. Lett. 132 (2024) 041602 [2308.01787].
[28] S. Giombi, A. Maloney and X. Yin, One-loop Partition Functions of 3D Gravity,
JHEP 08 (2008) 007 [0804.1773].
[29] A. Belin, J. de Boer and D. Liska, Non-Gaussianities in the statistical distribution
of heavy OPE coefficients and wormholes, JHEP 06 (2022) 116 [2110.14649].
[30] T. Anous, A. Belin, J. de Boer and D. Liska, OPE statistics from higher-point
crossing, JHEP 06 (2022) 102 [2112.09143].
[31] X. Yin, On Non-handlebody Instantons in 3D Gravity, JHEP 09 (2008) 120
[0711.2803].
[32] J. M. Maldacena and L. Maoz, Wormholes in AdS, JHEP 02 (2004) 053
[hep-th/0401024].
[33] D. Marolf and J. E. Santos, AdS Euclidean wormholes, Class. Quant. Grav. 38
(2021) 224002 [2101.08875].
[34] P. Saad, S. H. Shenker and D. Stanford, JT gravity as a matrix integral,
1903.11115.
[35] D. Marolf and H. Maxfield, Transcending the ensemble: baby universes, spacetime
wormholes, and the order and disorder of black hole information, JHEP 08 (2020)
044 [2002.08950].
[36] D. Stanford, More quantum noise from wormholes, 2008.08570.
[37] J. M. Deutsch, Quantum statistical mechanics in a closed system, Physical Review
A 43 (1991) 2046.
[38] M. Srednicki, Chaos and quantum thermalization, Physical Review E 50 (1994) 888.
– 110 –
[39] L. Foini and J. Kurchan, Eigenstate thermalization hypothesis and out of time
order correlators, Phys. Rev. E 99 (2019) 042139 [1803.10658].
[40] S. Pappalardi, L. Foini and J. Kurchan, Eigenstate Thermalization Hypothesis and
Free Probability, Phys. Rev. Lett. 129 (2022) 170603 [2204.11679].
[41] D. L. Jafferis, D. K. Kolchmeyer, B. Mukhametzhanov and J. Sonner, Matrix
Models for Eigenstate Thermalization, Phys. Rev. X 13 (2023) 031033
[2209.02130].
[42] A. Belin, J. de Boer, P. Nayak and J. Sonner, Generalized spectral form factors and
the statistics of heavy operators, JHEP 11 (2022) 145 [2111.06373].
[43] F. M. Haehl, C. Marteau, W. Reeves and M. Rozali, Symmetries and spectral
statistics in chaotic conformal field theories, JHEP 07 (2023) 196 [2302.14482].
[44] J. Boruch, G. Di Ubaldo, F. M. Haehl, E. Perlmutter and M. Rozali,
Modular-Invariant Random Matrix Theory and AdS3 Wormholes, Phys. Rev. Lett.
135 (2025) 121602 [2503.00101].
[45] W. P. Thurston, Three dimensional manifolds, Kleinian groups and hyperbolic
geometry, Bulletin (New Series) of the American Mathematical Society 6 (1982)
357 .
[46] W. P. Thurston, Three-Dimensional Geometry and Topology, Volume 1. Princeton
University Press, 1997.
[47] A. Maloney, H. Maxfield and G. S. Ng, A conformal block Farey tail, JHEP 06
(2017) 117 [1609.02165].
[48] W. P. Thurston, Hyperbolic structures on 3-manifolds. i: Deformation of
acylindrical manifolds, Annals of Mathematics 124 (1986) 203.
[49] O. Janssen, M. Mirbabayi and P. Zograf, Gravity as an ensemble and the moment
problem, JHEP 06 (2021) 184 [2103.12078].
[50] E. Perlmutter, An L-function Approach to Two-Dimensional Conformal Field
Theory, 2509.21672.
[51] T. Hartman, C. A. Keller and B. Stoica, Universal Spectrum of 2d Conformal Field
Theory in the Large c Limit, JHEP 09 (2014) 118 [1405.5137].
[52] S. Collier, A. Maloney, H. Maxfield and I. Tsiares, Universal dynamics of heavy
operators in CFT2, JHEP 07 (2020) 074 [1912.00222].
[53] A. Belin, A. Maloney and F. Seefeld, A measure on the space of CFTs and pure 3D
gravity, 2509.04554.
[54] A. A. Belavin, A. M. Polyakov and A. B. Zamolodchikov, Infinite Conformal
Symmetry in Two-Dimensional Quantum Field Theory, Nucl. Phys. B 241 (1984)
333.
[55] A. Hatcher and W. Thurston, A presentation for the mapping class group of a
closed orientable surface, Topology 19 (1980) 221.
– 111 –
[56] B. Bakalov and A. Kirillov, On the Lego-Teichm¨uller game, Transformation Groups
5 (2000) 207.
[57] G. W. Moore and N. Seiberg, Classical and Quantum Conformal Field Theory,
Commun. Math. Phys. 123 (1989) 177.
[58] W. B. R. Lickorish, A finite set of generators for the homeotopy group of a
2-manifold, Mathematical Proceedings of the Cambridge Philosophical Society 60
(1964) 769–778.
[59] S. P. Humphries, Generators for the mapping class group, in Topology of
Low-Dimensional Manifolds (R. Fenn, ed.), (Berlin, Heidelberg), pp. 44–47,
Springer Berlin Heidelberg, 1979.
[60] J. Cardy, A. Maloney and H. Maxfield, A new handle on three-point coefficients:
OPE asymptotics from genus two modular invariance, JHEP 10 (2017) 136
[1705.05855].
[61] B. Ponsot and J. Teschner, Liouville bootstrap via harmonic analysis on a
noncompact quantum group, hep-th/9911110.
[62] B. Ponsot and J. Teschner, Clebsch-Gordan and Racah-Wigner coefficients for a
continuous series of representations of Uq(sl(2, R)), Commun. Math. Phys. 224
(2001) 613 [math/0007097].
[63] J. Teschner and G. Vartanov, 6j symbols for the modular double, quantum
hyperbolic geometry, and supersymmetric gauge theories, Lett. Math. Phys. 104
(2014) 527 [1202.4698].
[64] J. Teschner and G. S. Vartanov, Supersymmetric gauge theories, quantization of
Mflat, and conformal field theory, Adv. Theor. Math. Phys. 19 (2015) 1
[1302.3778].
[65] C. Murthy and M. Srednicki, Bounds on chaos from the eigenstate thermalization
hypothesis, Phys. Rev. Lett. 123 (2019) 230606 [1906.10808].
[66] L. D’Alessio, Y. Kafri, A. Polkovnikov and M. Rigol, From quantum chaos and
eigenstate thermalization to statistical mechanics and thermodynamics, Adv. Phys.
65 (2016) 239 [1509.06411].
[67] A. Altland and J. Sonner, Late time physics of holographic quantum chaos, SciPost
Phys. 11 (2021) 034 [2008.02271].
[68] P. Saad, S. H. Shenker and D. Stanford, A semiclassical ramp in SYK and in
gravity, 1806.06840.
[69] J. S. Cotler, G. Gur-Ari, M. Hanada, J. Polchinski, P. Saad, S. H. Shenker et al.,
Black Holes and Random Matrices, JHEP 05 (2017) 118 [1611.04650].
[70] J. Cotler and K. Jensen, AdS3 wormholes from a modular bootstrap, JHEP 11
(2020) 058 [2007.15653].
[71] F. M. Haehl, W. Reeves and M. Rozali, Symmetries and spectral statistics in
– 112 –
chaotic conformal field theories. Part II. Maass cusp forms and arithmetic chaos,
JHEP 12 (2023) 161 [2309.00611].
[72] F. M. Haehl, W. Reeves and M. Rozali, Euclidean wormholes in two-dimensional
conformal field theories from quantum chaos and number theory, Phys. Rev. D 108
(2023) L101902 [2309.02533].
[73] D. L. Jafferis, L. Rozenberg, D. Sarkar and D. Wang, On random matrix statistics
of 3d gravity, 2512.05045.
[74] M. V. Berry, Semiclassical theory of spectral rigidity, Proceedings of the Royal
Society of London. Series A, Mathematical and Physical Sciences 400 (1985) 229.
[75] D. Sullivan, On the ergodic theory at infinity of an arbitrary discrete group of
hyperbolic motions, in Riemann Surfaces and Related Topics: Proceedings of the
1978 Stony Brook Conference, vol. 97 of Annals of Mathematics Studies,
pp. 465–496. Princeton University Press, 1981.
[76] B. Wajnryb, Mapping class group of a surface is generated by two elements,
Topology 35 (1996) 377.
[77] B. Wajnryb, Mapping class group of a handlebody, Fundamenta Mathematicae 158
(1998) 195.
[78] S. Hensel, A primer on handlebody groups, 2018,
https://api.semanticscholar.org/CorpusID:211542546.
[79] A. B. Zamolodchikov, Conformal symmetry in two dimensions: An explicit
recurrence formula for the conformal partial wave amplitude, Commun. Math.
Phys. 96 (1984) 419.
[80] L. Hadasz, Z. Jaskolski and P. Suchanek, Recursive representation of the torus
1-point conformal block, JHEP 01 (2010) 063 [0911.2353].
[81] M. Cho, S. Collier and X. Yin, Recursive Representations of Arbitrary Virasoro
Conformal Blocks, JHEP 04 (2019) 018 [1703.09805].
[82] X. Yin, Partition Functions of Three-Dimensional Pure Gravity, Commun. Num.
Theor. Phys. 2 (2008) 285 [0710.2129].
[83] M. Headrick, A. Maloney, E. Perlmutter and I. G. Zadeh, R´enyi entropies, the
analytic bootstrap, and 3D quantum gravity at higher genus, JHEP 07 (2015) 059
[1503.07111].
[84] J. D. Brown and M. Henneaux, Central Charges in the Canonical Realization of
Asymptotic Symmetries: An Example from Three-Dimensional Gravity, Commun.
Math. Phys. 104 (1986) 207.
[85] B. Post and I. Tsiares, A non-rational Verlinde formula from Virasoro TQFT,
JHEP 04 (2025) 015 [2411.07285].
[86] W. P. Thurston, On the geometry and dynamics of diffeomorphisms of surfaces,
Bulletin (New Series) of the American Mathematical Society 19 (1988) 417.
– 113 –
[87] J. Abajian, F. Aprile, R. C. Myers and P. Vieira, Correlation functions of huge
operators in AdS3/CFT2: domes, doors and book pages, JHEP 03 (2024) 118
[2307.13188].
[88] A. Maloney and E. Witten, Averaging over Narain moduli space, JHEP 10 (2020)
187 [2006.04855].
[89] S. Collier and A. Maloney, Wormholes and spectral statistics in the Narain
ensemble, JHEP 03 (2022) 004 [2106.12760].
[90] A. Ishii, K. Kishimoto, H. Moriuchi and M. Suzuki, A table of genus two
handlebody-knots up to six crossings, Journal of Knot Theory and Its Ramifications
21 (2012) 1250035.
[91] W. P. Thurston, Hyperbolic structures on 3-manifolds, ii: Surface groups and
3-manifolds which fiber over the circle, Collected works of William P. Thurston
with commentary 2 (1986) 79.
[92] D. Sullivan, On the ergodic theory at infinity of an arbitrary discrete group of
hyperbolic motions, in Riemann Surfaces Related Topics (AM-97), Volume 97,
pp. 465–496. Princeton University Press, 2016.
[93] G. Higman, B. H. Neumann and H. Neuman, Embedding theorems for groups,
Journal of the London Mathematical Society s1-24 (1949) 247
[https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/jlms/s1-24.4.247].
[94] C. T. C. Wall, Homological Group Theory, London Mathematical Society Lecture
Note Series. Cambridge University Press, 1979.
[95] J.-P. Serre, Trees. Springer Science & Business Media, 2002.
[96] A. Karrass and D. Solitar, The free product of two groups with a malnormal
amalgamated subgroup, Canadian Journal of Mathematics 23 (1971) 933.
[97] user HJRW, Centralizers in amalgamated free products, Sept., 2013. MathOverflow
question, viewed 09/09/2025,
https://mathoverflow.net/questions/142949/centralizers-in-amalgamated-free-
products.
[98] R. Brown, Topology and Groupoids: A Geometric Account of General Topology,
Homotopy Types and the Fundamental Groupoid. Ellis Horwood, 2020.
[99] K. Yoshida, The minimal volume orientable hyperbolic 3-manifold with 4 cusps,
Pacific Journal of Mathematics 266 (2013) 457.
[100] G. Bellettini, G. Paolini, M. Paolini and Y.-S. Wang, A table of genus two
handlebody-knots with seven crossings, 2511.12194.
[101] H. Maxfield, S. Ross and B. Way, Holographic partition functions and phases for
higher genus Riemann surfaces, Class. Quant. Grav. 33 (2016) 125018
[1601.00980].
– 114 –
[102] S. Kinoshita, On elementary ideals of polyhedra in the 3-sphere, Pacific Journal of
Mathematics 42 (1972) 89.
[103] A. Ishii, K. Kishimoto, H. Moriuchi and M. Suzuki, A table of genus two
handlebody-knots up to six crossings, Journal of Knot Theory and Its Ramifications
21 (2012) 1250035, 9 pp.
[104] M. Ozawa and S. A. Taylor, Two more proofs that the kinoshita graph is knotted,
The American Mathematical Monthly 126 (2019) 352.
[105] M. Mirzakhani, Simple geodesics and Weil-Petersson volumes of moduli spaces of
bordered Riemann surfaces, Invent. Math. 167 (2006) 179.
[106] B. Eynard and N. Orantin, Invariants of algebraic curves and topological
expansion, Commun. Num. Theor. Phys. 1 (2007) 347 [math-ph/0702045].
[107] D. L. Jafferis, L. Rozenberg and D. Wang, Open-closed 3d gravity as a random
ensemble, JHEP 10 (2025) 228 [2506.19817].
[108] D. L. Jafferis, D. K. Kolchmeyer, B. Mukhametzhanov and J. Sonner, JT gravity
with matter, generalized ETH, and Random Matrices, 2209.02131.
[109] N. Afkhami-Jeddi, H. Cohn, T. Hartman and A. Tajdini, Free partition functions
and an averaged holographic duality, JHEP 01 (2021) 130 [2006.04839].
[110] S. Datta, S. Duary, P. Kraus, P. Maity and A. Maloney, Adding flavor to the
Narain ensemble, JHEP 05 (2022) 090 [2102.12509].
[111] N. Benjamin, C. A. Keller, H. Ooguri and I. G. Zadeh, Narain to Narnia,
Commun. Math. Phys. 390 (2022) 425 [2103.15826].
[112] A. Castro, M. R. Gaberdiel, T. Hartman, A. Maloney and R. Volpato, The Gravity
Dual of the Ising Model, Phys. Rev. D 85 (2012) 024032 [1111.1987].
[113] C.-M. Jian, A. W. W. Ludwig, Z.-X. Luo, H.-Y. Sun and Z. Wang, Establishing
strongly-coupled 3D AdS quantum gravity with Ising dual using all-genus partition
functions, JHEP 10 (2020) 129 [1907.06656].
[114] V. Meruliya and S. Mukhi, AdS3 gravity and RCFT ensembles with multiple
invariants, JHEP 08 (2021) 098 [2104.10178].
[115] V. Meruliya, S. Mukhi and P. Singh, Poincar´e Series, 3d Gravity and Averages of
Rational CFT, JHEP 04 (2021) 267 [2102.03136].
[116] J. Dong, T. Hartman and Y. Jiang, Averaging over moduli in deformed WZW
models, JHEP 09 (2021) 185 [2105.12594].
[117] O. Aharony, A. Dymarsky and A. D. Shapere, Holographic description of Narain
CFTs and their code-based ensembles, JHEP 05 (2024) 343 [2310.06012].
[118] A. Dymarsky and A. Shapere, TQFT gravity and ensemble holography, JHEP 02
(2025) 091 [2405.20366].
[119] A. Dymarsky, J. Henriksson and B. McPeak, Holographic duality from Howe
duality: Chern-Simons gravity as an ensemble of code CFTs, 2504.08724.
– 115 –
[120] A. Barbar, Automorphism-weighted ensembles from TQFT gravity, 2511.04311.
[121] N. Angelinos, Abelian 3D TQFT gravity, ensemble holography and stabilizer states,
2509.26052.
[122] I. Romaidis and I. Runkel, CFT Correlators and Mapping Class Group Averages,
Commun. Math. Phys. 405 (2024) 247 [2309.14000].
[123] R. C. Kirby, The Topology of 4-Manifolds. Springer Berlin Heidelberg, Berlin,
Heidelberg, 1989, 10.1007/BFb0089039.
[124] N. Aghaei, M. K. Pawelkiewicz and M. Yamazaki, Towards Super Teichm¨uller Spin
TQFT, Adv. Theor. Math. Phys. 26 (2022) 245 [2008.09829].
[125] A. Bhattacharyya, S. Ghosh, P. Nandi and S. Pal, 3D N = 1 supergravity from
Virasoro TQFT: gravitational partition function and Out-of-time-order correlator,
JHEP 02 (2025) 027 [2408.01538].
[126] L.-Y. Hung and Y. Jiang, Building up quantum spacetimes with BCFT Legos,
2404.00877.
[127] D. Wang, Z. Wang and Z. Wei, Wormholes with ends of the world, JHEP 09
(2025) 166 [2504.12278].
[128] L.-Y. Hung, Y. Jiang and B.-X. Lao, Universal Structures and Emergent Geometry
from Large-c BCFT Ensemble, 2504.21660.
[129] H. Geng, L.-Y. Hung and Y. Jiang, It from ETH: Multi-interval Entanglement and
Replica Wormholes from Large-c BCFT Ensemble, 2505.20385.
[130] I. Tsiares, Universal dynamics in non-orientable CFT2, JHEP 09 (2025) 095
[2011.09250].
[131] L. Eberhardt, Summing over Geometries in String Theory, JHEP 05 (2021) 233
[2102.12355].
[132] B. Martelli, An introduction to geometric topology, 1610.02592.
[133] H. Rubinstein and M. Scharlemann, Genus two heegaard splittings of orientable
three-manifolds, Geometry and Topology Monographs 2 (1999) 489.
[134] X. Yin, J. Tang and F. Lei, On maximal collections of essential annuli in a
handlebody ii, Journal of Knot Theory and Its Ramifications 18 (2009) 199.
[135] A. Ishii, Moves and invariants for knotted handlebodies, Algebraic and Geometric
Topology 8 (2008) 1403 .
[136] S. Friedl, “Full topology lecture notes (4785 pages).”
https://friedl.app.uni-regensburg.de, 2024.
[137] V. Fateev, A. B. Zamolodchikov and A. B. Zamolodchikov, Boundary Liouville field
theory. 1. Boundary state and boundary two point function, hep-th/0001012.
[138] J. Teschner, Remarks on Liouville theory with boundary, PoS tmr2000 (2000) 041
[hep-th/0009138].
– 116 –
[139] B. Ponsot and J. Teschner, Boundary Liouville field theory: Boundary three point
function, Nucl. Phys. B 622 (2002) 309 [hep-th/0110244].
[140] K. Hosomichi, Bulk boundary propagator in Liouville theory on a disc, JHEP 11
(2001) 044 [hep-th/0108093].
[141] I. Nidaiev and J. Teschner, On the relation between the modular double of
Uq(sl(2, R)) and the quantum Teichmueller theory, 1302.3454.
[142] S. Takahashi, Anyon condensation in Virasoro TQFT: wormhole factorization,
JHEP 06 (2025) 243 [2412.11486].
[143] I. M. Gel’fand and G. E. Shilov, Generalized Functions, Volume 2: Spaces of
Fundamental and Generalized Functions. Academic Press, New York, 1968.
[144] H. Maxfield, Quantum corrections to the BTZ black hole extremality bound from
the conformal bootstrap, JHEP 12 (2019) 003 [1906.04416].
[145] J. H. Przytycki, R. P. Bakshi, D. Ibarra, G. Montoya-Vega and D. Weeks, Lectures
in Knot Theory. An Exploration of Contemporary Topics. Springer, Cham, 2024,
10.1007/978-3-031-40044-5.
[146] R. E. Gompf and A. I. Stipsicz, 4-Manifolds and Kirby calculus, Graduate studies
in mathematics vol. 20. American Mathematical Society, Providence R.I, 1999.
[147] T. Ohtsuki, Quantum Invariants: A Study of Knots, 3-manifolds, and Their Sets,
K & E series on knots and everything. World Scientific, 2002.
[148] W. B. R. Lickorish, A representation of orientable combinatorial 3-manifolds,
Annals of Mathematics 76 (1962) 531.
[149] A. H. Wallace, Modifications and cobounding manifolds, Canadian Journal of
Mathematics 12 (1960) 503–528.
[150] R. Kirby, A Calculus for Framed Links in S3, Inventiones mathematicae 45 (1978)
35.
[151] R. Fenn and C. Rourke, On Kirby’s calculus of links, Topology 18 (1979) 1.
– 117 –
