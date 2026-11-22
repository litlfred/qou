---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-020-37-yet-another-gradation-and-bound-on-degrees
section_title: "Yet another gradation and bound on degrees"
section_number: 3.7
pages: 27-30
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.973
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
The gradation introduced in Section [\[SubsectBound2\]](#SubsectBound2){reference-type="ref" reference="SubsectBound2"} is suitable for some purposes (as we have seen in the previous section), but it has the unpleasant aspect that all homogeneous spaces have an infinite dimension. In particular, Proposition [\[PropBound2\]](#PropBound2){reference-type="ref" reference="PropBound2"} does not give any information on the maximal power of $M_2$ which can appear in $L_\mu$. In this section we propose a way to avoid this difficulty. It is technical but will be useful in the next section.

We define a new algebraic basis of $\Lambda_\star^{(\alpha)}$ by: $$\begin{aligned}
M'_2 & =M_2,\\ 
M'_k & = M_k - (-\gamma)^{k-2} M_2 \qquad \text{for } k\geq 3.
\end{aligned}$$ We also consider the gradation defined by: $$\deg_3(M'_2) = 1, \quad \deg_3(M'_k) =k-2 \text{ for }k\ge 3,$$ so that $\deg_3(M'_\rho)=|\rho|-2\ell(\rho) +m_2(\rho)$. Obviously, there exists a polynomial $L'_\mu$ such that $$\mathop{\mathrm{Ch}}_\mu = L'_\mu(M'_2,M'_3,\dots).$$ For example, one has: $$L'_{(2,2)} = (M'_3)^2 +6(M'_2)^2 - 4 M'_4 -10 \gamma M'_3 -2M'_2.$$ We denote by $(a')_\rho^\mu$ the coefficient of $M'_\rho$ in $L'_\mu$. Then, one has the following result.

::: proposition
[]{#PropBound3 label="PropBound3"} The coefficient $(a')_\rho^\mu$ is a polynomial in $\gamma$ of degree at most $|\mu|-\ell(\mu)+m_1(\mu) - (|\rho|-2\ell(\rho) +m_2(\rho))$.
:::

::: remark
The analogous result is not true for $a_\rho^\mu$, as it can be seen on the case $\mu=(2,2)$.
:::

The algorithm to compute the coefficient $(a')_\rho^\mu$ is the same as for $a_\rho^\mu$ and the proof of the bound on degrees is similar to those of Propositions [\[PropBound1\]](#PropBound1){reference-type="ref" reference="PropBound1"} and [\[PropBound2\]](#PropBound2){reference-type="ref" reference="PropBound2"}. Let us give some details.

First, one can rewrite Proposition [\[PropMkLo\]](#PropMkLo){reference-type="ref" reference="PropMkLo"} in terms of the quantities $M'_k$: $$\begin{gathered}
    M'_k(\lambda^{(i)}) - M'_k(\lambda)
    =M_k(\lambda^{(i)}) - M_k(\lambda) - (-\gamma)^{k-2} \\
    =    \sum_{\substack{ r\geq 1, s,t \geq 0, \\ 2r+s+t \leq k \\  \bm{(r,s,t) \neq (1,k-2,0) }}}
     \Bigg[ z_i^{k-2r-s-t}  \binom{k-t-1}{2r+s-1}\binom{r+s-1}{s} \\ 
    \cdot (-\gamma)^s (M'_t(\lambda)+ (-\gamma)^{t-2} M'_2(\lambda)) \Bigg].
    \label{EqM'klo}
\end{gathered}$$ Please note that the term $(-\gamma)^{k-2}$ corresponding to $(r,s,t)=(1,k-2,0)$ does not belong to the sum any more. By multiplication, there exist some polynomials $(b')_{g,\pi}^\rho(\gamma)$ such that $$M'_\rho(\lambda^{(i)}) = M'_\rho(\lambda) + \sum_{g,\pi} (b')_{g,\pi}^\rho(\gamma)\
z_i^g\ M'_\pi(\lambda).$$ Using Equation [\[EqIng1Lassalle\]](#EqIng1Lassalle){reference-type="eqref" reference="EqIng1Lassalle"} and Proposition [\[PropLinearRelation\]](#PropLinearRelation){reference-type="ref" reference="PropLinearRelation"}, we obtain the following equalities: $$\begin{aligned}
    \sum_\rho (a')^\mu_\rho \left( \sum_{\substack{g,h \geq 0, \\ \pi \vdash h}} (b')_{g,\pi}^\rho(\gamma) 
    M'_\pi M_g  \right) &= m_1(\mu) \mathop{\mathrm{Ch}}_{\mu \backslash 1},
    \tag{$A'$}\label{EqRec1'}\\
    \sum_\rho (a')^\mu_\rho \left( \sum_{\substack{g,h \geq 0, \\ \pi \vdash h}} (b')_{g,\pi}^\rho(\gamma) 
    M'_\pi M_{g+1}  \right) &= \sum_{r \geq 2} r \cdot m_r(\mu) \mathop{\mathrm{Ch}}_{\mu_{\downarrow r}}.
    \tag{$B'$}\label{EqRec2'}
\end{aligned}$$ Plugging $M_g=M'_g + (-\gamma)^{g-2} M'_2$ in these equations and identifying the coefficient of $M'_\tau$ on both sides, we obtain the following system: $$\begin{gathered}
    \sum_\rho (a')^\mu_\rho \left( \sum_{\substack{g, \pi, \\ \pi \cup (g)=\tau}} (b')_{g,\pi}^\rho(\gamma) 
    + \sum_{\substack{g>2, \pi, \\ \pi \cup (2)=\tau}} (-\gamma)^{g-2} (b')_{g,\pi}^\rho(\gamma)  \right) \\ =
    m_1(\mu) (a')^{\mu \backslash 1}_\tau,
    \tag{$A'_\tau$}\label{EqRec1'tau}
\end{gathered}$$ $$\begin{gathered}
    \sum_\rho (a')^\mu_\rho \left( \sum_{\substack{g, \pi, \\ \pi \cup (g+1)=\tau}} (b')_{g,\pi}^\rho(\gamma) 
    + \sum_{\substack{g \geq 2, \pi ,\\ \pi \cup (2)=\tau}} (-\gamma)^{g-1} (b')_{g,\pi}^\rho(\gamma)
    \right) \\= \sum_{r \geq 2} r \cdot m_r(\mu) (a')^{\mu_{\downarrow r}}_\tau,
    \tag{$B'_\tau$}\label{EqRec2'tau}
 
\end{gathered}$$ It is easy to check that Lemma [\[LemTriangle\]](#LemTriangle){reference-type="ref" reference="LemTriangle"} still holds for this system.

The next step is to give a bound on the degree of $(b')_{g,\pi}^\rho(\gamma)$.

::: lemma
$$\deg_\gamma(b_{g,\pi}^\rho(\gamma)) \leq \deg_3(M'_\rho) - \deg_3(M'_\pi) - \max(g,1).$$ []{#LemDeg3B' label="LemDeg3B'"}
:::

::: proof
*Proof.* Let us call *pre-degree* (with respect to $\deg_3$) of an expression of the form $b(\gamma)\ M'_\pi\ z_i^g$ the quantity $\deg_\gamma(b)+\deg_3(M'_\pi)+g$. It is multiplicative. Clearly, $M'_k(\lambda^{(i)})$ has pre-degree $\max(k-2,1)$ (see Equation [\[EqM\'klo\]](#EqM'klo){reference-type="eqref" reference="EqM'klo"}), thus $M'_\rho(\lambda^{(i)})$ has pre-degree $\deg_3(M'_\rho)$, which finishes the proof of the case $g \geq 1$. For $g=0$, one has to look at the term which does not involve $z_i$. It is easy to check on Equation [\[EqM\'klo\]](#EqM'klo){reference-type="eqref" reference="EqM'klo"} (here, it is crucial to use $M'$ and not $M$) that $$M'_k(\lambda^{(i)})|_{z_i=0}=M'_k(\lambda)|_{z_i=0} + \left(\text{terms of pre-degree $k-3$}\right).$$ Hence by multiplication, $$M'_\rho(\lambda^{(i)})|_{z_i=0}=M'_\rho(\lambda)|_{z_i=0} + 
    \left(\text{terms of pre-degree }\deg_3(M'_\rho) - 1\right),$$ which finishes the proof of the lemma. ◻
:::

We have now all the tools to prove Proposition [\[PropBound3\]](#PropBound3){reference-type="ref" reference="PropBound3"} by induction. As usual, we first consider the case where $\rho=\tau \cup (2)$ has the smallest part equal to $2$. Then Equation $(A_\tau)$ can be written as: $$\begin{gathered}
    m_2(\rho) \cdot (a')^\mu_\rho = m_1(\mu) (a')^{\mu \backslash 1}_{\tau} 
    - \sum_{\substack{\pi,g, \\ \pi \cup (g) = \tau}} \sum_{\rho' >_1 \rho}
    (b')_{g,\pi}^{\rho'}(\gamma) (a')^\mu_{\rho'} \\
    -\sum_{\substack{g>2, \pi, \\ \pi \cup (2)=\tau}} \sum_{\rho' >_1 \rho}
    (-\gamma)^{g-2} (b')_{g,\pi}^\rho(\gamma)(a')^\mu_{\rho'}.
\end{gathered}$$ With arguments similar to the ones used previously, the first two terms are polynomials in $\gamma$ of degree at most $|\mu|-\ell(\mu)+m_1(\mu) - \deg_3(M'_{\rho})$. Let us focus on the last summand. By induction hypothesis $(a')^\mu_{\rho'}$ is a polynomial of degree $|\mu|-\ell(\mu)+m_1(\mu) - \deg_3(M'_{\rho'})$. By Lemma [\[LemDeg3B\'\]](#LemDeg3B'){reference-type="ref" reference="LemDeg3B'"}, $(b')_{g,\pi}^\rho(\gamma)$ has degree equal to $\deg_3(M'_\rho) - \deg_3(M'_\pi) - g$. Hence the product of these two terms with $(-\gamma)^{g-2}$ has degree at most $$|\mu|-\ell(\mu)+m_1(\mu) - (\deg_3(M'_\pi) - 2) = |\mu|-\ell(\mu)+m_1(\mu) - \deg_3(M'_\rho).$$ The equality comes from the fact that $\rho=\tau \cup (2)=\pi \cup (2,2)$.

Finally one obtains that $(a')^\mu_\rho$ has degree at most $|\mu|-\ell(\mu)+m_1(\mu) - \deg_3(M'_{\rho})$.

The case when $\rho$ has no parts equal to $2$ is similar. 0◻

::: corollary
For any partition $\mu$ one has: $$\deg_3(\mathop{\mathrm{Ch}}_\mu) = |\mu| - \ell(\mu)+m_1(\mu),$$ and the top degree part does not depend on $\alpha$. []{#corol:deg3_Ch label="corol:deg3_Ch"}
:::

::: remark
The top degree part of $\mathop{\mathrm{Ch}}_\mu$ for $\deg_3$ has, as far as we know, no close expression.
:::
