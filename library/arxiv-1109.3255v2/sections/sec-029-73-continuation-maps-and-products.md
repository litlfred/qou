---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-029-73-continuation-maps-and-products
section_title: "Continuation maps and products"
section_number: 7.3
pages: 68-70
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.971
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:continuation-product label="sec:continuation-product"}

We saw above that for $r > d_1-d_2$, the generators of $CF^*(L(d_1),L(d_2);rH)$ all have degree $0$, so there are no differentials, and we can identify these complexes with their homologies. In order to obtain the wrapped Floer cohomology, we must determine the continuation maps.

Let it be understood that we require $r \in \Z$ in case $L$, $r \in
2\Z$ in case $C$, and $r \in 3\Z$ in case $D$.

To get started, we consider the wrapped Floer cohomology of $L(d_1)$ with itself. Each complex $CF^*(L(d_1),L(d_1);rH)$ has a distinguished element $e_r$, sitting at the minimum of $H$. The complexes are filtered by action, and the continuation maps are non-increasing with respect to this filtration. Under the $r \to r'$ continuation map, $e_r \mapsto e_{r'}$; $e_r$ and $e_{r'}$ are the unique generators of minimal action in their respective complexes, and in fact their actions are equal, so the only strip is the constant map to the minimum.

At this point we bring in the product structure.

::: proposition
Let $L_i$ one of the Lagrangians $L(d_i)$ for $i = 1, 2, 3$. Under the identification $$CF^*(L_i,L_j;rH) \cong CF^*(\phi_{rH}(L_i),L_j)$$ The product $$HF^*(L_2,L_3; rH) \otimes HF^*(L_1,L_2; sH) \to HF^*(L_1,L_3; (r+s)H)$$ which counts inhomogeneous pseudo-holomorphic triangles corresponds to the product $$HF^*(\phi_{rH}(L_2),L_3) \otimes
  HF^*(\phi_{(r+s)H}(L_1),\phi_{rH}(L_2)) \to HF^*(\phi_{(r+s)H}(L_1),L_3)$$ counting pseudo-holomorphic triangles with no inhomogeneous term.
:::

::: proof
*Proof.* First we recall the equation for the product in the wrapped setting. The disk with three boundary punctures $S$ is equipped with strip-like ends: at the inputs they are parametrized by $(s,t) \in (0,\infty)\times [0,1]$, while at the output we have $(s,t) \in (-\infty,0)\times [0,1]$. $S$ is also equipped with a closed one form $\beta \in \Omega^1(S)$, whose restriction to $\partial S$ vanishes, such that on the strip-like ends of $S$, $\beta$ has the form $r\,dt$, $s\,dt$ and $(r+s)\,dt$ for the two inputs and the output respectively. The curves we count are solutions of $$(du - X_H \otimes \beta)^{0,1} = 0$$ Because $\beta$ is closed and $S$ has no first homology, we may find a primitive $\tau \in C^\infty(S)$ such that $d \tau = \beta$, and we assume $\tau = 0$ on the boundary corresponding to $L_3$. Denoting by $\phi^t_H$ the flow of $X_H$ for time $t$, we can define a new map $v = \phi^{-\tau}_H \circ u$, meaning that for $p \in S$, we take $u(p)$ and flow it for time $-\tau(p)$ by $X_H$. This has the effect of collapsing each Hamiltonian chord to a single point. Then the map $v$ is pseudo-holomorphic without inhomogeneous term, but with a domain-dependent almost complex structure obtained by conjugating the original $J$ by $\phi_H^\tau$ at each point.

We must relate the products $$HF^*(\phi_{rH}(L_2),L_3) \otimes
  HF^*(\phi_{(r+s)H}(L_1),\phi_{rH}(L_2)) \to HF^*(\phi_{(r+s)H}(L_1),L_3)$$ defined with respect to this domain-dependent almost complex structure $\{J_p\}_{p\in S}$ to the operation that we studied in Section [\[sec:degeneration\]](#sec:degeneration){reference-type="ref" reference="sec:degeneration"}, where the complex structure $J$ was fixed. We fix attention to one strip-like end, say the one corresponding to $L_2$ and $L_3$. On this end the complex structure depends only on $t \in [0,1]$. There is a continuation map $$HF^*(\phi_{rH}(L_2),L_3;\{J_t\}) \to HF^*(\phi_{rH}(L_2),L_3;J)$$ counting strips with a domain-dependent almost complex structure that interpolates between $\{J_t\}$ and $J$. We claim that, in our situation, all such strips are constant. This means that the bases of intersection points on the two sides of the continuation map correspond. These continuation maps intertwine the product with respect to $\{J_p\}$ and the one defined using $J$, implying that these products agree when expressed in the basis of intersection points on either side of the correspondence.

It remains to prove the claim that all the continuation strips are constant. Let $u$ denotes such a strip. Because the Hamiltonian flow preserves the structure of the Lefschetz fibration, each $J_p$ for $p \in S$ is a complex structure with the property that the tangent space to a fiber is complex, and the projection to the base is holomorphic, once we equip the base with a suitable complex structure $j_p$. As $u$ is pseudo-holomorphic with respect to $\{J_p\}$, this implies that $\pi \circ u$ has the property that its differential at each point has rank either $0$ or $2$. Thus the image of $\pi \circ u$ is a set whose boundary is contained in the images of the Lagrangians $\phi_{rH}(L_2)$ and $L_3$. Because there are no topological strips in the base joining different intersection points of the base paths, we conclude that $\pi \circ u$ must be constant, and the image of $u$ is contained in a fiber. But in the fiber there are also no topological strips joining different intersection points. Hence $u$ itself is constant. ◻
:::

When the differentials on the Floer complexes vanish, the identification of the products holds at the chain level as well. Tracing the isomorphisms through, we find that the product with $e_r$ induces the naive inclusion map on generators $$\mu^2(e_r,\cdot) = i : HF^*(L(d_1),L(d_2); sH) \to HF^*(L(d_1),L(d_2);(r+s)H)$$

Due to the compatibility of the product with the continuation maps, and the fact that $e_r \mapsto e_{r'}$ under continuation, we find that the naive inclusion maps commute with the continuation maps: $$\xymatrix{
    HF^*(L(d_1),L(d_2);sH)\ar[d]^{=} \ar[r]^{i}& HF^*(L(d_1),L(d_2); (s+r)H)\ar[d]^{\text{cont.}}\\
    HF^*(L(d_1),L(d_2);sH) \ar[r]^{i}& HF^*(L(d_1),L(d_2); (s+r')H)
  }$$ Thus the continuation map agrees with the naive inclusion map, at least on those generators which are in the image of $HF^*(L(d_1),L(d_2);sH)$. It follows that the continuation maps agree with the naive inclusion maps, at least for $r$ large enough depending on a particular generator. Hence $$HW^*(L(d_1),L(d_2)) = \lim_{r\to \infty} HF^*(L(d_1),L(d_2);rH),$$ where the limit is formed with respect to the continuation maps, or with respect to the naive inclusion maps, or (what is equal) the multiplications by the various elements $e_r$.

Spelling this out a bit more gives a precise correspondence with section [\[sec:algebraic-motivation\]](#sec:algebraic-motivation){reference-type="ref" reference="sec:algebraic-motivation"}. Consider the isomorphism $$HF^*(L(d_1),L(d_1);rH) \cong HF^*(L(d_1-r),L(d_1)) \cong H^*(\CP^2, \cO(r))$$

-   $L$: For $r \in \Z$, this isomorphism identifies $e_r$ with $y^r$.

-   $C$: For $r \in 2\Z$, this isomorphism identifies $e_r$ with $p^{r/2}$.

-   $D$: For $r \in 3\Z$, this isomorphism identifies $e_r$ with $(yp)^{r/3}$.

Thus the directed systems computing wrapped Floer cohomology are identified with those computing the cohomology of line bundles on the divisor complements.

We can identify the basis of $HW^*(L(d_1),L(d_2))$ with $\hat{B}(\frac{1}{d_2-d_1} \Z)$, where $\hat{B} =
\hat{B}_L,\hat{B}_C,\hat{B}_D$ is the completion of the affine manifold. The sets $B(\frac{1}{d_2-d_1+r}\Z)$ embed in $\hat{B}(\frac{1}{d_2-d_1}\Z)$ and this latter is their limit as $r
\to \infty$; the map is dilation by $\frac{d_2-d_1+r}{d_2-d_1}$ centered at the minimum of $H$.

Using the products we computed in section [\[sec:degeneration\]](#sec:degeneration){reference-type="ref" reference="sec:degeneration"}, we can identify this basis $\hat{B}(\frac{1}{d}\Z)$ for $HW^*(L(0),L(d))$ with a basis of $H^*(U;\cO(d))$, and complete the proof of Theorem [\[thm:wrapped-products\]](#thm:wrapped-products){reference-type="ref" reference="thm:wrapped-products"}

-   $L$: The point $q_{a,i}$ of $\hat{B}_L(\frac{1}{d}\Z)$ corresponds to the function $x^{-a}p^iy^{d+a-2i}$ for $a \leq 0$, and $z^ap^iy^{d-a-2i}$ for $a \geq 0$. In this case $i \geq 0$ can be arbitrarily large, so the exponent of $y$ is allowed to be negative.

-   $C$: The point $q_{a,i}$ of $\hat{B}_C(\frac{1}{d}\Z)$ corresponds to the function $x^{-a}p^iy^{d+a-2i}$ for $a \leq 0$, and $z^ap^iy^{d-a-2i}$ for $a \geq 0$. In this case $i \leq
      \left\lfloor\frac{d-|a|}{2}\right\rfloor$ can be negative, so the exponent of $p$ is allowed to be negative, while the exponent of $y$ is non-negative.

-   $D$: The point $q_{a,i}$ of $\hat{B}_D(\frac{1}{d}\Z)$ corresponds to the function $x^{-a}p^iy^{d+a-2i}$ for $a \leq 0$, and $z^ap^iy^{d-a-2i}$ for $a \geq 0$. In this case $i \in \Z$, so the exponents of $y$ and $p$ are allowed to be negative.
