---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-014-42-extending-the-fiber
section_title: "Extending the fiber"
section_number: 4.2
pages: 37-38
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.984
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:extend-fiber label="sec:extend-fiber"}

One problem with our Lagrangian boundary conditions $L(d)$ is that they intersect the horizontal boundary $\partial^h X(B)$. This raises the possibility that as we degenerate the fibration, part of a pseudo-holomorphic section can escape through $\partial^h X(B)$.

We now describe a technical trick that, by attaching bands to the fiber, allows us to close up the Lagrangians for the purpose of a particular computation, and thereby use only the results in the literature on sections with Lagrangian boundary conditions disjoint from the boundaries of the fibers. Proposition [\[prop:extended-sections\]](#prop:extended-sections){reference-type="ref" reference="prop:extended-sections"} states that this attachment does not change the spaces of holomorphic curves that we wish to count, because they do not enter the bands. On the other hand, when we degenerate the fibration, we find that some of these curves degenerate into curves that do enter the bands.

The starting point for this construction is, given inputs $a_1$ and $a_2$, to consider the portion of the fibration $\tilde{X}(B)|T \to T$ lying over the triangle $T$ in the base. We recall the assumption from section [\[sec:focus-focus-lefschetz\]](#sec:focus-focus-lefschetz){reference-type="ref" reference="sec:focus-focus-lefschetz"} that the symplectic connection is actually flat near the horizontal boundary. After passing to the universal cover of the base, the symplectic monodromies around the boundaries of $X(I)$ can be trivialized, and the fibration is actually symplectically trivial near the horizontal boundary. We also assume that the boundary intersections of our Lagrangians have been positively perturbed as in Section [\[sec:pert\]](#sec:pert){reference-type="ref" reference="sec:pert"}, so that they do not intersect at the boundary. After trivializing the fibration near the horizontal boundary, we find that in each fiber $F_z$ of $\tilde{X}(B)|T \to T$, there are six points on $\partial F_z$ (three on either component), arising as the symplectic parallel transport of the boundary points of $L(0)$, $L(n)$, and $L(n+m)$. These are the points where the Lagrangians $L(0),L(n),L(n+m)$ are allowed to intersect $\partial F_z$ (though $L(d) \cap \partial F_z$ is only nonempty if $z \in \ell(d)$ is on the appropriate boundary component of the triangle $T$). The two sets of three points on each component of $\partial F_z$ are matched according to which Lagrangian they come from, and we extend the fiber $F_z$ to $\hat{F}_z$ by attaching three bands running between the two components of $F_z$ according to this matching. We call the resulting fibration $\hat{X}_T
\to T$. We have an embedding $\iota: \tilde{X}(B)|T \to \hat{X}_T$.

Over the component of $\partial T$ where the Lagrangian boundary condition $L(0)$ lies, we extend $L(0)$ to $\hat{L}(0)$, closing it up fiberwise to a circle by letting it run through the corresponding band in $\hat{F}_z$. Similarly we close up $L(n)$ and $L(n+m)$ to their hat-versions, each passing through a different band.

Figure [1](#fig:extended-fiber){reference-type="ref" reference="fig:extended-fiber"} shows the cylinder with a band attached. The actual extended fiber has three such bands.

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
