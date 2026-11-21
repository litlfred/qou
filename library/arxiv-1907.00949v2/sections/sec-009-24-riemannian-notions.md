---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-009-24-riemannian-notions
section_title: "Riemannian notions"
section_number: 2.4
pages: 7-7
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.99
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:Riem label="sec:Riem"}

Although not specific to homogeneous or geodesic orbit spaces, we state the famous Hopf--Rinow theorem [@CE2008 Theorem $1.8$] and recall the definitions of Riemannian gradient and Hessian [@Helgason1978; @KN1969; @Boothby1975] below for easy reference.

::: theorem
[]{#thm:Hopf--Rinow label="thm:Hopf--Rinow"} Let $(M,g)$ be a connected Riemannian manifold. Then the following statements are equivalent:

1.  closed and bounded subsets of $M$ are compact;

2.  $M$ is a complete metric space;

3.  $M$ is geodesically complete, i.e., the exponential map $\exp_x: T_xM \to M$ is defined on the whole $T_xM$ for all $x\in M$.

Furthermore, any one of these conditions guarantees that any two points $x,y$ on $M$ can be connected by a distance minimizing geodesic on $M$.
:::

In the following we will write $\mathfrak{X}(M)$ for the set of all smooth vector fields on $M$.

::: definition
[]{#def:gH label="def:gH"} Let $(M,g)$ be a Riemannian manifold. Let $f:M \to \mathbb{R}$ be a smooth function. The *Riemannian gradient* of $f$, denoted $\nabla f$, is defined by $$g(\nabla f,V) = V(f),$$ for any $V \in \mathfrak{X}(M)$. The *Riemannian Hessian* of $f$, denoted $\nabla^2 f$, is defined by $$(\nabla^2 f)(U,V) = g\bigl(\nabla_U(\nabla f), V\bigr),$$ where $U,V \in \mathfrak{X}(M)$ and $\nabla_U V$ is the *covariant derivative* of $V$ along $U$, which is uniquely determined by the Riemannian metric $g$.
:::

By their definitions, $\nabla f$ is a smooth vector field and $\nabla^2 f$ is a smooth field of *symmetric bilinear forms*. In particular, $\nabla^2 f$ is uniquely determined by its values at points of the form $(V,V)$ over all $V\in \mathfrak{X}(M)$ because of bilinearity and symmetry, i.e., $$\label{eq:polar}
\nabla^2f(U,V) = \frac{1}{2} \bigl(\nabla^2f (U + V, U + V)  -\nabla^2f(U,U) - \nabla^2f(V,V) \bigr),$$ for any $U,V  \in \mathfrak{X}(M)$. Definition [\[def:gH\]](#def:gH){reference-type="ref" reference="def:gH"} is standard but not as useful for us as a *pointwise* definition --- the Riemannian gradient $\nabla f(x)$ and Riemannian Hessian $\nabla^2f(x)$ at a point $x\in M$ is given by $$\label{eq:gH}
g_x(\nabla f(x),X) = \frac{d f\bigl(\exp(tX)\bigr)}{dt}\Bigr|_{t=0},\qquad 
\nabla^2 f(x) (X,X) =\frac{d^2 f\bigl(\exp(tX)\bigr)}{dt^2}\Bigr|_{t=0},$$ where $\exp(tX)$ is the geodesic curve emanating from $x$ in the direction $X \in T_x M$. We may obtain [\[eq:gH\]](#eq:gH){reference-type="eqref" reference="eq:gH"} by Taylor expanding $f\bigl(\exp(tX)\bigr)$.

Given a specific function $f$, one may express [\[eq:gH\]](#eq:gH){reference-type="eqref" reference="eq:gH"} in terms of *local coordinates* on $M$ but in general there are no global formulas for $\nabla f(x)$ and $\nabla^2f(x)$, and without which it would be difficult if not impossible to do optimization on $M$. We will see in Section [\[sec:gH\]](#sec:gH){reference-type="ref" reference="sec:gH"} that when $M$ is a flag manifold, then [\[eq:gH\]](#eq:gH){reference-type="eqref" reference="eq:gH"} may be expressed globally in terms of extrinsic coordinates.
