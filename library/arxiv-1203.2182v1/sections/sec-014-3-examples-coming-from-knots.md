---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-014-3-examples-coming-from-knots
section_title: "Examples coming from knots"
section_number: 3
pages: 8-12
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
In this section, we illustrate the reﬁned / categoriﬁed volume conjectures stated in the general
form in (2.1) and (2.6) for a large class of examples coming fr om knots. In these examples,
the invariants Pn(q,t ) whose recursive behavior is captured by the conjectures en code the
graded dimensions of the homological knot invariants.
There are many diﬀerent kinds of homological knot invariants: doubly-graded and triply-
graded, reduced and unreduced, with diﬀerent choices of fram ing and grading conventions.
And, in our discussion we will need at least a basic understan ding of these concepts in order
to have most fun with the conjectures (2.1a) and (2.6a). In ot her words, we will need to
have at least a rough understanding of the relation between d iﬀerent types of knot invariants
shown in Figure 2. Luckily, much of this picture can be explai ned building on the relations
between polynomial knot invariants, which hopefully are mo re familiar to the reader.
– 7 –
a = q N dN
Euler characteristic (t=−1)
Euler characteristic (t=−1)
categorification
categorification colored HOMFLY
homology / superpolynomial
invariant
P
sl(N) knot homology
P
sl(N),R sl(N),R
R
polynomial
colored HOMFLY
sl(N) quantum group
R
a,q,t(K;       )a,q
q (K;    )J      (K;  )
P (K;     )
q,t
Figure 2: Categoriﬁcation of quantum knot invariants. To help the reader na vigate through this
picture we suggest to keep track of the variables a, q, t, as well as the rank of sl(N). Note, the
polynomial (resp. homological) knot invariants which have a-dependence (resp. a-grading) are not
labeled by sl(N).
We start with the lower left corner of the Figure 2 that descri bes the simplest family
of polynomial knot invariants J g,R(K;q) labeled by a representation R of a Lie algebra g =
Lie(G). In the special case when R =Vn is then-dimensional representation of g =sl(2), the
quantum group invariant Jn(K;q) := J sl(2),Vn(K;q) is the n-colored Jones polynomial of a
knot/linkK that we already encountered in the review of the generalized volume conjectures
(1.2) and (1.5). In general, a mathematical deﬁnition of J g,R(K;q) involves associating a
quantum R-matrix to every crossing in a plane diagram of a kno t K. Physically, these
quantum group invariants are simply the normalized expressions for the partition function of
Chern-Simons gauge theory [25]:
Z CS
G (M,K R;q) :=
∫
[dA]WR(K)[A]eikSCS[A;M ] (3.1)
with a Wilson loop operator WR(K)[A] := TrRP exp
[∮
KA
]
supported on a knot K and dec-
orated by a representationR. Here, SCS[A;M] is the famous Chern-Simons action functional
on a 3-manifold M,
SCS[A;M] = 1
4π
∫
M
Tradj
(
A ∧dA + 2
3A ∧A ∧A
)
. (3.2)
In general, the partition function (3.1) is a rather complic ated function of the coupling con-
stant k or, equivalently, the “quantum” parameter q = e
2πi
k+h . However, once normalized by
that of the unknot, it magically becomes a polynomial in q with integer coeﬃcients, at least
when M = S3:
J g,R(K;q) = Z CS
G (S3,K R;q)
Z CS
G (S3, R;q). (3.3)
– 8 –
The fact that the ﬁnal result turns out to be a polynomial, let alone integer coeﬃcients, is
not at all obvious in either R-matrix or path integral formul ation of J g,R(K;q). This nice
property, however, is a precursor of knot homologies, which beautifully explain it.
Another nice property comes from a closer look at g = sl(N), which will be the focus
our paper. (Although there are straightforward analogs for other classical groups, we will
not consider them here.) Then, not only J sl(N ),R(K;q) turn out to be polynomials in q, they
exhibit a very simple dependence on N. Namely, for each R (= Young tableaux) there exists
a polynomial invariant P R(K;a,q ) of a knot K, such that
J sl(N ),R(K;q) = P R(K;a =qN,q ). (3.4)
This relation is represented by a vertical arrow on the left i n Figure 2. The polynomial
P R(K;a,q ) is called the colored HOMFLY polynomial of K. To be more precise, it is the
normalized HOMFLY polynomial, meaning that P R( ) = 1.
Once we explained the left side of Figure 2, we can easily desc ribe its categoriﬁcation
shown on the right. To categorify J sl(N ),R(K;q) means to construct a doubly-graded homol-
ogy theory Hsl(N ),R
i,j (K), with gradings i andj, such that the polynomial J sl(N ),R(K;q) is its
q-graded Euler characteristic:
J sl(N ),R(K;q) = P R(K;a =qN,q ) =
∑
i,j
(−1)jqi dim Hsl(N ),R
i,j (K). (3.5)
Similarly, a categoriﬁcation ofP R(K;a,q ) is a triply-graded homology theory HR
i,j,k(K), with
gradings i, j and k, whose graded Euler characteristic is
P R(K;a,q ) =
∑
i,j,k
(−1)kaiqj dim HR
i,j,k(K). (3.6)
The relations (3.5) and (3.6) are represented by horizontal arrows in Figure 2. Sometimes,
it is convenient to express these relations as specializati ons of the corresponding Poincar´ e
polynomials P sl(N ),R(q,t ) and P R(a,q,t ) at t = −1. For example, the Poincar´ e polynomial
of the triply-graded homology theory HR
i,j,k(K) is deﬁned as follows
“superpolynomial” P R(K;a,q,t ) :=
∑
i,j,k
aiqjtk dim HR
i,j,k(K) (3.7)
and often is called the colored superpolynomial. To be more precise, just like below eq. (3.4) we
pointed out thatP R(a,q ) = P R(a,q,t = −1) is the normalized colored HOMFLY polynomial,
it is important to emphasize that P R(K;a,q,t ) is the Poincar´ e polynomial of the reduced
homology theory, in a sense that P R(
) = 1.
If one naively combines (3.5) and (3.6) one may be tempted to conclude that P sl(N ),R(q,t )
is a specialization of the superpolynomial at a =qN, as was stated e.g. in [26] and in some
other recent papers. We emphasize that, in general, this is not the case:
P R(a =qN,q,t ) ⁄= P sl(N ),R(q,t ) ≡
∑
i,j
qitj dim Hsl(N ),R
i,j (K). (3.8)
– 9 –
The reason is very simple and becomes crystal clear if one att empts to test (3.8) even in the
basic case of N = 1 and, say, R =□ . Indeed, the sl(1) theory is trivial in any approach to
knot polynomials / homologies. In other words, for any knot t hesl(1) homology Hsl(1),□
i,j (K)
is one-dimensional and the corresponding quantum group inv ariant J sl(1),□ (K;q) consists of
a single monomial.
This fact has a nice manifestation in the relation (3.4), whi ch says that almost all terms
in the HOMFLY polynomial P□ (a,q ) cancel out in the specialization a =q, leaving behind
a single term. This remarkable property of the HOMFLY polyno mial can be viewed as a
non-trivial constraint on the coeﬃcients of the polynomial P□ (a,q ). Since the coeﬃcients of
P□ (a,q ) can be positive and negative, this condition indeed can be satisﬁed if the total number
of “minuses” (counted with multiplicity) is balanced by the total number of “pluses.” This,
of course, can not work for (3.8) where the superpolynomial P□ (a,q,t ) has only positive
coeﬃcients, due to (3.7). Therefore, setting a = q will never reduce the total sum of the
coeﬃcients in this polynomial, and there is no way it can be equal to the Poincar´ e polynomial
P sl(1),R(q,t ) of a one-dimensional homology Hsl(1),R
i,j (K).
A more conceptual reason why (3.8) can not be true is that, whi le a specialization to
a = qN is perfectly acceptable at the polynomial level (the left si de of Figure 2), it has
to be replaced by a suitable operation from homological alge bra in order to make sense at
the higher categorical level (the right side of Figure 2). As explained in [27], the suitable
operation, which categoriﬁes the specializations a = qN, involves taking homology in the
triply-graded theory with respect to diﬀerentials dN, N ∈ Z. Indeed, the “extra terms” in
the superpolynomial P R(a,q,t ) that are not part of P sl(N ),R(q,t ) and otherwise would cancel
upon setting t = −1 always come in pairs, so that a more proper version of (3.8) r eads
P R(a,q,t ) = Rsl(N ),R(a,q,t ) + (1 +aαqβtγ)Qsl(N ),R(a,q,t ), (3.9)
whereRsl(N ),R(a,q,t ) andQsl(N ),R(a,q,t ) are polynomials with non-negative coeﬃcients, such
that the sl(N) homological invariant is a specialization of the “remaind er” (not the full
superpolynomial as in (3.8)):
Rsl(N ),R(a =qN,q,t ) = P sl(N ),R(q,t ), (3.10)
whereas the extra pairs of terms in (3.9) that come from Qsl(N ),R(a,q,t ) are killed by the
diﬀerentialdN of (a,q,t )-degree (α,β,γ ).
Now, once we introduced the cast of characters and explainedthe relations between them,
we can get straight down to business. We start in the next subs ection with the calculation
of colored superpolynomials for (2 , 2p + 1) torus. Then, in section 3.2 we use the results of
these calculations to derive and study the recursion relati ons, a.k.a. the quantum volume
conjecture (2.1a). Starting in section 3.2, we focus on the a =q2 specializations of Sr-colored
superpolynomial, which we denote as
Pn(q,t ) := P Sn−1
(a =q2,q,t ). (3.11)
– 10 –
In section 3.1.3 we present some evidence that in the reﬁned volume conjectures (2.1) and (2.6)
one can replace this deﬁnition of Pn(q,t ) with a true sl(2) homological knot invariant (2.2).
Finally, in section 3.3 we consider the classical limit and d iscuss the leading “volume” term
S0(u,t ) that dominates the asymptotic behavior (2.6a) of these hom ological knot invariants.
According to (2.7), this semi-classical limit is controlle d by the t-deformed algebraic curve,
Aref(x,y ;t) = 0, whose quantization will be revisited in section 3.4.
In a physical realization of knot homologies [28], the super polynomial P Sn−1
(a,q,t ) and
its specialization (3.11) are certain indices that count re ﬁned BPS invariants, essentially
identical to Z open
BPS (u,q,t ) where u =qn. Motivated by this, in the later section 4 we perform
a similar analysis of more general reﬁned open BPS partition functions and ﬁnd many similar
patterns.
