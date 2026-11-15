---
doc_id: arxiv-0811.1338v1
doc_title: "Modern theory of nuclear forces"
section_id: sec-006-i-qcd-and-nuclear-forces
section_title: "QCD AND NUCLEAR FORCES"
section_number: I
pages: 1-3
source_pdf: 0811.1338v1.pdf
source_sha256: 9a57cb6e014d3ead
doc_brief: "Modern theory of nuclear forces — 36 sections: QCD and Nuclear F orces 1; Conventional approaches to the nuc; EFT for F ew-Nucleon Systems: F ou"
text_source: latex
latex_prose_ratio: 0.769
latex_coverage_ratio: 0.988
---
\def\theequation{\arabic{section}.\arabic{equation}}
\setcounter{equation}{0}
\setcounter{page}{1}
\label{sec:intro}

Within the Standard Model of particle physics, the strong interactions
are described by Quantum Chromodynmics (QCD).
QCD is a fascinating theory with many intriguing
manifestations. Its structure and interactions are governed by a local
non-abelian gauge symmetry, namely  SU(3)$_{\rm color}$.
Its fundamental degrees of freedom, the quarks (the matter fields) and 
gluons (the force carriers), have never been observed in isolation 
(confinement). The strong coupling
constant $\alpha_S$ exhibits a very pronounced running and is of order one
in the typical energy scales of nuclear physics. The bound states made
from the basic constituents are the hadrons, the strongly interacting
particles. The particle spectrum shows certain regularities that can be
traced back to the flavor symmetries related to the fermions building 
up these states. More precisely, there are six quark flavors. These can 
be grouped into two very different sectors.
While the light quarks ($u,d,s$) are almost massless and thus have to 
be treated relativistically, bound states made from heavy quarks allow for a
precise non-relativistic treatment. In what follows, we will only consider the
light quarks at low energies, where perturbation theory in  $\alpha_S$ is
inapplicable (this regime is frequently called ``strong QCD''). 
A further manifestation  of strong QCD is the appearance of nuclei, 
shallow bound states composed of protons, neutrons, pions or strange 
particles like hyperons. The resulting nuclear forces that are responsible 
for the nuclear binding are residual color  forces, much like the van der 
Waals forces between neutral molecules. It is
the aim of this article to provide the link between QCD and its symmetries,
in particular the spontaneously and explicitely broken chiral symmetry, and
the nuclear forces which will allow to put nuclear physics on  firm
theoretical grounds and also gives rise to a very accurate calculational
scheme for nuclear forces and the properties of nuclei.

This review is organized as follows: In this section, we briefly discuss
some of the concepts underlying the chiral effective field theory of the
nuclear forces and make contact to ab initio lattice simulations of
two-baryon systems as well as to more phenomenological approaches.
Sec.~\ref{sec:EFT} deals with the foundations and applications of
nuclear EFT and should be considered the central piece of this review.
In particular, tests of these forces  in few-nucleon systems are discussed.
Attempts to tackle nuclear matter and finite nuclei are considered in
sec.~\ref{sec:many}. We end with a short summary and outlook.



