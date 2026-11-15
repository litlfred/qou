---
doc_id: arxiv-hep-lat-0003021v3
doc_title: "arXiv:hep-lat/0003021v3 19 May 2000"
section_id: sec-002-3-qcd-with-four-dynamical-fermions-at-high-tempe
section_title: "QCD with four dynamical fermions at high temperature"
section_number: 3
pages: 9-14
source_pdf: 0003021v3.pdf
source_sha256: b35dfd9ab88b71d8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.69
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-lat/0003021v3 19 May 2000 — We compute the low-lying spectrum of the staggered Dirac operator above and below the ﬁnite temperature phase transition in both quenched QCD and in dynamical"
---
\label{dynamical}

For our dynamical simulations we chose to work with $n_f=4$ flavors.
Four is the ``natural'' number of flavors for staggered fermions
in the continuum limit, and an efficient exact simulation algorithm
can be used, the Hybrid Monte Carlo algorithm. In addition, the
four flavor theory is known to have a rather strong first order finite
temperature phase transition~\cite{Brown}. Therefore, tunnelings
into the low temperature phase are strongly suppressed already on
rather small systems and at temperatures quite close to $T_c$.

\noi
We made dynamical simulations with quark masses $am_q = 0.1$, 0.05,
0.025, 0.01 and 0.002, and for couplings
$\beta$ in the high temperature phase (here $a$ is the lattice
spacing). 
Interestingly, the lowest eigenvalue provides a sensitive method for
determining the critical coupling $\beta_c(am_q)$:
in Fig~\ref{fig:1.eig_vs_beta} the lowest eigenvalue on a 
$8^3\times4$ lattice with $am_q=0.025$ is plotted against $\beta$.
$\beta$ ranges from 4.96 to 5.07 in intervals of 0.002.
Each point is an average over 5 configurations at that $\beta$-value.
A rise is observed between $\beta=5.012$ and $\beta=5.022$, which can
be clearly interpreted as the chiral symmetry restoring finite
temperature phase transition.
(For published values of the critical couplings $\beta_c(am_q)$)
see Ref.~\cite{Brown}.) The possibility of using the magnitude of the
smallest Dirac operator eigenvalues as probes for chiral symmetry
restoration was suggested by Jackson and Verbaarschot \cite{JV} on the
basis of a similarly observed behavior in a Random Matrix Theory context
that we will also discuss below. 



\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{1.eig_vs_beta.eps}
\end{center}
\vspace*{-2mm}
\caption[a]{The lowest eigenvalue, averaged over 5 configurations, on an
$8^3 \times 4$ lattice with $am_q=0.025$ as a function of $\beta$.
One sees a clear change in behavior around $\beta \sim 5.02$, indicating
the restoration of chiral symmetry around this temperature. Just this first
Dirac operator eigenvalue can thus serve as an excellent indicator of
the chiral phase transition point. }
\label{fig:1.eig_vs_beta}
\end{figure}



\noi
Most of our analysis with dynamical fermions was performed
at $\beta=5.2$, which is above $\beta_c$ for all values of $m_q$
we used.  Typically, we analyzed $\sim 3000$ configurations for each
volume and $m_q$, extracting the 50 smallest eigenvalues. Ensemble details
are summarized in Table \ref{tab:d_ensemb}. Note the large statistics
gathered for $\beta=5.2$ and $am_q=0.025$.

\begin{table}
\begin{center}
\begin{tabular}{c c c c}
$V$ & $\beta$ & $am_q$ & \#configurations \\
\hline
$8^3\times 4$ & 5.1 & 0.1 & 8897 \\
$8^3\times 4$ & 5.1 & 0.025 & 2909 \\
$8^3\times 4$ & 5.1 & 0.01 & 4050 \\
$8^3\times 4$ & 5.2 & 0.1 & 4348 \\
$8^3\times 4$ & 5.2 & 0.05 & 2149 \\
$8^3\times 4$ & 5.2 & 0.025 & 29632 \\
$12^3\times 4$ & 5.2 & 0.025 & 13929 \\
$8^3\times 4$ & 5.2 & 0.01 & 4050 \\
$12^3\times 4$ & 5.2 & 0.01 & 2882 \\
$8^3\times 4$ & 5.2 & 0.008 & 4200 \\
$8^3\times 4$ & 5.2 & 0.005 & 7948 \\
$8^3\times 4$ & 5.2 & 0.002 & 6950 \\
$8^3\times 4$ & 5.3 & 0.025 & 4549 \\
$8^3\times 4$ & 5.4 & 0.025 & 3746 \\
\hline
\end{tabular}
\end{center}
\caption[a]{Details of our ensembles with dynamical fermions.}
\label{tab:d_ensemb}
\end{table}


