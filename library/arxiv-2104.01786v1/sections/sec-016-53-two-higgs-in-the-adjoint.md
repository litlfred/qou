---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-016-53-two-higgs-in-the-adjoint
section_title: "Two Higgs in the adjoint"
section_number: 5.3
pages: 19-20
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a sin gle real"
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 1.0
---
As we already said, the Higgs field $\Phi$ cannot break the ${\rm U}(1)_{B-L}$ symmetry. One thus needs additional Higgs fields. The option that currently seems preferred in the literature goes under the name of the minimal left/right symmetric model, see e.g. [@Maiezza:2016ybz]. It introduces two more Higgs fields in the adjoint of each ${\rm SU}(2)_{L,R}$. It also requires neutrinos to be Majorana particles, and provides a natural room for the seesaw mechanism. The adjoint Higgs fields are $(B-L)$ charged and transform in the following representations $$\begin{aligned}
\Delta_L = (1,3,1,+2), \quad \Delta_R=(1,1,3,+2),
\end{aligned}$$ with ${\rm SU}(2)_L\times{\rm SU}(2)_R$ transformation properties $$\begin{aligned}
\Delta_L\to U_L \Delta_L U_L^\dagger, \qquad \Delta_R\to U_R \Delta_R U_R^\dagger.
\end{aligned}$$ The required VEV's for these fields are $$\begin{aligned}
\Delta_{L,R} = \left(\begin{array}{cc} 0 & 0 \\ v_{L,R} & 0 \end{array}\right).
\end{aligned}$$ The field $\Delta_L$ leaves unbroken the diagonal subgroup in ${\rm U}(1)_L \times{\rm U}(1)_{B-L}$, analogously for $\Delta_R$. This means that there is a single electromagnetic ${\rm U}(1)_{EM}$ unbroken. The electric charge of all the fields is worked out via $$\begin{aligned}
Q= T^3_L + T^3_R + \frac{B-L}{2}.
\end{aligned}$$ Thus, the hypercharge $Y=T^3_R + (B-L)/2$.

The adjoint Higgs fields allow for the construction of Yukawa mass terms. The lepton sector mass terms that can be written using $\Delta_{L,R}$ are $$\begin{aligned}
Y_\Delta ( L^T \epsilon \Delta_L L + \bar{L}^T  \Delta^*_R \epsilon \bar{L}),
\end{aligned}$$ where $Y_\Delta$ is a mass parameter (a mass matrix in the case when there is more than one generation). This term is designed to be invariant under the discrete ${\mathbb Z}_2$ symmetry $$\begin{aligned}
L \leftrightarrow \bar{L}, \qquad \Delta_L \leftrightarrow \Delta_R^\dagger.
\end{aligned}$$ Evaluating everything on the VEV we get the following contribution to leptonic mass terms $$\begin{aligned}
 Y_\Delta(v_L \nu \nu + v_R^* \bar{\nu}\bar{\nu}).
\end{aligned}$$ These are the neutrino Majorana mass terms giving rise to the seesaw mechanism.

## Two Higgs fields in the fundamental

Another option is to add two Higgs fields in the fundamental representations of ${\rm SU}(2)_{L,R}$. This is the original left/right symmetric model studied in [@Senjanovic:1978ev]. But there is no natural realisation of the seesaw mechanism.

Let us introduce the two Higgs fields $\chi_{L,R}$ transforming as under $G_{\rm LR}$ as $$\begin{aligned}
\chi_L = (2,1,+1), \qquad \chi_R=(1,2,+1).
\end{aligned}$$ There exists a vacuum configuration in which $\Phi$ takes the form ([\[Phi-vev\]](#Phi-vev){reference-type="ref" reference="Phi-vev"}) and $$\begin{aligned}
\label{fund-H-vev}
\chi_L=\left( \begin{array}{c} v_L \\  0 \end{array}\right), \qquad \chi_R = \left( \begin{array}{c} 0 \\ v_R \end{array}\right).
\end{aligned}$$ Each one of these vacuum configurations breaks ${\rm SU}(2)_{L,R}\times {\rm U}(1)_{B-L}$ to a ${\rm U}(1)$ subgroup. If $v_R\gg v_L$ the left/right symmetry is spontaneously broken, and we get an explanation of why only the left sector manifests itself at low energies.

## A model with only fundamental Higgs fields

There is also a version of the model with Higgs in the fundamental representations that does not introduce the bi-fundamental Higgs $\Phi$, see e.g. [@Hall:2018let]. Indeed, the two VEV's ([\[fund-H-vev\]](#fund-H-vev){reference-type="ref" reference="fund-H-vev"}) are sufficient to break ${\rm SU}(2)_{L}\times{\rm SU}(2)_R\times {\rm U}(1)_{B-L}$ down to the electromagnetic ${\rm U}(1)_{EM}$. The drawback of this model is that it does not allow for Yukawa-type mass terms. However, such terms can be produced using higher dimensional operators with two copies of the Higgs, see [@Hall:2018let].
