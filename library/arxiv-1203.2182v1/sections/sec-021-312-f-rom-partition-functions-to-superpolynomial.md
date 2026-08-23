---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-021-312-f-rom-partition-functions-to-superpolynomial
section_title: "F rom partition functions to superpolynomials"
section_number: 3.1.2
pages: 21-23
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
As we already explained around (3.7), the reduced colored su perpolynomial P R(K;a,q,t ) is
deﬁned as the Poincar´ e polynomial of the triply graded homology HR
i,j,k(K) that categoriﬁes
the colored HOMFLY polynomial P R(K;a,q ). Here, the word “reduced” means that the
normalization is such that P R(
) = 1. Although normalization is one of the delicate points
one has to worry about, luckily it will not be a major issue for us here.
Besides normalization, there are several other choices tha t aﬀect the explicit form of the
answer and, therefore, need to be explained, especially for comparison with other approaches.
Thus, earlier we already mentioned a very important choice o f framing. Another important
choice is a choice of grading conventions. In order to unders tand its important role, let us
recall that the triply-graded homology HR
i,j,k(K) is related to the doubly-graded sl(N) theory
Hsl(N ),R
i,j (K) by means of the diﬀerentials dN, illustrated in Figure 2:
Hsl(N ),R
∗,∗ (K) ∼
=
(
HR
∗,∗,∗(K),d N
)
. (3.53)
Taking the Poincar´ e polynomials on both sides gives (3.9)–(3.10).
– 20 –
In order to be consistent with the specialization a =qN (also illustrated on the left side
of Figure 2), the q-degree of dN should be N times greater than its a-degree and of opposite
sign. The standard convention for the homologicalt-grading of all diﬀerentialsdN withN >0
is −1. Modulo trivial 3 rescalings, such asa ↦→a2 andq ↦→q2, there are two sets of conventions
consistent with these rules used in the literature:
(a, q, t) grading conventions:
diﬀerentials conventions of [27, 43, 26, 46] conventions of [44]
dN >0 (−2, 2N, −1) (−1,N, −1)
dN <0 (−2, 2N, 2N − 1) (−1,N, −3)
dcolored (0, 2, 2) (0, 1, 0)
(−2, 0, −3) (−1, 0, −1)
.
.
.
(3.54)
Here, we mostly follow the latter conventions and occasiona lly, for comparison, state the
results in the former conventions.
Another choice of grading conventions comes from a somewhat surprising direction. A
special feature of the colored knot homology is the mirror symmetry conjectured in [44]:
HR
i,j,∗(K) ≃ H Rt
i,−j,∗(K). (3.55)
It relates triply-graded HOMFLY homologies colored by repr esentations (Young diagrams)
R and Rt related by transposition. Although this nice property is al so present even in the
basic uncolored case of R = Rt =□ as a generalization of the q ↔ q−1 symmetry [27],
its signiﬁcance is fully revealed in the colored theory with R ⁄= Rt. In particular, for our
applications it means that the triply-graded homologies HSr
(K) and HΛ r
(K) are essentially
the same, and so are the colored superpolynomials P Sr
and P Λ r
.
Put diﬀerently, the mirror symmetry (3.55) implies that inst ead of two diﬀerent triply-
graded homology theories HSr
(K) and HΛ r
(K) one really has only one theory,Hr(K), labeled
byr, such that passing fromR =Sr toR = Λr is achieved by ﬂipping the sign of theq-grading
accompanied by a suitable t-regrading. On the other hand, according to (3.53) the sign o f
the q-grading is correlated with the sign of N in the specialization to sl(N) doubly-graded
homology. Therefore, Hr(K) is related to the sl(N) colored knot homology via
(Hr(K),d N) =
{
Hsl(N ),Sr
(K), N > 0
Hsl(−N ),Λ r
(K), N < 0
(3.56)
or
(Hr(K),d N ) =
{
Hsl(N ),Λ r
(K), N > 0
Hsl(−N ),Sr
(K), N < 0
(3.57)
3Such rescalings are much more elementary choices of notatio n, rather than interesting choices of grading
convention that aﬀect the explicit form of the results in a mo re delicate way. A typical example of such harmless
rescaling is a doubling of all a- and q-gradings in the last column of (3.54) that gives deg( dN >0) = ( −2,2N,−1),
as in the middle column, deg( dN <0) = ( −2,2N,−3), etc.
– 21 –
The choice between (3.56) and (3.57) is a matter of convention. But it is an important choice
since it certainly aﬀects the form of Hr(K) and the corresponding superpolynomial (3.7).
To summarize, it seems that in our class of examples we have to deal with at least two
choices, between grading conventions in (3.54) and between (3.56) and (3.57). A nice surprise
is that these two choices are actually related [44]: switchi ng from (3.56) to (3.57) has the
same eﬀect as switching from one set of grading conventions in (3.54) to another. In other
words, to quickly go from one set of grading conventions in (3 .54) to another one can simply
exchange the role of symmetric and anti-symmetric represen tations or, equivalently, switch
the Young tableaux R and its transposed Rt. We shall use this trick in what follows, where
our default grading conventions will be that of [44] and (3.5 6).
Keeping in mind the relations between diﬀerent convention ch oices, now we are ready to
convert (3.49) and (3.50) into the colored superpolynomials P R(T 2,2p+1;a,q,t ) for symmetric
and anti-symmetric representations. Starting with the sym metric representationsR =Sr, we
can use the following change of variables
a = A
(q1
q2
) 3/2
,
q = 1
q2
, (3.58)
t = −
√ q2
q1
,
