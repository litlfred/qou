---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-010-42-riera-and-rodríguez-basis
section_title: "Riera and Rodríguez basis"
section_number: 4.2
pages: 7-9
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.859
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
[]{#section4.2 label="section4.2"}

We start by recapitulating the hyperbolic basis of interest. Riera and Rodrı́guez begin with a simple non-canonical basis. They first define $$\begin{gathered}
  \alpha_1  = 1 + 2, \qquad
  \alpha_2  = 3 + 4
\end{gathered}$$ (in edge traversal notation, see [@rauch; @riera]) and then act on these cycles by rotations of $\frac{2\pi k}{5}$ to obtain their initial basis. So essentially $$\alpha_i = (2i-1) + (2i).$$

Next they specify (by fiat) a matrix which transforms these $\alpha_i$ into a canonical basis and proceed to derive further basis change to make use of the symmetries. The end result is the following basis-change matrix (implicit in [@riera]) $$\label{basistrans}
  \begin{pmatrix}
  1 & 0  & 0 & 0  & -2 & 0 & 1  & 0  \\
  1 & -1 & 0 & -1 & -1 & 1 & 1  & 1  \\
  1 & -1 & 0 & 0  & -1 & 2 & 1  & -1 \\
  0 & -1 & 0 & 0  & 1  & 2 & 0  & 0  \\
  1 & -1 & 1 & 0  & -1 & 1 & -1 & -1 \\
  1 & -1 & 1 & -1 & 0  & 0 & -1 & 1  \\
  1 & -1 & 1 & -1 & 0  & 1 & 0  & 1  \\
  0 & -1 & 0 & -1 & 1  & 1 & 1  & 2
  \end{pmatrix},$$ which sends the initial $\alpha_1,\dots,\alpha_{8}$ homology basis to another $\{\mathfrak{a}_i,\mathfrak{b}_i\}_{i=1}\sp{4}$, that is not only canonical but behaves well with respect to the symmetry group of the curve. Now the symmetries relate the periods $\mathcal{A}_{ij}=\int_{\mathfrak{a}_i}v_j$ and $\mathcal{B}_{ij}=\int_{\mathfrak{b}_i}v_j$ (for any basis of holomorphic differentials $v_i$). As a consequence, the period matrix $\tau=\mathcal{B}\mathcal{A}\sp{-1}$ can be written as [\[RRstau\]](#RRstau){reference-type="eqref" reference="RRstau"}, where $\tau_0 \approx -0.5+0.185576\mathrm{i}$ is defined in terms of Klein's $j$-invariants[^1] by $$\begin{gathered}
\label{deftau0}
  j(\tau_0) = -\frac{29^3\times 5}{2^5}, \qquad
  j(5\tau_0) = -\frac{25}{2}.
\end{gathered}$$

[^1]: Riera and Rodrı́guez swap these two equations. However, we believe this to be a typographical error.
