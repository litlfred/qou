---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-012-31-chiral-perturbation-theory-and-power-counting
section_title: "Chiral perturbation theory and power counting"
section_number: 3.1
pages: 16-18
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.997
latex_coverage_ratio: 1.0
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
Effective Lagrangians have infinitely
many terms, and an unlimited number of Feynman graphs can be calculated
from them. Therefore, 
we need a scheme that makes the theory manageable and calculable.
This scheme
which tells us how to distinguish between large
(important) and small (unimportant) contributions
is chiral perturbation theory (ChPT).

In ChPT, 
graphs are analyzed
in terms of powers of small external momenta over the large scale:
$(Q/\Lambda_\chi)^\nu$,
where $Q$ is generic for a momentum (nucleon three-momentum or
pion four-momentum) or a pion mass and $\Lambda_\chi \sim 1$ GeV
is the chiral symmetry breaking scale (hadronic scale, hard scale).
Determining the power $\nu$ 
has become known as power counting.

For the moment, we will consider only so-called irreducible
graphs; the problem of reducible or iterative
diagrams and their relevance for the $NN$ system
will be discussed later (cf.\ Section~\ref{sec_reno}).
By definition, an irreducible graph is a diagram that
cannot be separated into two
by cutting only nucleon lines.
Following the Feynman rules of covariant perturbation theory,
a nucleon propagator is $Q^{-1}$,
a pion propagator $Q^{-2}$,
each derivative in any interaction is $Q$,
and each four-momentum integration $Q^4$.
This is also known as naive dimensional analysis.
Applying then some topological identities, Weinberg obtained
for the power of an irreducible diagram
involving $A$ nucleons~\cite{Wei90,Wei91,Wei92}
\begin{equation}
\nu_W = 4 - A - 2C + 2L + \sum_i \Delta_i 
\label{eq_nuw}
\end{equation}
with
\begin{equation}
\Delta_i  \equiv   d_i + \frac{n_i}{2} - 2  \, ,
\label{eq_Deltai}
\end{equation}
where $C$ denotes the number of separately connected pieces and
$L$ the number of loops in the diagram;
$d_i$ is the number of derivatives or pion-mass insertions 
and $n_i$ the number of nucleon fields (nucleon legs)
involved in vertex $i$;
the sum runs over all vertices $i$ contained in the diagram 
under consideration.
Note that $\Delta_i \geq 0$
for all interactions allowed by chiral symmetry.
Purely pionic interactions have at least two derivatives
($d_i\geq 2, n_i=0$);
interactions of pions with a nucleon have at least one
derivative
($d_i\geq 1, n_i=2$);
and nucleon-nucleon contact terms ($n_i=4$)
have $d_i\geq0$.
This demonstrates how chiral symmetry
guarantees a low-energy expansion.

The Weinberg formula 
Eq.~(\ref{eq_nuw})
works well for connected diagrams
with $A \leq 2$ nucleons and any number of pions, 
but there are problems when applied in 
systems with $A\geq 3$.

