---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INV ARIANTS"
section_id: sec-006-14-evaluation-and-gauss-sums
section_title: "Evaluation and Gauss sums"
section_number: 1.4
pages: 7-9
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariant s."
---
the evaluation map ev ξ by replacing q with ξ.
Suppose f (q; n1, . . . , nm) is a function of variables q±1 and integers n1, . . . , nm. In
quantum topology, the following sum plays an important role
∑
ni
ξ
f :=
∑
0<ni<2r
ni odd
evξf (q; n1, . . . , nm)
where in the sum all the ni run over the set of odd numbers between 0 and 2 r.
In particular, the following variation of the Gauss sum
γb(ξ) :=
∑
n
ξ
qb n2−1
4
is well–deﬁned, since for odd n, 4 | n2 − 1. It is known that, for odd r, |γb(ξ)| is never 0.
1.5. Deﬁnition of the WRT invariants. Let
FL(ξ) :=
∑
ni
ξ m∏
i=1
[ni] JL(n1, . . . , nm).
Theorem 1. [Reshetikhin–Turaev] FL(ξ) is invariant under K1–Move.
An important special case is when L = U b, the unknot with framing b ⁄= 0. In that
case FU b(ξ) can be calculated using the Gauss sum and is nonzero.
Let σ+ (respectively σ−) be the number of positive (negative) eigenvalues of the linking
matrix of L. Then we deﬁne
(3) τM (ξ) = FL(ξ)
(FU +1(ξ))σ + (FU −1(ξ))σ −
.
It is easy to see that τM (ξ) is invariant under K2–Move, and hence, by Theorem 1, it
is a topological invariant of M called the SO(3) WRT invariant. Moreover, τM (ξ) is
multiplicative with respect to the connected sum.
8 ANNA BELIAKOV A AND THANG LE
Remark. If we drop the condition that the colors in the summation are odd, an d sum
over all (odd and even) colors, the result will be the SU (2) WRT invariant τ SU (2)
M (ξ). In
this case, the order of ξ could also be even.
The SO(3) WRT invariant extends naturally to the invariant of the pair ( M, L′), where
the manifold M contains a link L′ inside. In this case we have to replace the surgery link
L of M by L ∪ L′ in all deﬁnitions, ﬁx colors on L′ and sum over all colorings of L only.
We omit here the precise deﬁnition and refer to [2] for more details.
For example, the SO(3) invariant of the lens space L(b, 1), obtained by surgery along
U b, is
(4) τL(b, 1)(ξ) = FU b(ξ)
FU sn(b)(ξ) ,
were sn(b) is the sign of the integer b.
Suppose M is a rational homology 3–sphere. Then there is a unique decompositio n
H1(M, Z) =⨁
i Z/biZ, where each bi is a prime power. We renormalize the SO(3) WRT
invariant as follows:
(5) τ′
M (ξ) = τM (ξ)
∏
i
τL(bi, 1)(ξ) ,
where L(b, a) denotes the ( b, a) lens space. Note that τL(b, 1)(ξ) is always nonzero.
Let us focus on the special case when the linking matrix of L is diagonal. Assume each
Lii = bi is a power of a prime or 1, up to sign. Then H1(M, Z) = ⊕m
i=1Z/|bi|, and
σ+ = card {i | bi > 0}, σ − = card {i | bi < 0}.
Thus from the deﬁnitions (3), (4) and (5) we have
(6) τ′
M (ξ) =
( m∏
i=1
τ′
L(bi, 1)(ξ)
)
FL(ξ)
∏ m
i=1 FU bi (ξ) ,
with
τ′
L(bi, 1)(ξ) = τL(bi, 1)(ξ)
τL(|bi|, 1)(ξ) .
The collection of SO(3) WRT invariants is diﬃcult to study, since their deﬁnition
heavily depends on the order of ξ. The following cyclotomic expansion will play an
important role for the uniﬁcation of the WRT invariants.
1.6. Habiro’s cyclotomic expansion of the colored Jones polynom ial. For non–
negative integers n, k we deﬁne
A(n, k) :=
∏ k
i=0 (qn + q−n − qi − q−i)
(1 − q) (qk+1; q)k+1
.
For k = (k1, . . . , km) let
A(n, k) :=
m∏
j=1
A(nj, kj).
Note that A(n, k) = 0 if kj ≥ nj for some index j. Also A(n, 0) = q−1JU (n)2.
UNIFIED 3–MANIFOLD INV ARIANTS 9
The colored Jones polynomial JL(n) can be repackaged into the invariant CL(k) as
stated in the following theorem.
Theorem 2. [Habiro] Suppose L is a link in S3 having zero linking matrix. Then there
are invariants
(7) CL(k) ∈ (qk+1; q)k+1
(1 − q) Z[q±1], where k = max{k1, . . . , km}
such that for every n = (n1, . . . , nm)
(8) JL(n)
m∏
i=1
[ni] =
∑
0≤ki≤ni−1
CL(k) A(n, k).
Note that the existence of CL(k) as rational functions in q satisfying (8) is easy to
establish. They correspond to the Jones polynomial colored by diﬀe rent elements of the
Grothendieck ring of Uq(sl2), i.e. by linear combinations of representations. The diﬃculty
here is to show the integrality of (7).
Since A(n, k) = 0 unless k < n, in the sum on the right hand side of (8) one can assume
that k runs over the set of all m–tuples k with non–negative integer components. We will
use this fact later.
