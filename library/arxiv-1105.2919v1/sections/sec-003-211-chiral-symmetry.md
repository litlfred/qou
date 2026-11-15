---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-003-211-chiral-symmetry
section_title: "Chiral symmetry"
section_number: 2.1.1
pages: 7-9
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.962
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The QCD Lagrangian reads
\begin{equation}
{\cal L}_{\rm QCD} = 
\bar{q} (i \gamma^\mu {\cal D}_\mu - {\cal M})q
 - \frac14 
{\cal G}_{\mu\nu,a}
{\cal G}^{\mu\nu}_{a} 
\label{eq_LQCD}
\end{equation}
with the gauge-covariant derivative
\begin{equation}
{\cal D}_\mu = \partial_\mu -ig\frac{\lambda_a}{2}
{\cal A}_{\mu,a}
\end{equation}
and the gluon field strength tensor\footnote{For $SU(N)$ group indices, we use 
Latin letters, $\ldots,a,b,c,\ldots,i,j,k,\dots$,
and, in general, do not distinguish between subscripts and superscripts.}
\begin{equation}
{\cal G}_{\mu\nu,a} =
\partial_\mu {\cal A}_{\nu,a}
-\partial_\nu {\cal A}_{\mu,a}
 + g f_{abc}
{\cal A}_{\mu,b}
{\cal A}_{\nu,c} \,.
\end{equation}
In the above, $q$ denotes the quark fields and ${\cal M}$
the quark mass matrix. Further, $g$ is the
strong coupling constant and ${\cal A}_{\mu,a}$
are the gluon fields. The $\lambda_a$ are the
Gell-Mann matrices and the $f_{abc}$
the structure constants of the $SU(3)_{\rm color}$
Lie algebra $(a,b,c=1,\dots ,8)$;
summation over repeated indices is always implied.
The gluon-gluon term in the last equation arises
from the non-Abelian nature of the gauge theory
and is the reason for the peculiar features
of the color force.

The masses of the up $(u)$, down $(d)$, and
strange (s) quarks are~\cite{PDG}:
\begin{eqnarray}
m_u &=& 2.5\pm 0.8 \mbox{ MeV} ,
\label{eq_umass} \\
m_d &=& 5\pm 0.9 \mbox{ MeV} ,
\label{eq_dmass} \\
m_s &=& 101\pm 25 \mbox{ MeV} .
\label{eq_smass}
\end{eqnarray}
These masses are small as compared to
a typical hadronic scale, i.e., a scale of low-mass
hadrons which are not Goldstone bosons, e.g., 
$m_\rho=0.78 \mbox{ GeV} \approx 1 \mbox{ GeV}$.

It is therefore of interest to discuss the
QCD Lagrangian in the limit of vanishing quark
masses:
\begin{equation}
{\cal L}_{\rm QCD}^0 = \bar{q} i \gamma^\mu {\cal D}_\mu
q - \frac14 
{\cal G}_{\mu\nu,a}
{\cal G}^{\mu\nu}_{a} \,.
\end{equation}
Defining right- and left-handed quark fields,
\begin{equation}
q_R=P_Rq \,, \;\;\;
q_L=P_Lq \,,
\end{equation}
with 
\begin{equation}
P_R=\frac12(1+\gamma_5) \,, \;\;\;
P_L=\frac12(1-\gamma_5) \,,
\end{equation}
we can rewrite the Lagrangian as follows:
\begin{equation}
{\cal L}_{\rm QCD}^0 = 
\bar{q}_R i \gamma^\mu {\cal D}_\mu q_R 
+\bar{q}_L i \gamma^\mu {\cal D}_\mu q_L 
- \frac14 
{\cal G}_{\mu\nu,a}
{\cal G}^{\mu\nu}_{a} \, .
\end{equation}
Restricting ourselves now to
up and down quarks,
we see that
${\cal L}_{\rm QCD}^0$ 
is invariant under the global unitary transformations
\begin{equation}
q_R =
\left( \begin{array}{c}
u_R \\ d_R
\end{array} \right)
\longmapsto
g_R \, q_R =
\exp
\left(
-i \Theta_i^R \frac{\tau_i}{2}
\right)
\left( \begin{array}{c}
u_R \\ d_R
\end{array} \right) 
\label{eq_gR}
\end{equation}
and
\begin{equation}
q_L =
\left( \begin{array}{c}
u_L \\ d_L
\end{array} \right)
\longmapsto
g_L \, q_L =
\exp
\left(
-i \Theta_i^L \frac{\tau_i}{2}
\right)
\left( \begin{array}{c}
u_L \\ d_L
\end{array} \right) 
\,,
\label{eq_gL}
\end{equation}
where $\tau_i \; (i=1,2,3)$ 
are the generators of $SU(2)_{\rm flavor}$,
the usual Pauli spin matrices with commutation relations
\begin{equation}
\left[\frac{\tau_i}{2},\frac{\tau_j}{2} \right]
= i\epsilon^{ijk}\frac{\tau_k}{2}
\,,
\end{equation}
and $g_R$ and $g_L$  are elements of 
$SU(2)_R$ and $SU(2)_L$, respectively. 
In conclusion: {\it The right- and left-handed components of
massless quarks do not mix.} 
This is
$SU(2)_R\times SU(2)_L$ 
symmetry, also known as {\it chiral symmetry}.
Noether's Theorem implies the existence of
six conserved currents;
three right-handed currents
\begin{equation}
R^\mu_i = \bar{q}_R \gamma^\mu \frac{\tau_i}{2} q_R 
\;\;\;\; \mbox{\small\rm with} \;\;\;\; \partial_\mu R^\mu_i = 0
\end{equation}
and three left-handed currents
\begin{equation}
L^\mu_i = \bar{q}_L \gamma^\mu \frac{\tau_i}{2} q_L 
\;\;\;\; \mbox{\small\rm with} \;\;\;\; \partial_\mu L^\mu_i = 0
\,.
\end{equation}
It is useful to consider the following linear
combinations; namely,
three vector currents
\begin{equation}
V^\mu_i = R^\mu_i + L^\mu_i = \bar{q} \gamma^\mu \frac{\tau_i}{2} q
\;\;\;\; \mbox{\small\rm with} \;\;\;\; \partial_\mu V^\mu_i = 0
\label{eq_Vmu}
\end{equation}
and three axial-vector currents
\begin{equation}
A^\mu_i = R^\mu_i - L^\mu_i = \bar{q} \gamma^\mu \gamma_5 
\frac{\tau_i}{2} q
\;\;\;\; \mbox{\small\rm with} \;\;\;\; \partial_\mu A^\mu_i = 0
\,,
\label{eq_Amu}
\end{equation}
which got their names from the fact that they
transform under parity as vector and axial-vector current densities, respectively.
The vector
transformations are given by
\begin{equation}
q =
\left( \begin{array}{c}
u \\ d
\end{array} \right)
\longmapsto
\exp
\left(
-i \Theta_i^V \frac{\tau_i}{2}
\right)
\left( \begin{array}{c}
u \\ d
\end{array} \right) ,
\end{equation}
which are isospin rotations
and, therefore, invariance under vector transformations can be
identified with isospin symmetry.

