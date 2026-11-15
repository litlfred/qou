---
doc_id: arxiv-0811.1338v1
doc_title: "Modern theory of nuclear forces"
section_id: sec-009-c-conventional-approaches-to-the-nuclear-force-p
section_title: "Conventional approaches to the nuclear force problem"
section_number: C
pages: 4-8
source_pdf: 0811.1338v1.pdf
source_sha256: 9a57cb6e014d3ead
doc_brief: "Modern theory of nuclear forces — 36 sections: QCD and Nuclear F orces 1; Conventional approaches to the nuc; EFT for F ew-Nucleon Systems: F ou"
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.997
---
\label{sec:conventional}

Before discussing the application of the  effective field theory approach 
to the nuclear force problem, let us make a few comments on the highly
successful conventional approaches. First, we consider the two-nucleon
case. Historically, meson field theory and dispersion relations have 
laid the foundations for the construction of a two-nucleon potential.
All these approaches incorporate the long-range one-pion exchange
as proposed by Yukawa in 1935~\cite{Yukawa:1935xg} which nowadays is
firmly rooted in QCD. Dispersion relations can be used to construct the
two-pion exchange contribution to the nuclear force as pioneered at 
Paris~\cite{Cottingham:1973wt} and Stony Brook~\cite{Jackson:1975be}.
For a review, see e.g. \cite{Machleidt:2001rw}. In
the 1990ties, the so-called high-precision potentials have been
developed that fit the large basis of $pp$ and $np$ elastic scattering data
with a $\chi^2/{\rm datum} \simeq 1$. One of these is the so-called CD-Bonn
potential~\cite{Machleidt:2000ge} (which was developed at Moscow, Idaho).
Besides one-pion, $\rho$ and $\omega$
vector-meson exchanges, it contains two scalar--isoscalar
mesons in each partial wave up to angular momentum $J=5$ with the mass and
coupling constant of the second $\sigma$ fine-tuned in any partial wave.
The hadronic vertices are regulated with form factors with cut-offs
ranging from 1.3 to 1.7~GeV. Similarly, in  the
Nijmegen~I,II potentials one--pion exchange is supplemented by 
heavy boson exchanges with
adjustable parameters which are fitted for all (low) partial waves
separately~\cite{Stoks:1994wp}.
The Argonne V18 (AV18) potential starts from a very general operator
structure in coordinate space and has fit functions for all these
various operators~\cite{Wiringa:1994wb}. While these various potentials
give an accurate representation of the nucleon-nucleon phase shifts and
of most deuteron properties, the situation becomes much less satisfactory
when it comes to the much smaller but necessary three-nucleon forces.
Such three-body forces are needed to describe the nuclear binding
energies and levels, as most systematically shown by the
Urbana-Argonne group~\cite{Pieper:2001mp}. Systematic studies of 
the dynamics and reactions of systems with three or four-nucleons
further sharpen the case for the necessity of including three-nucleon
forces (3NFs), see e.g.~\cite{Gloeckle:1995jg}.  The archetype of a 3NF
is due to Fujita and Miyazawa (FM) \cite{Fujita:1957zz}, who extended Yukawa's
meson exchange idea by sandwiching the pion-nucleon scattering amplitude 
between nucleon lines, thus generating the 3NF of longest range.
In fact, the work of Fujita and Miyazawa has been the seed for many 
meson-theoretical approaches to the three-nucleon force like the families 
of Tucson-Melbourne \cite{TM1,Coon:1974vc},  Brazilian \cite{Coelho:1984hk} or 
Urbana-Illinois \cite{Pudliner:1997ck,Pieper:2001ap} 3NFs. 

While the conventional approach as briefly outlined here as enjoyed
many successes and is frequently used in e.g. nuclear structure and reaction
calculations, it remains incomplete as there are certain deficiencies
that can only be overcome based on EFT approaches. These are: (i) it is
very difficult - if not impossible - to assign a trustworthy theoretical
error, (ii) gauge and chiral symmetries are difficult to implement, (iii)
none of the three-nucleon forces is consistent with the underlying 
nucleon-nucleon interaction models/approaches and (iv) the connection
to QCD is not at all obvious. Still, as we will show later, there is
a very natural connection between these models and the forces derived 
from EFT by mapping the complicated physics of the short-distance
part of any interaction at length scales $\sim 1/M_\rho$ to the tower 
of multi-fermion contact interactions that naturally arise in the EFT description
(see Sec.~\ref{sec:chiralEFT}).


