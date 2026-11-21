---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-032-73-checking-hypotheses
section_title: "Checking hypotheses"
section_number: 7.3
pages: 43-45
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.967
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#subsec:CheckingHypotheses label="subsec:CheckingHypotheses"}

Recall that we have defined $$W_k = n^{-k/2} \sqrt{k}^{-1} \mathop{\mathrm{Ch}}_{(k)}$$ and the random vector $$\tilde{W}_d = (W_2,\dots,W_{d+1})$$ on the probability space of Young diagrams of size $n$ endowed with Jack measure. Let $\lambda$ be a random partition distributed according to Jack measure, and $\lambda^*$ ($\lambda'$, respectively) be obtained from $\lambda$ by applying the Markov chain $M^{(\alpha)}$ ($L^{(\alpha)}$, respectively). By a small abuse of notations, set $\tilde{W}_d:=\tilde{W}_d(\lambda)$, $\tilde{W}_d^*:=\tilde{W}_d(\lambda^*)$ and $\tilde{W}'_d:=\tilde{W}_d(\lambda')$. We shall prove now, that for any $d \in \mathbb{N}$, the pair $(\tilde{W}_d, \tilde{W}_d^*)$ of random vectors satisfies conditions of Theorem [\[theo:MultivariateStein\]](#theo:MultivariateStein){reference-type="ref" reference="theo:MultivariateStein"}.

First, note that $\mathbb{E}_n^{(\alpha)}(\tilde{W}_d)=0$ from equation [\[eq:exp_Ch\]](#eq:exp_Ch){reference-type="eqref" reference="eq:exp_Ch"}.

We should now verify the hypothesis involving $(\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_k^*)$. Let us begin with two technical known statements about Jack polynomials.

::: lemma
[]{#lem:identities label="lem:identities"}

1.  [@Macdonald1995 Page 382] []{#eq:orthogonality label="eq:orthogonality"} $$\sum_{\rho \vdash n} \frac{\theta_\mu(\rho)\theta_\nu(\rho)}{j^{(\alpha)}_\rho} =  \frac{\delta_{\mu,\nu}}{z_\mu \alpha^{\ell(\mu)}};$$

2.  [@Stanley1989 Page 107] []{#eq:(n-1,1) label="eq:(n-1,1)"} $$\theta_\mu((n-1,1)) = \frac{\alpha^{n-\ell(\mu)}n!}{z_\mu}\frac{(\alpha(n-1)+1)m_1(\mu) - n}{\alpha n(n-1)}.$$
:::

Recall that $(\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}$ denotes the conditional expectation given $\tilde{W}_d$. Similarly, we denote by $(\mathbb{E}_n^{(\alpha)})^{\lambda}$ the conditional expectation given $\lambda$.

::: proposition
[]{#prop:SteinCondition1 label="prop:SteinCondition1"} Let $d \in \mathbb{N}$ and let $2 \leq k \leq d+1$. Then, one has $$\begin{aligned}
    (\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_k^*) &=
(\mathbb{E}_n^{(\alpha)})^{\lambda}(W_k^*) = \left(1-\frac{k}{n}\right)W_k ; \\
    (\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_k') &=
 (\mathbb{E}_n^{(\alpha)})^{\lambda}(W_k') = \left(1-\frac{k(\alpha(n-1)+1)}{\alpha n(n-1)}\right)W_k.
 
\end{aligned}$$
:::

::: proof
*Proof.* By definition, $$(\mathbb{E}_n^{(\alpha)})^{\lambda}(W_k^*)=
    \sum_{\lambda^*} M(\lambda,\lambda^*) W_k^*(\lambda^*).$$ From [@FulmanFluctuationChA2 Proposition 6.2.], we have that $(\theta_\mu(\lambda))_{\lambda \vdash n}$ is an eigenvector of $M^{(\alpha)}$ with eigenvalue $$d_\mu := 1 + \frac{\alpha(n-1)}{\alpha(n-1)+1}\left( \frac{z_\mu}{\alpha^{n-\ell(\mu)}n!}\theta_\mu((n-1,1)) - 1\right).$$ Using Lemma [\[lem:identities\]](#lem:identities){reference-type="ref" reference="lem:identities"}-(2), this eigenvalue can be simplified to (surprisingly, this was not noticed by Fulman) $$d_\mu=                                                                  
 \frac{(\alpha(n-1)+1)m_1(\mu)}{n(\alpha (n-1) + 1)} = \frac{m_1(\mu)}{n}.$$

As $(W_k^*(\lambda))_{\lambda \vdash n}$ is a multiple of $(\theta_\mu(\lambda))_{\lambda \vdash n}$, it is also an eigenvector of $M^{(\alpha)}$, with the same eigenvalue. Hence, $$(\mathbb{E}_n^{(\alpha)})^{\lambda}(W_k^*) (\lambda)= d_{(k,1^{n-k})}
W_k^*(\lambda).$$ For $\mu=(k,1^{n-k})$, we have $d_{(k,1^{n-k})}=1-\frac{k}{n}$, which finishes the proof of the second equality of the first statement.

In particular, we see that $(\mathbb{E}_n^{(\alpha)})^{\lambda}(W_k^*)$ depends only on $W_k$ and hence on $\tilde{W}_d$. As, conversely, $\tilde{W}_d$ is determined by $\lambda$, one has $$(\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_k^*) =
 (\mathbb{E}_n^{(\alpha)})^{\lambda}(W_k^*).$$

The statement for $W_k'$ follows easily from the one for $W_k^\star$, using Proposition [\[prop:FulmanComputations\]](#prop:FulmanComputations){reference-type="ref" reference="prop:FulmanComputations"}. ◻
:::

::: corollary
[]{#cor:SteinCondition1 label="cor:SteinCondition1"} Let $d \in \mathbb{N}$. Then $$(\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(\tilde{W}_d^* - \tilde{W}_d) = -\Lambda \tilde{W}_d,$$ with $\Lambda_{i,j} = \delta_{i,j}\frac{i+1}{n}$. In particular, with the notation of Theorem [\[theo:MultivariateStein\]](#theo:MultivariateStein){reference-type="ref" reference="theo:MultivariateStein"}, $$\lambda^{(i)} = \frac{n}{i+1}.$$
:::

::: proof
*Proof.* It is a straightforward consequence of Proposition [\[prop:SteinCondition1\]](#prop:SteinCondition1){reference-type="ref" reference="prop:SteinCondition1"}. ◻
:::

Consider now $\varSigma = \mathbb{E}_n^{(\alpha)}(\tilde{W}_d\tilde{W}_d^t)$ as in the statement of Theorem [\[theo:MultivariateStein\]](#theo:MultivariateStein){reference-type="ref" reference="theo:MultivariateStein"}. This matrix is symmetric by definition, but one has to check that it is positive definite.

For a matrix $A$, let $\lVert A \rVert:=\max_{i,j} |A_{i,j}|$ denotes the supremum norm on matrices.

::: proposition
[]{#prop:SteinCondition2 label="prop:SteinCondition2"} There exists a constant $A_{d,\alpha}$ which depends only on $d$ and $\alpha$ such that for any $n \geq A_{d,\alpha}$ the matrix $\varSigma$ is positive definite. Moreover, $$\lVert \varSigma^{1/2} - \mathop{\mathrm{Id}}\rVert = O(n^{-1/2}).$$
:::

::: proof
*Proof.* Strictly from the definition we have that $$\begin{gathered}
 \varSigma_{i,j} = \mathbb{E}_n^{(\alpha)} \left( \frac{1}{\sqrt{i+1}\sqrt{j+1} n^{(i+j+2)/2}} \mathop{\mathrm{Ch}}_{(i+1)} \mathop{\mathrm{Ch}}_{(j+1)} \right) \\
 = \frac{1}{\sqrt{i+1}\sqrt{j+1} n^{(i+j+2)/2}} \sum_\lambda g_{(i+1),(j+1);\lambda} \mathbb{E}_n^{(\alpha)}(\mathop{\mathrm{Ch}}_\lambda). 
 
\end{gathered}$$ Since $$\mathbb{E}_{\mathbb{P}_n^{(\alpha)}}(\mathop{\mathrm{Ch}}_\mu)=\begin{cases}
    (n)_k & \text{if }\mu=1^k \text{ for some }k \leq n,\\
    0   & \text{otherwise,}
\end{cases}$$ we have that $$\varSigma_{i,j} = \frac{1}{\sqrt{i+1}\sqrt{j+1} n^{(i+j+2)/2}} \sum_l g_{(i+1),(j+1);(1^l)} (n)_l,$$ and using items [\[eq:SC-1\]](#eq:SC-1){reference-type="eqref" reference="eq:SC-1"}, [\[eq:SC-2\]](#eq:SC-2){reference-type="eqref" reference="eq:SC-2"} and [\[eq:SC-3\]](#eq:SC-3){reference-type="eqref" reference="eq:SC-3"} of Lemma [\[lem:SC\]](#lem:SC){reference-type="ref" reference="lem:SC"}, we have, that $$\varSigma_{i,j} = \delta_{i,j} + O(n^{-1/2}).$$ In other terms, $$\lVert \varSigma - \mathop{\mathrm{Id}}\rVert = O(n^{-1/2}).$$ As the set of positive definite matrix is an open set of the space of symmetric matrices, this implies that $\varSigma$ is positive definite for $n$ big enough.

Besides, the application $A \mapsto \sqrt{A}$ is differentiable on this open set, which implies the bound $\lVert \varSigma^{1/2} - \mathop{\mathrm{Id}}\rVert = O(n^{-1/2})$. ◻
:::
