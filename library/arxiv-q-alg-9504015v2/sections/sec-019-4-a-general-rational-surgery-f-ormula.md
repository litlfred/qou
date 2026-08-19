---
doc_id: arxiv-q-alg-9504015v2
doc_title: "Witten’s Invariants of Rational Homology Spheres at Prime"
section_id: sec-019-4-a-general-rational-surgery-f-ormula
section_title: "A General Rational Surgery F ormula"
section_number: 4
pages: 20-21
source_pdf: 9504015v2.pdf
source_sha256: ea5588225a393477
doc_brief: "Witten’s Invariants of Rational Homology Spheres at Prime — We establish a relation between the coeﬃcients of asymptotic expan sion of the trivial connection contribution to Witten’s invariant of"
---
Up until this point we were working only with surgeries of the type ( p, 1). This was enough
to prove the theorems of Section 1, because H. Murakami and T. O htsuki showed [6] that any
RHS M can be constructed by ( pj, 1) surgeries on an ASL in S3 up to a connected sum of
lens spaces Lp′
j,1, that is, instead of M one might end up with M#Lp′
1,1# . . . Lp′
n,1. However
from the technical point of view it would be better to have a formula f or the invariant
19
Z ′(M; k) of a manifold constructed by general rational surgeries ( pj, qj) on the components
of an N-component link L in S3.
The formula for Witten’s invariant Z(M; k) was derived by L. Jeﬀrey [10]
Z(M; k) = Z(S3; k) exp

iπ
4
K − 2
K


N∑
j=1
Φ( U (pj ,qj) − 3 sign (L)



 (4.1)
×
∑
1≤α1,...,αN ≤K−1
Jα1,...,αN (L; k)
N∏
j=1
˜U
(pj ,qj)
αj 1 ,
here L is the linking matrix of L, pj
qj
being the self-linking numbers. The matrices
U (pj ,qj) =


pj rj
qj sj

 ∈ SL(2, Z Z) (4.2)
describe the surgeries (a meridian on the tubular neighborhood is glu ed to pj(meridian) +
qj(parallel) of the link complement),
Φ


p r
q s

 = p + s
q − 12s(p, q), (4.3)
s(p, q) being the Dedekind sum, and
˜U (p,q)
αβ = i sign (q)√
2K|q|
e−i π
4 Φ( U (p,q ))
q−1∑
n=0
∑
µ=±1
µ
× exp
[
iπ
2Kq (pα2 − 2α(2Kn + µβ) + s(2Kn + µβ)2)
]
. (4.4)
Let us introduce some notations. A rational ( pj, qj) surgery on Lj can be presented as
a combination of ( m(j)
t , 1), 1 ≤ t ≤ ¯t(j) surgeries on a chain of unknots simply linked to Lj
(see e.g. [9], [10] and references therein) such that
U (pj ,qj) = T
m(j)
¯t(j) ST
m(j)
¯t(j)−1S · · · T m(j)
