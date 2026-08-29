---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-000-12-theoretical-results
section_title: "Theoretical results"
section_number: 1.2
pages: 5-7
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
φ convergence as described in Deﬁnition 1.1 is suitable to obtainprecise large and mod-
erate deviation results for the sequence (Xn)n∈N (throughout the paper, we call precise
deviation result an equivalent of the deviation probability itself and not on its loga-
rithm). Namely, our results are the following.
• We give equivalents for the quantity P[Xn≥ tnx], where x is a ﬁxed positive
real number (see Theorem 3.4 for a lattice distribution φ and Theorem 4.3 for a
non-lattice distribution). This can be viewed as an analog (or an extension, see
Section 4.5.2) of Bahadur-Rao theorem [BR60].
• We also consider probabilities of the kind P[Xn∈ tnB] where B is a Borelian
set, and we give upper and lower bounds on this probability which coincide at
ﬁrst order for a nice Borelian set B, see Theorem 6.4. This result is an analog
of Ellis-Gärtner theorem [DZ98, Theorem 2.3.6] (see also the original papers
[Gär77, Ell84]): we have stronger hypotheses than in Ellis-Gärtner theorem, but
also a more precise conclusion (the bounds involve the probability itself, not its
logarithm).
• Besides, we give an equivalent for the probability P[Xn− E[Xn]≥ sntn], where
sn = o(1), covering all intermediate scales between central limit theorem and
deviations of order tn (Theorem 3.9 in the lattice case, and Theorem 4.8 in the
non-lattice case).
We also address the question of normality zone, i.e. the scale up to which the Gaussian
approximation (coming from the central limit theorem) for the tail of the distribution
6 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
of Xn is valid. In particular, our methods provide us with a systematic way to detect it
and also explains how this approximation breaks at the edge of this zone; see Section
5. The problem of detecting the normality zone for sums of i.i.d. random variables has
received some attention in the literature on limit theorems (origninally in [Cra38], see
also [IL71]). Our framework enables an extension of such results, going beyond the
setting of independent random variables:
• we cover more situations, e.g. sums of dependent random variables with a
sparse dependency graph, or integer valued random variables, such as random
additive functions, satisfying mod-Poisson convergence;
• we describe the correction to the normal approximation needed at the edge of
the normality zone.
An interesting fact in our deviation results is the appearance of the limiting function ψ
in deviations at scale tn. This means that, at smaller scales, a sequence Xn converging
mod-φ behaves exactly as a sum of tn i.i.d. variables with distribution φ. However,
at scale tn, this is not true any more and the limiting function ψ gives us exactly the
correcting factor.
In particular, in the case of mod-Gaussian convergence, the scale tn is the ﬁrst scale
where the equivalent given by the central limit theorem is not valid anymore. In this
case, one often observes a symmetry breaking phenomenon which is explained by the
appearance of function ψ; see Section 4.4.
A special case of mod-Gaussian convergence is the case where (1) is proved using
bounds on the cumulants of Xn — see Section 5.1. This case is particularly interesting
as:
• it contains a large class of examples, see below in Section 1.3;
• in this setting, one can obtain deviation results at a scale larger thattn (typically,
o((tn)5/4), see Proposition 5.2).
The arguments involved in the proofs of our deviation results are standard, but they
nonetheless need to be carefully adapted to the framework of Deﬁnition 1.1: elemen-
tary complex analysis, the method of change of probability measure or tilting due to
Cramér, or adaptations of Berry-Esseen type inequalities with smoothing techniques.
Remark 1.2. We should here mention the work of Hwang [Hwa96], with some similari-
ties with ours. Hwang works with hypotheses similar to Deﬁnition 1.1, except that the
convergence takes place uniformly on all compact sets contained in a given disk cen-
tered at the origin (while we assume convergence in a strip; thus this is weaker than
our hypothesis, see Remark 4.18 for a discussion on this point). Under this hypothe-
sis (and an hypothesis of the convergence speed), Hwang obtains an equivalent of the
probability P[Xn− E[Xn]≥ sntn] with sn = o(1), and even gives some asymptotic
expansion of this probability. However, Hwang does not give any deviation result at
the scale tn and hence, none of his results show the role of ψ in deviation probabilities.
Besides, he has no results in the multi-dimensional setting.
MOD-φ CONVERGENCE, I 7
