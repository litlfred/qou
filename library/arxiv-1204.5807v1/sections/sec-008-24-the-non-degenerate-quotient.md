---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-008-24-the-non-degenerate-quotient
section_title: "The non-degenerate quotient"
section_number: 2.4
pages: 8-11
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.941
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect examples."
---
[]{#subsec:nondeg-quotient label="subsec:nondeg-quotient"}

Let ${\mathcal C}$ be an additive $\Bbbk$-linear spherical category with $\operatorname{End}({\bf 1})\simeq \Bbbk$. For any two objects $X, Y$ in ${\mathcal C}$ there is a bilinear pairing $$\begin{aligned}
\Theta: \operatorname{Hom}_{{\mathcal C}}(X, Y) \times \operatorname{Hom}_{{\mathcal C}}(Y, X) &\to \Bbbk, & \Theta (fg) &= \operatorname{tr}_L(fg) = \operatorname{tr}_R(gf);
\end{aligned}$$ ${\mathcal C}$ is non-degenerate if $\Theta$ is, for any $X,Y$. By [@BaW-adv Theorem 2.9], see also [@T-ijm], any additive spherical category ${\mathcal C}$ gives rise a factor category $\underline{{\mathcal C}}$, with the same objects[^1] as ${\mathcal C}$ and morphisms $\operatorname{Hom}_{\underline{{\mathcal C}}}(X, Y) := \operatorname{Hom}_{{\mathcal C}}(X, Y)/\mathcal{J}(X,Y)$, $X,Y \in {\mathcal C}$, where $$\begin{aligned}
\mathcal{J}(X,Y) &= \{f \in  \operatorname{Hom}_{{\mathcal C}}(X, Y): \operatorname{tr}_L(fg) = 0, \forall g\in  \operatorname{Hom}_{{\mathcal C}}(Y, X) \}.
\end{aligned}$$ The category $\underline{{\mathcal C}}$ is an additive non-degenerate spherical category, but it is not necessarily abelian, even if ${\mathcal C}$ is abelian. Clearly, the quantum dimensions in $\operatorname{Rep}H$ and $\operatorname{\underline{Rep}}H$ are the same. See [@Kn] for a general formalism of tensor ideals, that encompasses the construction above.

We now give more information on $\operatorname{\underline{Rep}}H$ following [@BaW-adv Proposition 3.8]. Let us first point out some precisions on the terminology used in the literature on additive categories, see e. g. [@harada] and references therein. We shall stick to this terminology in what follows. Let ${\mathcal C}$ be an additive $k$-linear category, where $k$ is an arbitrary field.

-   ${\mathcal C}$ is *semisimple* if the algebras $\operatorname{End}(X)$ are semisimple for all $X\in {\mathcal C}$.

-   An object $X$ is *minimal*[]{#page:minimal label="page:minimal"} if any monomorphism $Y \to X$ is either 0 or an isomorphism; hence $\operatorname{End}(X)$ is a division algebra over $k$.

-   ${\mathcal C}$ is *completely reducible* if every object is a direct sum of minimal ones.

Beware that in more recent literature in topology (where it is assumed that $k = \Bbbk$), an object $S$ is said to be *simple* when $\operatorname{End}(S) \simeq \Bbbk$; and '${\mathcal C}$ is *semisimple*' means that every object in ${\mathcal C}$ is a direct sum of simple ones. For instance, if ${\mathcal C}= {{A} {\text -}\operatorname{mod}}$, $A$ an algebra, then a minimal object in ${\mathcal C}$ is just a a simple $A$-module; then $\operatorname{End}(S)\cong \Bbbk$ by the Schur Lemma. But it is well-known that the converse is not true.

::: Ex
Let $H = \Bbbk\langle
x,g\vert x^2, g^2 -1, gx + xg\rangle$ be the Sweedler Hopf algebra. $H$ has two simple modules, both one dimensional, namely the trivial $V^+$ and $V^-$, where $g$ acts as $-1$. Consider the non-trivial extension $V^{\pm}\in\operatorname{Ext}_H^1(V^-,V^+)$, that is $V^{\pm}=\Bbbk v \oplus \Bbbk w$ with action $$\begin{aligned}
&g\cdot v=v, &&g\cdot w=-w, &&  x\cdot v=w, &&  x\cdot w =0.
\end{aligned}$$ Then $V^{\pm}$ is not simple and $\operatorname{End}_H(V^{\pm})\cong \Bbbk$. It is easy to see that the indecomposable $H$-modules are $V^+$, $V^-$, $V^{\pm}$ and $V^{\mp} := (V^{\pm})^*$; hence $\operatorname{\underline{Rep}}H \simeq \operatorname{Rep}{\mathbb Z}/2$ by Step [\[le:caracterizacion de los simples\]](#le:caracterizacion de los simples){reference-type="ref" reference="le:caracterizacion de los simples"} of the proof of Theorem [\[prop:repoH-ss\]](#prop:repoH-ss){reference-type="ref" reference="prop:repoH-ss"} below. Also, notice that in $\operatorname{Rep}H$ it is not true that all endomorphism algebras are semisimple (just take the regular representation); and, related to this, that $\operatorname{Hom}_{H} (V^{\mp}, V^{\pm})  \neq 0$.
:::

However, the converse above is true when the category is semisimple.

::: Rem
[]{#obs:harada label="obs:harada"} [@harada 1.1, 1.3] Let ${\mathcal C}$ be a semisimple additive $k$-linear category, where $k$ is an arbitrary field.

1.  If $\alpha: V \to W$ is not zero, then there exists $\beta,\gamma: W\to V$ such that $\beta\alpha \neq 0$, $\alpha\gamma \neq 0$. If $\operatorname{Hom}_{{\mathcal C}}(V,W) =0$, then $\operatorname{Hom}_{{\mathcal C}}(W, V) =0$.

2.  If $V\in{\mathcal C}$ and $\operatorname{End}(V)$ is a division ring, then $V$ is minimal.

3.  If $V, W\in{\mathcal C}$ are minimal and non-isomorphic, then $\operatorname{Hom}_{{\mathcal C}}(V, W) =0$.
:::

::: proof
*Proof.* (a) Assume that $\operatorname{Hom}_{{\mathcal C}}(W, V)\alpha =0$. Set $U = V\oplus W$; then $\operatorname{End}_{{\mathcal C}}U \alpha$ is a nilpotent left ideal of $\operatorname{End}_{{\mathcal C}}U$, hence it is 0.

\(b\) Let $W\neq0$ and $f\in\operatorname{Hom}(W,V)$ be a monomorphism. Since $f\neq0$, $\operatorname{Hom}(V,W)\neq0$ by (a). Since $\operatorname{End}(V)$ is a division ring, the map $f\circ-: \operatorname{Hom}(V,W) \to \operatorname{End}(V)$ is surjective. Therefore there exists $g\in\operatorname{Hom}(V,W)$ such that $f\circ g=\operatorname{id}_V$. On the other hand, the map $\operatorname{End}(W)\rightarrow\operatorname{Hom}(W,V)$, $\tilde{h}\mapsto f\circ\tilde{h}$ is injective. Hence $g\circ f=\operatorname{id}_W$ since $f\circ(g\circ f)=f\circ\operatorname{id}_W$. Thus $W\simeq V$. (c) follows from (a) at once. ◻
:::

If $H$ is a spherical Hopf algebra, then we denote by $\operatorname{Indec}_q H$ the set of isomorphism classes of indecomposable finite-dimensional $H$-modules with non-zero quantum dimension.

::: Thm
[]{#prop:repoH-ss label="prop:repoH-ss"} [@BaW-adv 3.8] Let $H$ be a spherical Hopf algebra with pivot $\omega$. Then the non-degenerate quotient $\operatorname{\underline{Rep}}H$ is a completely reducible spherical tensor category, and $\operatorname{Irr}\operatorname{\underline{Rep}}H$ is in bijective correspondence with $\operatorname{Indec}_q H$.
:::

By Remark [\[obs:harada\]](#obs:harada){reference-type="ref" reference="obs:harada"}, 'completely reducible' becomes what is called semisimple in the recent literature.

::: proof
*Proof.* The crucial step is to show that $\operatorname{\underline{Rep}}H$ is semisimple.

::: step
[]{#step:baw-ss label="step:baw-ss"} [@BaW-adv 3.7] The algebra $\operatorname{End}_{\operatorname{\underline{Rep}}H} (X)$ is semisimple for any $X$ in $\operatorname{\underline{Rep}}H$.
:::

Indeed, the Jacobson radical $J$ of $\operatorname{End}_{H}(X)$ is contained in ${\mathcal J}(X,X)$. For, if $\vartheta \in J$, then $\vartheta\omega$ is nilpotent, hence $\operatorname{tr}_L(\vartheta) = \operatorname{tr}_V(\vartheta\omega) = 0$.

As a consequence of Step [\[step:baw-ss\]](#step:baw-ss){reference-type="ref" reference="step:baw-ss"} and Remark [\[obs:harada\]](#obs:harada){reference-type="ref" reference="obs:harada"}, $X\in \operatorname{\underline{Rep}}H$ is minimal if and only if $\operatorname{End}_{\operatorname{\underline{Rep}}H}(X) \simeq \Bbbk$, that is if and only if it is simple. Also, $\operatorname{Hom}_{\operatorname{\underline{Rep}}H} (S, T)  = 0$, for $S,T\in \operatorname{\underline{Rep}}H$ simple non-isomorphic.

::: step
[]{#le:caracterizacion de los simples label="le:caracterizacion de los simples"} $V$ is a simple object in $\operatorname{\underline{Rep}}H$ iff there exists $W\in\operatorname{Rep}H$ indecomposable with $\operatorname{qdim}W\neq0$ which is isomorphic to $V$ in $\operatorname{\underline{Rep}}H$.
:::

Assume that $W\in\operatorname{Rep}H$ is indecomposable. If $f\in\operatorname{End}_H(W)$, then $f$ is either bijective or nilpotent by the Fitting Lemma. If also $\operatorname{qdim}W\neq0$, then $\operatorname{End}_{\operatorname{\underline{Rep}}H}(W)$ is a finite dimensional division algebra over $\Bbbk$, necessarily isomorphic to $\Bbbk$. Now, assume that $V$ is a simple object in $\operatorname{\underline{Rep}}H$. Let $\pi\in\operatorname{End}_H(V)$ be a lifting of $\operatorname{id}_V=1\in\operatorname{End}_{\operatorname{\underline{Rep}}H}(V)\simeq\Bbbk$. We can choose $\pi$ to be a primitive idempotent. Then the image $W$ of $\pi$ is indecomposable and $\pi_{|W}$ induces an isomorphism between $W$ and $V$ in $\operatorname{\underline{Rep}}H$. Again by the Fitting Lemma, $\operatorname{End}_H(W)\simeq\Bbbk\pi_{|W}\oplus \operatorname{Rad}\operatorname{End}_H(W)$. Hence $\operatorname{qdim}W\neq0$ since $\pi$ is a lifting of $\operatorname{id}_V\in\operatorname{End}_{\operatorname{\underline{Rep}}H}(V)$.

::: step
[]{#step:harada-ss-complred label="step:harada-ss-complred"} Let $V, W\in\operatorname{Rep}H$ indecomposable with $\operatorname{qdim}V\neq0$, $\operatorname{qdim}W\neq0$, which are isomorphic in $\operatorname{\underline{Rep}}H$. Then $V\simeq W$ in $\operatorname{Rep}H$.
:::

Let $f\in \operatorname{Hom}_H(V, W)$ and $g\in \operatorname{Hom}_H(W, V)$ such that $gf = \operatorname{id}_V$ in $\operatorname{\underline{Rep}}H$; that is $$\begin{aligned}
\label{eq:step3-aux}
\operatorname{tr}_V (\vartheta(gf - \operatorname{id}) \omega) &= 0 & \text{for every }\vartheta\in \operatorname{End}_H(V).
\end{aligned}$$ Since $V$ is indecomposable, $gf$ is invertible in $\operatorname{End}(V)$, or otherwise [\[eq:step3-aux\]](#eq:step3-aux){reference-type="eqref" reference="eq:step3-aux"} would fail for $\vartheta = \operatorname{id}$. Thus $g$ is surjective and $f$ is injective. But $W$ is also indecomposable, hence $f$ is surjective and $g$ is injective, and both are isomorphisms.

To finish the proof of the statement about the irreducibles, observe that an indecomposable $U\in \operatorname{Rep}H$ with $\operatorname{qdim}U =0$ satisfies $U\simeq 0$ in $\operatorname{\underline{Rep}}H$. Since any $M\in \operatorname{Rep}H$ is a direct sum of indecomposables, we see that $M$ is isomorphic in $\operatorname{\underline{Rep}}H$ to a direct sum of indecomposables with non-zero quantum dimension.

Finally observe that the additive $\Bbbk$-linear category $\operatorname{\underline{Rep}}H$, being isomorphic to a direct sum of copies of $\operatorname{Vec}\Bbbk$, is abelian. ◻
:::

Here is a consequence of the Theorem: let $\iota: V \hookrightarrow W$ be a proper inclusion of indecomposable $H$-modules with $\operatorname{qdim}V\neq0$, $\operatorname{qdim}W\neq0$. Then $\iota \in {\mathcal J}(V,W)$.

::: Rem
[]{#rem:GK label="rem:GK"} From Theorem [\[prop:repoH-ss\]](#prop:repoH-ss){reference-type="ref" reference="prop:repoH-ss"} we see the relation between the constructions of [@BaW-adv] and [@GK-inv]. For, let ${\mathcal C}= \operatorname{Rep}H$ and let ${\mathcal C}^0$, resp. ${\mathcal C}^\perp$, be the full subcategory whose objects are direct sums of indecomposables with quantum dimension $\neq 0$, resp. 0. Then $\operatorname{\underline{Rep}}H$ is the quotient of ${\mathcal C}$ by ${\mathcal C}^\perp$ as described in [@GK-inv Section 1].
:::

Even when $H$ is finite-dimensional, $\operatorname{Irr}\operatorname{\underline{Rep}}H$ is not necessarily finite. It is then natural to look at suitable subcategories of $\operatorname{Rep}H$ that give rise to finite tensor subcategories of $\operatorname{\underline{Rep}}H$. A possibility is tilting modules, that proved to be very fruitful in the case of quantum groups at roots of one. We shall discuss this matter in Section [\[sec:titling2\]](#sec:titling2){reference-type="ref" reference="sec:titling2"}.

[^1]: This is a bit misleading, as non-isomorphic objects in ${\mathcal C}$ may became isomorphic in $\underline{{\mathcal C}}$.
