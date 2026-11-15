---
doc_id: arxiv-2508.03145v1
doc_title: "Θ -Categories and Tannakian duality"
section_id: sec-001--categories
section_title: "-Categories"
section_number: null
pages: 6-11
source_pdf: 2508.03145v1.pdf
source_sha256: 2bf03452cb503e96
toc_source: outline
text_source: latex
latex_prose_ratio: 0.825
latex_coverage_ratio: 0.968
doc_brief: "Θ -Categories and Tannakian duality — We introduce a notion of Θ-categories, which is a refinement of the notion of symmetric monoidal ∞-categories."
---
## $\mu$-Categories

We let $\infty\text{-}\mathbf{Cat}_{pr}^{R}$ be the $(2,\infty)$-category of presentable $(1,\infty)$-categories and right adjoints (i.e. limit preserving accessible $\infty$-functors). We have the corresponding $(2,\infty)$-category $\mathsf{Fun}(\Delta^1,\infty\text{-}\mathbf{Cat}^{R}_{pr})$, of morphisms in $\infty\text{-}\mathbf{Cat}_{pr}^{R}$. For any object $f \colon T' \to T$ in $\mathsf{Fun}(\Delta^1,\infty\text{-}\mathbf{Cat}^R_{pr})$, we will denote by $f^* \colon T \to T'$ the left adjoint to $f$, and sometimes write $f_*$ instead of $f$.

