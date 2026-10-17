---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-006-31-weierstrass-points
section_title: "Weierstrass Points"
section_number: 3.1
pages: 13-17
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.95
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
[]{#subsec: Weierstrass points label="subsec: Weierstrass points"} We recall the definition of an important class of points.

::: definition
[]{#def: Weierstrass points label="def: Weierstrass points"} A **Weierstrass Point** on a curve $X$ of genus $g$ with canonical embedding $X_{c} \subseteq \mathbb{P}^{g-1}$ is a point $P$ satisfying one of the following equivalent conditions:

1.  there exists a hyperplane $H \subset \mathbb{P}^{g-1}$such that $H \cap X_c$ has multiplicity at least $g$ at $P$,

2.  there exists a holomorphic differential on $X$ vanishing at $P$ with order $\geq g$,

3.  there exists a meromorphic function on $X$ with poles just at $P$ of order $\leq g$, and

4.  the Wronskian determinant given by $\operatorname{Wr}(P) = \det \left( \frac{d^i \omega_j}{dz^i} \right)_{i,j = 0, \dots, g-1}$, where $\{ \omega_j \}$ is a basis of holomorphic differentials and $z$ is a local coordinate around $P$, vanishes.
:::

In [@Singerman1997] the Weierstrass points are shown (implicitly) to correspond to the edge-centres of the universal map. This shows that the order 2 rotation that permutes the vertices and face-centres adjacent to an edge-centre will preserve the corresponding Weierstrass point. They can also be interpreted geometrically as pairwise-symmetric distributed along the edges of the small stellated dodecahedron. As Weber identifies the order-3 symmetry as the rotation about the axis through opposite vertices of the *unstellated* dodecahedron, one might wonder from this picture whether Weierstrass points are fixed points of the order-3 permutations in the group. This turns out not be the case and a counting argument helps elucidate: the small stellated dodecahedron has 12 faces, which in turn means we want to have $\frac{60}{12}=5$ Weierstrass points per face. Hence where three faces overlap there must be three Weierstrass points 'stacked' there, which are invisibly permuted by the action.

Having now identified the Weierstrass points as some of the geometric points, we give a concrete result about what the Weierstrass points are.

::: prop
[]{#WPprop label="WPprop"} Bring's curve has 60 Weierstrass points, on which $\mathop{\mathrm{Aut}}(\mathcal{B})$ acts transitively. Letting $\{ \alpha,\beta,\gamma\}$ be the roots of the cubic $x^3+2x^2+3x+4$, these are given in the $\mathbb{P}^4$-model by $W_{ijk}$ where, for example, $$W_{345} = [1:1:\alpha:\beta:\gamma]  .$$
:::

::: proof
*Proof.* Edge, working in the $\mathbb{P}^4$-model, identifies the Weierstrass points with the 60 intersections of the curve with the 10 planes $\Pi_{ij} = \left\{  x_i = x_j \right\}$. To do this, Edge quotes [@Wiman1895] to show that these intersection points are stalls[^1], i.e. inflection points of certain linear series, and for the canonical embedding these are exactly the Weierstrass points [@Arbarello1985 p. 37]. Simple algebra then gives the exact expression we write down. This viewpoint makes it clear that the Weierstrass points at the intersection with $\Pi_{ij}$ are preserved by the transposition[^2] $(ij)$ only, so have orbits of size $\frac{120}{2}=60$, and as the automorphism restricts to a permutation of the Weierstrass points, the action is then transitive. ◻
:::

With our naming convention, note $W_{ijk}$ is defined by $x_i=\alpha$, $x_j = \beta$, $x_k = \gamma$. If we choose a different labelling of the roots of the cubic, this would give a different labelling of the Weierstrass points. The Weierstrass points split as $60 = 6 \times 10$, with 6 Weierstrass points being fixed by each of the 10 involutions in $S_5$.

The property that the automorphism group acts transitively on the Weierstrass points is very rare, as characterised by the following result.

::: theorem
If $X$ is a Riemann surface of genus $g>2$ with $g^3-g$ Weierstrass points on which $\mathop{\mathrm{Aut}}X$ acts transitively then either

-   $g=4$ and $X$ is Bring's curve,

-   $g=3$ and $X$ is Klein's curve, or

-   $g=3$ and $\mathop{\mathrm{Aut}}X \cong S_4$.
:::

::: remark
As we have an explicit birational map from our plane model to our canonical embedding of the curve, we can get the explicit forms of the Weierstrass points in the HC-model using Edge's identification of the Weierstrass points in the $\mathbb{P}^4$-model. If one does not have this information, it is still possible to calculate the Weierstrass points using Sage and some educated guesswork. Using computer algebra, and the characterisation of Weierstrass points as zeros of the Wronskian determinant, one can check that in the HC-model the Weierstrass points have base coordinates at the 60 roots of the polynomial equations $$\begin{aligned}
    0 &= x^{12} - 32x^{11} - 114x^{10} - 200x^9 + 100x^8 + 48x^7 - 936x^6 + 1728x^5 - 2000x^4 + 3200x^3 \\
    &\phantom{=} - 2624x^2 + 768x - 64  , \\
    0 &= x^{24} - 24x^{23} + 1306x^{22} - 2864x^{21} + 10096x^{20} - 32704x^{19} - 5704x^{18} - 41824x^{17}  \\
    &\phantom{=} + 43056x^{16} + 831616x^{15} + 837856x^{14} + 992256x^{13} + 2603136x^{12} + 1238016x^{11}  \\
    &\phantom{=} + 1560576x^{10} + 5584896x^9 + 3357696x^8 + 3838976x^7 + 5856256x^6 + 2543616x^5  \\
    &\phantom{=} + 2200576x^4 + 1355776x^3 + 454656x^2 + 65536x + 4096  , \\
    0 &= x^{24} + 56x^{23} + 1176x^{22} - 1784x^{21} - 3904x^{20} + 36096x^{19} + 12776x^{18} - 211904x^{17}  \\
    &\phantom{=} + 304736x^{16} + 431616x^{15} + 339456x^{14} - 1985664x^{13} - 625344x^{12} + 1034496x^{11}  \\
    &\phantom{=} + 3512576x^{10} - 584704x^9 - 3572224x^8 - 2018304x^7 + 3303936x^6 + 3055616x^5  \\ 
    &\phantom{=} + 1099776x^4 + 45056x^3 + 229376x^2 - 16384x + 4096  .
\end{aligned}$$ One can check that the Galois group of each polynomial is $C_4 \times S_3$. We have seen that in the HC-model the automorphisms have coefficients in $\mathbb{Z}[\zeta]$, and so we know the splitting field must be an extension of $\mathbb{Q}[\zeta]$, which accounts for the $C_4$ factor in the Galois group. $S_3$ has a subgroup of order $2$, corresponding to an extension of degree-2, and a brute force calculation shows that we also wish to adjoin $i\sqrt{2}$. This has already nearly reduced the problem, and then one needs a small moment of inspiration to find the last thing to adjoin. Looking at [@Riera1992] then may inspire one to adjoin the real root of the polynomial $x^3+7x^2+8x+4$, say $\xi$, and this gives the full splitting field. We can solve the cubic explicitly using Cardano's formula to find $$\xi = -\frac{1}{3}\left\{ 7+  \left[ \sqrt[3]{145+30\sqrt{6}}+\sqrt[3]{145-30\sqrt{6}} \right] \right\}   ,$$ and as such we could also take our splitting field to be $$\mathbb{Q}\left[ \zeta, i\sqrt{2}, \sqrt[3]{145+30\sqrt{6}} \right]  .$$ We observe by Cardano's formula that $\alpha, \beta, \gamma \in \mathbb{Q}[i\sqrt{2}, \sqrt[3]{30+15\sqrt{6}}]$, and this latter field is isomorphic to $\mathbb{Q}[i\sqrt{2}, \sqrt[3]{145+30\sqrt{6}}]$. With these expression for the Weierstrass points, and the explicit knowledge of the automorphism group as an action on affine coordinates, we can find explicitly the transposition that preserves a given Weierstrass point.

Note that an alternative method for computing Weierstrass points algorithmically has been implemented in Magma [@Hess2002a].
:::

We now have seen how our Weierstrass points satisfy characterisations 1 and 4 of Definition [\[def: Weierstrass points\]](#def: Weierstrass points){reference-type="ref" reference="def: Weierstrass points"}, and we complete the picture with the following result which we believe new.

::: prop
[]{#prop: function and divisor associated to WP label="prop: function and divisor associated to WP"} Define the points $P_{345}$, $P^\prime_{345}$ corresponding to the Weierstrass point $W_{345}$ (and similarly for the other Weierstrass points) by $$\begin{aligned}
    P_{345} &= [\delta^\prime : \delta : (-43\alpha^2 - 113\alpha - 92)\beta/112 \\
    &\phantom{=}- (13\alpha^2 - 27\alpha - 20)/28 : (43\alpha^2 + 25\alpha - 4)\beta/112 + (13\alpha^2 + 3\alpha - 24)/28 : 1] \\
    P^\prime_{345} &= [\delta : \delta^\prime : (-43\alpha^2 - 113\alpha - 92)\beta/112 \\
    &\phantom{=} - (13\alpha^2 - 27\alpha - 20)/28 : (43\alpha^2 + 25\alpha - 4)\beta/112 + (13\alpha^2 + 3\alpha - 24)/28 : 1].
\end{aligned}$$ Here $\alpha$, $\beta$ were defined in Proposition [\[WPprop\]](#WPprop){reference-type="ref" reference="WPprop"} and $\delta$, $\delta^\prime$ are the roots of $$x^2 - \left[ \frac{(11 \alpha + 12)\beta + 4(3\alpha + 2)}{14} \right]x + \left[ \frac{23(155\alpha + 388)\beta + 92(97\alpha + 172)}{6272} \right]  .$$ Then there is a holomorphic differential $\nu_{345}$ on Bring's curve with divisor $$4W_{345} + P_{345} + P_{345}^\prime  ,$$ and a meromorphic function on Bring's curve with divisor $$P_{145} + P_{145}^\prime + P_{245} + P_{245}^\prime -4W_{345}  .$$
:::

::: proof
*Proof.* Note that algorithmically it is possible to construct these through the work in [@Hess2002], the tools for which are partially implemented in Sage but not with enough generality for us to use out-the-box. As such we need a different approach.

We know that for any Weierstrass point $W$ there is a hyperplane $H \subset \mathbb{P}^3$ intersecting the canonical embedding with multiplicity $g=4$ at $W$ (that is $H \cap \mathcal{B} = 4W + P + P^\prime$ for some $P, P^\prime \in \mathcal{B}$). Such a hyperplane gives a holomorphic differential $\nu_{ijk}$ with $(\nu_{ijk}) = 4W_{ijk} + P_{ijk} + P^\prime_{ijk}$. From [@Edge1978] we know that for Bring's curve the osculating plane[^3] at $W$ intersects 4 times, and so this is the plane we are looking for. As Edge gives a formula for the osculating plane (attributed to Hesse), we can explicitly calculate the remaining 2 intersections with the curve in terms of a polynomial roots. This gives us the first result for the divisor of the meromorphic differential.

Furthermore, from [@Edge1981] we have a tritangent plane which has intersection with Bring's curve $$2(W_{145} + W_{245} + W_{345})  .$$ We will discuss this plane (and others like it) more in §[\[subsec: tritangent planes\]](#subsec: tritangent planes){reference-type="ref" reference="subsec: tritangent planes"}, but for now all we need is that this means there is a holomorphic differential $\omega_{45\alpha}^{(1)}$ on $\mathcal{B}$ with $(\omega_{45\alpha}^{(1)}) = 2(W_{145} + W_{245} + W_{345})$. As such we get the divisor of the meromorphic function $$\left( \frac{\nu_{145}\nu_{245}}{\left( \omega_{45\alpha}^{(1)} \right)^2} \right) = P_{145} + P_{145}^\prime + P_{245} + P_{245}^\prime -4W_{345}  .$$ As we can calculate the formula for all these planes explicitly if we wish, we could (in principle) construct the corresponding function and differential. ◻
:::

::: remark
We are able to verify the results in Proposition [\[prop: function and divisor associated to WP\]](#prop: function and divisor associated to WP){reference-type="ref" reference="prop: function and divisor associated to WP"} using the Abel-Jacobi map implemented in the Sage [@DisneyHogg2021]; see the notebooks.
:::

[^1]: A **stall** of a plane curve is a point where the osculating (hyper)plane has a 4-point intersection [@Edge1971].

[^2]: In Theorem 4 of [@Dye1995], these transpositions are associated with the Brianchon points of the Clebsch hexagon $H$ from the proof of Proposition [\[prop: HC valid model for Bring\]](#prop: HC valid model for Bring){reference-type="ref" reference="prop: HC valid model for Bring"}.

[^3]: The **osculating plane** at a point $P$ on a curve is the limiting plane through $P$, $P^\prime$, $P^{\prime \prime}$ as $P^\prime, P^{\prime \prime} \to P$ on the curve [@Salmon1862].
