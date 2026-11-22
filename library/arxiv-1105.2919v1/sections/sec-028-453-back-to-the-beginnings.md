---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-028-453-back-to-the-beginnings
section_title: "Back to the beginnings"
section_number: 4.5.3
pages: 38-39
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The various problems with the renormalization procedures discussed above
may have a simple common reason:
An EFT that has validity only for momenta $Q < \Lambda_\chi$ is applied such that
momenta $Q \gg \Lambda_\chi$ are heavily involved (because the regulator cutoff
$\Lambda \rightarrow \infty$).
A recent paper by Epelbaum and Gegelia~\cite{EG09} illustrates the point:
The authors construct an exactly solvable toy-model that simulates a pionful EFT 
and yields finite results for
$\Lambda \rightarrow \infty$.  However, as it turns out, these
finite results are incompatible with the underlying EFT, while
for cutoffs in the order of the hard scale consistency is maintained.
In simple terms, the point to realize is this: 
{\it If an EFT calculation produces (accidentally) a finite result for
$\Lambda \rightarrow \infty$, then that
does not automatically imply that this result is also meaningful.}

This matter is further elucidated in
the lectures by Lepage of 1997~\cite{Lep97}.
Lepage points out that it makes little sense to take the momentum cutoff beyond
the range of validity of the effective theory. By assumption, our data involves energies
that are too low---wave lengths that are too long---to probe the true structure of
the theory at very short distances. When one goes beyond the hard-scale of the theory,
structures are seen that are almost certainly wrong. Thus, results cannot improve
and, in fact, they may degrade or, in more extreme cases, the theory may become
unstable or untunable. In fact, in the $NN$ case, this is what is happening in 
several partial waves (as reported above). Therefore, Lepage
suggests to take the following three steps when building an effective theory:
\begin{enumerate}
\item
Incorporate the correct long-range behavior: The long-range behavior of the underlying
theory must be known, and it must be built into the effective theory. In the case of
nuclear forces, the long-range theory is, of course, well known and 
given by one- and multi-pion exchanges.
\item
Introduce an ultraviolet cutoff to exclude high-momentum states, or, equivalent, to soften the 
short-distance behavior: The cutoff has two effects: First it excludes high-momentum states,
which are sensitive to the unknown short-distance dynamics; only states that we understand
are retained. Second it makes all interactions regular at $r=0$, thereby avoiding the infinities
that beset the naive approach.
\item
Add local correction terms (also known as contact or counter terms) 
to the effective Hamiltonian. These mimic the effects of the 
high-momentum states excluded by the cutoff introduced in the previous step.
In the meson-exchange picture, the short-range nuclear force is described by
heavy meson exchange, like the $\rho(770)$ and $\omega(782)$. However, at low
energy, such structures are not resolved. Since we must include contact terms 
anyhow, it is most efficient to use them to account for any heavy-meson exchange
as well.
The correction terms systematically remove dependence on the cutoff.
\end{enumerate}

A first investigation in the above spirit has been
conducted by Epelbaum and Mei\ss ner~\cite{EM06} in 2006.
The authors stress that there is no point in taking the cutoff $\Lambda$ beyond the
breakdown scale of the EFT, $\Lambda_\chi \approx m_\rho \approx 1$ GeV,
since the error of the calculation is not expected to decrease
in that regime.
Any value for the cutoff parameter $\Lambda$
is acceptable if the error associated with its finite value is within
the theoretical uncertainty at the given order.
The authors conduct an investigation at LO (including only the counter terms
implied by Weinberg counting)
and find that,
starting from $\Lambda \approx 3$ fm$^{-1}$, the error
in the $NN$ phase shifts due to keeping $\Lambda$ finite
stays within the theoretical uncertainty at LO.



\begin{figure}[t]\centering
\vspace*{-1.5cm}

\scalebox{0.55}{\includegraphics{ph1_orders.pdf}}
\vspace*{-2.5cm}
\caption{Phase shifts of $np$ scattering
as calculated from $NN$ potentials at different
orders of ChPT. The black dotted line is LO(500), 
the blue dashed is NLO(550/700)~\cite{EGM04},
the green dash-dotted NNLO(600/700)~\cite{EGM04},
and the red solid N$^3$LO(500)~\cite{EM03}, where the 
numbers in parentheses denote the cutoffs in MeV.
Partial waves with total angular momentum $J\leq 1$
are displayed.
Empirical phase shifts (solid dots and open circles)
as in Fig.~\ref{fig_f}.
\label{fig_phorders1}}
\end{figure}


\begin{figure}[t]\centering
\vspace*{-1.5cm}

\scalebox{0.55}{\includegraphics{ph2_orders.pdf}}
\vspace*{-2.5cm}
\caption{Same as Fig.~\ref{fig_phorders1}, but
$J=2$ phase shifts and 
$J\leq 2$ mixing parameters are shown.
\label{fig_phorders2}}
\end{figure}
