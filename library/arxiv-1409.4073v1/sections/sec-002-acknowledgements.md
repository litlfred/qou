---
doc_id: arxiv-1409.4073v1
doc_title: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI"
section_id: sec-002-acknowledgements
section_title: "Acknowledgements"
section_number: null
pages: 5-9
source_pdf: 1409.4073v1.pdf
source_sha256: b40be7f0022f70a1
doc_brief: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI — W e introduce “sheaﬁﬁcation” functors from categories of (l ax monoidal) linear functors to categories of quasi-coherent sheaves"
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.972
---
I would like to thank Jarod Alper, David Rydh, Daniel Sch�ppi, Mattia Talpo and Angelo Vistoli for the useful conversations I had with them and all the suggestions they gave me.

# []{#sec: Preliminaries on sheaves label="sec: Preliminaries on sheaves"} Preliminaries on sheaves and fibered categories

Let $\pi\colon\stX\arr\mathop{\mathrm{\textup{Aff}}}/R$ be a fibered category. There is a functor of rings $\odi{\stX}\colon\stX^{\mathop{\mathrm{\textup{op}}}}\arr\sets$ defined by $\odi{\stX}(\xi)=\mathop{\mathrm{\textup{H}}}^{0}(\odi{\pi(\xi)})$, so that $(\stX,\odi{\stX})$ is a ringed category. A presheaf of $\odi{\stX}$-modules on $\stX$ is a functor $\shF\colon\stX^{\text{op}}\arr\sets$ together with an $\mathop{\mathrm{\textup{H}}}^{0}(\odi{\pi(\xi)})$-module structure on $\shF(\xi)$ for all $\xi\in\stX$ such that, if $\xi\arr\eta$ is a map on $\stX$, then the map $\shF(\eta)\arr\shF(\xi)$ is $\mathop{\mathrm{\textup{H}}}^{0}(\odi{\pi(\eta)})$-linear. Morphism of presheaves of $\odi{\stX}$-modules are natural transformations respecting the module structures. We denote by $\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$ the category of presheaves of $\odi{\stX}$-modules.

::: defn
A quasi-coherent sheaf over $\stX$ is a presheaf of $\odi{\stX}$-modules such that for all maps $\xi\arr\eta$ in $\stX$ the induced map $$\shF(\eta)\otimes_{\mathop{\mathrm{\textup{H}}}^{0}(\odi{\pi(\eta)})}\mathop{\mathrm{\textup{H}}}^{0}(\odi{\pi(\xi)})\arr\shF(\xi)$$ is an isomorphism. We denote by $\mathop{\mathrm{\textup{QCoh}}}\stX$ the full subcategory of $\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$ of quasi-coherent sheaves.
:::

Notice that by fpqc descent of modules a quasi-coherent sheaf is a sheaf for the fpqc topology of $\stX$.

If $f\colon\stY\arr\stX$ is a morphism of fibered categories and $\shF\in\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$ we define $f^{*}\shF=\shF\circ f\colon\stY^{\mathop{\mathrm{\textup{op}}}}\arrdi f\stX^{\mathop{\mathrm{\textup{op}}}}\arrdi{\shF}\sets$. This association defines a functor $f^{*}\colon\mathop{\mathrm{\textup{Mod}}}\odi{\stX}\arr\mathop{\mathrm{\textup{Mod}}}\odi{\stY}$, called the pull-back functor, and restricts to a functor $f^{*}\colon\mathop{\mathrm{\textup{QCoh}}}\stX\arr\mathop{\mathrm{\textup{QCoh}}}\stY$. Notice that $f^{*}\odi{\stX}=\odi{\stY}$ tautologically.

