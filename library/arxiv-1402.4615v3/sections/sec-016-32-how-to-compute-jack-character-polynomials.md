---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-016-32-how-to-compute-jack-character-polynomials
section_title: "How to compute Jack character polynomials?"
section_number: 3.2
pages: 19-22
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.978
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#SubsectAlgo label="SubsectAlgo"} Unfortunately, the argument given above to prove the existence of $L_\mu$ and $K_\mu$ is not effective. M. Lassalle [@Lassalle2009] gave an algorithm for computing $K_\mu$ by induction over $\mu$. In this section we present a slightly simpler version of this algorithm which allows to compute $L_\mu$ instead of $K_\mu$.

One of the base ingredients is the following formula, which corresponds to [@Lassalle2009 Proposition 8.3].

::: proposition
[]{#PropMkLo label="PropMkLo"} Let $k \geq 2$, $\lambda$ be a Young diagram and $i=(x,y)$ an inner corner of $\lambda$. $$\begin{gathered}
 M_k(\lambda^{(i)})-M_k(\lambda) =
        \sum_{\substack{r\geq 1, s,t \geq 0, \\ 2r+s+t \leq k}}
    z_i^{k-2r-s-t} \\
    \binom{k-t-1}{2r+s-1}\binom{r+s-1}{s}
    \left( -\gamma \right)^s M_t(\lambda),
\end{gathered}$$ where $z_i=\sqrt{\alpha} x - \sqrt{\alpha}^{-1} y$ is the content of the corner corresponding to $i$ in the $\alpha$-anisotropic diagram $A_\alpha(\lambda)$.
:::

::: proof
*Proof.* As mentioned above, this is exactly [@Lassalle2009 Proposition 8.3]. To help the reader, we compare our notations to Lassalle's ones (we use boldface to refer to his notations): $$\begin{aligned}
        M_k(\lambda^{(i)}) &= \alpha^{k/2} \bm{M_k(\lambda^{(i)})}; \\
        M_t(\lambda) &= \alpha^{t/2} \bm{M_t(\lambda)}; \\
        z_i &= \sqrt{\alpha} \cdot \bm{x_i};\\
        \gamma &= \sqrt{\alpha}^{-1} - \sqrt{\alpha}.\qedhere
    
\end{aligned}$$ ◻
:::

For any partition $\rho$ we define $M_\rho(\lambda):=\prod_i M_{\rho_i}(\lambda)$ by multiplicativity. The above proposition implies immediately the following corollary:

::: corollary
[]{#CorolMlo label="CorolMlo"} For any partition $\rho$, any diagram $\lambda$ and any inner corner $i$ of $\lambda$, $$M_{\rho}(\lambda^{(i)}) = M_{\rho}(\lambda)
    + \sum_{\substack{ g,h \geq 0, \\ \pi \vdash h}} b_{g,\pi}^\rho(\gamma)
    \ z_i^g\ M_\pi(\lambda),$$ where $b_{g,\pi}^\rho(\gamma)$ is a polynomial in $\gamma$.
:::

::: proof
*Proof.* The case when $\rho$ consists of only one part is a direct consequence of Proposition [\[PropMkLo\]](#PropMkLo){reference-type="ref" reference="PropMkLo"} (one even has an explicit expression for $b_{g,\pi}^\rho(\gamma)$ in this case). The general case follows by multiplication. ◻
:::

This corollary is an analogue of Equation (8.1) in [@Lassalle2009].

Let $\mu$ be a partition. By definition of $L_\mu$, there exist some numbers $a^\mu_\rho$ (depending on $\alpha$) such that, for any Young diagram $\lambda$, $$\mathop{\mathrm{Ch}}_\mu(\lambda) = \sum_\rho a^\mu_\rho\ M_\rho(\lambda).$$ Using Corollary [\[CorolMlo\]](#CorolMlo){reference-type="ref" reference="CorolMlo"} we can compute $$\begin{gathered}
\label{EqIng1Lassalle}
    \mathop{\mathrm{Ch}}_\mu(\lambda^{(i)}) = \sum_\rho a^\mu_\rho\ M_\rho(\lambda^{(i)}) \\
    = \mathop{\mathrm{Ch}}_\mu(\lambda) + \sum_\rho a^\mu_\rho \left( \sum_{\substack{g,h \geq 0, \\ \pi \vdash h}}
    b_{g,\pi}^\rho(\gamma)\ z_i^g\ M_\pi(\lambda) \right).
    
\end{gathered}$$

The second ingredient of Lassalle's algorithm is a linear identity between the values of Jack character evaluated on different diagrams. We denote by $c_i(\lambda)$ the probability of the corner $i$ in the transition measure $\mu_{A_\alpha(\lambda)}$, so that $$\label{eq:Mk_co}
    M_k(\lambda) = \sum_i c_i(\lambda) z_i^k.$$ In particular, $$\begin{aligned}
    \sum_i c_i(\lambda)&=1, \label{eq:Sum_co}\\
    \sum_i c_i(\lambda) z_i&=0.\label{Sum_cozo}
\end{aligned}$$

Then we have [@Lassalle2009 Equation (3.6)] the following proposition.

::: proposition
[]{#PropLinearRelation label="PropLinearRelation"} For any (continuous) Young diagram $\lambda$ and any partition $\mu$ $$\begin{aligned}
        \sum_{i \in \mathbb{I}_\lambda} c_i(\lambda) \mathop{\mathrm{Ch}}_\mu(\lambda^{(i)})
        &= m_1(\mu) \mathop{\mathrm{Ch}}_{\mu \backslash 1}(\lambda) + \mathop{\mathrm{Ch}}_\mu(\lambda), \\
        \sum_{i \in \mathbb{I}_\lambda} c_i(\lambda) z_i \mathop{\mathrm{Ch}}_\mu(\lambda^{(i)})
        &= \sum_{r \geq 2} r m_r(\mu) \mathop{\mathrm{Ch}}_{\mu_{\downarrow r}} (\lambda).
    
\end{aligned}$$
:::

::: proof
*Proof.* It is an exercise to adapt Equations (3.6) of [@Lassalle2009] to our notations. ◻
:::

Using Equations [\[EqIng1Lassalle\]](#EqIng1Lassalle){reference-type="eqref" reference="EqIng1Lassalle"}, [\[eq:Mk_co\]](#eq:Mk_co){reference-type="eqref" reference="eq:Mk_co"}, [\[eq:Sum_co\]](#eq:Sum_co){reference-type="eqref" reference="eq:Sum_co"} and [\[Sum_cozo\]](#Sum_cozo){reference-type="eqref" reference="Sum_cozo"} together with Proposition [\[PropLinearRelation\]](#PropLinearRelation){reference-type="ref" reference="PropLinearRelation"}, we obtain the following equalities between functions on the set of (continuous) Young diagrams: for any partition $\mu$, $$\begin{aligned}
    \sum_\rho a^\mu_\rho \left( \sum_{\substack{g,h \geq 0, \\ \pi \vdash h}} b_{g,\pi}^\rho(\gamma) 
    \, M_\pi \, M_g  \right) &= m_1(\mu) \mathop{\mathrm{Ch}}_{\mu \backslash 1},
    \tag{A}\label{EqRec1}\\
    \sum_\rho a^\mu_\rho \left( \sum_{\substack{g,h \geq 0, \\ \pi \vdash h}} b_{g,\pi}^\rho(\gamma) 
    \, M_{\pi} \, M_{g+1}  \right) &= \sum_{r \geq 2} r \cdot m_r(\mu) \mathop{\mathrm{Ch}}_{\mu_{\downarrow r}}.
    \tag{B}\label{EqRec2}
\end{aligned}$$ Fix some partition $\tau$. We can identify the coefficient of a given monomial $M_\tau$ in the above equations. This gives us two linear equations which will be denoted by $(A_\tau)$ and $(B_\tau)$: $$\begin{aligned}
    \sum_\rho a^\mu_\rho \left( \sum_{\substack{g,h \geq 0, \ \pi \vdash h \\ \pi \cup (g)=\tau}} b_{g,\pi}^\rho(\gamma) 
     \right) &= m_1(\mu) \, a^{\mu \backslash 1}_\tau,
    \tag{$A_\tau$}\label{EqRecTau1}\\
    \sum_\rho a^\mu_\rho \left( \sum_{\substack{g,h \geq 0, \ \pi \vdash h \\ \pi \cup (g+1)=\tau}} b_{g,\pi}^\rho(\gamma) 
    \right) &= \sum_{r \geq 2} r \cdot m_r(\mu) \, a^{\mu_{\downarrow r}}_\tau.
    \tag{$B_\tau$}\label{EqRecTau2}
\end{aligned}$$

Now, assume that, for some partition $\mu$, we can compute $L_\nu$ for all partitions $\nu$ of size smaller than $|\mu|$. Then the equations [\[EqRecTau1\]](#EqRecTau1){reference-type="eqref" reference="EqRecTau1"} and [\[EqRecTau2\]](#EqRecTau2){reference-type="eqref" reference="EqRecTau2"} can be interpreted as a linear system, where the variables are the coefficients $a^\mu_\rho$.

This is a *finite* system of linear equations (indeed, $a^\mu_\rho=0$ as soon as $|\rho| \geq |\mu|+\ell(\mu)$ [@Lassalle2009 Proposition 9.2 (ii)]). As explained by M. Lassalle, the system obtained that way has a unique solution (we shall see another explanation of that in the next paragraph) and thus, one can compute the coefficients $a^\mu_\rho$ by induction over $|\mu|$.
