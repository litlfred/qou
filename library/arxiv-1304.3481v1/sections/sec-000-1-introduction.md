---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-graded colored homology of knots"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
doc_brief: "Quadruply-graded colored homology of knots — W e conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
2. Bosonic and Fermionic generators 7
3. Gradings, Diﬀerentials, Mirror Symmetry 19
4. Examples 35
5. Colored HOMFLY homology for torus knots 47
6. HOMFLY homology from A-model and B-model 55
7. “Bottom row” of the colored HOMFLY homology 61
Appendix A. Rectangle-colored invariants of (2 , m) torus knots 68
Appendix B. Unreduced colored HOMFLY homology 69
References 75
1. Introduction
The categoriﬁcation of quantum knot invariants started with Khov anov’s semi-
nal paper [54], where he deﬁned a doubly-graded homology theory, whose homot opy
type is an invariant of a knot, and such that its graded Euler charac teristic is equal
to the Jones polynomial. This opened a fast-growing ﬁeld in low-dimens ional topol-
ogy and started work on categoriﬁcation of other quantum knot in variants. Unlike
the quantum polynomial invariants of a knot K, denoted by P g,λ(K)(q), which are
1
2 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
explicitly deﬁned for any representation λ of Lie algebra g, their categoriﬁcations
are known only in very few cases. In particular, in the case of the Lie algebras
sl(N ) — which is the case on which we focus in this paper — the explicit catego ri-
ﬁcation is known in the case of the fundamental representations λ = [55], and in
a very few other cases. In addition, apart from the case of the Jo nes polynomial
(fundamental representation of sl(2)), the deﬁnition of the homology theory is very
complicated, which makes the computation of such invariants extre mely hard.
For a ﬁxed Young diagram λ and a knot K, the sl(N ) quantum polynomi-
als P sl(N ),λ(K)(q) can be organized in a single two-variable λ-colored HOMFLY
polynomial P λ(K)(a, q), so that the sl(N )-quantum polynomials are obtained as
a = qN specializations, i.e.
(1.1) P sl(N ),λ(K)(q) = P λ(K)(a = qN , q).
A triply-graded homology categorifying uncolored ( λ = ) HOMFLY polynomial
was deﬁned in [ 56]. Throughout the paper, we are mainly focusing on the reduced
polynomials, i.e. normalized such that the value of the unknot is equal to 1, and
unless otherwise stated, the (colored) HOMFLY polynomial means t he reduced
(colored) HOMFLY polynomial.
A remarkable property of the quantum knot invariants and their ca tegoriﬁca-
tions is that they are related to many diﬀerent areas of mathematic s and physics, all
of them bringing new viewpoints to this topic. The relationship betwee n quantum
ﬁeld theory, in particular the Chern-Simons theory, and the quant um knot invari-
ants was discovered in celebrated paper by Witten [ 85], and the physics insights
have been extremely fruitful ever since.
In the case of the categoriﬁcations, the realization of knot homolo gies as the
space of certain BPS states gave rise to various prediction on the s tructure of the
(colored) HOMFLY homologies, see e.g. [ 40] for a friendly introduction and a re-
view. Thus, in [ 21] N. Dunﬁeld, the second author and J. Rasmussen predicted
the existence of a triply-graded knot homology theory H (K), whose Euler char-
acteristic is given by the HOMFLY polynomial, and which comes equipped with
the collection of anti-commuting diﬀerentials {dN}N∈Z lifting the sl(N ) specializa-
tion property of the HOMFLY polynomial. More precisely, the diﬀeren tials dN , for
N > 0, are such that the homology of H (K) with respect to dN is isomorphic to
the homologyHsl(N ), (K) that categoriﬁes P sl(N ), (K)(q). Additionally, H (K)
has an involution φ extending the q↔ q−1 symmetry of the HOMFLY polynomial:
(1.2) P (K)(a, q) = P (K)(a, q−1),
It exchanges the positive and negative diﬀerentials: φdN = d−N φ.
Such a rigid structure enabled the computation of triply graded hom ology of
various knots. In addition such a triply-graded homology theory wa s constructed
mathematically in [ 56], and it was shown in [ 74] that it also carries the diﬀerentials
dN with the wanted properties.
In [ 42] the second and the third authors extended this picture and desc ribed
various structures in the colored HOMFLY homology in the case of the symmet-
ric ( Sr) and anti-symmetric (Λ r) representations. For such representation λ and
a knot K one can associate an ( a, q, t)-graded vector space Hλ(K) such that its
Euler characteristic with respect to the t-grading equals to the λ-colored HOMFLY
polynomial P λ(K)(a, q) of K. Like in the uncolored case, these homology theories
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 3
come with the collection of the diﬀerentials corresponding to the sl(N ) specializa-
tions. The main new feature is the existence of another collection of the so-called
colored diﬀerentials which give “dynamics” in the sequence of the homology th e-
oriesHSr
(K), for various r. For every pair of nonnegative integers r and k with
r > k there are two diﬀerent diﬀerentials d+
Sr→Sk and d−
Sr→Sk onHSr
(K) such
that the homology of HSr
(K) with respect to any of the two diﬀerentials d±
Sr→Sk
is isomorphic to HSk
(K).
The involution φ becomes the so-called mirror symmetry in colored homology,
that relates the homologies Hλ(K) and Hλt
(K): there exists an isomorphism be-
tweenHSr
(K) and HΛ r
(K) preserving the a-grading and reversing the q-grading.
It lifts the following relation between the colored HOMFLY polynomials
(1.3) P λ(K)(a, q) = P λt
(K)(a, q−1).
Surprisingly, in [ 42] it was realized that the exponential growth property holds
for certain classes of knots, i.e. the size of the Sr-colored homology grows expo-
nentially in r:
(1.4) dim HSr
(K) =
(
dimH
(K)
) r
.
Although this property does not hold for all knots, it holds for vario us large classes
of knots, like 2-bridge knots and torus knots. Moreover, the reﬁ ned exponential
growth is valid for the two-variable q = 1 specializations of the Poincar´ e polynomials
of the corresponding homology theories.
Such a large predicted structure made possible the explicit computa tion of col-
ored HOMFLY homologies for various knots and colors, that in turn h ave shown
the consistency of all the conjectured properties.
In present article we give more quantitative description of the resu lts of [ 42].
We extend the description of the colored diﬀerentials and the expon ential growth
conjecture to rectangular diagrams λ. This allows us to give a more uniﬁed treat-
ment of the Λ r and Sr colored homology.
The major novelty is endowing the space Hλ(K) with the fourth grading. In
other words, we conjecture the colored HOMFLY homology Hλ(K) of a knot K
to carry four independent gradings, which we will denote by a, q, tr, tc: apart from
the a and q gradings from the polynomial invariants, we introduce two homologic al
(or reﬁned) t-gradings, denoted tr and tc. Both t-gradings on the HOMFLY ho-
mology give a categoriﬁcation of P λ(K). In other words, if P λ
r (K) andP λ
c (K) are
three-variable Poincar´ e polynomials ofHλ(K) with respect to tr and tc gradings,
respectively, then
P λ
r (K)(a, q, tr =−1) = P λ
c (K)(a, q, tc =−1) = P λ(K)(a, q),
The appearance of the fourth grading is yet mysterious for us fro m geometric point
of view, but it seems to be inevitable. Let us list some of the evidences .
First of all, in such a way we managed to reconcile the two diﬀerent con ventions
for the homological grading in the case of symmetric representatio ns: tr is the
t-grading assigned to a generator of Hλ(K) in the grading conventions of [ 42],
whereas one can interpret tc as the t-grading assigned to a generator of Hλ(K) in
grading conventions of [ 2, 20, 21, 43 ]. The “mirror symmetry” exchanges the two
grading conventions. Therefore, one practical application of “mir ror symmetry” is
that it allows to convert from one set of grading conventions used in the literature
4 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
to the other one by looking at the HOMFLY homology of the knot color ed by
transposed Young tableaux λt.
One advantage of the quadruply-graded theory is that it makes all of the struc-
tural properties and isomorphisms completely explicit. This cannot b e achieved
within a triply-graded theory: for example in the case of the symmet ric represen-
tations (see [ 42]) only a few of the isomorphisms and symmetries could be made
explicit. Now, quadruply-graded theory Hλ(K) has remarkable properties: it gives
an explicit re-gradings of all colored isomorphisms, enables explicit ex pression in
all gradings for the mirror symmetry, and makes the exponential g rowth property
manifest as a fully reﬁned exponential growth property of three- variable polynomi-
als. In addition, miraculously, we discovered a new symmetry on Hλ(K) that we
call self-symmetry. This symmetry requires all four gradings, and unlike the mirror
symmetry it does not lift any known relation of the colored HOMFLY po lynomials.
What is even more surprising, is that all these symmetries, isomorph ism re-
gradings and exponential growth property have rather simple and pleasant expres-
sions. Moreover, all of them become particularly elegant when expr essed in terms
of an auxiliary grading, called Q-grading, deﬁned in the following simple way when
λ is a rectangular Young diagram with R rows:
(1.5) Q = q + tr− tc
R .
This new grading, which can be considered as a certain “corrected” q-grading,
cannot be seen on the decategoriﬁed, polynomial level, and as the f ormula indicates,
both t-gradings are needed for its deﬁnition. Therefore we need the qua druply-
graded theory in order to have all properties manifest, while only a s mall fraction
of this rich structure can be seen at the polynomial, “decategoriﬁe d” level.
Finally, the symmetries take the most elegant form when the homolog y is writ-
ten in ( a, Q, tr, tc)-gradings. Because of a linear relation between the gradings (1.5) ,
this is just a simple re-grading of Hλ(K). However, due to its importance, we give
it a special name, ~Hλ(K), and refer to it as the tilde-version of colored HOMFLY
homology. Thus, it is given by
(1.6) ~Hλ
i,j,k,l(K) := Hλ
i,Rj−k+l,k,l (K).
We note that only in the uncolored case the tr and tc gradings coincide (as well
as Q and q gradings), and the resulting homology is triply graded in agreement
with [ 21].
The second major novelty is that we extend the deﬁnition of the diﬀe rentials
dN to a two-dimensional family of diﬀerentials dn|m labeled by Lie superalgebras
sl(n|m). Then, the value of N from the familiar one-parameter family of the diﬀer-
entials{dN} corresponds to the diﬀerence n− m which is precisely the super-rank
of sl(n|m). This gives a much more natural treatment of the diﬀerentials dN , for
non-positive N , together with their gradings. We show that these new diﬀeren-
tials are nontrivial even in the uncolored homology (for suﬃciently lar ge knots)
and bring an interesting structure both to colored and uncolored k not homology.
We also describe explicitly the interaction between the diﬀerentials dn|m and the
colored diﬀerentials for the rectangle-colored homology.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 5
While it still deserves a much deeper understanding, the appearanc e of sl(n|m)
is natural for a number reasons. Primarily, the representation th eory of sl(n|m) ex-
plains the behavior of the colored diﬀerentials. For each rectangula r Young diagram
λ we deﬁne colored diﬀerentials removing any number of columns or row s from λ.
These diﬀerentials naturally appear from the identiﬁcation of the re presentations
of the superalgebra sl(n|m) labeled by two diﬀerent rectangles λ and µ. It turns
out that these are such that µ is obtained from λ by erasing some of its rows or
some of its columns. Then, the corresponding colored diﬀerential, dλ→µ, closes the
following commutative diagram:
Hλ(K)
dλ →µ
−−−→ H µ(K)
dn|m dn|m
↓ ↓
Hsl(n|m),λ(K)
∼
=−−−−−−−−→ Hsl(n|m),µ(K)
Furthermore, the diﬀerentials dn|m onHλ(K) exist for all pairs of nonnegative
integer (n, m) such that the superalgebra sl(n|m) has a representation correspond-
ing to the Young diagram λ. In such a way, all diﬀerentials have natural interpre-
tation, unlike the single-parameter family of diﬀerentials {dN}N∈Z for which only
the ones with N > 0 have clear interpretation as sl(N ) specialization diﬀerentials.
In addition, supergroups and the corresponding Lie superalgebra s are familiar in
the study of brane/anti-brane systems [ 83, 86 ]: much like a collection of N coin-
cident D-branes carries a gauge bundle with the structure group U (N ), a similar
system of n branes and m anti-branes carries U (n|m) gauge symmetry. Therefore,
since many physical realizations of knot homologies that we encount er in sections
2.1, 3.4, 6, and 7.2 are based on branes, it is not inconceivable that ap pearance of
supergroups and superalgebras is rooted there (although we will n ot try to pursue
this interpretation in the present paper).
Another direction of our study is the construction of the models fo r colored
homology for certain knots satisfying all above properties. We give a combinatorial
model for the unreduced homology of the unknot and study variou s diﬀerentials on
it. The HOMFLY homology is conjectured to be a free supercommuta tive algebra,
(1.7) A = Hλ(
)
and the diﬀerentials are described by the Koszul construction. We compare this
approach with other mathematical and physical approaches (pot entials and ma-
trix factorizations, categoriﬁcation of the Jones-Wenzl projec tors, algebra of BPS
states). We give an algebraic model for the Sr colored homology of torus knots and
compare it with the approaches of [ 37] and [ 23]. We study various diﬀerentials in
this model as well and show how the diﬀerentials dn|m naturally appear from the
rational Cherednik algebra. Finally, to demonstrate the full stren gth and robust-
ness of our approach, we describe the colored homology for the ﬁg ure eight knot,
which is a non-torus knot.
1.1. Structure of the paper. In Section 2 we describe a model for the unre-
duced colored homology of the unknot. It is a a free supercommuta tive algebra
A with one even and one odd generator per each box of the diagram λ. For
the representation Sn, this algebra can be naturally identiﬁed with the algebra
6 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
of Sn-invariant diﬀerential forms on Cn. Using the physics of BPS states, we de-
scribe some of these even and odd generators geometrically. We als o check that
the Poincar´ e polynomial for this algebra agrees with the evaluation formulas for
the Macdonald polynomial, that various authors [ 2, 14, 20 ] recently assign to the
unknot in the reﬁned Chern-Simons theory.
Both dm|n and the colored diﬀerentials can be interpreted as the Koszul dif-
ferentials on this algebra, sending odd generators to certain polyn omials in even
generators. We show that the approach of [ 43], where the homology of the unknot
is interpreted as the Jacobi ring of a certain potential W , ﬁts into this framework
if the Koszul complex is associated with the partial derivatives of W :
d(ξi) = ∂W
∂xi
, d (xi) = 0 .
Using this model, we also derive the equations for the colored diﬀeren tials: if the
representations of sl(m|n) labelled by λ and µ are isomorphic, we show that in some
examples the isomorphism between the corresponding Jacobi rings follows from the
equation
W λ
m|n(x1, . . . , x|λ|) = W µ
m|n(x1, . . . , x|µ|) + Wλ→µ(x|µ|+1, . . . , x|λ|),
where Wλ→µ is a non-degenerate quadratic function. We conjecture that the colored
diﬀerential dλ→µ is a Koszul diﬀerential associated with the partial derivatives of
Wλ→µ.
In Section 3 we describe the general structures on the colored HO MFLY ho-
mology. We give a detailed list of the properties of the quadruply-gra ded colored
HOMFLY homology Hλ(K) of a general knot K, together with the sl(n|m) and
colored diﬀerentials. Furthermore we describe explicitly the degree s of all colored
diﬀerentials and re-gradings in the corresponding colored isomorph isms. We end
the section with the two particular features in the case of the symm etric repre-
sentations: the δ-grading and the existence of the HFK-like diﬀerential on the
Sr-colored homology. Also, we discuss similarities and diﬀerences betwe en the case
of rectangle-labeled representations, which are the main topic of o ur present paper,
and the case of non-rectangular representations.
Section 4 contains the computations of the quadruply-graded hom ologies for
various knots and representations. Due to a large number of pred icted properties
such computations present a highly non-trivial check and conﬁrma tion of the theory.
Section 5 is devoted to torus knots. In Section 5.1 we recall the sta tement
about the stabilization of the HOMFLY polynomials of ( p, q) torus knots in the
limit q→∞ . We relate such stable λ-colored invariant of ( p,∞) torus knot to
the invariant of the pλ-colored unknot. Then, we conjecture a similar relation
between the corresponding colored homology theories of stable to rus knots and
that of the unknot. The λ-colored homology of the ﬁnite ( p, m) torus knot can be
realized as a certain quotient of this stable homology. This allows us to use the
algebraic description of the homology of the unknot, and in Section 2 .4 we give a
precise description of the generators in the rectangular homology of a torus knot
and their quadruple gradings. We describe and check the structur al properties of
colored homology using this algebraic model. We show the existence of a symmetry
between λ- and λt-colored homology, exchanging tr and tc gradings and preserving
the Q-grading. We check the reﬁned exponential growth conjecture f or the stable
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 7
homology of torus knots. We also describe respectively the self-du ality involution
and the action of diﬀerentials in the rectangular homology of torus k nots.
Generalizing the results of [ 37] and [ 23], we identify the colored homology of
torus knots with the certain representations of the rational Che rednik algebra. For
λ = Sr, we make this description precise and describe the space HSr
(T (m, n)) as
a space of diﬀerential forms on a certain non-reduced scheme
Mm,n,r :={(ur+1, . . . , unr; vr+1, . . . , vmr| U (z)m = V (z)n},
where the polynomials U (z) and V (z) are deﬁned by the equations
U (z) = 1 + zr+1ur+1 + . . . + znrunr, V (z) = 1 + zr+1ur+1 + . . . + zmrumr.
This description is ideally suited for a realization of colored HOMFLY hom ology
via Landau-Ginzburg B-model, which is the subject of Section 6. Usin g mirror
symmetry we also reformulate it in terms of the A-model and Lagran gian Floer
homology. We also provide some explicit formulas for the diﬀerentials a cting on
the HOMFLY homology and describe HSr
(T (m, n)) as a Jacobi ring of a certain
potential on a supermanifold.
Finally, section 7 is devoted to the “bottom row” of the HOMFLY homo logy,
i.e. a = 0 limit. We compare it to certain combinatorial models of Haglund et. a l.,
generalizing the models for q, t-Catalan numbers which played important role in
[37], and to the geometric models for coupled instanton-vortex syste ms proposed
in [ 19].
1.2. Acknowledgements. We are grateful to M. Abouzaid, M. Aganagic,
J.M. Baptista, I. Cherednik, K. Costello, R. Elliot, P. Etingof, A. Gor sky, K.
Hikami, M. Khovanov, B. Kim, A. N. Kirillov and A. A. Kirillov Jr., I. Losev,
A. Morozov, H. Nakajima, A. Negut, N. Nekrasov, A. Oblomkov, A. Okounkov, J.
Rasmussen, L. Rozansky, S. Shakirov, V. Shende, C. Vafa, O. Vir o, E. Witten, and
C. Woodward for the useful discussions. E. G. would like to thank th e California
Institute of Technology and Kyoto Research Institute for Mathe matical Sciences
for the hospitality. The research of E. G. is partially supported by t he grants
RFBR-10-01-678, NSh-8462.2010.1 and the Simons foundation. S.G . would like to
thank Instituto Superior Tecnico in Lisbon and the Simons Center fo r Geometry
and Physics at Stony Brook for hospitality during the key stages of this work. The
work of S. G. is supported in part by DOE Grant DE-FG03-92-ER407 01FG-02 and
in part by NSF Grant PHY-0757647. M. S. would like to thank the Califo rnia In-
stitute of Technology for hospitality during which part of this work w as done. The
work of M. S. was partially supported by the Portuguese Funda¸ c˜ao para a Ciˆ encia e
a Tecnologia through ISR/IST plurianual funding and through the p roject number
PTDC/MAT/101503/2008, New Geometry and Topology, and by the Ministry of
Science of Serbia, project no. 174012. Opinions and conclusions ex pressed here are
those of the authors and do not necessarily reﬂect the views of fu nding agencies.
2. Bosonic and F ermionic generators
2.1. The algebra of BPS states and knot cobordisms. While most of
this paper is probably aimed at a more mathematical reader, here we oﬀer a geo-
metric interpretation of some of our observations in the framewor k more familiar
to physicists. Therefore, the purpose of this section is twofold. F irst, it will help
physicists to understand better some of our observations (which , we believe, may
8 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
go beyond the scope of the present paper and are worth studying further in the
context of BPS state counting). Second, the physical interpret ation / motivation
provides further evidence for the structures of knot homologies discussed in this
paper. In Section 7.2 we also comment on the connection with the equ ivariant
instanton counting in the presence of a surface operator.
We begin with a lightning review of the physical interpretation of knot ho-
mologies, in whichHknot is identiﬁed with a space of supersymmetric particles (the
so-called BPS states) [ 41, 39, 87 ]:
(2.1) Hknot = HBPS .
