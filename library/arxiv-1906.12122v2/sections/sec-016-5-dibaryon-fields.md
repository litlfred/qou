---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-016-5-dibaryon-fields
section_title: "Dibaryon fields"
section_number: 5
pages: 13-13
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.995
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
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
