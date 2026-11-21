---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-005-312-configuration-unfolding
section_title: "Configuration unfolding"
section_number: 3.1.2
pages: 4-5
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.996
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 14 sections: Front matter; Introduction; Complete Dirac spectra in SU(2) ga"
---
\label{sec312}
We now unfold each configuration separately.  Observables are then
calculated for each configuration by running spectral average.
Thereafter we average over the ensemble. The basic characteristics are
already obtained for one single configuration, though the statistics
is considerably improved by ensemble averaging.  This is in the same
spirit as it was done in spectra of nuclei \cite{bohigas83} and
complex atoms \cite{rosen60}.  These spectra were unfolded for each
nuclei or atom separately.  Then observables were calculated as
described above, i.e. first taking the spectral and then the ensemble
average. In this case the ensembles consist of nuclei or atoms of
different types.

Configuration unfolding is, in contrast to ensemble unfolding, not a
unique procedure. One has to find either fits to the average staircase
function or to smooth it in some way. A priori, there is no criterion
whether the numerical estimated $N_{\rm ave}(\lambda)$ is close to the
real one or not.  Thus, we use three different approaches and
carefully compare them with one another to eliminate as many sources
for mistakes as possible and to obtain consistent results.

First, we fit $N(\lambda)$ to a polynomial of degree $n$,
\begin{equation}
\langle N(\lambda)\rangle
 =N_{\rm poly}(\lambda)=\sum_{j=0}^n\:a_j\,\lambda^j\;,
\label{poly}
\end{equation}
where $n$ is a small integer, $n=2,\ldots,5$.  This approach is
motivated by the fact that almost all physical systems are known to
have a level density which is as smooth as a polynomial. In our case
this ansatz is supported by pertubative calculations. Strong coupling
expansions for SU(2) with staggered fermions have been performed
\cite{kogut83} and, furthermore, $1/N_c$ expansion of the QCD level
density \cite{smilga93}, both suggesting a smooth level density. The
former gives a semi--circle whereas the latter explicitly predicts a
polynomial increase.

Second, we use the Gaussian method which was originally developed by
Strutinsky \cite{haake}.  One replaces the $\delta$--functions in
Eq.~(\ref{staircase}) by Gaussian functions with a width $\Delta$
which yields a smoothed staircase
\begin{equation}
N_\Delta(\lambda)=\int_{-\infty}^\lambda d\lambda'\:
        \sum_{i={\rm min}}^{{\rm max}}\:\frac{1}{\sqrt{\pi}\Delta}\,
        e^{-\frac{1}{\Delta^2}\,(\lambda'-\lambda_i)^2} .
\label{gauss}
\end{equation}
The summation runs from the smallest eigenvalue $\lambda_{\rm min}$ to
the largest eigenvalue $\lambda_{\rm max}$ in the interval under
consideration.  The limit $\Delta\to0$ restores $\delta$--distributed
eigenvalues, whereas the fluctuations are smeared out for finite
$\Delta$.  The optimal parameter $\Delta_{\rm opt}$ is found by a
$\chi^2$--fit of $N_\Delta(\lambda)$ to $N(\lambda)$. Then we identify
\begin{equation}
\langle N(\lambda)\rangle=N_{\Delta_{\rm opt}}(\lambda) \ .
\label{Ngauss}
\end{equation}

Third, we perform a local unfolding by calculating the unfolded
eigenvalues $\xi_i$ directly with the formula
\begin{equation}
\xi_{i+1}-\xi_i=\frac{\lambda_{i+1}-\lambda_i}{D_i}\;,
\end{equation}
with local mean level spacing
\begin{equation}
D_i=\frac{1}{2k+1}\sum_{j=i-k}^{i+k}(\lambda_{j+1}-\lambda_j)\;.
\label{mls}
\end{equation}
Here $2k$ is the number of consecutive level spacings over the running
average is performed.

Whatever approach one decides to use, a necessary condition is that on
the unfolded scale the average number of levels in an interval of
length $L$ should equal this length. This is a very important
requirement because we are also interested in very large energy
scales.  This assures that the spectrum on the numerically constructed
dimensionless scale $\xi$ has mean level density unity.  Consider the
interval $[\alpha,\alpha+L]$ which contains $n_\alpha(L)$ eigenvalues.
Spectral average $\langle\ldots\rangle$ and ensemble average
$\overline{(\ldots)}$ have to yield
\begin{equation}
\overline{\langle n_\alpha(L)\rangle}=L\;.
\label{meannumber}
\end{equation}
In Fig.~\ref{mean}, the difference between the calculated mean number
of eigenvalues $\overline{\langle n_\alpha(L)\rangle}$ and $L$ is
plotted as a function of $L$. For the Gaussian method the difference
appears to be zero to all scales. While it is small and does only
appear at large $L$ for polynomials fits with $n\geq3$, strong
deviations from the zero line already appear at small $L$ for $n=2$.
In the case of local unfolding, the difference $L-\overline{\langle
  n_\alpha(L)\rangle}$ is positive for small $k$, i.e.  there are on
average less levels in a given interval than there should be. For
growing $k$, it becomes negative with ever stronger deviations from
the flat line. The averaging interval length $k$ for which the
difference equals zero is $k\approx100$ for $V=16^4$. For other
lattice sizes this averaging interval is slightly smaller.  We take
this as the optimal parameter for this approach. {}From Fig.~\ref{mean}
we learn, that the necessary condition (\ref{meannumber}) is fulfilled
only for the Gaussian approach, polynomial fit with $n\geq3$ and local
unfolding with $k\approx100$ for $V=16^4$, all other choices of the
parameters must be rejected.

It should be mentioned that a new artificial scale both for local and
Gaussian approach is introduced, namely the averaging interval length
$k$ and the width $\Delta$, respectively. Therefore, one should be
cautious in the interpretation of effects seen on scales $L$ larger
than current value of the corresponding parameter. In units of the
mean level spacing $D$ we find a width of the Gaussian as
$\Delta/D\approx100$ at a $16^4$ lattice. On the other hand, both
approaches have the advantage that no particular function for the
average level density has to be assumed.

We checked all our numerical unfolding approaches with the spectrum of
a very different system. We used the spectrum of quantum chaotic
billiard that was simulated in a microwave experiment. In billiards,
the Weyl formula gives an analytically expression for the mean level
density \cite{graef92}. With our phenomenological approaches, we
indeed obtained quantitatively the same results.