\subsection{Brief introduction to effective field theory}
\label{sec:EFTintro}

Effective field theory (EFT) is a general approach to calculate the low-energy
behavior of physical systems by exploiting a separation of scales in
the system (for reviews see e.g. \cite{Georgi:1994qn,Manohar:1996cq,Burgess:2007pt}).
Its roots can be traced to the renormalization group 
\cite{Wilson-83} and the intuitive understanding of ultraviolet divergences
in quantum field theory \cite{Lepage-89}. A succinct formulation of the 
underlying principle was given by Weinberg \cite{Weinberg:1978kz}:
If one starts from the most general Lagrangian consistent with all 
symmetries of the underlying interaction, one will get the most general
S-matrix consistent with these symmetries. Together with a power counting 
scheme that specifies which terms are required at a desired accuracy
leads to a predictive paradigm for a low-energy theory.
The expansion is typically in powers of a low-momentum scale $\Mlo$
which can be the typical external momentum
over a high-momentum scale $\Mhi$. However, what physical scales 
$\Mhi$ and $\Mlo$ are identified with depends on the considered
system.  In its most simple setting, consider a theory that is made of two
particle species, the light and the heavy
ones with $\Mlo \ll \Mhi$. Consider now soft processes
in which the energies and momenta are of the order of the 
light particle mass (the so-called soft scale). 
Under such conditions, the short-distance
physics related to the heavy particles can never be resolved.
However, it can be represented by light-particle contact interactions 
with increasing dimension (number of derivatives). Consider
e.g. heavy particle exchange between light ones in the limit
that $\Mhi \to \infty$ while keeping the ratio $g/\Mhi$ fixed, with
$g$ the light-heavy coupling constant. As depicted in
Fig.~\ref{fig:resosat}, one can represent such exchange diagrams by a 
sum of local operators of the light fields with increasing
number of derivatives. In a highly symbolic notation
\beq
\frac{g^2}{\Mhi^2 - t} = \frac{g^2}{\Mhi^2} + 
\frac{g^2 \, t}{\Mhi^4} + \ldots~,
\eeq
with $t$ the squared invariant momentum transfer.
\begin{figure}[tb]
\includegraphics*[width=6.6cm]{resosat2.eps}
\vspace{0.1cm}
\begin{center}
\caption{Expansion of a heavy-particle exchange
diagram in terms of local light-particle operators.
The solid and dashed lines denote light and heavy
particles, respectively. The filled circle and square
denote insertions with zero and two derivatives, in order.
The ellipses stands for operators with more derivatives.
\label{fig:resosat}}
\vspace{-0.5cm}
\end{center}
\end{figure}
\noindent In many cases, the corresponding high-energy theory
is not known. Still, the framework of EFT offers a predictive
and systematic framework for performing calculations in the
light particle sector. Denote by ${\cal Q}$ a typical energy
or momentum of the order of $\Mlo$ and by $\Lambda$ the
hard scale where the EFT will break down. In many cases, this
scale is set by the masses of the heavy particles not considered
explicitely. In such a setting, any matrix element or Greens
function admits an expansion in the small parameter ${\cal Q}/
\Lambda$ \cite{Weinberg:1978kz} 
\beq
{\cal M} = \sum\limits_{\nu} \left(\frac{\cal Q}{\Lambda}\right)^{\nu}  
\,{\cal F} \left(\frac{{\cal Q}}{\mu}, g_i\right)
\eeq
where ${\cal F}$ is a function of order one (naturalness), $\mu$
a regularization scale (related to the UV divergences appearing
in the loop graphs) and the $g_i$ denotes a collection of
coupling constants, often called low-energy constants (LECs).
These parameterize (encode) the unknown high-energy (short-distance)
physics and must be determined by a fit to  data (or
can be directly calculated if the corresponding high-energy theory
is known/can be solved). The counting index $\nu$ in general depends 
on the fields in the effective theory, the number of derivatives and
the number of loops. This defines the so-called power counting 
which allows to categorize all contributions to any matrix element
at a given order.  It is important to stress that $\nu$ must be
bounded from below to define a sensible EFT. In QCD e.g. this is 
a consequence of the spontaneous breaking of its chiral symmetry. 
The contributions with the lowest possible value of $\nu$ 
define the so-called leading order (LO) contribution, the first
corrections with the second smallest allowed value of $\nu$ the
next-to-leading order (NLO) terms and so on. In contrast to more
conventional perturbation theory, the small parameter is not a 
coupling constant (like, e.g., in Quantum Electrodynamcis) but 
rather one expands in small energies or momentum, where small 
refers to  the hard scale $\Lambda$. The archetype of such
a perturbative EFT is chiral perturbation theory that exploits the
strictures of the spontaneous and explicit chiral symmetry breaking
in QCD \cite{Gasser:1983yg,Gasser:1984gg}.  Here, the light degrees
of freedom are the pions, that are generated through the symmetry violation.
Heavier particles like e.g. vector mesons only appear indirectly
as they generate local four-pion interactions with four, six, $\ldots$
derivatives. For a recent review, see Ref.~\cite{Bernard:2006gx}.  
Of course, the pions also couple to heavy matter fields like e.g. 
nucleons, that can also be included in CHPT, as reviewed by Bernard
\cite{Bernard:2007zu}.

