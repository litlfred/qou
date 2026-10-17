---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-008-green-functions-chiral-ward-identities-and-gener
section_title: "Green functions, chiral Ward identities, and generating functional"
section_number: null
pages: 9-15
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.996
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#subsubsection_gfcwigf label="subsubsection_gfcwigf"} For conserved currents, the spatial integrals of the charge densities are time independent, i.e., in a quantized theory the corresponding charge operators commute with the Hamilton operator. These operators are generators of infinitesimal transformations on the Hilbert space of the theory. The mass eigenstates should organize themselves in degenerate multiplets with dimensionalities corresponding to irreducible representations of the Lie group in question. For the moment, we assume that the dynamical system described by the Hamiltonian does not lead to a spontaneous symmetry breakdown. We will come back to this point later. Which irreducible representations ultimately appear, and what the actual energy eigenvalues are, is determined by the dynamics of the Hamiltonian. For example, SU(2) isospin symmetry of the strong interactions reflects itself in degenerate SU(2) multiplets such as the nucleon doublet, the pion triplet, and so on. Ultimately, the actual masses of the nucleon and the pion should follow from QCD.

It is also well-known that symmetries imply relations between $S$-matrix elements. For example, applying the Wigner-Eckart theorem to pion-nucleon scattering, assuming the strong-interaction Hamiltonian to be an isoscalar, it is sufficient to consider two isospin amplitudes describing transitions between states of total isospin $I=1/2$ or $I=3/2$. All the dynamical information is contained in these isospin amplitudes and the results for physical processes can be expressed in terms of these amplitudes together with geometrical coefficients, namely, the Clebsch-Gordan coefficients.

In quantum field theory, the objects of interest are the Green functions which are vacuum expectation values of time-ordered products. Later on, we will also refer to matrix elements of time-ordered products between states other than the vacuum as Green functions. The physical scattering amplitudes are obtained from the Green functions using the reduction formalism [@Lehmann:1954rq]. Symmetries provide strong constraints not only for scattering amplitudes, i.e. their transformation behavior, but, more generally speaking, also for Green functions and, in particular, *among* Green functions. Even if a symmetry is broken, i.e., the infinitesimal generators are time dependent, conditions related to the symmetry-breaking terms can still be obtained using equal-time commutation relations.

