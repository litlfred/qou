---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-001-abstract
section_title: "Abstract"
section_number: null
pages: 1-2
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial
and representation-theoretic points of view. We prove that a lot of dilogarithm identities (hypothetically
all!) can be obtained by using the ﬁve-term relation only. Amon g those the Coxeter, Lewin, Loxton
and Browkin ones are contained. Accessibility of Lewin’s one v ariable and Ray’s multivariable (here for
n≤ 2 only) functional equations is given. For odd levels the ˆsl2 case of Kuniba-Nakanishi’s dilogarithm
conjecture is proven and additional results about remainder term are obtained. The connections between
dilogarithm identities and Rogers-Ramanujan-Andrews-Gordon type partition identities via their asymp-
totic behavior are discussed. Some new results about the string functions for levelk vacuum representation
of the aﬃne Lie algebra ˆsln are obtained. Connection between dilogarithm identities and algebraic K-
theory (torsion in K3(R)) is discussed. Relations between crystal basis, branching fu nctionsbkΛ 0
λ (q) and
Kostka-Foulkes polynomials (Lusztig’s q-analog of weight multiplicity) are considered. The Melzer an d
Milne conjectures are proven. In some special cases we are proving that the branching functions bkΛ 0
λ (q)
are equal to an appropriate limit of Kostka polynomials (the so- called Thermodynamic Bethe Ansatz
limit). Connection between ”ﬁnite-dimensional part of cryst al base” and Robinson-Schensted-Knuth cor-
respondence is considered.
0. Introduction.
In this paper we consider mainly the properties of dilogarit hm related to the so-called
accessibility problem, representation theory of Virasoro and Kac-Moody algebras, and
Conformal Field Theory (CFT). The remarkable and mysteriou s dilogarithm [Za2], [Za3]
will be the main hero of our paper, but we start with deﬁnition and list some applications
of more general and may be even more amazing functions:
polylogarithm and hyperlogarithm.
Deﬁnition 1 (G. Leibnitz, 1696; L. Euler, 1768). The polylogarithm function Li k(x)
is deﬁned for 0<x< 1 by
Lik(x) :=
∞∑
n=1
xn
nk (0.1)
2 Anatol N. Kirillov
and admits analytic continuation to the complex plane as a mu ltivalued analytical function
on x.
Deﬁnition 2 (E. Kummer, 1840; I. Lappo-Danilevsky, 1910; K.-T. Chen, 19 77). For
given vector n∈ Zl
+, the hyperlogarithm of type n is deﬁned for a point x lying in the unit
cubeIl ={x = (x1,...,x l)|| xi|< 1, 1≤i≤l} by
Φ n(x1,...,x l) =
∑
0<k1<k2<···<kl
xk1
1 xk2
2 ...x kl
l
kn1
1 kn2
2 ...k nl
l
. (0.2)
The function Φ n(x) admits an analytic continuation to the complex space Cl.
0.1. Ubiquity of polylogarithms.
The polylogarithm and hyperlogarithm have many intriguing properties and have ap-
peared in various branches of mathematics and physics. We me ntion the following ones:
— volumes of polytopes in hyperbolic and spheric geometry (N . Lobachevsky (1836),
L. Schl¨ aﬂi (1852), H. Coxeter (1935), G. Kneser (1936), ... )
— volumes of 3-dim hyperbolic manifolds (S. Kojima, J. Milno r, W. Neumann, T. Yoshida,
D. Zagier, ...)
— combinatorial formula for characteristic classes (I.M. G el’fand, R. MacPherson,
A. Gabrielov, M. Losik, ...)
— cohomology of GLn(C) (A. Borel, J. Dupont, D. Quillen, A. Suslin, ... )
— special values of zeta functions for number ﬁelds/ellipti c curves (S. Bloch, A. Beilinson,
P. Deligne, A. Goncharov, D. Zagier, ... )
— algebraic K-theory (A. Borel, S. Bloch, A. Goncharov, A. Suslin, D. Zagi er,... )
— number theory : Rogers-Ramanujan’s type identities, asym ptotic behavior of partitions
(S. Ramanujan, G. Hardy, D. Littlewood, B. Richmond, G. Mein ardus, ... )
— representation theory of inﬁnite dimensional algebras (A . Feingold, J. Lepowsky,
