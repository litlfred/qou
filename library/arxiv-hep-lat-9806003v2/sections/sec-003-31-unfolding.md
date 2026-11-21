---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-003-31-unfolding
section_title: "Unfolding"
section_number: 3.1
pages: 3-3
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.977
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 14 sections: Front matter; Introduction; Complete Dirac spectra in SU(2) ga"
---
\label{sec31}

As RMT is capable of making predictions for the fluctuations on the
scale of the mean level spacing, one has to remove the influence of
the level density by unfolding the spectra.  The cumulative spectral
function
\begin{equation}
N(\lambda)=
        \int_{-\infty}^\lambda d\lambda^\prime
        \sum_{i=1}^{V/2}\delta(\lambda^\prime-\lambda_i)\;,
\label{staircase}
\end{equation}
is the number of levels below or at the energy $\lambda$. It is
frequently referred to as staircase function.  It can be separated
into an average part $N_{\rm ave}(\lambda)$, whose derivative is the
level density, and a fluctuating part $N_{\rm fluc}(\lambda)$,
\begin{equation}
  N(\lambda)=N_{\rm ave}(\lambda)+N_{\rm fluc}(\lambda)\;.
\end{equation}
The average part is determined by gross features
of the system and has to be removed.  The fluctuating part is in
all relevant systems of order ${\cal O}(1)$ and contains the
correlations to be analyzed. After extraction of the average part
$N_{\rm ave}(\lambda)$, it is unfolded from the spectra by the
introduction of a dimensionless energy variable
\begin{equation}
\xi_i=N_{\rm ave}(\lambda_i) \ .
\end{equation}
In this variable, the spectra have mean level spacing unity
everywhere,
\begin{equation}
1/\rho_{\rm ave}(\xi)\equiv 1,
\label{lsone}
\end{equation}
where $\rho_{\rm ave}(\xi)=dN_{\rm ave}(\xi)/d\xi$. However, the
extraction of $N_{\rm ave}(\lambda)$ from the data is non--trivial in
our case because little is known analytically about the level density
of QCD spectra, particularly in lattice calculations. We thus have to
resort to phenomenological unfolding procedures.  Faulty unfolding
leads to wrong results, especially on such large energy scales that we
are interested in. In the subsequent Secs.~\ref{sec311},
\ref{sec312} and \ref{sec313}, we discuss three different procedures
used here, ensemble unfolding, configuration unfolding and windowing,
respectively.