\subsection{Chiral symmetry}
\label{sec:chisym}
First, we must discuss chiral symmetry in the context of QCD. Chromodynamics is a
non-abelian $SU(3)_{\rm color}$ gauge theory with $N_f = 6$ flavors of quarks,
three of them being light ($u,d,s$) and the other three heavy ($c,b,t$).
Here, light and heavy refers to a typical hadronic scale of about 1~GeV.
In what follows, we consider light quarks only (the heavy quarks are to be 
considered as decoupled). The QCD Lagrangian reads
\beqa\label{LQCD}
{\mathcal L}_{\rm QCD} &=& -\frac{1}{2g^2} {\rm Tr} \left( G_{\mu\nu}G^{\mu\nu}
\right) + \bar q \, i \gamma^\mu D_\mu \, q -  \bar q {\mathcal M} \, q
\nonumber\\
&=&{\mathcal L}_{\rm QCD}^0  -  \bar q {\mathcal M} \, q   ~,
\eeqa
where we have absorbed the gauge coupling in the definition of the gluon
field and color indices are suppressed.  The three-component vector $q$
collects the quark fields, $q^T (x) = \left( u(s), d(x), s(x)\right)$. 
As far as the strong interactions
are concerned, the different quarks $u,d,s$ have identical properties, except
for their masses. The quark masses are free parameters in QCD - the theory
can be formulated for any value of the quark masses. In fact, light quark QCD
can be well approximated by a fictitious world of massless quarks,
denoted ${\mathcal L}_{\rm QCD}^0$ in Eq.~(\ref{LQCD}). Remarkably,
this theory contains no adjustable parameter - the gauge coupling $g$ merely
sets the scale for the renormalization group invariant scale $\Lambda_{\rm
  QCD}$. Furthermore, in the massless world left- and right-handed quarks
are completely decoupled. 
The Lagrangian of massless QCD is invariant under separate unitary
global transformations of the left- and right-hand quark fields, the
so-called {\em chiral rotations},
$q_I \to V_I q_I~,  V_I \in U(3)~,  I = L,R$,
leading to $3^2 =9$ conserved left- and $9$ conserved right-handed 
currents by virtue of Noether's theorem. These can be expressed in terms of 
vector ($V = L + R$) and  axial-vector ($A = L - R$) currents
\beqa\label{conscurr}
V_0^\mu &=& \bar q \, \gamma^\mu \, q~, \quad 
V^\mu_a = \bar q \, \gamma^\mu \frac{\lambda_a}{2} \, q~,\nonumber\\
A_0^\mu &=& \bar q \, \gamma^\mu \gamma_5 \, q~,\quad 
A^\mu_a = \bar q \, \gamma^\mu \gamma_5 \frac{\lambda_a}{2} \, q~,

\eeqa
Here, $a = 1, \ldots 8$, and the $\lambda_a$ are Gell-Mann's $SU(3)$
flavor matrices. The singlet axial current is anomalous,
and thus not conserved. The actual symmetry group of massless QCD
is generated by the charges of the conserved currents, it is
$G_0 = SU(3)_R \times SU(3)_L \times U(1)_V$. The $U(1)_V$ subgroup of 
$G_0$ generates conserved baryon number since the isosinglet vector 
current counts the number of quarks minus antiquarks in a hadron. 
The remaining group $SU(3)_R \times SU(3)_L$ is often
referred to as chiral $SU(3)$. Note that one also considers the light
$u$ and $d$ quarks only (with the strange quark mass fixed at its
physical value), in that case, one speaks of chiral $SU(2)$ and
must replace the generators in Eq.~(\ref{conscurr}) by the Pauli-matrices.
Let us mention that QCD is also invariant under the discrete symmetries of
parity ($P$), charge conjugation ($C$) and time reversal ($T$). 
Although interesting in itself, we do not consider strong $CP$ violation and
the related $\theta$-term in what follows, see e.g.~\cite{Peccei:2006as}.

The chiral symmetry is a symmetry of the Lagrangian of QCD but not of the
ground state or the particle spectrum -- to describe the strong interactions
in nature, it is crucial that chiral symmetry is spontaneously broken. This
can be most easily seen from the fact that hadrons do not appear in parity
doublets. If chiral symmetry were exact, from any hadron one could generate
by virtue of an axial transformation another state of exactly the same 
quantum numbers except of opposite parity. The spontaneous symmetry breaking
leads to  the formation of a quark condensate in the vacuum 
$\langle 0 | \bar q q|0\rangle =\langle 0  | \bar q_L q_R + \bar q_R q_L|0\rangle$, 
thus connecting the left- with the right-handed
quarks. In the absence of quark masses this expectation value
is flavor-independent: $\langle 0 | \bar u u|0\rangle = 
\langle 0 | \bar d d|0\rangle = \langle 0 | \bar q q|0\rangle$. 
More precisely, the vacuum is only invariant under the subgroup of 
vector rotations times the baryon number current, $H_0 = SU(3)_V \times
U(1)_V$. This is the generally accepted picture that is supported by general
arguments \cite{Vafa:1983tf} as well as lattice simulations of QCD (for 
a recent study, see~\cite{Giusti:2007cn}).
In fact, the vacuum expectation value of the quark condensate is only one
of the many possible order parameters characterizing the spontaneous symmetry
violation - all operators that share the invariance properties of the
vacuum 

