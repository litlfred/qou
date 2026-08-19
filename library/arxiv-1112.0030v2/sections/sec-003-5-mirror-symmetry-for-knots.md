---
doc_id: arxiv-1112.0030v2
doc_title: "Homological algebra of knots and BPS states"
section_id: sec-003-5-mirror-symmetry-for-knots
section_title: "Mirror symmetry for knots"
section_number: 5
pages: 25-36
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
doc_brief: "Homological algebra of knots and BPS states — It is known that knot homologies admit a physical descriptio n as spaces of open BPS states. W e study operators and algebras acting on these spaces."
---
In this section, we observe a remarkable “mirror symmetry” relatio n (1.11)
between two completely diﬀerent triply-graded homology theories a ssociated with
symmetric and anti-symmetric representations of sl(N ), which will allow us to
formulate even a bigger theory that will contain both. As a ﬁrst ste p, however, we
need to extend the discussion in section 4 to the HOMFLY homology co lored by
anti-symmetric representations of sl(N ).
5.1. Anti-symmetric representations. Much as for the symmetric repre-
sentation Sr, we can repeat the analysis for the anti-symmetric representatio ns Λ r
of sl(N ).
In particular, for every positive integer r there exists a triply-graded homology
theoryHΛ r
(K), together with the collection of diﬀerentials {dΛ r
N}, N ∈ Z, such
that the homology with respect to dΛ r
N is isomorphic to Hsl(N ), Λ r
(K). Moreover, it
comes equipped with the collection of “universal” colored diﬀerentials , like in the
case of the symmetric representations. The homologies HΛ r
(K), together with all
the diﬀerentials, satisfy the same properties as HSr
(K) from Conjecture 4.2.
Again, we have two canceling diﬀerentials, this time dΛ r
−1 and dΛ r
r of ( a, q, t)-
degrees (−1,−1,−3) and (−1, r,−1), respectively. The origin of these diﬀerentials
is clear, and can be inferred either from deformations of B-model p otentials, as in
section 3, or from basic representation theory. For example, the fact the represen-
tation Λ r of sl(r) is trivial gives rise to a canceling diﬀerential dΛ r
r .
Another basic fact is Λ r∼
= Λ for g = sl(r + 1), which leads to the relation
(5.1) Hsl(r+1), Λ r
(K) ∼
= Hsl(r+1),
(K) .
For the triply-graded theory HΛ r
(K), this relation implies that the a = qr+1 spe-
cializations of the homologies ( HΛ r
(K), dΛ r
r+1) and (H (K), dr+1) should be iso-
morphic.
Like in the case of symmetric representations, all the required pro perties allow
computation of the anti-symmetric homology for various small knot s. Below, we
provide the details for the trefoil knot.
Using the isomorphism so(6)∼
= sl(4) under which the vector representation of
so(6) is identiﬁed with the anti-symmetric representation of sl(4), we conclude
(5.2) Hsl(4),
(K) ∼
= Hso(6),V (K)
From this relation 11 we immediately ﬁnd
(5.3) Hsl(4),
(31) = q4 + q6t2 + q7t2 + q8t3 + q9t3 + q10t4 + q11t5 + q12t5 + q13t6
Also, for g = sl(3) we have Λ 2∼
= Λ, which implies another useful relation
(5.4) Hsl(3),
(K) ∼
= Hsl(3),
(K)
For the trefoil, this gives:
(5.5) Hsl(3),
(31) = q2 + q4t2 + q6t3
11Here, in comparing the two homology theories we take into acc ount that q-gradings diﬀer
by a factor of 2.
26 SERGEI GUKOV AND MARKO STO ˇSI ´C
Combining this data with the colored HOMFLY polynomial
(5.6) P
(a, q) = a2(q−4 + q−2 + q−1 + q2)− a3(q−4 + q−3 + q−1 + 1) + a4q−3
we easily ﬁnd the anti-symmetric version of the superpolynomial for the trefoil knot:
(5.7)
P
(31) = a2(q−4 + q−2t2 + q−1t2 + q2t4)+ a3(q−4t3 + q−3t3 + q−1t5 + t5)+ a4q−3t6
2
3
4
a
q
40
−5 −4 −3 −2 −1 0 1 2
3 5 5
6
2 2
3
Figure 4. The reduced Λ 2-colored homology of the trefoil
The homology H (31) is shown on the Figure 4 below. It has the following
diﬀerentials:
• canceling diﬀerential d−1 of ( a, q, t)-degree (−1,−1,−3)
• canceling diﬀerential d2 of (a, q, t)-degree (−1, 2,−1) reﬂects the fact that
Λ 2 is trivial in sl(2) theory
• diﬀerential d3 of ( a, q, t)-degree (−1, 3,−1) reﬂects the fact that Λ 2∼
= Λ
in sl(3) theory and gives, cf. (5.5):
(5.8) a2q−4t0 + a2q−2t2 + a3q−3t3 a=q3
= Hsl(3),
(31)
• diﬀerential d0 of ( a, q, t)-degree (−1, 0,−3) gives:
(5.9) a2q−2t2 + a2q2t4 + a3q0t5 = at2P (31)(a, q2, t).
• universal diﬀerential d2→1 of ( a, q, t)-degree (0 , 1, 0) gives:
(5.10) a2q−4t0 + a2q2t4 + a4q−3t6 = P (a2, q4, q−1t2)
5.2. Mirror symmetry for knot homology . By computing the triply-graded
homologiesHSr
(K) andHΛ r
(K) for various small knots, we discover the following
remarkable symmetry between these two classes of theories, labe led by R = Sr and
R = Λ r:
(5.11) HΛ r
i,j, ∗(K)∼
=HSr
i,−j,∗(K).
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 27
Furthermore, this symmetry extends to the diﬀerentials as well. Mo re precisely, let
(5.12) φ :HSr
(K)→H Λ r
(K),
be the isomorphisms from (5.11). Then
(5.13) φ dSr
N = dΛ r
−N φ, N ∈ Z.
As the ﬁrst illustration of the mirror symmetry, let us compare the s econd
symmetric and anti-symmetric homology for the trefoil knot. From Figures 3 and
4 it is clear that “mirror symmetry” is manifest both for the homology (5.11) and
for the diﬀerentials (5.13). The explicit t-grading change in (5.11) in this case is
given by:
(5.14) H
i,j,k (31)∼
=H
i,−j, 4i−k−4(31)
for the trefoil knot.
The ﬁrst implication of the mirror symmetry is that one can combine HSr
(K)
andHΛ r
(K) into a single homology theory. By setting Hr(K) to be HSr
(K), we
obtain the Conjecture 1.1. More precisely, we conjecture the follo wing:
Conjecture 5.1. For every positive integer r there exists a triply-graded ho-
mology theoryHr
∗(K) =HSr
i,j,k (K), that comes with a family of diﬀerentials {dr
N},
with N∈ Z, and also with an additional collection of universal colored diﬀerentials
dr→m, for every 1 ≤ m < r , satisfying the following properties:
• Mirror Symmetry
Hr
i,j, ∗(K)∼
=HSr
i,j, ∗(K)∼
=HΛ r
i,−j,∗(K).
• Categoriﬁcation: Hr
∗ categoriﬁes P Sr
and P Λ r
:
χ(Hr
∗(K)) = P Sr
(K)(a, q) = P Λ r
(K)(a, q−1).
• Anticommutativity: The diﬀerentials {dSr
N} anticommute12:
dr
N dr
M =−dr
M dr
N .
• Finite support:
dim(Hr
∗) < +∞.
• Specializations: For N > 1, the homology of Hr
∗(K) with respect to dr
N is
isomorphic toHsl(N ),S r
(K):
(Hr
∗(K), dr
N )∼
=Hsl(N ),S r
(K).
For N≤− 2r, the homology ofHr
∗(K) with respect to dr
N is isomorphic toHsl(−N ), Λ r
(K):
(Hr
∗(K), dr
N )∼
=Hsl(−N ), Λ r
(K).
• Canceling diﬀerentials: The diﬀerentials dr
1 and dr
−r are canceling: the ho-
mology of Hr
∗(K) with respect to the diﬀerentials dr
1 and dr
−r is one-dimensional.
This reﬂects the fact that Sr representation of sl(1) and Λ r representation of sl(r)
are trivial.
12cf. comments following (2.11)
28 SERGEI GUKOV AND MARKO STO ˇSI ´C
• sl(N ) Colored diﬀerentials: For every 1≤ k≤ r− 1, the homology of Hr
∗(K)
with respect to the diﬀerential dr
−r−k is isomorphic to Hk(K):
(
Hr
∗(K), dr
−r−k
) ∼
=Hk(K), 1≤ k≤ r− 1,
reﬂecting the fact that Λ r∼
= Λ k for sl(r + k), where 1 ≤ k≤ r− 1.
• V ertical Colored diﬀerentials: The diﬀerentials dr
1−k, for 1≤ k≤ r− 1, have
a-degree−1, and the homology of Hr
∗(K) with respect to the diﬀerential dr
1−k is
isomorphic (after simple regrading that preserves a- and t-gradings), toHk
∗(K):
(
Hr
∗(K), dr
1−k
) ∼
=Hk(K), 1≤ k≤ r− 1.
• Universal Colored diﬀerentials: For any positive integer m, with m < r ,
the diﬀerentials dr→mhave a-degree zero, and the homology of Hr
∗(K) with respect
to the colored diﬀerential dr→m is isomorphic (after regrading) to Hm
∗ (K):
(Hr
∗(K), dr→m)∼
=Hm
∗ (K).
Example.H3 for the trefoil knot
As another example of the symmetry (5.11), and this time for degre e
higher than 2, let us considerH3(31). Besides the two canceling diﬀerentials
d3
1 and d3
−3, we also have the diﬀerential d3
−4 of degree (−1,−4,−3). The
homology with respect to this diﬀerential is equal to
(5.15) ( H3(31), d3
−4) = a3q7t4 + a3q9t6 + a4q8t7.
The explicit t-grading change in (5.11) for the trefoil and r = 3 is given by:
(5.16) H
i,j,k (31)∼
=H
i,−j, 4i−k−6(31).
With this change of gradings, the “mirror image” of (5.15) is equal to
a3q−9t0 +a3q−7t2 +a4q−8t3 which, according to the Conjecture 1.1, should
be equal to the homology (H
(31), d4 ). In particular, for a = q4 it implies
that the Poincar´ e polynomial of (H (31), d4 ) is equal to q3 + q5t2 + q8t3.
The latter, in turn, is equal toP (31)(a = q4, q, t) (see (A.1)), in agreement
with the isomorphism Λ 3∼
= Λ for sl(4).In Appendix C we computeH3 of the ﬁgure-eight knot and show that it satisﬁes
all of the properties from conjecture 5.1.
It is straightforward to check that the triply-graded colored HOM FLY homolo-
gies of other knots that we computed in Section 4 satisfy all the req uired properties
ofH2.
As for the t-grading change in (5.11) for an arbitrary knot, φ sends a generator
x of ( a, q, t)-degree ( i, j, k) to a generator of degree ( i,−j, 4i− k + 2rδ′(x)). Here
δ′(x) is a certain grading of the generator x, generalizing the δ-grading of the ordi-
nary HOMFLY homologyH . In the case of thin knots, δ′-grading of all generators
is equal to the S-invariant of knots.
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 29
Now, since the t-gradings of x and φ(x) have the same parity, by decategori-
fying (5.11) we get the following simple and beautiful relation between the colored
HOMFLY polynomials:
(5.17) P Sr
(K)(a, q) = P Λ r
(K)(a, q−1).
To the best of our knowledge, this relation has not been observed b efore. It gener-
alizes the symmetry q↔ q−1 of the (ordinary) HOMFLY polynomial.
Based on the above observations about the mirror symmetry for s ymmetric
and anti-symmetric representations, we speculate that this symm etry extends to
arbitrary representations: for a representation R of sl(N ) that corresponds to a
partition λ, we conjecture:
(5.18) Hλ (K)∼
=Hλ t
(K) ,
where λt is the dual (transpose) partition of λ. Here, we also tacitly assume that for
every partition λ there exists a triply-graded homology theory Hλ (K) categorifying
the λ-colored HOMFLY polynomial.
Furthermore, decategorifying the isomorphism (5.18) we obtain th e following
symmetry of the colored HOMFLY polynomials (see appendix A for con ventions):
(5.19) P λ (K)(a, q) = P λ t
(K)(a, q−1) .
5.3. Physical interpretation. The only evidence for the mirror symmetry
(5.18) and for its polynomial version (5.19) comes from the physical interpretation
of knot homologies / polynomials in terms of BPS invariants. Indeed, t he symmetry
(5.19) of the reduced colored HOMFLY polynomial is a direct consequ ence of the
corresponding symmetry for the unreduced colored HOMFLY polyn omial:
(5.20)
P
λ t
(K)(a, q) = ( −1)|λ| P
λ
(K)(a, q−1) ,
where|λ| is the total number of boxes in the partition λ. This symmetry, in turn,
follows13 from the explicit form of the colored HOMFLY polynomial [ 15]:
(5.21) P
λ
(K)(a, q) =
∑
i,j
aiqj
q− q−1 N λ
i,j (K)
written in terms of the ordinary (that is, unreﬁned) BPS invariants N λ
i,j (K) and
from the property of the integer BPS invariants [ 26, eq. (2.17)]:
(5.22) N λ t
i,j (K) = ( −1)|λ|+1 N λ
i,−j(K) .
Indeed, when combined, (5.21) and (5.22) imply that under q↔ q−1 the unreduced
colored HOMFLY polynomial of every knot has parity (−1)|λ|. In particular, this is
true for the unknot. Hence, the normalized colored HOMFLY polyno mial, deﬁned
as the ratio of P
λ
(K) and P
λ
( ), enjoys the symmetry (5.19).
There is a reﬁned / homological version of (5.20) and (5.22) that lead s to (5.18).
Much as the colored HOMFLY polynomial can be written in terms of the unreﬁned
13Another way to derive (5.20) is to use the properties of the Cl ebsch-Gordon coeﬃcients for
the symmetric group Cλµ tν t = Cλµν and the characters Sλ t (q) = ( − 1)|λ |− 1Sλ (q− 1) in eq.(2.6) of
[61], which describes the geometric origin of the q-dependence in the colored HOMFLY polynomail.
30 SERGEI GUKOV AND MARKO STO ˇSI ´C
BPS invariants N λ
i,j (K), the unnormalized superpolynomial of every knot K can
be expressed in terms of the reﬁned integer BPS invariants [ 4]:
(5.23) P
λ
(K)(a, q, t) =
∑
i,j,k
aiqjtk
q− q−1 Dλ
i,j,k (K) .
The reﬁned BPS invariants Dλ
i,j,k (K) enjoy a symmetry that generalizes (5.22),
(5.24) Dλ t
i,j, ∗(K) = Dλ
i,−j,∗(K) ,
and follows from the CPT symmetry of the ﬁve-brane theory in (1.4) or (1.6). The
normalized / reduced version of the symmetry (5.24) is precisely (5.1 8).
Further details and interpretation of the mirror symmetry (5.18) f or the triply-
graded knot homology will appear elsewhere.
6. Unreduced colored HOMFL Y homology
Here we compute the unreduced colored superpolynomial and the c olored HOM-
FLY polynomial of the unknot and the Hopf link by using the reﬁned to pological
vertex approach from [ 9]. The formulas obtained there are partition functions, pre-
sented in the form of the quotient of two inﬁnite series. Below we ﬁnd the explicit
closed form expressions for the unreduced Sr-colored HOMFLY homology of the
unknot and the Hopf link. More precisely, we evaluate eq. (67) of [ 9], according
to which the unreduced superpolynomial (= the Poincar´ e polynomia l of the unre-
duced triply-graded colored homology) of the Hopf link with compone nts colored
by partitions λ and µ is given by:
(6.1) P
λµ
(Hopf) = (−1)|λ|+|µ|
( q1
q2
) |λ||µ| (
Q−1
√ q1
q2
) |λ |+|µ |
2
× Zλµ
Z∅∅
,
where
Zλµ =
∑
ν
(−Q)|ν|q
||ν ||
2
2 q
||ν t ||
2
1 ~Zν (q1, q2) ~Zν t(q2, q1)sλ (q−ρ
2 q−ν t
1 )sµ (q−ρ
2 q−ν t
1 ) .
The unreduced superpolynomial of the unknot colored by λ is obtained by setting
µ =∅ in (6.1).
The change of variables from topological strings variables ( Q, q1, q2) to knot
theory variables ( a, q, t) used in this paper is given by:
√q2 = q,(6.2)
√q1 = −tq,
Q = −ta−2.
In particular, the specialization q1 = q2 corresponds to the specialization t =−1 in
the homological knot invariants.
By expanding the product of the Schur functions as
sλ sµ =
∑
ϕ
cϕ
λ,µ sϕ ,
where cϕ
λ,µ is the Littlewood-Richardson coeﬃcient, we obtain:
Zλµ =
∑
ϕ
cϕ
λ,µ
∑
ν
(−Q)|ν|q
||ν ||
2
2 q
||ν t||
2
1 ~Zν (q1, q2) ~Zν t (q2, q1)sϕ (q−ρ
2 q−ν t
1 ) =
∑
ϕ
cϕ
λ,µ Zϕ .
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 31
Replacing this in (6.1) gives
P
λµ
(Hopf) = ( −1)|λ|+|µ|
( q1
q2
) |λ||µ| (
Q−1
√ q1
q2
) |λ |+|µ |
2
× Zλµ
Z∅∅
=
= ( −1)|λ|+|µ|
( q1
q2
) |λ||µ| (
Q−1
√ q1
q2
) |λ |+|µ |
2 ∑
ϕ
cϕ
λ,µ
Zϕ
Z∅∅
=
=
( q1
q2
) |λ||µ| ∑
ϕ
cϕ
λ,µ (−1)|ϕ|
(
Q−1
√
q1
q2
) |ϕ |
2 Zϕ
Z∅∅
=
=
( q1
q2
) |λ||µ| ∑
ϕ
cϕ
λ,µ
P
ϕ
( ) .
Equivalently, in the knot theory variables ( a, q, t) we found the following simple
formula for the superpolynomial of the Hopf link expressed in terms of that of the
unknot:
(6.3)
P
λµ
(Hopf) = t2|λ||µ| ∑
ϕ
cϕ
λ,µ
P
ϕ
( ) .
Thus, in order to compute the unreduced superpolynomial of the H opf link, it
suﬃces to compute the superpolynomial of the unknot from (6.1).
6.1. Unreduced colored HOMFL YPT polynomial and homology of
the unknot. Below we give the results for the unknot derived from (6.1). The
notations and computations are summarized in Appendix D.
The quantum sl(N ) invariant (that is, a = qN specialization of the colored
HOMFLY polynomial) is given by:
P
λ
( )(a = qN , q) = q−2 ∑
x∈λ c(x)
[ N
λt
]
=
= q−2(n(λ t)−n(λ ))
[ N
λt
]
= q−κ (λ )
[ N
λt
]
.
In particular, for the r-th symmetric representation Sr we ﬁnd
(6.4) P
Sr
( )(a = qN , q) = q−r(r−1)
[
N + r− 1
r
]
,
whereas for the anti-symmetric representation R = Λ r we have
(6.5) P
Λ r
( )(a = qN , q) = qr(r−1)
[ N
r
]
.
The two-variable polynomial P
λ
( )(a, q) can be obtained from the above
expressions by replacing qN with a and the q-binomial coeﬃcients by two-variable
polynomials in the following way:
(6.6)[ N
r− j
]
↔ (−1)r−jar−jqr−j
(1− q2)(1− q4) . . . (1− q2r)
r∑
l=0
(−1)la−2lql(r−j−1)
[ r− j
l
]
(1− q2(r−j+1))··· (1− q2r) ,
32 SERGEI GUKOV AND MARKO STO ˇSI ´C
where the left hand side is the a = qN specialization of the right hand side. This
last formula follows from
n−1∏
i=0
(1 + q2iz) =
n∑
j=0
qj(n−1)
[
n
j
]
zj .
In particular, for the symmetric representation we have:
(6.7)
P
Sr
( )(a, q) = (−1)rarqr
(1− q2)(1− q4) . . . (1− q2r) q−2r(r−1)
r∑
l=0
(−1)la−2lql(r−1)
[ r
l
]
q2(r−l)(r−1).
Now, the formula for the a = qN specialization of the Sr-colored superpolyno-
mial for the unknot is obtained by using the following quantum binomial coeﬃcients
formula:
(6.8)
[ N + r− 1
r
]
= qr(r−1)
r−1∑
j=0
q−j(N +r−1)
[ r− 1
j
] [ N
r− j
]
.
Then, the Poincar´ e polynomial of the Sr-colored sl(N ) homology of the unknot is
obtained by adding a factor t−2j in every summand in the above expression for the
quantum binomial coeﬃcient in (6.4):
P
sl(N ),S r
( )(q, t) = P
Sr
( )(a = qN , q, t) =(6.9)
=
r−1∑
j=0
q−j(N +r−1)
[
r− 1
j
] [
N
r− j
]
t−2j .
Note that the corresponding homology H
sl(N ),S r
( ) is ﬁnite-dimensional.
We list some particular instances of (6.9) for small r:
P
sl(N ),S 1
( ) = [ N ] ,(6.10)
P
sl(N ),S 2
( ) =
[
N
2
]
+ q−(N +1)[N ]t−2 ,(6.11)
P
sl(N ),S 3
( ) =
[ N
3
]
+ q−(N +2)[2]
[ N
2
]
t−2 + q−2(N +2)[N ]t−4 .(6.12)
Specifying further the value of N , one ﬁnds the following expressions:
P
sl(2),S 2
( ) = 1 + q−2t−2 + q−4t−2,
P
sl(3),S 2
( ) = q2 + 1 + q−2 + q−2t−2 + q−4t−2 + q−6t−2,
P
sl(3),S 3
( ) = 1 + q−2t−2 + 2q−4t−2 + 2q−6t−2 + q−8t−2 + q−8t−4 + q−10t−4 + q−12t−4,
P
sl(4),S 2
( ) = q4 + q2 + 2 + q−2 + q−4 + q−2t−2 + q−4t−2 + q−6t−2 + q−8t−2.
The expression for the whole triply-graded superpolynomial is obta ined from (6.9)
by using (6.6).
In the case of anti-symmetric representations, the entire homolo gy of the unknot
is concentrated in the homological degree zero, and thus the Λ r superpolynomial
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 33
of the unknot coincides with its Λ r-colored HOMFLY polynomial:
(6.13) P
sl(N ), Λ r
( ) = qr(r−1)
[
N
r
]
.
6.2. Comparison with other approaches. Much of the present paper is
devoted to exploring the structure — motivated from physics — of t he colored
knot homology, namely its reduced version. A combinatorial or grou p theoretic
deﬁnition of such theory is still waiting to be discovered. However, in the case of
the unreduced theory, which we sketched in this section, there ha ve been several
attempts to deﬁne the colored knot homology, especially in low rank. Therefore,
we conclude this section with a brief comparison to other approache s.
Unfortunately, the structure of the colored diﬀerentials become s more obscure
(alternatively, more interesting!) in the unreduced version of the c olored knot
homology.14 This, in part, is the reason why we kept our discussion here very
brief, relegating a more thorough analysis to future work. Anothe r reason, which
will become clear in a moment, is that even a quick look at the unknot ex poses
a number of questions that need to be understood in order to relat e and unify
diﬀerent formulations:
• singularities in moduli spaces (of BPS conﬁgurations): dim HBPS <∞
versus dimHBPS =∞
• framing dependence in the colored knot homology
• colored homological invariants versus cabling
• analog of wall crossing phenomena in mathematical formulations of c ol-
ored knot homologies
• the role of the “preferred direction” in the combinatorial formulat ion based
on 3d partitions
• proper interpretation of formal expressions, or
(6.14) 1− q2
1− q2 = (1− q2)(1 + q2 + q4 + q6 + . . .) versus 1− q2
1− q2 = 1
In addition, each formulation typically involves individual choices and s ubtleties,
which may also aﬀect the form of the answer. In fact, even the tot al dimension of
the colored homology may depend on some (or, perhaps, all) of thes e choices. 15
While good understanding of these aspects is still lacking, many appr oaches to
colored knot homology seem to agree on one general feature: the unreduced sl(N )
homology has ﬁnite support only for certain suﬃciently small repres entations. For
example, in [ 9, eq. (67)] this corresponds to the fact that for general repre sentations
there is no way to clear the denominators. This should be compared w ith the
fundamental representation of sl(N ), where every existent approach leads to a
homology with ﬁnite support. The simplest example that belongs to th e “grey
territory” is the second symmetric representation R = S2 of sl(N ). For N = 2,
this corresponds to the adjoint representation of sl(2) and, as we saw in (3.11),
physics realizations [ 4, 12 ] lead to a 3-dimensional knot homology H
sl(2),
( )
14This is familiar from the ordinary, non-colored knot homolo gy [ 3, 6 ].
15W e hope that at least some of these delicate aspects are washe d away when one passes to
the reduced theory, as it happens in the non-colored case. Th is is one of the reasons why in the
present paper we mainly consider the reduced homology.
34 SERGEI GUKOV AND MARKO STO ˇSI ´C
categorifying the colored Jones polynomial of the unknot,
(6.15)
P 2 ( ) = [3] = q−2 + 1 + q2 .
On the other hand, some mathematical formulations lead to a theor y with inﬁnite
support (which can be attributed to several gaps in the present u nderstanding and
the above-listed questions). For example, ﬁxing 16 a typo in [ 62, Proposition 3.4],
one ﬁnds the following candidate for the Poincar´ e polynomial of the colored unknot
homology:
(6.16)
P 2 ( ) = q−2t2 + 1 + q2t−2 + q−2 + q−2t
1− t2q−4 .
The structure of the corresponding homology theory is clear: the ﬁrst three terms
reproduce (upon specializing to t =−1) the colored Jones polynomial (6.15) and
the quotient in the last term corresponds to the inﬁnite-dimensiona l contribution
to the homology, all of which disappears upon taking the Euler chara cteristic.
Similar structure emerges in other frameworks, in particular in appr oaches
based on categoriﬁcation of the Jones-Wenzl projectors. The J ones-Wenzl projec-
tors appear in decomposing the ﬁnite dimensional representations of the quantum
group Uq(sl2) and, as such, play a key role in the deﬁnition and computation of
quantum group invariants of knots and 3-manifolds. Several ways to categorify the
Jones-Wenzl projectors have been proposed in the literature, e.g. the topological
categoriﬁcation [ 63] and the Lie theoretic categoriﬁcation [ 64] which agree (up to
Koszul duality). In particular, the latter approach leads to a theo ry that categori-
ﬁes (6.15) by replacing the middle term with inﬁnite-dimensional homolo gy whose
Poincar´ e polynomial equals
(6.17)
P 2 ( ) = q−2 + 1
[2][2] (q + q−1)2 + q2 ,
where [2] = q + q−1 and the authors of [ 64] instruct us to interpret 1
[2] as a power
series q−q3+q5−q7+. . .. This power series is familiar to physicists as a trace (“par-
tition function”) over the inﬁnite-dimensional Hilbert space HBose = H∗(CP∞) =
C[x] of a harmonic oscillator / single boson,
(6.18) PBose = 1
1− q2 = 1 + q2 + q4 + q6 + . . . .
Partition function of a single fermion has a similar form, except that f ermions
contribute to the numerator instead of the denominator. Indeed , the trace over a
two-dimensional Hilbert space of a single fermion looks like
(6.19) PFermi = 1 − q2 ,
in agreement with a well-known fact that contributions of bosons an d fermions
cancel each other, cf. (6.14). Therefore, instead of canceling the ratio in the middle
term of (6.17), the authors of [ 64] instruct us to interpret it as a Hilbert space of two
bosons and two fermions. Note, due to the presence of bosonic st ates this Hilbert
space is inﬁnite-dimensional, as opposed to a much smaller, ﬁnite-dime nsional space
that one might infer by simplifying the ratio. Similarly, (6.16) contains o ne boson
(due to the factor 1
1−t2q−4 in the last term), etc.
16W e thank E. Gorsky for pointing this out.
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES 35
If this, however, is the proper interpretation of (6.17), then one immediately
runs into a general question of how to interpret formal expressio ns like (6.14) and
when to clear denominators. The answer to this question will certain ly aﬀect many
calculations of Poincar´ e polynomials, in particular calculations based on [ 9, eq.
(67)] that has non-trivial numerators and denominators, as well as similar calcula-
tions in other frameworks.
A novel physical framework that appears to be closely related to k not homology
is the so-called “reﬁned Chern-Simons theory.” Although Lagrangia n deﬁnition of
this theory is not known at present, its partition function was conj ectured [ 58]
to compute topological invariants of knots and 3-manifolds that pr eserve an extra
rotation symmetry. This includes torus knots and Seifert 3-manifo lds. The rotation
symmetry gives rise to an extra quantum number, so that for toru s knots and
Seifert 3-manifolds the reﬁned Chern-Simons theory leads to a str iking prediction:
the space (1.2) is quadruply-graded rather than triply-graded in t hese cases.
In simple examples, the fourth grading (coming from the extra rota tion sym-
metry of a 3-manifold) is determined by the other three gradings (2 .3). It would be
interesting to study under which conditions this happens; when it do es, the partition
function of the SU (N ) reﬁned Chern-Simons theory computes the specialization of
the superpolynomial to a = qN . Assuming this is the case for the unknot colored
by the second symmetric representation, the SU (2) reﬁned Chern-Simons theory
gives:
(6.20)
P 2 ( ) = − (q2t + q−2)
(q− q−1)
(q4t2 + q−2t−1)
(q3t2− q−1) .
The corresponding Hilbert space contains at least two “bosons” (d ue to two factors
in the denominator of (6.20)) and, therefore, leads to a version of colored homology
with inﬁnite support.
In our quick tour through diﬀerent ways of categorifying the color ed Jones
polynomial of the unknot (6.15) we saw theories with ﬁnite support a s well as
theories with inﬁnite support, in fact, of diﬀerent kind (with diﬀeren t number of
“bosons” / factors in the denominator). One would hope that all th ese theories
correspond to diﬀerent choices (of framing, chamber, regulariza tion, ... ) and with
a proper understanding of the above-mentioned issues could be un iﬁed in a single
framework. One piece of evidence that it might be possible comes fro m the fact
that all physical and geometrical approaches agree when the cor responding moduli
spaces are non-singular, as e.g. for minuscule representations. Therefore, we hope
to see a much bigger story, only small elements of which have been re vealed so far.
Acknowledgments We would like to thank S. Cautis, M. Marino, K. Schaeﬀer,
Y. Soibelman, C. Stroppel, C. Vafa, J. Walcher, and E. Witten for va luable discus-
sions. The work of SG is supported in part by DOE Grant DE-FG03-92 -ER40701
and in part by NSF Grant PHY-0757647. Opinions and conclusions exp ressed here
are those of the authors and do not necessarily reﬂect the views o f funding agencies.
MS was partially supported by the Funda¸ c˜ ao para a Ciˆ encia e Tecnologia (ISR/IST
plurianual funding) through the programme Programa Operaciona l Ciˆ encia, Tec-
nologia, Inova¸ c˜ ao (POCTI) and the POS Conhecimento programm e, co-ﬁnanced
by the European Community fund FEDER. MS was also partially suppor ted by
the Ministry of Science of Serbia, project no. 174012.
36 SERGEI GUKOV AND MARKO STO ˇSI ´C
