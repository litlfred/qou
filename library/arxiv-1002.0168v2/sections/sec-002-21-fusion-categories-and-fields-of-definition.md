---
doc_id: arxiv-1002.0168v2
doc_title: "Non-cyclotomic fusion categories Introduction"
section_id: sec-002-21-fusion-categories-and-fields-of-definition
section_title: "Fusion categories and fields of definition"
section_number: 2.1
pages: 3-5
source_pdf: 1002.0168v2.pdf
source_sha256: c95d5d193d57b097
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Non-cyclotomic fusion categories Introduction — Etingof, Nikshych and Ostrik ask in [7, §2] if every fusion category can be completely deﬁned over a cyclotomic ﬁeld."
---
Let $k$ be a field. An object in an additive category is called simple if it has no non-trivial proper subobjects. An additive category is called semisimple if every object is a direct sum of simple objects (and in particular, every indecomposable object is simple). A category is called idempotent complete (or Karoubian or psuedoabelian) if every idempotent has an image (that is, a subobject which the idempotent factors through). It is easy to see that any idempotent complete additive semisimple category is abelian. A *split semisimple category over $k$* is a semisimple category over $k$ such that every simple object $X$ is split simple, that is $\End{X} = k$. If $k$ is an algebraically closed field, then any semisimple category over $k$ is automatically split.

A *fusion category over $k$* is a $k$-linear abelian semisimple rigid monoidal category with finitely many isomorphism classes of simple objects. A *split fusion category over $k$* is a fusion category over $k$ which is split semisimple. (Warning, some authors require that all fusion categories be split.)

::: example
Consider $\Real[\Integer/3 \Integer]\text{-mod}$. This is a fusion category over $\Real$ with two objects: the trivial module and the $2$-dimensional representation (where the generator acts by $120$-degree rotation). It is not split fusion because the endomorphism algebra of the $2$-dimensional representation is $\Complex$.
:::

Suppose that $k<K$ is an inclusion of fields and that $\cC_K$ is a semisimple abelian category over $K$ possibly with some fixed additional structures (e.g. it's a monoidal rigid category or a braided category). A *rational form* of $\cC$ over $k$ is a semisimple abelian category $\cC_k$ over $k$ (again with the same structure) together with an equivalence between the idempotent completion of $\cC_k \otimes_k K$ is and $\cC_K$ (this equivalence should preserve the additional structure). A *complete rational form* of $\cC$ over $k$ is a rational form $\cC_k$ such that $\cC_k \otimes_k K \cong \cC_K$, in other words, a complete rational form is a rational form such that $\cC_k \otimes_k K$ is already idempotent complete.

There are several reasons for considering incomplete rational forms. First, many constructions do not preserve completeness. For example, the category of $G$-graded rational vector spaces is a complete rational form of the category of $G$-graded complex vector spaces, while the center of the former category is only an incomplete rational form of the center of the latter. Second, any fusion category is the category of representations of a weak Hopf algebra $A$ [@MR1976459; @0206113; @9904073; @MR2522429] and if that weak Hopf algebra has an rational form $A_k$ then $A_k-\text{mod}$ is, in general, an incomplete rational form for $A-\text{mod}$. Third, the notion of incomplete rational form arises naturally in the context of planar algebras. Finally, it can be convenient to show that $\cC_k$ is a complete rational form by first showing that it is a rational form (which is often easy for the above reasons) and then explicitly checking completeness.

Notice that if $\cC_K$ is a split fusion category over $K$ and $\cC_k$ is a rational form over $k < K$ then $\cC_k$ is complete if and only if $\cC_k$ is a split fusion category.

If $\cC_K$ is a split fusion category then there is a more concrete description of having a complete rational form (pointed out to us by Victor Ostrik). A split fusion category $\cC_K$ can be completely described by a collection of vector spaces $\Hom{}{V_a \otimes V_b}{V_c}$ over $K$, and associativity maps between the appropriate tensor products of these spaces. The fusion category $\cC_K$ has a complete rational form over $k$ if and only if there exists a basis for each of these vector spaces such that all the associativity maps are given by matrices with entries in $k$.

::: example
[]{#ex:graded label="ex:graded"} $\cC_\Complex = \Complex[\Integer/3 \Integer]\text{-mod}$ has a complete rational form over $\Rational$. To see this notice that $\Integer/3\Integer$ is abelian, and hence $\Complex[\Integer/3 \Integer]\text{-mod}$ is equivalent to the category of $\Integer/3 \Integer$-graded complex vector spaces. We can take $\cC_\Rational$ to be the category of $\Integer/3 \Integer$-graded rational vector spaces.
:::

::: example
[]{#ex:incomplete label="ex:incomplete"} Consider $G$ a finite group. Notice that all of the representations of a group $G$ are defined over a field $k$ if and only if $k[G]\text{-mod}$ is split. All representations of any finite group $G$ are defined over $\Rational(\zeta_{n})$, where $n$ is the exponent of $G$. Therefore, $\Complex[G]\text{-mod}$ has a complete rational form over a cyclotomic field. On the other hand as Example [\[ex:graded\]](#ex:graded){reference-type="ref" reference="ex:graded"} shows, it is possible for $\Complex[G]\text{-mod}$ to be defined over a smaller field than the minimal field of definition for all its representations.
:::

If $\cC$ is a $k$-linear category, and $k < K$ is an inclusion of fields and the idempotent additive completion of $\cC \tensor_k K$ is semisimple, then $\cC$ is semisimple. This follows from the characterization of semisimplicity in terms of semisimplicity of the endomorphism algebras, given in the next Lemma, and the equivalence of semisimplicity of artinian rings with the absence of nilpotent ideals [@MR1009787 p. 203]. The same is not true for split semisimplicity as $\Real[\Integer/3 \Integer]\text{-mod}$ is not split semisimple while $\Complex[\Integer/3 \Integer]\text{-mod}$ is. The converse is also false at least when $k<K$ is inseparable [@MR1995781 Question 5.1].

::: lem
A $k$-linear additive idempotent complete category $\cC$ is semisimple if and only if the endomorphism algebra of every object is a semisimple algebra. The simple objects are exactly those objects whose endomorphism algebras are division rings.
:::

::: proof
*Proof.* By Schur's lemma, if $\cC$ is semisimple then the endomorphism algebra of an object is a sum of matrix algebras over division rings, which is a semisimple algebra.

In the other direction, suppose that $\cC$ has all endomorphism algebras semisimple. Since the category is idempotent complete, one may use the projections in the endomorphism algebras to decompose any object into a direct sum of objects whose endomorphism algebras are division rings. If $X$ and $Y$ are non-isomorphic objects whose endomorphism algebras are division rings, the semisimplicity of $\End{X\oplus Y}$ shows that there are no nonzero maps between $X$ and $Y$. Hence all objects whose endomorphism algebras are division rings are simple and every object is semisimple. ◻
:::
