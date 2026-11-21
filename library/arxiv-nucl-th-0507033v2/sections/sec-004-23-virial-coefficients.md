---
doc_id: arxiv-nucl-th-0507033v2
doc_title: "Cluster Formation and The Virial Equation of State of Low-Density Nuclear Matter"
section_id: sec-004-23-virial-coefficients
section_title: "Virial Coefficients"
section_number: 2.3
pages: 4-5
source_pdf: 0507033v2.pdf
source_sha256: 57509b3ce5f9f8cc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.844
latex_coverage_ratio: 0.77
doc_brief: "Cluster Formation and The Virial Equation of State of Low-Density Nuclear Matter — 15 sections: Front matter; Introduction; Formalism"
---
We relate the second virial coefficients to the relevant scattering phase shifts. This extends the standard results for spin-zero particles [@b2] to include spin and isospin. The virial coefficient is related to the partition function of the two-particles system $\sum_{\text{states}} e^{-E_{2}/T}$, where the sum is over all two-particle states of energy $E_{2}$. This sum can be converted to an integral over relative momentum $k$ weighted by the density of states. The difference between the density of states of an interacting and a free two-particle system can be expressed in terms of the derivative of the two-body phase shift $d\delta(k)/dk$ [@b2; @huang]. Finally, if one integrates by parts, the virial coefficients can be calculated from an integral over the scattering phase shifts summed over all partial waves with two-body spin $S$, isospin $T$, orbital angular momentum $L$ and total angular momentum $J$ allowed by spin statistics.

The virial coefficient $b_n$ describes the interactions in pure neutron matter, and we have $$b_n(T)=\frac{1}{2^{1/2}\,\pi T} \int_0^\infty dE \: e^{-E/2T} \, 
\delta^{\text{tot}}_n(E) - 2^{-5/2} \,.
\label{bn}$$ Here, $-2^{-5/2}$ is the free Fermi gas contribution due to the Pauli principle and $\delta^{\text{tot}}_n(E)$ is the sum of the $T=1$ elastic scattering phase shifts at laboratory energy $E$. This sum includes a degeneracy factor $(2J+1)$, $$\begin{aligned}
\delta^{\text{tot}}_n(E) &= \sum_{S,L,J} (2J+1) \, 
\delta_{\,^{2S+1}\text{L}_J}(E)
\nonumber \\[1mm]
&=\delta_{^1\text{S}_0}+\delta_{^3\text{P}_0}+3\,\delta_{^3\text{P}_1}
+5\,\delta_{^3\text{P}_2}+5\,\delta_{^1\text{D}_2}+ \ldots
\label{deltantot}
\end{aligned}$$ Here and in the following we have neglected the effects of the mixing parameters due to the tensor force. We expect that their contributions to the second virial coefficients describing spin-averaged observables vanish.

The $pn$ virial coefficient can be decomposed as $$b_{pn}(T)=b_{\text{nuc}}(T)-b_n(T) \,,
\label{bpn}$$ where $b_{\text{nuc}}$ is the second virial coefficient for symmetric nuclear matter. With $b_{pn}$ and $b_n$ one can describe asymmetric matter with arbitrary proton fraction. For $b_{\text{nuc}}$, the contributions from the deuteron bound state and the scattering continuum are given by $$\begin{aligned}
b_{\text{nuc}}(T) &= \frac{3}{2^{1/2}}\bigl(e^{E_d/T}-1\bigr) -2^{-5/2}
\nonumber \\[1mm]
&+ \frac{1}{2^{3/2}\,\pi T} \int_0^\infty dE \: e^{-E/2T} \, 
\delta^{\text{tot}}_{\text{nuc}}(E) \,,
\label{bnuc}
\end{aligned}$$ where the term $-1$ in the deuteron contribution comes from the partial integration (the phase shift at zero energy being $\pi$ times the number of bound states) and the factor $3$ counts the spin-isospin degeneracy of the deuteron. The total phase shift $\delta^{\text{tot}}_{\text{nuc}}(E)$ for nuclear matter also receives contributions from $T=0$ states, $$\begin{aligned}
\delta^{\text{tot}}_{\text{nuc}}(E) &= \sum_{S,L,J} (2J+1)(2T+1) \, 
\delta_{\,^{2S+1}\text{L}_J}(E)
\nonumber \\[1mm]
&=3\,\delta_{^1\text{S}_0}+3\,\delta_{^3\text{S}_1}
+3\,\delta_{^1\text{P}_1} \nonumber \\[1mm]
&+3\,\delta_{^3\text{P}_0}
+9\,\delta_{^3\text{P}_1}+15\,\delta_{^3\text{P}_2}
+15\,\delta_{^1\text{D}_2} \nonumber \\[1mm]
&+3\,\delta_{^3\text{D}_1}+5\,\delta_{^3\text{D}_2}
+7\,\delta_{^3\text{D}_3}+ \ldots
\label{deltanuctot}
\end{aligned}$$

