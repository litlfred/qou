---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-008-3-action-growth-of-black-holes
section_title: "Action growth of black holes"
section_number: 3
pages: 16-16
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.985
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{sec:bh}

In this section, we will calculate the rate of increase of action of a Wheeler-DeWitt patch of the two-sided black hole (which we are conjecturing to be dual to the rate of growth of complexity of the boundary state).

We will consider the Einstein-Maxwell theory. The action is (using the conventions of \cite{Poisson})
 \begin{equation}
\CA =   \frac{1}{16 \pi G} \int_{\mathcal{M}}  \sqrt{|g|} \left( \mathcal{R} - 2 \Lambda  \right) - \frac{1}{16 \pi } \int_{\mathcal{M}}  \sqrt{|g|} F_{\mu \nu} F^{\mu \nu}  +  \frac{1}{8 \pi G} \int_{\partial \mathcal{M}} \sqrt{|h|} {K} , \label{eq:EinsteinHilbertActionForRealz}
\end{equation}
where the three terms are the Einstein-Hilbert (EH) action including a negative cosmological constant, the Maxwell electromagnetic action, and a York, Gibbons, Hawking (YGH) surface action.  In defining the extrinsic curvature $K$
 spacelike normals are taken to point outwards and timelike normals  inwards.

 A Reissner-Nordstrom-AdS black hole has metric
 \begin{eqnarray}
 ds^2 & = & - f(r)dt^2 + \frac{dr^2}{f(r)} + r^2 d \Omega_{D-2}^2 \\
f(r)  & = &   1 - \frac{8 \pi}{(D-2)\Omega_{D-2}} \frac{2 G M}{r^{D-3}} + \frac{8 \pi}{(D-2)\Omega_{D-2}} \frac{G Q^2 }{r^{2(D-3)}}+ \frac{r^2}{\lads^2} .
 \end{eqnarray}
Horizons occur where $f(r) =0.$ The radial coordinate at the (unique) horizon of a neutral black hole will be labeled
$r_h.$ The outer and inner horizons of the charged black hole are at $r_+$ and $r_-.$
