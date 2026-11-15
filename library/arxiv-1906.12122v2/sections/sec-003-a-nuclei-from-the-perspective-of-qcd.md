---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-003-a-nuclei-from-the-perspective-of-qcd
section_title: "A Nuclei from the perspective of QCD"
section_number: null
pages: 3-4
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.993
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
\label{subsec:QCDperspective}

As an $SU(3)_{\rm c}$ gauge theory of colored quarks and gluons, QCD is 
characterized by a coupling constant $g_s$ that becomes strong at low momenta.
The fact that most hadron masses are about $1~\GeV$ or higher---for example, 
the nucleon mass $m_N\simeq 940$ MeV---reveals that nonperturbative QCD
phenomena are associated with a mass scale $\MQCD\sim 1~\GeV$.  The EFT at the 
scale of a few GeV includes not only strong interactions, but also electroweak
and even weaker interactions.  In contrast to most textbooks, for convenience we
refer to this EFT, which is our starting point, simply as QCD.  Focusing on the
two lightest (up and down) quarks most relevant to nuclear physics, the QCD
Lagrangian is written in terms of quark $q=( u \; d)^T$, gluon $G_{\mu}$ and
photon $A_{\mu}$ fields as

\begin{multline}
 \LL_{\text{QCD}} = 
 \bar{q} \left[\ii\gamma^\mu \left(\partial_\mu + \ii g_s G_\mu + \ii e Q 
 A_\mu\right) 
 + \bar{m} \left(1 - \varepsilon \tau_3\right)\right]q \\
 \null - \frac{1}{2} {\rm Tr} \; G_{\mu\nu}G^{\mu\nu}
 - \frac{1}{4} F_{\mu\nu}F^{\mu\nu} + {\cdots},
\label{QCDL}
\end{multline}

where $\gamma_\mu$ and $\tau_i$ are the Dirac and Pauli matrices, and 
$G_{\mu\nu}$ and $F_{\mu\nu}$ are the gauge and photon field strengths.
{Neglecting the ``$\cdots$'', which include for example weak interactions,}
the only parameters in QCD are the quark 
masses and electromagnetic charges.  We can express quark masses in terms of the
common mass $\bar{m} = (m_u+m_d)/2 \sim 5~\MeV$ and of the relative mass 
splitting $\varepsilon=(m_d-m_u)/(m_u+m_d)\sim 1/3$.  The quark charges are
fractions $Q={\text{diag}}(2/3, -1/3)$ of the proton charge 
$e=\sqrt{4\pi\alpha}\sim 1/3$.

Below $\MQCD$, QCD is best represented as a theory of colorless hadrons, where 
$SU(3)_{\mathrm{c}}$ is realized trivially.  An important role is played by
pions, which arise as pseudo-Goldstone bosons from the spontaneous breaking of 
approximate $SU(2)_{\mathrm{L}}\times SU(2)_{\mathrm{R}}$ chiral symmetry down 
to its vector subgroup $SU(2)_{\mathrm{V}}$ of isospin.  In the chiral limit
$\bar m=0$, $\varepsilon=0$ and $e=0$, chiral symmetry is exact, and pions are
massless and interact purely derivatively.  Away from the chiral limit, the
common quark mass breaks chiral symmetry explicitly and leads to a nonzero
common pion mass $m_\pi \simeq 140~\MeV$ and nonderivative pion interactions.
The QCD interactions associated with $\varepsilon$ and $e$ further break
isospin, and appear in relatively small quantities such as the pion mass
splitting $\delta m_\pi^2=m_{\pi^\pm}^2-m_{\pi^0}^2\simeq (36~\MeV)^2$ and the
neutron-proton mass difference $\delta m_N=m_n - m_p\simeq 1.3~\MeV$.

A more complete understanding of the low-energy consequences of QCD can be
achieved if we consider alternative realities where $\bar m$, $\varepsilon$,
and $e$ are varied from their real-world values.  So far,
{LQCD}
simulations of nuclear quantities have been carried out in the isospin-symmetry
limit, where $\varepsilon=0$ and $e=0$.  The only remaining QCD parameter, $\bar
m$, can be traded for the pion mass $m_\pi$.  Because the signal-to-noise ratio
for $A$-nucleon correlation functions at large time $t$ scales as
$\exp{[-A(m_N-3m_\pi/2)t]}$~\cite{Lepage:1989hd,Beane:2010em}, current
simulations are limited to unphysically large $m_\pi$ and to small $A$.
Although one can expect future simulations at smaller pion masses and more
nucleons, it is more efficient to switch to an EFT description suited to the
large distances involved in nuclear physics.

Years of experience suggest that nuclei can be seen as bound states or 
resonances made out of nucleons, or perhaps clusters of nucleons.  The 
choice of degrees of freedom determines the range of validity $\Mhi$ of the 
respective EFT.  Because isospin violation is a relatively small effect for most
nuclear dynamics (more so for light nuclei), we can classify nuclear EFTs by 
their regions of applicability according to typical momentum
and pion mass,
see Fig.~\ref{fig:EFTscape}.  A possible estimate of the typical binding
momentum, where each nucleon contributes equally to the binding energy $B_A$, is
$Q_A\sim \sqrt{2m_N B_A/A}$.  {Nuclear saturation for large $A$ leads, at 
physical pion mass,
to a constant $B_A/A \sim 10$ MeV and nuclear radii $R_A\sim R_0 A^{1/3}$, 
where $R_0\sim 1.2~\fm$.}  Numerically, $Q_A \sim
R_0^{-1}$ is not very different from $m_\pi$, and it has been assumed
that Chiral EFT is best suited for typical nuclei.  (In fact, we will see in
Sec.~\ref {sec:chiral} how $B_A/A \sim 10$ MeV arises naturally within Chiral
EFT.)  At sufficiently small $Q$ and $m_\pi$ (\ie, below a scale 
{$\MNN\sim270~\MeV$ at the physical pion mass, see Eq.~\eqref{OPEscale} for a
precise definition}), one expects pions to be perturbative.  As $Q$
increases  at fixed $m_\pi$, chiral-symmetric pion interactions become
nonperturbative (for $A\ge 2$), and as $Q$ increases further the EFT  eventually
ceases to converge.  As $m_\pi$ increases at fixed $Q$, chiral-symmetry breaking
becomes more important and again the Chiral EFT expansion eventually fails.
We expect that $\Mhi \sim \MQCD$, but the exact breakdown values of $Q$ and
$m_\pi$ are not well known.  It seems that for $A=0$, for example, Chiral EFT
(in the form of ChPT) has $\Mhi\le 500~\MeV$~\cite{Durr:2014oba}.


\begin{figure}[tb]
\centering
\includegraphics[clip,width=0.90\columnwidth]{EFT-Landscape}
\caption{Landscape of nuclear EFTs in the plane of typical momentum $Q$ and pion
 mass $m_\pi$.}
\label{fig:EFTscape}
\end{figure}


Light nuclei are weakly bound and radii scale differently than in the 
saturation regime.  Pions can be treated as short-range interactions
and in Pionless EFT we expect $\Mhi \sim m_\pi$ at all $m_\pi$, including values
beyond the breakdown of Chiral EFT such as in LQCD simulations {to date}.  
For $Q$ smaller
than the inverse radius of a nucleus, the nucleus itself can be treated as an
elementary particle in more complex systems where it appears as a sub-unit.
In the Halo/Cluster EFT relevant for clusterized nuclei, $\Mhi \sim R_c^{-1}$, 
the {inverse} cluster radius.  
Pionless and Halo/Cluster EFTs carry the information of 
QCD to the large distances of nuclear dynamics near the driplines.
