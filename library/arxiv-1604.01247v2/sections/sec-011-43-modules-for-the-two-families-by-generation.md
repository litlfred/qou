---
doc_id: arxiv-1604.01247v2
doc_title: "EXCEPTIONAL QUANTUM GEOMETRY"
section_id: sec-011-43-modules-for-the-two-families-by-generation
section_title: "Modules for the two families by generation"
section_number: 4.3
pages: 21-23
source_pdf: 1604.01247v2.pdf
source_sha256: 5a402405aadf5d54
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.989
doc_brief: "EXCEPTIONAL QUANTUM GEOMETRY — Based on an interpretation of the quark-lepton symmetry in terms of the unimodularity of the color group SU(3) and on the existence of 3 generations, we develop an"
---
As recalled in §3.1, there are two families by generation. In view of §4.2 it seems, at first sight, reasonable to take as $J^8_{3}$-module the product of two copies $J^u$ and $J^d$ of $J^8_3$ as module with the particle assignment $$J^u=\left ( \begin{array}{ccc}
 \alpha_1 & \nu_\tau+t & \bar\nu_\mu-c\\
 \bar\nu_\tau-t & \alpha_2 & \nu_e+u\\
 \nu_\mu+c & \bar\nu_e-u  &\alpha_3
 \end{array}
 \right)
 \label{Ju1}$$

$$J^d=\left ( \begin{array}{ccc}
 \beta_1 & \tau+b & \bar\mu-s\\
 \bar\tau-b & \beta_2 & e+d\\
 \mu+s & \bar e-d & \beta_3
 \end{array}
 \right)
 \label{Jd1}$$

