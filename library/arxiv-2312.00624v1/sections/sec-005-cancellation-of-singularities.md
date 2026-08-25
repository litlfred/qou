---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-005-cancellation-of-singularities
section_title: "Cancellation of singularities"
section_number: null
pages: 12-14
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
Again, we hide the explicit dependence on the classical solution α to simplify the notation. Here
and in the rest of this work, we will only re-introduce it when necessary. Recall that the exact wave
function χ(u; ℏ) is well-defined for ℏ> 0. In particular, it is well-defined for
ℏ = 2πP
Q, (3.15)
where P,Q are coprime positive integers. We will refer to values of ℏ of the form in Eq. (3.15)
as rational values . On the other hand, due to the conjectured integrality structure in Eq. (3.6),
ϕWKB(X;q) is singular for these values of ℏ precisely, thus implying that the singularities have to
cancel in the sum
ϕWKB(X;q) +ϕWKB(XD;qD), (3.16)
which appears in the formula for χ(u; ℏ) in Eq. (3.13). This leads to non-trivial constraints on the
coefficients ˆa±n(q) in Eq. (3.3). This type of cancellation of singularities played a major role in the
understanding of the ABJM matrix model [15] and the TS/ST correspondence [6, 8, 39].
We will now study how this cancellation occurs in the exact wave function χ(u; ℏ) as given
in Eq. (3.13), and, in Section 3.3, we will compute the finite, well-defined piece which is left from
the cancellation and constitutes the sum in Eq. (3.16). Moreover, as we will see following [12] in
Section 3.4, it is possible to compute this finite part by using only the information contained in the
quantum operator ˆA( ˆP, ˆX,q ). We take
q = eiℏ = e2πiP
Q, P,Q ∈ Z>0 coprime, (3.17)
and, substituting into Eq. (3.2), we find that the possible singularities ofϕWKB(X;q) occur ina±n(q)
whenn =sQ ands∈ Z>0. For these values ofn, the coefficient functionsa±n(q) in Eq. (3.3) become
a±sQ (q) = ˆa±sQ (q)
sQ(qsQ− 1)qσ±sQ
. (3.18)
6In the TS/ST correspondence, one can also define off-shell wave functions, in which case the dual blocks differ
from the original ones.
7One reason for this difference, which was pointed out to us by Sergei Gukov, is that the results of [22] involve the
super A-polynomial, and they might lead to a different specialization for SL(2 , C).
– 11 –
Similarly, considering the dual variable
qD = e
4π2
ℏ = e2πiQ
P , (3.19)
the possible singularities of the dual function ϕWKB(XD;qD) occur in a±n(qD) when n = sP and
s∈ Z>0. Indeed, the coefficient functions a±n(qD) in Eq. (3.3) become
a±sP (qD) = ˆa±sP (qD)
sP (qsP
D − 1)qσ±sP
D
. (3.20)
Let us now introduce
qϵ = eiℏϵ, q ϵ,D = e
4π2i
ℏϵ , ℏϵ = 2πP
Q +ϵ, 0<ϵ ≪ 1, (3.21)
and consider the limit ϵ→ 0. As detailed in Appendix A, Eqs. (3.18), (3.20) produce the NLO
ϵ-expansions
a±sQ (qϵ) =

− i
(sQ)2ϵ− 1
2sQ + 1
(sQ)2q ∂
∂q
 ˆa±sQ(q)
qσ±sQ
+O(ϵ), (3.22a)
a±sP (qϵ,D) =
 i
(sQ)2ϵ + 1
sP
 i
2πsQ− 1
2

+ 1
(sP )2qD
∂
∂qD
 ˆa±sP (qD)
qσ±sP
D
+O(ϵ). (3.22b)
We then require the cancellation of the ϵ-poles in Eqs. (3.22a), (3.22b), which yields the relation
ˆa±sQ

e2πiP
Q

e−2πiP
Qσ±sQ = ˆa±sP

e2πiQ
P

e−2πiQ
Pσ±sP , (3.23)
for all s,P,Q ∈ Z>0 with P,Q coprime. We remark that, for the geometric branch, the formula in
Eq. (3.23) assumes the simplified form 8
ˆa(geom)
sQ

e2πiP
Q

= ˆa(geom)
sP

e2πiQ
P

, (3.24)
where again s,P,Q ∈ Z>0 with P,Q coprime.
Let us now prove that the cancellation formula in Eq. (3.23) is indeed a consequence of the
integrality structure presented in Eq. (3.6). More precisely, Eqs. (3.3), (3.7) imply that
ˆan(q)q−σn =
X
k|n
kDk

q
n
k

q−n
kσk
k−1X
j=0
q
n
kj, (3.25)
and, after substituting n =sQ and q = e2πiP
Q with s,P,Q as above, we obtain
ˆasQ

e2πiP
Q

e−2πiP
QσsQ =
X
k|sQ
kDk

e2πisP
k

e−2πisP
k σk
k−1X
j=0
e2πisP
k j. (3.26)
Since the sum over j on the RHS is non-zero if and only if k|s, Eq. (3.26) gives
ˆasQ

e2πiP
Q

e−2πiP
QσsQ =
X
k|s
k2Dk(1) =cs∈ Z, s ∈ Z>0, (3.27)
8A similar cancellation requirement was obtained in [12] in the study of the wave function for quantum mirror
curves.
– 12 –
which is independent of the choice of P,Q∈ Z>0 coprime, thus proving the cancellation identity in
Eq. (3.23). We note that the case of ˆ a−n(q) is handled analogously, yielding the same result. In
particular, recalling that σ−n = 0, n∈ Z>0, it defines the sequence of integers
ˆa−sQ

e2πiP
Q

=
X
k|s
k2D−k(1) =c−s∈ Z, s ∈ Z>0. (3.28)
Finally, applying the M¨ obius inversion formula for arithmetic functions, we deduce that
D±s(1) = 1
s2
X
k|s
µ(k)c±s
k
, s ∈ Z>0, (3.29)
whereµ(k) is the M¨ obius function. As we will see, the construction presented here is experimentally
verified for the knots 41 and 52 in Section 4.
