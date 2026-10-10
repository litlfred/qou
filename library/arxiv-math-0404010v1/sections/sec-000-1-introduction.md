---
doc_id: arxiv-math-0404010v1
doc_title: "YANG–BAXTER OPERATORS ARISING FROM ALGEBRA STRUCTURES AND THE ALEXANDER POLYNOMIAL OF KNOTS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0404010v1.pdf
source_sha256: a9522d4bec3ce6fb
toc_source: outline
doc_brief: "YANG–BAXTER OPERATORS ARISING FROM ALGEBRA STRUCTURES AND THE ALEXANDER POLYNOMIAL OF KNOTS — In this paper, we consider the problem of constructing knot invariants from Yang–Baxter operators"
---
The Yang–Baxter equation and its solutions, the Yang–Baxter operators, ﬁrst ap-
peared in theoretical physics and statistical mechanics. Later, this equation has emerged
in other ﬁelds of mathematics such as quantum group theory. Some references on this
topic are [5, 7].
The Yang–Baxter equation also plays an important role in knot theory. Indeed, Tu-
raev has described in [12] a general scheme to derive an invariant of oriented links from a
Yang–Baxter operator, provided this one can be “enhanced”. The Jones polynomial [4]
and its two–variable extensions, namely the Homﬂypt polynomial [2, 10] and the Kauﬀ-
man polynomial [6], can be obtained in that way by “enhancing” some Yang–Baxter
operators obtained in [3]. Those solutions of the Yang–Baxter equation are associated
to simple Lie algebras and their fundamental representations. The Alexander polyno-
mial can be derived from a Yang–Baxter operator as well, using a slight modiﬁcation of
Turaev’s construction [8].
More recently, D˘asc˘alescu and Nichita have shown in [1] how to associate a Yang–
Baxter operator to any algebra structure over a vector space, using the associativity
of the multiplication. This method to produce solutions to the Yang–Baxter equation,
initiated in [9], is quite simple.
In this paper, we consider the problem of applying Turaev’s method to Yang–Baxter
operators derived from algebra structures. In general, ﬁnding the enhancements of a
given Yang–Baxter operator can be diﬃcult or lengthy. In the case of Yang–Baxter
operators associated to algebra structures, the simplicity of their deﬁnition makes the
search for enhancements an easy task. We do this here in full generality. We conclude
from this computation that the only invariant which can be obtained from those Yang–
Baxter operators is the Alexander polynomial of knots. Thus, in a way, the Alexander
polynomial is the knot invariant corresponding to the axioms of (unitary associative)
algebras. Note that specializations of the Homﬂypt polynomial had to be expected from
those Yang–Baxter operators since they have degree 2 minimal polynomials.
The paper is organized as follows. In §2, we recall how to associate to any (unitary
associative) algebra a Yang–Baxter operator. Next, in §3, we review Turaev’s proce-
dure to derive a knot invariant from a Yang–Baxter operator as soon as this one can be
Date: January, 2004.
1
2
G. MASSUYEAU AND F. F. NICHITA
enhanced. Following Murakami [8], we recall how this method can be improved in the
case when the Yang–Baxter operator satisﬁes a certain redundancy property. The fact
that their minimal polynomials are quadratic implies that the Yang–Baxter operators
associated to algebra structures are redundant (Proposition 3.6). In §4, we compute
the enhancements of the Yang–Baxter operator associated to a given algebra structure.
Finally, we conclude from this calculation that Turaev’s procedure, as modiﬁed by Mu-
rakami, invariably produces from any of those enhancements the Alexander polynomial
of knots (Theorem 4.3).
Throughout the paper, we shall use the following conventions and notations. The
letter k will denote a ﬁxed ﬁeld with characteristic char(k)̸ = 2. For a k–vector space V
and an integer n ≥1, we denote by V ⊗n the n–times tensor product V ⊗· · · ⊗V over
k. The identity map V →V will be denoted by IdV , or simply by Id when the space
V is clear from the context. If V is ﬁnite–dimensional with basis e = (e1, . . . , ed) and if
f : V ⊗n →V ⊗n is a k–linear map, we denote by f j1···jn
i1···in the matrix element of f with
respect to the basis e⊗n:
f (ei1 ⊗· · · ⊗ein) =
X
1≤j1,...,jn≤d
f j1···jn
i1···in · ej1 ⊗· · · ⊗ejn.
2. Yang–Baxter operators arising from algebra structures
In this section, we recall results from [1] and we follow the terminology used there.
For a k–vector space V , the ﬂip map T : V ⊗V →V ⊗V is deﬁned by T(v ⊗w) = w⊗v.
Given a k–linear map R : V ⊗V →V ⊗V , we will write R12 = R ⊗Id, R23 = Id ⊗R
and R13 = (Id ⊗T)(R ⊗Id)(Id ⊗T).
Deﬁnition 2.1. An invertible k–linear map R : V ⊗V →V ⊗V is called a Yang–Baxter
operator (or simply a YB operator) if it satisﬁes the equation
(1)
R12 ◦R23 ◦R12 = R23 ◦R12 ◦R23.
Remark 2.2. Equation (1) is usually called the braid equation. An operator R satisﬁes
(1) if and only if R ◦T satisﬁes the quantum Yang–Baxter equation
R12 ◦R13 ◦R23 = R23 ◦R13 ◦R12.
Given a (unitary associative) k–algebra A and scalars x, y, z ∈k, we consider the
k–linear map Rx,y,z : A ⊗A →A ⊗A deﬁned by
Rx,y,z(a ⊗b) = x · ab ⊗1 + y · 1 ⊗ab −z · a ⊗b
for any a, b ∈A. The following theorem determines the situations where this map is a
Yang–Baxter operator.
Theorem 2.3 (D˘asc˘alescu–Nichita [1]). Let A be a k–algebra of dimension at least 2
and let x, y, z ∈k be scalars. Then Rx,y,z is a Yang–Baxter operator if and only if one
of the following conditions holds:
(i) x = z̸ = 0, y̸ = 0,
(ii) y = z̸ = 0, x̸ = 0,
(iii) x = y = 0, z̸ = 0.
If so, its inverse is given by Rx,y,z−1 = Ry−1,x−1,z−1 in cases (i) and (ii), and by
R0,0,z−1 = R0,0,z−1 in case (iii).
3
We will be only interested in the non–trivial cases (i) and (ii) (which are equivalent
through inversion) and we will denote by Rx,y the operator Rx,y,x. Observe that
(2)
Rx,y −xy · Rx,y−1 = (y −x) · Id⊗2
and that, in particular, the minimal polynomial of Rx,y is of degree 2.
Next result gives a necessary and suﬃcient condition for two Yang–Baxter operators
of that kind to be isomorphic.
Deﬁnition 2.4. Two k–linear maps R : V ⊗V →V ⊗V and R′ : V ′ ⊗V ′ →V ′ ⊗V ′
are said to be isomorphic if there exists an invertible k–linear map f : V →V ′ such
that R′ ◦(f ⊗f) = (f ⊗f) ◦R.
Proposition 2.5 (D˘asc˘alescu–Nichita [1]). Let A and A′ be k–algebras of dimension
at least 2, and let x, y, x′, y′ be nonzero scalars. Then the YB operators Rx,y and Rx′,y′
associated to A and A′ respectively are isomorphic if, and only if, x = x′, y = y′ and
the k–algebras A and A′ are isomorphic.
Remark 2.6. In fact, according to the proof of [1, Proposition 3.1], a bijective k–linear
map f : A →A′ is such that Rx′,y′ ◦(f ⊗f) = (f ⊗f) ◦Rx,y if and only if x = x′, y = y′
and f is, up to multiplication by a scalar, an isomorphism of k–algebras. (Note that the
assumption char(k)̸ = 2 is used here.)