The category $\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$ is an abelian category and cokernels of maps between quasi-coherent sheaves are again quasi-coherent and thus cokernels in $\mathop{\mathrm{\textup{QCoh}}}\stX$. Notice that, since we have restricted our fiber categories to affine schemes, a map $f\colon\shF\arr\shG$ of quasi-coherent sheaves is an epimorphism if and only if it is pointwise surjective, that is surjective in $\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$. The category $\mathop{\mathrm{\textup{QCoh}}}\stX$ is $R$-linear but it is unclear if it is abelian. Moreover kernels in $\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$ of maps between quasi-coherent sheaves are almost never quasi-coherent, essentially because pull-backs are not left exact. There is a natural condition on $\stX$ which allows us to prove that $\mathop{\mathrm{\textup{QCoh}}}\stX$ is an $R$-linear abelian category.

::: defn
An *fpqc atlas* (or simply *atlas*) of a fibered category $\stX$ is a representable fpqc covering $X\arr\stX$ from a scheme. A fiber category is called *pseudo-algebraic* if it has an atlas, it is called *quasi-compact* if it has an atlas from an affine scheme.

Let$f\colon\stY\arr\stX$ be a morphism of fibered categories. The map $f$ is called *pseudo-algebraic* (resp. *quasi-compact*) if for all maps $T\arr\stX$ from a scheme (resp. quasi-compact scheme) the fiber product $T\times_{\stX}\stY$ is pseudo-algebraic (resp. quasi-compact). It is called *quasi-separated* if the diagonal $\stY\arr\stY\times_{\stX}\stY$ is quasi-compact.
:::

If $\stX$ is pseudo-algebraic then the diagonal $\Delta_{\stX}\colon\stX\arr\stX\times_{R}\stX$ is not necessarily representable. It is unclear whether this is true or not if $\stX$ is a fpqc stack, because it is not known if algebraic spaces satisfy effective descent along fpqc coverings.

Let $f\colon\stY\arr\stX$ be a map of fibered categories. If $\stX$ and $f$ are pseudo-algebraic then $\stY$ is pseudo-algebraic. If $\stY$ is pseudo-algebraic and $\Delta_{\stX}$ is representable then $f$ is pseudo-algebraic.

If $\catC$ is a (not full) subcategory of $\stX$ one can analogously define presheaves of $(\odi{\stX})_{|\catC}$-modules and quasi-coherent sheaves on $\catC$ just replacing all occurrences of $\stX$ with $\catC$. We denote by $\mathop{\mathrm{\textup{Mod}}}(\odi{\stX})_{|\catC}$ and $\mathop{\mathrm{\textup{QCoh}}}\catC$ the resulting categories.

::: defn
We define $\stX_{\text{fl}}$ (resp. $\stX_{\text{sm}}$, $\stX_{\text{et}}$) as the (not full) subcategory of $\stX$ of objects $\xi\colon\mathop{\mathrm{\textup{Spec}}}B\arr\stX$ which are representable and flat (resp. smooth, �tale) and the arrows are morphisms in $\stX$ whose underlying map of affine schemes is flat (resp. smooth, �tale).
:::

If $X\arr\stX$ is an fpqc atlas then by definition $R=X\times_{\stX}X$ is an algebraic space and the two projections $\shR\rightrightarrows X$ extends to a groupoid in algebraic spaces. We denote by $\mathop{\mathrm{\textup{QCoh}}}(R\rightrightarrows X)$ the category of quasi-coherent sheaves on $R\rightrightarrows X$ (see [@SP014 Tag 0440]). By standard arguments of fpqc descent for modules we have:

