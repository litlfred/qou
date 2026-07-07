<!-- FILE_START: fundamental-particles-intro.md -->
The unit particle was the simplest defect. We now populate the full elementary spectrum supported by the embeddable-knot generators. The up and down quarks fix the light-quark assignments. The electron, positron, neutrino, and antineutrino (as the mirror unknot $T_{1,0}^{\sigma}$) fix the first-generation leptons. The linking relations tabulate the linking data among these primitives. The $\mathcal{Q}_q$-value imports the $q$-deformed kinematic transition energy from the categorical action difference for use in production vertices.

Particle production is categorical. Breit–Wheeler pair production and quark–antiquark production realise pair creation as a Hecke vertex. The Frobenius Gram matrix and dual construction in $H_3(q)$ select the knot operator that survives Frobenius duality. We build the composite hadrons — meson, proton, and neutron — on this foundation. The proton formation relies on three pair productions and the energy scale $\mathfrak{E}_0$. Left and right trefoils encode electron and positron chirality data via antiparticle crossing reversal.

The stable nucleus packages the nuclear ground state as a Skein energy minimum. Torus knot composites on Bring's surface are stable hadrons. The genus-$4$ classification forces exactly two solutions: $T_{2,9}$ and $T_{3,5}$. These unique torus knots carry the gauge forces. The two-strand spectral completeness theorem over a commutative ring $R$ ensures uniqueness of the scalar gauge coupling on $A \otimes A$. The correction parameters $(\mathfrak{E}_0, \delta_{CS}, \kappa)$ record the current state of the $\alpha_{\mathrm{EM}}$ derivation, including the conjectured Chern–Simons form and the Gram-determinant ratio $\kappa$.

The closing blocks bridge to atomic and nuclear physics. The categorical Bohr radius, the archimedean energy unit $E_{\mathrm{Hartree}}$, and the uniqueness of the archimedean realization functor transport the QED scales through the archimedean wall. The categorical trace ratio and multiplicative chain record the running of $\alpha_{\mathrm{EM}}$ along the generation ladder. The valley of stability emerges as a Diophantine constraint on the integer lattice. Nuclear stability and decay treat this Diophantine valley as the ambient geometry, identifying which transitions across the valley are allowed by the Skein relation.
<!-- FILE_END: fundamental-particles-intro.md -->

<!-- FILE_START: electron-knot.md -->
The **electron** is the trefoil $T_{2,3}$ in the lepton sector. It shares the knot type of the up quark but avoids localization in a color tube.

$$
  e^- =  T_{2,3} \qquad \text{(trefoil, solid ●)}
$$

Environment dictates the distinction between the electron and the up quark. The up quark threads through a color tube of the Bring's surface ([color tube coordinates](#def:color-tube-coordinates)), while the electron orbits the nucleus via Hopf linking without entering the color tubes.

**Visual convention.** We draw the electron as a **solid** trefoil (forward time direction), identical to the up quark. Context (color tube vs. orbital) distinguishes the quark from the lepton.
<!-- FILE_END: electron-knot.md -->

<!-- FILE_START: electron-knot-example.md -->
The electron is the simplest nontrivial torus knot embedding on $\Sigma_4$: the trefoil $\tau(2,3)$. Its Seifert genus is $(2-1)(3-1)/2 = 1 \leq 4$. The trefoil has 3 crossings, carrying 3 units of information content. Its Jones polynomial is:

$$
  J_{\tau(2,3)}(q) = -q^{-4} + q^{-3} + q^{-1}
$$

The mass derives from the quantum dilogarithm at $q \approx 1.110$: $\mathfrak{m}_e = \mathrm{Li}_2(q^{-2})/\hbar_q^2$. This sets the electron mass as the fundamental mass unit. We express all other particle masses as ratios relative to this base.
<!-- FILE_END: electron-knot-example.md -->

<!-- FILE_START: positron-knot.md -->
The positron is the mirror trefoil $T_{2,3}^{\sigma}$ in the lepton sector. It acts as the antiparticle of the electron:

$$
  e^+ =  T_{2,3}^{\sigma}. \qquad \text{(mirror trefoil)}
