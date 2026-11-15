---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-032-transformation-properties-of-the-fields
section_title: "Transformation properties of the fields"
section_number: null
pages: 49-50
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.992
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#sec_tpf label="sec_tpf"} Our aim is the most general description of the interaction of baryons with Goldstone bosons and external fields at low energies. For that purpose we not only need to specify the transformation behavior of the Goldstone bosons and external fields but also of the remaining dynamical fields entering the Lagrangian. Our discussion follows Refs. [@Georgi], [@Gasser:1987rb]. Consider the nucleon doublet and the octet of $\frac{1}{2}^+$ baryons (see Fig. [\[2:2:2:fig:baryon_octet\]](#2:2:2:fig:baryon_octet){reference-type="ref" reference="2:2:2:fig:baryon_octet"}), $$\begin{aligned}
\label{4:1:1:nucleondoublet}
\Psi&=&\left(\begin{array}{c}p\\n\end{array}\right),\\
\label{4:1:1:su3oktett}
B&=&\sum_{a=1}^8 \frac{B_a\lambda_a}{\sqrt{2}}=
\left(\begin{array}{ccc}
\frac{1}{\sqrt{2}}\Sigma^0+\frac{1}{\sqrt{6}}\Lambda&\Sigma^+&p\\
\Sigma^-&-\frac{1}{\sqrt{2}}\Sigma^0+\frac{1}{\sqrt{6}}\Lambda&n\\
\Xi^-&\Xi^0&-\frac{2}{\sqrt{6}}\Lambda
\end{array}\right).
\end{aligned}$$ Each entry of $\Psi$ and $B$, respectively, is a complex, four-component Dirac field. In contradistinction to the case of the Goldstone-boson matrix $\phi$ of Eq. ([\[3:1:2:phisu3\]](#3:1:2:phisu3){reference-type="ref" reference="3:1:2:phisu3"}), we have $B\neq B^\dagger$. The representation of the isospin group $\mbox{SU}(2)_V$ and the flavor group $\mbox{SU}(3)_V$ on $\{\Psi\}$ and $\{B\}$, respectively, is given by $$\begin{aligned}
\label{4:1:1:su2hom}
\Psi&\mapsto& V \Psi,\quad V\in \mbox{SU}(2)_V,\\
\label{4:1:1:su3hom}
B&\mapsto& V B V^\dagger,\quad V\in\mbox{SU}(3)_V,
\end{aligned}$$ i.e., $\Psi$ transforms under the fundamental representation of SU(2) and $B$ transforms under the adjoint representation of SU(3). Starting from Eqs. ([\[4:1:1:su2hom\]](#4:1:1:su2hom){reference-type="ref" reference="4:1:1:su2hom"}) and ([\[4:1:1:su3hom\]](#4:1:1:su3hom){reference-type="ref" reference="4:1:1:su3hom"}) we will discuss realizations of $\mbox{SU(2)}_L\times\mbox{SU(2)}_R$ and $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$ on $\{\Psi\}$ and $\{B\}$, respectively.

Let us begin with $G=\mbox{SU(2)}_L\times\mbox{SU(2)}_R$. Recall that the transformation of Eq. ([\[3:1:2:utrfafo\]](#3:1:2:utrfafo){reference-type="ref" reference="3:1:2:utrfafo"}), $$U\mapsto RUL^\dagger,$$ defines a nonlinear realization of $G$ on $\{U\}$. Introducing $u^2=U$, we define the SU(2)-valued function $K(L,R,U)$ by $$\label{4:1:1:kdef}
u\mapsto u'=\sqrt{RUL^\dagger}\equiv RuK^{-1}(L,R,U),\quad\mbox{i.e.,}\quad
K(L,R,U)=u'^{-1}Ru=\sqrt{RUL^\dagger}^{-1}R \sqrt{U}.$$ The transformation $$\label{4:1:1:su2real}
\varphi(g):\left(\begin{array}{c}U\\ \Psi\end{array}\right)\mapsto
\left(\begin{array}{c}U'\\ \Psi'\end{array}\right)
=\left(\begin{array}{c}RUL^\dagger\\K(L,R,U)\Psi\end{array}\right)$$ defines an operation of the group $G$ on the set $\{(U,\Psi)\}$. This is true, because (a) the identity of $G$ leaves any pair $(U,\Psi)$ invariant and (b) the transformation satisfies the homomorphism property $$\begin{aligned}
\varphi(g_1)\varphi(g_2)
\left(\begin{array}{c}U\\ \Psi\end{array}\right)&=&\varphi(g_1)
\left(\begin{array}{c}R_2UL_2^\dagger\\K(L_2,R_2,U)\Psi\end{array}\right)
=\left(\begin{array}{c}R_1R_2UL_2^\dagger L_1^\dagger\\
K(L_1,R_1,R_2UL_2^\dagger)K(L_2,R_2,U)\Psi
\end{array}\right)\\
&=&\left(\begin{array}{c}R_1 R_2U(L_1L_2)^\dagger\\
K(L_1L_2,R_1R_2,U)\Psi\end{array}\right)=\varphi(g_1g_2)\left(\begin{array}{c}U\\ \Psi\end{array}\right),
\end{aligned}$$ where we made use of $$K(L_1, R_1, R_2 U L_2^\dagger)K (L_2,R_2,U)
=K((L_1 L_2), (R_1 R_2),U).$$ Note that for a general group element $g=(L,R)\in G$ the transformation behavior of $\Psi$ depends on $U$. The exception to this rule is the case of an isospin transformation $R=L=V$, where, because of $U'=u'^2=VuV^\dagger VuV^\dagger=Vu^2V^\dagger=VUV^\dagger$, one has $u'=VuV^\dagger$. Comparing with Eq. ([\[4:1:1:kdef\]](#4:1:1:kdef){reference-type="ref" reference="4:1:1:kdef"}), we obtain $K^{-1}(V,V,U)=V^\dagger$ or $K(V,V,U)=V$. This is consistent with our starting point that $\Psi$ transforms linearly as an isospin doublet under the isospin subgroup $H=\mbox{SU(2)}_V$ of $G=\mbox{SU(2)}_L\times\mbox{SU(2)}_R$. Recall that the symmetry of the vacuum determines the multiplet structure of the spectrum [@Coleman:1966:1:1].

For $G=\mbox{SU(3)}_L\times \mbox{SU(3)}_R$ one uses $$\label{4:1:1:su3real}
\varphi(g):\left(\begin{array}{c}U\\ B\end{array}\right)\mapsto
\left(\begin{array}{c}U'\\ B'\end{array}\right)
=\left(\begin{array}{c}RUL^\dagger\\K(L,R,U)B K^\dagger(L,R,U)
\end{array}\right),$$ where $K$ is defined completely analogously to Eq. ([\[4:1:1:kdef\]](#4:1:1:kdef){reference-type="ref" reference="4:1:1:kdef"}) after inserting the corresponding SU(3) matrices.

The generalization to other multiplets is straightforward. One first specifies the transformation behavior under the subgroup $H$ in terms of $V$ and $V^\dagger$. In order to find the transformation behavior under $G$ one simply replaces $V\to K$ and $V^\dagger\to K^\dagger$.
