---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-008-32-hikamis-invariant
section_title: "Hikami's invariant"
section_number: 3.2
pages: 32-34
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.949
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
[]{#sec:Hikami label="sec:Hikami"}

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

[^1]

To finish calculating the invariant of $M$, one glues the tetrahedra back together and takes inner products in every pair $V$ and $V^*$ corresponding to identified faces. This amounts to multiplying together all the matrix elements [\[S_element1\]](#S_element1){reference-type="eqref" reference="S_element1"} or [\[S_element2\]](#S_element2){reference-type="eqref" reference="S_element2"}, identifying the $p^{(i)}_j$ variables on identified faces (with matching head-to-tail normal vectors), and integrating over the $2N$ remaining $p$'s. To account for possible toral boundaries of $M$, however, one must revert back to the hyperbolic structure. This allows one to write the holonomy eigenvalues $\{ e^{u_k} \}$ as products of shape parameters $(z^{(i)},\,1-1/z^{(i)},\,1/(1-z^{(i)}))$, and, using [\[z_and_p\]](#z_and_p){reference-type="eqref" reference="z_and_p"}, to turn every cusp condition into a linear relation of the form $\sum p$'s$\, = 2u_k$. These relations are then inserted as delta functions in the inner product integral, enforcing global boundary conditions. In the end, noting that each matrix element [\[S_element1\]](#S_element1){reference-type="eqref" reference="S_element1"}-[\[S_element2\]](#S_element2){reference-type="eqref" reference="S_element2"} also contains a delta function, one is left with $N-b_0(\Sigma)$ nontrivial integrals, where $b_0 (\Sigma)$ is the number of connected components of $\Sigma = \partial M$. For example, specializing to hyperbolic 3-manifolds with a single torus boundary $\Sigma = T^2$, the integration variables can be relabeled so that Hikami's invariant takes the form $$\begin{aligned}
H (M; \hbar, u)
& = \frac{1}{(4\pi\hbar)^{N/2}} \int\,
\prod_{i=1}^{N} \Phi_{\hbar} \big( \, g_i ({\bf p}, 2u) +\epsilon_i (i \pi + \hbar) \,\big)^{\epsilon_i}
\,e^{f({\bf p}, 2u, \hbar)/2\hbar}\; dp_1 \ldots dp_{N-1}\,.
\label{gen_Hik_integral}
\end{aligned}$$ The $g_i$ are linear combinations of $(p_1, \ldots, p_{N-1},2u)$ with integer coefficients, and $f$ is a quadratic polynomial, also with integer coefficients for all terms involving $p_k$'s or $u$. In the classical limit, this integral can naively be evaluated in a saddle point approximation, and Hikami's claim is that the saddle point relations coincide precisely with the consistency conditions for the triangulation on $M$. There is more to this story, however, as we will see in Section [\[sec:statesumdef\]](#sec:statesumdef){reference-type="ref" reference="sec:statesumdef"}.

[^1]: Eqn. [\[z_and_p\]](#z_and_p){reference-type="eqref" reference="z_and_p"} is a little different from the relation appearing in [@hikami-2001-16; @hikami-2006], because our convention for assigning shape parameters to edges based on orientation differs from that of [@hikami-2001-16; @hikami-2006].
