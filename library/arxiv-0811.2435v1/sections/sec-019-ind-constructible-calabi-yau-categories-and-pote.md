---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-019-ind-constructible-calabi-yau-categories-and-pote
section_title: "Ind-constructible Calabi-Yau categories and potentials"
section_number: null
pages: 53-56
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.972
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Let $\k$ be a field of characteristic zero. Recall that a Calabi-Yau category of dimension $d$ is a weakly unital $\k$-linear triangulated $\A$-category ${\CC}$ (see [@KoSo2], [@KoSo3], [@So1]), such that for any two objects $E,F$ the $\Z$-graded vector space $\op{Hom}^\bullet(E,F)=\oplus_{n\in \Z}\op{Hom}^n(E,F)$ is finite-dimensional (hence the space $\op{Ext}^\bullet(E,F)$ is also finite-dimensional) and moreover:

1\) We are given a non-degenerate pairing $$(\bullet, \bullet): \op{Hom}^{\bullet}(E,F)\otimes \op{Hom}^{\bullet}(F,E)\to \k[-d]\,\,,$$ which is symmetric with respect to interchange of objects $E$ and $F$;

2\) For any $N\geqslant 2$ and a sequence of objects $E_1,E_2,\dots,E_N$ we are given a polylinear $\Z/N\Z$-invariant map $$W_N: \otimes_{1\le i\le N}\left(\op{Hom}^{\bullet}(E_i,E_{i+1})[1]\right)\to \k[3-d]\,\,,$$ where $[1]$ means the shift in the category of $\Z$-graded vector spaces, and we set $E_{N+1}=E_1$;

3\) We have: $$W_N(a_1,\dots,a_{N})=(m_{N-1}(a_1,\dots,a_{N-1}),a_N)\,\,,$$ where $m_n: \otimes_{1\le i\le n}\op{Hom}^{\bullet}(E_i,E_{i+1})\to \op{Hom}^{\bullet}(E_1,E_{n+1})[2-n]$ are higher composition maps.

The collection $(W_N)_{N\geqslant 2}$ is called the *potential of $\CC$*. If $d=3$ then for any object $E\in Ob(\CC)$ we define a formal series $W_{E}^{tot}$ at $0\in \op{Hom}^{\bullet}(E,E)[1]$ by the formula: $$W_E^{tot}(\alpha)=\sum_{n\geqslant 2}{W_n(\alpha,\dots, \alpha)\over{n}}\,\,.$$ We call $W_E^{tot}$ the *total (or full) potential of the object $E$*. We call the *potential of $E$* the restriction of $W_E^{tot}$ to the subspace $\op{Hom}^1(E,E)$. We will denote it by $W_E$.

The notion of a Calabi-Yau category admits a natural generalization to the ind-constructible case (the pairing is required to be a morphism of constructible vector bundles). It follows from the Axiom A3) that there exists a decomposition of $Ob(\CC)\simeq \sqcup S_i$ into the disjoint union of schemes such that all Taylor components $W_N$ of the potential are symmetrizations of regular sections of cyclic powers of algebraic vector bundles on schemes $S_i$. Therefore we can treat the family of potentials $W_{\CC}=(W_E)_{E\in Ob(\CC)}$ as a function, which is regular with respect to the variable $E$ and formal in the direction $\alpha\in \op{Hom}^1(E,E)$ (or $\alpha\in \op{Ext}^1(E,E)$ if our category is minimal on the diagonal). Also the potential $W_E$ considered as a function of $E\in S_j$ becomes a section of the pro-algebraic vector bundle $\prod_{n\geqslant 2}Sym^n({\cal HOM}^1_{|Diag(S_j)\subset S_j\times S_j})^\star$, where $Diag$ denotes here the diagonal embedding.

::: prp
In the case of $3d$ Calabi-Yau category $\CC$ consisting of one object $E$ the potential $W_E$ admits (after a formal change of coordinates) a splitting: $$W_E=W_E^{min}\oplus Q_E\oplus N_E\,\,,$$ where $W_E^{min}$ is the potential of the minimal model $\CC^{min}$ (i.e. it is a formal series on $\op{Ext}^1(E,E)$), the quadratic form $Q_E$ is defined on the vector space $\op{Hom}^1(E,E)/\op{Ker}(m_1:\op{Hom}^1(E,E)\to \op{Hom}^2(E,E))$ by the formula $Q_E(\alpha,\alpha)={m_2(\alpha,\alpha)\over{2}}$, and $N_E$ is the zero function on the image of the map $m_1:\op{Hom}^0(E,E)\to \op{Hom}^1(E,E)$. In the above splitting formula we use the notation $(f\oplus g)(x,y)=f(x)+g(y)$ for the direct sum of formal functions $f$ and $g$.
:::

The above Proposition follows from the minimal model theorem for Calabi-Yau algebras (i.e. Calabi-Yau categories with only one object). In its formulation below we are going to use the language of formal non-commutative geometry from [@KoSo3]. We assume that the ground field has characteristic zero.

