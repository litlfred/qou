---
doc_id: arxiv-1409.4073v1
doc_title: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI"
section_id: sec-003-2-sheafification-functors
section_title: "Sheafification functors."
section_number: 2
pages: 9-16
source_pdf: 1409.4073v1.pdf
source_sha256: b40be7f0022f70a1
text_source: latex
latex_prose_ratio: 0.807
latex_coverage_ratio: 0.91
doc_brief: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI — W e introduce “sheaﬁﬁcation” functors from categories of (l ax monoidal) linear functors to categories of quasi-coherent sheaves"
---
In this section we define and describe particular functors that generalize sheafification functors for affine schemes or projective schemes. The idea is to interpret the category of modules or graded modules respectively as a category of $R$-linear functors. More precisely:

::: defn
Given a fibered category $\stX$ over a ring $R$, an $R$-algebra $A$ and a subcategory $\shD$ of $\mathop{\mathrm{\textup{QCoh}}}\stX$ we define $\L_{R}(\shD,A)$ as the category of contravariant $R$-linear functors $\Gamma\colon\shD\arr\mathop{\mathrm{\textup{Mod}}}A$ and natural transformations as arrows. We define a functor $\Omega^{*}\colon\mathop{\mathrm{\textup{QCoh}}}_{A}\stX\arr\L_{R}(\shD,A)$ by $$\Omega_{-}^{\shF}=\mathop{\mathrm{\textup{Hom}}}_{\stX}(-,\shF)\colon\shD\arr\mathop{\mathrm{\textup{Mod}}}A$$ The functor $\Omega^{*}$ is called the *Yoneda functor* associated with $\shD$. A left adjoint of $\Omega^{*}$ is called a *sheafification* functor associated with $\shD$. If $\shF\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ we will call $\Omega^{\shF}$ the Yoneda functor associated with $\shF$.
:::

