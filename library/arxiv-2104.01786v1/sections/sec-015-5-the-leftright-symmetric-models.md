---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-015-5-the-leftright-symmetric-models
section_title: "The left/right symmetric models"
section_number: 5
pages: 18-19
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a sin gle real"
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.979
---
[]{#sec:left-right label="sec:left-right"}

We now interrupt our representation theoretic discussion to review the left/right symmetric extensions of the SM, as these are most closely related to our formalism. We follow [@DiLuzio:2011mda], see in particular Section 1.3.1.

## Spinor fields

It is convenient to organise the fermionic fields into the following multiplets $$\begin{aligned}
\label{fermions}
Q^i = \left( \begin{array}{c} u^i \\ d^i \end{array}\right), \quad
L = \left( \begin{array}{c} \nu \\ e \end{array}\right), \quad
\bar{Q}^i = \left( \begin{array}{ccc} \bar{d}^i \\ -\bar{u}^i \end{array}\right), \quad
\bar{L} = \left( \begin{array}{c} \bar{e} \\ -\bar{\nu} \end{array}\right).
\end{aligned}$$ These fields transform under the left/right-symmetric gauge group $$\begin{aligned}
\label{GLR}
G_{\rm LR}={\rm SU}(3)\times{\rm SU}(2)_L\times{\rm SU}(2)_R\times {\rm U}(1)_{B-L}
\end{aligned}$$ in the following representations $$\begin{aligned}
\label{charges}
Q = (3,2,1,+\frac{1}{3}), \quad L= (1,2,1,-1), \quad \bar{Q}=(\bar{3}, 1, 2, -\frac{1}{3}), \quad \bar{L}= (1,1,2,+1).
\end{aligned}$$ Specifically, the transformation properties under ${\rm SU}(2)_L\times{\rm SU}(2)_R$ are $$\begin{aligned}
Q\to U_L Q, \quad L\to U_L L, \quad \bar{Q} \to U_R \bar{Q}, \quad \bar{L}\to U_R \bar{L}.
\end{aligned}$$

## Bi-doublet Higgs field

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
