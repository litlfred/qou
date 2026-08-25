---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INV ARIANTS"
section_id: sec-009-21-strategy-of-the-proof
section_title: "Strategy of the proof"
section_number: 2.1
pages: 10-11
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariant s."
---
technical results that will be explained later.
We restrict to the case L = ∅ for simplicity. We would like to deﬁne IM ∈ R b, such
that
(10) τ′
M (ξ) = ev ξ (IM )
for any root of unity ξ of odd order. This uniﬁed invariant is multiplicative with respect
to the connected sum.
The following observation is important. By Proposition 4, there is at most one element
f (q) ∈ R b such that for every root ξ of odd order one has
τ′
M (ξ) = ev ξ (f (q)) .
That is, if we can ﬁnd such an element, it is unique, and we put IM := f (q).
2.2. Laplace transform. The following is the main technical result of [2]. A proof will
be explained in the next Section.
Theorem 5. [Beliakova–B¨ uhler–Le]Suppose b = ±1 or b = ±pl where p is a prime and
l is positive. For any non–negative integer k, there exists an element Qb,k ∈ R b such that
UNIFIED 3–MANIFOLD INV ARIANTS 11
for every root ξ of odd order r one has
∑
n
ξ qb n2−1
4 A(n, k)
FU b(ξ) = ev ξ(Qb,k ).
In addition, if b is odd, Qb,k ∈ S b.
2.3. Deﬁnition of the uniﬁed invariant: diagonal case. Suppose that the linking
number between any two components of L is 0, and the framing on components of L are
bi = ±pki
i for i = 1, . . . , m, where each pi is prime or 1. Let us denote the link L with all
framings switched to zero by L0.
Using (8), taking into account the framings bi’s, we have
JL(n)
m∏
i=1
[ni] =
∑
k≥0
CL0(k)
m∏
i=1
qbi
n2
i −1
4 A(ni, ki).
By the deﬁnition of FL, we have
FL(ξ) =
∑
k≥0
evξ(CL0(k))
m∏
i=1
∑
ni
ξ
qbi
n2
i −1
4 A(ni, ki).
From (6) and Theorem 5, we get
τ′
M (ξ) = ev ξ
{ m∏
i=1
IL(bi, 1)
∑
k
CL0(k)
m∏
i=1
Qbi,k i
}
,
where the existence of the uniﬁed invariant of the lens space IL(bi, 1) ∈ R b, with ev ξ(IL(bi, 1)) =
τ′
L(bi, 1)(ξ) can be shown by a direct computation (we refer to [2] for more det ails).
Thus if we deﬁne
IM :=
m∏
i=1
IL(bi, 1)
∑
k
CL0(k)
m∏
i=1
Qbi,k i ,
then (10) is satisﬁed. By Theorem 2, CL0(k) is divisible by ( qk+1; q)k+1/(1 − q), which is
divisible by ( q; q)k, where k = max ki. It follows that IM ∈ R b. In addition, if b is odd,
then IM ∈ S b.
