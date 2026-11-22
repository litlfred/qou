---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-017-33-a-triangular-subsystem
section_title: "A triangular subsystem"
section_number: 3.3
pages: 22-24
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.975
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
In the previous section we explained how to determine the coefficients $a^\mu_\rho$ (where $\rho$ runs over partitions without parts equal to $1$) of $L_\mu$ as the solution of an overdetermined linear system of equations. In this section, we extract from this system a triangular subsystem.

We will need an order on all partitions: let us define $<_1$ as follows: $$\rho <_1 \rho' \iff
\begin{cases}
    & |\rho| <|\rho'|; \\
    \text{or}&|\rho| = |\rho'| \text{ and } \ell(\rho) > \ell(\rho'); \\
    \text{or}&|\rho|= |\rho'|,\ \ell(\rho) = \ell(\rho') \text{ and } \min(\rho) > \min(\rho').
\end{cases}$$

We say that an equation involves a variable if its coefficient is non-zero.

::: lemma
Let $\rho$ be a partition and $q=\min(\rho)$ its smallest part.

-   If $q=2$, set $\tau=\rho\setminus (2)$. Then Equation $(A_\tau)$ involves the variable $a^\mu_\rho$ and involves some of the variables $a^\mu_{\rho'}$ for $\rho' >_1 \rho$ (and no other variables $a^\mu_{\rho'}$).

-   If $q>2$, set $\tau= \rho_{\downarrow q}$. Then Equation $(B_\tau)$ involves the variable $a^\mu_\rho$ and some of the variables $a^\mu_{\rho'}$ for $\rho' >_1 \rho$ (and no other variables $a^\mu_{\rho'}$).

[]{#LemTriangle label="LemTriangle"}
:::

::: proof
*Proof.* We can refine Corollary [\[CorolMlo\]](#CorolMlo){reference-type="ref" reference="CorolMlo"} as follows: for any partition $\rho$, any diagram $\lambda$ and any inner corner $i$ of $\lambda$, $$\begin{gathered}
    M_\rho(\lambda^{(i)}) = M_\rho(\lambda) + \sum_{j \leq \ell(\rho)}
    M_{\rho \setminus \rho_j} 
    \left( \sum_{\substack{g,t \geq 0, \\ g=\rho_j-2-t}} (\rho_j-t-1) M_t(\lambda) z_i^g \right)\\
    + \sum_{\substack{\pi,g \\ |\pi|+g < |\rho| - 2}} b_{g,\pi}^\rho(\gamma) M_\pi(\lambda) z_i^g.
    \label{eq:DsLemTriang}
\end{gathered}$$ Indeed, it is true for $\rho=(k)$ and follows directly for any $\rho$ by multiplication. The right-hand side is a linear combination of $M_\pi z_i^g$ with $$|\pi|+g \leq |\rho| - 2.$$ Moreover equality occurs only if $\pi \cup (g)$ is obtained from $\rho$ by choosing a part, removing $2$ to this part and splitting it in two (possibly empty) parts.

Let us consider the first statement of the lemma. Fix a partition $\rho$ with a smallest part equal to $2$, that is $\rho=\tau \cup (2)$ for some partition $\tau$. Let us determine which variables $a^\mu_{\rho'}$ appear in the left-hand side of Equation $(A_\tau)$. In other terms, we want to determine for which $\rho'$, the difference $M_{\rho'}(\lambda^{(i)})-M_{\rho'}(\lambda)$ contains some term $M_\pi z_i^g$, for which $\tau=\pi \cup (g)$. As explained above, a necessary condition is the inequality $|\tau|=|\pi|+g \leq |\rho'| - 2$, *i.e.* $|\rho'| \geq |\tau|+2$. Moreover, if $|\rho'| = |\tau| +2$, then $\tau$ must be obtained from $\rho'$ by removing $2$ from some part and splitting it into two. In particular, $\rho'$ cannot be longer than $\tau$, unless both new parts are empty. This happens only if the split part of $\rho'$ was $2$, that is if $\rho'= \tau \cup (2)$. We have proved that $(A_\tau)$ can involve $a^\mu_{\rho'}$ only if $\rho'=\rho$ or $\rho' >_1 \rho$ (either $\rho'$ has a bigger size than $\rho$, or it has a smaller length). It is easy to check that the coefficient of $a^\mu_\rho$ is equal to $m_2(\rho)$ (and thus, non-zero), which finishes the proof of the first point.

The proof of the second point is quite similar. Fix a partition $\rho$, denote $q$ its smallest part (assume $q>2$) and $\tau=\rho_{\downarrow q}$. The same argument than above tells us that the variable $a^\mu_{\rho'}$ can appear in the equation $(B_\tau)$ only if $|\tau|=|\pi|+g+1 \leq |\rho'| - 1$, i.e. $|\rho'| \geq |\tau|+1$. Moreover, if there is equality, $\tau$ must be obtained from $\rho'$ by removing $1$ from some part and splitting it into two. One of the two new parts is always non-empty (as $\rho'$ has no parts equal to $1$), thus $\rho'$ is at most as long as $\tau$. If they have the same length, it means that $\tau$ is obtained from $\rho'$ by shortening a part. If this part is equal to $q$, then $\rho'=\rho$. Otherwise $\rho'$ contains a part $q-1$ and thus $\rho' >_1 \rho$ (they have same size and same length). Finally, we have proved that $(B_\tau)$ can involve $a^\mu_{\rho'}$ only if $\rho' >_1 \rho$. Once again, the coefficient of $a^\mu_\rho$ in $(B_\tau)$ is easy to compute: it is equal to $(q-1) m_q(\rho)$ and, hence, non-zero. ◻
:::

The first interesting consequence is the following.

::: corollary
The coefficient $a_\rho^\mu$ is a polynomial in $\gamma$ with rational coefficients. The same is true for the coefficients of Kerov's polynomials $K_\mu$.
:::

::: proof
*Proof.* We proceed by induction over $|\mu|$. The quantities $a_\rho^\mu$ are the solution of a triangular linear system, whose right-hand side is a vector of $a_\tau^{\mu'}$ with $|\mu'|<|\mu|$. By induction hypothesis, the right-hand side belongs to $\mathbb{Q}[\gamma]$. The coefficients $b_{g,\pi}^\rho(\gamma)$ of the system also belong to $\mathbb{Q}[\gamma]$. Moreover, the diagonal coefficients of the system (given in the proof above) are invertible in $\mathbb{Q}[\gamma]$, hence the solution is also in $\mathbb{Q}[\gamma]$.

For the second statement, it is enough to say that each $M_k$ is a polynomial in the $R_k$'s with integer coefficients. ◻
:::

::: remark
Lemma [\[LemTriangle\]](#LemTriangle){reference-type="ref" reference="LemTriangle"} does not hold for Lassalle's system of equation [@Lassalle2009 Equations (9.1) and (9.2)], which computes recursively $K_\mu$.
:::
