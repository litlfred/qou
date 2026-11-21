---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-019-35-a-second-bound-on-degrees
section_title: "A second bound on degrees"
section_number: 3.5
pages: 26-27
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.971
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#SubsectBound2 label="SubsectBound2"} For some purposes the bound on the degree of $a_\rho^\mu$ given by Proposition [\[PropBound1\]](#PropBound1){reference-type="ref" reference="PropBound1"} is not strong enough. In this section we give another bound which is related to another gradation of $\Lambda_\star^{(\alpha)}$ defined by: $$\ \deg_2(M_k)=k-2 \qquad \text{for } k\geq 2 .$$ One has the following analogue of Lemma [\[LemDeg1B\]](#LemDeg1B){reference-type="ref" reference="LemDeg1B"}:

::: lemma
Let $\rho$ and $\pi$ be two partitions and $g\geq 0$ an integer. Then $$\begin{aligned}
            \deg_\gamma(b_{g,\pi}^\rho(\gamma)) &\leq \deg_2(M_\rho) - \deg_2(M_{\pi \cup (g)}), \\
            \deg_\gamma(b_{g,\pi}^\rho(\gamma)) &\leq \deg_2(M_\rho) - \deg_2(M_{\pi \cup (g+1)}) - 1. 
    
\end{aligned}$$ []{#LemDeg2B label="LemDeg2B"}
:::

::: proof
*Proof.* The proof is similar to the one of Lemma [\[LemDeg1B\]](#LemDeg1B){reference-type="ref" reference="LemDeg1B"}. We define the *pre-degree* (with respect to $\deg_2$) of an expression of the form $b(\gamma)\ M_\pi\ z_i^g$ to be $\deg_\gamma(b)+\deg_2(M_\pi)+g$. By Proposition [\[PropMkLo\]](#PropMkLo){reference-type="ref" reference="PropMkLo"}, the pre-degree of $M_k(\lambda^{(i)})$ is equal to $k-2$. Note that this pre-degree is multiplicative. Then $M_\rho(\lambda^{(i)})$ has pre-degree $|\rho|-2 \ell(\rho)=\deg_2(M_\rho)$. The lemma follows from the following inequalities: for $g\geq 0$, $$\begin{aligned}
        \deg_2(M_{\pi \cup (g)}) &\leq \deg_2(M_{\pi})+g; \\
        \deg_2(M_{\pi \cup (g+1)}) &\leq \deg_2(M_{\pi})+g-1.
    
\end{aligned}$$ Note that in the first inequality the difference between the right hand side and the left hand side is equal to $2$, unless $g=0$; in that case we have an equality. In the second inequality, the case $g=0$ is obvious as $M_{\pi \cup (1)}=0$ and hence its degree is $-\infty$ by convention. In all other cases, we have an equality. ◻
:::

We deduce from this lemma a new bound on the degree of $a_\rho^\mu$.

::: proposition
[]{#PropBound2 label="PropBound2"} The coefficient $a^\mu_\rho$ of $M_\rho$ in Jack character polynomial $L_\mu$ is a polynomial in $\gamma$ of degree smaller or equal to $|\mu|-\ell(\mu) - (|\rho|-2\ell(\rho))$.

The same is true for $K_\mu$.
:::

::: proof
*Proof.* It is a straightforward exercise to adapt the proof of Proposition [\[PropBound1\]](#PropBound1){reference-type="ref" reference="PropBound1"}. We use Lemma [\[LemDeg2B\]](#LemDeg2B){reference-type="ref" reference="LemDeg2B"} instead of Lemma [\[LemDeg1B\]](#LemDeg1B){reference-type="ref" reference="LemDeg1B"} and $|\rho|$ has to be replaced by $|\rho| - 2\ell(\rho)$. ◻
:::

As an immediate consequence we have

::: corollary
For any partition $\mu$ one has: $$\deg_2(\mathop{\mathrm{Ch}}_\mu) = |\mu| - \ell(\mu),$$ and the top degree part does not depend on $\alpha$.
:::

Note that Proposition [\[PropBound2\]](#PropBound2){reference-type="ref" reference="PropBound2"} is neither weaker nor stronger than Proposition [\[PropBound1\]](#PropBound1){reference-type="ref" reference="PropBound1"}. But it is sometimes more appropriate, as we shall see in the next section.

::: remark
The top degree part of $\mathop{\mathrm{Ch}}_\mu$ for $\deg_2$ does not admit an explicit expression as for $\deg_1$. One can however compute its linear terms in free cumulants, see [@FerayGouldenHook Section 3].
:::

## Polynomiality of $\theta_\mu(\lambda)$ {#SubsectCoefJackPoly}

In this section we prove that $\theta_\mu(\lambda)$ is a polynomial with rational coefficients in $\alpha$. This simple statement does not follow directly from the definition of Jack polynomials and had been open for twenty years. It was then proved by Lapointe and Vinet [@LapointeVinetJack], who also proved the integrality of the coefficients in the monomial basis. Short after that, this result was completed by a positivity result from Knop and Sahi [@KnopSahiCombinatoricsJack].

Using the material of this Section, we can find a new proof of the polynomiality in $\alpha$. Integrity and positivity seem unfortunately impossible to obtain *via* this method.

First, we consider the dependence of $M_k(\lambda)$ on $\alpha$.

::: lemma
Let $k \geq 2$ be an integer and $\lambda$ a partition. Then $\sqrt{\alpha}^{k-2} M_k(\lambda)$ is a polynomial in $\alpha$ with integer coefficients. []{#LemMkPol label="LemMkPol"}
:::

::: proof
*Proof.* We use induction over $|\lambda|$ and $k$. Proposition [\[PropMkLo\]](#PropMkLo){reference-type="ref" reference="PropMkLo"} can be rewritten as $$\begin{gathered}
 \sqrt{\alpha}^{k-2} M_k(\lambda^{(i)})
        -\sqrt{\alpha}^{k-2} M_k(\lambda) =
        \sum_{\substack{r\geq 1, s,t \geq 0, \\ 2r+s+t \leq k}}
        \alpha^r (\sqrt{\alpha} z_i)^{k-2r-s-t} \\
    \binom{k-t-1}{2r+s-1}\binom{r+s-1}{s}
    \left( \alpha-1 \right)^s \sqrt{\alpha}^{t-2} M_t(\lambda).
\end{gathered}$$ Note that $\sqrt{\alpha} z_i = \alpha x - y$ is a polynomial in $\alpha$ with integer coefficients. Hence the induction is immediate. ◻
:::

Now we write, for $\mu,\lambda \vdash n$, $$\begin{gathered}
    z_\mu \theta_\mu(\lambda)=\alpha^{\frac{|\mu|-\ell(\mu)}{2}} \mathop{\mathrm{Ch}}_\mu(\lambda)
= \alpha^{\frac{|\mu|-\ell(\mu)}{2}} \sum_\rho a^\mu_\rho M_\rho(\lambda) \\
= \sum_\rho \alpha^{\frac{|\mu|-\ell(\mu)-(|\rho|-2\ell(\rho))}{2}} 
a^\mu_\rho \left( \prod_{i \leq \ell(\rho)} \sqrt{\alpha}^{\rho_i-2}
M_{\rho_i}(\lambda) \right).
\end{gathered}$$ The quantities $\alpha^{\frac{|\mu|-\ell(\mu)-(|\rho|-2\ell(\rho))}{2}} 
a^\mu_\rho$ and $\sqrt{\alpha}^{\rho_i-2}
M_{\rho_i}(\lambda)$ are polynomials in $\alpha$ (by Proposition [\[PropBound2\]](#PropBound2){reference-type="ref" reference="PropBound2"} and Lemma [\[LemMkPol\]](#LemMkPol){reference-type="ref" reference="LemMkPol"}), hence $\theta_\mu(\lambda)$ is a polynomial in $\alpha$.
