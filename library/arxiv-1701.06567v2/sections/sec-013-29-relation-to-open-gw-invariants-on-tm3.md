---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-013-29-relation-to-open-gw-invariants-on-tm3
section_title: "Relation to open GW invariants on T∗M3"
section_number: 2.9
pages: 22-24
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Consider U(N) level-k Chern-Simon theory on a rational homology sphere M3,
b1(M3) = 0 , (2.50)
i.e.H1(M3, Z) = TorH1(M3, Z) is a ﬁnite abelian group. (What follows can be considered as
a generalization from the case H1(M3, Z)∼= Z considered in [57]).
Similar to the SU (2) case, ∑N
i=1𝓁k(ai,ai) = CS(a) is the Chern-Simons invariant of the
abelian ﬂat connection a, and Za(q) is a Borel resummation [22] of the asymptotic expansion
around a. Correspondingly, ˆZb(q) is a Borel resummation of the series of the following type:
ˆZb(q) =
∑
m≥0
nb
mq∆b+m resum= = =ˆZpert
b (k) =
∑
m≥1
Nb
m
(2πi
k
)m
∈ Q[[2πi/k]]. (2.51)
Consider
e2πia ∈ Hom
(
H1(M3),U (1)N)
/SN (2.52)
as a formal variable in a generating series. Then Sab, for eachb, up to a factor, can be viewed
as a basis element of the symmetric part of the group ring 21 of (H1(M3, Z))N:
|H1(M3)|N/2|StabSN (b)|−1Sab∈ Z
[
(H1(M3, Z))N
]SN
, b ∈ (H1(M3))N/SN, (2.55)
if we identify
N∏
i=1
e2πi𝓁k(ai,ci)≡ 1·c (2.56)
in the group ring of (H1(M3))N.
Then
(2k|H1(M3)|)N/2|StabSN (a)| Za(q) ∈ Z[[q1/|H1|]] ⊗Z Z
[
(H1(M3, Z))N
]SN
(2.57)
while ∑
b∈(H1(M3))N/SN
SabˆZpert
b (k) ∈ Q[[2πi/k]] ⊗Z Z
[
(H1(M3, Z))N
]SN
. (2.58)
21For example, when N = 2 and H1(M3, Z) = Z2 we have:
Z
[
(H1(M3, Z))N
]SN
∼= Z[x1,x 2]S2/{x2
1 = 1,x 2
2 = 1} (2.53)
and
Sa,(0,0)∝ 1
Sa,(1,0)∝x1 +x2
Sa,(1,1)∝x1x2
(2.54)
where xi =eπia.
– 21 –
On the other hand, one can consider open topological strings (A-model) on T∗M3 with
a Lagrangian brane along M3 equipped with a rank-N bundle and an abelian ﬂat connection
(local system) a. The free energy is given by
F top
a [T∗M3](gs) =
∑
g,h
g2g+h−2
s
∑
c∈(H1(M3,Z))h
Ng;c1,...,ch
h∏
j=1
e2πi ∑N
i=1𝓁k(ai,cj) (2.59)
where the open GW invariants
Ng;c1,...,ch ∈ Q (2.60)
count pseudoholomorphic maps from a genus-g Riemann surface with h holes to T∗M3 such
that the image of the j-th boundary component lands in a homology class cj∈ H1(M3, Z).
The factor
e2πi ∑N
i=1𝓁k(ai,cj) = Hol a(cj) (2.61)
is the holonomy of the abelian ﬂat connection a along cj. Note that
Ng;c1,...,ch = 0 unless c1 +... +ch = 0 ∈H1(M3, Z) (2.62)
because there are no non-trivial 2-cycles in T∗M3. When the ﬂat connection a is trivial, the
generating function (2.59) takes a familiar form
F top
0 [T∗M3](gs) =
∑
g,h
g2g+h−2
s Ng;hNh (2.63)
where the averaged version of open GW invariants
Ng;h =
∑
c∈(H1(M3,Z))h
Ng;c1,...,ch (2.64)
“forgets” where the boundary components map to.
Again, using the identiﬁcation ( 2.56), the generating function ( 2.59) can be regarded as
F top
a [T∗M3](gs) ∈ Q[[gs]]⊗Z Z
[
(H1(M3, Z))N
]SN
. (2.65)
Then, the relation between CS and open topological strings can be formulated as follows: 22
exp F top
a [T∗M3](gs)
⏐⏐
gs= 2πi
k
∝
∑
b
SabˆZpert
b (k) (2.66)
where the exponent is taken using multiplication rules in the ring in ( 2.65), the same as
the ring 23 in (2.58). The integer numbers nb
m in (2.51) are the “massless variants” of open
DT/Ooguri-Vafa invariants ofT∗M3.
22Normalizations of ZU(N)k, as well as the ﬁrst few terms in F top, are subject to ambiguity, and we won’t
attempt to ﬁx them here.
23Note, that any element of this ring has the form as in the right-hand side of ( 2.66) since ( 2.55) are basis
elements.
– 22 –
