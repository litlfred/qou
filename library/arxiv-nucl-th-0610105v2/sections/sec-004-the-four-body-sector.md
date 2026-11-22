---
doc_id: arxiv-nucl-th-0610105v2
doc_title: "Universal Properties of the Four-Body System with Large Scattering Length"
section_id: sec-004-the-four-body-sector
section_title: "The Four-Body Sector"
section_number: null
pages: 6-7
source_pdf: 0610105v2.pdf
source_sha256: 5f3bd6d31a419d4d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 1.0
doc_brief: "Universal Properties of the Four-Body System with Large Scattering Length — Few-body systems with large scattering length have universal properties that do not depend on the details of their"
---
[]{#sec:effT:4body label="sec:effT:4body"}

We now turn to the four-body sector. The four-body binding energies are given by the Yakubovsky equations which are a generalization of the Faddeev equations to the four-body system. The full four-body wave function $\Psi$ is first decomposed into Faddeev components, followed by a second decomposition into Yakubovsky components. For identical bosons, one has two Yakubovsky components $\psi_A$ and $\psi_B$. We start from the Yakubovsky equations including a general three-body force in the form written down by Glöckle and Kamada [@Glockle:1993vr]. The full four-body bound state wave function is decomposed into the Yakubovsky components $\psi_A$ and $\psi_B$ via $$\label{eq:yak_wavefunction}
\Psi=(1+(1+P) P_{34})(1+P)\psi_A +(1+P)(1+\tilde{P})\psi_B~,$$

where $P_{ij}$ exchanges particles $i$ and $j$, $P$ is defined in Eq. ([\[eq:defP\]](#eq:defP){reference-type="ref" reference="eq:defP"}), and $\tilde{P}$ is given by $$\tilde{P}=P_{13}P_{24}~.$$

The equations for the two wave function components read:

$$\begin{aligned}
\psi_A &=& G_0 t_{12} P [ (1+P_{34})\psi_A+\psi_B]
+\frac{1}{3}(1+G_0 t_{12})G_0 V_{3} \Psi~, \nonumber \\
\psi_B &=& G_0 t_{12} \tilde{P} [ (1+P_{34})\psi_A+\psi_B]~,
\label{eq:yaku}
\end{aligned}$$

where $t_{12}$ denotes the two-body t-matrix for particles 1 and 2 and $V_3$ is the three-body force defined in Eq. ([\[def:3pot\]](#def:3pot){reference-type="ref" reference="def:3pot"}). Note that the three-body force couples to the full four-body wave function $\Psi$. The factor of one third in front of the three-body force term arises because we insert the full three-body interaction for $V_3$. This is possible since we consider three-body contact interactions which are symmetric under the exchange of any pair of particles.

The renormalization analysis of the four-body system is complicated by the cutoff dependence of the number of bound states in the three-body subsystems. The further the cutoff $\Lambda$ is increased, the more three-body bound states appear. While this has no influence on low-energy three-body observables, it creates an instability in the four-body system which can collapse into a deep three-body bound state plus another particle. This limits cutoff variations to an interval $\Lambda_0 < \Lambda < 
22.7 \,\Lambda_0$ for some $\Lambda_0$, in which the number of three-body bound states remains constant. Despite this restriction, the cutoff can be varied by more than a factor of ten which is sufficient to study the renormalization properties and obtain converged numerical results [@Platter04].

In Ref. [@Yama06], it was pointed out that the calculation of [@Platter04] for the $^4$He tetramer was limited to repulsive three-body forces $\lambda_3 > 0$. The ability to renormalize without a four-body parameter was attributed to a very small probability of the four particles to be close together due to the repulsive three-body force. We note that the sign of the three-body force is cutoff dependent because of the limit cycle behavior of $\lambda_3(\Lambda)$ in Eq. ([\[eq:limcyc\]](#eq:limcyc){reference-type="ref" reference="eq:limcyc"}). In Ref. [@Platter04], we have performed calculations with both attractive and repulsive three-body forces. In particular, the three-body force is attractive for cutoffs close to $\Lambda_0$. However, in this case $\Lambda \sim (mB_4^{(0)})^{1/2}$ and the ground state energy $B_4^{(0)}$ is far from the converged value. The final converged value for $B_4^{(0)}$ was indeed obtained with a repulsive three-body force. The excited state energy $B_4^{(1)}$, however, is already converged at smaller cutoffs where the three-body force is attractive. Increasing the cutoff beyond $22.7 \,\Lambda_0$, where the three-body force is attractive again would require to project out the unphysical deep three-body state that appears in this case. Such a subtraction is beyond the scope of this work.

In the remainder of the paper, we will follow [@Platter04] and not include a four-body parameter in our calculations.
