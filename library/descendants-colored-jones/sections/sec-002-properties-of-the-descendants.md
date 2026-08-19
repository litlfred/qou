---
doc_id: descendants-colored-jones
doc_title: "Pure and Applied Mathematics Quarterly"
section_id: sec-002-properties-of-the-descendants
section_title: "Properties of the descendants"
section_number: null
pages: 5-8
source_pdf: descendants_colored_jones.pdf
source_sha256: f00693a5926c074f
doc_brief: "Pure and Applied Mathematics Quarterly The descendant colored Jones polynomials — We discuss two realizations of the colored Jones polyno- mials of a knot, one appearing in an unnoticed work of the"
---
From their very deﬁnition, the 0-th descendants DJ (0)
n (q)a n dD J(0)(q)a r e
nothing but the colored Jones polynomial Jn(q) and the Kashaev invariant of
2312 Stavros Garoufalidis and Rinat Kashaev
the knot. Thus, one may call DJ (m)
n (q)a n dD J(m)(q) the descendant colored
Jones and the descendant Kashaev invariant of a knot, respectively.
Note further that for all integers m, the 3-variable invariant DJ (m)(x, q)
is an element of the colored Habiro ring, and, for all n ≥ 0, it satisﬁes
DJ(m)(qn,q )=D J (m)
n (q).
Note moreover that DJ(m)
n (q) ∈ Z[q±]f o rn ≥ 1w h e r e a sD J(m)(q) ∈ ˆZ[q].
In a sense, DJ (m)(q) is a twisted Fourier transform of J n(q).
The next proposition describes the equivalence among these knot invari-
ants. Let μ denote the set of complex roots of unity.
Proposition 2.2. Each family of invariants {Jn(q)|n ∈ Z≥0}, {DJ(m)
n (q)|n ∈
Z≥0,m ∈ Z}, {DJ(m)(x, q)|m ∈ Z}, {DJ(m)(q)|m ∈ Z}, {Jn(ζ)|n ∈ Z≥0,ζ ∈
μ}, {DJ(m)
n (ζ)|n ∈ Z≥0,ζ ∈ μ}, {DJ(m)(x, ζ)m ∈ Z,ζ ∈ μ}, {DJ(m)(ζ)|m ∈
Z,ζ ∈ μ} determines all other families.
Proof. We ﬁrst discuss the equivalence of invariants in the left triangle of
Diagram ( 1). Clearly, the descendant colored Jones polynomials DJ (m)
n (q)
specialize to the colored Jones polynomials J n(q)w h e nm =0 .C o n v e r s e l y ,
Jn(q) determines H k(q) by Equation ( 2) and hence determines DJ (m)
n (q)b y
Equation (5).
The evaluation maps Λ → ˆZ[q]g i v e nb yx ↦→ qn for all n give an injection
of Λ to ˆZ[q]
N
as was shown in [ Hab08]. It follows that DJ (m)
n (q) determines
DJ(m)(x, q).
This shows that each one of the invariants Jn(q), DJ(m)
n (q), DJ(m)(x, q)d e -
termines all others. Moreover, since the collection of evaluation maps ˆZ[q] →
Q given by q ↦→ ζ uniquely determines an element of the Habiro ring [Hab04],
and the same holds for the colored Habiro ring [ Hab08], it follows that each
one of the invariants Jn(q), DJ(m)
n (q), DJ(m)(x, q), Jn(ζ), DJ(m)
n (ζ), DJ(m)(x, ζ)
determines all others.
We now discuss the equivalence of invariants in the right triangle of Di-
agram (1). The descendant colored Jones polynomials DJ (m)
n (q) specialize to
DJ(m)(q)w h e nn = 0, which specialize to DJ (m)(ζ) for any complex root of
unity ζ. Moreover, by Equation ( 5) and the inversion of the discrete Fourier
transform, it follows that DJ (m)(ζ) determines ( ζ; ζ)k(ζ−1; ζ−1)k Hk(ζ), and
hence, (q; q)k(q−1; q−1)k Hk(q) (since the latter are inZ[q±]), and hence Hk(q),
and hence DJ(m)
n (q).
The next proposition concerns the q-holonomic properties of the descen-
dant colored Jones functions. For a detailed deﬁnition of q-holonomic func-
tions in several variables and their closure properties, we refer the reader to
[Zei90, PWZ96]a n da l s ot o[Sab93, GL16]. Roughly speaking, q-holonomic
The descendant colored Jones polynomials 2313
functions have annihilating ideals (i.e., ideals of linear q-diﬀerence equations)
of maximal dimension.
Proposition 2.3. DJ(m)
n (q), DJ(m)(x, q)a n dD J(m)(q)a r eq-holonomic func-
tions of ( m, n), (m, x)a n d m, respectively. Linear q-diﬀerence equations for
these functions can be obtained from one for the Habiro polynomials H k(q).
Proof. The ﬁrst part follows from the closure properties of q-holonomic func-
tions explained in detail in [GL16], and the fact that the colored Jones polyno-
mial (and hence, the sequence of Habiro polynomials) is q-holonomic [GL05]
and cn,k(q)a n d gk,n(q)a r e q-holonomic (in fact q-proper hypergeometric)
functions. Using a computer implementation given by Koutschan [ Kou09,
Kou10], we can obtain a linear q-diﬀerence equation for DJ (m)(q)g i v e no n e
for Hk(q). The obtained linear q-diﬀerence equations may not be of the small-
est order.
The above proposition implies that the annihilating ideal of the 3-variable
invariant DJ(m)(x, q) is a knot invariant, and so is a minimal recursion of
DJ(m)(x, q) with respect to x or m. Moreover, a minimal recursion with re-
spect to m can be computed from a recursion for the Habiro polynomials H k
as well as some of their initial values. This is illustrated in Section 2.5 below.
The annihilating polynomial of DJ (m)(x, q) with respect to m has an ex-
cess degree whose relation to the character variety of SL2(C)-representations
is a challenging question discussed in Section 2.5 below.
To eﬀectively apply Proposition 2.3 we need to know a recursion for the
Habiro polynomials of a knot. Such a recursion can be obtained from a q-
hypergeometric formula for the Habiro polynomials, as was done in [GS06]f o r
all twist knots using a formula for the Habiro polynomials given in [ Hab02,
Mas03]. Alternatively, one can use a recursion for J n(q), Equation ( 3)a n d
the methods of [ Kou10] to obtain a recursion for the Habiro polynomials.
Although the above mentioned computer implementation in theory succeeds
(and does so with a certiﬁed computation), in practice it may not termi-
nate. As a concrete example, the colored Jones polynomials of the ( −2, 3, 7)
pretzel knot satisfy a guessed inhomogeneous sixth order q-diﬀerence equa-
tion [GK12], but a direct attempt to ﬁnd a recursion for its Habiro polyno-
mials did not terminate. Instead, one can use the recursion for the colored
Jones to compute several thousand values of them (modulo a prime) and
Equation (3) to do the same for the Habiro polynomials, and with some hints
for the shape of the Newton polygon to guess a recursion for the Habiro
polynomials. This is explained in detail for the (−2, 3, 7) pretzel knot and for
several other knots in forthcoming work [ GK].
2314 Stavros Garoufalidis and Rinat Kashaev
Let us comment on the chirality properties of the descendant colored
Jones functions. It is well-known that the Jones polynomial (and its colored
versions) are chiral invariants of knots. Explicitly, ifK∗ denotes the mirror of
ak n o tK,t h e nJK∗
n (q)=J n(q−1) which implies that H K∗
k (q)=H k(q−1)a n d
DJK∗,(m)(x, q)=D J K,(−m)(x−1,q −1).
