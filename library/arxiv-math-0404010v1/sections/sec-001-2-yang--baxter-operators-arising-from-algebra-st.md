---
doc_id: arxiv-math-0404010v1
doc_title: "YANG–BAXTER OPERATORS ARISING FROM ALGEBRA STRUCTURES AND THE ALEXANDER POLYNOMIAL OF KNOTS"
section_id: sec-001-2-yang--baxter-operators-arising-from-algebra-st
section_title: "Yang--Baxter operators arising from algebra structures"
section_number: 2
pages: 2-3
source_pdf: 0404010v1.pdf
source_sha256: a9522d4bec3ce6fb
toc_source: outline
doc_brief: "YANG–BAXTER OPERATORS ARISING FROM ALGEBRA STRUCTURES AND THE ALEXANDER POLYNOMIAL OF KNOTS — In this paper, we consider the problem of constructing knot invariants from Yang–Baxter operators"
---
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
