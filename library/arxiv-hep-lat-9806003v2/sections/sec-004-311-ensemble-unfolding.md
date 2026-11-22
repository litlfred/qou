---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-004-311-ensemble-unfolding
section_title: "Ensemble unfolding"
section_number: 3.1.1
pages: 3-4
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 1.0
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 14 sections: Front matter; Introduction; Complete Dirac spectra in SU(2) ga"
---
\label{sec311}
In RMT one deals with an ensemble of matrices, where the matrix
elements of each member are chosen randomly. Spectral observables
predicted by RMT are calculated as an average over the ensemble.  This
ensemble average is denoted by a bar $\overline{(\ldots)}$.  But
observables can also be calculated as spectral average, i.e.  one
performs a running average over overlapping intervals
$[\alpha,\alpha+L]$ of length $L$ in the spectrum of one member.  In
order to distinguish it from ensemble average, we denote spectral
averaging by angular brackets $\langle\ldots\rangle$. In the limit of
large matrix dimension both averages are equivalent \cite{guhr97}.
This property is called ergodicity.

In most experiments, one measures one - preferably long - spectrum.
Thus observables are usually calculated from spectral average. One
uses the theoretical concept of ergodicity to compare the RMT
predictions with the experimental results.  In our case, however, the
data consists of configurations, i.e. forms an ensemble. Hence,
questions related to ergodicity arise not only for the calculation of
observables, but also in the determination of the staircase function,
i.e.~in the unfolding procedure.  We have in principle two very
different ways of unfolding our data: first, ensemble unfolding,
$N_{\rm ave}(\lambda)=\overline{N}(\lambda)$, i.e.~we determine the
smooth part of the staircase function by averaging over the ensemble,
and second, configuration unfolding, $N_{\rm ave}(\lambda)=\langle
N(\lambda)\rangle$, i.e.~we determine the smooth part of the staircase
function for every configuration separately. The results differ
considerably, $\overline{N}(\lambda)\neq\langle N(\lambda)\rangle$,
for most of the configurations.  The ensemble averaged staircase
$\overline{N}(\lambda)$ for the lattice QCD Dirac operator is shown in
Fig.~\ref{stair}.  We find $\overline{N}(\lambda)$ by dividing the
energy range in $m$ bins with width $\Delta\lambda$ and average the
density $\rho(\lambda,\lambda+\Delta\lambda)$ for each bin over all
configurations. We then calculate the staircase function as
$\overline{N}(\lambda)=\sum_{i=1}^m\rho(\lambda_i,
\lambda_i+\Delta\lambda)\Delta\lambda$, with $\lambda_m=\lambda$.  In
Fig.~\ref{ensemble}, the difference between the ensemble averaged
staircase function and the configuration wise averaged ones, for
$V=16^4$ and $\beta=2.4$, for 50 arbitrarily chosen configurations is
plotted.  Each data point represents the difference
$\overline{N}(\lambda_{i,j})-\langle N(\lambda_{i,j})\rangle$, where
$i$ enumerates the eigenvalues, $i=1,\ldots,32768$ and $j$ is the
configuration number $j=1,\ldots,50$. We plot only every 500th
eigenvalue.  There are deviations of about
$\overline{N}(\lambda)-\langle N(\lambda)\rangle={\cal O}(10^1)$ in
certain energy ranges.

If the spectra are unfolded using the ensemble averaged staircase
function $\overline{N}(\lambda)$, observables should then also be
calculated as an ensemble average for a fixed value of $\lambda$. But
we checked that our results do not depend on $\lambda$ in a wide range
of the bulk.  This property is called translational invariance. It is
actually not present in the microscopic region, where it is destroyed
by point wise symmetry between positive and negative eigenvalues
\cite{bitsch98}. Translational invariance in the bulk allows us to
calculate observables from running average over overlapping intervals
for each configuration. We choose an overlap of $90\%$ for two
consecutive intervals. Then we average over all configurations. This
improves the statistics of the result considerably.
