---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mos"
section_id: sec-005-24-summary-of-jones-formulae
section_title: "Summary of Jones formulae"
section_number: 2.4
pages: 6-6
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
toc_source: outline
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
---
Summary of Jones formulae
Now we address to the case which is currently the only deﬁnite common point of the HOMFLY and Khovanov
cases. This is the case of Jones polynomial, which is obtained for A = q2 from the former and for t = −1
from the latter ones. Explicitly, the Jones polynomial of the satellites we consider has the form
JSK
Tork(q) = q−3k+1
−
1
1 + q2 + q2k−2 1 −q6
1 −q4 JK
adj(q)

,
JSK
Twk(q) =
q−4
1 + q4
1 + q2
−q−2k
1 −q6
1 + q2 JK
adj(q)

.
(11)
The antisymmetric Jones as well as the trivial Jones identically equals one. Both kinds of the satellite
polynomials are now expressed via the same coloured Jones, which is the descendent of both the adjoint
and symmetric HOMFLY and explicitly equals
JTorn
adj (q) = q−8n·
q2(q2 −1)
q6 −1
−
q2n
+
q10 −1
q2(q6 −1)q6n

,
JTwn
adj (q) =
(q18 −1)(q2 −1)
q12(q6 −1)2
+ q−12(1 + q6)(1 −q4)q−2n + (q10 −1)(q4 −1)(q2 −1)
q10(q6 −1)
q−6n
(12)
We present these expressions for the sake of reference. Namely, one can verify that (15,16) are reduced to
(11), and the polynomials (19) explicitly given in sec.4.3,4.4 are reduced to (12) for t = −1.
Disclaimer.
Note that n in (12) must be odd for torus knots and even for twist knots (see sec.B.1,B.2).
If one substitutes −q−2n with (−q2)−n in the torus formula, it yields the correct adjoint polynomials
both for torus knots with odd n and torus links with even n. The twist formula with (−q2)−n instead of
q−2n also gives a polynomial for any n, and these polynomials satisfy JTwn
adj (q) = q16JTw−n+1
adj
(q−1). I.e., the
formula still gives the true adjoint polynomials of the twist knots for even n, while the one with the odd
n now gives the polynomials of the mirror knots up to the extra factor of q16. This property seems to be
accidental and does not survive neither in HOMFLY, nor in Khovanov cases. In other words, there is no
“analytic” formula for twist knots with any integer n as the half-twist number (see sec.B.2).
