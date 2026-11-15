---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.959
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick ideals."
---
## Negligible morphisms

We are interested in the structure of tensor ideals [@Coulembier] [@Balmer] [@Boe-Kujawa-Nakano-tensor] [@Comes-Heidersdorf] in a rigid spherical monoidal category $\mathcal{C}$ over a field $\Bbbk$. Roughly speaking we have two notions of tensor ideals:

-   *tensor ideals*, submodules $\mathcal{I}(X,Y) \subset Hom_{\mathcal{C}}(X,Y)$ (for any $X,Y \in \mathcal{C}$) that are closed under composition and tensor products with morphisms;

-   *thick (tensor) ideals*, subsets of $ob(\mathcal{C})$ which are closed under tensor products with arbitrary objects of $\mathcal{C}$ and also closed under retracts.

Arguably the most important tensor ideal is the tensor ideal of negligible morphisms $$\mathcal{N}(X,Y) = \{ f:X \to Y \ |  \ Tr(f \circ g) = 0  \ \ \forall g:Y \to X \}.$$ By [@Andre-Kahn] it is the largest proper tensor ideal of $\mathcal{C}$, and the only tensor ideal such that the categorial quotient $\mathcal{C}/\mathcal{N}$ can be semisimple. Its associated thick ideal $$N = \{ X \in \mathcal{C} \ |  \ X \cong 0 \in \mathcal{C}/\mathcal{N} \}$$ consists of direct sums of indecomposable objects $X$ whose categorial dimension $\ensuremath{\operatorname{dim}}(X) = 0$ vanishes (the negligible objects).

## Generalized negligible morphisms

It is the aim of this article to present a generalization of the notion of negligible morphism which will lead to a measure - the *nullity*  - for the negligibility of an object $X \in \mathcal{C}$. While $\mathcal{N}$ and $\ensuremath{\operatorname{dim}}(X)$ can always be defined under our assumptions on $\mathcal{C}$, the definition of the generalized negligible tensor ideals $\mathcal{N}_I$ and the nullity requires more restrictive conditions.

In order to define these tensor ideals, we consider a deformation or lift of $\mathcal{C}$ to a monoidal category $\mathcal{C}_R$ over a local ring $R$ as follows. Let $\mathcal{C}_R$ denote a monoidal rigid spherical category whose ${\rm Hom}$ spaces are free $R$-modules satisfying $End(\mathbf 1) = R$. For any ideal $I$ of $R$ we put $$\mathcal{N}_I (X,Y) = \{ f: X\to Y \ |  \  Tr_X(g\circ f)\in I \text{ and }Tr_Y(f\circ g)\in I \ \forall g: Y\to X \},$$ the tensor ideal $I$-negligible morphisms in $\mathcal{C}_R$. An object $X \in \mathcal{C}_R$ is called $I$-negligible if $Tr_X(a)\in I$ for all $a\in {\rm End}(X)$. For a fixed ideal $I$ we can also say that $f:X \to Y$ is $k$-negligible with respect to $I$ if $Tr(f \circ g)$ is in $I^k$. We will only use this in the special situation where $I = \mathfrak{m}$, the maximal ideal of $R$. We then obtain the $k$-*negligible morphisms* $\mathcal{N}_k := \mathcal{N}_{\mathfrak{m}^k}$ which form a decreasing chain $$\mathcal{N}_1 \supset \mathcal{N}_2  \supset \mathcal{N}_3 \supset \ldots$$ of tensor ideals in $\mathcal{C}_R$ and likewise for the $N_k$.

In order to define these for the category $\mathcal{C}$ over $\Bbbk$ we suppose now that we have a surjective and full tensor functor $\mathcal{C}_R \to \mathcal{C}$ with $\Bbbk = R/\mathfrak{m}$. A special case of this is if $\mathcal{C}$ is the mod $\mathfrak{m}$ evaluation of $\mathcal{C}_R$: here the objects of $\mathcal{C}$ are the same as those of $\mathcal{C}_R$ with $$Hom_{\mathcal{C}} (X,Y) = Hom_{\mathcal{C}_R} (X,Y)/ \mathfrak{m} Hom_{\mathcal{C}_R} (X,Y) \cong Hom_{\mathcal{C}_R} (X,Y) \otimes_R R/\mathfrak{m}.$$

