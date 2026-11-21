---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-008-33-two--point-spectral-correlations
section_title: "Two--Point Spectral Correlations"
section_number: 3.3
pages: 6-7
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.995
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 14 sections: Front matter; Introduction; Complete Dirac spectra in SU(2) ga"
---
\label{sec33}

In an interval of length $L$ in units of the mean level spacing, the
mean number of eigenvalues should be equal to $L$, see
Eq.~(\ref{meannumber}). The variance of this number is defined by
\cite{Mehta}
\begin{equation}
\Sigma^2(L)=\overline{\langle(L-n_{\alpha}(L))^2\rangle} \ .
\label{sigma}
\end{equation}
Thus, an interval of length $L$ contains on average
$L\pm\sqrt{\Sigma^2(L)}$ levels.  For uncorrelated Poisson spectra
$\Sigma^2(L)=L$. RMT predicts for the number variance stronger
correlations, namely $\Sigma^2(L)\sim \log L$. 

Another important quantity is the spectral rigidity $\Delta_3(L)$,
defined as the least square deviation of the staircase function from
the straight line \cite{Mehta},
\begin{equation}
  \Delta_3(L)=\left\langle\frac{1}{L}{\rm
    min}_{A,B}\int_{\alpha}^{\alpha+L}d\xi(N(\xi)-A\xi-B)^2
           \right\rangle \ .
\end{equation}
Since it can be expressed as an integral over the number variance
\begin{equation}
\Delta_3(L)=\frac{2}{L^4}\int_0^Ldr(L^3-2L^2r+r^3)\Sigma^2(r)\;,
\label{rigidity}
\end{equation}
it is smoother than $\Sigma^2(L)$.  

The number variance can be expressed as an integral of the two--point
cluster function $Y_2(r)$ \cite{Mehta}, which depends for
translational invariant spectra only on the difference
$r=|\xi_2-\xi_1|$ between two levels at $\xi_1$ and $\xi_2$,
\begin{equation}
\Sigma^2(L)= L-2\int_{0}^{L}(L-r)Y_2(r)dr \ .
\label{mu2}
\end{equation}
The cluster function is related to the two--point correlation function
$X_2(r)$ which measures the probability density to find two levels at
a distant $r$ by $X_2(r)=1-Y_2(r)$.  In contrast to $P(s)$, these two
levels are not restricted to adjacent ones.  

In Fig.~\ref{agree1}, number variance and spectral rigidity for scales
up to $L=20$ and $L=100$, respectively, are shown. Lattice data and
RMT predictions agree remarkably well, even the oscillations in
$\Sigma_2(L)$ are accurately reproduced. Naturally, previous
analyses~\cite{halasz95} with smaller data sets have less statistical
significance.  Two--point cluster and correlation function which
usually are not accessible in data analysis are shown in
Fig.~\ref{twfig1}. Again, the agreement is impressive.

Beyond this scale there are considerable deviations of $\Delta_3(L)$
as well as of $\Sigma^2(L)$ from RMT predictions which depend on the
unfolding procedure used. We mention that on general grounds one can
show that any scales in $\Sigma^2(L)$ and $\Delta_3(L)$, say
$L^\Sigma$ and $L^\Delta$, respectively, are related by
$L^\Delta:L^\Sigma=4:1$, or so \cite{guhr97}, see Fig.~\ref{agree1}.
Thus, any deviations from RMT behavior appear at smaller $L$ in
$\Sigma^2(L)$ as compared to $\Delta_3(L)$.

If we unfold with the ensemble staircase function
$\overline{N}(\lambda)$, we obtain the following results.  The number
variance can be seen in Fig.~\ref{enssig}.  Data for different lattice
sizes and different gauge couplings are shown in comparison to the RMT
predictions for some regions of the spectra. We find that the point
where the deviation sets in, scales with the square root of the
lattice volume,
\begin{equation}
\frac{\lambda_{\rm RMT}}{D}\approx C \sqrt{V}\;.
\label{scale}
\end{equation}
The numerical constant $C$ is approximately given by $C\approx0.3$.
This should be compared with the result obtained in \cite{bitsch98}
for the microscopic region. There, the scaling $\lambda_{\rm
  RMT}/D\sim0.3\ldots0.7\sqrt{V}$ was found.  This is independent of
the region of the spectra we consider and of the coupling strength
$\beta$.  This is shown in Fig.~\ref{enssig}. There different regions
of the spectra are considered, each corresponding to different values
of $\overline{\rho}(\lambda)$, see Fig.~\ref{stair}.  The results are
the same. Furthermore, the deviation points for different $\beta$
appear to coincide, whereas the local average density depends on the
gauge coupling,
$\overline{\rho}(\lambda)=\overline{\rho}(\lambda,\beta)$, see
Fig.~\ref{stair}. The scaling relation (\ref{scale}) can nicely be seen
from Fig.~\ref{ensscl}, in which the $L$ axes of Fig.~\ref{enssig} is
rescaled with $\sqrt{V}$. We see that the crossover from RMT to
non--universal behavior appears to be the same for all lattice sizes
independent of $\beta$. But the slope varies for different couplings
and regions of the spectra.  When we use windowing instead, we get the
same results as obtained by ensemble unfolding.  But the data points
scatter more compared to Figs.~\ref{enssig} and \ref{ensscl}.

The importance of a proper choice of the unfolding method becomes
manifest as the above picture changes drastically if we unfold each
configuration separately.  As displayed in Fig.~\ref{deviate1}, the
polynomial unfolding leads to an overshooting of the data over the
predictions but further out, compared to ensemble unfolding, while in
the Gaussian as well as in the local case $\Sigma^2(L)$ saturates.
Note the different scale compared to Fig.~\ref{enssig} and also the
difference in scale between number variance and spectral rigidity, as
mentioned above.  The result of the polynomial approach does not
depend on the degree $n$ of the polynomial. Furthermore we find no
scaling with $\sqrt{V}$ for the deviations of polynomial unfolding,
see Fig.~\ref{consig}. The deviation point appears to be the same for
different lattice sizes.  The saturation of the small lattices is due
to the limited number of eigenvalues in the considered energy range.
The same picture arises for the number variance: overshooting for the
polynomial, saturation for Gaussian and local approach.  The general
tendency of this results are already obtained for each configuration
separately, but the data points scatter. After averaging over all
configurations the scattering becomes much smaller, see
Figs.~\ref{agree1} and \ref{deviate1}.
