---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-015-018-ribbon-quantum-groupoids
section_title: "Ribbon quantum groupoids"
section_number: 0.18
pages: 20-21
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.947
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
::: definition
[]{#Ribbon WHA label="Ribbon WHA"} A ribbon quantum groupoid is a quasitriangular quantum groupoid with an invertible central element $\nu\in H$ such that $$\Delta(\nu) = {\mathcal R}_{21}{\mathcal R}(\nu\otimes \nu) \quad\mbox{and}\quad S(\nu)=\nu.$$ The element $\nu$ is called a *ribbon element* of $H$.
:::

For an object $V$ of $\mbox{Rep}(H)$ we define the twist $\theta_V :V\to V$ to be the multiplication by $\nu$ : $$\theta_V(v) =\nu\cdot v, \quad v\in V.$$

::: proposition
[]{#twist label="twist"} Let $(H, {\mathcal R},\nu)$ be a ribbon quantum groupoid. The family of homomorphisms $\{\theta_V\}_V$ defines a twist in the braided monoidal category $\mbox{Rep}(H)$ compatible with duality. Conversely, if $\theta_V(v) =\nu\cdot v$ is a twist in $\mbox{Rep}(H)$, then $\nu$ is a ribbon element of $H$.
:::

::: proof
*Proof.* Since $\nu$ is an invertible central element of $H$, the homomorphism $\theta_V$ is an $H$-linear isomorphism. The twist identity follows from the properties of $\nu$ : $$c_{W,V}c_{V,W}(\theta_V\otimes\theta_W)(x) =
{\mathcal R}_{21}{\mathcal R}(\nu\cdot x^{(1)}\otimes \nu\cdot x^{(2)}) = \Delta(\nu)\cdot x
= \theta_{V\otimes W}(x),$$ for all $x =x^{(1)}\otimes x^{(2)}\in V\otimes W$. Clearly, the identity ${\mathcal R}_{21}{\mathcal R}(\nu\otimes \nu) =\Delta(\nu)$ is equivalent to the twist property. It remains to prove that $$(\theta_V \otimes \mbox{id}_{V^*})b_V(z) = (\mbox{id}_V \otimes \theta_{V^*})b_V(z),$$ for all $z\in H_t$, i.e., that $$\sum_i\,\nu z_{(1)}\cdot \gamma^i \otimes z_{(2)}\cdot g_i =
\sum_i\,z_{(1)}\cdot \gamma^i \otimes \nu  z_{(2)}\cdot g_i,$$ where $\sum_i\,\gamma^i \otimes g_i$ is the canonical element in $V^*\otimes V$. Evaluating the first factors of the above equality on an arbitrary $v\in V$, we get the equivalent condition : $$\sum_i\,(\nu z_{(1)}\cdot \gamma^i)(v) z_{(2)}\cdot g_i =
\sum_i\, (z_{(1)}\cdot \gamma^i)(v) \nu z_{(2)}\cdot g_i,$$ which reduces to $z_{(2)}S(\nu z_{(1)})\cdot v = S(z_{(1)})\nu z_{(2)}\cdot v$. The latter easily follows from the centrality of $\nu=S(\nu)$ and properties of $H_t$. ◻
:::

::: proposition
[]{#ribbon category label="ribbon category"} The category $\mbox{Rep}(H)$ is a ribbon category if and only if $H$ is a ribbon quantum groupoid.
:::

::: proof
*Proof.* Follows from Propositions [\[monoidal with duality\]](#monoidal with duality){reference-type="ref" reference="monoidal with duality"}, [\[braiding\]](#braiding){reference-type="ref" reference="braiding"}, and [\[twist\]](#twist){reference-type="ref" reference="twist"}. ◻
:::

For any endomorphism $f$ of the object $V$, we define, following [@T], I.1.5, its *quantum trace* $$\label{q1-trace}
\mbox{tr}_q(f)=d_V c_{V,V^*}(\theta_Vf \otimes \mbox{id}_{V^*})b_V$$ with values in $\mbox{End}(H_t)$ and the *quantum dimension* of $V$ by $\dim_q(V)=\mbox{tr}_q(id_V)$.

::: corollary
[]{#quantum trace label="quantum trace"} Let $(H, {\mathcal R},\nu)$ be a ribbon quantum groupoid, $f$ be an endomorphism of an object $V$ in $\mbox{Rep}(H)$. Then $$\mbox{tr}_q(f)(z) = \mbox{Tr}\,(S(1_{(1)})u\nu f)z1_{(2)},\qquad \dim_q(V)(z)=\mbox{Tr}\,(S(1_{(1)})u\nu)z1_{(2)},$$ where $\mbox{Tr}\,$ is the usual trace of endomorphism, and $u$ is the Drinfeld element.
:::

::: corollary
[]{#quantum trace for connected WHA label="quantum trace for connected WHA"} Let $k$ be algebraically closed. If the trivial $H$-module $H_t$ is irreducible (which happens exactly when $H_t \cap Z(H) = k$, i.e., when $H$ is connected ([@N1], 3.11, [@BNSz], 2.4), then $\mbox{tr}_q(f)$ and $dim_q(V)$ are scalars: $$\label{q-trace}
\mbox{tr}_q(f) = (\dim H_t)^{-1}\ \mbox{Tr}\,(u\nu f),\qquad 
\dim_q(V) = (\dim H_t)^{-1} \mbox{Tr}\,(u\nu).$$
:::

::: proof
*Proof.* Any endomorphism of an irreducible module is the multiplication by a scalar, therefore, we must have $\mbox{Tr}\,(S(1_{(1)})u\nu f)1_{(2)} = \mbox{tr}_q(f) 1$. Applying the counit to both sides and using that $\varepsilon(1) = \dim H_t$, we get the result. ◻
:::