\noi
As in the quenched case we find a small tail at the
lower end of the eigenvalue distribution, reaching towards $\lambda=0$
from the main bulk of the distribution.   This tail also appears to be
volume independent (see Fig.~\ref{fig:d_vol_test}).  However,
in this case it is somewhat more suppressed than in the quenched case,
and for small values of the quark mass it does not extend all the way 
to $\lambda=0$, see Fig.~\ref{fig:dyn_que_compare}.



\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{dyn_que_compare.eps}
\end{center}
\vspace*{-2mm}
\caption{Quenched spectrum of $\beta=5.9$ and a dynamical spectrum at
$\beta=5.4$ with $am_q=0.025$, both on an $8^3 \times 4$ lattice.
A blowup of the y-axis near the end of the tail
is also shown. There is a much stronger suppression of small eigenvalues
in the case of dynamical fermions, perhaps due to fewer would-be zero
modes in topological non-trivial gauge field configurations.}
\label{fig:dyn_que_compare}
\end{figure}



In Fig.~\ref{fig:various_dynamical} we show
eigenvalue distributions measured at $\beta=5.2$ and various $am_q$.
Note that for larger $am_q$, $\beta_c$ is also larger,
which causes a shift of the whole spectrum as $am_q$ is varied.
Therefore, a direct quantitative
comparison of the distributions in Fig.~\ref{fig:various_dynamical}
is not straightforward. 
However, we note that the distributions at  $am_q=0.025$ and $am_q=0.002$
are almost on top of each other, indicating that these distributions
are very close to the $am_q=0$ distribution.



\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{d_vol_test.eps}
\end{center}
\vspace*{-2mm}
\caption{The density of the 50 smallest eigenvalues in the high temperature
phase, $\beta=5.2$ and $am_q=0.025$ for spatial volumes $8^3$ and $12^3$.
The normalization of the distributions is as in Fig.~\ref{fig:q_vol_test}.
As in the quenched simulations, we observe no significant change in the 
eigenvalue spectrum at all as the three-volume is increased.}
\label{fig:d_vol_test}
\end{figure}





\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{various_dynamical.eps}
\end{center}
\vspace*{-2mm}
\caption{The density of the 50 smallest eigenvalues at $\beta=5.2$ for quark 
masses $am_q=0.1, 0.05, 0.025, 0.002$ on $8^3 \times 4$ lattices.
While there is some shift with decreasing quark mass for the larger values
of $am_q$, the spectral density seems to approach a limiting function, which
we can identify as the chiral limit of the spectrum. Note that the 
large-mass behavior of the spectrum is almost identical to the quenched
spectrum in this region, in agreement with the notion that on this scale
of eigenvalues the large-mass fermion has completely decoupled,
and effectively become quenched.}
\label{fig:various_dynamical}
\end{figure}




