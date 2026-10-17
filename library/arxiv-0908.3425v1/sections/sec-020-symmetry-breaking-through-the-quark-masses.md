---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-020-symmetry-breaking-through-the-quark-masses
section_title: "Symmetry breaking through the quark masses"
section_number: null
pages: 25-27
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.977
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
Up to now, we have assumed a perfect $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$ symmetry. As has been discussed in Section [\[subsec_csbdqm\]](#subsec_csbdqm){reference-type="ref" reference="subsec_csbdqm"}, the quark-mass term of QCD results in an explicit symmetry breaking, $$\label{3:2:2:qmt}
{\cal L}_{\cal M}=-\bar{q}_R{\cal M} q_L-\bar{q}_L {\cal M}^\dagger q_R,\quad
{\cal M}=\left(\begin{array}{ccc}m_u&0&0\\0&m_d&0\\0&0&m_s\end{array}\right).$$ In order to incorporate the consequences of Eq. ([\[3:2:2:qmt\]](#3:2:2:qmt){reference-type="ref" reference="3:2:2:qmt"}) into the effective-Lagrangian framework, one makes use of the following argument [@Georgi]: Although ${\cal M}$ is in reality just a constant matrix and does not transform along with the quark fields, ${\cal L}_{\cal M}$ of Eq. ([\[3:2:2:qmt\]](#3:2:2:qmt){reference-type="ref" reference="3:2:2:qmt"}) *would be* invariant *if* ${\cal M}$ transformed as $$\label{3:2:2:mgtrafo}
{\cal M}\mapsto R {\cal M} L^\dagger.$$ One then constructs the most general Lagrangian ${\cal L}(U,{\cal M})$ which is invariant under Eqs. ([\[3:1:2:utrfafo\]](#3:1:2:utrfafo){reference-type="ref" reference="3:1:2:utrfafo"}) and ([\[3:2:2:mgtrafo\]](#3:2:2:mgtrafo){reference-type="ref" reference="3:2:2:mgtrafo"}) and expands this function in powers of ${\cal M}$. At lowest order in ${\cal M}$ one obtains $$\label{3:2:2:lqm}
{\cal L}_{\rm s.b.}=\frac{F^2_0 B_0}{2}\mbox{Tr}({\cal M}U^\dagger+U{\cal M}^\dagger),$$ where the subscript s.b. refers to symmetry breaking. In order to interpret the new parameter $B_0$, let us consider the Hamiltonian density corresponding to the sum of the Lagrangians of Eq. ([\[3:2:1:l2\]](#3:2:1:l2){reference-type="ref" reference="3:2:1:l2"}) and ([\[3:2:2:lqm\]](#3:2:2:lqm){reference-type="ref" reference="3:2:2:lqm"}): $$\begin{aligned}
{\cal H}_{\rm eff}
&=&\frac{F_0^2}{4}\mbox{Tr}(\dot U \dot U^\dagger)
+\frac{F_0^2}{4}\mbox{Tr}(\vec{\nabla}U\cdot\vec{\nabla}U^\dagger)
-{\cal L}_{\rm s.b.}.
\end{aligned}$$ Since the first two terms are always larger or equal to zero, ${\cal H}_{\rm eff}$ is minimized by constant and uniform fields. Using the ansatz $$\phi=\phi_0+\frac{1}{F_0^2}\phi_2+\frac{1}{F_0^4}\phi_4+\cdots$$ for the minimizing field values and organizing the individual terms in powers of $1/F_0^2$, one finds $\phi=0$ as the classical solution even in the presence of quark-mass terms. Now consider the energy density of the ground state ($U_{\rm min}=U_0={\mathbbm 1}$), $$\label{2:2:3:Heff}
\langle{\cal H}_{\rm eff}\rangle_{\rm min}=-F_0^2 B_0(m_u+m_d+m_s),$$ and compare its derivative with respect to (any of) the light quark masses $m_q$ with the corresponding quantity in QCD, $$\left.\frac{\partial \langle 0|{\cal H}_{\rm QCD}|0\rangle}{\partial m_q}
\right|_{m_u=m_d=m_s=0}=\frac{1}{3}\langle 0|\bar{q}{q}|0\rangle_0
=\frac{1}{3}\langle \bar{q}q\rangle_0,$$ where $\langle\bar{q}{q}\rangle_0$ is the chiral quark condensate of Eq. ([\[2:2:3:cqc\]](#2:2:3:cqc){reference-type="ref" reference="2:2:3:cqc"}). Within the framework of the lowest-order effective Lagrangian, the constant $B_0$ is thus related to the chiral quark condensate as $$\label{3:2:2:b0}
3 F^2_0B_0=-\langle\bar{q}q\rangle_0.$$

Let us add a few remarks.

1.  A term $\mbox{Tr}({\cal M})$ by itself is not invariant.

2.  The combination $\mbox{Tr}({\cal M}U^\dagger-U {\cal M}^\dagger)$ has the wrong behavior under parity $\phi(t,\vec{x})\to-\phi(t,-\vec{x})$.

3.  Because ${\cal M}={\cal M}^\dagger$, ${\cal L}_{\rm s.b.}$ contains only terms even in $\phi$.

In order to determine the masses of the Goldstone bosons, we identify the terms of second order in the fields in ${\cal L}_{\rm s.b.}$, $$\label{3:2:2:lmzo}
{\cal L}_{\rm s.b}=-\frac{B_0}{2}\mbox{Tr}(\phi^2{\cal M}) +\cdots.$$ For the sake of simplicity we consider the isospin-symmetric limit $m_u=m_d=\hat m$ so that the $\pi^0\eta$ term vanishes and there is no $\pi^0$-$\eta$ mixing. The masses of the Goldstone bosons, to lowest order in the quark masses, are then given by $$\begin{aligned}
\label{3:2:2:mpi2}
M^2_\pi&=&2 B_0 \hat m,\\
\label{3:2:2:mk2}
M^2_K&=&B_0(\hat m+m_s),\\
\label{3:2:2:meta2}
M^2_\eta&=&\frac{2}{3} B_0\left(\hat m+2m_s\right).
\end{aligned}$$ These results, in combination with Eq. ([\[3:2:2:b0\]](#3:2:2:b0){reference-type="ref" reference="3:2:2:b0"}), $B_0=-\langle\bar{q}q\rangle_0/(3 F_0^2)$, correspond to relations obtained in Ref. [@Gell-Mann:rz:3] and are referred to as the Gell-Mann, Oakes, and Renner relations. Without additional input regarding the numerical value of $B_0$, Eqs. ([\[3:2:2:mpi2\]](#3:2:2:mpi2){reference-type="ref" reference="3:2:2:mpi2"}) - ([\[3:2:2:meta2\]](#3:2:2:meta2){reference-type="ref" reference="3:2:2:meta2"}) do not allow for an extraction of the absolute values of the quark masses $\hat m$ and $m_s$, because re-scaling $B_0\to \lambda B_0$ in combination with $m_q\to m_q/\lambda$ leaves the relations invariant. For the ratio of the quark masses one obtains, using the empirical values $M_\pi=135$ MeV, $M_K=496$ MeV, and $M_\eta=547$ MeV, $$\begin{aligned}
\frac{M^2_K}{M^2_\pi}=\frac{\hat m+m_s}{2\hat m}&\Rightarrow&\frac{m_s}{\hat m}=25.9,
\nonumber\\
\frac{M^2_\eta}{M^2_\pi}=\frac{2m_s+\hat m}{3\hat m}&\Rightarrow&\frac{m_s}{\hat m}=24.3.
\end{aligned}$$

Let us conclude this section with a remark on $\langle\bar{q}q\rangle_0$. A non-vanishing quark condensate in the chiral limit is a sufficient but not a necessary condition for a spontaneous chiral symmetry breaking. The effective Lagrangian term of Eq. ([\[3:2:2:lqm\]](#3:2:2:lqm){reference-type="ref" reference="3:2:2:lqm"}) not only results in a shift of the vacuum energy but also in finite Goldstone boson masses and both effects are proportional to the parameter $B_0$. We recall that it was a symmetry argument which excluded a term $\mbox{Tr}({\cal M})$ which, at leading order in ${\cal M}$, would decouple the vacuum energy shift from the Goldstone boson masses. The scenario underlying ${\cal L}_{\rm s.b.}$ of Eq. ([\[3:2:2:lqm\]](#3:2:2:lqm){reference-type="ref" reference="3:2:2:lqm"}) is similar to that of a Heisenberg ferromagnet which exhibits a spontaneous magnetization $\langle \vec{M}\rangle$, breaking the O(3) symmetry of the Heisenberg Hamiltonian down to O(2). In the present case the analogue of the order parameter $\langle \vec{M}\rangle$ is the quark condensate $\langle \bar{q} q\rangle_0$. In the case of the ferromagnet, the interaction with an external magnetic field $\vec{H}$ is given by $-\langle \vec{M}\rangle\cdot \vec{H}$, which corresponds to Eq. ([\[2:2:3:Heff\]](#2:2:3:Heff){reference-type="ref" reference="2:2:3:Heff"}), with the quark masses playing the role of the external field $\vec{H}$ (see Table [1](#3:2:2:table_analogy){reference-type="ref" reference="3:2:2:table_analogy"}).

::: center
::: {#3:2:2:table_analogy}
                                        Heisenberg ferromagnet                                                             QCD
  ---------------------------- ---------------------------------------- ----------------------------------------------------------------------------------------------------------
    Symmetry of Hamiltonian                      O(3)                                                      $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$
    Symmetry of $|0\rangle$                      O(2)                                                                $\mbox{SU(3)}_V$
    Vacuum expectation value           $\langle \vec{M}\rangle$                                                          $\langle
                                                                                                                   \bar{q} q\rangle_0$
   Explicit symmetry breaking          External magnetic field                                                         Quark masses
          Interaction           $-\langle \vec{M}\rangle\cdot \vec{H}$                                                $\langle{\cal
                                                                         H}_{\rm eff}\rangle$ of Eq. ([\[2:2:3:Heff\]](#2:2:3:Heff){reference-type="ref" reference="2:2:3:Heff"})

  : Comparison between the symmetry-breaking patterns of a Heisenberg ferromagnet and QCD.
:::
:::

However, in principle, it is also possible that $B_0$ vanishes or is rather small. In such a case the quadratic masses of the Goldstone bosons might be dominated by terms which are nonlinear in the quark masses, i.e., by higher-order terms in the expansion of ${\cal L}(U,{\cal M})$. Such a scenario is the origin of the so-called generalized chiral perturbation theory [@Knecht:1995tr:3]. The analogue would be an antiferromagnet which shows a spontaneous symmetry breaking but with $\langle \vec{M}\rangle=0$. The analysis of the $s$-wave $\pi\pi$-scattering lengths [@Colangelo:2000jc], [@Colangelo:2001sp] supports the conjecture that the quark condensate is indeed the leading order parameter of the spontaneously broken chiral symmetry (see also Sec. [\[subsubsection_pion_decay_pipi_scattering\]](#subsubsection_pion_decay_pipi_scattering){reference-type="ref" reference="subsubsection_pion_decay_pipi_scattering"}).
