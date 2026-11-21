---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-001-2-k-negligible-morphisms-and-their-tensor-ideals
section_title: "k-negligible morphisms and their tensor ideals"
section_number: 2
pages: 5-10
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.961
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick ideals."
---
[]{#sec:k-negl label="sec:k-negl"}

## Preliminaries {#sec:prel}

In the following let $R$ be a local ring with maximal ideal $\mathfrak{m}$. We assume $\mathcal C_R$ (or sometimes simply $\mathcal C$) to be a monoidal rigid spherical category whose ${\rm Hom}$ spaces are free $R$-modules and such that $End(\mathbf 1) = R$ (see e.g. [@EGNO Section 4.7] for details). For simplicity we additionally assume that $\mathcal C_R$ is braided. Otherwise we would have to distinguish between left thick ideals and right thick ideals and between partial and modified traces for the left and right versions. However, the followings notions make sense without the added *braided* if one is willing to either work with left or right versions of these.

Recall that under these assumptions there exist, for each object $X$ in $\mathcal C_R$, canonical morphisms $$i_X: {\bf 1}\to X\otimes X^*,\quad \tilde d_X: X\otimes X^* \to {\bf 1}$$ via which we can define the *trace* $Tr_X$ on ${\rm End}(X)$ by $$Tr_X(a)=\tilde d_X (a\otimes id_{X^*})i_X,\quad {\rm for\ all}\ a\in {\rm End}(X);$$ here $i_X$ and $d_{X^*}: X^{**}\otimes X^*\to{\bf 1}$ are the morphisms in the definition of rigidity for the objects $X$ and $X^*$, and $\tilde d_X= d_{X^*}\circ (s_X\otimes 1)$. The isomorphisms $s_X:X\to X^{**}$ from the spherical structure are normalized such that $\ensuremath{\operatorname{dim}}(X)=\ensuremath{\operatorname{dim}}(X^*)$ for all objects $X$ in $\mathcal C$, where $\ensuremath{\operatorname{dim}}(X)=Tr(id_X)$. For elements $a\in {\rm End}(X\otimes Y)$, we can also define the *partial trace* or *conditional expectation* $E_X:{\rm End}(X\otimes Y)\to {\rm End}(X)$ by $$E_X(a)= (id_X\otimes \tilde d_Y)(a\otimes id_{Y^*})(id_X\otimes i_Y).$$ The name *partial trace* is justified by the equation $$Tr_X(E_X(a))=Tr_{X\otimes Y}(a),\quad a\in {\rm End}(X\otimes Y).$$

## Tensor ideals

Let $\mathcal{C}$ be a monoidal category. A *tensor ideal* $\mathcal I$ in $\mathcal{C}$ consists of an $R$-submodule $\mathcal I(X,Y) \subset Hom(X,Y)$ for all $X,Y \in \mathcal C$ such that

-   for all $X,Y,Z,W \in \mathcal C$ and $g \in Hom(X,Y)$ and $h \in Hom(Z,W)$ $$f \in \mathcal I(Y,Z) \text{ implies } f \circ g \in \mathcal I(X,Z) \text{ and } h \circ f \in \mathcal I(Y,W);$$

-   $f \in \mathcal I(X,Y)$ implies $id_Z \otimes f \in \mathcal I(Z \otimes X,Z \otimes Y)$ and likewise from the right.

A collection of objects $I$ in a monoidal category $\mathcal C$ is called a *thick ideal* of $\mathcal C$ if the following conditions are satisfied:

1.  $X\otimes Y\in I$ whenever $X\in\mathcal C$ and $Y\in I$.

2.  If $X\in\mathcal C$, $Y\in I$ and there exist $\alpha:X\to Y$, $\beta:Y\to X$ such that $\beta\circ\alpha={\mathit{id}\hspace{-0.1em}}_X$, then $X\in I$.

To any tensor ideal $\mathcal I$ we can associate the thick ideal $I$ given by $$I = \{ X \in \mathcal C\ | \ id_X \in \mathcal I(X,X) \}.$$

One of the major reasons to study the tensor ideals and thick ideals in $\mathcal C$ is due to the fact that the morphisms that are sent to zero under a monoidal functor $\mathcal C\to \mathcal C'$ to another monoidal category $\mathcal{C}'$ form a tensor ideal; and the objects of $\mathcal C$ that are sent to zero form a thick ideal.

## Generalized negligible morphisms

Let $R$ be a local ring and $\mathcal C_R$ as in section [0.1](#sec:prel){reference-type="ref" reference="sec:prel"}.

::: definition
a\) Let $I \subset R$ be an ideal. We call a morphism $f: X\to Y$ $I$-negligible if $Tr_X(g\circ f)\in I$ and $Tr_Y(f\circ g)\in I$ for all morphisms $g: Y\to X$. An object $X$ is called $I$-negligible if $Tr_X(a)\in I$ for all $a\in {\rm End}(X)$.

b\) If $f$ is $I$-negligible with respect to $I = \mathfrak{m}^k$, we simply say that $f$ is $k$-negligible. An object is $k$-negligible if it is $I$-negligible for $I = \mathfrak{m}^k$.
:::

