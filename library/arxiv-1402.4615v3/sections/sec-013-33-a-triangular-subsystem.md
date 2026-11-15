---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-013-33-a-triangular-subsystem
section_title: "A triangular subsystem"
section_number: 3.3
pages: 22-26
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.98
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

## A first bound on the degree {#SubsectBound1}

Recall that $(M_k)_{k \geq 2}$ is an algebraic basis of the ring $\Lambda_\star^{(\alpha)}$ of $\alpha$-polynomial functions on Young diagrams. Hence, we can define a gradation on $\Lambda_\star^{(\alpha)}$ by choosing arbitrarily the degree of each of the generators $M_k$. In this section, we do the following natural choice: $$\deg_1(M_k)=k \qquad \text{for } k\geq 2.$$

Our goal is to obtain a bound on the degree of the polynomial $a^\mu_\rho\in\mathbb{Q}[\gamma]$. We begin by the following lemma concerning the polynomials $b_{g,\pi}^\rho(\gamma)$.

*Notational convention.* To emphasize the difference with gradations on $\Lambda_\star^{(\alpha)}$, we denote throughout the paper degrees of polynomials in $\gamma$ by $\deg_\gamma$.

::: lemma
[]{#lem:firstbound label="lem:firstbound"} Let $\rho$ and $\pi$ be two partitions and $g\geq 0$ be an integer. One has $$\deg_\gamma(b_{g,\pi}^\rho(\gamma)) \leq \deg_1(M_\rho) - \deg_1(M_{\pi \cup (g)}) - 2.$$ Moreover, if the right-hand side is an even (odd, respectively) number, then $b_{g,\pi}^\rho(\gamma)$ is an even (odd, respectively) polynomial. []{#LemDeg1B label="LemDeg1B"}
:::

::: proof
*Proof.* By Proposition [\[PropMkLo\]](#PropMkLo){reference-type="ref" reference="PropMkLo"}, $M_k(\lambda^{(i)})$ can be written as a linear combination of terms of the form $b(\gamma)\ M_\pi\ z_i^g$, where $b$ is some polynomial. We define the pre-degree (with respect to $\deg_1$) of such a term to be the quantity $\deg_\gamma(b) + |\pi| + g$. This degree is multiplicative. Then, $$M_k(\lambda^{(i)}) = M_k(\lambda) + \text{ terms of degree smaller or equal to }k-2.$$ By multiplying this kind of expressions we obtain that $$M_\rho(\lambda^{(i)}) = M_\rho(\lambda) + \text{ terms of degree smaller or equal to }|\rho|-2,$$ which corresponds to our bound on the degree. The parity also follows immediately from the one-part case by multiplication. ◻
:::

This yields the following result.

::: proposition
[]{#PropBound1 label="PropBound1"} The coefficient $a^\mu_\rho$ of $M_\rho$ in Jack character polynomial $L_\mu$ is a polynomial in $\gamma$ of degree smaller or equal to $|\mu|+\ell(\mu) - |\rho|$. Moreover, it has the same parity as the integer $|\mu|+\ell(\mu) - |\rho|$.

The same is true for $K_\mu$.
:::

::: proof
*Proof.* We proceed by induction over $(\mu,\rho)$. The base case $\mu=(1)$ is trivial as $L_{(1)}=M_2$. Fix two partitions $\mu$ and $\rho$. We assume that our result holds for any pair $(\mu',\rho')$ with $|\mu'| < |\mu|$ or $|\mu'|=|\mu|$ and $\rho' >_1 \rho$.

It may seem strange to assume that the result holds for $\rho' \bm{>_1} \rho$. We are indeed doing some kind of *descending induction*. This is possible because, for a given $\mu$, the number of partitions $\rho$ we shall consider is finite: indeed, $a^\mu_\rho=0$ as soon as $|\rho| \geq |\mu|+\ell(\mu)$ [@Lassalle2009 Proposition 9.2 (ii)]. The same remark holds for most proofs in this section.

Let us first consider the case when $\rho=\tau \cup (2)$ contains a part equal to 2. By Lemma [\[LemTriangle\]](#LemTriangle){reference-type="ref" reference="LemTriangle"}, Equation $(A_\tau)$ can be written as: $$m_2(\rho) \cdot a^\mu_\rho = m_1(\mu) a^{\mu \backslash 1}_{\tau} 
    - \sum_{\substack{\pi,g, \\ \pi \cup (g) = \tau}} \sum_{\rho' >_1 \rho}
    b_{g,\pi}^{\rho'}(\gamma) a^\mu_{\rho'}.$$ The first term on the right-hand-side is by convention equal to 0 if $\mu$ does not contain any part equal to 1. If $\mu$ contains a part equal to $1$, as $|\mu \setminus 1|$ is smaller than $|\mu|$, by induction hypothesis $a^{\mu \backslash 1}_{\tau}$ is a polynomial of degree at most $$|\mu \setminus 1| + \ell(\mu \setminus 1) - |\tau| = 
    |\mu|-1 + \ell(\mu)-1-(|\rho|-2)=|\mu|+\ell(\mu) - |\rho|.$$ As $\rho' >_1 \rho$, we can also apply the induction hypothesis to each summand of the second term: $a^\mu_{\rho'}$ is polynomial of degree at most $|\mu|+\ell(\mu)-|\rho'|$. But using Lemma [\[LemDeg1B\]](#LemDeg1B){reference-type="ref" reference="LemDeg1B"}, $b_{g,\pi}^{\rho'}(\gamma)$ has degree at most $|\rho'|-|\pi \cup (g)|-2$. Hence the degree of the product is bounded by $$|\mu|+\ell(\mu) - (|\pi \cup (g)|+2) = |\mu|+\ell(\mu) - |\rho|.$$ The last equality comes from the fact that $\pi \cup (g)=\tau=\rho \setminus 2$.

The proof of the case when the smallest part $q$ of $\rho$ is greater than $2$ is similar. We use Equation $(B_\tau)$ for $\tau=\rho_{\downarrow q}$, which takes the form: $$(q-1) m_q(\rho) \cdot a^\mu_\rho = \sum_{r\geq 2} r \cdot m_r(\mu) a^{\mu_{\downarrow r}}_{\tau} 
    - \sum_{\substack{\pi,g, \\ \pi \cup (g+1) = \tau}} \sum_{\rho' >_1 \rho}
    b_{g,\pi}^{\rho'}(\gamma) a^\mu_{\rho'}.$$ Note that $|\mu_{\downarrow r}|<|\mu|$, therefore by induction hypothesis $a^{\mu_{\downarrow r}}_{\tau}$ is a polynomial in $\gamma$ of degree at most $$|\mu_{\downarrow r}| + \ell(\mu_{\downarrow r}) -|\tau|=|\mu|-1+\ell(\mu)-(|\rho|-1)
    = |\mu|+\ell(\mu) - |\rho|.$$ For the second summand, the argument is the same as before, except that here the equality $|\pi \cup (g)|+2=|\rho|$ comes from the fact that $|\tau|=|\rho|-1$ and $|\tau|=|\pi \cup (g+1)|= |\pi \cup (g)|+1$.

The parity is obtained the same way. ◻
:::

::: corollary
[]{#corol:dominant_deg1 label="corol:dominant_deg1"} For any partition $\mu$ one has: $$\deg_1(\mathop{\mathrm{Ch}}_\mu) = |\mu| + \ell(\mu).$$ Moreover $$\mathop{\mathrm{Ch}}_\mu = \prod_{i}R_{\mu_i+1} + \text{lower degree terms with respect to $\deg_1$}.$$
:::

::: proof
*Proof.* By Proposition [\[PropBound1\]](#PropBound1){reference-type="ref" reference="PropBound1"}, $\mathop{\mathrm{Ch}}_\mu$ has at most degree $|\mu|+\ell(\mu)$ (this has also been proved by Lassalle [@Lassalle2009 Proposition 9.2 (ii)]) and its component of degree $|\mu|+\ell(\mu)$ does not depend on $\alpha$. Hence the result follows as this dominant term is known in the case $\alpha=1$ (see for example [@SniadyGenusExpansion Theorem 4.9]). ◻
:::