So far, we have made the implicit assumption of naturalness,
which implies e.g. that the scattering length $a$  
is of natural size as e.g. in CHPT, where the
scale is set by $1/\Lambda_\chi \simeq 1\, {\rm GeV}^{-1}\simeq 0.2\,$fm.
This also implies that there are no bound states close to the 
scattering thresholds. In many physical systems and of particular 
interest here, especially in the two-nucleon system, this is not the case, 
but one rather has to deal with unnaturally large scattering lengths (and
also shallow bound states). To be specific, let us consider nucleon-nucleon
scattering at very low energies in the $^1S_0$ channel, cf. Eq.~(\ref{aSTNN}).
For such low energies, even the pions can be considered heavy and are
thus integrated out. To construct an EFT that is applicable for momenta 
$p > 1/a$, one must retain all terms $a p \sim 1$ in the scattering matrix.  
This requires  a non-perturbative resummation and is most elegantly done
in the power divergence scheme of Kaplan, Savage and 
Wise~\cite{Kaplan:1998tg,Kaplan:1998we}. 
This amounts to summing the leading four-nucleon 
contact term $\sim C_0 (\psi^\dagger \psi)^2$
to all orders in $C_0$ and matching the scale-dependent LEC
$C_0$ to the scattering length. This leads to the T-matrix
\beq
T = \frac{4\pi}{m} \frac{1}{1/a + ip} \left[ 1 + {\cal O}(p^2)\right]~,
\eeq
where the expansion around the large scattering length is made explicit.
All other effects, like e.g. effective range corrections, are treated
perturbatively. This compact and elegant  scheme is, however, not
sufficient for discussing nuclear processes with momenta $p \ge M_\pi$.
We will come back to this topic when we give the explicit construction
of the chiral nuclear EFT in sec.~\ref{sec:chiralEFT}. It is important to 
stress that such EFTs with unnaturally large scattering length can exhibit
universal phenomena that can be observed in physical systems which differ
in their typical energy scale by many orders of magnitude, for a review
see Braaten and Hammer~\cite{Braaten:2004rn}.
We also remark that there are many subtleties in constructing a proper EFT, 
but space forbids to discuss these here. Whenever appropriate and/or
neccessary, we will mention these in the following sections and provide
explicit references. 



\subsection{First results from lattice QCD}
\label{sec:lattice}

Lattice QCD (LQCD) is a promising tool to calculate hadron properties ab
initio from the QCD Lagrangian on a discretized Euclidean space-time.
This requires state-of-the-art high performance computers and refined
algorithms to analyse the QCD partition function by Monte Carlo methods.
Only recently soft- and hardware developments have become available
that allow for full QCD simulations at small enough quark masses
(corresponding to pion masses below 300~MeV), large enough volumes
(corresponding to spatial dimensions larger than 2.5~fm) and
sufficiently fine lattice spacing ($a \simeq 0.05\,$fm) so that the
results are not heavily polluted by computational artefacts and
can really be connected to the physical quark masses by sensible
chiral extrapolations.

