---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-005-c-twopoint-spectral-correlations
section_title: "Two–Point Spectral Correlations"
section_number: C
pages: 6-10
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 8 sections: INTRODUCTION; COMPLETE DIRAC SPECTRA IN SU(2) GA; DATA ANALYSIS"
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.994
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


\subsection{Higher Order Spectral Correlations}
\label{sec34}

The wealth of data allows us to go beyond a previous
analysis~\cite{halasz97} of higher moments of the eigenvalue
partition,
\begin{equation}
\mu_k(L)=\overline{\langle(L-n_{\alpha}(L))^k\rangle}\;.
\label{moments}
\end{equation}
We notice that $\mu_2(L)=\Sigma^2(L)$. The skewness and the excess
\cite{Mehta} are defined by
\begin{equation}
\gamma_1(L)=\mu_3(L)\mu_2(L)^{-3/2}
\label{skew}
\end{equation}
and
\begin{equation}
\gamma_2(L)=\mu_4(L)\mu_2(L)^{-2}-3 \ ,
\label{excess}
\end{equation}
respectively.  The comparison of RMT predictions with lattice data for
these both quantities in Fig.~\ref{agree2} again shows very good
agreement.

The measures $\gamma_1(L)$ and $\gamma_2(L)$ only contain a small
amount of information of the spectral correlations. Moreover,
$\gamma_1(L)$ and $\gamma_2(L)$ also involve lower order correlations:
$\gamma_1$ is a combination of the two-- and the three--point
correlator, $Y_2(r)$ and $Y_3(r_1,r_2)$, and $\gamma_2$ involves in
addition the four--point correlator $Y_4(r_1,r_2,r_3)$. The
representation of the moments in terms of integrals over the
correlators reads
\begin{equation}
\mu_3(L) =
L-6\int_{0}^{L}(L-r)Y_2(r)dr-6\int_{0}^{L}dr_1\int_{0}^{L-r_1}dr_2
(L-r_1-r_2)Y_3(r_1,r_2)
\label{mu3}
\end{equation}
and
\begin{eqnarray}
  \mu_4(L) & = & L-(14-12L)\int_{0}^{L}(L-r)Y_2(r)dr + 12 \left[
  \int_{0}^{L}(L-r)Y_2(r)dr \right]^{2} \nonumber \\ & + & 36
  \int_{0}^{L}dr_1\int_{0}^{L-r_1}dr_2(L-r_1-r_2)Y_3(r_1,r_2)
  \nonumber \\ & - &
  24\int_{0}^{L}dr_1\int_{0}^{L-r_1}dr_2\int_0^{L-r_1-r_2}
  dr_3(L-r_1-r_2-r_3)Y_4(r_1,r_2,r_3)\;.  \nonumber\\
\label{mu4}
\end{eqnarray}
Obviously, by analyzing $\gamma_1(L)$ and $\gamma_2(L)$, one cannot
easily estimate to what extent the three-- and the four--point
correlators themselves obtained from the lattice calculations follow
the predictions of RMT.

Here, the three-- and the four--point cluster functions,
$Y_3(r_1,r_2)$ and $Y_4(r_1,r_2,r_3)$ are written as functions of the
arguments $r_i$ ($i=1,2,3$) which are defined terms of the original
arguments $\xi_i$ ($i=1,2,3,4$) by
\begin{equation}
  r_1=\xi_2-\xi_1, \ \ r_2=\xi_3-\xi_2, \ \ r_3=\xi_4-\xi_3.