\noi
Furthermore, as in the quenched case described in the previous section, 
we find the ``macroscopic'' behavior
of the eigenvalue density seemingly compatible with a square root form.
By fitting eq.~(\ref{eq:se_rho}) to the bulk of the spectrum
(leaving out the tail), we obtain different powers, depending 
on how much of the tail we choose to cut off. This fitting has been 
done for $V=8^3\times 4$ at $\beta=5.2$ and $am_q=0.025$ and the 
resulting values can be seen in Table~\ref{tab:fit_vs_cut}.
\begin{table}
\begin{center}
\begin{tabular}{c c c}
Cut at & $m$ & $2m+1/2$\\
\hline
0.09  & 0.055 $\pm 0.003$ & 0.609 $\pm 0.006$ \\
0.095 & 0.049 $\pm 0.004$ & 0.598 $\pm 0.007$ \\
0.1   & 0.040 $\pm 0.005$ & 0.580 $\pm 0.010$ \\
0.105 & 0.036 $\pm 0.006$ & 0.572 $\pm 0.011$ \\
0.11  & 0.041 $\pm 0.008$ & 0.582 $\pm 0.016$ \\
0.115 & 0.035 $\pm 0.010$ & 0.570 $\pm 0.019$ \\
0.12  & 0.043 $\pm 0.013$ & 0.585 $\pm 0.027$ \\
0.125 & 0.040 $\pm 0.016$ & 0.581 $\pm 0.032$ \\
0.13  & 0.033 $\pm 0.021$ & 0.567 $\pm 0.041$ \\
0.14  & 0.027 $\pm 0.034$ & 0.554 $\pm 0.068$ \\
\hline
\end{tabular}
\end{center}
\caption[a]{The dependence of the fitted power on the
$\lambda$ where the small-$\lambda$ tail is cut off.
The data are from $8^3\times 4$, $\beta=5.2$ and $am_q=0.025$
lattices, using the 50 smallest eigenvalues. The fits are almost compatible
with a square-root behavior of the spectrum at this soft edge, but there
is a consistent small upward shift in the exponent.}
\label{tab:fit_vs_cut}
\end{table}
There is a clear tendency towards a slightly higher power ($=2m+1/2$)
than the square root which would be expected from Random Matrix Theory.
In Fig.~\ref{fig:sqrt_fit} we show the fit with the cut at 0.1.
For comparison, we include the distribution of the first eigenvalue in 
the figure.  Clearly, the tail at small $\lambda$ is caused by the
excessive width of the distribution of the smallest eigenvalue.



\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{sqrt_fit.eps}
\end{center}
\vspace*{-2mm}
\caption[a]{Power fit to the spectral density for $\beta=5.2$ with $am_q=0.025$
on an $8^3 \times 4$ lattice with cut at 0.1 (see Table~\ref{tab:fit_vs_cut}). 
Also included is the distribution of the first eigenvalue. The distribution
of this smallest eigenvalue is very different from that demanded by
the Airy-function behavior (see below).}
\label{fig:sqrt_fit}
\end{figure}




