---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-033-74-error-term
section_title: "Error term"
section_number: 7.4
pages: 45-50
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.895
latex_coverage_ratio: 0.968
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#subsec:ErrorTerm label="subsec:ErrorTerm"} In the previous Section, we have checked that the pair $(\tilde{W}_d, \tilde{W}_d^*)$ of the random vectors satisfies the assumptions of Theorem [\[theo:MultivariateStein\]](#theo:MultivariateStein){reference-type="ref" reference="theo:MultivariateStein"}. In order to prove that the random vector $\tilde{W}_d$ is asymptotically Gaussian, we need to show that quantities $A$ and $B$ from Theorem [\[theo:MultivariateStein\]](#theo:MultivariateStein){reference-type="ref" reference="theo:MultivariateStein"} vanish as $n \to \infty$. This section is devoted to making these calculations.

::: lemma
[]{#lem:fourth_moment label="lem:fourth_moment"} The following inequality holds: $$\begin{gathered}
\mathop{\mathrm{Var}}_n^{(\alpha)}\left((\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_i - W_i^*)(W_j - W_j^*)\right) \leq \frac{1}{ij n^{i+j+2}}\\
\times \left(\sum_{\mu_1, \mu_2, l \atop 
{\tiny |\mu_1|+\ell(\mu_1) \le i+j \atop |\mu_2|+\ell(\mu_2) \le i+j} }
H^{(i,j)}_{\mu_1, \mu_2; (1^l)} (n)_l - (i+j)^2\left(\sum_{l \ge 0} g_{(i), (j); l} (n)_l \right)^2 \right),
\end{gathered}$$ where $$H^{(i,j)}_{\mu_1, \mu_2; \mu} := (i+j-|\mu_1|+m_1(\mu_1))(i+j-|\mu_2|+m_1(\mu_2))g_{(i),(j); \mu_1}g_{(i),(j); \mu_2}g_{\mu_1,\mu_2; \mu}.$$
:::

Note that the sums in the Lemma are clearly finite.

::: proof
*Proof.* Following Fulman [@FulmanFluctuationChA2 Proof of Proposition 6.4], from Jensen's inequality for conditional expectations, the fact that $\tilde{W}_d$ is determined by $\lambda$ implies that $$\mathbb{E}_n^{(\alpha)}\left((\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_i - W_i^*)(W_j - W_j^*)\right)^2 \leq \mathbb{E}_n^{(\alpha)}\left((\mathbb{E}_n^{(\alpha)})^\lambda(W_i - W_i^*)(W_j - W_j^*)\right)^2.$$ Fix a partition $\lambda$ of $n$. We have, by Proposition [\[prop:FulmanComputations\]](#prop:FulmanComputations){reference-type="ref" reference="prop:FulmanComputations"}, that $$\begin{gathered}
\label{eq:blablabla}
(\mathbb{E}_n^{(\alpha)})^\lambda(W_i^* - W_i)(W_j^* - W_j) = \frac{\alpha(n-1)}{\alpha(n-1)+1}(\mathbb{E}_n^{(\alpha)})^\lambda(W_i' - W_i)(W_j' - W_j)\\
 = \frac{\alpha(n-1)}{\alpha(n-1)+1}\left( (\mathbb{E}_n^{(\alpha)})^\lambda(W_i'W_j') - (\mathbb{E}_n^{(\alpha)})^\lambda(W_i')W_j - (\mathbb{E}_n^{(\alpha)})^\lambda(W_j')W_i + W_iW_j \right)\\
 = \frac{\alpha(n-1)}{\alpha(n-1)+1}\left( (\mathbb{E}_n^{(\alpha)})^\lambda(W_i'W_j') + \left( \frac{(i+j)(\alpha(n-1)+1)}{\alpha n(n-1)}-1\right) W_iW_j \right),
 
\end{gathered}$$ where the last equality follows from Proposition [\[prop:SteinCondition1\]](#prop:SteinCondition1){reference-type="ref" reference="prop:SteinCondition1"}. But the product $W_i W_j$ expands as $$W_i W_j = \frac{1}{\sqrt{ij} n^{(i+j)/2}} \sum_{|\mu| \leq i+j+2} g_{(i),(j); \mu} \mathop{\mathrm{Ch}}_\mu.
    \label{eq:prod_W}$$ Thus, strictly from the definition of $L^{(\alpha)}$, one has $$\begin{gathered}
    (\mathbb{E}_n^{(\alpha)})^\lambda(W_i'W_j') = \sum_{\rho \vdash n} L(\lambda,\rho) W_i(\rho) W_j(\rho)
    \\= \sum_{\tau \vdash n}\theta_\tau(\lambda)\theta_\tau(n-1,1)
    \frac{(z_\tau)^2\alpha^{2\ell(\tau)}}{\alpha^n n!\sqrt{ij} n^{(i+j)/2}}
 \sum_{|\mu| \leq i+j+2} g_{(i),(j); \mu} \sum_{\rho \vdash n}
\frac{\mathop{\mathrm{Ch}}_\mu(\rho)\theta_\tau(\rho)}{j_\rho^{(\alpha)}}.
\end{gathered}$$ We may assume $n \ge i+j$. Recall that $\mathop{\mathrm{Ch}}_\mu(\rho)$ is a multiple of $\theta_{\mu 1^{n-|\mu|}}(\rho)$ and, hence, using Lemma [\[lem:identities\]](#lem:identities){reference-type="ref" reference="lem:identities"} [\[eq:orthogonality\]](#eq:orthogonality){reference-type="eqref" reference="eq:orthogonality"}, only terms corresponding to $\tau=\mu 1^{n-|\mu|}$ survives and we get: $$\begin{gathered}
    (\mathbb{E}_n^{(\alpha)})^\lambda(W_i'W_j') =
    \frac{1}{\sqrt{ij} n^{(i+j)/2}} \sum_{|\mu| \leq i+j+2} g_{(i),(j); \mu} \mathop{\mathrm{Ch}}_\mu(\lambda)\\
    \theta_{\mu\cup 1^{n-|\mu|}}(n-1,1)
    \frac{z_{\mu\cup 1^{n-|\mu|}}\alpha^{\ell({\mu\cup 1^{n-|\mu|}})}}{\alpha^n n!}.
\end{gathered}$$ We now apply Lemma [\[lem:identities\]](#lem:identities){reference-type="ref" reference="lem:identities"} [\[eq:(n-1,1)\]](#eq:(n-1,1)){reference-type="eqref" reference="eq:(n-1,1)"}: $$\begin{gathered}
(\mathbb{E}_n^{(\alpha)})^\lambda(W_i'W_j') = \frac{1}{\sqrt{ij} n^{(i+j)/2}} 
\sum_{|\mu| \le i+j+2} g_{(i),(j); \mu} \mathop{\mathrm{Ch}}_\mu(\lambda) \\
\times \frac{(\alpha(n-1)+1)(n-|\mu|+m_1(\mu))-n}{\alpha n(n-1)}.
\end{gathered}$$

One can substitute above equation and equation [\[eq:prod_W\]](#eq:prod_W){reference-type="eqref" reference="eq:prod_W"} to the equation [\[eq:blablabla\]](#eq:blablabla){reference-type="eqref" reference="eq:blablabla"} and simplify it to obtain $$\begin{gathered}
    \label{eq:2nd_moment_wi*-wi}
(\mathbb{E}_n^{(\alpha)})^\lambda(W_i^* - W_i)(W_j^* - W_j) \\
= \frac{1}{\sqrt{ij} n^{(i+j)/2}} 
\sum_{|\mu| \le i+j+2} \frac{i+j-|\mu|+m_1(\mu)}{n} g_{(i),(j); \mu} \mathop{\mathrm{Ch}}_\mu(\lambda).
\end{gathered}$$ Notice that $g_{(i),(j); \mu}=0$ for $|\mu|+\ell(\mu) > i+j$, unless $\mu=(i,j)$ (Lemma [\[lem:SC\]](#lem:SC){reference-type="ref" reference="lem:SC"} [\[eq:SC-4\]](#eq:SC-4){reference-type="eqref" reference="eq:SC-4"}). In the latter case ($\mu=(i,j)$), the numerical factor $i+j-|\mu|+m_1(\mu)$ vanishes. It gives that the summation in equation [\[eq:2nd_moment_wi\*-wi\]](#eq:2nd_moment_wi*-wi){reference-type="eqref" reference="eq:2nd_moment_wi*-wi"} can be restricted to partitions $\mu$ with $|\mu|+\ell(\mu) \le i+j$.

Taking the square, it gives us $$\begin{gathered}
\mathbb{E}_n^{(\alpha)}\left((\mathbb{E}_n^{(\alpha)})^\lambda(W_i^* - W_i)(W_j^* - W_j) \right)^2 \\
= \frac{1}{ij n^{i+j+2}}\mathbb{E}_n^{(\alpha)}\left( \sum_{|\mu|+\ell(\mu) \le i+j} (i+j-|\mu|+m_1(\mu)) g_{(i),(j); \mu} \mathop{\mathrm{Ch}}_\mu(\lambda)\right)^2 \\
= \frac{1}{ij n^{i+j+2}}
\sum_{\mu_1, \mu_2, \mu \atop 
{\tiny |\mu_1|+\ell(\mu_1) \le i+j \atop |\mu_2|+\ell(\mu_2) \le i+j} }
H^{(i,j)}_{\mu_1, \mu_2; \mu}\mathbb{E}_n^{(\alpha)}(\mathop{\mathrm{Ch}}_\mu(\lambda)) \\
= \frac{1}{ij n^{i+j+2}} \sum_{\mu_1, \mu_2, l\atop                   
{\tiny |\mu_1|+\ell(\mu_1) \le i+j \atop |\mu_2|+\ell(\mu_2) \le i+j} }
H^{(i,j)}_{\mu_1, \mu_2; (1^l)} (n)_l,
\end{gathered}$$ where $H^{(i,j)}_{\mu_1, \mu_2; \mu}$ is defined as in the statement of the lemma. The last equality comes from the easy formula for the expectation of $\mathop{\mathrm{Ch}}_\mu$, see equation [\[eq:exp_Ch\]](#eq:exp_Ch){reference-type="eqref" reference="eq:exp_Ch"}.

Let us now analyse $\left(\mathbb{E}_n^{(\alpha)}\left( (\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_i^* - W_i)(W_j^* - W_j)\right) \right)$. After expanding the product, each term can be dealt with as follows: $$\begin{aligned}
    \mathbb{E}_n^{(\alpha)}\left( (\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}( W_i^* W_j^*) \right)&= \mathbb{E}_n^{(\alpha)}(W_i^* W_j^*)=
    \mathbb{E}_n^{(\alpha)}(W_i W_j) \\
    \mathbb{E}_n^{(\alpha)}\left( (\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}( W_i^* W_j) \right)&= \mathbb{E}_n^{(\alpha)}\left(W_j (\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}( W_i^*)\right)=\left( 1-\frac{i}{n} \right) \mathbb{E}_n^{(\alpha)} (W_i W_j)\\
\mathbb{E}_n^{(\alpha)}\left( (\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}( W_i^* W_j) \right)&=
    \left( 1-\frac{j}{n} \right) \mathbb{E}_n^{(\alpha)} (W_i W_j).\\
    \mathbb{E}_n^{(\alpha)}\left( (\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}( W_i W_j) \right)&=
    \mathbb{E}_n^{(\alpha)}(W_i W_j) 
\end{aligned}$$ The first equation comes from the fact that $\tilde{W}_d^*$ and $\tilde{W}_d$ have the same distribution, while the second one is a consequence of Proposition [\[prop:SteinCondition1\]](#prop:SteinCondition1){reference-type="ref" reference="prop:SteinCondition1"}. The third one is similar to the second one. Therefore $$\begin{gathered}
\left(\mathbb{E}_n^{(\alpha)}\left( (\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_i^* - W_i)(W_j^* - W_j)\right) \right)^2\\
= \left( \frac{i+j}{n} \mathbb{E}_n^{(\alpha)}(W_iW_j) \right)^2 = \frac{(i+j)^2}{ij n^{i+j+2}}\left(\sum_\mu g_{(i), (j); \mu} \mathbb{E}_n^{(\alpha)}(\mathop{\mathrm{Ch}}_\mu)\right)^2\\
=\frac{(i+j)^2}{ij n^{i+j+2}} \left(\sum_l g_{(i), (j);l} (n)_l\right)^2,
\end{gathered}$$ where we used equations [\[eq:prod_W\]](#eq:prod_W){reference-type="eqref" reference="eq:prod_W"} and [\[eq:exp_Ch\]](#eq:exp_Ch){reference-type="eqref" reference="eq:exp_Ch"} in the second and third equalities. We finish the proof by the following inequality: $$\begin{gathered}
\mathop{\mathrm{Var}}_n^{(\alpha)}\left((\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_i - W_i^*)(W_j - W_j^*)\right) \\
= \mathbb{E}_n^{(\alpha)}\left((\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_i^* - W_i)(W_j^* - W_j) \right)^2 - \left(\mathbb{E}_n^{(\alpha)}\left( (\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_i^* - W_i)(W_j^* - W_j)\right) \right)^2 \\
\leq \mathbb{E}_n^{(\alpha)}\left((\mathbb{E}_n^{(\alpha)})^\lambda(W_i^* - W_i)(W_j^* - W_j) \right)^2 - \left(\mathbb{E}_n^{(\alpha)}\left( (\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_i^* - W_i)(W_j^* - W_j)\right) \right)^2.
\end{gathered}$$ ◻
:::

::: proposition
[]{#prop:ErrorTermA label="prop:ErrorTermA"} Let $d \in \mathbb{N}$ and let $$A = \sum_{2 \leq i,j \leq d+1} \frac{n}{i} \sqrt{\mathop{\mathrm{Var}}_n^{(\alpha)}\left((\mathbb{E}_n^{(\alpha)})^{\tilde{W}_d}(W_i - W_i^*)(W_j - W_j^*)\right)}.$$
:::

Then $A = O(n^{-1/2})$.

::: proof
*Proof.* By Lemma [\[lem:fourth_moment\]](#lem:fourth_moment){reference-type="ref" reference="lem:fourth_moment"} we need to estimate the following sum: $$\label{eq:to_bound}
    \left(
\sum_{\mu_1, \mu_2, l \ge 1 \atop 
{\tiny |\mu_1|+\ell(\mu_1) \le i+j \atop |\mu_2|+\ell(\mu_2) \le i+j} }
H^{(i,j)}_{\mu_1, \mu_2; (1^l)}(n)_l - (i+j)^2\sum_{l,k} g_{(i), (j); (1^l)}g_{(i), (j); (1^k)} (n)_l(n)_k \right)^{1/2}.$$ Let us first consider the second sum, which is simpler. Suppose that $i \neq j$. Then, by Lemma [\[lem:SC\]](#lem:SC){reference-type="ref" reference="lem:SC"} [\[eq:SC-2\]](#eq:SC-2){reference-type="eqref" reference="eq:SC-2"}, summands corresponding to $l \ge (i+j)/2$ or $k \ge (i+j)/2$ vanish and the sum is $O(n^{i+j-1})$.

Consider now the case $i=j$ (recall that $i,j \ge 2$). We use this time Lemma [\[lem:SC\]](#lem:SC){reference-type="ref" reference="lem:SC"} [\[eq:SC-1\]](#eq:SC-1){reference-type="eqref" reference="eq:SC-1"}: summands corresponding to $l \ge i+1$ or $k \ge i+1$ vanish. Therefore there is no summands of order $n^{i+j+1}$. The unique summand of order $n^{i+j}$ (corresponding to $l=k=i$) is $i^2 \, (n)_i^2$ by Lemma [\[lem:SC\]](#lem:SC){reference-type="ref" reference="lem:SC"} [\[eq:SC-3\]](#eq:SC-3){reference-type="eqref" reference="eq:SC-3"}.

Finally, we have that $$\label{eq:estimate_sum_g2}
    (i+j)^2\sum_{l,k} g_{(i), (j); (1^l)}g_{(i), (j); (1^k)} (n)_l(n)_k =
\delta_{i,j} 4\, i^4 n^{i+j} + O(n^{i+j-1}).$$ Let us describe the terms corresponding to $l \ge i+j$ in the first sum of [\[eq:to_bound\]](#eq:to_bound){reference-type="eqref" reference="eq:to_bound"}. By Lemma [\[lem:SC\]](#lem:SC){reference-type="ref" reference="lem:SC"} [\[eq:SC-1\]](#eq:SC-1){reference-type="eqref" reference="eq:SC-1"}, $g_{\mu_1,\mu_2,(1^l)}$, and hence $H^{(i,j)}_{\mu_1,\mu_2,(1^l)}$, vanishes unless $$|\mu_1|+\ell(\mu_1) + |\mu_2|+\ell(\mu_2) \ge 2l \ge 2(i+j).$$ Comparing it with the conditions under the first summation symbol of [\[eq:to_bound\]](#eq:to_bound){reference-type="eqref" reference="eq:to_bound"}, we have, in fact, equalities instead of inequalities above, *i. e.* $$l = i+j = |\mu_1|+\ell(\mu_1) = |\mu_2|+\ell(\mu_2).$$ Moreover, in this case, by Lemma [\[lem:SC\]](#lem:SC){reference-type="ref" reference="lem:SC"} [\[eq:SC-1\]](#eq:SC-1){reference-type="eqref" reference="eq:SC-1"}, we have that $g_{\mu_1, \mu_2; (1^{i+j})} = 0$ unless $\mu_1 \cup \mu_2 = 1^{i+j}$, which means that $\mu_1 = \mu_2 = (1^{(i+j)/2})$ (in particular, $i+j$ must be even). Then, by Lemma [\[lem:SC\]](#lem:SC){reference-type="ref" reference="lem:SC"} [\[eq:SC-2\]](#eq:SC-2){reference-type="eqref" reference="eq:SC-2"}, one has that $g_{(i),(j);(1^{(i+j)/2})} = 0$ unless $i=j$. Therefore, $H^{(i,j)}_{\mu_1, \mu_2; (1^l)}=0$ if $i \neq j$ and $l \ge i+j$.

Additionally, using the definition of $H^{(i,j)}_{\mu_1,\mu_2,\mu}$, the observations above and Lemma [\[lem:SC\]](#lem:SC){reference-type="ref" reference="lem:SC"} [\[eq:SC-3\]](#eq:SC-3){reference-type="eqref" reference="eq:SC-3"}, one has that $H^{(i,i)}_{(1^i), (1^i); (1^{2i})} = 4 \, i^4$. Concluding, $$\label{eq:estimate_sum_H}
    \sum_{\mu_1, \mu_2, l}H^{(i,j)}_{\mu_1, \mu_2; (1^l)}(n)_l = \delta_{i,j}
    4\, i^4 n^{i+j} + O(n^{i+j-1}).$$ Comparing equations [\[eq:estimate_sum_g2\]](#eq:estimate_sum_g2){reference-type="eqref" reference="eq:estimate_sum_g2"} and [\[eq:estimate_sum_H\]](#eq:estimate_sum_H){reference-type="eqref" reference="eq:estimate_sum_H"}, it gives $$\begin{gathered}
\left(\sum_{\mu_1, \mu_2, l}H^{(i,j)}_{\mu_1, \mu_2; (1^l)}(n)_l - (i+j)^2\sum_{l,k} g_{(i), (j); (1^l)}g_{(i), (j); (1^k)} (n)_l(n)_k \right)^{1/2}\\
 = O(n^{(i+j-1)/2}),
 \label{eq:TechnicalBound}
\end{gathered}$$ which implies that $$A = \sum_{2 \leq i,j \leq d+1} \frac{1}{i\sqrt{ij} n^{(i+j)/2}}O(n^{(i+j-1)/2}) = O(n^{-1/2}),$$ which finishes the proof. ◻
:::

::: lemma
[]{#lem:momentsDegree label="lem:momentsDegree"} For any $k \geq 2$, and $\lambda \vdash n$ there exists $B_{\alpha,k} \in \mathbb{R}$, which depends only on $k$ and $\alpha$ such that $$|M_k(\lambda)| \leq B_{\alpha,k} \max(\lambda_1, \lambda_1')^k .$$
:::

::: proof
*Proof.* As explained in Section [\[SectDefKerov\]](#SectDefKerov){reference-type="ref" reference="SectDefKerov"}, $M^{(\alpha)}_k(\lambda)=M^{(1)}_k(A_\alpha(\lambda))$ is the $k$-th moment of the transition measure of the anisotropic digram $A_\alpha(\lambda)$. But this measure is supported by the contents of inner corners of $A_\alpha(\lambda)$. All these contents are clearly bounded in absolute value by $\max(\sqrt{\alpha} \, \lambda_1, \sqrt{\alpha}^{-1} \lambda'_1)$. Hence the $k$-th moment of the measure is bounded by the $k$-th power of this number, which proves the lemma. ◻
:::

::: proposition
[]{#prop:ErrorTermB label="prop:ErrorTermB"} Let $d \in \mathbb{N}$ and let $$\beta := \sum_{2 \leq i,j,k \leq d+1} \frac{n}{i} |(W_i^* - W_i)(W_j^* - W_j)(W_k^* - W_k)|.$$ Then $B := \mathbb{E}_n^{(\alpha)}(\beta) = O(n^{-1/2})$.
:::

::: proof
*Proof.* Fix some integer $k \ge 2$. From the definition of $M^{(\alpha)}$, we know that $\lambda^*$ is obtained from $\lambda$ by removing a box from the diagram of $\lambda$ and reattaching it somewhere. It means that $\lambda = \tau^{(i_1)}$ and $\lambda^* = \tau^{(i_2)}$ for some $\tau \vdash n-1$. It implies that $$\left|W_k^* - W_k\right| \leq \sqrt{k}^{-1} n^{-k/2} \left| \mathop{\mathrm{Ch}}_{(k)}(\tau^{(i_1)}) - \mathop{\mathrm{Ch}}_{(k)}(\tau^{(i_2)}) \right| .$$ By equation [\[EqIng1Lassalle\]](#EqIng1Lassalle){reference-type="eqref" reference="EqIng1Lassalle"}, the right hand side of the above inequality is equal to $$\sqrt{k}^{-1} n^{-k/2}\left|\sum_\rho a^{(k)}_\rho \left( \sum_{\substack{g,h \geq 0, \\ \pi \vdash h}}
    b_{g,\pi}^\rho(\gamma)\ M_\pi(\tau)\ \left(z_{i_1}^g - z_{i_2}^g\right) \right)\right|,$$ where $|\pi| \leq |\rho| - g - 2$. By Proposition [\[PropBound1\]](#PropBound1){reference-type="ref" reference="PropBound1"} we know, that $a^{(k)}_\rho = 0$ for $|\rho| > k+1$, hence $a^{(k)}_\rho b_{g,\pi}^\rho(\gamma) = 0$ for $|\pi| > k-g-1$. But $z_{i_1}^g$ and $z_{i_2}^g$ are bounded by $O_{\alpha,g}(\max(\lambda_1, \lambda_1')^g)$, as $\alpha$-contents of some box or corner of $\lambda$. Thanks to Lemma [\[lem:momentsDegree\]](#lem:momentsDegree){reference-type="ref" reference="lem:momentsDegree"}, it implies that there exists some $C_{\alpha,k} \in \mathbb{R}$ which depends only on $k$ and $\alpha$ such that $$\left|W_k^* - W_k\right| \leq n^{-k/2} C_{\alpha,k} \max(\lambda_1, \lambda_1')^{k-1}.$$ If $\lambda_1 \leq 2 e\sqrt{\frac{n}{\alpha}}$ and $\lambda_1' \leq 2 e\sqrt{n\alpha}$, then, for any integers $i,j,k \ge 2$, one has $$\begin{gathered}
\label{eq:BoundTripleProductGoodCase}
\left|(W_i^* - W_i)(W_j^* - W_j)(W_k^* - W_k)\right| \leq  |(W_i^* - W_i)| |(W_j^* - W_j)| |(W_k^* - W_k)|\\
 = O(n^{-3/2}) .
\end{gathered}$$ Summing over $i$, $j$ and $k$, we get $\beta = O(n^{-1/2})$. Otherwise, we use the obvious bounds $\lambda_1,\lambda'_1 \le n$, and we get $$\begin{gathered}
\left|(W_i^* - W_i)(W_j^* - W_j)(W_k^* - W_k)\right| \leq  |(W_i^* - W_i)| |(W_j^* - W_j)| |(W_k^* - W_k)|\\
 = O(n^{(i+j+k)/2-3})
\end{gathered}$$ that is $\beta = O(n^{3(d+1)/2-2})$. By Lemma [\[lem:FiniteSupport\]](#lem:FiniteSupport){reference-type="ref" reference="lem:FiniteSupport"}, the probability that the second case occurs is exponentially small. Hence the bound of the first case holds in expectation. It finishes the proof. ◻
:::