When passing from $\mathcal{C}_R$ to $\mathcal{C}$, the images of the $\mathcal{N}_I$ and $N_I$ define tensor ideals and thick ideals in $\mathcal{C}$ respectively (possibly zero if we are not in the special situation of the mod $\mathfrak{m}$ evaluation) which we denote again by $\mathcal{N}_I$ and $N_I$ (or $\mathcal{N}_k$ and $N_k$). Note that $\mathcal{N}_1$ and $N_1$ are mapped to $\mathcal{N}$ and $N$ in $\mathcal{C}$. We call an indecomposable object of $\mathcal{C}$ $k$-negligible if $X \in N_k$. Its *nullity* is the smallest $k$ such that $X \in N_k$.

## Examples

Given a monoidal category $\mathcal{C}$ the question is whether it admits a lift to a monoidal category $\mathcal{C}_R$. Our main examples are the following:

::: theorem
[]{#theorem-intro-eval label="theorem-intro-eval"} The following categories can be obtained as mod $\mathfrak{m}$ evaluations:

1.  The category of (quantum) tilting modules $Tilt(U_q(\mathfrak{g}), {\mathbb Q}(q))$, where $\mathfrak{g}$ is a semisimple complex Lie algebra and $q$ a nontrivial primitive $\ell$-th root of unity with $\ell$ odd, $\ell > h$ and not divible by $3$ if $\mathfrak{g}$ contains $\mathfrak{g}_2$, is the mod $\mathfrak{m}$ evaluation of $Tilt(U_v(\mathfrak{g}),R)$ where $R$ is the completion of $\mathbb{Q}[v]_{(v-q)}$, the polynomial ring localized at $(v-q)$, i.e. all rational functions over $\mathbb{Q}$ which are evaluable at $v=q$.

2.  The category of (modular) tilting modules $Tilt(G,k)$, where $G$ is a semisimple simply connected algebraic group over a perfect field $\Bbbk$ of characteristic $p > 0$, is the mod $\mathfrak{m}$ evaluation of $Tilt(G,W(k))$ where $W(k)$ is the ring of Witt vectors of $\Bbbk$.

3.  The Deligne categories $Rep(S_t)$, $Rep(GL_t)$ and $Rep(O_t)$, $t \in {\mathbb C}$, are mod $\mathfrak{m}$ evaluations from their analogs over the completion of ${\mathbb C}[t]_{(t-n)}$.
:::

The proof of theorem [\[theorem-intro-eval\]](#theorem-intro-eval){reference-type="ref" reference="theorem-intro-eval"} 1) and 2) is explained in sections [\[tilting-quantum\]](#tilting-quantum){reference-type="ref" reference="tilting-quantum"} - [\[sec:tilting-eval\]](#sec:tilting-eval){reference-type="ref" reference="sec:tilting-eval"}. The field $\mathbb{Q}(q)$ can of course be replaced by ${\mathbb C}$. Part 3) can be generalized to incorporate the $q$-versions $Rep(U_q(\mathfrak{gl}_t))$ and $Rep(U_q(\mathfrak{o}_t))$ [@Heidersdorf-Wenzl-Deligne]. In this case however we deal with two parameter versions, e.g. the local ring is the completion of ${\mathbb C}[r,\xi]_{r-\xi^{n-1}, \xi-q}$ (using BMW notation) for the $q$-version of $O_t$. Using 3) it is possible to define $k$-negligible ideals also for certain categories of representations of supergroups. In this case the nullity is related to the atypicality.

## Modified dimensions and link invariants

In recent years there has been a lot of interest in the construction of modified traces and dimension functions [@Geer-Kujawa-Patureau-Mirand] [@Geer-Kujawa-Patureau-Mirand-ambidextrous] [@Geer-Patureau-Mirand-Virelizer] [@Geer-Patureau-Mirand-projective]. One of the main motivations for the introduction of these modified trace and dimension functions is the construction of knot invariants since the invariant (in the sense of Reshetikhin-Turaev) of an indecomposable object $X$ with $\ensuremath{\operatorname{dim}}(X) = 0$ vanishes. It is very difficult to show that a given ideal has a nontrivial modified trace function. In many cases the only known thick ideal to admit such a nontrivial modified trace is the ideal of projective objects in $\mathcal{C}$, the smallest nontrivial thick ideal. Moreover, in most cases these modified trace functions are not explicitely given.

The situation changes if there is a surjective and full tensor functor $\mathcal{C}_R \to \mathcal{C}$. In this case we can often renormalize the usual trace in $\mathcal{C}_R$ and consider its image in $\mathcal{C}$ to get a modified trace function.

::: theorem
Let $R$ be a local domain (which is not a field) whose maximal ideal $(p)$ is generated by the element $p$. Let $\mathcal C_R$ be a rigid spherical monoidal category whose Hom spaces are free $R$-modules. Let $I$ be a thick ideal all of whose objects are $k$-negligible (with respect to $(p)$), such as e.g. the ideal $N_k$ of all $k$-negligible objects. For $X \in I$ and $a \in End(X)$ $$Tr^{(k)}_X(a)\ :=\ \frac{1}{p^k}\ Tr_X(a),\hskip 3em \ensuremath{\operatorname{dim}}^{(k)}(X)\ :=\ \frac{1}{p^k}\ \ensuremath{\operatorname{dim}}(X),$$ define modified trace and dimension functions on $I$. The image of the modified trace function under $\mathcal C_R \to \mathcal C$ defines a modified trace function on the image of $I$ in $\mathcal C$.
:::

The proof of this theorem is essentially trivial. The whole difficulty lies in the construction of an appropriate lift of $\mathcal{C}$ to an analogous category over a local ring $R$. Since any proper thick ideal is contained in the ideal of negligible objects, we obtain

::: corollary
Under the assumptions of the theorem, every thick ideal in $\mathcal{C}$ admits a modified trace function.
:::

Since in each case in theorem [\[theorem-intro-eval\]](#theorem-intro-eval){reference-type="ref" reference="theorem-intro-eval"} the maximal ideal is generated by a single element, we obtain

::: corollary
Each thick ideal of $Tilt(U_q(\mathfrak{g}), {\mathbb Q}(q))$, $Tilt(G,k)$ and the Deligne categories $Rep(S_t)$, $Rep(GL_t)$ and $Rep(O_t)$, $t \in {\mathbb C}$, admits a nontrivial modified trace function.
:::

The most interesting example for this is the case of $Tilt(U_q(\mathfrak{g}),{\mathbb C})$. The classical way of Reshetikhin-Turaev to define link invariants colored by objects of $Tilt(U_q(\mathfrak{g}),{\mathbb C})$ yields a trivial invariant $\mathcal L$ unless the objects are all in the fundamental alcove. Due to our lifting theorem, we can directly define a link invariant in the sense of Reshetikhin-Turaev over the local ring $R$, the completion of ${\mathbb C}[v]_{(v-q)}$. This invariant can be normalized by $\frac{1}{p^k}$ like the dimension function and yields an $R/(p)$ valued invariant for $Tilt(U_q(\mathfrak{g}),{\mathbb C})$.

::: theorem
(see theorem [\[thm:mod-link\]](#thm:mod-link){reference-type="ref" reference="thm:mod-link"}) Assume that the components of the link have been colored with the objects $X_1,\ldots, X_m \in \mathcal{C}_R$. Let $k$ be the nullity of $X_1^{\otimes c_1}\otimes X_2^{\otimes c_2}\otimes\ ...
\otimes X_m^{\otimes c_m}$. Then the value of the $R/(p)$-valued invariant is equal to $\frac{1}{k!}\frac{d^k}{dv^k}\mathcal L^{(X_1,\ ..., X_m)}(L)_{|v=q}$, which is valid for its evaluation on any $m$-component link $L$.
:::

## Thick ideals for tilting modules

What does the nullity capture in the tilting module case?

-   In the modular case, the maximal ideal $\mathfrak{m}$ of the complete discrete valuation ring $W(k)$ is generated by $p$. If a tilting module over $W(k)$ is in $N_k$, then in particular $rank(T(\lambda)) \in (p)^k$. There are however tilting modules over $W(k)$ satisfying $p^k | rank_{W(k)} T(\lambda)$ while $T(\lambda) \notin N_k$. However, if $T(\lambda)$ is irreducible, then $T(\lambda) \in N_k$ if and only if $p^k | rank_{W(k)} T(\lambda)$.

-   In the quantum case the maximal ideal is generated by $(v-q)$. The dimension is an element in the subring $\mathbb{Q}[v]_{(v-q)}$; and the dimension over ${\mathbb Q}(q)$ is obtained by evaluating this rational function at $v=q$. As for the modular case, $T(\lambda) \in N_k$ implies that the multiplicity of $(v-q)^k$ in the numerator is at least $k$; and conversely if $T(\lambda)$ is irreducible.

In the modular and quantum case the thick ideals are sums of thick ideals attached to a right $p$-cell or a right cell in the affine Weyl group $W^+_{p}$ (or $W^+_{\ell}$) (see section [\[sec:classif\]](#sec:classif){reference-type="ref" reference="sec:classif"}) by results of [@Achar-Hardesty-Riche] [@Ostrik-ideals]. The combinatorics of these cells is however very difficult and not fully understood, especially in the modular case [@Jensen-Phd]. We construct thick ideals $\mathcal{I}(F)$ associated to minimal facets $F$ and compute their nullities in Proposition [\[tensorexample\]](#tensorexample){reference-type="ref" reference="tensorexample"}. This suggests a description of tensor ideals as a collection of positive cones associated to certain facets.

For the quantum type $A_{n-1}$ every thick ideal is a sum of thick ideals attached to Young diagrams $\lambda$ of size $n$ (which parametrize the two-sided cells of the affine Weyl group). We attach a *standard facet* $F_0(\lambda)$ to every such Young diagram and prove:

::: theorem
(see theorem [\[TypeAmain\]](#TypeAmain){reference-type="ref" reference="TypeAmain"} for details) The thick ideal $\mathcal I(\lambda)=\mathcal I(F_0(\lambda))$ generated by the tilting modules $T(\nu)$ for which $\nu+\rho\in F_0(\lambda)$ coincides with the thick ideal constructed by Ostrik for the cell in the dominant Weyl chamber corresponding to the two-sided cell labeled by the Young diagram $\lambda^T$. In particular, the nullity of any generating module $T(\nu)$ of that ideal is equal to the value of Lusztig's $a$-function of that cell.
:::

For the relation between $N_k$ and the values of the $a$-function in all types see remark [\[a-fun\]](#a-fun){reference-type="ref" reference="a-fun"}. For type $A$ we can also give the already alluded geometric description of tensor ideals via positive cones associated to certain facets, see Theorem [\[Ilambda\]](#Ilambda){reference-type="ref" reference="Ilambda"} for details. This follows fairly easily from earlier work of [@Shi], where we have benefitted from its description in [@Cooper]. In particular, we obtain an explicit description of the $N_k$. Moreover, this approach also suggests a description of the ideal structure for the modular case which is done in section [\[sec:modular-regions\]](#sec:modular-regions){reference-type="ref" reference="sec:modular-regions"}.

## Structure of the article

In section [\[sec:k-negl\]](#sec:k-negl){reference-type="ref" reference="sec:k-negl"} we introduce basic properties of the generalized negligible ideals. Modified trace functions are studied in section [\[sec:traces\]](#sec:traces){reference-type="ref" reference="sec:traces"} and modified link invariants in section [\[sec:link\]](#sec:link){reference-type="ref" reference="sec:link"}. Sections [\[tilting-quantum\]](#tilting-quantum){reference-type="ref" reference="tilting-quantum"} - [\[sec:tilting-eval\]](#sec:tilting-eval){reference-type="ref" reference="sec:tilting-eval"} deal with the case of tilting modules. In section [\[sec:typeA\]](#sec:typeA){reference-type="ref" reference="sec:typeA"} we give a description of the thick ideals in quantum type $A$. We end the article with some open questions in section [\[sec:questions\]](#sec:questions){reference-type="ref" reference="sec:questions"}. A second article [@Heidersdorf-Wenzl-Deligne] will treat the case of Deligne categories. A third article will deal with open questions about the thick ideals and the $N_k$ for modular and quantum tilting modules.
