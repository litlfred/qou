---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-023-273-calculating-the-path
section_title: "Calculating the Path"
section_number: 2.7.3
pages: 53-57
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
In order to write down the expressions for fV
lr (R) and gV
lr,M(R), as illustrated in
Fig. 2.5, we deﬁne states |ψr
M(R)⟩ and|ψl
M(R)⟩ along the path for computational
convenience. Following the computation rule described in chapter. 2.7.2, the states
|ψr
M(R)⟩ and|ψl
M(R)⟩ are deﬁned as
|ψr
M(R)⟩
≡



∑
S
e
−VM ∆τ
2 e
−V†
M ∆τ
2 Ge
−VM+ 1∆τ
2 e
−V†
M+1∆τ
2 G...e
−V†
N−1∆τ
2 Ge
−VN ∆τ
2 |S⟩⟨RNS|ψr
T⟩,
| {z }
M⁄=N,0.
∑
S
e
−VN ∆τ
2 |S⟩⟨RNS|ψr
T⟩,
| {z }
M=N.
∑
S
e
−V†
0∆τ
2 Ge
−V1∆τ
2 e
−V†
1∆τ
2 Ge
−V2∆τ
2 e
−V†
2∆τ
2 G...e
−V†
N−1∆τ
2 Ge
−VN ∆τ
2 |S⟩⟨RNS|ψr
T⟩.
| {z }
M=0.
(2.101)
|ψl
M(R)⟩
≡



∑
S
(
Ge
−V1∆τ
2 e
−V†
1∆τ
2 G...Ge
−VM ∆τ
2 e
−V†
M ∆τ
2
)†
e
−V0∆τ
2 |S⟩⟨R0S|ψl
T⟩,
| {z }
M⁄=0,N.
∑
S
e
−V0∆τ
2 |S⟩⟨R0S|ψl
T⟩,
| {z }
M=0.
∑
S
e
−V†
N ∆τ
2
(
Ge
−V1∆τ
2 e
−V†
1∆τ
2 G...Ge
−VN−1∆τ
2 e
−V†
N−1∆τ
2 G
)†
e
−V0∆τ
2 |S⟩⟨R0S|ψl
T⟩.
| {z }
M=N.
(2.102)
Both|ψl
M(R)⟩ and|ψr
M(R)⟩ can be expanded by the Ntot spin isospin basis states
43
|S⟩ with accordingly probability amplitude φr
M(R,S ) and φl
M(R,S ),
φr
M(R,S ) =⟨S|ψr
M(R)⟩, (2.103)
φl
M(R,S ) =⟨S|ψl
M(R)⟩. (2.104)
So that,
|ψr
M(R)⟩ =
∑
S
|S⟩⟨S|ψr
M(R)⟩ =
∑
S
φr
M(R,S )|S⟩, (2.105)
|ψl
M(R)⟩ =
∑
S
|S⟩⟨S|ψl
M(R)⟩ =
∑
S
φl
M(R,S )|S⟩. (2.106)
FunctiongV
lr,M(R) depends on which bead M the operator ˆO is placed at. For a
givenM, it is calculated as
gV
lr,M(R) =



