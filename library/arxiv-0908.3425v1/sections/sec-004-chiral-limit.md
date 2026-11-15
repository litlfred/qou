---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-004-chiral-limit
section_title: "Chiral limit"
section_number: null
pages: 6-7
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.992
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
The terminology chiral limit refers to massless quarks, resulting in an important additional global symmetry of the QCD Lagrangian which will be discussed in the following. We introduce the chirality matrix $\gamma_5=\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3=\gamma_5^\dagger$, $\{\gamma^\mu,\gamma_5\}=0$, $\gamma_5^2=\mathbbm 1$, and define the projection operators $$\label{2:1:2:prpl}
P_L=\frac{1}{2}({\mathbbm 1}-\gamma_5)=P_L^\dagger,\quad
P_R=\frac{1}{2}({\mathbbm 1}+\gamma_5)=P_R^\dagger.$$ These operators satisfy the completeness relation $P_L+P_R=\mathbbm 1$, are idempotent, $P_L^2=P_L$, $P_R^2=P_R$, and respect the orthogonality relations $P_L P_R=P_R P_L=0$. When applied to the solutions of the free massless Dirac equation, the operators $P_R$ and $P_L$ project to the positive and negative helicity eigenstates, hence the subscripts $R$ and $L$ for right-handed and left-handed, respectively.

Omitting color and flavor indices, we introduce left- and right-handed quark fields as $$\label{2:1:2:qlr}
q_L=P_L q\quad\mbox{and}\quad q_R=P_R q.$$ A quadratic form containing any of the 16 independent $4\times 4$ matrices $\{{\mathbbm 1},\gamma^\mu,\gamma_5,\gamma^\mu\gamma_5,\sigma^{\mu\nu}\}$ can be decomposed as $$\label{2:1:2:qgq}
\bar{q}\,\Gamma_i q=\left \{\begin{array}{lcl}
\bar{q}_L\Gamma_1 q_L+\bar{q}_R\Gamma_1 q_R&\mbox{for}&
\Gamma_1\in\{\gamma^\mu,\gamma^\mu\gamma_5\}\\
\bar{q}_R\Gamma_2 q_L +\bar{q}_L\Gamma_2 q_R&\mbox{for}& \Gamma_2
\in\{{\mathbbm 1},\gamma_5,\sigma^{\mu\nu}\}
\end{array}
\right.,$$ where $$\bar{q}_R=\bar{q}P_L\quad\mbox{and}\quad \bar{q}_L=\bar{q}P_R.$$ The validity of Eq. ([\[2:1:2:qgq\]](#2:1:2:qgq){reference-type="ref" reference="2:1:2:qgq"}) is general and does not refer to "massless" quark fields.

From a phenomenological point of view the $u$ and $d$ quarks and to a lesser extent also the $s$ quark have relatively small masses in comparison to a typical hadronic scale of the order of 1 GeV. On the other hand, we will neglect the three heavy quarks $c$, $b$, and $t$, because we will restrict ourselves to energies well below the production threshold of particles containing a heavy (anti-) quark. In the following, we will approximate the full QCD Lagrangian by its light-flavor version, and will consider the chiral limit for the three light quarks $u$, $d$, and $s$. To that end, we apply Eq. ([\[2:1:2:qgq\]](#2:1:2:qgq){reference-type="ref" reference="2:1:2:qgq"}) to the term containing the contraction of the covariant derivative with $\gamma^\mu$. This quadratic quark form decouples into the sum of two terms which connect only left-handed with left-handed and right-handed with right-handed quark fields. The QCD Lagrangian in the chiral limit can then be written as $$\label{2:1:2:lqcd0lr}
{\cal L}^0_{\rm QCD}=\sum_{l=u,d,s}
(\bar{q}_{R,l}iD\hspace{-.6em}/\hspace{.3em}q_{R,l}+\bar{q}_{L,l}iD
\hspace{-.6em}/\hspace{.3em}
q_{L,l})-\frac{1}{4}{\cal G}_{a\mu\nu} {\cal G}^{\mu\nu}_a.$$ Note that because of Eq. ([\[2:1:2:qgq\]](#2:1:2:qgq){reference-type="ref" reference="2:1:2:qgq"}) the quark-mass term generates a coupling between left- and right-handed quark fields.
