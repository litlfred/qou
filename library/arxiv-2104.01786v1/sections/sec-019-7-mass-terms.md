---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-019-7-mass-terms
section_title: "Mass terms"
section_number: 7
pages: 22-23
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
text_source: latex
latex_prose_ratio: 0.651
latex_coverage_ratio: 0.946
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a sin gle real"
---
[]{#sec:mass label="sec:mass"}

We now put the formalism developed to some use. We search for a \"Higgs\" field that can break the ${\rm Spin}(11,3)$ symmetry, and also be used to write mass terms for the semi-spinor $S_+={\mathbb O}\otimes\tilde{{\mathbb O}}$. We thus need a field that lives in the tensor product of the representation $S_+$ with itself. We have the following decomposition of this tensor product $$\begin{eqnarray}
S_+\times S_+ = \Lambda^1 ({\mathbb R}^{11,3}) \oplus \Lambda^3 ({\mathbb R}^{11,3}) \oplus \Lambda^5 ({\mathbb R}^{11,3}) \oplus \Lambda^7_{sd} ({\mathbb R}^{11,3}).
\end{eqnarray}$$ Here $\Lambda^k ({\mathbb R}^{11,3})$ is the space of anti--symmetric tensors of rank $k$ in ${\mathbb R}^{11,3}$. The space of 7-forms is not an irreducible representation, but the space $\Lambda^7_{sd}$ of self-dual 7-forms is. The first factor in this sum is anti-symmetric, i.e. projection on it does not vanish only if we assume that the two $S_+$ factors anti-commute. The second term is symmetric. We are interested in the mass terms arising by projecting onto this representation. Thus, we are interested in the symmetric bilinear forms on $S_+$ that can be written as $$\begin{eqnarray}
C^{\mu\nu\rho} \langle\!\langle\Psi, \Gamma_\mu \Gamma_\nu \Gamma_\rho\Psi \rangle\!\rangle.
\end{eqnarray}$$

## Projection onto $\Lambda^3 {\mathbb R}^{11,3}$

Three copies of $\Gamma$-matrices can be inserted between two $S_+$ states and produce a ${\mathfrak so}(11,3)$ invariant expression. The different arising components are $$\begin{eqnarray}
\langle\!\langle\Psi, \Gamma_{x_1 x_2 x_3} \Psi \rangle\!\rangle= \langle\!\langle\Psi, L_{x_1} L_{x_2} L_{x_3} \otimes {\mathbb I}\Psi \rangle\!\rangle, 
\quad
\langle\!\langle\Psi, \Gamma_{y_1 y_2 y_3} \Psi \rangle\!\rangle= - \langle\!\langle\Psi, {\mathbb I}\otimes L_{y_1} L_{y_2} L_{y_3}  \Psi \rangle\!\rangle, 
\\ \nonumber
\langle\!\langle\Psi, \Gamma_{x_1 x_2 y_1} \Psi \rangle\!\rangle= \langle\!\langle\Psi, L_{x_1} L_{x_2}  \otimes  L_{y_1} \Psi \rangle\!\rangle, 
\quad
\langle\!\langle\Psi, \Gamma_{x_1 y_1 y_2} \Psi \rangle\!\rangle= - \langle\!\langle\Psi,   L_{x_1} \otimes L_{y_1} L_{y_2}  \Psi \rangle\!\rangle.
\end{eqnarray}$$ This means we have the following expression for the projection $S_+\times S_+ \to \Lambda^3 {\mathbb R}^{11,3}$ $$\begin{eqnarray}
\label{364-rep}
\langle\!\langle\Psi, \Gamma\Gamma\Gamma \Psi \rangle\!\rangle= \langle\!\langle\Psi, E^i E^j E^k \otimes {\mathbb I}\Psi \rangle\!\rangle e^{ijk} + \langle\!\langle\Psi, E^i E^j \otimes  \tilde{E}^k  \Psi \rangle\!\rangle e^{ij} \tilde{e}^k \\ \nonumber
-\langle\!\langle\Psi,   E^i \otimes \tilde{E}^j \tilde{E}^k  \Psi \rangle\!\rangle e^i \tilde{e}^j \tilde{e}^k 
-\langle\!\langle\Psi, {\mathbb I}\otimes \tilde{E}^i \tilde{E}^j \tilde{E}^k   \Psi \rangle\!\rangle\tilde{e}^i \tilde{e}^j \tilde{e}^k.
\end{eqnarray}$$

##  ${\rm SU}(3)\times{\rm U}(1)$ and Lorentz invariant pairing

We now select among the 364 terms in ([\[364-rep\]](#364-rep){reference-type="ref" reference="364-rep"}) those that are ${\rm SU}(3)$, ${\rm U}(1)_{EM}$ and Lorentz invariant.

We have the ${\rm SU}(3)$ invariant 3-forms in ${\mathbb R}^6\subset{\rm Im}({\mathbb O})$. These arise as the real and imaginary parts of an ${\rm SU}(3)$ invariant $(3,0)$ form $$\begin{eqnarray}
\Omega := ( e^1 - {\rm i\,}e^5)(e^2-{\rm i\,}e^6) (e^3-{\rm i\,}e^7).
\end{eqnarray}$$ Note, however, that $\Omega$ is a singlet with respect to ${\rm SU}(2)_L\times{\rm SU}(2)_R$, but transforms non-trivially under the ${\rm U}(1)_{B-L}$. This means that $\Omega$ is not a singlet with respect to ${\rm U}(1)_{EM}$, and cannot be used. There is then an ${\rm SU}(3)\times{\rm U}(1)_{B-L}$ invariant real 2-form $$\begin{eqnarray}
\omega = e^{15} + e^{26}+e^{37}.
\end{eqnarray}$$ The last building block we are allowed to use in the ${\mathbb R}^7$ factor is the 1-form $e^4$.

For objects in ${\rm Im}(\tilde{{\mathbb O}})$, we are only allowed to use the 1-, 2- and 3-forms built from $\tilde{e}^{1,2,3}$. These 1- and 2-forms transform as vectors under the weak ${\rm SU}(2)$, while the 3-form is invariant. We can use objects that transform non-trivially under the ${\rm SU}(2)$ because we do not intend to preserve this symmetry. In other words, objects that transform non-trivially under the ${\rm SU}(2)$ are components of a \"Higgs\" field that we know is present in the mass terms of the SM.

This leads us to consider the following \"mass\" quadratic form in $S_+$ $$\begin{eqnarray}
\label{mass}
\langle\!\langle\Psi, \Psi\rangle\!\rangle_M = m_1 \langle\!\langle\Psi, ( E^1 E^5 + E^2 E^6+E^3 E^7) E^4 \otimes {\mathbb I}\Psi \rangle\!\rangle
- m_2 \langle\!\langle\Psi, {\mathbb I}\otimes \tilde{E}^1 \tilde{E}^2 \tilde{E}^3 \Psi \rangle\!\rangle\\ \nonumber
+ \psi^i \langle\!\langle\Psi , ( E^1 E^5 + E^2 E^6+E^3 E^7) \otimes \tilde{E}^i \Psi \rangle\!\rangle
+ \frac{1}{2} \phi^i \epsilon^{ijk} \langle\!\langle\Psi, E^4 \otimes \tilde{E}^j \tilde{E}^k \Psi\rangle\!\rangle.
\end{eqnarray}$$ Here the indices $i,j,k$ run over the values $1,2,3$, and summation convention is implied. Here $\xi\in{\mathbb C}$ is a complex parameter, $m_{1,2}\in{\mathbb R}$ and $\phi^i,\psi^i$ are two real vectors.

## Evaluating the mass terms

We now evaluate ([\[mass\]](#mass){reference-type="ref" reference="mass"}) on the particle states. Every element of ${\mathbb O}$ splits into 8 different states $L,\bar{L}, Q_i,\bar{Q}_i$, and we have computed the relevant pairings in this basis in ([\[O-formulas-1\]](#O-formulas-1){reference-type="ref" reference="O-formulas-1"}), ([\[O-formulas-2\]](#O-formulas-2){reference-type="ref" reference="O-formulas-2"}), ([\[Ot-formulas-1\]](#Ot-formulas-1){reference-type="ref" reference="Ot-formulas-1"}), ([\[Ot-formulas-2\]](#Ot-formulas-2){reference-type="ref" reference="Ot-formulas-2"}).

Let us concentrate on the \"quark\" sector first. We get $$\begin{eqnarray}
\left( \begin{array}{cc} u & d \end{array}\right)  \left( \begin{array}{cc} 0 & 1 \\ -1 & 0 \end{array}\right)  \Phi_Q \left( \begin{array}{c} \bar{d} \\ -\bar{u} \end{array}\right) = Q^T \epsilon \Phi_Q \bar{Q} ,
\end{eqnarray}$$ where $$\begin{eqnarray}
\Phi_Q = \left((m_1+{\rm i\,}m_2){\mathbb I}+ (\phi^i -{\rm i\,}\psi^i) \sigma^i \right) ,
\end{eqnarray}$$ and $\sigma^i$ are the usual Pauli matrices. This should be compared with (the quark version of) ([\[Phi-Y\]](#Phi-Y){reference-type="ref" reference="Phi-Y"}).

For the lepton sector we get similarly $$\begin{eqnarray}
\left( \begin{array}{cc} \nu & e \end{array}\right)  \left( \begin{array}{cc} 0 & 1 \\ -1 & 0 \end{array}\right)  \Phi_L \left( \begin{array}{c} \bar{e} \\ -\bar{\nu} \end{array}\right) = L^T \epsilon \Phi_L \bar{L}  ,
\end{eqnarray}$$ where $$\begin{eqnarray}
\Phi_L =  \left((-3m_1+{\rm i\,}m_2){\mathbb I}+ (\phi^i +3{\rm i\,}\psi^i) \sigma^i \right) .
\end{eqnarray}$$ It is clear that we get a relation between the masses of quarks and leptons, as is typical in GUT, but the particular relation that arises does not seem to be of any phenomenological interest.

The main conclusion of the calculation performed is that the bi-doublet Higgs field $\Phi$ of the left/right symmetric version of the SM that appears in the Yukawa mass terms of this model (and thus contains the familiar Higgs field) can be identified with a general ${\rm SU}(3)\times{\rm U}(1)_{EM}$ and Lorentz invariant 3-form in ${\mathbb R}^{11,3}$. It is interesting that this 3-form Higgs field gives masses to both leptons and quarks, and breaks the symmetry between them. Note, however, that while the 3-form ([\[364-rep\]](#364-rep){reference-type="ref" reference="364-rep"}), with values of the parameters chosen to align with ([\[Phi-vev\]](#Phi-vev){reference-type="ref" reference="Phi-vev"}), breaks ${\rm Spin}(11,3)$ to the product of ${\rm SU}(3)\times{\rm U}(1)_{B-L}$ and the Lorentz groups, there is also the diagonal ${\rm U}(1)\subset{\rm SU}(2)_L\times{\rm SU}(2)_R$ that survives, similar to the left/right symmetric model. Thus, the 3-form Higgs field by itself is not sufficient to break ${\rm Spin}(11,3)$ to the product of the unbroken part of the SM gauge and Lorentz groups, as ${\rm U}(1)_{B-L}$ survives. As in the left/right symmetric model, other Higgs fields are required to complete the breaking.