or the representation ([\[cjl\]](#cjl){reference-type="ref" reference="cjl"})

$$J^u=\left( \begin{array}{ccc}
 \alpha_1 & \nu_\tau & \bar\nu_\mu\\
 \bar\nu_\tau & \alpha_2 & \nu_e\\
 \nu_\mu & \bar\nu_e & \alpha_3
 \end{array}
 \right)
 + (u,c,t)
 \label{Ju2}$$

$$J^d=\left( \begin{array}{ccc}
 \beta_1 & \tau & \bar\mu\\
 \bar\tau & \beta_2 & e\\
 \mu & \bar e & \beta_3
 \end{array}
 \right)
 + (d,s,b)
 \label{Jd2}$$ where we have identified the fundamental fermions with there internal spaces ($\mathbb C^3$ for the quarks and $\mathbb C$ for the leptons). The diagonals correspond then to new spin1/2 fermions with $\mathbb R$ as internal spaces. It is therefore natural to consider these particles $\alpha_k, \beta_k$ ($k\in\{1,2,3\}$) as described by Majorana spinors. The interest of this latter identifications is that the addition of such particles does not spoil the anomalies cancellation of the Standard Model. In this context the corresponding module over $C^\infty(M,J^8_3)$ would be the tensor product of the $C^\infty(M)$-module of Majorana spinor fields over spacetime by the above $J^8_3$-module.\

## Problem of the $U(1)\times SU(2)$-symmetry

Up to now the analysis deals only with the color symmetry $SU(3)$, its tentative connection with the quark-lepton symmetry and the 3 generations. This leads naturally to the above assignment of internal spaces for fundamental fermions (of §4.3) by ([\[Ju2\]](#Ju2){reference-type="ref" reference="Ju2"}) and ([\[Jd2\]](#Jd2){reference-type="ref" reference="Jd2"}) together with an action of $SU(3)\times SU(3)/\mathbb Z_3$ described in §4.2 by ([\[acg\]](#acg){reference-type="ref" reference="acg"}) where the first factor $SU(3)$ is the color group.\
However then, the description of the $U(1)\times SU(2)$-symmetry may become problematic. Either one can solve the problem by $\gamma_5$-combinatorics or one should work with a product of four factors $J^u_L, J^u_R, J^d_L, J^d_R$. But in this latter option the cancellation of anomalies could become a non-obvious task.

In view of the above framework, there is another natural way to explore which consists in adding over each spacetime point to the exceptional finite quantum space another finite quantum space in which the group $U(1)\times SU(2)$ is involved. That is to add to $J^8_3$ another finite-dimensional Euclidean Jordan algebra which admits $U(1)\times SU(2)$ as automorphism group preserving some additional structure (like $SU(3)\times SU(3)/\mathbb Z_3$ for $J^8_3$). There is such an algebra, namely the simple Euclidean Jordan algebra $$J^4_2={\cal H}_2(\mathbb H)=J \text{Spin} (5)$$ of the hermitian $2\times 2$-matrices with entries in the field of quaternions $\mathbb H$. Let us explain this.\
A quaternion $q$ can be viewed as two complexes $z_1$ and $z_2$ $$q=(z_1,z_2)=z_1+z_2 j
 \label{q2c}$$ and the subgroup of ${\mbox{Aut}}(\mathbb H)=SU(2)/\mathbb Z_2$ which is complex linear, i.e. which preserves the imaginary $i$, is the group $U(1)$ acting as $(z_1,z_2)\mapsto (z_1,e^{i\theta} z_2)$, that is $$z_1+z_2 j\mapsto z_1+e^{i\theta} z_2 j
 \label{U1H}$$ for $e^{i\theta}\in U(1)$. Thus $U(1)$ is the analog for $\mathbb H$ to $SU(3)$ for $\mathbb O$.\
Let now consider an element of $J^4_2$ written in terms of $q=z_1+z_2 j$ $$\left(
 \begin{array}{cc}
 \xi_1 & q\\
 \bar q & \xi_2
 \end{array}
 \right) =
 \left(
 \begin{array}{cc}
 \xi_1 & z_1+z_2j\\
 \bar z_1-z_2j & \xi_2
 \end{array}
 \right) =
 \left(
 \begin{array}{cc}
 \xi_1 & z_1\\
 \bar z_1 & \xi_2
 \end{array}
 \right )
 + z_2 \left(
 \begin{array}{cc}
 0 & j\\
 -j & 0
 \end{array}
 \right)$$ where $\xi_1,\xi_2\in \mathbb R$. Let $U\in SU(2)$ be an arbitrary unitary $2\times 2$ complex matrix of determinant 1. By using $jz=\bar z j$ for $z\in \mathbb C$ one gets $$U\left(
 \begin{array}{cc}
 0 & j\\
 -j & 0
 \end{array}
 \right)
 U^\ast=\left(
 \begin{array}{cc}
 0 & j\\
 -j & 0\end{array}
 \right)
 \label{jinv}$$ from which it follows that the action of $(e^{i\theta},U) \in U(1)\times SU(2)$ $$\left(
 \begin{array}{cc}
 \xi_1 & z_1\\
 \bar z_1 & \xi_2
 \end{array}
 \right) + z_2\left(
 \begin{array}{cc}
 0 & j\\
 -j & 0
 \end{array}
 \right)
 \mapsto U \left(
 \begin{array}{cc}
 \xi & z_1\\
 \bar z_1 & \xi_2
 \end{array}
 \right)
U^\ast +
 e^{i\theta}z_2 \left(
 \begin{array}{cc}
 0 & j\\
 -j & 0
 \end{array}
 \right)$$ is an automorphism of $J^4_2$ which preserves the representation of the quaternions occurring in the elements of $J^4_2$ as elements of $\mathbb C\oplus \mathbb C$. Furthermore any such an automorphism is of this form. Thus $U(1)$ is the analog for $J^4_2$ of the color $SU(3)$ for $J^8_3$ while $SU(2)$ is the analog for $J^4_2$ of the other $SU(3)$ for $J^8_3$ (with the action described by (4.4) in §4.2). Notice that the $SU(2)$-action is an action of $SU(2)/\mathbb Z_2=SO(3)$.\
It is too early to know whether the addition of the factor $J^4_2$ is relevant but if it occurs it is tempting to add the factor $J^2_1=\mathbb R$ since then we would have $$J=\oplus^3_{k=1} J^{2^k}_k
 \label{Jtent}$$ as finite-dimensional Euclidean Jordan algebra which looks like the semi-simple part of some more elaborated object. Notice that $J$ is the real Jordan algebra of hermitian elements of $$\mathbb C\oplus M_2(\mathbb H)\oplus M_3(\mathbb O)
 \label{MJ}$$ which is not associative in view of the occurrence of the last term $M_3(\mathbb O)$.