qualify as order parameters. The quark condensate
nevertheless enjoys a special role, it can be shown to be related to the
density of small eigenvalues of the QCD Dirac operator 
(see \cite{Banks:1979yr} and more recent discussions 
in \cite{Leutwyler:1992yt,Stern:1998dy}),
$\lim_{{\cal M} \to 0} \langle 0 | \bar q q|0\rangle = - \pi \, \rho(0)$.
For free fields, $\rho (\lambda) \sim \lambda^3$ near $\lambda = 0$. Only if
the eigenvalues accumulate near zero, one obtains a non-vanishing condensate.
This scenario is indeed supported by lattice simulations and many model studies
involving topological objects like instantons or monopoles.


Before discussing the implications of spontaneous symmetry breaking for QCD,
we briefly remind the reader of Goldstone's theorem 
\cite{Goldstone:1961eq,Goldstone:1962es}: to every generator of
a spontaneously broken symmetry corresponds a massless excitation of the
vacuum.  These states are the
{\em Goldstone bosons}, collectively denoted as pions $\pi(x)$ in what follows.
Through the corresponding symmetry current the Goldstone bosons couple 
directly to the vacuum,
\beq\label{GBME}
\langle 0 | A^0 (0) | \pi \rangle \neq 0~.
\eeq
In fact, the non-vanishing of this matrix element is a {\it necessary and
sufficient} condition for spontaneous symmetry breaking. In QCD, we have
eight (three) Goldstone bosons for $SU(3)$ ($SU(2)$) with spin zero and 
negative parity -- the latter property is a consequence that these Goldstone 
bosons are generated by applying the axial charges on the vacuum. The
dimensionful scale associated with the matrix element Eq.~(\ref{GBME}) 
is the pion decay constant (in the chiral limit)
\beq\label{GBM}
\langle 0|A^a_\mu(0)|\pi^b(p)\rangle = i \delta^{ab} F p_\mu~,
\eeq
which is a fundamental mass scale of low-energy QCD.
In the world of massless quarks, the value of $F$ differs from the
physical value by terms proportional to the quark masses, to be
introduced later, $F_\pi = F [1 + {\cal O}({\cal M})]$. The physical
value of $F_\pi$ is $92.4\,$MeV, determined from pion decay, $\pi\to \nu\mu$. 

Of course, in QCD the quark masses are not exactly zero. The quark mass term leads
to the so-called {\em explicit chiral symmetry breaking}. Consequently, the
vector and axial-vector currents are no longer conserved (with the exception
of the baryon number current)
\beq\label{div}
\partial_\mu V_a^\mu = \dfrac{1}{2} i \bar q \, [{\cal M},\lambda_a ]\, q~, \quad
\partial_\mu A_a^\mu = \dfrac{1}{2} i \bar q \, \{{\cal M},\lambda_a \} \, \gamma_5\, q~.
\eeq
However, the consequences of the spontaneous symmetry violation  can still be
analyzed systematically because the quark masses are {\em small}. QCD
possesses what is called an approximate chiral symmetry. In that case, the mass spectrum
of the unperturbed Hamiltonian and the one including the quark masses can not be
significantly different. Stated differently, the effects of the explicit symmetry
breaking can be analyzed in perturbation theory. 

