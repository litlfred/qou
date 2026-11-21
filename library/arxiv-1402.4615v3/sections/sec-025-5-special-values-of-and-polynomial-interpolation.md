---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-025-5-special-values-of-and-polynomial-interpolation
section_title: "Special values of and polynomial interpolation"
section_number: 5
pages: 33-37
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.992
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
[]{#SectSpecialValues label="SectSpecialValues"}

## Case $\alpha=1$: symmetric group algebra {#SubsectStructA1}

In the case $\alpha=1$, the structure constants considered in the previous section are linked with the symmetric group algebra. Let $\mathfrak{S}_{n}$ denote the symmetric group of size $n$, *i.e.* the group of permutations of the set $[n]:=\{1,\dots,n\}$. Recall that the cycle-type of a permutation $\sigma \in \mathfrak{S}_{n}$ is the integer partition $\mu \vdash n$ obtained by sorting the lengths of the cycles of $\sigma$. We consider the group algebra $\mathbb{Q}[\mathfrak{S}_{n}]$ of $\mathfrak{S}_{n}$ over the rational field $\mathbb{Q}$. Its center $Z(\mathbb{Q}[\mathfrak{S}_{n}])$ is spanned linearly by the conjugacy classes, that is the elements $$\mathcal{C}_\mu = \sum_{\substack{\sigma \in \mathfrak{S}_{n}, \\ \text{cycle-type}(\sigma)=\mu}} \sigma.$$ By a classical result of Frobenius (see [@Frobenius1900] or [@Macdonald1995 (I,7.8)]), for any $\lambda \vdash n$, $$\frac{\mathop{\mathrm{Tr}}\rho^\lambda(\mathcal{C}_\mu)}{\text{dimension of $\rho^\lambda$}} = \theta_\mu^{(1)}(\lambda),$$ where $\rho^\lambda$ is the irreducible representation of the symmetric group associated to the Young diagram $\lambda$. In other words: $\theta_\mu^{(1)}$ is the image of $\mathcal{C}_\mu$ by the abstract Fourier transform, which is an algebra morphism. Hence, the structure constants of the algebra $Z(\mathbb{Q}[\mathfrak{S}_{n}])$ with the basis $(\mathcal{C}_\mu)_{\mu \vdash n}$ coincide with $c^{(1)}_{\mu,\nu;\pi}$.

These structure constants have been widely studied in the last fifty years in algebra and combinatorics (they count some families of graphs embedded in orientable surfaces). A famous result in this topic is due to Farahat and Higman [@FarahatHigmanCentreQSn Theorem 2.2]: the quantity $c^{(1)}_{\mu 1^{n-|\mu|},\nu 1^{n-|\nu|};\pi 1^{n-|\pi|}}$ is a polynomial in $n$. Note that this is a consequence of Proposition [\[PropStructureTheta\]](#PropStructureTheta){reference-type="ref" reference="PropStructureTheta"}.

Besides, structure constants of the center of $Z(\mathbb{Q}[\mathfrak{S}_{n}])$ have a well-known and obvious combinatorial interpretation.

::: lemma
Let $\mu$, $\nu$ and $\pi$ be three partitions of the same integer $n$. Fix a permutation $\sigma$ of cycle-type $\pi$. Then $c^{(1)}_{\mu,\nu;\pi}$ is the number of pairs of permutations $(\sigma_1,\sigma_2)$, such that $\sigma_1$ has cycle-type $\mu$, $\sigma_2$ has cycle-type $\nu$ and $\sigma_1 \cdot \sigma_2=\sigma$. []{#lem:Interpretation_StructureConstants_A1 label="lem:Interpretation_StructureConstants_A1"}
:::

This can be used to compute $c^{(1)}_{\mu,\nu;\pi}$ in some particular cases, which will be useful later.

::: lemma
[]{#lem:SC1 label="lem:SC1"} We have the following identities:

1.  []{#eq:SC1-1 label="eq:SC1-1"} $c^{(1)}_{\mu, \nu; 1^n} = 0$ for any $\mu \neq \nu$;

2.  []{#eq:SC1-2 label="eq:SC1-2"} $c^{(1)}_{(k 1^n),(k 1^n);(1^{k+n})} = \binom{k+n}{k} (k-1)!$.
:::

::: proof
*Proof.* Consider the first item. The only permutation $\pi$ of cycle type $(1^n)$ is $\sigma=\mathop{\mathrm{id}}$. Hence, the condition $\sigma_1 \cdot \sigma_2=\sigma$ corresponds to $\sigma_2=\sigma_1^{-1}$ and in particular $\sigma_1$ and $\sigma_2$ must have the same cycle-type.

Consider now the second item. As before, we must choose $\sigma=\mathop{\mathrm{id}}$. As $\sigma_2=\sigma_1^{-1}$ has always the same cycle-type as $\sigma_1$, the coefficient $c^{(1)}_{(k 1^n),(k 1^n);(1^{k+n})}$ is simply the number of permutations of $k+n$ of type $(k 1^n)$. This is well-known [@SaganSymmetric equation (1.2)] to be $$\frac{(k+n)!}{z_{(k 1^n)}}=\binom{k+n}{k} (k-1)!. \qedhere$$ ◻
:::

::: remark
The quantities $g^{(1)}_{\mu,\nu;\pi}$ also have a direct combinatorial interpretation in terms of partial permutations, see [@IvanovKerovPartialPermutations].
:::

## Case $\alpha=2$: Hecke algebra of $(\mathfrak{S}_{2n},H_n)$ {#SubsectHecke}

An analogous interpretation of the structure constants exists in the case $\alpha=2$. We explain it here, following the development given in [@GouldenJacksonMapsZonal].

We can view the elements of the symmetric group $\mathfrak{S}_{2n}$ as permutations of the following set: $\{1,\bar{1},\dots,n,\bar{n}\}$. A subgroup formed by permutations $\sigma$ such that $$\overline{\sigma(i)} = \sigma(\overline{i})\qquad \text{for } i\in\{1,\dots,n\},$$ where by convention $\overline{\bar{j}}=j$, is called *hyperoctahedral group* and is denoted by $H_n$. We consider the subalgebra $\mathbb{Q}[H_n \backslash \mathfrak{S}_{2n} / H_n] < \mathbb{Q}[\mathfrak{S}_{2n}]$ of the elements invariant by multiplication on the left or on the right by any element of $H_n$; in other words $$x \in \mathbb{Q}[H_n \backslash \mathfrak{S}_{2n} / H_n] \stackrel{\text{\tiny def}}{\iff}
h x h'=x \quad \text{for all }h,h' \in H_n.$$ A non-trivial result is that this algebra is commutative.

The equivalence classes for the relation $x \sim hxh'$ (for $x \in \mathfrak{S}_{2n}$ and $h,h' \in H_n$) are called *double-cosets*. They are naturally indexed by partitions of $n$, see [@Macdonald1995 (VII,2)]. We denote by $\mathcal{C}^{(2)}_\mu \in \mathbb{Q}[H_n \backslash \mathfrak{S}_{2n} / H_n]$ the sum of all elements in the double coset corresponding to $\mu$. The family $(\mathcal{C}^{(2)}_\mu)_{\mu \vdash n}$ is a basis of $\mathbb{Q}[H_n \backslash \mathfrak{S}_{2n} / H_n]$.

One can show (see [@GouldenJacksonMapsZonal Equation (3) and (5)]) that there exist some orthogonal idempotents $E_\lambda$ such that: $$\mathcal{C}^{(2)}_\mu = 2^n n! \sum_{\lambda \vdash n} \theta_\mu^{(2)}(\lambda)\ E_\lambda,$$ and one has $$\begin{gathered}
    \mathcal{C}^{(2)}_\mu \cdot \mathcal{C}^{(2)}_\nu
= (2^n n!)^2 \sum_{\lambda \vdash n} \theta_\mu^{(2)}(\lambda)\ \theta_\nu^{(2)}(\lambda)\ E_\lambda\\
= (2^n n!)^2 \sum_{\pi \vdash n} \sum_{\lambda \vdash n} c_{\mu,\nu;\pi}^{(2)}\
\theta_\pi^{(2)}(\lambda)\ E_\lambda
=  (2^n n!) \sum_{\pi \vdash n} c_{\mu,\nu;\pi}^{(2)}\ \mathcal{C}^{(2)}_\pi.
\end{gathered}$$ Hence, the structure constants $h_{\mu,\nu;\pi}$ of the algebra $\mathbb{Q}[H_n \backslash \mathfrak{S}_{2n} / H_n]$ for the basis $(\mathcal{C}^{(2)}_\mu)_{\mu \vdash n}$ are, up to a factor $2^n n!$, the same as the ones of the algebra $\mathcal{F}(\mathcal{Y}_n,\mathbb{Q})$ with the basis $(\theta_\mu^{(2)})_{\mu \vdash n}$.

In particular, Proposition [\[PropStructureTheta\]](#PropStructureTheta){reference-type="ref" reference="PropStructureTheta"} implies the following, result, which is an analog of Farahet and Higman's result [@FarahatHigmanCentreQSn] (a combinatorial proof of the polynomiality has recently been given by O. Tout in [@Tout-Structure-constant-S2n-Hn]).

::: proposition
Let $\mu$, $\nu$ and $\pi$ be partitions without parts equal to $1$. The renormalized structure constant of the algebra $\mathbb{Q}[H_n \backslash \mathfrak{S}_{2n} / H_n]$ $$\frac{h_{\mu 1^{n-|\mu|},\nu 1^{n-|\nu|};\pi 1^{n-|\pi|}}}{n!\ 2^n\ \sqrt{2}^{d(\mu,\nu,\pi)}}$$ is a polynomial in $n$ of degree at most $d(\mu,\nu,\pi)$. Moreover, its coefficient of $n^{d(\mu,\nu,\pi)}$ is the same as in $c^{(1)}_{\mu 1^{n-|\mu|},\nu 1^{n-|\nu|};\pi 1^{n-|\pi|}}.$ In particular,

-   when $|\mu|-\ell(\mu) + |\nu|-\ell(\nu)=|\pi| - \ell(\pi)$, one has $$\frac{h_{\mu 1^{n-|\mu|},\nu 1^{n-|\nu|};\pi 1^{n-|\pi|}}}{n!\ 2^n}=
                c^{(1)}_{\mu 1^{n-|\mu|},\nu 1^{n-|\nu|};\pi 1^{n-|\pi|}}$$ and this quantity is independent of $n$ ;

-   when $|\mu|-\ell(\mu) + |\nu|-\ell(\nu)=|\pi| - \ell(\pi) - 1$, $$\frac{h_{\mu 1^{n-|\mu|},\nu 1^{n-|\nu|};\pi 1^{n-|\pi|}}}{n!\ 2^n}$$ is independent of $n$.
:::

::: proof
*Proof.* The claim that the renormalized structure constant mentioned above is a polynomial and the bound on its degree follow from Proposition [\[PropStructureTheta\]](#PropStructureTheta){reference-type="ref" reference="PropStructureTheta"} specialized to $\alpha=2$. The dominant coefficient is a polynomial in $\gamma$ of degree $0$, so it is the same for $\gamma \in \{0, -1/\sqrt{2}\}$, that is $\alpha \in \{1,2\}$. The first item follows immediately.

In the second item, we consider the case $d(\mu,\nu,\pi)= 1$. So, $$\frac{h_{\mu 1^{n-|\mu|},\nu 1^{n-|\nu|};\pi 1^{n-|\pi|}}}{n!\ 2^n\ \sqrt{2}}$$ is an affine function of $n$ with the same linear coefficient as $c^{(1)}_{\mu 1^{n-|\mu|},\nu 1^{n-|\nu|};\pi 1^{n-|\pi|}}$. But the latter is identically equal to $0$. Indeed, the fact that the sign of permutations is a group morphism implies that $$c^{(1)}_{\mu 1^{n-|\mu|},\nu 1^{n-|\nu|};\pi 1^{n-|\pi|}}=0$$ whenever $d(\mu,\nu;\pi)$ is odd. ◻
:::

Besides, Goulden and Jackson [@GouldenJacksonMapsZonal] described the coefficients $h_{\mu,\nu; \pi}$ combinatorially. Let $\mathcal{F}_\mathcal{S}$ be the set of all (perfect) matchings on a set $\mathcal{S}$, that is partitions of $\mathcal{S}$ in pairs. When $\mathcal{S}$ is the set $\{1,2\dots,2n\}$, we also denote $\mathcal{F}_\mathcal{S}$ by $\mathcal{F}_n$.

For $F_1,F_2 \in \mathcal{F}_\mathcal{S}$, let $G(F_1,F_2)$ be the multigraph with vertex-set $\mathcal{S}$ whose edges are formed by the pairs in $F_1,\dots,F_k$. Because of the natural bicoloration of the edges, the connected components of $G(F_1, F_2)$ are cycles of even length. Let the list of their lengths in weakly decreasing order be $(2\theta_1, 2 \theta_2, \dots) = 2\theta$, and define $\Lambda$ by $\Lambda(F_1, F_2) = \theta$.

::: lemma
[]{#lem:ZonalSC label="lem:ZonalSC"} Let $F_1, F_2$ be two fixed matchings in $\mathcal{F}_n$ such that $\Lambda(F_1,F_2) = \pi$, where $\pi \vdash n$. Then, for any $\mu, \nu \vdash n$ we have $$h_{\mu,\nu;\pi} = 2^n n! |\{F_3 \in \mathcal{F}_n: \Lambda(F_1, F_3) = \mu, \Lambda(F_2, F_3) = \nu\}|.$$ In particular $$c^{(2)}_{\mu,\nu;\pi} = |\{F_3 \in \mathcal{F}_n: \Lambda(F_1, F_3) = \mu, \Lambda(F_2, F_3) = \nu\}|.$$
:::

From this lemma one can evaluate some special cases of structure constants which will be helpful in the next subsection.

::: lemma
[]{#lem:SC2 label="lem:SC2"} We have the following identities:

1.  []{#eq:SC2-1 label="eq:SC2-1"} $c^{(2)}_{\mu, \nu; 1^n} = 0$ for any $\mu \neq \nu$;

2.  []{#eq:SC2-2 label="eq:SC2-2"} $c^{(2)}_{(k 1^n),(k 1^n);(1^{k+n})} = \binom{k+n}{k}2^{k-1}(k-1)!$.
:::

::: proof
*Proof.* The first item is immediate from Lemma [\[lem:ZonalSC\]](#lem:ZonalSC){reference-type="ref" reference="lem:ZonalSC"}, since whenever $F_1$ and $F_2$ are matchings such that $\Lambda(F_1,F_2) = 1^n$ then clearly $F_1 = F_2$.

Let $F_1, F_2$ be two fixed matchings such that $\Lambda(F_1,F_2) = (1^{k+n})$ (hence $F_1 = F_2$). We are looking for the number of matchings $F_3$ such that $\Lambda(F_1,F_3)=\Lambda(F_2,F_3)=(k 1^n)$. Of course, as $F_1=F_2$, it is the number of matchings $F_3$ with $\Lambda(F_1,F_3)=(k 1^n)$. This number does not depend on $F_1$. Using [@NousZonal Lemma 2.4], we know that the numbers of pairs $(F,F_3)$ with $\Lambda(F,F_3)=(k 1^n)$ is given by $$\frac{(2n+2k)!}{z_{(k 1^n)} 2^{n+1}}.$$ As there are $\frac{(2n+2k)!}{2^{n+k} (n+k)!}$ matchings in $\mathcal{F}_{n+k}$, that is possible values for $F$, for a fixed $F_1$, the number of matchings $F_3$ with $\Lambda(F_1,F_3)=(k 1^n)$ is $$\frac{2^{n+k} (n+k)!}{z_{(k 1^n)} 2^{n+1}}=\binom{k+n}{k}2^{k-1}(k-1)!.\qedhere$$ ◻
:::
