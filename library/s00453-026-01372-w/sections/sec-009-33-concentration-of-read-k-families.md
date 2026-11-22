---
doc_id: s00453-026-01372-w
doc_title: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence"
section_id: sec-009-33-concentration-of-read-k-families
section_title: "Concentration of read-k families"
section_number: 3.3
pages: 10-12
source_pdf: s00453-026-01372-w.pdf
source_sha256: 98b569eff84fb489
toc_source: outline
doc_brief: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence — We study the question of whether submodular functions of random variables satisfying various notions of negative"
---
In this subsection, we illustrate an application of our proof technique to give concen-
tration for a read-k family of supermodular functions. Read-k families arise naturally
in problems such as subgraph counting in random graphs, and can be seen as a comple-
mentary weak dependence notion to that of low-degree polynomials [29]. Our work
gives the ﬁrst concentration results for these problems under negative dependence.
Let’s consider this notion of weak dependence deﬁned in [4]. Let Y1, . . . , Yn be
random variables and assume that they can be factored as functions of random variables
X1, . . . , Xm. We say that Y1, . . . , Yn are a read-k family of X1, . . . , Xm if for each
variable Xi, there are at most k variables among Y1, . . . , Yn that are inﬂuenced by Xi.
Formally, we have the following.
Deﬁnition 4 Let X1, . . . , Xm be random variables. For each j ∈[n], let Pj ⊆[m]
and let f j : {0, 1}Pj →[0, 1] be functions of X Pj . We say that Y j = f j(X Pj ) are a
read-k family if |{ j : i ∈Pj}| ≤k for each i ∈[m] (i.e., each variable Xi inﬂuences
at most k functions).
When X1, . . . , Xm are independent, [4] showed that we have
Pr[n
j=1 f j(X Pj ) ≥(p + ϵ)n] ≤exp(−D(p + ϵ||p) · n/k)
(4)
Pr[n
j=1 f j(X Pj ) ≤(p −ϵ)n] ≤exp(−D(p −ϵ||p) · n/k),
(5)
where p = (1/n) n
j=1 E[Y j] and D(·||·) is the Kullback-Leibler divergence.
Notably, while Gavinsky et al. do not require random variables X1, . . . , Xm to be
Algorithmica (2026) 88 :21
Page 11 of 19
21
binary, as we do in our approach, their model requires Y1, . . . , Yn to be binary. We
will show that Inequality 4 on the upper tail still holds for supermodular functions
f1, . . . , fn. Similarily, Inequality 5, which addresses the lower tail bound, continues
to apply to submodular functions f1, . . . , fn.
Theorem 3.4 Let X1, . . . , Xm be 1-negatively associated random variables and let
X∗
1, . . . , X∗
m be independent random variables with the same respective marginal
distributions as X1, . . . , Xm. Suppose that f j(X Pj ) for j ∈[n] are a read-k fam-
ily, where f j : {0, 1}Pj →[0, 1] are supermodular functions. If we let p0 =
(1/n) n
j=1 E[ f j(X∗
Pj )] denote the averaged expectation when the underlying ran-
dom variables are independent, we have
Pr[n
j=1 f j(X Pj ) ≥(p0 + ϵ)n] ≤exp(−D(p0 + ϵ||p0) · n/k).
Proof Let f (X1, . . . , Xm) = n
j=1 f j(X Pj ) be the quantity of interest, and note that
f is the sum of supermodular functions so it is supermodular as well.
We will follow the standard proof via exponential moments. Let λ > 0; we have
Pr[ f (X1, . . . , Xm) ≥(p0 + ϵ)n] = Pr[exp(λ · f (X1, . . . , Xm)) ≥exp(λ · (p0 + ϵ)n)] (6)
≤E[exp(λ · f (X1, . . . , Xm))]/ exp(λ · (p0 + ϵ)n),
(7)
where the inequality follows by Markov’s. Since f is supermodular, we have by
Corollary 3.2 that
E[exp(λ · f (X1, . . . , Xm))] ≤E[exp(λ · f (X∗
1, . . . , X∗
m))] = E[exp(λ · n
j=1 f j(X∗
Pj ))].
(8)
In the new proof of concentration of read-k families, given in the Appendix, we show
that
E[exp(λ · n
j=1 f j(X∗
Pj ))] ≤
n
j=1 E[exp(λ · f j(X∗
Pj ))k]
	1/k
.
(9)
Combining equations 6–9, we have
Pr[ f (X1, . . . , Xm) ≥(p0+ϵ)n] ≤
n
j=1 E[exp(kλ · f j(X∗
Pj ))/ exp(kλ(p0 + ϵ)n]
	1/k
.
Let λ′ = kλ; since λ > 0 is a parameter we set, we can view λ′ > 0 as a parameter as
well. We will abuse notation and replace λ′ with λ, so we have
Pr[ f (X1, . . . , Xm) ≥(p0+ϵ)n] ≤
n
j=1 E[exp(λ · f j(X∗
Pj ))/ exp(λ(p0 + ϵ)n]
	1/k
,
for any λ > 0. Now, observe that the right hand side of the inequality is the exact same
as in the proof of the standard Chernoff bound under independence, except with an
21
Page 12 of 19
Algorithmica (2026) 88 :21
additional exponent 1/k. As a result, we can follow the original proof of the Chernoff
bound to show that
Pr[n
j=1 f j(X Pj ) ≥(p0 + ϵ)n] ≤exp(−D(p0 + ϵ||p0) · n/k),
which was our desired result.
⊓⊔
Corollary 3.5 Let X1, . . . , Xm be 1-negatively associated random variables. Suppose
that f j(X Pj ) for j ∈[n] are a read-k family, where f j : {0, 1}Pj →[0, 1] are
submodular functions. If we let p0 = (1/n) n
j=1 E[ f j(X∗
Pj )] denote the averaged
expectation when the underlying random variables are independent, we have
Pr[n
j=1 f j(X Pj ) ≤(p0 −ϵ)n] ≤exp(−D(p0 −ϵ||p0) · n/k).
Proof Deﬁne g j := 1 −f j, where g j : {0, 1}Pj →[0, 1] are supermodular. Then
1 −p0 = (1/n) n
j=1 E[g j(X∗
Pj )]. Applying Theorem 3.4, we have:
Pr[n
j=1 g j(X Pj ) ≥(1−(p0 −ϵ))n] ≤(1−p0 +ϵ)n] ≤exp(−D(1−p0 +ϵ||1−p0)·n/k).
The property of Kullback–Leibler divergence D(1 −p||1 −q) = D(p||q) implies
Pr[n
j=1 f j(X Pj ) ≤(p0 −ϵ)n] = Pr[n
j=1 g j(X Pj ) ≥(1 −(p0 −ϵ))n]
≤exp(−D(p0 −ϵ||p0) · n/k),
which concludes the proof.
⊓⊔
