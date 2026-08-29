---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-008-21-the-notion-of-zone-of-control
section_title: "The notion of zone of control"
section_number: 2.1
pages: 6-8
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
the speed of convergence in the resulting central limit theorem. More precisely, we take as reference
law a stable distributionφc,α,β and a sequence(Xn)n∈N that admits a zone of control (with respect to
φc,α,β). As for mod-φc,α,β convergent sequences, it is easy to prove that in this framework, an appropriate
renormalization Yn of Xn converges in distribution towardsφc,α,β (see Proposition 6 below).
If Y has distributionφc,α,β, we then want to estimate
dKol(Yn,Y ) = sup
s∈R
|P[Yn≤s]− P[Y ≤s]|. (1)
To do this, we follow a strategy proposed by Tao (see [Tao12, Section 2.2]) in the case of sums of
i.i.d. random variables with ﬁnite third moment. The right-hand side of (1) can be rewritten as
sup
f∈F
|E[f(Yn)]− E[f(Y )]|,
whereF is the class of measurable functionsy↦→ 1y≤s. Therefore, it is natural to approach the problem
of speed of convergence by looking at general estimates on test functions. The basic idea is then to use
the Parseval formula to compute the diﬀerenceE[f(Yn)]−E[f(Y )], since we have estimates on the Fourier
transforms ofYn and Y. A diﬃculty comes from the fact that the functionsy↦→ 1y≤s are not smooth,
and in particular, their Fourier transforms are only deﬁned in the sense of distributions. This caveat is
dealt with by standard techniques of harmonic analysis (Sections 2.2 to 2.4): namely, we shall work in a
space of distributions instead of functions, and use an adequate smoothing kernel in order to be able to
work with compactly supported Fourier transforms. Section 2.5 gathers all these tools to give an upper
bound for (1). This is the main result of this section and can be found in Theorem 20.
Remark 4.An alternative way to get an upper bound for (1) from estimates on characteristic functions
is to use the following inequality due to Berry (see [Ber41] or [Fel71, Lemma XVI.3.2]). LetX and Y
be random variables with characteristic functionsf∗(ζ) and g∗(ζ). Then, provided thatY has a density
bounded bym, we have, for anys∈ R,
|P[X≤s]− P[Y ≤s]|≤ 1
π
∫ T
−T
⏐⏐⏐⏐
f∗(ζ)−g∗(ζ)
ζ
⏐⏐⏐⏐ dζ + 24m
πT .
Mod-φ convergence, II: Estimates on the speed of convergence 7
Using this inequality in our context should lead to similar estimates as the ones we obtain, possibly with
diﬀerent constants. The proof we use here however has the advantage of being more self-contained, and
to provide estimates for test functions as intermediate results.
2.1 The notion of zone of control
Deﬁnition 5.Let (Xn)n∈N be a sequence of real random variables,φc,α,β a reference stable law, and
(tn)n∈N a sequence growing to inﬁnity. Consider the following assertions:
(Z1) Fixv >0, w >0 and γ∈ R. There exists a zone[−K(tn)γ,K (tn)γ] such that, for allξ in this zone,
if θn(ξ) = E[eiξXn] e−tnηc,α,β(iξ), then
|θn(ξ)− 1|≤ K1|ξ|v exp(K2|ξ|w)
for some positive constantsK1 and K2 that are independent ofn.
(Z2) One has
α≤w ; − 1
α≤γ≤ 1
w−α ; 0 <K ≤
( cα
2K2
) 1
w−α
.
Notice that (Z2) can always be forced by increasingw, and then decreasingK and γ in the bounds of
Condition (Z1). If Conditions (Z1) and (Z2) are satisﬁed, then we say that we have azone of control
[−K(tn)γ,K (tn)γ] with index (v,w ).
Note that although the deﬁnition of zone of control depends on the reference lawφc,α,β, the latter does
not appear in the terminology (throughout the paper, it is considered ﬁxed).
Proposition 6.Let (Xn)n∈N be a sequence of random variables,φc,α,β a reference stable law,Y with dis-
tributionφc,α,β andYn as in Proposition 3. Assume that(Xn)n∈N has a zone of control[−K(tn)γ,K (tn)γ]
with index (v,w ). Ifγ >− 1
α, then one has the convergence in lawYn ⇀Y .
Proof. Condition (Z1) implies that, ifYn is the renormalization ofXn and Y ∼φc,α,β, then for ﬁxedξ,
⏐⏐⏐⏐
E[eiξYn]
E[eiξY ] − 1
⏐⏐⏐⏐ =
⏐⏐⏐⏐θn
( ξ
(tn)1/α
)
− 1
⏐⏐⏐⏐≤ K1|ξ|v
(tn)v/α exp
(K2|ξ|w
(tn)w/α
)
for tn large enough, and the right-hand side goes to0. This proves the convergence in lawYn ⇀Y . ⊓ ⊔
The goal of the next few sections will be to get some speed of convergence estimates for this convergence
in distribution.
Remark 7.In the deﬁnition of zone of control, we do not assume the mod-φc,α,β convergence of the
sequence (Xn)n∈N with parameters (tn)n∈N and limit limn→∞θn(ξ) = θ(ξ). However, in almost all the
examples considered, we shall indeed have (complex) mod-φ convergence (convergence of the residuesθn),
with the same parameterstn as for the notion of zone of control. We shall then speak ofmod-φ convergence
with a zone of convergence[−K(tn)γ,K (tn)γ] and with index of control(v,w ). Mod-φ convergence implies
other probabilistic results than estimates of Berry–Esseen type: central limit theorem with a large range
of normality, moderate deviations (cf. [FMN16]), local limit theorem ([DKN15]),etc.
Remark 8.If one has mod-φc,α,β convergence of (Xn)n∈N, then there is at least a zone of convergence
[−K,K ] of index (v,w ) = (0, 0), withγ = 0; indeed, the residuesθn(ξ) stay locally bounded under this
hypothesis. Thus, Deﬁnition 5 is an extension of this statement. However, we allow in the deﬁnition the
exponent γ to be negative (but not smaller than− 1
α). Indeed, in the computation of Berry–Esseen type
bounds, we shall sometimes need to work with smaller zones than the one given by mod-φ convergence,
see the hypotheses of Theorem 20, and Sections 3.3 and 3.4 for examples.
