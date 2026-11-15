---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-043-1-form-factors
section_title: "Form Factors"
section_number: 1
pages: 32-33
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.985
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
The form factor of the $^{11}$Be ground state is computed by calculating the
contribution to the irreducible vertex for {$A_0 dd$} interactions
shown in Fig.~\ref{fig:formfactor-11Be}.  There is no diagram coupling the
photon to the neutron at this order since $Q_n=0$.  In the Breit frame, where
the four-momentum of the virtual photon is $q=(0,\mathbf{q})$, the
irreducible vertex for the $A_0$ photon coupling to the {$d$} field is
${-}\ii e Q_c G_E(|\mathbf{q}|)$ where $Q_c$ is the charge of the core.
A straightforward calculation yields

\begin{equation}
 G_E^{}(|\mathbf{q}|)= \frac{2 \gamma_0}{f|\mathbf{q}|}
 \arctan\!\left(\frac{f|\mathbf{q}|}{2 \gamma_0}\right)\,,
\label{eq:Gc}
\end{equation}

with $\gamma_0 =\sqrt{\mathstrut 2\mu_1 B_0}$ and $f=(1+m_0/m_1)^{-1}$, in the
notation of Eq.~\eqref{eq:lag_40}.  For the deuteron $m_0=m_N$ and $f=1/2$,
thus Eq.~\eqref{eq:Gc} reduces to the LO Pionless EFT result of
\textcite{Chen:1999tn}.


\begin{figure}[tb]
 \centerline{\includegraphics[width=3cm]{formfactor-new}}
 \caption{The LO contribution to the irreducible vertex for an $A_0$ photon
  coupling to the ${}^{10}$Be-neutron $S$-wave bound state.
  The thick solid line
  indicates the ${}^{11}$Be ground state, while the solid, dashed, and curly
  lines represent the neutron, ${}^{10}$Be core, and photon, respectively.
 }
\label{fig:formfactor-11Be}
\end{figure}


The form factor is a function of $\mathbf{q}^2$ only and the charge radius is
defined as $\langle r_E^2 \rangle^{} =-6 (\dd/\dd\mathbf{q}^2)
G_E|^{}_{\mathbf{q}^2=0}$.  Applying this expression to
Eq.~\eqref{eq:Gc} yields

\begin{equation}
 \langle r_E^2 \rangle^{}=\frac{f^2}{2 \gamma_0^2} \,,
\label{rcqs}
\end{equation}

which gives the charge radius of the $^{11}$Be ground state  relative to the
charge radius of $^{10}$Be.  Thus we have
$ \langle r_E^2 \rangle_{^{11}{\rm Be}}-\langle r_E^2 \rangle_{^{10}{\rm Be}}
= f^2/2 \gamma_0^2$.  This relation can be understood by writing the charge
distribution of $^{11}$Be as a convolution of the charge distribution of
$^{10}$Be with that of the $^{10}$Be-$n$ halo system.  Using the convolution
theorem for the Fourier transform, one finds that the total mean-square radius
is the sum of the squared radii for $^{10}$Be and the $^{10}$Be-$n$ halo system.

The latter effect can be calculated in Halo EFT.  We note that the finite size
of the core will also appear in Halo EFT at higher orders~\cite{Chen:1999tn}.
{An extended power-counting scheme that explicitly takes into account the
scaling of the mass ratio $f$ to move these contributions to lower orders was
given by \textcite{Ryberg:2019cvj}.}

Inserting $\gamma_0=0.15~\fm^{-1}$, the relative radius becomes
$\langle r_E^2\rangle_{^{11}{\rm Be}}-\langle
r_E^2\rangle_{^{10}{\rm Be}}=0.19~\fm^2$.  This is consistent with the
experimental result, $0.51(17)~\fm^2$~\cite{Nortershauser:2008vp}, within the
$40\%$ uncertainty from NLO effects in this system.  Using the experimental
result for the $^{10}$Be charge radius as further input, we find $\langle r_E^2
\rangle^{1/2}_{^{11}{\rm Be}}=2.40~\fm$ at LO.  This is 2--3\% smaller than the
atomic-physics measurement which yields $\langle r_E^2 \rangle^{1/2}_{^{11}{\rm
Be}}=2.463(16)~\fm $~\cite{Nortershauser:2008vp}.

At NLO a new operator associated with gauging the term {$\sim d^\dagger
\partial_0 d$} in the effective Lagrangian contributes.  The calculation
produces an increased charge radius, as long as the $S$-wave $n$-$^{10}$Be
effective range $r_0$ is positive (\cf~\cite{Beane:2000fi}),

\begin{equation}
 \langle r_E^2 \rangle_{^{11}{\rm Be}}-\langle r_E^2 \rangle_{^{10}{\rm Be}}
 =\frac{f^2}{2 (1- r_0 \gamma_0) \gamma_0^2}\,.
\end{equation}

