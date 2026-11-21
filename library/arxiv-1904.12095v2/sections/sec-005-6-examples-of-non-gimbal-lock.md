---
doc_id: arxiv-1904.12095v2
doc_title: "Veriﬁed computations for closed hyperbolic 3-manifolds"
section_id: sec-005-6-examples-of-non-gimbal-lock
section_title: "Examples of (non-)gimbal lock"
section_number: 6
pages: 14-15
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 1.0
doc_brief: "Verified computations for closed hyperbolic 3-manifolds — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed 3-manifold using"
---
[]{#section:examples label="section:examples"}

This section is giving examples where the condition $\Theta_e=2\pi$ from Theorem [\[thm:hypStruct\]](#thm:hypStruct){reference-type="ref" reference="thm:hypStruct"} is known to be fulfilled for most but not all edges. Let $\mathcal{T}$ be a finite, orientable triangulation with $o$ vertices and $m$ edges. We partition the edges as $E^\sim=\{e^\sim_1,\dots,e^\sim_l\}$ and $E^==\{e^=_1,\dots,e^=_{m-l}\}$ depending on whether we know that $\Theta_e$ is close to or, respectively, exactly equal to $2\pi$.

Geometrically, this yields a singular hyperbolic structure with cone singularities along the edges with $\Theta_{e^\sim_i}\not=2\pi$. Looking at a vertex $v$ connected to such an edge, its neighborhood is the hyperbolic cone of its link which is $S^2$ topologically but has a spherical cone structure different from the standard $S^2$. In this section, we extend Definition [\[def:trigGimbalFunction\]](#def:trigGimbalFunction){reference-type="ref" reference="def:trigGimbalFunction"} to the case where $l=|E^\sim|$ might not be $3o$ and say that gimbal lock is avoided if $Dg$ has no kernel.

::: example
[]{#example:singleEdgeViolation label="example:singleEdgeViolation"} Consider the case $l=1$ with $e^\sim_1$ connecting two distinct vertices $v_1$ and $v_2$. Assume $\Theta_{e^\sim_1}\not=2\pi$. The links of $v_1$ and $v_2$ would have a spherical cone structure with exactly one singularity. These do not exist, so $\Theta_{e'}=2\pi$. This also follows from Lemma [\[lemma:noGimbalImpliesAllEqnsVertexLink\]](#lemma:noGimbalImpliesAllEqnsVertexLink){reference-type="ref" reference="lemma:noGimbalImpliesAllEqnsVertexLink"}.
:::

::: example
[]{#ex:gimbalLockGeodesic label="ex:gimbalLockGeodesic"} Let us start with a (non-singular) hyperbolic structure on $\mathcal{T}$ such that the edges $e^\sim_1,\dots, e^\sim_l$ form a simple closed geodesic. Such a hyperbolic structure can often be deformed so that the geodesic becomes a cone singularity[^1], i.e., such that $\Theta_{e^\sim_1}=\cdots=\Theta_{e^\sim_l}$ are close but not equal to $2\pi$. Note that the spherical structure of the link of a vertex $v_i$ connected to $e^\sim_i$ and $e^\sim_{i+1}$ gets deformed to have two conical singularities at antipodal points with equal cone angle. In the language of cocycles, pick a gimbal loop $\Gamma_i$ for $v_i$ as in Definition [\[def:gimbalLoop\]](#def:gimbalLoop){reference-type="ref" reference="def:gimbalLoop"} such that the associated gimbal matrix is of the form $$\label{eqn:gimbalMatrixAntipodal}
m_{\Gamma_i}=R_{\Theta_{e^\sim_i}}\cdot \prod\nolimits_1 \cdot R_{\Theta_{e^\sim_{i+1}}}\cdot \prod\nolimits_1^{-1} = R_{\Theta_{e^\sim_i}} R_{-\Theta_{e^\sim_{i+1}}}$$ where $\prod_1\in\mathrm{SO}_{3}$ is a rotation by $\pi$ about an axis orthogonal to $z$. Then $m_{\Gamma_i}=\mathrm{Id}$ whenever $\Theta_{e^\sim_i}=\Theta_{e^\sim_{i+1}}$, so $Dg$ has a non-trivial kernel. If we add edges to $E^\sim$ such that $|E^\sim|=3o$, $Dg$ still has a non-trivial kernel, so we have gimbal lock and thus not a contradiction to Theorem [\[thm:mainThm\]](#thm:mainThm){reference-type="ref" reference="thm:mainThm"}.
:::

::: example
[]{#ex:avoidGimbalLockGeodesic label="ex:avoidGimbalLockGeodesic"} Consider the situation in the previous example but move one vertex, say $v_1$, slightly. Assume $\Theta_{e^\sim_1}\not=2\pi$. The link of $v_1$ would be a spherical cone structure with exactly two cone singularities having distance $<\pi$ (when scaling such that the curvature is $1$). Such a cone structure does not exist [@mondelloPanov Corollary 3.5]. In the language of cocycles, $\prod_1$ in Equation [\[eqn:gimbalMatrixAntipodal\]](#eqn:gimbalMatrixAntipodal){reference-type="ref" reference="eqn:gimbalMatrixAntipodal"} is now a rotation by an angle strictly between $0$ and $\pi$, so $m_{\Gamma_1}$ is the product of two rotations about two different axes and thus only the identity when $\Theta_{e^\sim_l}=\Theta_{e^\sim_{1}}=2\pi$. In fact, this forces $\Theta_{e^\sim_1}=\dots=\Theta_{e^\sim_l}=2\pi$.
:::

::: example
Consider the two tetrahedron triangulation of $S^3$ obtained by identifying the boundary of the first tetrahedron with the boundary of the second tetrahedron via the identity map. Assign the same length to all edges such that each tetrahedron has a hyperbolic structure individually but all of the six edges equations are violated. Perform several 1-4 moves on one or both of the tetrahedra preserving the hyperbolic structure on each tetrahedron. This gives an example of a non-hyperbolic manifold where more than $m-3o$ but not all edge equations are fulfilled. Compare this to the ideal case where Neumann-Zagier (see Appendix) state that all edge equations must be fulfilled whenever $m-o$ are fulfilled.
:::

We give a characterization of gimbal lock in 1-vertex triangulations later in Theorem [\[thm:singleVertexTriangulationGimbalLockCondition\]](#thm:singleVertexTriangulationGimbalLockCondition){reference-type="ref" reference="thm:singleVertexTriangulationGimbalLockCondition"}.

[^1]: For example, `Manifold("m003(-3.3,1.1)")` in SnapPy gives a geometric spun triangulation for the singular hyperbolic structure on the closed Weeks manifold `m003(-3,1)` with cone angle $2\pi/1.1$.
