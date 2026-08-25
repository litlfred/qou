---
doc_id: 04procbryden
doc_title: "Some computations of Ohtsuki series"
section_id: sec-004-23-properties-of-ohtsuki-series
section_title: "Properties of Ohtsuki series"
section_number: 2.3
pages: 8-9
source_pdf: 04procbryden.pdf
source_sha256: 8baffbc6542c34a5
doc_brief: "Some computations of Ohtsuki series — We present some computational data on Ohtsuki series for a two pa- rameter family of integer homology spheres obtained by surgery around what we call ‘2–strand"
---
The Ohtsuki series ∑ ∞
m=0 λm(q − 1)m will depend on S and T (and U,
or equivalently on the sign of the surgery). To include this dependence
clearly in the notation, we will denote the coeﬃcients by λ±
m(S, T).
Theorem For ﬁxed parity and signs forS and T, λm is a polyno-
mial in S and T of degree 2m with rational coeﬃcients.
Proof. It is known that M −→λm(M) is a ﬁnite type invariant
of manifolds of order m. On the other hand, the map K −→ λm(S3
K)
(doing +1 surgery on the knot) gives a Vassiliev invariant of order 2m.
(This follows for example from the Melvin-Morton-Rozansky conjecture
(B-NG) and Le (Le).)
However if|S|+|T | > 2m, then let us pick any 2m+1 of the crossings
in the knot diagram ofK(( S
T )) in Figure 1, says of these crossings will be
from the ones that were counted byS and t from the crossings that were
counted by T, where s+t =2 m+1. One can consider the 22m+1 knots
obtained by variously altering the orientations of these crossings in all
possible ways. Since λm is Vassiliev of order 2m, the alternating sum
of the values of λm on these knots vanishes. When the orientation of a
crossing (say of typeS)i n K(( S
T )) is ﬂipped, the resulting knot is of the
same type, by withS changed toS −2signS. Without loss of generality,
S and T are positive. Then the result of changing the orientations of i
crossings of type S and j crossings of type T,i sK (( S−2i
T −2j )). There are
( s
i
)( t
j
)
ways in which to pick the subsets of crossings to ﬂip, so that
s∑
i=0
t∑
j=0
(−1)i+j
( s
i
)( t
j
)
λ±
m(S − 2i, T − 2j)=0 , (4)
for all S and T positive and all s, t with s + t =2 m + 1. The left
hand side of (4) is the order s + t ﬁnite diﬀerence partial derivative of
λ±
m, s times in the S direction and t times in the T direction. Observe
also that all the terms in (4) involve S and T of ﬁxed parities. This
condition is suﬃcient to guarantee that (for ﬁxed parities) λ±
m
(S, T)i s
expressible as a polynomial inS and T of order at most 2m, as required.
Since λm ∈ Z, these polynomials must have rational coeﬃcients, in fact
22m((2m)!!)2λm(S, T) ∈ Z[S, T] where n!! ≡ ∏ n
r=1 r!.
60
Some computations of Ohtsuki series
