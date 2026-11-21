---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-007-quark-masses-and-chiral-symmetry-breaking
section_title: "Quark masses and chiral symmetry breaking"
section_number: null
pages: 8-9
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.979
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#subsec_csbdqm label="subsec_csbdqm"} So far, we have discussed an idealized world with massless light quarks. The finite $u$-, $d$-, and $s$-quark masses explicitly break the chiral symmetry and generate divergences of the symmetry currents. As a consequence, the charge operators are, in general, no longer time independent. However, as first pointed out by Gell-Mann [@Gell-Mann:xb:3:5], the equal-time commutation relations still play an important role even if the symmetry is explicitly broken.

Defining the quark-mass matrix as $${\cal M}=\mbox{diag}(m_u,m_d,m_s),$$ the quark-mass term in the QCD Lagrangian leads to a mixing of left- and right-handed fields \[see Eq. ([\[2:1:2:qgq\]](#2:1:2:qgq){reference-type="ref" reference="2:1:2:qgq"})\], $$\label{2:1:5:lm} {\cal L}_{\cal M}= -\bar{q}{\cal M}q= -(\bar{q}_R
{\cal M} q_L +\bar{q}_L {\cal M} q_R).$$ Inserting the transformations of Eqs. ([\[2:1:3:u3lu3r\]](#2:1:3:u3lu3r){reference-type="ref" reference="2:1:3:u3lu3r"}) into the quark-mass term of Eq. ([\[2:1:5:lm\]](#2:1:5:lm){reference-type="ref" reference="2:1:5:lm"}) results in the variation $\delta{\cal L}_{\cal M}$, from which one obtains for the divergences $$\begin{aligned}
\label{2:1:5:dslr}
\partial_\mu L^{\mu}_a&=&\frac{\partial \delta {\cal L}_{\cal M}}{\partial \epsilon^L_a}
=-i\left(\bar{q}_L\frac{\lambda_a}{2}{\cal M} q_R -\bar{q}_R {\cal
M} \frac{\lambda_a}{2}
q_L\right),\nonumber\\
\partial_\mu L^{\mu}&=&\frac{\partial \delta {\cal L}_{\cal M}}{\partial \epsilon^L}
=-i\left(\bar{q}_L {\cal M} q_R -\bar{q}_R {\cal M} q_L\right).
\end{aligned}$$ The analogous expressions for $\partial_\mu R^{\mu}_a$ and $\partial_\mu R^{\mu}$ are obtained from Eqs. ([\[2:1:5:dslr\]](#2:1:5:dslr){reference-type="ref" reference="2:1:5:dslr"}) through the substitution $R\leftrightarrow L$. The divergences are proportional to the mass parameters which is the origin of the expression current-quark mass. In terms of the vector and axial-vector currents the divergences read $$\begin{aligned}
\label{2:1:5:dsva}
\partial_\mu V^{\mu}_a&=&
i\bar{q}[{\cal M},\frac{\lambda_a}{2}]q,\nonumber\\
\partial_\mu A^{\mu}_a&=&
i\bar{q}\{{\cal M},\frac{\lambda_a}{2}\}\gamma_5q,\nonumber\\
\partial_\mu V^\mu&=&0,\nonumber\\
\partial_\mu A^\mu&=&2i\bar{q}{\cal M}\gamma_5 q+
\frac{3 g^2_3}{32\pi^2}\epsilon_{\mu\nu\rho\sigma} {\cal G}^{\mu\nu}_a
{\cal G}^{\rho\sigma}_a,\quad \epsilon_{0123}=1.
\end{aligned}$$

We are now in the position to summarize the various (approximate) symmetries of the strong interactions in combination with the corresponding currents and their divergences.

-   In the limit of massless quarks, the sixteen currents $L^\mu_a$ and $R^\mu_a$ or, alternatively, $V^\mu_a$ and $A^\mu_a$ are conserved. The same is true for the singlet vector current $V^\mu$, whereas the singlet axial-vector current $A^\mu$ has an anomaly.

-   For any value of quark masses, the individual flavor currents $\bar{u}\gamma^\mu u$, $\bar{d}\gamma^\mu d$, and $\bar{s}\gamma^\mu s$ are always conserved in the strong interactions reflecting the flavor independence of the strong coupling and the diagonality of the quark-mass matrix. Of course, the singlet vector current $V^\mu$, being the sum of the three flavor currents, is always conserved.

-   In addition to the anomaly, the singlet axial-vector current has an explicit divergence due to the quark masses.

-   For equal quark masses, $m_u=m_d=m_s$, the eight vector currents $V^\mu_a$ are conserved, because $[\lambda_a,{\mathbbm 1}]=0$. Such a scenario is the origin of the SU(3) symmetry originally proposed by Gell-Mann and Ne'eman [@EightfoldWay:3:6]. The eight axial-vector currents $A^\mu_a$ are not conserved. The divergences of the octet axial-vector currents of Eq. ([\[2:1:5:dsva\]](#2:1:5:dsva){reference-type="ref" reference="2:1:5:dsva"}) are proportional to pseudoscalar quadratic forms. This can be interpreted as the microscopic origin of the PCAC relation (partially conserved axial-vector current) [@Gell-Mann:1964tf:3:6], [@Adler:1968:3:6] which states that the divergences of the axial-vector currents are proportional to renormalized field operators representing the lowest-lying pseudoscalar octet.

-   Taking $m_u=m_d\neq m_s$ reduces SU(3) flavor symmetry to SU(2) isospin symmetry.

-   Taking $m_u\neq m_d$ leads to isospin symmetry breaking.

-   Various symmetry-breaking patterns are discussed in great detail in Ref. [@Pagels:1974se].
