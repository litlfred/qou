---
doc_id: s00453-026-01372-w
doc_title: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence"
section_id: sec-008-32-proof-of-submodular-concentration
section_title: "Proof of Submodular Concentration"
section_number: 3.2
pages: 7-10
source_pdf: s00453-026-01372-w.pdf
source_sha256: 98b569eff84fb489
toc_source: outline
doc_brief: "Concentration of Submodular Functions and Read-k Families Under Negative Dependence — We study the question of whether submodular functions of random variables satisfying various notions of negative"
---
We will now prove our main result. As mentioned in the introduction, our proof is
based on the standard technique of bounding the exponential moments, which can be
enhanced using the p-th moment method. The following lemma contains our main
technical contribution, which implies that the exponential moments of f (X1, . . . , Xn)
under 1-negative association are dominated by that under independence. Our results
will follow easily afterwards.
Lemma 3.1 Let X1, . . . , Xn be 1-negatively associated random variables and let
X∗
1, . . . , X∗
n be independent random variables with the same marginal distributions.
Also let g be a supermodular function. Then
E[g(X1, . . . , Xn)] ≤E[g(X∗
1, . . . , X∗
n)].
21
Page 8 of 19
Algorithmica (2026) 88 :21
Proof Observe that in order to prove the lemma, it sufﬁces to prove
E[g(X1, . . . , Xi, . . . , Xn)] ≤E[g(X1, . . . , X∗
i , . . . , Xm)],
(1)
since we can iteratively apply the above inequality to each Xi (note that we can do
this because independent variables are also negatively associated). For simplicity of
notation and without loss of generality, we will prove the inequality for i = 1.
By considering the cases of X1 = 0 and X1 = 1 separately, we have
g(X1, . . . , Xn) = X1 · g(1, X2, . . . , Xn)) + (1 −X1) · g(0, X2, . . . , Xn),
where the equality holds pointwise on the underlying probability space. Via simple
algebraic manipulations, we can rewrite the right hand side as
X1 · [g(1, X2, . . . , Xn) −g(0, X2, . . . , Xn)] + g(0, X2, . . . , Xn).
Taking expectations, we now have that E[g(X1, . . . , Xn)] can be written as
E

X1 · [g(1, X2, . . . , Xn) −g(0, X2, . . . , Xn)]

+ E

g(0, X2, . . . , Xn)

(2)
Observe that X1 is clearly an increasing function of X1, and

g(1, X2, . . . , Xn) −
g(0, X2, . . . , Xn)

