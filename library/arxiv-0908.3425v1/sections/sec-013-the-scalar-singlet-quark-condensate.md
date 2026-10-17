---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-013-the-scalar-singlet-quark-condensate
section_title: "The scalar singlet quark condensate"
section_number: null
pages: 19-21
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.963
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#subsec_sqc label="subsec_sqc"} In the following, we will show that a non-vanishing scalar singlet quark condensate in the chiral limit is a sufficient (but not a necessary) condition for a spontaneous symmetry breaking in QCD. In this section all physical quantities such as the ground state, the quark operators etc. are considered in the chiral limit.

Let us first recall the definition of the nine scalar and pseudoscalar quark densities: $$\begin{aligned}
\label{2:2:3:sqd}
S_a(y)&=&\bar{q}(y)\lambda_a q(y),
\quad a=0,\cdots,8,\\
\label{4:1:psqd} P_a(y)&=&i\bar{q}(y)\gamma_5\lambda_a  q(y),
\quad a=0,\cdots,8,
\end{aligned}$$ where $\lambda_0=\sqrt{2/3}\,\mathbbm 1$. We need the equal-time commutation relation of two quark operators of the form $A_i(x)=q^\dagger(x)\hat{A}_i q(x)$, where $\hat{A}_i$ symbolically denotes Dirac and flavor matrices and a summation over color indices is implied: $$\label{2:2:3:comrel}
[A_1(t,\vec{x}),A_2(t,\vec{y})]=\delta^3(\vec{x}-\vec{y})
q^\dagger(x)[\hat{A}_1,\hat{A}_2]q(x).$$ With the definition $$Q_{aV}(t)=\int \mbox{d}^3 x q^\dagger(t,\vec{x}) \frac{\lambda_a}{2} q(t,\vec{x}),$$ and using $$=0,\quad
{[}\frac{\lambda_a}{2},\gamma_0\lambda_b]=
\gamma_0 i f_{abc} \lambda_c,$$ we see, after integration of Eq. ([\[2:2:3:comrel\]](#2:2:3:comrel){reference-type="ref" reference="2:2:3:comrel"}) over $\vec{x}$, that the scalar quark densities of Eq. ([\[2:2:3:sqd\]](#2:2:3:sqd){reference-type="ref" reference="2:2:3:sqd"}) transform under $\mbox{SU(3)}_V$ as a singlet and as an octet, respectively, $$\begin{aligned}
\label{2:2:3:sitr}
[Q_{aV}(t),S_0(y)]&=&0,\quad a=1,\cdots,8,\\
\label{2:2:3:octr}
{[Q_{aV}(t),S_b(y)]}&=&i\sum_{c=1}^8f_{abc}S_c(y),
\quad a,b=1,\cdots,8,
\end{aligned}$$ with analogous results for the pseudoscalar quark densities. Using the relation $$\sum_{a,b=1}^8 f_{abc}f_{abd}=3\delta_{cd}$$ for the structure constants of SU(3), we re-express the octet components of the scalar quark densities as $$\label{2:2:3:soktett}
S_a(y)=-\frac{i}{3}\sum_{b,c=1}^8f_{abc}[Q_{bV}(t),S_c(y)].$$

In the chiral limit the ground state is necessarily invariant under $\mbox{SU(3)}_V$ [@Vafa:1983tf], i.e., $Q_{aV}|0\rangle=0$, and we obtain from Eq. ([\[2:2:3:soktett\]](#2:2:3:soktett){reference-type="ref" reference="2:2:3:soktett"}) $$\label{2:2:3:saun}
\langle 0|S_a(y)|0\rangle
=\langle 0|S_a(0)|0\rangle
\equiv\langle S_a\rangle =0,\quad a=1,\cdots,8,$$ where we made use of translational invariance of the ground state. As an intermediate result we see that the octet components of the scalar quark condensate *must* vanish in the chiral limit. From Eq. ([\[2:2:3:saun\]](#2:2:3:saun){reference-type="ref" reference="2:2:3:saun"}), we obtain for $a=3$ $$\langle\bar{u}u\rangle-\langle\bar{d}d\rangle=0,$$ i.e. $\langle\bar{u}u\rangle=\langle\bar{d}d\rangle$ and for $a=8$ $$\langle\bar{u}u\rangle+\langle\bar{d}d\rangle
-2\langle\bar{s}s\rangle=0,$$ i.e. $\langle\bar{u}u\rangle=\langle\bar{d}d\rangle=
\langle\bar{s}s\rangle$.

Because of Eq. ([\[2:2:3:sitr\]](#2:2:3:sitr){reference-type="ref" reference="2:2:3:sitr"}) a similar argument cannot be used for the singlet condensate, and if we assume a non-vanishing singlet scalar quark condensate in the chiral limit, we find using $\langle\bar{u}u\rangle=\langle\bar{d}d\rangle=
\langle\bar{s}s\rangle$: $$\label{2:2:3:cqc}
0\neq \langle \bar{q}q\rangle
=\langle\bar{u}u+\bar{d}d+\bar{s}s\rangle
=3\langle\bar{u}u\rangle =
3\langle\bar{d}d\rangle
=3\langle \bar{s}s\rangle.$$ Finally, we make use of (no summation implied!) $$(i)^2 [\gamma_5 \frac{\lambda_a}{2},\gamma_0\gamma_5\lambda_a]
=\lambda^2_a\gamma_0$$ in combination with $$\lambda_1^2=\lambda_2^2=\lambda_3^2=
\left(
\begin{array}{rrr}
1&0&0\\
0&1&0\\
0&0&0
\end{array}
\right),\,\,
\lambda_4^2=\lambda_5^2=
\left(
\begin{array}{rrr}
1&0&0\\
0&0&0\\
0&0&1
\end{array}
\right),\,\,
\lambda_6^2=\lambda_7^2=
\left(
\begin{array}{rrr}
0&0&0\\
0&1&0\\
0&0&1
\end{array}
\right),\,\,
\lambda_8^2=
\frac{1}{3}
\left(
\begin{array}{rrr}
1&0&0\\
0&1&0\\
0&0&4
\end{array}
\right)$$ to obtain $$\label{2:2:3:crqapsqd}
i[Q_{aA}(t), P_a(y)]
=
\left \{\begin{array}{cl}
\bar{u}u+\bar{d}d, & a=1,2,3\\
\bar{u}u+\bar{s}s, & a=4,5\\
\bar{d}d+\bar{s}s, & a=6,7\\
\frac{1}{3}(\bar{u}u+\bar{d}d+4\bar{s}s), & a=8
\end{array}
\right.$$ where we have suppressed the $y$ dependence on the right-hand side. We evaluate Eq. ([\[2:2:3:crqapsqd\]](#2:2:3:crqapsqd){reference-type="ref" reference="2:2:3:crqapsqd"}) for a ground state which is invariant under $\mbox{SU(3)}_V$, assuming a non-vanishing singlet scalar quark condensate, $$\label{2:2:3:crqc}
\langle 0|i[Q_{aA}(t),P_a(y)]|0\rangle
=\frac{2}{3}\langle\bar{q}q\rangle,\quad a=1,\cdots,8,$$ where, because of translational invariance, the right-hand side is independent of $y$. Inserting a complete set of states into the commutator of Eq. ([\[2:2:3:crqc\]](#2:2:3:crqc){reference-type="ref" reference="2:2:3:crqc"}) yields that both the pseudoscalar density $P_a(y)$ as well as the axial charge operators $Q_{aA}$ must have a non-vanishing matrix element between the vacuum and massless one-particle states $|\phi_b\rangle$. In particular, because of Lorentz covariance, the matrix element of the axial-vector current operator between the vacuum and these massless states, appropriately normalized, can be written as $$\label{2:2:3:acc}
\langle 0|A_a^\mu(0)|\phi_b(p)\rangle=ip^\mu F_0 \delta_{ab},$$ where $F_0\approx 93$ MeV denotes the "decay" constant of the Goldstone bosons in the chiral limit. From Eq. ([\[2:2:3:acc\]](#2:2:3:acc){reference-type="ref" reference="2:2:3:acc"}) we see that a non-zero value of $F_0$ is a necessary and sufficient criterion for spontaneous chiral symmetry breaking. On the other hand, because of Eq. ([\[2:2:3:crqc\]](#2:2:3:crqc){reference-type="ref" reference="2:2:3:crqc"}) a non-vanishing scalar quark condensate $\langle \bar{q}
q\rangle$ is a sufficient (but not a necessary) condition for a spontaneous symmetry breakdown in QCD.