::: prop
[]{#prop:reducing to atlases for quasi-geometric categories label="prop:reducing to atlases for quasi-geometric categories"} If $\stX$ admits an fpqc (resp. smooth, �tale) atlas then the restriction $\mathop{\mathrm{\textup{QCoh}}}\stX\arr\mathop{\mathrm{\textup{QCoh}}}\stX_{\text{fl}}$ (resp. $\mathop{\mathrm{\textup{QCoh}}}\stX_{\text{sm}}$, $\mathop{\mathrm{\textup{QCoh}}}\stX_{\text{et}}$) is an equivalence of categories. If $f\colon X\arr\stX$ is an fpqc atlas then $f^{*}\colon\mathop{\mathrm{\textup{QCoh}}}\stX\arr\mathop{\mathrm{\textup{QCoh}}}X$ is faithful and it induces an equivalence $\mathop{\mathrm{\textup{QCoh}}}\stX\arr\mathop{\mathrm{\textup{QCoh}}}(R\rightrightarrows X)$.
:::

We see that if $\stX$ is pseudo-algebraic then $\mathop{\mathrm{\textup{QCoh}}}\stX$ is equivalent to an $R$-linear abelian category, namely $\mathop{\mathrm{\textup{QCoh}}}(R\rightrightarrows X)$. Moreover if $\alpha\colon\shF\arr\shG$ is a map of quasi-coherent sheaves then $\mathop{\mathrm{\textup{Ker}}}(\alpha)$ is defined by taking $\mathop{\mathrm{\textup{Ker}}}(\alpha_{|\stX_{\text{fl}}})\in\mathop{\mathrm{\textup{QCoh}}}\stX_{\text{fl}}$, which is just given by $\mathop{\mathrm{\textup{Ker}}}(\alpha_{|\stX_{\text{fl}}})(\mathop{\mathrm{\textup{Spec}}}B\arrdi{\xi}\stX)=\mathop{\mathrm{\textup{Ker}}}(\alpha(\xi)\colon\shF(\xi)\arr\shG(\xi))$ for $\xi\in\stX_{\text{fl}}$, and then extending it to the whole $\stX$. If $\stX$ is an algebraic stack or a scheme we see that $\mathop{\mathrm{\textup{QCoh}}}\stX$ is equivalent to the usual category of quasi-coherent sheaves via an $R$-linear and exact functor. If it is given a subcategory $\shD$ of $\mathop{\mathrm{\textup{QCoh}}}\stX$, an exact sequence of sheaves in $\shD$ will always be an exact sequence in $\mathop{\mathrm{\textup{QCoh}}}\stX$ of sheaves belonging to $\shD$.

We now deal with the problem of defining a right adjoint of a pull-back functor. Given $\shF\in\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$ we define the global section $\shF(\stX)=\mathop{\mathrm{\textup{Hom}}}(\odi{\stX},\shF)$ of $\shF$, also denoted by $\mathop{\mathrm{\textup{H}}}^{0}(\stX,\shF)$ or simply $\mathop{\mathrm{\textup{H}}}^{0}(\shF)$, which is an $\odi{\stX}(\stX)$-module. More generally given a map of fibered categories $g\colon\stZ\arr\stX$ we define $\shF(\stZ)=(g^{*}\shF)(\stZ)$. If $\stZ=\mathop{\mathrm{\textup{Spec}}}B$ is affine we will often write $\shF(B)$ instead of $\shF(\mathop{\mathrm{\textup{Spec}}}B)$.

Let $f\colon\stY\arr\stX$ be a map of fibered categories. Given $\shG\in\mathop{\mathrm{\textup{Mod}}}\odi{\stY}$ and an object $\xi\colon T\arr\stX$ of $\stX$ we define $$(f_{p}\shG)(\xi)=\shG(T\times_{\stX}\stY)$$ Given another object $\xi'\colon T'\arr\stX$ and a morphism $\beta\colon\xi'\arr\xi$ in $\stX$ there is an induced morphism $(f_{p}\shG)(\xi)\arr(f_{p}\shG)(\xi')$. This data define a functor $f_{p}\colon\mathop{\mathrm{\textup{Mod}}}\odi{\stY}\arr\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$ and we have:

