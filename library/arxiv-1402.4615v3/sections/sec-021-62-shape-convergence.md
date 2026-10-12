---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-021-62-shape-convergence
section_title: "Shape convergence"
section_number: 6.2
pages: 40-41
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.96
---
In the previous Section, we proved that evaluations of polynomial functions at $D_{1/\sqrt{n}} \big(A_\alpha(\lambda_{(n)})\big)$ converge towards the evaluation at $\Omega$. Ivanov and Olshanski has established that, if one can prove that the support of these renormalized Young diagrams lies in some compact, this would imply the uniform convergence, that is Theorem [\[theo:RYD-limit\]](#theo:RYD-limit){reference-type="ref" reference="theo:RYD-limit"}.

The following technical lemma, proved by Fulman [@FulmanFluctuationChA2 Lemma 6.6] will allow us to conclude:

::: lemma
[]{#lem:FiniteSupport label="lem:FiniteSupport"} Suppose that $\alpha > 0$. Then

1.  $$\mathbb{P}_n^{(\alpha)}\left(\lambda_1\geq 2 e\sqrt{\frac{n}{\alpha}}\right) \leq \alpha n^2 4^{-e\sqrt{\frac{n}{\alpha}}},$$

2.  $$\mathbb{P}_n^{(\alpha)}(\lambda_1' \geq 2 e\sqrt{n\alpha}) \leq \frac{n^2}{\alpha} 4^{-e\sqrt{n\alpha}}.$$

In particular $$\lim_{n \to \infty} \mathbb{P}_n^{(\alpha)} \left(
 \left[-\frac{\lambda'_1}{\sqrt{n}};\frac{\lambda_1}{\sqrt{n}}\right] \subseteq \left[-2e\sqrt{\alpha}, \frac{2e}{\sqrt{\alpha}}\right]
 \right) =1.$$
:::

*End of proof of Theorem [\[theo:RYD-limit\]](#theo:RYD-limit){reference-type="ref" reference="theo:RYD-limit"}.* It follows from Proposition [\[PropAPlanchWeakConv\]](#PropAPlanchWeakConv){reference-type="ref" reference="PropAPlanchWeakConv"} and Lemma [\[lem:FiniteSupport\]](#lem:FiniteSupport){reference-type="ref" reference="lem:FiniteSupport"} by the same argument as the one given in [@IvanovOlshanski2002 Theorem 5.5]. 0◻

# Jack measure: central limit theorem for Jack characters {#sect:CLT}

In this section we prove the central limit theorem for Jack characters (Theorem [\[theo:FluctuationsJackCharacters\]](#theo:FluctuationsJackCharacters){reference-type="ref" reference="theo:FluctuationsJackCharacters"}) and the bound of the speed of convergence in this theorem (Theorem [\[theo:SpeedConvergence\]](#theo:SpeedConvergence){reference-type="ref" reference="theo:SpeedConvergence"}).

## Multivariate Stein's method

As explained in introduction, our main tool will be a multivariate analog of the so-called *Stein's method* due to Reinert and Röllin [@ReinertRollin2009]. For any discrete random variables $W, W^*$ with values in $\mathbb{R}^d$, we say that the pair $(W,W^*)$ is *exchangeable* if for any $w_1,w_2 \in \mathbb{R}^d$ one has $\mathbb{P}(W = w_1, W^* = w_2) = \mathbb{P}(W = w_2, W^* = w_1)$. Let $\mathbb{E}^W(\cdot)$ denotes the conditional expected value given $W$. The theorem of Reinert and Röllin is the following [@ReinertRollin2009 Theorem 2.1]:

::: theorem
[]{#theo:MultivariateStein label="theo:MultivariateStein"} Let $(W,W^*)$ be an exchangeable pair of $\mathbb{R}^d$-valued random variables such that $\mathbb{E}(W) = 0$ and $\mathbb{E}(WW^t) = \varSigma$, where $\Sigma \in M_{d \times d}(\mathbb{R})$ is symmetric and positive definite matrix. Suppose that $\mathbb{E}^W(W^* - W) = - \Lambda W$, where $\Lambda \in M_{d \times d}(\mathbb{R})$ is invertible. Then, if $Z$ is a $d$-dimensional standard normal distribution, we have for every three times differentiable function $h:\mathbb{R}^d \to \mathbb{R}$, $$\left| \mathbb{E}h(W) - \mathbb{E}h(\varSigma^{1/2}Z) \right| \leq \frac{|h|_2}{4}A + \frac{|h|_3}{12}B,$$ where, using the notation $\lambda^{(i)} := \sum_{1 \leq m \leq d}|(\Lambda^{-1})_{m,i}|$, $$\begin{aligned}
    |h|_n &= \sup_{i_1,\dots,i_n} \left\lVert \frac{\partial^n}{\partial x_{i_1} \cdots \partial x_{i_n}}h\right\rVert, \\
 A &= \sum_{1 \leq i,j \leq d} \lambda^{(i)} \sqrt{\mathop{\mathrm{Var}}\mathbb{E}^W(W_i^* - W_i)(W_j^* - W_j)}, \\
 B &= \sum_{1 \leq i,j,k \leq d} \lambda^{(i)} \mathbb{E}|(W_i^* - W_i)(W_j^* - W_j)(W_k^* - W_k)|.
\end{aligned}$$
:::

Let $d$ be a positive integer. For $k \ge 2$, as in the statement of Theorem [\[theo:FluctuationsJackCharacters\]](#theo:FluctuationsJackCharacters){reference-type="ref" reference="theo:FluctuationsJackCharacters"}, we define the following function of Young diagrams of size $n$: $$W_k = n^{-k/2} \sqrt{k} \, \theta^{(\alpha)}_{(k,1^{n-k})} = n^{-k/2} \sqrt{k}^{-1} \mathop{\mathrm{Ch}}_{(k)}.$$ It can be seen as a random variable on the probability space of Young diagrams of size $n$ endowed with Jack measure. We also consider the corresponding random vector $$\tilde{W}_d = (W_2,\dots,W_{d+1}).$$ Theorem [\[theo:FluctuationsJackCharacters\]](#theo:FluctuationsJackCharacters){reference-type="ref" reference="theo:FluctuationsJackCharacters"} states that $\tilde{W}_d$ converges in distribution towards a vector of independent Gaussian random variables. Therefore we would like to apply the theorem above to this $d$-uplet of random variables. In the next sections, we shall contruct an exchangeable pair and check the hypothesis of Theorem [\[theo:MultivariateStein\]](#theo:MultivariateStein){reference-type="ref" reference="theo:MultivariateStein"}.
