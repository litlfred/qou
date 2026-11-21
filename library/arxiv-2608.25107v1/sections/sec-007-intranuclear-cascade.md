---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_id: sec-007-intranuclear-cascade
section_title: "Intranuclear cascade"
section_number: null
pages: 6-6
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.962
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples — 19 sections: ADoNIS: A Differentiable generatOr; Introduction; Differentiable programming in part"
---
[]{#sec:adonis_cascade label="sec:adonis_cascade"}

The hadrons produced at the vertex propagate through the residual nucleus and undergo final-state interactions, modelled with a JAX re-implementation of the intranuclear cascade used in ACHILLES [@Isaacson:2020wlx]: elastic and inelastic nucleon--nucleon and pion--nucleon scattering, pion absorption, and charge exchange. Everything at the vertex is a smooth function of the parameters once the kinematics are fixed. The cascade is not: a hadron leaving the vertex takes a variable-length sequence of sampled re-interactions, and the number, position and identity of those interactions are themselves random. Differentiating any single realised history gives nothing, because a parameter change does not move that history, it changes how probable it was.

*The construction.* [ADoNIS]{.smallcaps} compactly stores the history each event actually took, and recomputes its probability under new parameters. The cascade factor in Eq. [\[eq:adonis_weight\]](#eq:adonis_weight){reference-type="ref" reference="eq:adonis_weight"} is the likelihood ratio of that history, $$r^{\rm FSI}_i(\bm\theta) = \prod_{n\,\in\,{\rm history}_i}
\frac{p_n(\bm\theta)}{p_n({\rm nominal})},
\label{eq:adonis_fsi}$$ a product over the interaction and survival probabilities of every step, each a smooth function of the corresponding rate parameter and equal to unity at nominal. Reweighting the stored history in this way is the importance-weight expression of the change of rates, and it is differentiable in the cascade parameters without re-running the cascade. It is closely related to the score-function construction for stochastic computation graphs [@Foerster:2018dice]: there the derivative of an expectation is obtained from the log-probability of the realised choices, whereas here the full likelihood ratio of each stored history is written down directly. The finite parameter dependence is therefore available explicitly, and its derivatives at any $\bm\theta$ follow by automatic differentiation.

*The step probabilities.* A propagating hadron advances in small steps. At each step the nucleons within reach are candidates, and the hadron interacts with the closest of them with probability $$p_0 = \exp(-a), \qquad a = \frac{\pi b^{2}}{\sigma_{\rm tot}},$$ where $b$ is the impact parameter to that nucleon and $\sigma_{\rm tot}$ the total cross section there. A rate parameter enters through $\sigma_{\rm tot}$ and so has two distinct effects. First, it changes *whether* the hadron interacts: rescaling the total by a factor $g$ maps $a \to a/g$ and gives an interaction-probability factor $p_g/p_0$ on a step that interacted and a survival-probability factor $(1-p_g)/(1-p_0)$ on one that did not, with $p_g = \exp(-a/g)$. Second, it changes *which* channel occurred, contributing $s_{\rm realised}/g$ on a step that interacted. A common rescaling of every channel leaves the second factor at unity but not the first, which is the mean-free-path effect.

*Pion channels.* A pion may scatter elastically, charge exchange, be absorbed on a nucleon pair, or convert to $\eta N$; the four parameters $s^{\rm el}_{\pi N}$, $s^{\rm cex}_{\pi N}$, $s_{\rm abs}^{\pi}$ and $s_{\rm conv}$ scale those four rates respectively, and $$\begin{aligned}
g \;=\; 1
&+ (s_{\rm abs}^{\pi}-1)\,f_{\rm abs}
+ (s^{\rm el}_{\pi N}-1)\,f_{\rm el}
\nonumber\\
&+ (s^{\rm cex}_{\pi N}-1)\,f_{\rm cex}
+ (s_{\rm conv}-1)\,f_{\rm conv},
\end{aligned}$$ with $f_i$ the fraction of the total cross section carried by channel $i$ at that step. Written in this form $g$ is exactly unity at nominal in any precision, which matters because $\exp(-a/g)$ amplifies any error in $g$. A pion converted through $\pi N\to\eta N$ produces a propagating $\eta$, which may subsequently back-convert to a pion or leave the nucleus; the strangeness-producing branch is treated as terminal. The underlying cross sections are those of ACHILLES: the ANL--Osaka amplitudes of Sec. [\[sec:adonis_amplitudes\]](#sec:adonis_amplitudes){reference-type="ref" reference="sec:adonis_amplitudes"} for meson--baryon scattering [@Nakamura:2015rta], and the optical-potential model of Oset and Salcedo for absorption [@Oset:1987re], in which the pion is absorbed through the imaginary part of its self-energy in nuclear matter.

*Nucleon channels.* A nucleon may scatter elastically or inelastically, the latter proceeding through $NN \to N\Delta$ with the $\Delta$ decaying immediately to $N\pi$; this is the channel that degrades fast nucleons and creates pions inside the nucleus. Both rates are resolved by isospin pair, since $pp$, $pn$ and $nn$ cross sections differ, giving six parameters $s^{\rm el}_{NN,ij}$ and $s^{\rm inel}_{NN,ij}$ that act only on steps of the matching pair, with $g = s^{\rm el}(1-f_{\rm inel}) + s^{\rm inel} f_{\rm inel}$. The elastic cross section follows the GiBUU parametrisation [@Buss:2011mx] and the inelastic one the $NN \to N\Delta$ model of Dmitriev and Sushkov [@Dmitriev:1986st].

*Charge exchange.* The last cascade parameter is not a rate but a probability. When a proton and a neutron scatter elastically the outgoing pair may or may not exchange identity, and ACHILLES assigns the two outcomes equal weight. $f^{\rm cex}_{NN}$ varies that split, contributing $f^{\rm cex}_{NN}/0.5$ on a step that exchanged and $(1-f^{\rm cex}_{NN})/0.5$ on one that did not. Identical pairs cannot exchange, so $pp$ and $nn$ steps are unaffected and carry no factor. Its nominal value is $0.5$ rather than unity because it is a fraction, not a scale.