$$

The positron is topologically identical to the down quark; we distinguish them solely by their environment (orbital versus color tube). It carries reversed crossing chirality. Where the electron has Coulomb charge $Q = -1$, the positron has $Q = +1$.

**Visual convention.** We draw the positron as an outlined trefoil, denoting reversed time direction.

**Time reversal interpretation.** The mirror operation $\sigma$ reverses all crossings. In the Reeb flow, this corresponds to reversing the direction of time ([chirality remark](#rem:chirality-trefoil-electron-positron)). The positron represents an electron traveling backward in time, matching the Feynman–Stueckelberg interpretation.
<!-- FILE_END: positron-knot.md -->

<!-- FILE_START: neutrino-knot.md -->
The neutrino is the unknot $K_{0_1}$.

$$
  \nu =  K_{0_1} \qquad \text{(unknot, circle ○)}
$$

The unknot has Seifert genus $0$, crossing number $0$, and trivial Skein polynomial $J_\nu(q) = 1$. It contributes no hyperbolic volume and hence no bare mass. Neutrino mass derives entirely from vacuum drag, not from knot topology.

**Visual convention.**
We draw the neutrino as a simple circle, distinct from both the solid trefoil (forward-time fermion) and the outlined trefoil (backward-time fermion).

**Properties.**
- **Zero crossing chirality**: $Q(\nu) = 0$. The lack of crossings ensures electrical neutrality.
- **Trivial braiding**: The $R$-matrix acts as the identity on the unknot component. Neutrinos evade the crossing-energy interactions responsible for Coulomb repulsion.
- **Vacuum drag mass**: The neutrino mass $m_\nu \sim \mu_0 \cdot (q - 1)$ is proportional to the baseline vacuum drag, vanishing at $q = 1$.
<!-- FILE_END: neutrino-knot.md -->

<!-- FILE_START: antineutrino-knot.md -->
The **antineutrino** is the mirror unknot $T_{1,0}^{\sigma}$, the antiparticle of the neutrino.

$$
  \nu^{\sigma} =  T_{1,0}^{\sigma} \qquad \text{(mirror unknot, dashed circle ⊙)}
$$

Because the unknot is amphichiral ($T_{1,0} \cong T_{1,0}^{\sigma}$ as unoriented knots), the antineutrino shares the identical knot invariants with the neutrino:
- Jones polynomial: $J_{\nu^{\sigma}}(q) = 1$
- Alexander polynomial: $\Delta_{\nu^{\sigma}}(t) = 1$
- Hyperbolic volume: $\mathrm{Vol}(\nu^{\sigma}) = 0$
- Seifert genus: $g = 0$
- Crossing number: $c = 0$

Orientation (framing) distinguishes $\nu$ and $\nu^{\sigma}$, not knot type. In the braid group, the neutrino is the identity braid $e \in B_1$ with positive orientation; the antineutrino is $e$ with negative orientation.

**Visual convention.** We draw the antineutrino as a dashed circle (⊙) to distinguish it from:
- Solid circle (○) = neutrino (forward time)
- Solid trefoil (●) = electron (forward time)
- Outlined trefoil (○) = positron (backward time)

**Role in beta decay.** In $\beta^-$ decay, the $L_0^{-}$ smoothing of the $\mathfrak{d} \to \mathfrak{u}$ crossing change yields:

$$
  L_0^{-} =  T_{2,3} \sqcup T_{1,0}^{\sigma}
  \quad=\quad e^- +  \nu_e^{\sigma}.
$$

The electron $T_{2,3}$ carries topological mass (zero hyperbolic volume, but crossing energy from the trefoil structure). The antineutrino $T_{1,0}^{\sigma}$ carries zero topological mass and exits as a massless particle.

**Lepton number.** The $L_0^{\pm}$ smoothing strictly produces one fermion knot ($T_{2,3}$ or $T_{2,3}^{\sigma}$) and one (anti)neutrino ($T_{1,0}$ or $T_{1,0}^{\sigma}$). Each smoothing creates exactly one lepton-antilepton pair, conserving lepton number.
<!-- FILE_END: antineutrino-knot.md -->

