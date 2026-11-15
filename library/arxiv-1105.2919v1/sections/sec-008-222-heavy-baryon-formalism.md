---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-008-222-heavy-baryon-formalism
section_title: "Heavy baryon formalism"
section_number: 2.2.2
pages: 12-15
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.996
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The relativistic treatment of baryons in chiral perturbation
theory leads to problems. The reason for the problems is
the fact that the time-derivative of a relativistic baryon field generates
a factor $E\approx M$ (where $M$ denotes the baryon mass)
which is not small as compared to the chiral-symmetry breaking
scale $\Lambda_\chi \approx 1$ GeV; in fact,
$M_N/\Lambda_\chi \approx 1$.
Note also that the nucleon mass does not vanish in the chiral limit.
The consequence of all this is that the one-to-one correspondence
between the expansion in pion loops, on the one hand,
and the expansion in terms of small external momenta and pion masses,
on the other side, is destroyed~\cite{GSS88,Ber92,BKM95}.

A solution to these problems has been proposed by Jenkins and
Manohar~\cite{JM91} using effective field theory techniques
originally developed by Georgi~\cite{Geo90}
for the study of heavy quark systems.
The basic idea is to treat the baryons
as heavy static sources (``extreme non-relativistic limit'')
such that the momentum transfer between
baryons by pion exchange is small as compared to the baryon mass.
The expansion is performed in terms of these small momenta
over the baryon mass and has become known as
heavy baryon (HB)  
chiral perturbation theory (HBChPT).
We will now briefly sketch this approach.

The four-momentum of the heavy baryon is parametrized as
\begin{equation}
p^\mu=Mv^\mu+l^\mu
\label{eq_pmu}
\end{equation}
where $v^\mu$ is the four-velocity satisfying $v^2=1$ and
$l^\mu$ is a small residual momentum, $v\cdot l \ll M$.
Defining projection operators
\begin{equation}
P_v^\pm=\frac{1\pm \gamma_\mu v^\mu}{2} \,,
\quad \quad \quad
P_v^+ + P_v^- = 1 \,,
\end{equation}
we introduce the so-called velocity-dependent fields
\begin{equation}
N=e^{iMv\cdot x} P_v^+ \Psi \,,
\quad \quad \quad
h=e^{iMv\cdot x} P_v^- \Psi \,,
\label{eq_Nh}
\end{equation}
such that the relativistic four-component 
Dirac spinor field representing the baryon can be written as
\begin{equation}
\Psi=e^{-iMv\cdot x}(N+h) \,.
\label{eq_PsiNh}
\end{equation}
The exponential factor in Eq.~(\ref{eq_Nh}) eliminates the kinematical dependence
on the baryon mass.
To make the meaning of the fields $N$ and $h$ more
transparent, consider a positive-energy plane wave solution of
the Dirac equation
\begin{equation}
\psi_p(x)=u(\vec p,s) e^{-i p\cdot x} \,,
\quad \quad
	u(\vec p,s) = \sqrt{\frac{E+M}{2M}} 
        \left(
	\begin{array}{c}
	  I   \\
	\frac{\vec \sigma \cdot \vec p}{E+M}
	\end{array}
	\right)
        \chi_s
\,,
\end{equation}
where $I$ is the two-dimensional identity matrix, 
$p^0=E=\sqrt{{\vec p}~^2+M^2}$, and $\chi_s$ a Pauli 
spinor describing the spin state of the baryon.
Assuming for the four-velocity $v^\mu = (1,0,0,0)$,
which is what we have in the rest frame of the baryon,
the explicit expressions for the wave function components
$N_p$ and $h_p$ are
\begin{eqnarray}
N_p&=&\sqrt{\frac{E+M}{2M}}
        \left(
	\begin{array}{c}
	 \chi_s\\
	   0
	\end{array}
	\right)
  e^{-i(E-M)t+i\vec p \cdot \vec x} 
\longmapsto 
        \left(
	\begin{array}{c}
	 \chi_s\\
	   0
	\end{array}
	\right)
  e^{-i(E-M)t+i\vec p \cdot \vec x} 
\,,
\\
h_p&=&\sqrt{\frac{E+M}{2M}}
        \left(
	\begin{array}{c}
	   0   \\
	\frac{\vec \sigma \cdot \vec p}{E+M}\chi_s
	\end{array}
	\right)
  e^{-i(E-M)t+i\vec p \cdot \vec x} \,,
\end{eqnarray}
where the $0$ represents a column vector that consists
of two zeros.
The arrow indicates the properly normalized spinor at leading order.
So, for $v^\mu=(1,0,0,0)$, 
$N_p$ represents the large/upper component
and $h_p$ the small/lower component of the 
Dirac wave function $\psi_p$.
Note also that the energy of 
$N_p$ and $h_p$ 
is different
from $\psi_p$; namely,  
they carry the small
residual energy
[cf.\ Eq.~(\ref{eq_pmu})]
\begin{equation}
l_0=E-M\approx 0 + \frac{{\vec p}~^2}{2M} + \ldots \,.
\end{equation}
Thus, $l_0$ is zero in leading order and ${\vec p}~^2/2M$ at 
next-to-leading order (NLO).

