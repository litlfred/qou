---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-035-associating-2-holonomies-to-embedded-spheres
section_title: "Associating 2-holonomies to embedded spheres"
section_number: null
pages: 41-43
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.985
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#WS label="WS"}

Let ${\Gc=(\d\colon E \to G,\tr)}$ be a Lie crossed module. Let $M$ be a smooth manifold. Consider a principal $G$-bundle $P$ over $M$ with a $\Gc$-categorical connection $(\w,m)$. Consider an embedded oriented 2-sphere $\Sigma\subset M$. We want to define the categorical holonomy of $\Sigma$, which we call a *Wilson Sphere*, by analogy with Wilson loops, familiar in gauge theory.

::: Definition
Choose an orientation preserving parametrisation $$S^2 = {{\rm D}}^2 / \d {{\rm D}}^2 \ra{\f} \Sigma \subset M$$ of $\Sigma$. Let $*=\f(\d {{\rm D}}^2) \in \Sigma \subset M$. Choose $u\in P_*$, the fibre of $P$ at $*$. The categorical holonomy of $\Sigma$ is defined as: $${\Wc}_{(\w,m)}(\Sigma,\f,u)=F^2_{(\w,m,u)}(\f) \in \ker(\d) \subset E.$$
:::

The fact that the categorical holonomy ${\Wc}_{(\w,m)}(\Sigma,\f,u)$ lives in $\ker(\d) \subset E$ follows from the fact that $\d_d(\f)=\d_u(\f)=*$, and lemma [\[DDD\]](#DDD){reference-type="ref" reference="DDD"}.

::: Theorem
[]{#asd label="asd"} The categorical holonomy ${\Wc}_{(\w,m)}(\Sigma,\f,u)$ does not depend on $\f$ and $u$, up to acting by an element of $G$. Therefore, we can define a categorical holonomy ${\Wc}_{(\w,m)}(\Sigma)$ of embedded 2-spheres $\Sigma$ in $M$ (the Wilson Sphere), taking values in $E/G$. If $\Sigma^*$ is obtained from $\Sigma$ by reversing its orientation then ${\Wc}_{(\w,m)}(\Sigma^*)=\left ({\Wc}_{(\w,m)}(\Sigma)\right)^{-1}$.
:::

::: Example
Consider the $U(1)$-bundle $P^n$ over $S^2$ with Chern class $n$, where $n \in \Z$. Define a crossed module $\Gc$ given by the exponential map $\exp \colon i \R \to  U(1)$, considering the trivial action of $U(1)$ on $i\R$. Consider some connection 1-form $\w$ on $P_n$, thus $(\w,\W)$ is a categorical $\Gc$-connection on $P^n$. We will then have that $\Wc_{(\w,\W)}(S^2)= n$.
:::

::: Proof
**(Theorem [\[asd\]](#asd){reference-type="ref" reference="asd"})** The independence of ${\Wc}_{(\w,m)}(\Sigma,\f,u)$ on the choice of $u \in P_*$, up to acting by an element of $G$, follows from theorem [\[I\]](#I){reference-type="ref" reference="I"}.

Choose a different orientation preserving parametrisation ${{\rm D}}^2 / \d {{\rm D}}^2 \ra{\f'} \Sigma$ of $\Sigma$. Since both $\f$ and $\f'$ are orientation preserving, there exists a smooth 1-parameter family of embeddings $x \in [0,1] \mapsto \f_x$ connecting $\f$ and $\f'$. Here $\f_x$ is an orientation preserving parametrisation $\f_x \colon {{\rm D}}^2 / \d {{\rm D}}^2 \to \Sigma$, for each $x \in [0,1]$.

Let $q\colon [0,1] \to M$ be the map such that $q(x)=\f_x(\d ([0,1]^2)), \forall x \in  [0,1]$; therefore $* =q(0)$. Put $\G^x(t,s)\doteq \f_x(t,s),$ where $t,s,x \in [0,1]$. Therefore $\d_l(\G^x)=\d_r(\G^x)=q(x),$ for each $x \in  [0,1]$. Let also $J(t,s,x)\doteq \G^x(t,s)$, where $t,s,x \in [0,1]$.

The map $J\colon [0,1]^3 \to \Sigma \subset M$ satisfies the conditions of theorem [\[Main2\]](#Main2){reference-type="ref" reference="Main2"}. In particular $${\Wc}_{(\w,m)}(\Sigma,\f_0,u)=e_{\G^0} =e_{\G^1} ={\Wc}_{(\w,m)}(\Sigma,\f_1,\H_\w(q,1,u)),$$ since certainly $\Rank ({\EuScript{D}}_z J)\leq 2,\forall z \in [0,1]^3.$

Finally, let $\f^{-1}(x,y)=\f(1-x,y); \forall x,y \in [0,1]$. It does not follow that $\f^{-1}\circ_h \f$ is rank-2 homotopic to $*$ in a strict sense, since a homotopy connecting $\f^{-1}\circ_h \f$ with $*$ will have some singular points, as $\f$ and $\f^{-1}$ are not 2-paths, because they fail the sitting instant conditions.

Let $\g_s(t)=\f(t,s)$ and $\g_s'(t)=\f^{-1}(t,s)$, where $t,s \in[0,1]$. Let us analyse $e_{\f^{-1}}(s)$ directly. We have: $$\begin{aligned}
\frac{d}{d s} e_{\f^{-1}}(s) 
&=  e_{\f^{-1}}(s)   \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s'(t)},\t{\frac{\d}{\d s}\g_s'(t)} \right)  _{{\mathcal{H}}_\w(\g_s',t,u) } dt\\&= - e_{\f^{-1}}(s)   \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,ug_{\g_s'}) } dt
\end{aligned}$$ Therefore: $$\begin{aligned}
\frac{d}{d s} e_{\f^{-1}}(s) &= - e_{\f^{-1}}(s) \Big ( g_{\g_s'}^{-1} \tr  \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,u) } dt\Big)\\
&= - e_{\f^{-1}}(s) \Big ( \d \left (e^{-1}_{\f^{-1}}(s) \right ) \tr  \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,u) } dt\Big)\\
&= -\Big( \int_{0}^{1} m \left (\t{\frac{\d}{\d t}\g_s(t)},\t{\frac{\d}{\d s}\g_s(t)} \right)  _{{\mathcal{H}}_\w(\g_s,t,u) } dt\Big)  e_{\f^{-1}}(s).
\end{aligned}$$ The result follows from the fact that if $A(t)$ is a smooth function $[0,1] \to E$ and if $w(s)$ is a solution of $\frac{d}{d s} w(s)=w(s)A(s)$ then the smooth function $v(s)\doteq w(s)^{-1}$ is a solution of $\frac{d}{d s} v(s)=-A(s)v(s)$. In particular $e_{\f^{-1}}(1)=  e_{\f}^{-1}(1)$.
:::

Note that the previous proof uses, in an essential way, the fact that the mapping class group of $S^2$ is $\{\pm 1\}$. Therefore, it is likely that the previous theorem does not extend to an embedded surface of genus greater than zero. However, it is probable that this can be fixed if any embedded surface $\Sigma \subset M$ is assigned an equivalence class of embedding $S \to \Sigma$, where two embeddings $\f,\f'\colon S \to \Sigma$ are equivalent if $\f^{-1} \circ \f'$ is isotopic to the identity diffeomorphism. We will analyse this issue in a subsequent publication.
