---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-028-72-wrapping
section_title: "Wrapping"
section_number: 7.2
pages: 64-68
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.991
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:wrapping label="sec:wrapping"}

In this subsection we describe the geometric setup for wrapped Floer cohomology in the mirrors of $U_L,U_C$, and $U_D$.

### Completions {#sec:completions}

Wrapped Floer cohomology is formulated in terms of noncompact manifolds containing noncompact Lagrangian submanifolds. These can be defined as (partial) completions of compact manifolds with boundary.

The starting point for all three cases is the original Lefschetz fibration $X(B)\to X(I)$ containing the Lagrangians $\{L(d)\}_{d\in\Z}$. We define completions $\hat{X}_L$, $\hat{X}_C$, and $\hat{X}_D$. This process involves replacing a boundary component with an infinite end, either on the base or in the fiber of the Lefschetz fibration.

-   $L$: The manifold $\hat{X}_L$ retains a boundary component at the top horizontal boundary, corresponding to the fiber of the superpotential $W_L = u$. The fibers of $X(B) \to X(I)$ are completed at the other, bottom, end. The base annulus $X(I)$ is completed to a cylinder $\hat{X}(I)$, and the fibration is extended over this cylinder.

-   $C$: The manifold $\hat{X}_C$ retains a boundary component at the bottom horizontal boundary, corresponding to the fiber of the superpotential $W_C = \frac{e^{-\Lambda}v^2}{uv-1}$. The fibers are completed at the other, top, end. The base annulus is completed to a cylinder $\hat{X}(I)$, and the fibration is extended over this cylinder.

-   $D$: The manifold $\hat{X}_D$ has no boundary, and the fibers are completed at both ends. The base annulus is completed to a cylinder $\hat{X}(I)$, and the fibration is extended over this cylinder.

The torus fibration on $X(B)$ extends to these completions, and yields torus fibrations over completed bases $\hat{B}_L$,$\hat{B}_C$, $\hat{B}_D$.

-   $\hat{B}_L$ is a half-plane with singular affine structure given by removing the bottom boundary from $B$ and extending in that direction.

-   $\hat{B}_C$ is a half-plane with singular affine structure given by removing the top boundary from $B$ and extending in that direction.

-   $\hat{B}_D$ is an entire plane with singular affine structure given by removing all boundaries from $B$ and extending in all directions.

The Lagrangian submanifolds $L(d)$ are extended to $\hat{L}(d)$; In all cases, we extend $L(d)$ into whatever ends are attached so as to be invariant under the Liouville flow within the end. However, in the case of $L$, respectively $C$, we still have the boundary condition that $\hat{L}(d)$ is required to end on $\Sigma_1$ (the complex hypersurface contained in the top boundary), respectively $\Sigma_0$ (contained in the bottom boundary).

### Hamiltonians {#sec:hamiltonians}

The most crucial difference between the three cases comes from the choices of Hamiltonians that are be used to perform the wrapping. The Hamiltonians we consider are the sum of contributions from the base and the fiber.

Let $H_b: \hat{X}(B) \to \R$ be the pullback of a function on the base cylinder which is a function of the radial coordinate $\eta = \log|w|$ only. Writing the symplectic form on the base as $d\rho \wedge
d\theta$, where $\rho$ is a function of $\eta$, we take $H_b$ to be a convex function of $\rho$ on the compact part $X(I)$, and linear in $\rho$ on the ends. We also require $H_b \geq 0$, with minimum on the central circle $\eta = 0$. Since $dH_b$ vanishes on the fibers, $X_{H_b}$ is horizontal.

The fiber Hamiltonian $H_f$ is chosen differently in each case. The main constraint is that its differential must vanish at any boundary component which may still be present. The construction is most convenient if we assume the completion preserves the $S^1$-symmetry that rotates the fibers. If $\mu$ denotes the moment map for this action, we can take $H_f$ to be a function of $\mu$. Since $X_{H_f}$ is tangent to the fibers, we have $$\{H_b,H_f\} = \omega(X_{H_b},X_{H_f}) = 0$$ which allows us to compute the flow of $H_b+H_f$ term by term.

