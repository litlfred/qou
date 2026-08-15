---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-graded colored homology of knots"
section_id: sec-001-2-bosonic-and-fermionic-generators
section_title: "Bosonic and Fermionic generators"
section_number: 2
pages: 8-35
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
doc_brief: "Quadruply-graded colored homology of knots — W e conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
knot invariants and will also help us in section 7.2 to understand the limit a→ 0.
As we shall see, the latter allows one to focus on the “bottom row” o f the superpoly-
nomial which turns out to have a very elegant and simple geometric int erpretation
in the physical framework.
In one of the duality frames, the physical system involves a compac tiﬁcation on
a very particular (non-compact) Calabi-Yau 3-fold X in the presence of ﬁve-branes
supported on a Lagrangian submanifold LK⊂ X:
space-time : R× X× M4(2.2)
M5-branes : R× LK× D
Speciﬁcally, X is the total space of the O(−1)⊕O (−1) bundle over CP1, while
the Lagrangian submanifold LK is determined by a knot K⊂ S3, cf. [71, 82, 59 ].
Furthermore, the number of ﬁve-branes in (2.2) is equal to |λ| (= the total number
of boxes in the Young diagram λ), whereas the K¨ ahler modulus of X is related to
the variable a in the superpolynomial:
(2.3) a = exp
(
−Vol(CP1)
)
.
This summary was very telegraphic, of course, but the reader can always consult
e.g. [ 42] for further details, references, and the outline of the relation b etween
diﬀerent ways of looking at this physical system (2.2). As reviewed t here, the
system (2.2) was studied in physics as well as in math literature from m any diﬀerent
angles, e.g. from the target space point of view [ 41, 43 ] that leads to a description
of (2.1) in terms of enumerative invariants of ( X, LK), or from the viewpoint of the
ﬁve-brane [ 87], or from the viewpoint of the N = 2 gauge theory on a 4-manifold
M4 with ramiﬁcation [ 19]. However, only recently [ 27, 28 ] the system (2.2) has
been considered from the viewpoint of the two-dimensional theory on D, that will
be yet another motivation for the discussion in Section 7.2.
Now we are ready to discuss the BPS states that contribute to the reduced and
unreduced superpolynomials, P λ(a, q, t) andP
λ
(a, q, t), respectively.
As discussed e.g. in [ 71, 41, 66 ], there are two kinds of BPS particles that
contribute to (2.1) in the problem at hand: M2-branes supported o n bordered
surfaces embedded in X with boundary on LK, and momentum modes ( a.k.a. D0-
branes). The charge of the former is precisely the a-grading, while the charge of the
latter is the q-grading. Both types of states can mix together (forming stable B PS
particles that carry both charges) and both can carry a non-triv ial spin j3, which
becomes the third t-grading on (2.1). To summarize, the dictionary between three
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 9
gradings on the colored HOMFLY homology and the charges of the BP S particles
is as follows:
(2.4)
“a− grading” = β∈ H2(X, LK)∼
= Z (“winding number”)
“q− grading” = n∈ Z (“D0-brane charge”)
“t− grading” = 2 j3∈ Z (spin)
Using this dictionary, we can identify every generator of (2.1) with t he correspond-
ing BPS particle. For example, if we see a term amqntk in the superpolynomial,
the proper translation to the physics language is
(2.5) monomial ←→ “a BPS particle with winding number m ,
amqntk⊂P λ D0-brane charge n , and spin k
2 ”
The particles that carry no winding number ( m = 0) are usually called simply
D0-branes.
One well-known property of the BPS states in the present setup is t hat particles
that carry non-trivial winding number m = 1 are fermions, whereas D0-brane
states (with m = 0) are bosonic [ 18, 51 ]. When translated to the language of
knot homologies, this statement says that statistics of the gener ators in the colored
HOMFLY homology is correlated with the a-grading!
Namely, the generators with trivial a-grading are bosonic, whereas the genera-
tors with a-grading equal to 1 are fermions. This will play a key role in what follows .
Figure 1. A real isotropic knot cobordism Σ ⊂ R× S3 deﬁnes a
coassociative 4-manifold LΣ ⊂ R× T∗S3.
Another useful lesson that we can learn from the connection with e numerative
(BPS) invariants (2.1)–(2.2) is the behavior of colored HOMFLY homo logy with
respect to cobordisms. First, however, it is convenient to conside r a dual brane
10 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
system related to (2.2) by a geometric transition 1 [32, 71 ]:
space-time : R× T∗W× M4
N M5-branes : R× W× D(2.6)
|λ| M5-branes : R× LK× D
where W = S3 in most of our applications (or, its close cousin W = R3). This
system is relevant to sl(N ) homological knot invariants and has been studied from
various points of view in [ 2, 50, 87 ]. One advantage of the duality frame (2.6) that
will serve us well in building knot cobordisms is that the Lagrangian sub manifold
LK⊂ T∗W can be deﬁned simply as the conormal bundle to the knot K⊂ W .
Now, it is easy to describe how knot cobordisms can be implemented in t he
physical setup. Since the factor of R in (2.2) and (2.6) plays the role of the “time”
direction, one can replace R× S3 by a general 4-manifold cobordism V and replace
R× K embedded in it by a more general knot cobordism Σ ⊂ V , as in Figure 1:
space-time : X7× M4
N M5-branes : V× D(2.7)
|λ| M5-branes : LΣ× D
Supersymmetry imposes certain constraints, which ensure that t he physical setup
here continues to maintain the relation between supersymmetric co nﬁgurations
(BPS states) and functors on knot homologies. Speciﬁcally, the 7- manifold X7 must
be a special holonomy manifold with holonomy group G2, while the 4-manifold LΣ
must be a coassociative submanifold in X7. Both can be constructed in a fairly
simple way, starting with the data of V and Σ, respectively.
Just like T∗W is a “canonical” Calabi-Yau 3-fold associated to a 3-manifold
W , from a 4-manifold V one can build a “canonical” G2-holonomy manifold X7 =
Λ 2,+(V ) as the total space of the bundle of self-dual 2-forms. This 7-ma nifold
X7 = Λ 2,+(V ) replaces R× T∗W and reduces to it when V = R× W . In what
follows, we restrict our attention only to this case and, moreover, assume W = S3.
Then, given a knot cobordism Σ ⊂ V = R×S3, we wish to construct a coassociative
4-manifold LΣ ⊂ Λ 2,+(V ) with the property
(2.8) LΣ∩ V = Σ
which is a suitable G2-manifold version of the property LK∩ S3 = K in (2.6). By
analogy with the conormal bundle construction of LK, the desired coassociative
4-manifold LΣ can be deﬁned as the subbundle of Λ 2,+(V ) over Σ֒→V such that
restriction of the ﬁber to Σ is trivial, provided that Σ is a real isotrop ic minimal
surface [ 49, 52 ]. Details of this construction and its implications for functors on
colored knot homologies will be discussed elsewhere. Here, we simply p oint out
that the existence of such geometric construction implies the exist ence of a map
(2.9) Hλ( )⊗H λ(K) → Hλ(K)
Indeed, applying geometric transition one more time to the setup (2 .7) with V =
R× S3 we get a “cobordism version” of (2.2):
space-time : R× X× M4(2.10)
M5-branes : LΣ× D
1sometimes also called “large N duality,” which is somewhat of a misnomer since the duality
holds for all values of N , as long as one is careful with diﬀerentials and wall crossin g [ 21, 42 ]
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 11
where LΣ is a coassociative 4-manifold in R× X. When Σ is a link cobordism from
K⨆ to K, the setup (2.10) deﬁnes a functor on the space of reﬁned open B PS
states and, via (2.1), leads to a functor (2.9) on the colored HOMFL Y homology.
W
−1
2W
−1
1W1
1
vol(CP1)
W
−1
3
N
3 2 −1 0 1 −2 −3
W
1
W
1
2 3
Figure 2. Walls and chambers for the conifold X in (2.2).
Note, that (2.9) is very similar — and, in fact, possibly related — to the
conjecture [ 42] that Hλ(K) = Hopen
BPS is a module over the algebra of closed BPS
statesHclosed
BPS :
(2.11)
reﬁned open BPS states : Hopen
BPS
⟲
reﬁned closed BPS states : Hclosed
BPS
Even though we did not pursue the detailed comparison of A =H( ) and the
algebraHclosed
BPS here, it is worth mentioning that the two share some similarities.
For instance, much likeH( ) has sl(N ) specializations indexed by N and realized
by the action of diﬀerentials dN (see below), the space Hclosed
BPS for the problem at
hand also has an inﬁnite set of chambers, conveniently labeled by N , see Figure 2.
Moreover, in the N -th chamber the space Hclosed
BPS has N stable BPS objects [ 66]:
D0/D2 bound states of charge ( n, β) = ( j, 1), where 0 ≤ j < N , nicely matching
the fact that Hsl(N ), ( ) is also N -dimensional.
2.2. Colored polynomials of the unknot. For a Young diagram λ and a
box x in it we deﬁne the arm a(x), leg l(x), co-arm a′(x) and co-leg l′(x) by the
Figure 3. The hook-length of x is deﬁned as h(x) = a(x) +l(x) + 1, and the content
of x is deﬁned as c(x) = a′(x)− l′(x).
Let λ be a Young diagram with k boxes, let Vλ denote the irreducible represen-
tation of Sk labelled by λ, and let Uλ = Sλ(CN ) denote the irreducible representa-
tion of sl(N ) labelled by λ. The sl(N ) quantum invariant of the λ-colored unknot
coincides with the character of the representation Uλ and is given by (2.12). This
character is given by the hook formula:
chUλ =
∏
x∈λ
(1− qN +c(x))
(1− qh(x)) .
If we substitute A = qN , we get
(2.12) P λ(a, q) =
∏
x∈λ
(1− Aqc(x))
(1− qh(x)) .
12 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
x a(x)a′(x)
l(x)
l′(x)
Figure 3. Arm, leg, co-arm and co-leg
Let Mλ(q, t; pi) be a Macdonald polynomial corresponding to a diagram λ. Recall
that its evaluation can be computed by the formula [ 63]:
(2.13) M∗
λ(A, q, t) = Mλ
(
pi = 1− Ai
1− ti
)
=
∏
x∈λ
tl′(x)− Aqa′(x)
1− qa(x)tl(x)+1 .
Note that at q = t the Macdonald polynomials degenerate to Schur polynomials and
(2.13) degenerates to the equation (2.12). In all approaches bas ed on the reﬁned
BPS invariants the (unreduced) colored superpolynomials of the un knot are given
by the Macdonald dimensions
(2.14)
P
λ
( ) = M∗
λ(A, q, t) .
In order to write these expressions with positive coeﬃcients, one n eeds to convert
to the variables used e.g. in [ 21]:
A =−a2t , q = q2t2 , t = q2.
The ﬁrst few values of (2.14) read as
(2.15)
P ( ) = 1− A2
1− t2 = 1 + a2t
1− q2
(2.16) P ( ) = (1− A2)(1− A2q2)
(1− t2)(1− q2t2) = (1 + a2t)(1 + a2q2t3)
(1− q2)(1− q4t2)
where we normalized by an overall powers of A, q, and t, so that all expressions
(2.14) have the form of a power series P
λ
( ) = 1 + . . ..
From now on we will work in the variables a, q, t. The variable t will be also
denoted by tc. The equation (2.14) in these variables has a form:
(2.17) P
λ
( ) =
∏
x∈λ
1 + a2q2c(x)t2a′(x)+1
1− q2h(x)t2a(x)
Note that the right hand side is a polynomial in a and a series in q with all nonneg-
ative coeﬃcients. For λ = Sr, these answers match the stable homology of ( r,∞)
torus knots deﬁned in [ 21].
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 13
2.3. Schur-Weyl duality . Following [56], let us model the fundamental rep-
resentation of sl(N ) as U□ = C[x]/(xN ). The Schur-Weyl duality (e.g. [ 29]) says
that
U⊗k
□ =
⨁
|µ|=k
Vµ⊗ Uµ,
or, equivalently,
(2.18) Uλ = Hom Sk (Vλ, U⊗k
□ ) = Hom Sk (Vλ, C[x1, . . . , xk]/IN ),
where the ideal IN ⊂ C[x1, . . . , xk] is generated by xN
1 , . . . , xN
k . If λ corresponds
to the symmetric power of the fundamental representation, the construction (2.18)
gives the identity
SkU□ = (C[x1, . . . , xk]/IN )Sk = C[x1, . . . , xk]Sk /(IN )Sk .
The symmetrized ideal I Sk
N is generated by pN +s =∑ xN +s
i for 0≤ s≤ k− 1. If
λ corresponds to the exterior power of the fundamental represe ntation, we have to
study the anti-symmetric part of In. One can check ([ 43]) that ( IN )ǫ is generated
by ∆ · hN +1−j, 1≤ j≥ k, where hi denote the complete symmetric polynomials,
and ∆ denotes the Vandermonde determinant. Therefore
Λ kU□ = (C[x1, . . . , xk]/IN )ǫ = ∆ · (C[x1, . . . , xk])Sk /(hN +1−j).
Remark that the latter equation allows us to identify the exterior po wer with the
cohomology of the Grassmannian:
Λ kU□ (sl(N )) = ∆ · H∗(Gr(k, N )),
since hi can be naturally identiﬁed with the Chern classes of the quotient bun dle.
The setup of [ 21] and [ 42] prescribes the knot homology to be obtained by a
certain reduction procedure from the “large N limit”. Let us describe this construc-
tion for the case of unknot. Given a Young diagram λ, there supposed to exist a
triply graded spaceHλ modelling the λ-colored HOMFLY homology of the unknot.
This space is equipped with the diﬀerentials dN , and the homology of Hλ with
respect to dN should be isomorphic to the sl(n) homology of the unknot colored
by λ. Let us describe Hλ along the lines of the above Schur-Weyl duality. We start
with the fundamental representation U□ (sl(N )) = C[x]/(xN ). The corresponding
triply graded space will be
H□ = Ω•(C) = C[x, dx],
and the diﬀerential comes from the Koszul complex:
dN (x) = 0 , d N (dx) = xN .
It is clear that H∗(H□ , dN )≃ U□ (sl(N )). The k-th tensor power of this construc-
tion will give
H□ ⊗k
= Ω•(Ck) = C[x1, . . . , xk; dx1, . . . , dxk],
and the diﬀerential is given by the formula dN (xi) = xN
i . Therefore a natural
candidate forHλ will be [ 43]:
(2.19) Hλ := Hom Sk
(
Vλ, Ω•(Ck)
)
.
Note that this space (as in the uncolored case) diﬀers from the naiv e limit of
Uλ(sl(N )). It is naturally equipped with two gradings: a-grading is given by the
degree of a diﬀerential form and q-grading is a standard polynomial grading. In
other words, the ( a, q)-degree for xi equals to q2i and for dxi equals to a2.
14 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
Let us check that the ( a, q)-character of the space Hλ agrees with the colored
HOMFLY polynomial of the unknot. It follows from the results of [ 57] (see also
[64]) that the character of Hλ equals
(2.20) ch Hλ(a, q) =
∏
(i,j)∈λ
(qi−1 + aqj−1)
(1− qh(i,j)) .
Therefore chHλ(a, q) = qν(λ)P λ(−a, q), where ν(λ) = ∑ (i− 1)λi. At a = 0 the
character (2.20) degenerates to:
Pbottom(Hλ) =
∏
(i,j)∈λ
qi−1
1− qh(i,j) .
For a symmetric representation we have
HSk
=
(
Ω•(Ck)
) Sk
= Ω•(Ck/Sk) = C[u1, . . . , uk; du1, . . . , duk],
where ui denote the elementary symmetric polynomials. Remark that the ( a, q)-
degree for ui equals to q2i and for dui =∑ ∂ui
∂xj
dxj equals to a2q2i−2. Therefore
the bigraded Poincar´ e seriesHSk
has a form:
P (HSk
) =
k∏
i=1
1 + a2q2i−2
1− q2i ,
in agreement with (2.17).
Let us describe the “bottom” a = 0 part of the homology for λ = . The
corresponding representation of S3 is the standard two-dimensional representation.
We have to compute Hom Sk (Vλ, C[x1, x2, x3]). Let a⊂ C[x1, x2, x3] denote the
ideal generated by the symmetric polynomials of positive degree. It is known that
C[x1, x2, x3]/a is isomorphic to the regular representation of S3, and it contains
two copies of Vλ in gradings 1 and 2. These copies can be multiplied by arbitrary
symmetric polynomials, so the character of the a = 0 part of the homology equals
to
q + q2
(1− q)(1− q2)(1− q3) = q
(1− q)2(1− q3) .
This results agrees with the hook formula (2.12) at a = 0, since the hook-lengths
for the boxes of our diagram are equal to 1, 1 and 3.
2.4. Colored homology of the unknot. Consider a free supercommutative
algebraA with even generators u1, . . . , ur and odd generators ξ1, . . . , ξs. Suppose
that the algebra is graded such that deg ui = αi, deg ξi = βi. It is clear that the
Hilbert series of this algebra is given by the formula
(2.21) Hα,β(q) =
∏ s
i=1(1 + qβi)
∏ r
i=1(1− qαi ) .
The similarity of this formula to (2.12) and (2.17) suggests the followin g construc-
tion. We conjecture that the homology Hλ of the unknot colored by the represen-
tation λ is isomorphic to the free graded supercommutative algebra A. To every
box x of λ we associate an even generator ux and an odd generator ξx. The algebra
has three gradings q, a, tc such that
(q, a, tc)[ux] = (2 h(x), 0, 2a(x)), (q, a, tc)[ξx] = (2 c(x), 2, 2a′(x) + 1).
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 15
By (2.21) and (2.17) the Hilbert series of this algebra equals to
P
λ
( )(a, q, tc) =
∏
x∈λ
1 + a2q2c(x)t2a′(x)+1
c
1− q2h(x)t2a(x)
c
.
As we will mostly discuss the rectangle-shaped Young diagrams, let u s ﬁx some
notations for them. Let λ be a rectangle with R rows and S columns. For a box
x = (i, j), 1≤ i≤ S, 1≤ j≤ R in it we have:
a(x) = S− i, l (x) = R− j, h (x) = R + S− i− j + 1,
a′(x) = i− 1, l ′(x) = j− 1.
To this box we associate a bosonic generator uij and a fermionic generator ξij such
that
(q, a, tc)[uij] = (2( R + S− i− j + 1), 0, 2(S− i)), (q, a, tc)[ξij] = (2( i− j), 2, 2i− 1).
We deﬁne a fourth grading using the mirror symmetry between R×S and S×R
rectangles. To write down the isomorphism Mλ :Hλ→H λt
, one can deﬁne it on
the level of generators. We deﬁne
Mλ(uij) := uR−j+1,S−i+1, M λ(ξij) := ξji.
The correspondence between boxes is shown in Figure 4. Note that for bosonic
generators we ﬁx the southeast corner of the rectangle (marke d with *) while for
the fermionic ones we ﬁx the southwest corner. We deﬁne the grad ing tr using the
mirror symmetry relation tr(w) = tc(Mλ(w)), so
tr(uij) = 2 j− 2, t r(ξij) = 2 j− 1.
Using the formula
Q = q + tr− tc
R ,
we get
Q(uij) = 2 , Q (ξij) = 0 .
2.5. Potentials and diﬀerentials: antisymmetric case. It is known ([ 21,
33, 43, 60 ], see also Section 3) that the reduction from HOMFLY homology to
sl(N ) homology is given by the following procedure. Let Hλ(K) and Hsl(N ),λ(K)
respectively denote the HOMLFY and sl(N ) homology of a knot K. There exists
a diﬀerential dN of ( a, q)-degree (−1, N) such that
Hsl(N ),λ(K) = H∗(Hλ(K), dN )
Remark that dN preserves the grading N a + q, and its Euler characteristic with
respect to this grading equals P λ(K; a = qN , q) = P sl(N ),λ(K).
On the other hand, it is known that for some diagrams λ one can construct
a family of potentials Wλ,N (u1, . . . , ud) such that Hsl(N ),λ( ) coincides with the
Jacobi ring J = C[ui]/
(
∂Wλ,N
∂ui
)
. More generally, Hsl(N ),λ( ) is expected to
coincide with the Hochschild homology of the category of the matrix f actorizations
of Wλ,N , that is, with the homology of the Koszul complex associated with th e
sequence of the partial derivatives of Wλ,N . The latter homology contains the
Jacobi ring J and is equal to it if and only if Wλ,N has only isolated singularities.
In other words, if the potentials Wλ,N (u1, . . . , ud) exist then one can consider the
16 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
•i
j
*
M
•
i
j
*
•i
j
*
M •
i
j
*
Figure 4. Mirror symmetry for uij (upper pair) and for ξij (lower pair).
free supercommutative algebra A with even generators u1, . . . , ud, odd generators
ξ1, . . . , ξd and the diﬀerential
dN : C[ui, ξj]→ C[ui, ξj ], d N (ξi) = ∂Wλ,N
∂ui
, d N (ui) = 0 .
This matches with the above construction of diﬀerentials, if one can identify ui and
ξi with the even and odd generators of Hλ, so that C[ui, ξj] =Hλ.
The potential WΛ k,N was found in [ 43]:
WΛ k,N (u1, . . . , uk) = Coef N +1
[
ln(1 + zu1 + . . . + zkuk)
]
.
It has an isolated singularity at the origin, and the Jacobi rings of WΛ k,N and
WΛ N −k,N are isomorphic. Moreover, one can check that up to some change o f
variables (ui)→ (vi) the following identity holds:
(2.22) WΛ k,2k−j (u1, . . . , uk) = WΛ k−j ,2k−j (v1, . . . , vk−j ) + 1
2
j∑
s=1
vk−j+svk+1−s.
For example, one can check that WΛ 2,3 =− u4
1
4 + u2
1u2− u2
2
2 , WΛ 1,3 =− u4
1
4 , hence
WΛ 2,3 =−WΛ 1,3− (u2− u2
1)2
2 .
Remark 2.1. Let us explain the construction of vi in general. Consider sup-
plementary variables wj deﬁned by the equation
ws = Coef j
[ 1 + zu1 + . . . + zkuk
1 + zu1 + . . . + zk−juk−j
]
.
Clearly, ws = 0 for s≤ k− j, and the change of variables
(u1, . . . , uk)→ (u1, . . . , uk−j, wk−j+1, . . . , wk)
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 17
is invertible. Now
WΛ k ,2k−j(u1, . . . , uk)− WΛ k−j ,2k−j(u1, . . . , uk−j) =
Coef 2k−j+1 ln
[ 1 + zu1 + . . . + zkuk
1 + zu1 + . . . + zk−juk−j
]
=
Coef 2k−j+1 ln
[
(1 + wk−j+1zk−j+1 + . . . + wkzk + . . .)
]
=
1
2
j∑
s=1
wk−j+swk+1−s + . . . .
Since the quadratic part of this expression is non-degenerate, on e can apply Morse
lemma with parameters and get rid of terms of higher degree in w’s. See also [ 45]
for an alternative proof of this result and further discussions.
The equation (2.22) can be rewritten as WΛ k,2k−j = WΛ k−j ,2k−j + W′, and we
get the following diagram:
(2.23)
HΛ k dΛ k→Λ k−j
−−−−−−−→ HΛ k−j
d2k−j d2k−j
↓ ↓
HΛ k,2k−j =
−−−−−−−−→ HΛ k−j ,2k−j
Here the colored diﬀerential dΛ k→Λ k−j coincides with the one deﬁned in [ 42]. It
is deﬁned on HOMFLY homology colored by Λ k, and its homology are isomorphic
to the HOMFLY homology colored by Λ k−j. It corresponds to the “remainder po-
tential” W′ = 1
2
∑ j
s=1 vk−j+svk+1−s in (2.22). The corresponding Koszul complex
is associated to the sequence of polynomials vk−j+1, . . . , vk:
dΛ k→Λ k−j (ξi) = vi+k−j ,
and its homology is isomorphic to a free superpolynomial algebra gene rated by
v1, . . . , vk−j, ξj+1, . . . , ξn. We can easily see this diﬀerential on the picture with the
bosonic and fermionic generators labeled by the boxes of a Young dia gram. Recall
that their q-degrees are twice the contents and the hook-length of the boxe s of Λ k
respectively, as shown in Figure 5. The diﬀerential dΛ k→Λ k−j has q-degree 4 k− 2j,
(2.24) ( a, q)[dΛ k→Λ k−j ] = ( −2, 4k− 2j)
2.6. Potentials and diﬀerentials: extension to nλ. Let us ﬁrst ﬁx some
notations. Let λ = ( λ1, . . . , λr) be a Young diagram. Then the boxes of nλ =
(nλ1, . . . , nλr) are split into groups by n boxes labelled by the boxes of λ. If x is a
box of λ, then we label the corresponding boxes in nλ by x(1), . . . , x(n).
For every x in λ we can also consider the generators ux and ξx inHλ and the
generators u(i)
x and ξ(i)
x inHnλ. For convenience, we can consider the generating
functions
ux(τ ) =
n−1∑
i=1
u(i)
x τ i−1, ξ x(τ ) =
n−1∑
i=1
ξ(i)
x τ i−1.
18 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
2
2(k− j + 1)
2k
.
.
.
.
.
.
u1
uk−j+1
uk
q(ux)
2− 2k
2j− 2k
0
.
.
.
.
.
.
ξ1
ξj
ξk
q(ξx)
.
.
.
Figure 5. Action of the diﬀerential dΛ k→Λ k−j and the q-degrees
of the generators ux, ξx.
u(2)
2 u(1)
2
u(2)
1 u(1)
1
u2
u1
Figure 6. Bosonic generators for Λ 2 and 2Λ 2.
Suppose that the diagram λ admits a potential Wλ,N (u1, . . . , ud). We conjec-
ture that for all n the diagrams nλ admit potentials Wnλ,N such that
(2.25) ˆW (τ ) =
∞∑
n=1
τ n−1Wnλ,N = Wλ,N (u1(τ ), . . . , ud(τ )).
Since WΛ 2,3(u1, u2) =− u4
1
4 + u2
1u2− u2
2
2 , we have
W2Λ 2,3(u(1)
1 , u(1)
1 , u(1)
2 , u(2)
2 ) = Coef 1
[
− u1(τ )4
4 + u1(τ )2u2(τ )− u2(τ )2
2
]
=
=−
(
u(1)
1
) 3
u(2)
1 +
(
u(1)
1
) 2
u(2)
2 + 2u(1)
1 u(2)
1 u(1)
2 − u(1)
2 u(2)
2 .
Remark that u(j)
i correspond to the boxes of the 2 × 2 rectangle (see Figure 6), so
that their q-degrees are equal to the hook-lengths:
q(u(1)
1 ) = q(u1) = 2 , q (u(2)
1 ) = 4 , q (u(1)
2 ) = q(u2) = 4 , q (u(2)
2 ) = 6 .
The potential W2Λ 2,3 is homogeneous of q-degree 10.
Moreover, suppose that we have some diﬀerential D onHλ given by the formula
D(ξl) = pl(u1, . . . , ud). Such a diﬀerential can be naturally extended to nλ by the
formula
(2.26) Dn(ξ(i)
l ) = Coef n−1−i[pl(u1(τ ), . . . , ud(τ ))]
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 19
ξ(1)
2 ξ(2)
2
ξ(1)
1 ξ(2)
1
ξ2
ξ1
Figure 7. Fermionic generators for Λ 2 and 2Λ 2.
6 4
4 3
0 2
−2 0
ux ξx
Figure 8. Colored diﬀerential d2Λ 2→2Λ 1 .
Remark that equations (2.25) and (2.26) agree with each other. In deed, every
potential W induced a diﬀerential DW such that DW (ξl) = ∂W
∂ul
, if we match a
bosonic variable ul with the fermionic variable ξl. We can match u(i)
l with ξ(i)
l so
that
∂Wn
∂u(i)
l
= Coef n−1
[
∂ˆW
∂ul
∂ul(τ )
∂u(i)
l
]
= Coef n−1−i[pl(u1(τ ), . . . , ud(τ ))].
As an example of this construction, consider λ = (1), so that nλ = ( n) = Sn.
We have Wλ,N = xN +1, and it was suggested in [ 38] (see also [ 37]) that
WSn,N = Coef n−1(x(1) + x(2)τ + . . . + x(n)τ n−1)N +1.
This diﬀerential diﬀers form the one proposed in [ 43], but its homology agree with
the known categoriﬁcations of the Jones-Wenzl projectors [ 15, 16, 25 ].
As a more interesting example, let us compute the colored diﬀerentia l for the
rectangular R×S diagram. Such a diagram can be presented as S·Λ R, and, as such,
admits an extension of the colored diﬀerential dΛ R→Λ j . We have dΛ R→Λ j (ξl) = ul−j,
so
dR×S→j×S(ξ(m)
l ) = u(m)
l−j .
In Figure 8 we show the action of the diﬀerential d2Λ 2→2Λ 1 . The left and
right rectangles illustrate the q-degrees of the bosonic and fermionic generators
respectively. The diﬀerential has q-degree 6 (the same as dΛ 2→Λ 1 ), and its homology
is a free graded supercommutative algebra isomorphic to HS2
.
3. Gradings, Diﬀerentials, Mirror Symmetry
3.1. Introduction. For any Young diagram λ, the λ-colored HOMFLY poly-
nomial of a knot K, denoted P λ(K)(a, q), is a two-variable polynomial knot in-
variant whose a = qN one-variable specialization (1.1) equals the quantum knot
invariant obtained by the representation λ of the quantum sl(N ). Throughout the
paper, P λ(K) denotes the reduced polynomial, i.e. it is normalized so that the
value of the unknot is equal to 1.
20 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
We conjecture the existence of the homology theory Hλ(K) categorifying the
polynomials P λ(K), i.e. such that its graded Euler characteristic is equal to P λ(K).
Although we do not give the explicit deﬁnition of these homology theor ies, the in-
sight from physics, representation theory and the double aﬃne He cke algebras (DA-
HAs) predict a very rich structure of diﬀerentials on Hλ(K), together with various
symmetries of Hλ(K). We focus on rectangular Young diagrams λ, i.e. Young di-
agrams which have the form of a rectangle with R rows and S columns, and which
will be denoted λ = R× S. This is a large class of representations, that includes
as particular cases all symmetric representations ( R = 1) and antisymmetric ones
(S = 1). 2
Our main results for Hλ(K) can be split in two groups, which match together
perfectly. First, we conjecture that certain, grading-independ ent structures exist
and the following properties hold on Hλ(K):
• Hλ(K) is ﬁnite-dimensional.
• There are two symmetries on Hλ(K): one is the mirror symmetry that
switches between λ and its transpose partition λt:
(3.1) Hλ(K)∼
=Hλt
(K).
The other one is the self-symmetry onHλ(K). While the mirror symme-
try categoriﬁes the known relation for the colored HOMFLY polynom ials
(1.3):
(3.2) P λ(K)(a, q) = P λt
(K)(a, q−1),
the self-symmetry is a completely new symmetry, that does not cat egorify
any polynomial relation. It uses homological grading in a non-trivial w ay,
and exists only on the homological level.
• For every pair of non-negative integers ( n, m), such that n≥ R or m≥ S,3
there exists a collection of diﬀerentials dn|m onHλ(K), such that they
pairwise anti-commute, and such that the homology of Hλ(K) with re-
spect to dn|m is isomorphic to the homology Hsl(n|m),λ(K) that categori-
ﬁes the quantum invariant of a knot K labeled by a representation λ of
sl(n|m):
(3.3) H∗(Hλ(K), dn|m) =Hsl(n|m),λ(K).
Introducing this two-parameter collection of diﬀerentials is one of t he main
goals of the present paper 4. All previous results on the structural proper-
ties of the colored HOMFLY homologies (fundamental [ 21] and symmetric
ones [ 42]) predicted only the existence of one-parameter family of anti-
commuting diﬀerentials, with the parameter N representing the rank of
sl(N ) specializations. As we shall explain, various reasons suggest that
introduction of a two-parameter family associated with sl(n|m) represen-
tations is a much more natural thing to do.
2Although many of the properties and results still hold for no n-rectangular representations,
there are certain subtleties in that case. W e discuss this in section 3.11.
3For other values of m and n the diﬀerentials may exist in the unreduced theory, which we
do not cover in details here.
4Although some of these operators were implicitly deﬁned in [ 34] for the uncolored homology,
there relation to supergroups was not understood there.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 21
• There exist colored diﬀerentials that change representations (colors). In
other words, they allow passage from one homology theory Hλ(K) to
another one Hµ(K), for some Young diagram µ⊂ λ. More precisely,
colored diﬀerential dλ→µ onHλ(K) has the property that the homology
ofHλ(K) with respect to dλ→µ is isomorphic to Hµ(K).
The main group of colored diﬀerentials, namely the group of 2( R+S−
1) diﬀerentials, is directly related to particular diﬀerentials dn|m. More
precisely, for every Young diagram µ that is obtained from λ by removing
either some of its rows or some of its columns, there should be two diﬀ erent
diﬀerentials of the form dλ→µ such that
(3.4) H∗(Hλ(K), dλ→µ) =Hµ(K).
They ”lift” the relation Hsl(n|m),λ(K)∼
=Hsl(n|m),µ(K) coming from the
isomorphism λ∼
= µ as sl(n|m) representations for appropriate values of n
and m, and we also denote such diﬀerential by dcol
n|m. In other words, we
have the following commutative diagram:
Hλ(K)
dλ →µ (i.e. d col
n|m)
− −−−−−−−−−−− → Hµ(K)
dn|m dn|m
↓ ↓
Hsl(n|m),λ(K)
∼
=−−−−−−−−→ Hsl(n|m),µ(K)
We note that onHλ(K) the diﬀerentials dn|m and dcol
n|m share many similar
properties. In particular, frequently the diﬀerential dn|m onHµ(K) acts
trivially, and then on Hλ(K) the diﬀerentials dn|m and dcol
n|m coincide.
• For large classes of knots, including torus knots and two-bridge kn ots, the
size of the homology Hλ(K) is equal to the |λ|-th power of the dimension
ofH
(K). For an arbitrary knot K, such relation holds asymptotically
when|λ| tends to inﬁnity.
Our second major conjecture is that the colored HOMFLY homology Hλ(K)
of a knot K is quadruply-graded. We denote these four gradings by a, q, tr, tc.
Thus, apart from the a- and q-gradings associated to each generator, we also assign
two homological t-gradings. Any of the two t-gradings give a categoriﬁcation of
P λ(K), i.e. forgetting one of them gives triply-graded categoriﬁcation o f the colored
HOMFLY-polynomial. In other words, if we denote the (four-variab le) Poincar´ e
polynomial ofHλ(K) byP λ(K)(a, q, tr, tc), then we have
(3.5) P λ(K)(a, q, tr =−1, tc = 1) =P λ(K)(a, q, tr = 1, tc =−1) = P λ(K)(a, q).
The appearance of the fourth grading is rather mysterious from t he geometric
point of view, but it seems to be inevitable. Let us list some of the evide nces.
First of all, in the case of symmetric and anti-symmetric representa tions, the cor-
responding homology Hλ(K) has been studied in the literature, and although the
results in various papers are isomorphic, there are two diﬀerent co nventions for the
homological t-gradings. The tr-grading that we propose is the t-grading assigned to
a generator of Hλ(K) in the grading conventions of [ 27, 42 ], whereas one can in-
terpret tc as the t-grading assigned to a generator of Hλ(K) in grading conventions
of [2, 20, 21, 43 ]. As argued in [ 42], the “mirror symmetry” — the symmetry that
relates the homology colored by a Young diagram and its transposed — exchanges
22 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
the two grading conventions. However, despite being very similar, o ne cannot pass
from one convention to another by an explicit gradings transforma tion. The so-
lution that we propose is to keep track of both t-grading conventions together,
and regard the homology Hλ as quadruply-graded theory, with four independent
gradings a, q, tr and tc.
The deﬁnite advantage of the quadruply-graded theory is that it m akes all of
the structural properties and isomorphisms completely explicit. Th is cannot be
achieved by a triply-graded theory: for example in the case of the s ymmetric repre-
sentations (see [ 42]) only a few of the isomorphisms and symmetries could be made
explicit. In quadruply-graded theory Hλ(K) one has completely explicit mirror
symmetry and self-symmetry. Moreover, the re-grading in all of t he isomorphisms
of colored diﬀerential (3.4) can be made explicit, in all gradings. Finally , the ex-
ponential growth conjecture for the size of the colored homology becomes a totally
reﬁned exponential growth property of an appropriate three-v ariable Poincar´ e poly-
nomial. What is even more miraculous, is that all these symmetries, iso morphism
re-gradings and exponential growth property have rather simple and pleasant ex-
pressions. Moreover, all of them become particularly elegant with t he introduction
of an auxiliary grading, called the Q-grading, deﬁned in a following simple way:
(3.6) Q = q + tr− tc
R .
This new grading, which can be considered as certain “corrected” q-grading, cannot
be seen on the decategoriﬁed, polynomial level, and as the formula in dicates, both
t-gradings are needed for its deﬁnition. Therefore we need the qua druply-graded
theory in order to have all explicit properties, and only a few of vario us symmetries
and isomorphisms have polynomial counterparts at the decategor iﬁed level.
Finally, the symmetries get the nicest form when the homology is writt en in
(a, Q, tr, tc)-gradings. Because of a linear relation between the gradings (3.6) , this
is just a simple re-grading of Hλ(K). However, due to its importance, we give it
a special name, ~Hλ(K), and refer to it as the tilde-version of colored HOMFLY
homology. Thus, it is given by:
(3.7) ~Hλ
i,j,k,l(K) := Hλ
i,Rj−k+l,k,l (K).
The only case when the two t-gradings coincide is the uncolored case, λ =
, and
the resulting homology is triply-graded in agreement with [ 21]. In this case the q-
and Q-gradings coincide, and the mirror symmetry and the self-symmetr y are in
fact the same symmetry.
Now we start with the detailed description of the structure of the q uadruply-
graded colored HOMFLY homology.
3.2. Self-symmetry. There are two remarkable symmetries in the colored
homology when color is given by a rectangular Young diagram λ. The ﬁrst one is
self-symmetry on the homology Hλ(K) and the second one is the mirror symmetry
that relates the Hλ(K) andHλt
(K) homologies.
The main advantage of the Q-grading is that in the quadruple ( a, Q, tr, tc)-
grading both symmetries have a very simple and beautiful form. Thu s, we present
them in the corresponding tilde-version ~Hλ(K).
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 23
Conjecture 3.1. The homology ~Hλ(K) enjoys the following self-symmetry:
(3.8) ~Hλ
i,j,k,l(K)∼
= ~Hλ
i,−j,k−Rj,l−Sj (K).Moreover, we conjecture the existence of an involution Φ λ :Hλ(K)→H λ(K)
such that
(a, Q, tr, tc)[Φ λ(x)] = ( a(x),−Q(x), tr(x)− RQ(x), tc(x)− SQ(x)).
Note that this symmetry does not descend to any relation on the co lored HOM-
FLY polynomial (except in the uncolored case λ = ). In fact, due to a nontrivial
presence of the Q-grading, it can be seen only on the quadruply-graded homology,
and as to our knowledge, such symmetry has not been observed be fore.
For some knots, including torus knots (see below) we also conjectu re that this
involution comes from some version of the hard Lefshetz isomorphis m. Namely,
there exists an operator Lλ :Hλ(K)→H λ(K) such that
(3.9) ( a, q, Q, tr, tc)[Lλ] = (0 , R + S, 2, R, S), Φ λ(x) = L−Q(x)
λ .
Note, according to the “dictionary” (2.4) this operator is a bound s tate of R + S
D0-branes.
3.3. Mirror symmetry. Based on results for symmetric and anti-symmetric
representations, it was conjectured [ 42] that colored HOMFLY homology enjoys
mirror symmetry:
Conjecture 3.2. ([42]) For any knot, there exists an isomorphism (called
mirror symmetry ) between λ- and λt-colored HOMFLY homologies preserving the
a-grading and reversing the q-grading.
However, to obtain the behavior of the t-gradings under this symmetry, one
needs to introduce the fourth grading. We are able to write an explic it formulas
for the t-degrees change in the case of rectangular λ. We start with a diﬀerent
conjectural symmetry between λ- and λt-colored homology.
Conjecture 3.3. In ( a, Q, tr, tc) gradings one has
(3.10) ~Hλt
i,j,k,l(K)∼
= ~Hλ
i,j,l,k(K).In order to obtain the explicit quadruply-graded version of the mirr or symmetry
from (3.2), we combine self-symmetry (3.8) and mirror symmetry (3 .10):
Corollary 3.4. In ( a, Q, tr, tc) gradings one has
(3.11) ~Hλt
i,j,k,l(K)∼
= ~Hλ
i,−j,l−Sj,k−Rj (K).The last equation enables one to write the explicit change of gradings in the
mirror symmetry. Denote by Mλ :Hλ→H λt
the mirror symmetry isomorphism.
Consider the gradings of a generator x inHλ theory and the gradings of the gen-
erator Mλ(x) of Hλt
, denoted by ( ˆa,ˆq, ˆQ,ˆtr,ˆtc), where λ is an R× S rectangular
24 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
Young diagram and λt is S× R rectangular Young diagram. They are related by
the following transformation:
ˆa = a, ˆq =−q, ˆQ =−Q,
ˆtr = tc− SQ = (1 + S
R )tc− S
R tr− S
R q,
ˆtc = tr− RQ = tc− q.
Since the mirror symmetry (3.11) inverts the q-grading, it “categoriﬁes” the
following relation between the colored HOMFLY polynomials:
(3.12) P λ(K)(a, q) = P λt
(K)(a, q−1)
which is often attributed to level-rank duality.
3.4. sl(n|m) diﬀerentials. The homology Hλ(K) comes with a large struc-
ture of pairwise anti-commuting diﬀerentials on it. We conjecture th at there exists
a diﬀerential for every pair of nonnegative integers ( n, m), such that n≥ R or
m≥ S. These diﬀerentials should be related to the homologies correspond ing to
Lie superalgebras sl(n|m) and representations labeled by Young diagram λ. The
condition that n≥ R or m≥ S gives precisely those pairs ( n, m) for which the
Lie superalgebra sl(n|m) has an irreducible representation labeled by λ (see Sec-
tion 3.6). This generalizes the structure from [ 21] and [ 42], where the analogous
diﬀerentials are labelled by a single integer N and were related to the sl(N ) repre-
sentations, i.e. sl(N ) specializations of the λ-colored HOMFLY polynomial. As we
shall argue in this paper, the structure corresponding to Lie supe ralgebras is more
natural, and the single parameter N from [ 21] and [ 42] is just a super-rank of a
corresponding Lie superalgebra:
(3.13) N = n− m.
This structure has appeared in the physics literature [ 83, 86 ] as a symmetry
of brane/anti-brane systems, which makes it especially easy to imple ment it in
the brane system (2.2) or, better yet, in the dual system (2.6) wh ere the rank N
enters as the number of ﬁve-branes. In this framework, replacin g sl(N ) by a Lie
superalgebra sl(n|m) can be easily implemented by replacing N ﬁve-brane with a
system of n ﬁve-branes and m anti-branes.
Another, more supersymmetric way to realize quantum and homolog ical in-
variants of knots labeled by sl(n|m) representations is to consider n ﬁve-branes
supported on R× W× D exactly as in (2.6) and introduce m new ﬁve-branes
supported on R× W× D′, such that C∼
= D′⊂ M4 and D∩ D′ ={0},
space-time : R× T∗W× M4
n M5-branes : R× W× D(3.14)
m M5-branes : R× W× D′
For instance, if M4∼
= C2 is parametrized by coordinates ( z1, z2), then we can choose
D ={z1 = 0} and D′ ={z2 = 0}. Furthermore, identifying M4 with the Taub-
NUT space and reducing on the circle ﬁber takes us from M-theory t o type IIA
string theory with a system of D4-branes and D6-branes shown in F igure 9.
Then, as in [ 87], homological sl(n|m) knot invariants can be obtained by
“counting” solutions to the following partial diﬀerential equations o n a 5-manifold
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 25
D4 D4
D6
Figure 9. In the approach of [ 87], homological invariants of knots
labeled by representations of sl(n|m) can be realized by a system
of n semi-inﬁnite D4-branes ending on one side of the D6-brane
and m semi-inﬁnite D4-branes ending on the other side of the D6-
brane.
R× W× Ry:
F +− 1
4 B× B− 1
2 DyB = 0
Fyi + DjBji = 0
with the prescribed behavior near the “interface” y = 0:
B≃ B(±)
0
y as y→± 0 .
Here, B is a section of Ω 2,+(R× W )⊗ ad(E), so that
(B× B)ij =
∑
k
[Bik, Bjk]
Relegating further study of this physical system to a future work , we now return
to the discussion of mathematical structures that we expect to s ee in such physical
realizations of homological sl(n|m) knot invariants.
Conjecture 3.5. For every pair of nonnegative integers ( n, m) such that n≥
R or m≥ S there exists a diﬀerential dn|m on the homology Hλ(K), satisfying the
following properties:
• Specialization:
(3.15) ( Hλ(K), dn|m)|a=qn−m∼
=Hsl(n|m),λ(K).
• Anticommutativity: All dn|m pairwise anti-commute.
The homology theory Hsl(n|m),λ(K) categoriﬁes ( n− m)-specialization of the
λ-colored HOMFLY polynomial. In other words:
(3.16) P sl(n|m),λ(K)(q, t =−1) = P λ(K)(a = qn−m, q).
26 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
Although the right hand side of the above relation equals the quantu m polynomial
invariant associated with sl(n|m) representations labeled by λ, it depends only on
the super-rank of the Lie superalgebra. However, the homologies Hsl(n|m),λ(K) for
various pairs ( n, m) with ﬁxed n− m can in general be non-isomorphic. That is
one of the reasons why we expect to have diﬀerentials parametrize d by two integers
instead of just one, as it was predicted for the fundamental repr esentation [21] and
for the symmetric representations [ 42].
The main reason for the existence of such structure comes from t he representa-
tion theory of the Lie superalgebras sl(n|m). The condition that n≥ R or m≥ S
gives precisely those pairs ( n, m) for which the Lie superalgebra sl(n|m) has an
irreducible representation labeled by λ. We denote the subset of the ( x, y) plane
satisfying x≥ 0, y≥ 0 and x≥ R or y≥ S by Ω. Then, the set of all admissible
pairs (n, m) for which we have a diﬀerential dn|m consists exactly of the points from
Ω whose both coordinates are integers.
As for the degrees of the diﬀerentials dn|m, we have the following:
(3.17) ( a, q)[dn|m] = (−2, 2(n− m)),
in agreement with the specialization a = qn−m. The tc-degree is equal to
(3.18) tc[dn|m] =−2m− 1.
The tr-degree is more subtle, and is given in the next section; in particular, it
depends on R and S.
In the case of the fundamental [ 21] and the symmetric representations [ 42],
the conjectured diﬀerentials dN were parametrized by a single integer N . It was
argued that they correspond to the sl(N ) representations for N > 0, while for the
other values of N there was no clear motivation. However, when observed from
the sl(n|m) point of view, they become much more natural: dN becomes in fact
precisely the diﬀerential dn|m, where n and m are uniquely determined by requiring
that N = n− m and such that ( n, m) lies on the boundary of Ω, see Figure 10.
In the case of the fundamental representation, the t-degrees of the diﬀerentials
dN were deﬁned in a rather artiﬁcial way. By using the conventions fro m above,
we get directly the desired degrees. (Note that in the fundamenta l representations
the two t-gradings coincide: tr = tc = t.) Indeed, for N > 0, we have dN = dN|0,
and therefore according to (3.18) their t-degrees are equal to −1. For N = 0, we
have that d0 = d1|1, so the t-degree of d0 equals−3, while for N > 0, we have that
d−N = d0|N , and so the t-degree of d−N equals−2N− 1, exactly as predicted in
[21].
Although there are inﬁnitely many integer pairs in Ω, for a given knot K only
ﬁnitely many of the diﬀerentials dn|m can act non-trivially. Indeed, since Hλ(K)
is ﬁnite-dimensional and since q(dn|m) = 2( n− m) and tc(dn|m) = −2m− 1, the
diﬀerential dn|m becomes void on Hλ(K) for suﬃciently large values of n or m.
Thus we have:
Conjecture 3.6. For a knot K and a rectangular Young diagram λ, we have
(3.19) P sl(n|m),λ(K)(q, tr, tc) =P λ(K)(a = qn−m, q, tr, tc),
when either n or m is suﬃciently large.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 27
1
2
3
4
5
6
0 7 1 2 3 4 5 6
N=4 N=5 N=6 N=7
N=3
N=2
N=1
N=0
N=−1N=−2N=−3N=−4N=−5
N=−6
Ω
n
m
λt
Figure 10. Domain Ω can be visualized as the complement of λt
in a positive quadrant of the ( n, m) plane. Integer points on its
boundary correspond to diﬀerentials dn|m or, equivalently, dN with
N = n− m, among which three are special. They correspond to
the three corners of the domain Ω and are marked by red bullets.
The diﬀerentials for this examples are shown in Figure 11.
3.5. Colored diﬀerentials. For every knot K, the homology theory Hλ(K)
comes with a remarkable structure of the so-called colored diﬀerentials that allow
passage to homology theories Hµ(K) for various partitions µ⊂ λ. In other words,
for certain such partitions µ, there exists a diﬀerential d onHλ(K) such that the
homology with respect to this diﬀerential is isomorphic to Hµ(K), i.e.
(3.20) H∗(Hλ(K), d)∼
=Hµ(K).
As we shall describe, the possible partitions µ will be the ones that can be obtained
by removing either some rows or some columns from λ. All these diﬀerentials are
in fact “lifting” sl(n|m) diﬀerentials dn|m for some speciﬁc values of ( n, m) that
are on the boundary of the region Ω, see Figure 10. These are prec isely the pairs
(n, m) such that λ∼
= µ as sl(n|m) representations (see section 3.6). We denote the
corresponding colored diﬀerential by dcol
n|m, and the “lifting” property is given by
the following commutative triangle:
Hλ(K)
dcol
n|m
−−−−−−− → Hµ(K)
dn|m dn|m
↓ ↓
Hsl(n|m),λ(K)
∼
=−−−−−−−−→ Hsl(n|m),µ(K)
28 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
Here the arrow going from H1 toH2 labeled by d means that a diﬀerential d on
H1 is such that H∗(H1, d)∼
=H2. In particular, note that the two diﬀerentials, both
denoted dn|m, are essentially diﬀerent since they are deﬁned on diﬀerent homolog y
theories. The diﬀerentials dn|m and dcol
n|m are very similar, in particular, the four
gradings of dn|m and dcol
n|m are identical.
We show that for each rectangular diagram µ that is obtained from λ by re-
moving either some rows or some columns, there exist two diﬀerent d iﬀerentials on
Hλ realizing the isomorphism (3.20). As we explained, all these colored diﬀ erentials
are of the form dcol
n|m. However, in order to clearly indicate the color-changing prop-
erty of the diﬀerential, we also label them by a superscript “ ±” as in d±
λ→µ. One
of them will be denoted as d+
λ→µ: it has positive Q-degree (equal to +2), and we
will be referred to as the positive diﬀerential . The second diﬀerential has negative
Q-degree (equal to −2) and will be denoted by d−
λ→µ.
We will show that d+
λ→µ and d−
λ→µ are exchanged by the involution Φ λ. In a
particular case when µ =∅, the homology Hµ is one-dimensional and the corre-
sponding colored diﬀerentials are called canceling diﬀerentials. All these diﬀeren-
tials are deep generalizations of the diﬀerentials d1 and d−1 in the uncolored theory
[21], which can be considered as colored diﬀerentials to the trivial repre sentation
∅. Positive colored diﬀerentials can be seen as analogs of d1 and negative colored
diﬀerentials can be seen as analogs of d−1.
Now, let us give a more precise deﬁnition of colored diﬀerentials, toge ther
with the explicit change of gradings in the isomorphism (3.20). We note that the
introduction of the fourth grading is again crucial: the Q-grading is indispensable
for the explicit re-gradings.
Let Σ denote the S-invariant of a knot K, i.e. it is even integer such that
the homology of the uncolored homology H
(K) with respect to the canceling
diﬀerential d1, which is one-dimensional, has ( a, q, tr, tc)-degree (Σ ,−Σ , 0, 0), see
[21, 73 ].
Positive row-removing diﬀerentials: For any 0 ≤ k < R there exists
a “row-removing diﬀerential” d+
R×S→k×S (which is in fact dcol
R+k|0) such that the
homology ofHR×S(K) with respect to it is isomorphic to Hk×S(K). In particular,
for k = 0 the diﬀerential d+
R×S→∅ is canceling. These diﬀerentials have the following
degrees:
(3.21) ( a, q, tr, tc)[d+
R×S→k×S ] = (−2, 2R + 2k,−2k− 1,−1).
Since Q = q+tr−tc
R , we have Q[d+
R×S→k×S] = 2 . The explicit grading change in the
corresponding isomorphism (3.20) is as follows: let x be a generator of Hk×S(K)
with degree ( a, Q, tr, tc, q). Then the degrees of the corresponding generator φ(x)
of H∗(HR×S(K), d+
R×S→k×S), denoted by (ˆa,ˆQ,ˆtr,ˆtc,ˆq), are given by:
ˆa = a + S(R− k)Σ , ˆQ = Q− S(R− k)Σ ,
ˆtr = tr + (R− k)Q + Sk(R− k)Σ ,
ˆtc = tc, ˆq = q− S(R− k)(R + k)Σ .
Positive column-removing diﬀerentials: For any 0 ≤ l < S there exists
a “column-removing diﬀerential” d+
R×S→R×l (which is in fact dcol
R|l) such that the
homology ofHR×S(K) with respect to it is isomorphic to HR×l(K). In particular,
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 29
for l = 0 the diﬀerential d+
R×S→∅ is canceling and coincides with the canceling
diﬀerential above. These diﬀerentials have the following degrees:
(a, q, tr, tc)[d+
R×S→R×l] = (−2, 2R− 2l,−1,−2l− 1).
One can check that Q[d+
R×S→R×l] = 2 . The grading change formulas have the form:
ˆa = a + R(S− l)Σ , ˆQ = Q− R(S− l)Σ ,
ˆtr = tr, ˆtc = tc + (S− l)Q + Rl(S− l)Σ ,
ˆq = q + (S− l)Q + R(S− l)(l− R)Σ .
Negative row-removing diﬀerentials: For any 0 ≤ k < R there exists a
“row-removing diﬀerential” d−
R×S→k×S (which is in fact dcol
k|S) such that the homol-
ogy of HR×S(K) with respect to it is isomorphic to Hk×S(K). In particular, for
k = 0 the diﬀerential d−
R×S→∅ is canceling. These diﬀerentials have the following
degrees:
(a, q, tr, tc)[d−
R×S→k×S ] = (−2, 2k− 2S,−2k− 2R− 1,−2S− 1).
One can check that Q[d−
R×S→k×S] = −2. The grading change formulas have the
form:
ˆa = a + S(R− k)Σ , ˆQ = Q + S(R− k)Σ ,
ˆtr = tr + S(R− k)(R + k)Σ , ˆtc = tc + S2(R− k)Σ ,
ˆq = q + kQ + S(R− k)(S− k)Σ .
Negative column-removing diﬀerentials: For any 0≤ l < S there exists
a “column-removing diﬀerential” d−
R×S→R×l (which is in fact dcol
0|S+l) such that the
homology ofHR×S(K) with respect to it is isomorphic to HR×l(K). In particular,
for l = 0 the diﬀerential d−
R×S→∅ is canceling and coincides with the canceling
negative diﬀerential above. These diﬀerentials have the following de grees:
(a, q, tr, tc)[d+
R×S→R×l] = (−2,−2l− 2S,−2R− 1,−2l− 2S− 1).
One can check that Q[d+
R×S→R×l] = −2. The grading change formulas have the
form:
ˆa = a + R(S− l)Σ , ˆQ = Q + R(S− l)Σ ,
ˆtr = tr + R2(S− l)Σ , ˆtc = tc + R(S− l)(S + l)Σ ,
ˆq = q + R(S− l)(S + l)Σ .
To explain better such a large structure of diﬀerentials, we presen t them in
Figure 11. This diagram represents the case of the representatio n labeled by the
Young diagram with R = 4 rows and S = 5 columns. An arrow labelled by dn|m
going from Young diagram D1 to D2 means that there exists a diﬀerential dcol
n|m on
HD1(K) andHD2 (K), such that
(3.22) H∗(HD1 (K), dcol
n|m)∼
=HD2 (K).
There are three ”special” diﬀerentials which are represented by th ick lines: two
of them ( dcol
4|0 and dcol
0|5) are canceling, i.e. the homology with respect to them is
one-dimensional, and the third one (the middle one) is trivial dcol
4|5 = 0.
30 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
• •
d0|9
d0|8
d0|7
d0|6
d0|5
CANCELING
d1|5
d2|5
d3|5
dcol
4|5 = 0
d4|4
d4|3
d4|2
d4|1
d4|0
CANCELING
d5|0
d6|0
d7|0
Figure 11. Colored diﬀerentials for the 4 × 5 rectangle.
In a general case of an arbitrary R× S rectangular Young diagram λ, the
picture would be of the same form with 2 R + 2 S− 1 diﬀerentials: written in a
clockwise direction, they will be dR+i|0, with i ranging i = R− 1, . . . ,0, dR|i, with
i ranging i = 0 , . . . , S, di|S, with i ranging i = R− 1, . . . ,0, and d0|S+i, with i
ranging i = 0 , . . . , S− 1, The canceling diﬀerentials will be the diﬀerentials dR|0
and d0|S, while the middle one would be dR|S.5
In the upper half of the diagram are the positive row- and negative c olumn-
removing diﬀerentials, with the row-removing ( dR+i|0 with 0 ≤ i < R ) being in
the upper right part and column-removing ( d0|S+i with 0 ≤ i < S ) being in the
upper left part of the diagram. The negative row- and positive colum n-removing
diﬀerentials are in the lower half of the picture (below the canceling diﬀ erentials).
The row-removing ones ( di|S with 0≤ i < R ) are in the lower left part and column-
removing ( dR|i with 0 ≤ i < S ) are in the lower right part of the diagram. The
positive colored diﬀerentials are in the right half of the diagram, while t he negative
5Although this middle colored diﬀerential dcol
R|S is trivial, the sl(R|S) colored diﬀerential dR|S
is in general non-trivial and is related to knot Floer homolo gy, in the same way as the diﬀerential
d0 in the uncolored case [ 21]. W e discuss these HFK-like diﬀerentials in Section 3.10.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 31
colored diﬀerentials are in the left half.
We conjecture that the collection of diﬀerentials is self-contained u nder the
mirror symmetry and self-symmetry isomorphism. Namely, Let λ be a rectangular
Young diagram and let µ be obtained from λ by removal of some of the rows or
columns. Then the following identities hold:
Φ λ(d+
λ→µ(x)) = d−
λ→µ(Φ λ(x)),(3.23)
Mλ(d±
λ→µ(x)) = d±
λt→µt (Mλ(x))).(3.24)
The involution Φ provides an isomorphism
(3.25) H∗(Hλ(K), d+
λ→µ(x))
Φ
−→ H∗(Hλ(K), d−
λ→µ(x)).
3.6. Representation theory interpretation of the colored d iﬀerentials.
The main explanation for the existence of all these positive and nega tive colored
diﬀerentials with the wanted behavior comes from the representat ion theory of
sl(n) and sl(n|m). We include the classical Lie algebra sl(n) in the family of Lie
superalgebras sl(m|n), by identifying it with sl(n|0).
Indeed, it is well-known that the irreducible polynomial representat ions of sl(n)
are labeled with the Young diagrams with at most n rows. Moreover, some of
these representations are isomorphic: namely, for every k with 0 ≤ k < R , the
representations labeled by the rectangular Young diagrams R× S and k× S are
isomorphic as sl(R+k)-representations. This in turn implies that the doubly-graded
homologiesHsl(R+k),R×S andHsl(R+k),k×S categorifying respectively the quantum
polynomial invariants P sl(R+k),R×S(q) and P sl(R+k),k×S(q), should be isomorphic.
Finally, since Hsl(R+k),R×S is isomorphic to the homology of HR×S with respect
to the diﬀerential dR+k|0, we obtain the explanation of the wanted behavior of the
positive row-removing diﬀerentials.
As for the positive column-removing diﬀerentials one should look for t he rep-
resentations of the Lie superalgrebras sl(n|m). There is an analogous theory for
the polynomial representations of sl(n|m) [ 6, 7 ], extending the classical case of
sl(n) algebras. This time, the irreducible representations are labeled by Young
diagrams such that the ( n + 1)-st row contains at most m boxes. Again, some of
these representations are isomorphic: for every k with 0 ≤ k < S we have that
the representations labeled by the rectangular Young diagrams R× S and R× k
are isomorphic as sl(R|k)-representations. Now one gets the homology theory cor-
responding to the ( sl(R|k), R× S)-representations as the homology of HR×S with
respect to dR|k. Hence, the above isomorphisms of the sl(R|k)-representations give
rise to the positive column-removing diﬀerentials.
As for the negative diﬀerentials, they can be obtained in the same wa y as the
positive diﬀerentials by using “dual” isomorphisms from above, combin ed with the
mirror symmetry. Indeed, for two Young diagrams λ and µ we have the following
isomorphism of representations:
(3.26) λ∼
= µ, as sl(n|m) representations ,
if and only if
(3.27) λt∼
= µt, as sl(m|n) representations .
In such way the existence of the negative row-removing diﬀerentia ls dcol
k|S with 0≤
k < R is a consequence of the isomorphism of sl(k|S)-representations corresponding
32 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
to Young diagrams R× S and k× S. Finally, the existence of negative column-
removing diﬀerentials dcol
0|S+k with 0 ≤ k < S follows from the isomorphism of
sl(0|S + k)-representations corresponding to Young diagrams R× S and R× k.
3.7. Universal colored diﬀerentials. There exists yet another set of colored
diﬀerentials on Hλ(K) such that the homology with respect to any of them is
isomorphic to Hλ′
(K) for some λ′ obtained from λ by removing some of its rows
or columns. The diﬀerence with respect to the diﬀerentials dcol
n|m from above is that
they are universal in the sense that their a-degree is equal to 0.
Although the insights from the theory of deformations of potentia ls imply that
such universal colored diﬀerentials should exists for any row- or co lumn-removal,
we have managed to ﬁnd explicitly such diﬀerentials only in the cases wh en λ has
two rows or two columns.
Conjecture 3.7. Let K be a knot. Let λ be 2× S rectangular diagram and
let λ′ be 1× S rectangular diagram. Then there exists a diﬀerential d↑ onHλ(K)
of a-degree 0, such that the homology of Hλ(K) with respect to d↑ is isomorphic
toHλ′
(K).
Let µ be R× 2 rectangular diagram and let µ′ be R× 1 rectangular diagram.
Then their exists a diﬀerential d← onHµ(K) of a-degree 0 such that the homology
ofHµ(K) with respect to d← is isomorphic to Hµ′
(K).
To be more precise, we give explicit values for the degrees of diﬀeren tials d↑
and d← and the degree changes in the isomorphisms of the Conjecture 3.7. We
describe everything in the ( a, Q, tr, tc, q)-gradings. The degrees of the diﬀerentials
are given by:
deg d↑ = (0 , 0,−2, 0, 2),(3.28)
deg d← = (0 , 0, 0, 2, 2).(3.29)
The ﬁrst isomorphism from Conjecture 3.7 gives:
(3.30) H∗(Hλ(K), d↑)∼
=Hλ′
(K).
Let x be a generator of Hλ′
(K) with degree ( a, Q, tr, tc, q). Then the degrees of
the corresponding generator φ(x) of H∗(Hλ(K), dN ), denoted by (ˆa,ˆQ,ˆtr,ˆtc,ˆq), are
given by:
ˆa = 2a, ˆQ = 2Q, ˆtr = 4tr,
ˆtc = 2tc, ˆq = 4q− 2tc.
The second isomorphism from Conjecture 3.7 gives:
(3.31) H∗(Hµ(K), d←)∼
=Hµ′
(K).
Let x be a generator of Hµ′
(K) with degree ( a, Q, tr, tc, q). Then the degrees of
the corresponding generator φ(x) of H∗(Hµ(K), dN ), denoted by (ˆa,ˆQ,ˆtr,ˆtc,ˆq), are
given by:
ˆa = 2a, ˆQ = 2Q, ˆtr = 2tr,
ˆtc = 4tc, ˆq = 2q + 2tc.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 33
3.8. Reﬁned exponential growth. Now we are ready to formulate a quan-
titative reﬁnement of the “exponential growth conjecture” fro m [ 42].
Conjecture 3.8. Let K be either two-bridge knot or a torus knot. Let
~P λ(K)(a, Q, tr) denote the Poincar´ e polynomial (in ( a, Q, tr) gradings, i.e. after
setting tc = 1) of ~Hλ(K). Let ~P Λ R
(K)(a, Q, tr) denote the Poincar´ e polynomial
of ~HΛ R
(K) ( R-th antisymmetric colored homology). Then the following relation
holds:
(3.32) ~P λ(K)(a, Q, tr) =
(
~P Λ R
(K)(a, Q, tr)
) S
.
By using the mirror symmetry and by switching tr←→ tc, we get the dual
statement:
Conjecture 3.9. Let K be either two-bridge knot or a torus knot. Let
~P λ(K)(a, Q, tc) denote the Poincar´ e polynomial in ( a, Q, tc) gradings of ~Hλ(K).
Let ~P SS
(K)(a, Q, tc) denote the Poincar´ e polynomial of ~HSS
(K) ( S-th symmetric
colored homology). Then the following relation holds:
(3.33) ~P λ(K)(a, Q, tc) =
(
~P SS
(K)(a, Q, tc)
) R
.
Corollary 3.10. The dimensions of the “rectangular homology groups” sat-
isfy the equation
(3.34) dim Hλ(K) =
(
dimH
(K
)
)|λ|.
Moreover, the similar statement holds in ( a, Q)-gradings, i.e. with both tr and tc
specialized to 1:
(3.35) ~P λ(K)(a, Q) =
(
~P
(K)(a, Q)
) |λ|
.
Corollary 3.11. The Poincar´ e polynomial of the symmetric homology in
(a, Q, tr) gradings can be deduced from the uncolored Poincar´ e polynomial (recall
that tr = tc = t for the uncolored homology):
(3.36) ~P Sr
(K)(a, Q = q, tr = t, tc = 1) =
(
P (K)(a, q, t)
) r
.
The Poincar´ e polynomial of the antisymmetric homology in ( a, Q, tc) gradings can
be deduced from the uncolored Poincar´ e polynomial:
(3.37) ~P Λ r
(K)(a, Q = q, tr = 1, tc = t) =
(
P
(K)(a, q, t)
) r
.
Going back to original q-degrees, i.e. the ordinary version of the colored ho-
mologyHλ(K), the above relations reduce to two-variable (in variables a and t)
exponential growths:
(3.38) P Sr
(K)(a, q = 1, tr = t, tc = 1) =
(
P
(K)(a, q = 1, t)
) r
,
and
(3.39) P Λ r
(K)(a, q = 1, tr = 1, tc = t) =
(
P
(K)(a, q = 1, t)
) r
.
Although such nice (and surprising) exponential growth propertie s should exist for
large classes of knots, it is not expected that it should hold in genera l, i.e. for
every knot. For example, the uncolored homology of the knot 9 42 is 9-dimensional
(see [ 21]), its (triply-graded) S2-colored homology is computed and the result has
34 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
401 generators. Therefore, we don’t have any exponential grow th property for it. 6
Nevertheless, such exponential growth property should hold in ge neral but only
asymptotically, as we brieﬂy explain in the following subsection.
3.9. Relation to the super- A-polynomial. The exponential growth of the
colored HOMFLY homology summarized in (3.32)–(3.36) nicely compleme nts the
results of [ 26, 27, 68 ], where the large- r limit of the Sr homology was studied in
detail. In particular, it was conjectured in [ 27] that for an arbitrary knot K the Sr-
colored superpolynomials obey a recursion relation that comes from quantization
of an algebraic curve Asuper(x, y; a, t) = 0. Speciﬁcally, this recursion relation has
the following general form:
(3.40) P Sr+n
(K; a, q, t) + an−1P Sr+n−1
(K; a, q, t) + . . . + a0P Sr
(K; a, q, t) = 0
and can be conveniently expressed in the operator form ˆAsuperP S∗
= 0, where the
coeﬃcients ai≡ ai(x, a, q, t) are rational functions of a, q, t, and x≡ qr. To make
contact with (3.35), we need to set q = 1 which, by deﬁnition, reduces the operator
ˆAsuper to its characteristic polynomial, the super- A-polynomial Asuper(x, y; a, t).
Furthermore, since setting q = 1 also implies x = qr = 1, we conclude that
making contact with (3.35) involves comparison with the super- A-polynomial eval-
uated as x = 1. Something very nice happens in this limit; namely, in every example
studied so far, all coeﬃcients ai(x; a, t) of the super- A-polynomial vanish, except
for an−1. As a result, (3.40) reduces to a much simpler recursion relation:
(3.41) P Sr+n
(K; a, q = 1, t) + an−1(x = 1, a, t)P Sr+n−1
(K; a, q = 1, t) = 0 ,
which indeed takes the form (3.35). Speciﬁcally, it can be consistent with (3.35) if
and only if an−1(x = 1 , a, t) =P(K; a, q = 1 , t). We conjecture that this is always
the case, therefore, providing a bridge between our present wor k and [ 26, 27, 68 ]:
Conjecture 3.12. For any knot K, the following relation between the super-
A-polynomial Asuper(x, y; a, t) and the (uncolored) superpolynomial holds:
(3.42) Asuper(x = 1, y; a, t) = yk + yk−1P(K; a, q = 1, t) .
3.10. Symmetric and antisymmetric representations. In [42] the triply-
graded colored HOMFLY homology for the symmetric and antisymmet ric repre-
sentations have been computed for plenty of knots. We obtain a qu adruply-graded
theory by adding a t-degree of the corresponding generator of the colored homology
for the dual representation. The t-grading we used in [ 42] (and called “old”) corre-
sponds to tr-grading in this paper. The other tc-grading coincides with the t-grading
used in [ 2, 20, 21, 43 ]. In the case of the symmetric representations, we have two
additional properties of the quadruply-graded colored homology: δ-grading and
HFK-like diﬀerential. To every generator x of Sr-colored quadruply-graded theory
we can associate a δ-grading by:
(3.43) δ(x) = a(x) + q(x)
2 − tr(x) + tc(x)
2 = a(x) + Q(x)
2 − tr(x).
6This could also be seen on the level of the S2-colored HOMFLY polynomial of 9 42. It has
nonzero terms with a-degree − 6, while the uncolored homology is concentrated in a-degrees -2,0
and 2. W e thank Paul W edrich for providing us with his computa tions of the colored HOMFLY
polynomials.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 35
We call a knot K S r-thin if all generators of HSr
(K) have the same δ-grading.
In the uncolored case, r = 1, this coincides with the deﬁnition of a thin knot. Also,
in the uncolored case, the δ-grading of all generators of a thin knot K is equal to
Σ /2, where Σ is deﬁned as in Section 3.5. We conjecture that every thin knot K is
also Sr-thin with the δ-grading of all generators of HSr
(K) being equal to rΣ /2.
We also conjecture that the reﬁned exponential growth conject ure (3.36) holds for
all thin knots.
The action of the “special” diﬀerential d1|r on Sr-colored homology is related
to the action of the diﬀerential d1|1 on the uncolored homology. The latter one
is denoted d0 in [ 21] and it is conjectured that the homology H∗(H (K), d0) is
isomorphic to the knot Floer homology of K. We conjecture the following isomor-
phism:
(3.44) ( ~HSr
(K), d1|r)(a, Q = q, tr = t, tc = 1) =
(
H
(K), d1|1)(a, q, t)
) r
.
We note two things: ﬁrst, the above property does not descend t o any relation
on the colored HOMFLY polynomial level, due to the non-trivial prese nce of the
Q-grading. Secondly, both d1|1 onH (K) and d1|r onHSr
(K) have non-zero δ-
grading and therefore act trivially on thin knots. Hence, the relatio n (3.44) in the
case of thin knots becomes simply (3.36). However, once we pass to thick knots, in
general the two relations are diﬀerent, as we shall show in the exam ple below for
the (3,4)-torus knot.
3.11. Rectangular vs. non-rectangular representations. What makes
rectangular representations special? Well, these are precisely rep resentations, whose
corresponding knot invariants obey Hirota equation. Speciﬁcally, if λ is a Young
diagram of size R× S, then the corresponding invariants P λ≡ PR,S obey recursion
equations of the form
(3.45) P 2
R,S = PR+1,S PR−1,S + PR,S+1 PR,S−1
or
(3.46) PR,S(u + 1) PR,S(u− 1) = PR+1,S (u) PR−1,S(u) + PR,S+1(u) PR,S−1(u)
where u is the spectral parameter. Both of these equations are variants of the
familiar Hirota equation. For instance, it is easy to verify that
(3.47) PR,S (
) =
R∏
i=1
S∏
j=1
aqj−i− a−1q−j+i
qR+S−i−j+1− q−(R+S−i−j+1)
satisﬁes (3.45).
Another special property of the rectangular Young diagram, is th at these
are precisely the Young diagrams λ such that for every Young diagram µ, the
Littlewood-Richardson coeﬃcient cµ
λ,λ is either 0 or 1. These in turn are precisely
those λ for which the two-variable HOMFLY polynomial P λ(K)(a, q) does not de-
tect mutants (see [ 65]).
