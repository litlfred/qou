---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-010-soft-edge-and-the-airy-kernel
section_title: "Soft edge and the Airy kernel"
section_number: null
pages: 12-14
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.996
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
[]{#sec:airy label="sec:airy"} The Bessel functions in [\[eq:discreteBessel\]](#eq:discreteBessel){reference-type="eqref" reference="eq:discreteBessel"} have three regimes when $A\gg 1$ [@Watson1944; @Olver1974]: an oscillatory bulk for orders $|\nu|\ll A$, an exponentially decaying tail for $|\nu|\gg A$, and a turning-point region of width $\sim A^{1/3}$ near the edge $|\nu|\sim A$. Physically, this transition marks the boundary between easily accessible multi-photon processes (where many sideband channels are open) and exponentially suppressed ones (where the drive can no longer excite carriers into higher sidebands). The Airy kernel emerges precisely from that turning-point region, which is the Floquet analogue of a classical caustic: two stationary-phase points in the integral representation of $J_\nu(A)$ coalesce as $\nu\to A$.

It is convenient to introduce the canonical edge scale $$\kappa_A := \left(\frac{A}{2}\right)^{1/3}
  \label{eq:kappa}$$ and, for $s\in\mathbb R$, the rescaling $$\nu_A(s) := \lfloor A + s\kappa_A\rfloor.
  \label{eq:nuAs}$$ We also define the rescaled kernel $$\widehat K_A(s,t) := \kappa_A\,K_A^{\rm (disc)}\big(\nu_A(s),\nu_A(t)\big).
  \label{eq:Khat}$$ Note that $\widehat K_A(s,t)$ is piecewise constant in $s$ and $t$ (it takes the same value for all $s$ that map to the same integer $\nu_A(s)$). As $A\to\infty$ the step size $1/\kappa_A\to 0$ and the staircase converges to a smooth limit.

The key asymptotic input is the Debye--Olver uniform approximation [@Olver1974] for Bessel functions near the turning point. For integer order $n$ in the transition region, it gives $$\kappa_A\, J_n(A) = \mathop{\mathrm{Ai}}\!\left(\frac{n-A}{\kappa_A}\right) + O(A^{-2/3}),
  \label{eq:Olver-exact}$$ uniformly for $(n-A)/\kappa_A$ in any compact set. For $n\ge A$, setting $\xi:=(n-A)/\kappa_A$, the Johansson--Olver piecewise estimate [@Johansson2001; @Olver1974] gives $|\kappa_A J_n(A)|\le C\exp[-c\min(\kappa_A,\sqrt\xi)\,\xi]$; near the turning region ($\xi=O(1)$) this behaves as $e^{-c\xi^{3/2}}$, matching the Airy tail, while for $\xi\gg 1$ the global decay is at least $e^{-c\xi}$.[^1]

When [\[eq:Olver-exact\]](#eq:Olver-exact){reference-type="eqref" reference="eq:Olver-exact"} is composed with the floor in [\[eq:nuAs\]](#eq:nuAs){reference-type="eqref" reference="eq:nuAs"}, the discretization $\lfloor A+s\kappa_A\rfloor = A+s\kappa_A+\delta$ with $\delta\in(-1,0]$ shifts the Airy argument by $\delta/\kappa_A = O(A^{-1/3})$. Since $\mathop{\mathrm{Ai}}$ is Lipschitz on compacts, this gives $$\kappa_A\, J_{\nu_A(s)}(A) = \mathop{\mathrm{Ai}}(s) + O(A^{-1/3}),
  \label{eq:turningcompact}$$ where the $O(A^{-1/3})$ error is dominated by the floor, not by the Olver correction. The convergence $\widehat K_A\to K_{\mathop{\mathrm{Ai}}}$ is unaffected (only the rate changes); we state it as follows.

::: thm
[]{#thm:airy label="thm:airy"} Under the zero-temperature, single-step assumption [\[eq:Fermistep\]](#eq:Fermistep){reference-type="eqref" reference="eq:Fermistep"}, the rescaled kernel [\[eq:Khat\]](#eq:Khat){reference-type="eqref" reference="eq:Khat"} satisfies $$\widehat K_A(s,t) \longrightarrow K_{\mathop{\mathrm{Ai}}}(s,t)
  := \int_0^{\infty}\mathop{\mathrm{Ai}}(s+u)\mathop{\mathrm{Ai}}(t+u)\,du
  \label{eq:AiryKernel}$$ as $A\to\infty$, locally uniformly in $(s,t)\in\mathbb R^2$.
:::

The proof (given in Appendix [\[app:airy\]](#app:airy){reference-type="ref" reference="app:airy"}) rewrites the discrete sum in [\[eq:discreteBessel\]](#eq:discreteBessel){reference-type="eqref" reference="eq:discreteBessel"} as a Riemann sum with mesh $1/\kappa_A$. The convergence of the discrete Bessel kernel to the Airy kernel is known in the combinatorics literature [@Johansson2001; @Borodin2000]; we include a self-contained proof adapted to our scaling conventions. The pointwise approximation [\[eq:turningcompact\]](#eq:turningcompact){reference-type="eqref" reference="eq:turningcompact"} controls the finite part, and the exponential tail bound provides the uniform domination needed for the exchange of limit and summation.

::: cor
[]{#cor:airyprocess label="cor:airyprocess"} At fixed central energy $E$, define the rescaled occupation measure $$\Xi_A := \sum_\nu N_\nu\,\delta_{(\nu-A)/\kappa_A}.
  \label{eq:Xi}$$ Then the correlation functions of $\Xi_A$ converge to those of the Airy determinantal point process $\Xi_{\mathop{\mathrm{Ai}}}$ [@TracyWidom1994; @Forrester2010]; full point-process weak convergence follows from the locally uniform kernel convergence of Theorem [\[thm:airy\]](#thm:airy){reference-type="ref" reference="thm:airy"} combined with the tail control in Appendix [\[app:airy\]](#app:airy){reference-type="ref" reference="app:airy"}, by the general criterion for determinantal processes [@HKPV2009; @Johansson2001]. In terms of the raw discrete variables, this means $$\kappa_A\,\langle N_{\nu_A(s)}\rangle \longrightarrow K_{\mathop{\mathrm{Ai}}}(s,s),
  \qquad
  \kappa_A^2\,\langle N_{\nu_A(s)}N_{\nu_A(t)}\rangle_c \longrightarrow -\abs{K_{\mathop{\mathrm{Ai}}}(s,t)}^2
  \quad (s\neq t),
  \label{eq:edge-scaling}$$ with the individual site occupations $\langle N_{\nu_A(s)}\rangle\sim\kappa_A^{-1}K_{\mathop{\mathrm{Ai}}}(s,s)\to 0$ at each fixed $s$, reflecting the dilution of a finite number of edge excitations across a growing number of sites.
:::

In physical terms: at each fixed $E$, the rescaled sideband correlations near the Fermi edge are governed by the Airy kernel and depend only on the edge scaling variable $s=(\nu-A)/\kappa_A$. For the monochromatic Bessel case proved here, this is independent of the static scatterer $\mathcal U(E)$ (which drops out of the correlator under the conditions of Sec. [\[sec:discrete-bessel\]](#sec:discrete-bessel){reference-type="ref" reference="sec:discrete-bessel"}). Whether the same Airy edge persists for general drive waveforms---i.e., for the Fourier coefficients $\mathcal F_k$ replacing $J_k(A)$---is plausible on stationary-phase grounds (Sec. [\[sec:pearcey\]](#sec:pearcey){reference-type="ref" reference="sec:pearcey"}) but has not been proved here.

![Airy scaling collapse of sideband occupations. (a) Diagonal of the discrete Bessel kernel $K_A^{\rm (disc)}(\nu,\nu) = \langle N_\nu\rangle$ as a function of the shifted sideband index $\nu=n-m_F$ for several drive amplitudes $A$. (b) After rescaling $\nu\to s=(\nu-A)/\kappa_A$ and multiplying by $\kappa_A$, the data for different $A$ collapse onto the diagonal of the Airy kernel $K_{\mathop{\mathrm{Ai}}}(s,s)$ (black curve). The residual scatter at $A=20$ reflects the $O(A^{-1/3})$ discretization error discussed around Eq. [\[eq:turningcompact\]](#eq:turningcompact){reference-type="eqref" reference="eq:turningcompact"}.](fig_sideband_airy.pdf){#fig:airy-collapse width="\\linewidth"}

![Two-point kernel at the soft edge for $A=100$. (a) Rescaled discrete Bessel kernel $\kappa_A K_A^{\rm (disc)}(\nu_A(s),\nu_A(0))$ (dots) compared to the Airy kernel $K_{\mathop{\mathrm{Ai}}}(s,0)$ (solid curve) as a function of $s$ at fixed $t=0$. (b) Difference $\kappa_A K_A^{\rm (disc)} - K_{\mathop{\mathrm{Ai}}}$ over the edge region, showing $O(A^{-1/3})$ residual errors that decrease toward zero as $A\to\infty$.](fig_kernel_comparison.pdf){#fig:kernel-2pt width="\\linewidth"}

Figures [1](#fig:airy-collapse){reference-type="ref" reference="fig:airy-collapse"} and [2](#fig:kernel-2pt){reference-type="ref" reference="fig:kernel-2pt"} illustrate the scaling collapse numerically. For $A$ as small as $20$, the rescaled diagonal already tracks the Airy kernel closely (Fig. [1](#fig:airy-collapse){reference-type="ref" reference="fig:airy-collapse"}b); the residual scatter is consistent with the $O(A^{-1/3})$ floor-discretization error. The two-point kernel comparison at $A=100$ (Fig. [2](#fig:kernel-2pt){reference-type="ref" reference="fig:kernel-2pt"}) confirms the convergence in the off-diagonal entries as well. For orientation, the discretization error $(A/2)^{-1/3}$ is about $0.34$ at $A=50$ and $0.22$ at $A=200$; these numbers set the scale of the mismatch between the discrete Bessel and Airy kernels. They should not be read as rigorous error bounds on a physical observable, since the actual error depends on the observable, the window, and the $E$-integration.

[^1]: The standard Olver prefactor uses the order $n$ rather than the argument $A$, i.e., $(n/2)^{1/3}$ rather than $(A/2)^{1/3}$; since $n = A+O(A^{1/3})$ in the transition region, the two differ by a relative $O(A^{-2/3})$ that is absorbed in the error term.
