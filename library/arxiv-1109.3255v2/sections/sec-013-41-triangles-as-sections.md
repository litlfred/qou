---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-013-41-triangles-as-sections
section_title: "Triangles as sections"
section_number: 4.1
pages: 32-37
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.93
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:triangles-sections label="sec:triangles-sections"}

Let $q_1 \in HF^0(L(0),L(n))$ and $q_2 \in HF^0(L(n),L(n+m))$ be two degree zero morphisms whose Floer product $\mu^2(q_2,q_1)$ we wish to compute. Suppose that $p \in HF^0(L(0),L(n+m))$ contributes to this product. Let $S$ denote a disk with three boundary punctures, and a complex structure that is allowed to vary. To find the coefficient of $p$ in $\mu^2(q_2,q_1)$, we count pseudo-holomorphic triangles, that is, pseudo-holomorphic maps $u: S \to X(B)$ that send the punctures to $q_1,q_2,p$ and the boundary components to $L(0),L(n),L(n+m)$. Various authors have studied the construction of such invariants; we follow the theory as developed by Seidel in [@seidel-book; @seidel-les].

Because we want to make contact with the theory of pseudo-holomorphic sections of Lefschetz fibrations, we need to import the setup from [@seidel-les §2.1]. Let $\pi : E \to B$ be a exact symplectic Lefschetz fibration. We choose primitive $\theta$ for the symplectic form $\omega$ such that the Liouville vector field $Z$ defined on the fiber $M$ by $\iota_Z(\omega|_M) = \theta|_M$ points outward along the boundary of $M$. The flow of $Z$ defines a collar $[-\epsilon,0]\times M \to M$, and we let $\sigma$ be the function on a neighborhood of $\partial M$ given by projection to the $[-\epsilon,0]$ factor. We pick an almost complex structure $j$ on the base of the fibration, we always consider an almost complex structure $J$ on the total space which is *compatible relative to $j$*, meaning

1.  $J$ is integrable in a neighborhood of each critical point,

2.  $\pi$ is a $(J,j)$-holomorphic map,

3.  For each fiber $E_z$, the form $\omega(\cdot, J\cdot)|TE_z$ is symmetric and positive definite

4.  on a neighborhood of the horizontal boundary of $E$, $J$ satisfies $\theta \circ J = d(e^\sigma)$.

