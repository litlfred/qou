---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-003-the-qcd-lagrangian
section_title: "The QCD Lagrangian"
section_number: null
pages: 4-6
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.914
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#sec_qcdl label="sec_qcdl"} The QCD Lagrangian can be obtained from the Lagrangian for free quarks by applying the gauge principle with respect to the group SU(3) of all unitary, unimodular, $3\times 3$ matrices. Denoting the quark field components by $q_{f,A,\alpha}$, where $f=1,\cdots, 6$ refers to the flavor index, $A=1,2,3$ to the color index, and $\alpha=1,\cdots,4$ to the Dirac spinor index, respectively, the "free" quark Lagrangian without interaction may be regarded as the sum of $6\times 3=18$ free fermion Lagrangians: $$\label{2:1:1:lfq}
{\cal L}_{\rm free\, quarks}
=\sum_{f=1}^6 \sum_{A=1}^3\sum_{\alpha,\alpha'=1}^4
\bar{q}_{f,A,\alpha}(\gamma^\mu_{\alpha\alpha'}i\partial_\mu
-m_f\delta_{\alpha\alpha'})q_{f,A,\alpha'}.$$ Suppressing the Dirac spinor index and introducing for each quark flavor $f$ a color triplet $$\label{2:1:1:qtriplet}
 q_f=\left(\begin{array}{c}q_{f,1}
\\q_{f,2}\\q_{f,3}\end{array}\right),$$ the gauge principle is applied with respect to the group SU(3), i.e., all $q_f$ are subject to the same local SU(3) transformation: $$\label{2:1:1:qtraf}
q_f\mapsto q_f'=\exp\left(-i\sum_{a=1}^8 \Theta_a
\frac{\lambda_a^c}{2}\right)q_f=U q_f,$$ where the eight $\lambda_a^c$ denote Gell-Mann matrices acting in color space and the $\Theta_a$ are smooth, real functions in Minkowski space. Whenever convenient, we will make use of the summation convention implying a summation over repeated indices. Introducing eight gauge potentials ${\cal A}_{a\mu}$, transforming as $$\label{2:1:1:atraf}
{\cal A}_\mu\equiv{\cal A}_{a\mu}\frac{\lambda_a^c}{2}\mapsto
{\cal A}_\mu'=
U{\cal A}_\mu U^\dagger +\frac{i}{g_3}\partial_\mu U U^\dagger,$$ the covariant derivative of the quark field, by construction, transforms as the quark field: $$\label{2:1:1:cdq}
D_\mu q_f \equiv (\partial_\mu
 +ig_3{\cal A}_\mu)q_f\mapsto
(D_\mu q_f)'=D'_\mu
q'_f=U D_\mu q_f.$$ In Eq. ([\[2:1:1:cdq\]](#2:1:1:cdq){reference-type="ref" reference="2:1:1:cdq"}), $g_3$ denotes the strong coupling constant. In order to treat the gauge potentials as dynamical degrees of freedom, one defines a generalization of the field strength tensor to the non-Abelian case as $$\label{2:1:1:gmunu}
{\cal G}_{a\mu\nu}=\partial_\mu {\cal A}_{a\nu}-\partial_\nu {\cal A}_{a\mu}
-g_3 f_{abc}{\cal A}_{b\mu} {\cal A}_{c\nu},$$ where, suppressing the superscript $c$ in the Gell-Mann matrices, the standard totally antisymmetric SU(3) structure constants are given by (see Table [1](#table:2:1:1:su3structurconstants){reference-type="ref" reference="table:2:1:1:su3structurconstants"}) $$\label{2:1:1:fabc}
f_{abc}=\frac{1}{4i}\mbox{Tr}([\lambda_a,\lambda_b]\lambda_c).$$

::: center
::: {#table:2:1:1:su3structurconstants}
        $abc$   123             147              156             246             257             345              367                     458                     678
  ----------- ----- --------------- ---------------- --------------- --------------- --------------- ---------------- ----------------------- -----------------------
    $f_{abc}$     1   $\frac{1}{2}$   $-\frac{1}{2}$   $\frac{1}{2}$   $\frac{1}{2}$   $\frac{1}{2}$   $-\frac{1}{2}$   $\frac{1}{2}\sqrt{3}$   $\frac{1}{2}\sqrt{3}$

  : Totally antisymmetric non-vanishing structure constants of SU(3): $[\frac{\lambda_a}{2},\frac{\lambda_b}{2}]=if_{abc}\frac{\lambda_c}{2}$.
:::
:::

Given Eq. ([\[2:1:1:atraf\]](#2:1:1:atraf){reference-type="ref" reference="2:1:1:atraf"}), the field strength tensor transforms under SU(3) as $$\label{2:1:1:gtrafo} {\cal G}_{\mu\nu}\equiv
{\cal G}_{a\mu\nu} \frac{\lambda_a^c}{2}\mapsto U{\cal G}_{\mu\nu}
U^\dagger.$$ The QCD Lagrangian obtained by applying the gauge principle to the free Lagrangian of Eq. ([\[2:1:1:lfq\]](#2:1:1:lfq){reference-type="ref" reference="2:1:1:lfq"}), finally, reads $$\label{2:1:1:lqcd} {\cal L}_{\rm QCD}=\sum_{f={u,d,s, \atop c,b,t}}
\bar{q}_f(i D\hspace{-.6em}/ -m_f)q_f -\frac{1}{4}{\cal
G}_{a\mu\nu}{\cal G}^{\mu\nu}_a.$$

From the point of view of gauge invariance the strong-interaction Lagrangian could also involve a term of the type $$\label{2:1:1:ltheta} {\cal
L}_\theta=\frac{g^2_3\bar{\theta}}{64\pi^2}\epsilon_{\mu\nu\rho\sigma}
{\cal G}_a^{\mu\nu}{\cal G}_a^{\rho\sigma},\quad \epsilon_{0123}=1,$$ where $\epsilon_{\mu\nu\rho\sigma}$ denotes the totally antisymmetric Levi-Civita tensor. The so-called $\theta$ term of Eq. ([\[2:1:1:ltheta\]](#2:1:1:ltheta){reference-type="ref" reference="2:1:1:ltheta"}) implies an explicit $P$ and $CP$ violation of the strong interactions which, for example, would give rise to an electric dipole moment of the neutron. The present empirical information indicates that the $\theta$ term is small and, in the following, we will omit Eq. ([\[2:1:1:ltheta\]](#2:1:1:ltheta){reference-type="ref" reference="2:1:1:ltheta"}) from our discussion.
