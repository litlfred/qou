---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-021-construction-of-invariants
section_title: "Construction of invariants"
section_number: null
pages: 27-29
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.971
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#subsubsection_ci label="subsubsection_ci"} So far, we have discussed the lowest-order effective Lagrangian for a *global* $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$ symmetry. In Sec. [\[subsubsection_gfcwigf\]](#subsubsection_gfcwigf){reference-type="ref" reference="subsubsection_gfcwigf"} we stated that the Ward identities of QCD are obtained from a *locally* invariant generating functional involving a coupling to external fields. Therefore, following Refs. [@Gasser:1983yg], [@Gasser:1984gg], we will promote the global symmetry of the effective Lagrangian to a local one, $$L\rightarrow V_L(x),\, R\rightarrow V_R(x),$$ and introduce a coupling to the *same* external fields $v$, $a$, $s$, and $p$ as in QCD \[see Eq. ([\[2:1:6:lqcdsn\]](#2:1:6:lqcdsn){reference-type="ref" reference="2:1:6:lqcdsn"})\]. The transformation behavior of the special unitary matrix $U$ of Eqs. ([\[3:1:2:upar\]](#3:1:2:upar){reference-type="ref" reference="3:1:2:upar"}) and ([\[3:1:2:phisu3\]](#3:1:2:phisu3){reference-type="ref" reference="3:1:2:phisu3"}) under $G=\mbox{SU(3)}_L\times\mbox{SU(3)}_R$, parity $P$, and charge conjugation $C$ is given by $$U\stackrel{G}{\mapsto}V_R U V_L^{\dagger},\quad
U(\vec{x},t)\stackrel{P}{\mapsto}U^\dagger(-\vec{x},t),\quad
U\stackrel{C}{\mapsto}U^T.$$ Given an object $A$ transforming as $V_R A V_L^\dagger$, such as $U$ or $\chi$, the covariant derivative of $A$, $D_\mu A$, is defined as $$\label{3:2:3:kaa}
D_\mu A\equiv\partial_\mu A -i r_\mu A+iA l_\mu
\mapsto D'_\mu A'
= V_R(D_\mu A) V_L^\dagger.$$ The defining property is that the covariant derivative should transform as the object it acts on. In particular, the covariant derivative of $U$ is given by $$\label{3:2:3:kdU}
 D_{\mu} U =\partial_{\mu}U-ir_{\mu}U+iU l_{\mu}.$$ For the external fields we introduce corresponding field strength tensors in matrix form as $$\begin{aligned}
\label{3:2:3:fr}
f_{\mu\nu}^R&\equiv&\partial_\mu r_\nu-\partial_\nu r_\mu-i{[r_\mu,r_\nu]}
\stackrel{G}{\mapsto}V_R f_{\mu\nu}^R V_R^\dagger,\\
\label{3:2:3:fl} f_{\mu\nu}^L&\equiv&\partial_\mu l_\nu-\partial_\nu
l_\mu-i{[l_\mu,l_\nu]}\stackrel{G}{\mapsto}V_L f_{\mu\nu}^L
V_L^\dagger.
\end{aligned}$$ They are traceless, because $\mbox{Tr}(l_\mu)=\mbox{Tr}(r_\mu)=0$ and the trace of any commutator vanishes. Finally, we introduce the linear combination $\chi=2B_0(s+ip)$, where, e.g., pure QCD is given by $\chi=2B_0\mbox{diag}(m_u,m_d,m_s)$.

