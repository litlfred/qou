---
doc_id: arxiv-0707.2003v2
doc_title: "A geometric model for Hochschild homology of Soergel bimodules"
section_id: sec-006-6-equivariant-formality
section_title: "Equivariant formality"
section_number: 6
pages: 15-20
source_pdf: 0707.2003v2.pdf
source_sha256: 0b8fe37aabeee412
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.729
doc_brief: "A geometric model for Hochschild homology of Soergel bimodules — An important step in the calculation of the triply graded link homology theory of Khovanov and Rozansky is the determination of the"
---
[]{#sec:equiv-form label="sec:equiv-form"}

Now, we will carry out some actual computations of $B$-equivariant cohomology, and thus of Hochschild homology.

Of course, the best setting in which to compute equivariant cohomology of a variety is when that variety (or more precisely, the sheaf one intends to compute the hypercohomology of) is equivariantly formal.

::: deth
[]{#eq-for-def label="eq-for-def"} We call $\mc F\in D^b_T(X)$ on a $T$-variety $X$ equivariantly formal if one of the following equivalent conditions holds:

1.  The $S$ module $\hc_T(X,\mc F)$ is free.

2.  The differentials in the spectral sequence $$\hc(X,\mc F)\otimes\HT\Rightarrow\hc_{T}(X,\mc F)$$ are trivial, that is, if $\hc(X,\mc F)\otimes\HT\cong\hc_{T}(X,\mc
        F)$ as $\HT$-modules.

3.  We have the equality $\dim_\C H^*(X)= \dim_{\C}H^*(X^T)$.
:::

The equivariant formality of the Bott-Samelsons of $\SL n$ has been proven by Rasmussen in different language.

::: prop
If $G=\SL n$ or $\GL n$, the $T$-space $\BSi$ is equivariantly formal for all $\Bi$.
:::

::: proof
*Proof.* By Theorem [\[sec:introduction-1\]](#sec:introduction-1){reference-type="ref" reference="sec:introduction-1"}, $\HH_*(\S{\Bi})$ is free as an $S$-module if and only if $H^*_T(\BS{\Bi})$ is. By [@Ras06 Propositon 4.6], the module $\HH_*(\S{\Bi})$ is free in type $A$, so by Definition/Theorem [\[eq-for-def\]](#eq-for-def){reference-type="ref" reference="eq-for-def"} above $\BSi$ is equivariantly formal. ◻
:::

This in turn implies that $m_*\Cs{\BSi}$ is equivariantly formal, where $m:\BSi\to G$ is the multiplication map. Since all summands of equivariant formal sheaves are themselves equivariantly formal, and each $\IC(\Gw)$ appears as a summand of such a sheaf (if, for example, $\Bi$ is a reduced word for $w$), this completes the proof of Theorem [\[intro-e-f\]](#intro-e-f){reference-type="ref" reference="intro-e-f"} and the first part of Theorem [\[BS-match\]](#BS-match){reference-type="ref" reference="BS-match"}.

While the most obvious consequence of equivariant formality, calculating the equivariant cohomology from ordinary or vice versa, is a rather useful one, it has less obvious ones as well.

::: prop
*(Goresky, Kottwitz, MacPherson [@GKM Theorem 6.3])* If $\mc F$ is equivariantly formal, then the pullback map $$i^*_T:H_T^*(X,\mc F)\to H_T^*(X^T,\mc F)$$ is injective.
:::

As we mentioned earlier, we are interested in the Hochschild homology of Soergel bimodules as a bigraded object (so that we get a triply-graded knot homology theory), but the grading on equivariant hypercohomology is only one of these. From now on, we consider $H^*_T(\Gw)$ as a bigraded $\HT$-module, with the bigrading defined by the isomorphism with Hochschild homology given by Proposition [\[formal-isom\]](#formal-isom){reference-type="ref" reference="formal-isom"}.

::: proof
*Proof of Theorems [\[grading-match\]](#grading-match){reference-type="ref" reference="grading-match"} and [\[BS-match\]](#BS-match){reference-type="ref" reference="BS-match"}.* Since the pullback map $H_T^*(\BSi)\to H_T^*(\BSi^T)$ is induced by a map of Soergel bimodules, it is homogeneous in both gradings. Similarly with the map induced by the inclusion of a summand $\IC(\Gw)\hookrightarrow m_*\Cs{\BSi}$. Thus we need only establish the theorem for $\BSi^T$. As this is a union of complex tori with the trivial action, we need only establish the theorem for $T$.

This case follows immediately from applying $\HH_0$ to the Koszul resolution of $H_{T\times T}(T)\cong S$ as a bimodule over itself. ◻
:::

Let us turn to the case where $\Gw$ is smooth. Since $H^*_T(\Gw)\cong S\otimes H^*(\Gw)$, it will prove very interesting to understand $H^*(\Gw)$. Surprisingly, no description of this cohomology seems to be in the literature, but in fact there is a very beautiful one.

As is well known (and we reprove in the course of Lemma [\[schub-lemma\]](#schub-lemma){reference-type="ref" reference="schub-lemma"} below), there exists a unique decreasing sequence of positive integers $k_1,\cdots k_{n}$ such that the Hilbert series of $H^*(\Gw/B)$ is of the form $$\sum_{i=1}^{\ell(w)}q^{i/2}\dim H^i(\Gw/B)=\prod_{j=1}^n\frac{1-q^{k_j}}{1-q}$$

::: thm
[]{#equiv-form label="equiv-form"} If $\Gw$ is smooth, then as an algebra, $$\label{eq:1}
    H^*(\Gw)\cong \land^{\bullet}(\ga_1,\ldots \ga_n)$$ where $\deg(\ga_i)=2k_i-1$, and as an $\HT$-algebra, $$H^*_T(\Gw)\cong\HH_i(\S w)\cong \HT\otimes H^*(\Gw).$$ In the standard double grading on $\HH_i(\S w)$, we have $\deg(1\otimes \ga_i)=(1,2k_i)$.
:::

This explicitly describes the Hilbert series of $\HH_i(\S w)$, proving a conjecture of Rasmussen.

::: cor
The Hilbert series of $\HH_i(\S w)$ is given by $$\sum_{i,j}a^iq^j \HH_i(\S w)_{2j}=\prod_{\ell=1}^{n}\frac{1+aq^{k_\ell}}{1-q}$$
:::

Since $\dim H^*(\Gw)=2^{\rank G}$, Definition/Theorem [\[eq-for-def\]](#eq-for-def){reference-type="ref" reference="eq-for-def"}(3) establishes the equivariant formality of $\Gw$ independently of the earlier results of this paper (and for all types).

As usual in Lie theory, we define the height $h(\al)=\langle\rho^\vee, \al\rangle$ of a root $\al$ to be its evaluation against the fundamental coweight.

::: lem
[]{#schub-lemma label="schub-lemma"} The cohomology ring $H^*(\Gw/B)$ is a quotient of the polynomial ring $\HT$ by a regular sequence $(f_1,\ldots, f_{n})$. Define $k_i=\deg(f_i)$.

The number of times the integer $m$ appears in the list $k_1,\ldots,
  k_{n}$ is precisely the number of roots in $R^+\cap w^{-1}(R^-)$ of height $m-1$ minus the number of such roots of height $m$, where $R^+$ is the set of positive roots of $G$ and $R^-=-R^+$.
:::

::: proof
*Proof.* For ease, assume $\Gw$ is not contained in a parabolic subgroup. By results of Akyıldız and Carrell [@AC89], the ring $H^*(\Gw/B)$ is a quotient of $\C[BwB/B]$ by a regular sequence of length $\ell(w)$ by a regular sequence $(g_1,\ldots, g_{k})$ where $k=\ell(w)$.

In this grading, $\C[BwB/B]$ is a polynomial algebra generated by elements of degree $2h(\al)$ for each root $\al\in R^+\cap
  w^{-1}(R_-)$, and the degrees of $g_i$ are given by $2h(\al)+2$ as $\al$ ranges over the same roots. Corresponding to the simple roots are $n-1$ generators $x_1,\ldots x_{n}$ of degree 2, which are the first Chern classes of line bundles on $G/B$ corresponding the fundamental weights, and for the other roots we have $\ell(w)-n+1$ other generators $y_n,\cdots y_{\ell(w)}$ of higher degree. Here, we assume these are in increasing order by degree.

It is a well known fact that the cohomology ring $H^*(G/B)$ is generated by the Chern classes $x_i$. Since the natural pullback map $H^*(G/B)\to H^*(\Gw/B)$ is onto, the ring $H^*(\Gw/B)$ is as well. That is, if $p=\deg y_{k}>2$, then $$y_k-\sum_{\deg(g_i)=p}\be_ig_i\in \sum_{\deg(g_j)<p} \HT g_j.$$ Since $y_k\notin \sum_{\deg(g_j)<p}\HT g_j$, we can eliminate $y_k$ and any single relation $g_i$ such that $\be_i\neq 0$. Obviously, $(g_1,\ldots,g_n)\setminus\{g_i\}$ is again a regular sequence in $\C[x_1,\ldots,x_{n},y_n,\ldots, y_{k-1}].$ Applying this argument inductively, we obtain a subsequence $(g_{i_1},\ldots, g_{i_{n}})$ which is regular in $\HT$, which is the desired sequence.

Since the number of relations of degree $j$ which have been eliminated is the number of generators of degree $j$, the remaining number of relations is precisely the difference between these, which is also the number of roots of height $j/2-1$ minus the number of height $j/2$ in $R^+\cap w^{-1}(R^-)$. ◻
:::

::: proof
*Proof of Theorem [\[equiv-form\]](#equiv-form){reference-type="ref" reference="equiv-form"}.* Applying the Hirsch lemma (as stated in the paper [@DGMS]) to the fibration $B\to \Gw\to \Gw/B$, we see that the cohomology ring $H^*(\Gw)$ is the cohomology of the dg-algebra $H^*(\Gw/B)\otimes_\HT\EuScript{K}_T$ where $\EuScript{K}_T$ is the Koszul complex of $\HT$ (the natural free resolution of $\C$ as an $\HT$-module equipped with the Yoneda product).

Since $(f_1,\ldots, f_{n})$ is regular, $H^*(\Gw/B)$ is quasi-isomorphic to the Koszul complex $\EuScript{K}_{\Bf}$. Thus, the cochain complex of $\Gw$ is quasi-isomorphic to $\EuScript{K}_{\Bf}\otimes_\HT\C$. This is just an exterior algebra over $\C$ with generators $\gamma_1,\ldots, \gamma_{n}$ with degree given by $\deg(\gamma_i)=2k_i-1$.

Since we used a Koszul complex, the generators $\ga$ land in Hochschild degree 1 under the restriction map to $T$, so the degree of $\gamma_i$ is $(2k_i,1)$.

If $w\in W'$, where $W'$ is a proper parabolic subgroup of $W$ (with corresponding Levi subgroup $G'\subset G$), and $W'$ is the minimal such parabolic. Then $G_w\cong G'_w\times T/T'\times N\cap
  w_0'Nw_0'$. Since $N\cap w_0'Nw_0'$ is unipotent and thus contractible, by Künneth, we have $$\dim_\C H^*(G_w)\cong \dim_\C H^*(G_{w'})\dim_\C H^*(T/T')=2^{\dim T'}2^{\dim T/T'}=2^{\dim T}. \qedhere$$ Thus, $G_w$ is equivariantly formal and the degrees $k_i$ for $G_w$ are simply those of $G_{w'}$ extended by adding 1's. ◻
:::