\label{arg1}
\end{equation}
We constructed from the data the two--point and the three--point
correlation functions $X_2(s)$ and $X_3(s_1,s_2)$ and the
corresponding cluster functions $Y_2(s)$ and $Y_3(s_1,s_2)$. Here, for
convenience, we redefined the arguments for the three--point
correlators as follows:
\begin{equation}
s_1=\xi_2-\xi_1=r_1, \ \ \ s_2=\xi_3-\xi_1=r_1+r_2.
\end{equation}
The results for $X_3(s_1,s_2)$ and $Y_3(s_1,s_2)$ are plotted with
error bars in Fig.~\ref{twfig2} for some given values of $s_1$.  The
results do not depend on unfolding.  In the construction of these
correlators, we first performed a spectral average by using the
translational invariance due to unfolding, and then averaged over the
ensemble. The errors for $X_3(s_1,s_2)$ and $Y_3(s_1,s_2)$ were
estimated as the variance of the ensemble fluctuations.  Once more,
very good agreement with the RMT predictions for $X_3(s_1,s_2)$ is
found, apart from a small systematic deviation which we believe can be
understood as follows. {}From the relation between $X_3(s_1,s_2)$ and
$X_2(s)$
\begin{equation}
X_3(s_1,s_2)=Y_3(s_1,s_2)-2+X_2(s_1)+X_2(s_2)+X_2(s_1-s_2),
\end{equation}
one has
\begin{equation}
X_3(s_1,s_2)|_{s_2\to \infty} = X_2(s_1).
\end{equation}
Therefore, even a small point--deviation of the two--point correlator
at $s_1$ from the theoretical predictions can result in a systematic
deviation of the whole curve $X_3(s_1,s_2)$ versus $s_2$ for this
given $s_1$.  For $Y_3(s_1,s_2)$, the quality of the agreement with
RMT is only slightly reduced, but still remarkable.  In addition to
the systematic deviation, one can see some random fluctuations around
the theoretical curves.  This is because $Y_3(s_1,s_2)$ is the
disconnected correlator, and it should represent the true three--point
correlation, while $X_3(s_1,s_2)$ also contains the two-- and
one--point functions. They play a dominate role and are in good
agreement with the corresponding GSE predictions. We notice that this
analysis was only possible due to the extremely higher number of
levels available.



\subsection{Qualitative discussion of the deviations for
  configuration unfolding}
\label{sec35}

Using ensemble unfolding, we find deviations from RMT behavior, which
scale with the square root of the volume according to the theoretical
predictions. But as we unfold each configuration separately this
effect vanishes. There are still deviations left but none of them show
a $\sqrt{V}$ scaling law.  Moreover, we have a dependence of the
results on the unfolding approach.

Concerning local and Gaussian unfolding, an explanation seems to be
easy at hand. As mentioned above, both procedures have an intrinsic,
artificial, scale. In units of the mean level spacing it has the value
$L\approx100$ for $V=16^4$ in both cases. This is approximately where
the saturation of the statistics seen in Fig.~\ref{deviate1} sets in.
We conclude that this artificial scale causes $\Sigma^2(L)$ and
$\Delta_3(L)$ to saturate. In other words, both approaches are not
capable to allow statements at scales $L\gtrsim100$.  Nevertheless,
both approaches do not show a behavior as shown in
Figs.~\ref{enssig},\ref{ensscl} for $L<100$.

On the other hand, the polynomial unfolding also deviates from RMT
predictions, see Fig.~\ref{consig}. As this approach does not contain
an additional scale, we can rule out effects like the one discussed
above. The question is, whether the deviations in Fig.~\ref{consig} are
due to a Thouless energy or if they have another origin.

The fluctuating part of the integrated level density $N_{\rm
  fluc}(\lambda)$ should be of order ${\cal O}(1)$, as mentioned
above.  In the upper part of Fig.~\ref{diff} the difference between the
real staircase function and the smooth polynomial staircase function,
$N(\lambda)-N_{\rm poly}(\lambda)$, for one specific configuration is
plotted. This picture remains qualitatively the same whatever
configuration is chosen.  The polynomial fits have a systematic
deviation from a smooth behavior larger than ${\cal O}(1)$. The
difference between the ensemble staircase and polynomial fit
$\overline{N}(\lambda)-N_{\rm poly}(\lambda)$ is shown in the lower
part of Fig.~\ref{diff}.  A polynomial of degree $n=3$ gives the same
result as $n=4$.  To obtain a better insight in this obviously not
universal behavior, we calculate the power spectrum
\begin{equation}
  F(f)=\int^{\infty}_{-\infty} d\lambda e^{2\pi if\lambda}
  K(\lambda_1,\lambda_2,\lambda)
  \frac{d}{d\lambda}\left(N(\lambda)-N_{\rm poly}(\lambda)\right) \ .