::: df
[]{#d1-1 label="d1-1"} An object $f_* \colon T' \to T$ in $\mathsf{Fun}(\Delta^1,\infty\text{-}\mathbf{Cat}^{R}_{pr})$ is a *$\mu$-category* if $f_*$ is conservative and preserves sifted colimits.
:::

Note that, by the Barr--Beck theorem [@HA Thm. 4.7.0.3] the condition of being a $\mu$-category implies that the canonical factorization of $f_*$ $$T' \to \mathsf{LMod}_{M}(T) \to T,$$ induces an equivalence $T' \simeq \mathsf{LMod}_M(T)$. Here $M=f_*f^*$ is the monad on $T$ associated with the adjunction $(f^*, f_*)$, and $\mathsf{LMod}_{M}(T)$ is the $\infty$-category of $M$-modules in $T$.

::: df
[]{#d1-2 label="d1-2"} Let $f_* \colon T_1' \to T_1$ and $g_* \colon T_2' \to T_2$ be two $\mu$-categories in the sense of Definition [\[d1-1\]](#d1-1){reference-type="ref" reference="d1-1"}. A *$\mu$-morphism* from $T_1' \to T_1$ to $T_2' \to T_2$ consists of a commutative square in $\infty\text{-}\mathbf{Cat}$ $$\xymatrix{
T_1' \ar[r]^{u}  \ar[d]_-{f_*} & T_2' \ar[d]^-{g_*} \\
T_1 \ar[r]_{v} & T_2,
}$$ with $u$ and $v$ colimit preserving $\infty$-functors, and such that the induced natural transformation $g^* \circ v \Rightarrow u\circ f^*$ is an equivalence. We will write $$\infty\text{-}\mathbf{Cat}^\mu\subset \mathsf{Fun}(\Delta^1,\infty\text{-}\mathbf{Cat})$$ for the (non-full) sub-$(2,\infty)$-category of $\mu$-categories and $\mu$-morphisms.
:::

::: rmk
Let us highlight the variance of the $\infty$-functors in the above definition: we have decided to use the *left* adjoints $u$ and $v$, instead of their right adjoints $u_*$ and $v_*$ to specify the variance. A $\mu$-morphism is therefore given by a commutative square as in Definition [\[d1-2\]](#d1-2){reference-type="ref" reference="d1-2"} that is *right adjointable* in the sense of [@HA Def. 4.7.4.13].
:::

::: rmk
[]{#r-1 label="r-1"} The condition on a $\mu$-morphism implies that we have several canonical equivalences between functors, obtained by taking various adjoints $$g^*\circ v \simeq u\circ f^* \quad\qquad v\circ f_* \simeq g_* \circ u \quad\qquad v_*\circ g_* \simeq f_*\circ u_*.$$ Using this, there are various equivalent ways of defining $\mu$-morphisms. For instance, a $\mu$-morphism from $T_1' \to T_1$ to $T_2' \to T_2$ can equivalently be encoded by a *left adjointable* square in $\infty\text{-}\mathbf{Cat}$ of the form $$\xymatrix{
T_2' \ar[r]^{u_*}  \ar[d]_-{f_*} & T_1' \ar[d]^-{g_*} \\
T_2 \ar[r]_{v_*} & T_1,
}$$ This exhibits $\infty\text{-}\mathbf{Cat}^\mu\subset \mathsf{Fun}(\Delta^1,\infty\text{-}\mathbf{Cat}^{R}_{pr})^{op}$ as a (non-full) sub-$(2, \infty)$-category of the *opposite* $(2, \infty)$-category of morphisms in $\infty\text{-}\mathbf{Cat}^R_{pr}$.
:::

By definition, an object $T' \to T$ can also be written, up to equivalence, as the forgetful $\infty$-functor $\mathsf{LMod}_M(T) \to T$ for a monad $M$ on $T$, which furthermore commutes with sifted colimits. Objects in $\infty\text{-}\mathbf{Cat}^\mu$ can therefore be identified, up to equivalence, with pairs $(T', M)$, with $T$ a presentable $\infty$-category and $M$ a sifted colimit preserving monad on $T$. Morphisms in $\infty\text{-}\mathbf{Cat}^\mu$ can then be viewed as $\infty$-functors endowed with compatibility data with the monads; see [@MR4367222] for more details. This is our justification for the terminology *$\mu$-category*, where $\mu$ stands for *monad*.

We will often present objects in $\infty\text{-}\mathbf{Cat}^\mu$ as pairs $(T, M)$ of a presentable $\infty$-category $T$ and a sifted colimit preserving monad $M$ on $T$. The $\infty$-category $T$ will be called the *underlying $\infty$-category* of the object $(T, M)$. The association $(T, M) \mapsto T$ defines an evident forgetful $(2,\infty)$-functor $$\infty\text{-}\mathbf{Cat}^\mu\to \infty\text{-}\mathbf{Cat}^L_{pr},$$ where $\infty\text{-}\mathbf{Cat}_{pr}^L$ is the $(2,\infty)$-category of presentable $\infty$-categories and left adjoints as morphisms. The $(2,\infty)$-functor above is also induced by the composition of the inclusion $\infty\text{-}\mathbf{Cat}^\mu\subset \mathsf{Fun}(\Delta^1,\infty\text{-}\mathbf{Cat})$ and the evaluation $\mathsf{Fun}(\Delta^1,\infty\text{-}\mathbf{Cat})\to \infty\text{-}\mathbf{Cat}$ at the object $1 \in \Delta^1$. The forgetful $(2,\infty)$-functor $\infty\text{-}\mathbf{Cat}^\mu\to \infty\text{-}\mathbf{Cat}_{pr}^L$ is easily seen to be conservative. Indeed, if $$\xymatrix{
T_1' \ar[r]^{u}  \ar[d]_-{f_*} & T_2' \ar[d]^-{g_*} \\
T_1 \ar[r]_{v} & T_2,
}$$ is a right adjointable square in $\infty\text{-}\mathbf{Cat}$ and if $v$ is an equivalence, then $u$ is automatically an equivalence. The adjointability property implies that the unit and counit of the adjunction $(u,u_*)$ $$a \colon u \circ u_* \Rightarrow id \qquad b : id \Rightarrow u_* \circ u$$ are sent by $f_*$ and $g_*$ to the unit and counit of the adjunction $(v,v_*)$. As $v$ is an equivalence, these are equivalences in $T_1$ and $T_2$, and as $f_*$ and $g_*$ are conservative, $a$ and $b$ must be equivalences to.\
We finish this first section by noticing that $\infty\text{-}\mathbf{Cat}^\mu$ receives a natural $(2,\infty)$-functor from the $(2,\infty)$-category of presentable symmetric monoidal $\infty$-categories. For this, we let $\infty\text{-}\mathbf{Cat}^{\otimes}_{pr}$ be the $(2,\infty)$-category of presentable symmetric monoidal $\infty$-categories, and colimit preserving symmetric monoidal $\infty$-functors as morphisms. To each $T \in \infty\text{-}\mathbf{Cat}^\otimes_{pr}$ we can associate the $\infty$-category of commutative algebras in $T$, formally defined as $\mathsf{CAlg}(T) := \mathsf{Fun}^{lax-\otimes}(*,T)$, the $\infty$-category of symmetric lax-monoidal $\infty$-functors from the punctual $\infty$-category (with its canonical symmetric monoidal structure) to $T$. Evaluation at the unique object $*$ provides a well-defined right adjoint $\infty$-functor $\mathsf{CAlg}(T) \to T$. This construction extends to a $(2,\infty)$-functor $$\infty\text{-}\mathbf{Cat}^{\otimes}_{pr} \to \infty\text{-}\mathbf{Cat}^\mu; \quad T \mapsto (\mathsf{CAlg}(T) \to T)$$ from symmetric monoidal $\infty$-categories to $\mu$-categories. To see this, note that each symmetric monoidal left adjoint $\infty$-functor $u\colon T_1\to T_2$ defines a left adjoint in the $(2,\infty)$-category of symmetric monoidal $\infty$-categories and symmetric lax-monoidal $\infty$-functors (see [@HA Cor. 7.3.2.7]). Composition with $(u, u_*)$ then defines an adjunction between $\infty$-categories of commutative algebras, which commutes with the forgetful functors; this implies that $u$ induces a natural transformation from $\mathsf{CAlg}(T_1)\to T_1$ to $\mathsf{CAlg}(T_2)\to T_2$ that is right adjointable.

In terms of monads, one can think of $\infty\text{-}\mathbf{Cat}^{\otimes}_{pr} \to \infty\text{-}\mathbf{Cat}^\mu$ as sending a presentable symmetric monoidal $\infty$-category $T$ to the pair $(T,M)$, consisting of the underlying $\infty$-category $T$ endowed with the $E_\infty$-algebra monad $$\mathrm{Sym}_{E_\infty}(x) = \coprod_{n\in \mathbb{N}}(x^{\otimes n})_{h\Sigma_n}.$$

## $\Theta$-Categories

Let $C$ be the $(2,\infty)$-category defined by the following lax-cartesian square $$\xymatrix{
\infty\text{-}\mathbf{Cat}^{\otimes}_{pr} \ar[r]^-{q} \ar@{}[rd]^(0.3){}="s"^(0.7){}="t"\ar@{=>} "s";"t" & \mathsf{Fun}(\Delta^1, \infty\text{-}\mathbf{Cat}_{pr}^{R})^{op} \\
C \ar[r] \ar[u] & \infty\text{-}\mathbf{Cat}^\mu. \ar[u]_-{p}
}$$ In this diagram, the top right corner is the $(2,\infty)$-category of all morphisms in $\infty\text{-}\mathbf{Cat}_{pr}^R$, the $(2,\infty)$-category of presentable $\infty$-categories and right adjoints. The top horizontal arrow $q$ arises from the canonical construction discussed at the end of the last section: it sends $T \in \infty\text{-}\mathbf{Cat}_{pr}^\otimes$ to the pair $\mathsf{CAlg}(T) \to T$, and a symmetric monoidal $\infty$-functor $u \colon T_1 \to T_2$ to its right adjoint $$\xymatrix{
\mathsf{CAlg}(T_2) \ar[r]^-{u_*} \ar[d] & \mathsf{CAlg}(T_1) \ar[d] \\
T_2 \ar[r]_-{u_*} & T_1.}$$ The morphism $p$ is the inclusion from Remark [\[r-1\]](#r-1){reference-type="ref" reference="r-1"}, sending a $\mu$-category $(T'\to T)$ to $T' \to T$, and a morphism $(u,v)$ to its right adjoint square $(u_*, v_*)$.

Objects in $C$ can be thought of as triples $(T_1, (T_2'\to T_2), u)$, where $T_1$ is a presentable symmetric monoidal $\infty$-category, $(T_2' \to T_2)$ is a $\mu$-category and $u$ is a commutative diagram in $\infty\text{-}\mathbf{Cat}_{pr}^{R}$ $$\xymatrix{
T_2' \ar[r] \ar[d] & \mathsf{CAlg}(T_1) \ar[d]  \\
T_2 \ar[r] &T_1 .
}$$

::: df
[]{#d1-3 label="d1-3"} The *$(2,\infty)$-category of $\Theta$-categories* is the full sub-$(2,\infty)$-category of the $(2, \infty)$-category $C$ defined above consisting of the objects $(T_1,(T_2'\to T_2),u)$ that satisfy the following conditions.

1.  The induced (right adjoint) $\infty$-functor $T_2 \to T_1$ is an equivalence.

2.  The induced (right adjoint) $\infty$-functor $T_2'\to \mathsf{CAlg}(T_1)$ commutes with arbitrary colimits.

This $(2,\infty)$-category is denoted by $\infty\text{-}\mathbf{Cat}_{pr}^\Theta$.
:::

In more intuitive terms, objects in $\infty\text{-}\mathbf{Cat}_{pr}^\Theta$ are presentable symmetric monoidal $\infty$-categories $T$ together with a monad $M$ on their underlying $\infty$-category, as well as a morphism of sifted colimit preserving monads $Sym_{E_\infty} \to M$ satisfying condition $(2)$ from Definition [\[d1-3\]](#d1-3){reference-type="ref" reference="d1-3"}. Note that, because push-outs in $\mathsf{CAlg}(T)$ are given by tensor products, this condition has the following equivalent reformulations.

1.  For $x, y\in T$, the natural maps of $E_\infty$-algebras $\mathbf{1}_M\to M(\emptyset)$ and $M(x)\otimes M(y) \to M(x\amalg y)$ are equivalences.

2.  The forgetful functor $\mathsf{LMod}_M(T)\to \mathsf{CAlg}(T)$ preserves push-outs, that is, push-outs in $\mathsf{LMod}_M(T)$ are compatible with tensor products in $T$.

The equivalence of these conditions with condition (2) from Definition [\[d1-3\]](#d1-3){reference-type="ref" reference="d1-3"} follows from the fact $\mathsf{LMod}_M(T)\to \mathsf{CAlg}(T)$ already preserves sifted colimits, so that it preserves all colimits if and only if it preserves finite coproducts of free algebras.

There is an obvious forgetful $(2,\infty)$-functor $$\infty\text{-}\mathbf{Cat}_{pr}^\Theta\to \infty\text{-}\mathbf{Cat}^\otimes_{pr},$$ which forgets the monad $M$. Note that it is conservative, because its composition with the conservative $\infty$-functor $\infty\text{-}\mathbf{Cat}^{\otimes}_{pr}\to \infty\text{-}\mathbf{Cat}^{L}_{pr}$ forgetting the monoidal structure is equivalent to the forgetful $\infty$-functor sending a triple $(T_1, (T_2'\to T_2), u)$ to $T_2 \simeq T_1$.

On the other hand, any symmetric monoidal $\infty$-category $T$ can be sent to the object in $\infty\text{-}\mathbf{Cat}_{pr}^\Theta$ defined by taking $M=\mathrm{Sym}_{E_\infty}$, or equivalently to the triple $(T, (\mathsf{CAlg}(T)\to T), id)$. By construction, it is a fully faithful $(2,\infty)$-functor and provides a full embedding of $(2,\infty)$-categories $$\infty\text{-}\mathbf{Cat}_{pr}^{\otimes} \longrightarrow \infty\text{-}\mathbf{Cat}_{pr}^\Theta.$$

::: rmk
[]{#r-1-3 label="r-1-3"} The $(1,\infty)$-category underlying $\infty\text{-}\mathbf{Cat}_{pr}^\Theta$ has small limits, and the forgetful functor $\infty\text{-}\mathbf{Cat}_{pr}^\Theta\to \infty\text{-}\mathbf{Cat}$ preserves these. Indeed, the lax pull-back $C$ has limits, computed at the level of the underlying $\infty$-categories, because the functors $q\colon \infty\text{-}\mathbf{Cat}^{\otimes}_{pr}\to \mathsf{Fun}(\Delta^1, \infty\text{-}\mathbf{Cat}_{pr}^{R})^{op}$ and $p\colon \infty\text{-}\mathbf{Cat}^\mu\to \mathsf{Fun}(\Delta^1, \infty\text{-}\mathbf{Cat}_{pr}^{R})^{op}$ both preserve limits. For $q$, this uses the fact that $(T, \otimes)\mapsto \mathsf{CAlg}(T)$ preserves limits by [@HA Prop 2.2.4.9]. Since the conditions from Definition [\[d1-2\]](#d1-2){reference-type="ref" reference="d1-2"} are stable under limits, $\infty\text{-}\mathbf{Cat}_{pr}^\Theta\subset C$ is closed under limits.
:::

::: nota
A $\Theta$-category will be denoted symbolically by $T^\Theta$, and its underlying presentable symmetric monoidal $\infty$-category will be denoted by $T$. The *$\Theta$-structure* of $T^\Theta$ is by definition the extra right adjoint $T'\simeq \mathsf{LMod}_M(T) \to \mathsf{CAlg}(T) \to T$ participating in the data of a $\Theta$-category. It will be symbolically denoted by $$\Theta\text{-}\mathsf{CAlg}(T^\Theta):=T' \to \mathsf{CAlg}(T)$$ and objects in $\Theta\text{-}\mathsf{CAlg}(T^\Theta)$ will be called *$\Theta$-algebras*.
:::

The $\infty$-category of $\Theta$-algebras comes equipped with a natural adjunction of presentable $\infty$-categories $$F^\Theta_{E_\infty} \colon \mathsf{CAlg}(T) \leftrightarrows \Theta\text{-}\mathsf{CAlg}(T^\Theta) : U_{E_\infty}^{\Theta}.$$ The right adjoint $U_{E_\infty}^{\Theta}$ is conservative and, more importantly, also a left adjoint, as it commutes with arbitrary colimits by assumption. In particular, it preserves the initial object. The initial object in $\mathsf{CAlg}(T)$ is the monoidal unit $\mathbf{1} \in T$, which therefore possesses a canonical compatible $\Theta$-algebra structure. The corresponding object will still be denoted by $\mathbf{1} \in \Theta\text{-}\mathsf{CAlg}(T^\Theta)$.\
We finish this part with a basic description of the $\infty$-categories of morphisms in $\infty\text{-}\mathbf{Cat}_{pr}^\Theta$. Let $T_1^\Theta$ and $T_2^\Theta$ be two $\Theta$-categories and $T_1$ and $T_2$ their underlying symmetric monoidal $\infty$-categories. Recall that $\infty\text{-}\mathbf{Cat}_{pr}^\Theta$ is defined as a full sub-$(2,\infty)$-category of $C$, the lax-fiber product below $$\xymatrix{
\infty\text{-}\mathbf{Cat}^{\otimes}_{pr} \ar[r]^-{q} \ar@{}[rd]^(0.3){}="s"^(0.7){}="t"\ar@{=>} "s";"t" & \mathsf{Fun}(\Delta^1, \infty\text{-}\mathbf{Cat}_{pr}^{R})^{op} \\
C \ar[r] \ar[u] & \infty\text{-}\mathbf{Cat}^\mu. \ar[u]_-{p}
}$$ Consequently, the $\infty$-category $\mathsf{Fun}_{\infty\text{-}\mathbf{Cat}_{pr}^\Theta}(T_1^{\Theta}, T_2^{\Theta})$ of morphisms in $\infty\text{-}\mathbf{Cat}_{pr}^\Theta$ can be identified with a natural fiber product as well. More precisely, the mapping $\infty$-category fits into a square of $\infty$-categories $$\xymatrix{
\mathsf{Fun}_{\infty\text{-}\mathbf{Cat}_{pr}^\Theta}(T_1^{\Theta}, T_2^{\Theta})\ar[r]\ar[d] & \mathsf{Fun}^R\big(\Theta\text{-}\mathsf{CAlg}(T_2^{\Theta}), \Theta\text{-}\mathsf{CAlg}(T_1^{\Theta})\big)\ar[d]\\
\mathsf{Fun}_{\infty\text{-}\mathbf{Cat}^{\otimes}_{pr}}(T_1,T_2)\ar[r] & \mathsf{Fun}^R\big(\Theta\text{-}\mathsf{CAlg}(T_2^{\Theta}), \mathsf{CAlg}(T_1)\big).
}$$ Here the bottom functor sends a left adjoint symmetric monoidal functor $f^*\colon T_1\to T_2$ to the composite right adjoint $$f_*\circ U^\Theta_{E_\infty}\colon \Theta\text{-}\mathsf{CAlg}(T_2^\Theta)\to \mathsf{CAlg}(T_2)\to \mathsf{CAlg}(T_1).$$ The right functor sends a right adjoint $u_*\colon \Theta\text{-}\mathsf{CAlg}(T_2^\Theta)\to \Theta\text{-}\mathsf{CAlg}(T_1^\Theta)$ to the composite $U^{\Theta}_{E_\infty}\circ u_*$.

::: lem
[]{#l-3 label="l-3"} The above square exhibits $\mathsf{Fun}_{\infty\text{-}\mathbf{Cat}_{pr}^\Theta}(T_1^{\Theta}, T_2^{\Theta})$ as the full sub-$\infty$-category of the fiber product on those tuples of a morphism $f^*\colon T_1\to T_2$ in $\infty\text{-}\mathbf{Cat}_{pr}^{\otimes}$ and a right adjoint $u_*\colon \Theta\text{-}\mathsf{CAlg}(T_2^\Theta)\to \Theta\text{-}\mathsf{CAlg}(T_1^\Theta)$ such that the commutative square in $\infty\text{-}\mathbf{Cat}_{pr}^R$ $$\xymatrix{
\Theta\text{-}\mathsf{CAlg}(T_2) \ar[d]_-{U^\Theta_{E_\infty}} \ar@{.>}[r]^-{u_*} & \Theta\text{-}\mathsf{CAlg}(T_1) \ar[d]^{U^\Theta_{E_\infty}} \\
\mathsf{CAlg}(T_2) \ar[r]_-{f_*} & \mathsf{CAlg}(T_1)
}$$ is left adjointable: the induced natural transformation $f^* \circ U^\Theta_{E_\infty} \Rightarrow U^\Theta_{E_\infty}\circ u^*$ is an equivalence.
:::

::: proof
*Proof.* Let us write $U^{E_\infty}\colon \mathsf{CAlg}(T)\to T$ and $U^{\Theta}=U^{E_\infty}\circ U^{\Theta}_{E_\infty}$ for the forgetful functors. Unravelling the definitions (using Remark [\[r-1\]](#r-1){reference-type="ref" reference="r-1"}), one sees that $\mathsf{Fun}_{\infty\text{-}\mathbf{Cat}_{pr}^\Theta}(T_1^{\Theta}, T_2^{\Theta})$ is the full sub-$\infty$-category of the fiber product on the pairs $(f^*, u_*)$ such that the natural transformation $f^*\circ U^\Theta\Rightarrow U^\Theta\circ u^*$ is an equivalence. This natural transformation is equivalent to the composition $f^*\circ U^{E_\infty}\circ U^{\Theta}_{E_\infty} \Rightarrow U_{E_\infty}\circ f^*\circ U^{\Theta}_{E_\infty}\Rightarrow U_{E_\infty}\circ U^{\Theta}_{E_\infty}\circ u^*$. The result follows because the first map is an equivalence and $U^{E_\infty}$ is conservative. ◻
:::

Taking the fiber of $\mathsf{Fun}_{\infty\text{-}\mathbf{Cat}_{pr}^\Theta}(T_1^\Theta,T_2^\Theta) \to \mathsf{Fun}_{\infty\text{-}\mathbf{Cat}^{\otimes}_{pr}}(T_1,T_2)$ over a fixed morphism $f \colon T_1 \to T_2$ in $\infty\text{-}\mathbf{Cat}_{pr}^\otimes$, we obtain the following proposition.

::: prop
[]{#p1-1 label="p1-1"} For two $\Theta$-categories $T_1^\Theta$ and $T_2^\Theta$, and $f \colon T_1 \to T_2$ in $\infty\text{-}\mathbf{Cat}_{pr}^{\otimes}$ a fixed symmetric monoidal $\infty$-functor, we have a cartesian square $$\xymatrix{\ar[d] \mathsf{Fun}^{R, adj}_{/\mathsf{CAlg}(T_1)}(\Theta\text{-}\mathsf{CAlg}(T_2),\Theta\text{-}\mathsf{CAlg}(T_1)) 
\ar[r] & 
\mathsf{Fun}_{\infty\text{-}\mathbf{Cat}_{pr}^\Theta}(T_1^\Theta,T_2^\Theta) \ar[d] \\
\{*\} \ar[r]_{f} & \mathsf{Fun}_{\infty\text{-}\mathbf{Cat}_{pr}^{\otimes}}(T_1,T_2),
}$$ where $$\mathsf{Fun}^{R, adj}_{/\mathsf{CAlg}(T_1)}(\Theta\text{-}\mathsf{CAlg}(T_2),\Theta\text{-}\mathsf{CAlg}(T_1))  \subset \mathsf{Fun}^{R}_{/\mathsf{CAlg}(T_1)}(\Theta\text{-}\mathsf{CAlg}(T_2),\Theta\text{-}\mathsf{CAlg}(T_1))$$ is the full sub-simplicial set of right adjoint functors $u_*$ making the square from Lemma [\[l-3\]](#l-3){reference-type="ref" reference="l-3"} commute and left adjointable.
:::

::: rmk
[]{#r-1-2 label="r-1-2"} The $\infty$-category $\mathsf{Fun}^R_{/\mathsf{CAlg}(T_1)}(\Theta\text{-}\mathsf{CAlg}(T_2),\Theta\text{-}\mathsf{CAlg}(T_1))$, and hence the fiber of $f$, is automatically an $\infty$-groupoid because the forgetful $\infty$-functor $\Theta\text{-}\mathsf{CAlg}(T_1) \to \mathsf{CAlg}(T_1)$ is conservative.
:::
