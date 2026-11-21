---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-044-2-e1-transition-and-photodisintegration
section_title: "E1 transition and photodisintegration"
section_number: 2
pages: 33-35
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.992
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
Next we discuss the E1 transition from the $1/2^+$ state to the $1/2^-$ state.
The irreducible vertex for this transition is depicted in
Fig.~\ref{fig:Gammajmu}.  We compute the transition for a photon of arbitrary
four momentum $k=(\omega,{\bf k})$, and the sum of diagrams yields
${-}\ii\Gamma_{j\mu}$, where $j$ is the angular momentum index of the {$d^*$}
field and $\mu$ is the polarization index of the photon.
The diagrams depicted in Fig.~\ref{fig:Gammajmu} are divergent, but their
divergences cancel---providing a nontrivial check on the calculation.  As long
as both diagrams are considered current conservation is also
satisfied~\cite{Hammer:2011ye}, $k^\mu \Gamma_{j \mu} = 0$.  Note that if only
the long-distance E1 mechanism on the left-hand side of Fig.~\ref{fig:Gammajmu}
is considered---as was done, for example, by \textcite{Typel:2008bw}---then
current conservation is not satisfied and it appears that some input from
short-distance physics is needed in order to define the prediction for this
observable.


\begin{figure}[tb]
 \centerline{\includegraphics[width=6cm]{sptransition-new}}
 \caption{The two diagrams contributing to the irreducible vertex for the
   $S$-to-$P$-state transition, $\Gamma_{j \mu}$, at LO.
   The double line indicates the ${}^{11}$Be excited state; the other
   lines are as in Fig.~\ref{fig:formfactor-11Be}.
 }
\label{fig:Gammajmu}
\end{figure}


Evaluating the diagrams in
Fig.~\ref{fig:Gammajmu}, we obtain the LO Halo EFT result for ${\rm B(E1)}$,

\begin{equation}
 {\rm B(E1)} =
 -\frac{Z_\text{eff}^2 e^2}{3 \pi} \frac{\gamma_0}{r_1}
 \left[\frac{2 \gamma_1 + \gamma_0}{(\gamma_0 + \gamma_1)^2}\right]^2 \,,
\label{eq:BE1}
\end{equation}

with $Z_\text{eff} = f Q_c \approx 0.366$ the effective charge.
No regularization is needed in order to get a finite result.  We note that the
result~\eqref{eq:BE1} is ``universal'' in the sense that it applies to any E1
$S$-to-$P$-wave transition in a one-neutron halo nucleus.  Once $r_1$,
$\gamma_1$, and $\gamma_0$ are known for a given one-neutron halo,
the prediction (\ref{eq:BE1}) is accurate up to corrections of

{${\mathcal O}(\Mlo/\Mhi)$}.

Since there is no experimental value for the $P$-wave effective range $r_1$,
\textcite{Hammer:2011ye} extracted it from the experimental number ${\rm
B(E1)}(1/2^+ \rightarrow 1/2^-) = 0.105(12)~e^2$ \fm$^2$ from
\textcite{Summers:2007du}, yielding $r_1^{\rm LO} = {-}0.66~\fm^{-1}$.
Short-distance effects enter B(E1) through a counterterm
in the NLO corrections.  The B(E1) ($1/2^+ \rightarrow 1/2^-$) transition
therefore cannot be predicted at NLO, which can be seen from the presence of the
operator with LEC $L^{(1/2)}_{E1}$ in Eq.~\eqref{eq:nonminimalEM}.

Comparing this calculation with a shell-model treatment of ${}^{11}$Be, it is
clear that one effect which is subsumed into the NLO counterterm
$L^{(1/2)}_{E1}$ is the transition of a neutron from a $d_{5/2}$ to a $p_{3/2}$
orbital, with that neutron coupled to the $2^+$ state of ${}^{10}$Be.  This
$2^+$ state is $3.4~\MeV$ above the ${}^{10}$Be ground state, so the dynamics
associated with it takes place at distances $\sim \Mhi^{-1}$.  Hence in Halo EFT
it can only appear in short-distance operators such as that multiplying
$L^{(1/2)}_{E1}$.  The computation of
\textcite{Millener:1983zz} suggests that such a contribution reduces the E1
matrix element by $\sim 30$\%, which is the anticipated size of an NLO effect
when the $\Mlo/\Mhi$ expansion is employed in the ${}^{11}$Be system.
There are other effects of a similar size that will affect B(E1) at NLO.
Specifically, there are NLO corrections from the wavefunction renormalization
factors associated with the $S$- and $P$-wave fields.  Both tend to increase
B(E1) over the LO prediction.