For spin-zero alpha particles we can directly use the results of [@b2; @huang], which give for the virial coefficient $b_\alpha$ $$b_\alpha(T)=\frac{2^{1/2}}{\pi T} \int_0^\infty dE \: e^{-E/2T} \,
\delta^{\text{tot}}_\alpha(E) + 2^{-5/2} \,,
\label{ba}$$ where $+2^{-5/2}$ describes the contribution for a free Bose gas and the total phase shift $\delta^{\text{tot}}_\alpha(E)$ for elastic $\alpha\alpha$ scattering is given by $$\begin{aligned}
\delta^{\text{tot}}_\alpha(E) &= \sum_{L} (2L+1) \,
\delta_{\text{L}}(E)
\nonumber \\[1mm]
&=\delta_{\text{S}}+5\,\delta_{\text{D}}+9\,\delta_{\text{G}}
+13\,\delta_{\text{I}} + \ldots
\label{deltaaatot}
\end{aligned}$$ For the $\alpha\alpha$ virial coefficient and for the following N$\alpha$ virial coefficient, we have not taken into account the effects of inelasticities. For low temperatures, we expect their contributions to be small due to the tight binding of the alpha particle.

Finally, the N$\alpha$ virial coefficient is given by $$b_{\alpha n}(T)=\biggl(\frac{5}{4}\biggr)^{1/2} \frac{1}{\pi T} 
\int_0^\infty dE \: e^{-4E/5T} \, \delta^{\text{tot}}_{\alpha n}(E) \,,
\label{ban}$$ with total phase shift $\delta^{\text{tot}}_{\alpha n}(E)$ for N$\alpha$ scattering at nucleon laboratory energy $E$, $$\begin{aligned}
\delta^{\text{tot}}_{\alpha n}(E) &= \sum_{L,J} (2J+1) \, 
\delta_{\text{L}_J}(E)
\nonumber \\[1mm]
&=2\,\delta_{\text{S}_{1/2}}+2\,\delta_{\text{P}_{1/2}}
+4\,\delta_{\text{P}_{3/2}}+4\,\delta_{\text{D}_{3/2}}
+6\,\delta_{\text{D}_{5/2}} \nonumber \\[1mm]
&+6\,\delta_{\text{F}_{5/2}}+8\,\delta_{\text{F}_{7/2}}+ \ldots
\label{deltaantot}
\end{aligned}$$ Once the four virial coefficients $b_n(T)$, $b_{pn}(T)$, $b_\alpha(T)$ and $b_{\alpha n}(T)$ have been calculated, the pressure is determined from Eq. ([\[p\]](#p){reference-type="ref" reference="p"}) using fugacities $z_n$ and $z_p$ that reproduce the desired baryon density $n_b$ and proton fraction $Y_p$ using Eqs. ([\[zalpha\]](#zalpha){reference-type="ref" reference="zalpha"},[\[nn\]](#nn){reference-type="ref" reference="nn"}-[\[yp\]](#yp){reference-type="ref" reference="yp"}).
