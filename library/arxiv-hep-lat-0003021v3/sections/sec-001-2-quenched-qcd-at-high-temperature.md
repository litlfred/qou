---
doc_id: arxiv-hep-lat-0003021v3
doc_title: "arXiv:hep-lat/0003021v3 19 May 2000"
section_id: sec-001-2-quenched-qcd-at-high-temperature
section_title: "Quenched QCD at high temperature"
section_number: 2
pages: 4-9
source_pdf: 0003021v3.pdf
source_sha256: b35dfd9ab88b71d8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.984
doc_brief: "arXiv:hep-lat/0003021v3 19 May 2000 — We compute the low-lying spectrum of the staggered Dirac operator above and below the ﬁnite temperature phase transition in both quenched QCD and in dynamical"
---
\label{quenched}

For our quenched finite temperature Monte Carlo
simulations we have used lattices
with temporal extent $N_t=4$ and up to three spatial volumes: $8^3$,
$12^3$ and $16^3$.  For $N_t=4$ the deconfinement phase transition for
SU(3) pure gauge theory with Wilson action
has been very accurately determined,
occurring at lattice gauge coupling $\beta_c=5.6925(2)$~\cite{T_c}.
It has for long been assumed that the chiral phase transition of the
quenched theory occurs at exactly this deconfinement phase transition
point of the pure gauge theory, but this has recently been challenged 
\cite{EHKN_fT}.

\noi
We now give some technical details of our simulations.
The gauge field configurations were generated with a mixture of
overrelaxation and heat bath updates, and were analyzed after every
20-th heat bath sweep. On each configuration we computed the 50
lowest-lying eigenvalues, and in some cases even more, using the variational
Ritz functional method \cite{Ritz}. Many ensembles consisted of several
thousand configurations. Gauge coupling, lattice size and statistics
of our ensembles is summarized in Table \ref{tab:q_ensemb}.

\begin{table}
\begin{center}
\begin{tabular}{c c c}
$V$ & $\beta$ & \#configurations \\
\hline
$8^3\times 4$ & 5.5 & 5931 \\
$8^3\times 4$ & 5.66 & 5544 \\
$8^3\times 4$ & 5.695 & 1769 \\
$8^3\times 4$ & 5.71 & 1145 \\
$8^3\times 4$ & 5.72 & 1426 \\
$8^3\times 4$ & 5.73 & 2021 \\
$8^3\times 4$ & 5.75 & 7029 \\
$12^3\times 4$ & 5.75 & 1933 \\
$16^3\times 4$ & 5.75 & 692 \\
$8^3\times 4$ & 5.8 & 5335 \\
$8^3\times 4$ & 5.85 & 6149 \\
$8^3\times 4$ & 5.9 & 4263 \\
$12^3\times 4$ & 5.9 & 1755 \\
$16^3\times 4$ & 5.9 &  824 \\
\hline
\end{tabular}
\end{center}
\caption[a]{Details of our quenched ensembles.}
\label{tab:q_ensemb}
\end{table}

\noi
As is well-known, the staggered Dirac operator
\beqn
\slash{D}_{x,y} &=& \frac{1}{2}\sum_{\mu}\eta_{\mu}(x)\left(U_{\mu}(x)
\delta_{x+\mu,y} - U^{\dagger}_{\mu}(y)\delta_{x,y+\mu}\right)\cr
&\equiv& \slash{D}_{e,o} + \slash{D}_{o,e} \label{staggeredD}
\eeqn
is anti-hermitian, with purely imaginary eigenvalues $i\lambda$ that come
in pairs of opposite sign. In eq.~(\ref{staggeredD})
\beq
\eta_{\mu}(x) ~=~ (-1)^{\sum_{\nu<\mu}x_{\nu}}
\eeq
are the usual phase factors for staggered fermions. 
Denoting 
\beq
\epsilon(x) ~=~ (-1)^{\sum_{\nu}x_{\nu}} ~,
\eeq 
we have also
explicitly shown how $\slash{D}$ connects {\em even} sites, i.e. those
with $\epsilon(x)=+1$, with {\em odd} sites, those with $\epsilon(x)=-1$, and
vice versa. This means that the operator $-\slash{D}^2$ is hermitian and
positive semi-definite. The sign function $\epsilon(x)$ defined above
plays the role of $\gamma_5$ in the continuum: it
anticommutes with $\slash{D}: ~\{\slash{D},\epsilon\}=0$. As
$-\slash{D}^2$ does not mix between even and odd lattice sites, we need only
compute the eigenvalues, on, say, the even sublattice. One easily sees that if
$\psi_e$ is a normalized eigenvector of $-\slash{D}^2$ with eigenvalue
$\lambda^2$, then $\psi_o \equiv \frac{1}{\lambda} \slash{D}_{o,e}\psi_e$
is a normalized eigenvector of $-\slash{D}^2$ with eigenvalue $\lambda^2$,
and non-zero only on odd sites. Moreover, as we will never encounter exact
zero modes on genuine quantum configurations, there is no difficulty with 
the above definition of $\psi_o$. We of course make use of these properties, 
and hence compute only the (positive) eigenvalues of
$-\slash{D}^2$ restricted to the even sublattice, and then take the
(positive) square root. All eigenvalues 
to be shown in the following thus have an equal number of negative
companions, of the exact same magnitude.

