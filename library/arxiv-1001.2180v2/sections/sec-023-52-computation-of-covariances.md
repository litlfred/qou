---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-023-52-computation-of-covariances
section_title: "Computation of covariances"
section_number: 5.2
pages: 21-22
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.974
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
Now, let us compute explicitly the limit (co)variances of the rescaled deviations of the $\varSigma_k$. First, note that if $l$ and $m$ are two positive integers, then: $$\begin{aligned}
k^\bullet(\varSigma_l,\varSigma_m)&=\mathbb{E}[\varSigma_l \bullet \varSigma_m] - \mathbb{E}[\varSigma_l]\,\mathbb{E}[\varSigma_m] = \mathbb{E}[\varSigma_{l,m}] - \mathbb{E}[\varSigma_l]\,\mathbb{E}[\varSigma_m]\\
&= \frac{(1-q)^{l+m}}{1-q^{l,m}}\,\left(n^{\downarrow l+m} - n^{\downarrow l}\,n^{\downarrow m}\right)=-lm\,\frac{(1-q)^{l+m}}{1-q^{l,m}}\,n^{l+m-1}+ O(n^{l+m-2})
\end{aligned}$$ The last identity follows from the development of the falling factorial: $$n^{\downarrow k} =n^k- \frac{k(k-1)}{2}\,n^{k-1}+O(n^{k-2})$$ Now, we can compute the higher term of the standard cumulant $k(\varSigma_l,\varSigma_m)$ if we use the graded development of $\varSigma_l\,\varSigma_m-\varSigma_{l,m}$ in the algebra of observables: $$\begin{aligned}
k(\varSigma_l,\varSigma_m)&=k^{\mathrm{id}}(\varSigma_l,\varSigma_m)+k^\bullet(\varSigma_l,\varSigma_m)=\mathbb{E}[\varSigma_{l}\,\varSigma_{m}-\varSigma_{l,m}]+k^\bullet(\varSigma_l,\varSigma_m)\\
&=\mathbb{E}[lm\,\varSigma_{l+m-1}]-lm\,\frac{(1-q)^{l+m}}{1-q^{l,m}}\,n^{l+m-1}+ O(n^{l+m-2})\\
&=lm\,(1-q)^{l+m}\,\left(\frac{1}{1-q^{l+m-1,1}} - \frac{1}{1-q^{l,m}}\right)\,n^{l+m-1}+ O(n^{l+m-2})
\end{aligned}$$ We have therefore proved:

::: proposition
[]{#PropFluctuationsCharacters label="PropFluctuationsCharacters"} If we denote $Z_{n,q,k}=\sqrt{n}\,(\varSigma_k/n^k - (1-q)^k/(1-q^k))$, then $(Z_{n,q,k})_{k \geq 2}$ converges in finite-dimensional laws towards a gaussian vector $(Z_{q,k})_{k \geq 2}$, with the following covariance matrix: $$k(Z_{q,l},Z_{q,m})=lm\,(1-q)^{l+m}\,\left(\frac{1}{1-q^{l+m-1,1}} - \frac{1}{1-q^{l,m}}\right)$$
:::

::: proof
*End of the proof of Proposition [\[prop:deviation_powersums\]](#prop:deviation_powersums){reference-type="ref" reference="prop:deviation_powersums"}.* It turns out that the sequence $(W_{n,q,k})_{k\geq 2}$ of the rescaled deviations of power sums has the same limit law $(Z_{q,k})_{k \geq 2}$. Indeed, we have already shown that the limit of the rescaled deviations of power sums is a gaussian vector, and it suffices then to show that $k(p_l,p_m)$ has the same higher term as $k(\varSigma_l,\varSigma_m)$. According to the proposition [\[prop:sigma_pk\]](#prop:sigma_pk){reference-type="ref" reference="prop:sigma_pk"}, each symbol $\varSigma_k$ is a rational polynomial in the $p_{l\leq k}$ with higher term $p_k$. So, we can use the multi-linearity of joint cumulants to write: $$k(\varSigma_l,\varSigma_m)=k(p_l,p_m) + (\text{cumulants of observables }a_i,b_j\text{ with }\deg a_i+\deg b_j <l+m).$$ But if $a$ and $b$ are two observables of degree $A$ and $B$, then we have seen that $k(a,b)$ is a $O(n^{A+B-1})$. As a consequence, the remaining terms are all $O(n^{l+m-2})$. This ends the proof of Proposition [\[prop:deviation_powersums\]](#prop:deviation_powersums){reference-type="ref" reference="prop:deviation_powersums"}. ◻
:::

::: remark
[]{#RemFluctuationsQCharacters label="RemFluctuationsQCharacters"} Lemma [\[lem:ordre_cumulants\]](#lem:ordre_cumulants){reference-type="ref" reference="lem:ordre_cumulants"} also implies that the rescaled $q$-characters converge towards a gaussian vector. For these $q$-characters, it can be shown that if $S_{n,q,k}=\sqrt{n}\,(\varSigma_{k,q}/n^{k})\simeq \sqrt{n} \,\chi^{\lambda}(k1^{n-k},q)$, then $(S_{n,q,k})_{k \geq 2}$ converges in finite-dimensional laws towards a gaussian vector $(S_{q,k})_{k \geq 2}$, with the following covariance matrix: $$k(S_{q,l},S_{q,m})=(q-q^{2})^{l+m-3}\,(1-q^{2})\,\frac{\{l-1\}_{q}\,\{m-1\}_{q}}{\{l+m-1\}_{q}\,\{l+m-2\}_{q}\,\{l+m-3\}_{q}}$$ Hence, one has a $q$-analogue of Kerov's central limit theorem (see [@IO02 Theorem 6.1]) for the $q$-characters of the Hecke algebras under $q$-Plancherel measures. However, notice that the fluctuations of the $q$-characters are always some $O(n^{-1/2})$, in contrast to the case of the characters $\chi^{\lambda}(k1^{n-k})$ under Plancherel measures, whose fluctuations are $O(n^{-k/2})$. The proof of the formula given above involves a generalization of Proposition [\[PropFluctuationsCharacters\]](#PropFluctuationsCharacters){reference-type="ref" reference="PropFluctuationsCharacters"} to the case of arbitrary central characters $\varSigma_{\mu}$, and a Möbius inversion formula that allows to simplify the expression of the covariances; we refer to a future paper of the second author ([@Mel10]) for details on these computations.
:::