Later on, in Section [\[sec:horiz-sections\]](#sec:horiz-sections){reference-type="ref" reference="sec:horiz-sections"}, we will also need to consider $J$ which are *horizontal*, meaning that $J$ preserves the horizontal subspaces of the symplectic connection. Once we extend the Lagrangian boundary condition Section [\[sec:extend-fiber\]](#sec:extend-fiber){reference-type="ref" reference="sec:extend-fiber"} so that our Lagrangians are compact in each fiber, these conditions imply that the curves we wish to count lie in a compact subset disjoint from the horizontal boundary [@seidel-les Lemma 2.2]. The second condition is particularly useful because it allows us to study pseudo-holomorphic curves by projecting them to the base of the fibration.

Consider the projection of such a triangle to the base by $w : X(B)\to
X(I)$. This yields a 2-chain on the base with boundary on the corresponding base paths $\ell(0),\ell(n),\ell(n+m)$ with corners at the points $w(q_1),w(q_2),w(p)$. This projection is not necessarily embedded, so the next step is to pass to the universal cover of the base. Let $\tilde{X}(I)$ denote infinite strip which is the universal cover of the annulus, and let $\tilde{w}: \tilde{X}(B) \to
\tilde{X}(I)$ denote the induced fibration. We denote by $\pi:
\tilde{X}(B) \to X(B)$ the covering map. When drawing pictures in the base $\tilde{X}(I)$, we can represent it as $[-1,1] \times \R$, with the infinite direction drawn vertically. With this convention, the path $\ell(d)$ lifts to a $\Z$-family of paths which have slope $-d$.

Figure [1](#fig:universal-cover){reference-type="ref" reference="fig:universal-cover"} shows the universal cover of $X(I)$, with the base paths for $L(0)$, $L(1)$, and $L(2)$.

![The universal cover of $X(I)$.](universal-cover){#fig:universal-cover width="2in"}

The choice of lift of $q_1$ determines a lift of $L(0)$ and $L(n)$, which then determines a lift of $q_2$ and of $L(n+m)$, which in turn determines where the lift of any $p$ must lie. By looking at the slopes of the base paths $\ell(0),\ell(n),\ell(n+m)$ involved, we obtain the following proposition:

::: proposition
In the terminology of Definition [\[def:indexing\]](#def:indexing){reference-type="ref" reference="def:indexing"}, Suppose that $q_1 =
  q_{a,i}$ lies in the fiber indexed by $a/n$, and that $q_2 =
  q_{b,j}$ lies in the fiber indexed by $b/m$. Then any $p$ contributing to the product is $q_{a+b,h}$ for some $h$, that is, it lies in the fiber indexed by $(a+b)/(n+m)$
:::

We can rephrase this proposition as saying that we can introduce a second grading on $HF^*(L(d),L(d+n))$ where $HF^{*,a}(L(d),L(d+n))$ is generated by $q_{a,i}$ for $i \in \{0,1,\dots\left\lfloor\frac{n-|a|}{2}\right\rfloor\}$, and that $\mu^2$ respects this grading.

We must now consider two cases: either the input generators $q_1$ and $q_2$ lie in different fibers of $w$, or they lie in the same fiber. The rest of this section is devoted to case where $q_1$ and $q_2$ lie in different fibers, which is the more difficulty one. In the case where $q_1$ and $q_2$ lie in the same fiber, the preceding proposition says that the output $p$ must also lie in the same fiber. This means that we can compute the contribution of $p$ to $\mu^2(q_2,q_1)$ by counting triangles that lie entirely in this fiber, since the projection of such a triangle to the base must be constant. We will employ an alternative strategy where we perturb one of the base paths, say $\ell(0)$, by a small amount so that there are no points where all three base paths intersect. This forces the triangle in the fiber to spread out over a small triangle in the base, so that in particular it cannot be constant. With this proviso, the arguments in this section apply without exception.

Now we show that any triangles contributing to the product of interest are sections of the Lefschetz fibration $\tilde{w}: \tilde{X}(B)\to
\tilde{X}(I)$:

::: proposition
[]{#prop:triangles-sections label="prop:triangles-sections"} Let $u: S \to X(B)$ be a pseudo-holomorphic triangle contributing to the component of $p$ in $\mu^2(q_2,q_1)$, such that $q_1$ and $q_2$ do not lie in the same fiber of $w$. Then there is a triangle $T$ in $\tilde{X}(I)$ bounded by appropriate lifts of $\ell(0),\ell(n)$ and $\ell(n+m)$, a holomorphic isomorphism $\tau: S\to T$, and a pseudo-holomorphic section $s :T \to \tilde{X}(B)$, such that $u = \pi\circ s \circ \tau$.

Conversely, any pseudo-holomorphic section $s: T \to \tilde{X}(B)$ with boundary on $L(0),L(n),L(n+m)$ which maps the corners to $q_2,
  q_1, p$ contributes to the coefficient of $p$ in $\mu^2(q_2,q_1)$.
:::

::: proof
*Proof.* Since $u : S \to X(B)$ is a map from a simply-connected domain, there is a lift $\tilde{u}: S \to \tilde{X}(B)$. Since $q_1$ and $q_2$ are not in the same fiber, the image of $u$ cannot be contained entirely within a fiber. The triangle $T$ and the lifts of the $\ell(d)$ are determined by the considerations from the previous proposition. Clearly $\tilde{w}\circ \tilde{u}$ defines a 2-chain in $\tilde{X}(I)$, which by maximum principle is supported on $T$. By positivity of intersection with the fibers of $\tilde{w}$, all components of this 2-chain are positive, and the map $\tilde{w}\circ
  \tilde{u} : S\to T$ is a ramified covering. However, if the degree were greater than one, then $\partial S$ would have to wind around $\ell(0),\ell(n),\ell(n+m)$ more than once, contradicting the boundary conditions we placed on the map $u$.

Since the projection $\tilde{w}: \tilde{X}(B) \to \tilde{X}(I)$ is holomorphic, the composition $\tilde{w}\circ \tilde{u}: S \to T$ is a holomorphic map which sends the boundary to the boundary and the punctures to the punctures, so it is a holomorphic isomorphism, and we let $\tau$ be its inverse.

For the converse, uniformization for the disk with three boundary punctures yields a complex structure on $S$ and a map $\tau: S \to
  T$, such the composition $\tilde{u} = s \circ \tau$ is the desired triangle in $\tilde{X}(B)$. Composing this with $\pi :
  \tilde{X}(B)\to X(B)$ yields the triangle in $X(B)$. ◻
:::

::: proposition
[]{#prop:k-criticalpoints label="prop:k-criticalpoints"} Suppose $q_1= q_{a,i}$ lies in the fiber indexed by $a/n$, and $q_2
  = q_{b,j}$ in the fiber indexed by $b/m$. Then the sections in Proposition [\[prop:triangles-sections\]](#prop:triangles-sections){reference-type="ref" reference="prop:triangles-sections"} cover the critical values of the Lefschetz fibration $k$ times, where

-   $k = 0$ if $a$ and $b$ are both non-negative or both non-positive.

-   $k = \min(|a|,|b|)$ if $a$ and $b$ have different signs.
:::

::: proof
*Proof.* We identify $\tilde{X}(I)$ with $[-1,1]\times \R$. The critical values lie at the points $\{0\} \times (\Z + \frac{1}{2})$.

If $a$ and $b$ are both non-negative or both non-positive, then the triangle $T$ is entirely to one side of the vertical line $\{0\}
  \times \R$ where all the critical values lie.

Suppose $a$ and $b$ have opposite signs and $|a| \leq |b|$. Then the output point lies at $(a+b)/(n+m)$, which has the same sign as $b$. The side of $T$ corresponding to $\ell(n)$ crosses the line $\{0\}\times \R$ at $(0,a)$, while the side corresponding to $\ell(0)$ crosses at $(0,0)$, so the distance is $|a|$, and in fact the set $\{0\} \times (\Z+\frac{1}{2})$ contains $|a|$ points in this interval.

If $|b| \leq |a|$, the output point at $(a+b)/(n+m)$ has the same sign as $a$, and so we need to look at where $\ell(n+m)$ intersects the line $\{0\}\times \R$. This happens at $(0,a+b)$, and the distance to $(0,a)$ is $|b|$. ◻
:::

With the notation introduced so far, we can state the main result of our computation for $\mu^2(q_{b,j},q_{a,i})$.

::: proposition
[]{#prop:counts-summary label="prop:counts-summary"} Suppose that $q_{a,i} \in HF^0(L(0),L(n))$ and $q_{b,j} \in
  HF^0(L(n),L(n+m))$ as in Definition [\[def:indexing\]](#def:indexing){reference-type="ref" reference="def:indexing"}, and let $k$ be as in Proposition [\[prop:k-criticalpoints\]](#prop:k-criticalpoints){reference-type="ref" reference="prop:k-criticalpoints"}. Then $$\mu^2(q_{b,j},q_{a,i}) = \sum_{s=0}^k \binom{k}{s}q_{a+b,i+j+s}$$
:::

::: proof
*Proof.* This proposition is the combination of Propositions [\[prop:TQFT-gluing\]](#prop:TQFT-gluing){reference-type="ref" reference="prop:TQFT-gluing"}, [\[prop:horiz-sections\]](#prop:horiz-sections){reference-type="ref" reference="prop:horiz-sections"}, [\[prop:which-output\]](#prop:which-output){reference-type="ref" reference="prop:which-output"}, [\[prop:polygon-count\]](#prop:polygon-count){reference-type="ref" reference="prop:polygon-count"}, and [\[prop:signs\]](#prop:signs){reference-type="ref" reference="prop:signs"}. ◻
:::

The proof of Proposition [\[prop:counts-summary\]](#prop:counts-summary){reference-type="ref" reference="prop:counts-summary"} is where most of the technical work of this paper is spent, and it will occupy Sections [\[sec:extend-fiber\]](#sec:extend-fiber){reference-type="ref" reference="sec:extend-fiber"}--[\[sec:signs\]](#sec:signs){reference-type="ref" reference="sec:signs"}. Sections [\[sec:extend-fiber\]](#sec:extend-fiber){reference-type="ref" reference="sec:extend-fiber"} and [\[sec:degenerated-spaces\]](#sec:degenerated-spaces){reference-type="ref" reference="sec:degenerated-spaces"} present a technique for degenerating the total space of the Lefschetz fibration to break these counts into simpler pieces. Sections [\[sec:horiz-sections\]](#sec:horiz-sections){reference-type="ref" reference="sec:horiz-sections"} and [\[sec:sections-polygon\]](#sec:sections-polygon){reference-type="ref" reference="sec:sections-polygon"} compute these pieces, and Section [\[sec:signs\]](#sec:signs){reference-type="ref" reference="sec:signs"} determines the signs.

We shall now reformulate Proposition [\[prop:counts-summary\]](#prop:counts-summary){reference-type="ref" reference="prop:counts-summary"} in algebro-geometric terms. Let $$\label{eq:homog-coord-ring}
  A = \bigoplus_{d=0}^\infty A_d = \bigoplus_{d=0}^\infty H^0(\PP^2, \cO_{\PP^2}(d)) \cong \K[x,y,z]$$ be the homogeneous coordinate ring of $\PP^2$. We write elements of $A_d
= H^0(\PP^2,\cO_{\PP^2}(d))$ as degree $d$ homogeneous polynomials in the variables $x,y,z$. Define $$\label{eq:P}
  p = xz - y^2,$$ and set, for $a \in \{-d,\dots,d\}$, $i \in \{0,\dots,\left\lfloor\frac{d-|a|}{2}\right\rfloor\}$, $$\label{eq:big-Q}
  Q_{a,i} = \left\{
  \begin{aligned}
    x^{-a}p^iy^{d+a-2i}& \quad \text{if } a \leq 0\\
    z^ap^iy^{d-a-2i} & \quad \text{if } a > 0\\
  \end{aligned} \right\} \in A_d.$$

::: proposition
[]{#prop:polynomial-algebra label="prop:polynomial-algebra"} Take $Q_{a,i} \in A_n$ and $Q_{b,j} \in A_m$, then in $A$, $$\label{eq:polynomial-algebra}
    Q_{a,i}Q_{b,j} = \sum_{s=0}^{k}\binom{k}{s} Q_{a+b,i+j+s}$$ where $k = \min(|a|,|b|)$ if $a$ and $b$ have different signs, and $k = 0$ otherwise.
:::

::: proof
*Proof.* The case where $a$ and $b$ have the same sign is obvious.

Suppose that $a \leq 0$ and $b \geq 0$, and suppose that $|a| \leq
  |b|$. Then we have $a+b \geq 0$, and $k = -a$. $$Q_{a,i}Q_{b,j} = x^{-a}p^iy^{n+a-2i}z^bp^jy^{m-b-2j} =
    z^{a+b}(xz)^kp^{i+j}y^{n+m+a-b-2(i+j)}$$ Since $xz = p + y^2$, we have $$(xz)^k = \sum_{s=0}^k \binom{k}{s}p^sy^{2(k-s)}$$ $$Q_{a,i}Q_{b,j} = \sum_{s=0}^k
    \binom{k}{s}z^{a+b}p^{i+j+s}y^{(n+m)-(a+b)-2(i+j+s)}$$ and the monomial on the right is just $Q_{a+b,i+j+s}$. The other cases are similar. ◻
:::

The operation $\mu^2$ determines a product, $q_2 \cdot q_1 =
(-1)^{|q_1|} \mu^2(q_2,q_1)$. The sign is present to connect the conventions for an $A_\infty$-category at those of a dg-category; in the case all morphisms have degree zero the sign is trivial. The following proposition states how our Lagrangian intersections give rise to a distinguished basis of the homogeneous coordinate ring $A$. From the preceding propositions, we can deduce Theorem [\[thm:triangle-products\]](#thm:triangle-products){reference-type="ref" reference="thm:triangle-products"}.

::: proposition
[]{#prop:coord-ring-iso label="prop:coord-ring-iso"} The map $\psi_{d,n}: HF^0(L(d),L(d+n)) \to A_n$ defined by $$\psi_{d,n}: q_{a,i} \mapsto Q_{a,i}$$ is an isomorphism. We have $$\psi_{d,n+m} (q_1 \cdot q_2) = \psi_{d,n}(q_1) \cdot \psi_{d+n,m}(q_2)$$
:::

::: proof
*Proof.* That $\psi_{d,n}$ is an isomorphism is because it maps a basis to a basis. The other statement is the combination of Propositions [\[prop:counts-summary\]](#prop:counts-summary){reference-type="ref" reference="prop:counts-summary"} and [\[prop:polynomial-algebra\]](#prop:polynomial-algebra){reference-type="ref" reference="prop:polynomial-algebra"}. ◻
:::

Thus the proof of Theorem [\[thm:triangle-products\]](#thm:triangle-products){reference-type="ref" reference="thm:triangle-products"} will be complete once we prove Proposition [\[prop:counts-summary\]](#prop:counts-summary){reference-type="ref" reference="prop:counts-summary"}, which in turn depends on Propositions [\[prop:TQFT-gluing\]](#prop:TQFT-gluing){reference-type="ref" reference="prop:TQFT-gluing"}, [\[prop:horiz-sections\]](#prop:horiz-sections){reference-type="ref" reference="prop:horiz-sections"}, [\[prop:which-output\]](#prop:which-output){reference-type="ref" reference="prop:which-output"}, [\[prop:polygon-count\]](#prop:polygon-count){reference-type="ref" reference="prop:polygon-count"}, and [\[prop:signs\]](#prop:signs){reference-type="ref" reference="prop:signs"}. The rest of this section is devoted to the proofs of these propositions.
