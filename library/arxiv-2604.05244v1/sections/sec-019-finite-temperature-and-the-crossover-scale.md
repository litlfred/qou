---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-019-finite-temperature-and-the-crossover-scale
section_title: "Finite temperature and the crossover scale"
section_number: null
pages: 23-24
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.962
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
[]{#sec:finite-T label="sec:finite-T"} At finite electron temperature $T_{\rm el}$, the Fermi step is smoothed over $\Delta n_T\sim k_BT_{\rm el}/\hbar\Omega$ sidebands. The Airy edge occupies $\Delta n_{\rm edge}\sim\kappa_A\sim A^{1/3}$ sidebands. Define the crossover parameter $$\theta_A := \frac{k_BT_{\rm el}/\hbar\Omega}{\kappa_A} = \frac{k_BT_{\rm el}}{\hbar\Omega}\left(\frac{2}{A}\right)^{\!1/3}.
  \label{eq:theta-def}$$ Replacing the sharp Fermi step by the smooth occupation $\bar f(E_m)=[1+\exp((E_m-\mu)/k_BT_{\rm el})]^{-1}$ in the kernel sum gives the finite-temperature kernel $$K_{A,T}(\nu,\lambda) = \sum_{r\in\mathbb Z} J_{\nu+r}(A)\,J_{\lambda+r}(A)\;\frac{1}{1+e^{-(r+\eta)\hbar\Omega/k_BT_{\rm el}}},
  \label{eq:KAT}$$ where $\eta(E)=(\mu-E)/\hbar\Omega - m_F(E)\in[0,1)$. The same Riemann-sum argument as in the proof of Theorem [\[thm:airy\]](#thm:airy){reference-type="ref" reference="thm:airy"} gives, in the edge scaling regime $\nu=A+s\kappa_A$, $$\kappa_A\,K_{A,T}(\nu_A(s),\nu_A(t)) \;\longrightarrow\; K_{\mathop{\mathrm{Ai}}}^{(\theta)}(s,t),
  \label{eq:KAT-limit}$$ with the *finite-temperature Airy kernel* [@Johansson2007; @DeanLeDoussal2015; @DeanLeDoussal2016] $$K_{\mathop{\mathrm{Ai}}}^{(\theta)}(s,t) = \int_{-\infty}^{\infty} \frac{\mathop{\mathrm{Ai}}(s+u)\,\mathop{\mathrm{Ai}}(t+u)}{1+e^{-u/\theta}}\,du.
  \label{eq:K-Ai-theta}$$ As $\theta\to 0$, this reduces to the ordinary Airy kernel $K_{\mathop{\mathrm{Ai}}}(s,t)=\int_0^\infty\mathop{\mathrm{Ai}}(s+u)\mathop{\mathrm{Ai}}(t+u)\,du$. Figure [\[fig:deficit\]](#fig:deficit){reference-type="ref" reference="fig:deficit"}(b) shows the thermal crossover on the diagonal.

This makes condition (5) of the Introduction quantitative: the zero-temperature Airy edge is sharp when $$k_BT_{\rm el} \ll \hbar\Omega\,\kappa_A = \hbar\Omega\,(A/2)^{1/3},
  \label{eq:T-condition}$$ and the crossover to thermal broadening occurs at $\theta_A\sim 1$, i.e., $k_BT_{\rm el}\sim\hbar\Omega\kappa_A$. For a drive frequency $\Omega/2\pi=10\;\mathrm{GHz}$ and $A=50$, one has $hf/k_B\approx 0.48\;\mathrm{K}$ and $\kappa_{50}=(50/2)^{1/3}\approx 2.9$, giving $T_{\rm cross}\sim hf\kappa_A/k_B\approx 1.4\;\mathrm{K}$---well above typical dilution-fridge base temperatures, confirming that the Airy edge should be experimentally accessible.

For $\theta_A\ll 1$, a Sommerfeld expansion of [\[eq:K-Ai-theta\]](#eq:K-Ai-theta){reference-type="eqref" reference="eq:K-Ai-theta"} gives the leading thermal correction on the diagonal: $$K_{\mathop{\mathrm{Ai}}}^{(\theta)}(s,s) = K_{\mathop{\mathrm{Ai}}}(s,s) - \frac{\pi^2}{3}\,\theta^2\,\mathop{\mathrm{Ai}}(s)\,\mathop{\mathrm{Ai}}'(s) + O(\theta^4).
  \label{eq:Sommerfeld}$$ This provides a practical formula for experimentalists who need the low-temperature correction without computing the full integral: the leading effect of finite temperature is a shift proportional to $\mathop{\mathrm{Ai}}(s)\mathop{\mathrm{Ai}}'(s)$, which is antisymmetric about the edge and vanishes at $s=0$.

::: remark
[]{#rem:scope label="rem:scope"} This subsection analyzes the finite-temperature crossover of the underlying edge kernel. Deriving the corresponding finite-$T$ shot-noise plateau deficit requires inserting the thermal distribution into the full noise formula [\[eq:PAN\]](#eq:PAN){reference-type="eqref" reference="eq:PAN"}, which yields a convolution of the Airy kernel diagonal with a thermal broadening function; we do not carry out that derivation here.
:::
