---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-001-11-complex-convergence-and-interpretation-of-the
section_title: "Complex convergence and interpretation of the residue"
section_number: 1.1
pages: 3-5
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
sequence of real-valued random variables (Xn)n∈N, but this time we assume that their
Laplace transforms E[ezXn] are convergent in an open disk of radiusc > 0. In this case,
they are automatically well-deﬁned and holomorphic in a band of the complex plane
Bc ={z∈ C,|Re(z)| < c} (see [LS52, Theorem 6], and [Ess45] for a general survey of
the properties of Laplace and Fourier transforms of probability measures).
Deﬁnition 2. The sequence (Xn)n∈N is said to converge in the complex mod-Gaussian sense
with parameters tn and limiting function ψ if, locally uniformly onBc,
E[ezXn] e− tn z2
2 = ψ(z) (1 + o(1)),
where ψ is a continuous function onBc with ψ(0) = 1. Then, one has in particular convergence
in the sense of Deﬁnition 1, with θ(t) = ψ(it).
In this setting which is more restrictive than before, the residueψ has a natural inter-
pretation as a measure of "breaking of symmetry" when one tries to push the estimates
4 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
of the central limit theorem from the scale √tn to the scale tn. The previously men-
tioned central limit theorem (1) tells us that:
P
[
Xn≥ a
√
tn
]
=
( 1√
2π
∫ ∞
a
e− x2
2 dx
)
(1 + o(1))
for any a∈ R. In the setting of complex mod-Gaussian convergence, this estimate
remains true with a = o(√tn), so that if ε = o(1), then
P [Xn≥ ε tn] =
( 1√
2π
∫ ∞
ε√tn
e− x2
2 dx
)
(1 + o(1)),
= e− tnε2
2
√2πtn ε (1 + o(1)) if 1≫ ε≫ 1√tn
,
where the notation an ≫ bn stands for bn = o(an). Then, at scale tn, the limiting
residue ψ comes into play, with the following estimate that holds without additional
hypotheses than those in Deﬁnition 2:
∀x∈ (0, c), P[Xn≥ xtn] = e− tnx2
2
√2πtn x ψ(x) (1 + o(1)), (2)
the remainder o(1) being uniform when x stays in a compact set of R∗+∩ (0, c). This
estimate of positive large deviations has the following counterpart on the negative side:
∀x∈ (0, c), P[Xn≤− xtn] = e− tnx2
2
√2πtn x ψ(−x) (1 + o(1)).
So for instance, if (Yn)n∈N is a sequence of i.i.d. random variables with convergent
moment generating function, mean 0, variance 1 and third moment E[Y] > 0, then
Xn = 1
n1/3 ∑n
i=1 Yi converges in the complex mod-Gaussian sense with parameters n1/3
and limiting function ψ(z) = exp(E[Y3] z3/6), and therefore for x > 0,
P
[
n
∑
i=1
Yi≥ xn2/3
]
= P
[
N (0, 1)≥ xn1/6
]
exp
( E[Y3] x3
6
)
(1 + o(1)).
Thus, at scale n2/3, the ﬂuctuations of the sum of i.i.d. random variables are no more
Gaussian, and the residue ψ(x) measures this "breaking of symmetry": in the previous
example, it makes moderate deviations on the positive side more likely than moderate
deviations on the negative side, since ψ(x) > 1 > ψ(−x) for x > 0.
Remark. The problem of ﬁnding the normality zone, i.e. the scale up to which the
central limit theorem is valid, is a known problem in the case of i.i.d. random variables
(see e.g. [IL71]). The description of the "symmetry breaking" is new and moreover the
mod-Gaussian framework covers many examples with dependent random variables
(see also [FMN13] for more examples).
Thus, the observation of large deviations of the random variables Xn provides a
ﬁrst probabilistic interpretation of the residue ψ in the deconvolution of a sequence of
characteristic functions of random variables by a sequence of large Gaussian variables.
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS 5
In Section 3, we shall provide another interpretation of ψ, which is inspired by some
classical results from statistical mechanics (cf. [EN78, ENR80]).