We use the same base Hamiltonian $H_b$ for all cases. The specific choice of $H_f$ in each case is as follows.

-   $L$: Let $H_{f,L} \geq 0$ be a function with a minimum at the top of the fiber, convex in $\mu$ on the compact part, and linear in $\mu$ on the bottom end.

-   $C$: Let $H_{f,C} \geq 0$ be a function with a minimum at the bottom of the fiber, convex in $\mu$ on the compact part, and linear in $\mu$ on the top end.

-   $D$: Let $H_{f,D} \geq 0$ be a function with a minimum in the two-thirds of the way down from the top of the compact part of the fiber, convex in $\mu$ on the compact part, and linear in $\mu$ on the ends.

In each case, the total Hamiltonian $H = H_b + H_f$ achieves its minimum along a torus in $X(B)$, which is one of the fibers of the torus fibration over $B$. Since $L(r)$ is a section of the torus fibration, $H$ has a unique minimum on $L(r)$, and hence there is a unique constant chord for $L(r)$, which corresponds to the identity element $e_r \in HW^*(L(r),L(r))$. The cases are:

-   $L$: The minimum is along the torus corresponding to the midpoint of the top edge of $B$, where the generator $y$ lies. All of the Lagrangians $L(r)$ for $r \in \Z$ intersect this torus at the same point. As an intersection point of $L(0)$ and $L(d)$, the minimum corresponds to $q_{a,i}$ for $(a,i) = (0,0)$.

-   $C$: The minimum is along the torus corresponding to the midpoint of the bottom edge of $B$, where the generator $p$ lies. All of the Lagrangians $L(r)$ for $r \in 2\Z$ intersect this torus at the same point. As an intersection point of $L(0)$ and $L(r)$, the minimum corresponds to $q_{a,i}$ for $(a,i)= (0,r/2)$.

-   $D$: The minimum is along the torus two-thirds of the way from the top of the middle fiber of the map $B \to I$, where the generator $yp$ lies. All of the Lagrangians $L(r)$ for $r \in 3\Z$ intersect this torus in the same point. As an intersection point of $L(0)$ and $L(r)$, the minimum corresponds to $q_{a,i}$ for $(a,i) = (0,r/3)$.

::: remark
The Hamiltonians we obtain as $H_b + H_f$ are not admissible in the usual sense, because they vanish at some boundaries, and, even in the case $D$, are not linear with respect to a cylindrical end. Closer to our situations are the *Lefschetz admissible* Hamiltonians considered by Mark McLean [@mclean-lf-sh], that are precisely those functions on the total space of a Lefschetz fibration that are the sum of admissible Hamiltonians on the base and fiber separately.
:::

### Generators {#sec:generators}

