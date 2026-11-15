---
doc_id: arxiv-math-0612592v1
doc_title: "Analytic q -diﬀerence equations"
section_id: sec-003-moduli-spaces-for-difference-modules
section_title: "Moduli spaces for difference modules"
section_number: null
pages: 9-10
source_pdf: 0612592v1.pdf
source_sha256: a5d29fa15a0b74ff
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.985
doc_brief: "Analytic q -diﬀerence equations — 7 sections: Front matter; Difference equations in general; First examples of q-difference equ"
---
Fix a split difference module $S=P_1\oplus \cdots \oplus P_r$ over $K$, where $P_i$ is pure with slope $\lambda _i$ and $\lambda _1<\cdots <\lambda _r$. The problem is to classify the difference modules $M$ over $K$ such that $gr(M)$ is isomorphic to $S$. The collection of the isomorphy classes is a rather ugly object due to the fact that $S$ has many automorphisms.

A better way to formulate the problem is to consider pairs $(M,f)$ consisting of a difference module $M$ and an isomorphism $f:gr(M)\rightarrow S$. Two pairs $(M_1,f_1), (M_2,f_2)$ are called *equivalent* if there exists an isomorphism $g:M_1\rightarrow M_2$ such that the induced graded isomorphism $gr(g):gr(M_1)\rightarrow
gr(M_2)$ has the property $f_1=f_2\circ gr(g)$. Let $Equiv(S)$ denote the set of equivalence classes.

This formulation allows us to define a covariant functor $\mathcal F$ from the category of finitely generated $\mathbb{C}$-algebras $R$ (i.e., $R$ is commutative and has a $1$) to the category of sets. For a finitely generated $\mathbb{C}$-algebra $R$ one considers $K_R:=R\otimes _{\mathbb{C}}K$ and one can define the notion of difference module over $K_R$. The set ${\mathcal F}(R)$ is the set of equivalence classes of pairs $(M,f)$ with $M$ a difference module over $K_R$ and $f$ is a $K_R$-isomorphism $f:gr(M)\rightarrow K_R\otimes S$. Equivalence of two pairs is defined as above. We note that ${\mathcal F}(\mathbb{C})$ is precisely $Equiv(S)$.

One can see the functor $\mathcal F$ as a contravariant functor on the category of affine $\mathbb{C}$-schemes (of finite type).

::: theorem
The contravariant functor $\mathcal F$ on affine $\mathbb{C}$-schemes is representable. In fact, the affine space $\mathbb{A}_{\mathbb{C}}^N$ with $N=\sum _{i<j}(\lambda _j-\lambda _i)\dim P_i\cdot \dim P_j$, represents $\mathcal F$. In other words, the covariant functor $\mathcal F$ is represented by a certain universal $q$-difference module $M$ over $\mathbb{C}[X_1,\dots ,X_N]$. Further $Equiv(S)$ identifies with $\mathbb{C}^N$.
:::

For the case of integer slopes $\lambda _i$, the above result is announced by J.-P.  Ramis and J. Sauloy. The general case is treated in \[P-R\].

One can normalize the representing space $\mathbb{A}^N_{\mathbb{C}}$ by letting $0$ correspond to the class of the pair $(S,id_S)$. The vector space structure of $\mathbb{A}^N_{\mathbb{C}}$ has an interpretation for $s=2$, namely as the vector space ${\rm coker} (\Phi -1,{\rm Hom}(P_2,P_1))$. For $s>2$, the functor $\mathcal F$ and its representing space still have a weaker structure, namely that of an iterated torsor.

We illustrate Theorem 4.1 by the following *basic example*:\
$S=P_1\oplus P_2$, where $P_1=(Ke_1,\ \Phi e_1=e_1)$ and $P_2=(Ke_2,\  \Phi e_2=(-z)^te_2)$ with $t>0$. The moduli space is $\mathbb{A}^t_{\mathbb{C}}$ and the universal family above this moduli space is $$K[x_0,\dots ,x_{t-1}]e_1+K[x_0,\dots ,x_{t-1}]e_2,\  \Phi e_1=e_1,$$ $$\Phi e_2=(-z)^te_2+(x_0+x_1z+\cdots +x_{t-1}z^{t-1})e_1\ .$$ Surprisingly enough, Theorem 4.1 (for the case of integer slopes) and this example are already present in the work of Birkhoff of Guenther.

::: corollary
Every difference module $M$ over $K$ has a unique global lattice. This lattice will be called, as before, $M_{global}$. Moreover, every morphism $f:M\rightarrow N$ satisfies $f(M_{global})\subset
N_{global}$. In particular, one can extend the functor $V$ of Theorem 3.8 to the category of all $q$-difference modules over $K$.
:::

This corollary can be deduced from the Theorem 4.1 and Corollary 3.9.
