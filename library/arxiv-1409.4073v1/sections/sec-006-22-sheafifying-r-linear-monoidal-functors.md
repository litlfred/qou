---
doc_id: arxiv-1409.4073v1
doc_title: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION"
section_id: sec-006-22-sheafifying-r-linear-monoidal-functors
section_title: "Sheafifying R-linear monoidal functors."
section_number: 2.2
pages: 14-16
source_pdf: 1409.4073v1.pdf
source_sha256: b40be7f0022f70a1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.887
latex_coverage_ratio: 0.913
doc_brief: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION — We introduce “sheaﬁﬁcation” functors from categories of (lax monoidal) linear functors to categories of quasi-coherent sheaves (of algebras) of"
---
In this section we show how "ring structures" on a quasi-coherent sheaf over $\stX$ correspond to "monoidal" structures on the corresponding Yoneda functor.

We start setting up some definitions:

::: defn
[]{#def: pseudo monoidal commutativi associative label="def: pseudo monoidal commutativi associative"} Let $\catC$ and $\catD$ be $R$-linear symmetric monoidal categories. A (contravariant) *pseudo-monoidal* functor $\Omega\colon\catC\arr\catD$ is an $R$-linear (and contravariant) functor together with a natural transformation $$\iota_{V,W}^{\Omega}\colon\Omega_{V}\otimes\Omega_{W}\arr\Omega_{V\otimes W}\text{ for }V,W\in\catC$$ A (contravariant) pseudo-monoidal functor $\Omega\colon\catC\arr\catD$ is

1.  *[]{#enu:commutative for functors label="enu:commutative for functors"} symmetric* or commutative if for all $V,W\in\catC$ the following diagram is commutative$$\begin{tikzpicture}[xscale=2.7,yscale=-1.2]     \node (A0_1) at (1, 0) {$\Omega_V\otimes \Omega_W$};     \node (A0_2) at (2, 0) {$\Omega_{V\otimes W}$};     \node (A1_1) at (1, 1) {$\Omega_W\otimes \Omega_V$};     \node (A1_2) at (2, 1) {$\Omega_{W\otimes V}$};     \path (A0_1) edge [->]node [auto] {$\scriptstyle{\iota_{V,W}^\Omega}$} (A0_2);     \path (A0_2) edge [->]node [auto] {$\scriptstyle{}$} (A1_2);     \path (A1_1) edge [->]node [auto] {$\scriptstyle{\iota_{W,V}^\Omega}$} (A1_2);     \path (A0_1) edge [->]node [auto] {$\scriptstyle{}$} (A1_1);   \end{tikzpicture}$$where the vertical arrows are the obvious isomorphisms;

2.  *[]{#enu:associative for functors label="enu:associative for functors"} associative* if for all $V,W,Z\in\catC$ the following diagram is commutative $$\begin{tikzpicture}[xscale=4,yscale=-1.2]     \node (A0_0) at (0, 0) {$\Omega_V\otimes \Omega_W\otimes \Omega_Z$};     \node (A0_1) at (1, 0) {$\Omega_{V\otimes W}\otimes \Omega_Z$};     \node (A1_0) at (0, 1) {$\Omega_V\otimes \Omega_{W\otimes Z}$};     \node (A1_1) at (1, 1) {$\Omega_{V\otimes W\otimes Z}$};     \path (A0_0) edge [->]node [auto] {$\scriptstyle{\iota_{V,W}^\Omega \otimes \id}$} (A0_1);     \path (A1_0) edge [->]node [auto] {$\scriptstyle{\iota_{V,W\otimes Z}^\Omega}$} (A1_1);     \path (A0_0) edge [->]node [auto] {$\scriptstyle{\id\otimes \iota_{W,Z}^\Omega}$} (A1_0);     \path (A0_1) edge [->]node [auto] {$\scriptstyle{\iota_{V\otimes W,Z}^\Omega}$} (A1_1);   \end{tikzpicture}$$

If $I$ and $J$ are the unit objects of $\catC$ and $\catD$ respectively, a unity for $\Omega$ is a morphism $1\colon J\arr\Omega_{I}$ such that, for all $V\in\catC$, the compositions $$\Omega_{V}\otimes J\arrdi{\id\otimes1}\Omega_{V}\otimes\Omega_{I}\arrdi{\iota_{V,I}^{\Omega}}\Omega_{V\otimes I}\arr\Omega_{V}\text{ and }J\otimes\Omega_{V}\arrdi{1\otimes\id}\Omega_{I}\otimes\Omega_{V}\arrdi{\iota_{I,V}^{\Omega}}\Omega_{I\otimes V}\arr\Omega_{V}$$ coincide with the natural isomorphisms $\Omega_{V}\otimes J\arr\Omega_{V}$ and $J\otimes\Omega_{V}\arr\Omega_{V}$ respectively. A (contravariant) *monoidal* functor $\Omega\colon\catC\arr\catD$ is a symmetric and associative pseudo-monoidal (contravariant) functor with a unity $1$.
:::

A morphism of pseudo-monoidal functors $(\Omega,\iota^{\Omega})\arr(\Gamma,\iota^{\Gamma})$, called a monoidal morphism or tranformation, is a natural transformation $\Omega\arr\Gamma$ which commutes with the monoidal structures $\iota^{*}$. A morphism of monoidal functors is a monoidal transformation preserving the unities.

::: defn
[]{#def: monoidal subcategories label="def: monoidal subcategories"} We define the categories:

-   $\mathop{\mathrm{\textup{Rings}}}_{A}\stX$, whose objects are $\alB\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ with an $A$-linear map $m\colon\alB\otimes_{\odi{\stX_{A}}}\alB\arr\alB$, called the multiplication;

-   $\mathop{\mathrm{\textup{QAlg}}}_{A}\stX$, as the (not full) subcategory of $\mathop{\mathrm{\textup{Rings}}}_{A}\stX$ whose objects are $\alB$ with a commutative, associative multiplication with a unity and the arrows are morphisms preserving unities;

We also set $\mathop{\mathrm{\textup{Rings}}}\stX=\mathop{\mathrm{\textup{Rings}}}_{R}\stX$ and $\mathop{\mathrm{\textup{QAlg}}}\stX=\mathop{\mathrm{\textup{QAlg}}}_{R}\stX$.

Let $\shD$ be a monoidal subcategory of $\mathop{\mathrm{\textup{QCoh}}}\stX$, that is a subcategory such that $\odi{\stX}\in\shD$ and for all $\E,\E'\in\shD$ we have $\E\otimes\E'\in\shD$. We define the category $\mathop{\mathrm{\textup{PML}}}_{R}(\shD,A)$ (resp. $\mathop{\mathrm{\textup{ML}}}_{R}(\shD,A)$), whose objects are $\Gamma\in\L_{R}(\shD,A)$ with a pseudo-monoidal (resp. monoidal) structure.
:::

::: rem
If $q\colon\stX_{A}\arr\stX$ is the projection, the equivalence $\mathop{\mathrm{\textup{QCoh}}}\stX_{A}\arr\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ extends to an equivalence $$q_{*}\colon\mathop{\mathrm{\textup{QRings}}}\stX_{A}\arr\mathop{\mathrm{\textup{QRings}}}_{A}\stX$$ Indeed, if $\shG\in\mathop{\mathrm{\textup{QCoh}}}\stX_{A}$ then $q_{*}(\shG\otimes_{\odi{\stX_{A}}}\shG)=q_{*}\shG\otimes_{\odi{\stX_{A}}}q_{*}\shG$ (see [\[rem: remark on the tensor product over A\]](#rem: remark on the tensor product over A){reference-type="ref" reference="rem: remark on the tensor product over A"}). We will use the following notation, which is somehow implicit in the definition of $\mathop{\mathrm{\textup{QAlg}}}_{A}\stX$: a sheaf $\alB\in\mathop{\mathrm{\textup{QRings}}}_{A}\stX$ with $\alB\simeq q_{*}\alB'$ is associative (resp. commutative, has a unity, \...) if $\alB'$ has the same property.

If $\alB\in\mathop{\mathrm{\textup{QRings}}}_{A}\stX$ with multiplication $m$, then the composition $\alB\otimes_{\odi{\stX}}\alB\arr\alB\otimes_{\odi{\stX_{A}}}\alB\arrdi m\alB$ induces a ring structure on $\alB$ as an $\odi{\stX}$-module, i.e. $\alB\in\mathop{\mathrm{\textup{QRings}}}\stX$. Moreover $\alB\in\mathop{\mathrm{\textup{QRings}}}_{A}\stX$ is associative (resp. commutative, has a unity) if and only if $\alB$ has the same property. If $\alB\in\mathop{\mathrm{\textup{QAlg}}}_{A}\stX$ we can form the relative spectrum $\mathop{\mathrm{\textup{Spec}}}\alB$ over $\stX_{A}$ and also over $\stX$. The final result is the same.
:::

::: rem
For $\alB\in\mathop{\mathrm{\textup{Rings}}}_{A}\stX$ or $\Gamma\in\mathop{\mathrm{\textup{PMon}}}_{R}(\shD,A)$ having a unity is a property, not an additional datum. Indeed in both cases unities are unique.
:::

Let $\shD$ be a monoidal subcategory of $\mathop{\mathrm{\textup{QCoh}}}\stX$. If $\alB\in\mathop{\mathrm{\textup{Rings}}}_{A}\stX$ with multiplication $m$, we endow $\Omega^{\alB}\in\L_{R}(\shD,A)$ with the pseudo monoidal structure $$\iota^{\alB}\colon\mathop{\mathrm{\textup{Hom}}}(\E,\alB)\otimes_{A}\mathop{\mathrm{\textup{Hom}}}(\overline{\E},\alB)\arr\mathop{\mathrm{\textup{Hom}}}(\E\otimes\overline{\E},\alB\otimes_{\odi{\stX_{A}}}\alB)\arrdi{\mathop{\mathrm{\textup{Hom}}}(\E\otimes\overline{\E},m)}\mathop{\mathrm{\textup{Hom}}}(\E\otimes\overline{\E},\alB)\comma\E,\overline{\E}\in\shD$$ that is $\iota_{\E,\overline{\E}}^{\alB}(\phi\otimes\psi)=m\circ(\phi\otimes\psi)$. If $1\in\alB$ is a unity then we set $1_{\alB}=1\in\Omega_{\odi{\stX}}^{\alB}=\mathop{\mathrm{\textup{H}}}^{0}(\alB)$

::: prop
[]{#prop:Omegastar on algebras label="prop:Omegastar on algebras"} The structures defined above yield an extension of the functor $\Omega^{*}\colon\mathop{\mathrm{\textup{QCoh}}}_{A}\stX\arr\L_{R}(\shD,A)$ to a functor $\Omega^{*}\colon\mathop{\mathrm{\textup{QRings}}}_{A}\stX\arr\mathop{\mathrm{\textup{PML}}}_{R}(\shD,A)$. Moreover if $\alB\in\mathop{\mathrm{\textup{Rings}}}_{A}\stX$ is associative (resp. commutative, has a unity $1\in\alB$) then $\Omega^{\alB}$ is associative (resp. symmetric, has unity $1_{\alB}\in\Omega_{\odi{\stX}}^{\alB}$). In particular we also get a functor $\Omega^{*}\colon\mathop{\mathrm{\textup{QAlg}}}_{A}\stX\arr\mathop{\mathrm{\textup{ML}}}_{R}(\shD,A)$.
:::

::: proof
*Proof.* The proof is elementary and it consists of applying the definitions. ◻
:::

Let $\shC$ be a small monoidal subcategory of $\mathop{\mathrm{\textup{QCoh}}}\stX$. Given $\Gamma\in\mathop{\mathrm{\textup{PMon}}}_{R}(\shC,A)$ with monoidal structure $\iota$, we define the multiplication $m_{\Gamma}\colon\alA_{\Gamma,\shC}\otimes_{\odi{\stX_{A}}}\alA_{\Gamma,\shC}\arr\alA_{\Gamma,\shC}$ on $\alA_{\Gamma,\shC}=\shF_{\Gamma,\shC}$ by $$\alA_{\Gamma,\shC}(B)\otimes_{B\otimes_{R}A}\alA_{\Gamma,\shC}(B)\ni x_{\E,\psi}\otimes\overline{x}_{\overline{\E},\overline{\psi}}\arr\iota_{\E,\overline{\E}}(x\otimes\overline{x})_{\E\otimes\overline{\E},\psi\otimes\overline{\psi}}\in\alA_{\Gamma,\shC}(B)$$ where $\mathop{\mathrm{\textup{Spec}}}B\arr\stX$ is a map, $\E,\overline{\E}\in\shC$, $\psi\in\E(B)$, $\overline{\psi}\in\overline{\E}(B)$, $x\in\Gamma_{\E}$, $\overline{x}\in\Gamma_{\overline{\E}}$ (see [\[def: unit and counit for adjunction\]](#def: unit and counit for adjunction){reference-type="ref" reference="def: unit and counit for adjunction"}). We continue to denote by $\alA_{\Gamma,\shC}$ the sheaf $\shF_{\Gamma,\shC}$ together with the multiplication map just defined. If $1\in\Gamma_{\odi{\stX}}$ is a unity we set $1_{\Gamma}\in\alA_{\Gamma,\shC}$ the image of $1$ under the morphism $\Gamma_{\odi{\stX}}\arr\Omega_{\odi{\stX}}^{\alA_{\Gamma,\shC}}=\mathop{\mathrm{\textup{H}}}^{0}(\alA_{\Gamma,\shC})$.

::: prop
[]{#prop: from sheaves to algebras label="prop: from sheaves to algebras"}The structures defined above yield an extension of the functor $\shF_{*,\shC}\colon\L_{R}(\shC,A)\arr\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ to a functor $\alA_{*,\shC}\colon\mathop{\mathrm{\textup{PML}}}_{R}(\shC,A)\arr\mathop{\mathrm{\textup{Rings}}}_{A}\stX$ which is left adjoint to $\Omega^{*}\colon\mathop{\mathrm{\textup{Rings}}}_{A}\stX\arr\mathop{\mathrm{\textup{PML}}}_{R}(\shC,A)$. More precisely, if $\alB\in\mathop{\mathrm{\textup{Rings}}}_{A}\stX$ then the morphism $\delta_{\alB}\colon\alA_{\Omega^{\alB},\shC}\arr\alB$ preserves multiplications and unities, while if $\Gamma\in\mathop{\mathrm{\textup{PMon}}}_{R}(\shC,A)$ then the natural transformation $\gamma_{\Gamma}\colon\Gamma\arr\Omega^{\alA_{\Gamma,\shC}}$ is monoidal and preserves unities (see [\[def: unit and counit for adjunction\]](#def: unit and counit for adjunction){reference-type="ref" reference="def: unit and counit for adjunction"}).

If $\Gamma\in\mathop{\mathrm{\textup{PMon}}}_{R}(\shC,A)$ is associative (resp. symmetric, has a unity $1\in\Gamma_{\odi{\stX}}$) then $\alA_{\Gamma,\shC}$ is associative (resp. commutative, has unity $1_{\Gamma}\in\alA_{\Gamma,\shC}$). In particular we get a functor $\alA_{*,\shC}\colon\mathop{\mathrm{\textup{ML}}}_{R}(\shC,A)\arr\mathop{\mathrm{\textup{QAlg}}}_{A}\stX$ which is left adjoint to $\Omega^{*}\colon\mathop{\mathrm{\textup{QAlg}}}_{A}\stX\arr\mathop{\mathrm{\textup{ML}}}_{R}(\shC,A)$.
:::

::: proof
*Proof.* A lot of properties have to be checked. All of them are very easy, because they consist only in the application of the definitions. We therefore leave them to the reader. ◻
:::
