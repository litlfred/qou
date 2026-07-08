<!-- FILE_START: large-scale-intro.md -->
Strutinsky's shell correction expresses the nuclear residue as a categorical sum. At macroscopic scales, this same residue structure surfaces in CMB anisotropy, gravitational coupling, and topological defects.

This section begins with the cosmic microwave background. The remark "CMB non-uniformity from $q$-torsion" attributes the angular power spectrum to a $q$-torsion contribution. The "CMB torsion data" block records the measured anisotropies against which we fit this prediction.

We then examine the gravitational sector. The remark "Gravity as emergent substrate geometry" frames Newton's constant as an emergent quantity. The central proposition — "Newton's $G$ as the universal-residue prefactor of the unified mass formula" — identifies $G$ as a residue prefactor, a result the remaining blocks build upon. The remark "Closed $q$-rational form of $G_q$ and Planck-unit consistency" writes $G_q$ in closed $q$-rational form and verifies Planck-unit consistency. The "Gravity emergent data" block collects the numerical fits.

The section closes with the defect spectrum and the Navier–Stokes connection. The remark "Topological signatures in large-scale structure" and the "Topological defects data" block identify candidate defect signatures in galaxy-cluster surveys. The remark "Physical signatures of the Navier--Stokes blow-up: intermittency, GRBs, CMB anomalies" packages the fluid-dynamics interface for use in the nuclear-stability section. The same intermittency signature recurs at nuclear scales when the substrate locally approaches golden-ratio degeneration.

_(draft.)_
<!-- FILE_END: large-scale-intro.md -->