\noi
In Fig.~\ref{fig:Airy_compare} we compare the spectral density for
quark mass $am_q=0.025$ with the prediction
(\ref{eq:Airy_rho}) of the Random Matrix Theory for the density near
a soft edge.  In order to make the comparison possible, we rescale 
the spectral density as
\beq
\rho(\lambda)\rightarrow \frac{\lambda_0}{2}\left(\frac{2}{\pi\lambda_0 KV}
\right)^{\frac{2}{3}}\rho\left(\frac{2}{\lambda_0}(\lambda-\lambda_0)\left(
\frac{2}{\pi\lambda_0 KV}\right)^{-\frac{2}{3}}\right)
\eeq
where we determine $\lambda_0$ and $K$ from a fit to a square root:
$\sqrt{\frac{\lambda_0}{2}}K\sqrt{(\lambda-\lambda_0)}$.  Here $V$ is
the lattice volume.  We see that the tail predicted by the Random
Matrix Theory is much more strongly suppressed than the measured
distribution.  Moreover, we can also observe that the density of the
eigenvalues themselves does not match: the measured distribution
includes 50 eigenvalues, whereas the function (\ref{eq:Airy_rho}) has
only 40 `wiggles' in the $\lambda$-range of the distribution.
However, if we attempt to perform the comparison by matching the
number of eigenvalues/wiggles, the overall fit becomes worse.  In
itself, this mismatch is not surprising, when we remember that the
overall shape is {\em not} well described by a square root behavior
in the first place (see Table~\ref{tab:fit_vs_cut}).




\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{airy_compare.eps}
\end{center}
\vspace*{-2mm}
\caption[a]{Comparison of the spectral density for $\beta=5.2$, $am_q=0.025$ 
on a $8^3\times4$ lattice, with the Random Matrix Theory prediction
for a soft edge, as in eq.~(\protect\ref{eq:Airy_rho}).}
\label{fig:Airy_compare}
\end{figure}



\noi 
In the quenched simulations we saw that correlations between the
first 5 or 6 eigenvalues were not very accurately given by Random Matrix
Theory.  In
Fig.~\ref{fig:d_level_space} the distribution of $s_i$, defined in
eq.~(\ref{eq:level_space}), is shown for a dynamical simulation with
$\beta=5.2$ , $am_q=0.025$ on a $8^3\times4$ lattice.  
Here we see, on the same lattice volume, 
a clear deviation from the Wigner surmise
only for the first two or three spacings, $s_1$, $s_2$ and $s_3$. Again,
comparisons can only be made at equal volumes, as larger volumes imply
more eigenvalues in the region around the soft edge where correlations
are poorly described by Random Matrix Theory.



\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{d_level_space.eps}
\end{center}
\vspace*{-2mm}
\caption[a]{Distributions of the unfolded level spacings between the
first few eigenvalues in the dynamical case, compared to the Wigner surmise.
As in the quenched case, we find a small disagreement for the first
eigenvalues. But in contrast to the quenched case the agreement sets
in after almost just the 2nd eigenvalue, at the same volume.}
\label{fig:d_level_space}
\end{figure}



\noi
There is an interesting physical consequence of a genuine gap in
the Dirac eigenvalue spectrum. Consider the difference between the
($\pi$) susceptibility $\chi_P$ and the susceptibility of its scalar 
partner ($a_0$), which we denote by $\chi_S$ \cite{B,C}. In a manner similar
to the Banks-Casher formula for the chiral condensate one finds that
this difference can be written
\beq
\omega ~=~ 4m^2 \int_0^{\infty} \! d\lambda ~\frac{\rho(\lambda;m)}{
(\lambda^2+ m^2)^2} ~,
\eeq
where the spectral density $\rho(\lambda;m)$ includes the zero modes
due to topology as well. In the infinite-volume limit this contribution
from exact zero modes should vanish, and we should be left with the
integral over non-zero modes. If the spectral density has a gap around
the origin this means that $\omega$ vanishes in the chiral limit. Because
axial U(1) rotates $\chi_P$ into $\chi_S$ and vice versa, this would
imply a restoration of axial U(1) at these high temperatures \cite{B,C}.
Conversely, if one believes that this axial U(1) symmetry is {\em not}
restored at high temperature, one gets constraints on the behavior of
the spectral density of the Dirac operator near the origin. For a power-law
behavior near $\lambda \sim 0$ a non-vanishing $\omega$ in the
infinite-volume chiral limit can only be supported for $\rho(\lambda,0)
\sim \lambda^{\alpha}$ with $\alpha \leq 1$, and in fact $\omega$ would
only remain finite in that limit if $\alpha = 1$.
 
\noi
Of course, the fact that we appear to see a gap in the eigenvalue
spectrum with staggered fermions at this particular coupling does not
imply that this gap persists in physical units as we take the continuum
limit. If not, we are here studying a pure lattice artifact. The only
way to test this is to study the shift in the apparent cut-off
eigenvalue $\lambda_0$ as we change the lattice spacing (this is, however,
far beyond what we can do at present). A very different uncertainty
comes from the fact that we are working with fermions that are almost
insensitive to topology at the couplings and volumes available to us.
This means that there are some would-be zero modes mixed up with our
regular eigenvalues near the origin. At zero temperature we found that
these would-be zero modes somewhat surprisingly behaved as the non-zero
eigenvalues at realistic couplings and volumes \cite{DHNR}. But there
is no guarantee that this is the case at finite temperature. This means
that the small tail extending to zero in our quenched simulations, and
some of the smallest eigenvalues in the simulations with dynamical
fermions may be due to these would-be zero modes. In particular, the
disagreement with Airy-function behavior very close to the soft edge
may be partly due to these would-be zero modes.
