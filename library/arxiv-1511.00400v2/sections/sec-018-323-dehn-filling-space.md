---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-018-323-dehn-filling-space
section_title: "Dehn filling space"
section_number: 3.2.3
pages: 22-23
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 1.0
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
[]{#sec:Dehnfilling label="sec:Dehnfilling"}

Again let $M^3$ be an oriented, finite volume hyperbolic manifold with one cusp. Consider the peripheral torus $T^2$, which is the boundary of a compact core of $M^3$. Choose a frame on the peripheral torus $T^2$, i.e. two simple closed curves that generate $\pi_1 T^2$, denote this frame by $\{m,l\}$. The notation suggests that the canonical choice for a knot exterior is the pair meridian-longitude.

A *Dehn filling* on $M^3$ is the result of gluing a solid torus $D^2\times S^1$ to a compact core $M^3$ along the boundary. Up to homeomorphism, this manifold depends only on the (unoriented) homology class in $T^2$ of the meridian, i.e. the curve $\partial D^2\times \{*\}$. This curve is written as $\pm (p\, m+q\, l)$, and the Dehn filling is denoted by $M^3_{p/q}$.

When $\vert p\vert +\vert q\vert$ is sufficiently large, by Thurston's theorem $M_{p/q}$ is hyperbolic. To prove it, he introduces the *Thurston's parameters* of the Dehn filling space, by writing, for representations close to the holonomy of the complete hyperbolic structure, $$\label{eqn:u}
\rho(m)=\pm \begin{pmatrix}
         e^{u/2} & 1 \\ 0 & e^{-u/2}
        \end{pmatrix}
        \qquad
 \rho(l)   =  \pm \begin{pmatrix}
         e^{v/2} & f(u) \\ 0 & e^{-v/2}
        \end{pmatrix}$$ with $u,v\in\mathbb{C}$ in a neighborhood of the origin. For the holonomy of the complete structure, $u=v=0$ and write $$\operatorname{cs}= \operatorname{cs}(l,m)=f(0)\in \mathbb{C}-\mathbb{R}.$$

::: definition
[]{#def:cs label="def:cs"} The parameter $u\in U \subset \mathbb{C}$ as above is called the *Thurston parameter* and $\operatorname{cs}= \operatorname{cs}(l,m)\in \mathbb{C}-\mathbb{R}$ the *cusp shape* of the complete structure.
:::

The Thurston parameter $u$ is in fact a parameter of a double branched covering of a neighborhood of the lift of the holonomy $\varrho$, as the local parameter of $X_0(M^3)$ is $\operatorname{tr}(\rho(m))= \pm 2 \cosh\frac{u}{2}$. For the complete structure, the peripheral group acts as a lattice on a horosphere, that we view as $\mathbb{C}$. Up to affine equivalence, this lattice is given by $m\mapsto 1$, $l\mapsto \operatorname{cs}$.

::: lemma
There exists a (standard) neighborhood of the origin $U\subset \mathbb{C}$ such that:

(a) The map $U\to X_0(M^3)$ such that $u\mapsto \chi_\rho$, where $\rho$ is as in [\[eqn:u\]](#eqn:u){reference-type="eqref" reference="eqn:u"} is a double branched covering of a neighborhood in $X_0(M^3)$ of the character of the holonomy of the complete structure.

(b) $v$ is an analytic odd function on $u$ that satisfies $$v(u)=\operatorname{cs}u+ O(u^3).$$

(c) $f(u)=\sinh(v)/\sinh(u)$.
:::

The *generalized Dehn filling coefficients* are the $(p,q)\in\mathbb{R}^2\cup\{\infty\}$ such that $$\label{eqn:pq}
p\,u+q\, v=2\pi i$$ when $u\neq 0$ and $\infty$ when $u=0$.

::: thm
[@ThurstonBook; @NZ85] The generalized Dehn filling coefficients define a homeomorphism between $U$ and a neighborhood of $\infty$ in $S^2=\mathbb{R}^2\cup\{\infty\}$. If a pair of coprime integers $(p,q)\in\mathbb{Z}^2$ lies in the image of this homeomorphism, then $M^3_{p/q}$ is hyperbolic, with holonomy whose restriction to $M^3$ satisfies [\[eqn:pq\]](#eqn:pq){reference-type="eqref" reference="eqn:pq"}.
:::

We are interested in properties of $M^3_{p/q}$.

::: thm
$$\operatorname{vol}(M^3_{p/q})=\operatorname{vol}(M^3)-\pi^2\frac{\operatorname{Im}(\operatorname{cs})}{|p+\operatorname{cs}q|^2}+ O\left(\frac{1}{|p+\operatorname{cs}q|^4 }\right).$$
:::

We are also interested in the complex length of the soul of the solid torus added by Dehn filling, which is a short geodesic. Let $r$ and $s$ be integers satisfying $p\, s-q\, r=1$, this complex length is $r\, u+s\, v$. A straightforward computation yields [@Memoirs]:

::: remark
[]{#rem:length label="rem:length"} The complex length of the core of the solid torus $M_{p/q}^3$ is $$r\, u+s\, v= 2\pi i\frac{r}{p}+ \frac{v}{p}= 2\pi i\frac{s}{q}+ \frac{u}{q}$$
:::

Given a spin structure $\sigma$ on $M^3$, it may extend or not to $M_{p,q}^3$. It is easy to give a characterization using the bijection of Proposition [\[prop:spin\]](#prop:spin){reference-type="ref" reference="prop:spin"}.

::: lemma
[@MFP14] []{#lemma:extendspin label="lemma:extendspin"} A spin structure $\sigma$ on $M$ extends to $M_{p,q}$ iff the corresponding lift of the holonomy $\varrho_{\sigma}$ (for the complete structure on $M^3$) satisfies $$\operatorname{tr}(\varrho_{\sigma}( p\, m+ q\, l ))=-2.$$
:::