As a consequence, QCD has a remarkable mass gap
- the pions (and, to a lesser extent,
the kaons and the eta) are much lighter than all other hadrons.  To be more
specific, consider chiral $SU(2)$. The second formula of Eq.~(\ref{div}) is
nothing but a Ward-identity (WI) that relates the axial current $A^\mu =  \bar d
\gamma^\mu \gamma_5 u$ with the pseudoscalar density $P = \bar d i \gamma_5
u$,
\beq
\partial_\mu A^\mu = (m_u + m_d)\, P~.
\eeq
Taking on-shell pion matrix elements of this WI, one arrives at
\beq\label{pimass}
M_\pi^2 = (m_u + m_d) \frac{G_\pi}{F_\pi}~,
\eeq
where the coupling $G_\pi$ is given by $\langle 0 | P(0)| \pi(p)\rangle =
G_\pi $. This equation leads to some intriguing consequences: In
the chiral limit, the pion mass is exactly zero - in accordance with Goldstone's
theorem. More precisely, the ratio $G_\pi /F_\pi$ is a constant in the chiral
limit and the pion mass grows as $\sqrt{m_u+m_d}$ if the quark masses are
turned on. 

There is even further symmetry related to the quark mass term. It is observed
that hadrons appear in isospin multiplets, characterized by very tiny
splittings of the order of a few MeV. These are generated by the small
quark mass difference $m_u -m_d$ 


and also by electromagnetic effects of the
same size (with the notable exception of the charged to neutral pion mass
difference that is almost entirely of electromagnetic origin). This can be
made more precise: For $m_u = m_d$, QCD is  invariant under $SU(2)$ isospin 
transformations: $q \to q' = U q\,$,
with $U$ a unitary matrix.
In this limit, up and down quarks can not be disentangled as far as the
strong interactions are concerned.  Rewriting of the QCD quark mass term
allows to make the strong isospin violation explicit:
\beqa
{\cal H}_{\rm QCD}^{\rm SB} &=& m_u \,\bar u u + m_d
  \,\bar  d d \\
             &=& \dfrac{m_u+m_d}{2}(\bar u u + \bar d d)
              + \dfrac{m_u-m_d}{2}(\bar u u - \bar d d)~,
\nonumber
\eeqa
where the first (second) term is an isoscalar (isovector). Extending 
these considerations to $SU(3)$, one arrives at the eighfold way of
Gell-Mann and Ne'eman
that played a decisive role in our understanding
of the quark structure of the hadrons. The $SU(3)$ flavor symmetry
is also an approximate one, but the breaking is much stronger than it is
the case for isospin. From this, one can directly infer that the quark mass
difference $m_s - m_d$ must be much bigger than $m_d -m_u$. 


The consequences of these broken symmetries can be analyzed systematically
in a suitably tailored effective field theory (EFT), as discussed in more
detail below. At this point, it is important to stress that the chiral symmetry
of QCD plays a crucial role in determining the longest ranged parts of the nuclear
force, which, as we will show, is given by Goldstone boson exchange between
two and more nucleons. This was already stressed long ago, see e.g
\cite{Brown:1970th} (and references therein) but only with the powerful
machinery of chiral effective field theory this connection could be
worked out model-independently, as we will show in what follows.




