---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-024-42-projection-on-functions-on-young-diagrams-of
section_title: "Projection on functions on Young diagrams of size n"
section_number: 4.2
pages: 32-33
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.99
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#SubsectProjN label="SubsectProjN"} Recall that $\Lambda_\star^{(\alpha)}$ is a subalgebra of the algebra of functions on all Young diagrams. The latter has a natural projection map $\varphi_n$ onto $\mathcal{F}(\mathcal{Y}_n,\mathbb{Q})$, the algebra of functions on Young diagrams of size $n$. As Jack symmetric functions $J_\lambda$ form a basis of the symmetric function ring, the functions $(\theta_\mu)_{\mu \vdash n}$ form a basis of $\mathcal{F}(\mathcal{Y}_n,\mathbb{Q})$ (see [@FerayInductionJM Proposition 4.1]).

We consider the structure constants $c_{\mu,\nu;\pi}$ of $\mathcal{F}(\mathcal{Y}_n,\mathbb{Q})$ with basis $(\theta_\mu)_{\mu \vdash n}$, that is the numbers uniquely defined by: $$\label{EqDefC}
\theta_\mu(\lambda) \cdot \theta_\nu(\lambda)
= \sum_{\pi \vdash n} c_{\mu,\nu;\pi} \, \theta_\pi(\lambda) \quad \text{for all $\lambda \vdash n$}.$$ Note that $c_{\mu,\nu;\pi}$ depends on $\alpha$, but, according to our convention, we omit the superscript, when it does not bring any confusion. It is important to keep in mind that the $c$'s are indexed by triples of partitions of *the same size*, while the $g$'s are indexed by any triple of partitions.

It turns out that the quantities $c_{\mu,\nu;\pi}$ can be expressed in terms of the quantities $g_{\mu,\nu;\tau}$. To explain that, for any partition $\mu$, let $\tilde{\mu}$ denotes the partition obtained from $\mu$ by erasing all parts equal to $1$. Fix two partitions $\mu$ and $\nu$ of the same integer $n$; then $$\mathop{\mathrm{Ch}}_{\tilde{\mu}} \cdot \mathop{\mathrm{Ch}}_{\tilde{\nu}} 
= \sum_\tau g_{\tilde{\mu},\tilde{\nu};\tau} \mathop{\mathrm{Ch}}_{\tau}.$$ But using the definition of $\mathop{\mathrm{Ch}}$ from Section [\[eq:definition-Jack\]](#eq:definition-Jack){reference-type="ref" reference="eq:definition-Jack"}, this implies that, for all $\lambda \vdash n$, one has: $$\begin{gathered}
    \alpha^{-\frac{|\mu|-\ell(\mu)}{2}}\ z_{\tilde{\mu}}\ \theta_\mu(\lambda) \cdot
 \alpha^{-\frac{|\nu|-\ell(\nu)}{2}}\ z_{\tilde{\nu}}\ \theta_\nu(\lambda) \\
= \sum_{\substack{\tau, \\|\tau| \leq n}} g_{\tilde{\mu},\tilde{\nu};\tau}\ 
 \alpha^{\frac{|\tau|-\ell(\tau)}{2}}\ z_\tau\ \binom{n-|\tau|+m_1(\tau)}{m_1(\tau)}\
 \theta_{\tau 1^{n-|\tau|}}(\lambda).
 
\end{gathered}$$ Every partition $\tau$ with $|\tau| \leq n$ can be written uniquely as $\tilde{\pi} 1^i$ where $\pi$ is a partition of $n$ and $i \leq m_1(\pi)$. Denoting $$d(\mu,\nu;\pi) := |\mu|-\ell(\mu) + |\nu|-\ell(\nu) - (|\pi| - \ell(\pi)),$$ one has $$\theta_\mu(\lambda) \cdot \theta_\nu(\lambda)
= \frac{\alpha^{d(\mu,\nu;\pi)/2}}{z_{\tilde{\mu}} z_{\tilde{\nu}}} \sum_{\pi \vdash n} 
\left( \sum_{0 \leq i \leq m_1(\pi)} g_{\tilde{\mu},\tilde{\nu};\tilde{\pi}
1^i}
\cdot z_{\tilde{\pi}} \cdot i! \cdot \binom{n-|\tilde{\pi}|}{i} \right) \theta_\pi(\lambda).$$ As this holds for all partitions $\lambda$ of $n$, by definition of structure constants, we have: $$\label{EqCG}
    c_{\mu,\nu;\pi} = \frac{\alpha^{d(\mu,\nu;\pi)/2}}{z_{\tilde{\mu}} z_{\tilde{\nu}}} 
\sum_{0 \leq i \leq m_1(\pi)} g_{\tilde{\mu},\tilde{\nu};\tilde{\pi} 1^i}    
\cdot z_{\tilde{\pi}} \cdot i! \cdot \binom{n-|\tilde{\pi}|}{i}.$$ Using Theorem [\[theo:struct-const\]](#theo:struct-const){reference-type="ref" reference="theo:struct-const"} with $\deg_3$, we know that $g_{\tilde{\mu},\tilde{\nu};\tilde{\pi} 1^i}$ is a polynomial of degree at most $d(\mu,\nu;\pi)-i$. We have thus proved the following result:

::: proposition
[]{#PropStructureTheta label="PropStructureTheta"} Let $\mu$, $\nu$ and $\pi$ be three partitions without parts equal to $1$. Then, $\alpha^{-d(\mu,\nu;\pi)/2} c_{\mu 1^{n-|\mu|},\nu 1^{n-|\nu|};\pi 1^{n-|\pi|}}$ is a polynomial in $n$ and $\gamma$ with rational coefficients, of total degree at most $d(\mu,\nu;\pi)$.

Moreover, seen as a polynomial in $\gamma$, it has the same parity as $d(\mu,\nu;\pi)$.
:::

::: corollary
[]{#CorolConnectionSeries label="CorolConnectionSeries"} The quantity $c_{\mu 1^{n-|\mu|},\nu 1^{n-|\nu|};\pi 1^{n-|\pi|}}$ is a polynomial in $n$ and $\alpha$. Moreover, it has degree at most $d(\mu,\nu;\pi)$ in $n$ and at most $d(\mu,\nu;\pi)$ in $\alpha$ (the total degree may be bigger).
:::

Applications of these statements are given in next section as well as in appendix [\[app:Matching-Jack_And_Matsumoto\]](#app:Matching-Jack_And_Matsumoto){reference-type="ref" reference="app:Matching-Jack_And_Matsumoto"}.
