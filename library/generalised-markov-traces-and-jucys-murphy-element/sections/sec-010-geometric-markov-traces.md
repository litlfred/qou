---
doc_id: generalised-markov-traces-and-jucys-murphy-element
doc_title: "Glasgow Mathematical Journal (2026), 1–10"
section_id: sec-010-geometric-markov-traces
section_title: "Geometric Markov traces"
section_number: null
pages: 8-10
source_pdf: Generalised_Markov_traces_and_Jucys-Murphy_element.pdf
source_sha256: 9246e10a44d0b4aa
toc_source: outline
doc_brief: "Glasgow Mathematical Journal (2026), 1–10 — We give a simple construction of Markov traces for Iwahori–Hecke algebras associated with the crystallographic Coxeter groups of types An, Bn and Dn."
---
Markov traces trB
n : Hv,v(Bn) →A(a), trD
n : H(Dn) →A(a) studied in [7, 20] are specialisations of traces
trX
n,y satisfying the extension of the properties (U1) and (M2) for the embeddings B0 →B1 and D1 →
D2, D0 →D1. Since these traces are of geometric origin, we call them ‘geometric Markov traces’. In
particular, these traces satisfy
trB
1(t0) = v −v−1, trD
1 (t1) = v −v−1, trD
2 (t1t1′) = (v −v−1)2.
The condition on trB
1 forces y = v −v−1 and y + α0 = 0. Thus, we get that trB
n = trζn, the trace from
Theorem 3.1.4.
The conditions on trD
1 , trD
2 imply that
y2 = trD
2 (U1U2) = trD
2 (t1′t−1
1 ) = trD
2 (t1t1′) −αtrD
2 (t1′) = α2 −α2(1 + a) = −α2a.
It is easy to see that geometric Markov traces trB
n, trD
n take values in A[a]. Let trX,k
n : H(Xn) →A be
the coeﬃcient of trX
n at ak. We summarise the above discussion in the following
Theorem 3.3.1. The functional trB,k
n is represented by the kth elementary symmetric polynomial in Jucys–
Murphy elements:
trB,k
n (h) = ⟨ek(JB
1 , . . . , JB
n ), h⟩.
Let e′
k(x1, . . . , xn; α) be the symmetric polynomial in (xi) appearing as a degree 2k homogeneous
part in
n
i=1
(1 + αxi −x2
i ) =
n
i=1
(v −xi)(v−1 + xi),
where α = v −v−1. Then
trD,k
n (h) = (−1)k⟨e′
k(jD
1 , . . . , jD
n ; α), h⟩.
The symmetric polynomial e′
k can be written explicitly as
e′
k =

