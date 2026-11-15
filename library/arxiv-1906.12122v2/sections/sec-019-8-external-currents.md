---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-019-8-external-currents
section_title: "External currents"
section_number: 8
pages: 15-17
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.784
latex_coverage_ratio: 0.962
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
\label{sec:Currents-TwoBody}

One of the great advantages of the EFT approach is that it is straightforward
to include external currents in addition to interactions between nucleons.
Power counting leads to a systematic expansion of current operators, which had
previously been classified only as one-body and many-body pieces (also known as
``meson-exchange currents'').

Photons are introduced in the effective Lagrangian as described above.   In
addition, weak interactions are accounted for by current-current interactions,
where the currents have the well-known vector-axial ($V-A$) form.  Power
counting is similar to that described in Sec.~\ref{sec:PowerCounting}, with
current operators subject to the same enhancement by powers of $\aleph^{-1}$
when $S$ waves are involved~\cite{Chen:1999tn}.
{Electromagnetic couplings were analyzed with the Wilsonian
RG by \textcite{Kvinikhidze:2018dnw}.}

The earliest example in the context of Pionless EFT are calculations of static
deuteron properties by \textcite{Chen:1999tn}, paralleling previous work by
{\textcite{Kaplan:1998sz} and \textcite{Savage:1998ae}} in Chiral EFT with
perturbative pions.
\textcite{Chen:1999tn} calculated several deuteron properties (charge, magnetic
dipole and electric quadrupole form factors, as well {as} electric
polarizabilities)
beyond LO, including also relativistic corrections.  Results were found to be
in
very good agreement with both experimental data and, at low orders, with those
obtained from effective-range
theory~\cite{Lucas:1968aa,Friar:1984zzb,Wong:1994sy}.  At higher orders, the
EFT goes beyond the effective-range approach (which is based on input from
elastic $N\!N$ scattering only) because new operators appear with undetermined
coefficients.  For example, there are magnetic four-nucleon-one-photon
couplings at NLO,

\begin{multline}
 \LL_{\text{mag}}^{(1)}
 = e L_1 \left(N^T P^i_{\textrm{s}} N\right)^\dagger
         \left(N^T P^3_{\textrm{t}} N\right) B_i \\
 - \ii e L_2 \, \leviciv_{ijk} \left(N^T P^i_{\textrm{s}} N\right)^\dagger
                              \left(N^T P^j_{\textrm{s}} N\right) B^k
 + \hc \,.
\label{eq:L-mag-L1L2}
\end{multline}

This is the two-nucleon analog of the single-particle ``Pauli term'' that
describes the direct $\vec{S}\cdot \vec{B}$ coupling of the nucleon spin to a
magnetic field, which accounts for the nucleon anomalous magnetic moment.
Here $L_1$ and $L_2$ are LECs that contribute to the deuteron dipole magnetic
moment as well as to the capture process $np \to d\gamma$.

Motivated by the original work of \textcite{Bethe:1949yr} and
\textcite{Bethe:1950jm}, \textcite{Phillips:1999hh} proposed a new scheme to
incorporate \NLO and higher orders in processes involving the deuteron.  Up to
higher-order corrections contained in the ellipses we can read off the residue
of the deuteron pole from Eq.~\eqref{eq:ERE-d},

\begin{equation}
 Z_d = \left(1-\gamd\rhod\right)^{-1}
 = 1 + \gamd\rhod + (\gamd\rhod)^2 + \cdots \,.
\label{eq:Z-d}
\end{equation}

This residue is directly related to the long-range tail of the deuteron
wavefunction in configuration space.  \textcite{Phillips:1999hh} argued that
convergence of deuteron observables (at least those  sensitive to the
long-range tail of the wavefunction) can be dramatically improved by fitting
to $Z_d$ exactly right at \NLO---rather than building it up perturbatively as
given in Eq.~\eqref{eq:Z-d}---while not spoiling convergence for the
\ThreeSOne phase shifts.

A deuteron dibaryon field (see Sec.~\ref{sec:Dibaryons}) is particularly
convenient for processes with external deuterons.  The dressed dibaryon can be
used directly as an interpolating field to define the $S$ matrix, provided its
wavefunction renormalization is properly taken into account. With a dibaryon,
the effects of a resummation of the effective range can be
assessed~\cite{Beane:2000fi,Ando:2004mm}.

A number of processes has been carefully addressed with these tools.  A precise
and controlled theoretical prediction of the $np \to d\gamma$ cross section is
important because {it enters as an input parameter into big-bang
nucleosynthesis calculations.}  The low-energy values required are difficult
to access experimentally, but are ideally suited for an application of Pionless
EFT.  The {pionless} analysis of this process started by
\textcite{Chen:1999tn} was refined in subsequent
papers~\cite{Chen:1999vd,Chen:1999bg}.  \textcite{Rupak:1999rk} carried out the
analysis {to \NNNNLO}, giving a prediction that is accurate to
a theoretical uncertainty below 1\%. This reaction was revisited with dibaryon
fields at NLO and a resummation of effective-range effects by
\textcite{Ando:2005cz}.