::: lemma
The $I$-negligible morphisms form a tensor ideal $\mathcal N_I$ in the category $\mathcal C_R$. The $I$-negligible objects form a thick ideal $N_I$ in $\mathcal C_R$.
:::

::: proof
*Proof.* It is easy to see that $\mathcal{N}_I$ is an ideal using $Tr(f\circ g) = Tr(g \circ f)$ for composable morphisms $f:X \to Y$, $g:Y \to X$ [@Kassel Theorem XIV.4.2]. Now let $f \in \mathcal{N}_I(X,Y)$ and $g \in Hom(W,Z)$ arbitrary for $X,Y,W,Z$ in $\mathcal{C}_R$. Let $h \in Hom(Y \otimes Z,X \otimes W)$. Then $$Tr((f \otimes g) \circ h) = Tr(h \circ (f \otimes g)) = Tr(h' \circ f)$$ for some $h': Y  \to X$ (as in [@Barrett-Westbury Theorem 2.9]). Since $f$ is $I$-negligible, this implies $Tr((f \otimes g) \circ h) \in I$.

Let now $X$ be an $I$-negligible object, and $Y$ any object in $\mathcal C$. If $a\in {\rm End}(X\otimes Y)$, we have $$Tr_{X\otimes Y}(a)=Tr_X(E_X(a))\in I,$$ as $E_X(a)\in{\rm End}(X)$ and $X$ is $I$-negligible. Hence $X\otimes Y$ is an object in $N_I$ as well. ◻
:::

::: remark
The definition is similar to the the one of the Jantzen filtration on morphisms defined by the form $Tr(f \circ g)$.
:::

## The mod $\mathfrak{m}$ evaluation

We are primarily interested in categories whose ${\rm Hom}$ spaces are vector spaces over a field. Recall that if $M$ is a free $R$-module of rank $r$, we obtain a well-defined vector space $M/\mathfrak{m}M$ over $\Bbbk=R/\mathfrak{m}$ of dimension $r$. We call the *mod $\mathfrak{m}$ evaluation* (or reduction modulo $\mathfrak{m}$) of $\mathcal C_R$ the category $\mathcal C$ over $\Bbbk$ whose objects are in 1-1 correspondence with the ones of $\mathcal C_R$, and where $$Hom_{\mathcal C}(X,Y)=Hom_{\mathcal C_R}(X,Y)/\mathfrak{m}Hom_{\mathcal C_R}(X,Y) \cong Hom_{\mathcal C_R}(X,Y) \otimes_R R/\mathfrak{m}.$$ In the following, the notations ${\rm Hom}$, ${\rm End}$ etc will refer to the evaluation category $\mathcal C$. The corresponding spaces for $\mathcal C_R$ will be denoted by ${\rm Hom}_R$, ${\rm End}_R$ etc. We call $\mathcal C_R$ a *lift* of $\mathcal C$.

## Examples

We give some examples of the lifting of a monoidal category $\mathcal{C }$ over $\Bbbk$ to a monoidal category over a local ring.

### Fusion categories

Let $\Bbbk$ be any field, $R$ a local ring with $R/\mathfrak{m} \cong k$. If $\mathcal{C}$ is a split fusion category over $\Bbbk$, a lifting of $\mathcal{C}$ in the sense of [@EGNO 9.16] is a split fusion category $\tilde{\mathcal{C}}$ over $R$ such that $\mathcal{C}$ is the mod $\mathfrak{m}$ evaluation of $\tilde{\mathcal{C}}$.

::: theorem
[@EGNO Theorem 9.16.1] If the global dimension of $\mathcal{C}$ is non-zero, $\mathcal{C}$ admits a lifting to $R$ and this lifting is unique up to equivalence.
:::

Of particular interest is the situation where $\Bbbk$ is a perfect field of prime characteristic $p$. Then the ring of Witt vectors $W(k)$ is a discrete valuation ring with maximal ideal generated by $p$ and $W(k)/pW(k) \cong k$. If $\mathcal{C}$ is a non-degenerate (symmetric/braided) fusion category category over $\Bbbk$, then it admits a (symmetric/braided) lifting to $W(k)$ by [@ENO-fusion Theorem 9.3, Corollary 9.4]. Since we are interested here in the construction of tensor ideals, the semisimple case is not relevant to us.

### Algebraic groups {#sec:alg}

While we can define the mod $\mathfrak{m}$ evaluation for any monoidal category over the local ring $R$, it is often not the correct category one is interested in. Consider the case of an algebraic group $G$ over the local ring $R$. Then extension of scalars of $Rep(G,R)$ defines a monoidal functor $$\begin{aligned}
 Rep(G,R) & \to Rep(G \otimes R/\mathfrak{m}, R/\mathfrak{m}) \\ V & \mapsto V \otimes_R R/\mathfrak{m} \\ Hom_G(X,Y) & \mapsto Hom_G(X,Y) \otimes R/\mathfrak{m}.
\end{aligned}$$ The image of $Rep(G,R)$ under this functor is the mod $\mathfrak{m}$ evaluation, but it is not the category $Rep(G \otimes R/\mathfrak{m}, R/\mathfrak{m})$ (unless we are in the semisimple case). Indeed the canonical functor $$Hom_G (M,N) \otimes R/\mathfrak{m} \to Hom_{G_{R/\mathfrak{m}}}(M \otimes R/\mathfrak{m}, N \otimes R/\mathfrak{m}),$$ where $G_{R/\mathfrak{m}}$ is the algebraic group over $\Bbbk$ obtained by extension of scalars, is in general not bijective [@Jantzen 10.14].

### Deligne categories

For every field $\Bbbk$ Deligne [@Deligne-interpolation] defined symmetric monoidal categories $Rep(S_t)$, $Rep(GL_t)$ and $Rep(O_t)$, $t \in k$, which interpolate the representation categories of the symmetric group, the general linear group and the orthogonal group. Each of this categories is constructed in the following way: One defines a skeletal subcategory corresponding to the tensor powers of the permutation representation $V$ of $S_n$, the standard representation $V$ of $O(n)$ or the tensor product $V \otimes V^{\vee}$ of the standard representation $V$ of $GL(n)$ and its dual. The object corresponding to such a tensor power $V^{\otimes r}$ is denoted $r$ in the $S_n$ and $O(n)$-case and $(r,s)$ in the $GL(n)$-case. The endomorphism algebras of these objects are by definition

1.  $End_{Rep(S_t)}(r) = kP_r(t)$, the partition algebra for the parameter $t$.

2.  $End_{Rep(O_t)}(r) = kBr_r(t)$, the Brauer algebra for the parameter $t$.

3.  $End_{Rep(GL_t)}(r,s) = kWB_{r,s}(t)$, the walled Brauer algebra for the parameter $t$.

To get the full category, we take the additive karoubian envelope of the skeletal subcategory. The categories $Rep(S_t)$, $Rep(GL_t)$ and $Rep(O_t)$ admit a lift to the completion of the local ring of evaluable rational functions $R = k[T]_{(T-t)}$ [@Heidersdorf-Wenzl-Deligne]. Indeed the construction described above makes sense over $R$ as well. This can be generalized to inlcude the $q$-deformations of $Rep(O_t)$ and $Rep(GL_t)$.

### Tilting modules

Let $Tilt$ denote the monoidal category of modular/quantized tilting modules. Then $Tilt$ admits a lift to the category of tilting modules over the ring of Witt vectors $W(k)$ (where $\Bbbk$ is a perfect field of characteristic $p > 0$) respectively a lift to the category of tilting modules over the completion of ${\mathbb Q}[v]_{v-q}$. For details we refer the reader to sections [\[tilting-modular\]](#tilting-modular){reference-type="ref" reference="tilting-modular"}, [\[tilting-quantum\]](#tilting-quantum){reference-type="ref" reference="tilting-quantum"} and [\[sec:tilting-eval\]](#sec:tilting-eval){reference-type="ref" reference="sec:tilting-eval"}.

## New tensor ideals

::: lemma
The tensor ideals $\mathcal{N_I}$ of $\mathcal{C}_R$ define tensor ideals in the mod $\mathfrak{m}$ evaluation $\mathcal{C}$. The thick ideals $N_I$ define thick ideals in the mod $\mathfrak{m}$ evaluation. The tensor ideal $\mathcal{N}_1$ corresponds to the ideal of negligible morphisms in $\mathcal{C}$ and the thick ideal $N_1$ corresponds to the indecomposable objects of categorial dimension 0.
:::

In particular we obtain a chain of tensor ideals $$\ldots \subseteq \mathcal{N}_3 \subseteq \mathcal{N}_2 \subseteq \mathcal{N}$$ and likewise a chain of thick ideals $$\ldots \subseteq N_3 \subseteq N_2 \subseteq N.$$

The number $k$ can often be seen as a measure for the vanishing of $\ensuremath{\operatorname{dim}}(X)$. If $X \in N_k$ with $k$ minimal, we say that $X$ has *nullity* $k$. For the explicit meaning of this nullity we refer to the examples that appear later in the article.

::: question
The following question was raised by Kevin Coulembier and Victor Ostrik: Can one find a local ring $R$ such that the $N_J$, where $J$ runs over the ideals of $R$, is a complete list of thick ideals in $\mathcal{C}$? While we do not know the answer, the existence of a lifting to a local ring seems delicate in the non-semisimple case.
:::

## Compatibilities and $k$-semisimplicity

The following lemma follows immediately from the definition.

::: lemma
Let $\mathcal{C}$ be the mod-$\mathfrak{m}$ evaluation of $\mathcal{C}_R$ over the local ring $R$. The diagram $$\xymatrix{ \mathcal{C}_R \ar[r] \ar[d] & \mathcal{C} \ar[d] \\ \mathcal{C}_R/\mathcal{N}_k \ar[r] & \mathcal{C}/\mathcal{N}_k }$$ commutes. In particular $\mathcal{C}/\mathcal{N}_k$ is the mod $\mathfrak{m}$ evaluation of $\mathcal{C}_R/\mathcal{N}_k$.
:::

Since $\mathcal{N}_k \subset \mathcal{N}_{k+1}$ we obtain a chain of full and surjective tensor functors $$\xymatrix{ \ldots \ar[r] \ar[d] & \mathcal{C}_R/\mathcal{N}_3 \ar[r] \ar[d] & \mathcal{C}_R/\mathcal{N}_2 \ar[r] \ar[d] & \mathcal{C}/\mathcal{N} \ar[d] \\ \ldots \ar[r] & \mathcal{C}/\mathcal{N}_3 \ar[r] & \mathcal{C}/\mathcal{N}_2 \ar[r] & \mathcal{C}/\mathcal{N}.  }$$ If $\mathcal C$ is a tensor category so that $\mathcal{C}/\mathcal{N}$ is semisimple, this loosely suggests to interpret $\mathcal{C}/\mathcal{N}_k$ as *$k$-semisimple*. This can be made more precise by considering the trace. Recall [@Deligne-interpolation Proposition 5.7] that a tensor category is semisimple if and only if the trace pairing $Hom(X,Y) \times Hom(Y,X) \to k$ is non-degenerate, i.e. $Tr(fg) = 0$ for all $g:Y \to X$ implies $f=0$. For a morphism $f$ in $\mathcal{C}/\mathcal{N}_k$ the deviation for the failure of the non-degeneracy condition can be seen as an element in $I^{\leq k-1}$ by considering the lift of $f$ in $\mathcal{C}_R/\mathcal{N}_k$.

## A generalization {#sec:general}

If a monoidal functor is full and surjective (on objects), the images of the tensor ideals and thick ideals $\mathcal{N}_k$ are again tensor ideals and thick ideals. Therefore we can more generally define $k$-negligible morphisms and objects provided we have a full and surjective monoidal functor $\mathcal{C}_R \to \mathcal{C}$.

## Monoidal supercategories

The notion of an $I$-negligible ideal and the mod $\mathfrak{m}$ evaluation can be defined in the same way for monoidal supercategories as in [@Brundan-Ellis] [@Coulembier A.1.2]. Examples of monoidal supercategories are the odd Temperley-Lieb supercategory $\mathcal{STL}(\delta), \delta \in k$ of [@Brundan-Ellis Example 1.17], the affine VW supercategory $\mathit{s}\hspace{-0.7mm}\mathop{\mathrm{\bigvee\mkern-15mu\bigvee}}$ [@many-1] and the oriented Brauer-Clifford and degenerate affine oriented Brauer-Clifford supercategories [@Brundan-Comes-Kujawa]. An ideal $J$ in a supercategory is an ideal as in an ordinary category with the extra assumption that $J(X,Y)$ is a graded subgroup of $Hom(X,Y)$ for all $X,Y \in \mathcal{C}$. The notion of a tensor ideal is otherwise unchanged. Thick ideals can be defined as for monoidal categories.