i+j=2k,
i,j≥0
(−1)ivj−ieiej.
Note that the highest a-coeﬃcient is always represented by the ‘full twist’ element S−1 =
en(JX
1 , . . . , JX
n ), trX,n
n = trS−1. This recovers the symmetry of the HOMFLY-PT polynomial observed by
Kálmán [11] that was categoriﬁed in [4] in type A and in [2] in general type.
Remark 3.3.2. The statement analogous to Theorem 3.3.1 was lifted to the level of Khovanov–Rozansky
homology in [2]. Namely, there it is shown that the object representing the kth degree of the invariant
has a ﬁltration by the objects representing products of Jucys–Murphy elements. For an arbitrary Weyl
group, the object representing the kth degree was constructed in [2] in terms of some explicit charac-
ter sheaves on a reductive group G with the Weyl group W. It was also explained how these character
sheaves correspond to exterior powers of the reﬂection representation of W. We expect that, if the anal-
ogous ﬁltration categorifying expressions in Theorem 3.3.1 can be constructed in types B and D, the
arguments in this paper can be lifted to the level of Khovanov–Rozansky homology: the pairing ⟨, ⟩is
categoriﬁed to the Hom-pairing on the Hecke category; the ‘Serre property’ of Proposition 2.4.2 has
a categorical analogue in the description of the Serre functor of the Hecke category [1, 4]; elements
jX
n can be expressed using the braid group action on the Hecke category. Such an extension would, for
example, give a geometric interpretation to the special properties of Markov traces in types Bn and Dn
involving the elements Tn, Un. We hope to address this in a future work.
We would also like to remark that, in type A, the fact that Jucys–Murphy elements and their symmetric
polynomials come from the extended aﬃne Hecke algebra has an interpretation in terms of geometric
representation theory, see [6, 15 and 19]. We do not know if this interpretation can be extended to other
types.
Acknowledgements. The results of this paper were obtained while the authors participated in Yulia’s Dream programme. We
would like to thank the programme’s organisers for this wonderful initiative. We would like to thank Mykhailo Barkulov, another
participant of the programme, for helpful discussions.
We have conducted numerical experiments using SageMath software [18] throughout the work on this paper and would like
to thank its developers.
K.T. was funded by the Deutsche Forschungsgemeinschaft SFB 1624 grant, Projektnummer 506632645.
References
[1] A. Beilinson, R. Bezrukavnikov and I. Mirković, Tilting exercises, Mosc. Math. J. 4(2004), no. 3, 547–557.
[2] R. Bezrukavnikov and K. Tolmachov, Monodromic model for Khovanov–Rozansky homology, J. Reine Angew. Math.
2022 (2022), no. 787, 79–124.
[3] M. Geck, Trace functions on Iwahori-Hecke algebras, Banach Center Publ. 42(1998), no. 1, 87–109.
10
Kostiantyn Tolmachov and Heorhii Zhylinskyi
[4] E. Gorsky, M. Hogancamp, A. Mellit and K. Nakagane, Serre duality for Khovanov–Rozansky homology, Sel. Math.
25(2019), no. 5, 79.
[5] M. Geck and S. Lambropoulou, Markov traces and knot invariants related to Iwahori-Hecke algebras of type B, J. Reine
Angew. Math. 485 (1997), 191–214.
[6] E. Gorsky, A. Neguţ and J. Rasmussen, Flag Hilbert schemes, colored projectors and Khovanov-Rozansky homology,
arXiv preprint arXiv:1608.07308, 2016.
[7] Y. Gomi, The Markov traces and the fourier transforms, J. Algebra 303(2006), no. 2, 566–591.
[8] M. Geck and G. Pfeiﬀer, Characters of ﬁnite Coxeter groups and Iwahori-Hecke algebras, Vol. 21., Oxford University
Press, 2000.
[9] Q. P. Ho and P. Li, Relative Serre duality for Hecke categories, arXiv preprint arXiv:2504.12798, 2025.
[10] V. F. R. Jones, “Hecke algebra representations of braid groups and link polynomials” in New Developments in the Theory
of Knots, World Scientiﬁc, 1987, 20–73.
[11] T. Kálmán, Meridian twisting of closed braids and the Homﬂy polynomial, Math. Proc. Camb. Philos. Soc. 146 (2009),
no. 03, 649.
[12] M. Khovanov, Triply-graded link homology and Hochschild homology of Soergel bimodules, Int. J. Math. 18(2007), no.
08, 869–885.
[13] S. Lambropoulou, ”Solid torus links and Hecke algebras of B-type“ in Proceedings of the Conference on Quantum
Topology (Manhattan, KS. 1993), River Edge, NJ, World Sci. Publ. Co., Inc., 1994, 225–245.
[14] G. Lusztig, “Singularities, character formulas, and a q-analog of weight multiplicities” in Analyse et topologie sur les
espaces singuliers (II-III) - 6 - 10 juillet 1981, Astérisque, no. 101–102, 1983.
[15] A. Oblomkov and L. Rozansky, Aﬃne braid group, JM elements and knot homology, Transform Groups 24(2019), no. 2,
531–544.
[16] A. Ram, Seminormal representations of Weyl groups and Iwahori-Hecke algebras, Proc. Lond. Math. Soc. 75(1997), no.
1, 99–133.
[17] A. Ram and J. Ramagge, “Aﬃne Hecke algebras, cyclotomic Hecke algebras and Cliﬀord theory” In A Tribute to C. S.
Seshadri: Perspectives in Geometry and Representation Theory, Hindustan Book Agency, Gurgaon, 2003, 428–466.
[18] Sage Developers, SageMath, the Sage Mathematics Software System (Version 10.6), 2025, https://www.sagemath.org.
[19] K. Tolmachov, Linear structure on a ﬁnite Hecke category in type A, arXiv preprint arXiv:2403.19734, 2024.
[20] B. Webster and G. Williamson, The geometry of Markov traces, Duke Math. J. 160(2011), no. 2, 401–419.
[21] B. Webster and G. Williamson, A geometric construction of colored HOMFLYPT homology, Geom. Topol. 21(2017), no.
5, 2557–2600.
