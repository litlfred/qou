---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-011-4-summary-and-discussion
section_title: "Summary and discussion"
section_number: 4
pages: 10-12
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 1.0
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 14 sections: Front matter; Introduction; Complete Dirac spectra in SU(2) ga"
---
\label{sec4}

After summarizing our results in Sec.~\ref{sec41}, we discuss our
findings in Sec.~\ref{sec42}.


\subsection{Summary}
\label{sec41}

We presented a detailed analysis of statistical properties of complete
eigenvalue spectra for staggered fermions for SU(2) lattice gauge
theory for various couplings and lattice volumes. Unfolding the data
posed certain difficulties which are not encountered in other systems.
The staircase function found by an average over the ensemble differs
in most cases from the smooth staircase of one specific configuration.
The deviations are as large as $\langle
N(\lambda)\rangle-\overline{N}(\lambda)={\cal O}(10^1)$ for $V=16^4$.
Varying the unfolding approach leads to different results for large
scales. In particular, there is a drastic difference between ensemble
and configuration unfolding.

Using ensemble unfolding, we find a range of validity of RMT, giving
$\lambda_{\rm RMT}/D=C\sqrt{V}$.  The numerical constant is
approximately given as $C\approx0.3$.  which is compatible with the
result obtained in \cite{bitsch98} for the microscopic region where
the scaling $\lambda_{\rm RMT}/D\sim0.3\ldots0.7\sqrt{V}$ was found.
The same results are obtained if we use windowing, but with less
statistical significance.

By unfolding each configuration separately, we do not see any scaling
of this type. This procedure obviously removes the fluctuations of the
staircase function relative to the ensemble average seen in
Fig.~\ref{ensemble}. We notice that fluctuations over the ensemble can
already be observed in the integrated level density. But there are
still deviations depending on the unfolding approach used.  In
particular there is an overshoot for polynomial unfolding at large
$L$. The reasons for this lies in special features of the average
level density, which consists of at least two parts: a smooth
polynomial--like and an oscillatory part.  Hence the Thouless energy
is due to the fluctuations in the ensemble.

We want to clarify the difference in the notion of ergodicity used in
spectral analysis and in lattice calculations, respectively.
Concerning the analysis of spectra, a system is called ergodic if
spectral and ensemble average yield the same results. It can be proven
rigorously that random matrices have this property in the limit of
large matrix dimension. However, here we face a different situation.
We emphasize that these issues do not affect the notion of ergodicity
as used in connection with lattice simulations. The latter is defined
by the requirement that the space of possible lattice configuration is
explored reasonably fast by the simulation algorithm.  We emphasize
that the time history of the spectra is not of importance for the
calculation of the spectral observable of Sec.~\ref{sec3}, because it
is only relevant that the configurations used, see Table \ref{tab1}, are
representative members of the ensemble, i.e.~ergodicity in the sense
of lattice simulations is fulfilled. This is ensured by our algorithms
as described in Sec.~\ref{sec2}. Furthermore, this is supported by the
observation that our results do not change if we take arbitrary
subsets of configurations, only the scattering of the data points
increases.

Furthermore we analyzed the nearest neighbor--spacing distribution,
skewness and excess for small $L$. Due to the large amount of data,
our results achieved a quality never reached before.  Due to
translational invariance in the bulk of the spectra the general
tendency for all of the observables can already be seen for one
specific configuration.  Averaging over all configurations increases
the statistical significance of the results.  The results for small
values $L$ considerably improve the statistical significance of
previous analyses\cite{halasz95,halasz97}.  To the best of our
knowledge, we presented the first statistically highly significant
analysis of bare two-- and, importantly, three--point spectral
correlators. Very good agreement between lattice data and RMT
predictions is found.  We find minor deviations for the three--point
cluster functions. In our opinion, their origin are probably very
small point--deviations of the two--point functions.


\subsection{Discussion}
\label{sec42}

Some scenarios for the level statistics are shown in
Fig.~\ref{cartoon}.  There the spectral rigidity is plotted. The two
solid lines represent Poisson and RMT behavior, $\Delta_3(L)\sim L$
and $\Delta_3(L)\sim\log L$, respectively. The dashed lines represent
schematically two different cases.  Case `A' correspond to a scenario
known from systems with few degrees of freedom. The shortest periodic
orbit in phase space sets a scale which forces $\Delta_3(L)$ to
saturate at a certain $L_A$ \cite{berry85}. But by increasing the
degrees of freedom of the system, this scale become ever larger and is
hard to be seen.  As we may view lattice gauge theory as a many body
problem or disordered system, we do not expect to see this scale in
the level statistics.  Therefore one should not be tempted to conclude
that the saturation seen in Figs.~\ref{deviate1},\ref{poly_cut} is the
analogue of ``saturation of fluctuation measures'' which was observed
in the energy level statistics for classically chaotic systems and was
interpreted by Berry in terms of shortest periodic orbits
\cite{berry85}.  Unlike in the case of quantum billiards where an
analytic expression for the average spectral density exists, the
$N_{\rm ave}(\lambda)$ that we obtained in our analysis was only a
numerical result. Most likely all three approaches, i.e.  Gauss, local
and modified polynomial, fit also parts of the universal fluctuations
which shows up as a saturation of the statistics $\Delta_3(L)$ and
$\Sigma^2(L)$.

Another scenario is given by case `B' which lies between Poisson and
RMT behavior. It can arise in three different physical situations
\cite{guhr97}:
\begin{enumerate}
\item Systems in few degrees of freedom between regularity and
      chaos. The spectral rigidity lies between the Poisson limit,
      which applies to regular systems and the RMT limit which applies
      to chaotic systems, provided the scale $L_A$ is much larger
      than $L_B$.
