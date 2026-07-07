<!-- FILE_START: intro-six-term-crystal-isospin-chirality.md -->
We now detail the full six-term mass formula. The formula replaces the phenomenological Bethe-Weizsäcker coefficients with substrate-derived invariants. We trace the isospin-symmetric terms and isolate the structural isospin violations.
<!-- FILE_END: intro-six-term-crystal-isospin-chirality.md -->

<!-- FILE_START: six-term-mass-formula-complete.md -->
**Theorem (the unified six-term mass formula).**
*The categorical mass of the particle $\varrho$ breaks cleanly into six derived terms:*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \underbrace{|\mathrm{tr}_M(T_w)|}_{\text{Term 1}}
  \;+\;
  \underbrace{\sum_{i=0}^{n-2} \Phi_q(|\hat V_i^{\mathrm{full}}|)}_{\text{Term 2}}
  \;+\;
  \underbrace{z^2 \sum_{i < j} \Phi_q(|\hat V_i^{\mathrm{full}} \hat V_j^{\mathrm{full}}|)}_{\text{Term 3}}
  \;+\;
  \underbrace{m_e \cdot \tau(C_{\dim_q})}_{\text{Term 4}}
  \;+\;
  \underbrace{a_K \cdot \mathcal{C}_K}_{\text{Term 5}}
  \;+\;
  \underbrace{\sum_{\ell \geq 2} \frac{\mathrm{Res}_{q = \zeta_\ell}[\cdot]}{q_0 - \zeta_\ell}}_{\text{Term 6}}.
$$

Every term evaluates uniquely from the canonical braid word and substrate parameter. The formulation strictly enforces the Markov trace invariance across all observables. The breakdown identifies exactly the origin of isospin and parity violations. 

Term 1 carries the core topological invariant. Terms 2 and 3 evaluate the specific knot's processing cost on the substrate. Term 4 captures the universal vacuum representation overhead. Term 5 measures the chirality of the knot, separating particles from antiparticles. Term 6 adds the higher-stratum cyclotomic poles.
<!-- FILE_END: six-term-mass-formula-complete.md -->

<!-- FILE_START: six-term-per-derivation-weights.md -->
**Proposition (binding energy decomposition).**
*The atomic binding energy derives directly from the six terms. It requires zero empirical parameter fits:*

$$
  B(Z, N)
  \;=\;
  \underbrace{E_{0,\beta} \cdot \big(T_1^{\rm free} - T_1^{\rm atom}\big)}_{\text{T1 binding}}
  \;+\;
  \underbrace{\alpha \cdot \big((T_2 + T_3)^{\rm atom} - (T_2 + T_3)^{\rm free}\big)}_{\text{T2/T3 binding}}
  \;+\;
  \underbrace{m_e \cdot \big(T_4^{\rm atom} - T_4^{\rm free}\big)}_{\text{T4 binding}}
  \;+\;
  \underbrace{E_{0,\beta} \cdot (a_K - 1) \cdot T_1^{\rm atom}}_{\text{T5 binding}}
  \;+\;
  \underbrace{\big(T_6^{\rm atom} - T_6^{\rm free}\big)}_{\text{T6 binding}}
$$

The scale difference separating $T_1$ from $T_2+T_3$ isolates the weak scale from the hadronic core.
<!-- FILE_END: six-term-per-derivation-weights.md -->

<!-- FILE_START: crystal-isospin-degeneracy.md -->
**Proposition (crystal isospin degeneracy).**
*Let $\beta_A$ be an atomic braid expressed as a finite word of signed generators $\sigma_i^{\pm 1}$. Inverting the sign of any subset of generators leaves the crystal-limit shell-correction sum invariant:*

$$
  S_{\mathrm{crystal}}(\beta_A) \;=\; S_{\mathrm{crystal}}(\beta_A').
$$

The crystal limit $q \to 0$ completely masks generator inversions. It cannot distinguish between proton and neutron structures inside the bare Hecke algebra. Any non-zero mass splitting between isospin mirrors, such as $^3\mathrm{H}$ and $^3\mathrm{He}$, must originate strictly outside the crystal limit or via an asymmetric interface protocol.
<!-- FILE_END: crystal-isospin-degeneracy.md -->

<!-- FILE_START: isospin-mass-split-em-localisation.md -->
**Remark (Coulomb localisation of the isospin split).**
*The empirical mirror-isobar mass split $\mathfrak{m}({}^3\mathrm{H}) - \mathfrak{m}({}^3\mathrm{He}) \approx 0.529\;\mathrm{MeV}$ breaks both Hecke-skein sign-flip invariance and Hopf-antipode invariance. It must therefore be entirely sourced by the Coulomb term.*

The trace tower, co-Casimir, chirality, and shell-correction functionals all respect these structural involutions. The Coulomb charge explicitly breaks them. The categorical separation forces the mass splitting entirely into the electromagnetic sector.
<!-- FILE_END: isospin-mass-split-em-localisation.md -->

<!-- FILE_START: isospin-from-canonical-bowtie.md -->
**Conjecture (isospin-Z/2-anti-symmetric closure).**
*Let $\beta_A$ be an atomic braid using the canonical operator-valued interface $\bowtie_K$. The regularised crystal functional leaves the canonical isospin swap invariant up to a single isospin-Z/2-anti-symmetric residue.*

*This residue resolves precisely to the substrate flavor split evaluated at $q_0$:*

$$
  \frac{\Delta m}{M_N}
  \;=\;
  \frac{\hbar_q^2 \cdot h \cdot [2]_q \cdot (1 + \hbar_q^3)}{3}
  \qquad \text{(305 ppm against CODATA)}.
$$

The interface coefficient $h$ diverges at $q=0$. A regularised Cesàro limit extracts the finite remainder. This separates the isospin-invariant substrate background from the structural isospin violation.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-analytic constructs. Any generic categorical identities remain valid over an abstract coefficient ring.
<!-- FILE_END: isospin-from-canonical-bowtie.md -->