is an increasing function of X2, . . . , Xn by supermodularity of g.
Therefore, by 1-negative association, we have that the ﬁrst term is upper bounded by
E[X1] · E[g(1, X2, . . . , Xn)) −g(0, X2, . . . , Xn)].
Consequently, the entire expression in (2) is upper bounded by
E[X1] · E[g(1, X2, . . . , Xn) −g(0, X2, . . . , Xn)] + E[g(0, X2, . . . , Xn)].
Since X1 and X∗
1 have the same marginal distributions, the above is exactly equal to
E[X∗
1] · E[g(1, X2, . . . , Xn) −g(0, X2, . . . , Xn)] + E[g(0, X2, . . . , Xn)].
And since X∗
1 is independent with X2, . . . , Xn by assumption, the above is equal to
E[X∗
1 · g(1, X2, . . . , Xn) −g(0, X2, . . . , Xn)] + E[g(0, X2, . . . , Xn)].
In particular, observe that this is in the exact same form as Equation 2, except with X1
replaced with X∗
1. Note that when we transformed the left-hand side of Equation 1 to
Equation 2, we never used any properties of the random variables X1, . . . , Xn other
than the fact that they take values in {0, 1}. As a result, we can reverse the direction
of all of the equalities to show that the above expression is equal to
E[g(X∗
1, X2, . . . , Xn)],
which completes the proof of the lemma.
⊓⊔
Algorithmica (2026) 88 :21
Page 9 of 19
21
Corollary 3.2 Let X1, . . . , Xn be 1-negatively associated random variables and let
X∗
1, . . . , X∗
n be independent random variables with the same marginal distributions.
• If f is a supermodular non-increasing function and λ > 0, we have E[exp(λ
f (X1, . . . , Xn))] ≤E[exp(λ f (X∗
1, . . . , X∗
n))].
• If f is a submodular non-decreasing function and λ < 0, we have E[exp(λ
f (X1, . . . , Xn))] ≤E[exp(λ f (X∗
1, . . . , X∗
n))].
Proof This follows from the fact that the composition of a non-decreasing convex
function with a non-increasing supermodular function is supermodular, which allows
us to apply Lemma 3.1. The second claim follows by observing that f is submodular
if and only if −f is supermodular.
⊓⊔
Now, we will complete the proof of our main result. Combining the theorem below
with Claims A.4 and A.5 immediately gives a proof of Theorem 1.1. Here, our proof
will rely heavily on the proof of the Chernoff bound for submodular functions under
independence given in Chekuri et al. [2].
Theorem 3.3 Let X1, . . . , Xn be binary random variables with mean x1, . . . , xn satis-
fying 1-negative association. Let f be a non-negative monotone submodular function
with marginal values in [0, 1] and let F be the multilinear extension of f . If we let,
μ0 = F(x1, . . . , xn), then for any δ ∈(0, 1) we have:
Pr[ f (X1, . . . , Xn) ≤(1 −δ) · μ0] ≤exp(−μ0δ2/2).
Proof Let X∗
1, . . . , X∗
n be independent random variables with the same respective
marginals as X1, . . . , Xn and let λ < 0 be a parameter to be set later. Let us decompose
f (X∗
1, . . . , X∗
n) = n
i=1 Y ∗
i , where
Y ∗
i = f (X∗
1, . . . , X∗
i , 0, . . . , 0) −f (X∗
1, . . . , X∗
i−1, 0, . . . , 0).
Let us denote E[Y ∗
i ] = ωi and μ0 = n
i=1 ωi = E[ f (X∗
1, . . . , X∗
n)]. By the convexity
of the exponential and the fact that Y ∗
i ∈[0, 1], we have that
E[exp(λ·Y ∗
i )] ≤ωi ·exp(λ)+(1−ωi) = 1+[exp(λ)−1]·ωi ≤exp[(exp(λ)−1)·ωi].
Combining the above with Lemma C.1 from [2], we have that
E[exp(λ · f (X∗
1, . . . , X∗
n)] = E[exp(λ · n
i=1 Y ∗
i )] ≤n
i=1 E[exp(λ · Y ∗
i )]
≤exp[(exp(λ) −1) · μ0].
(3)
21
Page 10 of 19
Algorithmica (2026) 88 :21
Now, we can follow the proof of the standard Chernoff bound:
Pr[ f (X1, . . . , Xn) ≤(1 −δ) · μ0] = Pr[exp(λ · f (X1, . . . , Xn)) ≥exp(λ(1 −δ) · μ0)]
≤E[exp(λ · f (X1, . . . , Xn))]
exp(λ(1 −δ) · μ0)
≤E[exp(λ · f (X∗
1, . . . , X∗n))]
exp(λ(1 −δ) · μ0)
≤exp[(exp(λ) −1) · μ0]
exp(λ(1 −δ) · μ0)
The ﬁrst equality follows since exp(λ · x) is a monotone function, the ﬁrst inequality
follows by Markov’s inequality, the second inequality follows by Corollary 3.2, and
the ﬁnal inequality follows Equation 3.
Finally, we can choose λ such that exp(λ) = 1 −δ, which gives
Pr[ f (X1, . . . , Xn) ≥(1 −δ)μ0] ≤
exp(−δμ0)
(1 −δ)(1−δ)μ0 ≤exp(−μ0 · δ2/2),
where we used (1 −δ)1−δ ≤exp(−δ + δ2/2) for δ ∈(0, 1] in the ﬁnal inequality. ⊓⊔
