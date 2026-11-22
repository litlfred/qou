---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-002-21-dyes-sextic
section_title: "Dye's sextic"
section_number: 2.1
pages: 2-3
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.812
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
[]{#section2.1 label="section2.1"}

Let $j = \frac{1+\sqrt{5}}{2}$, a root of $j^2=j+1$. Dye [@dye] introduces the plane sextic curves given by $$\begin{gathered}
  \mathcal{D}_\lambda(x,y,z) :=
  (x+jy)^6 + (x-jy)^6 + (y+jz)^6  \\
\hphantom{\mathcal{D}_\lambda(x,y,z) :=}{}    + (y-jz)^6 + (z+jx)^6 + (z-jx)^6 + \lambda\big(x^2+y^2+z^2\big)^3 = 0.
\end{gathered}$$ For generic $\lambda\in\mathbb{C}$ the curve has genus 10, but if $\lambda$ is chosen to be $-\frac{78+104j}{5}$ then the genus drops to 4 and the resulting curve is shown to be equivalent to Bring's. We correspondingly define $$\mathcal{D}(x,y,z) := \mathcal{D}_{-\frac{78+104j}{5}}(x,y,z).$$ The curve $\mathcal{D}(x,y,z)$ has the obvious order three cyclic symmetry $$b' : \ (x,y,z) \mapsto (y,z,x),$$ as well as the less obvious order two symmetry $$a' : \
  \begin{pmatrix}
    x\\y\\z
  \end{pmatrix}
  \mapsto
  \begin{pmatrix}
    -j  & 1    & j^2 \\
    1   & -j^2 & j \\
    j^2 & j    & 1
  \end{pmatrix}
  \begin{pmatrix}
    x\\y\\z
  \end{pmatrix},$$ both presented by Dye in his paper. It is easy to check that these are the classical generators for $A_5$: $$a'b' =
  \begin{pmatrix}
    j^2 & -j  & 1 \\
    j   & 1   & -j^2 \\
    1   & j^2 & j
  \end{pmatrix}$$ has order five and (taking into account the projective nature of the space) $$a'^2 = b'^3 = (a'b')^5 = 1.$$
