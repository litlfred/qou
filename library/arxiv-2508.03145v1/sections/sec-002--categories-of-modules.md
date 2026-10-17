---
doc_id: arxiv-2508.03145v1
doc_title: "Θ -Categories and Tannakian duality"
section_id: sec-002--categories-of-modules
section_title: "-Categories of modules"
section_number: null
pages: 11-14
source_pdf: 2508.03145v1.pdf
source_sha256: 2bf03452cb503e96
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.978
doc_brief: "Θ -Categories and Tannakian duality — We introduce a notion of Θ-categories, which is a refinement of the notion of symmetric monoidal ∞-categories."
---
To conclude this part on $\Theta$-categories, we will define a $\Theta$-category of left $B$-modules for a given $\Theta$-algebra $B \in \Theta\text{-}\mathsf{CAlg}(T^\Theta)$. To this end, we first consider the underlying commutative algebra $B_0:=U_{E_\infty}^{\Theta}(B)$ and the corresponding symmetric monoidal $\infty$-category $\mathsf{LMod}_{B_0}(T)$ of left $B_0$-modules in $T$ endowed with its natural symmetric monoidal structure $\otimes_{B_0}$. It will be denoted by $B_0\text{-}\mathsf{Mod}(T)$.

We define a $\Theta$-structure on $B_0\text{-}\mathsf{Mod}(T)$ by considering the composition of forgetful $\infty$-functors $$B/\Theta\text{-}\mathsf{CAlg}(T^\Theta) \longrightarrow B_0/\mathsf{CAlg}(T)\simeq \mathsf{CAlg}(B_0\text{-}\mathsf{Mod}(T)) \longrightarrow B_0\text{-}\mathsf{Mod}(T).$$ The above sequence of $\infty$-functors defines an new $\Theta$-category whose underlying $\infty$-category is the $\infty$-category of $B_0$-modules and whose $\infty$-category of $\Theta$-algebras is $B/\Theta\text{-}\mathsf{CAlg}(T^\Theta)$, the $\infty$-category of $\Theta$-algebras under $B$.

