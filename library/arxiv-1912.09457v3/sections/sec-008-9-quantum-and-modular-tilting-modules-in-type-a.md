---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-008-9-quantum-and-modular-tilting-modules-in-type-a
section_title: "Quantum and modular tilting modules in type A"
section_number: 9
pages: 27-34
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.984
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick ideals."
---
[]{#sec:typeA label="sec:typeA"}

For $U_q(\mathfrak{sl}_n)$ two-sided cells of the affine Weyl group are parametrized by Young diagrams $\lambda$ of size $n$. We show that the thick ideal $\mathcal{I}(F_0(\lambda))$ agrees with the thick ideal attached to the two-sided cell by work of Shi and Ostrik. This also connects the nullity with the values of Lusztig's $a$-function. We propose a geometric description of the thick ideals for $U_q(\mathfrak{sl}_n)$ and for $SL(n)$. We assume throughout that $\ell$ and $p$ are bigger than the Coxeter number $h$, which is equal to $n$ in our case.

## Description of $\mathcal I(F)$s

We would like to get an elementary geometric description of the region in which the dominant integral weights $\lambda$ lie for which $T(\lambda)$ is in $\mathcal I(F)$, for a given minimal facet. For rank 2 these can be found in [@Lusztig-homepage]. It turns out that the regions corresponding to cells in the dominant Weyl chamber given by Lusztig coincide with the regions described in Proposition [\[tensorexample\]](#tensorexample){reference-type="ref" reference="tensorexample"}. We expect that the regions described in Proposition [\[tensorexample\]](#tensorexample){reference-type="ref" reference="tensorexample"} would also describe cells beyond rank 2. We will illustrate this below for some cases.

The cells for the affine Weyl groups of type $A$ have been determined by Shi in [@Shi]. Using Ostrik's results, this implies that the thick ideals in type $A_{n-1}$ are labeled by the partitions $\lambda$ of the set $\{ 1,2,\ ...,\ n\}$. As usual, we write partitions $\lambda=[\lambda_1,\lambda_2,\ ...\ \lambda_r]$ where the $\lambda_i$ are integers satisfying $\lambda_1\geq \lambda_2\geq\ ...\ \lambda_r >0$. We identify them with Young diagrams, where $\lambda_i$ indicates the number of boxes in the $i$-th row. We denote weights of $\mathfrak{sl}_n$ by the projections of $n$-tuples of integers into the plane of ${\mathbb R}^n$ given by vectors whose coordinate sum is equal to 0. We will usually only write the $n$-tuple of integers for simplicity of notation. We will also use the notation $\lv$ for $\lambda+\rho$.

::: definition
[]{#standardfacet label="standardfacet"} Let $\ell$ be a positive integer, $\ell>n$, and let $s$ be the number of columns of $\lambda$. Then we write the expression $(i-1)\ell+x_{j-1}$ into the box of $\lambda$ in the $i$-th row and $j$-th column, where we have the convention $0=x_0<x_1<\ ...\ < x_{s-1}<\ell$. The *standard facet $F_0(\lambda)$* consists of all $n$-tuples whose coordinates consist of all possible arrangements of numbers in the boxes of $\lambda$, written in descending order.
:::

::: definition
We call a facet $F$ strongly minimal if $F'\not < F$ for any $F'$ with $W(F')\cong W(F)$. Here all facets are assumed to be in the interior of $C$.
:::

::: definition
[]{#simpleroot label="simpleroot"} Let $F$ be a facet. We call $\alpha$ a root of the stabilizer $W(F)$ if there exists an integer $n_\alpha$ such that $(\alpha, x)=n_\alpha\ell$ for every $x\in F$. We call a root $\alpha$ positive if $(\alpha,x)>0$ for all $x\in F$. Finally, we call a collection $R_F^+=\{ \alpha_i\}$ of positive roots of $W(F)$ a set of simple roots of $F$ if every positive root of $W(F)$ can be uniquely written as a linear combination of the $\alpha_i$s with nonnegative integer coefficients.
:::

::: remark
[]{#D(F) label="D(F)"} The simple roots of $W(F)$ allow us an easy description of the region $C_+(F)$: If $(\alpha, y)=n_\alpha\ell$ for all $y\in F$, then $C_+(F)$ consists of all points $x\in\mathfrak h^*$ such that $(\alpha, x)\geq n_\alpha\ell$ for all simple $\alpha\in W(F)$. It is tempting to speculate whether a description of the tensor ideal $\mathcal I(F)$ can be given via the region $$D(F)\ = \bigcup_{W(F')=W(F)} C_+(F'),$$ where it would be enough to only consider strongly minimal facets $F'$ on the right hand side. We study this question in more detail for type $A$ in the following sections.
:::

## More facets

Let $y$ be a point in the interior or lower closure of a given alcove. The following definition will be useful for Shi's algorithm for identifying cells which will be used later.

::: definition
[]{#ychain label="ychain"} Let $y$ be a point in the interior or lower closure of a given alcove. We call a subset $\{ y_i, i\in I\}$ of the coordinates of $y$ a $y$-chain if $|y_i-y_j|\geq \ell$ for all $i,j\in I$. We call it an $\ell$-strict (or just strict) $y$-chain if its elements are of the form $y_i-r\ell$ for $0\leq r < |I|-1$.
:::

Observe that if $y$ is a point in the standard facet $F_0(\lambda)$, the coordinates of $y$ can be written as a disjoint union $\bigcup_j \Gamma_j$ of strict chains where $|\Gamma_j|=\lambda_j^T$. Namely $\Gamma_j$ consists of all the coordinates of $y$ which are congruent to $x_{j-1}$ mod $\ell$, where $x_0=0$.

There is a more general procedure to produce facets from any standard tableau of shape $\lambda$, i.e. for any filling of the boxes of $\lambda$ such that the numbers increase along the rows and down the columns. Let $i(r,c)$ be the number in the box in the $r$-th row and $c$-th column. Then we define the facet $F_t$ by the points $y$ satisfying the equalities $$y_{i(r,c)}-y_{i(r+1,c)}=\ell$$ for any pair of boxes $(r,c)$ and $(r+1,c)$ of our tableau. In general, these equations may describe a collection of facets. In this case, we pick the lowest one. It can be obtained by adding the additional inequalities $y_i-y_{i+1}<\ell$, $1\leq i<n$. We now say that $$\label{faceconjugate}
 F\sim F_0(\lambda)$$ if $F=F_t$ for some standard tableau of shape $\lambda$. We now also define the region $D(\lambda)$ by $$\label{Dlambdadef}
D(\lambda)\ =\ \bigcup_{F\sim F_0(\lambda)} C_+(F).$$

::: remark
1\. Not every minimal facet is of the form $F_t$ for a standard tableau. E.g. for $\mathfrak{sl}_3$ the facet given by $y_2-y_3=\ell$ and $y_1-y_2<\ell$ is minimal, but can not be defined via a standard tableau $t$. However, we will see that any strongly minimal facet can be obtained from a standard tableau.

2\. If $1\leq i\leq n$, we define $\bar i=n+1-i$. If a root $\alpha$ is given by $\alpha(y)=y_i-y_j$, we define the root $\bar\alpha$ by $\bar\alpha(y)=y_{\bar j}-y_{\bar i}$. If $F$ is a facet defined by $\alpha(y)=\ell$ for certain roots $\alpha$, we analogously define the facet $\bar F$ by the same equalities replacing each $\alpha$ by $\bar\alpha$. We leave it to the reader to check that $F_0(\lambda)=\bar F_t$, where $t$ is the standard tableau obtained by filling the boxes of $\lambda$ row by row.
:::

## Identifying minimal facets and their cells

Shi has given several algorithms how to identify the 2-sided cell to which a given alcove belongs. We review one of the here, and another one in the next section, following the presentation in [@Cooper], [@Cooper-journal].

Given a point $y$ in the interior of the dominant Weyl chamber, define a Young diagram $\mu=\mu(y)$ as follows: $\mu_1$ is the maximum of $|\Gamma_1|$, for all possible $y$-chains $\Gamma_1$. Assuming we know $\mu_1$ up to $\mu_i$ we then define $\mu_{i+1}$ by the condition $$\label{mudef}
\sum_{j=1}^{i+1}\ \mu_j\ =\ max\{\ \sum_{j=1}^{i+1} |\Gamma_j|\ \},$$ where the $\Gamma_j$s are mutually disjoint $y$-chains, and the maximum is taken over all possible collection of $i+1$ disjoint $y$-chains.

::: proposition
[]{#identifyideals label="identifyideals"} If $y$ is a point on a facet $F\sim F_0(\lambda)$ for the Young diagram $\lambda$, we have $\mu(y)=\lambda^T$. Moreover, $F_0(\lambda)$ is a minimal facet.
:::

::: proof
*Proof.* Let $y$ be a point on the facet $F$. Let $\Gamma_i$ be the chain consisting of all the entries $y_i$ which are congruent to $i-1$ mod $\ell$; by construction it has $\lambda_i^T$ elements. The claim would follow if we can show that for any other collection of mutually disjoint $y$-chains $\tilde \Gamma_j$ we have $$\sum_{j=1}^{i+1} |\tilde \Gamma_j|\ \leq \ \sum_{j=1}^{i+1} |\Gamma_j|,
\quad {\rm for\ } 0\leq i<n.$$ Let $I(m)$ be the number of indices $k$ for which $m\ell\leq y_k<(m+1)\ell$. Then obviously the number of such indices in a disjoint union of $i$ chains is less or equal to the minimum of $i$ and $I(m)$. Summing over all $m$ from 0 to $n$ shows that the largest possible number we can get is the number of boxes of $\lambda$ in its first $i$ columns. As by induction assumption $\mu_j=\lambda_j^T$ for $1\leq j\leq i$, it follows that $\mu(y)=\lambda^T$.

To prove the second claim, let $y$ be the point on $F_0(\lambda)$ with $x_j=j-1$. Observe that any point $\tilde y\in W.y\cup C$ with $\tilde y\leq y$ needs to have the same $L^1$ norm, it needs to have the same number of coordinates congruent $i$ mod $\ell$ as $y$ for each $i$, and its coordinates need to be positive and strictly decreasing. By construction, the coordinates of $y$ are the smallest possible numbers subject to these constraints. Hence if $\tilde y\neq y$, we could find an $i$ such that $\sum_{j=1}^i \tilde y_j>\sum_{j=1}^i  y_j$, contradicting $\tilde y\leq y$. ◻
:::

## Description of $D(\lambda)$

We now describe a second way how to determine the two-sided cell to which a given alcove in the dominant Weyl chamber belongs. It is also due to Shi. Given a point $y$ in the dominant Weyl chamber, we construct a standard tableau $t_y$ as follows: We start with putting the number 1 into the top-left box. We then add the box with the number 2 on the right if $y_1-y_2<\ell$, and we add it below the first box if $y_1-y_2\geq \ell$. Having placed boxes with the numbers 1 until $i$, we add the box containing $i+1$ at the bottom of the left-most column such that $y_r-y_{i+1}\geq \ell$, where $r$ is the number in the lowest box of that column. Then one can show (see e.g. [@Cooper], Section 3.2 and 3.2):

::: proposition
[]{#Dyalgorithm label="Dyalgorithm"} If $y$ is a dominant integral weight, the procedure above constructs a standard tableau $t_y$. If $\lambda$ is the associated Young diagram, and $y$ is in the lower closure of the alcove $A$, then $A$ is in the two-sided cell labeled by $\lambda^T$.
:::

::: theorem
[]{#Ilambda label="Ilambda"} The indecomposable module $T(\nu)$ is in the ideal $\mathcal I(\lambda)$ generated by the facet $F_0(\lambda)$ if and only if $\nu+\rho$ is in the region $D(\lambda)$ as defined in [\[Dlambdadef\]](#Dlambdadef){reference-type="ref" reference="Dlambdadef"}.
:::

::: proof
*Proof.* It follows from Proposition [\[identifyideals\]](#identifyideals){reference-type="ref" reference="identifyideals"} that whenever $\nu +\rho\in F$ with $F\sim F_0(\lambda)$, then $T(\nu)\in\mathcal I(\lambda)$. Hence $T(\nu)\in\mathcal I(\lambda)$ whenever $\nu+\rho\in D(\lambda)$ by Proposition [\[tensorexample\]](#tensorexample){reference-type="ref" reference="tensorexample"}. To prove the other inclusion, let $T(\nu)$ be an indecomposable tilting module with highest weight $\nu$ such that $\nu+\rho$ is in an alcove belonging to the two-sided cell labeled by $\lambda^T$. Then we obtain a tableau $t_y$ of shape $\lambda$, where $y=\nu+\rho$. Let $i(r,c)$ be the number in the box in the $r$-th row and $c$-th column. Then by construction $y_{i(r,c)}-y_{i(r+1,c)}\geq \ell$. Define $F$ as the set of points $x$ such that $x_{i(r,c)}-x_{i(r+1,c)}= \ell$. This is exactly the facet obtained from $t_y$, see the discussion above [\[faceconjugate\]](#faceconjugate){reference-type="ref" reference="faceconjugate"}. Then obviously $y\in C_+(F)$. ◻
:::

## Examples

In the following we list the *strongly minimal* facets $F$ conjugate (as defined in [\[faceconjugate\]](#faceconjugate){reference-type="ref" reference="faceconjugate"}) to $F_0(\lambda)$ for $\mathfrak{sl}_n$, $n\leq 5$, for each Young diagram $\lambda$ with $n$ boxes. We use the convention that $0<x_1<x_2<\ ...\ <\ell$. The region $C_+(F)$ is then given by all points $y$ satisfying $(y,\alpha)\geq \ell$ for all roots $\alpha$ listed under simple roots. We start with $\mathfrak{sl}_3$, where all strongly minimal facets are standard facets: $$\begin{tabular}{|c|c|c|c|} $\lambda$ & facet & nullity & simple roots\\
\hline
$[3]$ & $(x_2,x_1,0)$ &0&$\emptyset$\\
$[2,1]$ & $(\ell, x_1, 0)$ &1&$\ep_1-\ep_3$\\ 
$[1^3]$&$ (2\ell, \ell, 0)$&3&$\ep_1-\ep_2,\ep_2-\ep_3$\\
\end{tabular}$$ In the following, we list all strongly minimal facets for $\mathfrak{sl}_4$. Observe that we also have a strongly minimal facet which is not a standard facet for the diagram $[2,1^2]$.

$$\begin{tabular}{|c|c|c|c|} $\lambda$ & facet & nullity & simple roots \\
\hline
$[4]$ & $(x_3, x_2,x_1,0)$ &0&$\emptyset$\\
$[3,1]$ & $(\ell, x_2, x_1, 0)$ &1&$\ep_1-\ep_4$\\ 
$[2^2]$&$ (\ell+x_1, \ell, x_1, 0)$&2&$\ep_1-\ep_3, \ep_2-\ep_4$\\
$[2, 1^2]$&$ (2\ell, \ell, x_1, 0)$&3&$\ep_1-\ep_2,\ep_2-\ep_4$\\
&$ (2\ell, \ell+x_1, \ell,  0)$&3&$\ep_1-\ep_3,\ep_3-\ep_4$\\
$[1^4]$&$ (3\ell, 2\ell, \ell, 0)$&6&$\ep_1-\ep_2,\ep_2-\ep_3,\ep_3-\ep_4$\\
\end{tabular}$$ For $\mathfrak{sl}_5$, we will omit the facets corresponding to $[5]$ (the fundamental alcove), to $[4,1]$ (the wall of the fundamental alcove which is not in a reflection plane of the finite Weyl group) and $[1^5]$, which consists of the point $(4\ell, 3\ell, 2\ell, \ell, 0)$ corresponding to the Steinberg module. The remaining facets then consist of

$$\begin{tabular}{|c|c|c|c|} $\lambda$ & facet & nullity \\
\hline
$[3,2]$ & $(\ell+x_1, \ell, x_2,x_1,0)$ &2&$\ep_1-\ep_4, \ep_2-\ep_5$\\
$[3,1,1]$ & $(2\ell,\ell, x_2, x_1, 0)$ &3&$\ep_1-\ep_2,\ep_2-\ep_5$\\ 
 & $(2\ell,\ell+x_1, \ell, x_2,  0)$ &3&$\ep_1-\ep_3,\ep_3-\ep_5$\\
 & $(2\ell,\ell+x_2,\ell+x_1,\ell,  0)$ &3&$\ep_1-\ep_4,\ep_4-\ep_5$\\
$[2^2, 1]$&$ (2\ell, \ell+x_1, \ell, x_1, 0)$&4&$\ep_1-\ep_3,\ep_3-\ep_5, \ep_2-\ep_4$\\
$[2, 1^3]$&$ (3\ell,2\ell, \ell, x_1, 0)$&6&$\ep_1-\ep_2,\ep_2-\ep_3,\ep_3-\ep_5$\\
&$ (3\ell,2\ell, \ell+x_1, \ell,  0)$&6&$\ep_1-\ep_2,\ep_2-\ep_4, \ep_4-\ep_5$\\
&$ (3\ell,2\ell+x_1, 2\ell, \ell,  0)$&6&$\ep_1-\ep_3,\ep_3-\ep_4,\ep_4-\ep_5$\\
\end{tabular}$$

## The $a$-function {#sec:a-A}

Recall from the introduction that Lusztig defined an integer valued function on two-sided cells. In type $A$ there is an easy description of the $a$-function [@Elias-Hogancamp Section 4.2, 5.2]. By [@Shi] the two-sided cells of the affine Weyl group $W$ are parametrized by partitions of $n$. It is well-known that it is sufficient (in type A) to compute the value of the $a$-function in the finite case $W_n = S_n$. By [@Elias-Hogancamp] $$a(\lambda^T) = r(\lambda)$$ where $r(\lambda)$ is the row number of $\lambda$, the sum over the row numbers of the boxes in the Young diagram where the row number of a box in the $i$-th row is $i-1$ (note that we use $\lambda^T$ for the partition labeled by $\lambda$ in [@Elias-Hogancamp]).

::: example
For $n=8$ consider the partition $\lambda = (4,3,1)$. Its row number is $0 + 0 + 0  + 0 + 1 + 1 + 1 + 2 = 5$. Hence the value of the $a$-function on the two-sided cell associated to $\lambda$ is 5.
:::

::: theorem
[]{#TypeAmain label="TypeAmain"} The thick ideal $\mathcal I(\lambda)=\mathcal I(F_0(\lambda))$ generated by the tilting modules $T(\nu)$ for which $\nu+\rho\in F_0(\lambda)$ coincides with the thick ideal constructed by Ostrik for the cell in the dominant Weyl chamber corresponding to the two-sided cell labeled by the Young diagram $\lambda^T$. In particular, the nullity of any generating module $T(\nu)$ of that ideal is equal to the $a$-function of that cell. Moreover, that thick ideal contains all tilting modules $T(\nu)$ for which $\nu+\rho\in D(\lambda)$, as defined below ([\[faceconjugate\]](#faceconjugate){reference-type="ref" reference="faceconjugate"}).
:::

::: proof
*Proof.* Let $T(\nu)$ be a tilting module for which $y=\nu+\rho\in F_0(\lambda)$. As $F_0(\lambda)$ is a minimal facet by Proposition [\[identifyideals\]](#identifyideals){reference-type="ref" reference="identifyideals"}, $T(\lambda)=V(\lambda)$. Hence its nullity can be determined from its dimension, see Corollary [\[modulenullity\]](#modulenullity){reference-type="ref" reference="modulenullity"}. By construction of $F_0(\lambda)$ $y_i$ is congruent $y_j$ mod $\ell$ if $y_i$ and $y_j$ are in the same column of $\lambda$. Hence the nullity is given by $\sum_i \binom{\lambda_i^T-1}{2}$, which is equal to the row number $r(\lambda)$. This shows that the nullity of $F_0(\lambda)$ coincides with the $a$-function.

We have seen in Proposition [\[identifyideals\]](#identifyideals){reference-type="ref" reference="identifyideals"} that if $y\in F$ with $F\sim F_0(\lambda)$ then $\mu(y)=\lambda^T$. Hence any module $T(\nu)$ with $\nu+\rho\in F$ is also in $\mathcal I(\lambda)$. The last statement now follows from Proposition [\[tensorexample\]](#tensorexample){reference-type="ref" reference="tensorexample"}. ◻
:::

::: remark
[]{#a-fun label="a-fun"} It was shown by Ostrik for $\ell$ a large enough prime (see [@Ostrik-dim] [@Ostrik-support]) that the dimension of any tilting module corresponding to a two-sided cell $A$ is divisible by $\ell^{a(A)}$ and for any cell there exists a tilting module such that its dimension is not divisible by $\ell^{a(A)+1}$. Hence the relationship between nullity and $a$-function in Theorem [\[TypeAmain\]](#TypeAmain){reference-type="ref" reference="TypeAmain"} would hold whenever one can show that the nullity of such a module is given by its dimension. So it would seem reasonable to expect this to be true in general. But see the example in Section [\[sec-modularA1\]](#sec-modularA1){reference-type="ref" reference="sec-modularA1"} where the nullity of a modular tilting module is not given by its dimension.
:::

::: remark
[]{#Dlambda-conjecture label="Dlambda-conjecture"} We were able to give a fairly explicit description of the tensor ideals thanks to the work of Shi [@Shi]. In the formulation as $D(F)$, see Remark [\[D(F)\]](#D(F)){reference-type="ref" reference="D(F)"}, our approach might also be useful to characterize tensor ideals for other Lie types. E.g. this formulation works for all rank 2 cases, but not for all ideals for type $D_4$, see Remark [\[nullity-rem\]](#nullity-rem){reference-type="ref" reference="nullity-rem"}.
:::

::: remark
The thick ideal $N_k$ is the sum of the $I(\lambda)$ $(\lambda$ partition of $n$) for which the nullity is $\geq k$.
:::

## Regions for the modular case {#sec:modular-regions}

We can use the results from the previous subsection also for the modular case; to conform with the usual notations, we replace $\ell$ by the prime $p$. In addition, we can use the "telescoping effect\" in Lemma [\[minfacet\]](#minfacet){reference-type="ref" reference="minfacet"} (b) and Proposition [\[tensorexample\]](#tensorexample){reference-type="ref" reference="tensorexample"} (b) to construct infinitely many thick ideals. We will also extend our conjectural description of these ideals and the related cells to this case. We use the same notation as in the previous subsection. Let $F_0(\lambda)$ be the standard minimal facet associated to the Young diagram $\lambda$, and let $r$ be an integer, $r\geq 1$. Then we construct the region $D_r(\lambda)$ by $D_1(\lambda)=D(\lambda)$ and

$$D_r(\lambda)\ =\ \bigcup_{F \sim F_0(\lambda)} (\bigcup_{\lambda\in F} \lambda^{(r)}+X^+), \quad r>1$$ where $\lambda^{(r)}$ is as in Lemma [\[minfacet\]](#minfacet){reference-type="ref" reference="minfacet"} (and $\lambda$ is interpreted as a weight), and the first union goes over all strongly minimal facets $F$ which are equivalent to $F_0(\lambda)$. The following proposition again follows from Lemma [\[minfacet\]](#minfacet){reference-type="ref" reference="minfacet"} and Proposition [\[tensorexample\]](#tensorexample){reference-type="ref" reference="tensorexample"}.

::: proposition
If $\mu+\rho$ is in $D_r(\lambda)$ its nullity is at least equal to $r|R^+|+k(F_0(\lambda))$.
:::

::: question
Is every thick ideal in type A a sum of ideals of the form $D_r(\lambda)$?
:::

An affirmative answer would give a geometric description of the right $p$-cells in the affine Weyl group.

::: remark
[]{#modularguessremark label="modularguessremark"} 1. It is easy to see for $r\geq 1$ that $D_r(\emptyset)=D_{r-1}([1^k])$. We will identify these regions in the following.

2\. For type $A_1$ the thick ideals are generated by the Steinberg modules. It is easy to see that our regions do describe the thick ideals in this case. An explicit description of the tensor ideals has also been given for type $A_2$, see section [0.7.1](#sec:a2){reference-type="ref" reference="sec:a2"}. One checks easily that this is compatible with our regions.
:::

### The modular $A_2$-case {#sec:a2}

By [@Andersen-cells Example 15] [@Jensen-Phd Chapter 10] the thick ideals are given by the the Steinberg cells $<St_r> = T(\leq \underline{c}_1^r)$ and the tilting modules associated to the weight cell $$\underline{c}_2^r = Y_r \setminus (Y_{r+1} \cup \underline{c}_1^r)  \ .$$ A beautiful picture illustrating the $p= 5$-case can be found in [@Andersen-cells] .

In the $\mathfrak{sl_2}$-case we have $<St_r> = N_{r|R^+|}$, so in order to determine the $k$-negligible ideals it suffices to find one weight $\lambda$ in each $c_2^r$ such that the associated tilting module is a Weyl module and compute its nullity with the dimension formula. All in all we obtain

1.  The Steinberg ideals with nullity $3s$ for $s=0,1,2,\ldots$ and

2.  for $s=0,1,2,\ldots$ the ideals generated by the $T(\lambda)$ with $$(\lambda+\rho, \rho)= p^{s+1}, \  (\lambda+\rho, \alpha_1)= rp^s, 1\leq r <p$$ of nullity $3s+1$.
