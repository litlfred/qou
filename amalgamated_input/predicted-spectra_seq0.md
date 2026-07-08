<!-- FILE_START: fundamental-particles-intro.md -->
We populate the elementary spectrum using embeddable-knot generators. The up and down quarks form the light-quark sector; the electron, positron, neutrino, and antineutrino form the first-generation leptons. The $\mathcal{Q}_q$-value specifies the $q$-deformed transition energy derived from the categorical action difference at production vertices.

Categorical relations govern particle production. Pair creation, such as Breit–Wheeler production, appears as a Hecke vertex. The Frobenius Gram matrix in $H_3(q)$ determines which knot operators survive Frobenius duality. This mechanism dictates composite hadron formation. A proton requires three pair productions, bounded by the energy scale $\mathfrak{E}_0$. Crossing reversal of left and right trefoils encodes chirality.

Stable nuclei represent nuclear ground states at a Skein energy minimum. The genus-$4$ classification of Bring's surface admits exactly two torus knot solutions for the gauge forces: $T_{2,9}$ and $T_{3,5}$. The two-strand spectral completeness theorem over a commutative ring $R$ guarantees a unique scalar gauge coupling on $A \otimes A$. The parameters $(\mathfrak{E}_0, \delta_{CS}, \kappa)$ define the fine-structure constant $\alpha_{\mathrm{EM}}$.

Finally, categorical scaling bridges atomic and nuclear physics. The archimedean realization functor maps QED scales across the archimedean wall via the Bohr radius and the Hartree energy $E_{\mathrm{Hartree}}$. The categorical trace ratio tracks the running of $\alpha_{\mathrm{EM}}$ across generations. The valley of stability appears as a Diophantine constraint on the integer lattice, governing which decay transitions the Skein relation permits.
<!-- FILE_END: fundamental-particles-intro.md -->

<!-- FILE_START: electron-knot.md -->
The electron corresponds to the trefoil knot $T_{2,3}$ in the lepton sector.

$$
  e^- =  T_{2,3} \qquad \text{(trefoil, solid ●)}
$$

It shares this knot type with the up quark. Environment distinguishes them: the up quark threads a color tube on Bring's surface, while the electron orbits the nucleus via Hopf linking.

We draw both the electron and the up quark as a solid trefoil to denote the forward time direction. Context separates the lepton from the quark.
<!-- FILE_END: electron-knot.md -->

<!-- FILE_START: electron-knot-example.md -->
The electron represents the simplest nontrivial torus knot embedded on $\Sigma_4$: the trefoil $\tau(2,3)$. Its Seifert genus is $(2-1)(3-1)/2 = 1 \leq 4$. With $3$ crossings, the trefoil carries $3$ units of information. Its Jones polynomial is:

$$
  J_{\tau(2,3)}(q) = -q^{-4} + q^{-3} + q^{-1}
$$

Its mass derives from the quantum dilogarithm at $q \approx 1.110$, yielding $\mathfrak{m}_e = \mathrm{Li}_2(q^{-2})/\hbar_q^2$. We use this value as the fundamental mass unit, expressing all other particle masses as ratios against it.
<!-- FILE_END: electron-knot-example.md -->

<!-- FILE_START: positron-knot.md -->
The positron corresponds to the mirror trefoil $T_{2,3}^{\sigma}$ in the lepton sector. It serves as the antiparticle of the electron:

$$
  e^+ =  T_{2,3}^{\sigma}. \qquad \text{(mirror trefoil)}
$$

Like the electron, environment distinguishes the positron from its quark counterpart (the down quark). The mirror operation $\sigma$ reverses all crossings. This reversed crossing chirality shifts the Coulomb charge from $Q = -1$ to $Q = +1$.

We draw the positron as an outlined trefoil to denote reversed time direction. In the Reeb flow, crossing reversal corresponds to reversing time. The positron thus represents an electron traveling backward in time, recovering the Feynman–Stueckelberg interpretation.
<!-- FILE_END: positron-knot.md -->

<!-- FILE_START: neutrino-knot.md -->
The neutrino corresponds to the unknot $K_{0_1}$.

$$
  \nu =  K_{0_1} \qquad \text{(unknot, circle ○)}
$$

The unknot has Seifert genus $0$, crossing number $0$, and a trivial Skein polynomial $J_\nu(q) = 1$. It contributes no hyperbolic volume and thus carries no topological bare mass. Instead, neutrino mass arises entirely from vacuum drag.

We draw the neutrino as a simple circle.

The unknot dictates the neutrino's physical properties:
- **Zero crossing chirality:** The lack of crossings ensures electrical neutrality ($Q(\nu) = 0$).
- **Trivial braiding:** The $R$-matrix acts as the identity on the unknot. Neutrinos therefore evade the crossing-energy interactions responsible for Coulomb repulsion.
- **Vacuum drag mass:** The mass $m_\nu \sim \mu_0 \cdot (q - 1)$ scales with the baseline vacuum drag, vanishing at $q = 1$.
<!-- FILE_END: neutrino-knot.md -->

<!-- FILE_START: antineutrino-knot.md -->
The antineutrino corresponds to the mirror unknot $T_{1,0}^{\sigma}$. It serves as the antiparticle of the neutrino.

$$
  \nu^{\sigma} =  T_{1,0}^{\sigma} \qquad \text{(mirror unknot, dashed circle ⊙)}
$$

Because the unknot is amphichiral, the antineutrino shares identical knot invariants with the neutrino: Seifert genus $0$, crossing number $0$, zero hyperbolic volume, and trivial Jones and Alexander polynomials.

Orientation—not knot type—distinguishes the neutrino and antineutrino. In the braid group, the neutrino acts as the identity braid $e \in B_1$ with positive orientation, while the antineutrino acts as $e$ with negative orientation. We draw the antineutrino as a dashed circle (⊙).

In $\beta^-$ decay, the $L_0^{-}$ smoothing of the $\mathfrak{d} \to \mathfrak{u}$ crossing change yields the decay products:

$$
  L_0^{-} =  T_{2,3} \sqcup T_{1,0}^{\sigma}
  \quad=\quad e^- +  \nu_e^{\sigma}.
$$

The electron $T_{2,3}$ carries topological mass via crossing energy. The antineutrino $T_{1,0}^{\sigma}$ carries zero topological mass and exits as a massless particle.

The $L_0^{\pm}$ smoothing strictly produces one fermion knot ($T_{2,3}$ or $T_{2,3}^{\sigma}$) and one (anti)neutrino ($T_{1,0}$ or $T_{1,0}^{\sigma}$). By creating exactly one lepton-antilepton pair, each smoothing conserves lepton number.
<!-- FILE_END: antineutrino-knot.md -->

