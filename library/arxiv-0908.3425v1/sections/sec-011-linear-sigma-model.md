---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-011-linear-sigma-model
section_title: "Linear sigma model"
section_number: null
pages: 16-17
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.9
latex_coverage_ratio: 1.0
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
Spontaneous symmetry breaking occurs if the ground state has a lower symmetry than the Hamiltonian. For example, in the linear sigma model [@Schwinger:1957em], [@Gell-Mann:1960np], the Lagrangian is constructed in terms of the O(4) multiplet $(\sigma,\pi_1,\pi_2,\pi_3)$, $$\label{2:2:1:lsm}
{\cal L}=\frac{1}{2}\left(\partial_\mu\sigma\partial^\mu\sigma+
\partial_\mu\vec\pi\cdot\partial^\mu\vec\pi\right)
-\frac{m^2}{2}(\sigma^2+\vec\pi^2)-\frac{\lambda}{4}(\sigma^2+\vec\pi^2)^2,$$ where $\lambda>0$. Under parity we assume $\sigma(t,\vec x)\mapsto \sigma(t,-\vec x)$ and $\pi_i(t,\vec x)\mapsto -\pi_i(t,-\vec x)$. The Lagrangian is invariant under the infinitesimal transformations $$\left(\begin{array}{c} \sigma\\ \pi_1 \\ \pi_2\\ \pi_3\end{array}\right)
\mapsto
\left(\begin{array}{c} \sigma'\\ \pi'_1\\ \pi'_2\\ \pi'_3\end{array}\right)
=\left({\mathbbm 1}-i\sum_{a=1}^6\epsilon_a T_a\right)
\left(\begin{array}{c} \sigma\\ \pi_1 \\ \pi_2\\ \pi_3\end{array}\right),$$ where the six $4\times 4$ matrices are given by $$\begin{aligned}
&&T_1=\left(\begin{array}{rrrr}0&0&0&0\\0&0&0&0\\0&0&0&-i\\0&0&i&0
\end{array}\right),\quad\,
T_2=\left(\begin{array}{rrrr}0&0&0&0\\0&0&0&i\\0&0&0&0\\0&-i&0&0
\end{array}\right),\quad\,
T_3=\left(\begin{array}{rrrr}0&0&0&0\\0&0&-i&0\\0&i&0&0\\0&0&0&0
\end{array}\right),\\
&&T_4=\left(\begin{array}{rrrr}0&-i&0&0\\i&0&0&0\\0&0&0&0\\0&0&0&0
\end{array}\right),\quad\,
T_5=\left(\begin{array}{rrrr}0&0&-i&0\\0&0&0&0\\i&0&0&0\\0&0&0&0
\end{array}\right),\quad\,
T_6=\left(\begin{array}{rrrr}0&0&0&-i\\0&0&0&0\\0&0&0&0\\i&0&0&0
\end{array}\right).
\end{aligned}$$ The linear combinations $R_i=(T_i+T_{i+3})/2$ and $L_i=(T_i-T_{i+3})/2$, $i=1,2,3$, satisfy the commutation relations corresponding to an SU(2)$\times$SU(2) Lie group. The multiplet $(\sigma,\pi_1,\pi_2,\pi_3)$ transforms according to the $(\frac{1}{2},\frac{1}{2})$ representation. By choosing $m^2<0$, the symmetry is realized in the Nambu-Goldstone mode [@Nambu:xd:1:1], [@Goldstone:eq:1:1]. Let us assume that the ground state is characterized by the vacuum expectation values $$\label{2:2:1:groundstate}
\langle \sigma\rangle = v\equiv -\sqrt{-\frac{m^2}{\lambda}},\quad \langle\pi_i\rangle=0.$$ Introducing $\sigma=v+\sigma'$, the Lagrangian reads $$\label{2:2:1:lsmp}
{\cal L}=\frac{1}{2}\left(\partial_\mu\sigma'\partial^\mu\sigma'+
\partial_\mu\vec\pi\cdot\partial^\mu\vec\pi\right)
+\frac{1}{2}(-2m^2)\sigma'^2
+\lambda v\sigma' (\pi_1^2+\pi_2^2+\pi_3^2+\sigma'^2)
+\frac{\lambda}{4}(\pi_1^2+\pi_2^2+\pi_3^2+\sigma'^2)^2-\frac{\lambda}{4}v^4.$$ The ground-state configuration is no longer invariant under the full group O(4). While the generators $T_1$, $T_2$, and $T_3$ annihilate the ground state of Eq. ([\[2:2:1:groundstate\]](#2:2:1:groundstate){reference-type="ref" reference="2:2:1:groundstate"}), the generators $T_4$, $T_5$, and $T_6$ do not. The model-independent feature of the above example is given by the fact that for each of the three generators $T_4$, $T_5$, and $T_6$ which do not annihilate the ground state one obtains a *massless* Goldstone boson. This is why Eq. ([\[2:2:1:lsmp\]](#2:2:1:lsmp){reference-type="ref" reference="2:2:1:lsmp"}) contains no mass terms for the pions. In fact, the number of Goldstone bosons is determined by the structure of the symmetry groups [@Goldstone:es:1:1]. Let $G$ denote the symmetry group of the Lagrangian with $n_G$ generators and the subgroup $H$ the symmetry group of the ground state with $n_H$ generators. For each generator which does not annihilate the vacuum one obtains a massless Goldstone boson, i.e., the total number of Goldstone bosons equals $n_G-n_H$.

The Lagrangians used in *motivating* the phenomenon of a spontaneous symmetry breakdown are typically constructed in such a fashion that the degeneracy of the ground states is built into the potential at the classical level (the prototype being the "Mexican hat" potential). As in the above case, it is then argued that an *elementary* Hermitian field of a multiplet transforming non-trivially under the symmetry group $G$ acquires a vacuum expectation value signaling a spontaneous symmetry breakdown. However, there also exist theories such as QCD where one cannot infer from inspection of the Lagrangian whether the theory exhibits spontaneous symmetry breaking. Rather, the criterion for spontaneous symmetry breaking is a non-vanishing vacuum expectation value of some Hermitian operator, not an elementary field, which emerges through the dynamics of the underlying theory. In particular, we will see that the quantities developing a vacuum expectation value may also be local Hermitian operators composed of more fundamental degrees of freedom of the theory.

While the model of Eq. ([\[2:2:1:lsm\]](#2:2:1:lsm){reference-type="ref" reference="2:2:1:lsm"}) is constructed to illustrate the concept of a spontaneous symmetry breaking, it is not fully understood theoretically why QCD should exhibit this phenomenon. We will first motivate why experimental input, the hadron spectrum of the "real" world, indicates that spontaneous symmetry breaking happens in QCD. Secondly, we will show that a non-vanishing singlet scalar quark condensate is a sufficient condition for a spontaneous symmetry breaking in QCD.