For the nuclear force problem, there are two main developments
in LQCD to be reviewed here. These concern the extraction of hadron-hadron
scattering lengths from unquenched simulations and the first attempts
to construct a nuclear potential. These are groundbreaking studies,
but clearly at present one has not yet achieved an accuracy to obtain
high-precision predictions for nuclear properties. We look very much 
forward to the development of these approaches in the years to come.

The first exploratory study of the nucleon-nucleon scattering lengths
goes back to Fukugita et al.~\cite{Fukugita:1994na,Fukugita:1994ve}
in the quenched approximation. They make use of an elegant formuala,
frequently called the ``L\"uscher formula'',
that relates the S-wave scattering length $a_0$ between two hadrons $h_1$
and $h_2$ to the energy shift $\delta E = E_{h_1h_2} - (m_1+m_2)$ of the
two-hadron state at zero relative momentum  confined in spatial box of
size $L^3$. It is given by \cite{Hamber:1983vu,Luscher:1986pf,Luscher:1990ux}
\beq\label{eq:luescher}
\delta E = -\frac{2\pi a_0}{\mu L^3} \left[ 1 + c_1 \frac{a_0}{L}
 + c_2 \frac{a_0^2}{L^2}\right] + {\cal O}(L^{-6})~,
\eeq
with $\mu = m_1 m_2/(m_1+m_2)$ the reduced mass and 
$c_1 = 2.837297$ and $c_2 = 6.375183$.
A generalization of this formalism was given by Beane et al.\cite{Beane:2003da}
utilizing methods developed for the so-called pionless nuclear EFT (EFT
with contact interactions, for a review see e.g. \cite{Bedaque:2002mn}).
It reads
\beqa\label{eq:Sbeane}
p \, \cot\delta_0(p) &=& \frac{1}{\pi L} {\cal S}\left((Lp/2\pi)^2\right)~,
\nonumber\\
{\cal S}(\eta) &=& \sum_{\vec j}^{\Lambda_j} \, \frac{1}{|\vec j\,|^2 - \eta}
- 4\pi \Lambda_j~,
\eeqa
which gives the location of all energy eigenstates in the box. Here,
$\delta_0$ is the S-wave phase shift. The sum over
all three-vectors of integers ${\vec j}$ is such that $|{\vec j}\,| < \Lambda_j$
and the limit $\Lambda_j \to \infty$ is implicit. In the limit $L \gg |a_0|$,
Eq.~(\ref{eq:Sbeane}) reduces to the L\"uscher formula,
Eq.~(\ref{eq:luescher}). On the other hand, for large scattering length,
$|(p \cot\delta_0)^{-1} | \gg L$, the energy of the lowest state is given 
by 
\beq
E_0 = \frac{4\pi^2}{\mu L^2} \left[ d_1 + d_2 Lp\cot\delta_0+ \ldots\right] ~,
\eeq
with $d_1 = 0.472895$, $d_2 = 0.0790234$ and $p \cot\delta_0$ is evaluated at
the energy $E = 4\pi^2 d_1/(\mu L^2)$. Within this framework, in 
Ref.~\cite{Beane:2006mx} the first fully dynamical simulation of the
neutron-proton scattering lengths was performed, with a lowest pion mass of 354~MeV.
This mass is still too high to perform a precise chiral extrapolation
to the physical pion mass, but this calculation clearly demonstrates the
feasilbilty of this approach (see also sec.~\ref{sec:chiralextrap}). 
This scheme can also be extended to hyperon-nucleon interactions, 
see \cite{Beane:2003yx}. A first signal  for $\pi \Lambda$  and 
$n \Sigma^-$ scattering was reported in Ref.~\cite{Beane:2006gf}.
For a recent review on these activities of the NPLQCD collaboration, 
we refer the reader to~\cite{Beane:2008dv}.