To derive the leading-order heavy-baryon Lagrangian,
we start from the leading-order relativistic one,
\begin{equation}
{\cal L}^{(1)}_{\pi N}  =  
 \bar{\Psi} \left(i\gamma^\mu {D}_\mu 
 - M
 + \frac{g_A}{2} \gamma^\mu \gamma_5 u_\mu
  \right) \Psi  
\,,
\end{equation}
and insert 
Eq.~(\ref{eq_PsiNh}),
assuming $v^\mu=(1,0,0,0)$ for simplicity\footnote{For a 
full-fledged derivation, see Ref.~\cite{Sch03}}.
One immediate result is that the $e^{-iMt}$ factor of
Eq.~(\ref{eq_PsiNh})
generates a term $\gamma_0 M$ which kills the
troublesome baryon mass term $(-M)$ in the upper component
projection yielding
\begin{equation}
{\cal L}^{(1)}_{\pi N}  =  
 \bar{N} \left(i\gamma^\mu {D}_\mu 
 + \frac{g_A}{2} \gamma^\mu \gamma_5 u_\mu
  \right) N  
 + \ldots
\label{eq_L1relN}
\end{equation}
where the ellipsis stands for additional expressions 
involving the lower-component
field $h$. Since $N$ contains only upper components, 
Eq.~(\ref{eq_L1relN})
collapses to
\begin{equation}
\widehat{\cal L}^{(1)}_{\pi N} 
 =  
\bar{N} \left(
 i {D}_0 
 - \frac{g_A}{2} \; 
\vec \sigma \cdot \vec u
\right) N  
\label{eq_L1HB}
\end{equation}
plus $1/M$ corrections which are generated by expressing $h$
in terms of $N$ via the equations of motion for $N$ and $h$. 
The first such $1/M$ corrections are shown in
Eq.~(\ref{eq_L2fixed}), below.

Equation~(\ref{eq_L1HB}) is the leading order $\pi N$
Lagrangian in the HB formalism (as indicated by the hat).
Expanding in numbers of pion fields, 
this Lagrangian reads
\begin{eqnarray}
\widehat{\cal L}^{(1)}_{\pi N} 
& = & 
\bar{N} \left\{ 
i \partial_0 
- \frac{1}{4f_\pi^2} \;
\mbox{\boldmath $\tau$} \cdot 
 ( \mbox{\boldmath $\pi$}
\times
 \partial_0 \mbox{\boldmath $\pi$})
- \frac{g_A}{2f_\pi} \;
\mbox{\boldmath $\tau$} \cdot 
 ( \vec \sigma \cdot \vec \nabla )
\mbox{\boldmath $\pi$} 
\right. 
\nonumber \\ && 
\left.
+ \frac{g_A(4\alpha-1)}{4f_\pi^3} \;
(\mbox{\boldmath $\tau$} \cdot 
\mbox{\boldmath $\pi$}) 
\left[ \mbox{\boldmath $\pi$} \cdot 
 ( \vec \sigma \cdot \vec \nabla )
\mbox{\boldmath $\pi$} \right]
+ \frac{g_A\alpha}{2f_\pi^3} \;
\mbox{\boldmath $\pi$}^2 
\left[ \mbox{\boldmath $\tau$} \cdot 
 ( \vec \sigma \cdot \vec \nabla )
\mbox{\boldmath $\pi$} 
\right]
\right\} N 
+ \ldots
\label{eq_L1}
\end{eqnarray}
where the ellipsis stands for terms involving four
or more pions.

{\it At dimension two},
the relativistic $\pi N$ Lagrangian reads
\begin{equation}
{\cal L}^{(2)}_{\pi N} 
= \sum_{i=1}^{4} c_i \bar{\Psi} O^{(2)}_i \Psi \, .
\label{eq_L2rel}
\end{equation}
The various operators $O^{(2)}_i$ are given in Ref.~\cite{Fet00}.
The fundamental rule by which this Lagrangian---as well as all 
the other
ones---are assembled is that they must contain {\it all\/} terms
consistent with chiral symmetry and Lorentz invariance 
(apart from other trivial
symmetries) at a given chiral dimension (here: order two).
The parameters $c_i$ are known as low-energy constants (LECs)
and are determined empirically from fits to $\pi N$ data.

The HB projected $\pi N$ Lagrangian at order two 
is most conveniently broken up into two pieces,
\begin{equation}
\widehat{\cal L}^{(2)}_{\pi N} \, = \,
\widehat{\cal L}^{(2)}_{\pi N, \, \rm fixed} \, + \,
\widehat{\cal L}^{(2)}_{\pi N, \, \rm ct} \, ,
\label{eq_L2}
\end{equation}
with
\begin{eqnarray}
\widehat{\cal L}^{(2)}_{\pi N, \, \rm fixed}  
 & = &  
 \bar{N} \left[
\frac{1}{2M_N}\: \vec D \cdot \vec D
+ i\, \frac{g_A}{4M_N}\: \{\vec \sigma \cdot \vec D, u_0\}
 \right] N
