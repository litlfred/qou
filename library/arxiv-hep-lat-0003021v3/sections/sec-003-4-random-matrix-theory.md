---
doc_id: arxiv-hep-lat-0003021v3
doc_title: "arXiv:hep-lat/0003021v3 19 May 2000"
section_id: sec-003-4-random-matrix-theory
section_title: "Random Matrix Theory"
section_number: 4
pages: 14-19
source_pdf: 0003021v3.pdf
source_sha256: b35dfd9ab88b71d8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.704
doc_brief: "arXiv:hep-lat/0003021v3 19 May 2000 — We compute the low-lying spectrum of the staggered Dirac operator above and below the ﬁnite temperature phase transition in both quenched QCD and in dynamical"
---
\label{RMT}

We have just shown our lattice gauge theory data for the spectrum of the
Dirac operator below, around, and above $T_c$, and compared it with
some of the analytical formulas of Random Matrix Theory in the limit
where the size of these matrices $N$ goes to infinity. It is of interest
to see how a simple {\em model} of a chiral phase transition in Random
Matrix Theory behaves at finite $N$, as some external parameter (mimicking
temperature $T$) is changed. The model we shall focus on here
was proposed by Jackson and Verbaarschot in the first of Ref.~\cite{JV}
and has also been studied in Ref.~\cite{Tilo}. 
It is based on a modified chiral ensemble
of $N\times N$ complex matrices $W$, with partition function 
\beq
{\cal Z} ~=~ \int\! dW \prod_{f=1}^{N_{f}}\det(M - im_f) \exp\left[-N
Tr(WW^{\dagger})\right] \label{RMM} 
\eeq
in a sector of topological charge zero. Here  
\beq
M ~=~ \left( \begin{array}{cc}
              0 & W^{\dagger} + T\\
              W + T & 0
              \end{array}
      \right)
\eeq
is a $2N\times 2N$ 
block hermitian matrix, and the external deterministic parameter $T$
is playing a r\^{o}le reminiscent of temperature. In the 
normalization chosen here, a continuous ``phase transition'' occurs at
$T_c = 1$, where the spectral density $\rho(\lambda)$ of the eigenvalues
of the random matrices just reaches zero \cite{JV}. For $T > T_c$ the
spectrum becomes two-banded, with a gap surrounding zero. The global shape 
of $\rho(\lambda)$ in this model will be very
different from the actual (macroscopic) Dirac operator spectral density. But
the interesting feature lies in having here a simple model which qualitatively
seems to describe some of the observed behavior of the staggered Dirac operator
with $N_f=4$, in particular the apparent
gap in the density for $T > T_c$.\footnote{Many other details do not match
at all. For instance the ``phase transition'' in the model (\ref{RMM}) is
continuous, in contrast to the finite-temperature phase transition in the 
massless $N_f=4$ theory, which is believed to be of first order.} 

\noi
It is very simple to do quenched ($i.e$, $N_f=0$) 
numerical simulations of the above 
Random Matrix model, as it just corresponds to generating an ensemble
of complex matrices with Gaussian weight. Such matrices are ``maximally
random'' in that their matrix elements are independently of Gaussian 
distribution. This
allows us to choose very large random matrices numerically, and then 
finding the eigenvalues of the hermitian matrix $M$. In this way we have
studied the detailed behavior of the finite-$N$ Random Matrix model
(\ref{RMM}) just below $T_c$, at $T_c$, and just above $T_c$ (where the
two bands separate as the gap develops).\footnote{Similar numerical
studies have been performed by K. Splittorff, M.Sc. thesis, The Niels Bohr 
Institute 1999 (unpublished). Simulations of the
macroscopic spectral density in this model can also be found in the original
paper by Jackson and Verbaarschot \cite{JV}.}   



\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{diff_macroscopic.eps}
\end{center}
\vspace*{-2mm}
\caption{Full spectra of $200\times200$ matrices at $T=0, 0.5, 0.75, 1.0,
1.2, 2.0$. In this simple model a gap indeed develops around 
$\lambda = 0$ at $T=1$.}
\label{fig:diff_macroscopic}
\end{figure}


 