<!-- FILE_START: cmb-q-torsion.md -->
In the Descartes universe ([Descartes universe](#thm:descartes)), the negative Euler characteristic $\chi(\mathcal{S}) = -6$ forces a non-trivial distribution of angular modes across the CR manifold ([Descartes CMB](#rem:cmb-photon-color-content)). The $q$-torsion leaves ([$q$-torsion leaf](#ex:q-torsion-leaf)) imprint a characteristic pattern on the CMB that deviates from the statistically isotropic Gaussian field predicted by $\Lambda$CDM. Specifically, the $q$-deformed Reeb flow ([$q$-Reeb flow](#ex:q-reeb-flow)) introduces torsion into the temperature and polarisation multipoles, producing preferred spiral directions in the $B$-mode spectrum.
<!-- FILE_END: cmb-q-torsion.md -->

<!-- FILE_START: gravity-emergent.md -->
In the QOU framework, general relativity emerges as the substrate geometry of the CR manifold ([GR substrate geometry](#rem:gr-substrate-geometry)). The quantum-weighted stress-energy tensor $T_{\mu\nu}^{(q)}$ introduces $q$-dependent corrections to the Einstein field equations. This formally realises gravity as an information-theoretic phenomenon.
<!-- FILE_END: gravity-emergent.md -->

<!-- FILE_START: gravity-spectral-prefactor.md -->
*Working over $A = H_n(R, q)$, the universal curvature-rank tail $\mathfrak{m}^{\geq 4}_{q,\mathcal{K}}(\mathcal{T})$ of the unified mass formula ([universal residue](#prop:plancherel-term-7-formulation)) carries a stratum-dependent prefactor:*

$$
  \alpha \;=\; m_e \cdot 8\,G,
$$

*where $G$ is Newton's gravitational constant in Planck units ($G_{\mathrm{Planck}} = 1$). Equivalently, the dimensionless gravitational coupling at substrate parameter $q$ is:*

$$
  G_q \;=\;
  \frac{\alpha(q)}{8\, m_e}
  \;=\;
  \frac{1}{8\, m_e}
  \cdot \lim_{k \to \infty} \frac{\mathfrak{m}^{\geq k}_{q,\mathcal{K}}(\mathcal{T})}
                                   {\sum_{j \geq k} \Phi_j(\mathcal{K}, \mathcal{T})}
  \,\in\, R,
$$

*the limiting ratio of the deep-tower mass to the Plancherel-weighted character residue.*

**Archimedean specialisation (§7c).** This block operates on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs: real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The generic categorical and $q$-deformation identities it draws on remain valid over an abstract coefficient ring. Only their archimedean realisation is specialised here.
<!-- FILE_END: gravity-spectral-prefactor.md -->

<!-- FILE_START: gravity-spectral-prefactor-interpretation.md -->
**Interpretation.**

The dimensionless coupling $8G/m_e^{-2}$ functions as the universal prefactor. It evaluates to the identical constant for every braid $\beta_\mathcal{K}$ extracted from the deep-tower Plancherel residue. In the QOU framework, gravity is the macroscopic-stratum signature of the categorical mass functional. At high curvature-rank, no specific knot structure survives. Only the universal Frobenius co-Casimir tail remains. Its normalisation defines $G$.
<!-- FILE_END: gravity-spectral-prefactor-interpretation.md -->

<!-- FILE_START: g-q-closed-form.md -->
**Question.** Does the universal-residue prefactor $\alpha = m_e \cdot 8 G$ ([gravity spectral prefactor](#prop:gravity-spectral-prefactor)) fix $G$ as a numerical constant, or does $G$ inherit a closed $q$-rational form from the substrate parameter $q$? Both faces admit a sharp answer.

**Closed $q$-rational form (information face).**

The $q$-Yang–Mills–Levi variation ([gravitational constant](#def:gravitational-constant)) yields $G$ as the ratio of $c_q^3 \hbar_q$ to the cumulative jet-tower entropy $S_{\mathrm{cell}}(q) = (q-1)^2/q^3$. Substituting $c_q = 1/(q-1)$ and $\hbar_q = (q-1)/q$ gives:

$$
  G_q
  \;=\;
  \frac{c_q^3 \cdot \hbar_q}{S_{\mathrm{cell}}(q)}
  \;=\;
  \frac{1/(q-1)^3 \cdot (q-1)/q}{(q-1)^2/q^3}
  \;=\;
  \frac{q^2}{(q-1)^4}.
$$

This strictly $q$-rational expression in $\mathbb{Q}(q)$ requires no transcendental input and zero fitted coefficients. It is the $q$-natural form of $G$, prior to any unit conversion (Planck or SI).

**Planck-unit identity.**

Newton's constant in Planck units is the dimensionless ratio $G_{\mathrm{Planck}} = G_q \cdot (\hbar_q / c_q)^2$. With $\hbar_q / c_q = (q-1)^2/q$, we compute:

$$
  G_{\mathrm{Planck}}
  \;=\;
  \frac{q^2}{(q-1)^4}
  \cdot
  \left(\frac{(q-1)^2}{q}\right)^2
  \;=\;
  \frac{q^2}{(q-1)^4}
  \cdot
  \frac{(q-1)^4}{q^2}
  \;=\;
  1
$$

This holds identically in $\mathbb{Q}(q)$ for every $q \neq 0, 1$. The algebraic identity is verified in Lean as `gravitational_planck_eq_one` (file [gravitational-constant.lean](#def:gravitational-constant)).

**Consequence for the spectral prefactor.**

Substituting $G_{\mathrm{Planck}} = 1$ into $\alpha = m_e \cdot 8 G$ ([gravity spectral prefactor](#prop:gravity-spectral-prefactor)) yields the Planck-unit relation:

$$
  \alpha_{\mathrm{Planck}}(q)
  \;=\;
  8\, m_e(q).
$$

The electron mass $m_e(q)$ and the Plancherel-weighted residue $\sum_{k \geq 4}\Phi_k$ carry the entire $q$-dependence of the universal-residue prefactor in Planck units. $G$ itself contributes no further $q$-dependence; the Planck normalisation exactly cancels its $q$-rational content.

**Reconciling the two faces.**

The two derivations of $G$ in this folio are dual, not competing.

| Face | Source | Closed form | Planck value |
| --- | --- | --- | --- |
| Categorical (spectral) | Plancherel residue $\mathfrak{m}^{\geq 4}_{q,\mathcal{K}}$ at depth $\geq 4$ | $\alpha/(8 m_e)$ | $1$ |
| Information (variational) | $q$-YM–Levi action, jet-tower entropy | $q^2/(q-1)^4$ | $1$ |

The categorical face sets $G$ as the universal-residue prefactor of the deep-tower stratum. The information face sets $G$ as the information-geometric coupling of the substrate. Both derivations reduce to $G_{\mathrm{Planck}} = 1$ identically in $q$. The two faces are algebraically consistent without any calibration condition at $q_0$.

**Empirical anchor.**

Newton's constant in SI units ($G_{\mathrm{Newton}} \approx 6.674 \times 10^{-11}\, \mathrm{m^3\, kg^{-1}\, s^{-2}}$) establishes the Planck length, mass, and time triple via $\ell_P = \sqrt{\hbar G / c^3}$, $m_P = \sqrt{\hbar c / G}$, and $t_P = \sqrt{\hbar G / c^5}$. In QOU units, the conversion $(\hbar_q / c_q)^2 = (q-1)^4/q^2$ absorbs these quantities. The SI value of $G$ functions strictly as the human-scale rescaling that maps $\ell_P, m_P, t_P$ onto metres, kilograms, and seconds. The empirical $G_{\mathrm{Newton}}$ therefore enters as a unit-system datum, not as a fit parameter on $q$. The lepton-mass cross-check ([substrate consistency window](#prop:substrate-consistency-window)) fixes the substrate value $q_0 = 1.109978595554181\ldots$ (50 dps), independent of gravity.

**Summary.**

In $q$-natural units, $G_q = q^2/(q-1)^4$. In Planck units, $G_{\mathrm{Planck}} = 1$ identically for all $q \neq 0, 1$. The universal-residue prefactor reduces to $\alpha_{\mathrm{Planck}}(q) = 8 m_e(q)$ with no residual $q$-dependence in $G$.
<!-- FILE_END: g-q-closed-form.md -->

<!-- FILE_START: topological-defects.md -->
The $\mathrm{SO}(3)$ holonomy of the bulk bundle ([$\mathbb{C}$-quantum universe](#ex:c-quantum-universe)) and the monodromy fixed points of the ([quantum characteristic classes](#def:quantum-characteristic-classes)) may leave topological imprints on the large-scale distribution of matter. Such imprints include preferred filamentary alignments or voids correlated with the brane tower structure ([recursive brane tower](#def:recursive-brane-tower)).
<!-- FILE_END: topological-defects.md -->

<!-- FILE_START: ns-blowup-physical-evidence.md -->
The QOU framework predicts that classical Navier--Stokes admits finite-time blow-up where the enstrophy transfinite $\mathcal{Z}_q \asymp \varepsilon^{-4/3}$ outruns the mass-gap infinitesimal $\Delta_q \asymp \varepsilon^3$ ([NS surreal bound](#rem:ns-surreal-bound), [blowup as Yekutieli lifting obstruction](#prop:blowup-yekutieli)). We treat the mathematical infinity not as a breakdown, but as the moment where the classical approximation $q = 1$ reverts to the underlying quantum substrate $q > 1$.

## Physical meaning of a blow-up

At a finite-time singularity $T^\ast$ of the classical NS flow, the velocity gradient $|\nabla u|$ diverges in any $L^2_q$-bound sense. In the QOU substrate interpretation:

- **The continuum shatters.** The classical $q = 1$ approximation fails to contain the vorticity cascade. The surreal squeeze $\mathcal{Z}_q > \Delta_q$ forbids any dissipation path at $\varepsilon = 0$.
- **Substrate reversion.** The region around the singularity is forced to leave the classical standard-part ([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon)) and operate at $\varepsilon > 0$ on the underlying braided monoidal substrate. The fluid briefly reveals its knot-theoretic interior.

## Predicted physical signatures

### A. Turbulence intermittency

Standard homogeneous-isotropic turbulence exhibits fat-tailed velocity-increment distributions ("intermittency") that Kolmogorov 1941 scaling cannot explain. The framework predicts these fat tails are the statistical residue of near-blow-up events regularised by the underlying substrate. Each intermittent burst is a local excursion into $\varepsilon > 0$ before the cascade is re-absorbed.

Quantitative prediction: Along the Leray self-similar profile ([Leray profile](#prop:leray-profile)), the distribution of velocity increments $\delta u_r$ at separation $r$ satisfies $\ordw(\delta u_r) = -\tfrac{r + 1}{3} \ordw(d)$ in surreal-order notation ([Big-O via $\ordw$](#rem:conway-normal-form)). Classical intermittency exponents are the standard parts of these surreal orders.

### B. High-energy astrophysical matter creation

In the knot-braid particle model ([particle interactions](#chap:particle-interactions)), particles are closed braids. Matter creation corresponds to braid composition. A near-blow-up event concentrates enough crossing energy to braid vacuum modes into matter. For gamma-ray bursts (GRBs), the matter density in the prompt phase exceeds classical dissipation limits. This corresponds to the surreal-squeeze regime where $\mathcal{Z}_q > \Delta_q$. The substrate momentarily re-braids vacuum photons into pair-production channels. This manifests as a characteristic hadron/lepton yield whose ratio tracks the $q$-Hecke branching of [Hecke algebra from braiding](#rem:hecke-algebra-from-braiding).

### C. CMB non-Gaussianities

If the inflationary epoch traversed a regime where classical NS regularity failed (an early cosmological blow-up), the CMB would carry topological defects as scars of substrate reversion:
- Non-Gaussian patches in the CMB temperature map at scales correlated with the surreal order of the early-universe Reeb period.
- Quadrupole and octupole anomalies matching the $\chi = -6$ topology of Bring's curve ([Descartes universe](#chap:brings-surface)).
- Cross-correlation with $q$-torsion data ([CMB $q$-torsion](#rem:cmb-q-torsion)).

### D. Laboratory-accessible probes

- **BEC vortex reconnection events** ([BEC vortex data](#rem:bec-vortex-data)): The near-blow-up moment at a vortex reconnection produces a sharp substrate-reversion signature detectable as a transient violation of classical helicity conservation.
- **High-Reynolds-number laboratory turbulence:** Intermittency exponents match the surreal-order predictions of Section A to leading standard-part order.

## Quantitative handles

The table below pins each qualitative prediction to a concrete observational handle from Chapter 7:

| Signature | QOU data row | Quantitative anchor |
|---|---|---|
| Intermittency exponent deviations | [CMB $q$-torsion data](#sec:cmb-torsion-data) | Structure-function scaling $\langle (\delta u_r)^p \rangle \asymp r^{\zeta_p}$ with $\zeta_p$ a surreal-order sequence |
| GRB hadron/lepton yield | [BEC vortex data](#rem:bec-vortex-data) | Ratio set by $q$-Hecke branching of [Hecke algebra from braiding](#rem:hecke-algebra-from-braiding) |
| CMB non-Gaussianity patches | [CMB $q$-torsion data](#sec:cmb-torsion-data) | Angular cross-correlation with $\chi = -6$ topology; low-$\ell$ quadrupole/octupole anomalies |
| BEC vortex reconnection signature | [BEC vortex data](#rem:bec-vortex-data) | Transient helicity-conservation violation at reconnection events |

Each row is falsifiable. A null result on the specific observable disconfirms the surreal-squeeze interpretation of the corresponding millennium problem. Finite intermittency exponents inconsistent with any surreal-order scaling disconfirm the NS-blowup reading of [NS surreal bound](#rem:ns-surreal-bound).

## Physical finiteness of the mathematical blow-up

In classical PDE theory, blow-up means $|\nabla u| \to \infty$. In the QOU framework, this means the classical limit is the wrong asymptotic object and the underlying $q > 1$ substrate must be used instead. The surreal inequality $\mathcal{Z}_q > \Delta_q$ ([NS surreal bound](#rem:ns-surreal-bound)) is strict in $\mathbb{R}(\varepsilon)$ but becomes a standard-real comparison under the standard-part map only where the cascade has been re-absorbed. Blow-up is the failure of the standard-part map to commute with time evolution.

## Relation to the other millennium problems

The substrate-reversion mechanism underlies every physical manifestation of the millennium squeeze ([millennium unification](#rem:millennium-unification)):
- **RH reversion:** A hypothetical drifted zero requires a spectral jump similar to a localised substrate reversion. No drifted zero is observed empirically.
- **Collatz reversion:** The non-existence of rogue cycles is the arithmetic version of the energy-budget bound.
- **P vs NP reversion:** The loss of $q$-substrate efficiency under classical compression is the complexity-theoretic analogue.

In each case, the physical impossibility of the classical pathology is the non-existence of a substrate channel capable of carrying the transfinite surplus.
<!-- FILE_END: ns-blowup-physical-evidence.md -->

