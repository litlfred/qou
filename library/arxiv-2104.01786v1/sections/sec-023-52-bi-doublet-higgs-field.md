---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-023-52-bi-doublet-higgs-field
section_title: "Bi-doublet Higgs field"
section_number: 5.2
pages: 18-19
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.986
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a single real"
---
Most (but not all, see below) versions of the left/right symmetric model require a Higgs field in the bi-doublet representation $$\begin{aligned}
\label{Phi}
\Phi = (1,2,2,0), \qquad \Phi \to U_L \Phi U_R^\dagger.
\end{aligned}$$ Out of the components of $\Phi^*$ of the complex conjugate matrix one can construct another matrix $$\begin{aligned}
\label{epsilon}
\tilde{\Phi} = \epsilon \Phi^* \epsilon^T, \qquad \epsilon:=\left( \begin{array}{cc} 0 & 1 \\ -1 & 0\end{array}\right)
\end{aligned}$$ that has the same transformation properties $\tilde{\Phi}\to U_L \tilde{\Phi} U_R^\dagger$ as $\Phi$. The VEV of this Higgs field $$\begin{aligned}
\label{Phi-vev}
\Phi =\left( \begin{array}{cc} v_1 & 0 \\ 0 & v_2 \end{array}\right), \qquad
\tilde{\Phi} =\left( \begin{array}{cc} v^*_2 & 0 \\ 0 & v^*_1 \end{array}\right)
\end{aligned}$$ breaks the symmetry down to the diagonal ${\rm U}(1)\subset{\rm SU}(2)_L\times{\rm SU}(2)_R$. The ${\rm U}(1)_{B-L}$ remains unbroken. To break the remaining symmetries to the electromagnetic ${\rm U}(1)$ one needs to introduce further Higgs fields, see below.

It is very convenient to have the Higgs field $\Phi$ because it allows construction of Yukawa mass terms. The $G_{\rm LR}$ invariant (lepton) mass term that can be constructed from $\Phi,\tilde{\Phi}$ is $$\begin{aligned}
\label{Phi-Y}
Y_L L^T \epsilon^T \Phi \bar{L} + \tilde{Y}_L L^T \epsilon^T \tilde{\Phi} \bar{L},
\end{aligned}$$ where $Y_L,\tilde{Y}_L$ are mass parameters (matrices in the case there is more than one generation). Evaluating these terms on the VEV's of $\Phi,\tilde{\Phi}$ we get $$\begin{aligned}
(Y_L v_1 +\tilde{Y}_L v_2^*) e\bar{e} + (Y_L v_2 +\tilde{Y}_L v_1^*) \nu\bar{\nu},
\end{aligned}$$ which are the Dirac mass terms for the electron and the neutrino. Note that it is sufficient to take $v_1\not=0, v_2=0$ to obtain the Dirac masses.
