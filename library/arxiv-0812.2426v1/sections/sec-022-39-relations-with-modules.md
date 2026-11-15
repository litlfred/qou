---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-022-39-relations-with-modules
section_title: "Relations with modules"
section_number: 3.9
pages: 13-14
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.917
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
The notions of bimonads, Hopf monads, quasitriangular Hopf monads, or ribbon Hopf monads have a natural interpretation in terms of the category of modules over the underlying monad. We summarize these properties in the following theorem:

::: thm
[]{#thm-biHopfmon label="thm-biHopfmon"}

1.  Let $T$ be a monad on a monoidal category $\mathcal{C}$. If $T$ is a bimonad, then the category $T\mbox{-}\,\mathcal{C}$ of $T$-modules is monoidal by setting: $$(M,r) \otimes_{T\mbox{-}\,\mathcal{C}} (N,s)=(M \otimes N, (r \otimes s) T_2(M,N)) \quad \text{and} \quad \mathbb{1}_{T\mbox{-}\,\mathcal{C}}=(\mathbb{1},T_0).$$ Moreover this gives a bijective correspondence between bimonad structures for the monad $T$ and monoidal structures of $T\mbox{-}\,\mathcal{C}$ such that the forgetful functor $U_T \colon T\mbox{-}\,\mathcal{C}\to \mathcal{C}$ is strict monoidal.

2.  Let $T$ be a bimonad on a left autonomous $\mathcal{C}$. Then $T$ has a left antipode $s^l$ if and only if the category $T\mbox{-}\,\mathcal{C}$ of $T$-modules is left autonomous. In terms of a left antipode $s^l$, left duals in $T\mbox{-}\,\mathcal{C}$ are given by: $$\leftidx{^\vee}{\!(M,r)}{}=(\leftidx{^\vee}{\!M}{}, s^l_M T(\leftidx{^\vee}{\!r}{})),\quad \mathrm{ev}_{(M,r)}=\mathrm{ev}_M, \quad\mathrm{coev}_{(M,r)}=\mathrm{coev}_M.$$

3.  Let $T$ be a bimonad on a right autonomous $\mathcal{C}$. Then $T$ has a right antipode $s^l$ if and only if the category $T\mbox{-}\,\mathcal{C}$ of $T$-modules is right autonomous. In terms of a right antipode $s^r$, right duals in $T\mbox{-}\,\mathcal{C}$ are given by: $${(M,r)}^\vee=({M}^\vee, s^r_M T({r}^\vee)),\quad \widetilde{\mathrm{ev}}_{(M,r)}=\widetilde{\mathrm{ev}}_M, \quad\widetilde{\mathrm{coev}}_{(M,r)}=\widetilde{\mathrm{coev}}_M.$$

4.  Let $T$ be a bimonad on an autonomous $\mathcal{C}$. Then $T$ is a Hopf monad if and only if the category $T\mbox{-}\,\mathcal{C}$ of $T$-modules is autonomous.

5.  Let $T$ be a bimonad on a monoidal category $\mathcal{C}$. Any $\mathrm{R}$-matrix $R$ for $T$ yields a braiding $\tau$ on $T\mbox{-}\,\mathcal{C}$ as follows: $$\tau_{(M,r),(N,s)}=(s \otimes t)R_{M,N}\colon(M,r) \otimes (N,s) \to (N,s) \otimes (M,r).$$ This assignment gives a bijection between $\mathrm{R}$-matrices for $T$ and braidings on $T\mbox{-}\,\mathcal{C}$.

6.  Let $T$ be a quasitriangular Hopf monad on an autonomous category $\mathcal{C}$. Any twist $\theta$ for $T$ yields a twist $\Theta$ on $T\mbox{-}\,\mathcal{C}$ as follows: $$\Theta_{(M,r)}=r \theta_M\colon(M,r) \to (M,r).$$ This assignment gives a bijection between twists for $T$ and twists on $T\mbox{-}\,\mathcal{C}$. Moreover, in this correspondence, $\theta$ is self-dual (and so $T$ is ribbon) if and only if $\Theta$ is self-dual (and so $T\mbox{-}\,\mathcal{C}$ is ribbon).
:::
