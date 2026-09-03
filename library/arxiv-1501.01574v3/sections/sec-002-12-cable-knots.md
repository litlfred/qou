---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-002-12-cable-knots
section_title: "Cable knots"
section_number: 1.2
pages: 2-4
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polyn omial and the boundary slopes of knots under the operation of cabling."
---
The (p, q)-cable Kp,q of K is the 0-framed satellite of K with pattern ( p, q)-torus knot (see
Section 2 for more details). In the statements of results bel ow, and throughout the paper,
we will assume that our cables are non-trivial in the sense th at |q| > 1.
Theorem 1.2. For every knot K ⊂ S3 and (p, q) coprime integers we have
(
q2bsK ∪ {pq}
)
⊂ bsKp,q.
To continue, we recall that for any knot K ⊂ S3 the degrees d+[JK (n)] and d−[JK (n)]
are quadratic quasi-polynomials in n [9]. This implies that their coeﬃcients are periodic
functions N → Q. The common period of d+[JK (n)] and d−[JK (n)] is called the period of
K, denoted by π(K).
In this paper we are concerned with the Jones slopes for knots with π(K) ≤ 2 and
for knots where the leading coeﬃcient of d+[JK (n)] becomes constant for n large enough.
We show that the Jones slopes of these knots behave similarly to boundary slopes under
cabling operations (Propositions 3.2 and 4.4). In particul ar, for knots with period at most
two, combining our results about Jones slopes with Theorem 1 .2 we obtain the following.
Theorem 1.3. Let K be a knot such that, for n ≫ 0,
d+[JK (n)] = a(n)n2 + b(n)n + d(n) and d−[JK (n)] = a∗(n)n2 + b∗(n)n + d∗(n)
are quadratic quasi-polynomials of period ≤ 2, with b(n) ≤ 0 and b∗(n) ≥ 0. Suppose
p
q /∈ jsK. Then, we have
jsKp,q ⊂
(
q2jsK ∪ {pq/4}
)
and js∗
Kp,q ⊂
(
q2js∗
K ∪ {pq/4}
)
.
Furthermore, if (jsK ∪ js∗
K ) ⊂ bsK we have (jsKp,q ∪ js∗
Kp,q) ⊂ bsKp,q.
3
The proof of Theorem 1.3 reveals that the properties that b(n) ≤ 0 and b∗(n) ≥ 0 are
preserved under cabling. We conjecture that these properti es hold for all knots, and that
b(n) and b∗(n) detect the presence of essential annuli in the knot complem ent. This is
stated in Conjecture 5.1, which we have veriﬁed for all the kn ots for which the degrees
d+[JK (n)] and d−[JK (n)] are known.
Note that since we take |q| > 1, the hypothesis that p/q is not a Jones slope of K
will automatically be satisﬁed for knots that have all of the ir Jones slopes integers. A
large class of knots with integer Jones slopes is the class of adequate knots, which includes
alternating knots, Montesinos knots of length at least four , pretzel knots with at least four
strings and Conway sums of strongly alternating tangles. Th e class of semi-adequate knots
(knots that are A– or B–adequate) is much broader including all but a handful of pri me
knots up to 12 crossings, all Montesinos and pretzel knots, p ositive knots, torus knots,
and closed 3-braids. The reader is referred to Section 3 belo w for the precise deﬁnition
(Deﬁnition 3.5) and to [6, 5, 8, 12] and references therein fo r more details and examples
of semi-adequate knots.
Theorem 1.4. Let K be a knot and let K ′ be an iterated cable knot of K.
(1) If K is a B-adequate knot, then jsK ′ ⊂ bsK ′.
(2) If K is an A-adequate knot, then js∗
K ′ ⊂ bsK ′.
Hence, if K is an adequate knot then K ′ satisﬁes the Slope Conjecture.
An iterated torus knot is an iterated cable of the trivial kno t. As a corollary of Theorem
1.4 we have the following.
Corollary 1.5. Iterated torus knots satisfy the Slope Conjecture.
Theorem 1.3 also applies to several non-alternating prime k nots with up to nine crossings
(see Corollary 3.10). We should mention that Motegi-Takata [26] used Theorem 1.3 to
generalize Corollary 1.5 to all knots of zero Gromov norm (gr aph knots).
The proofs of Theorems 1.2 and 1.3 reveal that there is a remar kable similarity in the
behaviors, under cabling, of the linear terms of d+[JK (n)] and d−[JK (n)] and the Euler
characteristic of the essential surfaces “selected” by the Slope Conjecture. We conjecture
that the cluster points of the sets {2bK (n)} and {2b∗
K (n)} contain information about
the topology of essential surfaces that satisfy the Slope Co njecture for K. To state the
conjecture, let ℓd+[JK (n)] denote the linear term of d+[JK (n)] and let
jxK :=
{
2n−1ℓd+[JK (n)]
} ′
= {2bK (n)}′.
Conjecture 1.6 (Strong Slope Conjecture) . Let K be a knot and a/b ∈ jsK, with b > 0
and gcd(a, b) = 1 , a Jones slope of K. Then there is an essential surface S ⊂ MK, with
|∂S | boundary components, and such that each component of ∂S has slope a/b and
χ(S)
|∂S |b ∈ jxK .
Conjecture 1.6 implies a similar statement for {2b∗
K (n)}′ since it is know that d−[JK (n)] =
d+[J ∗
K (n)], where K ∗ denotes the mirror image of K. An immediate corollary of Theorem
3.9 is the following:
4
Corollary 1.7. Iterated cables of adequate knots satisfy the Strong Slope Con jecture. In
particular, iterated torus knots satisfy the Strong Slope Co njecture.
We also prove Conjecture 1.6 for pretzel knots of type ( −2, 3, p) and all Montesinos
knots with up to nine crossings (see Section 5).
