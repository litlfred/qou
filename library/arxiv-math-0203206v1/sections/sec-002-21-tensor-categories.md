---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-002-21-tensor-categories
section_title: "Tensor Categories"
section_number: 2.1
pages: 3-6
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.968
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
[]{#ss-categ label="ss-categ"} For the definitions of categories, functors and natural transformations we refer, e.g., to [@cwm]. In this subsection we briefly recall some of the less standard notions of category theory which will be needed here, others will be introduced as we proceed. We may occasionally say 'arrows' instead of 'morphisms' in order to avoid confusion with algebra homomorphisms. All categories which we consider are essentially small, i.e. equivalent to a small category. We mostly speak of 'tensor categories' rather than 'monoidal categories' but cannot avoid the adjective 'monoidal'. In view of the coherence theorems for (braided, symmetric) tensor categories we may assume all tensor categories to be strict, satisfying $X\otimes(Y\otimes Z)=(X\otimes
Y)\otimes Z$ for all $X,Y,Z$. Following widespread use, we also consider the tensor categories of vector spaces as strict, appealing to the canonical isomorphisms to identify $X\otimes(Y\otimes Z)$ with $(X\otimes Y)\otimes Z$. We often write $XY$ in the place of $X\otimes Y$. By ${\cal H}$ we mean the strictification of $\mathrm{Hilb}$. (We also suppress all other canonical isomorphisms in $\mathrm{Hilb}$, identifying $B(H\otimes K)=B(H)\otimes B(K)$.) Note, however, that one cannot assume all tensor functors to be strict without losing generality. Thus we need the following.

