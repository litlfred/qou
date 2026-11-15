---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-040-82-a-decomposition-joint-with-hirasawa-ishiwata
section_title: "$A$-decomposition (joint with Hirasawa-Ishiwata)"
section_number: 8.2
pages: 63-68
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
63
In ﬁgure 8, we perform the move (a) →(b), sliding B along N. The last surface F′, in ﬁgure 8 (b), is Murasugi sum of
a ﬁbre surface spanning the (2,2,−2)-pretzel link and ˜F, where ˜F consists of k −1 copies of F′
0 and the band N. By
induction on k, we see that F′ is a ﬁbre surface, and hence ˆβ is a ﬁbred link.
✷
A.2.
A-decomposition (joint with Hirasawa-Ishiwata)
For the proof of theorem 1.2 we introduce the A-decomposition due to T. Kobayashi [Ko].
A sutured manifold in the sense of Gabai [Ga3] can be understood as a pair (L,H) consisting of a closed 3-dimensional
submanifold H of R3 with boundary S = ∂H a connected surface, and a set of oriented loops L ⊂H. We require that
one can orient the connected components of S \ L so that the induced orientations on L coincide from both sides of L
(in particular a connected component of S\L never bounds to itself along a loop of L), and are given by the orientation
of L.
Let F be a connected Seifert surface of a(n oriented) link L = ∂F. We embed F as F ×{0.5} into the bicolar H = F ×I
(with I = [0,1]). Then (L,H) becomes a sutured manifold. We call it canonical sutured manifold C(F) of F.
We describe some basic operations on sutured manifolds (L,H).
A decomposition disk D is a disk with P = ∂D ⊂∂H, properly embedded in the complement of H (i.e. D ∩H = P).
We require that D is not parallel to S = ∂H, and satisﬁes P∩F̸ = ∅. We assume also that the intersection of P and F
is transversal, so that it is a collection of points.
Since L = ∂F is separating on S, the intersection D∩L = P∩F is an even number of points, and the orientation of L
at the intersection points is alternating (with respect to the orientation of the loop P). See ﬁgure 10 (a).
D
L
D
L
L
a
−→
D
(a)
(b)
Figure 10
Then L ∩P separates P into a collection of intervals or arcs. Let a be such an arc. An A-operation on D along a is a
transformation of (L,H) into a sutured manifold (L′,H), where L′ is obtained by splicing L along a. See ﬁgure 10 (b).
A product decomposition along D is a similar operation, due to Gabai [Ga3], and can be described as an A-operation if
|L∩D| = 2 (in which case which of the two arcs is chosen is irrelevant), followed by a subsequent gluing of a D2 ×I
into H along a neighborhood N(P) ≃S1 ×I of P on S.
Deﬁnition A.2 We deﬁne a sutured manifold (L,H) to be A-decomposable as follows:
1) Assume H is a standardly embedded handlebody (i.e. so that S3 \ H is also one). If L is a collection of trivial
loops on ∂H, and all loops bound disjoint disks in ∂H, then (L,H) is A-decomposable.
2) If (L′,H′) is obtained from (L,H) by a product decomposition (along some decomposition disk D), and (L′,H′)
is A-decomposable, then so is (L,H).
3) Let D be a decomposition disk of H with |L ∩D| = 2n and choose among the 2n arcs on P = ∂D a collection
of n cyclically consecutive arcs a1,...,an. (Consecutive is to mean that, taken with their boundary in L ∩P,
their union is a single interval in P, and not several such intervals.) Let (Li,H) be obtained from (L,H) by
A-decomposition on D along ai for i = 1,...,n. Then if all (Li,H) are A-decomposable, so is (L,H).
64
References
Theorem A.1 (T. Kobayashi [Ko], O. Kakimizu [Kk])
1) A ﬁber surface is a unique incompressible surface.
2) The property a surface to be a unique incompressible surface is invariant under Hopf (de)plumbing.
3) If C(F) is A-decomposable, then F is a unique incompressible surface for L = ∂F.
Now we complete the proof of theorem 1.2.
Proof of theorem 1.2.
Let L be a 3-braid link. If L is split, the splitting sphere also splits any incompressible
surface for L. Since L is a split union of a 2-braid link and an unknot (incl. 2 and 3-component unlinks), the claim is
easy. Excluding split links, corollary 4.2 shows we need to consider only connected Seifert surfaces. It also sufﬁces
to deal with the non-ﬁbered links only. These are equivalent under Hopf (de)plumbing to some of (123)k (k̸ = 0).
For such links, we can modify the transformation of Hirasawa and Murasugi from §A.1. Then we can turn by Hopf
(de)plumbing the surfaces into those like in ﬁgure 8 (a), consisting of k copies of F′
0, but now without the lower band
N. (Figure 9 shows the case k = 4.) Then we use A-decomposition, as shown in ﬁgure 11. One applies A-operations
along the arcs a1,2. We show only the result for a1, the case of a2 and other k is analogous.
✷
References
[Al]
J. W. Alexander, A lemma on systems of knotted curves, Proc. Nat. Acad. Sci. U.S.A. 9 (1923), 93–95.
[Al2]
”
, Topological invariants of knots and links, Trans. Amer. Math. Soc. 30 (1928), 275–306.
[Ar]
E. Artin, Theorie der Z¨opfe, Abh. Math. Sem. Hamburgischen Univ. 4 (1926), 47–72.
[Ar2]
”
, Theory of braids, Ann. of Math. 48(2) (1947), 101–126.
[Be]
D. Bennequin, Entrelacements et ´equations de Pfaff , Soc. Math. de France, Ast´erisque 107-108 (1983), 87–161.
[Bi]
S. Bigelow, Representations of braid groups, Proceedings of the International Congress of Mathematicians, Vol. II (Beijing,
2002), 37–45.
[B]
J. S. Birman, On the Jones polynomial of closed 3-braids, Invent. Math. 81(2) (1985), 287–294.
[BKL]
”
, K. Ko and S. J. Lee, A new approach to the word and conjugacy problems in the braid groups, Adv. Math.
139(2) (1998), 322–353.
[BM]
”
and W. W. Menasco, Studying knots via braids III: Classifying knots which are closed 3 braids, Paciﬁc
J. Math. 161(1993), 25–113.
[BM2]
”
and
”
, Studying links via closed braids II: On a theorem of Bennequin, Topology Appl.
40(1) (1991), 71–82.
[BM3]
”
and
”
, Studying knots via braids VI: A non-ﬁniteness theorem, Paciﬁc J. Math. 156 (1992),
265–285.
[BW]
”
and H. Wenzl, Braids, link polynomials and a new algebra, Trans. Amer. Math. Soc. 313(1) (1989),
249–273.
[Bl]
S. A. Bleiler, Realizing concordant polynomials with prime knots, Paciﬁc J. Math. 100(2) (1982), 249–257.
[BLM] R. D. Brandt, W. B. R. Lickorish and K. Millett, A polynomial invariant for unoriented knots and links, Inv. Math. 74
(1986), 563–573.
[CK]
A. Champanerkar and I. Kofman, On the Mahler measure of Jones polynomials under twisting, Algebr. Geom. Topol. 5
(2005), 1–22.
[Cr]
P. R. Cromwell, Homogeneous links, J. London Math. Soc. (series 2) 39 (1989), 535–552.
[DL]
O. Dasbach and X.-S. Lin, On the Head and the Tail of the Colored Jones Polynomial, Compositio Math. 142(5) (2006),
1332–1342.
[EKT] S. Eliahou, L. H. Kauffman and M. Thistlethwaite, Inﬁnite families of links with trivial Jones polynomial, Topology 42(1)
(2003), 155–169.
[Fi]
T. Fiedler, A small state sum for knots, Topology 32 (2) (1993), 281–294.
References
65
a1
−→
Figure 11: This sequence of diagrams describes the A-decomposition along arc a1 of the
canonical sutured manifold corresponding to the surface in ﬁgure 9. The A-operation is the
change between the ﬁrst and the second diagram. The following diagrams (left to right in
each row) display isotopies and product decompositions, leading ﬁnally to a trivial curve on
a torus. The A-operation along a2 must be performed too, but the decomposition is similar.
66
References
[Fi2]
”
, Gauss sum invariants for knots and links, Kluwer Academic Publishers, Mathematics and Its Applications
Vol 532 (2001).
[FK]
”
and V. Kurlin, A one-parameter approach to knot theory, preprint math.GT/0606381.
[FW]
J. Franks and R. F. Williams, Braids and the Jones-Conway polynomial, Trans. Amer. Math. Soc. 303 (1987), 97–108.
[F&]
P. Freyd, J. Hoste, W. B. R. Lickorish, K. Millett, A. Ocneanu and D. Yetter, A new polynomial invariant of knots and links,
Bull. Amer. Math. Soc. 12 (1985), 239–246.
[Fu]
H. Fujii, Geometric indices and the Alexander polynomial of a knot, Proc. Amer. Math. Soc. 124(9) (1996), 2923–2933.
[Ga]
D. Gabai, The Murasugi sum is a natural geometric operation, Low-dimensional topology (San Francisco, Calif., 1981),
Contemp. Math. 20, 131–143, Amer. Math. Soc., Providence, RI, 1983.
[Ga2]
”
, The Murasugi sum is a natural geometric operation II, Combinatorial methods in topology and algebraic
geometry (Rochester, N.Y., 1982), 93–100, Contemp. Math. 44, Amer. Math. Soc., Providence, RI, 1985.
[Ga3]
”
, Detecting ﬁbred links in S3, Comment. Math. Helv. 61(4) (1986), 519–555.
[Gr]
F. Garside, The braid group and other groups, Q. J. Math. Oxford 20 (1969), 235–264.
[HM]
M. Hirasawa and K. Murasugi, Double-torus ﬁbered knots and pre-ﬁber surfaces, Musubime to Teijigen Topology (Dec.
1999), 43–49.
[HT]
J. Hoste and M. Thistlethwaite, KnotScape, a knot polynomial calculation and table access program, available at http:
//www.math.utk.edu/˜morwen.
[HTW]
”
,
”
and J. Weeks, The ﬁrst 1,701,936 knots, Math. Intell. 20 (4) (1998), 33–48.
[I]
M. Ishikawa, On the Thurston-Bennequin invariant of graph divide links, Math. Proc. Cambridge Philos. Soc. 139(3)
(2005), 487–495.
[J]
V. F. R. Jones, Hecke algebra representations of braid groups and link polynomials, Ann. of Math. 126 (1987), 335–388.
[J2]
”
, A polynomial invariant of knots and links via von Neumann algebras, Bull. Amer. Math. Soc. 12 (1985),
103–111.
[Kk]
O. Kakimizu, Classiﬁcation of the incompressible spanning surfaces for prime knots of ≤10 crossings, Hiroshima Math.
J. 35 (2005), 47–92.
[K]
T. Kanenobu, Relations between the Jones and Q polynomials of 2-bridge and 3-braid links, Math. Ann. 285 (1989),
115–124.
[K2]
”
, Examples on polynomial invariants of knots and links II, Osaka J. Math. 26(3) (1989), 465–482.
[K3]
”
, Examples on polynomial invariants of knots and links, Math. Ann. 275 (1986), 555–572.
[K4]
”
, An evaluation of the ﬁrst derivative of the Q polynomial of a link, Kobe J. Math. 5(2) (1988), 179–184.
[Ka]
L. H. Kauffman, An invariant of regular isotopy, Trans. Amer. Math. Soc. 318 (1990), 417–471.
[Ka2]
”
, State models and the Jones polynomial, Topology 26 (1987), 395–407.
[Kw]
K. Kawamuro, The algebraic crossing number and the braid index of knots and links, Algebr. Geom. Topol. 6 (2006),
2313–2350.
[Ki]
M. E. Kidwell, On the degree of the Brandt-Lickorish-Millett-Ho polynomial of a link, Proc. Amer. Math. Soc. 100(4)
(1987), 755–762.
[Kn]
J. A. Kneissler, Woven braids and their closures, J. Knot Theory Ramiﬁcations 8(2) (1999), 201–214.
[Ko]
T. Kobayashi, Uniqueness of minimal genus Seifert surfaces for links, Topology Appl. 33(3) (1989), 265–279.
[Kr]
D. Kreimer, Knots and Feynman diagrams, Cambridge Lecture Notes in Physics 13, Cambridge University Press, Cam-
bridge, 2000.
[LM]
W. B. R. Lickorish and K. C. Millett, A polynomial invariant for oriented links, Topology 26 (1) (1987), 107–141.
[LT]
”
and M. B. Thistlethwaite, Some links with non-trivial polynomials and their crossing numbers, Comment.
Math. Helv. 63 (1988), 527–539.
[MT]
W. W. Menasco and M. B. Thistlethwaite, The Tait ﬂyping conjecture, Bull. Amer. Math. Soc. 25 (2) (1991), 403–412.
[Mo]
H. R. Morton, Seifert circles and knot polynomials, Proc. Camb. Phil. Soc. 99 (1986), 107–109.
[Mo2]
”
(ed.), Problems, in “Braids”, Santa Cruz, 1986 (J. S. Birman and A. L. Libgober, eds.), Contemp. Math.
78, 557–574.
References
67
[MS]
”
and H. B. Short, The 2-variable polynomial of cable knots, Math. Proc. Cambridge Philos. Soc. 101(2)
(1987), 267–278.
[MS2]
”
and
”
, br9z.p, a Pascal program for calculation of the skein polynomial from braids,
http://www.liv.ac.uk/˜su14/knotprogs.html.
[Mr]
J. Murakami, The Kauffman polynomial of links and representation theory, Osaka J. Math. 24(4) (1987), 745–758.
[Mu]
K. Murasugi, On the braid index of alternating links, Trans. Amer. Math. Soc. 326 (1) (1991), 237–260.
[Mu2]
”
, On closed 3-braids, Memoirs AMS 151 (1974), AMS, Providence.
[Mu3]
”
, Jones polynomial and classical conjectures in knot theory, Topology 26 (1987), 187–194.
[MP]
”
and J. Przytycki, The skein polynomial of a planar star product of two links, Math. Proc. Cambridge
Philos. Soc. 106(2) (1989), 273–276.
[MP2]
”
and
”
, An index of a graph with applications to knot theory, Mem. Amer. Math. Soc. 106
(508) (1993).
[Na]
T. Nakamura, Notes on the braid index of closed positive braids, Topology Appl. 135(1-3) (2004), 13–31.
[Na2]
”
, Braidzel surfaces and the Alexander polynomial, Proceedings of the Workshop “Intelligence of Low
Dimensional Topology”, Osaka City University (2004), 25–34.
[Ni]
Y. Ni, Closed 3-braids are nearly ﬁbred, preprint math.GT/0510243.
[Oh]
Y. Ohyama, On the minimal crossing number and the braid index of links, Canad. J. Math. 45(1) (1993), 117–131.
[Or]
S. Orevkov, Quasipositivity problem for 3-braids, Turkish Journal of Math. 28 (2004), 89–93; also available at http://
picard.ups-tlse.fr/homepage/orevkov.html.
[PV]
M. Polyak and O. Viro, Gauss diagram formulas for Vassiliev invariants, Int. Math. Res. Notes 11 (1994), 445–454.
[PV2]
”
and
”
, On the Casson knot invariant, Knots in Hellas ’98, Vol. 3 (Delphi), J. Knot Theory
Ramiﬁcations 10(5) (2001), 711–738.
[Ro]
D. Rolfsen, Knots and links, Publish or Perish, 1976.
[Ru]
L. Rudolph, Braided surfaces and Seifert ribbons for closed braids, Comment. Math. Helv. 58 (1983), 1–37.
[Ru2]
”
, Quasipositivity as an obstruction to sliceness, Bull. Amer. Math. Soc. (N.S.) 29(1) (1993), 51–59.
[Sc]
O. Schreier, ¨Uber die Gruppen AaBb = 1, Abh. Math. Sem. Univ. Hamburg 3 (1924), 167–169.
[SSW] D. Silver, A. Stoimenow and S. G. Williams, Euclidean Mahler measure and Twisted Links,
math.GT/0412513,
Algebr. Geom. Topol. 6 (2006), 581–602.
[SW]
”
and S. Williams, Coloring link diagrams with a continuous palette, Topology 39 (2000), 1225–1237.
[Sq]
C. Squier, The Burau representation is unitary, Proc. Amer. Math. Soc. 90 (1984), 199–202.
[St]
A. Stoimenow, On polynomials and surfaces of variously positive links, math.GT/0202226, Jour. Europ. Math. Soc.
7(4) (2005), 477–509.
[St2]
”
, The skein polynomial of closed 3-braids, J. Reine Angew. Math. 564 (2003), 167–180.
[St3]
”
, On the crossing number of positive knots and braids and braid index criteria of Jones and Morton-
Williams-Franks, Trans. Amer. Math. Soc. 354(10) (2002), 3927–3954.
[St4]
”
, Coefﬁcients and non-triviality of the Jones polynomial, preprint math.GT/0606255.
[St5]
”
, Diagram genus, generators and applications, preprint.
[St6]
”
, The braid index and the growth of Vassiliev invariants, J. Of Knot Theory and Its Ram. 8(6) (1999),
799–813.
[St7]
”
, Positive knots, closed braids, and the Jones polynomial, math.GT/9805078, Ann. Scuola Norm. Sup.
Pisa Cl. Sci. 2(2) (2003), 237–285.
[St8]
”
, Knots of genus two, preprint math.GT/0303012.
[SV]
”
and A. Vdovina, Counting alternating knots by genus, Math. Ann. 333 (2005), 1–27.
[ST]
C. Sundberg and M. B. Thistlethwaite, The rate of growth of the number of prime alternating links and tangles, Paciﬁc
Journal of Math. 182 (2) (1998), 329–358.
[Th]
M. B. Thistlethwaite, On the Kauffman polynomial of an adequate link, Invent. Math. 93(2) (1988), 285–296.
[Th2]
”
, A spanning tree expansion for the Jones polynomial, Topology 26 (1987), 297–309.
68
References
[Tr]
P. Traczyk, 3-braids with proportional Jones polynomials, Kobe J. Math. 15(2) (1998), 187–190.
[Vo]
P. Vogel, Representation of links by braids: A new algorithm, Comment. Math. Helv. 65 (1990), 104–113.
[Wi]
R. F. Williams, Lorenz knots are prime, Ergodic Theory Dynam. Systems 4(1) (1984), 147–163.
[Wo]
S. Wolfram, Mathematica — a system for doing mathematics by computer, Addison-Wesley, 1989.
[Xu]
Peijun Xu, The genus of closed 3-braids, J. Knot Theory Ramiﬁcations 1(3) (1992), 303–326.
[Y]
S. Yamada, The minimal number of Seifert circles equals the braid index, Invent. Math. 88 (1987), 347–356.
[Yo]
Y. Yokota, Polynomial invariants of positive links, Topology 31(4) (1992), 805–811.
