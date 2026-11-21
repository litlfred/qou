---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-009-2-power-counting
section_title: "Power counting"
section_number: 2
pages: 9-11
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.74
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
\label{sec:PowerCounting}

Of course, the power counting of the theory should be such that it actually
\emph{mandates} this procedure.  The small inverse $N\!N$ scattering lengths
introduce a genuine new low-momentum scale $\Mlo$ (or large length $\Mlo^{-1}$).
Typically, this is referred to as ``fine tuning'' because the existence of this
scale---at odds with the perfectly natural assumption that pion exchange should
set the lowest energy scale---implies that different contributions from quarks
and gluons have to combine in just the right way to produce this scenario (see
Sec.~\ref{subsec:qcdconn}).

Equation \eqref{eq:T-C0} is nothing but Eq.~\eqref{LS} for a two-body potential
$C_0$, which, from the discussion above, is enhanced by a factor $\Mlo^{-1}$.
The loops connecting two insertions of the potential contain nucleon
propagators, which from Eq.~\eqref{eq:L-NN-simple} we read off to be

\begin{equation}
 \ii D_N(p_0,\vecp)
 = \ii \left(p_0-\dfrac{\vecp^2}{2\MN}+\cdots + \ii\eps\right)^{-1} \,.
\end{equation}

Here, $p_0$ and $\vecp$ are the energy and momentum associated with a nucleon
line in Fig.~\ref{fig:BubbleChain}.  If a total momentum $k \sim Q$ runs
through the diagram, we see that, after regularization effects have been
removed by renormalization, the dominant contribution in a loop integral
$\dd q_0\dd^3 q$ will come from the region where $q\sim Q$.  Hence, keeping
in mind that $q_0$ is a nonrelativistic kinetic energy $\sim q^2/\MN$, we count

\begin{subalign}[eq:PionlessPC]
 \text{nucleon propagator} &\sim m_N Q^{-2} \,,
 \label{nucprop} \\
 \text{(reducible) loop integral} &\sim (4\pi m_N)^{-1} Q^5 \,.
 \label{redloopint}
\end{subalign}

Equations \eqref{nucprop} and~\eqref{redloopint} lead directly to the
estimate~\eqref{VGV} and imply that the one-loop contribution in
Fig.~\ref{fig:BubbleChain} scales like the tree-level one times a factor
$Q/\aleph$.  In fact, each additional dressing by one loop with a $C_0$ vertex
contributes such a factor.  Hence,
{in the regime} where $Q\sim\aleph \ll \LamNoPi$ each such {diagram} is
equally
important, and they all have to be summed up to get the LO amplitude
nonperturbatively.  On the other hand, for $Q\ll\aleph$ one can still use
a perturbative approach, so the counting here is able to capture both scenarios.

Operators with derivatives in the effective Lagrangian must contain inverse
powers of $\Mhi$ in order not to introduce additional low-energy poles in the
LO $T$ matrix.  They provide corrections to the $2N$ potential,

\begin{equation}
 V_{2N}(\vecp',\vecp) = C_{0} + C_{2} \left(\vecp'^2 + \vecp^2\right) + \cdots\,.
\label{eq:V-pp}
\end{equation}

Being suppressed, higher orders can be calculated in perturbation theory and
matched to an expansion of Eq. \eqref{eq:T-kcot-a}{,

\begin{equation}
 T = \frac{4\pi}{\MN}\frac{1}{1/a_0+\ii k}
 \left(1 + \frac{r_0k^2/2}{1/a_0+\ii k} + \cdots \right).
\label{eq:EREexp}
\end{equation}

The specific scaling with
$\Mhi$ can be inferred from this} and from regulator effects considered below.

For example, the NLO amplitude $T^{(1)}$ is the result from inserting a single
$C_2$ vertex into each combination that can be formed with the LO amplitude
\cite{Bedaque:1997qi,vanKolck:1997ut,Kaplan:1998tg,Kaplan:1998we,
Bedaque:1998mb,vanKolck:1998bw}, as shown in Fig.~\ref{fig:C2-corr}.  Matching
to the {$k^2$} coefficient in {Eq.~\eqref{eq:EREexp}}

shows that the $C_2$ contributions are related to the effective ranges.  Since
the values of the $N\!N$ $S$ waves
{are} $r_{\ThreeSOne}\simeq 1.75~\fm$ and $r_{\OneSNot}\simeq 2.7~\fm$,
and thus of the order $\Mpi^{-1}\sim\Mhi^{-1}$, we
conclude $C_2$ is indeed an NLO effect,

