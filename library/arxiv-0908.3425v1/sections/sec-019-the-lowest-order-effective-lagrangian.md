---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-019-the-lowest-order-effective-lagrangian
section_title: "The lowest-order effective Lagrangian"
section_number: null
pages: 24-25
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.98
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#sec_loel label="sec_loel"} In terms of the SU(3) matrix $U(x)$ of Eqs. ([\[3:1:2:upar\]](#3:1:2:upar){reference-type="ref" reference="3:1:2:upar"}) and ([\[3:1:2:phisu3\]](#3:1:2:phisu3){reference-type="ref" reference="3:1:2:phisu3"}) the most general, chirally invariant, effective Lagrangian with the minimal number of derivatives reads $$\label{3:2:1:l2}
{\cal L}_{\rm eff}
=\frac{F^2_0}{4}\mbox{Tr}\left(\partial_\mu U \partial^\mu U^\dagger
\right),$$ where $F_0\approx 93$ MeV is a free parameter which later on will be related to the pion decay $\pi^+\to\mu^+\nu_\mu$. Because of the trace property $\mbox{Tr}(AB)=\mbox{Tr}(BA)$, the Lagrangian is invariant under the *global*  $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$ transformation $U \mapsto R U L^\dagger$ of Eq. ([\[3:1:2:utrfafo\]](#3:1:2:utrfafo){reference-type="ref" reference="3:1:2:utrfafo"}). The global $\mbox{U(1)}_V$ invariance is trivially satisfied, because the Goldstone bosons have baryon number zero, thus transforming as $\phi\mapsto\phi$ under $\mbox{U(1)}_V$ which also implies $U \mapsto U$.

The substitution $\phi_a(t,\vec{x})\mapsto -\phi_a(t,\vec{x})$ or, equivalently, $U(t,\vec{x})\mapsto U^\dagger(t,\vec{x})$ provides a simple method of testing, whether an expression is of so-called even or odd *intrinsic* parity, i.e., even or odd in the number of Goldstone boson fields. For example, the Lagrangian of Eq. ([\[3:2:1:l2\]](#3:2:1:l2){reference-type="ref" reference="3:2:1:l2"}) is even. Since the Goldstone bosons of QCD are pseudoscalars, the true parity transformation is given by $\phi_a(t,\vec{x})\mapsto -\phi_a(t,-\vec{x})$ or, equivalently, $U(t,\vec{x})\mapsto U^\dagger(t,-\vec{x})$.

The purpose of the multiplicative constant $F^2_0/4$ in Eq. ([\[3:2:1:l2\]](#3:2:1:l2){reference-type="ref" reference="3:2:1:l2"}) is to generate the standard form of the kinetic term $\frac{1}{2}\partial_\mu \phi_a\partial^\mu \phi_a$, which can be seen by expanding the exponential $U={\mathbbm 1}+i\phi/F_0+\cdots$, $\partial_\mu U=i\partial_\mu\phi/F_0
+\cdots$, resulting in $${\cal L}_{\rm eff}=
\frac{F^2_0}{4}\mbox{Tr}\left[\frac{i\partial_\mu\phi}{F_0}
\left(-\frac{i\partial^\mu\phi}{F_0}\right)\right]+\cdots
=\frac{1}{4}\partial_\mu\phi_a\partial^\mu
\phi_b\mbox{Tr}(\lambda_a\lambda_b)+\cdots
=\frac{1}{2}\partial_\mu\phi_a\partial^\mu\phi_a +{\cal L}_{\rm int},$$ where we made use of $\mbox{Tr}(\lambda_a \lambda_b)=2\delta_{ab}$. Since there are no other terms containing only two fields, the eight fields $\phi_a$ indeed describe eight independent *massless* particles.

There are no other independent, chirally invariant terms containing only two derivatives. A term of the type $\mbox{Tr}[(\partial_\mu\partial^\mu U) U^\dagger]$ may be re-expressed as $$\mbox{Tr}[(\partial_\mu\partial^\mu U) U^\dagger]
=\partial_\mu[\mbox{Tr}(\partial^\mu U U^\dagger)]
-\mbox{Tr}(\partial^\mu U \partial_\mu U^\dagger),$$ i.e., up to a total derivative it is proportional to the Lagrangian of Eq. ([\[3:2:1:l2\]](#3:2:1:l2){reference-type="ref" reference="3:2:1:l2"}). However, in the present context, total derivatives do not have a dynamical significance, i.e. they leave the equations of motion unchanged and can thus be dropped. The product of two invariant traces is excluded at lowest order, because $\mbox{Tr}(\partial_\mu U U^\dagger)=0$.

Let us turn to the vector and axial-vector currents associated with the global $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$ symmetry of the effective Lagrangian of Eq. ([\[3:2:1:l2\]](#3:2:1:l2){reference-type="ref" reference="3:2:1:l2"}). To that end, we parameterize $$\begin{aligned}
\label{3:2:1:L}
L&=&{\mathbbm 1}-i\epsilon^L_a\frac{\lambda_a}{2},\\
\label{3:2:1:R}
R&=&{\mathbbm 1}-i\epsilon^R_a\frac{\lambda_a}{2}.
\end{aligned}$$ In order to construct $J^{\mu}_{aL}$, set $\epsilon^R_a=0$ and choose $\epsilon^L_a=\epsilon^L_a(x)$. Using $$\label{3:2:1:utrick}
U^\dagger U={\mathbbm 1}\quad\Rightarrow\quad\partial^\mu(U^\dagger U)=0\quad
\Rightarrow\quad \partial^\mu U^\dagger U=-U^\dagger \partial^\mu U,$$ the variation of the Lagrangian can be brought into the form $$\label{4:3:dll}
\delta{\cal L}_{\rm eff}=\frac{F^2_0}{4}i\partial_\mu \epsilon^L_a\mbox{Tr}\left(\lambda_a
\partial^\mu U^\dagger U\right).$$ Applying the method of Ref. [@Gell-Mann:1960np], we obtain for the left currents $$\label{3:2:1:jl}
J^\mu_{aL}=\frac{\partial \delta {\cal L}_{\rm eff}}{
\partial \partial_\mu \epsilon_a^L}
=i\frac{F^2_0}{4}\mbox{Tr}\left(\lambda_a \partial^\mu U^\dagger U\right),$$ and, completely analogously, choosing $\epsilon_a^L=0$ and $\epsilon_a^R=\epsilon_a^R(x)$, for the right currents $$\label{3:2:1:jr}
J^\mu_{aR}=\frac{\partial \delta {\cal L}_{\rm eff}
}{\partial \partial_\mu \epsilon^R_a}
=-i\frac{F^2_0}{4}\mbox{Tr}\left(\lambda_a U \partial^\mu U^\dagger\right).$$ Combining Eqs. ([\[3:2:1:jl\]](#3:2:1:jl){reference-type="ref" reference="3:2:1:jl"}) and ([\[3:2:1:jr\]](#3:2:1:jr){reference-type="ref" reference="3:2:1:jr"}) the vector and axial-vector currents read $$\begin{aligned}
\label{3:2:1:jv}
J^\mu_{aV}&=&J^\mu_{aR}+J^\mu_{aL}=-i\frac{F^2_0}{4}
\mbox{Tr}\left(\lambda_a[U,\partial^\mu U^\dagger]\right),\\
\label{3:2:1:ja}
J^\mu_{aA}&=&J^\mu_{aR}-J^\mu_{aL}=-i\frac{F^2_0}{4}
\mbox{Tr}\left(\lambda_a\{U,\partial^\mu U^\dagger\}\right).
\end{aligned}$$ Furthermore, because of the symmetry of ${\cal L}_{\rm eff}$ under $\mbox{SU(3)}_L\times\mbox{SU(3)}_R$, both vector and axial-vector currents are conserved. Using the substitution $U\leftrightarrow U^\dagger$ and Eq. ([\[3:2:1:utrick\]](#3:2:1:utrick){reference-type="ref" reference="3:2:1:utrick"}), the vector current densities $J^\mu_{aV}$ of Eq. ([\[3:2:1:jv\]](#3:2:1:jv){reference-type="ref" reference="3:2:1:jv"}) contain only terms with an even number of Goldstone bosons and the axial-vector current densities $J^\mu_{aA}$ of Eq. ([\[3:2:1:ja\]](#3:2:1:ja){reference-type="ref" reference="3:2:1:ja"}) only terms with an odd number of Goldstone bosons. To find the leading term let us expand Eq. ([\[3:2:1:ja\]](#3:2:1:ja){reference-type="ref" reference="3:2:1:ja"}) in the fields, $$J^\mu_{aA}=-i\frac{F^2_0}{4}\mbox{Tr}\left(\lambda_a\left\{{\mathbbm 1}+\cdots,
-i\frac{\lambda_b\partial^\mu \phi_b}{F_0}+\cdots\right\}\right)=
-F_0\partial^\mu\phi_a+\cdots.$$ We conclude that the axial-vector current has a non-vanishing matrix element when evaluated between the vacuum and a one-Goldstone boson state: $$\label{3:2:1:jamatrixelemtn}
\langle 0|J^\mu_{aA}(x)|\phi_b(p)\rangle
=\langle 0|-F_0\partial^\mu\phi_a(x)|\phi_b(p)\rangle
=-F_0\partial^\mu \exp(-ip\cdot x)\delta_{ab}
=ip^\mu F_0\exp(-ip\cdot x)\delta_{ab}.$$ Equation ([\[3:2:1:jamatrixelemtn\]](#3:2:1:jamatrixelemtn){reference-type="ref" reference="3:2:1:jamatrixelemtn"}) is the manifestation of Eq. ([\[2:2:3:acc\]](#2:2:3:acc){reference-type="ref" reference="2:2:3:acc"}) at lowest order in the effective field theory.