There are six conserved charges,
\begin{equation}
Q^R_i = \int d^3x \; R^0_i = \int d^3x \; q_R^\dagger (t,\vec x) 
\frac{\tau_i}{2} q_R(t,\vec x)
\;\;\;\; \mbox{\small\rm with} \;\;\;\; \frac{dQ^R_i}{dt} = 0
\end{equation}
and
\begin{equation}
Q^L_i = \int d^3x \; L^0_i = \int d^3x \; q_L^\dagger (t,\vec x) 
\frac{\tau_i}{2} q_L(t,\vec x)
\;\;\;\; \mbox{\small\rm with} \;\;\;\; \frac{dQ^L_i}{dt} = 0
\, ,
\end{equation}
or, alternatively,
\begin{equation}
Q^V_i = \int d^3x \; V^0_i = \int d^3x \; q^\dagger (t,\vec x) 
\frac{\tau_i}{2} q(t,\vec x)
\;\;\;\; \mbox{\small\rm with} \;\;\;\; \frac{dQ^V_i}{dt} = 0
\end{equation}
and
\begin{equation}
Q^A_i = \int d^3x \; A^0_i = \int d^3x \; q^\dagger (t,\vec x) 
\gamma_5 \frac{\tau_i}{2} q(t,\vec x)
\;\;\;\; \mbox{\small\rm with} \;\;\;\; \frac{dQ^A_i}{dt} = 0
\, .
\label{eq_charges}
\end{equation}
The $Q^L_i$ and $Q^R_i$ satisfy the commutation relations 
of the Lie algebra of $SU(2)_R\times SU(2)_L$ (chiral algebra),
\begin{equation}
\left[ Q^R_i, Q^R_j \right] = i \epsilon^{ijk} Q^R_k, \quad \quad
\left[ Q^L_i, Q^L_j \right] = i \epsilon^{ijk} Q^L_k, \quad \quad
\left[ Q^R_i, Q^L_j \right] = 0
\,.
\end{equation}
For $Q^V_i$ and $Q^A_i$, the commutation relations read,
\begin{equation}
\left[ Q^V_i, Q^V_j \right] = i \epsilon^{ijk} Q^V_k, \quad \quad
\left[ Q^A_i, Q^A_j \right] = i \epsilon^{ijk} Q^V_k, \quad \quad
\left[ Q^V_i, Q^A_j \right] = i \epsilon^{ijk} Q^A_k
\,.
\end{equation}
For reasons of completeness, we mention that massless $u$ and $d$ quarks satisfy
an even larger symmetry group, namely,  $SU(2)_R\times SU(2)_L\times U(1)_V\times U(1)_A$. 
While the $U(1)_V$ symmetry corresponds to quark number conservation, the
$U(1)_A$ is broken on the quantum level (``$U(1)_A$ anomaly'') and is not a symmetry
of the system.
