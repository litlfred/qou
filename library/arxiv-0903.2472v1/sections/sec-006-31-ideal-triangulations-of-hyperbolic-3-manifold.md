---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-006-31-ideal-triangulations-of-hyperbolic-3-manifold
section_title: "Ideal triangulations of hyperbolic 3-manifolds"
section_number: 3.1
pages: 27-33
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.858
latex_coverage_ratio: 0.978
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
[]{#sec:ideal label="sec:ideal"}

The construction of a state integral model described in the rest of this section applies to orientable hyperbolic 3-manifolds of finite volume (possibly with boundary) and uses ideal triangulations in a crucial way. Therefore, we begin this section by reviewing some relevant facts from hyperbolic geometry (more details can be found in [@thurston-1980; @thurston-1982; @thurston-1999]).

Recall that hyperbolic 3-space ${\mathbb{H}}^3$ can be represented as the upper half-space $\{(x_1,x_2,x_3) \vert$ $x_3>0 \}$ with metric [\[hthreemetric\]](#hthreemetric){reference-type="eqref" reference="hthreemetric"} of constant curvature $-1$. The boundary $\partial {\mathbb{H}}^3$, topologically an ${\bf S}^2$, consists of the plane $x_3=0$ together with the point at infinity. The group of isometries of ${\mathbb{H}}^3$ is $PSL(2,{\mathbb{C}})$, which acts on the boundary via the usual Möbius transformations. In this picture, geodesic surfaces are spheres of any radius which intersect $\partial {\mathbb{H}}^3$ orthogonally.

An ideal tetrahedron $\Delta$ in ${\mathbb{H}}^3$ has by definition all its faces along geodesic surfaces, and all its vertices in $\partial {\mathbb{H}}^3$ --- such vertices are called *ideal points*. After Möbius transformations, one can fix three of the vertices at $(0,0,0)$, $(1,0,0)$, and infinity. The coordinate of the fourth vertex $(x_1,x_2,0)$, with $x_2\geq 0$, defines a complex number $z=x_1 + i x_2$ called the *shape parameter* (sometimes also called *edge parameter*). At various edges, the faces of the tetrahedron $\Delta$ form dihedral angles $\arg z_j$ ($j=1,2,3$) as indicated in Figure [\[fig:ideal\]](#fig:ideal){reference-type="ref" reference="fig:ideal"}, with

$$z_1 = z\,, \quad z_2 = 1-\frac{1}{z}\,, \quad z_3 = \frac{1}{1-z}\,.  \label{zj}$$

The ideal tetrahedron is noncompact, but has finite volume given by $$\label{volviad} {\mbox{Vol\,}}(\Delta_z) \;=\; D(z)\,,$$ where $D(z)$ is the Bloch-Wigner dilogarithm function, related to the usual dilogarithm $\text{Li}_2$ (see Section [\[sec:qdilog\]](#sec:qdilog){reference-type="ref" reference="sec:qdilog"}) by $$\label{BW} D(z) = {\rm Im}\,\bigl(\text{Li}_2(z)\bigr) + \arg(1-z)\,\log |z|\,.$$ Note that any of the $z_j$ can be taken to be the shape parameter of $\Delta$, and that $D(z_j) = {\mbox{Vol\,}}(\Delta_z)$ for each $j$. We will allow shape parameters to be any complex numbers in ${\mathbb{C}}-\{0,1\}$, noting that for $z\in{\mathbb{R}}$ an ideal tetrahedron is degenerate and that for ${\rm Im}\,\,z<0$ it technically has negative volume due to its orientation.

An ideal tetrahedron in ${\mathbb{H}}^3$. []{#fig:ideal label="fig:ideal"}

A hyperbolic structure on a 3-manifold is a metric that is locally isometric to ${\mathbb{H}}^3$. A 3-manifold is called hyperbolic if it admits a hyperbolic structure that is geodesically complete and has finite volume. Most 3-manifolds are hyperbolic, including the vast majority of knot and link complements in ${\bf S}^3$. Specifically, a knot complement is hyperbolic as long as the knot is not a torus or satellite knot [@thurston-1986]. Every closed 3-manifold can be obtained via Dehn surgery on a knot in ${\bf S}^3$, and for hyperbolic knots all but finitely many such surgeries yield hyperbolic manifolds [@thurston-1980].

By the Mostow rigidity theorem [@mostow-1973; @prasad-1973], the complete hyperbolic structure on a hyperbolic manifold is unique. Therefore, geometric invariants like the hyperbolic volume are actually topological invariants. For the large class of hyperbolic knot complements in ${\bf S}^3$, the unique complete hyperbolic structure has a parabolic holonomy with unit eigenvalues around the knot. In $SL(2,{\mathbb{C}})$ Chern-Simons theory, this structure corresponds to the "geometric" flat connection ${\cal A}^{({\rm geom})}$ with $u=0$. As discussed in Section [\[sec:loops\]](#sec:loops){reference-type="ref" reference="sec:loops"}, hyperbolic manifolds with complete hyperbolic structures can also be described as quotients $\mathbb{H}^3/\Gamma$.

Given a hyperbolic knot complement, one can deform the hyperbolic metric in such a way that the holonomy $u$ is not zero. Such deformed metrics are unique in a neighborhood of $u=0$, but they are not geodesically complete. For a discrete set of values of $u$, one can add in the "missing" geodesic, and the deformed metrics coincide with the unique complete hyperbolic structures on closed 3-manifolds obtained via appropriate Dehn surgeries on the knot in ${\bf S}^3$. For other values of $u$, the knot complement can be completed by adding either a circle $S^1$ or a single point, but the resulting hyperbolic metric will be singular. For example, if $u\in i{\mathbb{R}}$ one adds a circle and the resulting metric has a conical singularity. These descriptions can easily be extended to link complements (*i.e.* multiple cusps), using multiple parameters $u_k$, one for each link component.

Any orientable hyperbolic manifold $M$ is homeomorphic to the interior of a compact 3-manifold $\bar{M}$ with boundary consisting of finitely many tori. (The manifold $M$ itself can also be thought of as the union of $\bar{M}$ with neighborhoods of the cusps, each of the latter being homeomorphic to $T^2\times [0,\infty)$.) All hyperbolic manifolds therefore arise as knot or link complements in closed 3-manifolds. Moreover, every hyperbolic manifold has an ideal triangulation, *i.e* a finite decomposition into (possibly degenerate[^1]) ideal tetrahedra; see *e.g.* [@thurston-1980; @petronio-2000].

To reconstruct a hyperbolic 3-manifold $M$ from its ideal triangulation $\{\Delta_i\}_{i=1}^N$, faces of tetrahedra are glued together in pairs. One must remember, however, that vertices of tetrahedra are not part of $M$, and that the combined boundaries of their neighborhoods in $M$ are not spheres, but tori. (Thus, some intuition from simplicial triangulations no longer holds.)

There always exists a triangulation of $M$ whose edges can all be oriented in such a way that the boundary of every face (shared between two tetrahedra) has two edges oriented in the same direction (clockwise or counterclockwise) and one opposite. Then the vertices of each tetrahedron can be canonically labeled 0, 1, 2, 3 according to the number of edges entering the vertex, so that the tetrahedron can be identified in a unique way with one of the two numbered tetrahedra shown in Figure [\[fig:tetr_momenta\]](#fig:tetr_momenta){reference-type="ref" reference="fig:tetr_momenta"} of the next subsection. This at the same time orients the tetrahedron. The orientation of a given tetrahedron $\Delta_i$ may not agree with that of $M$; one defines $\epsilon_i=1$ if the orientations agree and $\epsilon_i=-1$ otherwise. The edges of each tetrahedron can then be given shape parameters $(z^{(i)}_1,z^{(i)}_2,z^{(i)}_3)$, running counterclockwise around each vertex (viewed from outside the tetrahedron) if $\epsilon_i=1$ and clockwise if $\epsilon_i=-1$.

For a given $M$ with cusps or conical singularities specified by holonomy parameters $u_k$, the shape parameters $z_j^{(i)}$ of the tetrahedra $\Delta_i$ in its triangulation are fixed by two sets of conditions. First, the product of the shape parameters $z_j^{(i)}$ at every edge in the triangulation must be equal to 1, in order for the hyperbolic structures of adjacent tetrahedra to match. More precisely, the sum of some chosen branches of $\log z_j^{(i)}$ (equal to the standard branch if one is near the complete structure) should equal $2\pi i$, so that the total dihedral angle at each edge is $2\pi$. Second, one can compute holonomy eigenvalues around each torus boundary in $M$ as a product of $z_j^{(i)}$'s by mapping out the neighborhood of each vertex in the triangulation in a so-called developing map, and following a procedure illustrated in, *e.g.*, [@nz-1985]. There is one distinct vertex "inside" each boundary torus. One then requires that the eigenvalues of the holonomy around the $k$th boundary are equal to $e^{\pm u_k}$. These two conditions will be referred to, respectively, as *consistency* and *cusp* relations.

Every hyperbolic 3-manifold has a well-defined class in the Bloch group [@neumann-1997]. This is a subgroup

[^2]

of the quotient of the free ${\mathbb{Z}}$-module ${\mathbb{Z}}[{\mathbb{C}}-\{0,1\}]$ by the relations $$-[y]+[\frac{y}{x}]-[\frac{1-x^{-1}}{1-y^{-1}}]+[\frac{1-x}{1-y}]=0\,. \label{FT}$$

This five-term or pentagon relation accounts for the fact that a polyhedron with five ideal vertices can be decomposed into ideal tetrahedra in multiple ways. The five ideal tetrahedra in this polyhedron (each obtained by deleting an ideal vertex) can be given the five shape parameters $x,\,y,\,y/x,...$ appearing above. The signs of the different terms correspond to orientations. Geometrically, an instance of the five-term relation can be visualized as the 2-3 Pachner move, illustrated in Figure [\[fig:Pachner\]](#fig:Pachner){reference-type="ref" reference="fig:Pachner"}.

The 2-3 Pachner move. []{#fig:Pachner label="fig:Pachner"}

The class $[M]$ of a hyperbolic 3-manifold $M$ in the Bloch group can be computed by summing (with orientation) the shape parameters $[z]$ of any ideal triangulation, but it is *independent* of the triangulation. Thus, hyperbolic invariants of 3-manifolds may be obtained by functions on the Bloch group --- *i.e.* functions compatible with [\[FT\]](#FT){reference-type="eqref" reference="FT"}. For example, the Bloch-Wigner function [\[BW\]](#BW){reference-type="eqref" reference="BW"} satisfies

$$D(x)-D(y)+D\big(\frac{y}{x}\big)-D\big(\frac{1-x^{-1}}{1-y^{-1}}\big)+D\big(\frac{1-x}{1-y}\big)=0\,,$$

and the hyperbolic volume of a manifold $M$ triangulated by ideal tetrahedra $\{\Delta_i\}_{i=1}^{N}$ can be calculated as

$${\mbox{Vol\,}}(M) = \sum_{i=1}^{N}\epsilon_i D(z^{(i)})\,. \label{VolM}$$

The symbols $\epsilon_i$ here could be removed if shape parameters were assigned to tetrahedra in a manner independent of orientation, noting that reversing the orientation of a tetrahedron corresponds to sending $z\mapsto 1/z$ and that $D(1/z)=-D(z)$. This is sometimes seen in the literature.

The complexified volume $i({\mbox{Vol\,}}(M)+i{\rm CS}(M))$ is trickier to evaluate. For a hyperbolic manifold with a spin structure, corresponding to full $SL(2,{\mathbb{C}})$ holonomies, this invariant is defined modulo $4\pi^2$. Here, we will outline a computation of the complexified volume modulo $\pi^2$, following [@neumann-2004]; for the complete invariant modulo $4\pi^2$, see [@zickert-2008]. To proceed, one must first make sure that the three shape parameters $z^{(i)}=z_1^{(i)}$, $z_2^{(i)}$, and $z_3^{(i)}$ are specifically assigned to edges $[v_1^{(i)},v_2^{(i)}]$, $[v_1^{(i)},v_3^{(i)}]$, and $[v_1^{(i)},v_2^{(i)}]$ (respectively) in each tetrahedron $\Delta_i$ of an oriented triangulation of $M$, where $[v_a^{(i)},v_b^{(i)}]$ denotes the edge going from numbered vertex $v_a^{(i)}$ to numbered vertex $v_b^{(i)}$. One also chooses logarithms $(w_1^{(i)},w_2^{(i)},w_3^{(i)})$ of the shape parameters such that

$$\begin{align}& e^{w^{(i)}_1}=\pm z^{(i)}_1\,,\quad e^{w^{(i)}_2}=\pm z^{(i)}_2\,, \quad e^{w^{(i)}_3}=\pm z^{(i)}_3\,, \\
& w^{(i)}_1+w^{(i)}_2+w^{(i)}_3 = 0\quad \forall\,i\,,
\end{align}$$

and defines integers $(q^{(i)},r^{(i)})$ by

$$w_1^{(i)}={\rm Log}(z^{(i)})+\pi i q^{(i)}\,,\qquad w_2^{(i)}=-{\rm Log}(1-z^{(i)})+\pi i r^{(i)}\,,$$

where ${\rm Log}$ denotes the principal branch of the logarithm, with a cut from $0$ to $-\infty$. For a consistent labeling of the triangulation, called a "combinatorial flattening," the sum of log-parameters $w^{(i)}_j$ around every edge must vanish, and the (signed[^3]) sum of log-parameters along the two paths generating $\pi_1(T^2)={\mathbb{Z}}^2$ for any boundary (cusp) $T^2$ must equal twice the logarithm of the $SL(2,{\mathbb{C}})$ holonomies around these paths.

[^4]

The complexified volume is then given, modulo $\pi^2$, as

$$i({\mbox{Vol\,}}(M)+i {\rm CS}(M)) \,=\, \sum_{i=1}^N \epsilon_i {\rm L}(z^{(i)};q^{(i)},r^{(i)}) - \sum_{{\rm cusps}\,k}(v_k\overline{u}_k+i\pi u_k)\,, \label{CSVolM}$$

with

$${\rm L}(z;q,r) = \text{Li}_2(z)+\frac{1}{2}({\rm Log}(z)+\pi i q)({\rm Log}(1-z)+\pi i r) + \frac{\pi^2qr}{2} - \frac{\pi^2}{6}\,. \label{RogersL}$$

The function ${\rm L} (z;q,r)$, a modified version of the Rogers dilogarithm, satisfies a five-term relation in an extended Bloch group that lifts [\[FT\]](#FT){reference-type="eqref" reference="FT"} in a natural way to the space of log-parameters. [^5]

## Hikami's invariant {#sec:Hikami}

We can now describe Hikami's geometric construction. Roughly speaking, to compute the invariant for a hyperbolic manifold $M$, one chooses an ideal triangulation of $M$, assigns an infinite-dimensional vector space $V$ or $V^*$ to each tetrahedron face, and assigns a matrix element in $V\otimes V\otimes V^* \otimes V^*$ to each tetrahedron. These matrix elements depend on a small parameter $\hbar$, and in the classical $\hbar \to 0$ limit they capture the hyperbolic structure of the tetrahedra. The invariant of $M$ is obtained by taking inner products of matrix elements on every pair of identified faces (gluing the tetrahedra back together), subject to the cusp conditions described above in the classical limit.

To describe the process in greater detail, we begin with an orientable hyperbolic manifold that has an oriented ideal triangulation $\{\Delta_i\}_{i=1}^N$, and initially forget about the hyperbolic structures of these tetrahedra. As discussed in Section [\[sec:ideal\]](#sec:ideal){reference-type="ref" reference="sec:ideal"} and indicated in Figure [\[fig:tetr_momenta\]](#fig:tetr_momenta){reference-type="ref" reference="fig:tetr_momenta"}, each tetrahedron comes with one of two possible orientations of its edges, which induces an ordering of its vertices $v_j^{(i)}$ (the subscript $j$ here is not to be confused with the shape parameter subscript in [\[zj\]](#zj){reference-type="eqref" reference="zj"}), an ordering of its faces, and orientations on each face. The latter can be indicated by inward or outward-pointing normal vectors. The faces (or their normal vectors) are labelled by $p_j^{(i)}$, in correspondence with opposing vertices. The normal face-vectors of adjacent tetrahedra match up head-to-tail (and actually define an oriented dual decomposition) when tetrahedra are glued to form $M$.

Oriented tetrahedra, to which matrix elements $\langle p_1,p_3|{\bf S}|p_2,p_4\rangle$ (left) and $\langle p_2,p_4|{\bf S}^{-1}|p_1,p_3\rangle$ (right) are assigned. []{#fig:tetr_momenta label="fig:tetr_momenta"}

Given such an oriented triangulation, one associates a vector space $V$ to each inward-oriented face, and the dual space $V^*$ to each outward-oriented face. (Physicists should think of these spaces as "Hilbert" spaces obtained by quantizing the theory on a manifold with boundary.) The elements of $V$ are represented by complex-valued functions in one variable, with adjoints given by conjugation and inner products given by integration. Abusing the notation, but following the very natural set of conventions of [@hikami-2001-16; @hikami-2006], we denote these complex variables by $p_j^{(i)}$, which we used earlier to label the corresponding faces of the tetrahedra. As a result, to the boundary of every tetrahedron $\Delta_i$ one associates a vector space $V\otimes V\otimes V^* \otimes V^*$, represented by functions of its four face labels, $p_1^{(i)}$, $p_2^{(i)}$, $p_3^{(i)}$, and $p_4^{(i)}$.

To each tetrahedron one assigns a matrix element $\langle p_1,p_3|{\bf S}|p_2,p_4\rangle$ or $\langle p_2,p_4|{\bf S}^{-1}|p_1,p_3\rangle$, depending on orientation as indicated in Figure [\[fig:tetr_momenta\]](#fig:tetr_momenta){reference-type="ref" reference="fig:tetr_momenta"}. Here, the matrix ${\bf S}$ acts on functions $f(p_1,p_2) \in V\otimes V$ as $${\bf S} \;=\; e^{\hat{q}_1\hat{p}_2/2\hbar}\; \Phi_\hbar ( \hat{p}_1 + \hat{q}_2 - \hat{p}_2)\,,
\label{S-matrix}$$ where $\hat{p}_i f =p_i f$ and $\hat{q}_i f = 2\hbar \frac{\partial}{\partial p_i} f$. The function $\Phi_\hbar$ is the quantum dilogarithm, to be described in the next subsection. Assuming that $\int \frac{idq}{4\pi\hbar} |q \rangle \langle q| = \int dp\, |p\rangle \langle p| = 1$ and $\langle p | q \rangle = e^{\frac{pq}{2i\hbar}}$ (the exact normalizations are not important for the final invariant), one obtains via Fourier transform $$\begin{aligned}
\langle p_1,p_3|{\bf S}|p_2,p_4\rangle
& = \frac{\delta(p_1 + p_3 - p_2)}{\sqrt{-4\pi i\hbar}} \Phi_{\hbar} (p_4 - p_3 + i\pi + \hbar)
\, e^{\frac{1}{2\hbar} \left( p_1 (p_4 - p_3) + \frac{i\pi\hbar}{2} - \frac{\pi^2-\hbar^2}{6} \right) }\,,
\label{S_element1} \\
\langle p_2,p_4|{\bf S}^{-1}|p_1,p_3\rangle
& = \frac{\delta(p_1 + p_3 - p_2)}{\sqrt{-4\pi i\hbar}} \frac{1}{\Phi_{\hbar}
(p_4 - p_3 - i\pi-\hbar)} e^{\frac{1}{2\hbar} \left( p_1 (p_3 - p_4) - \frac{i\pi\hbar}{2}
+ \frac{\pi^2-\hbar^2}{6} \right)}\,.
\label{S_element2}
\end{aligned}$$ In the classical limit $\hbar \to 0$, the quantum dilogarithm has the asymptotic $\Phi_\hbar(p)\sim \frac{1}{2\hbar} \text{Li}_2(-e^p)$. One therefore sees that the classical limits of the above matrix elements look very much like exponentials of $\frac{1}{2\hbar}$ times the complexified hyperbolic volumes of tetrahedra. For example, the asymptotic of [\[S_element1\]](#S_element1){reference-type="eqref" reference="S_element1"} coincides with $\exp(L(z;\cdot,\cdot)/(2\hbar))$ if we identify $e^{p_4-p_3}$ with $z$ and $e^{-2p_1}$ with $1/(1-z)$. For building a quantum invariant, however, only half of the variables $p_j$ really "belong" to a single tetrahedron. Hikami's claim [@hikami-2001-16; @hikami-2006] is that if we only identify a shape parameter

$$z^{(i)} = e^{p_4^{(i)}-p_3^{(i)}}\,,
\label{z_and_p}$$

for every tetrahedron $\Delta_i$, the classical limit of the resulting quantum invariant will completely reproduce the hyperbolic structure and complexified hyperbolic volume on $M$.

[^6]

To finish calculating the invariant of $M$, one glues the tetrahedra back together and takes inner products in every pair $V$ and $V^*$ corresponding to identified faces. This amounts to multiplying together all the matrix elements [\[S_element1\]](#S_element1){reference-type="eqref" reference="S_element1"} or [\[S_element2\]](#S_element2){reference-type="eqref" reference="S_element2"}, identifying the $p^{(i)}_j$ variables on identified faces (with matching head-to-tail normal vectors), and integrating over the $2N$ remaining $p$'s. To account for possible toral boundaries of $M$, however, one must revert back to the hyperbolic structure. This allows one to write the holonomy eigenvalues $\{ e^{u_k} \}$ as products of shape parameters $(z^{(i)},\,1-1/z^{(i)},\,1/(1-z^{(i)}))$, and, using [\[z_and_p\]](#z_and_p){reference-type="eqref" reference="z_and_p"}, to turn every cusp condition into a linear relation of the form $\sum p$'s$\, = 2u_k$. These relations are then inserted as delta functions in the inner product integral, enforcing global boundary conditions. In the end, noting that each matrix element [\[S_element1\]](#S_element1){reference-type="eqref" reference="S_element1"}-[\[S_element2\]](#S_element2){reference-type="eqref" reference="S_element2"} also contains a delta function, one is left with $N-b_0(\Sigma)$ nontrivial integrals, where $b_0 (\Sigma)$ is the number of connected components of $\Sigma = \partial M$. For example, specializing to hyperbolic 3-manifolds with a single torus boundary $\Sigma = T^2$, the integration variables can be relabeled so that Hikami's invariant takes the form $$\begin{aligned}
H (M; \hbar, u)
& = \frac{1}{(4\pi\hbar)^{N/2}} \int\,
\prod_{i=1}^{N} \Phi_{\hbar} \big( \, g_i ({\bf p}, 2u) +\epsilon_i (i \pi + \hbar) \,\big)^{\epsilon_i}
\,e^{f({\bf p}, 2u, \hbar)/2\hbar}\; dp_1 \ldots dp_{N-1}\,.
\label{gen_Hik_integral}
\end{aligned}$$ The $g_i$ are linear combinations of $(p_1, \ldots, p_{N-1},2u)$ with integer coefficients, and $f$ is a quadratic polynomial, also with integer coefficients for all terms involving $p_k$'s or $u$. In the classical limit, this integral can naively be evaluated in a saddle point approximation, and Hikami's claim is that the saddle point relations coincide precisely with the consistency conditions for the triangulation on $M$. There is more to this story, however, as we will see in Section [\[sec:statesumdef\]](#sec:statesumdef){reference-type="ref" reference="sec:statesumdef"}.

[^1]: It is conjectured and widely believed that nondegenerate tetrahedra alone are always sufficient.

[^2]: Namely, the kernel of the map $[z]\mapsto 2z\wedge(1-z) \in {\mathbb{C}}^*\wedge_{\mathbb{Z}}{\mathbb{C}}^*$ acting on this quotient module.

[^3]: Signs arise from tetrahedron orientations and the sense in which a path winds around edges; see [@neumann-2004], Def. 4.2.

[^4]: []{#foot:v2pi label="foot:v2pi"}Explicitly, in the notation of Section [\[sec:quantization\]](#sec:quantization){reference-type="ref" reference="sec:quantization"} and above, the sum of log-parameters along the two paths in the neighborhood of the $k$th cusp must equal $2u_k$ and $2v_k+2\pi i$, respectively.

[^5]: The branch of $\text{Li}_2$ in [\[RogersL\]](#RogersL){reference-type="eqref" reference="RogersL"} is taken to be the standard one, with a cut from $1$ to $+\infty$. Note, however, that we could also take care of ambiguities arising from the choice of dilogarithm branch by rewriting [\[RogersL\]](#RogersL){reference-type="eqref" reference="RogersL"} in terms of the function $\tilde{\rm L}(w)=\int_{-\infty}^w \frac{t\,dt}{1-e^{-t}}$. This is a well-defined holomorphic function :${\mathbb{C}}\rightarrow {\mathbb{C}}/4\pi^2{\mathbb{Z}}$ because all the residues of $t/(1-e^t)$ are integer multiplies of $2\pi i$, and it coincides with a branch of the function $\text{Li}_2(e^w)+w\log(1-e^w)$.

[^6]: Eqn. [\[z_and_p\]](#z_and_p){reference-type="eqref" reference="z_and_p"} is a little different from the relation appearing in [@hikami-2001-16; @hikami-2006], because our convention for assigning shape parameters to edges based on orientation differs from that of [@hikami-2001-16; @hikami-2006].
