---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-003-12-results-and-outline-of-the-paper
section_title: "Results and outline of the paper"
section_number: 1.2
pages: 2-4
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
We take as reference law a stable distributionφ of index α∈ (0, 2]. Let (Xn)n∈N be a sequence of
variables that admits a zone of control (this notion will be deﬁned in Deﬁnition 5; this is closely related to
themod-φconvergenceof (Xn)n∈N).AswewillseeinProposition6,thisimpliesthatsomerenormalization
Yn of Xn converges in distribution towardsφ and we are interested in the speed of convergence for this
convergence. More precisely, we are interested in upper bounds for theKolmogorov distance
dKol(Yn,φ ) = sup
a∈R
⏐⏐⏐⏐P[Yn≤a]−
∫ a
−∞
φ(dx)
⏐⏐⏐⏐.
The main theorem of Section 2 (Theorem 20) shows that this distance isO(t−γ−1/α
n ), where γ is a
parameter describing how large our zone of control is. We also obtain as intermediate result estimates for
Mod-φ convergence, II: Estimates on the speed of convergence 3
⏐⏐⏐⏐E[f(Yn)]−
∫
R
f(x)φ(dx)
⏐⏐⏐⏐,
wheref lies in some speciﬁc set of tests functions (Proposition 16). A detailed discussion on the method
of proof of these bounds can be found at the beginning of Section 2.
Section 3 gives some examples of application of the theoretical results of Section 2. The ﬁrst one is a
toy example, while the other ones are new to the best of our knowledge.
• We ﬁrst consider sums of i.i.d. random variables with ﬁnite third moment. In this case, the classical
Berry–Esseen estimate ensures that
dKol(Yn,NR(0, 1))≤ 3 E[|A1|3]
σ3√n ,
see [Ber41] or [Fel71, §XVI.5, Theorem 1]. Our general statement for variables with a zone of conver-
gence gives essentially the same result, only the constant factor is not as good.
• We can extend the Berry–Esseen estimates to the case of independent but non identically distributed
random variables. As an example, we look at the number of zeroesZr of a random analytic series
that fall in a disc of radiusr; it has the same law as a series of independent Bernoulli variables of
parameters r2k, k≥ 1. When the radiusr of the disc goes to1, one has a central limit theorem for
Zr, and the theory of zones of control yields an estimateO((1−r)−1/2) on the Kolmogorov distance.
• We then look at the winding numberϕt of a planar Brownian motion starting at1 (see Section 3.2 for
a precise deﬁnition). This quantity has been proven to converge in the mod-Cauchy sense in [DKN15],
based on the computation of the characteristic function done by Spitzer [Spi58]. The same kind of
argument easily yields the existence of a zone of control and our general result applies: whent goes to
inﬁnity, after renormalization,ϕt converges in distribution towards a Cauchy law and the Kolmogorov
distance in this convergence isO((logt)−1).
• In the third example, we considercompound Poisson laws(see [Sat99, Chapter 1, §4]). These laws
appear in the proof of the Lévy–Khintchine formula for inﬁnitely divisible laws (loc. cit., Chapter 2,
§8, p. 44–45), and we shall be interested in those that approximate the stable distributionsφc,α,β.
Again, establishing the existence of a zone of control is straight-forward and our general result shows
that the speed of convergence isO(n−1/ min(α,1)) (Proposition 23), with an additional log factor if
α = 1 and β⁄= 0 (thus exhibiting an interesting phase transition phenomenon).
• Ratios of Fourier transforms of probability measures appear naturally in the theory of self-decompos-
able laws and of the corresponding Ornstein–Uhlenbeck processes. Thus, any self-decomposable law
φ is the limiting distribution of a Markov process(Ut)t≥0, and whenφ is a stable law, one has mod-φ
convergence of an adequate renormalisation ofUt, with a constant residue. This leads to an estimate
of the speed of convergence which depends onα, on the speed of(Ut)t≥0 and on its starting point
(Proposition 25).
• Finally, logarithms of characteristic polynomials of random matrices in a classical compact Lie group
are mod-Gaussian convergent (see for instance [FMN16, Section 7.5]), and one can compute a zone
of control for this convergence, which yields an estimate of the speed of convergenceO((logn)−3/2).
For unitary groups, one recovers [BHNY08, Proposition 5.2]. This example shows how one can force
the indexv of a zone of control of mod-Gaussian convergence to be equal to3, see Remark 26.
The last two sections concentrate on the case where the reference law is Gaussian (α = 2). In this case,
we show that a suﬃcient condition for having a zone of control is to haveuniform bounds on cumulants
(see Deﬁnition 28 and Lemma 29). This is not surprising since such bounds are known to imply (with
small additional hypotheses) mod-Gaussian convergence [FMN16, Section 5.1]. Combined with our main
result, this gives bounds for the Kolmogorov distance for variables having uniform bounds on cumulants
– see Corollary 30. Note nevertheless that similar results have been given previously by Statulevičius
[Sta66] (see also Saulis and Statulevičius [SS91]). Our Corollary 30 coincides up to a constant factor
