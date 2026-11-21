---
doc_id: arxiv-1309.3313v1
doc_title: "Hadron Structure in Chiral Perturbation Theory"
section_id: sec-001-ii-pion-form-factor
section_title: "II Pion Form Factor"
section_number: null
pages: 1-3
source_pdf: 1309.3313v1.pdf
source_sha256: 11614aa35b1ffa50
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.991
doc_brief: "Hadron Structure in Chiral Perturbation Theory — 6 sections: Front matter; I Introduction; II Pion Form Factor"
---
The spatial pion electromagnetic form factor has been addressed in [@Ga84; @NR; @JK; @FC; @IBG; @MT] and is under experimental study currently [@Fpi]. To investigate the behavior of the pion form factor experimentally at momentum transfers $Q^{2}>0.3\, GeV^{2}$ and in the transitional region between long-distance and short-distance QCD, one must use the charged pion electroproduction process. The two-fold differential cross section for the exclusive pion electroproduction can be parametrized by a well known formula [@EP1] in terms of photoabsorption cross sections, where each term corresponds to certain polarization states of the virtual photon: $$\begin{aligned}
&&2\pi\frac{d^{2}\sigma}{dtd\phi}=\epsilon\frac{d\sigma_{L}}{dt}+
\frac{d\sigma_{T}}{dt}+ \nonumber \\ \nonumber \\
&&\sqrt{2\epsilon(\epsilon+1)} \frac{d\sigma_{LT}}{dt}\cos\phi 
+\epsilon\frac{d\sigma_{TT}}{dt}\cos2\phi \space . \label{eq:1}
\end{aligned}$$ Here, subscripts L and T correspond to the longitudinal and transverse polarizations of the virtual photon respectively. Parameter $t$ is the negative momentum transfer to the hadronic target squared and $\phi$ is the azimuthal angle of the detected hadron in the center-of-mass reference frame. If the experimental setup has the azimuthal acceptance [@Fpi], it is possible to determine interference terms, $\sigma_{LT}$ and $\sigma_{TT}$, and then extract the longitudinal term $\sigma_{L}$ by the Rosenbluth separation. In the t-pole approximation, the longitudinal term, $\sigma_{L}$, is related to the pion form factor, $F{}_{\pi}$, in the following way: $$\begin{aligned}
\frac{d\sigma_{L}}{dt}\propto-\frac{tQ^{2}}{t-m_{\pi}^{2}}g_{\pi NN}^{2}(t)F_{\pi}^{2}(Q^{2},t),\label{eq:2} \space ,
\end{aligned}$$ where $g{}_{\pi NN}(t)$ is a pion-proton coupling. Thus, Eq.([\[eq:2\]](#eq:2){reference-type="ref" reference="eq:2"}) allows the extraction of the pion electromagnetic form factor for different momentum transfers above the pion production threshold. As it is well known, the determination of the pion form factor from the pion electroproduction is impacted by radiative corrections, $\delta=\frac{d\sigma_{obs}}{d\sigma_{o}}$. The radiative corrections to the electron current and vacuum polarization were calculated in [@AAB], and leading hadronic corrections (two-photon box diagrams) were addressed in [@AAB2]. In [@AAB2], it was found that the two-photon box correction could reach as much as -20% for the backward kinematics ($\epsilon\rightarrow0$) and high momentum transfers. In order to calculate the form factor of the pion, we use the CHM from [@CHM], which is based on CHPT. Here, we do one-loop calculations with a subtractive renormalization scheme for the scale fixed by the charge radius of the pion: ($<r_{\pi}^{2}>=(0.439\pm0.030)\,\mbox{fm\ensuremath{^{2}}}$). For the $\pi-\gamma-\pi$ interaction, we arrive at the following renormalized amplitude: $$\begin{aligned}
M_{r}(q)=e\epsilon\cdot(p'+p) \ \bigg(1-\frac{q^{2}}{f_{\pi}^{2}}f_{1}(q^{2},\Lambda^{2},m_{\pi}^{2})\bigg)-
\nonumber \\
e\frac{\epsilon\cdot q(p'^{2}-p^{2})}{f_{\pi}^{2}}f_{2}(q^{2},\Lambda^{2},m_{\pi}^{2}).\label{eq:3}
\end{aligned}$$ From this, we can form two form factors - one on-shell and another off-shell (if one of the pions is off-shell): $$\begin{aligned}
&&F_{on-shell}(q^{2})=1-\frac{q^{2}}{f_{\pi}^{2}}f_{1}(q^{2},\Lambda^{2},m_{\pi}^{2})\label{eq:4}\\
&&F_{off-shell}(q^{2})=-\frac{p'^{2}-p^{2}}{f_{\pi}^{2}}f_{2}(q^{2},\Lambda^{2},m_{\pi}^{2}).\label{eq:5}
\end{aligned}$$ Here, $p$ and $p'$ are momenta of the incoming and outgoing pion, $q$ is the momentum of the virtual photon, and the functions, $f_{1, 2}(q^{2},Q^{2},m_{\pi}^{2})$, depend on one- and two-point Passarino-Veltman functions. To incorporate CHPT into the calculations of the two-photon box correction, we fit the pion on-shell monopole formfactor to the form factor in Eq.[\[eq:4\]](#eq:4){reference-type="ref" reference="eq:4"} for the $Q^{2}<0.3\,\mbox{GeV}^{2}$ and get $F_{on-shell}(Q^{2})=\frac{\Phi^{2}}{\Phi^{2}+Q^{2}}$ with $\Phi=0.73\,\mbox{GeV}$. A reason to choose the monopole form factor is its asymptotic behavior at high momentum transfers, $F_{on-shell}(Q^{2})\bigg|_{Q^{2}\rightarrow\infty}=\frac{8\pi\alpha_{s}(Q^{2})f_{\pi}^{2}}{Q^{2}}$, driven by the perturbative QCD. For the off-shell form factor in Eq.([\[eq:5\]](#eq:5){reference-type="ref" reference="eq:5"}), we also choose the monopole form, which is fitted to the CHPT off-shell form factor, so we get $F_{off-shell}(Q^{2},t)=(m_{\pi}^{2}-t)\frac{Q^{2}}{\Omega^{2}+Q^{2}}$ with $\Omega=2.5\,\mbox{GeV.}$

<figure id="fig3">
<div class="centering">
<img src="pionFF" />
</div>
<figcaption>On-shell and off-shell pion form factors. The red line shows the monopole fit of the on-shell formfactor to CHPT results. Experimental data are taken from <span class="citation" data-cites="Amend Acker Brauel Hub"></span>. The off-shell form factor is shown for both low (<span class="math inline"><em>t</em> =  − 0.005 GeV<sup>2</sup></span>, blue line) and high (<span class="math inline"><em>t</em> =  − 0.212 GeV<sup>2</sup></span>, green line) hadronic momentum transfers.</figcaption>
</figure>

From Fig.[1](#fig3){reference-type="ref" reference="fig3"}, one can see that our fit is in rather good agreement with experimental data. We now use the fitted form factors in the calculations of the two-photon box pion electroproduction correction with the same tools for the exact calculations as in [@AAB2], for high ($Q^{2}=6.0\,\mbox{GeV}^{2}$) and low ($Q^{2}=0.3\,\mbox{GeV}^{2}$) momentum transfers (see Fig.[\[fig3-1\]](#fig3-1){reference-type="ref" reference="fig3-1"}).

::: figure*
::: centering
![image](TPE-high) ![image](TPE-low)
:::
:::

Two lines, $\Phi=0.73\,\mbox{GeV}$ (green dashed line) and $\Phi=0.85\,\mbox{GeV}$ (red solid line), illustrate the box correction sensitivity to the choice of the scale in the form factor. As can be clearly seen from the right plot of Fig.[\[fig3-1\]](#fig3-1){reference-type="ref" reference="fig3-1"}, for the low momentum transfer the correction is rather sensitive to the scale, which induces an additional theoretical uncertainty due to the box correction model dependence. For the high momentum transfer (left plot of Fig.[\[fig3-1\]](#fig3-1){reference-type="ref" reference="fig3-1"}, we observe that the correction does not change much with the change of the scale in the form factor. Thus, we observe a reduced degree of model dependence in the correction for high momentum transfers. For the off-shell part of the pion form factor, we have observed a contribution of less than 1% to the correction, which certainly diminishes any role of the off-shell form factor in the pion electroproduction process.