Another interesting development was initiated and carried out 
by Aoki, Hatsuda and Ishii \cite{Ishii:2006ec}. They have 
generalized the two-center Bethe-Salpeter wavefunction approach 
of the CP-PACS collaboration~\cite{Aoki:2005uf}, which
offers an alternative to L\"uscher's formula, to the 
two-nucleon (NN) system.
Given an interpolating field for the neutron and for the proton, the
NN potential can be defined from the properly reduced 6-quark Bethe-Salpeter
amplitude $\phi (\vec r\,)$. The resulting Lippmann-Schwinger equation 
defines a non-local  potential for a given, 
fixed separation $r = |{\vec r}|$. Performing a derivative expansion, the
central potential $V_c (r) $ at a given energy $E$ is extracted from
\beq\label{Vlatt}
V_C(r) = E + \frac{1}{m}\frac{\vec\nabla^2 \phi(r)}{\phi (r)}~.
\eeq
Monte Carlo Simulations are then performed to generate the 6-quark 
Bethe-Salpeter
amplitude in a given spin and isospin state of the two-nucleon system on
a large lattice, $V = (4.4\,{\rm fm})^4$ in the quenched approximation for
pion masses between 380 and 730~MeV. Despite these approximations, the 
resulting effective potential extracted using Eq.~(\ref{Vlatt}) shares the
features of the phenomenological NN potentials - a hard core (repulsion)
at small separation surrounded by an attractive well at intermediate and
larger distances, see Fig.~\ref{fig:Vlatt}.
\begin{figure}[tb]
\includegraphics*[width=7.5cm]{Vlatt.eps}


\begin{center}
\caption{Effective potential in the $^1S_0$ channel for three different
quark masses in quenched LQCD after Ref.~\protect\cite{Ishii:2007xz}.
The dashed line is the asymptotic OPEP for $M_\pi =380\,$MeV, $m =
1.2\,$GeV and $g_{þi N}^2/(4\pi) = 14.0$.
We are grateful to Dr. N.~Ishii for providing us with the data.
\label{fig:Vlatt}}
\vspace{-0.5cm}
\end{center}
\end{figure}
\noindent  Furthermore, the asymptotic form of this potential has
exactly the form of the OPE, provided one rescales the formula
\beq
V_C^{\rm OPE} (r) = \frac{g_{\pi N}^2}{4\pi}\,\fet\tau_1\cdot\fet\tau_2
\frac{\vec\sigma_1 \cdot \vec\sigma_2}{3}\left( \frac{M_\pi}{2m}\right)^2
\frac{{\rm e}^{-M_\pi r}}{r}
\eeq   
with the pion and nucleon masses used in the simulations but keeping
the pion-nucleon coupling at its physical value, $g_{\pi N}^2/(4\pi) \simeq
14.0$. These interesting results 
have led to some enthusiastic appraisal,
see e.g. \cite{Wilczek:2007}. However, it is important to stress that 
the so-calculated potential is not unique, especially its properties at
short distances, since it depends on the definition of the interpolating
nucleon fields. Furthermore, the quenched approximation is known to have
uncontrolled systematic uncertainties as it does not even define a quantum
field theory. In this context, the authors of Ref.~\cite{Aoki:2005uf} 
report on the numerical absence of the large-distance-dominating 
$\eta$-exchange from the  flavor-singlet hair-pin diagram. Still, 
one would like to see this promising calculation repeated with dynamical 
quarks of sufficiently small masses. 
In Ref.~\cite{Nemura:2008sp} this framework was used to study the $\Xi N$
interaction. Interestingly, the central potential of the $p\Xi^0$ interaction
looks very similar to the central $np$ potential. It would be interesting 
to extend these calculations to other hyperon-nucleon channels and also
study the effects of SU(3) symmetry breaking. We will come back to these
issues in the context of an three-flavor chiral EFT in sec.~\ref{sec:YN}.
For recent developments in this scheme concerning the calculation of the 
tensor force, the energy dependence of the NN potential and  preliminary
results for full QCD (2+1 flavors), see the talks by  Aoki, Ishii, and
Nemura at the Lattice 2008 conference \cite{Latt08conf}.



\subsection{Observables and not-so observable quantities}

There is an extensive literature, primarily from the sixties and seventies,
on the role of off-shell physics in nuclear phenomena
(see, e.g., Ref.~\cite{SRIVASTAVA75} and references therein).
This includes
not only few-body systems (e.g., the triton) and nuclear matter,
but interactions of two-body systems with external probes,
such as nucleon-nucleon bremstrahlung and the electromagnetic form
factors of the deuteron.
The implicit premise was that there is
a true underlying potential governing the nucleon-nucleon force,
so that its off-shell properties can be determined.
Indeed,
the nuclear many-body problem has traditionally been posed as
finding approximate solutions to the many-particle Schr\"odinger
equation, given a fundamental two-body interaction that reproduces
two-nucleon observables.

