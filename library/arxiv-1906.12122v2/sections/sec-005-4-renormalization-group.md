---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-005-4-renormalization-group
section_title: "Renormalization group"
section_number: 4
pages: 12-13
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.943
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 38 sections: Nuclear effective field theory: st; Contents; Two-body scattering amplitude"
---
\label{sec:RG}

\paragraph{Running coupling}
Imposing renormalizability of physical amplitudes leads to solutions of
RG equations.  Their detailed form depends on the regularization scheme.  For
example, in PDS one finds for the dimensionless coupling constant
$\hat{C_0}\equiv\MN\mu C_0/(4\pi)$~\cite{Kaplan:1998tg},

\begin{equation}
 \mu \frac{\dd}{\dd\mu} \hat{C_0} =
 \hat{C_0}(1+\hat{C_0})\,,
\label{eq:C0-running-mu}
\end{equation}

where the right-hand side is given by the beta function.  It is convenient to
consider the flow of $\hat{C_0}$ instead of $C_0$ in order to separate the
behavior of the operator from the behavior of  the coupling constant.  The RG
equation~\eqref{eq:C0-running-mu} has two fixed points: the free fixed point
$\hat{C_0}=0$ and a nontrivial fixed point
$\hat{C_0}=-1$~\cite{Weinberg:1991um}, which correspond to $a_0=0$ and to the
unitary limit $1/a_0=0$, respectively.  Similar equations can be derived for
all coupling constants in the effective Lagrangian, and the beta function will
in general change as one goes to higher orders.  Thus the expansion in Pionless
EFT can be thought of as an expansion around the unitary limit of infinite
scattering length, similar to the expansion in Chiral EFT around the chiral
limit of vanishing quark masses.  An equation similar
to~\eqref{eq:C0-running-mu} holds for a simple momentum cutoff $\Lambda$,
leading then to Eq.~\eqref{eq:C0-Lambda}.  In dimensional regularization with
minimal subtraction, on the other hand, the coupling $C_0$ is independent
of $\mu$~\cite{Kaplan:1996xu}.  In this scheme the unitary limit cannot be
reached for any finite value of the coupling.

\paragraph{Wilsonian renormalization group}
The RG is more generally useful to study the behavior of the EFT.  Extending
previous
work~\cite{Weinberg:1990rz,Weinberg:1991um,Adhikari:1995uu,Adhikari:1997dz,
Beane:1997pk,Phillips:1997xu,Kaplan:1998tg,Kaplan:1998we,Kaplan:1998sz},
\textcite{Birse:1998dk} studied the RG flow of an effective potential of the
form

\begin{equation}
 V_{2N}(\vecp',\vecp, k)= V_{2N}(\vecp',\vecp)+ C_{02} k^2 + \cdots \,,
\label{eq:V-ppk}
\end{equation}

where the additional energy-dependent terms compared to Eq.~\eqref{eq:V-pp}
come from a different choice of operators in the effective
Lagrangian~\eqref{eq:L-NN-simple}.  It is possible to trade energy dependence
for momentum dependence and \viceversa by field redefinitions or,
alternatively,
using the equation of motion.  Within a Wilsonian formulation of the
RG~\cite{Wilson-83}, demanding that the off-shell amplitude stays invariant
under a decrease in the momentum cutoff $\Lambda$ in the Lippmann-Schwinger
equation defines a ``running'' potential $V(p,p',k,\Lambda)$ which satisfies

\begin{equation}
 \frac{\partial V}{\partial \Lambda}
 = \frac{\MN}{2\pi^2} V(p',\Lambda,k,\Lambda)
 \frac{\Lambda^2}{\Lambda^2 - k^2}
 V(\Lambda,p,k,\Lambda) \,.
\end{equation}

Defining further a rescaled potential $\hat{V}$ by multiplying all quantities
with appropriate powers of $\Lambda$, \textcite{Birse:1998dk} showed that in
the limit where $\Lambda\to0$ there exist two IR fixed points satisfying
$\partial\hat{V}/\partial\Lambda=0$.
One of these, $\hat{V} = 0$, is trivial
whereas the second, nontrivial one corresponds to the unitary limit.
{Additional fixed points are accessible with further fine tuning
\cite{Birse:2015iea}.
An} extensive study including also higher waves was carried by
\textcite{Harada:2006cw} and \textcite{Harada:2007ua}.
The RG analysis captures
the results obtained from Feynman diagrams, which yield directly the solutions
of the RG equations.\footnote{{\textcite{Weinberg:1995mt} gives a
general discussion of the connection between the Wilsonian RG and the
conventional renormalization program.}}
It unifies both the natural and fine-tuned cases discussed
in Sec.~\ref{sec:PowerCounting}, and it is possible to derive the power counting
for either case by studying perturbations of the potential around the fixed
points.
