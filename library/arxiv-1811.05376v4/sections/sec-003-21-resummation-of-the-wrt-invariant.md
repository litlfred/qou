---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-003-21-resummation-of-the-wrt-invariant
section_title: "Resummation of the WRT invariant"
section_number: 2.1
pages: 17-18
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.883
latex_coverage_ratio: 1.0
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphere X we show that the q-series invariant ˆZ0(X; q) introduced by"
---
We now turn to the resummation of the normalized WRT invariant $\tilde{\mathop{\mathrm{Z}}}_k(X)$. Recall that for $\mu \in \mathbb{Q}/ \mathbb{Z}$ we introduced the set $$\begin{aligned}
\label{R}
\mathcal{T}(\mu) = & \{m=1,...,2P -1 :-m^2/4P=\mu \ \mathop{\mathrm{mod}}\ \mathbb{Z} \}.
\end{aligned}$$ We also introdude the residue operator $\mathcal{I}_\mu$ which for a meromorphic function $\hat{\varphi}$ is given by $$\begin{aligned}
  \label{Lmu}  \mathcal{I}_{\mu}(\hat{\varphi})(\xi) = -& \sum_{x \in \mathcal{T}(\mu)} \mathop{\mathrm{Res}}\left (\frac{\exp\left(\xi \frac{iy^2}{8\pi P}\right)}{(1-e^{-\xi y})} \frac{y}{ 4P}\hat{\varphi}\left(\frac{y^2}{i8\pi P }\right) , y=2\pi i x\right)
\end{aligned}$$ Observe that by definition $\mathcal{T}(\mu)$ is empty for all but finitely many $\mu \in \mathbb{Q} / \mathbb{Z}$ and therefore $\mathcal{I}_{\mu}$ is $0$ for all but these finitely many $\mu.$

::: corollary
[]{#2.2 label="2.2"} The polynomials $\mathop{\mathrm{Z}}_{\theta}$ and the quantum invariant $\widetilde{\mathop{\mathrm{Z}}}_k(X)$ are determined by $\mathcal{B}(\mathop{\mathrm{Z}}_{0})$ as follows $$\begin{aligned}
 \label{Poooly}  \mathop{\mathrm{Z}}_{\theta} (k) & = e^{-2\pi i k \theta} \mathcal{I}_{\theta}\left(\mathcal{B}(\mathop{\mathrm{Z}}_{0})\right)(k).
    \\   \widetilde{\mathop{\mathrm{Z}}}_k(X) &= \mathcal{L}_{\mathbb{R}_+}( \mathcal{B}(\mathop{\mathrm{Z}}_{0}))(k)+\sum_{\theta \in \frac{i}{2\pi} \Omega \ \mathop{\mathrm{mod}}\ \mathbb{Z}} \mathcal{I}_{\theta}\left(\mathcal{B}(\mathop{\mathrm{Z}}_{0})\right)(k) \label{Resuuumation} .
    
\end{aligned}$$
:::

The identity [\[Resuuumation\]](#Resuuumation){reference-type="eqref" reference="Resuuumation"} of Corollary [\[2.2\]](#2.2){reference-type="ref" reference="2.2"} is reminiscent of the typical resummation process from resurgence [@Schiappa18; @Dorigoni14]. The Ohtsuki-series is known to determine $\tau_k(X).$ The new insight provided by resurgence is that it does so via resummation as stated in Corollary [\[2.2\]](#2.2){reference-type="ref" reference="2.2"}.

We now prove Corollary [\[2.2\]](#2.2){reference-type="ref" reference="2.2"}.

::: proof
*Proof.* It easily follows from [\[ComputingBorel\]](#ComputingBorel){reference-type="eqref" reference="ComputingBorel"} that $$\label{TYTY}
    F(\zeta)= \mathcal{B}(\mathop{\mathrm{Z}}_{0})\left(\frac{\zeta^2}{i8P\pi}\right) \frac{\zeta }{4P}.$$ Recall from [\[eq:formulaforpolynomial\]](#eq:formulaforpolynomial){reference-type="eqref" reference="eq:formulaforpolynomial"} that $$e^{2\pi ik \theta} \mathop{\mathrm{Z}}_{\theta}(k)=- \sum_{\tilde m \in \mathcal{T}(\theta)}  \text{Res} \left( \frac{F(y)e^{kg(y)}}{1-e^{-ky}}, y=2\pi i \tilde m \right).$$ From this and Equation [\[TYTY\]](#TYTY){reference-type="eqref" reference="TYTY"} one easily obtains [\[Poooly\]](#Poooly){reference-type="eqref" reference="Poooly"}.

In the proof of Theorem [\[2.1\]](#2.1){reference-type="ref" reference="2.1"} we obtained the following exact formula $$\label{eq:DecompWRT}
\tilde{\mathop{\mathrm{Z}}}_k(X) = \mathcal{L}_{\mathbb{R}_+}(\mathcal{B})(k)+ \sum_{\theta \in \mathop{\mathrm{CS}}_{\mathbb{C}}^*(X)} e^{2\pi i k \theta} \mathop{\mathrm{Z}}_\theta(k).$$ Thus we see that [\[Resuuumation\]](#Resuuumation){reference-type="eqref" reference="Resuuumation"} follows from this formula and [\[Poooly\]](#Poooly){reference-type="eqref" reference="Poooly"}. ◻
:::
