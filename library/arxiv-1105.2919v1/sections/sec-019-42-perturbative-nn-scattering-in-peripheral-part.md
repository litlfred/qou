---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-019-42-perturbative-nn-scattering-in-peripheral-part
section_title: "Perturbative NN scattering in peripheral partial waves"
section_number: 4.2
pages: 26-31
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.848
latex_coverage_ratio: 0.986
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
\begin{table}[t]
\caption{Hadron masses and
low-energy constants (LECs).
$m_{\pi^\pm}$ and $m_{\pi^0}$ denote the charged- and neutral-pion masses,
and $M_p$ and $M_n$ are the proton and neutron masses, respectively, in units of MeV.
$g_A$ is the axial-vector coupling constant (dimensionless)
and $f_\pi$ the pion decay constant (in units of MeV).
The $c_i$ belong to the dimension-two $\pi N$ Lagrangian,
Eqs.~(\ref{eq_L2ct}) and (\ref{eq_LD1}), and are in units of GeV$^{-1}$,
whereas the $\bar{d}_i$ are associated with the dimension-three
Lagrangian, Eqs.~(\ref{eq_L3rel}) and (\ref{eq_LD2}), and
are in units of GeV$^{-2}$.
Column ``$NN$ Potential'' lists the values
used for a $NN$ potential
at N$^3$LO presented in Section~\ref{sec_potn3lo}, while
column ``Peripheral perturbative $NN$'' shows the parameters applied in the 
peripheral $NN$ scattering calculations of Section~\ref{sec_peri}.
Finally, the last column displays values from empirical
determinations (see text for comments).
\label{tab_LEC}}
\smallskip
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}cccc}
\hline
\hline
\noalign{\smallskip}
  &                           & Peripheral           &                \\
  & $NN$ Potential & perturbative $NN$    & Empirical \\
     & (Sec.~\ref{sec_potn3lo}) & (Sec.~\ref{sec_peri}) & \\
\hline
\noalign{\smallskip}
$m_{\pi^\pm}$ & 139.5702 & 139.5702 & 139.57018(35)~\cite{PDG} \\
$m_{\pi^0}$ & 134.9766 & 134.9766 & 134.9766(6)~\cite{PDG} \\
$M_p$    & 938.2720 & 938.2720   & 938.272013(23)~\cite{PDG} \\
$M_n$    & 939.5653 & 939.5653   & 939.565346(23)~\cite{PDG} \\
$g_A$ & $1.29^a$ & $1.29^a$ & $1.2759(45)$~\cite{Liu10} \\
$f_\pi$ & 92.4 & 92.4 & $92.2\pm 0.2$~\cite{PDG} \\
$c_1$ & --0.81 & --0.81 & $-0.81\pm 0.15^b$ \\
$c_2$ & 2.80 & 3.28 & $3.28\pm 0.23^c$ \\
$c_3$ & --3.20 & --3.40 & $-4.69\pm 1.34^b$ \\
$c_4$ & 5.40 & 3.40 & $3.40\pm 0.04^b$ \\
$\bar{d}_1 + \bar{d}_2$ & 3.06 & 3.06 & $3.06\pm 0.21^c$ \\
$\bar{d}_3$ & --3.27 & --3.27 & $-3.27\pm 0.73^c$ \\
$\bar{d}_5$ & 0.45 & 0.45 & $0.45\pm 0.42^c$ \\
$\bar{d}_{14} - \bar{d}_{15}$ & --5.65 & --5.65 & $-5.65\pm 0.41^c$ \\
\hline
\hline
\noalign{\smallskip}
\end{tabular*}
$^a$Confer discussion of Goldberger-Treiman discrepancy in
Section~\ref{sec_1pe}.\\
$^b$Table~1, Fit~1 of Ref.~\cite{BM00}.\\
$^c$Table~2, Fit~1 of Ref.~\cite{FMS98}.
\end{table}


