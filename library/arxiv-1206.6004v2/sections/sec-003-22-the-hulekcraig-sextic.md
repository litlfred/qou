---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-003-22-the-hulekcraig-sextic
section_title: "The Hulek–Craig sextic"
section_number: 2.2
pages: 3-3
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.827
latex_coverage_ratio: 0.967
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
[]{#section2.2 label="section2.2"}

Hulek and Craig both introduce the sextic $$\label{craig}
  \mathcal{C}(\bar{x},\bar{y},\bar{z}) :=
    \bar{x}\big(\bar{y}^5+\bar{z}^5\big) + (\bar{x}\bar{y}\bar{z})^2 - \bar{x}^4\bar{y}\bar{z}-2(\bar{y}\bar{z})^3  = 0.$$ This curve is also of genus 4 and admits $A_5$ as a symmetry group[^1]. In this case an order five symmetry is obvious and we may take $$\overline{ab} : \ (\bar{x},\bar{y},\bar{z}) \mapsto \big(\zeta^2 \bar{x}, \zeta^4 \bar{y}, \bar{z}\big),$$ where $\zeta=\mathrm{e}^{2\pi\mathrm{i}/5}$. There is also a corresponding order two symmetry $$\overline{a} : \
  \begin{pmatrix}
    \bar{x}\\\bar{y}\\\bar{z}
  \end{pmatrix}
  \mapsto
  \begin{pmatrix}
    1 & 2                 & 2 \\
    1 & \zeta+\zeta^{-1}   & \zeta^2+\zeta^{-2} \\
    1 & \zeta^2+\zeta^{-2} & \zeta+\zeta^{-1}
  \end{pmatrix}
  \begin{pmatrix}
    \bar{x}\\\bar{y}\\\bar{z}
  \end{pmatrix}.$$ Together these generate $A_5$ again since $\overline{a}\overline{ab} =:
\overline{b}$ has order three (hence the slightly unusual choice of notation for $\overline{ab}$ above).

In fact the sextic ([\[craig\]](#craig){reference-type="ref" reference="craig"}) is also a model for Bring's curve using Dye's result and the following theorem.

::: theorem
With $A =
  \begin{pmatrix}
    j & 1              & 1 \\
    0 & -\mathrm{i}\sqrt{2+j} & \mathrm{i}\sqrt{2+j} \\
    1 & -j             & -j
  \end{pmatrix}$ then $\mathcal{D}(A\mathbf{x}) = -960(9 + 4\sqrt{5}) \mathcal{C}(\mathbf{x})$ and hence $\mathcal{D}(\mathbf{x}) = 0 \iff \mathcal{C}(A^{-1} \mathbf{x}) = 0$.
:::

This may be directly verified. The choice of the matrix $A$ follows upon consideration of the conjugacy classes of automorphisms of both models (see [@northover] for further details).

We observe that the antiholomorphic involution $[\bar{x},\bar{y},\bar{z}]\mapsto [\bar{x}\sp\ast,\bar{y}\sp\ast,\bar{z}\sp\ast]$ (where $\sp\ast$ is complex conjugation) is a symmetry of $\mathcal{C}$ though it is orientation-reversing and so not a conformal automorphism. This involution endows $\mathcal{C}$ with a real structure. The fixed point set of such a real structure is either empty or the disjoint union of simple closed curves, known as ovals following Hilbert's terminology [@begg]. A classical result of Harnack for a Riemann surface of genus $g$ with real structure says there are at most $g+1$ ovals. We shall show the the HK curve has one oval with this real structure.

[^1]: Here a bar over variables is used to distinguish them from the Dye curve, rather than to denote complex conjugation. Craig notes the results of Ramanujan [@berndtiii Chapter 19, Entry 10(iv), 10(vii)] entail the parameterization $$\begin{gathered}
    (\bar{x},\bar{y},\bar{z})
     =
    \left(\sum_{n=-\infty}\sp{\infty} q^{(5n)^2},\sum_{n=-\infty}\sp{\infty} q^{(5n+1)^2},
    \sum_{n=-\infty}\sp{\infty} q^{(5n+2)^2}\right).
    \end{gathered}$$
