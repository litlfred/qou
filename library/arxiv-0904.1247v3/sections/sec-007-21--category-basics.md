---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-007-21--category-basics
section_title: "-category basics"
section_number: 2.1
pages: 14-18
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.974
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
[]{#infinity label="infinity"}

Roughly speaking, an $\infty$-category (or synonymously $(\infty,
1)$-category) encodes the notion of a category whose morphisms form topological spaces and whose compositions and associativity properties are defined up to coherent homotopies. The theory of $\infty$-categories has many alternative formulations (see [@Bergner] for a comparison between the different versions). We will follow the conventions of [@topos], which is based on Joyal's quasi-categories [@Joyal]. Namely, an $\infty$-category is a simplicial set satisfying a weak version of the Kan condition guaranteeing the fillability of certain horns. The underlying vertices play the role of the set of objects while the fillable horns correspond to sequences of composable morphisms. The book [@topos] presents a detailed study of $\infty$-categories, developing analogues of many of the common notions of category theory (an overview of the $\infty$-categorical language, including limits and colimits, appears in [@topos Chapter 1.2]). An important distinction between $\infty$-categories and the more traditional settings of model categories or homotopy categories is that coherent homotopies are naturally built into the definitions. Thus for example, all functors are derived and the natural notions of limits and colimits correspond to homotopy limits and colimits. We will make essential use of the theory of adjoint functors, monads and Lurie's extension [@HA 6.2.2] of the Barr-Beck theorem to the setting of $\infty$-categories.

Most of the $\infty$-categories that we will encounter are presentable [@topos 5.5] in the sense that they are closed under all small colimits (as well as limits, by [@topos Proposition 5.5.2.4]), and generated under suitable colimits by a small category. Examples include $\infty$-categories of spaces and of modules over a ring. Presentable $\infty$-categories form an $\infty$-category ${\mathcal Pr}$ whose morphisms are left adjoints, or equivalently by the adjoint functor theorem [@topos 5.2], functors that preserve all colimits [@topos 5.5.3].

An $\infty$-category is stable [@HA 1.1,1.2] if it has a zero object, is closed under finite limits and colimits, and pushouts and pullbacks coincide. Stable $\infty$-categories are an analogue of the additive setting of homological algebra: the homotopy category of a stable $\infty$-category has the canonical structure of a triangulated category [@HA 1.1.2]. We will denote by $St\subset \mathcal Pr$ the full $\infty$-subcategory of stable presentable $\infty$-categories as studied in [@HA 1.4.5].

### Ind-categories and compact generators {#sect ind-categories}

Recall that an object $c$ of an $\infty$-category $\mathcal C$ is compact if the functor $\mathop{\mathrm{Hom}}_\mathcal C(c, -)$ preserves (small) colimits (see [@topos 5.3.4] for a detailed discussion).

Given a functor $f:\mathcal C\to \mathcal D$ between $\infty$-categories, we will say

1.  $f$ is *continuous* if it preserves all (small) colimits, and

2.  $f$ is *quasi-proper* if it takes compact objects to compact objects.

We briefly recall the properties of ind-categories from [@topos Section 5.3.5]. Given a small $\infty$-category $\mathcal C$ which admits finite colimits, we may freely adjoin to $\mathcal C$ all small filtered colimits. The result is a new $\infty$-category $\operatorname{Ind}\mathcal C$, called the ind-category of $\mathcal C$, which is presentable (and so in particular, admits all small colimits). By [@HA 1.1.3], if $\mathcal C$ is stable then so is $\operatorname{Ind}\mathcal C$. In general, $\operatorname{Ind}\mathcal C$ can be identified with the category of those presheaves on $\mathcal C$ taking finite colimits to finite limits (and so in particular, it comes with an embedding $\mathcal C\subset \operatorname{Ind}\mathcal C$).

Let us denote by ${st}$ the $\infty$-category of small stable $\infty$-categories that are idempotent-complete [@topos 4.4.5] (see [@BFN 4.1] for a discussion). For $\mathcal C\in{st}$, we can recover $\mathcal C$ from its ind-category $\operatorname{Ind}\mathcal C$ as the full $\infty$-category $\mathcal C\simeq (\operatorname{Ind}\mathcal C)_{cpt}$ of compact objects of $\operatorname{Ind}\mathcal C$ (see [@topos Lemma 5.4.2.4] or [@topos 5.3.4.17], and also Neeman [@neemanTTY]).

This hints at the intimate relation between ind-categories and the classical notion of compact generation (see [@HA 1.4.5] and [@topos 5.5.7] for more details). A stable $\infty$-category $\mathcal C$ is said to be compactly generated if it admits filtered colimits and there is a small $\infty$-category $\mathcal C^\circ$ of compact objects $c_i\in
\mathcal C$ whose right orthogonal vanishes: if $m\in\mathcal C$ satisfies $\operatorname{\mathop{\mathrm{Hom}}}_\mathcal C(c_i,m)\simeq 0$, for all $i$, then $m\simeq 0$.

Note that an ind-category $\operatorname{Ind}\mathcal C$ is automatically compactly generated (with compact objects the objects of $\mathcal C$). In fact, any compactly generated stable presentable $\infty$-category $\mathcal C$ can be identified with the ind-category $\operatorname{Ind}\mathcal C_{cpt}$ of its subcategory $\mathcal C_{cpt}\subset \mathcal C$ of compact objects. This is a version of a theorem of Schwede and Shipley [@schwedeshipley] characterizing module categories for $A_\infty$-algebras (see [@HA 7.1.2] for the $\infty$-categorical version, and [@Keller] for the differential graded version). More generally, the functor $\operatorname{Ind}:{st}\to St$ identifies ${st}$ with the subcategory of $St$ consisting of compactly generated $\infty$-categories, and with morphisms quasi-proper continuous functors; a quasi-inverse is given by $\mathcal C\mapsto
\mathcal C_{cpt}$.

### Opposite categories and restricted opposites {#restricted op}

We denote by $\mathcal C^\diamondsuit$ the opposite category of an $\infty$-category $\mathcal C$ (reserving the superscript ${op}$ for the opposite monoidal structure on algebras; see Section [0.1](#monoidal infinity){reference-type="ref" reference="monoidal infinity"} below). We will typically consider opposite categories for small categories only. For $\mathcal C=\operatorname{Ind}\mathcal C_{cpt}$ a compactly generated $\infty$-category, we will work with the modified notion of the restricted opposite category defined by $$\mathcal C'=\operatorname{Ind}(\mathcal C_{cpt}^\diamondsuit).$$ The terminology is motivated by that of the restricted dual of vector spaces equipped with an extra structure such as a grading.

::: example
For the $\infty$-category $\operatorname{Vect}_\mathbb C$ of $\mathbb C$-vector spaces, $\operatorname{Vect}_{\mathbb C, cpt}$ consists of perfect complexes of $\mathbb C$-vector spaces. Duality gives an identification $\operatorname{Vect}_{\mathbb C, cpt}\simeq \operatorname{Vect}_{\mathbb C, cpt}^\diamondsuit$, which extends by continuity to an equivalence $\operatorname{Vect}_{\mathbb C}\simeq \operatorname{Vect}_{\mathbb C}'$. Note that the plain opposite category $\operatorname{Vect}_{\mathbb C}^\diamondsuit$ is the $\infty$-category of pro-finite dimensional vector spaces, which is quite different from $\operatorname{Vect}_\mathbb C'$.
:::

### Adjoint and quasi-proper functors

We record here a couple of other useful statements.

::: lemma
[]{#quasi-proper functors label="quasi-proper functors"} Let $F:{\mathcal C}\longleftrightarrow{\mathcal D}: G$ denote an adjoint pair of functors of $\infty$-categories. If $G$ is continuous, then $F$ is quasi-proper. Conversely, if ${\mathcal C}$ is compactly generated and $F$ is quasi-proper, then $G$ is continuous.
:::

::: proof
*Proof.* See [@BunG; @compact Proposition 1.2.4]. ◻
:::

We will only need the following in the stable setting though it holds more generally.

::: lemma
[]{#Ind adjoint label="Ind adjoint"} Let $f:\mathcal C\longleftrightarrow \mathcal D: g$ denote an adjoint pair of exact functors between small stable $\infty$-categories. Then the induced functors $\operatorname{Ind}f:\operatorname{Ind}\mathcal C\longleftrightarrow \operatorname{Ind}\mathcal D: \operatorname{Ind}g$ are also adjoint.
:::

::: proof
*Proof.* The assertion follows immediately from the universal property [@topos Proposition 5.3.5.10] of the $\operatorname{Ind}$ construction: for $\mathcal C$ a small stable $\infty$-category and $\mathcal D\in St$ a presentable stable $\infty$-category, there is an equivalence of $\infty$-categories $$\xymatrix{
\operatorname{Ind}: \mathop{\mathrm{Fun}}^{ex}(\mathcal C,\mathcal D)\ar[r]^-\sim & \mathop{\mathrm{Fun}}^L(\operatorname{Ind}\mathcal C,\mathcal D)
}$$ between the categories of continuous functors (equivalently, left adjoints) from $\operatorname{Ind}\mathcal C$ to $\mathcal D$ and functors from $\mathcal C$ to $\mathcal D$ that preserve finite colimits. ◻
:::

### Reversing diagrams {#reversing diagrams}

The adjoint functor theorem has a very useful corollary that enables us to calculate suitable colimits of $\infty$-categories by turning them into (much simpler) limits. Recall that given a small colimit-preserving (respectively, small limit-preserving accessible) functor $F:\mathcal C\to \mathcal D$ between stable presentable $\infty$-categories, the adjoint functor theorem provides a right (respectively, left) adjoint. In other words, the opposite of the $\infty$-category $St$ of stable presentable $\infty$-categories with morphisms colimit-preserving functors is the $\infty$-category $St^R$ of stable presentable $\infty$-categories with morphisms accessible limit-preserving functors (see ([@topos Corollary 5.5.3.4] in the unstable setting). Moreover, small limits of stable presentable $\infty$-categories are independent of context: the forgetful functors $$\xymatrix{
St\ar[r] & \operatorname{Cat}_\infty&  St^R \ar[l] 
}$$ to the $\infty$-category $\operatorname{Cat}_\infty$ of all $\infty$-categories preserve limits. Thus the limit of a diagram in $St$ consisting of limit-preserving functors can be calculated as the limit of the same diagram regarded in $St^R$. In turn, the limit of a diagram in $St^R$ can be calculated as the colimit of the corresponding diagram in $St$ formed by the left adjoints.

## Monoidal $\infty$-categories and duals {#monoidal infinity}

A monoidal $\infty$-category as defined in [@HA 4.1.1] is an $\infty$-category equipped with a homotopy coherent associative unital product. Its homotopy category is an ordinary monoidal category. An algebra object $A$ in a monoidal $\infty$-category as defined in [@HA 4.1.2] is an object equipped with a homotopy coherent multiplication. Left and right module objects over an algebra object are defined similarly [@HA 4.2.2], with right modules identified with left modules over the opposite algebra object $A^{op}$ in the opposite monoidal $\infty$-category. There is a relative tensor product $\cdot \otimes_A \cdot$ of left and right modules given by the two-sided bar construction [@HA 4.3.4]. Monoidal $\infty$-categories, algebra objects in a monoidal $\infty$-category, and module objects over an algebra object themselves form $\infty$-categories, some of whose properties (in particular, behavior of limits and colimits) are worked out in [@HA 4.2].

The definition of a symmetric monoidal $\infty$-category is given in [@HA 2.0.0.7] modeled on the Segal machine for infinite loop spaces. Its homotopy category is an ordinary symmetric monoidal category. There is the notion of commutative algebra object $A$ in a symmetric monoidal $\infty$-category such that $A$-modules form a symmetric monoidal $\infty$-category with respect to relative tensor product  [@HA 4.4.2]. Given two associative algebra objects $A, B$, their monoidal product $A\otimes B$ carries a natural associative algebra structure. Furthermore, any associative algebra object $A$ is a left (as well as a right) module object over the associative algebra $A\otimes A^{op}$ via left and right multiplication.

The $\infty$-category ${\mathcal Pr}$ of presentable $\infty$-categories and continuous functors carries a symmetric monoidal structure introduced in [@HA 6.3.1]. The tensor product $\mathcal C\otimes\mathcal D$ of presentable $\mathcal C,\mathcal D$ is a recipient of a universal functor from the Cartesian product $\mathcal C\times \mathcal D$ which is "bilinear\" (commutes with colimits in each variable separately). In fact, the tensor product lifts to a symmetric monoidal structure in which the unit object is the $\infty$-category of spaces [@HA 6.3.1]. Furthermore, the symmetric monoidal structure is closed in the sense that ${\mathcal Pr}$ admits an internal hom functor compatible with the tensor structure  [@topos Remark 5.5.3.9], [@HA Remark 6.3.1.17]. The internal hom assigns to presentable $\infty$-categories $\mathcal C$ and $\mathcal D$ the $\infty$-category of colimit-preserving functors $\mathop{\mathrm{Fun}}(\mathcal C,\mathcal D)$ which is presentable by [@topos Proposition 5.5.3.8].

The symmetric monoidal structure on the $\infty$-category $\mathcal Pr$ of presentable $\infty$-categories restricts to one on the full $\infty$-subcategory $St\subset \mathcal Pr$ of stable presentable $\infty$-categories [@HA 6.3.2], [@HA 6.3.2]. The unit is the stable category, modules over the sphere spectrum. By [@BFN Proposition 4.4], the functor $\operatorname{Ind}:{st}\to St$ is in a natural way a symmetric monoidal functor $$\operatorname{Ind}(\mathcal C_1\otimes\mathcal C_2)\simeq \operatorname{Ind}(\mathcal C_1)\otimes\operatorname{Ind}(\mathcal C_2)$$ for the natural symmetric monoidal structures on both sides.

A basic example of a symmetric monoidal stable $\infty$-category is $\operatorname{Vect}_\mathbb C$, which underlies the dg category of chain complexes of $\mathbb C$-vector spaces. The rest of this paper takes place in the setting of the symmetric monoidal $\infty$-category $$St_\mathbb C=\mathop{\mathrm{Mod}}_{\operatorname{Vect}_\mathbb C}(St)$$ of $\mathbb C$-linear stable presentable $\infty$-categories, defined as modules for $\operatorname{Vect}_\mathbb C$ in stable categories. The category $St_\mathbb C$ provides a model for the theory of differential graded categories over $\mathbb C$ (see [@cohn] for the identification of the corresponding homotopy theories). As the category of modules over a commutative algebra object (namely $\operatorname{Vect}_\mathbb C$), $St_\mathbb C$ inherits a symmetric monoidal structure itself with unit $\operatorname{Vect}_\mathbb C$. All of the foundations and formal results for stable $\infty$-categories naturally translate to the $\mathbb C$-linear setting by base change to the commutative algebra $\operatorname{Vect}_\mathbb C$.

### Dualizability {#duals}

Let $A$ denote a monoidal $\infty$-category with monoidal product $\star$ and monoidal unit $1_A$. A key property for objects of $A$ is dualizability (see [@HA Section 4.2.5]).

::: definition
An object $a\in A$ of a monoidal $\infty$-category is *left dualizable* (respectively, *right dualizable*) if there is an object ${}^\vee a$ (respectively, $a^\vee$) together with morphisms $$\xymatrix{
coev: 1_A\ar[r] &  {}^\vee a \star a
& 
ev: a \star {}^\vee a
  \ar[r] &  1_A
  }$$ so that the obvious compositions $$\xymatrix{
a\ar[r] & a\star {}^\vee a \star a \ar[r] & a &
      {}^\vee a\ar[r] & {}^\vee a \star a \star {}^\vee a \ar[r] &
      {}^\vee a}$$ are equivalent to the corresponding identity maps (respectively, $$\xymatrix{
      coev:1_A\ar[r] &  a\star a^\vee  &
      ev: a^\vee \star a\ar[r] & 1_A
      }$$ satisfying analogous composition identities).
:::

Note that the left dual of $a^\vee$ is again $a$, and the right dual of ${}^\vee a$ is again $a$, i.e., left and right dualities are inverses of each other. For a symmetric monoidal $\infty$-category $A$, we will take advantage of the natural identification between the notions of left and right duals and speak simply of the dual $a'$.

One can reinterpret the notion of dualizable object in terms of adjoint functors: $a\in A$ is left dualizable (respectively, right dualizable) if the functor $\star a$ admits the left adjoint $\star {}^\vee a$, or equivalently the functor $a \star$ admits the right adjoint ${}^\vee a \star$ (respectively, if the functor $\star a$ admits the right adjoint $\star a^\vee$, or equivalently the functor $a\star$ admits the left adjoint $a^\vee\star$). Let us record this in the following form for easy reference.

::: lemma
[]{#internal label="internal"} For a right (respectively, left) dualizable object $a$ in a monoidal $\infty$-category $A$ we have functorial identifications $$\xymatrix{
\mathop{\mathrm{Hom}}_A(a^\vee\star b, c)\simeq \mathop{\mathrm{Hom}}_A( b,a\star c)
&
\mathop{\mathrm{Hom}}_A( b\star a, c)\simeq \mathop{\mathrm{Hom}}_A( b, c \star a^\vee)
}$$

which are monoidal in $a$.

Likewise, for an $A$-module category $M$ and objects $m,n\in M$, we have a functorial identification $$\xymatrix{
\mathop{\mathrm{Hom}}_M(a^\vee\star  m, n)\simeq \mathop{\mathrm{Hom}}_M( m, a \star  n)
}$$

where we write $\star$ for the $A$-action on $M$.
:::

### Dualizability of stable $\infty$-categories

We work with stable presentable $\mathbb C$-linear categories $St_\mathbb C$ (or dg categories), though everything works in the general setting $St$ over the sphere. As discussed above, the $\infty$-category $St_\mathbb C$ is naturally symmetric monoidal with unit the $\infty$-category $\operatorname{Vect}_\mathbb C$ of chain complexes.

::: prop
[]{#jacob duality label="jacob duality"} Suppose $\mathcal C\in St$ is compactly generated so that $\mathcal C=\operatorname{Ind}
\mathcal C_{cpt}$. Then $\mathcal C$ is dualizable in $St$ with dual the restricted opposite $\mathcal C'=\operatorname{Ind}(\mathcal C_{cpt}^\diamondsuit)$.
:::

::: proof
*Proof.* See [@DGcat Proposition 2.3.1]. ◻
:::

### Dualizability of modules

We will also require a slightly generalized notion of dualizablity, which applies in the (non-monoidal) setting of modules over an associative algebra. Let $A\in \mathcal Alg(\mathcal S)$ denote an associative algebra in a symmetric monoidal $\infty$-category $\mathcal S$ with unit $1_\mathcal S$, and let $\mathcal C=A\otimes A^{op}\operatorname{-mod}$ denote the $\infty$-category of $A$-bimodules in $\mathcal S$.

::: definition
[]{#duality for modules label="duality for modules"} An $A$-module $M$ is said to be $A$-dualizable (respectively, $\mathcal S$-dualizable) if there is an $A^{op}$-module ${}^\vee M$ (respectively $M^\vee$) together with morphisms $$\xymatrix{
ev^L:  M \otimes_\mathcal S{}^{\vee} M  \ar[r] & A \mbox{ in }\mathcal C&
  coev^L:1_\mathcal S\ar[r] &  {}^{\vee}M\otimes_A M\mbox{ in }\mathcal S
  }$$ (respectively, $$\xymatrix{
  ev^R: M^\vee\otimes_A  M\ar[r] & 1_\mathcal S\mbox{ in }\mathcal S& 
  coev^R:A \ar[r] &  M\otimes_\mathcal SM^\vee\mbox{ in }\mathcal C)
  }$$ satisfying the usual identities.
:::

::: remark
[]{#infty,2 label="infty,2"} The notion of dualizability for $A$-modules is perhaps more naturally seen as usual dualizability for bimodules for algebra objects $A$ and $B$ (in the case $B=1_\mathcal S$), under the convolution product on bimodules.

Recall (see [@jacob; @TFT]) that by considering monoidal categories as 2-categories with a single object, we can understand duality for objects in a monoidal category as a special case of the notion of adjoints in a $2$-category. The above notion of duality for $A$-modules (or bimodules) has a similar interpretation. Namely, we consider an $A$-module $M\in \mathcal C$ as a bimodule for $A$ and the unit $1_S$, and thus as a morphism $A\to 1_S$ in the Morita $(\infty,2)$-category $Alg_{(1)}(\mathcal S)$ of algebra objects in $\mathcal S$. In this interpretation, $M$ is $A$- (respectively, $\mathcal S$-) dualizable precisely when $M$ admits a left (respectively, right) adjoint.
:::

We record here the following elementary compatibility of our previous definitions.

::: lemma
[]{#duals compatible label="duals compatible"} An $A$-module $M\in \mathop{\mathrm{Mod}}_A(\mathcal S)$ is $\mathcal S$-dualizable if and only if the underlying object $M\in \mathcal S$ is dualizable. In this case, the $\mathcal S$-dual $M^\vee\in \mathop{\mathrm{Mod}}_{A^{op}}(\mathcal S)$ has underlying object the dual $M'\in \mathcal S$, compatibly with evaluation and coevaluation maps.
:::

::: proof
*Proof.* Suppose $M$ is $\mathcal S$-dualizable with $\mathcal S$-dual $M^\vee$. Then we can extend its evaluation morphism $$\xymatrix{
ev:M\otimes_\mathcal SM^\vee \ar[r] & M\otimes_A M^\vee \ar[r]^-{ev^R}  & 1_\mathcal S
}$$ where the first map is the natural quotient, and its coevaluation morphism $$\xymatrix{
coev:1_\mathcal S\ar[r] & A \ar[r]^-{coev^R} & M^\vee \otimes_\mathcal SM
}$$ where the first map is the unit of the algebra $A$. It is straightforward to check that these exhibit $M^\vee$ as the plain dual of $M$.

Conversely, suppose $M$ is dualizable with dual $M'$. There is a canonical identification of algebras $$\operatorname{End}_\mathcal S(M') \simeq \operatorname{End}_\mathcal S(M)^{op},$$ and so $M'$ inherits a natural $A^{op}$-module structure. By construction, the evaluation $ev$ descends to provide the evaluation $ev^R$. Likewise, by adjunction, the coevaluation $coev$ extends to provide the $A$-bilinear coevaluation $coev^R$. ◻
:::
