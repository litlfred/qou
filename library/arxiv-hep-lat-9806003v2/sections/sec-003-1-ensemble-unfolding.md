---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-003-1-ensemble-unfolding
section_title: "Ensemble unfolding"
section_number: 1
pages: 3-5
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 8 sections: INTRODUCTION; COMPLETE DIRAC SPECTRA IN SU(2) GA; DATA ANALYSIS"
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.997
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


\subsubsection{Configuration unfolding}
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
