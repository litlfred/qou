---
doc_id: arxiv-1203.4538v1
doc_title: "The exponential-logarithmic equivalence classes of surreal numbers"
section_id: sec-003-22-sign-sequences
section_title: "Sign sequences."
section_number: 2.2
pages: 6-7
source_pdf: 1203.4538v1.pdf
source_sha256: 5e44909e355c78d6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.988
doc_brief: "The exponential-logarithmic equivalence classes of surreal numbers — 9 sections: Front matter; Introduction.; Preliminaries on surreal numbers."
---
Gonshor obtains in [@gonshor_surreal] detailed results on the sign sequences of the surreals under the various operations and maps. We will use repeatedly his results. Moreover, we introduce in this section some new operations on the sign sequences.

::: defn
-   Given two surreal numbers $a,b\in\textbf{No}$, we define their **concatenation** $a\binampersand b$ as the juxtaposition of their sign sequences. We note that $l(a\binampersand b)=l(a)+l(b)$, the *ordinal sum* of $l(a)$ and $l(b)$.

-   As in [@gonshor_surreal Theorem 9.5], for any surreal number $a\in\textbf{No}$, we can write its sign sequence as the following transfinite concatenation:

    ::: center
    $a=\alpha_0\oplus\binampersand \beta_0\ominus\binampersand \alpha_1\oplus\binampersand \beta_1\ominus\binampersand\cdots$
    :::

    where for any $\mu\in\textbf{On}$ used in this writing of $a$, we have $\alpha_\mu,\ \beta_\mu\in\textbf{On}$ with in particular $\alpha_\mu$ possibly 0 for $\mu=0$ or for any *limit* ordinal $\mu$.

-   Given a surreal number $a\in\textbf{No}$, we denote by $a^+$ the total number of pluses in the sign sequence of $a$ ($a^+\in\textbf{No}$). Therefore is the ordinal sum of the packages of $\oplus$'s: $$a^+=\displaystyle\sum_{\mu}\alpha_\mu= \displaystyle\binampersand_{\mu}(\alpha_\mu \oplus).$$

-   Given a positive surreal number $a\in\textbf{No}_{>0}$, we derive from it the surreal number $\flat a$ obtained by suppressing the first $\oplus$ in the sign sequence of $a$.

    Given a negative surreal number $a\in\textbf{No}_{<0}$, we derive from it the surreal number $\sharp a$ obtained by suppressing the first $\ominus$ in the sign sequence of $a$.

-   Given a surreal number in normal form $\displaystyle\sum_{i<\lambda}\omega^{a_i}.r_i$, we define its corresponding **reduced sequence** $(a_i^0)_{i<\lambda}$ as follows. For any $i<\lambda$, $a_i^0$ is derived from $a_i$ by suppressing in its sign sequence the following $\ominus$'s:

    -   given an ordinal number $\nu\in\textbf{On}$, if $a_i(\nu)=\ominus$ and if there exists $j<i$ such that $a_j(\xi)=a_i(\xi)$ for any $\xi\leq\nu$, then suppress the $\nu$th $\ominus$;

    -   if $i$ is a successor ordinal, $a_{i-1}\binampersand\ominus$ is a truncation of $a_i$ and if $r_{i-1}$ is not a dyadic rationnal number, then suppress the $\ominus$ coming after $a_{i-1}$ in the writing of $a_i$.
:::

Concerning the exponentiation with base $\omega$, we recall [@gonshor_surreal Theorem 5.12 and Corollary 5.1]:

::: thm
[]{#theo:signe-omega label="theo:signe-omega"}

-   Given a surreal number $a=\alpha_0\oplus\binampersand \beta_0\ominus\binampersand \alpha_1\oplus\binampersand \beta_1\ominus\binampersand\cdots$, for any ordinal $\mu\in\textbf{On}$ intervening in the writing of $a$, we set $\gamma_\mu:=\displaystyle\sum_{\lambda\leq\mu}\alpha_\lambda$ (ordinal sum). Then the sign sequence of $\omega^a$ is:

    ::: center
    $\omega^a=\omega^{\gamma_0}\oplus\binampersand \omega^{\gamma_0+1}\beta_0\ominus\binampersand \omega^{\gamma_1}\oplus\binampersand \omega^{\gamma_1+1}\beta_1\ominus\binampersand\cdots$
    :::

-   Given a positive real number $r=\rho_0\oplus\binampersand\sigma_0\ominus\binampersand\cdots$, the sign sequence of $\omega^a.r$ is

    ::: center
    $\omega^a.r=\omega^a\binampersand \omega^{a^+}\flat\rho_0\oplus\binampersand\omega^{a^+}\sigma_0\ominus\binampersand \omega^{a^+}\rho_1\oplus\binampersand\omega^{a^+}\sigma_1\binampersand\cdots$
    :::

    (ordinal multiplication). If $r$ is negative, reverse all the signs in the preceding sequence.

-   Given a surreal number in normal form $\displaystyle\sum_{i<\lambda}\omega^{a_i}.r_i$, its sign sequence is:

    ::: center
    $\displaystyle\binampersand_{i<\lambda}\omega^{a_i^0}.r_i$
    :::

    where $(a_i^0)_{i<\lambda}$ is the corresponding reduced sequence.\
:::