⟨ψl
M−1(R)|Ge
−VM ∆τ
2 ˆOMe
−V†
M ∆τ
2 G|ψr
M+ 1(R)⟩, M ⁄= 0,N.
∑
S
⟨ψl
T| ˆO|R0S⟩⟨S|ψr
0(R)⟩, M = 0.
∑
S
⟨ψl
N(R)|S⟩⟨RNS| ˆO|ψr
T⟩, M =N.
(2.107)
In particular, if the operator ˆO commutes with Hamiltonian, then ˆO can be moved
to leftmost or the rightmost position, and the result Eq.(2.3) can then be written as
Eq.(2.12), and the corresponding g(R)lr becomes,
g(R)lr = 1
2
[
gV
lr,M(R)|M=0 +gV
lr,M(R)|M=N
]
gF (R). (2.108)
This is for example how we calculate the ground state energy ˆO =H.
For the AV6’ interaction which does not have a spin-orbit term, the G in Eq.(2.107)
is just 1. Note that the integer M in gV
lr,M(R) is usually set at the middle between
0 and N, such that e
−VM ∆τ
2 ˆOe
−V†
M ∆τ
2 is exactly placed in the middle of all the beads,
so we make sure operator ˆO is truly sandwiched between the same state which is the
ground state if total imaginary time τ is big enough.
44
The function fV
lr (R) does not depend on M. Its value is the same as long as the
left and right order l, r, andR are the same. For any integer M from 0 to N− 1, it
can be calculated as,
fV
lr (R) =⟨ψl
M(R)|G|ψr
M+1(R)⟩ =
∑
S
⟨ψl
M(R)|S⟩⟨S|G|ψr
M+1(R)⟩, (2.109)
where
⟨S|G|ψr
M+1(R)⟩
=
⟨
S
⏐⏐⏐⏐⏐
{
1 + m
4iℏ2
∑
i<j
v7(rM
ij )
[
rM
ij × ∆rM,M +1
ij · (σi +σj)
]}⏐⏐⏐⏐⏐ψr
M+1(R)
⟩
, (2.110)
and the deﬁnitions of rM
ij ,rM
ij and ∆rM,M +1
ij are the same form as for r′
ij,r′
ij and
∆rR′,R
ij used in Eq.(2.68). The M and M + 1 simply mean the conﬁgurations RM and
RM+1. For the AV6’ interaction we haveG = 1 so fV
lr (R) is simpliﬁed to the following
form,
fV
lr (R) =⟨ψl
M(R)|ψr
M+1(R)⟩
=
∑
S
⟨ψl
M(R)|S⟩⟨S|ψr
M+1(R)⟩
=
∑
S
φl
M
∗
(R,S )φr
M+1(R,S ). (2.111)
In our PIMC code, the spin, isospin states are written in binary representation
(Carlson and Wiringa (1991)) and we label the A particles from 0 to A− 1. In the
code, we use 0 for neutron and spin down, 1 for proton and spin up. We use a 2
dimensional complex array a(li,ls) to represent a state. For example, in Eq.(2.106),
a certain basis state is φr
M(R,S )|S⟩, if|S⟩ =|n↑n↓p↑p↑⟩, then this basis state
can be stored as a(3, 11) =φr
M(R,S ). Integer li = 3 for the isospin in binary is 0011
which, from right to left, means 0 th and 1st particles are protons, 2 nd and 3rd particles
are neutrons, so it is |nnpp⟩. Integer ls = 11 for the spin in binary is 1011, means
45
that the 0 th and 1st particles are spin up, 2 nd particles is spin down, 3 rd one is spin
up, so it is|↑↓↑↑⟩ . All those|ψl
M(R)⟩ and|ψr
M(R)⟩ states deﬁned in Eqs.(2.105,2.106)
for each bead, are represented by their coeﬃcients φr
M(R,S ) and φl
M(R,S ) deﬁned
in Eqs.(2.105,2.106), and therefore stored in those 2 dimensional complex arrays like
a(li,ls). All the quantities can be calculated from |ψr
M(R)⟩ and|ψl
M(R)⟩.
It will be slow if we calculate fV
lr (R) and gV
lr,M(R) by ﬁrst calculating all the Ntot
byNtot matrices of⟨S′|e
−VI∆τ
2 |S⟩ and⟨S′|G|S⟩ along all the beads in Fig. 2.5, then
multiplying all of them. This is because these matrices are sparse. Any 2-body charge
conserving operator will only have either 4 or 8 nonzero entries in a row or column.
We can instead from right to left directly calculate |ψr
N−1(R)⟩ from|ψr
N(R)⟩, then
|ψr
N−2(R)⟩ from|ψr
N−1(R)⟩, ..., until|ψr
M+1(R)⟩ from|ψr
M+2(R)⟩. Also, from left to
right, we can calculate |ψl
1(R)⟩ from|ψl
0(R)⟩, then|ψl
2(R)⟩ from|ψl
1(R)⟩, ..., until
|ψl
M(R)⟩ from|ψl
M−1(R)⟩. The recursion relations from Eqs.(2.101) and (2.102), can
be written as,
|ψr
M(R)⟩ =



∑
S
(
e
−VM ∆τ
2 e
−V†
M ∆τ
2 G
)
|S⟩⟨S|ψr
M+1(R)⟩, M ⁄=N, 0.
∑
S
e
−VN ∆τ
2 |S⟩⟨RNS|ψr
T⟩, M =N.
∑
S
e
−V†
0∆τ
2 G|S⟩⟨S|ψr
1(R)⟩, M = 0.
(2.112)
|ψl
M(R)⟩ =



∑
S
(
Ge
−VM ∆τ
2 e
−V†
M ∆τ
2
)†
|S⟩⟨S|ψl
M−1(R)⟩, M ⁄= 0,N.
∑
S
e
−V0∆τ
2 |S⟩⟨R0S|ψl
T⟩, M = 0.
∑
S
e
−V†
N ∆τ
2 G†|S⟩⟨S|ψl
N−1(R)⟩, M =N.
(2.113)
Once we have the corresponding |ψr
M(R)⟩ and|ψl
M(R)⟩ calculated, we can use
Eqs.(2.109) and (2.107) to calculate fV
lr (R) and gV
lr,M(R) and then Alr(R) and Blr(R)
and thus⟨ ˆO(∆τ)⟩. This updating strategy for |ψr
M(R)⟩ and|ψl
M(R)⟩ is much faster
46
# # # # # # # # # # # # 
# * * # # # # # # # # # 
# # # # # # # * * # # # 
…
# # # * * * # # * * # # 
…
# * # * # * # # * * * # 
* * * * * * * * * * * 
* * * # * # # * * * # * 
Figure 2.6: Illustration of calculating |ψr
K−1(R)⟩ from|ψr
K(R)⟩ from right to left
directly.
than direct Ntot byNtot sparse matrix multiplication method. This is why we deﬁne
states|ψr
M(R)⟩ and|ψl
M(R)⟩ and use Eqs. (2.112) and (2.113) to calculate them and
then ﬁnally calculate fV
lr (R) and gV
lr,M(R) by using Eqs.(2.109) and (2.107).
Fig. 2.6 illustrates the right to left direct calculation of |ψr
K−1(R)⟩ from|ψr
K(R)⟩.
In the direct calculation|ψr
K−1(R)⟩ and|ψr
K(R)⟩ are always treated as column vectors,
we directly operate the G, e
−V†∆t
2 and e
−V∆t
2 on the column vector|ψr
K(R)⟩ and get
new column vectors each time until we get the next column vector |ψr
K−1(R)⟩. By
doing that we prevent writing each of the operators as Ntot byNtot sparse matrix and
doing the slow matrix multiplications.
