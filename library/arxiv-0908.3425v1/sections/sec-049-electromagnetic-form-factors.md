---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector"
section_id: sec-049-electromagnetic-form-factors
section_title: "Electromagnetic form factors"
section_number: null
pages: 68-72
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.951
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Results in the One-Nucleon Sector — We provide an introduction to the basic concepts of chiral perturbation theory and discuss some recent"
---
[]{#subsectionemff label="subsectionemff"} Imposing the relevant symmetries such as translational invariance, Lorentz covariance, the discrete symmetries, and current conservation, the nucleon matrix element of the electromagnetic current operator ${\cal J}^\mu(x)$, $${\cal J}^{\mu}(x)
=\frac{2}{3}\,\bar{u}(x)\gamma^{\mu}u(x)
-\frac{1}{3}\,\bar{d}(x)\gamma^{\mu}d(x),$$ can be parameterized in terms of two form factors, $$\label{H1:emff:empar} \langle N(p',s')|{\cal J}^{\mu}(0)|N(p,s)\rangle=
\bar{u}(p',s')\left[F_1^N(Q^2)\gamma^\mu
+i\frac{\sigma^{\mu\nu}q_\nu}{2m_p}F_2^N(Q^2) \right]u(p,s),\quad
N=p,n,$$ where $q=p'-p$, $Q^2=-q^2$, and $m_p$ is the proton mass. At $Q^2=0$, the so-called Dirac and Pauli form factors $F_1$ and $F_2$ reduce to the charge and anomalous magnetic moment in units of the elementary charge $e$ and the nuclear magneton $e/(2m_p)$, respectively, $$F_1^{p}(0)=1,\quad F_1^{n}(0)=0,\quad F_2^{p}(0)=1.793,\quad
F_2^{n}(0)=-1.913.$$ The Sachs form factors $G_E$ and $G_M$ are linear combinations of $F_1$ and $F_2$, $$G_E^N(Q^2)=F_1^N(Q^2)-\frac{Q^2}{4m_p^2}F_2^N(Q^2),\quad
G_M^N(Q^2)=F_1^N(Q^2)+F_2^N(Q^2), \quad N=p,n,$$ and, in the non-relativistic limit, their Fourier transforms are commonly interpreted as the distribution of charge and magnetization inside the nucleon. For a covariant interpretation in terms of the transverse charge density see Refs. [@Miller:2007uy], [@Carlson:2007xd]. The description of the electromagnetic form factors of the nucleon presents a stringent test for any theory or model of the strong interactions (see, e.g., Ref. [@Perdrisat:2006hj] for a recent review).

In the framework of chiral perturbation theory, the electromagnetic form factors were calculated in the early relativistic approach [@Gasser:1987rb], the heavy-baryon approach [@Bernard:1992qa], [@Fearing:1997dp], the small-scale expansion [@Bernard:1998gv], the infrared regularization [@Kubis:2000zd], and the EOMS scheme [@Fuchs:2003ir]. All these calculations have in common that they fail to describe the proton and nucleon form factors for momentum transfers beyond $Q^2\sim 0.1\, \mbox{GeV}^2$. Moreover, up to and including ${\cal O}(q^4)$, the most general effective Lagrangian provides sufficiently many independent parameters such that the empirical values of the anomalous magnetic moments and the charge and magnetic radii are fitted rather than predicted. Figure [1](#G_ohne){reference-type="ref" reference="G_ohne"} shows the Sachs form factors in the momentum transfer region $0\,{\rm GeV^2}\le Q^2\le 0.4\,{\rm GeV^2}$ in the EOMS scheme and the reformulated infrared regularization [@Schindler:2005ke].

<figure id="G_ohne">
<div class="center">

</div>
<figcaption><span id="G_ohne" label="G_ohne"></span> The Sachs form factors of the nucleon in manifestly Lorentz-invariant chiral perturbation theory at <span class="math inline">${\cal O}(q^4)$</span> without vector mesons. Full lines: results in the extended on-mass-shell scheme; dashed lines: results in infrared regularization. The experimental data are taken from Ref. <span class="citation" data-cites="Friedrich:2003iz"></span>.</figcaption>
</figure>

In Ref. [@Kubis:2000zd] it was shown that the inclusion of vector mesons can result in the re-summation of important higher-order contributions. In standard ChPT, such vector meson contributions manifest themselves in terms of the values of the low-energy coupling constants. Symbolically, the contributions to certain LECs originate from the expansion of the vector-meson propagator, $$\frac{1}{q^2-M_{V}^2}=-\frac{1}{M_{V}^2}
\left[1+\frac{q^2}{M_{V}^2}+\left(\frac{q^2}{M_{V}^2}\right)^2+\mathcal{O}(q^6)\right]$$ combined with the relevant vector-meson vertices. However, diagrams with internal vector-meson lines *inside* loops were not considered, because a generalization of ChPT which fully includes the effects of vector mesons as intermediate states in loops was not yet available [@Kubis:2000zd]. On the other hand, the EOMS renormalization scheme of Ref. [@Fuchs:2003qc] and the reformulated version of infrared regularization of Ref. [@Schindler:2003xv] both allow to include virtual vector mesons *systematically* in the region of the applicability of baryon chiral perturbation theory [@Fuchs:2003sh] (see also Ref. [@Bruns:2008ub]). The standard power counting determines which diagrams (including diagrams with vector mesons appearing in loops) should be taken into account to a given order in the chiral expansion.

In Ref. [@Schindler:2005ke] the electromagnetic form factors were calculated with the $\rho$, $\omega$, and $\phi$ mesons as explicit degrees of freedom. In the vector-field representation of Ref. [@Ecker:1989yg] the $\rho$ meson is represented by $\rho^{\mu}=\rho^{\mu}_i\tau_i$ and the $\omega$ and $\phi$ mesons by $\omega^\mu$ and $\phi^\mu$, respectively. The coupling of the vector mesons to pions and external fields is at least of ${\cal O}(q^3)$, $$\label{PionLagrange}
   \mathcal{L}_{{\pi}V}^{(3)}=-f_\rho\mbox{Tr}(\rho^{\mu\nu}f^+_{\mu\nu})
-f_\omega\omega^{\mu\nu}f^{(s)}_{\mu\nu}-f_\phi\phi^{\mu\nu}f^{(s)}_{\mu\nu}+\cdots,$$ where the field strength tensors are given by $$f^{(s)}_{\mu\nu}=\partial_\mu v^{(s)}_\nu-\partial_\nu
v^{(s)}_\mu,\quad
f^+_{\mu\nu}=u^+f^R_{\mu\nu}u+u f^L_{\mu\nu} u^+,$$ with $f^R_{\mu\nu}$ and $f^L_{\mu\nu}$ defined in Eqs. ([\[3:2:3:fr\]](#3:2:3:fr){reference-type="ref" reference="3:2:3:fr"}) and ([\[3:2:3:fl\]](#3:2:3:fl){reference-type="ref" reference="3:2:3:fl"}), respectively. For the case of a coupling to an external electromagnetic potential ${\cal A}_\mu$, the external fields are given by Eq. ([\[2:1:6:rlasu2\]](#2:1:6:rlasu2){reference-type="ref" reference="2:1:6:rlasu2"}). Furthermore, in terms of the connection $\Gamma^\mu$ of Eq. ([\[4:1:2:gamma\]](#4:1:2:gamma){reference-type="ref" reference="4:1:2:gamma"}), we define $$\rho^{\mu\nu}=\nabla^{\mu}\rho^{\nu}-\nabla^{\nu}\rho^{\mu},\quad
    \nabla^{\mu}\rho^{\nu}=\partial^{\mu}\rho^{\nu}+\left[\Gamma^{\mu},\rho^{\nu}\right],$$ and, finally, $$\omega^{\mu\nu}=\partial^\mu\omega^\nu-\partial^\nu\omega^\mu,\quad
\phi^{\mu\nu}=\partial^\mu\phi^\nu-\partial^\nu\phi^\mu.$$ The lowest-order Lagrangian for the coupling to the nucleon is given by $$\label{LagNV0}
   \mathcal{L}_{VN}^{(0)}=\frac{1}{2}\sum_{V=\rho,\omega,\phi}g_V\,\bar{\Psi}\gamma^{\mu}V_{\mu}\Psi,$$ and the ${\cal O}(q)$ Lagrangian reads $$\label{LagNV1}
   \mathcal{L}_{VN}^{(1)}=\frac{1}{4}\sum_{V=\rho,\omega,\phi}G_V
   \bar{\Psi}\sigma^{\mu\nu}V_{\mu\nu}\Psi.$$ The additional power-counting rules state that vertices from $\mathcal{L}_{{\pi}V}^{(3)}$ count as $\mathcal{O}(q^3)$ and vertices from $\mathcal{L}_{VN}^{(i)}$ as $\mathcal{O}(q^i)$, respectively, while the vector-meson propagators count as $\mathcal{O}(q^0)$. The additional diagrams involving vector mesons that contribute in the calculation of the form factors up to and including ${\cal O}(q^4)$ using the Lagrangians of Eqs. ([\[PionLagrange\]](#PionLagrange){reference-type="ref" reference="PionLagrange"}), ([\[LagNV0\]](#LagNV0){reference-type="ref" reference="LagNV0"}), and ([\[LagNV1\]](#LagNV1){reference-type="ref" reference="LagNV1"}) are shown in Fig. [2](#Dia_mit){reference-type="ref" reference="Dia_mit"}.

<figure id="Dia_mit">
<div class="center">

</div>
<figcaption><span id="Dia_mit" label="Dia_mit"></span> Feynman diagrams including vector mesons that contribute to the electromagnetic form factors of the nucleon up to and including <span class="math inline">${\cal O}(q^4)$</span>. External leg corrections are not shown. Solid, wiggly, and double lines refer to nucleons, photons, and vector mesons, respectively. The numbers in the interaction blobs denote the order of the Lagrangian from which they are obtained. The direct coupling of the photon to the nucleon is obtained from <span class="math inline">${\cal L}_{\pi N}^{(1)}$</span> and <span class="math inline">${\cal L}_{\pi
N}^{(2)}$</span>.</figcaption>
</figure>

The parameters of the vector-meson Lagrangian of Eq. ([\[PionLagrange\]](#PionLagrange){reference-type="ref" reference="PionLagrange"}) for the coupling to external fields have been taken from Ref. [@Ecker:1989yg], and those of Eqs. ([\[LagNV0\]](#LagNV0){reference-type="ref" reference="LagNV0"}) and ([\[LagNV1\]](#LagNV1){reference-type="ref" reference="LagNV1"}) for the coupling of vector mesons to the nucleon from the dispersion relations of Refs. [@Mergell:1995bf], [@Hammer:2003ai].

As expected on phenomenological grounds, the quantitative description of the data has improved considerably for $Q^2\geq 0.1$ GeV$^2$ (see Fig. [3](#H1:emff:G:neu){reference-type="ref" reference="H1:emff:G:neu"}).

<figure id="H1:emff:G:neu">
<div class="center">

</div>
<figcaption><span id="H1:emff:G:neu" label="H1:emff:G:neu"></span> The Sachs form factors of the nucleon in manifestly Lorentz-invariant chiral perturbation theory at <span class="math inline">${\cal
O}(q^4)$</span> including vector mesons as explicit degrees of freedom. Full lines: results in the extended on-mass-shell scheme; dashed lines: results in infrared regularization. The experimental data are taken from Ref. <span class="citation" data-cites="Friedrich:2003iz"></span>.</figcaption>
</figure>

The small difference between the two renormalization schemes is due to the way how the regular higher-order terms of loop integrals are treated. Numerically, the results are similar to those of Ref. [@Kubis:2000zd]. Due to the renormalization condition, the contribution of the vector-meson loop diagrams either vanishes (IR) or turns out to be small (EOMS). Thus, in hindsight our approach puts the traditional phenomenological vector-meson-dominance model on a more solid theoretical basis. In the sense of a strict chiral expansion in terms of small external momenta $q$ and quark masses $m_q$ at a fixed ratio $m_q/q^2$ [@Gasser:1983yg], up to and including ${\cal O}(q^4)$ the results with and without explicit vector mesons are completely equivalent. The additional vector-meson contributions up to this order are compensated by a readjustment of the low-energy constants pertaining to the theory including vector mesons as dynamical degrees of freedom. On the other hand, the inclusion of vector-meson degrees of freedom in the present framework results in a reordering of terms which, in an ordinary chiral expansion, would show up at higher orders beyond ${\cal O}(q^4)$. It is these terms which change the form factor results favorably for larger values of $Q^2$. It should be noted, however, that this re-organization proceeds according to well-defined rules so that a controlled, order-by-order, calculation of corrections is made possible. In contrast to the calculation without vector mesons, the Sachs form factors $G_E^p$, $G_M^p$, and $G_M^n$ now show sufficient curvature to generate a more accurate phenomenology for values of $Q^2$, where the ordinary chiral expansion to the same order is no longer reliable.