\begin{equation}
 \frac{C_2 Q^2}{C_0} \sim \frac{Q^2}{\Mlo\Mhi} \,.
\label{eq:scaling-re}
\end{equation}

For comparison, given that the $C_0$ term is a dimension-6 operator whereas the
one with $C_2$ is {dimension-8}, the na\"ive (natural) scaling is
$C_2 Q^2 / C_0 \sim (Q/\LamNoPi)^2$.  The additional low-energy enhancement
$\aleph$ also occurs in the scaling of the $C_2$ parameters.


\begin{figure}[tb]
\centering
\includegraphics[clip,width=0.85\columnwidth]{C2-corr-new}
\caption{NLO correction to the $N\!N$ scattering amplitude from the $C_2$
 interaction (circled circle).}
\label{fig:C2-corr}
\end{figure}


This procedure can be generalized to higher orders and other operators.  At
N$^2$LO we must consider two insertions of $C_2$ and one insertion of $C_4$; the
latter is determined entirely in terms of $r_0^2$, the shape parameter emerging
at N$^3$LO~\cite{Kaplan:1998tg,Kaplan:1998we,vanKolck:1998bw}.
{Generally, enhancements depend on the partial waves involved.}
The interactions contributing to such waves are operators in the ``$\cdots$'' of
Eq.~\eqref{eq:L-NN-simple} that make $T$ dependent on the scattering angle.
There is no enhancement for operators that contribute only to higher waves, as
long as there are no other low-energy poles as is the case in $N\!N$ scattering.
Thus, for example, a $P$-wave operator leading to a term $\propto
\veck'\cdot\veck$ appears first at N$^3$LO.  The enhancement is only partial for
operators that connect an $S$ wave to other waves.  The short-range tensor force
that connects $S$ and $D$ waves is present at N$^2$LO because it is enhanced by
one power of $\aleph^{-1}$~\cite{Chen:1999tn}.  The lowest orders in the
potential are shown schematically in Fig.~\ref{fig:pionlesspot}.


\begin{figure}[tb]
\begin{center}
\includegraphics[width=0.9\columnwidth]{pionlesspot-new}
\end{center}
\caption{Diagrams representing the $AN$ nuclear potential in Pionless EFT.  The
 order of the contributions is indicated as $\OO(Q^\mu/\Mhi^\mu)$, $\mu\geq0$,
 where $Q\sim\Mlo$ and $\Mhi\sim\mpi$, so that circles around the central
 solid circle denotes inverse powers of $\Mhi$.
}
\label{fig:pionlesspot}
\end{figure}


Summarizing, the $2N$ potential~\eqref{eq:V-pp} is a particularly simple form of
Eq.~\eqref{Vexp} where there are no non-analytic functions and

\begin{align}
 &\mu = d/2 \;\; (s_2=2)
 \mathtext{,}
 \mu = d+1-s_2 \;\; (s_2=0,1) \,,
 \label{pionlesspot}
 \\
 &\tilde{\mathcal{N}} = \OO\left((4\pi)^{A-1} \MN^{-1} \Mlo^{5-3A}\right)
 \,,
\label{pionlesspotnorm}
\end{align}

with $A=2$, $d$ the number of derivatives, and $s_2=0,1,2$ the number of $S$
waves connected by the
operator~\cite{Bedaque:1997qi,vanKolck:1997ut,Kaplan:1998tg,Kaplan:1998we,
Bedaque:1998mb,vanKolck:1998bw}.  Using the standard graph equalities to
eliminate the number of internal lines $I$ and loops $L$, $I=\sum_i V_i+L-1$ and
$I=-A+ \sum_i f_iV_i/2$, where $V_i$ is the number of vertices with $f_i$
nucleon lines, we obtain Eq.~\eqref{Texp} for the amplitude with

\begin{equation}
 \nu = \sum_i V_i \mu_i \mathtext{,}
 \mathcal{N} = \OO\left((4\pi)^{A-1} m_N^{-1} \Mlo^{5-3A}\right) \,.
\label{pionlessamp}
\end{equation}

Assuming $\Mlo\sim \gamma_d$, a rough estimate of the expansion parameter is
$\Mlo/\Mhi\sim \gamma_d/m_\pi \sim 1/3$.