Given Lagrangian submanifolds $L_1, L_2$ of $X$, equipped with Hamiltonian $H$, and $r \in \R$, we get Floer cohomology complexes $CF^*(L_1,L_2;rH)$ generated by time-$1$ trajectories of $X_{rH}$ starting on $L_1$ and ending on $L_2$. As usual the differential counts inhomogeneous pseudo-holomorphic strips. We also have continuation maps $$CF^*(L_1,L_2;rH) \to CF^*(L_1,L_2;r'H), \quad r < r'$$ given by counting strips where the inhomogeneous term interpolates between $r'X_H$ and $rX_H$. At the homology level, the continuation maps form an inductive system, and we define the *wrapped Floer cohomology* $$HW^*(L_1,L_2) = \lim_{r\to \infty} HF^*(L_1,L_2;rH)$$

Our purpose in this section is simply to set up an enumeration of the generators of $CF^*(L(d_1),L(d_2);rH)$ in each of the three cases. These generators can also be regarded as intersection points $\phi_{rH}(L(d_1))\cap L(d_2)$. In order to make the situation as convenient as possible for our later arguments, we refine our choice of Hamiltonians so as to ensure that $\phi_{rH}(L(d))$ is actually $L(d')$ for some $d'$; thus we can identify wrapped Floer cohomology generators with intersection points of our original Lagrangians. This is done by adjusting the slopes of our Hamiltonians on the ends.

-   We take the base Hamiltonian $H_b$ so that the time--$1$ flow completes $1$ turn on the cylindrical ends of the base.

-   For cases $L$ and $C$, we take the fiber Hamiltonian $H_f$ so that the time--$1$ flow completes $1/2$ turn on the cylindrical end of the fiber.

-   For case $D$, we take the fiber Hamiltonian $H_f$ so that the time--$1$ flow completes $1/3$ turn at the top of the fiber, and $1/6$ turn at the bottom of the fiber.

In all cases the total Hamiltonian we use is $H = H_b + H_f$.

The way to understand the flow of $H$ is to first apply $H_f$, then $H_b$. The flow of $H_f$ wraps $L(d)$ in the fiber, while the flow of $H_b$, when it completes a loop in the base, performs the monodromy of the Lefschetz fibration around that loop, which undoes some of the wrapping due to $H_f$.

We can relate $\phi_H(L(d))$ to $L(d')$ as follows:

-   $L$: we have $\phi_{rH}(L(d)) = L(d-r)$.

-   $C$: we have $\phi_{2rH}(L(d)) = L(d-2r)$. Note that the same *cannot* be said with $r$ in place of $2r$; in that case the two Lagrangians intersect the bottom boundary (where no wrapping occurs) in different points.

-   $D$: we have $\phi_{3rH}(L(d)) = L(d-3r)$. Again the same cannot be said with $r$ in place of $3r$.

In order to identify generators with intersection points, we perturb the boundary intersection points in a positive sense just as before. In the cases with boundary, where the Hamiltonian is supposed to have a minimum at the boundary, it is useful to perform this perturbation in an extra collar attached to the boundary, so that the Lagrangians still intersect at the minimum of $H$ if they did prior to the perturbation. Once this is done, we can identify $$CF^*(L(d_1),L(d_2);rH) \cong CF^*(\phi_{rH}(L(d_1)),L(d_2)) \cong CF^*(L(d_1-r),L(d_2))$$ where $r\in \Z$ in case $L$, $r\in 2\Z$ in case $C$, and $r\in 3\Z$ in case $D$. This identification is compatible with the gradings, which shows that for $r > d_1 - d_2$, the Floer complex $CF^*(L(d_1),L(d_2);rH)$ is concentrated in degree zero, and so has vanishing differential. Recall that the generators of the last group are identified with $B(\frac{1}{d_2-d_1+r}\Z)$.

Once we are in the range $d_2-d_1 + r > 0$, we find that as $r$ increases, new generators are created, none are destroyed, and the generators that already exist are "compressed" toward the minimum of $H$. This gives rise to naive inclusion maps $i :
CF^*(L(d_1),L(d_2);rH) \to CF^*(L(d_1),L(d_2);r'H)$ for $r < r'$, where $r > d_1-d_2$. In terms of fractional integral points, this $i$ corresponds to the map $B(\frac{1}{d_2-d_1+r}\Z) \to
B(\frac{1}{d_2-d_1+r'}\Z)$ which is dilation by the appropriate factor centered at the point corresponding to the minimum of $H$.

We can index the points of $\hat{B}(\frac{1}{d}\Z)$ with two indices. The index $a\in \Z$ corresponds to the column lying at $\eta
= a/d$, while the index $i$ that indexes points within a column, and which lies in $\{0,\dots,\left\lfloor\frac{d-|a|}{2}\right\rfloor\}$ in the compact case, is now unbounded in the positive direction in case $L$, in the negative direction in case $C$, and in both directions in case $D$. We use the notation $q_{a,i}$ for these points.
