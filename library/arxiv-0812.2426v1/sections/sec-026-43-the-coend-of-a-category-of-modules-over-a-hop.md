---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-026-43-the-coend-of-a-category-of-modules-over-a-hop
section_title: "The coend of a category of modules over a Hopf monad"
section_number: 4.3
pages: 16-16
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.961
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
Let $T$ be a centralizable Hopf monad on an autonomous category $\mathcal{C}$. Denote $Z_T$ its centralizer, $i_{X,Y} \colon
\leftidx{^\vee}{\!T(Y)}{} \otimes X \otimes Y \to Z_T(X)$ its associated universal dinatural transformation, and $\Omega\colon TZ_T \to
Z_TT$ the canonical distributive law of $T$ over $Z_T$. Then :

::: thm
[]{#thm-coend label="thm-coend"} The category $T\mbox{-}\,\mathcal{C}$ of $T$-modules admits a coend, which is: $$\int^{(M,r) \in T\mbox{-}\,\mathcal{C}}\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\! \leftidx{^\vee}{\!(M,r)}{} \otimes
(M,r)=\bigl(Z_T(\mathbb{1}),Z_T(T_0)\Omega_\mathbb{1}\bigr),$$ with $I_{(M,r)}=i_{\mathbb{1},M}(\leftidx{^\vee}{\!r}{} \otimes \mathrm{id}_M)\colon\leftidx{^\vee}{\!(M,r)}{} \otimes (M,r) \to
\bigl(Z_T(\mathbb{1}),Z_T(T_0)\Omega_\mathbb{1}\bigr)$ as universal dinatural transformation.
:::

Note that if $T$ is furthermore quasitriangular, then $T\mbox{-}\,\mathcal{C}$ is braided and so the coend $\bigl(Z_T(\mathbb{1}),Z_T(T_0)\Omega_\mathbb{1}\bigr)$ is a Hopf algebra in $T\mbox{-}\,\mathcal{C}$.

::: rem
If we apply this to the double $D_T$ of a centralizable Hopf monad, which we suppose to be itself centralizable, we get an explicit description of the coend of the braided category $D_T \mbox{-}\,\mathcal{C}\cong \mathcal{Z}(T\mbox{-}\,\mathcal{C})$ in terms of the monad $T$. Using this description and Hopf diagrams, we hence have a way of computing the quantum invariants of 3-manifolds defined using $\mathcal{Z}(T\mbox{-}\,\mathcal{C})$, see Section [\[sect-Hdiag\]](#sect-Hdiag){reference-type="ref" reference="sect-Hdiag"}. In the next section, we explicit the case where $\mathcal{C}$ is a spherical fusion category and $T=1_\mathcal{C}$.
:::
