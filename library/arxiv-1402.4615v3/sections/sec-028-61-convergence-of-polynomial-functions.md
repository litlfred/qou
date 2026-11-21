---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-028-61-convergence-of-polynomial-functions
section_title: "Convergence of polynomial functions"
section_number: 6.1
pages: 39-40
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.973
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
Let us recall equation [\[eq:exp_Ch\]](#eq:exp_Ch){reference-type="eqref" reference="eq:exp_Ch"}, which gives us the expectation of Jack characters with respect to Jack measure: $$\mathbb{E}_{\mathbb{P}_n^{(\alpha)}}(\mathop{\mathrm{Ch}}^{(\alpha)}_\mu)=\begin{cases}
    n(n-1)\cdots(n-k+1) & \text{if }\mu=1^k \text{ for some }k \leq n,\\
    0   & \text{otherwise.}
\end{cases}$$ As $\mathop{\mathrm{Ch}}_\mu$ is a linear basis of $\Lambda_\star^{(\alpha)}$, it implies the following lemma (which is an analogue of [@OlshanskiJackPlancherel Theorem 5.5] with another gradation).

::: lemma
Let $F$ be an $\alpha$-polynomial function. Then $\mathbb{E}_{\mathbb{P}_n^{(\alpha)}}(F)$ is a polynomial in $n$ of degree at most $\deg_1(F)/2$. []{#LemDegEsper label="LemDegEsper"}
:::

::: proof
*Proof.* It is enough to verify this lemma on the basis $\mathop{\mathrm{Ch}}_\mu$ because of the remark in Section [\[SubsectDegCh\]](#SubsectDegCh){reference-type="ref" reference="SubsectDegCh"}. But in this case $\mathbb{E}_{\mathbb{P}_n^{(\alpha)}}(F)$ is explicit (see formula [\[eq:exp_Ch\]](#eq:exp_Ch){reference-type="eqref" reference="eq:exp_Ch"}) and the lemma is obvious (recall that $\deg_1(\mathop{\mathrm{Ch}}_\mu)=|\mu|+\ell(\mu)$, see Section [\[SubsectBound1\]](#SubsectBound1){reference-type="ref" reference="SubsectBound1"}). ◻
:::

Informally, smaller terms for $\deg_1$ are asymptotically negligible. We can now prove the following weak convergence result:

::: proposition
[]{#PropAPlanchWeakConv label="PropAPlanchWeakConv"} Let $(\lambda_{(n)})_{n \geq 1}$ be a sequence of random partitions distributed with Jack measure. For any 1-polynomial function $F \in \Lambda_\star^{(1)}$, when $n \to \infty$, one has $$F\bigg(D_{1/\sqrt{n}} \big(A_\alpha(\lambda_{(n)})\big)\bigg) \xrightarrow{\mathbb{P}_n^{(\alpha)}} 
    F( \Omega) ,$$ where $\xrightarrow{\mathbb{P}_n^{(\alpha)}}$ means convergence in probability and $\Omega$ is given by [\[eq:DefOmega\]](#eq:DefOmega){reference-type="eqref" reference="eq:DefOmega"}.
:::

::: proof
*Proof.* As $(R^{(1)}_k)_{k \geq 2}$ is an algebraic basis of $\Lambda_\star^{(1)}$, it is enough to prove the proposition for any $R^{(1)}_k$.

Let $\mu$ be partition. By Corollary [\[corol:dominant_deg1\]](#corol:dominant_deg1){reference-type="ref" reference="corol:dominant_deg1"} $$\begin{gathered}
\label{EqTopDeg1}
    \prod_{i \leq \ell(\mu)} R_{\mu_i+1} =
    \mathop{\mathrm{Ch}}_\mu + \text{ terms of degree at most }\\
    |\mu|+\ell(\mu)-1\text{ with respect to }\deg_1.
\end{gathered}$$ Together with Lemma [\[LemDegEsper\]](#LemDegEsper){reference-type="ref" reference="LemDegEsper"} and the formula [\[eq:exp_Ch\]](#eq:exp_Ch){reference-type="eqref" reference="eq:exp_Ch"} for $\mathbb{E}_{\mathbb{P}_n^{(\alpha)}}(\mathop{\mathrm{Ch}}_\mu)$, this implies: $$\mathbb{E}_{\mathbb{P}_n^{(\alpha)}} \left(\prod_{i \leq \ell(\mu)}R_{\mu_i+1}\right) = \begin{cases}
    n(n-1)\cdots(n-k+1) + O(n^{k-1}) & \text{if }\mu=1^k \text{ for some }k; \\
    o(n^{\frac{|\mu|+\ell(\mu)}{2}}) & \text{otherwise.}
\end{cases}$$ In particular $$\begin{aligned}
    \mathbb{E}_{\mathbb{P}_n^{(\alpha)}} (R_k(D_{1/\sqrt{n}}(\lambda_{(n)}))) &=
\frac{1}{n^{k/2}}
    \mathbb{E}_{\mathbb{P}_n^{(\alpha)}} (R_k) = \delta_{k,2} + O\left(\frac{1}{\sqrt{n}}\right), \\
    \mathop{\mathrm{Var}}_{\mathbb{P}_n^{(\alpha)}} (R_k(D_{1/\sqrt{n}}(\lambda_{(n)}))) &= \frac{1}{n^k}
\left( 
    \mathbb{E}_{\mathbb{P}_n^{(\alpha)}} \big((R_k)^2\big) - \mathbb{E}_{\mathbb{P}_n^{(\alpha)}} (R_k)^2
\right)
    = O\left(\frac{1}{n}\right).
\end{aligned}$$ Thus, for each $k$, $R_k(D_{1/\sqrt{n}}(\lambda_{(n)}))$ converges in probability towards $\delta_{k,2}$. But, by definition $$R_k(D_{1/\sqrt{n}}(\lambda_{(n)}))=R^{(1)}_k \bigg(D_{1/\sqrt{n}}\big(A_\alpha(\lambda_{(n)})\big)\bigg)$$ and $(\delta_{k,2})_{k \geq 2}$ is the sequence of free cumulants of the continuous diagram $\Omega$ (see [@Biane2001 Section 3.1]), *i.e.* $$\delta_{k,2} = R_k^{(1)}(\Omega).\qedhere$$ ◻
:::
