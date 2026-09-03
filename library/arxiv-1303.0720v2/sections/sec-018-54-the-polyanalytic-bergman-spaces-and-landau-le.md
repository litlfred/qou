---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-018-54-the-polyanalytic-bergman-spaces-and-landau-le
section_title: "The polyanalytic Bergman spaces and Landau levels. The polyanalytic spaces PA2"
section_number: 5.4
pages: 11-13
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
q,m (see
Subsection 5.1) have been considered in, e.g., [30], [1], [26], and [16], focusing on Ω= C and
the quadratic potential Q(z) = |z|2, so that the corresponding weight ω(z) = e−2m|z|2 is Gaussian.
One instance where these spaces appear is as eigenspaces of the operator
˜∆z = −∆z + 2m¯z ¯∂z,
12
ANTTI HAIMI AND HAAKAN HEDENMALM
which is densely deﬁned in L2(C, e−2m|z|2). More precisely, the eigenspaces are of the form
PA2
q,m⊖A2
q−1,m, where ⊖denotes the orthogonal diﬀerence within the Hilbert space L2(C, e−2m|z|2).
The related operator
H := Me−m|z|2 ˜∆zMem|z|2,
where M denotes the operator of multiplication by the function in the subscript, is the Hamil-
tonian associated with a single electron in C within a uniform magnetic ﬁeld perpendicular to
the plane. The operator is called the Landau Hamiltonian and the eigenspaces are commonly
referred to as Landau levels.
Returning to a general potential Q, we may think of the orthogonal diﬀerence spaces
δPA2
q,m := PA2
q,m ⊖PA2
q−1,m,
as way to generalize the notion of Landau levels. Here, we note that in [28], Rozenblum
and Tashchiyan identify approximate spectral subspaces related to a Hamiltonian describing
a single electron in a magnetic ﬁeld with strength ∆Q. It may be observed that those spaces
are in a sense dual to the orthogonal diﬀerence spaces δPA2
q,m.
5.5. Asymptotic analysis of weighted polyanalytic Bergman kernels. It is our aim is to supply
an algorithm to compute a near-diagonal asymptotic expansion of the weighted polyanalytic
Bergman kernel Kq,m as m tends to inﬁnity. Under suitable assumptions on the potential Q, the
kernel has – up to an error term – the (local) expansion
Kq,m(z, w) ∼
n
mqbq
0(z, w) + mq−1bq
1(z, w) + · · · + mq−kbq
k(z, w)
o
e2mQ(z,w),
where near the diagonal z = w, the coeﬃcient functions bq
j(z, w) are q-analytic in each of the
variables z and ¯w. As before, Q(z, w) is a polarization of Q(z). The control of the error term
is of order O(mq−k−1) in the parameter m. We work this out in detail in the bianalytic case
q = 2, and obtain explicit formulae for b2
j when j = 0, 1, 2 (see Remark 7.6). Note that we may
use the formula δKq,m := Kq,m −Kq−1,m to asymptotically express the reproducing kernel δKq,m
associated with the orthogonal diﬀerence space δPA2
q,m.
We base our approach is based on the recent work of Berman, Berndtsson, and Sjöstrand [8],
where they give an elementary algorithm to compute the coeﬃcients bj = b1
j of the asymptotic
expansion of the weighted Bergman kernel. We now extend their method to polyanalytic
functions of one variable. We explain our results in detail in the case q = 2 and compute the
ﬁrst two terms of the asymptotic expansion. We supply some hints on how to the approach
applies for bigger values of q. The actual computations become unwieldy and for this reason
they are not presented. Our asymptotic analysis leads to the following blow-up result.
Theorem 5.1. (q = 2) Let Ωbe a domain in C, and suppose Q : Ω→R is C4-smooth with ∆Q > 0
on Ωand
sup
Ω
1
∆Q∆log 1
∆Q < +∞.
Suppose, in addition, that Q is real-analytically smooth in a neighborhood of a point z0 ∈Ω, and
introduce the rescaled coordinates ξ′ := [2m∆Q(z0)]−1/2ξ and η′ := [2m∆Q(z0)]−1/2η. Then there
exists a positive m0 such that, for all m ≥m0, we have
(5.5.1)
1
2m∆Q(z0)|K2,m(z0 + ξ′, z0 + η′)|e−mQ(z0+ξ′)−mQ(z0+η′) = |2 −|ξ −η|2|
π
e−1
2 |ξ−η|2 + O(m−1/2),
where the constant in the error term is uniform in compact subsets of (ξ, η) ∈C2.
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
13
We remark that since the limiting kernel on the right-hand side of (5.5.1) does not depend
on the particular weight Q, we may view the above theorem as a universality result; for more
on universality, see, e.g., [11]. The probabilistic interpretation is that in the large m limit, the
determinantal point process (for a deﬁnition, see [20]) deﬁned by the kernel K2,m obeys local
statistics (after the appropriate local blow-up) given by the kernel π−1(2−|ξ−η|2)e−|ξ−η|2/2. This
local blow-up kernel appeared earlier in our previous paper [16] which was concerned with the
quadratic potential Q(z) = |z|2. In that paper, we analyzed a system of noninteracting fermions
described by the Landau Hamiltonian of Subsection 5.4, so that each of the q ﬁrst Landau
levels was ﬁlled with n particles. As n tends to inﬁnity and the magnetic ﬁeld is rescaled
by m, with m = n + O(1), the particles accumulate on the closed unit disk (which equals the
spectral droplet in this instance) with uniform density, and the Laguerre polynomial kernel
π−1L(1)
q−1(|ξ−η|2)e−|ξ−η|2/2 describes the local blow-up statistics in the limit in this polynomial case
for general values of q. Here, L(α)
r
stands for the generalized Laguerre polynomial of degree r
with parameter α; note that L(1)
1 (x) = 2 −x, which explains the expression in Theorem 5.1.
To be more precise, this system of free fermions is a determinantal point process given by
the reproducing kernels of the spaces
Polq,m,n := span{¯zrzj | 0 ≤r ≤q −1, 0 ≤j ≤n −1} ⊂L2(C, e−2m|z|2).
In later work, we intend to replace the weight e−2m|z|2 by a more general weight e−2mQ(z) and apply
the methods developed here to obtain the asymptotic analysis of the corresponding stochastic
processes. On a more general complex manifold, this should correspond to studying sections
on line bundles ¯L⊗q ⊗L⊗n.
Finally, we suggest that it is probably possible to extend our results to the several complex
variables setting and in a second step, to more general complex manifolds. Moreover, we
would expect that asymptotic expansion results could be obtained for reproducing kernels
associated with diﬀerential operators more general than ¯∂q.
