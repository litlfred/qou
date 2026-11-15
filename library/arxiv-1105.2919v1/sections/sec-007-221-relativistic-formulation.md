---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-007-221-relativistic-formulation
section_title: "Relativistic formulation"
section_number: 2.2.1
pages: 10-12
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.996
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The next step in our EFT program is to build the most general
Lagrangian consistent with the (broken) symmetries discussed
above.
An elegant formalism for the construction of such Lagrangians
was developed by 
Callan, Coleman, Wess, and Zumino (CCWZ)~\cite{CCWZ}
who worked out
the group-theoretical foundations 
of non-linear realizations of chiral symmetry.\footnote{An accessible introduction into the rather
involved CCWZ formalism can be found in Ref.~\cite{Sch03}.}
It is characteristic for these non-linear realizations that, whenever functions of the Goldstone bosons
appear in the Lagrangian, they are always accompanied with at least one
space-time derivative.
The Lagrangians given below are built upon the CCWZ
formalism. 

As discussed, the relevant degrees of freedom are
pions (Goldstone bosons) and nucleons.
Since the interactions of Goldstone bosons must
vanish at zero momentum transfer and in the chiral
limit ($m_\pi \rightarrow 0$), the low-energy expansion
of the Lagrangian is arranged in powers of derivatives
and pion masses.
The hard scale is the chiral-symmetry breaking
scale, $\Lambda_\chi \approx 1$ GeV. Thus, the expansion is in terms
of powers of $Q/\Lambda_\chi$ where $Q$ is a (small) momentum
or pion mass.
This is chiral perturbation theory (ChPT).

The effective Lagrangian can formally be written as,
\begin{equation}
{\cal L_{\rm eff}} 
=
{\cal L}_{\pi\pi} 
+
{\cal L}_{\pi N} 
 + \, \ldots \,,
\end{equation}
where ${\cal L}_{\pi\pi}$
deals with the dynamics among pions, 
${\cal L}_{\pi N}$ 
describes the interaction
between pions and a nucleon,
and the ellipsis stands for
terms that involve pions and two or more nucleons.
The individual Lagrangians are organized as follows:
\begin{equation}
{\cal L}_{\pi\pi} 
 = 
{\cal L}_{\pi\pi}^{(2)} 
 + {\cal L}_{\pi\pi}^{(4)} 
 + \ldots 
\end{equation}
and
\begin{equation}
{\cal L}_{\pi N} 
= 
{\cal L}_{\pi N}^{(1)} 
+
{\cal L}_{\pi N}^{(2)} 
+
{\cal L}_{\pi N}^{(3)} 
+ \ldots ,
\end{equation}
where the superscript refers to the number of derivatives or 
pion mass insertions (chiral dimension)
and the ellipsis stands for terms of higher dimensions.

To construct chiral Lagrangians,
we introduce the following $SU(2)$ matrix $U$ in flavor space
which collects the Goldstone pion fields,
{\boldmath $\pi$}:
\begin{equation}
U  = 1 + 
\frac{i}{f_\pi}
\mbox{\boldmath $\tau$} \cdot 
\mbox{\boldmath $\pi$}
-\frac{1}{2f_\pi^2} 
\mbox{\boldmath $\pi$}^2
-\frac{i\alpha}{f_\pi^3}
(\mbox{\boldmath $\tau$} \cdot \mbox{\boldmath $\pi$})^3
+\frac{8\alpha-1}{8f_\pi^4} 
\mbox{\boldmath $\pi$}^4
+ \ldots  \,,
\label{eq_U}
\end{equation}
where $f_\pi$ denotes the pion decay constant.
In this expansion, the coefficient of the 
term linear 
in the pion field 
{\boldmath $\pi$}
is fixed such as to produce the correct kinetic
term in the $\pi\pi$ Lagrangian, below,
and the coefficient of the
quadratic term is chosen 
to satisfy the unitary condition $U^\dagger U = 1$,
at second order in the pion field.
However, the coefficient $\alpha$
of the third order is arbitrary
because of our freedom of choice for the interpolating
pion fields
(constrained only by $U$ unitary and $\det U = 1$).
The coefficient of the fourth order is then
dictated by the unitarity condition,
$U^\dagger U = 1$, at fourth order.
Note that (on-shell) observables must not depend
on the choice for the pion fields 
or, in other words, they must not depend
on the (unphysical) parameter $\alpha$ (and there are more
such parameters as you continue to higher orders
in the above expansion of $U$).
Therefore, diagrams with vertices that involve
three or four pions must always be grouped together
such that the $\alpha$ dependence drops out.
For more on this issue, see the calculation of the
two-loop $2\pi$ and $3\pi$ contributions, below,
where those vertices enter.
Popular choices for the pion fields are 
the exponential parametrization
$U=\exp
(i\mbox{\boldmath $\tau$} \cdot \mbox{\boldmath $\pi$}
/f_\pi)$ which corresponds to 
$\alpha=1/6$
and the so-called sigma representation
$U = ( \sigma +
i\mbox{\boldmath $\tau$} \cdot \mbox{\boldmath $\pi$} )
/f_\pi$
with
$\sigma=\sqrt{f_\pi^2- \mbox{\boldmath $\pi$}^2}$
which is equivalent to
$\alpha=0$.