\label{transf}
\end{equation}
By construction, the derivative in the integrand gives the
fluctuations of the level density.  The window function
$K(\lambda_1,\lambda_2,\lambda)$ has to be introduced because we only
have a finite interval of eigenvalues in the Fourier transform over
the whole real axis. It is zero outside the interval
$\lambda_1\leq\lambda\leq\lambda_2$. The choice is not unique inside
\cite{nr}.  Thus, the Fourier transform is a convolution of the
transforms of $N(\lambda)-N_{\rm poly}(\lambda)$ and
$K(\lambda_1,\lambda_2,\lambda)$.  In order to reduce the influence of
the Fourier transform of $K(\lambda_1,\lambda_2,\lambda)$ on the
results as far as possible, we use a triangle window \cite{nr}.  The
result is shown in Fig.~\ref{spectrum}. In the right part one sees the
Fourier transform of the ensemble averaged density. Only the very
first peak is left, both for polynomial of degree $n=4$ and $n=5$.
The latter is reduced in amplitude. On the left side the transform of
an arbitrary chosen configuration is plotted. The first peaks are
reduced in amplitude again for $n=5$, whereas the remaining ones are
the same for both degrees.  We conclude that only the first peak,
corresponding to the long wave part of Fig.~\ref{diff}, is common to
all configurations. All others fluctuate from configuration to
configuration.

We conclude that the average level density $\rho_{\rm ave}(\lambda)$ and
thus the average integrated level density $N_{\rm ave}(\lambda)$
consist of two parts, namely a very smooth polynomial--like part and
another, non--universal, part,
\begin{equation}
N_{\rm ave}(\lambda)=N_{\rm poly}(\lambda)+N_{\rm osc}(\lambda)\;.
\end{equation}
We stress again that the existence of a polynomial--like smooth part
is suggested by pertubative and $1/N_c$ expansions of the QCD level
density \cite{kogut83,smilga93}. It is expected to be governed by the
available phase space: for free fermions the spectral density is given
at $|\lambda|\to\infty$ by $\rho_{\rm
  ave}(\lambda)=N_cV|\lambda|^3/4\pi^2$ \cite{leutsmilga}, where $N_c$
is the number of colors. This also holds in a $1/N_c$ expansion of
the interacting theory on scales which are large compared to the
hadronic scale \cite{smilga93}. This is the region we investigated in
the spectra, as the eigenvalues are given in units of the inverse
lattice spacing as $a^{-1}\approx10~{\rm fm}^{-1}\approx2~{\rm GeV}$,
see Figs.~\ref{stair} and \ref{diff}. This is why we tried to
approximate the average level density by a function which is as smooth
as a polynomial.

The additional structure of the level density appears to have
similarities to oscillations, see Figs.~\ref{diff} and \ref{spectrum}.
Thus, we refer to it as ``oscillatory part'', $N_{\rm osc}(\lambda)$.
This oscillatory part explains the different behavior of $\Delta_3(L)$
and $\Sigma^2(L)$ for large $L$ for different unfolding methods.  The
polynomial unfolding is clearly unable to remove the oscillations and
fits only $N_{\rm poly}(\lambda)$. Thus, the oscillatory part is still
present in the unfolded spectrum.  The presence of these oscillations
leads to values for $\Delta_3(L)$ larger than predicted by RMT,
because a fit to a straight line can only be done in a less accurate
manner. In contrast to that, the Gaussian and the local unfolding is
capable to fit $N_{\rm poly}(\lambda)$ and part of $N_{\rm
  osc}(\lambda)$.  However, it is not clear whether the fit to the
oscillatory part is done completely or if, on the other hand, it does
not smooth out part of the universal fluctuations, i.e.  overfits the
data points. But, because of the saturation of $\Sigma^2(L)$ and
$\Delta_3(L)$, see Fig.~\ref{deviate1}, we think that probably the
latter happens.

