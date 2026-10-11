---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-010-41-triangles-as-sections
section_title: "Triangles as sections"
section_number: 4.1
pages: 32-40
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped with a binodal cubic curve as"
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.955
---
[]{#sec:triangles-sections label="sec:triangles-sections"}

Let $q_1 \in HF^0(L(0),L(n))$ and $q_2 \in HF^0(L(n),L(n+m))$ be two degree zero morphisms whose Floer product $\mu^2(q_2,q_1)$ we wish to compute. Suppose that $p \in HF^0(L(0),L(n+m))$ contributes to this product. Let $S$ denote a disk with three boundary punctures, and a complex structure that is allowed to vary. To find the coefficient of $p$ in $\mu^2(q_2,q_1)$, we count pseudo-holomorphic triangles, that is, pseudo-holomorphic maps $u: S \to X(B)$ that send the punctures to $q_1,q_2,p$ and the boundary components to $L(0),L(n),L(n+m)$. Various authors have studied the construction of such invariants; we follow the theory as developed by Seidel in [@seidel-book; @seidel-les].

Because we want to make contact with the theory of pseudo-holomorphic sections of Lefschetz fibrations, we need to import the setup from [@seidel-les §2.1]. Let $\pi : E \to B$ be a exact symplectic Lefschetz fibration. We choose primitive $\theta$ for the symplectic form $\omega$ such that the Liouville vector field $Z$ defined on the fiber $M$ by $\iota_Z(\omega|_M) = \theta|_M$ points outward along the boundary of $M$. The flow of $Z$ defines a collar $[-\epsilon,0]\times M \to M$, and we let $\sigma$ be the function on a neighborhood of $\partial M$ given by projection to the $[-\epsilon,0]$ factor. We pick an almost complex structure $j$ on the base of the fibration, we always consider an almost complex structure $J$ on the total space which is *compatible relative to $j$*, meaning

1.  $J$ is integrable in a neighborhood of each critical point,

2.  $\pi$ is a $(J,j)$-holomorphic map,

3.  For each fiber $E_z$, the form $\omega(\cdot, J\cdot)|TE_z$ is symmetric and positive definite

4.  on a neighborhood of the horizontal boundary of $E$, $J$ satisfies $\theta \circ J = d(e^\sigma)$.

Later on, in Section [\[sec:horiz-sections\]](#sec:horiz-sections){reference-type="ref" reference="sec:horiz-sections"}, we will also need to consider $J$ which are *horizontal*, meaning that $J$ preserves the horizontal subspaces of the symplectic connection. Once we extend the Lagrangian boundary condition Section [0.1](#sec:extend-fiber){reference-type="ref" reference="sec:extend-fiber"} so that our Lagrangians are compact in each fiber, these conditions imply that the curves we wish to count lie in a compact subset disjoint from the horizontal boundary [@seidel-les Lemma 2.2]. The second condition is particularly useful because it allows us to study pseudo-holomorphic curves by projecting them to the base of the fibration.

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

The proof of Proposition [\[prop:counts-summary\]](#prop:counts-summary){reference-type="ref" reference="prop:counts-summary"} is where most of the technical work of this paper is spent, and it will occupy Sections [0.1](#sec:extend-fiber){reference-type="ref" reference="sec:extend-fiber"}--[\[sec:signs\]](#sec:signs){reference-type="ref" reference="sec:signs"}. Sections [0.1](#sec:extend-fiber){reference-type="ref" reference="sec:extend-fiber"} and [0.2](#sec:degenerated-spaces){reference-type="ref" reference="sec:degenerated-spaces"} present a technique for degenerating the total space of the Lefschetz fibration to break these counts into simpler pieces. Sections [\[sec:horiz-sections\]](#sec:horiz-sections){reference-type="ref" reference="sec:horiz-sections"} and [\[sec:sections-polygon\]](#sec:sections-polygon){reference-type="ref" reference="sec:sections-polygon"} compute these pieces, and Section [\[sec:signs\]](#sec:signs){reference-type="ref" reference="sec:signs"} determines the signs.

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

## Extending the fiber {#sec:extend-fiber}

One problem with our Lagrangian boundary conditions $L(d)$ is that they intersect the horizontal boundary $\partial^h X(B)$. This raises the possibility that as we degenerate the fibration, part of a pseudo-holomorphic section can escape through $\partial^h X(B)$.

We now describe a technical trick that, by attaching bands to the fiber, allows us to close up the Lagrangians for the purpose of a particular computation, and thereby use only the results in the literature on sections with Lagrangian boundary conditions disjoint from the boundaries of the fibers. Proposition [\[prop:extended-sections\]](#prop:extended-sections){reference-type="ref" reference="prop:extended-sections"} states that this attachment does not change the spaces of holomorphic curves that we wish to count, because they do not enter the bands. On the other hand, when we degenerate the fibration, we find that some of these curves degenerate into curves that do enter the bands.

The starting point for this construction is, given inputs $a_1$ and $a_2$, to consider the portion of the fibration $\tilde{X}(B)|T \to T$ lying over the triangle $T$ in the base. We recall the assumption from section [\[sec:focus-focus-lefschetz\]](#sec:focus-focus-lefschetz){reference-type="ref" reference="sec:focus-focus-lefschetz"} that the symplectic connection is actually flat near the horizontal boundary. After passing to the universal cover of the base, the symplectic monodromies around the boundaries of $X(I)$ can be trivialized, and the fibration is actually symplectically trivial near the horizontal boundary. We also assume that the boundary intersections of our Lagrangians have been positively perturbed as in Section [\[sec:pert\]](#sec:pert){reference-type="ref" reference="sec:pert"}, so that they do not intersect at the boundary. After trivializing the fibration near the horizontal boundary, we find that in each fiber $F_z$ of $\tilde{X}(B)|T \to T$, there are six points on $\partial F_z$ (three on either component), arising as the symplectic parallel transport of the boundary points of $L(0)$, $L(n)$, and $L(n+m)$. These are the points where the Lagrangians $L(0),L(n),L(n+m)$ are allowed to intersect $\partial F_z$ (though $L(d) \cap \partial F_z$ is only nonempty if $z \in \ell(d)$ is on the appropriate boundary component of the triangle $T$). The two sets of three points on each component of $\partial F_z$ are matched according to which Lagrangian they come from, and we extend the fiber $F_z$ to $\hat{F}_z$ by attaching three bands running between the two components of $F_z$ according to this matching. We call the resulting fibration $\hat{X}_T
\to T$. We have an embedding $\iota: \tilde{X}(B)|T \to \hat{X}_T$.

Over the component of $\partial T$ where the Lagrangian boundary condition $L(0)$ lies, we extend $L(0)$ to $\hat{L}(0)$, closing it up fiberwise to a circle by letting it run through the corresponding band in $\hat{F}_z$. Similarly we close up $L(n)$ and $L(n+m)$ to their hat-versions, each passing through a different band.

Figure [2](#fig:extended-fiber){reference-type="ref" reference="fig:extended-fiber"} shows the cylinder with a band attached. The actual extended fiber has three such bands.

![Attaching a band to close up one of the Lagrangians in the fiber.](extended-fiber){#fig:extended-fiber width="2in"}

It is immediate from the construction that $\hat{X}_T \setminus \image
(\iota)$ is symplectically a product. Let us use a complex structure which is also a product in this region. Transversality can be achieved using such structures because all intersection points lie in $\image
(\iota)$, and hence any pseudo-holomorphic section must also pass through $\image (\iota)$, where we are free to perturb $J$ as usual. We have the following proposition:

::: proposition
[]{#prop:extended-sections label="prop:extended-sections"} Any pseudo-holomorphic section $s:T \to \hat{X}_T$ with boundary conditions $\hat{L}(d)$, $d = 0, n, n+m$ lies within $\image
  (\iota)$.
:::

::: proof
*Proof.* Let $p: \hat{X}_T \setminus \image(\iota) \to \hat{F}$ denote the projection to the fiber, whose image consist of the bands. Let us consider one band containing the Lagrangian $L$. Introduce coordinates $(s,t) \in [0,a]\times [-1,1]$ on the band such that the part of the Lagrangian within the band is $L = [0,a]\times \{0\}$.

Let $V \subset T$ be the preimage of the open band $(0,a)\times
  [-1,1]$ under $p \circ s$. The set $V$ is relatively open. Let $V^\circ = V \setminus \partial T$. As the map $p\circ s :V^\circ
  \to [0,a]\times[-1,1]$ is actually a holomorphic map between Riemann surfaces, the open mapping theorem implies that the image $W =
  (p\circ s)(V^\circ)$ is an open subset of $(0,a)\times
  (-1,1)$. Also, the boundary of $W$ is contained in the union of the Lagrangian $[0,a]\times \{0\}$ (where the boundary of the domain is sent) and the ends of the band $\{0,a\}\times (-1,1)$ (where image of $V$ connects to the rest of the holomorphic curve). The only such $W$ is the empty set. ◻
:::

## Degenerating the fibration {#sec:degenerated-spaces}

By propositions [\[prop:triangles-sections\]](#prop:triangles-sections){reference-type="ref" reference="prop:triangles-sections"} and [\[prop:extended-sections\]](#prop:extended-sections){reference-type="ref" reference="prop:extended-sections"}, in order to compute the Floer product between two morphisms $q_1 \in HF^0(L(0),L(n))$ and $q_2 \in
HF^0(L(n),L(n+m))$, it is just as good to count sections of the fibration $\hat{X}_T \to T$ with Lagrangian boundary conditions $\hat{L}(0)$, $\hat{L}(n)$, $\hat{L}(n+m)$.

In order to obtain these counts, we will consider a degeneration of the Lefschetz fibration. We consider a one-parameter family of Lefschetz fibrations $\hat{X}^r \to T^r$, which for $r = 1$ is simply the one we started with. As $r$ goes to zero, the fibration deforms so that all of the $k$ critical values contained within $T$ move toward the side of $T$ corresponding to $\ell(n)$. In the limit, a disc bubble appears around each critical value, and at $r = 0$, the base $T$ has broken into a $(k+3)$-gon, with $k$ "new" vertices along the side corresponding to $\ell(n)$, each of which joins to a disk with a single critical value. We can equip each fibration with Lagrangian boundary conditions varying continuously with $r$, and degenerating to a collection of Lagrangian boundary conditions for each of the component fibrations at $r = 0$.

The base of the Lefschetz fibration undergoes the degeneration shown in figure [3](#fig:degeneration){reference-type="ref" reference="fig:degeneration"}. This figure shows specifically the case for the product of $x \in CF^*(L(0),L(1))$ and $z \in
CF^*(L(1),L(2))$. The marked point on the upper portion is the Lefschetz critical value, while the marked points on the lower portion are the Lefschetz critical value and a node.

![Degenerating the fibration.](degeneration){#fig:degeneration width="1.5in"}

When performing this construction carefully, it is better to describe this family as a smoothing of the degenerate $r = 0$ end. Let $T^0$ be a disk with $(k+3)$ boundary punctures. We emphasize that the conformal structure of $T^0$ is fixed. Let $\hat{X}^0 \to T^0$ be a symplectically trivial Lefschetz fibration. Let $D_1,\dots,D_k$ denote the $k$ disks with one boundary puncture that are our "bubbles". For each $i$ let $E_i \to D_i$ denote a Lefschetz fibration with a single critical value, and which is trivial near the puncture. Let the symplectic monodromy around $\partial D_i$ be denoted $\tau_i$.

We will equip each of the components of this fibration with a Lagrangian boundary condition as follows.

-   The base $T^0$ has one boundary component corresponding to $\ell(0)$, one boundary component corresponding to $\ell(n+m)$, and $(k+1)$ boundary components corresponding to $\ell(n)$. Since the fibration $\hat{X}^0 \to T^0$ is trivial, it suffices to describe each boundary condition in the fiber. Over the point where $\ell(0)$ and $\ell(n+m)$ come together, we identify the fiber with that of $\hat{X}^1 \to T^1$, and take $\hat{L}(0)^0$ and $\hat{L}(n+m)^0$ to be the corresponding Lagrangians.

-   Over the $k+1$ boundary components of $T^0$ corresponding to $\ell(n)$, we construct a sequence $\hat{L}(n)^0_i$ of Lagrangians. At the puncture where $\ell(0)$ and $\ell(n)$ come together, we take $\hat{L}(n)^0_0$ to have the same position relative to $\hat{L}(0)^0$ (already constructed) that $\hat{L}(n)$ has relative to $\hat{L}(0)$ in the original fibration. As we pass each of the new punctures where the disks are attached, the monodromies $\tau_i$ must be applied. So we let $$\label{eq:Ln-twists}
        \hat{L}(n)^0_i = \tau_i(\hat{L}(n)^0_{i-1})$$ This can be done so that, over the puncture where $\ell(n)$ and $\ell(n+m)$ come together, $\hat{L}(n)^0_k$ and $\hat{L}(n+m)^0$ intersect as the original $\hat{L}(n)$ and $\hat{L}(n+m)$ do.

-   Over the $k$ disks $D_i$, we take a Lagrangian boundary condition which interpolates between $\hat{L}(n)^0_{i-1}$ and $\hat{L}(n)^0_i$. This is possible because each $D_i$ contains a single Lefschetz critical value.

Note that at this stage we only care about the twists $\tau_i$ up to Hamiltonian isotopy, but we will make a particular choice in §[\[sec:horiz-sections\]](#sec:horiz-sections){reference-type="ref" reference="sec:horiz-sections"}, as required by the technical considerations there. This gives us $\tau_i$ such that $\hat{L}(n)^0_{i-1}$ and $\hat{L}(n)^0_i$ have one intersection point over $i$-th new puncture of $T^0$.

Since the boundary conditions agree over the corresponding punctures, we can glue the components over $T^0$ and $D_1,\dots,D_k$ with large gluing length in order to obtain $\hat{X}^\epsilon \to T^\epsilon$ for small $\epsilon > 0$, which has three boundary components and $k$ critical values all near the $\ell(n)$ boundary. There is a family of Lefschetz fibrations interpolating between $\hat{X}^\epsilon
\to T^\epsilon$ back to our original $\hat{X}^1 \to T^1$, along which the critical values move back to their original points.

We equip $T^0$ and $D_1,\dots,D_k$ with complex structures, and equip $T^\epsilon$ with a family of complex structures $j^\epsilon$ converging to those in the limit. All total spaces are equipped with relatively compatible almost complex structures.

Now we appeal to the gluing theorem [@seidel-les Proposition 2.2] telling us how the curve counts behave under the degeneration.

::: proposition
[]{#prop:TQFT-gluing label="prop:TQFT-gluing"} The count of pseudo-holomorphic sections of $\hat{X}^1 \to T^1$, with Lagrangian boundary conditions $\hat{L}(d)$, $d = 0 ,n ,n+m$ is obtained from the counts of sections of $\hat{X}^0 \to T^0$ and $E_i
  \to D_i$ by gluing together sections whose values over the punctures match.
:::

::: proof
*Proof.* Considering pseudo-holomorphic sections of the fibrations $\hat{X}^\epsilon \to T^\epsilon$, as long as the gluing length is large, the sections for $r = \epsilon$ will be obtained from sections over $T^0$ and $D_1,\dots,D_k$ by gluing sections with matching values at the punctures [@seidel-les Proposition 2.2]. During the deformation from $r = \epsilon$ to $r =
1$, no Floer strip breaking can occur because our Lagrangians $\hat{L}(d)$, $d = 0, n, n+m$ do not bound any strips, even topologically, so the count remains the same at $r = 1$. ◻
:::
