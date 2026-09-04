---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-007-51-large-n-solutions-and-automodel-diagrams
section_title: "Large N solutions and automodel diagrams"
section_number: 5.1
pages: 16-18
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
All possible large N solutions of (5.9) were discussed in [7] and it was observed that (5.9) ad-
mits two possible solutions. However, here we look at the problem more carefully keeping the
symmetry of the growth process in mind. From the Plancherel measure (3.8) we see that at any
level k, two Young diagrams related to each other by transposition, have same probability P(λk).
Therefore the large N solution of (5.9) must be invariant under transposition. Young diagrams,
symmetric under transposition, are called rectangular diagrams [2, 5].
16
Following [7], we can take the following ansatz foru(h) to get a rectangular Young diagram
u(h) =
{1 h∈ [0, p)
˜u(h) h∈ (p, q]. (5.12)
To solve the saddle point equation we deﬁne a resolvent
H(h) =
∫ hU
hL
u(h′)dh′
h− h′ . (5.13)
After a little algebra, we ﬁnd that the resolvent H(h) is given by [7]
H(z) = ln

h
(
h− 1−
√
(h− 1)2− 4ξ2
)
2ξ2
. (5.14)
The resolvent is same as the moment generating function for the rectangular diagrams deﬁned in
(3.16) [5]. The resolvent has a branch cut in the complex h plane. Young diagram density is given
by the discontinuity of H(h) about the branch cut
˜u(h) = 1
π cos−1
[h− 1
2ξ
]
, for p≤ h≤ q. (5.15)
The supports p and q are given by,
p = 1− 2ξ, q = 1 + 2ξ. (5.16)
This particular class of solution exists subject to the following condition
k′ =ξ2. (5.17)
Since p≥ 0, this solution is valid for 0≤ξ≤ 1/2. From the deﬁnition of ξ (ξ2 = zk′) we also see
that this solution exists for
either ξ = k′ = 0 or z = 1. (5.18)
The case ξ = k′ = 0 is trivial. This means there is no box in the Young diagram. The non-trivial
solution corresponds to z = 1 (i.e. fugacity is one and hence zero chemical potential). It is easy
to check that the Young diagram is invariant under transposition. The height of the ﬁrst column
can be calculated from equation (5.4) and is given by 2 ξ which is similar to the length of the
ﬁrst row. Also the function ˜ u(h) is symmetric about body diagonal. A typical Young diagram
for this class is depicted in ﬁgure 5. In this phase the renormalised number of boxes (i.e. k′) in
a Young diagram grows from k′ = 0 to k′ = 1/4 as ξ changes from 0 to 1/2. For any value of
ξ between 0 and 1/2 the dominant Young diagram is always symmetric under transposition and
hence a rectangular diagram. The limiting value ξ = 1/2 (GWW transition point) corresponds to
the distribution
˜u(h) = 1
π cos−1(h− 1). (5.19)
17
Figure 5: A Young diagram in English notation for automodel class (0<ξ < 1/2).
This terminal distribution is same as the universal curve or the limit shape obtained by [3, 4].
Hence we see that the limit shape Young diagram corresponds to GWW transition point in matrix
model side.
We calculate Plancherel measure (3.8) for this dominant diagram. Following [7], the Plancherel
measure in large N limit is given by
1
N2 lnPλk =
∫ q
0
dhu(h)−
∫ q
0
dh′u(h′) ln|h− h′|− 2
∫ q
0
u(h)h ln h dh + k′ + 1 + k′ ln k′. (5.20)
Evaluating the right hand side for symmetric solutions (5.12) and (5.15) we get
Pλk = 1 + O (1/N). (5.21)
Thus we see that in the large k (or large N) limit the symmetric solution (5.12, 5.15) is the max-
imum probable solution. Probability of having other diagrams is suppressed by powers of N.
This gives an alternate proof of limit shape theorem of Vershik-Kerov and Logan-Shepp result
[3, 4].
The partition function (4.3) admits another phase. The dominant diagrams in that phase are not
self-transpose. See Appendix C for details. Growth of such diagrams are di ﬀerent than that
studied in section 3.