::: example
[]{#example: quasi-projective case label="example: quasi-projective case"} The analogy with the sheafification functor associated with $\stX=\PP_{R}^{n}$ or any quasi-projective and quasi-compact scheme over $R$ is the following. If $\shC=\{\odi{\stX}(n)\}_{n\in\Z}$ then with $\Gamma\in\L_{R}(\shC,R)$ we can associate the $\Z$-graded $R$-module $M=\bigoplus_{n\in\Z}\Gamma_{\odi{\stX}(-n)}$. The functorial properties of $\Gamma$ allow us to define a structure of graded $S$-module on $M$, where $S=\bigoplus_{n\in\Z}\mathop{\mathrm{\textup{H}}}^{0}(\odi{\stX}(n))$ is the homogeneous coordinate ring of $\stX$. This associations extends to an equivalence of categories between $\L_{R}(\shC,R)$ and the category of graded $S$-modules. The functor $\Omega^{*}$ corresponds to the functor $\Gamma_{*}$ which carries a quasi-coherent sheaf $\shF$ on $\stX$ to the graded $S$-module $\bigoplus_{n\in\Z}\mathop{\mathrm{\textup{H}}}^{0}(\shF(n))$. Finally the sheafification functor from the graded $S$-modules to $\mathop{\mathrm{\textup{QCoh}}}\stX$ is left adjoint to $\Gamma_{*}$.
:::

Let us fix an $R$-algebra $A$ and a fibered category $\pi\colon\stX\arr\mathop{\mathrm{\textup{Aff}}}/R$.

## Sheafifying $R$-linear functors.

In this section we want to explicitly describe sheafification functors for small subcategories of $\mathop{\mathrm{\textup{QCoh}}}\stX$. In particular we fix a *small* (and non empty) subcategory $\shC$ of $\mathop{\mathrm{\textup{QCoh}}}\stX$.

In the construction of the sheafification functors we will make use of the coend construction in the settings of categories enriched over categories of modules over a ring. The general theory simplifies considerably in this context and we will also apply such construction only in particular cases. In the following remark we collect all the properties we will need.

::: rem
[]{#rem: coends label="rem: coends"} Let $\stY$ be a fibered category over $R$, $F\colon\shC\arr\mathop{\mathrm{\textup{QCoh}}}\stY$ be an $R$-linear functor and $\Gamma\in\L_{R}(\shC,A)$. The coend of the $R$-linear functor $\Gamma_{-}\otimes_{R}F_{-}\colon\shC^{\mathop{\mathrm{\textup{op}}}}\otimes\shC\arr\mathop{\mathrm{\textup{QCoh}}}_{A}\stY$, denoted by $$\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}F_{\E}\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stY$$ is the cokernel of the map $$\bigoplus_{\E\arrdi u\overline{\E}}(\Gamma_{u}\otimes\id_{F_{\E}}-\id_{\Gamma_{\overline{\E}}}\otimes F_{u})\colon\bigoplus_{\E\arrdi u\overline{\E}}\Gamma_{\overline{\E}}\otimes_{R}F_{\E}\arr\bigoplus_{\E\in\shC}\Gamma_{\E}\otimes_{R}F_{\E}$$ Moreover it comes equipped with an $A$-linear natural isomorphism $$\mathop{\mathrm{\textup{Hom}}}_{\mathop{\mathrm{\textup{QCoh}}}_{A}\stY}(\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}F_{\E},\shH)\arrdi{\alpha}\mathop{\mathrm{\textup{Hom}}}_{\L_{R}(\shC,A)}(\Gamma,\mathop{\mathrm{\textup{Hom}}}_{\stY}(F_{-},\shH))\text{ for }\shH\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stY$$ given by $$\alpha(\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}F_{\E}\arrdi u\shH)(x)=u\circ p_{\overline{\E}}(x\otimes-)\colon F_{\overline{\E}}\arr\shH\text{ for }\overline{\E}\in\shC,x\in\Gamma_{\overline{\E}}$$ where $p_{\E}\colon\Gamma_{\E}\otimes_{R}F_{\E}\arr\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}F_{\E}$ for $\E\in\shC$ are the structure morphisms. Its inverse is uniquely determined by the expression $$\alpha^{-1}(\Gamma\arrdi v\mathop{\mathrm{\textup{Hom}}}_{\stY}(F_{-},\shH))\circ p_{\E}\colon\Gamma_{\E}\otimes_{R}\E\arr\shH\comma x\otimes y\longmapsto v_{\E}(x)(y)\text{ for }\E\in\shC$$ Natural transformations $F\arr F'$ and $\Gamma\arr\Gamma'$ yields morphisms $\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}F_{\E}\arr\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}F'_{\E}$ and $\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}F_{\E}\arr\int^{\E\in\shC}\Gamma'_{\E}\otimes_{R}F_{\E}$ respectively. Those can be defined either using Yoneda's lemma and the above characterization of $\mathop{\mathrm{\textup{Hom}}}(\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}F_{\E},-)$ or directly using the description of $\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}F_{\E}$ as a cokernel.

All the above claims are standard in the theory of coend in the enriched settings (in our case enriched by $\mathop{\mathrm{\textup{Mod}}}R$), but, in this simplified context, it is elementary to prove them directly.
:::

We start by showing that $\shC$ (and therefore any essentially small subcategory of $\mathop{\mathrm{\textup{QCoh}}}\stX$) admits a sheafification functor.

::: prop
[]{#prop:adjoint of Omegastar with the cokernel label="prop:adjoint of Omegastar with the cokernel"} The Yoneda functor $\Omega^{*}\colon\mathop{\mathrm{\textup{QCoh}}}_{A}\stX\arr\L_{R}(\shC,A)$ has a left adjoint $\shF_{-,\shC}\colon\L_{R}(\shC,A)\arr\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ given by $$\shF_{\Gamma,\shC}\colon\stX^{\text{op}}\arr\sets\comma\stX\ni\xi\longmapsto\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}\E(\xi)\in\mathop{\mathrm{\textup{Mod}}}(\mathop{\mathrm{\textup{H}}}^{0}(\odi{\pi(\xi)})\otimes_{R}A)$$ where $\E(\xi)$ denotes the evaluation $\shC\arr\mathop{\mathrm{\textup{Mod}}}\mathop{\mathrm{\textup{H}}}^{0}(\odi{\pi(\xi)})$ of sheaves in $\xi\in\stX$. Alternatively $$\shF_{\Gamma,\shC}=\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}\E\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$$ where $\E$ denotes the inclusion $\shC\arr\mathop{\mathrm{\textup{QCoh}}}\stX$.
:::

::: proof
*Proof.* It is enough to apply [\[rem: coends\]](#rem: coends){reference-type="ref" reference="rem: coends"} with $\stY=\stX$ and $F\colon\shC\arr\mathop{\mathrm{\textup{QCoh}}}\stX$ the inclusion. Using the description of coend as cokernel one can check that the two functors defined in the statement are canonically isomorphic. ◻
:::

::: defn
[]{#def: unit and counit for adjunction label="def: unit and counit for adjunction"} We denote by $\gamma_{\Gamma}\colon\Gamma_{-}\arr\Omega_{-}^{\shF_{\Gamma,\shC}}=\mathop{\mathrm{\textup{Hom}}}_{\stX}(-,\shF_{\Gamma,\shC})$ and $\delta_{\shG}\colon\shF_{\Omega^{\shG},\shC}\arr\shG$ for $\Gamma\in\L_{R}(\shC,A)$ and $\shG\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ the unit and the counit of the adjunction between $\Omega^{*}\colon\mathop{\mathrm{\textup{QCoh}}}_{A}\stX\arr\L_{R}(\shC,A)$ and $\shF_{*,\shC}\colon\L_{R}(\shC,A)\arr\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ respectively.

Given $\xi\in\stX$, $\E\in\shC$, $\psi\in\E(\xi)$ and $x\in\Gamma_{\E}$ we denote by $x_{\E,\psi}\in\shF_{\Gamma,\shC}(\xi)$ the image of $x\otimes\psi$ under the map $\Gamma_{\E}\otimes_{R}\E(\xi)\arr\shF_{\Gamma,\shC}(\xi)$
:::

::: prop
[]{#prop:FGammaC on affine schemes label="prop:FGammaC on affine schemes"} Let $\Gamma\in\L_{R}(\shC,A)$. The unit $\gamma_{\Gamma}\colon\Gamma_{-}\arr\Omega_{-}^{\shF_{\Gamma,\shC}}=\mathop{\mathrm{\textup{Hom}}}_{\stX}(-,\shF_{\Gamma,\shC})$ is given by $$\begin{tikzpicture}[xscale=3.8,yscale=-0.6]     
\node (A0_0) at (0.2, 0) {$\Gamma_\E$};   
\node (A1_0) at (0.2, 1) {$x$}; 
\node (A0_1) at (1, 0) {$\mathop{\mathrm{\textup{Hom}}}_{\stX}(\E,\shF_{\Gamma,\shC})$};     
\node (A1_1) at (1, 1) {$(\phi \longmapsto x_{\E,\phi})$};     
\path (A0_0) edge [->]node [auto] {$\scriptstyle{}$} (A0_1);     
\path (A1_0) edge [|->,gray]node [auto] {$\scriptstyle{}$} (A1_1);        
\end{tikzpicture}$$ If $\shG\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ the counit $\delta_{\shG}\colon\shF_{\Omega^{\shG},\shC}\arr\shG$ is given by $$\shF_{\Omega^{\shG},\shC}(\xi)\ni x_{\E,\psi}\longmapsto x(\psi)\in\shG(\xi)\text{ for }\E\in\shC,x\in\Omega_{\E}^{\shG}=\mathop{\mathrm{\textup{Hom}}}_{\stX}(\E,\shG),\xi\in\stX,\psi\in\E(\xi)$$
:::

::: proof
*Proof.* If $p_{\E}\colon\Gamma_{\E}\otimes_{R}\E\arr\shF_{\Gamma,\shC}$ for $\E\in\shC$ are the maps associated with the coend defining $\shF_{\Gamma,\shC}$, then $p_{\E}(x\otimes\psi)=x_{\E,\psi}$ for $x\in\Gamma_{\E},\psi\in\E(\xi)$ and $\xi\in\stX$. All the claims follows by a direct check using the explicit description of the isomorphism $$\mathop{\mathrm{\textup{Hom}}}_{\mathop{\mathrm{\textup{QCoh}}}_{A}\stX}(\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}\E,\shH)\arrdi{\alpha}\mathop{\mathrm{\textup{Hom}}}_{\L_{R}(\shC,A)}(\Gamma,\Omega^{\shH})\text{ for }\shH\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$$ and its inverse given in [\[rem: coends\]](#rem: coends){reference-type="ref" reference="rem: coends"}. ◻
:::

Given a map $g\colon\stY\arr\stX$ of fibered categories we want to express $g^{*}\shF_{\Gamma,\shC}\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stY$ for $\Gamma\in\L_{R}(\shC,A)$ as $\shF_{g^{*}\Gamma,g^{*}\shC}$ for a suitable choice of $g^{*}\shC\subseteq\mathop{\mathrm{\textup{QCoh}}}\stY$ and $g^{*}\Gamma\in\L_{R}(g^{*}\shC,A)$.

::: defn
Let $\stY$ be a fibered category, $g\colon\stY\arr\stX$ be a morphism and $\shD$ be a subcategory of $\mathop{\mathrm{\textup{QCoh}}}\stX$. We set $g^{*}\shD$ for the subcategory of $\mathop{\mathrm{\textup{QCoh}}}\stY$ of sheaves $g^{*}\E$ for $\E\in\shD$. If $\shD'\subseteq\mathop{\mathrm{\textup{QCoh}}}\stY$ is a subcategory containing $g^{*}\shD$ we can define a restriction functor $$\begin{tikzpicture}[xscale=2.7,yscale=-0.6]     \node (A0_0) at (0, 0) {$\L_R(\shD',A)$};     \node (A0_1) at (1, 0) {$\L_R(\shD,A)$};     \node (A1_0) at (0, 1) {$\Gamma$};     \node (A1_1) at (1, 1) {$\Gamma\circ g^*$};     \path (A0_0) edge [->]node [auto] {$\scriptstyle{g_*}$} (A0_1);     \path (A1_0) edge [|->,gray]node [auto] {$\scriptstyle{}$} (A1_1);   \end{tikzpicture}$$
:::

::: prop
[]{#thm:adjoint of push forward label="thm:adjoint of push forward"} Let $\stY$ be a fibered category, $g\colon\stY\arr\stX$ be a morphism and $\shD$ be a subcategory of $\mathop{\mathrm{\textup{QCoh}}}\stY$ such that $g^{*}\shC\subseteq\shD$. Then $g_{*}\colon\L_{R}(\shD,A)\arr\L_{R}(\shC,A)$ has a left adjoint $g^{*}\colon\L_{R}(\shC,A)\arr\L_{R}(\shD,A)$ and it is given by $$(g^{*}\Gamma)_{\shG}=\int^{\E\in\shC}\Gamma_{\E}\otimes_{R}\mathop{\mathrm{\textup{Hom}}}_{\stY}(\shG,g^{*}\E)\in\mathop{\mathrm{\textup{Mod}}}A\text{ for }\Gamma\in\L_{R}(\shC,A)\comma\shG\in\shD$$ where $\mathop{\mathrm{\textup{Hom}}}_{\stY}(\shG,g^{*}-)$ is thought of as a functor $\shC\arr\mathop{\mathrm{\textup{Mod}}}R$. If $\stY=\stX$ and $g=\id_{\stX}$, so that $\shC\subseteq\shD$ and $(\id_{\stX})_{*}\colon\L_{R}(\shD,A)\arr\L_{R}(\shC,A)$ is the restriction, then the unit $\Gamma\arr(\id_{\stX}^{*}\Gamma)_{|\shC}$ is an isomorphism for $\Gamma\in\L_{R}(\shC,A)$.
:::

::: proof
*Proof.* Let $\Omega\in\L_{R}(\shD,A)$. $$Applying [\[rem: coends\]](#rem: coends){reference-type="ref" reference="rem: coends"} with $F=\mathop{\mathrm{\textup{Hom}}}_{\stY}(\shG,g^{*}-)$ we get a bijection between $\mathop{\mathrm{\textup{Hom}}}_{A}((g^{*}\Gamma)_{\shG},\Omega_{\shG})$ and the set of $A$-linear natural transformations $\Gamma_{\E}\arr\mathop{\mathrm{\textup{Hom}}}_{R}(\mathop{\mathrm{\textup{Hom}}}(\shG,g^{*}\E),\Omega_{\shG})$ for $\E\in\shC$. A natural transformation $g^{*}\Gamma\arr\Omega$ corresponds to a collection $\underline{\gamma}$ of $A$-linear maps $\gamma_{\shG,\E}\colon\Gamma_{\E}\arr\mathop{\mathrm{\textup{Hom}}}_{R}(\mathop{\mathrm{\textup{Hom}}}(\shG,g^{*}\E),\Omega_{\shG})$ natural in $\E\in\shC$ and such that $$\gamma_{\shG,\E}(x)(\phi\circ u)=\Omega_{u}(\gamma_{\overline{\shG},\E}(x)(\phi))\text{ for }x\in\Gamma_{\E},\overline{\shG}\arrdi{\phi}g^{*}\E,\shG\arrdi u\overline{\shG}\in\shD$$ Set $\mu_{\underline{\gamma}}(x)=\gamma_{g^{*}\E,\E}(x)(\id_{g^{*}\E})\in\Omega_{g^{*}\E}$ for $\E\in\shC,x\in\Gamma_{\E}$. If $\underline{\gamma}$ is a collection as above it follows that $\gamma_{\shG,\E}(x)(\psi)=\Omega_{\psi}(\mu_{\underline{\gamma}}(x))$ for $\E\in\shC$, $\shG\in\shD$, $x\in\Gamma_{\E}$ and $\shG\arrdi{\psi}g^{*}\E$ and that $\mu_{\underline{\gamma}}\colon\Gamma_{\E}\arr\Omega_{g^{*}\E}=(g_{*}\Omega)_{\E}$ is $A$-linear and natural in $\E$. Conversely, given a morphism $\mu\colon\Gamma\arr(g_{*}\Omega)$ in $\L_{R}(\shC,A)$ we can always define a collection $\underline{\gamma}$ as above by setting $\gamma_{\shG,\E}(x)(\psi)=\Omega_{\psi}(\mu(x))$. It is easy to check that $\underline{\gamma}$ induces a morphism $g^{*}\Gamma\arr\Omega$ and that the above constructions yields a bijection $\mathop{\mathrm{\textup{Hom}}}(g^{*}\Gamma,\Omega)\simeq\mathop{\mathrm{\textup{Hom}}}(\Gamma,g_{*}\Omega)$.

Assume now $\stY=\stX$ and $g=\id_{\stX}$ and let $\Gamma\in\L_{R}(\shC,A)$ and $\overline{\E}\in\shC$. Denote by $\alpha\colon\Gamma\arr(\id_{\stX}^{*}\Gamma)_{|\shC}$ the unit morphism. If $p_{\widetilde{\E}}\colon\Gamma_{\widetilde{\E}}\otimes\mathop{\mathrm{\textup{Hom}}}_{\stX}(\overline{\E},\widetilde{\E})\arr(\id_{\stX}^{*}\Gamma)_{\overline{\E}}$ are the structure morphisms as in [\[rem: coends\]](#rem: coends){reference-type="ref" reference="rem: coends"}, then $\alpha_{\overline{\E}}=p_{\overline{\E}}(-\otimes\id_{\overline{\E}})$. In particular, given $\shH\in\mathop{\mathrm{\textup{Mod}}}A$ and using [\[rem: coends\]](#rem: coends){reference-type="ref" reference="rem: coends"}, the map $\mathop{\mathrm{\textup{Hom}}}_{A}(\alpha_{\overline{\E}},\shH)\colon\mathop{\mathrm{\textup{Hom}}}_{A}((\id_{\stX}^{*}\Gamma)_{\overline{\E}},\shH)\arr\mathop{\mathrm{\textup{Hom}}}_{A}(\Gamma_{\overline{\E}},\shH)$ sends an $A$-linear natural transformation $\delta\colon\Gamma_{-}\arr\mathop{\mathrm{\textup{Hom}}}_{R}(\mathop{\mathrm{\textup{Hom}}}_{\stX}(\overline{\E},-),\shH)$ to $\Gamma_{\overline{\E}}\ni x\longmapsto\delta(x)(\id_{\overline{\E}})\in\shH$. Since $\delta$ corresponds to an $R$-linear natural transformation $\mathop{\mathrm{\textup{Hom}}}_{\stX}(\overline{\E},-)\arr\mathop{\mathrm{\textup{Hom}}}_{A}(\Gamma_{-},\shH)$, by Yoneda lemma we see that $\mathop{\mathrm{\textup{Hom}}}_{A}(\alpha_{\overline{\E}},\shH)$ is an isomorphism. ◻
:::

The above proposition yields a natural extension of any $\Gamma\in\L_{R}(\shC,A)$ to a functor $\Gamma^{ex}\in\L_{R}(\mathop{\mathrm{\textup{QCoh}}}\stX,A)$. By abuse of notation we will denote them by the same symbol $\Gamma$. This means that if $\Gamma\in L_{R}(\shC,A)$ and $\shG\in\mathop{\mathrm{\textup{QCoh}}}\stX$ then we can evaluate $\Gamma$ on $\shG$, writing $\Gamma_{\shG}$.

Given a map $g\colon\stY\arr\stX$ we will denote by $g^{*}\colon\L_{R}(\shC,A)\arr\L_{R}(g^{*}\shC,A)$ the left adjoint of the restriction $\L_{R}(g^{*}\shC,A)\arr\L_{R}(\shC,A)$. So, given $\Gamma\in\L_{R}(\shC,A)$, $g^{*}\Gamma$ is a functor $g^{*}\shC\arr\mathop{\mathrm{\textup{Mod}}}A$ but it also defines a functor $\mathop{\mathrm{\textup{QCoh}}}\stY\arr\mathop{\mathrm{\textup{Mod}}}A$ denoted, by our convention, by the same symbol. By [\[thm:adjoint of push forward\]](#thm:adjoint of push forward){reference-type="ref" reference="thm:adjoint of push forward"} the functor $g^{*}\Gamma\colon\mathop{\mathrm{\textup{QCoh}}}\stY\arr\mathop{\mathrm{\textup{Mod}}}A$ coincides with the value of the left adjoint of the restriction $\L_{R}(\mathop{\mathrm{\textup{QCoh}}}\stY,A)\arr\L_{R}(\shC,A)$.

::: rem
[]{#rem: extends to h0OX label="rem: extends to h0OX"}Given $\Gamma\in\L_{R}(\shC,A)$ and $\E\in\shC$ we have $R$-linear morphisms of rings $$\mathop{\mathrm{\textup{H}}}^{0}(\odi{\stX})\simeq\mathop{\mathrm{\textup{End}}}_{\stX}(\odi{\stX})\arr\mathop{\mathrm{\textup{End}}}_{\stX}(\E)\arr\mathop{\mathrm{\textup{End}}}_{A}(\Gamma_{\E})$$ This defines a lifting of $\Gamma$ to an $R$-linear functor $\Gamma\colon\shC\arr\mathop{\mathrm{\textup{Mod}}}(\mathop{\mathrm{\textup{H}}}^{0}(\odi{\stX})\otimes_{R}A)$ and an equivalence $$\L_{R}(\shC,A)\arr\L_{R}(\shC,\mathop{\mathrm{\textup{H}}}^{0}(\odi{\stX})\otimes_{R}A)$$ In particular, if $g\colon\mathop{\mathrm{\textup{Spec}}}B\arr\stX$ is a map and $\Gamma\in\L_{R}(\shC,A)$ then $(g^{*}\Gamma)_{B}$ has a $B\otimes_{R}A$-module structure. By [\[prop:adjoint of Omegastar with the cokernel\]](#prop:adjoint of Omegastar with the cokernel){reference-type="ref" reference="prop:adjoint of Omegastar with the cokernel"} and [\[thm:adjoint of push forward\]](#thm:adjoint of push forward){reference-type="ref" reference="thm:adjoint of push forward"} there is a canonical $A$-linear isomorphism $$\shF_{\Gamma,\shC}(B)\simeq(g^{*}\Gamma)_{B}$$ and it is easy to see that it is also $B$-linear.
:::

::: prop
Let $g\colon\stY\arr\stX$ be a morphism of fibered categories. Then there exists an isomorphism $g^{*}\shF_{\Gamma,\shC}\simeq\shF_{g^{*}\Gamma,g^{*}\shC}$ natural in $\Gamma\in\L_{R}(\shC,A)$, that is a $2$-commutative diagram $$\begin{tikzpicture}[xscale=3.1,yscale=-1.2]     \node (A0_0) at (0, 0) {$\L_R(\shC,A)$};     \node (A0_1) at (1, 0) {$\mathop{\mathrm{\textup{QCoh}}}_A \stX$};     \node (A1_0) at (0, 1) {$\L_R(g^*\shC,A)$};     \node (A1_1) at (1, 1) {$\mathop{\mathrm{\textup{QCoh}}}_A \stY$};     \path (A0_0) edge [->]node [auto] {$\scriptstyle{\shF_{-,\shC}}$} (A0_1);     \path (A0_0) edge [->]node [auto] {$\scriptstyle{g^*}$} (A1_0);     \path (A0_1) edge [->]node [auto] {$\scriptstyle{g^*}$} (A1_1);     \path (A1_0) edge [->]node [auto] {$\scriptstyle{\shF_{-,g^*\shC}}$} (A1_1);   \end{tikzpicture}$$
:::

::: proof
*Proof.* Let $\Gamma\in\L_{R}(\shC,A)$. Let also $\mathop{\mathrm{\textup{Spec}}}B\arrdi{\xi}\stY$ be a map and $N\in\mathop{\mathrm{\textup{Mod}}}B\otimes_{R}A$. Denote by $F\colon\shC\arr\mathop{\mathrm{\textup{Mod}}}B$ and $G\colon g^{*}\shC\arr\mathop{\mathrm{\textup{Mod}}}B$ the functors obtained by taking sections over $B$. In particular $F=G\circ g^{*}$. We have isomorphisms $$\begin{alignat*}
{1}
\mathop{\mathrm{\textup{Hom}}}_{B\otimes_{R}A}(\shF_{g^{*}\Gamma,g^{*}\shC}(B),N) & \simeq\mathop{\mathrm{\textup{Hom}}}_{\L_{R}(g^{*}\shC,A)}(g^{*}\Gamma,\mathop{\mathrm{\textup{Hom}}}_{B}(G,N))\simeq\mathop{\mathrm{\textup{Hom}}}_{\L_{R}(\shC,A)}(\Gamma,g_{*}\mathop{\mathrm{\textup{Hom}}}_{B}(G,N))\\
 & =\mathop{\mathrm{\textup{Hom}}}_{\L_{R}(\shC,A)}(\Gamma,\mathop{\mathrm{\textup{Hom}}}_{B}(F,N))\simeq\mathop{\mathrm{\textup{Hom}}}_{B\otimes_{R}A}((g^{*}\shF_{\Gamma,\shC})(B),N)
\end{alignat*}$$ In particular we get an isomorphism $(g^{*}\shF_{\Gamma,\shC})(B)\simeq\shF_{g^{*}\Gamma,g^{*}\shC}(B)$. By a direct check it follows that this isomorphism is natural in $\Gamma$ and it also extends as an isomorphism of functors $g^{*}\shF_{\Gamma,\shC}\simeq\shF_{g^{*}\Gamma,g^{*}\shC}$. ◻
:::

Notice that, as soon as $g^{*}\colon\mathop{\mathrm{\textup{QCoh}}}\stX\arr\mathop{\mathrm{\textup{QCoh}}}\stY$ has a right adjoint $g_{*}\colon\mathop{\mathrm{\textup{QCoh}}}\stY\arr\mathop{\mathrm{\textup{QCoh}}}\stX$ (see [\[prop:properties of push-forward\]](#prop:properties of push-forward){reference-type="ref" reference="prop:properties of push-forward"}), then $g_{*}\Omega^{\shG}\simeq\Omega^{g_{*}\shG}$ for $\shG\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stY$ and the above proposition follows taking the left adjoints.

::: rem
[]{#rem: LR and QCoh as stacks label="rem: LR and QCoh as stacks"} If $A\arr A'$ is a morphism of $R$-algebras then we have pull-back functors $\L_{R}(\shC,A)\arr\L_{R}(\shC,A')$ and $\mathop{\mathrm{\textup{QCoh}}}_{A}\stX\arr\mathop{\mathrm{\textup{QCoh}}}_{A'}\stX$. The first one is obtained considering the tensor product $-\otimes_{A}A'$, while the second one corresponds to the pullback $\mathop{\mathrm{\textup{QCoh}}}\stX_{A}\arr\mathop{\mathrm{\textup{QCoh}}}\stX_{A'}$ along the projection $\stX_{A'}\arr\stX_{A}$. Alternatively, those functors are left adjoints to the restriction of scalars $\L_{R}(\shC,A')\arr\L_{R}(\shC,A)$ and $\mathop{\mathrm{\textup{QCoh}}}_{A'}\stX\arr\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ respectively. It is easy to see that in this way we obtain two fpqc stacks (not in groupoids) $\L_{R}(\shC,-)$ and $\mathop{\mathrm{\textup{QCoh}}}_{-}\stX$ over the category of affine $R$-schemes. Notice that the functor $\Omega^{*}\colon\mathop{\mathrm{\textup{QCoh}}}_{-}\stX\arr\L_{R}(\shC,-)$ is not a morphism of stacks because $\mathop{\mathrm{\textup{Hom}}}_{\stX}(\E,\shG)\otimes_{A}A'\not\simeq\mathop{\mathrm{\textup{Hom}}}_{\stX}(\E,\shG\otimes_{A}A')$ in general for $\E\in\shC$ and $\shG\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$.
:::

::: prop
[]{#prop:base change for FstarC label="prop:base change for FstarC"} The functor $\shF_{*,\shC}\colon\L_{R}(\shC,-)\arr\mathop{\mathrm{\textup{QCoh}}}_{-}\stX$ is a morphism of stacks.
:::

::: proof
*Proof.* Given a morphism $A\arr A'$ of $R$-algebras we have a $2$-commutative diagram $$\begin{tikzpicture}[xscale=2.9,yscale=-1.0]     \node (A0_0) at (0, 0) {$\mathop{\mathrm{\textup{QCoh}}}_{A'}\stX$};     \node (A0_1) at (1, 0) {$\L_R(\shC,A')$};     \node (A1_0) at (0, 1) {$\mathop{\mathrm{\textup{QCoh}}}_A \stX$};     \node (A1_1) at (1, 1) {$\L_R(\shC,A)$};     \path (A0_0) edge [->]node [auto] {$\scriptstyle{\Omega^*}$} (A0_1);     \path (A0_0) edge [->]node [auto] {$\scriptstyle{}$} (A1_0);     \path (A0_1) edge [->]node [auto] {$\scriptstyle{}$} (A1_1);     \path (A1_0) edge [->]node [auto] {$\scriptstyle{\Omega^*}$} (A1_1);   \end{tikzpicture}$$ where the vertical arrows are obtained by restricting the scalars from $A'$ to $A$. Using [\[rem: LR and QCoh as stacks\]](#rem: LR and QCoh as stacks){reference-type="ref" reference="rem: LR and QCoh as stacks"} and taking the left adjoint functors of the functors in the diagram we exactly get the $2$-commutative diagram expressing the fact that $\shF_{*,\shC}$ preserves Cartesian arrows. ◻
:::

We conclude this section by showing that, when considering sheafification functors $\shF_{-,\shC}$, we can always reduce problems to the case when $\shC$ is an additive category. Moreover in this case the sections of $\shF_{-,\shC}$ have a nice expression in terms of a direct limit.

::: defn
Given a subcategory $\shD$ of $\mathop{\mathrm{\textup{QCoh}}}\stX$ we denote by $\shD^{\oplus}$ the subcategory of $\mathop{\mathrm{\textup{QCoh}}}\stX$ whose objects are all finite direct sums of sheaves in $\shD$.
:::

Notice that if $\shD$ is small then $\shD^{\oplus}$ is small.

::: prop
[]{#prop:find a directed category label="prop:find a directed category"} The restriction $\L_{R}(\shC^{\oplus},A)\arr\L_{R}(\shC,A)$ and its left adjoint are inverses of each other. In particular if $\Gamma\in\L_{R}(\shC^{\oplus},A)$ then we have a canonical isomorphism $\shF_{\Gamma,\shC^{\oplus}}\simeq\shF_{\Gamma_{|\shC},\shC}$.
:::

::: proof
*Proof.* Denote the restriction by $\alpha$ and its left adjoint by $\beta$. From [\[thm:adjoint of push forward\]](#thm:adjoint of push forward){reference-type="ref" reference="thm:adjoint of push forward"} we know that $\alpha\beta(\Gamma)\simeq\Gamma$ for $\Gamma\in\L_{R}(\shC,A)$. Conversely, if $\Gamma\in\L_{R}(\shC^{\oplus},A)$, we have a canonical morphism $\gamma\colon\beta\alpha(\Gamma)\arr\Gamma$. If $\E\in\shC$ the map $\gamma_{\E}$ is easily seen to be an isomorphism and by additivity this also follows for $\gamma$. For the last claim it is enough to note that the composition $\mathop{\mathrm{\textup{QCoh}}}_{A}\stX\arrdi{\Omega^{*}}\L_{R}(\shC^{\oplus},A)\arr\L_{R}(\shC,A)$ is exactly $\Omega^{*}\colon\mathop{\mathrm{\textup{QCoh}}}_{A}\stX\arr\L_{R}(\shC,A)$. ◻
:::

::: rem
[]{#rem: natural transf are linear for additive categories label="rem: natural transf are linear for additive categories"} If $\catC$ is an $R$-linear and additive category and $F,G\colon\catC\arr\mathop{\mathrm{\textup{Mod}}}A$ are $R$-linear (covariant or contravariant) functors then any natural transformation $\lambda\colon F\arr G$ of functors of sets is $R$-linear. Indeed by considering $\catC^{\mathop{\mathrm{\textup{op}}}}$ we can consider only covariant functors. In this case it is easy to show that the maps $\lambda_{X}\colon F(X)\arr G(X)$ for $X\in\catC$ are $R$-linear using functoriality on the map $r\id_{X}\colon X\arr X$ for $r\in R$ and $\mathop{\mathrm{\textup{pr}}}_{1},\mathop{\mathrm{\textup{pr}}}_{2},\mathop{\mathrm{\textup{pr}}}_{1}+\mathop{\mathrm{\textup{pr}}}_{2}\colon X\oplus X\arr X$, where $\mathop{\mathrm{\textup{pr}}}_{*}$ are the projections.
:::

::: defn
Let $\mathop{\mathrm{\textup{Spec}}}B\arr\stX$ be a map. We denote by $J_{B,\shC}$ the category of pairs $(\E,\psi)$ where $\E\in\shC^{\oplus}$ and $\psi\in\E(B)$. Given $\Gamma\in\L_{R}(\shC,A)$ we have a functor $\Gamma\colon J_{B,\shC}\arr\mathop{\mathrm{\textup{Mod}}}A$ given by $\Gamma_{\E,\psi}=\Gamma_{\E}$.
:::

::: prop
[]{#prop:FGammaCB as a direct limit label="prop:FGammaCB as a direct limit"} Let $\mathop{\mathrm{\textup{Spec}}}B\arr\stX$ be a map and $\Gamma\in\L_{R}(\shC,A)$. The category $J_{B,\shC}$ is non-empty and for all $\xi,\xi'\in J_{B,\shC}$ there exists $\xi''\in J_{B,\shC}$ and maps $\xi''\arr\xi$, $\xi''\arr\xi'$. The $A$-linear maps $\Gamma_{\E,\psi}=\Gamma_{\E}\arr\shF_{\Gamma,\shC^{\oplus}}(B)\simeq\shF_{\Gamma,\shC}(B)$, $x\longmapsto x_{\E,\psi}$ for $(\E,\psi)\in J_{B,\shC}$ (see [\[def: unit and counit for adjunction\]](#def: unit and counit for adjunction){reference-type="ref" reference="def: unit and counit for adjunction"}) induce an $A$-linear isomorphism $$\varinjlim_{(\E,\psi)\in J_{B,\shC}^{\mathop{\mathrm{\textup{op}}}}}\Gamma_{\E,\psi}\arr\shF_{\Gamma,\shC}(B)$$ In particular all elements of $\shF_{\Gamma,\shC}(B)$ are of the form $x_{\E,\psi}$ for some $\E\in\shC^{\oplus}$, $x\in\Gamma_{\E}$ and $\psi\in\E(B)$. The multiplication by $b\in B$ on the first limit is induced by mapping $\Gamma_{\E,\psi}$ to $\Gamma_{\E,b\psi}$ using $\id_{\Gamma_{\E}}$ for $(\E,\psi)\in J_{B,\shC}$.
:::

::: proof
*Proof.* By [\[prop:find a directed category\]](#prop:find a directed category){reference-type="ref" reference="prop:find a directed category"} we can assume $\shC=\shC^{\oplus}$. Denote by $\shH$ and $\alpha\colon\shH\arr\shF_{\Gamma,\shC}(B)$ the limit and the map in the statement respectively. The category $J_{B,\shC}$ is not empty because $(\E,0)\in J_{B,\shC}$ for all $\E\in\shC$ and the map $\alpha$ is well defined because, for all $x\in\Gamma_{\overline{\E}}$ and for all $(\E,\psi)\arrdi u(\overline{\E},u(\psi))$ we have $x_{\overline{\E},u(\psi)}=(\Gamma_{u}(x))_{\E,\psi}$, by definition of $\shF_{\Gamma,\shC}(B)$ as coend. Moreover if $(\E_{1},\psi_{1}),(\E_{2},\psi_{2})\in J_{B,\shC}$ then we have maps $\mathop{\mathrm{\textup{pr}}}_{i}\colon(\E_{1}\oplus\E_{2},\psi_{1}\oplus\psi_{2})\arr(\E_{i},\psi_{i})$ for $i=1,2$, where $\mathop{\mathrm{\textup{pr}}}_{i}$ is the projection. In particular any element of $\shH$ comes from a map $\Gamma_{\E,\psi}\arr\shH$, where $(\E,\psi)\in J_{B,\shC}$. Thus all elements of $\shF_{\Gamma,\shC}(B)$ are of the form $x_{\E,\psi}$ for some $\E\in\shC^{\oplus}$, $x\in\Gamma_{\E}$ and $\psi\in\E(B)$ provided that we prove that $\alpha$ is an isomorphism.

Given an $A$-module $N$ then $\mathop{\mathrm{\textup{Hom}}}_{A}(\shH,N)$ is $A$-linearly isomorphic to the set of natural transformations of sets $\beta_{\E}\colon\E(B)\arr\mathop{\mathrm{\textup{Hom}}}_{A}(\Gamma_{\E},N)$. Since $\shC$ is additive, by [\[rem: natural transf are linear for additive categories\]](#rem: natural transf are linear for additive categories){reference-type="ref" reference="rem: natural transf are linear for additive categories"}, those transformations are automatically $R$-linear. Given $b\in B$ there is an $A$-linear map $\phi_{b}\in\mathop{\mathrm{\textup{End}}}_{A}(\shH)$ as described in the last sentence in the statement. A direct check shows that, given an $A$-module $N$, the map $\mathop{\mathrm{\textup{Hom}}}_{A}(\phi_{b},N)\colon\mathop{\mathrm{\textup{Hom}}}_{A}(\shH,N)\arr\mathop{\mathrm{\textup{Hom}}}_{A}(\shH,N)$ sends an $R$-linear natural transformation $\beta_{\E}\colon\E(B)\arr\mathop{\mathrm{\textup{Hom}}}_{A}(\Gamma_{\E},N)$ to $\beta_{\E}\circ b\id_{\E}$. This easily implies that $\phi\colon B\arr\mathop{\mathrm{\textup{End}}}_{A}(\shH)$ makes $\shH$ into a $B\otimes_{R}A$-module and that $\alpha\colon\shH\arr\shF_{\Gamma,\shC}(B)$ is also $B$-linear. Since $B\otimes_{R}A$-linear maps $\shH\arr N$, for $N\in\mathop{\mathrm{\textup{Mod}}}B\otimes_{R}A$, corresponds to $B$-linear natural transformations $\E(B)\arr\mathop{\mathrm{\textup{Hom}}}_{A}(\Gamma_{\E},N)$ and thus to $A$-linear natural transformations $\Gamma_{\E}\arr\mathop{\mathrm{\textup{Hom}}}_{B}(\E(B),N)$ as described above, one can check directly (using [\[rem: coends\]](#rem: coends){reference-type="ref" reference="rem: coends"}) that $\mathop{\mathrm{\textup{Hom}}}_{B\otimes_{R}A}(\alpha,N)$ induces the identity on $\mathop{\mathrm{\textup{Hom}}}_{\L_{R}(\shC,A)}(\Gamma_{-},\mathop{\mathrm{\textup{Hom}}}_{B}(-(B),N))$. This implies that $\alpha\colon\shH\arr\shF_{\Gamma,\shC}(B)$ is an isomorphism. ◻
:::

## Sheafifying $R$-linear monoidal functors.

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

- $\mathop{\mathrm{\textup{Rings}}}_{A}\stX$, whose objects are $\alB\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ with an $A$-linear map $m\colon\alB\otimes_{\odi{\stX_{A}}}\alB\arr\alB$, called the multiplication;

- $\mathop{\mathrm{\textup{QAlg}}}_{A}\stX$, as the (not full) subcategory of $\mathop{\mathrm{\textup{Rings}}}_{A}\stX$ whose objects are $\alB$ with a commutative, associative multiplication with a unity and the arrows are morphisms preserving unities;

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
