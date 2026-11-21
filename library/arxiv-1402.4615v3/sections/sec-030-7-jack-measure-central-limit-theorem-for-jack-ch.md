---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-030-7-jack-measure-central-limit-theorem-for-jack-ch
section_title: "Jack measure: central limit theorem for Jack characters"
section_number: 7
pages: 40-41
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.969
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#sect:CLT label="sect:CLT"}

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
