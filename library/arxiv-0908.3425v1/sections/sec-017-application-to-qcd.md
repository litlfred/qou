---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-017-application-to-qcd
section_title: "Application to QCD"
section_number: null
pages: 22-24
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 1.0
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
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
