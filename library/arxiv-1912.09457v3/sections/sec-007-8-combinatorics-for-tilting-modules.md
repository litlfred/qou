---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-007-8-combinatorics-for-tilting-modules
section_title: "Combinatorics for tilting modules"
section_number: 8
pages: 22-27
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.983
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick ideals."
---
[]{#sec:combi label="sec:combi"}

By theorem [\[thm:tilting-eval\]](#thm:tilting-eval){reference-type="ref" reference="thm:tilting-eval"} the $k$-negligible ideals are defined for modular and quantum tilting modules. Contrary to the case of Deligne categories, not every thick ideal is one of the $N_k$. We would like to understand the negligible ideals $N_k$ for modular and quantum tilting modules. In both cases the thick ideals are governed by the intricated Kazhdan-Lusztig cell theory of the affine Weyl group which is largely not understood in the modular case. In the following we try to give a more direct geometric description of these cells. While the results in the current section are general, we focus on type A in section [\[sec:a-A\]](#sec:a-A){reference-type="ref" reference="sec:a-A"}.

## Classification of thick ideals {#sec:classif}

We first recall the classification of the thick ideals due to Ostrik and Achar-Hardesty-Riche.

### Ostrik's classification {#quantum-cells}

::: definition
([@Ostrik-ideals] [@Andersen-cells]) For $\lambda,\mu \in X^+$ write $\lambda \leq_q \mu$ if there exists $Q \in  Tilt(U_q(\mathfrak{g}),{\mathbb Q}(q))$ such that $T(\lambda)$ is a summand of $T(\mu) \otimes Q$. If both $\lambda \leq_q \mu$ and $\mu \leq_q \lambda$ write $\lambda \sim_q \mu$. The equivalence classes are called weight cells.
:::

We remark that for any $\lambda \in X^+$ we have $\lambda + \nu \leq_q \lambda$ for all $\nu \in X^+$ since $T(\lambda + \nu)$ is a summand of $T(\lambda) \otimes T(\nu)$. The fundamental alcove $C_{\ell}$ is the unique maximal weight cell in the $\leq_q$ ordering. For a weight cell $\underline{c}$ we denote by $$T(\leq_q \underline{c})$$ the subcategory of objects in $Tilt(U_q(\mathfrak{g}),{\mathbb Q}(q))$ whose objects are direct sums of $T(\lambda)$ with $\lambda$ in a cell $\underline{c}'$ satisfying $c' \leq_q c$. Then $T(\leq_q \underline{c})$ is a thick ideal in $Tilt(U_q(\mathfrak{g}),{\mathbb Q}(q))$.

The division of $X^+$ into weight cells gives a division of $W_{\ell}^+$. Recall that Lusztig and Xi have defined a partition of $W_{\ell}^+$ into right cells along with a right order $\leq_R$ on the set of right cells.

::: theorem
([@Ostrik-ideals]) The weight cells in $X^+$ (and therefore the thick ideals in $Tilt(U_q(\mathfrak{g}),{\mathbb Q}(q))$) correspond to the right cells in $W^+_{\ell}$, i.e. for any right cell $A \in W_{\ell}^+$ the full subcategory $Tilt(U_q(\mathfrak{g}),{\mathbb Q}(q))_{\leq A} \subset Tilt(U_q(\mathfrak{g}),{\mathbb Q}(q))$ of direct sums of tilting modules $T(\lambda)$ for $$\lambda \in \bigcup_{w \in B \leq_R A} \underline{C}_w$$ is a thick ideal.
:::

By [@Ostrik-ideals Remark 5.6] every thick ideal is a sum of ideals of the form $Tilt(U_q(\mathfrak{g}),{\mathbb Q}(q))_{\leq A}$ for a right cell $A$ so that this theorem yields the classification of thick ideals in $Tilt(U_q(\mathfrak{g}),{\mathbb Q}(q))$.

### Thick ideals in the modular case {#sec:modular-cells}

The notion of a weight cell can be defined in complete analogy to the quantum case in section [0.1.1](#quantum-cells){reference-type="ref" reference="quantum-cells"}. We denote the modular analog of the preorder and the equivalence classes by $\leq_T$ and $\sim_T$. An equivalence class is called a *modular weight cell* and $C_p$ is the largest modular weight cell. Contrary to the quantum case there are infinitely many modular weight cells (see section [\[steinberg-cells\]](#steinberg-cells){reference-type="ref" reference="steinberg-cells"}). Any modular weight cell $\underline{c}$ defines a thick ideal $$T(\leq_T c).$$ Ostrik's classification carries over to the modular case if we replace right cells by right $p$-cells (also called anti-spherical right $p$-cells).

::: theorem
([@Achar-Hardesty-Riche Theorem 7.7, Corollary 7.8]) The modular weight cells in $X^+$ (and therefore the thick ideals in $Tilt(G,k)$) correspond to the right $p$-cells in $W^+_p$, i.e. for any right $p$-cell $A \in W_p^+$ the full subcategory $Tilt(G,k)_{\leq A} \subset Tilt(G,k)$ of direct sums of tilting modules $T(\lambda)$ for $$\lambda \in \bigcup_{w \in B \leq_{R,p} A} \underline{C}_w$$ is a thick ideal.
:::

As in the quantum case, every thick ideal is a sum of ideals attached to right $p$-cells.

::: example
By [@Andersen-cells] the set $$\underline{c}_1^r = (p^r-1)\rho + X_{p^r} + p^rC_p$$ is a weight cell which contains $St_r$. We call this weight cell the $r$-th Steinberg cell. We have an equality of thick ideals $<St_r> = T(\leq \underline{c}_1^r)$.
:::

::: remark
Since every thick ideal in the quantum and modular case is a sum of thick ideals attached to right cells, the nullity of a tilting module is constant on an alcove. Indeed, if $T(\lambda)$ is a tilting module in a thick ideal $I$ and $T(\lambda)$ is contained in an alcove $A$, the entire alcove is contained in $I$ since the ideal is a union of weight cells.
:::

## Affine Weyl groups

We review some basic combinatorics in connection with affine Weyl groups and tilting modules. See [@Jantzen], [@JLink] , [@ALink], [@Soergel1], [@Soergel2] and the literature quoted in these papers for more details. The use of facets for Kazhdan-Lusztig combinatorics already appeared before e.g. in [@Goodman-Wenzl].

Let $X_n$ be a finite root system, and let $X_n^{(1)}$ be the root system of the corresponding untwisted affine Weyl group. It has a faithful representation in $\mathfrak h^*$, where the generating reflections for $X_n$ act as usual, and the additional generator acts via the reflection in the hyperplane given by $(\theta, \gamma)=\ell$, where $\ell$ is a positive integer, $\theta$ is the long resp short root of greatest length if $d|\ell$ resp $d\nmid \ell$; here $d$ is the ratio of the square length of a long and a short root.

We obtain a system of hyperplanes on $\mathfrak h^*$ from the orbits of the generating hyperplanes under the affine Weyl group. They can be described explicitly by $$H_{\alpha,k} \ =\ \{ x\in\mathfrak h^*\ | \ (x,\alpha)=k\ell\},\quad \alpha\in \Delta_+, k\in{\mathbb Z},$$ if $d|\ell$. If $d\nmid \ell$, we just replace the roots $\alpha$ by coroots in the definition above. The positive and negative sides of these hyperplanes are defined in the obvious way, replacing the equal sign in the definition by inequality signs. These hyperplanes make $\mathfrak h^*$ into a cell complex as follows: We call an intersection of $k$ hyperplanes maximal if it has dimension $n-k$, and we denote by $\mathfrak h^*(n-k)$ the union of all maximal intersections of $k$ hyperplanes. The set of $j$-cells then is given by all connected components of $\mathfrak h^*(j)\backslash \mathfrak h^*(j-1)$, with $\mathfrak h^*(-1)$ being the empty set.

## Alcoves and facets

As usual, we call the $n$-cells $alcoves$, and lower-dimensional cells $facets$. The $(n-1)$-cells which are in the closure of a given alcove $A$ are called the $walls$ of $A$. The fundamental alcove $C_{\ell}$ is defined to be the unique alcove in the dominant Weyl chamber whose closure contains the origin 0. We say that a wall of $C_{\ell}$ corresponds to the simple reflection $s_i$ if it is fixed by it. This defines a 1-1 correspondence between the walls of $C_{\ell}$ and the simple reflections. We can now define a 1-1 correspondence between the alcoves and the elements $w$ of the affine Weyl group as well as a labeling of the walls via simple reflections by induction on the length of $w$ as follows: The element 1 corresponds to $C_{\ell}$. If the alcove $A$ corresponds to the element $w$, and $s_i$ is a simple reflection such that $ws_i$ has greater length than $w$, then the alcove $A'=As_i$ corresponding to $ws_i$ is obtained by reflecting $A$ in the wall labeled by $s_i$. This reflection also defines the labeling of the walls of $A'$. Moreover, the action of the $s_i$ defines a right action of the affine Weyl group on the alcoves. The alcoves in the dominant Weyl chamber are in 1-1 correspondence with the shortest elements of the cosets of the finite Weyl group in the affine Weyl group. The Bruhat order then has the geometric interpretation that $u<w$ is equivalent to the fact that whenever $u(C_{\ell})$ and $v(C_{\ell})$ lie on opposite sides of a hyperplane, $u(C_{\ell})$ must be on the negative and $w(C_{\ell})$ must be on the positive side of that hyperplane. We similarly define for two facets $F_1$ and $F_2$ that $F_1<F_2$ if $F_2$ lies in or on the positive side of any hyperplane which contains $F_1$.

For a given facet $F$, the stabiliser group $W(F)$ is the group generated by the reflections in the hyperplanes which contain $F$. We denote by $C_{\ell}(F)$ the unique alcove whose closure contains $F$, and which is on the positive side of every hyperplane which contains $F$. The set $\Delta(F)$ denotes the positive roots corresponding to the hyperplanes which contain $F$ and a wall of $C_{\ell}(F)$. By definition, $C_{\ell}(F)$ is on the positive side of each of these hyperplanes. We call the reflections corresponding to the roots in $\Delta(F)$ the simple reflections of $W(F)$, and the roots in $\Delta_F$ the simple roots of $W(F)$. We also define the positive cone $C_+(F)$ to be the region which is above all hyperplanes corresponding to the roots in $\Delta(F)$.

## Tilting modules and linkage

If the context is not specified, the statement holds for tilting modules of quantum groups at roots of unity as well as for tilting modules of algebraic groups in characteristic $p$. Let $T(\lambda)$ be the unique indecomposable tilting module up to isomorphism whose highest weight is $\lambda$. We will use the well-known fact that if the Weyl module $V(\lambda)$ is simple, it coincides with $T(\lambda)$ and with the simple module $L(\lambda)$ of highest weight $\lambda$.

::: theorem
[]{#linkagetheorem label="linkagetheorem"} (Linkage Principle) The Weyl module $V(\mu)$ appears in a filtration of the tilting module $T(\lambda)$ only if $\mu$ is in the orbit of $\lambda$ under the affine Weyl group and $\mu\leq \lambda$ in Bruhat order.
:::

## Minimal facets

The following lemma describes some tilting modules which are simple. We call a facet $F$ $minimal$ if it lies in the $interior$ of the dominant Weyl chamber $C$ and no other facet in its orbit which also lies in the interior of $C$ can be smaller than it in Bruhat order. We then have the following easy lemma:

::: lemma
[]{#minfacet label="minfacet"} Let $F$ be a minimal facet and let $\lambda$ be an integral dominant weight such that $\lambda+\rho\in F$.

\(a\) In both the quantum group case and in the modular case, we have $T(\lambda)=V(\lambda)$ and the nullity of $T(\lambda)$ is equal to $k(F)$, the number of hyperplanes in which $F$ lies.

\(b\) Consider the modular case in characteristic $p$. Let $\lambda^{(r)}=p^r\lambda+(p^{r-1}-1)\rho$. Then $T(\lambda^{(r)})=V(\lambda^{(r)})$ and the nullity of $T(\lambda^{(r)})$ is equal to $r|R^+|+k(F)$.
:::

$Proof.$ By definition of minimal facet and the linkage principle, there exists no dominant integral weight $\mu$ in the orbit of $\lambda$ such that $\mu<\lambda$ in Bruhat order. Hence the only Weyl module which appears in the filtration of $T(\lambda)$ is $V(\lambda)$ itself. The statement about the nullity is a direct consequence of the dimension formula (for $p>h$ in the modular case). The same argument also works for case (b), using Lemma [\[dimmod\]](#dimmod){reference-type="ref" reference="dimmod"}.

## Thick tensor ideals

Let $\mathcal I(F)$ be the thick ideal generated by the tilting modules $T(\lambda)$ with $\lambda+\rho\in F$. Recall that $C_+(F)$ is the region consisting of all points $x\in \mathfrak h^*$ which are on the positive side of any hyperplane which contains $F$.

::: proposition
[]{#tensorexample label="tensorexample"} Let $F$ be a minimal facet, and let $\lambda$ and $\lambda^{(r)}$ be as in Lemma [\[minfacet\]](#minfacet){reference-type="ref" reference="minfacet"}.

\(a\) In the quantum group case, the ideal $\mathcal I(F)$ contains all modules $T(\nu)$ with $\nu+\rho$ in $C_+(F)$. Any module in $\mathcal I(F)$ has nullity $\geq k(F)$.

\(b\) In the modular case, the ideal $\mathcal I(F^{(r)})$ generated by all $T(\lambda^{(r)})$ with $\lambda+\rho\in F$ contains all modules $T(\nu)$ with $\nu\in\lambda^{(r)}+X_+$, where $X_+$ is the set of all dominant all dominant integral weights. Any module in $\mathcal I(F^{(r)})$ has nullity at least $r|R^+|+k(F)$.
:::

::: proof
*Proof.* Assume $\nu+\rho\in C_+(F)$. Then we can find a dominant integral weight $\lambda$ such that $\lambda+\rho\in F$ and $\nu-\lambda$ is a dominant weight. Hence the tensor product $T(\lambda)\otimes T({\nu-\lambda})$ has highest weight $\nu$. It follows that $T_\nu\in \mathcal I(F)$, and hence has at least the nullity of $F$. ◻
:::

::: example
In the modular situation, the case $\lambda = 0$ corresponds to the Steinberg representations $St_r$.
:::

In order to get a more concrete description of these tensor ideals, it will be important to determine when two different facets generate the same tensor ideal.

::: definition
[]{#tensorequivalence label="tensorequivalence"} Let $F_1$ and $F_2$ be minimal facets. We say that they are tensor equivalent if $\mathcal I(F_1)=\mathcal I(F_2)$.
:::

::: lemma
[]{#genequiv label="genequiv"} Let $\mathcal I$ be the tensor ideal generated by the $simple$ object $T$, and let $S$ be an object in $\mathcal I$ with the same nullity as $T$. Then also $S$ generates $\mathcal I$. In particular, if $F_1$ and $F_2$ are tensor equivalent minimal facets, then $k(F_1)=k(F_2)$.
:::

::: proof
*Proof.* By assumption, there exists an object $W$ such that $S\subset T\otimes W$. There exist maps $$\iota: {\bf 1}\to W\otimes  W^*, \quad d: W\otimes  W^*\to {\bf 1}$$ such that $d\circ\iota = \ensuremath{\operatorname{dim}}(W)$. Moreover, by assumption, there exist morphisms $\iota_S: S\to T\otimes W$ and $d_S: T\otimes W\to S$ such that $d_S\circ\iota_S=id_S$. Let $a\in{\rm End}(S)$ such that $Tr(a)$ has minimal nullity. We then define maps $u: T\to S\otimes W^*$ and $v:  S\otimes  W^*
\to T$ by $$u= (d_S\otimes id_{ W^*})\circ (id_T\otimes \iota),\quad v= 
(id_T\otimes d)\circ (\iota_Sa\otimes id_{W^*}).$$ It follows that $vu$ is an endomorphism of the simple object $T$, and hence $vu=\alpha id_T$ for some scalar $\alpha$. By functoriality of the trace operation, it follows from the definitions $$\alpha \ensuremath{\operatorname{dim}}(T) = Tr(vu)=Tr(uv)=Tr(a).$$ As $Tr(a)$ and $\ensuremath{\operatorname{dim}}(T)$ have the same nullity, it follows that $\alpha$ is invertible. But then $\alpha^{-1}uv$ is an idempotent in ${\rm End}(S\otimes \bar W)$ whose image is isomorphic to $T$. ◻
:::

::: corollary
If $F_1>F_2$ and they have the same nullity, then $\mathcal I(F_1)=\mathcal I(F_2)$ and $C_+(F_1)\subset C_+(F_2)$.
:::

::: remark
[]{#nullity-rem label="nullity-rem"} 1. In our cases, the nullity of the tensor ideal would correspond to the length of the longest element of the stabilizer of $F$. On the other hand, it is well-known that the longest element $w_0$ of a parabolic subgroup is in a cell for which the $a$-function is equal to the length of $w_0$. For rank 2 and for type $A_n$, these exhaust all two-sided cells.

2\. All thick ideals are explicitly known in type $A$, see [@Shi]. Each of them can be associated to a parabolic subgroup, and hence to a facet. However, there already seems to be a left cell for type $D_4$ whose value of the $a$-function, seven, would not be the length of the longest element of a parabolic subgroup of affine $D_4$, see [@DuD4], [@ChenD4].
:::
