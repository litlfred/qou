---
doc_id: ant-v14-n7-s-p02
doc_title: "Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values"
section_id: sec-005-5-iteration-of-the-frobenius-on-p1-s
section_title: "Iteration of the Frobenius on P1 \ S"
section_number: 5
pages: 31-34
source_pdf: ant-v14-n7-s-p02.pdf
source_sha256: fd2121feb180b282
toc_source: inferred
doc_brief: "Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values — 10 sections: Front matter; Introduction; Preliminaries"
---
ξ B(ξ, 1)
In the previous sections, we considered the Frobenius of πun,crys
1
(P1 \ {0, µN, ∞}) at base-points (1, 0)
and the harmonic Frobenius. We now consider the Frobenius of πun,crys
1
(P1 \ {0, µN, ∞}) on the afﬁnoid
subspace U an = P1,an \ S
ξ N=1 B(ξ, 1) of P1,an over K, where B(ξ, 1) is the open ball of center ξ and
of radius 1. As in Section 2, we will have a ﬁxed-point equation (Section 5A) and an iteration equation
(Section 5B). Additionally, we will have a third equation coming from the study of regularized iterated
integrals in [Jarossay 2019, Section 5.3].
5A. Fixed point equation. The ﬁxed point equation of the Frobenius is known thanks to the theory of
Coleman integration. It amounts to the deﬁnition of p-adic multiple polylogarithms LiKZ
q
as Coleman
integrals, in [Furusho 2004; 2007] for N = 1 and in [Yamashita 2010] for any N; we have
φlog(q)/log(p)(LiKZ
q ) = LiKZ
q
.
(5-1)
Restricted to U an, the ﬁxed point equation amounts to the following equations [Jarossay 2019, Propo-
sition 2.1.3], they involve the overconvergent p-adic multiple polylogarithms Li†
p,α[w] [Jarossay 2019,
Deﬁnition 1.2.5], which are overconvergent analytic functions on U an:
Li†
p,α(z) = LiKZ
q (z)(pαe0, (pαeξ)ξ)LiKZ
q
(pα)(z pα)(e0, (Ad8(ξ)
p,α(eξ)ξ))−1,
(5-2)
Li†
p,−α(z) = LiKZ
q
(pα)(z pα)(e0, (eξ(pα))ξ) LiKZ
q (z)(pαe0, pα(Ad8(ξ pα )
p,−α (eξ(pα))ξ))−1,
(5-3)
where LiKZ
q
(pα) is the analogue of LiKZ
q
on X(pα) equal to the pull-back of X = (P1 \ {0, µN, ∞})/K by
σ α where σ is the Frobenius automorphism of K. When α is a multiple of log(q)/log(p), X(pα) = X
and LiKZ
q
(pα) = LiKZ
q , and when α = log(q)/log(p), (5-2), (5-3) are directly equivalent to (5-1).
Notation 5A.1. For any ˜α ∈Z ∪{±∞} \ {0}, let Li†
q,˜α = Li†
p,α and Li†
q,−˜α = Li†
p,−α, with pα = q ˜α.
The Frobenius on U an is characterized by the couple (Li†
p,α, 8p,α). We already know by Section 2 a
description of 8p,α as a function of α. If we combine it with (5-2), (5-3), we deduce a description of
Li†
p,α as a function of α. This gives a description of the iterated Frobenius on U an as a function of its
number of iterations. We leave the details to the reader. One can also write an analogue for U an of the
notion of contraction mapping at base-points (1, 0) of Deﬁnition 1B.2 and of the fact that the Frobenius
at (1, 0) is a contraction of Lemma 1B.7.
Let us just consider the convergence of the iterated Frobenius towards the ﬁxed point when the number
of iterations tends to ∞, in the unit ball B(0, 1).
1742
David Jarossay
Proposition 5A.2. For all z ∈K such that |z|p < 1, we have, for the N3,D-topology,
τ(q−˜α) Li†
q,˜α(z)
˜α→∞
−−−→LiKZ
q (z)(e0, (eξ)ξ),
τ(q−˜α) Li†
q,−˜α(z)
˜α→∞
−−−→LiKZ
q (z)(e0, (Ad8(ξ)
q,−∞(eξ))ξ).
Moreover, these convergences are uniform on all the closed disks of center 0 and radius ρ < 1.
Proof. τ(q−˜α) Li†
q,˜α(z) is the product of LiKZ
q (z)(e0, (eξ)ξ) by
τ(q−˜α) LiKZ
p,X(q ˜α)
K
(zq ˜α)(e0, (Ad8(ξ)
q,˜α(eξ))ξ)−1.
(5-4)
The coefﬁcient of (5-4) at a word w is of the form,
q−˜α weight(w) X
(w1,w2)
∞
X
m=0
hqαm(w1) zq ˜αm
(q ˜αm)L ζq,α(w2)
where L ∈N∗and w1, w2 are in a ﬁnite set depending only on w, determined by the combinatorics of the
composition of noncommutative formal power series. For all m ∈N∗we have −vp(m)⩾−log(m)/log(p).
Applying this to the mi in (0-2) we deduce
vp(harq ˜αm(w)) ⩾−weight(w) ˜α log(q) + log(n)
log(p)
.
For all C, C′ ∈R+∗, and z ∈K such that |z|p < 1, we have q ˜αnvp(z) −C ˜α −C′ log(n)
˜α→∞
−−−→+∞and
this convergence is uniform with respect to n. Indeed, let n0 be an integer such that for all n ⩾n0, we
have C′ log(n) ⩽1
2nvp(z); then n0 is independent of ˜α and we have, for all n ⩾n0,
q ˜αnvp(z) −C ˜α −C′ log(n) ⩾q ˜αn
2 vp(z) −C ˜α.
Because of the bounds of valuations of cyclotomic p-adic multiple zeta values of [Jarossay 2019, Section 4],
the sequence (N3,D(8q,−α))˜α∈N∗is bounded. Thus, τ(q−˜α) Li†
q,α(z) converges to LiKZ
q (z). Moreover,
we can see that n0 can be chosen independently from z in a closed disk of center 0 and radius ρ < 1.
The proofs of the statements concerning τ(q−˜α) Li†
q,−α(z) are similar.
□
Remark 5A.3. The convergence in Proposition 5A.2 does not a priori extend to a uniform convergence
on U an. Indeed, otherwise, in fact, the map LiKZ
q
would be rigid analytic on U an. By the main result
of Appendix A of [Jarossay 2019], this would imply that, for any word w, the multiple harmonic sums
functions m 7→harm(w) restricted to classes of congruences modulo N should be continuous as a function
m ∈N ⊂lim
←−−Z/NplZ. This seems to contradict the results of Section 3C. More generally, we expect
that the lack of regularity of the maps m 7→harm(w) can be at least partially reﬂected in the mode of
convergence of the sequences Li†
q,˜α[w] when α →∞.
Remark 5A.4. One can deduce a result similar to Proposition 5A.2 on the ball B(∞, 1) by applying the
automorphism z 7→1/z of P1 \ {0, µN, ∞} and the functoriality of πun,crys
1
.
Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values 1743
5B. Iteration equation. We now write an equation for the iteration of the Frobenius on the subspace
P1,an \ S
ξ∈µN(K) B(ξ, 1). We restrict the statement to positive numbers of iterations for simplicity, but
a similar result holds for negative numbers of iterations. If f (z) = P∞
m=0 cmzm is a power series with
coefﬁcients in K, let f (pα)(z) = P∞
m=0 σ α(cm)zm where σ is the Frobenius automorphism of K.
Proposition 5B.1. For any, α0, α ∈N∗with α0 dividing α, we have
Li†
p,α(e0, (eξ)ξ) = Li†
p,α0(e0, (eξ)ξ)Li†
p,α0
(pα0)(e0, (Ad8(ξ)
p,α0(eξ)ξ) · · · Li†
p,α0
(pα/α0−1)(e0, (Ad8α−1
p,α0
(ξ)(eξ)ξ)).
Proof. The crystalline Frobenius of πun
1 (P1 \ {0, µN, ∞}), restricted to the rigid analytic sections on
P1,an \ S
ξ∈µN(K) B(ξ, 1), is given, with the conventions of [Jarossay 2019], by the formula
τ(pα)φα : f (e0, (eξ)ξ)(z) 7→Li†
p,α(e0, (eξ)ξ)(z) × f (pα)(z pα)(e0, Ad8(ξ)
p,α(eξ)ξ).
(5-5)
This implies the result.
□
5C. Another iteration equation via regularized iterated integrals. The computation of overconvergent
p-adic multiple polylogarithms in [Jarossay 2019], which was centered around a notion of regularization
of iterated integrals, gives us another point of view on how they depend on α. Below, for a power series
S ∈K[[z]], we denote by S[zm] the coefﬁcient of zm in S for all m ∈N. Again we restrict the statement
to positive numbers of iteration of the Frobenius for simplicity, but a similar statement holds for negative
number of iterations.
Proposition 5C.1. For any word w on e0∪µN and any m0 ∈N, there exists a sequence
(c(l,ξ,n)[w](m0))
l∈N
ξ∈µN(K)
n∈N
of elements of K such that, for any ˜α ∈N such that q ˜α > m0 and m ∈N∗satisfying |m −m0|p ⩽q−˜α, we
have
Li†
q,˜α[w][zm] =
∞
X
n=0
(q ˜α)n
X
l∈N
X
ξ
c(l,ξ,n)[w](m0)ξ −m(m −m0)l

.
Proof. In [Jarossay 2019, Section 3], we have deﬁned a notion of regularized iterated integrals attached
to any sequence of differential forms among pα dz
z , pαdz
z−ξ , ξ ∈µN(K),
d(z pα )
z pα −ξ pα , ξ ∈µN(K). We have
computed these regularized iterated integrals by induction on the depth, and this gives us information
on how they depend on α. Namely, each regularized iterated integral is a rigid analytic function on
P1,an\S
ξ∈µN(K) B(ξ, 1) which has a power series expansion P∞
m=0 cmzm satisfying the following property:
for any m0 ∈{0, . . . , pα −1}, there exists a sequence (c(l,ξ)(m0))
l∈N
ξ∈µN(K) of elements of K such that, for
all m ∈N with |m −m0|p ⩽p−α, we have cm = P∞
l=0
P
ξ c(l,ξ)(m0)ξ −m(m −m0)l.
In [Jarossay 2019, Appendix B], we have showed that the numbers c(l,ξ)(m0) have an expression
as certain sums of series involving multiple harmonic sums, and particularly prime weighted multiple
harmonic sums.
1744
David Jarossay
In [Jarossay 2019, Section 4], we have showed an expression of each Li†
p,α[w] as a linear combination
of regularized p-adic iterated integrals over the ring of p-adic cyclotomic multiple zeta values ζp,α(w′).
Combining these facts with the results of Sections 1 and 2 on how ζq,˜α and harq ˜α depend on ˜α, we
deduce the result.
□
