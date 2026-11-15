---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-019-46-figure-eight-knot
section_title: "Figure-eight knot"
section_number: 4.6
pages: 39-42
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.987
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:gauge41 label="sec:gauge41"}

As our final example, we consider the theory associated to a manifold with a torus cusp boundary: the complement of the figure-eight knot $M=S^3\backslash\mathbf{4_1}$.

The minimal triangulation of $M$ into two tetrahedra, discussed in Section [\[sec:cuspbdy\]](#sec:cuspbdy){reference-type="ref" reference="sec:cuspbdy"}, has two internal edges and both of them are hard:

$$C_1 = 2Z+Z''+2W+W''\,,\qquad C_2 = 2Z'+Z''+2W'+W'' \,.$$

We could certainly try to write down a gauge theory from this triangulation. Indeed, starting with $T_{\Delta_Z,\Pi_{Z'}}\otimes T_{\Delta_W,\Pi_W}$, we can change the polarization to $\widetilde\Pi$ with (positions; momenta)$=(U,C_1;v,\Gamma)$, where $U=Z'-W$, $v=Z-Z'$ as in [\[Uv41\]](#Uv41){reference-type="eqref" reference="Uv41"}, and $\Gamma_1=-W$ is the conjugate to $C_1$. The resulting theory $T^{(2)}_{\mathbf{4_1},\tilde\Pi}$ is a $U(1)$ gauge theory with two chiral matter fields both of charge $+1$, and no dynamical Chern-Simons coupling. The factors in the global symmetry group $U(1)_{\rm vector}\times U(1)_{\rm top}$ correspond to position coordinates $\tfrac12U$ and $-C_1-\tfrac32U$, respectively. Explicitly, we find a Lagrangian

$$\begin{aligned}
\mathcal{L}^{(2)}_{\mathbf{4_1},\tilde\Pi}[V_U,V_{C_1}] &= \frac{1}{4\pi}\int d^4\theta\,\Big(-\frac32 \Sigma_U V_U-(2\Sigma_{C_1}+3\Sigma_U)V\Big) \notag \\
 &\hspace{1in} +\int d^4\theta \big( \phi_{Z'}^\dagger e^{V+V_U}\phi_{Z'}+ \phi_W^\dagger e^{V} \phi_W\big)\,,
\label{41tet2}
\end{aligned}$$

with $V$ dynamical. Unfortunately, we are hard-pressed to find two monopole operators $\mathcal{O}_{C_1},\,\mathcal{O}_{C_2}$ in this theory that could be added to a superpotential. Their existence is crucial to break the (essentially topological) $U(1)_{C_1}$ symmetry, to set $V_{C_1}\to 0$ and to complete the gluing procedure.

![The torus cusp for the figure-eight knot complement, triangulated into six tetrahedra. The cyclic order of edge parameters $(z,z',z'')$, etc., is always the same, so we only indicate one parameter per vertex triangle.](cusp6){#fig:cusp6 width="5in"}

To resolve this problem, we must resolve the triangulation. For example, we have found a decomposition of the figure-eight knot complement into six tetrahedra, such that all internal edges are easy. We sketch a developing map of the resulting cusp neighborhood in Figure [1](#fig:cusp6){reference-type="ref" reference="fig:cusp6"}, from which we read off the six internal edge coordinates

[^1]

$$\begin{array}{l@{\qquad}l} C_1 = X+W+2(R'+S'+Z'')\,, &
C_2 = R+Y+2(Z'+W'+S'')\,, \\
C_3 = S+W+2(R''+X''+Y')\,, &
C_4 = R+Z+2(Y''+W''+X')\,, \\
C_5 = X+Y\,, &
C_6 = S+Z\,.
\end{array}$$

We also find eigenvalues for the meridian and longitude cycles on the boundary $T^2$,

$$U = S'+R'-X''+Y''-W'+Z''\,,\qquad v = X+R'-S-R''\,.$$

Using the combinatorial data for this gluing, it is straightforward (if tedious) to follow the rules of Section [\[sec:defTM\]](#sec:defTM){reference-type="ref" reference="sec:defTM"} to define the actual figure-eight knot theory $T_{\mathbf{4_1},\Pi}$, where $\Pi$ has position $U$ and momentum $v$. This theory has six operators $\mathcal{O}_{C_1},...,\mathcal{O}_{C_6}$ that can be added to the superpotential to break the $U(1)$ symmetries corresponding to the internal edges.

# Moduli space on ${\mathbb R}^2\times S^1$ {#sec:moduli}

One simple way to test the correspondence $M \longleftrightarrow  T_M$ is to associate a moduli space to each side. In the analogous construction [@Gaiotto-dualities] of the 4d $\mathcal{N}=2$ superconformal theory from a Riemann surface $\mathcal{C}$, there is a similar test of the correspondence $\mathcal{C}\longleftrightarrow T(\mathcal{C})$ based on comparing the moduli space of complex (equivalently, conformal) structures on $\mathcal{C}$ with the moduli space of marginal couplings of the theory $T(\mathcal{C})$.

In the present case, there is a similar test of the correspondence $M  \longleftrightarrow T_M$ based on comparing moduli spaces of complex flat connections on $M$ and the moduli space of supersymmetric vacua of the theory $T_M$. To be more precise, the space of complex flat connections on $M$ can be identified with the space of SUSY moduli in the theory $T_M$ on ${\mathbb R}^2 \times S^1$ [@DGH]: $$\boxed{\phantom{\int}
\mathcal{M}_{{\rm flat}} (M,SL(2,{\mathbb C})) \; = \; \mathcal{M}_{{\rm SUSY}} (T_M)\,.
\phantom{\int}}
\label{MMclaim}$$ While the definition of the moduli space $\mathcal{M}_{{\rm flat}} (M,SL(2,{\mathbb C}))$ is clear (and was reviewed in section [\[sec:geom\]](#sec:geom){reference-type="ref" reference="sec:geom"}) we need to properly interpret the right-hand side of [\[MMclaim\]](#MMclaim){reference-type="eqref" reference="MMclaim"}.

Upon compactification on ${\mathbb R}^2\times S^1$, the $\mathcal{N}=2$ theory $T_M$ becomes effectively two-dimensional. Supersymmetry then requires that the vevs of chiral and twisted chiral fields, whether dynamical or not, are complex valued. For example, 3d real mass parameters associated to a background $U(1)$ gauge multiplet $V$ become complexified by the holonomies of the background photon on $S^1$. Therefore, moduli spaces parametrized by vevs of chiral and twisted chiral fields are always complex manifolds. Here, we are mostly interested in the moduli space parameterized by vevs of twisted chiral fields --- the descendants of 3d gauge multiplets --- and denote this space $\mathcal{M}_{\rm SUSY}$.

For example, if $M$ is a closed 3-manifold without boundaries or cusps, the corresponding field theory $T_M$ on ${\mathbb R}^2 \times S^1$ has the moduli space of supersymmetric vacua $\mathcal{M}_{{\rm SUSY}} (T_M)$ obtained by minimizing the twisted superpotential $\widetilde{\mathcal{W}}$. Since the twisted superpotential is a holomorphic function, the variety defined by the equations $\partial \widetilde{\mathcal{W}}=0$ is a complex variety, just like the moduli space of flat $SL(2,{\mathbb C})$ connections on $M$.

More generally, if $M$ is a 3-manifold with boundary $\mathcal{C}= \partial M$, it is natural to project the moduli space $\mathcal{M}_{{\rm flat}} (M,SL(2,{\mathbb C}))$ onto the moduli space of flat connections on $\mathcal{C}$, *i.e.* consider those flat connections on $\mathcal{C}$ which can be extended to all of $M$. In Section [\[sec:geom\]](#sec:geom){reference-type="ref" reference="sec:geom"}, this projection was cut out by the Lagrangian submanifold

$$\mathcal{L}_M\;\subset\;\mathcal{P}_{\partial M} = \mathcal{M}_{\rm flat}(\mathcal{C},SL(2,{\mathbb C}))\,.$$

Correspondingly, in the $\mathcal{N}=2$ gauge theory $T_M$, it is natural to ask for which values of the parameters $v_i$ (= vevs of non-dynamical fields) the theory $T_M$ has SUSY vacua on ${\mathbb R}^2 \times S^1$. In order to answer this question, we introduce the effective twisted superpotential $\widetilde{\mathcal{W}}_{{\rm eff}}$ obtained by minimizing $\widetilde{\mathcal{W}}$ with respect to all *dynamical* fields, and then define [@DG-Sdual]:

$$\mathcal{M}_{\rm SUSY}^{\text{(param)}}(T_M)\,:\quad u_i = \frac{\partial \widetilde{\mathcal{W}}_{{\rm eff}}}{\partial v_i} \,.
\label{uidef}$$

In the the case where $v_i$ is the twisted mass in a background $U(1)$ gauge field, the coordinate $u_i$ should be thought of as the background FI parameter for this field; then it is clear that [\[uidef\]](#uidef){reference-type="eqref" reference="uidef"} is the condition for unbroken supersymmetry. As we illustrate in a number of examples below, $\widetilde{\mathcal{W}}_{{\rm eff}}$ is a transcendental function, generically a sum of dilogarithm functions. However, after taking the derivatives in [\[uidef\]](#uidef){reference-type="eqref" reference="uidef"} and introducing the new coordinates

$$\ell_i = e^{v_i}\,, \qquad m_i = e^{u_i}
\label{lmviauv}$$

(which are natural, because the complexified vevs $u_i$ and $v_i$ are periodic), one finds a nice algebraic variety that is identical to $\mathcal{L}_M$.

Geometrically, it should be clear that the Lagrangian submanifold $\mathcal{L}_M$ cannot depend on the coordinates and polarization used to describe the phase space $\mathcal{P}_{\partial M}$ when $M$ has a boundary. Changing coordinates will simply re-parametrize $\mathcal{L}_M$. Similarly, the space $\mathcal{M}_{\rm SUSY}^{(\rm param)}(T_{M,\Pi})$ should not depend on the polarization $\Pi$ (or boundary triangulation, etc.) used in previous sections to define a theory $T_{M,\Pi}$. One way to see this is to interpret $T_{M,\Pi}$ on ${\mathbb R}^2\times S^1$ as describing a boundary condition $\mathcal{B}[T_{M,\Pi}]$ for a 4d $\mathcal{N}=2$ theory $T[\mathcal{C}]$ ($\mathcal{C}=\partial M$) compactified on ${\mathbb R}^3\times S^1$, as in Section [\[sec:gauge4d\]](#sec:gauge4d){reference-type="ref" reference="sec:gauge4d"}. With a little bit of work, one can show that the coordinates $\ell_i,\, m_i$ become boundary values of natural coordinates (*e.g.* $\mathcal{X}_E$ of [@GMN; @GMNII]) on the moduli space of the compactified 4d theory. From this point of view, $\mathcal{M}_{\rm SUSY}^{(\rm param)}(T_M)=\mathcal{L}_M$ becomes a complex Lagrangian submanifold in the four-dimensional moduli space

[^2]

$\mathcal{M}_{\rm SUSY}(T[\mathcal{C}])\simeq \mathcal{P}_{\partial M}$. This Lagrangian characterizes the boundary condition itself, rather than any specific realization of it via a 3d SCFT. In particular, changing the polarization $\Pi$ merely shifts the duality frame of the combined 4d-3d system, and must map $\mathcal{M}_{\rm SUSY}^{(\rm param)}(T_M)$ to an isomorphic space.\
The present discussion of supersymmetric vacua, particularly as given by equations [\[uidef\]](#uidef){reference-type="eqref" reference="uidef"} with $\widetilde W$ a sum of dilogarithm functions, is highly reminiscent of recent work relating effective 2d field theories to quantum integrable systems [@NS-I; @NShatashvili; @NRS]. For example, 3d $\mathcal{N}=2$ theories much like $T_{M}$ compactified on a circle are related to the XXZ spin chain. A precise connection between our present constructions and integrable systems would be very interesting, but has yet to be established.

[^1]: We invite the reader to check that this triangulation produces the same A-polynomial as in [\[A41\]](#A41){reference-type="eqref" reference="A41"}.

[^2]: As discussed (*e.g.*) in [@GMN; @GMNII], this 4d moduli space actually has the structure of a hyperkahler manifold. The space $\mathcal{M}_{\rm SUSY}^{(\rm param)}(T_M)$ is then embedded into $\mathcal{M}_{\rm SUSY}(T[\mathcal{C}])$ as a brane of type $(A,B,A)$.
