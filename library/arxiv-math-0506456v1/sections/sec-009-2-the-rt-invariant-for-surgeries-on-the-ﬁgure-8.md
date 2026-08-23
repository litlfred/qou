---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-009-2-the-rt-invariant-for-surgeries-on-the-ﬁgure-8
section_title: "The RT-invariant for surgeries on the ﬁgure 8 knot"
section_number: 2
pages: 10-11
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
This section is primarily intended to introduce notation. Moreover, w e present some
preliminary formulas for the colored Jones polynomial of the ﬁgure 8 knot and for
the RT–invariants of the 3–manifolds Mp/q.
Let t = exp(2π√−1/(4r)), r an integer ≥ 2, and let Ut be the modular Hopf
algebra considered in [27, Sec. 8], i.e. Ut is a ﬁnite-dimensional factor of the quantum
groupUξ(sl2(C)),ξ =t4. (In [27], and in most literature on the subject, ξ is denoted
q, but we use in this paper q to mean something diﬀerent.) For an integer k we let
[k] = t2k −t−2k
t2 −t−2 = sin(πk/r)
sin(π/r) ,
sometimes called a quantum integer. For a knot K inS3 we denote by K 0 the knot
K considered as a framed knot with framing zero. The colored Jones p olynomial
associated to Ut of a framed oriented knot K with color λ ∈ {1, 2,...,r } is denoted
JK(λ), and for an oriented knot K in S3 we let J ′
K(λ) = JK 0 (λ)/[λ]. Here the
colors are the dimensions (as complex vector spaces) of irreducible Ut–modules.
Let Nf be the 3–manifold obtained by surgery on S3 along K with surgery
coeﬃcient f ∈ Z. By [16] or [27] the RT–invariant (at level r − 2) of Nf is
τr(Nf ) = α
r−1∑
k=1
ξ(k2−1)f/ 4[k]2J ′
K(k), (2.12)
where K is given an arbitrary orientation. Here α =Csign(f )D−2, where
D =
√
r
2
1
sin(π/r),
C = exp
(√−1π
4
3(2 −r)
r
)
.
We use here the normalization of [34]. This is D−1 times the normalization of [16]
and C−b1(Nf )D−1 times the normalization of [27], where b1(Nf ) is the ﬁrst Betti
number of Nf , see [8, Appendix A]. (In the notation of [34], C = ∆ D−1.)
Let us next generalize to arbitrary rational surgery. Let p,q be a pair of coprime
integers with q ⁄= 0, and let Np/q be the 3–manifold obtained by surgery along K
with surgery coeﬃcient p/q. Choose c,d ∈ Z such that B =
( p c
q d
)
∈ SL(2, Z).
Then (see e.g. [8, Theorem 5.1 and the proofs of Corollary 8.3 and The orem 8.4]),
τr(Np/q) =
(
e
iπ
4 exp
(
−iπ
2r
)) Φ(B)−3sign(pq)√
2
r sin
(π
r
) r−1∑
λ=1
[λ]J ′
K(λ) ˜Bλ,1,
