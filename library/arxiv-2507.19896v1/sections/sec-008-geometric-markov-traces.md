---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-008-geometric-markov-traces
section_title: "Geometric Markov traces."
section_number: null
pages: 9-12
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — WegiveasimpleconstructionofMarkovtracesforIwahori-Heckealgebrasassociated with infinite series of crystallographic Coxeter groups."
---
n : Hv,v(Bn) → A(a), trD
n :
H(Dn)→ A(a) studied in [Gom06], [WW11] are specializations of traces trX
n,y sat-
isfying the extension of the properties (U1), (M2) for the embeddingsB0→ B1 and
D1→D2,D 0→D1. In particular, these traces satisfy
trB
1 (t0) =v−v−1, trD
1 (t1) = trD
1 (t1′) =v−v−1, trD
2 (t1t1′) = (v−v−1)2.
The condition ontrB
1 forces y =v−v−1 and y−α0 = 0. Thus we get thattrB
n = trζn,
the trace from Theorem 3.1.4.
The conditions ontrD
1 , trD
2 imply that
y2 = trD
2 (U1U2) = trD
2 (t1t−1
1′ ) = trD
2 (t1t1′)−αtrD
2 (t1) =α2−α2(1 +a) =−α2a.
It is easy to see that geometric Markov tracestrB
n, trD
n take values inA[a]. Let
trX,k
n :H(Xn)→A be the coefficient oftrX
n atak. We summarize the above discussion
in the following
Theorem 3.3.1. The functional trB,k
n is represented by thekth elementary symmetric
polynomial in Jucys-Murphy elements:
trB,k
n (h) =⟨ek(JB
1 ,...,J B
n ),h⟩.
Let e′
k(x1,...,x n;α) be the symmetric polynomial in(xi) appearing as a degree2k
homogeneous part in
nY
i=1
(1 +αxi−x2
i ) =
nY
i=1
(v−xi)(v−1 +xi).
whereα =v−v−1. Then
trD,k
n (h) = (−1)k⟨e′
k(jD
1 ,...,j D
n ;α),h⟩.
9
The symmetric polynomiale′
k can be written explicitly as
e′
k =
X
i+j=2k,
i,j≥0
(−1)ivj−ieiej.
Note that the highest a-coefficient is always represented by the “full twist” element
S−1 =en(JX
1 ,...,J X
n ), trX,n
n = trS−1. This recovers the symmetry of the HOMFLY-PT
polynomial observed by Kálmán [Kál09], that was categorified in [GHMN19] in typeA
and in [BT22] in general type.
Remark 3.3.2. The statement analogous to Theorem 3.3.1 was lifted to the level of
Khavanov-Rozansky homology in [BT22]. Namely, there it is shown that the object
representing thekth degree of the invariant has a filtration by the objects representing
products of Jucys-Murphy elements. For an arbitrary Weyl group, the object repre-
senting thekth degree was constructed in [BT22] in terms of some explicit character
sheaves on a reductive groupG with the Weyl groupW. It was also explained how
these character sheaves correspond to exterior powers of the reflection representation
of W. We expect that, if the analogous filtration categorifying expressions in Theo-
rem 3.3.1 can be constructed in typesB and D, the arguments in this paper can be
lifted to the level of Khovanov-Rozansky homology: the pairing⟨,⟩ is categorified to the
Hom-pairing on the Hecke category; the “Serre property” of Proposition 2.4.2 has a cat-
egorical analogue in the description of the Serre functor of the Hecke category [BBM04],
[GHMN19]; elementsjX
n can be expressed using the braid group action on the Hecke
category. Such an extension would, for example, give a geometric interpretation to the
special properties of Markov traces in typesBn and Dn involving the elementsTn,Un.
We hope to address this in a future work.
We would also like to remark that, in typeA, the fact that Jucys-Murphy elements
and their symmetric polynomials come from the extended affine Hecke algebra has an
interpretation in terms of geometric representation theory, see [GNR16], [OR19] and
[Tol24]. We do not know if this interpretation can be extended to other types.
References
[BBM04] Aleksandr Beilinson, Roman Bezrukavnikov, and Ivan Mirković. Tilting
exercises. Moscow Mathematical Journal, 4(3):547–557, 2004.
[BT22] Roman Bezrukavnikov and Kostiantyn Tolmachov. Monodromic model
for Khovanov–Rozansky homology.Journal für die reine und angewandte
Mathematik (Crelles Journal), 2022(787):79–124, June 2022.
[Gec98] Meinolf Geck. Trace functions on Iwahori-Hecke algebras. Banach Center
Publications, 42(1):87–109, 1998.
[GHMN19] Eugene Gorsky, Matthew Hogancamp, Anton Mellit, and Keita Nakagane.
Serre duality for Khovanov–Rozansky homology. Selecta Mathematica,
25(5):79, 2019.
[GL97] Meinolf Geck and Sofia Lambropoulou. Markov traces and knot invariants
related to Iwahori-Hecke algebras of type B. Journal für die reine und
angewandte Mathematik, 485:191–214, 1997.
10
[GNR16] EugeneGorsky, AndreiNeguţ, andJacobRasmussen. FlagHilbertschemes,
colored projectors and Khovanov-Rozansky homology. arXiv preprint
arXiv:1608.07308, 2016.
[Gom06] Yasushi Gomi. The markov traces and the fourier transforms. Journal of
Algebra, 303(2):566–591, 2006.
[GP00] Meinolf Geck and Götz Pfeiffer. Characters of finite Coxeter groups and
Iwahori-Hecke algebras. Number 21. Oxford University Press, 2000.
[HL25] Quoc P. Ho and Penghui Li. Relative serre duality for hecke categories.
arXiv preprint arXiv:2504.12798, 2025.
[Jon87] Vaughan F. R. Jones. Hecke algebra representations of braid groups and
link polynomials. In New Developments In The Theory Of Knots, pages
20–73. World Scientific, 1987.
[Kál09] Tamás Kálmán. Meridian twisting of closed braids and the Homfly poly-
nomial. Mathematical Proceedings of the Cambridge Philosophical Society,
146(03):649, May 2009.
[Kho07] Mikhail Khovanov. Triply-graded link homology and Hochschild homology
of Soergel bimodules. International Journal of Mathematics, 18(08):869–
885, 2007.
[Lam94] Sofia Lambropoulou. Solid torus links and hecke algebras of b-type. InPro-
ceedings of the Conference on Quantum Topology (Manhattan, KS, 1993),
pages 225–245. World Sci. Publ. Co., Inc. River Edge, NJ, 1994.
[Lus83] George Lusztig. Singularities, character formulas, and a q-analog of weight
multiplicities. In Analyse et Topologie Sur Les Espaces Singuliers. CIRM,
6 - 10 Juillet 1981. (Actes Du Colloque de Luminy 1981). II - III. 1983.
[OR19] Alexei Oblomkov and Lev Rozansky. Affine braid group, JM elements and
knot homology. Transformation Groups, 24(2):531–544, June 2019.
[Ram97] Arun Ram. Seminormal representations of weyl groups and iwahori-hecke
algebras. Proceedings of the London Mathematical Society, 75(1):99–133,
1997.
[RR03] Arun Ram and Jacqui Ramagge. Affine Hecke Algebras, Cyclotomic Hecke
Algebras and Clifford Theory. InA Tribute to C. S. Seshadri: Perspectives
in Geometry and Representation Theory, pages 428–466, Gurgaon, 2003.
Hindustan Book Agency.
[Sag25] Sage Developers. SageMath, the Sage Mathematics Software System (Ver-
sion 10.6), 2025. https://www.sagemath.org.
[Tol24] Kostiantyn Tolmachov. Linear structure on a finite Hecke category in type
A. arXiv preprint arXiv:2403.19734, 2024.
[WW11] Ben Webster and Geordie Williamson. The geometry of Markov traces.
Duke Mathematical Journal, 160(2):401 – 419, 2011.
K. Tolmachov, Department of Mathematics, University of Hamburg, Hamburg,
Germany
E-mail address : tolmak@khtos.com
11
H. Zhylinskyi, Department of Mathematics, Jagiellonian University, Krakow,
Poland
E-mail address : georgyzhilinsky144@gmail.com
12
