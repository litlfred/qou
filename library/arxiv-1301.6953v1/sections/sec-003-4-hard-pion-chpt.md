---
doc_id: arxiv-1301.6953v1
doc_title: "Chiral Perturbation Theory and Mesons"
section_id: sec-003-4-hard-pion-chpt
section_title: "Hard pion ChPT"
section_number: 4
pages: 7-8
source_pdf: 1301.6953v1.pdf
source_sha256: 8c9231d0832df3b6
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.98
doc_brief: "Chiral Perturbation Theory and Mesons — 7 sections: Front matter; Chiral Perturbation Theory; Introduction"
---
The usual formulation of the powercounting in mesonic ChPT \cite{Weinberg0}
assumes that all the momenta in all diagrams are soft and this allows the
powercounting to work as simple dimensional counting. In baryon and heavy
meson ChPT one takes a step further. There is a line with a heavy mass
running through all diagrams but in a way all spatial momenta can still be
considered small. In vector meson ChPT it has been argued that it is possible
to also include diagrams where lines take a hard momentum, but not a hard mass
\cite{HP0}. This type of arguments was used by Flynn and Sachrajda \cite{HP1}
to obtain results for $K_{\ell3}$ in the heavy Kaon limit also away from the
end-point. These arguments, as described below were generalized and applied
to a larger number of processes in \cite{HP2,HP3,HP4,HP5}. Some doubt on
the simple arguments has been presented in \cite{Procura,HP6}.

The underlying idea behind hard pion ChPT is that nonanalyticities in the
the light masses, e.g. pion, come from soft lines in the diagrams.
The couplings of soft particles and in particular soft pions are constrained by
current algebra via
\begin{equation}
\lim_{q\to 0}\langle\pi^k(q)\alpha|O|\beta\rangle
 = -\frac{i}{F_\pi}\langle\alpha|\left[Q_5^k,O\right]|\beta\rangle\,,
\end{equation}
and nothing prevents hard pions to be present in the states $|\alpha\rangle$
or $|\beta\rangle$. One thus expects that by heavily using current algebra
it should be possible to obtain chiral logarithms for almost any process.
 one can always expand in
soft momenta over hard momenta/large masses in a way which is analogous to
the treatment of infrared divergences in QED. The general argument was
already described in my previous chiral dynamics talk \cite{talk2} and
can be found in \cite{HP2,HP3,HP4} as well. It roughly goes as follows:
Take any diagram with a particular external and internal momentum configuration.
Identify the soft lines and cut them.
The resulting part is analytic in the soft stuff and
should thus be describable by an effective Lagrangian with
coupling constants dependent on the external given
momenta (Weinberg's folklore theorem \cite{Weinberg0})
Lagrangian in hadron fields with all orders of derivatives.
This effective Lagrangian should be thought of as a Lagrangian in hadron fields
but all possible orders of the momenta included: possibly
an infinite number of terms
If symmetries are present, the Lagrangian should respect them.
The problem is that the simple power-counting is gone
In some cases we can argue that up to a certain order in
the expansion in light masses, not momenta, matrix
elements of higher order operators are reducible to those
of lowest order, first done in \cite{HP1} for $K_{\ell3}$ and later generalized.
The Lagrangian should be complete in the neighbourhood of the
original process and loop diagrams with this effective Lagrangian should
reproduce the non-analyticities in the light masses.
The latter is the crucial part of the argument.

A check at two-loop order has been performed for the pion vector and scalar
form-factor in \cite{HP3,HP4} and was found to work well. Applications to the
$B,D\to\pi,K,\eta$ vector form-factors can be found in \cite{HP4} and to
some charmonium decays in \cite{HP5}. In Fig.~\ref{fig4} I show how the
inclusion of the chiral logarithms improves the relation between the
$D\to\pi$ and $D\to K$ form-factors \cite{HP4} using the CLEO data \cite{CLEO}.
\begin{figure}
\begin{minipage}{0.48\textwidth}
\includegraphics[angle=270, width=0.99\textwidth]{cleof+.eps}
\end{minipage}
\begin{minipage}{0.48\textwidth}
\includegraphics[angle=270, width=0.99\textwidth]{cleof+logs.eps}
\end{minipage}
\caption{\label{fig4} The left plot shows the form-factor $f_+$ in $D\to\pi e\nu$
and $D\to K e\nu$ decays from CLEO \cite{CLEO}. In the right hand side
the $D\to K e\nu$ has been corrected with the chiral logarithms via
$f_{+D\to\pi}=f_{+D\to K} F_{D\to\pi}/F_{D\to K}$ \cite{HP4}.}
\end{figure}

Recently \cite{Procura,HP6}, the test done at two loops was extended to
higher orders. What was found there was that the hard pion ChPT prediction
held to all orders for the elastic intermediate state but failed in a
three loop calculation of the inelastic four-particle-cut part.
For details I refer to \cite{Procura,HP6}.
The arguments for the general method are the same as for
IR divergences, SCET,\ldots, so I do believe these to be valid.
Something like hard pion ChPT should exist. 
The arguments for the proportionality to the lowest order
are much weaker and
assume that each soft propagator has a free momentum. The calculation of
\cite{HP6} was done using dispersive methods and a full calculation
at 3 loops will be very difficult but would allow a better study of why the
arguments failed. The ultimate would of course be to find
a proper power-counting under the given assumptions.