Nucleon-nucleon scattering in peripheral partial waves
is of special interest---for several reasons.
First, these partial waves probe the long- and 
intermediate-range of the nuclear force. Due to the centrifugal
barrier, there is only small sensitivity to short-range
contributions and, in fact, the N$^3$LO contact terms
make no contributions for orbital angular momenta
$L\geq 3$ (cf.\ Section~\ref{sec_ct}).
Thus, for $F$ and higher waves and energies below the pion-production
threshold, we have a window in which the $NN$ interaction
is governed by chiral symmetry alone (chiral one-
and two-pion exchanges), and we can 
conduct a relatively clean test of how well 
the theory works.
Using values for the LECs from $\pi N$ analysis,
the $NN$ predictions are even parameter free.
Moreover, the smallness of the phase shifts in peripheral
partial waves suggests that the calculation can
be done perturbatively. This avoids the complications
and the possible model-dependence
that the non-perturbative treatment of the
Schroedinger equation, necessary for low partial
waves (Section~\ref{sec_reno}), is beset with.
Because of the importance of peripheral $NN$ scattering,
many calculations
based upon chiral dynamics can be found in the
literature~\cite{RR94,KBW97,KGW98,EM02,Ric99,BM04,Hig04}.
We will follow Ref.~\cite{EM02}.

Since we will compare the predictions with neutron-proton ($np$) phase shifts,
we will specifically calculate $np$ scattering in this sub-section.
Defining,
\begin{equation}
V_{1\pi} (m_\pi) \equiv -\, 