The leading order (LO) 
$\pi\pi$ Lagrangian is now given by~\cite{GL84}
\begin{equation}
{\cal L}_{\pi\pi}^{(2)} =
\frac{f^2_\pi}{4} \, {\rm tr} \left[ \,
\partial_\mu U 
\partial^\mu U^\dagger 
+ m_\pi^2 ( U + U^\dagger)\, \right] \,,
\label{eq_Lpipi}
\end{equation}
where tr denotes the trace in flavor space and $m_\pi$ is the pion mass.
Since Goldstone bosons can interact only when they
carry momentum, the interaction between pions comes
in powers of $\partial_\mu U$.
Only even powers are allowed because of Lorentz invariance. 
Note that the $U$ field transforms under global chiral rotations via
\begin{equation}
U  \longmapsto  g_L \, U \, g_R^\dagger
\end{equation}
with $g_R$ and $g_L$  elements of 
$SU(2)_R$ and $SU(2)_L$, respectively,
cf.\ Eqs.~(\ref{eq_gR}) and (\ref{eq_gL}).
Since we consider global chiral rotations, 
$g_R$ and $g_L$ do not depend on space-time and, therefore,
$\partial_\mu U$ transforms in the same way as $U$.
Thus, the first term in Eq.~(\ref{eq_Lpipi}) is clearly chiral invariant.
The second term
breaks chiral symmetry explicitly with
the coefficient 
chosen such as to reproduce
the correct mass term, which can be seen by
inserting $U$ and expanding in numbers of
pion fields:
\begin{eqnarray}
	{\cal L}_{\pi\pi}^{(2)} 
     &=&
	\frac{1}{2} 
	\partial_\mu \mbox{\boldmath{$\pi$}} \cdot 
	\partial^\mu \mbox{\boldmath{$\pi$}}
     -  \frac{1}{2} m_\pi^2 \mbox{\boldmath{$\pi$}}^2
\label{eq_Lpipi2a}\\ &&
     +  \frac{1-4\alpha}{2f_\pi^2} 
        (\mbox{\boldmath{$\pi$}} \cdot \partial_\mu \mbox{\boldmath{$\pi$}})
        (\mbox{\boldmath{$\pi$}} \cdot \partial^\mu \mbox{\boldmath{$\pi$}})
     -  \frac{\alpha}{f_\pi^2} 
        \mbox{\boldmath{$\pi$}}^2
	\partial_\mu \mbox{\boldmath{$\pi$}} \cdot 
	\partial^\mu \mbox{\boldmath{$\pi$}}
     +\;  \frac{8\alpha-1}{8f_\pi^2} 
        m_\pi^2 \mbox{\boldmath{$\pi$}}^4
     + \; {\cal O} (\mbox{\boldmath $\pi$}^6)
\,,
\label{eq_Lpipi2}
\end{eqnarray}
where we dropped the constant term $f_\pi^2m_\pi^2$,
since it does not contribute to the dynamics.


Baryon fields can also be incorporated into the effective
field theory in a chirally consistent manner.
Gasser {\it et al.}~\cite{GSS88} have derived
the LO relativistic $\pi N$ Lagrangian to be
\begin{equation}
{\cal L}^{(1)}_{\pi N}  =  
 \bar{\Psi} \left(i\gamma^\mu {D}_\mu 
 - M_N
 + \frac{g_A}{2} \gamma^\mu \gamma_5 u_\mu
  \right) \Psi  
\label{eq_L1rel}
\end{equation}
with
\begin{equation}
{D}_\mu  =  \partial_\mu + \Gamma_\mu 
\end{equation}
the chirally covariant derivative 
which introduces the so-called
chiral connection
(an analogy to a gauge term)
\begin{eqnarray}
\Gamma_\mu & = & 
                 \frac12      \left[
                           \xi^\dagger, \partial_\mu \xi
                              \right]