In contrast, effective field theories {\em are\/} determined
completely by on-energy-shell information, up to a well-defined
truncation error. In writing down the most general Lagrangian
consistent with the symmetries of the underlying theory,
many-body forces arise naturally. Even though they are
usually suppressed at low energies, they enter at some order
in the EFT expansion. These many-body forces have to be determined
from many-body data. The key point is, however, that no
off-energy-shell information is needed or experimentally accessible.
A fundamental theorem of quantum field theory states that
physical observables (or more precisely, S-matrix elements) are
independent of the choice of interpolating fields that appear in
a Lagrangian \cite{Haag58,COLEMAN69}.
Equivalently, observables are invariant
under a change
of field variables in a field theory Lagrangian (or Hamiltonian):
\beq
\psi(x) \to \psi(x) + \eta P[\psi]\,,
\eeq
where $P[\psi]$ is a local polynomial of the field $\psi$ and its derivatives
and $\eta$ is an arbitray counting parameter.
Newly generated contributions to observables have to cancel separately at
each order in $\eta$. 
This ``equivalence theorem'' holds for renormalized field theories.
In an EFT, one exploits the invariance under field redefinitions
to eliminate redundant terms in the effective Lagrangian and to choose
the most convenient or efficient form for practical
calculations \cite{POLITZER80,GEORGI91,KILIAN94,SCHERER95a,ARZT95}.
Since off-shell Green's functions and the corresponding off-shell amplitudes
{\it do\/} change under field redefinitions, one must conclude that off-shell
properties are unobservable.

Several recent works have emphasized from a field theory
point of view the impossibility of observing off-shell effects.
In Refs.~\cite{FEARING98,FEARING99},
model calculations were used to illustrate how apparent determinations of
the two-nucleon off-shell T-matrix in
nucleon-nucleon bremstrahlung are illusory, since field redefinitions
shift contributions between off-shell contributions and contact interactions.
Similarly, it was shown in Ref. \cite{SCHERER95b} that Compton scattering
on a pion cannot be used to extract information on the off-shell
behavior of the pion form factor.
The authors of Refs.~\cite{FHK99,CFM96} emphasized the nonuniqueness
of chiral Lagrangians for three-nucleon forces and pion production.
Field redefinitions lead to different off-shell forms that yield the same
observables within a consistent power counting.
In Ref.~\cite{KSW99}, an interaction proportional to the equation of
motion is shown to have no observable consequence
for the deuteron electromagnetic form factor, even though it contributes
to the off-shell T-matrix.

In systems with more than two nucleons, one can trade off-shell, two-body
interactions for many-body forces.
This explains how two-body interactions related by unitary transformations
can predict different binding energies for the triton \cite{ARNAN73}
if many-body forces are not consistently included.
These issues were discussed from the viewpoint of unitary transformations
in Refs.~\cite{POLYZOU90} and \cite{AMGHAR95}.
The extension to many-fermion systems in the thermodynamic limit was
considered in \cite{Furnstahl:2000we}. The effects of field redefinitions 
were
illustrated using the EFT for the dilute Fermi gas \cite{Hammer:2000xg}. 
If many-body interactions generated by the field redefinitions are neglected,
a Coester line similar to the one observed for
nuclear matter \cite{COESTER70} is generated. 
Moreover, the connection to more traditional treatments using unitary 
transformations was elucidated.
The question of whether occupation numbers and momentum distributions of 
nucleons in nuclei are observables 
was investigated in Ref.~\cite{Furnstahl:2001xq}. 
Field redefinitions lead to variations in the occupation numbers
and momentum distributions that imply the answer is negative.
The natural size of the inherent ambiguity (or scheme dependence)
in these quantities is determined by the applicability of the 
impulse approximation. Only if the impulse approximation is well justified,
the ambiguity is small and these quantities are approximately scheme
independent. This has important  implications for the interpretation 
of ($e$,$e'p$) experiments with nuclei. Whether the stark difference in 
occupation numbers between nonrelativistic and relativistic Brueckner
calculations can be explained by this ambiguity is another interesting
question \cite{Jaminon:1990zz}.