However, as argued above, since we expect the physical density to be
as smooth as a polynomial, the oscillatory part is likely to be a
lattice artifact. This is suggested by Figs.~\ref{diff} and
\ref{spectrum} which show that these oscillations live on the scale of
the inverse lattice spacing $1/a$. As $|\lambda|$ cannot be
arbitrarily large in lattice gauge theory, due to an ultraviolet
cutoff in momentum for finite lattice spacing $a$, the increase of the
density is disturbed by lattice artifacts.  For the large lattices,
i.e.  $V=16^4$, the deviations due to lattice artifacts set in at
approximately the same scale as the expected equivalent of a Thouless
energy. This can be seen from the $\sqrt{V}$ scaling of the smaller
lattices. A rough estimate gives $\lambda_{\rm RMT}/D\approx30$ for
$V=16^4$ for $\Sigma^2(L)$.  Therefore one should be careful with the
determination of the deviation point for large lattices in the bulk of
the spectra.  After removing this part from the data, we find for
$\Sigma^2(L)$ reasonable agreement with the RMT prediction up to at
least $L\approx300$ and with some uncertainties even to $L\approx500$,
see Fig.~\ref{poly_cut}.  Because of the complicated structure of the
average level density it is not possible to make any statement beyond
this scale.  In chaotic billiards, so--called bouncing ball modes
generate effects which are similar to the ones here \cite{graef92}.
In that case, however, an analytical prediction for the oscillatory
behavior was at hand. Such a result is also highly desirable in our
case.  It would be needed to furnish our phenomenological removal of
the oscillations with a theoretical justification.

In any case, we may use the information displayed in
Fig.~\ref{spectrum} to phenomenologically remove the oscillatory part.
We cut the power spectrum at a certain interval, back transform the
remaining peaks in the frequency interval $[0,f_{\rm cut}]$ and
subtract the smooth oscillatory part of the integrated level density
obtained in this manner.  We do this for each configuration
separately.  This procedure changes the result of the statistical
analysis in a crucial way, as can be seen from Fig.~\ref{poly_cut}.
There, the results for spectral measures are shown for different
choices of $f_{\rm cut}$.  Because only the very first peak is common
to all spectra whereas higher frequencies appear to be specific for
each configuration, a choice of $f_{\rm cut}>3.0\cdot(2a)$ is actually
too large. This manifests in a saturation of the statistics in
Fig.~\ref{spectrum} for $f_{\rm cut}=7.0\cdot(2a),10.0\cdot(2a)$.  A
cutoff of $f_{\rm cut}=1.5\ldots3.0\cdot(2a)$ seems to be the best
choice, but we are not able to give an exact value.  This figure also
shows a comparison between $\beta=2.4$ and $\beta=2.5$ for $V=16^4$.
Both values of $\beta$ give almost the same result.  The procedure
also removes the slight differences seen in Fig.~\ref{mean} for the
polynomials for $L\gtrsim200$. From all this, we conclude that the
deviations in Fig.~\ref{consig} are due to a non polynomial--like part
in the average level density and not due to an equivalent a Thouless
energy.  

A possible way to circumvent the problems encountered by lattice
artifacts is windowing as discussed in Sec.~\ref{sec313}.  However,
this works only if the size of the windows $\delta\lambda$ is at least
so small that the oscillations of Fig.~\ref{diff} are not important,
i.e. $\delta\lambda\ll a^{-1}$. Another way might be ensemble
unfolding, Sec.~\ref{sec311}. As the lattice artifacts are seen in each
configuration as well as in the average integrated level density this
approach might remove the oscillations. But it is by no means clear if
it really does, especially for large interval lengths.  As both
approaches give similar results for small lattices, $V\leq10^4$, for
intervals $L\lesssim20$, we conclude that the artifacts are not
important on these scales. This is supported by the observations that
deviations due to them set in at $L\approx25$ for polynomial
unfolding, independently of the lattice size, see Fig.~\ref{consig}.
Thus, these artifacts become important for analysis of larger
lattices, i.e. $V=16^4$, and for even larger ones in future
examinations.

From all this we conclude that we do not see an equivalent of a
Thouless energy if we unfold each configuration separately.  This is
in complete contrast to the results gained by ensemble unfolding. The
former surely removes the fluctuations in Fig.~\ref{ensemble}, whereas
the latter does not. We conclude that this fluctuation with respect to
the ensemble already contains the information needed to determine the
Thouless energy. After removing this information it seems that there
is no further information in the spectra, i.e. we find agreement with
RMT on huge scales.
