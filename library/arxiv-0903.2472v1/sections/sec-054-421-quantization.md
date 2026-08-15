---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-054-421-quantization
section_title: "Quantization"
section_number: 4.2.1
pages: 51-52
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
In order to test the proposed state integral model (3.53), we ﬁrst compute the perturbative
SL(2, C) invariants of M via quantization of Mﬂat (GC, Σ), as outlinted in Section 2.2.
Recall the expression (1.8) for the perturbative Chern-Sim ons partition function,
Z (α)(M ; ℏ,u ) = exp
(
1
ℏS(α)
0 (u)− 1
2δ(α) log ℏ +
∞∑
n=0
S(α)
n+1(u)ℏn
)
, (4.36)
where for the ﬁgure-eight knot complement α∈{ geom, conj, abel}, and, as explained e.g.
in [22, 23], δ(α⁄=abel) = 0.
In Section 2.2 we saw how quantization of the relation A(l,m ) = 0 leads to the equation
ˆA(ˆl, ˆm) Z (α)(M ; ℏ,u ) = 0 , (4.37)
which then determines the perturbative GC invariantZ (α)(M ; ℏ,u ). As explained earlier,
cf. eqs. (1.17) and (2.36), a simple way to ﬁnd the operator ˆA(ˆl, ˆm) is to note that it also
annihilates the polynomial invariants (of the knot K) computed by Chern-Simons theory
with compact gauge group G. In the present case, G = SU (2) and the equation (2.36)
takes the form of a recursion relation on the set of colored Jo nes polynomials,{Jn(K;q)}.
Speciﬁcally, using the fact that ˆl acts by shifting the value of the highest weight of the
representation and writing ˆA(ˆl, ˆm) =∑ d
j=0aj( ˆm,q )ˆlj as in (2.43), we obtain
d∑
j=0
aj(qn/2,q )Jn+j(K;q) = 0. (4.38)
It is easy to verify that the colored Jones polynomials of the ﬁgure-eight knot indeed satisfy
such a recursion relation, with the coeﬃcients (see also 22 [17, 18]):
a0( ˆm,q ) = q ˆm2
(1 +q ˆm2)(−1 +q ˆm4), (4.39a)
a1( ˆm,q ) = 1 + (q2− 2q) ˆm2− (q3−q2 +q) ˆm4− (2q3−q2) ˆm6 +q4 ˆm8
q1/2 ˆm2(1 +q2 ˆm2−q ˆm4−q3 ˆm6) , (4.39b)
a2( ˆm,q ) =− 1− (2q2−q) ˆm2− (q5−q4 +q3) ˆm4 + (q7− 2q6) ˆm6 +q8 ˆm8
q ˆm2(1 +q ˆm2−q5 ˆm4−q6 ˆm6) , (4.39c)
a3( ˆm,q ) =− q4 ˆm2
q1/2(1 +q2 ˆm2)(−1 +q5 ˆm4). (4.39d)
Note that in the classical limit q =e2ℏ→ 1, we have
ˆA(ˆl, ˆm) −→
ℏ→0
A(l,m )
m2(m2− 1)(m2 + 1)2 . (4.40)
22Note that [17, 18] look at asymptotics of the colored Jones po lynomial normalized by its value at the
unknot, while the SL(2, C) Chern-Simons partition function should agree with the unn ormalized colored
Jones polynomial. Hence, we must divide the expressions for aj there by ( m2qj/ 2 − q−j/ 2) to account for
the diﬀerence, introducing a few factors of q1/ 2 in our formulas.
– 50 –
We could multiply all the aj’s by the denominator of (4.40) (or a q-deformation thereof) to
obtain a more direct correspondence between ˆA(ˆl, ˆm) and A(l,m ), but this does not aﬀect
any of the following calculations.
To ﬁnd the exact perturbative invariant Z (α)(M ; ℏ,u ) for each α, we reduce ˆm to
a classical variable m (since in the u-space representation the operator ˆ m just acts via
ordinary multiplication), expand each of the above aj’s asaj(m,q ) =∑ ∞
p=0aj,p(m)ℏp, and
substitute the aj,p into the hierarchy of diﬀerential equations derived in Secti on 2.2 and
displayed in Table 1. The equations are then solved recursiv ely on each branch α of the
A-polynomial to determine the coeﬃcients S(α)
n (u).
Geometric branch
For the geometric branch, the solution to the ﬁrst equation i n Table 1 is chosen to be
S(geom)
0 (u) = i
