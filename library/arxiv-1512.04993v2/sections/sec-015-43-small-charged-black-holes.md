---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-015-43-small-charged-black-holes
section_title: "Small charged black holes"
section_number: 4.3
pages: 23-24
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 1.0
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{sec:smallchargedblackholescomplexity}
We may also test our conjecture with electric charge. The bound of \S\ref{sec:conserved-charge} is now
\be
\frac{d \CC}{dt} \leq \frac{2}{\pi \hbar} \left[ (M - \mu Q) -(M-\mu Q)_\textrm{gs} \right] .
\label{masterform2}
\ee
We will now apply this formula to charged black holes that are much smaller than the AdS radius ($r_+ \ll \lads$), for which
\bea
f(r) &=& 1 -\frac{2GM}{r} + \frac{GQ^2}{r^2} = \frac{(r-r_+)(r-r_-)}{r^2}.
\eea
These have
\begin{equation}
GM = \frac{r_+ + r_-}{2}  \ \ \ \ \& \ \ \ \ GQ^2 = r_+ r_-.
\end{equation}
The chemical potential is
\be
\mu = \frac{Q}{r_+}.
\ee
For a given $\mu$, the smallest value of $M- \mu Q$ is zero (at leading semiclassical order), achieved by empty space $M=Q =0$. Thus the ground state contribution to \eqref{masterform2} vanishes and we find,
\bea
 (M - \mu Q) -(M-\mu Q)_\textrm{gs}  &=& \frac{r_+ + r_-}{2G} -\frac{Q^2}{r_+} = \frac{r_+ - r_-}{2G} = \sqrt{M^2 -\frac{Q^2}{G}} .
\eea




Small charged black holes exactly saturate the complexification bound in Eq.~\ref{C-bound}.