The effective Lagrangian is constructed in terms of $U$, $U^\dagger$, $\chi$, $\chi^\dagger$, $f^{R}_{\mu\nu}$, $f^{L}_{\mu\nu}$ and covariant derivatives of these objects. Suppose we have matrices $A,B,C,\cdots$, all of which transform as $$A\stackrel{G}{\mapsto} V_R A V_L^\dagger, \quad
B\stackrel{G}{\mapsto} V_R B V_L^\dagger, \quad
\cdots.$$ Invariants may be formed by "multiplying" in the following way: $$\begin{aligned}
\mbox{Tr}(A B^\dagger)& \stackrel{G}{\mapsto} & \mbox{Tr}(V_R A
\underbrace{V_L^\dagger\, V_L}_{\mbox{$\mathbbm 1$}}  B^\dagger V_R^{\dagger})
=\mbox{Tr}( V_R^{\dagger}\, V_R A B^\dagger)=\mbox{Tr}(A B^\dagger),
\end{aligned}$$ where the generalization to a longer string of terms is obvious and the product of invariant traces is also invariant: $$\label{3:2:3:chains} \mbox{Tr}(AB^\dagger C D^\dagger),\quad
\mbox{Tr}(A B^\dagger)\mbox{Tr}(C D^\dagger),\quad \cdots.$$ In the chiral counting scheme the elements count as $$U={\cal O}(q^0),\quad
D_{\mu} U={\cal O}(q),\quad
r_{\mu},l_{\mu}={\cal O}(q),\quad
f^{L/R}_{\mu\nu}={\cal O}(q^2), \quad
\chi = {\cal O}(q^2).$$ Any additional covariant derivative counts as ${\cal O}(q)$. The list of objects $A$ up to and including order $q^2$ which transform as $A'=V_R A V_L^{\dagger}$ reads $$U,\, D_{\mu} U,\, D_{\mu} D_{\nu}U,\, \chi,\, U f^L_{\mu\nu},\,
f^R_{\mu\nu} U.$$ The construction of chirally invariant expressions up to and including order $q^2$ proceeds as follows. At ${\cal O}(q^0)$ the only invariant term is a constant, $\mbox{Tr}\left ( U U^{\dagger} \right ) =
\mbox{Tr} ( {\mathbbm 1} ) = const$. Because of $\mbox{Tr}\left( D_{\mu} U U^{\dagger} \right) = 0$, terms of the type $\mbox{Tr}[{\cal O}(q)] \times \mbox{Tr}(\cdots)$ are excluded. At ${\cal O}(q^2)$ we have $$\begin{aligned}
&&\mbox{Tr} \left (D_{\mu} D_{\nu} U U^{\dagger}
\right)
=-\mbox{Tr}\left[D_{\nu} U (D_{\mu} U)^{\dagger}\right],\quad
\mbox{Tr} \left [ D_{\mu} U (D_{\nu} U)^{\dagger} \right ],\quad
\mbox{Tr} \left [ U (D_{\mu} D_{\nu} U)^{\dagger} \right ]
=-\mbox{Tr}\left[D_{\mu} U (D_{\nu} U)^{\dagger}\right], \\
& & \mbox{Tr} \left ( \chi U^{\dagger} \right ),\quad
\mbox{Tr} \left ( U \chi^{\dagger} \right ),\quad
\mbox{Tr} \left [ (U f^L_{\mu\nu}) U^{\dagger} \right ]
= \mbox{Tr} \left ( f^L_{\mu\nu} \right )=0,\quad
\mbox{Tr} \left ( f^R_{\mu\nu} \right )=0.
\end{aligned}$$ Because of Lorentz invariance, indices have to be contracted and the remaining three candidates are $$\mbox{Tr}\left[D_{\mu} U (D^{\mu} U)^{\dagger} \right], \quad
\mbox{Tr}\left ( \chi U^{\dagger} \pm U \chi^{\dagger} \right ).$$ Finally, due to parity conservation, $${\cal L}(\vec{x},t)  \stackrel{P}{\mapsto}  {\cal L}(-\vec{x},t).$$ $\mbox{Tr}(\chi U^\dagger-U\chi^\dagger)$ has to be excluded because of the wrong parity. At ${\cal O}(q^2)$, charge conjugation does not generate any additional constraint.

The locally invariant lowest-order Lagrangian ${\cal L}_2$ is given by $$\label{3:2:3:lol} {\cal L}_2 = \frac{F_0^2}{4} \mbox{Tr} \left[D_{\mu}
U (D^{\mu}U)^{\dagger} \right] +\frac{F_0^2}{4} \mbox{Tr} \left (
\chi U^{\dagger}+ U \chi^{\dagger} \right ).$$ At ${\cal O}(q^2)$ it contains two parameters: the SU(3) chiral limit of the Goldstone boson decay constant $F_0\approx 93\, \mbox{MeV},$ and, hidden in the definition of $\chi$, $B_0=-\langle 0|\bar{q}{q}|0\rangle_0/(3 F^2_0)$.

The lowest-order equation of motion corresponding to Eq. ([\[3:2:3:lol\]](#3:2:3:lol){reference-type="ref" reference="3:2:3:lol"}) is obtained by considering small variations of the SU(3) matrix, $$\label{3:2:3:deltau} U'(x)=U(x)+\delta U(x)=\left({\mathbbm 1}+i\sum_{a=1}^8
\Delta_a(x)\lambda_a\right) U(x),$$ where the $\Delta_a(x)$ are real functions. The matrix $U'$ satisfies both conditions $U' U'^\dagger= {\mathbbm 1}$ and $\mbox{det}(U')=1$ up to and including terms linear in $\Delta_a$. Applying the principle of stationary action, the variation of the action reads $$\delta S=i\frac{F^2_0}{4}\int_{t_1}^{t_2}\mbox{d}t
\int \mbox{d}^3 x \sum_{a=1}^8
\Delta_a(x) \mbox{Tr}\left\{\lambda_a[
D_\mu D^\mu U U^\dagger- U(D_\mu D^\mu U)^\dagger -\chi U^\dagger
+ U\chi^\dagger]\right\},$$ where we made use of partial integration, the standard boundary conditions $\Delta_a(t_1,\vec{x})=\Delta_a(t_2,\vec{x})=0$, the divergence theorem, and the definition of the covariant derivative of Eq. ([\[3:2:3:kaa\]](#3:2:3:kaa){reference-type="ref" reference="3:2:3:kaa"}). Since the test functions $\Delta_a(x)$ may be chosen arbitrarily, we obtain eight Euler-Lagrange equations $$\label{3:2:3:eom8} \mbox{Tr}\left\{\lambda_a[D^2U U^\dagger - U (D^2
U)^\dagger -\chi U^\dagger + U\chi^\dagger]\right\}=0, \quad
a=1,\cdots, 8,$$ which may be combined into a compact matrix form $$\label{3:2:3:eom} {\cal O}_{\rm EOM}^{(2)}(U)\equiv D^2 U U^\dagger -
U (D^2 U)^\dagger -\chi U^\dagger + U \chi^\dagger
+\frac{1}{3}\mbox{Tr}(\chi U^\dagger- U \chi^\dagger)=0.$$ The trace term in Eq. ([\[3:2:3:eom\]](#3:2:3:eom){reference-type="ref" reference="3:2:3:eom"}) appears, because Eq. ([\[3:2:3:eom8\]](#3:2:3:eom8){reference-type="ref" reference="3:2:3:eom8"}) contains eight and not nine independent equations.
