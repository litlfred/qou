---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-001-2-results-on-squared-norms-global-dimensions-wea
section_title: "Results on squared norms, global dimensions, weak Hopf algebras, and Ocneanu rigidity"
section_number: 2
pages: 3-4
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.895
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
Let $k$ be an algebraically closed field. By a *multi-fusion* category over $k$ we mean a rigid semisimple $k$-linear tensor category ${\mathcal C}$ with finitely many simple objects and finite dimensional spaces of morphisms. If the unit object $\bold 1$ of ${\mathcal C}$ is simple, then the category ${\mathcal C}$ is said to be a *fusion* category. Otherwise (if $\bold 1$ is not simple), it is easy to see that we have $\mathbf 1=\oplus_{i\in J}\mathbf 1_i$, where $\mathbf 1_i$ are pairwise nonisomorphic simple objects.

Let us list a few examples to keep in mind when thinking about fusion and multi-fusion categories.

.05in

**Examples of fusion categories.**

1\. The category ${\rm Vec}_{G}$ of finite dimensional vector spaces graded by a finite group $G$ (or, equivalently, finite dimensional modules over the function algebra ${\rm Fun}(G,k)$.) Simple objects in this category are evaluation modules $V_g$, $g\in G$, and the tensor product is given by $V_g\otimes V_h=V_{gh}$, with the associativity morphism being the identity.

More generally, pick a 3-cocycle $\omega\in
Z^3(G,k^\times)$. To this cocycle we can attach a twisted version ${\rm Vec}_{G,\omega}$ of ${\rm Vec}_{G}$: the simple objects and the tensor product functor are the same, but the associativity isomorphism is given by $\Phi_{V_g,V_h,V_k}=\omega(g,h,k)\textrm{id}$. The pentagon axiom then follows from the cocycle condition $$\omega(h,k,l)\omega(g,hk,l)\omega(g,h,k)=\omega(gh,k,l)\omega(g,h,kl).$$ Note that cohomologous cocycles define equivalent fusion categories.

2\. The category of finite dimensional $k$-representations of a finite group $G$, whose order is relatively prime to the characteristic of $k$.

3\. The category of integrable modules (from category $\mathcal O$) over the affine algebra $\widehat{sl}_2$ at level $l$ (see [@BaKi]). The tensor product in this category is the fusion product, defined at the level of objects by the Verlinde fusion rule $$V_i\otimes
V_j=\sum_{\substack{k=\vert i-j\vert
\\ k\equiv i+j~\textrm{mod}~2}}^{l-\vert i+j-l\vert}V_k$$ .05in

**Examples of multi-fusion categories.**

1\. The category of finite dimensional bimodules over a finite dimensional semisimple $k$-algebra, with bimodule tensor product. It has simple objects $M_{ij}$ with "matrix" tensor product $M_{ij}\otimes
M_{jk}=M_{ik}$; thus the identity object is $\bold 1=\oplus_i M_{ii}$.

2\. The category of finite dimensional modules over the function algebra on a finite groupoid.
