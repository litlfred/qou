---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-032-84-pseudo-unitary-categories
section_title: "Pseudo-unitary categories"
section_number: 8.4
pages: 34-39
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.803
---
Let us say that a fusion category ${\mathcal C}$ is *pseudo-unitary* if $\dim({\mathcal C})={\rm FPdim}({\mathcal C})$. This property is automatically satisfied for unitary categories, which occur in the theory of operator algebras, but it fails, for example, for the Yang-Lee category.

::: proposition
[]{#uniqpivo label="uniqpivo"} Any pseudo-unitary fusion category ${\mathcal C}$ admits a unique pivotal (in fact, spherical) structure, with respect to which the categorical dimensions of all simple objects are positive, and coincide with their Frobenius-Perron dimensions.
:::

::: proof
*Proof.* Let $g: Id\to ****$ be an isomorphism of tensor functors, $a:Id\to **$ an isomorphism of additive functors, such that $a^2=g$, $d_i$ be the dimensions of simple objects $X_i$ associated to $a$ as in Section 3.1, and $\mathbf d$ the vector with components $d_i$. Then $T_i\mathbf d=d_i\mathbf d$, and $|d_i|=f_i$ is the Frobenius-Perron dimension of $X_i$. But $|(T_i)_{jk}|\le (N_i)_{jk}$. Thus, $$f_if_j=|d_id_j|=|\sum (T_i)_{jk}d_k|\le \sum (N_i)_{jk}f_k=f_if_j$$ This means that the inequality in this chain is an equality. In particular $(T_i)_{jk}=\pm (N_i)_{jk}$, and the argument of $d_id_j$ equals the argument of $(T_i)_{jk}d_k$ whenever $(N_i)_{jk}>0$. This implies that whenever $X_k$ occurs in the tensor product $X_i\otimes X_j$, the ratio $d_i^2d_j^2/d_k^2$ is positive. Thus, the automorphism of the identity functor $\sigma$ defined by $\sigma|_{X_i}=d_i^2/|d_i|^2$ is a tensor automorphism. Let us twist $g$ by this automorphism. After this twisting, the new dimensions $d_i$ will be real. Thus, we can assume without loss of generality that $d_i$ were real from the beginning.

It remains to twist the square root $a$ of $g$ by the automorphism of the identity functor $\tau$ given by $\tau|_{X_i}=d_i/|d_i|$. After this twisting, new $T_i$ is $N_i$ and new $d_k$ is $f_k$. This means that $\beta_i^{jk}=1$ and $a$ is a pivotal structure with positive dimensions. It is obvious that such a structure is unique. We are done. ◻
:::

## Fusion categories with integer Frobenius-Perron dimension

::: proposition
[]{#intFP label="intFP"} Let ${\mathcal C}$ be a fusion category, such that $\Delta:={\rm FPdim}({\mathcal C})$ is an integer. Then ${\mathcal C}$ is pseudo-unitary. In particular, the category of representations of a semisimple finite dimensional quasi-Hopf algebra is pseudo-unitary.
:::

::: proof
*Proof.* Let $D$ be the global dimension of ${\mathcal C}$. Let $D_1=D,D_2,...,D_N$ be all the algebraic conjugates of $D$, and $g_1,...,g_N$ the elements of $Gal(\bar{\mathbb Q}/{\mathbb Q})$ such that $D_i=g_i(D)$. Applying Propostion [\[divi\]](#divi){reference-type="ref" reference="divi"} to the category $g_i({\mathcal C})$, we find that $D_i/\Delta$ is an algebraic integer $\le 1$. Then $\prod_i (D_i/\Delta)$ is an algebraic integer $\le 1$. But this product is a rational number. So it equals $1$ and hence all factors equal $1$. Hence $D=\Delta$, as desired. ◻
:::

::: remark
We note that Proposition [\[intFP\]](#intFP){reference-type="ref" reference="intFP"} may be regarded as a categorical analog of the well known theorem of Larson and Radford [@LR2], saying that in a semisimple Hopf algebra, the square of the antipode is the identity. More precisely, using Proposition [\[intFP\]](#intFP){reference-type="ref" reference="intFP"}, one can obtain the following proof of the Larson-Radford theorem (which is close to the original proof). Let $A$ be a finite dimensional semisimple Hopf algebra with antipode $S$. Since $S$ has finite order, $S^2$ is semisimple, and its eigenvalues are roots of $1$. Now, for every simple $A$-module $V$, $S^2$ preserves ${\rm
  End}(V)\subset A$ (as $V^{**}$ is isomorphic to $V$), and $|V|^2=\text{Tr}(S^2|_{{\rm End}(V)})$, while ${\rm FPdim}(V)^2=
\dim(V)^2=\dim{\rm End}(V)$. Thus, by Proposition [\[intFP\]](#intFP){reference-type="ref" reference="intFP"}, $\text{Tr}(S^2|_{{\rm End}(V)})=\dim{\rm End}(V)$. Since $S^2$ is semisimple and its eigenvalues are roots of unity, we have $S^2=1$.
:::

::: remark
In general, the Frobenius-Perron dimension of a fusion category may not only be different from its global dimension, but may in fact be not conjugate to the global dimension by the Galois group action. The same is true for the numbers ${\rm FPdim}(V)^2$ and $|V|^2$ for a simple object $V$. An example is a tensor product of the Yang-Lee category and its Galois conjugate. It has global dimension $5$, but Frobenius-Perron dimension $5(3+\sqrt{5})/2$. Also, this category has a simple object $V$ with $|V|^2=1$ but ${\rm FPdim}(V)^2=(7+3\sqrt{5})/2$.
:::

One may wonder if a fusion category ${\mathcal C}$ with integer ${\rm FPdim}({\mathcal C})$ must have integer Frobenius-Perron dimensions of simple objects. Unfortunately, the answer is "no" (see [@TY], where dimensions of some simple objects are square roots of integers). However, the following weaker result is true. Let ${\mathcal C}_{ad}$ be the full tensor subcategory of ${\mathcal C}$ generated by objects occuring in $X\otimes X^*$, where $X\in {\mathcal C}$ is simple (if ${\mathcal C}=\text{Rep}(G)$ for a group $G$ then ${\mathcal C}_{ad}$ is the representation category of the adjoint group $G/Z(G)$ -- the quotient by the center).

::: proposition
[]{#roots label="roots"} Suppose that ${\rm FPdim}({\mathcal C})$ is an integer. The Frobenius-Perron dimensions of simple objects in ${\mathcal C}_{ad}$ are integers. Furthermore, for any simple object $X\in {\mathcal C}$, one has ${\rm
  FPdim}(X)=\sqrt{N}$, where $N$ is an integer.
:::

::: proof
*Proof.* The second statement follows from the first one, since for any simple object $X\in {\mathcal C}$ the object $X\otimes X^*$ lies in ${\mathcal C}_{ad}$. To prove the first statement, consider the object $B=\oplus_i X_i\otimes X_i^*\in {\mathcal C}_{ad}$, where $X_i$ are the simple objects of ${\mathcal C}$. For some $n$ the matrix of multiplication by the object $B^{\otimes n}$ has strictly positive entries. On the other hand, the vector of dimensions of objects of ${\mathcal C}_{ad}$ is an eigenvector of this matrix with integer eigenvalue ${\rm FPdim}({\mathcal C})^n$. Thus, by the Frobenius-Perron theorem its entries are rational (as $d_0=1$), and hence integer (as they are algebraic integers). ◻
:::

## Fusion categories of Frobenius-Perron dimension $p^n$

::: theorem
[]{#filtrat label="filtrat"} Let ${\mathcal C}$ be a fusion category of Frobenius-Perron dimension $p^n$, where $n\ge 1$ is an integer, and $p$ is a prime. Then:

\(i\) There exists a nontrivial automorphism $g\in {\rm Aut}_\otimes (Id_{\mathcal C})$ of order $p$, so that ${\mathcal C}$ is $\Bbb Z/p\Bbb Z$ graded: ${\mathcal C}=\oplus_{j=0}^{p-1}{\mathcal C}_j$, where ${\mathcal C}_j$ is spanned by simple objects $X$ such that $g|_X=
e^{2\pi ij/p}$. The Frobenius-Perron dimension of the fusion category ${\mathcal C}_0$ and module categories ${\mathcal C}_j$ over it are equal to $p^{n-1}$.

\(ii\) ${\mathcal C}$ admits a filtration by fusion subcategories ${\mathcal C}\supset
{\mathcal C}^{(1)}\supset...\supset {\mathcal C}^{(n)}=<\mathbf 1>$, where $\dim {\mathcal C}^{(i)}=p^{n-i}$.
:::

::: remark
For representation categories of semisimple Hopf algebras, this theorem says that a semisimple Hopf algebra of order $p^n$ has a central group-like element of order $p$, so one can take a quotient and obtain a Hopf algebra of dimension $p^{n-1}$. This result is due to Masuoka [@Ma].
:::

::: proof
*Proof.* It is clear that (ii) follows from (i), so it suffices to prove (i). Since the Frobenius-Perron dimension of ${\mathcal C}$ is an integer, it is pseudo-unitary. In particular, it is spherical. By Proposition [\[moddivi\]](#moddivi){reference-type="ref" reference="moddivi"}, the dimensions of all objects $X\in Z({\mathcal C})$ which occur in $I(\mathbf 1)$, are divisors of $p^n$. In addition, they are all integers, since the image of $X$ in ${\mathcal C}$ belongs to ${\mathcal C}_{ad}$. By the class equation (Proposition [\[cleq\]](#cleq){reference-type="ref" reference="cleq"}), there have to be at least $p$ such objects $X$, which are invertible. This means, the group of invertible objects of $Z({\mathcal C})$ is nontrivial. By Proposition [\[subdivi\]](#subdivi){reference-type="ref" reference="subdivi"}, the order of this group must divide $p^{2n}$. In particular, this group contains a cyclic subgroup $G$ of order $p$. The group $G$ maps trivially to ${\mathcal C}$, so by Proposition [\[gradi\]](#gradi){reference-type="ref" reference="gradi"} we get a faithful $G^\vee$-grading on ${\mathcal C}$. The rest follows from Proposition [\[dimgradi\]](#dimgradi){reference-type="ref" reference="dimgradi"}. The theorem is proved. ◻
:::

The following corollary of this result is a categorical generalization of (the semisimple case of) the well known result of Y. Zhu [@Zhu] saying that a Hopf algebra of prime dimension is a group algebra.

::: corollary
[]{#zhu label="zhu"} Let ${\mathcal C}$ be a fusion category of Frobenius-Perron dimension $p$, where $p$ is a prime number. Then ${\mathcal C}$ is the category of representations of the group $\mathbb Z/p\mathbb Z$, in which associativity is defined by a cohomology class in $H^3(\mathbb Z/p\mathbb Z,{\mathbb{C}}^*)=\mathbb Z/p\mathbb Z$.
:::

::: proof
*Proof.* The corollary is immediate from Theorem [\[filtrat\]](#filtrat){reference-type="ref" reference="filtrat"}. Indeed, this theorem shows that ${\mathcal C}$ is faithfully graded by $\Bbb Z/p\Bbb Z$, so by Proposition [\[dimgradi\]](#dimgradi){reference-type="ref" reference="dimgradi"}, all ${\mathcal C}_g$ are 1-dimensional, i.e. ${\mathcal C}_g$ contains a single simple object, which is invertible. Thus, ${\mathcal C}$ has $p$ simple objects, which are invertible, and we are done. ◻
:::

::: corollary
[]{#quasih label="quasih"} A semisimple quasi-Hopf algebra of prime dimension $p$ is twist equivalent to the group algebra of a cyclic group of order $p$, with associator defined by a 3-cocycle.
:::

The following proposition classifies fusion categories of dimension $p^2$.

::: proposition
Let ${\mathcal C}$ be a fusion category of Frobenius-Perron dimension $p^2$, where $p$ is a prime number. If $p$ is odd, then simple objects of ${\mathcal C}$ are invertible, so ${\mathcal C}$ is the category of representations of a group of order $p^2$ with associativity defined by a 3-cocycle. If $p=2$, then either ${\mathcal C}$ is the representation category of a group of order $4$ with a 3-cocycle, or it has 3 objects of dimensions $1,1$ and $\sqrt{2}$, and thus belongs to the list of [@TY].
:::

::: proof
*Proof.* Assume that not all simple objects of ${\mathcal C}$ are invertible. Our job is to show that $p=2$. Indeed, in this case the dimension is 4, and we have a subcategory of dimension 2 by Theorem [\[filtrat\]](#filtrat){reference-type="ref" reference="filtrat"}. Since dimensions of all simple objects are square roots of integers, there is room for only one new object of dimension $\sqrt{2}$. All such categories are listed in [@TY] (there are two of them, and they correspond in physics to "Ising model").

Assume the contrary, i.e. that $p$ is odd. We have a grading of ${\mathcal C}$ by $\Bbb Z/p\Bbb Z$, and for all $j\in \Bbb Z/p\Bbb Z$ the dimension of ${\mathcal C}_j$ is $p$ by Proposition [\[dimgradi\]](#dimgradi){reference-type="ref" reference="dimgradi"}. Clearly, ${\mathcal C}_0$ holds $p$ invertible simple objects, and no other simple objects. It is also clear that all invertible objects of ${\mathcal C}$ are contained in ${\mathcal C}_0$ (as by Proposition [\[subdivi\]](#subdivi){reference-type="ref" reference="subdivi"}, the order of the group of invertibles is a divisor of $p^2$). Further, any object $X$ in ${\mathcal C}_j$, $j\ne 0$, must be invariant under tensoring (on either side) with invertibles from ${\mathcal C}_0$, since otherwise the dimension of ${\mathcal C}_j$ would be greater than $p$ (as the dimension of $X$ is greater than $1$). This means that $X\otimes X^*$ contains all the invertibles from ${\mathcal C}_0$, and hence the dimension of $X$ is at least $\sqrt{p}$. Since the dimension of ${\mathcal C}_j$ is $p$, we find that the dimension of $X$ is exactly $\sqrt{p}$, and $X$ is the only simple object of ${\mathcal C}_j$. Let $j,k\in \Bbb Z/p\Bbb Z$ be nonzero and distinct (they exist since $p>2$). Let $X_j,X_k$ be the only simple objects of ${\mathcal C}_j,{\mathcal C}_k$. Then $X_j\otimes X_k^*$ is a $p$-dimensional object, which is an integer multiple of a $\sqrt{p}$-dimensional object, which spans ${\mathcal C}_{j-k}$. Contradicton. The proposition is proved. ◻
:::
