---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-017-application-to-qcd
section_title: "Application to QCD"
section_number: null
pages: 22-25
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.993
---
[]{#subsec_aqcd label="subsec_aqcd"}

The symmetry groups relevant to the application in QCD are $$G=\mbox{SU($N$)}\times\mbox{SU($N$)}=\{(L,R)|
L\in \mbox{SU($N$)}, R\in
\mbox{SU($N$)}\}\,\,\mbox{and}\,\, H=\{(V,V)|V\in \mbox{SU($N$)}\}
\cong\mbox{SU($N$)}.$$ Let $\tilde{g}=(\tilde{L},\tilde{R})\in G$. We characterize the left coset $\tilde{g}H$ through the SU($N$) matrix $U=\tilde{R}\tilde{L}^\dagger$ [@Balachandran:zj:2:2] such that $\tilde{g}H=({\mathbbm 1},\tilde{R}\tilde{L}^\dagger)H$. This corresponds to the convention of choosing as the representative of the coset the element which has the unit matrix in its first argument. The transformation behavior of $U$ under $g=(L,R)\in G$ is obtained by multiplication in the left coset: $$g \tilde{g}H=(L, R\tilde{R}\tilde{L}^\dagger)H=
({\mathbbm 1},R\tilde{R}\tilde{L}^\dagger L^\dagger)(L,L)H=
({\mathbbm 1},R(\tilde{R}
\tilde{L}^\dagger)L^\dagger)H,$$ i.e. $$\label{3:1:2:utrafo}
U=\tilde{R}\tilde{L}^\dagger \mapsto U'=R(\tilde{R}\tilde{L}^\dagger)L^\dagger
=RUL^\dagger.$$ As mentioned above, we need to introduce an $x$ dependence to account for the fact that we are dealing with fields: $$\label{3:1:2:utrfafo}
U(x)\mapsto R U(x) L^\dagger.$$ For the physically relevant cases the corresponding unitary matrices may be parameterized as $$\label{3:1:2:upar}
U(x)=\exp\left(i\frac{\phi(x)}{F_0}\right),$$ where, for $N=2$, $$\label{3:1:2:phisu2}
\phi=\sum_{i=1}^3\phi_i\tau_i
\equiv
\left(\begin{array}{cc}
\pi^0&\sqrt{2}\pi^+\\
\sqrt{2}\pi^-&-\pi^0
\end{array}\right)$$ and, for $N=3$, $$\label{3:1:2:phisu3}
\phi=\sum_{a=1}^8  \phi_a\lambda_a \equiv
\left(\begin{array}{ccc}
\pi^0+\frac{1}{\sqrt{3}}\eta &\sqrt{2}\pi^+&\sqrt{2}K^+\\
\sqrt{2}\pi^-&-\pi^0+\frac{1}{\sqrt{3}}\eta&\sqrt{2}K^0\\
\sqrt{2}K^- &\sqrt{2}\bar{K}^0&-\frac{2}{\sqrt{3}}\eta
\end{array}\right).$$

The origin $\phi(x)=0$, i.e. $U_0=\mathbbm 1$, denotes the ground state of the system. Under transformations of the subgroup $H=\{(V,V)|V\in \mbox{SU($N$)}\}$ corresponding to rotating both left- and right-handed quark fields in QCD by the same $V$, the ground state remains invariant, $$U_0\mapsto VU_0 V^\dagger=V V^\dagger={\mathbbm 1}=U_0.$$ On the other hand, under "axial transformations," i.e. rotating the left-handed quarks by $A$ and the right-handed quarks by $A^\dagger$, the ground state does *not* remain invariant, $$U_0\mapsto A^\dagger U_0 A^\dagger=A^\dagger A^\dagger
\neq U_0,$$ which is consistent with the assumed spontaneous symmetry breakdown.

The traceless and Hermitian matrices of Eqs. ([\[3:1:2:phisu2\]](#3:1:2:phisu2){reference-type="ref" reference="3:1:2:phisu2"}) and ([\[3:1:2:phisu3\]](#3:1:2:phisu3){reference-type="ref" reference="3:1:2:phisu3"}) contain the Goldstone boson fields. We want to discuss their transformation behavior under the subgroup $H=\{(V,V)|V\in \mbox{SU($N$)}\}$. Expanding $$U={\mathbbm 1}+i\frac{\phi}{F_0}-\frac{\phi^2}{2F_0^2}+\cdots,$$ we immediately see that the transformation behavior of Eq. ([\[3:1:2:utrfafo\]](#3:1:2:utrfafo){reference-type="ref" reference="3:1:2:utrfafo"}) restricted to the subgroup $H$, $${\mathbbm 1}+i\frac{\phi}{F_0}-\frac{\phi^2}{2F_0^2}+\cdots\mapsto
V({\mathbbm 1}+i\frac{\phi}{F_0}-\frac{\phi^2}{2F_0^2}+\cdots)V^\dagger
={\mathbbm 1}+i\frac{V \phi V^\dagger}{F_0}-\frac{V\phi V^\dagger V\phi V^\dagger}{2F_0^2}
+\cdots,$$ implies $$\label{3:1:2:phihtrafo}
\phi\mapsto V\phi V^\dagger.$$ However, this corresponds exactly to the fact that the Goldstone bosons transform according to the adjoint representation under SU(3)$_V$, i.e. they transform as an octet.

For group elements of $G$ of the form $(A,A^\dagger)$ one may proceed in a completely analogous fashion. However, one finds that the fields $\phi_a$ do *not* have a simple transformation behavior under these group elements.

## Effective Lagrangian and power-counting scheme

The application of effective field theory (EFT) to strong interaction processes has become one of the most important theoretical tools in the low-energy regime. The basic idea consists of writing down the most general possible Lagrangian, including *all* terms consistent with assumed symmetry principles, and then calculating matrix elements with this Lagrangian within some perturbative scheme [@Weinberg:1978kz]. A successful application of this program thus requires two main ingredients:

1.  A knowledge of the most general effective Lagrangian;

2.  an expansion scheme for observables in terms of a consistent power-counting method.

### The lowest-order effective Lagrangian {#sec_loel}

In terms of the SU(3) matrix $U(x)$ of Eqs. ([\[3:1:2:upar\]](#3:1:2:upar){reference-type="ref" reference="3:1:2:upar"}) and ([\[3:1:2:phisu3\]](#3:1:2:phisu3){reference-type="ref" reference="3:1:2:phisu3"}) the most general, chirally invariant, effective Lagrangian with the minimal number of derivatives reads $$\label{3:2:1:l2}
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