To illustrate the problem, consider
one-pion exchange 
($L=0$, $\Delta_i=0$) 
between two nucleons
in an $A=2$ system ($C=1$) which yields 
$\nu_W=0$.
Now, when the same interaction occurs
in an $A=3$ environment, then $C=2$, since one
nucleon is not interacting, and 
Eq.~(\ref{eq_nuw}) 
produces $\nu_W=-3$.
The reason for this result is that, by widespread convention~\cite{PDG},
particle states are normalized to Dirac $\delta$-functions,
\begin{equation}
\langle p' | p \rangle = 
\delta^3(\vec p - {\vec p}~') 
\,,
\label{eq_norm}
\end{equation}
which carry dimension $Q^{-3}$.
A nucleon line 
passing through a diagram
without interaction is represented by such a 
three-momentum-conserving
$\delta$-function. 

The above-illustrated $A$-dependence of the power $\nu_W$
is undesirable.
As indicated, the reason for the problem is the dimension $(-3)$
introduced for each nucleon through the normalization Eq.~(\ref{eq_norm}).
Therefore, to fix the problem,
we add $(+3A)$ to Eq.~(\ref{eq_nuw}) and subtract $6$ to have the $A=2$ case
unaltered.
Thus, we introduce the new power $\; \nu=\nu_W+3A-6$, which reads explicitly,
\begin{equation} \nu = -2 +2A - 2C + 2L 
+ \sum_i \Delta_i \, .  
\label{eq_nu} 
\end{equation}
This definition of the power $\nu$ will be applied
throughout this report.
It is also what is used in other works~\cite{Epe06}.
Another way to get the formula Eq.~(\ref{eq_nu}) is to define $\nu$
as the difference between $\nu_W$ and the smallest possible power,
$\nu_{\rm min}$: $\nu=\nu_W-\nu_{\rm min}$.
The minimal power $\nu_{\rm min}$ is obtained from Eq.~(\ref{eq_nuw})
for the case of no loops ($L=0$), $\Delta_i=0$ for all vertices, and the 
maximal number of separately connected pieces, which is $C=A-1$
if at least two nucleons interact;
thus, $\nu_{\rm min}=6-3A$.

Notice that, even though $A$ still appears in 
Eq.~(\ref{eq_nu}), 
the formula is essentially $A$ independent:
when a non-interacting nucleon is added,
$A$ and $C$ go up by one, which cancels.
From the above derivation, 
it should also be clear that Eq.~(\ref{eq_nu})
is suitable only for systems with $A \geq 2$ nucleons
while 
Eq.~(\ref{eq_nuw})
may be used for connected graphs with $A \leq 2$.

An alternative method for developing a reasonable
power formula has been presented by Friar~\cite{Fri97},
who considers the expectation value of an $m$-nucleon operator 
($m\leq A$) in $A$-nucleon space.
Working in configuration space generates additional
phase-space factors of power $3(A-1)$
to be added to Eq.~(\ref{eq_nuw}).
Thus, Friar's power is $\nu_F =\nu_W +3A-3=\nu+3$.
The additional power of three by which Friar differs from
Eq.~(\ref{eq_nu})
is due to an additional momentum-space integration
that converts the units of a momentum-space potential
into units of energy, which is reasonable.
Finally, we note that
normalizing the
nucleon states in a box to a Kronecker-$\delta$ (instead of
using the Dirac $\delta$-function normalization of the continuum)
should lead to Eq.~(\ref{eq_nu}) 
in a straightforward fashion.

In any case,
the most important observation from power counting is that
the powers are bounded from below and, 
specifically, $\nu \geq 0$. 
This fact is crucial for the convergence of 
the low-momentum expansion.

Moreover, the power formula 
Eq.~(\ref{eq_nu}) 
allows to predict
the leading orders of connected multi-nucleon forces.
Consider a $m$-nucleon irreducibly connected diagram
($m$-nucleon force) in an $A$-nucleon system ($m\leq A$).
The number of separately connected pieces is
$C=A-m+1$. Inserting this into
Eq.~(\ref{eq_nu}) together with $L=0$ and 
$\sum_i \Delta_i=0$ yields
$\nu=2m-4$. Thus, two-nucleon forces ($m=2$) start 
at $\nu=0$, three-nucleon forces ($m=3$) at
$\nu=2$ (but they happen to cancel at that order),
and four-nucleon forces at $\nu=4$ (they don't cancel).
More about this in the next sub-section and 
Section~\ref{sec_manyNF}.

For later purposes, we note that for an irreducible 
$NN$ diagram ($A=2$, $C=1$), the
power formula collapses to the very simple expression
\begin{equation}
\nu =  2L + \sum_i \Delta_i \,.
\label{eq_nunn}
\end{equation}

In summary, the chief point of the ChPT expansion is
that,
at a given order $\nu$, there exists only a finite number
of graphs. This is what makes the theory calculable.
The expression $(Q/\Lambda_\chi)^{\nu+1}$ provides a rough estimate
of the relative size of the contributions left out and, thus,
of the accuracy at order $\nu$.
In this sense, the theory can be calculated to any
desired accuracy and has
predictive power.