\item Disordered systems in $d$ dimensions. The time $t_c$ for the
      classical diffusion through the system of size $L_S^d$ where
      $L_S$ is the size in each dimension determines an energy scale
      \begin{equation}
      E_c = \hbar / t_c \ ,
      \label{thoul}
      \end{equation}
      the Thouless energy. This in turn sets the scale
      $\lambda_{\rm RMT}/D$ where $D$ is the single particle mean
      level spacing. For energy separations in units of $D$ smaller
      than this scale, RMT fluctuations are seen. For larger energy
      separation, deviations as sketched in Fig.~\ref{cartoon} occur.
\item Many body systems such as nuclei, molecules or complex atoms.
      In the language of condensed matter physics, these systems
      are zero--dimensional. Consider the Hamiltonian of such a system
      $H=H_0+H_1$ where $H_0$ has a certain property and $H_1$ breaks this
      property. The influence of $H_1$ on the statistics of the spectrum
      of $H_0$ is measured in terms of the spreading width
      \begin{equation}
      \Gamma = 2\pi \langle H_1^2 \rangle / D_0
      \label{spread}
      \end{equation}
      where $D_0$ is the mean level spacing of $H_0$ and $\langle H_1^2
      \rangle$ the mean square matrix element of $H_1$.  In particular,
      if $H_0$ has Poisson statistics and $H_1$ RMT statistics the
      spectral rigidity acquires the form of Fig.~\ref{cartoon} and
      $\Gamma$ sets the scale $\lambda_{\rm RMT}/D$.
\end{enumerate}

As discussed above, situation 1.~is not likely to apply. We emphasize
that the Thouless energy $E_c$ and the spreading width $\Gamma$
defined in 2.~and 3.~are closely related concepts. Actually, in his
original paper, Thouless~\cite{thou75} defined $E_c$ as a special kind
of spreading width.  The precise relation between $\lambda_{\rm
  RMT}/D$ and $E_c$ has been studied in great detail in the framework
of RMT~\cite{Frahm98}. We notice that the definition in 2. which is
most commonly used in condensed matter physics, relates $E_c$ to
dimensionality, whereas $\Gamma$ is defined in zero dimensions.  Thus,
the sheer existence of a scale $\lambda_{\rm RMT}/D$ can imply, but
does not necessarily imply that the deviation from RMT is related to a
diffusion in a $d$ dimensional disordered system.

Recent theoretical studies aim at establishing
\cite{stern98,osborn98,janik98} a link between disordered systems and
QCD. In these works, a range of validity $\lambda_{\rm RMT}$ of
applicability of RMT was considered.  Using the Gell-Mann-Oakes-Renner
relation, it should be determined by the pion decay constant $F_\pi$
and the chiral condensate $\Sigma$,
\begin{equation}
\lambda_{\rm RMT}\sim\frac{F_\pi^2}{\Sigma\sqrt{V}}\;.
\label{thou1}
\end{equation}
In the microscopic region the mean level spacing is
$D=\pi/(\Sigma V)$, so that Eq.(\ref{thou1}) can be rewritten as
\begin{equation}
\frac{\lambda_{\rm RMT}}{D}\sim\frac{F_\pi^2}{\pi}\sqrt{V}\;.
\label{thou2}
\end{equation}
The predicted scaling behavior was found very recently in the
microscopic region \cite{bitsch98}.  There a crossover from RMT to
non--universal behavior was found with the scaling Eq.(\ref{thou2}).
As argued in Ref.~\cite{osborn98}, a similar relation should also be
seen in the bulk of the spectrum. Here, however, the mean level
spacing $D$ is that of the bulk. In the present work, we have shown
that, first, the scale $\lambda_{\rm RMT}/D$ exists in the bulk, and,
second, that it shows the predicted scaling behavior.  The latter
observation is a support for the ideas that link QCD to disordered
systems and thus to a diffusion in a $d$ dimensions.  However, as
outlined above, our findings are necessary but not sufficient for this
conclusion. They do not rule out other physical mechanisms that lead
to a spreading width or Thouless energy. This underlines the strength
of our analysis: it does not depend in any way on a model for this
mechanism. It is a self--consistent statistical method to find the
scale $\lambda_{\rm RMT}/D$.

We hope that the identification of this scale $\lambda_{\rm RMT}/D$
can help to improve our understanding of certain features of QCD as it
may allow one to separate the stochastic noise of the short range
fluctuations from the true dynamics of the QCD vacuum. Most desirably,
these results could help to design effective models or to simplify the
presently used simulation algorithms in lattice gauge theories.