::: defin
[]{#d-mon-func label="d-mon-func"} Let ${\cal C}, {\cal D}$ be (strict) tensor categories. A functor $F: {\cal C}\rightarrow{\cal D}$ is weakly monoidal if there exist morphisms $d_{X,Y}: F(X)\otimes F(Y)\rightarrow F(X\otimes Y)$ for all $X,Y\in{\cal C}$ and a morphism $e: {\bf 1}_{\cal D}\rightarrow F({\bf 1}_{\cal C})$ such that

1.  The morphisms $d_{X,Y}$ are natural w.r.t. both arguments.

2.  For all $X,Y,Z\in{\cal C}$ the following diagram commutes:

    ::: diagram
    F(X)F(Y)F(Z) & \^d\_X,Y\_F(Z) & F(XY)F(Z)\
    \^\_F(X)d\_Y,Z & & \_d\_XY,Z\
    F(X)F(YZ) & \_d\_X, YZ & F(XYZ)
    :::

3.  The following compositions are the identity morphisms of $F(X)$

    ::: diagram
    F(X) F(X)\_D & \^\_F(X)e & F(X)F(**1**\_C) & \^d\_X,**1** & F(X\_C) F(X)
    :::

    ::: diagram
    F(X) \_DF(X) & \^e\_F(X) & F(**1**\_C)F(X) & \^d\_**1**,X & F(**1**\_CX) F(X)
    :::

    for all $X\in{\cal C}$.

The functor $F$ is monoidal if $e$ and all the $d_{X,Y},\ X,Y\in{\cal C}$ are isomorphisms. If ${\cal C},{\cal D}$ are tensor $*$-categories and $F$ is $*$-preserving, the isomorphisms $e, d_{X,Y}$ are required to be unitary.
:::

We will mainly be interested in linear categories over the complex field. Viz., for all $X,Y$, $\mathrm{Mor}(X,Y)$ is a complex vector space, and the compositions $\circ,\otimes$ of morphisms are bilinear. All functors are supposed ${\mathbb C}$-linear. A *$*$-operation* on a ${\mathbb C}$-linear (tensor) category ${\cal C}$ is a map which assigns to an arrow $s\in\mathrm{Mor}(X, Y)$ another arrow $s^*\in\mathrm{Mor}(Y,X)$. This map has to be antilinear, involutive ($s^{**}=s$), contravariant ($(s\,\circ\, t)^*=t^*\,\circ\,s^*$) and, if ${\cal C}$ is monoidal, monoidal ($(s\times t)^*=s^*\times t^*$). A $*$-operation is *positive* iff $s^*\,\circ\,s=0$ implies $s=0$. A (tensor) $*$-category is a ${\mathbb C}$-linear (tensor) category with a positive $*$-operation. A morphism $s:X\rightarrow Y$ is an isometry iff it satisfies $s^*\circ s=\mathrm{id}_X$. A morphism $s$ is unitary iff $s$ and $s^*$ are isometries. A functor $F$ between $*$-categories is $*$-preserving if $F(s^*)=F(s)^*$ for every morphism $s$.

An object $Z$ is a direct sum of $X_1,X_2$, denoted $Z\cong X_1\oplus X_2$, if there are isometries $s_i: X_i\rightarrow Z, i=1,2$ such that $s_1\circ s_1^*+s_2\circ s_2^*=\mathrm{id}_Z$. A $*$-category 'has direct sums' if for every pair $X_1, X_2$ there exists a direct sum. An object $Y$ is a subobject of $X$ if there exists an isometry $s:Y\rightarrow X$. A $*$-category 'has subobjects' if for every $p=p\circ p=p^*\in\mathrm{End}(X)$ there exist $Y$ and an isometry $s:Y\rightarrow X$ such that $s\circ s^*=p$. An object $X$ in a ${\mathbb C}$-linear category is irreducible if it is non-zero and $\mathrm{End}\,X={\mathbb C}\,\mathrm{id}_X$.

::: defin
A $*$-category is semisimple if it has finite dimensional spaces of morphisms, a zero object, direct sums and subobjects. A tensor $*$-category is semisimple if, in addition, the tensor unit ${\bf 1}$ is irreducible.
:::

In a semisimple $*$-category ${\cal C}$, $\mathrm{End}(X)$ is a finite dimensional $C^*$-algebra for every $X$, and every object is a finite direct sum of irreducible objects. (It is well-known that a category which is semisimple in our sense is abelian and semisimple in the usual sense, i.e. all exact sequences split.)

Let ${\cal C}$ be a tensor $*$-category and $X\in{\cal C}$. A 'solution of the conjugate equations' is a triple $(\overline{X},r,\overline{r})$, where $\overline{X}\in{\cal C}$ and $r:{\bf 1}\rightarrow\overline{X}\otimes X,\ \overline{r}:{\bf 1}\rightarrow X\otimes\overline{X}$ satisfy $$\begin{aligned}
\overline{r}^*\otimes\mathrm{id}_X\,\circ\,\mathrm{id}_X\otimes r &=&\mathrm{id}_X, \\
   r^*\otimes\mathrm{id}_{\overline{X}}\,\circ\,\mathrm{id}_{\overline{X}}\otimes\overline{r} &=&\mathrm{id}_{\overline{X}}.
\end{aligned}$$ A tensor $*$-category ${\cal C}$ 'has conjugates' if there is a solution of the conjugate equations for every $X\in{\cal C}$. A solution $(X,r,\overline{r})$ is normalized iff $r^*\circ r=\overline{r}^*\circ\overline{r}$. It is a standard solution iff there are irreducible objects $X_i, i\in I_X$, solutions $(\overline{X_i},r_i,\overline{r}_i)$ of the conjugate equations and isometries $v_i: X_i\rightarrow X, w_i: \overline{X_i}\rightarrow\overline{X}, i\in I_X$ satisfying $$v_i^*\,\circ\,v_j=\delta_{ij}\,\mathrm{id}_{X_i}, \quad\quad\sum_i v_i\,\circ\,v_i^*=\mathrm{id}_X,$$ similar equations for $w_i$, and we have

$$r=\sum_i w_i\otimes v_i\,\circ\,r_i, \quad \overline{r}=\sum_i v_i\otimes w_i\,\circ\,\overline{r_i}.$$ We define the (intrinsic or categorical) dimension $d(X)\in{\mathbb R}_+$ of $X$ by $r^*\circ r=d(X)\mathrm{id}_{\bf 1}$ where $(\overline{X},r,\overline{r})$ is a normalized standard solution. One can prove the following facts, cf. [@LR]. The dimension is additive under direct sums and multiplicative under tensor products. It takes values in the set $\{ 2\cos\frac{\pi}{n}, n=3,4,\ldots \}\cup[2,\infty)$, in particular $d(X)\ge 1$ with $d(X)=1$ iff $X\otimes\overline{X}\cong{\bf 1}$ iff $X$ is invertible, i.e. there exists $Y$ such that $X\otimes Y\cong{\bf 1}$. If $d(X)=1$ then $X$ is irreducible. In the category ${\cal H}$ of Hilbert spaces we have $d_{\cal H}(H)=\dim_{\mathbb C} H$.

We briefly comment on a somewhat more general setting. A $C^*$-(tensor) category is a (tensor) $*$-category where $\mathrm{Mor}(X,Y)$ is a Banach space for every pair $(X, Y)$ of objects and the norms satisfy $\|X^*\,\circ\,X\|=\|X\|^2$. A $W^*$-category is a $C^*$-category where every $\mathrm{Mor}(X,Y)$ is the dual of a Banach space for every pair $(X,Y)$. In a $C^*$-category with conjugates and irreducible tensor unit all spaces of morphisms are finite dimensional. This is useful in applications where this finite dimensionality is not known a priori, like in quantum field theory. Conversely, every $*$-category which is semisimple in our sense is a $W^*$-category, cf. [@mue06]. In a $W^*$-category, every morphism $s: X\rightarrow Y$ has a polar decomposition $s=pu$, where $p$ is positive and $u$ a partial isometry. As a consequence, whenever $\mathrm{Mor}(X,Y)$ contains a split monic (or isomorphism), it also contains an isometry (respectively, unitary). This shows that most of the above definitions, e.g., of direct sums, are equivalent to the the usual ones as given, e.g., in [@cwm].

If ${\cal C}$ is a semisimple tensor $*$-category we denote the set of isomorphism classes of irreducible objects by $I_{\cal C}$. Let $(X_i, i\in I_{\cal C})$ be a complete set of irreducible objects and write $d_i=d(X_i)$. We have $0\in I_{\cal C}$ such that $X_0\cong{\bf 1}$. If ${\cal C}$ has conjugates, $I_{\cal C}$ comes with an involution $i\mapsto\bar{\imath}$ such that $X_{\bar{\imath}}$ is a conjugate of $X_i$. For $i,j,k\in I_{\cal C}$ we define $N_{ij}^k=\dim\mathrm{Mor}(X_k,X_i\otimes X_j)$. These numbers satisfy the following properties.

1.  For every pair $(i,j)$ there are only finitely many $k\in I_{\cal C}$ such that $N_{ij}^k\ne 0$. We have $X_i\otimes X_j\cong\bigoplus_{k\in I_{\cal C}} N_{ij}^k\,X_k$ and thus $d_id_j=\sum_k N_{ij}^k d_k$.

2.  $\displaystyle\sum_l N_{ij}^l N_{lk}^m = \sum_n N_{in}^m N_{jk}^n$ for all $i,j,k,m\in I_{\cal C}$.

3.  $\displaystyle N_{ij}^k=N_{k\overline{\jmath}}^i=N_{ \overline{\imath}k}^j=N_{\overline{k}i}^{\overline{\jmath}}=N_{j\overline{k}}^{\overline{\imath}}=N_{\overline{\jmath},
    \overline{\imath}}^{\overline{k}}$ for all $i,j,k\in I_{\cal C}$.

4.  $\displaystyle N_{ij}^0=\delta_{i,\overline{\jmath}}$.

5.  If ${\cal C}$ is braided, cf. Section [\[s-braid\]](#s-braid){reference-type="ref" reference="s-braid"}, then $N_{ij}^k=N_{ji}^k$ for all $i,j,k\in
    I_{\cal C}$.