The related processes of deuteron electro- and photodisintegration are
experimentally accessible, and discrepancies between phenomenological potential
models and data have been reported.  Dibaryon fields implementing a resummation
of range effects have been used to \NNLO for $ed\to
e'pn$~\cite{Christlmeier:2008ye} and $d\gamma\to
np$~\cite{Ando:2011nv,Song:2017bkb}, with results generally supporting
phenomenological models.  For example, \textcite{Christlmeier:2008ye} concluded
that no consistent theoretical calculation could describe the data because the
EFT calculation, unlike the potential-model approach, comes with a rigorous
uncertainty estimate.  Subsequently, the
resolution of a problem with the data analysis gave agreement between
experiment and the EFT calculation~\cite{Ryezayeva:2008zz}{, see
Fig.~\ref{fig:GrieChrist}.}


\begin{figure}[tb]
\centering
\includegraphics[clip,width=0.9\columnwidth]{dee-180-fig4-cropped}
\caption{Total cross section $\sigma$ for deuteron electrodisintegration as
 function of the photon energy $E_\gamma$.
 Good agreement is seen
 between measured data points and theoretical calculation (lines), which
 was achieved after the pionless calculation of \textcite{Christlmeier:2008ye}
 helped resolve a problem with the experimental analysis.
 Figure adapted from \textcite{Ryezayeva:2008zz} by H.~W.~Grie\ss hammer.
 Courtesy of H.~W.~Grie\ss hammer.}
\label{fig:GrieChrist}
\end{figure}


The proton-proton fusion process $pp \to d e^+ \nu_e$ is of similar importance
for an understanding of the Sun.  Obviously, Coulomb effects play an important
role for this reaction at very low energies.
\textcite{Kong:1999tw,Kong:1999mp,Kong:2000px}, building upon their previous
work on $pp$ scattering {(see Sec.~\ref{sec:pionlessCoulomb})}, presented a
first
calculation in Pionless EFT at NLO. This calculation was later extended to
N$^4$LO by \textcite{Butler:2001jj}.  An NLO calculation using a dibaryon field
to resum effective-range corrections was presented by \textcite{Ando:2008va}.
\textcite{Chen:2012hm} extended the calculation of the astrophysical $pp$
S-factor to also include its energy derivatives.

The inverse process, neutrino-deuteron breakup scattering, was considered by
\textcite{Butler:2000zp} to N$^2$LO, along the lines of an earlier NLO
perturbative-pion calculation \cite{Butler:1999sv}.  At NLO, the axial-vector
counterparts of Eq.~\eqref{eq:L-mag-L1L2} appear, with two analogous LECs
usually denoted $L_{1,A}$ and $L_{2,A}$. However, because of the quantum numbers
of initial and final states, only the isovector $L_{1,A}$, which contributes to
$pp \to d e^+ \nu_e$ as well, is significant.  Various constraints on $L_{1,A}$
have been discussed by \textcite{Butler:2002cw}, \textcite{Chen:2002pv},
\textcite{Balantekin:2003ep} and \textcite{Chen:2005ak}, confirming SNO's
conclusions about neutrino oscillations.

Additionally, single-nucleon properties can be inferred from nuclear data.
Compton scattering is influenced by the nucleon polarizabilities, which are
response functions that carry much information about hadron dynamics and thus
QCD.  While proton polarizabilities can be extracted directly, neutron
polarizabilities can only be probed in nuclear Compton scattering.  Compton
scattering on the deuteron was studied to N$^2$LO by
\textcite{Griesshammer:2000mi}, where effective ranges were resummed and $Z_d$
fitted.  Values for the isoscalar, scalar electric and magnetic
polarizabilities were extracted by \textcite{Griesshammer:2000mi}.
Additional features of the
cross section were considered by \textcite{Chen:2004wv} and
\textcite{Chen:2004wwa}.  Sum rules for vector and tensor polarizabilities
were given by \textcite{Ji:2003ia}, while a low-energy theorem for the
spin-dependent Compton amplitude was obtained by~\textcite{Chen:2004fg}.

All in all, these calculations support the convergence of Pionless EFT for
momenta below the pion mass, with the power counting discussed in
Sec.~\ref{sec:PowerCounting}. They provide theoretically-controlled cross
sections that impact astrophysics and particle physics.  Heavier probes, such
as pions~\cite{Beane:2002aw}, can be considered as well through a heavy-field
treatment.  Most interesting for nuclear physics are processes with additional
nucleons, which we consider next.