{Using the value $r_0=2.7~\fm$ determined from Coulomb dissociation
of $^{11}$Be (see below), the relative radius becomes
$\langle r_E^2\rangle_{^{11}{\rm Be}}-\langle
r_E^2\rangle_{^{10}{\rm Be}}=0.31(5)~\fm^2$ at NLO, which improves the
agreement with the atomic-physics measurement. The change is
of order $40$\%, in agreement with the \apriori  expectation.
As a consequence,
the result for the full
charge radius of the ${}^{11}$Be ground state increases to
$\langle r_E^2 \rangle^{1/2}_{{}^{11}{\rm Be}}=2.42~\fm$.}
In contrast to observables involving the $1/2^-$ state, the radius
of the ${}^{11}$Be ground state does not receive any corrections from
short-distance physics until N$^3$LO{~\cite{Chen:1999tn}.}
The remaining difference between
NLO and experimental values is consistent with the presence of the
short-distance operator {$\sim L_{C0}^{}$} from
Eq.~\eqref{eq:nonminimalEM} at N$^3$LO in the expansion for the radius.

For the charge form factor of the $1/2^-$ excited state, NLO corrections might
be expected to be smaller since its typical momentum is lower.  However, a
counterterm enters already at NLO for this observable.  The form factor is given
by the contribution to the irreducible vertex for {$A_0 d^* d^*$}
interactions.
There are two diagrams at LO, the first of which is analogous to that for the
$1/2^+$ state shown in Fig.~\ref{fig:formfactor-11Be}, while the second diagram
represents a direct coupling of the photon from gauging the {$d^{*\dagger}
\partial_0 d^*$} term in the effective Lagrangian.  The latter contributes at
LO because the effective range $r_1$ corresponds to an LO operator for the
$1/2^-$ state.  The charge form factor of the $1/2^-$ state at LO is obtained
as~\cite{Hammer:2011ye}

\begin{equation}
 {G_E^{(*)}(|\mathbf{q}|)
 = 1 - \frac{\gamma_1}{r_1} +\frac{f^2
  \mathbf{q}^2
 + 2 \gamma_1^2}{|\mathbf{q}| f r_1}\,
 \arctan\!\left(\frac{f|\mathbf{q}|}{2 \gamma_1}\right)
 \,,}
\label{eq:Gc-p}
\end{equation}

where $\gamma_1 =\sqrt{2\mu_1 B_1}$ and $r_1$ is the $P$-wave effective range
for $n$-$^{10}$Be scattering.
Note that {$G_E^{(*)}(0)=1$}, as required by charge conservation,
while the charge radius of the $1/2^+$ state relative to the $^{10}$Be
ground state is

\begin{equation}
 {\langle r_E^2 \rangle^{(*)}  = {-}\frac{5 f^2}{2 \gamma_1 r_1} \,.}
\label{eq:LOpradresult}
\end{equation}

This scales as $1/(\Mlo\Mhi)$ as expected.
It seems counterintuitive that there is a short-distance contribution
to {$\langle r_E^2 \rangle^{(*)}$} already at NLO---especially when the
corresponding effect does not occur in $\langle r_E^2 \rangle^{}$
until N$^3$LO \cite{Chen:1999tn}.  The reason for this enhanced sensitivity is
that the probability distribution of $P$-wave states is drawn in to shorter
distances than the one of $S$-wave states, as it gets caught between the
attractive potential that produces the $P$-wave state and the centrifugal
barrier.  Observables associated with a shallow $P$-wave bound state will,
therefore, generically exhibit counterterms at lower order than those of their
$S$-wave counterparts.

Numerical evaluation of the LO expression~\eqref{eq:LOpradresult} leads to
the prediction $\langle r_E^2 \rangle_{^{11}{\rm Be}^*}-\langle r_E^2
\rangle_{^{10}{\rm Be}} = 0.36~\fm^{2}$, where we have used the value
$r_1=-0.66~\fm$ from the $B(E1)$ value as input (see below).  The NLO radius
includes contributions from the counterterm {$L_{C0}^{(*)}$}
in Eq.~\eqref{eq:nonminimalEM}, the coefficient of which is unknown.
\textcite{Hammer:2011ye} estimated the NLO contributions to be of order
20\%, assuming that the short-distance effects in $\langle r_E^2
\rangle^{1/2}_{^{11}{\rm Be}^*}$ scale with $f$. This {assumption}
is in agreement with the expectation from the power counting.  Using again the
experimental result for the $^{10}$Be charge radius~\cite{Nortershauser:2008vp},
the prediction for the charge radius of $^{11}$Be$^*$ at LO is $\langle r_E^2
\rangle^{1/2}_{^{11}{\rm Be}^*} = (2.43 \pm 0.1)~\fm$.  To date there is no
experimental determination of this charge radius.

Halo EFT calculations for the charge and magnetic form factors of $^{11}$Be and
$^{19}$C were performed to NLO by~\textcite{Fernando:2015jyd}.  They considered
$^{15}$C as well and suggested the inclusion of the effective range as an LO
effect in this particular case.
