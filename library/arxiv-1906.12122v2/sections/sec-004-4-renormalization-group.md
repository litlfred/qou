---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear effective field theory: status and perspectives"
section_id: sec-004-4-renormalization-group
section_title: "Renormalization group"
section_number: 4
pages: 12-13
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives — 34 sections: Contents; Two-body scattering amplitude; Power counting"
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.975
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



\subsubsection{Dibaryon fields}
\label{sec:Dibaryons}

It is possible to efficiently capture the physics associated with the shallow
$S$-wave two-body states by introducing in the effective Lagrangian ``dimeron''
(``molecular'' or, here, ``dibaryon'') fields with their quantum numbers, an
idea first introduced in EFT by \textcite{Kaplan:1996nv}.  For {any single
channel} we can write, instead of~\eqref{eq:L-NN-simple},

\begin{multline}
 {\!\LL
 = \psi^\dagger
 \Big(\ii\partial_0 + \frac{\Laplace}{2\MN}\Big)\psi
  + g\left[d^\dagger (\psi\psi) + \hc\right]} \\
  {\null + d^\dagger \Big[\eta\Big(\ii\partial_0
  + \frac{\Laplace}{4\MN}\Big) -\Delta \Big] d
  + \cdots \,,}
\label{eq:L-NN-simple-d}
\end{multline}

where $\eta=\pm 1$ is a parameter that determines the sign of the effective
range. It will be fixed to $\eta=-1$ in the remainder of this section to ensure
$r_0>0$.  Instead of $C_0$ and $C_2$, we have the new parameters $\Delta$ (the
``residual mass'') and $g$.  With this choice, nucleons no longer couple
directly, but only through the $s$-channel exchange of the dibaryon {$d$}.
If one neglects the kinetic term for this field, it is possible to recover the
leading terms in Eq.~\eqref{eq:L-NN-simple} by using the equation of motion
for {$d$},

\begin{equation}
 {d = \frac{g}{\Delta} \psi\psi\,,}
\end{equation}

and identifying $C_0 = -g^2/\Delta$.  Because of this redundancy, without loss
of generality one may fix $g$ at LO; a convenient choice is
$g^2\equiv 4\pi/m_N$~\cite{Griesshammer:2004pe} so that $\Delta=-1/a_0$
represents the low-energy scale $\Mlo$.
The {$d$} kinetic term leads to both energy- and
momentum-dependent four-nucleon-field interactions, corresponding to a choice of
operators that differs from Eq.~\eqref{eq:L-NN-simple}, but can be shown to be
equivalent up to higher orders and field redefinitions~\cite{Bedaque:1999vb}.

The original bubble series with $C_0$ vertices turns into a self-energy
correction for the dibaryon field: whereas the tree-level bare propagator is
just $\ii D(p_0,\vecp) = {-}\ii/\Delta$, summing up all bubble insertions as
shown in Fig.~\ref{fig:DibaryonProp} gives the full LO propagator as

\begin{equation}
 \ii D^{(0)}(p_0,\vecp)
 = {-}\ii \left[ \Delta + g^2 \, I_0\!\left(\sqrt{\MN p_0-\vecp^2/4}\right)
 \right]^{-1} \,.
\label{eq:Delta-L0}
\end{equation}

The {center-of-mass} $N\!N$ scattering amplitude is recovered by attaching
nucleon-dibaryon
vertices on both ends: $T^{(0)} = {-}g^2 D^{(0)}(p_0=k^2/\MN,\vecp=0)$.


\begin{figure}[tb]
\centering
\includegraphics[clip,width=0.99\columnwidth]{DibaryonProp}
\caption{Bubble sum for the dressed dibaryon propagator
 obtained from the bare propagator (double dashed line).
}
\label{fig:DibaryonProp}
\end{figure}


Not only is the dibaryon formalism useful to study processes with deuterons in
the initial and/or final state (see below), where it can conveniently be used
as an interpolating field, but it also makes higher-order corrections
particularly
simple.  For example, where before we had to insert $C_2$ vertices in different
places (see Fig.~\ref{fig:C2-corr}), we now only have to insert the dibaryon
kinetic-energy operator into the LO propagator, giving

\begin{equation}
 \ii D^{(1)}(p_0,\vecp)
  = \ii \left(p_0-\frac{\vecp^2}{4m_N}\right) \left(D^{(0)}(p_0,\vecp)\right)^2
\label{eq:Delta-NLO}
\end{equation}

at NLO.  As in the case without dibaryons, renormalization is carried out
by relating $D^{(1)}$ to the NLO amplitude correction $T^{(1)}(k)$ and matching
to the effective-range term in Eq.~\eqref{eq:T-kcot-b}.  A difference is,
however, that this is now carried out with an energy-dependent operator---note
the dependence of Eq.~\eqref{eq:Delta-NLO} on the Galilei-invariant energy
$\tilde{p}_0=p_0-\vecp^2/(4\MN)$---whereas our choice of $C_2$ terms in
Eq.~\eqref{eq:L-NN-simple} only includes momentum-dependent operators.  The NLO
component of $g$ can be adjusted to reproduce $r_0$, and $g$ and $\Delta$ are
now independent.  This means that these parameters have RG runnings that differ
from those for $C_0$ and $C_2$~\cite{Birse:1998dk}.

With a dibaryon, range effects can be resummed using the propagator

\begin{equation}
 \ii D^{\text{resum}}(p_0,\vecp)
 = \frac{{-}\ii}
 {\Delta + g^2 \, I_0\!\left(\sqrt{\MN \tilde{p}_0\vphantom{2^3}}\right)
 - \tilde{p}_0} \,.
\label{eq:Prop-d-resum}
\end{equation}

The Wigner bound is automatically avoided by allowing the dibaryon to be a
ghost field.  In fact, \textcite{Beane:2000fi} proposed that the relatively
large sizes of the $N\!N$ effective ranges (about $2m_\pi^{-1}$) justify their
resummation as an LO effect.  However, this procedure leads to two $S$-matrix
poles per channel and is thus more likely to be interpreted as a resummation of
NLO interactions, which includes additional higher-order effects.