\subsection{Scales in nuclear physics}
\label{sec:scales}
To appreciate the complexity related to a theoretical description
of the nuclear forces, it is most instructive to briefly discuss the
pertinent scales arising in this problem. This can most easily
be visualized by looking at the phenomenological central potential
between two nucleons, as it appears e.g. in meson-theoretical approaches
to the nuclear force, see Fig.~\ref{fig:Vc}. The longest range
part of the interaction is the one-pion exchange (OPE) that is firmly rooted
in QCD's chiral symmetry. Thus, the corresponding natural scale 
\begin{figure}[tb]
\includegraphics*[width=5.0cm]{Vc.eps}
\vspace{0.1cm}
\begin{center}
\caption{Schematic plot of the central nucleon-nucleon potential.
The longest range contribution is the one-pion-exchange, the intermediate
range attraction is described by two-pion exchanges and other shorter ranged
contributions. At even shorter distances, the NN interaction is strongly
repulsive.
\label{fig:Vc}}
\vspace{-0.5cm}
\end{center}
\end{figure}
\noindent of the nuclear force problem is the Compton wavelength of
the pion
\beq
\lambda_\pi = 1 /M_\pi \simeq 1.5\,{\rm fm}~,
\eeq
where $M_\pi = 139.57\,$MeV is the charged pion mass. The central
intermediate range attraction is given by $2\pi$ exchange (and
shorter ranged physics). Finally, the wavefunctions of two nucleons do 
not like to overlap, which is reflected in a short-range repulsion that
can e.g. be modelled by vector meson exchange. From such considerations,
one would naively expect to be able to describe nuclear binding in
terms of energy scales of the order of the pion mass.  However, the true
binding energies of the nuclei are given by much smaller energy scales,
between 1 to 9 MeV per nucleon. Another measure for the shallow
nuclear binding is the
so called binding-momentum $\gamma$. In the deuteron, 
$\gamma = \sqrt{m B_D} \simeq 45\,{\rm MeV} \ll M_\pi$, with
$m = 938.2\,$MeV the nucleon mass and $B_D = 2.224\,$MeV the
deuteron binding energy. The small value of $\gamma$
signals the appearance of energy/momentum scales much below the pion mass. The
most dramatic reflection of the complexity of the nuclear force problem
are the values of  the S-wave neutron-proton scattering lengths,
\beq\label{aSTNN}
|a(^1S_0)| = 23.8\,{\rm fm} \gg 1/M_\pi\, , ~ 
a(^3S_1)   =  5.4\,{\rm fm} \gg 1/M_\pi\, .
\eeq 
Thus, to properly set up an effective field theory for the forces 
between two (or more) nucleons, it is mandatory to deal with these very 
different energy scales. If one were to treat the large S-wave scattering
lengths perturbatively, the range of the corresponding EFT would be
restricted to momenta below $p_{\rm max} \sim 1/|a(^1S_0)|\simeq 8\,$MeV.
To overcome this barrier, one must generate the small binding
energy scales by a non-perturbative resummation. This can e.g. be done
in a theory without explicit pion degrees of freedom, the so-called
pion-less EFT. In such an approach, the limiting hard scale is the
pion mass. To go further, one must include the pions explicitely,
as it is done in the pion-full or chiral nuclear EFT. The relation
between these different approaches is schematically displayed
in Fig.~\ref{fig:nucscales}.
\begin{figure}[tb]
\includegraphics*[width=6.0cm]{nucscale.eps}
\vspace{0.1cm}
\begin{center}
\caption{Scales in the two-nucleon problem and the range
of validity of the corresponding EFTs as explained in the
text. Here $\Lambda_\chi$ is the hard scale related to 
spontaneous chiral symmetry breaking, with  $\Lambda_\chi
\simeq M_\rho$, with $M_\rho = 770\,$MeV the mass of the
rho meson. 
\label{fig:nucscales}}
\vspace{-0.5cm}
\end{center}
\end{figure}
\noindent 
A different and more formal argument that shows the
breakdown of a perturbative treatment of the EFT with 
two or more nucleons is related to the pinch singularities 
in the two-pion exchange diagram in the static limit as will be 
discussed later in the context of the
explicit construction of the chiral nuclear EFT.

In addition, if one extends the considerations to heavier nuclei
or even nuclear matter, the many-body system exhibits yet another
scale, the Fermi momentum $k_F$, with $k_F \simeq 2M_\pi$ at nuclear
matter saturation density. This new scale must be included in a 
properly modified EFT for the nuclear many-body problem which
is not a straightforward exercise as we will show below. It is therefore
not astonishing that the theory for heavier nuclei is still in a much
less developed stage that the one for the few-nucleon problem. These issues
will be taken up in Sec.~\ref{sec:many}.

For more extended discussions of scales in the nuclear force
problem and in nuclei, we refer to 
\cite{Friar:1995dt,Friar:1996zw,Kaiser:2006tu,Delfino:2007zu}.