\frac{g_A^2}{4f_\pi^2}\, \frac{
\vec \sigma_1 \cdot \vec q \,\, \vec \sigma_2 \cdot \vec q}
{q^2 + m_\pi^2} 
\,,
\label{eq_1pe_bare}
\end{equation}
the correct 1PE for $np$ scattering is given by
\begin{equation}
V_{1\pi}^{(np)} ({\vec p}~', \vec p) 
= -V_{1\pi}(m_{\pi^0}) + (-1)^{I+1}\, 2\, V_{1\pi} (m_{\pi^\pm})
\,,
\label{eq_1penp}
\end{equation}
where $I$ denotes the isospin of the two-nucleon system.
We use the pion masses given in Table~\ref{tab_LEC} and
\begin{equation}
M_N  =  \frac{2M_pM_n}{M_p+M_n} = 938.9182 \mbox{ MeV}
\,.
\end{equation}
Also in the iterative 2PE, we apply the correct $np$
1PE, i.e., in Eq.~(\ref{eq_2piitKBW}) we replace $V_{1\pi}$
with $V_{1\pi}^{(np)}$.
Thus, the perturbative relativistic $T$-matrix for $np$ scattering,
taking the exchange of up to two pions into account,
is calculated in the following way,
\begin{eqnarray}
T({\vec p}~',\vec p) &=& 
 V_{1\pi}^{(np)} ({\vec p}~', \vec p) +
 V_{2\pi}^{(np)} ({\vec p}~', \vec p) 
\nonumber \\
      &=&
 V_{1\pi}^{(np)} ({\vec p}~', \vec p) +
 V_{2\pi, \rm it}^{({\rm KBW},np)} 
({\vec p}~',{\vec p}) +
 V_{2\pi}'({\vec p}~',{\vec p}) 
\,.
\label{eq_tall}
\end{eqnarray}
As discussed, the expression for $V_{1\pi}^{(np)}$ is good to any order
we will consider in this article (cf.\ 
Section~\ref{sec_1pe}) and 
$V_{2\pi, \rm it}^{({\rm KBW},np)}$ 
includes all orders.
There is no need to break the latter term
up into orders, because
the admixture of (very small) higher order contributions from 
$V_{2\pi, \rm it}^{({\rm KBW},np)}$ 
will not affect the accuracy we are working at.
The most important term in the above equation is
$V_{2\pi}'$, 
{\it the irreducible 2PE contributions}, 
for which we have the low-momentum expansion,
\begin{equation}
V_{2\pi}' = 
V_{2\pi}^{'(2)} +
V_{2\pi}^{'(3)} +
V_{2\pi}^{'(4)} 
+ \ldots 
\,,
\end{equation}
with the various 
$V_{2\pi}^{'(\nu)}$ 
given in Section~\ref{sec_2pi}.
In the calculation of 
$V_{2\pi}'$, 
we use the average pion mass $m_\pi = 138.039$ MeV and, thus,
neglect the charge-dependence due to pion-mass splitting
in irreducible diagrams.
The charge-dependence that emerges from irreducible $2\pi$ 
exchange was investigated in Ref.~\cite{LM98b} and found to be
negligible for partial waves with $L\geq 3$.



\begin{figure}[t]\centering
\vspace*{-2.8cm}

\scalebox{0.55}{\includegraphics{ph_f.pdf}}
\vspace*{-3.0cm}
\caption{$F$-wave phase shifts of neutron-proton scattering
for laboratory kinetic energies below 300 MeV.
We show the predictions from chiral pion exchange
to leading order (LO), next-to-leading order (NLO),
next-to-next-to-leading order (NNLO), and
next-to-next-to-next-to-leading order (N3LO).
Note that in $^3F_4$, the NNLO and N3LO curves
cannot be distinguished on the scale of the figure.
The solid dots and open circles are the results from the Nijmegen
multi-energy $np$ phase shift analysis~\protect\cite{Sto93} 
and the VPI/GWU
single-energy $np$ analysis SM99~\protect\cite{SM99}, respectively.}
\label{fig_f}
\end{figure}



For the $T$-matrix given in Eq.~(\ref{eq_tall}),
we calculate phase shifts for
partial waves with $L\geq 3$ and 
$T_{lab}\leq 300$ MeV (see Ref.~\cite{EM02} for the details of
this calculation).
The LECs used in this calculation are shown in Table~\ref{tab_LEC},
column ``Peripheral perturbative $NN$''.
Note that many determinations of the LECs, $c_i$ and $\bar{d}_i$,
can be found in the literature.
The most reliable way to determine the LECs from empirical
$\pi N$ information is to extract them from the $\pi N$ amplitude
inside the Mandelstam triangle (unphysical region) which can
be constructed with the help of dispersion relations from empirical
$\pi N$ data. This method was used by B\"uttiker and Mei\ss ner~\cite{BM00}.
Unfortunately, the values for $c_2$ and all $\bar{d}_i$ parameters
obtained in Ref.~\cite{BM00} carry uncertainties,
so large that the values cannot provide any guidance.
Therefore, in Table~\ref{tab_LEC}, only  $c_1$, $c_3$, and $c_4$
are from Ref.~\cite{BM00}, while the other LECs
are taken from Ref.~\cite{FMS98} where the $\pi N$ amplitude in the
physical region was considered.
To establish a link between $\pi N$ and $NN$, we apply 
the values from the above determinations in our calculations
of the $NN$ peripheral phase shifts.
In general, we use the central values;
the only exception is $c_3$, where we choose
a value that is, in terms of magnitude, about one standard
deviation below the one from Ref.~\cite{BM00}.
With the exception of $c_3$,
phase shift predictions do not depend sensitively on
variations of the LECs within the quoted uncertainties.


\begin{figure}[t]\centering
\vspace*{-2.8cm}

\scalebox{0.55}{\includegraphics{ph_g.pdf}}
\vspace*{-3.0cm}
\caption{Same as Fig.~\ref{fig_f}, but for $G$ waves.}
\label{fig_g}
\end{figure}


In Figs.~\ref{fig_f} and \ref{fig_g},
we show the phase-shift
predictions for neutron-proton scattering in $F$ and $G$
waves, respectively, for laboratory kinetic energies below 300 MeV.
The orders displayed are defined as follows:
\begin{itemize}
\item
Leading order (LO) is just 1PE, 
first term on the r.h.s.\
of Eq.~(\ref{eq_tall}).
\item
Next-to-leading order (NLO) 
includes the first two terms on the r.h.s.\
of Eq.~(\ref{eq_tall}) (1PE \& iterative 2PE)
plus 
$V_{2\pi}^{'(2)}$
[Section~\ref{sec_NLO}, Eqs.~(\ref{eq_2C}) and (\ref{eq_2T})].
\item
Next-to-next-to-leading order (NNLO)
consists of NLO plus  
$V_{2\pi}^{'(3)}$
[Section~\ref{sec_NNLO},
Eqs.~(\ref{eq_3C})-(\ref{eq_3LS})].
\item
Next-to-next-to-next-to-leading order 
(denoted by N3LO in the figures)
is made up of NNLO plus 
$V_{2\pi}^{'(4)}$
[\ref{app_N3LO},
Eqs.~(\ref{eq_4c2C})-(\ref{eq_4M2sL}) 
and (\ref{eq_42lC})-(\ref{eq_42lT})]. 
\end{itemize}
It is clearly seen in 
Figs.~\ref{fig_f} and \ref{fig_g}
that the leading $2\pi$ exchange (NLO)
is, in general, rather small, insufficient to explain
the empirical facts in most partial waves. 
In contrast, the next order (NNLO)
is very large; in some cases, several times NLO. This is due to the
$\pi\pi N N$ contact interactions proportional
to the LECs $c_i$ that are introduced in the
sub-leading Lagrangian 
${\cal L}^{\Delta=1}$, Eq.~(\ref{eq_LD1}). 
These contacts are supposed to simulate the contributions
from intermediate $\Delta$-isobars and correlated $2\pi$
exchange which are known
to be large 
and crucial for a realistic model for the $NN$ interaction
at intermediate ranges
(see, e.~g., Ref.~\cite{MHE87}). 


\begin{figure}[t]\centering
\vspace*{-2.8cm}

\scalebox{0.55}{\includegraphics{ph_ff.pdf}}
\vspace*{-3.0cm}
\caption{$F$-wave phase shifts of neutron-proton scattering
for laboratory kinetic energies below 300 MeV.
We show the results from one-pion-exchange (1PE),
and one- plus two-pion exchange as predicted by ChPT at
next-to-next-to-next-to-leading order (N3LO) and 
by the Bonn Full Model~\protect\cite{MHE87} (Bonn).
Note that the ``Bonn'' curve does not include the repulsive
$\omega$ and $\pi\rho$ exchanges of the full model, since 
this figure serves the purpose to compare just predictions
by different models/theories for the $\pi+2\pi$ contribution 
to the $NN$ interaction.
Empirical phase shifts (solid dots and open circles)
as in Fig.~\protect\ref{fig_f}.}
\label{fig_ff}
\end{figure}



\begin{figure}[t]\centering
\vspace*{-2.8cm}

\scalebox{0.55}{\includegraphics{ph_gg.pdf}}
\vspace*{-3.0cm}
\caption{Same as Fig.~\ref{fig_ff}, but for $G$ waves.}
\label{fig_gg}
\end{figure}



At N$^3$LO a clearly identifiable
trend towards convergence emerges.
In $G$ waves (except for $^3G_5$, see \ref{app_N3LO_ph}
for a discussion of this issue),
N$^3$LO differs very little from NNLO
implying that we have reached convergence.
Also $^1F_3$ and $^3F_4$ appear fully converged.
However, in $^3F_2$ and $^3F_3$, N$^3$LO differs
noticeably from NNLO, but the difference is much smaller than the
one between NNLO and NLO. This is what we perceive as a trend towards
convergence.
Individual N$^3$LO contributions to peripheral phase shifts
are shown in \ref{app_N3LO_ph}.

In Figs.~\ref{fig_ff} and \ref{fig_gg}, 
we conduct a comparison between the predictions from chiral one- and
two-pion exchange at N$^3$LO and the corresponding 
predictions from conventional
meson theory (curve `Bonn'). 
As representative for conventional meson theory, we choose the Bonn
meson-exchange model for the $NN$ interaction~\cite{MHE87},
since it contains a comprehensive and thoughtfully constructed
model for $2\pi$ exchange.
This $2\pi$ model includes box and crossed box diagrams with
$NN$, $N\Delta$, and $\Delta\Delta$ intermediate states
as well as direct $\pi\pi$ interaction in $S$- and $P$-waves
(of the $\pi\pi$ system)
consistent with empirical information from $\pi N$ and $\pi\pi$
scattering.
Besides this the Bonn model also includes (repulsive) $\omega$-meson
exchange and irreducible diagrams of $\pi$ and $\rho$ exchange
(which are also repulsive).
However, note that
in the phase shift predictions displayed in 
Figs.~\ref{fig_ff} and \ref{fig_gg}, 
the ``Bonn'' curve includes only the $1\pi$ and $2\pi$ contributions
from the Bonn model; the short-range contributions are
left out since the purpose of the figure is to compare
different models/theories for $\pi+2\pi$.
In all waves shown (with the usual exception of $^3G_5$)
we see, in general, good agreement between N$^3$LO and Bonn.
In $^3F_2$ and $^3F_3$ above 150 MeV and in
$^3F_4$ above 250 MeV the chiral model to N$^3$LO is more
attractive than the Bonn $2\pi$ model. Note, however,
that the Bonn model is relativistic and, thus, includes
relativistic corrections up to infinite orders.
Thus, one may speculate that higher orders in 
ChPT may create some
repulsion, moving the Bonn and the chiral predictions even closer
together~\cite{foot2}.


The $2\pi$ exchange contribution to the $NN$ interaction
can also be derived
from {\it empirical} $\pi N$ and $\pi\pi$ input
using dispersion theory, which is based upon unitarity,
causality (analyticity), and crossing symmetry.
The amplitude $N\bar{N}\rightarrow \pi\pi$ is
constructed from $\pi N \rightarrow \pi N$
and $\pi N \rightarrow \pi\pi N$ data using 
crossing properties and analytic
continuation; this amplitude is then `squared' to yield 
the $N\bar{N}$ amplitude 
which is related to $NN$ by crossing symmetry~\cite{BJ76}.
The Paris group~\cite{Vin79,Lac80} pursued this path and 
calculated $NN$ phase shifts in peripheral partial waves.
Naively, the dispersion-theoretic approach is
the ideal one, since it is based exclusively on empirical
information. Unfortunately, in practice,
quite a few uncertainties enter.
First, there are ambiguities
in the analytic continuation and, second, 
the dispersion integrals have to be cut off at a certain
momentum to ensure reasonable results.
In Ref.~\cite{MHE87}, a thorough comparison was conducted
between the predictions by the Bonn model and the
Paris approach and it was demonstrated that the Bonn
predictions always lie comfortably within the range of uncertainty
of the dispersion-theoretic results.
Therefore, there is no need to perform a
separate comparison of our chiral N$^3$LO predictions with
dispersion theory, since it would not add anything that we
cannot conclude from Figs.~\ref{fig_ff} and \ref{fig_gg}.

Finally, we need to compare the
predictions with the empirical phase shifts.
In $F$ waves the N$^3$LO predictions above 200 MeV are,
in general, too attractive. Note, however, that this is
also true for the predictions by the Bonn $\pi + 2\pi$
model. In the {\it full} Bonn model, 
besides $\pi+2\pi$, 
(repulsive)
$\omega$ and $\pi\rho$ exchanges are included
which move
the predictions right on top of the data.
The exchange of a $\omega$ meson or  combined $\pi\rho$
exchange are $3\pi$ exchanges.
Three-pion exchange occurs first at chiral order four.
It has been investigated by Kaiser~\cite{Kai00a,Kai00b} and found to be
negligible, at this order.
However, $3\pi$ exchange at order five appears 
to be sizable~\cite{Kai01}
and may have impact on $F$ waves.
Besides this, there is the usual short-range phenomenology.
In ChPT, this short-range interaction
is parametrized in terms of four-nucleon contact terms
(since heavy mesons do not have a place in that theory).
Contact terms of order four (N$^3$LO) do not contribute to
$F$-waves, but order six does.
In summary, the remaining small 
discrepancies between the N$^3$LO predictions and the empirical
phase shifts may be straightened out in
fifth or sixth order of ChPT.




\subsection{$NN$ contact terms \label{sec_ct}}

The successful test of the chiral pion-exchange contributions
in peripheral partial waves in the previous section
has shown that we got the long- and intermediate-range
parts of the nuclear force right.
However, for a ``complete'' nuclear force, we have to 
describe correctly all partial waves, including the lower ones.
In fact, in calculations of $NN$ observables at low energies (cross
sections, analyzing powers, etc.),
the lower partial
waves with $L\leq 2$ are the most important ones, generating
the largest contributions.
The same is true for microscopic nuclear structure
calculations.
These lower partial waves are dominated by the
dynamics at short distances.
Therefore, we need to look now into the short-range part
of the $NN$ potential.

In conventional meson theory, the short-range nuclear force
is described by the exchange of heavy mesons, notably the
$\omega(782)$. 
Qualitatively, the short-distance behavior of the $NN$ 
potential is obtained
by Fourier transform of the propagator of
a heavy meson,
\begin{equation}
\int d^3q \frac{e^{i{\vec q} \cdot {\vec r}}}{m^2_\omega
+ {\vec q}^2} \;
\sim \;
 \frac{e^{-m_\omega r}}{r} \; .
\end{equation}

ChPT is an expansion in small momenta $Q$, too small
to resolve structures like a $\rho(770)$ or $\omega(782)$
meson, because $Q \ll \Lambda_\chi \approx m_{\rho,\omega}$.
But the latter relation allows us to expand the propagator 
of a heavy meson into a power series,
\begin{equation}
\frac{1}{m^2_\omega + Q^2} 
\approx 
\frac{1}{m^2_\omega} 
\left( 1 
- \frac{Q^2}{m^2_\omega}
+ \frac{Q^4}{m^4_\omega}
-+ \ldots
\right)
,
\end{equation}
where the $\omega$ is representative
for any heavy meson of interest.
The above expansion suggests that it should be 
possible to describe the short distance part of
the nuclear force simply in terms of powers of
$Q/m_\omega$, which fits in well
with our over-all 
power expansion since $Q/m_\omega \approx Q/\Lambda_\chi$.

A second purpose of contact terms is renormalization.
Dimensional regularization
of the loop integrals that occur in multi-pion exchange diagrams
typically generates polynomial terms
with coefficients that are, in part, infinite or scale
dependent (cf.\ \ref{app_NLO}). Contact terms pick up infinities
and remove scale dependences, which is why they are also known as counter terms.


The partial-wave decomposition of a power
$Q^\nu$ has an interesting property.
First note that $Q$ can only be either
the momentum transfer between the two interacting
nucleons $q$ or the average momentum $k$
[cf.\ Eq.~(\ref{eq_defqk}) for their definitions].
In any case, for even $\nu$,
\begin{equation}
Q^\nu = 
f_{\frac{\nu}{2}}(\cos \theta) 
\, ,
\end{equation}
where $f_m$ stands for a polynomial of degree $m$
and $\theta$ is the CMS scattering angle.
The partial-wave decomposition of $Q^\nu$ for a state
of orbital-angular momentum $L$
involves the integral
\begin{equation}
I^{(\nu)}_L  
=\int_{-1}^{+1} Q^\nu P_L(\cos \theta) d\cos \theta 
=\int_{-1}^{+1}
f_{\frac{\nu}{2}}(\cos \theta) 
 P_L(\cos \theta) d\cos \theta 
\,,
\end{equation}
where $P_L$ is a Legendre polynomial.
Due to the orthogonality of the $P_L$, 
\begin{equation}
I^{(\nu)}_L = 0  
\hspace*{.5cm}
\mbox{for}
\hspace*{.5cm}
L > \frac{\nu}{2} \, .
\end{equation}
Consequently, contact terms of order zero contribute only
in $S$-waves, while order-two terms contribute up to 
$P$-waves, order-four terms up to $D$-waves,
etc..

Due to parity, only even powers of $Q$
are allowed.
Thus, the expansion of the contact potential is
formally given by
\begin{equation}
V_{\rm ct} =
V_{\rm ct}^{(0)} + 
V_{\rm ct}^{(2)} + 
V_{\rm ct}^{(4)} 
+ \ldots \; ,
\end{equation}
where the superscript denotes the power or order.

We will now present, one by one, the various orders of 
$NN$ contact terms which result from the contact
Lagrangians presented in Section~\ref{sec_Lct}.
