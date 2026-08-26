---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗ A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mo"
section_id: sec-010-4-explicit-form-of-the-pattern-and-companion-inv
section_title: "Explicit form of the pattern and companion invariants"
section_number: 4
pages: 8-9
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗ A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
---
Now we give an explicit form of the two basic ingredients in PPCD formulae from sec.3.2. First, we
describe the pattern invariant in sec.4.1. In fact, we recall the well known Khovanov polynomials of the two-
strand torus and twist knots, bringing the expressions to a proper form. In next sec.4.2,4.3,4.4, we present
the explicit expressions for the companion invariants extracted from PPCD. We call them an asymptotic
adjoint Khovanov (AAK) polynomials, since we believe them to be “tails” of the true adjoint Khovanov
polynomials that survive in the satellite polynomials. Although the exact relation of the two quantities is
not yet established, the AAK may be interesting in itself, as an explicitly deﬁned and readily computable
Khovanov-like knot invariant.
4.1 The pattern-deﬁning polynomial
By deﬁnition, the k in ourSTwk andSTork, as well as in (15,16,17) is a satellite invariant independent of the
companion knot. Hence k and thus the knot Twk or Tork deﬁnes the pattern of the satellite (see sec.2.3).
The ﬁrst term in the PPCD decomposition is just the respective Khovanov polynomial. Namely, the reduced
polynomial for the twist knot is
KhTwk = −(−t)Θk
(
q2t
)−k−2
·
(
1 +q2t·
(
1 +q4t2)(
1− (q2t)k−1)
1−q2t
)
(23)
= ( −t)Θk
(
q2t
)−k
·
(
1 +
(
q2t
)k−2
·
(
1 +q4t2)(
1− (q2t)−k)
1−q2t
)
=
= ( −t)Θk(q2t)−2
(
1 +q4t2
1−q2t− (q2t)−k 1 +q6t3
1−q2t
)
,
while the reduced polynomial for the torus knot is
KhTork = −(−t)Θkt−1qk−1
(
1 +
(
q2t
)2
· 1− (q2t)k−1
1−q2t
)
(24)
= ( −t)Θkqk+1
(
1 +
(
q2t
)k
· 1− (q2t)−k−1
1−q2t
)
=
= ( −t)Θkq(q3t)k
(
1
1−q2t− (q2t)−k−1 1 +q6t3
1−q4t2
)
,
8
and the unreduced polynomial for the torus knot is
uKhTork = qk·
{
1− (−t)Θk
(
1
q2t +q2t·
(
1 +q4t
)(
1− (q2t)k−1)
1−q4t2
)}
= (25)
= qk·
{
1 + (−t)Θk
(
q2 +
(
q2t
)k
·
(
1 +q4t
)(
1− (q2t)−k−1)
1−q4t2
)}
.
We give several equivalent expressions in all cases. The ﬁrst and the second expressions for each of the
polynomials are manifestly positive for n> 0, and n< 0, respectively. The third expression for each of the
reduced polynomials is useful to rewrite our PPCD formulae (16,15) like (4,5) and (11).
