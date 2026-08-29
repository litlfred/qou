---
doc_id: arxiv-1009.4034v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2 PIERRE-LOÏC MÉLIOT"
section_id: sec-001-4-gaussian-concentration-of-measures-on-partitio
section_title: "Gaussian concentration of measures on partitions"
section_number: 4
pages: 12-13
source_pdf: 1009.4034v1.pdf
source_sha256: 8f8d6d786b60c279
doc_brief: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2 PIERRE-LOÏC MÉLIOT — In this article, we show that Kerov’s central limit theorem related to the ﬂuctuations of Young"
---
To establish the gaussian concentration of probability measures on partitions coming from reducible
representationsofsymmetricgroups, P.Śniadyhasdevelopedin[Ś06]atheoryofcumulantsofobservables
that works in a very general setting, and in particular for Schur-Weyl measures. IfX1,...,X r are real
or complex random variables, we recall that thejoint cumulant of X1,...,X r is
k(X1,...,X r) = ∂r
∂t1··· ∂tr
⏐⏐⏐⏐
t1=t2=···=tr=0
log E [exp(t1X1 +··· +trXr)].
In particular, gaussian vectors are characterized by the vanishing of joint cumulants of orderr≥ 3, and
the ﬁrst and second joint cumulants give the expectation of the gaussian vector and its covariance matrix.
That said, ifa1,...,a r commute in the group algebraC Sn, and ifP is a probability measure onPn, then
one can consider theai’s as commutative random variables by setting
ai =ai(λ) =χλ(ai)
with λ picked randomly according toP ; as a consequence, the joint cumulantk(a1,...,a r) makes sense.
On the other hand, we have seen that observables of diagrams may also be considered as random variables,
and besides, any observable can be interpreted as an element of the center of the group algebraC Sn, see
[Ś06, §2.1]; so, the joint cumulant of observables of diagrams also makes sense. Then, the major result of
[Ś06] is the following:
Theorem 6 (Sniady’s theory of cumulants of observables). Let (P n)n∈N be a family a probability mea-
sures on the setsPn of integer partitions, and let us denote by(E n)n∈N and (kn)n∈N the corresponding
expectations and joint cumulants. The following assertions are equivalent:
(1) For all positive integersl1,...,l r,
kn(Σl1,...,Σ lr)n−l1 +···+lr−r+2
2 =O(1).
(2) For all integersl1,...,l r≥ 2,
kn(Rl1,...,R lr)n−l1 +···+lr−2r+2
2 =O(1).
(3) If σl1,...,σ lr are disjoint cycles of respective lengthsl1,...,l r, then
kn(σl1,...,σ lr)n
l1 +···+lr +r−2
2 =O(1).
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES 13
Moreover, if these assertions hold, then the following limits are equal (assuming that they exist):
cl+1 = lim
n→∞
E n[Σl]n−l+1
2 = lim
n→∞
E n[Rl+1]n−l+1
2 = lim
n→∞
E n[σl]n
l−1
2
vl+1,m+1 = lim
n→∞
kn(Σl,Σm)n−l+m
2 = lim
n→∞
kn(Rl+1,Rm+1)n−l+m
2
= lim
n→∞
kn(σl,σm)n
l+m
2 −lmcl+1cm+1 +
∑
l=a1+···+ar
m=b1+···+br
lm
r ca1+b1··· car+br
In this setting, the random processes(
n−l
2
(
Rl+1− E n[Rl+1]
))
l≥1
and
(
n−l
2
(
Σl− E n[Σl]
))
l≥1
converge in ﬁnite-dimensional laws towards a gaussian process whose covariance matrix is(vl+1,m+1)l,m≥1.
Under a Schur-Weyl measureSWn,α,c with parametersα = 1/2 andc> 0, the expectation of a permu-
tation of cycle typeµ is SWn,α,c[σµ] =N𝓁(µ)−|µ|≃c|µ|−𝓁(µ)n
𝓁(µ)−|µ|
2 , and this expression is multiplicative
with respect to the lengths of the cycles ofσµ. Consequently, given disjoint cycles of lengthsl1,...,l r,
one has:
kn(σl1,...,σ lr) =
{
N1−l1 if r = 1,
0 otherwise.
From this, one deduces that Schur-Weyl measures with parametersα = 1/2 and c > 0 satisfy the
hypotheses of Theorem 6, and the limit of the random process(
Xl = Σl
n
l
2
−cl−1n
1
2
)
l≥2
is a centered gaussian process with covariance matrix
vl+1,m+1 = 0−lmcl+m−2 +
∑
r≥1
∑
l=a1+···+ar
m=b1+···+br
lm
r cl+m−2r =
∑
r≥2
(l
r
)(m
r
)
rcl+m−2r,
see [Ś06, Example 6]. In particular, whenc = 0, the random variables√nχλ(σl) converge in ﬁnite-
dimensional laws towards independent normal variables of variancel; this is a form of Kerov’s central
limit theorem. As we shall see in §6, the extension of Kerov’s theorem to the case of Schur-Weyl measures
stems from a very natural idea; namely, one wanted to produceindependent gaussian variables from
the ﬂuctuationsΣln−l
2−cl−1n
1
2 when c is not equal to0 and the ﬂuctuations are not asymptotically
independent. The obvious way to do this was to perform a Gram-Schmidt orthogonalisation in the
gaussian space of the limiting process, and we discovered that the orthogonalized basis is related to
translated versions of the Chebyshev polynomials of the second kind.
