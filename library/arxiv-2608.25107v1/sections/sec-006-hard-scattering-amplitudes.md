---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_id: sec-006-hard-scattering-amplitudes
section_title: "Hard-scattering amplitudes"
section_number: null
pages: 4-6
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.974
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples — 19 sections: ADoNIS: A Differentiable generatOr; Introduction; Differentiable programming in part"
---
[]{#sec:adonis_amplitudes label="sec:adonis_amplitudes"}

At the interaction vertex the event is weighted by the squared electroweak amplitude for the selected channel: quasi-elastic scattering, governed by the nucleon axial and vector form factors, and resonant pion production, described by the dynamical coupled-channels amplitudes used in ACHILLES [@Isaacson:2022cwh; @Nakamura:2015rta]. Evaluating these amplitudes is computationally expensive and, in the case of the tabulated coupled-channels amplitudes, is not written to be differentiated. Rather than autodifferentiate through that evaluation, [ADoNIS]{.smallcaps} captures its dependence on the parameters of interest at generation time.

*The reweighting construction.* The hadron current is linear in the quantities through which the physics parameters enter, $$H_b \;=\; \sum_i F_i\,H_{i,b},$$ where $b$ labels the nucleon spin combination, the $H_{i,b}$ are unit currents fixed by the event kinematics and spin state, and the $F_i$ encode the parameter dependence: form factors in the quasi-elastic case, and more generally form factors and other amplitude strengths in the resonant case. The squared amplitude is therefore an exact quadratic form in the $F_i$, $$|\mathcal{M}|^2
=
\sum_{ij} F_i F_j\, M_{ij},
\quad
M_{ij}
=
\mathrm{Re}\!\sum_{ab}
(L_a\!\cdot\!H_{i,b})^{*}
(L_a\!\cdot\!H_{j,b}),
\label{eq:adonis_quad}$$ where $L_a$ is the leptonic current for lepton spin combination $a$, and $a$ and $b$ run over the lepton and nucleon spin combinations, respectively. The symmetric matrix $M_{ij}$ depends only on the kinematics, not on the physics parameters, so it is assembled once at generation and stored per event. The vertex factor of Eq. [\[eq:adonis_weight\]](#eq:adonis_weight){reference-type="ref" reference="eq:adonis_weight"} is then $$r^{\rm vertex}_i(\bm\theta)
=
\frac{F(\bm\theta)^{\!\top} M\,F(\bm\theta)}
     {F(\bm\theta_0)^{\!\top} M\,F(\bm\theta_0)},
\label{eq:adonis_vertex}$$ where $\bm\theta_0$ denotes the nominal values. This is an identity rather than a fit: the underlying amplitude calculation is never rerun after generation, the weight is exactly unity at nominal, and because every parameter enters only through the smooth map $\bm\theta \mapsto F$, the construction is exact for arbitrary simultaneous variations and differentiable to any order. For quasi-elastic scattering, $F=\{F_1,F_2,F_A,F_P\}$, so $M$ is $4\times4$; the resonant channel is treated analogously, with separate vector, axial and pion-pole contributions for each partial wave.

Where the parameters of interest affect only a subset of these contributions, the quadratic separates exactly. Splitting $F$ into the components that vary, $F_{\rm var}$, and those held at their nominal values, $F_{\rm fix}$, $$|\mathcal{M}|^2
=
F_{\rm var}^{\!\top} M_{\rm vv} F_{\rm var}
+ 2\,F_{\rm var}^{\!\top} v + c,$$ with $v = M_{\rm vf} F_{\rm fix}^0$ and $c = F_{\rm fix}^{0\top} M_{\rm ff} F_{\rm fix}^0$, so that only $(M_{\rm vv},v,c)$ need be stored. The fixed contributions are compressed into $v$ and $c$ rather than discarded, and the record grows or shrinks with the list of parameters exposed.

*The quasi-elastic current.* Quasi-elastic scattering proceeds through the one-body weak current. For charged-current scattering it takes the standard form [@LlewellynSmith:1971uhs], $$\begin{aligned}
J^\mu = \bar{u}(p')\Big[\,& F_1\gamma^\mu
+ \frac{i F_2}{2m_N}\sigma^{\mu\nu}q_\nu \nonumber\\
&+ F_A\gamma^\mu\gamma_5
+ \frac{F_P}{m_N}q^\mu\gamma_5 \Big] u(p),
\label{eq:adonis_ls}
\end{aligned}$$ with $q$ the four-momentum transfer. Neutral-current elastic scattering has the same four current structures, so the quadratic construction of Eq. [\[eq:adonis_quad\]](#eq:adonis_quad){reference-type="ref" reference="eq:adonis_quad"} applies unchanged; only the electroweak combinations entering their coefficients differ. In particular, the vector contributions depend on different proton and neutron form-factor combinations, while the axial contribution changes sign between proton and neutron. Strange form factors are not included in ACHILLES and are therefore also absent from [ADoNIS]{.smallcaps}.

The vector form factors $F_1$ and $F_2$ describe the charge and magnetisation distributions of the nucleon and are fixed by electron scattering; $F_A$ and $F_P$ are the axial and induced pseudoscalar form factors. In addition to the parameters entering these form factors themselves, [ADoNIS]{.smallcaps} introduces two overall scaling parameters: $S_V^{\rm QE}$ scales $F_1$ and $F_2$ together, while $S_A^{\rm QE}$ scales $F_A$ and $F_P$ together.

*Vector form factors.* $F_1$ and $F_2$ are built from the Sachs electric and magnetic form factors, $$F_1 = \frac{G_E + \tau G_M}{1+\tau}, \qquad
F_2 = \frac{G_M - G_E}{1+\tau},$$ with $\tau = Q^2/4m_N^2$. These are taken from the Kelly parametrisation [@Kelly:2004hm], in which each Sachs form factor is a ratio of polynomials in $\tau$, $$G(\tau) \;=\; \frac{1 + a_1\tau}{1 + b_1\tau + b_2\tau^2 + b_3\tau^3},$$ fitted to elastic electron--proton data and constructed to fall with the correct power of $Q^2$ at large momentum transfer. The four parameters $\mu_p$, $\mu_n$, $G_E^p$ and $G_E^n$ scale $G_M^p$, $G_M^n$, $G_E^p$ and $G_E^n$ individually, and enter Eq. [\[eq:adonis_vertex\]](#eq:adonis_vertex){reference-type="ref" reference="eq:adonis_vertex"} through the linear relations above.

*Axial form factor.* The axial form factor is taken as a $z$-expansion, the model-independent parametrisation that maps the analytic domain of $F_A(Q^2)$ onto the unit disc, $$z(Q^2) = \frac{\sqrt{t_c+Q^2}-\sqrt{t_c-t_0}}
              {\sqrt{t_c+Q^2}+\sqrt{t_c-t_0}}, \qquad
F_A = \sum_{k} a_k\,z^k,$$ with $t_c = 9m_\pi^2$ the three-pion production threshold and $t_0$ a fixed expansion point. The coefficients are those of Ref. [@Meyer:2016oeg], obtained from neutrino--deuteron data. Because this form has no axial mass, $M_A^{\rm QE}$ acts instead through the ratio of two dipoles, $$\begin{aligned}
F_A^{\rm dip}(Q^{2};M_A) &= \frac{-g_A}{\left(1+Q^{2}/M_A^{2}\right)^{2}},
\nonumber\\
r(Q^{2};M_A) &= \frac{F_A^{\rm dip}(Q^{2};M_A)}
                     {F_A^{\rm dip}(Q^{2};1.0~{\rm GeV})},
\end{aligned}$$ evaluated at the momentum transfer $Q^2$ of each event, which is stored in the event record, and multiplying the axial block in Eq. [\[eq:adonis_vertex\]](#eq:adonis_vertex){reference-type="ref" reference="eq:adonis_vertex"}. It therefore deforms the axial $Q^2$ dependence about the nominal in the direction an axial mass would, and is unity at $M_A=1.0$ GeV by construction. Only $M_A^2$ appears, so the ratio is even in $M_A$. The induced pseudoscalar follows from $F_A$ by the pion-pole dominance relation $F_P = 2m_N^2 F_A/(Q^2+m_\pi^2)$ and is therefore carried along by both $S_A^{\rm QE}$ and $M_A^{\rm QE}$.

*Resonant vertex.* Single-pion production is described by the ANL--Osaka dynamical coupled-channels model [@Nakamura:2015rta]. Rather than summing independent Breit--Wigner resonances, it solves coupled scattering equations for the meson--baryon channels $\pi N$, $\eta N$, $K\Lambda$ and $K\Sigma$ simultaneously, so that resonant and non-resonant contributions and their interference emerge from one unitary amplitude. Only $\pi N$ is produced at the interaction vertex; the remaining channels enter through the coupled-channel solution rather than as generated final states. The amplitude is decomposed into partial waves labelled $L_{2I\,2J}$ by the orbital angular momentum, isospin and total angular momentum of the pion--nucleon pair; fourteen are tabulated, $$\begin{aligned}
&S_{11},\; S_{31},\; P_{11},\; P_{13},\; P_{31},\; P_{33},\; D_{13},\\
&D_{15},\; D_{33},\; D_{35},\; F_{15},\; F_{17},\; F_{35},\; F_{37},
\end{aligned}$$ each containing the resonances with the corresponding quantum numbers. All fourteen contribute to the nominal [ADoNIS]{.smallcaps} prediction, and each can carry an independent differentiable normalisation because the amplitude is linear in that contribution. For simplicity, the studies below vary only $S_\Delta$, which scales the $P_{33}$ partial wave that contains the $\Delta(1232)$ resonance and dominates pion production at accelerator energies.

Beyond the partial-wave normalisations, $F_{\rm pp}$ scales the longitudinal pion-pole term of the charged-current resonant current, analogous to the induced pseudoscalar contribution discussed above. The axial current is controlled by $C_5^A$ and $M_A^{\rm RES}$: the former scales its overall strength, while the latter modifies its $Q^2$ dependence using the same dipole-ratio construction introduced for $M_A^{\rm QE}$.

Neutral-current resonant production uses the same DCC decomposition. The partial-wave normalisations and the axial parameters $C_5^A$ and $M_A^{\rm RES}$ are common to charged- and neutral-current production. The differences lie in the electroweak current: the vector contribution uses the corresponding neutral-current combination of isovector and isoscalar components, and the pion-pole term is absent. Consequently, $F_{\rm pp}$ affects only charged-current resonant events.

In this way, the event-dependent ingredients of the amplitude are evaluated once at generation, while its dependence on the axial masses, form-factor scales and strengths remains explicit and can be differentiated exactly at negligible fit-time cost.
