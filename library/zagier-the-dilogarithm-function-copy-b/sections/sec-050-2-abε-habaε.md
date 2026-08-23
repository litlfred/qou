---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-050-2-abε-habaε
section_title: "A+B)ε HA,B+A(ε)"
section_number: 2
pages: 50-51
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
for HA,B(ε). Write HA,B(ε)=
∞∑
n=0
hn(A, B) εn where h0 ≡ 1a n d hn(A, B)i s
a polynomial of degree 2 n in B without constant term for n ≥ 1. Substituting
this into the functional equation and replacing B by B − A, we obtain
hn(A, B−A)= Qh n(A, B+1 −A)+( 1 − Q)
n∑
s=0
(A/2 − B)s
s! hn−s(A, B) ,
and this equation gives the coeﬃcient hn,m of Bm in hn(A, B) recursively in
terms of earlier coeﬃcients hn′,m′ with n′ <n or with n′ = n, m′ <m .
Remark. The functional equation (37) remains true formally if one re-
places FA,B(q)b y F ⋆
A,B(q)= qB2/2AF1/A,B /A(q−1), so the formal power se-
ries HA,B(ε) satisﬁes a second functional equation H1/A,B /A(−ε)= eεB2/2A
HA,B(ε). (Note that the change ( A, B) ↦→(1/A, B /A) changes Q to 1 − Q =
QA and does not change B2/A or QA.) It follows that the coeﬃcients cj(A, B)
in (35) satisfy the functional equations
cj(A, B) − (−1)j cj(1/A, B /A)= γj(A)+
{
B2/2A if j =1 ,
0 otherwise
for some constants γj = γj(A) independent of B. Using the explicit formulas
for cj which will be computed below, we ﬁnd that γ−1 = L(1), γ0 = − 1
2 log A,
γ1 = − 1
24 , γ2 = γ3 = γ4 = 0. This suggests the conjecture that γj =0f o r
all j ≥ 2. Assuming this, we have the formal functional equation
F ⋆
A,B
(
e−ε)
=
√
A exp
(
− π2
6ε + ε
24 +O
(
εN))
FA,B
(
e−ε)
(∀N> 0). (38)
(b) The second method is based on the asymptotics of the individual te rms
in the series (34). Denote the nth term in this series by un. Then the ratio
un/un−1 = qAn+B−A/2/(1−qn) is small for q small and large for q very near 1,
and becomes equal to 1 when qn is near to the unique root Q ∈ (0, 1) of the
equation Q + QA = 1. The terms that contribute are therefore those of the
The Dilogarithm Function 53
form qn = Qq−ν with ν ∈ ν0 + Z of order much less than n, where ν0 denotes
the fractional part of − log(Q)/ log(q). To know the size of un in this range we
ﬁrst have to know the behavior of ( q)n as q → 1a n d n →∞ with qn tending
to a ﬁxed number Q.I ti sg i v e nb y :
Lemma. For ﬁxed Q ∈ (0, 1) and q = e−ε → 1 with qn = Qq−ν with n →∞ ,
ν = o(n), we have
log
( 1
(q)n
)
∼
[ π2
6 − Li2(Q)
]
ε−1 −
[
(ν − 1
2 ) log
( 1
1 − Q
)
+ 1
2 log
( 2π
ε
)]
−
[ 1
24 + 1
2
(
ν2 − ν + 1
6 ) Q
1 − Q
]
ε −
∞∑
r=3
Br(ν)L i2−r(Q) εr−1
r!
as ε → 0, where Br(ν) denotes the rth Bernoulli polynomial and Li−j(Q) is
the negative-index polylogarithm Li−j(Q)=
∞∑
m=1
mjQm =
(
Q d
dQ
) j 1
1 − Q .
Proof. The Euler-Maclaurin formula or the modularity of η(z) gives
log
( 1
(q)∞
)
= π2
6ε − 1
2 log
( 2π
ε
)
− ε
24 +O
(
εN)
for all N as ε → 0. On the other hand, we have
log
( (q)n
(q)∞
)
=
∞∑
s=1
log
( 1
1 − qn+s
)
=
∞∑
s=1
log
( 1
1 − Qqs−ν
)
=
∞∑
s=1
∞∑
k=1
Qk
k qk(s−ν) =
∞∑
k=1
Qk
k
eνkε
ekε − 1
=
∞∑
k=1
Qk
k
∞∑
r=0
Br(ν)
r! (kε)r−1 =
∞∑
r=0
Br(ν)
r! Li2−r(Q) εr−1 .
Subtracting these two formulas gives the desired result. □
With the same conventions ( q = e−ε, qn = Qq−ν), we also have
log
(
q
1