::: thm
a\) Let $(X,x_0,\omega,d_X)$ be a $\Z/2\Z$-graded non-commutative formal pointed manifold $(X,x_0)$ endowed with an odd symplectic form $\omega$ and homological vector field $d_X$ which preserves $\omega$ and vanishes at $x_0$. Then it is isomorphic to the product $$(X^{\prime}, x_0^{\prime},\omega^{\prime}, d_{X^{\prime}})\times (X^{\prime\prime}, x_0^{\prime\prime},\omega^{\prime\prime}, d_{X^{\prime\prime}})\,\,,$$ where $(X^{\prime}, x_0^{\prime},\omega^{\prime}, d_{X^{\prime}})$ is minimal in the sense that $(Lie_{d_{X^{\prime}}})_{|T_{x_0^{\prime}X^{\prime}}}=0$ (i.e. $d_{X^{\prime}}$ vanishes quadratically at $x_0^{\prime}$), and the second factor satisfies the following property: there exists a finite-dimensional super vector space $V$ endowed with an even non-degenerate quadratic form $Q_V$ such that $(X^{\prime\prime}, x_0^{\prime\prime},\omega^{\prime\prime}, d_{X^{\prime\prime}})$ is isomorphic to the non-commutative formal pointed manifold associated with $V\oplus \Pi V^{\ast}$ (here $\Pi$ is the change of parity functor) endowed with a constant symplectic form $\omega_V$ coming from the natural pairing between $V$ and $\Pi V^{\ast}$, and homological vector field $d_V$ is the Hamiltonian vector field associated with the pull-back of $Q_V$ under the natural projection $V\oplus \Pi V^{\ast}\to V$.

b\) In the $\Z$-graded case when $X$ corresponds to a $3d$ Calabi-Yau algebra (i.e. $\omega$ has degree $-1$) a similar statement holds. In this case $V$ is $\Z$-graded vector space, $Q_V$ has degree $0$, and the tangent space $T_{x_0^{\prime\prime}}X^{\prime\prime}$ isomorphic to $V\oplus V^{\ast}[-1]$.
:::

*Proof.* One can prove part a) similarly to the usual minimal model theorem for $\A$-algebras or $L_{\infty}$-algebras (it is induction by the order of the Taylor expansion, see e.g. [@KoSo2]). Part b) is a ${\bf G}_m$-equivariant version of part a). $\blacksquare$

The Proposition follows from part b) of the Theorem, since we have a decomposition $\op{Hom}^1(E,E)\simeq \op{Ext}^1(E,E)\oplus V^0\oplus (V^1)^{\ast}$ where $V^i,i\in \Z$ are the graded components of $V$. The restriction of $W^{tot}_E$ to $\op{Hom}^1(E,E)$ is the direct sum of $W_E^{min}$, the restriction of $Q_V$ to $V^0$ (we identify $Q_V$ with $Q_E$) and the zero function on $(V^1)^{\ast}$.

::: cor
The minimal model potential $W_E^{min}$ does not depend on a choice of minimal model for $\op{End}^\bullet(E)$, if considered up to a formal non-linear automorphism of the bundle ${\cal HOM}^1$ restricted to the diagonal $Diag(S_j)\subset S_j\times S_j$.
:::

*Proof.* Change of the minimal model is a $\Z$-graded change of coordinates. It preserves the topological ideal generated by all coordinates of non-zero degrees. $\blacksquare$

We remark that there is a notion of Calabi-Yau category valid over a field $\k$ of arbitrary characteristic. In the case of a category with one object $E$ let us denote by $A$ the $\A$-algebra $\op{Hom}^{\bullet}(E,E)$. We assume that $\op{Ext}^\bullet(E,E)=H^\bullet(A)$ is finite-dimensional. Then a Calabi-Yau structure of dimension $d$ on $A$ is given by a functional $Tr$ of degree $-d$ on the cyclic homology $HC_{\bullet}(A)$ such that the induced functional on $H^{\bullet}(A)/[H^{\bullet}(A),H^{\bullet}(A)]$ gives rise to a non-degenerate bilinear form $(a,b)\mapsto Tr(ab)$, where $a,b\in H^{\bullet}(A)$.

In the case of positive characteristic the notion of the potential does not exist in the conventional sense. This can be seen in the example $A={\bf F}_3\langle \xi\rangle/(\xi^4), \op{deg}\xi=+1$. The potential should have the form $W(\xi)=\xi^3/3+\dots$ which does not make sense over the field ${\bf F}_3$.

In general it seems that although the potential does not exist, its differential is well-defined as a closed $1$-form.

::: rmk
In the case of characteristic zero the cyclic homology $HC_{\bullet}(A)$ can be identified with the cohomology of the complex $\oplus_{n\geqslant 1}Cycl^n(A[1])$ of cyclically invariant tensors (see [@KoSo3]). Therefore the potential $W$ becomes a functional of degree $3-d$ on the latter complex, vanishing on the image of the differential. Hence it defines a class $[W]$ in $(HC_{\bullet}(A))^{\ast}$. The latter space is a $\k[[u]]$-module, where $u$ is a variable, $\op{deg} u=+2$ (see loc. cit.). The class $[W]$ is related to the functional $Tr$ discussed above by the formula $[W]=uTr$. In the case of a Calabi-Yau algebra of dimension $d=2k+1$ it is natural to introduce a cyclic functional $W_k$ with the corresponding class $[W_k]=u^kTr$. It can be thought of as a higher-dimensional Chern-Simons action. In particular, it defines a formal power series $W_k^0$ of degree zero such that it vanishes with the first $k$ derivatives on the formal scheme of solutions to the Maurer-Cartan equation.
:::