=                \frac12      \left(
                           \xi^\dagger \partial_\mu \xi
                        +  \xi \partial_\mu \xi^\dagger
                               \right)
\label{eq_gamma}
\\
&=& 
\frac{i}{4f^2_\pi} \,
\mbox{\boldmath $\tau$} \cdot 
 ( \mbox{\boldmath $\pi$}
\times
 \partial_\mu \mbox{\boldmath $\pi$})
 \; + \; {\cal O} (\mbox{\boldmath $\pi$}^4) \,,
\end{eqnarray}
representing a vector current
that leads to a coupling of even numbers of pions with the nucleon.
Besides this, the Lagrangian includes a
coupling term which involves the axial vector
\begin{eqnarray}
u_\mu & = & 
                i \left\{
                           \xi^\dagger, \partial_\mu \xi
                  \right\}
              = i \left(
                           \xi^\dagger \partial_\mu \xi
                        -  \xi \partial_\mu \xi^\dagger
                  \right)  
\label{eq_umu}
\\
       &=&
      - \frac{1}{f_\pi} \mbox{\boldmath{$\tau$}} 
	\cdot \partial_\mu \mbox{\boldmath{$\pi$}}
        + \frac{4\alpha-1}{2f_\pi^3} 
	(\mbox{\boldmath{$\tau$}} \cdot \mbox{\boldmath{$\pi$}})
	(\mbox{\boldmath{$\pi$}} \cdot \partial_\mu \mbox{\boldmath{$\pi$}})
        + \frac{\alpha}{f_\pi^3} 
        \mbox{\boldmath{$\pi$}}^2 \,
	(\mbox{\boldmath{$\tau$}} \cdot \partial_\mu \mbox{\boldmath{$\pi$}})
 \; + \; {\cal O} (\mbox{\boldmath $\pi$}^5)  \,,
\end{eqnarray}
which couples an odd number of pions to the nucleon.
The definition of $\xi$ used in the above is
\begin{equation}
\xi  = \sqrt{U} = 1 +
\frac{i}{2f_\pi}
\mbox{\boldmath $\tau$} \cdot \mbox{\boldmath $\pi$}
-\frac{1}{8f_\pi^2} 
\mbox{\boldmath $\pi$}^2
-\frac{i(8\alpha-1)}{16f_\pi^3}
(\mbox{\boldmath $\tau$} \cdot \mbox{\boldmath $\pi$})^3
+ \ldots \,.
\label{eq_xi}
\end{equation}
Note that 
$\xi\xi^\dagger = 1$; therefore,
$\partial_\mu (\xi\xi^\dagger) =  
 (\partial_\mu \xi ) \xi^\dagger 
+\xi \partial_\mu \xi^\dagger =0$,
which is applied in Eqs.~(\ref{eq_gamma}) and (\ref{eq_umu}).

Thus, more explicitly, the LO relativistic $\pi N$
Lagrangian, Eq.~(\ref{eq_L1rel}), reads
\begin{equation}
{\cal L}^{(1)}_{\pi N}  =  
 \bar{\Psi} \left(i\gamma^\mu \partial_\mu - M_N
-\frac{1}{4f^2_\pi} \, \gamma^\mu
\mbox{\boldmath $\tau$} \cdot 
 ( \mbox{\boldmath $\pi$}
\times
 \partial_\mu \mbox{\boldmath $\pi$})
      - \frac{g_A}{2f_\pi} \gamma^\mu \gamma_5
        \mbox{\boldmath{$\tau$}} 
	\cdot \partial_\mu \mbox{\boldmath{$\pi$}}
  + \ldots
  \right) \Psi  
\,.
\label{eq_L1relalt}
\end{equation}
In this equation,
$\Psi$ is the relativistic four-component Dirac spinor field
representing the nucleon,
$M_N$ denotes the nucleon mass and
$g_A$ the axial-vector coupling constant.
Numerical values will be given later.
The term proportional to $g_A/2f_\pi$ is the familiar axial-vector
coupling of one pion to the nucleon,
while the nonlinear term proportional to $1/4f_\pi^2$ is 
known as the Weinberg-Tomozawa coupling (a $2\pi$ contact term)~\cite{Wei66,Tom66},
which is crucial for $\pi$-$N$ $s$-wave scattering at threshold.
