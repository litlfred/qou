---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-026-31-approximate-factorization-property-for--polyn
section_title: "Approximate factorization property for -polynomial functions"
section_number: 3.1
pages: 20-23
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.904
latex_coverage_ratio: 0.968
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
::: definition
Let $\mathcal{A}$ and $\mathcal{B}$ be filtered, commutative, unital algebras and let $\mathbb{E}:\mathcal{A}\rightarrow\mathcal{B}$ be a unital map. We say that $\mathbb{E}$ has *approximate factorization property* if for all choices of $x_1,\dots,x_\ell\in\mathcal{A}$ we have that $$\label{eq:approximate-factorization-property}
    \deg_{\mathcal{B}} \kappa_{\mathcal{A}}^{\mathcal{B}}(x_1,\dots,x_\ell) \leq \left( \deg_{\mathcal{A}} x_1 \right) + \cdots + \left( \deg_{\mathcal{A}} x_\ell \right)- 2(\ell-1).$$
:::

We consider the filtered unital algebras $\mathscr{P}_\bullet$ and $\mathscr{P}$ from [\[sec:polynomial-disjoint\]](#sec:polynomial-disjoint){reference-type="ref" reference="sec:polynomial-disjoint"}, and as a conditional expectation between them we take the identity map:

$$\label{eq:commutative-diagram-A}
\begin{tikzpicture}[node distance=2cm, auto, baseline=-0.8ex]
\node (A) {$\mathscr{P}_\bullet$};
\node (B) [right of=A] {$\mathscr{P}.$};

\draw[->] (A) to node {$\mathop{\mathrm{id}}$} (B);
\end{tikzpicture}$$

We denote by $\kappa_{\bullet}:=\kappa_{\mathscr{P}_\bullet}^{\mathscr{P}}$ the conditional cumulants related to the conditional expectation [\[eq:commutative-diagram-A\]](#eq:commutative-diagram-A){reference-type="eqref" reference="eq:commutative-diagram-A"}.

We are now ready to state the main auxiliary result, proved very recently by the second-named author, which will be necessary for the proof of the key tool, [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"}.

::: theorem
[]{#theo:factorization-of-characters label="theo:factorization-of-characters"} The identity map [\[eq:commutative-diagram-A\]](#eq:commutative-diagram-A){reference-type="eqref" reference="eq:commutative-diagram-A"}

has approximate factorization property.
:::

## Approximate factorization for $\alpha=1$

We denote by $\mathscr{P}^{(1)}$ a version of the filtered algebra of $\alpha$-polynomial functions $\mathscr{P}$ obtained by the specialization $\alpha:=1$, $\gamma:=0$; analogously we denote by $\mathscr{P}^{(1)}_\bullet$ the algebra $\mathscr{P}^{(1)}$ equipped with the multiplication given by the disjoint product.

The following result has been proved earlier by the second-named author.

::: theorem
[]{#theo:aprox-fact-property-oldversion label="theo:aprox-fact-property-oldversion"} The identity map

$$\label{eq:commutative-diagram-Aprim}
    \begin{tikzpicture}[node distance=2.3cm, auto, baseline=-0.8ex]
    \node (A) {$\mathscr{P}^{(1)}_\bullet$};
    \node (B) [right of=A] {$\mathscr{P}^{(1)}.$};
    
    
    \draw[<-,swap] (A) to node {$\mathop{\mathrm{id}}$} (B);
    
    
    \end{tikzpicture}$$

has approximate factorization property.
:::

Theorems [\[theo:factorization-of-characters\]](#theo:factorization-of-characters){reference-type="ref" reference="theo:factorization-of-characters"} and [\[theo:aprox-fact-property-oldversion\]](#theo:aprox-fact-property-oldversion){reference-type="ref" reference="theo:aprox-fact-property-oldversion"} are of the same flavor. There are two major differences between them: firstly, the arrows in [\[eq:commutative-diagram-A\]](#eq:commutative-diagram-A){reference-type="eqref" reference="eq:commutative-diagram-A"} and [\[eq:commutative-diagram-Aprim\]](#eq:commutative-diagram-Aprim){reference-type="eqref" reference="eq:commutative-diagram-Aprim"} point in the opposite directions; secondly, the algebra $\mathscr{P}$ is more rich than its specialized version $\mathscr{P}^{(1)}$, in particular the variable $\gamma\in\mathscr{P}$ is not treated like a scalar since $\deg \gamma=1 >0$.

## Proof of [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"}, part [\[item:afp2\]](#item:afp2){reference-type="ref" reference="item:afp2"} {#sec:detailed}

This proof follows closely its counterpart from the work of the second-named author [@Sniady2006c Theorem and Definition 1] with the references to [\[theo:aprox-fact-property-oldversion\]](#theo:aprox-fact-property-oldversion){reference-type="ref" reference="theo:aprox-fact-property-oldversion"} replaced by [\[theo:factorization-of-characters\]](#theo:factorization-of-characters){reference-type="ref" reference="theo:factorization-of-characters"} and, occasionally, the roles of $\mathscr{P}$ and $\mathscr{P}_\bullet$ reversed. We present the details below.

### Proof of the equivalence [\[item:AFP-A\]](#item:AFP-A){reference-type="ref" reference="item:AFP-A"}$\iff$[\[item:disjoint-cumulants\]](#item:disjoint-cumulants){reference-type="ref" reference="item:disjoint-cumulants"}.

The quantities [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"} and [\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} coincide with their counterparts from the work of the second-named author [@Sniady2006c Eqs. (12) and (13)]. The equivalence of the conditions [\[item:AFP-A\]](#item:AFP-A){reference-type="ref" reference="item:AFP-A"} and [\[item:disjoint-cumulants\]](#item:disjoint-cumulants){reference-type="ref" reference="item:disjoint-cumulants"} was proved in [@Sniady2006c Section 4.7].

### Proof of the equivalence [\[item:cumulants-classic-characters\]](#item:cumulants-classic-characters){reference-type="ref" reference="item:cumulants-classic-characters"}$\iff$[\[item:cumulants-classic-polynomial\]](#item:cumulants-classic-polynomial){reference-type="ref" reference="item:cumulants-classic-polynomial"}.

The implication [\[item:cumulants-classic-polynomial\]](#item:cumulants-classic-polynomial){reference-type="ref" reference="item:cumulants-classic-polynomial"}$\implies$[\[item:cumulants-classic-characters\]](#item:cumulants-classic-characters){reference-type="ref" reference="item:cumulants-classic-characters"} is immediate since $\mathop{\mathrm{Ch}}_1,\mathop{\mathrm{Ch}}_2,\ldots\in\mathscr{P}$.

The following result was proved by the second-named author [@Sniady2006c Corollary 19] (note that the original paper does not contain the assumption [\[eq:lost-assumption\]](#eq:lost-assumption){reference-type="eqref" reference="eq:lost-assumption"} without which it is not true). The proof did not use any specific properties of the filtered algebra $\mathscr{P}$ and thus it remains valid also in our context when the original *algebra of polynomial functions* is replaced by *the algebra of $\alpha$-polynomial functions*.

::: lemma
[]{#lem:Sniady2006-recycled-zombie label="lem:Sniady2006-recycled-zombie"} Assume that $X\subseteq \mathscr{P}$ is a set with the property that each $z\in\mathscr{P}$ can be expressed as a polynomial in the elements of $X$: $$\label{eq:takie-jednomiany-lubie}
    z= \sum_{1\leq i \leq n}  z_{i,1} \cdots z_{i,l_i}$$ for some $n\geq 0$ and $z_{i,j}\in X$ in such a way that such that for each value of $1\leq i\leq n$ $$\label{eq:lost-assumption}
    \deg z \geq  \deg z_{i,1}+ \cdots +\deg z_{i,l_i};$$ in other words the degree of each monomial should be bounded from above by the degree of $z$.

Under the above assumption, if condition [\[item:cumulants-classic-characters\]](#item:cumulants-classic-characters){reference-type="ref" reference="item:cumulants-classic-characters"} holds true for all $x_1,\dots,x_\ell\in X$ then more general condition [\[item:cumulants-classic-polynomial\]](#item:cumulants-classic-polynomial){reference-type="ref" reference="item:cumulants-classic-polynomial"} holds true for arbitrary $x_1,\dots,x_\ell\in \mathscr{P}$.
:::

We claim that the set $X=\{\gamma,\mathop{\mathrm{Ch}}_1,\mathop{\mathrm{Ch}}_2,\mathop{\mathrm{Ch}}_3,\dots\}$ generates the filtered algebra $\mathscr{P}$ in the way specified in [\[lem:Sniady2006-recycled-zombie\]](#lem:Sniady2006-recycled-zombie){reference-type="ref" reference="lem:Sniady2006-recycled-zombie"}. Indeed, by the way the filtration on $\mathscr{P}$ was defined (cf. [\[def:polynomial-functions\]](#def:polynomial-functions){reference-type="ref" reference="def:polynomial-functions"}) it is enough to check the assumption of [\[lem:Sniady2006-recycled-zombie\]](#lem:Sniady2006-recycled-zombie){reference-type="ref" reference="lem:Sniady2006-recycled-zombie"} for $z=\gamma^k \mathop{\mathrm{Ch}}_{\pi}$ for integer $k\geq 0$ and a partition $\pi=(\pi_1,\dots,\pi_\ell)$; we will do it by induction over $\deg z=k+|\pi|+\ell$. We write $$z=  \gamma^k \mathop{\mathrm{Ch}}_{\pi_1}\cdots \mathop{\mathrm{Ch}}_{\pi_\ell} + \left[  \gamma^k \mathop{\mathrm{Ch}}_{\pi} - \gamma^k \mathop{\mathrm{Ch}}_{\pi_1}\cdots \mathop{\mathrm{Ch}}_{\pi_\ell} \right].$$ The first summand on the right-hand side is of the form which is fits the framework given by the right-hand side of [\[eq:takie-jednomiany-lubie\]](#eq:takie-jednomiany-lubie){reference-type="eqref" reference="eq:takie-jednomiany-lubie"}. By [@DolegaFeray2014 Corollary 2.5, Corollary 3.8], the second summand on the right-hand side is of smaller degree, thus the inductive hypothesis can be applied. This concludes the proof.

We claim that [\[eq:AFPCumulants-characters\]](#eq:AFPCumulants-characters){reference-type="eqref" reference="eq:AFPCumulants-characters"} holds true for all $x_1,\dots,x_\ell\in X$. Indeed, in the case when $x_1,\dots,x_\ell\in\{\mathop{\mathrm{Ch}}_1,\mathop{\mathrm{Ch}}_2,\dots\}$ this is just the assumption [\[item:cumulants-classic-polynomial\]](#item:cumulants-classic-polynomial){reference-type="ref" reference="item:cumulants-classic-polynomial"}. Consider now the remaining case when $x_j=\gamma$ for some index $j$. For $\ell=1$ the corresponding expression from [\[eq:AFPCumulants\]](#eq:AFPCumulants){reference-type="eqref" reference="eq:AFPCumulants"} is equal to $$\kappa^{\chi_n}_{1}(\gamma)\ 
n^{- \frac{1}{2}} =\frac{\gamma}{\sqrt{n}}$$ which by [\[eq:double-scaling-refined\]](#eq:double-scaling-refined){reference-type="eqref" reference="eq:double-scaling-refined"} converges to a finite limit, as required. For $\ell\geq 2$, the corresponding cumulant $$\kappa^{\chi_n}_{\ell}(\dots,\gamma,\dots)=0$$ vanishes because it involves a deterministc random variable $\gamma$. It follows immediately that the limit [\[eq:AFPCumulants\]](#eq:AFPCumulants){reference-type="eqref" reference="eq:AFPCumulants"} exists.

In this way we verified that the assumptions of [\[lem:Sniady2006-recycled-zombie\]](#lem:Sniady2006-recycled-zombie){reference-type="ref" reference="lem:Sniady2006-recycled-zombie"} are fulfilled. Condition [\[item:cumulants-classic-polynomial\]](#item:cumulants-classic-polynomial){reference-type="ref" reference="item:cumulants-classic-polynomial"} follows immediately.

### Proof of the equivalence [\[item:cumulants-classic-polynomial\]](#item:cumulants-classic-polynomial){reference-type="ref" reference="item:cumulants-classic-polynomial"}$\iff$[\[item:disjoint-cumulants\]](#item:disjoint-cumulants){reference-type="ref" reference="item:disjoint-cumulants"}.

The proof will follow closely the ideas from [@Sniady2006c Section 4.7] with the roles of the cumulants $\kappa^{\chi_n}$ and $\kappa^{\chi_n}_{\bullet}$ interchanged. The original proof was based on the observation that the conditional cumulants (denoted in the original work [@Sniady2006c] by the symbol $k^{\operatorname{id}}=\kappa_{\mathscr{P}^{(1)}}^{\mathscr{P}_\bullet^{(1)}}$) related to the map [\[eq:commutative-diagram-Aprim\]](#eq:commutative-diagram-Aprim){reference-type="eqref" reference="eq:commutative-diagram-Aprim"} fulfill the degree bounds [\[eq:approximate-factorization-property\]](#eq:approximate-factorization-property){reference-type="eqref" reference="eq:approximate-factorization-property"} given by the approximate factorization property. By changing the meaning of the symbol $k^{\operatorname{id}}$ and setting $k^{\operatorname{id}}:=\kappa^{\mathscr{P}}_{\mathscr{P}_\bullet}=\kappa_{\bullet}$ to be the conditional cumulants related to the map [\[eq:commutative-diagram-A\]](#eq:commutative-diagram-A){reference-type="eqref" reference="eq:commutative-diagram-A"} and by applying [\[theo:factorization-of-characters\]](#theo:factorization-of-characters){reference-type="ref" reference="theo:factorization-of-characters"} we still have in our more general context that the cumulants $k^{\operatorname{id}}$ fulfill the degree bounds [\[eq:approximate-factorization-property\]](#eq:approximate-factorization-property){reference-type="eqref" reference="eq:approximate-factorization-property"}. The reasoning from [@Sniady2006c Section 4.7] is still valid in our context.