::: df
[]{#d1-5 label="d1-5"} We will refer to the $\Theta$-category constructed above $$B/\Theta\text{-}\mathsf{CAlg}(T^\Theta) \longrightarrow \mathsf{CAlg}(B_0\text{-}\mathsf{Mod}(T)) \longrightarrow B_0\text{-}\mathsf{Mod}(T)$$ as the *$\Theta$-category of $B$-modules in $T$*, and denote it simply by $B\text{-}\mathsf{Mod}(T^\Theta)$.
:::

The $\Theta$-category of $\Theta$-modules in $T^\Theta$ receives a natural morphism from $T^\Theta$ by tensoring with $B$. This natural morphism $T^\Theta \to B\text{-}\mathsf{Mod}(T^\Theta)$ can be represented by the following commutative diagram of $\infty$-categories $$\xymatrix{
\Theta\text{-}\mathsf{CAlg}(T^\Theta) \ar[r] \ar[d]_-{\coprod B} & \mathsf{CAlg}(T) \ar[d]^-{\otimes B_0} \ar[r] & 
T \ar[d]^-{\otimes B_0} \\
B/\Theta\text{-}\mathsf{CAlg}(T^\Theta)  \ar[r] & B_0/\mathsf{CAlg}(T) \ar[r] & B_0\text{-}\mathsf{Mod}(T).
}$$ Here the rows are right adjoints whereas the vertical morphisms are left adjoints, whose right adjoints (forgetting the maps from $B$ or $B_0$) commute with the horizontal functors.

We can now state the following proposition, which is an extension to the context of $\Theta$-categories of the results [@HA Cor. 4.8.5.21] on symmetric monoidal $\infty$-categories and commutative algebras.

::: prop
[]{#p1-2 label="p1-2"} Let $T^\Theta$ be a $\Theta$-category. The $\infty$-functor sending a $\Theta$-algebra $B \in \Theta\text{-}\mathsf{CAlg}(T^\Theta)$ to $T^\Theta \to B\text{-}\mathsf{Mod}(T^\Theta)$ induces a fully faithful left adjoint $\infty$-functor $$\Theta\text{-}\mathsf{CAlg}(T^\Theta) \longrightarrow T^\Theta/\infty\text{-}\mathbf{Cat}_{pr}^\Theta.$$
:::

::: proof
*Proof.* Unwinding the definitions, this is a consequence of the following two statements.

1.  The $\infty$-functor sending a commutative algebra $B_0 \in \mathsf{CAlg}(T)$ to $T \to B_0\text{-}\mathsf{Mod}(T)$ induces a fully faithful left adjoint functor of $(2, \infty)$-categories $$\mathsf{CAlg}(T) \longrightarrow T/\infty\text{-}\mathbf{Cat}_{pr}^{\otimes}.$$

2.  For any presentable $\infty$-category $C$, the $\infty$-functor $$C \to (\infty\text{-}\mathbf{Cat}_{pr}^R/C)^{op}$$ sending $x \in C$ to the comma $\infty$-category $x/C$ with the projection $x/C \to C$, and a morphism $u \colon y\to x$ to the composition $x/C \to y/C$ with $u$, defines a full embedding.

Note that the $\infty$-category of maps $B\text{-}\mathsf{Mod}(T)\to T'$ in $T/\infty\text{-}\mathbf{Cat}^\otimes_{pr}$ is in fact a space: any natural transformation $\mu\colon f\Rightarrow g$ between morphisms $f, g\colon B\text{-}\mathsf{Mod}(T)\to T'$ in $T/\infty\text{-}\mathbf{Cat}_{pr}^{\otimes}$ is an equivalence. Indeed, the class $B$-modules $M$ such that $\mu_M$ is an equivalence is closed under colimits and contains the free $B$-modules. In light of this, statement $(1)$ is proven in [@HA Thm. 4.8.5.11, Cor. 4.8.5.21], whereas statement $(2)$ is simply a version of the Yoneda lemma.\
Let $B\in \Theta\text{-}\mathsf{CAlg}(T^{\Theta})$ be a $\Theta$-algebra in $T^\Theta$ and $g\colon T^{\Theta}\to T_2^{\Theta}$ a $\Theta$-functor. Let $g_*(\mathbf{1})\in \Theta\text{-}\mathsf{CAlg}(T^{\Theta})$ be the image of $\mathbf{1}\in \Theta\text{-}\mathsf{CAlg}(T_2^{\Theta})$ under the right adjoint $g_*$. We then have the following commutative square of mapping spaces (rather than $\infty$-categories, by Remark [\[r-1-2\]](#r-1-2){reference-type="ref" reference="r-1-2"}) $$\xymatrix{
\mathbf{Map}_{T^\Theta/\infty\text{-}\mathbf{Cat}_{pr}^\Theta}(B\text{-}\mathsf{Mod}(T^\Theta),T_2^{\Theta}) \ar[r] \ar[d] &
\mathbf{Map}_{\Theta\text{-}\mathsf{CAlg}(T^\Theta)}(B,g_*(\mathbf{1})) \ar[d] \\
\mathbf{Map}_{T/\infty\text{-}\mathbf{Cat}_{pr}^\otimes}(B_0\text{-}\mathsf{Mod}(T),T_2) \ar[r] & \mathbf{Map}_{\mathsf{CAlg}(T)}(B_0,g_*(\mathbf{1})).}$$ Here the top horizontal map sends a $\Theta$-functor $f\colon B\text{-}\mathsf{Mod}(T^{\Theta})\to T_2^{\Theta}$ to the unit map $B\to f_*(\mathbf{1})$ in $\Theta\text{-}\mathsf{CAlg}(B\text{-}\mathsf{Mod}(T^{\Theta}))$. This corresponds to a map $B\to g_*(\mathbf{1})$ in $\Theta\text{-}\mathsf{CAlg}(T^{\Theta})$ under the equivalence $$\Theta\text{-}\mathsf{CAlg}(B\text{-}\mathsf{Mod}(T^{\Theta}))\simeq B/\Theta\text{-}\mathsf{CAlg}(T^{\Theta}).$$ The bottom horizontal map is defined similarly.

It now suffices to verify that the top horizontal map is an equivalence. Indeed, this shows that the functor $B\mapsto B\text{-}\mathsf{Mod}(T^{\Theta})$ is a left adjoint. Taking $T_2^{\Theta}=B_2\text{-}\mathsf{Mod}(T^{\Theta})$, so that $g_*(\mathbf{1})=B_2$, shows that it is fully faithful.

By property (1) above, the bottom horizontal map is an equivalence. Let us therefore fix a symmetric monoidal $\infty$-functor $f\colon B\text{-}\mathsf{Mod}(T)\to T_2$ under $T$, and compare the induced map between the fibers of the two vertical maps. By Proposition [\[p1-1\]](#p1-1){reference-type="ref" reference="p1-1"}, there is a canonical equivalence between $\mathbf{Map}_{T^\Theta/\infty\text{-}\mathbf{Cat}_{pr}^\Theta}(B\text{-}\mathsf{Mod}(T^\Theta),T_2^\Theta)_f$ and the space of all possible limit preserving $\infty$-functors $u$ filling up the diagram below in $\infty\text{-}\mathbf{Cat}^R_{pr}$ $$\xymatrix{
\ar@{.>}@/_4pc/[dd]_ -{u} \Theta\text{-}\mathsf{CAlg}(T_2^\Theta) \ar[d]_-{g_*} \ar[r] & \ar@/_3pc/[dd]_>>>>>>>{f_*} 
\mathsf{CAlg}(T_2) \ar[d]^-{g_*} \\
\Theta\text{-}\mathsf{CAlg}(T^\Theta) \ar[r]|(0.635)\hole & \mathsf{CAlg}(T) \\
B/\Theta\text{-}\mathsf{CAlg}(T^\Theta) \ar[r] \ar[u] & B_0/\mathsf{CAlg}(T) \ar[u] 
}$$ such that $f^*\circ U^{\Theta}_{E_\infty}\Rightarrow U^{\Theta}_{E_\infty}\circ u^*$ is an equivalence.

Note that there is an equivalence of $\infty$-categories $$\Theta\text{-}\mathsf{CAlg}(T_2^{\Theta})\times_{\Theta\text{-}\mathsf{CAlg}(T^{\Theta})} B/\Theta\text{-}\mathsf{CAlg}(T^{\Theta}) \simeq g(B)/\Theta\text{-}\mathsf{CAlg}(T_2^{\Theta})$$ since $g\colon \Theta\text{-}\mathsf{CAlg}(T^\Theta)\to \Theta\text{-}\mathsf{CAlg}(T_2^{\Theta})$ is left adjoint to $g_*$, and similarly for commutative algebras. Property (2) recalled at the start of the proof therefore identifies the space of $u$ filling the diagram with the fiber at $f$ of the natural morphism $$\mathbf{Map}_{\Theta\text{-}\mathsf{CAlg}(T_2^\Theta)}(g(B),\mathbf{1}) \to \mathbf{Map}_{\mathsf{CAlg}(T_2)}(g(B_0),\mathbf{1}).$$ By adjunction, this is equivalent to the fiber at $f$ of the natural morphism $$\mathbf{Map}_{\Theta\text{-}\mathsf{CAlg}(T^\Theta)}(B,g_*(\mathbf{1})) \to \mathbf{Map}_{\mathsf{CAlg}(T)}(B_0,g_*(\mathbf{1})).$$ The result now follows by noting that for each map of $\Theta$-algebras $B\to g_*(\mathbf{1})$, the natural transformation $g_*(\mathbf{1})\otimes_{B_0} U^{\Theta}_{E_\infty}(-)\Rightarrow U^{\Theta}_{E_\infty}(g_*(\mathbf{1})\amalg_B -)$ is an equivalence since $U^{\Theta}_{E_\infty}$ preserves colimits. ◻
:::

Proposition [\[p1-2\]](#p1-2){reference-type="ref" reference="p1-2"} can be usefully combined with the following recognition result. For this, we note that a $\Theta$-functor $f \colon T_1^\Theta \to T_2^\Theta$ always induces an adjunction on the level of the corresponding $\infty$-categories of $\Theta$-algebras $$f \colon \Theta\text{-}\mathsf{CAlg}(T_1^\Theta) \leftrightarrows \Theta\text{-}\mathsf{CAlg}(T_2^\Theta) : f_*$$ where $f$ and $f_*$ commute with the forgetful $\infty$-functors to $T_1$ and $T_2$. For any $B \in \Theta\text{-}\mathsf{CAlg}(T_1^\Theta)$, this yields a well-defined $\Theta$-functor at the level of modules $$f \colon B\text{-}\mathsf{Mod}(T_1^\Theta) \to f(B)\text{-}\mathsf{Mod}(T_2^\Theta).$$ Applying this to $B = f_*(\mathbf{1})$, and composing with the base change along the counit $f(f_*(\mathbf{1})) \to \mathbf{1}$, we obtain a natural $\Theta$-functor $f_*(\mathbf{1})\text{-}\mathsf{Mod}(T_1^\Theta) \to T_2^\Theta$ whose underlying adjunction of $\infty$-categories takes the form $$\mathbf{1}\otimes_{f(f_*(\mathbf{1}))} f(-)\colon f_*(\mathbf{1})\text{-}\mathsf{Mod}(T_1)\leftrightarrows T_2 : f_*.$$

::: prop
[]{#p1-3 label="p1-3"} Let $T_1^\Theta \to T_2^\Theta$ be a $\Theta$-functor and $f \colon T_1 \to T_2$ the underlying symmetric monoidal $\infty$-functor. We assume that the right adjoint $f_* \colon T_2 \to T_1$ of $f$ satisfies the following conditions.

1.  The $\infty$-functor $f_*$ is conservative and preserves geometric realizations.

2.  For $y \in T_2$ and $x \in T_1$, the natural morphism $$x\otimes f_*(y) \to f_*(f(x) \otimes y)$$ is an equivalence in $T_1$.

Then the natural $\Theta$-functor $$f_*(\mathbf{1})\text{-}\mathsf{Mod}(T_1^\Theta) \longrightarrow T_2^\Theta$$ is an equivalence of $\Theta$-categories.
:::

::: proof
*Proof.* The underlying symmetric monoidal $\infty$-functor $f_*(\mathbf{1})\text{-}\mathsf{Mod}(T_1) \to T_2$ is an equivalence by the second part of [@HA Cor. 4.8.5.21]. As forgetting the $\Theta$-structure $\infty\text{-}\mathbf{Cat}_{pr}^\Theta\to \infty\text{-}\mathbf{Cat}_{pr}^{\otimes}$ is conservative, this implies the proposition. ◻
:::
