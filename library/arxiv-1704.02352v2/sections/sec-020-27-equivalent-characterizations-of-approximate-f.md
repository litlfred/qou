---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-020-27-equivalent-characterizations-of-approximate-f
section_title: "Equivalent characterizations of approximate factorization of characters"
section_number: 2.7
pages: 18-23
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.903
latex_coverage_ratio: 0.984
---
The following result, [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"}, is the key tool for the purposes of the current paper. Its main content is part [\[item:afp2\]](#item:afp2){reference-type="ref" reference="item:afp2"}; roughly speaking, it states that each of the four families of numbers [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"}--[\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} can be transformed into the others. Each of these four families describes some convenient aspect of the characters $\chi_n$ in the limit $n\to\infty$. To be more specific:

-   The family [\[eq:AFPCumulants\]](#eq:AFPCumulants){reference-type="eqref" reference="eq:AFPCumulants"} (and its subset, the family [\[eq:AFPCumulants-characters\]](#eq:AFPCumulants-characters){reference-type="eqref" reference="eq:AFPCumulants-characters"}) has a direct probabilistic meaning. It contains information about the cumulants of some random variables which might be handy while proving probabilistic statements such as Central Limit Theorem or Law of Large Numbers.

-   On the other hand, the cumulants appearing in the families [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"} and [\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} are purely algebraic and do *not* have any direct probabilistic meaning. However, their merit lies in the fact that in many concrete applications (such as the ones from [@DolegaSniady-examples-AFP]) it is much simpler to verify algebraic conditions [\[item:AFP-A\]](#item:AFP-A){reference-type="ref" reference="item:AFP-A"} and [\[item:disjoint-cumulants\]](#item:disjoint-cumulants){reference-type="ref" reference="item:disjoint-cumulants"} than their probabilistic counterparts [\[item:cumulants-classic-characters\]](#item:cumulants-classic-characters){reference-type="ref" reference="item:cumulants-classic-characters"} and [\[item:cumulants-classic-polynomial\]](#item:cumulants-classic-polynomial){reference-type="ref" reference="item:cumulants-classic-polynomial"}.

::: theorem
[]{#def:approx-factorization-charactersB label="def:approx-factorization-charactersB"} Assume that $\alpha=\alpha(n)$ is such as in [\[sec:hypothesis-double-scaling\]](#sec:hypothesis-double-scaling){reference-type="ref" reference="sec:hypothesis-double-scaling"}. Assume also that for each integer $n\geq 1$ we are given a reducible Jack character $\chi_n\colon\mathcal{P}_{n}\to\mathbb{R}$.

1.  []{#item:afp2 label="item:afp2"} *Equivalent characterization of approximate factorization property.*

    Then the following four conditions are equivalent:\

    1.  []{#item:AFP-A label="item:AFP-A"} for each integer $\ell \geq 1$ and all integers $l_1,\dots,l_\ell\geq 2$ the limit

        $$\label{eq:AFPPartitions}
                    \lim_{n\to\infty} k^{\chi_n}_\ell (l_1, \dots, l_\ell) \ 
                    n^{\frac{l_1+\cdots+l_\ell+\ell-2}{2}}$$ exists and is finite;

    2.  []{#item:cumulants-classic-characters label="item:cumulants-classic-characters"} for each integer $\ell\geq 1$ and all $x_1,\dots,x_\ell\in\{\mathop{\mathrm{Ch}}_1,\mathop{\mathrm{Ch}}_2,\dots\}$ the limit $$\label{eq:AFPCumulants-characters}
                    \lim_{n\to\infty}    \kappa^{\chi_n}_{\ell}(x_{1},\dots,x_{\ell})\ 
                    n^{- \frac{\deg x_1+ \cdots + \deg x_\ell - 2(\ell-1)}{2}}$$ exists and is finite;

    3.  []{#item:cumulants-classic-polynomial label="item:cumulants-classic-polynomial"} for each integer $\ell\geq 1$ and all $x_1,\dots,x_\ell\in\mathscr{P}$ the limit $$\label{eq:AFPCumulants}
                    \lim_{n\to\infty}    \kappa^{\chi_n}_{\ell}(x_{1},\dots,x_{\ell})\ 
                    n^{- \frac{\deg x_1+ \cdots + \deg x_\ell - 2(\ell-1)}{2}}$$ exists and is finite;

    4.  []{#item:disjoint-cumulants label="item:disjoint-cumulants"} for each integer $\ell\geq 1$ and all $x_1,\dots,x_\ell\in\mathscr{P}_\bullet$ the limit $$\label{eq:AFPDisjointCumulants}
                    \lim_{n\to\infty}    \kappa^{\chi_n}_{\bullet\ell}(x_{1},\dots,x_{\ell})\ 
                    n^{- \frac{\deg x_1+ \cdots + \deg x_\ell - 2(\ell-1)}{2}}$$ exists and is finite.

2.  []{#item:equivalent-enhanced label="item:equivalent-enhanced"}

    Assume that the conditions from part [\[item:afp2\]](#item:afp2){reference-type="ref" reference="item:afp2"} hold true. Furthermore, assume that for $\ell=1$ the rate of the convergence of *any* of the four expressions under the limit symbol in [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"}--[\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} is of the form $$\label{eq:nice-limit}
            \operatorname{const}_1+ \frac{\operatorname{const}_2+o(1)}{\sqrt{n}}$$ in the limit $n \to \infty$ and all choices of $l_1$ (respectively, for all choices of $x_1$); the constants depend on the choice of $l_1$ (respectively, $x_1$).

    Then for $\ell=1$ the rate of convergence of *each* of the four expressions [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"}--[\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} is of the form [\[eq:nice-limit\]](#eq:nice-limit){reference-type="eqref" reference="eq:nice-limit"}.
:::

When $\alpha=1$, part [\[item:afp2\]](#item:afp2){reference-type="ref" reference="item:afp2"} of the above result corresponds to [@Sniady2006c Theorem and Definition 1]. The proof is postponed to [1](#sec:proof-of-key-tool-short){reference-type="ref" reference="sec:proof-of-key-tool-short"}.

# Proof of [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"} {#sec:proof-of-key-tool-short}

In the current section we shall prove the key tool, [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"}.

Additionally, concerning part [\[item:afp2\]](#item:afp2){reference-type="ref" reference="item:afp2"} of [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"} we shall discuss the exact relationship between the limits of the quantities [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"}--[\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} in the case $\ell\in\{1,2\}$. This relationship provides the information about the limit shape of random Young diagrams in [\[theo:lln\]](#theo:lln){reference-type="ref" reference="theo:lln"} as well as about the covariance of the limit Gaussian process describing the fluctuations in [\[theo:clt\]](#theo:clt){reference-type="ref" reference="theo:clt"}.

Concerning part [\[item:equivalent-enhanced\]](#item:equivalent-enhanced){reference-type="ref" reference="item:equivalent-enhanced"} of [\[def:approx-factorization-charactersB\]](#def:approx-factorization-charactersB){reference-type="ref" reference="def:approx-factorization-charactersB"} we shall discuss the exact relationship between the constants which describe the fine asymptotics [\[eq:nice-limit\]](#eq:nice-limit){reference-type="eqref" reference="eq:nice-limit"} of the quantities [\[eq:AFPPartitions\]](#eq:AFPPartitions){reference-type="eqref" reference="eq:AFPPartitions"}--[\[eq:AFPDisjointCumulants\]](#eq:AFPDisjointCumulants){reference-type="eqref" reference="eq:AFPDisjointCumulants"} in the case $\ell=1$. This relationship provides the information about the mean value $\mathbb{E}\Delta_\infty$ of the limit Gaussian process from [\[eq:weak-topology\]](#eq:weak-topology){reference-type="ref" reference="eq:weak-topology"}.

## Approximate factorization property for $\alpha$-polynomial functions

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
