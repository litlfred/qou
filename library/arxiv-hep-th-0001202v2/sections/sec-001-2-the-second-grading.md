---
doc_id: arxiv-hep-th-0001202v2
doc_title: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees"
section_id: sec-001-2-the-second-grading
section_title: "The second grading"
section_number: 2
pages: 3-4
source_pdf: 0001202v2.pdf
source_sha256: b2e3e22ea3d51c0b
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.993
doc_brief: "Towards cohomology of renormalization: bigrading the combinatorial Hopf algebra of rooted trees — The renormalization of quantum ﬁeld theory twists the antipode of a non- cocommutative Hopf algebra"
---
The weight $n$ of a rooted tree $t$ is the number of its nodes. The weight of a forest $F=\prod_j t_j$ is the sum of the weights of the trees $t_j$ in the product. This is the first grading.

To define the index $k$ for the second grading, $k$-primitivity, we use $k$-fold iterations of the coproduct $\Delta$, defined by the highly nontrivial recursion [@DK] $$\Delta(t)=t\otimes e+({\rm id}\otimes B_+)\circ\Delta\circ B_-(t)
\label{D}$$ for a nonempty tree $t$. Here $e$ is the empty tree, evaluating to unity, ${\rm id}$ is the identity map, $B_-$ removes the root of $t$, and $B_+$ combines the trees of a product by appending them to a common root. The coproduct $\Delta$ is coassociative. Hence it has a unique iteration, which may be written in a variety of equivalent ways. Since $\Delta$ has only single trees on the right, the recursion $$\Delta^k=({\rm id}\otimes\Delta^{k-1})\circ\Delta
\label{Dk}$$ is particularly convenient. For a forest $F=\prod_j t_j$ we have $\Delta^k(F)=\prod_j\Delta^k(t_j)$.

Let $X$ be a ${\Qb}$-linear combination of monomials of trees, i.e. of forests. We say that $X$ is $k$-primitive if every term of $\Delta^k(X)$ has at least one empty tree $e$. Symbolically we may consider the composition of tensor products of the projection operator $P:={\rm
id}-E\circ\bar{e}$ with iterations of $\Delta$. $P$ projects onto the augmentation ideal ${\cal H}_c=\{X\in{\cal H}_R\mid P(X)=X\}$, where $X=P(X)+E\circ\bar{e}(X)$. Here $\bar{e}$ is the counit, which annihilates everything except the empty tree, for which it gives $\bar{e}(e)=1$. The map from the rationals back to the algebra is simply $E(q)=q e$ for $q\in{\Qb}$. Hence $P$ annihilates $e$ and leaves everything else unchanged. Let $U_0:=P$ and $$U_k:=(\underbrace{P\otimes\ldots\otimes P}_{k+1~{\rm times}})\circ\Delta^k
=(P\otimes U_{k-1})\circ\Delta
\label{Uk}$$ for $k>0$. In using the recursive form, note should be taken that, in general, the projection makes $U_k(X_1X_2)\not=U_k(X_1)U_k(X_2)$: one should store results for forests; not just for trees.

We have said that $X$ is $k$-primitive if $U_k(X)=0$. Then clearly $X$ is $(k+1)$-primitive, since $\Delta^{k+1}(X)$ has at least two empty trees $e$ in every term. We are interested in the number, $H_{n,k}:=D_{n,k}-D_{n,k-1}$, of weight-$n$ terms that are $k$-primitive but are not $(k-1)$-primitive, where $D_{n,k}$ is the dimension of the subspace with weight $n$ and index $k$. To compute $D_{n,k}$ for specific (and rather modest) values of $n,k$ one considers the most general linear combination $X$ of weight-$n$ terms, with unknown coefficients, and solves $U_k(X)=0$. The rank deficiency of this large system of linear equations is $D_{n,k}$. From this one subtracts the number $D_{n,k-1}$ of weight-$n$ terms that are $(k-1)$-primitive. By this means we obtained the first 7 rows of Tables 1 and 2, for the Hopf subalgebras ${\cal H}_{\rm ladder}$ and ${\cal H}_{\rm CM}$, and inferred their generating principles. In the case of the full Hopf algebra ${\cal H}_R$, bigraded in Table 3, data were much harder to obtain. Fortunately the generating principle is very distinctive.
