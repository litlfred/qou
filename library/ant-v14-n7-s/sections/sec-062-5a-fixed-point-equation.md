---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-062-5a-fixed-point-equation
section_title: "5A. Fixed point equation"
section_number: null
pages: 75-77
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Coleman integration. It amounts to the deﬁnition of p-adic multiple polylogarithms LiKZ
q as Coleman
integrals, in [Furusho 2004; 2007] for N= 1 and in [Yamashita 2010] for any N; we have
φlog(q)/log(p)(LiKZ
q )= LiKZ
q . (5-1)
Restricted to U an, the ﬁxed point equation amounts to the following equations [Jarossay 2019, Propo-
sition 2.1.3], they involve the overconvergent p-adic multiple polylogarithms Li†
p,α[w] [Jarossay 2019,
Deﬁnition 1.2.5], which are overconvergent analytic functions on U an:
Li†
p,α(z)= LiKZ
q (z)(pαe0,( pαeξ)ξ)LiKZ
q
(pα)
(z pα
)(e0,( Ad8(ξ)
p,α
(eξ)ξ))−1, (5-2)
Li†
p,−α(z)= LiKZ
q
(pα)
(z pα
)(e0,( eξ(pα))ξ) LiKZ
q (z)(pαe0, pα(Ad8(ξ pα)
p,−α
(eξ(pα))ξ))−1, (5-3)
where LiKZ
q
(pα)
is the analogue of LiKZ
q on X(pα) equal to the pull-back of X=(P1\{ 0,µ N,∞})/K by
σα whereσ is the Frobenius automorphism of K . When α is a multiple of log(q)/log(p), X(pα)= X
and LiKZ
q
(pα)
= LiKZ
q , and whenα= log(q)/log(p), (5-2), (5-3) are directly equivalent to (5-1).
Notation 5A.1. For any˜α∈ Z∪{±∞}\{ 0}, let Li†
q,˜α= Li†
p,α and Li†
q,−˜α= Li†
p,−α, with pα= q˜α.
The Frobenius on U an is characterized by the couple (Li†
p,α,8 p,α). We already know by Section 2 a
description of8p,α as a function of α. If we combine it with (5 -2), (5-3), we deduce a description of
Li†
p,α as a function of α. This gives a description of the iterated Frobenius on U an as a function of its
number of iterations. We leave the details to the reader. One can also write an analogue for U an of the
notion of contraction mapping at base-points (1, 0) of Deﬁnition 1B.2 and of the fact that the Frobenius
at(1, 0) is a contraction of Lemma 1B.7.
Let us just consider the convergence of the iterated Frobenius towards the ﬁxed point when the number
of iterations tends to∞, in the unit ball B(0, 1).
1742 David Jarossay
Proposition 5A.2. For all z∈ K such that|z|p< 1, we have, for the N3,D-topology,
τ(q−˜α) Li†
q,˜α(z) ˜α→∞−−−→LiKZ
q (z)(e0,( eξ)ξ),
τ(q−˜α) Li†
q,−˜α(z) ˜α→∞−−−→LiKZ
q (z)(e0,( Ad8(ξ)
q,−∞
(eξ))ξ).
Moreover, these convergences are uniform on all the closed disks of center 0 and radiusρ< 1.
Proof.τ(q−˜α) Li†
q,˜α(z) is the product of Li KZ
q (z)(e0,( eξ)ξ) by
τ(q−˜α) LiKZ
p,X(q˜α)
K
(zq˜α
)(e0,( Ad8(ξ)
q,˜α
(eξ))ξ)−1. (5-4)
The coefﬁcient of (5-4) at a word w is of the form,
q−˜α weight(w) ∑
(w1,w2)
∞∑
m=0
hqαm(w1) zq˜αm
(q˜αm)Lζq,α(w2)
where L∈ N∗ andw1,w 2 are in a ﬁnite set depending only on w, determined by the combinatorics of the
composition of noncommutative formal power series. For allm∈ N∗ we have−vp(m)>− log(m)/log(p).
Applying this to the mi in (0-2) we deduce
vp(harq˜αm(w))>− weight(w)˜α log(q)+ log(n)
log(p) .
For all C, C′∈ R+∗, and z∈ K such that|z|p< 1, we have q˜αnvp(z)− C˜α− C′ log(n) ˜α→∞−−−→+∞and
this convergence is uniform with respect to n. Indeed, let n0 be an integer such that for all n> n0, we
have C′ log(n)⩽ 1
2nvp(z); then n0 is independent of˜α and we have, for all n> n0,
q˜αnvp(z)− C˜α− C′ log(n)> q˜αn
2 vp(z)− C˜α.
Because of the bounds of valuations of cyclotomicp-adic multiple zeta values of [Jarossay 2019, Section 4],
the sequence(N3,D(8q,−α))˜α∈N∗ is bounded. Thus, τ(q−˜α) Li†
q,α(z) converges to LiKZ
q (z). Moreover,
we can see that n0 can be chosen independently from z in a closed disk of center 0 and radius ρ< 1.
The proofs of the statements concerning τ(q−˜α) Li†
q,−α(z) are similar. □
Remark 5A.3. The convergence in Proposition 5A.2 does not a priori extend to a uniform convergence
on U an. Indeed, otherwise, in fact, the map LiKZ
q would be rigid analytic on U an. By the main result
of Appendix A of [Jarossay 2019], this would imply that, for any word w, the multiple harmonic sums
functions m↦→ harm(w) restricted to classes of congruences modulo N should be continuous as a function
m∈ N⊂ lim←−−Z/N pl Z. This seems to contradict the results of Section 3C. More generally, we expect
that the lack of regularity of the maps m↦→ harm(w) can be at least partially reﬂected in the mode of
convergence of the sequences Li†
q,˜α[w] whenα→∞ .
Remark 5A.4. One can deduce a result similar to Proposition 5A.2 on the ball B(∞, 1) by applying the
automorphism z↦→ 1/z of P1\{ 0,µ N,∞} and the functoriality ofπ un,crys
1 .
Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values 1743
