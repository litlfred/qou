---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-045-87-categories-with-integer-frobenius-perron-dime
section_title: "Categories with integer Frobenius-Perron dimensions of simple objects"
section_number: 8.7
pages: 37-39
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.965
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
::: theorem
[]{#quasihopf label="quasihopf"} Let ${\mathcal C}$ be a fusion category. The following two conditions are equivalent.

1.  for all $X\in {\mathcal C}$, the number ${\rm FPdim}(X)$ is an integer.

2.  ${\mathcal C}$ is a representation category of a finite dimensional quasi-Hopf algebra $A$.
:::

::: remark
It is shown in [@EG2] that $A$ is determined uniquely up to twisting.
:::

::: proof
*Proof.* (i)$\to$ (ii). Let $F:{\mathcal C}\to {\rm Vect}$ be the additive functor that maps simple objects $X_i$ of ${\mathcal C}$ to vector spaces $F(X_i)$ of dimension ${\rm FPdim}(X_i)$. For any $i,j$, choose any isomorphism $J_{ij}: F(X_i)\otimes F(X_j)\to F(X_i\otimes X_j)$ (this is possible by Theorem [\[fp\]](#fp){reference-type="ref" reference="fp"}). Then by a standard reconstruction argument the algebra $\text{End}_k(F)$ has a natural structure of a quasi-Hopf algebra (changing $J$ corresponds to twisting the quasi-Hopf algebra). We note that $A$ is not, in general, a Hopf algebra, since $J$ is not required to be a tensor structure on $F$.

(ii)$\to$ (i). This is clear since for ${\mathcal C}=\text{Rep}(A)$, ${\rm FPdim}(X)={\rm Dim}(X)$, where ${\rm Dim}(X)$ denotes the dimension of the underlying vector space. ◻
:::

It is obvious that the class of fusion categories with integer Frobenius-Perron dimensions is closed under the operations of tensor product, passing to the opposite category, and taking a fusion subcategory. The following theorem shows that it is also closed under taking duals (i.e., in the language of [@Mu1],[@O] the property of integer Frobenius-Perron dimensions is weak Morita invariant).

::: theorem
[]{#dualfrob label="dualfrob"} Let ${\mathcal C}$ be a fusion category with integer Frobenius-Perron dimensions, ${\mathcal M}$ be an indecomposable module category over ${\mathcal C}$. Then the fusion category ${\mathcal C}_{{\mathcal M}}^*$ has integer Frobenius-Perron dimensions.
:::

::: proof
*Proof.* We know from [@Mu1],[@O1] that $Z({\mathcal C})$ is canonically equivalent to $Z({\mathcal C}_{\mathcal M}^*)$. So let $V$ be an object of $Z({\mathcal C})$ such that the matrix of multiplication by $V$ in both ${\mathcal C}$ and ${\mathcal C}^*_{\mathcal M}$ has strictly positive entries (it exists, since both ${\mathcal C}$ and ${\mathcal C}^*_{\mathcal M}$ are fusion categories, and so the natural functors $Z({\mathcal C})\to {\mathcal C}$, $Z({\mathcal C}^*)\to {\mathcal C}^*_{\mathcal M}$ are surjective).

Let $[X], [X]_*$ be the matrices of multiplication by $X\in Z({\mathcal C})$ in the Grothendieck groups $K({\mathcal C}),K({\mathcal C}^*_{\mathcal M})$, respectively. For a square matrix $A$ with nonnegative entries, let $t(A)$ be the largest real eigenvalue of $A$. By the assumptions of the theorem, $t([V])$ is an integer (it is the Frobenius-Perron dimension of $V$ as an object of ${\mathcal C}$). Since the asssignments $X\to t([X])$, $X\to t([X]_*)$, $X\in Z({\mathcal C})$, are both homomorphisms of algebras, Lemma [\[uniq\]](#uniq){reference-type="ref" reference="uniq"} implies that $t([V])=t([V]_*)$. Hence, $t([V]_*)$ is an integer.

The vector of Frobenius-Perron dimensions of simple objects in ${\mathcal C}_{\mathcal M}^*$ is the unique, up to scaling, eigenvector of $[V]_*$ with eigenvalue $t([V]_*)$. Since the matrix $[V]_*$ has integer entries, the entries of this vector are rational numbers (as the zeroth entry is $1$). This means that they are integers (as they are eigenvalues of integer matrices and hence algebraic integers). The theorem is proved. ◻
:::

::: corollary
[]{#quotcat label="quotcat"} The class of fusion categories with integer Frobenius-Perron dimensions is closed under the operation of taking a component of a quotient category.
:::

::: proof
*Proof.* Let ${\mathcal C}$ be a fusion category with integer Frobenius-Perron dimensions, ${\mathcal D}$ an indecomposable multi-fusion category, and and $F:{\mathcal C}\to {\mathcal D}$ be a surjective tensor functor (so ${\mathcal D}$ is a quotient of ${\mathcal C}$). Let ${\mathcal M}$ be an indecomposable module category over ${\mathcal D}$. Then $F^*:{\mathcal D}^*\to {\mathcal C}^*$ is an injective tensor functor between the corresponding dual fusion categories (${\mathcal C}^*$ is fusion since ${\mathcal M}$ is indecomposable over ${\mathcal C}$, by surjectivity of $F$). By Theorem [\[dualfrob\]](#dualfrob){reference-type="ref" reference="dualfrob"}, ${\mathcal C}^*$ has integer Frobenius-Perron dimensions. Hence, so does ${\mathcal D}^*$ as its full subcategory. But any component category ${\mathcal D}_{ii}$ of ${\mathcal D}$ is dual to ${\mathcal D}^*$ with respect to the $i$-th part of ${\mathcal M}$ as a ${\mathcal D}^*$-module. Thus, ${\mathcal D}_{ii}$ has integer Frobenius-Perron dimensions by Theorem [\[dualfrob\]](#dualfrob){reference-type="ref" reference="dualfrob"}. ◻
:::

::: proposition
[]{#frobmod1 label="frobmod1"} Let ${\mathcal C}$ be a fusion category with integer Frobenius-Perron dimensions. Then for any indecomposable module category ${\mathcal M}$ over ${\mathcal C}$, the Frobenius-Perron dimensions of objects in ${\mathcal M}$ are integers (under a suitable normalization).
:::

::: proof
*Proof.* Since the matrix $[V]_{\mathcal M}$ from Proposition [\[frobmod\]](#frobmod){reference-type="ref" reference="frobmod"} has integer entries, and its largest real eigenvalue ${\rm FPdim}(V)$ is an integer and has multiplicity $1$, the entries of $\mathbf m$ are rational. ◻
:::

In [@O2], it is asked whether there are finitely many fusion categories with a given number of simple objects, and proved that the answer is "yes" for representation categories of Hopf algebras. Using the above techniques, one can show that the answer is "yes" for fusion categories with integer Frobenius-Perron dimension (which includes Hopf and quasi-Hopf algebras). Namely, we have

::: proposition
There are finitely many fusion categories of integer Frobenius-Perron dimension with a given number of simple objects. In particular, there are finitely many equivalence classes of semisimple quasi-Hopf algebras with a given number of matrix blocks.
:::

::: proof
*Proof.* Let ${\mathcal C}$ be such a category with $N$ simple objects. Since the Frobenius-Perron dimension of ${\mathcal C}$ is an integer, it is pseudo-unitary, in particular has a canonical spherical structure. Let $d_i$ be the categorical (=Frobenius-Perron) dimensions of simple objects of $Z({\mathcal C})$ which occur in $I(\mathbf 1)$, and $D$ be its global (=Frobenius-Perron) dimension. Then $d_i$ are integers (by Proposition [\[roots\]](#roots){reference-type="ref" reference="roots"}, since for $X_i$ occuring in $I(\mathbf 1)$, $X_i|_{\mathcal C}$ lies in ${\mathcal C}_{ad}$ by Proposition [\[I(1)\]](#I(1)){reference-type="ref" reference="I(1)"}). Thus, $D/d_i=m_i$ are (usual) integers by Proposition [\[moddivi\]](#moddivi){reference-type="ref" reference="moddivi"}, and $\sum_i[X_i|_{\mathcal C}:1]\frac{1}{m_i}=1$. The number of summands $1/m_i$ here is $\sum [X_i|_{{\mathcal C}}:\mathbf 1]$, which is at most $N$ by Proposition [\[numobj\]](#numobj){reference-type="ref" reference="numobj"}. By a classical argument of Landau (see [@O2] and references therein), the number of such collections $m_i$ is finite for any given $N$. On the other hand, $m_0=D$ (as $X_0$ is the neutral object). Thus, $D$ is bounded by some function of $N$. But for a given $D$, there are only finitely many fusion rings, and hence, by Ocneanu rigidity, finitely many fusion categories. ◻
:::
