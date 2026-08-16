---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-021-53-fluctuations-of-rows
section_title: "Fluctuations of rows"
section_number: 5.3
pages: 22-23
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
to a Young diagram λ, and by X∞;q the limit probability measure of the Xλ under the q-Plancherel
measures. If f ∈ C 1([−1, 1]) is a continuously diﬀerentiable function on [−1; 1], we deﬁne the rescaled
deviation of f under q-Plancherel measure. It is the random variable Dn,q(f ) obtained by composition
of q-Plancherel measure by the function:
λ ↦→√n (Xλ(f ) − X∞;q(f )) ,
where µ(f ) is a short notation for
∫ 1
−1 f dµ.
In this context, the convergence in law of rescaled power sum s can be reformulated as a convergence
in law of the vector
(
Dn,q(xl)
)
1≤l≤k towards a gaussian vector (Zq;l) with covariance matrix:
k(Zq;l, Zq;m) = X∞;q((l + 1)(m + 1) xlxm) − (l + 1)(m + 1) X∞;q(xl) X∞;q(xm);
= X∞;q
(
(xl+1)′ (xm+1)′)
− X∞;q
(
(xl+1)′)
X∞;q
(
(xm+1)′)
.
Recall that with respect to the C 1-topology, /CA [X] is dense in the space of continuously diﬀerentiable
functions C 1([−1, 1]). By using this density together with the bilinearity of Dn,q and covariance, we
conclude that for any functions f1, f2, . . . , fr ∈ C 1([−1, 1]), the vector of rescaled deviations Dn,q(fi)
converges towards a gaussian vector (Zq;fi )i∈[ [1,r] ]with covariance matrix:
k(Zq;fi , Zq;fj ) = X∞;q ((xfi)′ (xfj )′) − X∞;q ((xfi)′) X∞;q ((xfj)′) .
Proof of Theorem 2. If i ≥ 1, we denote by fi a class C 1 and non-negative function such that fi(x) = 1 on
a vicinity Vi of qi−1 (1 − q) and fi(x) = 0 outside a vicinity Wi ⊃ Vi, cf. ﬁgure 5. We shall also suppose
that the Wi are disjoint open sets; in particular, X∞;q(fi) = qi−1(1 − q). Since f ′
i (qi−1(1 − q)) = 0 ,
(xfi)′(qi−1(1 − q)) = fi(qi−1(1 − q)) = 1 , and as a consequence,
X∞;q((x fi(x))′2) − X∞;q((x fi(x))′)2 = qi−1(1 − q) − q2(i−1)(1 − q)2.
Wi
qi− 1(1 − q)
Figure 5. Graphical representation of the test function fi.
Moreover, fi fj = 0 for all i ⁄= j, and the same holds for fi f ′
j, f ′
i fj or f ′
i f ′
j. Therefore, the covariance
matrix of the corresponding limit gaussian vector (Zq;fi )i≥1 is:
X∞;q ((x fi(x))′ (x fj(x))′) − X∞;q ((x fi(x))′) X∞;q ((x fj(x))′) = −X∞;q ((x fi(x))′) X∞;q ((x fj(x))′) ;
= −(1 − q)2 qi+j−2.
Finally, for n large enough and outside a set of arbitrary small probabilit y, a∗
i (λ)/n is in Vi, a∗
i−1(λ)/n is
in Vi−1 and a∗
i+1(λ)/n is in Vi+1. Thus, with a probability close to 1, the support of Xλ and the support
of fi ⁄= 0 intersect only at a∗
i (λ)/n, and Xλ(fi) = a∗
i (λ)/n. As a consequence,
√
n
(a∗
i (λ)
n − qi−1(1 − q)
)
= √n (Xλ(fi) − X∞;q(fi)) ,
ASYMPTOTICS OF q-PLANCHEREL MEASURES 23
outside a set of arbitrary small probability, and the repart ition functions of these random variables have
the same asymptotic behavior. Theorem 2 follows then from the estimation a∗
i (λ) = λi + O(1). □
