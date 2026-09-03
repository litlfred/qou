---
doc_id: arxiv-1804.10084v1
doc_title: "Concentration of Lipschitz Functions of Negatively Dependent Variables"
section_id: sec-003-3-concentration-under-negative-regression
section_title: "Concentration under negative regression"
section_number: 3
pages: 3-4
source_pdf: 1804.10084v1.pdf
source_sha256: 716da9708f06d930
doc_brief: "Concentration of Lipschitz Functions of Negatively Dependent Variables — We explore the question whether Lipschitz functions of random var iables under various forms of negative correlation satisfy"
---
We provide here what (we claim) is a correct proof of a previously claim ed result [5, Proposition
31], namely a concentration bound for Lipschitz functions of rando m variables under the property
of negative regression. In fact we improve their theorem in the sen se that we do not require the
assumption of monotonicity of f . For simplicity, we focus on the case of 1-Lipschitz functions.
3
Theorem 1. Let X1, . . . , X n be {0, 1} random variables satisfying the condition of negative regr es-
sion. Let f : {0, 1}n → R be a 1-Lipschitz function, and µ = E[f (X1, . . . , X n)]. Then for any
t > 0,
Pr[f (X1, . . . , X n) ≥ µ + t] ≤ e−t2/2n,
Pr[f (X1, . . . , X n) ≤ µ − t] ≤ e−t2/2n.
If f is monotone, then the bound can be improved to e−2t2/n.
We remark that in the case of monotone f , our bound coincides with that of McDiarmid’s
inequality for independent random variables [9], in which case the con stant in the exponent is
known to be tight. In the non-monotone case, it is known that the s ame constant cannot be
achieved [13], but it might be possible to prove a bound of e−t2/n; i.e., our constant could be oﬀ by
a factor of 2.
Negative regression is weaker than stochastic covering, or the st rong Rayleigh property, and
hence qualitatively our bound subsumes that of [13]. In terms of ap plications, it is fair to say
that most of the known examples satisfying negative regression in f act satisfy the strong Rayleigh
property and are hence covered by [13]. Quantitatively speaking, t he constants in the exponent
proved by Pemantle and Peres [13] are somewhat worse than ours, but their bounds are functions
of µ = E[∑ Xi] rather than n, so are not directly comparable to ours.
In terms of techniques, our proof is more elementary than that of [13], which relies on the
(beautiful) theory of stable polynomials. We follow the classical mart ingale paradigm, with one
new twist — an adaptive ordering of the variables.