The symmetry currents relevant to the global $\mbox{SU(3)}_L\times\mbox{SU(3)}_R\times\mbox{U(1)}_V$ of QCD are given in Eqs. ([\[2:1:3:v\]](#2:1:3:v){reference-type="ref" reference="2:1:3:v"}), ([\[2:1:3:a\]](#2:1:3:a){reference-type="ref" reference="2:1:3:a"}), and ([\[2:1:3:sv\]](#2:1:3:sv){reference-type="ref" reference="2:1:3:sv"}). Moreover, since we also want to discuss explicit symmetry breaking, we introduce the scalar and pseudoscalar densities $$\label{2:1:6:quadraticforms}
S_a=\bar{q}\lambda_a q,\quad
P_a=i\bar{q}\gamma_5 \lambda_a  q,\quad
a=0,\cdots, 8,$$ where $\lambda_0=\sqrt{2/3}\,\mathbbm 1$. For example, linear combinations of $S_a$ and $P_a$ are needed to describe the divergences of the currents in Eqs. ([\[2:1:5:dsva\]](#2:1:5:dsva){reference-type="ref" reference="2:1:5:dsva"}). Whenever it is more convenient, we will also use $$\label{2:1:6:SP}
S(x)=\bar{q}(x) q(x),\quad
P(x)=i\bar{q}(x)\gamma_5 q(x),$$ instead of $S_0$ and $P_0$.

For example, the following Green functions of the "vacuum" sector $$\begin{aligned}
\langle 0|T[A^\mu_a(x) P_b(y)]|0\rangle,\\
\langle 0|T[P_a(x)J^\mu(y) P_c(z)]|0\rangle,\\
\langle 0|T[P_a(w)P_b(x)P_c(y)P_d(z)]|0\rangle
\end{aligned}$$ are related to pion decay, the pion electromagnetic form factor ($J^\mu$ is the electromagnetic current), and pion-pion scattering, respectively. One may also consider similar time-ordered products evaluated between a single nucleon in the initial and final states in addition to the vacuum Green functions. This allows one to discuss properties of the nucleon as well as dynamical processes involving a single nucleon, such as $$\begin{aligned}
\langle N|J^\mu(x)|N\rangle&\leftrightarrow&\mbox{nucleon electromagnetic form factors},\\
\langle N|A^\mu_a(x)|N\rangle&\leftrightarrow&\mbox{axial form factor + induced pseudoscalar form factor},\\
\langle N|T[J^\mu(x) J^\nu(y)]|N\rangle&\leftrightarrow&\mbox{Compton scattering},\\
\langle N|T[J^\mu(x) P_a(y)]|N\rangle&\leftrightarrow&\mbox{pion electroproduction}.
\end{aligned}$$

Generally speaking, a chiral Ward identity relates the divergence of a Green function containing at least one factor of $V^{\mu}_a$ or $A^{\mu}_a$ to some linear combination of other Green functions. The terminology *chiral* refers to the underlying $\mbox{SU(3)}_L\times
\mbox{SU(3)}_R$ group. To make this statement more precise, let us consider as a simple example the two-point Green function involving an axial-vector current and a pseudoscalar density, $$\label{2:1:6:gfaav}
G^\mu_{AP,ab}(x,y)=\langle 0| T[A^\mu_a(x) P_b(y)]|0\rangle
=\Theta(x_0-y_0)\langle 0|A^\mu_a(x) P_b(y)|0\rangle
+\Theta(y_0-x_0)\langle 0|P_b(y) A^\mu_a(x)|0\rangle,$$ and evaluate the divergence $$\begin{aligned}
\partial_\mu^x G^{\mu}_{AP,ab}(x,y)
&=&
 \partial_\mu^x [\Theta(x_0-y_0)\langle 0| A^\mu_a(x) P_b(y)|0\rangle
+\Theta(y_0-x_0)\langle 0|  P_b(y)A^\mu_a(x)|0\rangle ]\\
&=&\delta(x_0-y_0)\langle 0| A_0^a(x) P_b(y)|0\rangle
-\delta(x_0-y_0)\langle 0|  P_b(y)A_0^a (x)|0\rangle\\
&&
+\Theta(x_0-y_0)\langle 0|\partial_\mu^x A^\mu_a(x) P_b(y)|0\rangle
+\Theta(y_0-x_0)\langle 0| P_b(y)\partial_\mu^x A^\mu_a(x)|0\rangle\\
&=&\delta(x_0-y_0)\langle 0|[A^a_0(x),P_b(y)]|0\rangle
+\langle 0|T[\partial_\mu^x A^\mu_a(x) P_b(y)]|0\rangle,
\end{aligned}$$ where we made use of $\partial_\mu^x \Theta(x_0-y_0)=\delta(x_0-y_0)
g_{0\mu}=-\partial_\mu^x \Theta(y_0-x_0)$. This simple example already shows the main features of (chiral) Ward identities. From the differentiation of the theta functions one obtains equal-time commutators between a charge density and the remaining quadratic forms. The results of such commutators are a reflection of the underlying symmetry. As a second term, one obtains the divergence of the current operator in question. If the symmetry is perfect, such terms vanish identically. If the symmetry is only approximate, an additional term involving the symmetry breaking appears. For a soft breaking such a divergence can be treated as a perturbation.

The time ordering of $n+1$ points $x,x_1,\cdots,x_n$ gives rise to $(n+1)$! distinct orderings, each involving products of $n$ theta functions. Via induction, the generalization of the above simple example to an $(n+1)$-point Green function is symbolically of the form $$\begin{aligned}
\label{2:1:6:gendmug}
\lefteqn{\partial_\mu^x \langle 0|T\{J^\mu(x) A_1(x_1)\cdots A_n(x_n)
\}|0\rangle=}\nonumber\\
&&\langle 0|T\{[\partial_\mu^x J^\mu(x)]
A_1(x_1)\cdots A_n(x_n)\}|0\rangle\nonumber\\
&&+\delta(x^0-x_1^0)\langle 0|T\{[J_0(x),A_1(x_1)] A_2(x_2)\cdots A_n(x_n)\}|
0\rangle\nonumber\\
&&+\delta(x^0-x_2^0)\langle 0|T\{A_1(x_1)[J_0(x),A_2(x_2)]
\cdots A_n(x_n)\}|0\rangle\nonumber\\
&&+\cdots+\delta(x^0-x_n^0)
\langle 0|T\{A_1(x_1)\cdots [J_0(x),A_n(x_n)]\}|0\rangle,
\end{aligned}$$ where $J^\mu$ stands generically for any of the Noether currents.

The discussion so far assumes that one explicitly works out the particular chiral Ward identity one is interested in. However, there is an elegant way of obtaining *all* chiral Ward identities from a single expression. To that end we introduce into the Lagrangian of QCD the couplings of the nine vector currents, eight axial-vector currents, nine scalar quark densities, and nine pseudoscalar quark densities to external c-number fields [@Gasser:1984gg]: $$\label{2:1:6:lQCD+ext}
{\cal L}={\cal L}^0_{\rm QCD}+{\cal L}_{\rm ext},$$ where $$\begin{aligned}
\label{2:1:6:lqcds}
{\cal L}_{\rm ext}&=&
\sum_{a=1}^8v^\mu_a\, \bar q\gamma_\mu\frac{\lambda_a}{2} q
+v^\mu_{(s)}\, \frac{1}{3}\bar q\gamma_\mu q
+ \sum_{a=1}^8a^\mu_a\,\bar q\gamma_\mu\gamma_5\frac{\lambda_a}{2} q
-\sum_{a=0}^8 s_a\, \bar q\lambda_a q
+\sum_{a=0}^8 p_a\, i\bar q\gamma_5\lambda_a q
\nonumber\\
&=&\bar{q}\gamma_\mu (v^\mu
+\frac{1}{3}v^\mu_{(s)} +\gamma_5 a^\mu )q -\bar{q}(s-i\gamma_5 p)q.
\end{aligned}$$ The 35 real functions $v^\mu_a(x)$, $v^\mu_{(s)}(x)$, $a^\mu_a(x)$, $s_a(x)$, and $p_a(x)$, will collectively be denoted by $[v,a,s,p]$. A precursor of this method was already used by Bell and Jackiw [@Bell:1969ts] in their discussion of the anomalous divergences in the $\pi^0\to\gamma\gamma$ decay. The Green functions of the vacuum sector may be combined in the generating functional $$\label{2:1:6:gfgfvs}
\exp(i Z[v,a,s,p]) =\langle 0|T\exp\left[i\int \mbox{d}^4 x\, {\cal
L}_{\rm ext}(x) \right]|0\rangle_0.$$ Note that both the quark field operators $q$ in ${\cal L}_{\rm ext}$ and the ground state $|0\rangle$ refer to the chiral limit, indicated by the subscript 0 in Eq. ([\[2:1:6:gfgfvs\]](#2:1:6:gfgfvs){reference-type="ref" reference="2:1:6:gfgfvs"}). A particular Green function is then obtained through a functional derivative with respect to the external fields. As an example, suppose we are interested in the scalar $u$-quark condensate in the chiral limit, $\langle 0| \bar{u}u|0\rangle_0$. We express $\bar u u$ as $$\bar u u=\frac{1}{2}\sqrt{\frac{2}{3}}\bar q\lambda_0 q
+\frac{1}{2}\bar q\lambda_3 q +\frac{1}{2}\frac{1}{\sqrt{3}} \bar
q\lambda_8 q$$ and obtain $$\langle 0|\bar{u}(x) u(x)|0\rangle_0 = \left.\frac{i}{2}\left[\sqrt{\frac{2}{3}}\frac{\delta}{\delta
s_0(x)} +\frac{\delta}{\delta s_3(x)} +\frac{1}{\sqrt{3}}
\frac{\delta}{\delta s_8(x)}\right]
\exp(iZ[v,a,s,p])\right|_{v=a=s=p=0}.$$

From the generating functional, we can even obtain Green functions of the "real world," where the quark fields and the ground state are those with finite quark masses. For example, the two-point function of two axial-vector currents of the "real world," i.e., for $s=\mbox{diag}(m_u,m_d,m_s)$, and the "true vacuum" $|0\rangle$, is given by $$\label{2:1:6:grw}
\langle 0|T[A^\mu_a(x) A^\nu_b(0)]|0\rangle =\left.
(-i)^2 \frac{\delta^2}{\delta a_{a\,\mu}(x)\delta
a_{b\,\nu}(0)}
\exp(iZ[v,a,s,p])\right|_{v=a=p=0,s=\mbox{diag}(m_u,m_d,m_s)}.$$ Note that the left-hand side involves the quark fields and the ground state of the "real world," whereas the right-hand side is the generating functional defined in terms of the quark fields and the ground state of the chiral limit. The actual value of the generating functional for a given configuration of external fields $v$, $a$, $s$, and $p$ reflects the dynamics generated by the QCD Lagrangian.

The (infinite) set of *all* chiral Ward identities resides in an invariance of the generating functional under a *local* transformation of the external fields [@Gasser:1983yg], [@Leutwyler:1993iq]. The use of local transformations allows one to also consider divergences of Green functions. We require $\cal L$ of Eq. ([\[2:1:6:lQCD+ext\]](#2:1:6:lQCD+ext){reference-type="ref" reference="2:1:6:lQCD+ext"}) to be a Hermitian Lorentz scalar, to be even under $P$, $C$, and $T$, and to be invariant under *local* chiral transformations. In fact, it is sufficient to consider $P$ and $C$, only, because $T$ is then automatically incorporated owing to the $CPT$ theorem.

Under parity, the quark fields transform as $$\label{2:1:6:qtrafop}
q_f(t,\vec{x})\stackrel{\mbox{$P$}}{\mapsto}\gamma_0 q_f(t,-\vec{x}),$$ and the requirement of parity conservation, $$\label{2:1:6:parinv}
{\cal L}(t,\vec{x}) \stackrel{\mbox{$P$}}{\mapsto} {\cal L}(t,-\vec{x}),$$ leads, using the results of Table [1](#2:1:6:parity){reference-type="ref" reference="2:1:6:parity"}, to the following constraints for the external fields, $$\label{2:1:6:eftrafop}
v^\mu\stackrel{\mbox{$P$}}{\mapsto}v_\mu,\quad
v^\mu_{(s)}\stackrel{\mbox{$P$}}{\mapsto}v_\mu^{(s)},\quad
a^\mu\stackrel{\mbox{$P$}}{\mapsto}-a_\mu,\quad
s\stackrel{\mbox{$P$}}{\mapsto}s,\quad
p\stackrel{\mbox{$P$}}{\mapsto}-p.$$ In Eq. ([\[2:1:6:eftrafop\]](#2:1:6:eftrafop){reference-type="ref" reference="2:1:6:eftrafop"}) it is understood that the arguments change from $(t,\vec{x})$ to $(t,-\vec{x})$.

::: center
::: {#2:1:6:parity}
            $\Gamma$            $\mathbbm 1$   $\gamma^\mu$   $\sigma^{\mu\nu}$   $\gamma_5$    $\gamma^\mu\gamma_5$
  ---------------------------- -------------- -------------- ------------------- ------------- -----------------------
   $\gamma_0 \Gamma \gamma_0$   $\mathbbm 1$   $\gamma_\mu$   $\sigma_{\mu\nu}$   $-\gamma_5$   $-\gamma_\mu\gamma_5$

  : Transformation properties of the Dirac matrices $\Gamma$ under parity.
:::
:::

Similarly, under charge conjugation the quark fields transform as $$\label{2:1:6:qtrafc}
q_{f,\alpha}\stackrel{\mbox{$C$}}{\mapsto}C_{\alpha\beta}\bar{q}_{f,\beta},
\quad
\bar{q}_{f,\alpha}\stackrel{\mbox{$C$}}{\mapsto}
-q_{f,\beta}C^{-1}_{\beta\alpha},$$ where the subscripts $\alpha$ and $\beta$ are Dirac spinor indices, $$C=i\gamma^2\gamma^0
=\left(\begin{array}{cccc}0&0&0&-1\\0&0&1&0\\
0&-1&0&0\\
1&0&0&0
\end{array}\right)$$ is the usual charge conjugation matrix, and $f$ refers to flavor. Taking Fermi statistics into account, one obtains $$\bar{q}\,\Gamma F q=-\bar{q}\, C \Gamma^T C F^T q,$$ where $F$ denotes a matrix in flavor space. In combination with Table [2](#2:1:6:chargeconjugation){reference-type="ref" reference="2:1:6:chargeconjugation"} it is straightforward to show that invariance of ${\cal L}_{\rm ext}$ under charge conjugation requires the transformation properties $$\label{2:1:6:eftrafoc}
v_\mu\stackrel{C}{\rightarrow}-v_\mu^T,\quad
v_\mu^{(s)}\stackrel{C}{\rightarrow}-v_\mu^{(s)T},\quad
a_\mu\stackrel{C}{\rightarrow}a_\mu^T,\quad
s,p\stackrel{C}{\rightarrow}s^T,p^T,$$ where the transposition refers to the flavor space.

::: center
::: {#2:1:6:chargeconjugation}
     $\Gamma$      $\mathbbm 1$   $\gamma^\mu$    $\sigma^{\mu\nu}$    $\gamma_5$   $\gamma^\mu\gamma_5$
  --------------- -------------- --------------- -------------------- ------------ ----------------------
   $-C\Gamma^TC$   $\mathbbm 1$   $-\gamma^\mu$   $-\sigma^{\mu\nu}$   $\gamma_5$   $\gamma^\mu\gamma_5$

  : Transformation properties of the Dirac matrices $\Gamma$ under charge conjugation.
:::
:::

Finally, we need to discuss the requirements to be met by the external fields under local $\mbox{SU(3)}_L\times\mbox{SU(3)}_R\times\mbox{U}(1)_V$ transformations. In a first step, we write Eq. ([\[2:1:6:lqcds\]](#2:1:6:lqcds){reference-type="ref" reference="2:1:6:lqcds"}) in terms of the left- and right-handed quark fields. Using the projection operators of Eq. ([\[2:1:2:prpl\]](#2:1:2:prpl){reference-type="ref" reference="2:1:2:prpl"}) the Lagrangian of Eq. ([\[2:1:6:lqcds\]](#2:1:6:lqcds){reference-type="ref" reference="2:1:6:lqcds"}) reads $$\label{2:1:6:lqcdsn}
{\cal L}={\cal L}_{\rm QCD}^0
+\bar{q}_L\gamma^\mu\left(l_\mu+\frac{1}{3}v^{(s)}_\mu\right)q_L
+\bar{q}_R\gamma^\mu\left(r_\mu+\frac{1}{3}v^{(s)}_\mu\right)q_R-\bar{q}_R(s+ip)q_L-\bar{q}_L(s-ip)q_R.$$ Equation ([\[2:1:6:lqcdsn\]](#2:1:6:lqcdsn){reference-type="ref" reference="2:1:6:lqcdsn"}) remains invariant under *local* transformations $$\begin{aligned}
\label{2:1:6:qrl}
q_R&\mapsto&\exp\left(-i\frac{\Theta(x)}{3}\right) V_R(x) q_R,\nonumber\\
q_L&\mapsto&\exp\left(-i\frac{\Theta(x)}{3}\right) V_L(x) q_L,
\end{aligned}$$ where $V_R(x)$ and $V_L(x)$ are independent space-time-dependent SU(3) matrices, provided the external fields are subject to the transformations $$\begin{aligned}
\label{2:1:6:sg}
r_\mu&\mapsto& V_R r_\mu V_R^{\dagger}
-i \partial_\mu V_R V_R^{\dagger},\nonumber\\
l_\mu&\mapsto& V_L l_\mu V_L^{\dagger}
-i\partial_\mu V_L V_L^{\dagger},
\nonumber\\
v_\mu^{(s)}&\mapsto&v_\mu^{(s)}-\partial_\mu\Theta,\nonumber\\
s+ip&\mapsto& V_R(s+ip)V_L^{\dagger},\nonumber\\
s-ip&\mapsto& V_L(s-ip)V_R^{\dagger}.
\end{aligned}$$ The derivative terms in Eq. ([\[2:1:6:sg\]](#2:1:6:sg){reference-type="ref" reference="2:1:6:sg"}) serve the same purpose as in the construction of gauge theories, i.e., they cancel analogous terms originating from the kinetic part of the quark Lagrangian. Note that the external currents are coupled with an "opposite" sign in comparison with our convention for gauge theories.

There is another, yet, more practical aspect of the local invariance, namely: such a procedure allows one to also discuss a coupling to external gauge fields in the transition to the effective theory to be discussed later. For example, a coupling of the electromagnetic field to point-like fundamental particles results from gauging a U(1) symmetry. Here, the corresponding U(1) group is to be understood as a subgroup of a local $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$. Another example deals with the interaction of the light quarks with the charged and neutral gauge bosons of the weak interactions.

Let us consider both examples explicitly. The coupling of quarks to an external electromagnetic field ${\cal A}_\mu$ is given by $$\label{2:1:6:rla}
r_\mu=l_\mu=-e Q {\cal A}_\mu,$$ where $Q=\mbox{diag}(2/3,-1/3,-1/3)$ is the quark charge matrix and $e>0$ the elementary charge: $${\cal L}_{\rm ext}=-e {\cal A}_\mu(\bar{q}_L Q\gamma^\mu q_L
+\bar{q}_R Q \gamma^\mu q_R)
=-e {\cal A}_\mu \bar{q}Q\gamma^\mu q
=-e {\cal A}_\mu\left(\frac{2}{3}\bar{u}\gamma^\mu u
-\frac{1}{3} \bar{d}\gamma^\mu d -\frac{1}{3}\bar{s}\gamma^\mu s\right).$$ On the other hand, if one considers only the two-flavor version of QCD one has to insert for the external fields $$\label{2:1:6:rlasu2}
r_\mu=l_\mu=-e\frac{\tau_3}{2}{\cal A}_\mu,\quad
v_\mu^{(s)}=-\frac{e}{2}{\cal A}_\mu.$$

In the description of semi-leptonic interactions such as $\pi^-\to \mu^-\bar{\nu}_\mu$, $\pi^-\to\pi^0e^-\bar{\nu}_e$, or neutron decay $n\to p e^-\bar{\nu}_e$ one needs the interaction of quarks with the massive charged weak bosons ${\cal W}^\pm_\mu=({\cal W}_{1\mu}\mp i {\cal W}_{2\mu})/\sqrt{2}$, $$\label{2:1:6:rlw} r_\mu=0,\quad l_\mu=-\frac{g}{\sqrt{2}} ({\cal W}^+_\mu T_+ +
\mbox{H.c.}),$$ where H.c. refers to the Hermitian conjugate and $$T_+=\left(\begin{array}{rrr}0&V_{ud}&V_{us}\\0&0&0\\0&0&0\end{array}\right).$$ Here, $V_{ij}$ denote the elements of the Cabibbo-Kobayashi-Maskawa quark-mixing matrix describing the transformation between the mass eigenstates of QCD and the weak eigenstates [@PDG_2008], $$|V_{ud}|=0.97418\pm 0.00027,\quad
|V_{us}|=0.2255\pm 0.0019.$$ At lowest order in perturbation theory, the Fermi constant is related to the gauge coupling $g$ and the $W$ mass as $$\label{2:1:6:GF}
G_F=\sqrt{2} \frac{g^2}{8 M^2_W}=1.16637(1)\times 10^{-5}\,\mbox{GeV}^{-2}.$$ Making use of $$\bar{q}_L\gamma^\mu {\cal W}_\mu^+ T_+ q_L
=\frac{1}{2}{\cal W}_\mu^+[V_{ud}\bar{u}\gamma^\mu(1-\gamma_5)d
+V_{us}\bar{u}\gamma^\mu(1-\gamma_5)s],$$ we see that inserting Eq. ([\[2:1:6:rlw\]](#2:1:6:rlw){reference-type="ref" reference="2:1:6:rlw"}) into Eq. ([\[2:1:6:lqcdsn\]](#2:1:6:lqcdsn){reference-type="ref" reference="2:1:6:lqcdsn"}) leads to the standard charged-current weak interaction in the light-quark sector, $$\begin{aligned}
{\cal L}_{\rm ext}&=&-\frac{g}{2\sqrt{2}}\left\{{\cal W}^+_\mu[
V_{ud}\bar{u}\gamma^\mu(1-\gamma_5)d+V_{us}\bar{u}\gamma^\mu(1-\gamma_5)s]
+\mbox{H.c.}\right\}.
\end{aligned}$$

The situation is slightly different for the neutral weak interaction. Here, the three-flavor version requires a coupling to the singlet axial-vector current which, because of the anomaly of Eq. ([\[2:1:5:dsva\]](#2:1:5:dsva){reference-type="ref" reference="2:1:5:dsva"}), we have dropped from our discussion. On the other hand, in the two-flavor version the axial-vector current part is traceless and we have $$\begin{aligned}
\label{2:1:6:rlz}
r_\mu&=&e \tan(\theta_W) \frac{\tau_3}{2} {\cal Z}_\mu,\nonumber\\
l_\mu&=&-\frac{g}{\cos(\theta_W)}\frac{\tau_3}{2} {\cal Z}_\mu+
e \tan(\theta_W) \frac{\tau_3}{2} {\cal Z}_\mu,
\nonumber\\
v_\mu^{(s)}&=&\frac{e\tan(\theta_W)}{2}{\cal Z}_\mu,
\end{aligned}$$ where $\theta_W$ is the weak angle. With these external fields, we obtain the standard weak neutral-current interaction $${\cal L}_{\rm ext}=-\frac{g}{2\cos(\theta_W)}{\cal Z}_\mu\left(
\bar{u}\gamma^\mu\left\{\left[\frac{1}{2}-\frac{4}{3}\sin^2(\theta_W)\right]{\mathbbm 1}
-\frac{1}{2}\gamma_5\right\}u+\bar{d}\gamma^\mu\left\{\left[-\frac{1}{2}
+\frac{2}{3}\sin^2(\theta_W)\right]{\mathbbm 1}
+\frac{1}{2}\gamma_5\right\}d\right),$$ where we made use of $e=g\sin(\theta_W)$.
