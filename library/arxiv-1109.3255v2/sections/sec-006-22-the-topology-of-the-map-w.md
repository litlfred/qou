---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-006-22-the-topology-of-the-map-w
section_title: "The topology of the map W"
section_number: 2.2
pages: 16-17
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.986
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:topology-W label="sec:topology-W"}

A direct computation shows that the superpotential $W$ given by [\[eq:main-lg-model\]](#eq:main-lg-model){reference-type="eqref" reference="eq:main-lg-model"} has three critical points $$\label{eq:W-crit-pts}
  \Crit(W) = \{(v = e^{\Lambda/3}e^{2\pi i (n/3)}, w = 1) \mid n = 0, 1, 2\},$$ and corresponding critical values $$\label{eq:W-crit-vals}
  \Critv(W) = \{3e^{-\Lambda/3}e^{-2\pi i (n/3)} \mid n = 0, 1, 2\}.$$ As expected, $\Critv(W)$ is the set of eigenvalues of quantum multiplication by $c_1(T\CP^2)$ in $QH^*(\CP^2)$, that is, multiplication by $3h$ in the ring $\C[h]/\langle h^3 = e^{-\Lambda}\rangle$.

::: proposition
Any regular fiber $W^{-1}(c) \subset X^\vee$ is a twice-punctured elliptic curve.
:::

::: proof
*Proof.* In the $(u,v)$ coordinates, $W^{-1}(c)$ is defined by the equation $$u + \frac{e^{-\Lambda}v^2}{uv-1} = c,$$ $$u(uv-1) + e^{-\Lambda}v^2 = c(uv-1).$$ This is an affine cubic plane curve, and it is disjoint from the affine conic $\{uv - 1=0\}$. It is smooth as long as $c$ is a regular value.

The projective closure of $W^{-1}(c)$ in $(u,v)$ coordinates is given by the homogeneous equation (with $\xi$ as the third coordinate) $$u(uv-\xi^2) + e^{-\Lambda}v^2\xi = c\xi(uv-\xi^2).$$ This is a projective cubic plane curve, hence elliptic, and it intersects the line at infinity $\{\xi = 0\}$ when $u^2v = 0$. So it is tangent to the line at infinity at $(u:v:\xi) = (0:1:0)$ and intersects it transversely at $(u:v:\xi) = (1:0:0)$. Hence the affine curve is the projective curve minus these two points. ◻
:::

::: remark
The function $W$ above is to be compared to the "standard" superpotential for $\CP^2$, namely, $$\label{eq:toric-W}
    W = x + y + \frac{e^{-\Lambda}}{xy}$$ corresponding to the choice of the toric boundary divisor, a union of three lines, as anticanonical divisor. This $W$ has the same critical values, and its regular fibers are all thrice-punctured elliptic curves. Hence smoothing the anticanonical divisor to the union of a conic and a line corresponds to compactifying one of the punctures of $W^{-1}(c)$.
:::
