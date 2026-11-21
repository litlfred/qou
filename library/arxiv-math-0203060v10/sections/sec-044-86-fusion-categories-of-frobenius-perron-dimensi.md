---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-044-86-fusion-categories-of-frobenius-perron-dimensi
section_title: "Fusion categories of Frobenius-Perron dimension pn"
section_number: 8.6
pages: 36-37
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 1.0
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
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
