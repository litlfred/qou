---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-003-22-quantum-vc
section_title: "Quantum VC"
section_number: 2.2
pages: 9-11
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.963
doc_brief: "Quantum Field Theory and the Volume Conjecture — 15 sections: Front matter; Preliminaries; The many dimensions of the volume"
---
The second option for generalizing the volume conjecture [\[VC\]](#VC){reference-type="eqref" reference="VC"} is to ask for higher-order terms in the asymptotic expansion of the colored Jones polynomial. Let us define a new "quantum" parameter $\hbar$ as

$$\hbar = \frac{i\pi}{k}\,,$$

so that

$$q = e^{2\hbar}\,.$$

The two parameters $N$ and $k$ of the colored Jones polynomial can be traded for $\hbar$ and $u$, and the limit [\[lim\]](#lim){reference-type="eqref" reference="lim"} is simply $\hbar\to 0$. At $u=i\pi$, higher-order asymptotics are then predicted [@gukov-2003; @DGLZ] to have the form

$$V_N(K;q=e^{\frac{2\pi i}{N}}) \;\overset{N\to\infty}{\sim}\;
 \exp\left(\frac{1}{2\hbar}({\rm Vol}+i{\rm CS})-\frac{3}{2}\log\hbar+\frac{1}{2}\log\frac{-i\pi T_K}{4} + \sum_{n=2}^\infty \tilde{S}_n\hbar^{n-1}\right)\,. \label{VCh0}$$

Here, for example, $T_K$ is the Ray-Singer torsion of the knot complement $S^3\backslash K$. It can be defined after putting any background metric on $S^3\backslash K$ [@Porti] as

$$T(M) = \exp\left(-\frac12\sum_{n=0}^3n(-1)^n\log{\rm det}'\Delta_n\right) = \frac{(\det'\Delta_0)^\frac32}{(\det'\Delta_1)^\frac12}\,,$$

where $\Delta_n$ is the Laplacian acting on $n$-forms.

It is fairly straightforward to combine the present quantum deformation with the parametrization of the volume conjecture in $u$. The expectation is that

$$\boxed{J_N(K;q) \;\overset{N,k\to\infty}{\sim}\;
 \exp\left( -\frac{1}{4\hbar}I_{CS}({\cal A}(u)) -\frac{3}{2}\log\hbar + \frac{1}{2}\log \frac{iT_K(u)}{4\pi}+\sum_{n=2}^\infty S_n(u)\hbar^{n-1}\right)}\,. \label{VCh}$$

Here, $T_K(u)$ is a $u$-deformed torsion, and is related to the Alexander polynomial of $K$ [@Mur-Alex]. The higher-order coefficients in [\[VCh0\]](#VCh0){reference-type="eqref" reference="VCh0"} are related to those in [\[VCh\]](#VCh){reference-type="eqref" reference="VCh"} as

$$\sum_{n\geq2}\tilde{S}_n\hbar^{n-1}=\sum_{n\geq2}S_n(i\pi)\hbar^{n-1}-\log\frac{\sinh\hbar}{\hbar}\,.$$

For the figure-eight knot, the quantum volume conjecture [\[VCh\]](#VCh){reference-type="eqref" reference="VCh"} was tested to first subleading order in [@gukov-2006], using the Ray-Singer torsion

$$T_{\mathbf{4_1}}(u) = \frac{4\pi^2}{\sqrt{-m^{-4}+2m^{-2}+1+2m^{2}-m^{4}}}\,.$$

Higher-order coefficients $S_n(u)$ can also be computed [@DGLZ]. For example,

$$\begin{aligned}
 S_2(u) &= \frac{-i(T_{\mathbf{4_1}})^3}{12(4\pi^2)^3m^6}\big(1-m^2-2m^4+15m^6-2m^8-m^{10}+m^{12}\big)\,, \\
  S_3(u) &= \frac{-2(T_{\mathbf{4_1}})^6}{(4\pi^2)^6m^6}\big(1-m^2-2m^4+5m^6-2m^8-m^{10}+m^{12}\big)-\frac16\,.
\end{aligned}$$

These expressions appear to be new, unexplored knot invariants with distinctive number-theoretic properties. Needless to say, it would be interesting to test the quantum volume conjecture [\[VCh\]](#VCh){reference-type="eqref" reference="VCh"} for other hyperbolic knots and/or to higher order in the $\hbar$-expansion.\
Just as the generalization of the volume conjecture to $u\neq 0$ was interpreted in terms of the $SL(2,{\mathbb{C}})$ Chern-Simons functional, there is also a Chern-Simons interpretation of the quantum volume conjecture. One must consider how the functional $I_{CS}({\cal A})$ behaves when the connection ${\cal A}$ undergoes "quantum fluctuations" away from the flat connection ${\cal A}(u)$. This is accomplished in physics via perturbative quantum field theory. Symbolically, we can write ${\cal A}={\cal A}(u)+{\cal A}'$, where ${\cal A}'$ contains the fluctuations away from flatness, and define a perturbative "partition function" via the path integral

$$Z(S^3\backslash K;u;\hbar)_{\rm pert} = \int {\cal D}{\cal A}'\,e^{-\frac{1}{4\hbar}I_{CS}({\cal A}(u)+{\cal A}')}\,. \label{path2}$$

The exponent in the integrand has a critical point at ${\cal A}'=0$, and a saddle point expansion around this point yields the right-hand-side of [\[VCh\]](#VCh){reference-type="eqref" reference="VCh"}. (To be very precise, $J_N(K;q)\sim Z(S^3\backslash K;\hbar;u)/Z(S^3;\hbar)$, where $Z(S^3;\hbar) = \sqrt{2/k}\sin(\pi/k)$ is the partition function of the three-sphere $S^3$.)