We move on to the photodisintegration of ${}^{11}$Be into ${}^{10}$Be
plus a neutron.  In practice this process is measured using Coulomb
excitation of the ${}^{11}$Be nucleus, with the two reactions connected within
the equivalent-photon approximation.
There are three contributions to this process, as depicted in
Fig.~\ref{fig:photodis-11Be}.  The first diagram, denoted ``LO'' in the figure,
corresponds to the contribution from the plane-wave impulse approximation.  The
second and third diagrams, denoted ``NLO'', include the final-state interactions
between the neutron and the core in the $J=1/2$ channel.  As we will show below,
the first diagram is dominant over diagrams involving $P$-wave final-state
interactions.  From these diagrams, we obtain the differential B(E1) strength
distribution at NLO~\cite{Hammer:2011ye},

\begin{multline}
 {\frac{\dd{\rm B(E1)}}{\dd E}
 = \frac{e^2 Z_\text{eff}^2}{4\pi}
 \frac{12\mu_1 \gamma_0 {|\mathbf p'}|^3}{\pi^2({\mathbf p'}^2
 + \gamma_0^2)^4}} \\
 {\null \times \left(1+r_0 \gamma_0 + \frac{2 \gamma_0}{3 r_1}
 \frac{3 {\mathbf p'}^2+ \gamma_0^2}{{\mathbf p'}^2 + \gamma_1^2}\right) \,.}
\label{eq:dBdE1NLO}
\end{multline}