\noi
The spectral density of the Dirac operator is given by
\beq
\rho(\lambda) ~\equiv~ \frac{1}{V}\langle \sum_n\delta(\lambda -
 \lambda_n)\rangle ~,
\eeq
and it is readily computed numerically from our Monte Carlo simulations
by a binning of the measured eigenvalues per configuration at convenient
small intervals.




\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{various_quenched.eps}
\end{center}
\vspace*{-2mm}
\caption[a]{The measured distribution of the 50 lowest eigenvalues in quenched 
QCD at finite temperature for several $\beta$'s on $8^3 \times 4$ lattices.
One sees a clear suppression of the spectral density at the origin
$\rho(0)$ as the temperature (coupling) is increased, indicating
a diminishing chiral condensate according to the Banks-Casher formula. For
large temperatures the spectrum is heavily suppressed near the origin,
although in this quenched case a small tail always seems to extend towards
$\lambda=0$ (see below).}
\label{fig:various_quenched}
\end{figure}



\noi 
In Fig.~\ref{fig:various_quenched} we show the density of low
lying eigenvalues on $8^3 \times 4$ lattices for several $\beta$
values between 5.5 (in the confined phase) to 5.9 (in the deconfined
phase).  In each case we computed the 50 lowest positive eigenvalues
$i\lambda$ of the staggered Dirac operator. The plots are normalized
by the following condition, $\int_0^{\infty}\rho(\lambda)d\lambda=\textrm{\#eigenvalues}/V$.
In the confined phase it is quite evident that the density at zero
would be non-zero in the thermodynamic limit. As the temperature is
increased, the density at zero decreases.
There is a qualitative change of the eigenvalue density once the
temperature is increased above $T_c$. Beyond the first few eigenvalues
the eigenvalue density assumes a shape compatible with a square root
behavior (\ref{eq:sqrt_rho}). However, a sizable tail, decreasing with
increasing temperature, of small eigenvalues persists, which seems to
extend all the way down to zero.



\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{q_vol_test.eps}
\end{center}
\vspace*{-2mm}
\caption{The density of the smallest eigenvalues in the high
temperature phase of quenched QCD, at $\beta=5.9$,
for spatial volumes $8^3$, $12^3$
and $16^3$. In the two large volumes we measured 100 eigenvalues and
only 50 in the small volume.  Since the eigenvalue density increases
with increasing volume, the distributions are correspondingly cut off
at smaller $\lambda$. There is no observable change in the eigenvalue
density as the three-volume is increased. This holds even at the very
small tail extending towards $\lambda=0$, as shown in the magnified
plot inserted.}
\label{fig:q_vol_test}
\end{figure}



\noi
In Fig.~\ref{fig:q_vol_test} we compare the eigenvalue density in the
high temperature phase, at $\beta=5.9$, for several spatial volumes.
As can be seen the eigenvalue density is volume independent to a
surprising degree. In particular, the tail of small eigenvalues is
seen to be volume independent and appears to persist in the thermodynamic
limit. We note that the tail is much larger than would be compatible with
the exponential tail from the Airy function behavior of random matrix
theory at a soft edge eq.~(\ref{eq:Airy_asympt}) (see
Fig.~\ref{fig:Airy_compare} in section 3 below for an example).

\noi
It is tempting to speculate that the tail seen here in the quenched case
with staggered fermions is a reflection of the accumulation of small
eigenvalues seen with overlap fermions in \cite{EHKN_fT} and attributed
there to a dilute gas of instantons and anti-instantons. In the staggered
case, the explicit chiral symmetry breaking at finite lattice spacing
shifts the small modes, presumably resulting in the observed tail.



\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{q_level_space.eps}
\end{center}
\vspace*{-2mm}
\caption{Distributions of the unfolded level spacings between the
first few eigenvalues for $\beta=5.75$ on an $8^3\times 4$ lattice,
compared to the Wigner surmise.
The agreement with Random Matrix Theory is clear once we go beyond
the first few eigenvalues. However, there is not very good agreement
for the first 2-3 eigenvalues at this volume. }
\label{fig:q_level_space}
\end{figure}



\noi
We also looked at the unfolded level spacing between 
individual eigenvalues $i$ and $i+1$
\beq
s_i~=~\frac{\lambda_{i+1}-\lambda_i}{\langle\lambda_{i+1}-\lambda_i\rangle}\,.
\label{eq:level_space}
\eeq
In Fig.~\ref{fig:q_level_space} the distribution of the $s_i$ between 
eigenvalue $i$ and $i+1$, $i=1..6$ is shown and compared to the expected 
distribution, the Wigner surmise
\beq
P(s) = \frac{32}{\pi^2}s^2e^{-\frac{4}{\pi}s^2}\,.
\eeq
Evidently, the level spacings between the first eigenvalues are not very 
accurately given by Random Matrix Theory correlations. 
But as we move into the bulk, say for $i>5$ in the case of the $8^3\times 4$
lattice, the agreement with Random Matrix Theory becomes almost perfect.
It should be stressed here that this is a volume-dependent statement.
For larger volumes one needs to go beyond more eigenvalues starting at
the soft edge before one finds good agreement. This is consistent with the
fact that there is a definite scale around the soft edge, where eigenvalue
correlations are poorly described by Random Matrix Theory. Going to larger
volumes simply forces more eigenvalues into that region.