\noi
We show some of our numerical results in Figs.~\ref{fig:diff_macroscopic} 
and \ref{fig:diff_microscopic}. First, in 
Fig.~\ref{fig:diff_macroscopic} we display a sequence of the macroscopic 
spectral density with increasing magnitude of the
parameter $T$: $T= 0, 0.5, 0.75, 1.0, 1.2, 2.0$. The plots were made by
diagonalizing 10000 $200\times200$ matrices. At $T=0$ this macroscopic
Random Matrix Theory spectrum is just the Wigner semi-circle law (we display
only the $\lambda > 0$ part):
\beq
\rho(\lambda,T=0) = \frac{1}{2\pi}\sqrt{4 - \lambda^2} ~.
\eeq


\noi
As $T$ increases, a dip in the spectral density around $\lambda = 0$ slowly
develops, and it subsequently turns into a gap. Of course, this macroscopic
Random Matrix Theory spectrum is totally unlike the macroscopic
Dirac operator spectrum. But it is interesting to zoom in on the microscopic
behavior of the Random Matrix spectral density at the soft edge of the
gap. In this way, by blowing up the scale of the smallest eigenvalues,
we obtain the plots in Fig.~\ref{fig:diff_microscopic} for the same 
parameter values of $T$ as above.


\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{diff_microscopic.eps}
\end{center}
\vspace*{-2mm}
\caption{A blowup of the graphs in Fig.~\ref{fig:diff_macroscopic}. The 
microscopic spectrum changes smoothly from Bessel-type behavior to
Airy-type behavior, going through an intermediate ``critical'' 
distribution at $T=1$ corresponding to a macroscopic power-law behavior of
type $\rho(\lambda) \sim \lambda^{1/3}$. The exact analytical curve for the
microscopic spectral density at $T=1$ has been computed in
Ref.~\protect\cite{Z}.}
\label{fig:diff_microscopic}
\end{figure}


One sees clearly how the universal Bessel-kernel behavior below $T_c$
turns into the also universal Airy-kernel above $T_c$. We note that it is
has been shown in Ref.~\cite{JV} that the massless microscopic spectral
density of the above Random Matrix model has precisely the usual 
zero-temperature form,
\beq
\rho_s(\zeta(T)) ~=~ \frac{\zeta(T)}{2}\left[J_{N_{f}}(\zeta(T))^2
- J_{N_{f}-1}(\zeta(T))J_{N_{f}+1}(\zeta(T))\right] ~, 
\label{rhobessel}
\eeq
where $\zeta(T)$ is simply the eigenvalues rescaled by the (T-dependent) 
infinite-volume spectral density at the origin $\rho(0,T)$:
\beq
\zeta(T) ~=~ \lambda 2\pi N\rho(0,T) ~.
\eeq
In this model $\rho(0)$ approaches zero with a mean-field type of
behavior \cite{JV}:
\beq
\rho(0,T) ~=~ \rho(0,0)\sqrt{1 - T^2} ~.
\eeq
For $T$ bigger than $T_c$, but still close to it, we find, as expected,
a deformation of the Airy-kernel. In fact, the microscopic behavior
there smoothly interpolates between the Bessel-form and the Airy-form.
The peaks corresponding to individual eigenvalues from the Bessel-function
behavior below $T_c$ gradually smoothen out to become the inflection points
in the spectral density of the Airy-kind as the soft edge moves away from
the origin.
To illustrate how accurately one reproduces the Airy-behavior
in this kind of simulations, we show in 
Fig.~\ref{fig:matrix_airy_compare} the soft edge prediction appropriately 
scaled to fit simulation data at T=3.
The Airy-behavior is perfectly reproduced close to the edge, but with 
deviations after the first few eigenvalues(wiggles).  
The deviation is presumably caused by the limited number of eigenvalues
at $N=300$, and when $N$ is increased we expect the fit to improve.  




\begin{figure}
\begin{center}
\epsfxsize=0.6\textwidth
\epsffile{matrix_airy_compare.eps}
\end{center}
\vspace*{-2mm}
\caption{A blowup of a $T=3$ spectrum compared with the Airy-prediction.
There is nice agreement near the edge.}
\label{fig:matrix_airy_compare}
\end{figure}
