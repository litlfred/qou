---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-001-2-complete-dirac-spectra-in-su2-gauge-theory
section_title: "Complete Dirac spectra in SU(2) gauge theory"
section_number: 2
pages: 2-2
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.993
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 14 sections: Front matter; Introduction; Complete Dirac spectra in SU(2) ga"
---
\label{sec2}

The computation of large ensembles of complete spectra of the
Euclidean Dirac operator for staggered fermions in SU(2) gauge theory
has recently been performed Ref.\cite{MBB98} expanding the numerical
work of \cite{Kalk95}. In lattice gauge theory simulations one
generates a sequence of gauge field configurations distributed
according to the Boltzmann weight. On each of the gauge field
configurations the eigenvalue equation (\ref{eq1}) is solved
numerically on the lattice and a distinct partition of eigenvalues is
obtained.  The lattices have the size $V=L^4$ where $L$ denotes the
length of the Euclidean box with a lattice spacing $a$.  Parameters
and statistics of the simulation are summarized in Table\ref{tab1}.
The choice of SU(2) as the gauge group implies that every eigenvalue
of $i\slash D$ is twofold degenerate due to a global charge
conjugation symmetry. The random--matrix ensemble for this situation
has symplectic symmetry and is referred to as chiral Gaussian
Symplectic Ensemble (chGSE) \cite{verbaar94,guhr97}.  In addition, the
squared Dirac operator $-\slash D^2$ couples only even to even and odd
to odd lattice sites, respectively.  Thus, $-\slash D^2$ has $V/2$
distinct eigenvalues.  We use the Cullum--Willoughby version of the
Lanczos algorithm \cite{Stoe93} to compute the complete eigenvalue
spectrum of the sparse hermitian matrix $-\slash D^2$ in order to
avoid numerical uncertainties for the low-lying eigenvalues.  There
exists an analytical sum rule, ${\rm tr}(-\slash D^2) = 4V$, for the
distinct eigenvalues of $-\slash D^2$ \cite{Kalk95}.  We have checked
that this sum rule is satisfied by our data, the largest relative
deviation was about $10^{-8}$.

Examples of the spectra are shown in Fig.~\ref{stair}, where the
average level density and the integrated average level density, see
Eq.~(\ref{staircase}), for a $16^4$, i.e.~$L=16a$, lattice are shown.
It should be pointed out that due to the $V/2=32768$ distinct
eigenvalues of each configuration there are millions of eigenvalues at
our disposal. We used two different values of the gauge coupling
$\beta=4/g^2$ where the weak coupling regime of SU(2) sets in and
where most of the scaling test have been performed so far.  Finally,
the chiral condensate was obtained by fitting the spectral density and
extracting $\rho(0)$.  Our findings \cite{MBB98} are in rough
agreement with the values obtained by Hands and Teper \cite {Hands90}
for the same simulation parameters in SU(2) but only the 20 smallest
eigenvalues have been computed by these authors.
