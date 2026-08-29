---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-002-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
1.1 Mod-φ convergence
Let (Xn)n∈N be a sequence of real-valued random variables. In many situations, there exists a scale
sn and a limiting lawφ which is inﬁnitely divisible, such that(Xn/sn)n∈N converges in law towardsφ.
For instance, in the classical central limit theorem, ifXn =∑n
i=1Ai is a sum of centered i.i.d. random
variables with E[(A1)2]<∞, then
sn =
√
n E[(A1)2]
and the limit is the standard Gaussian distributionNR(0, 1). In [JKN11] and the subsequent papers
[DKN15, FMN16], the notion of mod-φ convergence was developed in order to get quantitative estimates
on the convergenceXn
sn
⇀φ (throughout the paper,⇀ denotes convergence in distribution).
Deﬁnition 1.Letφ be an inﬁnitely divisible probability measure, andD⊂ C be a subset of the complex
plane, which we assume to contain0. We assume that the Laplace transform ofφ is well deﬁned overD,
with Lévy exponentη:
∀z∈D,
∫
R
ezxφ(dx) = eη(z).
We then say that (Xn)n∈N converges mod-φ over D, with parameters (tn)n∈N and limiting function
ψ :D→ C, iftn→ +∞ and if, locally uniformly onD,
1
arXiv:1705.10485v2  [math.PR]  20 Feb 2018
2 Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali
lim
n→∞
E[ezXn] e−tnη(z) =ψ(z).
If D = iR, we shall just speak of mod-φ convergence; it is then convenient to use the notation
θn(ξ) = E[eiξXn] e−tnη(iξ);
θ(ξ) =ψ(iξ),
so that mod-φ convergence corresponds tolimn→∞θn(ξ) =θ(ξ) (uniformly forξ in compact subsets ofR).
When nothing is speciﬁed, in this paper, we implicitly consider thatD = iR. WhenD = C we shall speak
of complex mod-φ convergence. In some situations, it is also appropriate to study mod-φ convergence on
a band R× i[−b,b ], or [−c,c ]× iR (see [FMN16, MN15]).
Intuitively, a sequence of random variables (Xn)n∈N converges mod-φ if it can be seen as a large
renormalization of the inﬁnitely divisible lawφ, plus some residue which is asymptotically encoded in the
Fourier or Laplace sense by the limiting functionψ. Then,φ will typically be:
1. in the case of lattice-valued distributions, a Poisson law or a compound Poisson law (cf. [BKN09,
KN10, FMN16, CDMN15]);
2. or, astable distribution, for instance a Gaussian law.
In this paper, we shall only be interested in the second case. Background on stable distributions is given
at the end of this introduction (Section 1.3). In particular we will see that, ifφ is a stable distribution,
then the mod-φ convergence ofXn implies the convergence in distribution of a renormalized versionYn
of Xn to φ (Proposition 3).
We believe that mod-φ is a kind of universality class behind the central limit theorem (or its stable
version) in the following sense. For many sequences(Xn)n∈N of random variables that are proven to be
asymptotically normal (or converging to a stable distribution), it is possible to prove mod-φ convergence;
we refer to our monograph [FMN16] or Sections 3-5 below for such examples. These estimates on the
Laplace transform/characteristic function can then be used to derive in an automatic way somecom-
panion theorems, reﬁning the central limit theorem. In [FMN16], we discuss in details the question of
moderate/large deviation estimates and of ﬁnding thenormality zone.
In the present paper, we shall be interested in the speed of convergence towards the Gaussian (or more
generally the stable) distribution of the appropriate renormalizationYn ofXn. To obtain sharp bounds on
this speed of convergence, we do not work with mod-φ convergence, but we introduce the notion ofzone
of controlfor the renormalized characteristic functionθn(ξ). In many examples, such a zone of control can
be obtained by essentially the same arguments used to prove mod-φ convergence, and in most examples,
mod-φ convergence actually holds.
