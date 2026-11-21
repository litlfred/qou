---
doc_id: arxiv-1409.4073v1
doc_title: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION"
section_id: sec-004-2-sheafification-functors
section_title: "Sheafification functors."
section_number: 2
pages: 9-10
source_pdf: 1409.4073v1.pdf
source_sha256: b40be7f0022f70a1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.933
doc_brief: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION — We introduce “sheaﬁﬁcation” functors from categories of (lax monoidal) linear functors to categories of quasi-coherent sheaves (of algebras) of"
---
In this section we define and describe particular functors that generalize sheafification functors for affine schemes or projective schemes. The idea is to interpret the category of modules or graded modules respectively as a category of $R$-linear functors. More precisely:

::: defn
Given a fibered category $\stX$ over a ring $R$, an $R$-algebra $A$ and a subcategory $\shD$ of $\mathop{\mathrm{\textup{QCoh}}}\stX$ we define $\L_{R}(\shD,A)$ as the category of contravariant $R$-linear functors $\Gamma\colon\shD\arr\mathop{\mathrm{\textup{Mod}}}A$ and natural transformations as arrows. We define a functor $\Omega^{*}\colon\mathop{\mathrm{\textup{QCoh}}}_{A}\stX\arr\L_{R}(\shD,A)$ by $$\Omega_{-}^{\shF}=\mathop{\mathrm{\textup{Hom}}}_{\stX}(-,\shF)\colon\shD\arr\mathop{\mathrm{\textup{Mod}}}A$$ The functor $\Omega^{*}$ is called the *Yoneda functor* associated with $\shD$. A left adjoint of $\Omega^{*}$ is called a *sheafification* functor associated with $\shD$. If $\shF\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ we will call $\Omega^{\shF}$ the Yoneda functor associated with $\shF$.
:::

::: example
[]{#example: quasi-projective case label="example: quasi-projective case"} The analogy with the sheafification functor associated with $\stX=\PP_{R}^{n}$ or any quasi-projective and quasi-compact scheme over $R$ is the following. If $\shC=\{\odi{\stX}(n)\}_{n\in\Z}$ then with $\Gamma\in\L_{R}(\shC,R)$ we can associate the $\Z$-graded $R$-module $M=\bigoplus_{n\in\Z}\Gamma_{\odi{\stX}(-n)}$. The functorial properties of $\Gamma$ allow us to define a structure of graded $S$-module on $M$, where $S=\bigoplus_{n\in\Z}\mathop{\mathrm{\textup{H}}}^{0}(\odi{\stX}(n))$ is the homogeneous coordinate ring of $\stX$. This associations extends to an equivalence of categories between $\L_{R}(\shC,R)$ and the category of graded $S$-modules. The functor $\Omega^{*}$ corresponds to the functor $\Gamma_{*}$ which carries a quasi-coherent sheaf $\shF$ on $\stX$ to the graded $S$-module $\bigoplus_{n\in\Z}\mathop{\mathrm{\textup{H}}}^{0}(\shF(n))$. Finally the sheafification functor from the graded $S$-modules to $\mathop{\mathrm{\textup{QCoh}}}\stX$ is left adjoint to $\Gamma_{*}$.
:::

Let us fix an $R$-algebra $A$ and a fibered category $\pi\colon\stX\arr\mathop{\mathrm{\textup{Aff}}}/R$.
