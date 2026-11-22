---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-011-33-lagrangians-fibered-over-paths
section_title: "Lagrangians fibered over paths"
section_number: 3.3
pages: 25-32
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.992
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:lags-construction label="sec:lags-construction"}

The base of the Lefschetz fibration is the annulus $X(I) = \{R^{-1}
\leq |w| \leq R\}$ with a critical value at $w = -1$. The symplectic structures constructed in [\[sec:focus-focus-lefschetz\]](#sec:focus-focus-lefschetz){reference-type="ref" reference="sec:focus-focus-lefschetz"} have the property that the symplectic connection is flat throughout the annuli $X(I_{-\epsilon}) = \{R^{-1} \leq |w| \leq e^{-\epsilon}\}$, $X(I_{+\epsilon}) = \{e^\epsilon \leq |w| \leq R\}$, as well as through a band along the positive real axis joining these annuli.

We call the Lagrangians $L(d)$ constructed here *sections*, because they will turn out to be sections of the torus fibration on $X(B)$. At the same time, they are *not* sections of the Lefschetz fibration, but rather fiber over paths in $X(I)$.

### The zero-section {#sec:zero-section}

The first step is to construct the Lagrangian submanifold $L(0)
\subset X(B)$, which we will use as a zero-section of the torus fibration and reference point through out the paper.

::: definition
Let $\ell(0) \subset X(I)$ be the path that runs along the positive real axis. Trivializing the fibration along that path, take a path in the fiber cylinder connecting the top and bottom boundary circles. The Lagrangian tori intersect the fibers of the Lefschetz fibration in circles, and we choose our fiber path so that it intersects each such circle once. We denote by $L(0) \subset X(B)$ the product Lagrangian submanifold.
:::

If we want to be specific, we could take the factor in the fiber to be the positive real locus of the coordinates $z_-$ or $z_+$. By construction, $L(0)$ intersects each Lagrangian torus once.

Once $L(0)$ is chosen, it selects leaves of the foliations by horizontal sections on each boundary face, namely those leaves containing the fiberwise boundary of $L(0)$. Call these leaves $\Sigma_0$ and $\Sigma_1$ (bottom and top respectively). Clearly we could have chosen these leaves first and then constructed $L(0)$ accordingly.

### The degree $d$ section {#sec:other-sections}

We can now use $L(0)$ as a reference to construct the other Lagrangians $L(d)$.

::: definition
Let $\ell(d)$ be a base path, with the same end points and midpoint as $\ell(0)$, and which winds $d$ times (relative to $\ell(0)$) in $X(I_{-\epsilon})$ and also $d$ times in $X(I_{+\epsilon})$. The winding of $\ell(d)$ is clockwise as we go from smaller to larger radius. The Lagrangian $L(d)$ is defined to coincide with $L(0)$ in the fiber over the common endpoint of $\ell(0)$ and $\ell(d)$ on the inner boundary circle of $X(I)$, and to be defined elsewhere as the submanifold swept out by symplectic parallel transport along the path $\ell(d)$.
:::

Recall that we cut off the corners of $B$ so that we actually have fibers at the endpoints of $\ell(0)$ and $\ell(d)$. Because the boundary leaves $\Sigma_0$ and $\Sigma_1$ are preserved by symplectic parallel transport, the boundary of $L(d)$ is contained in these same leaves, which as in Remark [\[rem:leaves-W\]](#rem:leaves-W){reference-type="ref" reference="rem:leaves-W"} correspond to hypersurfaces defined by the individual terms of the superpotential.

The behavior of $L(d)$ in the fiber direction is determined with the aid of Proposition [\[prop:key-properties\]](#prop:key-properties){reference-type="ref" reference="prop:key-properties"}.

::: proposition
[]{#prop:fiber-behavior label="prop:fiber-behavior"} As we parallel transport clockwise along $\ell(d)$ in inner annulus $X(I_{-\epsilon})$, the fiber component of $L(d)$ is transformed by half-right-handed Dehn twists, while as we parallel transport clockwise along $\ell(d)$ in the outer annulus $X(I_{+\epsilon})$, we pick up half-left-handed Dehn twists. In the end, all of the twisting cancels out, so that $L(d)$ and $L(0)$ again coincide over the common endpoint of $\ell(0)$ and $\ell(d)$ on the outer boundary circle of $X(I)$.
:::

The proposition is illustrated in Figure [1](#fig:lags-over-paths){reference-type="ref" reference="fig:lags-over-paths"}, which depicts $L(0)$, $L(1)$, and $L(2)$. The lower portion of the figure shows the base: the straight line is $\ell(0)$, while the spirals are $\ell(1)$ and $\ell(2)$. The marked point is the Lefschetz critical value. The upper portion of the figure shows the five fibers where $\ell(0)$ and $\ell(2)$ intersect. The behavior of $L(i)$ for $i = 0,1,2$ in these fibers is depicted.

![The Lagrangians $L(0)$, $L(1)$, and $L(2)$. Parts of the figure corresponding to $L(i)$ are labeled by $i$.](lags-over-paths){#fig:lags-over-paths width="3in"}

The Lagrangian submanifold $L(d)$ is indeed a section of the torus fibration. If $T_{R,\lambda}$ is the torus over the circle $\{|w| = R\}$ at height $\lambda$, then since $\ell(d)$ intersects $\{|w| = R\}$ at one point, there is exactly one fiber of $w:X(B)\to X(I)$, where $L(d)$ and $T_{R,\lambda}$ intersect. Since $L(d)$ intersects each $S^1$--orbit in that fiber once, we find that $L(d)$ and $T_{R,\lambda}$ indeed intersect once.

### Admissibility {#sec:admissibility}

We now explain in what sense these Lagrangians are admissible. The relevant notion of admissibility is the one found in [@auroux07 § 7.2], where admissibility with respect to a reducible hypersurface whose components correspond to the terms of the superpotential is discussed. In our case, we have two components $\Sigma_0$ and $\Sigma_1$, and the admissibility condition is that, near $\Sigma_i$, the holomorphic function $z_i$ such that $\Sigma_i =
\{z_i = 1\}$ satisfies $z_i|L \in \R$. The Lagrangian $L(d)$ will have this property if the symplectic structure is chosen so that the symplectic monodromy near $\Sigma_1$ is actually trivial, while the symplectic monodromy near $\Sigma_0$ is a rigid rotation by $\pi$. Otherwise, we can only say that the phase of $z_i$ varies within a small range near $\Sigma_i$. In the computations in section [\[sec:degeneration\]](#sec:degeneration){reference-type="ref" reference="sec:degeneration"} we actually perturb these Lagrangians in a prescribed manner near the boundary.

The notion of admissibility also prescribes the behavior over the endpoints of the base path $\ell(d)$. Recall that we cut off the corners of $B$ in order to define the symplectic structure. Our notion of admissibility remembers that there was a corner at this point, by requiring the $L(d)$ to coincide with $L(0)$ over the endpoints of $\ell(d)$. The justification for this is that, if we try to extend the geometry all the way to the corner of $B$, we see that the two components $\Sigma_0$ and $\Sigma_1$ would intersect, and we need the Lagrangian to behave tamely at this intersection. A local model for this sort of situation is the two complex curves $\Sigma_0 = \{x=0\}$, $\Sigma_1 = \{y= 0\}$ intersecting at $(0,0)$ in $\C^2$, with the Lagrangian being $L = (\R_{\geq 0})^2$, and with the fibration being $w = x+y : \C^2 \to \C$.

### Positive perturbations {#sec:pert}

The Lagrangians $L(d)$ constructed above intersect each other on the boundary of $X(B)$, and in particular it is not clear whether such intersection points are supposed count toward the Floer cohomology. There is a canonical way to perturb the Lagrangians so as to push all intersection points which should count toward Floer cohomology into the interior of $X(B)$, also used by Abouzaid [@abouzaid06]. This construction is not symmetric with respect to switching the Lagrangians.

Let $K$ and $L$ be two of the Lagrangians $L(d)$. The perturbation process we use in computing morphisms $CF^*(K,L)$ from $K$ to $L$ has two steps. First we perturb the Lagrangians near the boundary, staying within the class of Lagrangians fibering over paths, so that they intersect at the boundary in such way that the tangent space to the base path of $L$ is a small *counterclockwise* rotation of the tangent space to base path of $K$, and similarly in the fiber. If $K = L(d_1)$ and $L = L(d_2)$ with $d_1 < d_2$, this will create new intersection points in the interior, while if $d_1 > d_2$ the pair $K,L$ is already in the desired position.

The second step is that we perturb $K$ and $L$ at the boundary intersection so as to destroy the intersection there. Alternatively, we could just forget about the boundary intersection points in our computations, but actually removing them is more convenient in the technical part of the paper.

The pair of Lagrangians obtained from this process is called *positively perturbed*. This has the effect that one of Lagrangians in the pair may not admissible in the sense above, since it does not have boundary on $\Sigma_0$ and $\Sigma_1$. In section [\[sec:degeneration\]](#sec:degeneration){reference-type="ref" reference="sec:degeneration"}, the Lagrangians we work with are positive perturbations of admissible Lagrangians.

Please see figure [2](#fig:perturbation){reference-type="ref" reference="fig:perturbation"} for a local picture of the positive perturbation, and the end result in the case of $K = L(0)$ and $L = L(2)$.

![(a) The local picture of positive perturbation. (b) The end result when $K = L(0)$ and $L= L(2)$.](perturbation){#fig:perturbation width="3in"}

::: remark
The asymmetry in the perturbations is essential for the mirror symmetry statement that we wish to prove. Mirror symmetry predicts that $HF^*(L(d_1),L(d_2))$ is isomorphic to $\Ext^*(\cO_{\CP^2}(d_1),\cO_{\CP^2}(d_2)) \cong H^*(\CP^2,\cO_{\CP^2}(d_2-d_1))$. (The main purpose of the paper is to verify that this is true for $d_1 < d_2$ in a way compatible with the product structures.) Even at the level of total dimension, this space is not symmetric with respect to swapping $d_1$ and $d_2$, so it makes sense that we must treat intersection points differently depending on whether we consider them to be morphisms from $L(d_1)$ to $L(d_2)$ or vice versa.

While we only discuss the product $\mu^2$ on Floer cohomology in this paper, it would be possible to use this sort of perturbation in the definition of higher $A_\infty$ operations, and to define a Fukaya category, by adapting the analogous constructions in Abouzaid's work [@abouzaid06; @abouzaid09].
:::

### Gradings and degrees {#sec:gradings}

We now explain how the degrees of the intersection points between the positively perturbed Lagrangians $L(d)$ is determined. Our conventions follow Seidel [@seidel-book §11]. We choose a smooth trivialization of the canonical bundle of $X(B)$ given by a complex volume form $\Omega$. Our $X(B)$ is diffeomorphic to the manifold $X^\vee$ considered in section [\[sec:fiber-superpotential\]](#sec:fiber-superpotential){reference-type="ref" reference="sec:fiber-superpotential"}, which carries the volume form $$\Omega_{X^\vee} = \frac{du \wedge dv}{w} = \frac{du}{u} \wedge \frac{dw}{w}$$ having the convenient property that, away from the singular fiber of the Lefschetz fibration, $\Omega_{X^\vee}$ decomposes as a wedge product of one-forms with respect to the local product structure determined by the coordinates $(u,w)$. We can transfer this form over to $X(B)$, and deform it to a complex volume form $\Omega$ that is compatible with the fibration structure, in the sense that, when $\Omega$ is restricted to the tangent space of a point on a smooth fiber, it decomposes into a wedge product of a one-form on the vertical tangent space and a one-form on the horizontal space.

We can also describe the trivialization determined by $\Omega$ in terms of the foliation by the tori $T_{R,\lambda}$. The tangent space to $X(B)$ at any point is the complexification of the tangent space to the torus $T_{R,\lambda}$ passing through that point, so an orientation on $T_{R,\lambda}$ trivializes the canonical bundle of $X(B)$ along that torus. Since all of these tori can be oriented in a consistent manner, we obtain a trivialization of the canonical bundle over the complement of the critical point in $X(B)$. This trivialization is homotopic to the one determined by $\Omega$ for the following reason. The holomorphic volume form $\Omega_{X^\vee}$ on $X^\vee$ admits a family of special Lagrangian tori, which means precisely that $\Omega_{X^\vee}$ restricted to each torus is a real volume form times a constant phase factor. When we transfer $\Omega_{X^\vee}$ over to $X(B)$, this foliation by special Lagrangian tori goes over to a foliation by tori that is isotopic to the foliation by the tori $T_{R,\lambda}$. (The fact that the tori are Lagrangian is not important here, only that they are totally real.) The foliation by the tori $T_{R,\lambda}$ is also compatible with the fibration structure, as each torus fibers over a circle in the base $X(I)$ and intersects each fiber in a circle. Thus we obtain foliations by circles on the base and the fiber.

The point of these choices is that we will be able to compute the degrees of our intersection points in terms of amounts of rotation with respect to the circle foliations on the base and the fiber. Because the Lagrangian $L(d)$ satisfies $H^1(L(d)) = 0$, it admits gradings. Moreover, because it fibers over a path in the base, and consists of a path in each fiber, it may be graded separately in the base and fiber directions. To say what we mean by this, recall the notion of a *squared phase map* from [@seidel-book]. This is the map $$\alpha_{L(d)} : L(d) \to S^1, \quad \alpha_{L(d)}(p) = \frac{\Omega(v_1\wedge v_2)^2}{|\Omega(v_1\wedge v_2)|^2}$$ where $\{v_1, v_2\}$ is a basis of $T_pL(d)$. A grading is then a real-valued lift $\tilde{\alpha}_{L(d)}: L(d) \to \R$ such that $\exp(2\pi i \tilde{\alpha}_{L(d)}) = \alpha_{L(d)}$. In our situation, we can decompose this squared phase map into base and fiber components $$\alpha_{L(d)}^b,\  \alpha_{L(d)}^f : L(d) \to S^1$$ such that $\alpha_{L(d)} = \alpha_{L(d)}^b\cdot \alpha_{L(d)}^f$, such that $\alpha_{L(d)}^b$ is the squared phase with respect to the foliation by circles on the base, and $\alpha_{L(d)}^f$ is the squared phase with respect to the foliation by circles on the fiber. Normalizing and homotoping the volume form $\Omega$ if necessary, we may assume that the squared phase of the torus $T_{R,\lambda}$ is $1 \in S^1$ for all three versions, and so that the squared phase of $L(0)$ is $-1 \in S^1$ for both $\alpha^b$ and $\alpha^f$ (and hence its total phase is $\alpha = 1$).

Now, if we set $d > 0$, and we consider $L(d)$, we find that the tangent space of $L(d)$, in either the base or fiber, is obtained from that of $T_{R,\lambda}$ by a small counterclockwise rotation. This means that $\alpha_{L(d)}^b$ and $\alpha_{L(d)}^f$ lie on the upper half circle between $1$ and $-1$ in $S^1$.

Next, choose lifts $\tilde{\alpha}^b$ and $\tilde{\alpha}^f$ for the base and fiber squared phase maps of the manifolds $L(d)$ for $d \geq 0$, preferring values the interval $[0,1]$. Note that $L(0)$ has $$\tilde{\alpha}_{L(0)}^b = \tilde{\alpha}_{L(0)}^f = \frac{1}{2}$$ For the other $L(d)$ with $d > 0$ the value of $\tilde{\alpha}_{L(d)}^b$ will always lie in the interval $(0,\frac{1}{2})$, while the value of $\tilde{\alpha}^f$ lies in the interval $(0,1)$, since the intersection of $L(d)$ with any fiber is always a path that is transverse to the foliation by circles.

Finally, with the gradings in place, we can compute the degrees of the intersection points between $L(0)$ and $L(d)$ for $d > 0$.

::: proposition
Suppose $d_1 < d_2$. The the Floer complex $CF^*(L(d_1),L(d_2))$ of the positively perturbed pair $L(d_1), L(d_2)$ is concentrated in degree zero. The Floer complex $CF^*(L(d_2)), L(d_1))$ for the positively perturbed pair $L(d_2),L(d_1)$ is concentrated in degree two.
:::

::: proof
*Proof.* Let us first consider the case $d_1 = 0$ and $d_2 = d > 0$. Using the local splitting given by the fibration, this degree is a sum of contributions from the base and fiber. Since the base and fiber are complex one-dimensional, the base and fiber contributions are for $p \in L(0) \cap L(d)$ using [@seidel-book Eq. 11.35], $$\begin{aligned}
  i^b(L(0),L(d),p) & = [\tilde{\alpha}^b_{L(d)}-\tilde{\alpha}^b_{L(0)}]+1\\
 i^f(L(0),L(d),p) & = [\tilde{\alpha}^f_{L(d)} - \tilde{\alpha}^f_{L(0)}]+1
\end{aligned}$$d where $[\cdot]$ denotes the greatest integer function. Look at the diagram shows that, at any intersection point $p$, the quantity inside the $[\cdot]$ is negative, as the tangent space to $L(d)$ is a small *clockwise* rotation of the tangent space to $L(0)$. Thus both $i^b(L(0),L(d),p)$ and $i^f(L(0),L(d),p)$ are zero, and the total degree is zero.

If we keep $d > 0$, but swap the roles of $L(0)$ and $L(d)$, we find that $$\begin{aligned}
  i^b(L(d),L(0),p) & = [\tilde{\alpha}^b_{L(0)}-\tilde{\alpha}^b_{L(d)}]+1 = 1\\
  i^f(L(d),L(0),p) & = [\tilde{\alpha}^f_{L(0)} - \tilde{\alpha}^f_{L(d)}]+1 = 1
\end{aligned}$$ so that the intersection point $p$, regarded as a morphism from $L(d)$ to $L(0)$, has degree 2.

A similar analysis shows that the degrees of intersections $L(d_1)\cap L(d_2)$, regarded as a morphism from $L(d_1)$ to $L(d_2)$, depends on $d_2 - d_1$. If $d_2 - d_1$ is positive, they have degree $0$, while if $d_2 - d_1$ is negative, they have degree $2$. ◻
:::

Since, in each case, the complex is concentrated in a single degree, the differential vanishes, and we may identify the complex $CF^*(L(d_1),L(d_2))$ with its cohomology $HF^*(L(d_1),L(d_2))$.

### Intersection points and integral points {#sec:intersections}

With the above prescription for perturbing the Lagrangians $L(d)$, we now work out the bijection between the intersection points of $L(0)$ and $L(d)$ for $d>0$, regarded as morphisms from $L(0)$ to $L(d)$, and the $(1/d)$-integral points of $B$.

::: proposition
Let $B$ be scaled so that the top face has length $2$. Take $d > 0$. Then the intersection points $L(0) \cap L(d)$ giving a basis of $CF^0(L(0),L(d))$ correspond to $(1/d)$-integral points of $B$, including those on the boundary of $B$. For $d < 0$, the intersection points giving a basis of $CF^2(L(0),L(d))$ correspond the same set but with points on the boundary of $B$ excluded. For the pair $L(d_1),L(d_2)$, the same conclusion holds with $d = d_2 - d_1$.
:::

This proposition is proved by explicitly indexing all of the various points. We start at the intersection point of $\ell(0)$ and $\ell(d)$ near the inner radius of the annulus $X(I)$. This intersection point survives the perturbation. In the fiber over this point there is one intersection point that survives after perturbation. As we transport around the inner part of the annulus, we pick up half-twists in the fiber (Proposition [\[prop:fiber-behavior\]](#prop:fiber-behavior){reference-type="ref" reference="prop:fiber-behavior"}), which increases the number of intersection points by one after every two turns in the base. This pattern continues until $\ell(d)$ reaches the middle radius and starts winding around the other side of the Lefschetz singularity, where the pattern reverses. (See Figure [1](#fig:lags-over-paths){reference-type="ref" reference="fig:lags-over-paths"}.)

Assign the rational numbers $$[-1,1] \cap (1/d)\Z = \{-1,
-(d-1)/d,\dots, -1/d, 0, 1/d, \dots, 1\}$$ to the intersection points of $\ell(0)$ and $\ell(d)$, then over the point indexed by $a/d$ the number of intersection points in the fiber is $1+\left\lfloor\frac{d-|a|}{2}\right\rfloor$. We index the points in a given fiber using the index $i \in \{0,1,\dots, \left\lfloor\frac{d-|a|}{2}\right\rfloor\}$, starting at the top of the fiber.

If we scale $B$ so that the top face has affine length $2$, the $1/d$ integral points of $B$ are also organized by the projection $\eta: B \to I$ into columns indexed by $[-1,1] \cap (1/d)\Z$. By inspection, the column over $a/d$ has $1+ \left\lfloor\frac{d-|a|}{2}\right\rfloor$ points. These are also indexed by $i \in \{0,1,\dots, \left\lfloor\frac{d-|a|}{2}\right\rfloor\}$, starting at the top of the fiber.

Under this bijection the $(1/d)$-integral points on the boundary of $B$ correspond to intersections of the unperturbed $L(0)$ and $L(d)$ that lie on the boundary of $X(B)$. According to our definition of positive perturbation, these points do (do not) contribute when $d > 0$ ($d < 0$).

::: definition
[]{#def:indexing label="def:indexing"} Take $d > 0$. For $a \in \{-d,\dots,d\}$, and $i \in
\{0,1,\dots,\left\lfloor\frac{d-|a|}{2}\right\rfloor\}$, let $q_{a,i}(n)
\in L(n)\cap L(n+d)$ be the intersection which lies in the column indexed by $a/d$, and which is the $i$th from the top of the fiber.
:::

We can already verify mirror symmetry at the level of the Hilbert polynomial: $$\label{eq:hilbert-poly}
  |L(0)\cap L(d)| = \left|B\left(\frac{1}{d}\Z\right)\right| =
  \frac{(d+2)(d+1)}{2} = \dim H^0(\CP^2, \cO_{\CP^2}(d))$$

Figure [3](#fig:intersections){reference-type="ref" reference="fig:intersections"} shows the points of $B(\frac{1}{4}\Z)$ representing the basis of morphisms $L(d) \to L(d+4)$.

![The $1/4$--integral points of $B$.](intersections){#fig:intersections width="3in"}

### Hamiltonian isotopies {#sec:ham-iso}

There is an alternative way to express the relationship between $L(d)$ and $L(0)$, which is by a Hamiltonian isotopy. There is a Hamiltonian function $H$ on $X(B)$ such that the time-$d$ flow of $H$ takes $L(0)$ to $L(d)$. During the intermediate times of this isotopy the Lagrangian will not be admissible (or even close to it), but at the end of the isotopy admissibility is restored. This observation is used when we consider wrapped Floer cohomology in section [\[sec:complements\]](#sec:complements){reference-type="ref" reference="sec:complements"}.

This isotopy also allows us to identify the intersection points $L(n)\cap L(n+d)$ for different values of $n$. For this reason, we will write $q_{a,i}(n)$ as simply $q_{a,i}$.