::: prop
Let $f\colon\stY\arr\stX$ be a map of fibered categories. Then $f_{p}$ is a right adjoint of $f^{*}$ and, if $$\begin{tikzpicture}[xscale=1.5,yscale=-1.2]     \node (A0_0) at (0, 0) {$\stY'$};     \node (A0_1) at (1, 0) {$\stY$};     \node (A1_0) at (0, 1) {$\stX'$};     \node (A1_1) at (1, 1) {$\stX$};     \path (A0_0) edge [->]node [auto] {$\scriptstyle{g'}$} (A0_1);     \path (A1_0) edge [->]node [auto] {$\scriptstyle{g}$} (A1_1);     \path (A0_1) edge [->]node [auto] {$\scriptstyle{f}$} (A1_1);     \path (A0_0) edge [->]node [auto] {$\scriptstyle{f'}$} (A1_0);   \end{tikzpicture}$$ is a $2$-cartesian diagram of fibered categories, there is an isomorphism of functors $$g^{*}f_{p}\arr f'_{p}g'^{*}\colon\mathop{\mathrm{\textup{Mod}}}\odi{\stY}\arr\mathop{\mathrm{\textup{Mod}}}\odi{\stX'}$$ If $f$ is affine then $f_{p}(\mathop{\mathrm{\textup{QCoh}}}\stY)\subseteq\mathop{\mathrm{\textup{QCoh}}}\stX$ and $(f_{p})_{|\mathop{\mathrm{\textup{QCoh}}}\stY}\colon\mathop{\mathrm{\textup{QCoh}}}\stY\arr\mathop{\mathrm{\textup{QCoh}}}\stX$ is right adjoint to $f^{*}\colon\mathop{\mathrm{\textup{QCoh}}}\stX\arr\mathop{\mathrm{\textup{QCoh}}}\stY$.
:::

::: proof
*Proof.* The adjunction between $f^{*}$ and $f_{p}$ can be found in [@SP014 Tag 00XF]. With notation from this reference, we have that $_{\eta}^{f}\shI\simeq T\times_{\stX}\stY$ for an object $\eta\colon T\arr\stX$. Moreover if $\shF\in\mathop{\mathrm{\textup{Mod}}}\odi{\stY}$ then $\shF(T\times_{\stX}\stY)$ is the limit of $\shF_{|T\times_{\stX}\stY}$ over the whole $T\times_{\stX}\stY$. Thus what is denoted by $_{p}f$ is easily seen to be equivalent to our $f_{p}$ if we take limits of $R$-modules and not of sets. The isomorphism for the base change is tautological. For the last claim we can assume that $\stX$ is an affine scheme in which case the result follows because (usual) push-forwards commutes with arbitrary base changes. ◻
:::

In general $f_{p}$ does not preserve quasi-coherent sheaves, even if $f$ is a proper map of schemes. To get a right adjoint of pullback we have to require more.

::: defn
A pseudo-algebraic map $f\colon\stY\arr\stX$ of fibered categories is called *flat* if given an object $\xi\colon T\arr\stX$ of $\stX$ and an atlas $V\arr T\times_{\stX}\stY$ the resulting map $V\arr T$ is flat.
:::

::: prop
[]{#prop:properties of push-forward label="prop:properties of push-forward"} Let $f\colon\stY\arr\stX$ be a quasi-compact and quasi-separated map of pseudo-algebraic fibered categories. Then the composition $\mathop{\mathrm{\textup{QCoh}}}\stY\arrdi{f_{p}}\mathop{\mathrm{\textup{Mod}}}\odi{\stX}\arr\mathop{\mathrm{\textup{Mod}}}(\odi{\stX})_{|\stX_{\text{fl}}}$ has values in $\mathop{\mathrm{\textup{QCoh}}}\stX_{\text{fl}}$. The induced map $f_{*}\colon\mathop{\mathrm{\textup{QCoh}}}\stY\arr\mathop{\mathrm{\textup{QCoh}}}\stX$ is a right adjoint of $f^{*}\colon\mathop{\mathrm{\textup{QCoh}}}\stX\arr\mathop{\mathrm{\textup{QCoh}}}\stY$. If $$\begin{tikzpicture}[xscale=1.5,yscale=-1.2]     \node (A0_0) at (0, 0) {$\stY'$};     \node (A0_1) at (1, 0) {$\stY$};     \node (A1_0) at (0, 1) {$\stX'$};     \node (A1_1) at (1, 1) {$\stX$};     \path (A0_0) edge [->]node [auto] {$\scriptstyle{g'}$} (A0_1);     \path (A1_0) edge [->]node [auto] {$\scriptstyle{g}$} (A1_1);     \path (A0_1) edge [->]node [auto] {$\scriptstyle{f}$} (A1_1);     \path (A0_0) edge [->]node [auto] {$\scriptstyle{f'}$} (A1_0);   \end{tikzpicture}$$ is a $2$-cartesian diagram of fibered categories with $\stX'$ pseudo-algebraic then $\stY'$ is pseudo-algebraic, $f'$ is quasi-compact and quasi-separated and there is a natural transformation of functors $$g^{*}f_{*}\arr f'_{*}g'^{*}\colon\mathop{\mathrm{\textup{QCoh}}}\stX\arr\mathop{\mathrm{\textup{QCoh}}}\stY'$$ which is an isomorphism if $g$ is flat.
:::

::: proof
*Proof.* Consider the $2$-Cartesian diagram in the statement. The diagonal of $f'$ is quasi-compact because it is base change of the diagonal of $f$. To see that $f_{p}(\shF)_{|\stX_{\text{fl}}}$ is quasi-coherent for $\shF\in\mathop{\mathrm{\textup{QCoh}}}\stY$, we can assume $\stX=\mathop{\mathrm{\textup{Spec}}}B$ affine and that $\stY$ is quasi-compact with quasi-compact diagonal. If $U=\mathop{\mathrm{\textup{Spec}}}A\arr\stY$ is a fpqc atlas, it follows that $R=U\times_{\stY}U$ is a quasi-compact algebraic space. By covering $R$ by finitely many affine schemes $\mathop{\mathrm{\textup{Spec}}}A_{i}$ we can write $\shF(\stY)$ as kernel of a map $\shF(A)\arr\oplus_{i}\shF(A_{i})$. If we base change along a flat map $B\arr B'$ it is now easy to see that $\shF(\stY\times_{B}B')\simeq\shF(\stY)\otimes_{B}B'$, as required.

To define the natural transformation $\alpha\colon g^{*}f_{*}\arr f'_{*}g'^{*}$ notice that there is a natural map $f_{*}\shF\arr f_{p}\shF$ which extends the identity on $\stX_{\text{fl}}$. Applying $g^{*}$ we get $g^{*}f_{*}\shF\arr g^{*}f_{p}\shF\simeq f'_{p}g'^{*}\shF$ and then, restricting to $\stX'_{\text{fl}}$, a map $(g^{*}f_{*}\shF)_{|\stX'_{\text{fl}}}\arr(f'_{*}g'^{*}\shF)_{|\stX'_{\text{fl}}}$. Since both sides are in $\mathop{\mathrm{\textup{QCoh}}}\stX'_{\text{fl}}$ this map uniquely extends to a natural transformation $\alpha$ as required. Finally assume that $g$ is flat and let $\xi\colon\mathop{\mathrm{\textup{Spec}}}B\arr\stX'\in\stX'_{\text{fl}}$. If the composition $\mathop{\mathrm{\textup{Spec}}}B\arr\stX$ is in $\stX_{\text{fl}}$ then one can easily check that $\alpha(\xi)$ is an isomorphism. Otherwise, by definition of flatness, there exists an fpqc covering $\mathop{\mathrm{\textup{Spec}}}B'\arr\mathop{\mathrm{\textup{Spec}}}B$ whose composition $\xi'\colon\mathop{\mathrm{\textup{Spec}}}B'\arr\stX'$ satisfies the previous condition. Since $\alpha(\xi)\otimes_{B}B'\simeq\alpha(\xi')$ we get the desired result. ◻
:::

::: rem
There are set-theoretic problems in considering global sections of presheaves and therefore push-forwards, because $\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$ is in general not locally small. The common way to solve this problem is to use Grothendieck universes. Take a universe $U$ and define rings inside $U$, so that $\mathop{\mathrm{\textup{Aff}}}/R$ is small (with respect to a bigger universe). Fibered categories should then be required to be small too. In this situation it is easy to show that $\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$ is locally small and therefore global sections and push-forwards are well defined. With this approach we have to be careful in considering (big) rings defined starting from some $\shF\in\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$: for instance $\mathop{\mathrm{\textup{Spec}}}\odi{\stX}(\stX)$ is in general not an object of $\mathop{\mathrm{\textup{Aff}}}/R$.

Notice that global sections and pushforwards of quasi-coherent sheaves are always well defined for a pseudo-algebraic fibered category and a pseudo-algebraic map respectively. The reason is that if $\shF\in\mathop{\mathrm{\textup{QCoh}}}\stX$ and $p\colon X\arr\stX$ is a fpqc atlas then $\shF(\stX)\arr(p^{*}\shF)(X)$ is injective and thus $\shF(\stX)$ is a set.

In the rest of the paper we will not be concerned about those set-theoretic problems.
:::

::: defn
[]{#rem: A module structures of odix modules label="rem: A module structures of odix modules"} If $A$ is an $R$-algebra and $\shF\in\mathop{\mathrm{\textup{Mod}}}\odi{\stX}$ then a compatible $A$-module structure on $\shF$ is the data of $A$-module structures on $\shF(\xi)$ commuting with the $\mathop{\mathrm{\textup{H}}}^{0}(\odi{\pi(\xi)})$-module structure on $\shF(\xi)$ for all $\xi\in\stX$ and such that, for all $\xi\arr\eta$ in $\stX$, the map $\shF(\eta)\arr\shF(\xi)$ is $A$-linear. We define $\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ as the category of quasi-coherent sheaves over $\stX$ with an $A$-module structure. We also define $\stX_{A}$ as the fiber product $\mathop{\mathrm{\textup{Spec}}}A\times_{R}\stX$.
:::

Notice that if $\stY\arrdi g\stX$ is a map of fibered categories and $\shF$ is a presheaf of $\odi{\stX}$-modules with an $A$-module structure then $g^{*}\shF$ inherits an $A$-module structure. In particular $g^{*}\colon\mathop{\mathrm{\textup{QCoh}}}\stX\arr\mathop{\mathrm{\textup{QCoh}}}\stY$ extends to a functor $\mathop{\mathrm{\textup{QCoh}}}_{A}\stX\arr\mathop{\mathrm{\textup{QCoh}}}_{A}\stY$.

::: prop
Let $A$ be an $R$-algebra. Then the push-forward map $\mathop{\mathrm{\textup{QCoh}}}\stX_{A}\arr\mathop{\mathrm{\textup{QCoh}}}\stX$ extends naturally to an equivalence $\mathop{\mathrm{\textup{QCoh}}}\stX_{A}\arr\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$.
:::

::: proof
*Proof.* The result is very simple if $\stX$ is an affine scheme. In general, if we set $g\colon\stX_{A}\arr\stX$ for the projection and we consider $\shG\in\mathop{\mathrm{\textup{QCoh}}}\stX_{A}$, then $g_{*}\shG\in\mathop{\mathrm{\textup{QCoh}}}\stX$ and it inherits an $A$-module structure from the action of $A$ on $\shG$. Therefore $g_{*}\shG\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$. If $h\colon\mathop{\mathrm{\textup{Spec}}}B\arr\stX$ is a map consider the diagrams $$\begin{tikzpicture}[xscale=3.4,yscale=-1.0]     
\node (A0_0) at (0.3, 0) {$\mathop{\mathrm{\textup{Spec}}}(B\otimes_R A)$};     
\node (A0_1) at (1, 0) {$\stX_A$};     \node (A0_2) at (2, 0) {$\mathop{\mathrm{\textup{QCoh}}}\stX_A$};     \node (A0_3) at (3, 0) {$\mathop{\mathrm{\textup{QCoh}}}\mathop{\mathrm{\textup{Spec}}}(B\otimes_R A)$};     \node (A1_0) at (0.3, 1) {$\mathop{\mathrm{\textup{Spec}}}B$};    
\node (A1_1) at (1, 1) {$\stX$};     \node (A1_2) at (2, 1) {$\mathop{\mathrm{\textup{QCoh}}}_A \stX$};     \node (A1_3) at (3, 1) {$\mathop{\mathrm{\textup{QCoh}}}_A \mathop{\mathrm{\textup{Spec}}}B$};     \path (A0_0) edge [->]node [auto] {$\scriptstyle{h'}$} (A0_1);     \path (A0_1) edge [->]node [auto] {$\scriptstyle{g}$} (A1_1);     \path (A1_0) edge [->]node [auto] {$\scriptstyle{h}$} (A1_1);     \path (A0_3) edge [->]node [auto] {$\scriptstyle{g'_*}$} (A1_3);     \path (A0_2) edge [->]node [auto] {$\scriptstyle{g_*}$} (A1_2);     \path (A0_0) edge [->]node [auto] {$\scriptstyle{g'}$} (A1_0);     \path (A0_2) edge [->]node [auto] {$\scriptstyle{h'^*}$} (A0_3);     \path (A1_2) edge [->]node [auto] {$\scriptstyle{h^*}$} (A1_3);   \end{tikzpicture}$$ The second diagram is $2$-commutative and the last vertical map is an equivalence. Using those diagrams it is easy to define a quasi-inverse $\mathop{\mathrm{\textup{QCoh}}}_{A}\stX\arr\mathop{\mathrm{\textup{QCoh}}}\stX_{A}$ of $g_{*}$. ◻
:::

We will almost always regard quasi-coherent sheaves over $\stX_{A}$ as objects of $\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$.

::: rem
[]{#rem: remark on the tensor product over A label="rem: remark on the tensor product over A"} If $\shF,\shG\in\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ then $\shF\otimes_{\odi{\stX}}\shG$ does not correspond to the tensor product in $\mathop{\mathrm{\textup{QCoh}}}\stX_{A}$: $\shF\otimes_{\odi{\stX}}\shG$ has two distinct $A$-module structures. Under the equivalence $\mathop{\mathrm{\textup{QCoh}}}\stX_{A}\arr\mathop{\mathrm{\textup{QCoh}}}_{A}\stX$ the tensor product of $\shF$ and $\shG$, that we will denote by $\shF\otimes_{\odi{\stX_{A}}}\shG$, is given by $$U\longmapsto\shF(U)\otimes_{\mathop{\mathrm{\textup{H}}}^{0}(\odi U)}\shG(U)/\langle ax\otimes y-x\otimes ay\st x\in\shF(U),y\in\shG(U)\rangle$$
:::

::: defn
A locally free sheaf $\E$ (of rank $n$) over $\stX$ is a quasi-coherent sheaf such that $\E(\mathop{\mathrm{\textup{Spec}}}B\arr\stX)$ is a finitely generated projective $B$-module (of rank $n$) for all maps $\mathop{\mathrm{\textup{Spec}}}B\arr\stX$. We denote by $\mathop{\mathrm{\textup{Loc}}}\stX$ the subcategory of $\mathop{\mathrm{\textup{QCoh}}}\stX$ of locally free sheaves.

We will say that a fiber category $\stX$ has the *resolution property* if $\mathop{\mathrm{\textup{Loc}}}\stX$ generates $\mathop{\mathrm{\textup{QCoh}}}\stX$.
:::