\nonumber \\ & = & 
 \bar{N} \left\{
 \frac{{\vec \nabla}^2}{2M_N} 
-\frac{ig_A}{4M_Nf_\pi} 
\mbox{\boldmath $\tau$} \cdot 
\left[
\vec \sigma \cdot
\left( \stackrel{\leftarrow}{\nabla} 
\partial_0 \mbox{\boldmath $\pi$}
 -
\partial_0 \mbox{\boldmath $\pi$}
\stackrel{\rightarrow}{\nabla} \right)
\right]
\right.
\nonumber \\ &&
\left.
- \frac{i}{8M_N f_\pi^2}
\mbox{\boldmath $\tau$} \cdot 
\left[
\stackrel{\leftarrow}{\nabla} 
\cdot
( \mbox{\boldmath $\pi$} \times \vec\nabla \mbox{\boldmath $\pi$} )
   -   
( \mbox{\boldmath $\pi$} \times \vec\nabla \mbox{\boldmath $\pi$} )
\cdot
\stackrel{\rightarrow}{\nabla} 
\right]
\right\} N 
 + \ldots
\label{eq_L2fixed}
\end{eqnarray}
and
\begin{eqnarray}
\widehat{\cal L}^{(2)}_{\pi N, \, \rm ct}
& = & 
 \bar{N} \left[
 2\, c_1
\, m_\pi^2\, (U+U^\dagger)
\, + \, 
\left( c_2 - \frac{g_A^2}{8M_N}\right) u_0^2
 \, + \,
c_3
\, u_\mu  u^\mu

+ \, \frac{i}{2} 
\left( c_4 + \frac{1}{4M_N} \right) 
  \vec \sigma \cdot ( \vec u \times \vec u)
 \right] N 
\nonumber \\ & = & 
 \bar{N} \left[
 4c_1m_\pi^2
-\frac{2 c_1}{f_\pi^2} \, m_\pi^2\, \mbox{\boldmath $\pi$}^2 
\, + \, 
\left( c_2 - \frac{g_A^2}{8M_N}\right) 
\frac{1}{f_\pi^2}
(\partial_0 \mbox{\boldmath{$\pi$}} \cdot 
 \partial_0 \mbox{\boldmath{$\pi$}})

 + \, \frac{c_3}{f_\pi^2}\,
(\partial_\mu \mbox{\boldmath{$\pi$}} \cdot 
\partial^\mu \mbox{\boldmath{$\pi$}})
\right.  
\nonumber \\ && \left.
 - \, \left( c_4 + \frac{1}{4M_N} \right) 
\frac{1}{2f_\pi^2}
\epsilon^{ijk} \epsilon^{abc} \sigma^i \tau^a
(\partial^j \pi^b) (\partial^k \pi^c)
 \right] N 
\, + \, \ldots ,
\label{eq_L2ct}
\end{eqnarray}
where we neglected the isospin-breaking $c_5$-term
proportional to $(m_u-m_d)$;
the ellipsis represents terms involving 
more pions.

Note that 
$\widehat{\cal L}^{(2)}_{\pi N, \, \rm fixed}$  
is created entirely from the HB expansion of the relativistic
${\cal L}^{(1)}_{\pi N}$ and thus has no free parameters (``fixed''),
while 
$\widehat{\cal L}^{(2)}_{\pi N, \, \rm ct}$
is made up by the new $\pi N$ contact terms proportional to the
$c_i$ parameters (plus those $1/M_N$ corrections
which happen to have the same mathematical structure as
$c_i$ terms).

{\it At dimension three},
the relativistic $\pi N$ Lagrangian can be formally written as
\begin{equation}
{\cal L}^{(3)}_{\pi N} 
= \sum_{i=1}^{31} d_i \bar{\Psi} O^{(3)}_i \Psi \, ,
\label{eq_L3rel}
\end{equation}
with the operators, $O^{(3)}_i$, listed in Refs.~\cite{Fet00,FMS98}; 
not all 31 terms will be of interest here.
The new LECs that occur at this order are the $d_i$.
Similar to the order two case,
the HB projected Lagrangian at order three can be broken into two pieces,
\begin{equation}
\widehat{\cal L}^{(3)}_{\pi N} \, = \,
\widehat{\cal L}^{(3)}_{\pi N, \, \rm fixed} \, + \,
\widehat{\cal L}^{(3)}_{\pi N, \, \rm ct} \, ,
\label{eq_L3}
\end{equation}
with
$\widehat{\cal L}^{(3)}_{\pi N, \, \rm fixed}$
and
$\widehat{\cal L}^{(3)}_{\pi N, \, \rm ct}$
given in Refs.~\cite{Fet00,FMS98}.
