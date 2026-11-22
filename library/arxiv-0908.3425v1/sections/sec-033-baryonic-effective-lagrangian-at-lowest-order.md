---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-033-baryonic-effective-lagrangian-at-lowest-order
section_title: "Baryonic effective Lagrangian at lowest order"
section_number: null
pages: 50-52
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.996
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#sec_loebl label="sec_loebl"}

Given the dynamical fields of Eqs. ([\[4:1:1:su2real\]](#4:1:1:su2real){reference-type="ref" reference="4:1:1:su2real"}) and ([\[4:1:1:su3real\]](#4:1:1:su3real){reference-type="ref" reference="4:1:1:su3real"}) and their transformation properties, we will now discuss the most general effective baryonic Lagrangian at lowest order. We will start with the effective $\pi N$ Lagrangian ${\cal L}^{(1)}_{\pi N}$ which we demand to have a *local* $\mbox{SU}(2)_L\times\mbox{SU(2)}_R\times\mbox{U(1)}_V$ symmetry. The transformation behavior of the external fields is given in Eq. ([\[2:1:6:sg\]](#2:1:6:sg){reference-type="ref" reference="2:1:6:sg"}), whereas $U$ and the nucleon doublet transform as $$\label{4:1:2:psitrans}
\left(\begin{array}{c}U(x)\\ \Psi(x)\end{array}\right)\mapsto
\left(\begin{array}{c}V_R(x)U(x)V_L^\dagger(x)\\
\exp[-i\Theta(x)]K[V_L(x),V_R(x),U(x)]\Psi(x)\end{array}\right).$$ The local character of the transformation implies that we need to introduce a covariant derivative $D_\mu \Psi$ with the usual property that it transforms in the same way as $\Psi$, $$\label{4:1:2:kovder}
D_\mu\Psi=(\partial_\mu+\Gamma_\mu-iv_\mu^{(s)})\Psi,$$ where the so-called connection is given by $$\label{4:1:2:gamma}
\Gamma_\mu=\frac{1}{2}\left[u^\dagger(\partial_\mu-ir_\mu)u
+u(\partial_\mu-il_\mu)u^\dagger\right].$$ Since $K$ not only depends on $V_L$ and $V_R$ but also on $U$, the covariant derivative contains besides the external fields also $u$ and $u^\dagger$ and their derivatives. At ${\cal O}(q)$ there exists another Hermitian building block, the so-called vielbein, $$\label{4:1:2:chvi}
u_\mu\equiv i\left[u^\dagger(\partial_\mu-i r_\mu)u-u(\partial_\mu-i
l_\mu)u^\dagger\right],$$ which under parity transforms as an axial vector, $u_\mu\mapsto -u^\mu$, and under $\mbox{SU(2)}_L\times\mbox{SU(2)}_R\times \mbox{U}(1)_V$, transforms as $u_\mu \mapsto Ku_\mu K^\dagger$.

The structure of the most general effective $\pi N$ Lagrangian describing processes with a single nucleon in the initial and final states is of the type $\bar{\Psi} \widehat{O} \Psi$, where $\widehat{O}$ is an operator acting in Dirac and flavor space, transforming under $\mbox{SU(2)}_L\times\mbox{SU(2)}_R\times \mbox{U}(1)_V$ as $K\widehat{O}K^\dagger$. The Lagrangian must be a Hermitian Lorentz scalar which is even under the discrete symmetries $C$, $P$, and $T$. The most general such Lagrangian with the smallest number of derivatives is given by [@Gasser:1987rb] $$\label{4:1:2:l1pin}
{\cal L}^{(1)}_{\pi N}=\bar{\Psi}\left(iD\hspace{-.6em}/ -m
+\frac{\texttt{g}_A}{2}\gamma^\mu \gamma_5 u_\mu\right)\Psi.$$ It contains two parameters not determined by chiral symmetry: the chiral limit $m$ of the nucleon mass $m_N$ and the chiral limit $\texttt{g}_A$ of the axial-vector coupling constant $g_A$. The physical value of $g_A$ is determined from neutron beta decay and is given by $g_A=1.2695\pm 0.0029$. The overall normalization of the Lagrangian is chosen such that in the case of no external fields and no pion fields it reduces to that of a free nucleon of mass $m$.

Similarly as in the mesonic case, the Lagrangian ${\cal L}^{(1)}_{\pi N}$ has predictive power once the two parameters have been identified. For example, a tree-level calculation of pion-nucleon scattering produces the famous Weinberg-Tomozawa relation for the $s$-wave $\pi N$-scattering lengths [@Weinberg:1966kf], [@Tomozawa:1966jm], $$\label{5:3:weinbergtomozawa}
a^I=-\frac{M_\pi}{8\pi (1+\mu)F_\pi^2}\left[I(I+1)-\frac{3}{4}-2\right],$$ where $I=1/2$ or $I=3/2$ refers to the total isospin of the $\pi N$ system. As in $\pi\pi$ scattering, the $s$-wave $\pi N$-scattering lengths vanish in the chiral limit, i.e., Goldstone bosons interact "weakly" with other hadrons in the zero-energy and mass limit.

Since the nucleon mass $m_N$ does not vanish in the chiral limit, the zeroth component $\partial^0$ of the partial derivative acting on the nucleon field does not produce a "small" quantity. This results in new features of the chiral power counting in the baryonic sector. The counting of the external fields as well as of covariant derivatives acting on the mesonic fields remains the same as in mesonic chiral perturbation theory. On the other hand, the counting of bilinears $\bar{\Psi}\Gamma\Psi$ is probably easiest understood by investigating the matrix elements of positive-energy plane-wave solutions to the free Dirac equation in the Dirac representation: $$\psi^{(+)}(t,\vec{x}\,)=\exp(-ip\cdot x) \sqrt{E+m_N}\left(
\begin{array}{c}
\chi\\
\frac{\vec{\sigma}\cdot\vec{p}}{E+m_N}\chi
\end{array}
\right),$$ where $\chi$ denotes a two-component Pauli spinor and $p^\mu=(E,\vec{p})$ with $E=\sqrt{\vec{p}\,^2+m_N^2}$. In the low-energy limit, i.e., for non-relativistic kinematics, the lower (small) component is suppressed as $|\vec{p}\,|/m_N$ in comparison with the upper (large) component. For the analysis of the bi-linears it is convenient to divide the 16 Dirac matrices into even and odd ones, ${\cal E}=
\{{\mathbbm 1}, \gamma_0,\gamma_5 \gamma_i,\sigma_{ij}\}$ and ${\cal
O}=\{\gamma_5,\gamma_5 \gamma_0,\gamma_i,\sigma_{i0}\}$ [@Foldy:1949wa], respectively, where odd matrices couple large and small components but not large with large, whereas even matrices do the opposite. Finally, $i\partial^\mu$ acting on the nucleon solution produces $p^\mu$ which we write symbolically as $p^\mu=(m_N,\vec{0})+(E-m_N,\vec{p}\,)$, where we count the second term as ${\cal O}(q)$, i.e., as a small quantity. We are now in the position to summarize the chiral counting scheme for the (new) elements of baryon chiral perturbation theory [@Krause:1990xc]: $$\begin{aligned}
\label{4:1:2:powercounting}
&&\Psi,\bar{\Psi} =  {\cal O}(q^0),\, D_{\mu} \Psi = {\cal  O}(q^0),\,
(iD\hspace{-.6em}/ - m)\Psi={\cal O}(q),\nonumber\\
&&{\mathbbm 1},\gamma_\mu,\gamma_5\gamma_\mu,\sigma_{\mu\nu}={\cal O}(q^0),\,
\gamma_5 ={\cal O}(q),
\end{aligned}$$ where the order given is the minimal one. For example, $\gamma_\mu$ has both an ${\cal O}(q^0)$ piece, $\gamma_0$, as well as an ${\cal O}(q)$ piece, $\gamma_i$. Note that because of the additional spin degree of freedom the baryonic effective Lagrangian contains both odd and even chiral orders. A rigorous non-relativistic reduction may be achieved in the framework of the Foldy-Wouthuysen method [@Foldy:1949wa], [@Fearing:1993ii] or the heavy-baryon approach [@Jenkins:1990jv], [@Bernard:1992qa].

The construction of the $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$ Lagrangian proceeds similarly except for the fact that the baryon fields are contained in the $3\times 3$ matrix of Eq. ([\[4:1:1:su3oktett\]](#4:1:1:su3oktett){reference-type="ref" reference="4:1:1:su3oktett"}) transforming as $K B K^\dagger$. As in the mesonic sector, the building blocks are written as products transforming as $K\cdots K^\dagger$ with a trace taken at the end. The lowest-order Lagrangian reads [@Georgi], [@Krause:1990xc] $$\label{4:1:2:l1su3}
{\cal L}^{(1)}_{MB}=\mbox{Tr}\left[\bar{B}\left(iD\hspace{-.7em}/\hspace{.2em}
-M_0\right)B\right]
-\frac{D}{2}\mbox{Tr}\left(\bar{B}\gamma^\mu\gamma_5\{u_\mu,B\}\right)
-\frac{F}{2}\mbox{Tr}\left(\bar{B}\gamma^\mu\gamma_5[u_\mu,B]\right),$$ where $M_0$ denotes the mass of the baryon octet in the chiral limit. The covariant derivative of $B$ is defined as $$\label{4:1:2:kovderb}
D_\mu B=\partial_\mu B +[\Gamma_\mu,B],$$ with $\Gamma_\mu$ of Eq. ([\[4:1:2:gamma\]](#4:1:2:gamma){reference-type="ref" reference="4:1:2:gamma"}) \[for $\mbox{SU(3)}_L\times\mbox{
SU(3)}_R$\]. The constants $D$ and $F$ may be determined by fitting the semi-leptonic decays $B\to B'+e^-+\bar{\nu}_e$ at tree level [@Borasoy:1998pe]: $$\label{5:2:df}
D=0.80,\quad
F=0.50.$$