where ${\mathbf p'}$ is is the relative momentum of the outgoing $^{10}$Be-$n$
pair and $E={\mathbf p'}^2/(2\mu_1)$ is the kinetic energy of the $^{10}$Be-$n$
pair in the center-of-mass frame.


\begin{figure}[tb]
 \centerline{\includegraphics[width=18em]{stocont-new}}
 \caption{
  Diagrams contributing to photodissociation of the ${}^{11}$Be
  ground ($S$-wave) state. The notation is as in Fig~\ref{fig:Gammajmu}.}
\label{fig:photodis-11Be}
\end{figure}


The LO result corresponds to taking only the 1 in the {parenthesis}
of Eq.~\eqref{eq:dBdE1NLO}.  The NLO correction comes from two sources.  The
first is the shift of of the wavefunction renormalization to larger values due
to $r_0 > 0$, which tends to increase the B(E1) strength.  Second, final-state
interactions between the neutron and the core in the $J=1/2$ channel enter at
this order.  Accurate measurements of the Coulomb dissociation spectrum
therefore provide information on the $S$-wave $n$-${}^{10}$Be effective range,
if the $P$-wave effective range is already fixed from another observable.

Up to LO accuracy for bound-to-bound state transition and NLO for
bound-to-continuum, there are four LECs: $\gamma_0$ and $\gamma_1$ (which are
known from separation energies) and the $S$- and $P$-wave effective ranges $r_0$
and $r_1$.  At the next order, the counterterm $L_{E1}^{(1/2)}$ from
Eq.~\eqref{eq:nonminimalEM} enters as well.

Folding the Halo EFT result~\eqref{eq:dBdE1NLO} with the neutron detector
resolution and the spectrum of E1 photons, the experimental data of
\textcite{Palit:2003av} are well described, as shown in Fig.~\ref{fig:results}.
At NLO, if we take the value of $r_1$ fixed above, we have one free parameter,
the value of the $S$-wave effective range $r_0$.  A reasonable fit is found for
$r_0=2.7~\fm$, very close to the effective-range result of
\textcite{Typel:2004us} with all integrals cut off at $R=2.78~\fm$.
This choice of the cutoff corresponds to specific assumptions about the
counterterms.  Another experiment by~\textcite{Fukuda:2004ct} can be described
equally well but suggests a 3-4\% larger value for $r_0$.


\begin{figure}[tb]
 \centerline{\includegraphics*[width=7cm,clip=true]{dBdEv1rmp.pdf}}
 \caption{Differential B(E1) strength for Coulomb dissociation of $^{11}$Be
  into $^{10}$Be + $n$ as a function of excess energy of the
  neutron, $E^*$.  The dashed (solid) lines show the Halo EFT result of
  \textcite{Hammer:2011ye} at LO (NLO) folded with the detector resolution.
  The experimental data are from \textcite{Palit:2003av}, while the
  dotted line {(almost on top of the solid line)} gives the effective range
  model of \textcite{Typel:2004us}.
  Reprinted from \cite{Hammer:2011ye}, with permission from Elsevier.
 }
\label{fig:results}
\end{figure}


The Coulomb dissociation of the one-neutron halo nucleus $^{19}$C was studied
by \textcite{Acharya:2013nia} using the $^{18}$C core and the neutron as
effective degrees of freedom.  In this case, there is no excited state present.
The authors demonstrated the power of Halo EFT by calculating various
observables and extracted the ERE parameters and the separation energy of the
halo neutron from the Coulomb dissociation data of \textcite{Nakamura:1999rp}.
In particular, they obtained the values $(575 \pm 55 \pm 20)~\keV$ for the
one-neutron separation energy of $^{19}$C, and $(7.75 \pm 0.35 \pm 0.3)~\fm$ for
the $^{18}$C-neutron scattering length, where the first error is statistical and
the second error is an estimate of the EFT uncertainty.  Their prediction for
the longitudinal-momentum distribution is in good agreement with the data of
\textcite{Bazin:1995zz} and confirms the $S$-wave dominance for $^{19}$C.

The charge form factor and the Coulomb breakup of two-neutron halo nuclei
were first calculated by \textcite{Hagen:2013xga}, \textcite{Hagen:2014tt}, and
\textcite{Acharya:2015tt} {at} LO.  The calculation of the charge form
factor was recently extended to NLO by \textcite{Vanasse:2016hgn}. (Vanasse also
corrected an error in the  prefactor of one term in the form factor calculation
of \textcite{Hagen:2013xga}.)  Since the value of the neutron-core
effective range is unknown and can only be estimated, we only quote
in Table~\ref{tab:electricradii} the LO charge radii for
${}^{11}$Li, ${}^{12}$Be, and ${}^{22}$C from~\cite{Vanasse:2016hgn},
together with the input value for the two-neutron separation energy.
The charge radius for ${}^{11}$Li has been measured by
\textcite{Puchalski:2006zz} and \textcite{Sanchez:2006zz}.
The result $\langle r_E^2 \rangle=1.104(85)$ fm$^2$ is consistent with the LO
result within the estimated $40$\% uncertainty due to range effects.
The charge radii of $^{14}$Be and $^{22}$C have not yet been measured.


\begin{table}
   \centering
   \begin{tabular}{|c| c c|} \hline
     Nucleus & $S_{2n}$ [MeV] & $\langle r^2_{E}\rangle$ [fm$^2$] \\
     \hline\hline
     $^{11}$Li & 0.3693(6) & 0.744 \\
     $^{14}$Be & 1.27(13)  & 0.126 \\
     $^{22}$C  & 0.11(6)   & 0.519 $^{+\infty}_{{-}0.274}$ \\
     \hline
 \end{tabular}
 \caption{Two-neutron separation energies and LO charge radii squared
  for four different two-neutron halos.  Adapted from \cite{Vanasse:2016hgn}.
 }
\label{tab:electricradii}
\end{table}


Halo EFT has also been used to calculate the matter radii of the two-neutron
halos {listed} in Table~\ref{tab:electricradii} up to NLO using (i) dimeron
propagators with resummed range effects~\cite{Canham:2008jd,Canham:2009xg} and
(ii) with a fully perturbative treatment of range
corrections~\cite{Vanasse:2016hgn}.  Both methods lead to consistent results.
