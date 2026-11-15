---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-006-313-windowing
section_title: "Windowing"
section_number: 3.1.3
pages: 5-5
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 1.0
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 14 sections: Front matter; Introduction; Complete Dirac spectra in SU(2) ga"
---
\label{sec313}
Ideally, an unfolding procedure should only remove the global
variations of the spectral density, i.e. in our case the overall
behavior seen in Fig.~\ref{stair}. For reasons which will become
clearer later, it is difficult to numerically distinguish the global
variations from the local fluctuations. This is in particular the case
for data of large lattice size.  In other words, we might have removed
too much by some of the unfolding procedures, while we might have
removed too little by others. This will be discussed in great detail
below, especially in Sec.~\ref{sec35}.

One has to ensure that any deviations seen in the spectral statistics
are not due to global variations in the average density which were not
removed adequately. One way is to use different unfolding approaches
and compare the results carefully. Another way is to take only a small
window of the spectra in which the global variation of the density is
expected to be small.  Thus we choose an interval
$[\lambda,\lambda+\delta\lambda]$ and calculate the ensemble averaged
mean level spacing $D$ for it. We then rescale the eigenvalues in this
interval as
\begin{equation}
\xi_i=\lambda_i/D\quad,\quad
\lambda<\lambda_i<\lambda+\delta\lambda\;.
\end{equation}
This is done in the same manner as in \cite{ma97} where the
microscopic region was considered. However, it is not clear beforehand
that a scale in the spectra, if any, does not exceed the interval
length $\delta\lambda$. Unfolding, if done correctly, allows to make
investigations to much larger scales.

This approach is closely related to ensemble unfolding defined above.
Indeed, the results coincide, but with a less statistical significance
by only rescaling.  By using this approach, we intended to avoid any
unfolding procedures. As we will see later, there are a slight, but
still systematic variations of the spectral density within the small
window.
