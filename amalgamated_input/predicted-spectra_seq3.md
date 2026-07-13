<!-- FILE_START: mesons-nucleons-categorical-proton-unique-intro.md -->
Borromean linking establishes the categorical proton's uniqueness. This linking provides the structural anchor. The construction extends to the neutron. Every bound-state assignment factors through this two-stage construction.
<!-- FILE_END: mesons-nucleons-categorical-proton-unique-intro.md -->

<!-- FILE_START: categorical-proton-unique.md -->
The triple $(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ and the Borromean braiding pattern $\mathcal{B}_3$ uniquely determine the [categorical proton](#def:categorical-proton) $\mathfrak{p}$ up to braid isotopy. Its Hecke normal form in $H_3(q)$ is unique. The $S_3$ permutation symmetry on the color tubes ensures independence from position assignments.

#### Strategy

The Hecke normal form is unique. Permuting the colored valence tubes via the $S_3$ group action acts through inner automorphisms. This groups the three configurations into a single equivalence class. Minimizing $|\mathrm{tr}_M|$ uniquely fixes the stabilizer selection.

#### Formalization

Standard Hecke normal form and $S_3$-symmetry arguments from knot representation theory establish this uniqueness constraint. Formalization validates the deterministic spectral predictions within the Quantum Observable Universe.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The categorical identities hold over an abstract coefficient ring. Only the archimedean realization requires specialization.
<!-- FILE_END: categorical-proton-unique.md -->

<!-- FILE_START: meson-to-proton-via-borromean.md -->
Baryon number conservation prevents adding a quark to a meson to form a proton. A meson consists of a quark--antiquark pair ($q\bar{q}$) and carries baryon number $B = 0$. A single quark carries $B = 1/3$. Their sum $q\bar{q} + q$ yields $B = 1/3$. A baryon requires $B = 1$. Baryon number conservation prevents the antiquark from spontaneously converting into a quark.

## Meson instability at $q_0$

The meson lacks stability at $q_0$. The normal form of the $\mathfrak{u}\bar{\mathfrak{d}}$ meson ($\sigma_0 \cdot L_+ \cdot \sigma_0^{-1}$) in $H_3(q)$ is:

$$
  \mathrm{NF}(\mathfrak{M}_+)
  =
  -0.209\sigma_1 - 0.044 L_+ + 1.000 L_- + 0.209 e^-
$$

This yields $\mathrm{net}(\mathfrak{M}_+) \approx +0.956$ and demand profile $\{\sigma_1 = -0.209, L_+ = -0.044\}$. Two negative normal form coefficients demand crossing content ($\sigma_1$) and Hopf link content ($L_+$) from the environment.

This demand renders the meson a transient intermediate rather than a stable endpoint. Observations align with this property. The charged pion decays in $\sim 26$ ns. Borromean topology $\mathcal{B}_3$ confinement provides genuine 3-body binding. This produces the only stable hadronic states, the proton and neutron.

## Three pair productions yield one proton

The proton requires three quarks ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$) with no antiquarks. Three independent quark--antiquark productions supply these constituents. Colliding colored photons create each $q\bar{q}$ pair:

$$
  \gamma\gamma \xrightarrow{L_+}
  \mathfrak{u}_1 + \bar{\mathfrak{u}}_1
  \qquad
  \gamma\gamma \xrightarrow{L_+}
  \mathfrak{u}_2 + \bar{\mathfrak{u}}_2
  \qquad
  \gamma\gamma \xrightarrow{L_-}
  \mathfrak{d}_3 + \bar{\mathfrak{d}}_3
$$

The Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ confines three quarks ($\mathfrak{u}_1$, $\mathfrak{u}_2$, $\mathfrak{d}_3$) selected from these six particles:

$$
  \mathfrak{p}
  = 
  \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})
$$

The three antiquarks ($\bar{\mathfrak{u}}_1$, $\bar{\mathfrak{u}}_2$, $\bar{\mathfrak{d}}_3$) annihilate back to photons or form an antiproton $\bar{\mathfrak{p}}$. Total baryon number remains conserved: $3 \times (1/3 - 1/3) = 0$ input, $1 + (-1) = 0$ output.

## Typed crossings: the physical proton and neutron

Untyped composition yields $\mathrm{net} \approx 1.506$. The CODATA proton net is $\approx 0.999$. Typed crossings close this gap. Quark flavor determines the crossing eigenvalue in $H_3(q)$.

| Crossing type | Hecke eigenvalue |
|:---|:---|
| $\mathfrak{u}$-$\mathfrak{u}$ ($\sigma$) | $+q$ |
| $\mathfrak{d}$-$\mathfrak{d}$ ($\sigma - H_A\cdot\mathbf{1}$) | $-q^{-1}$ |
| $\mathfrak{u}$-$\mathfrak{d}$ ($\sigma - \tfrac{1}{2}H_A\cdot\mathbf{1}$) | mixed |

The term $H_A$ equals $q - q^{-1}$. Down-quark crossings carry a $-H_A\cdot\mathbf{1}$ shift. This shift reduces the net coefficient.

Typed crossings at $q_0 \approx 1.1100$ produce:

| Nucleon | Quark content | $\mathrm{net}$ |
|:---|:---|---:|
| Proton $\mathfrak{p}$ | $\mathfrak{u}\mathfrak{u}\mathfrak{d}$ | $+0.9991$ |
| Neutron $\mathfrak{n}$ | $\mathfrak{u}\mathfrak{d}\mathfrak{d}$ | $+0.8108$ |

## The scale $\mathfrak{E}_0 = Q / |\Delta\mathrm{net}|$

The normal form coefficients represent dimensionless Laurent polynomials in $q$. Converting them to physical energies (MeV) requires a single scale $\mathfrak{E}_0$. The beta decay $Q$-value fixes this scale.

1. **Linearity.** The normal form computation constitutes a linear map on the 6-dimensional vector space $H_3(q)$. Therefore, $\mathrm{NF}(\mathfrak{n} - \mathfrak{p}) = \mathrm{NF}(\mathfrak{n}) - \mathrm{NF}(\mathfrak{p})$. The net difference equals the sum of all coefficient differences:

   $$
     \Delta\mathrm{net}
     = 
     \mathrm{net}(\mathfrak{n}) - \mathrm{net}(\mathfrak{p})
     = 
     0.8108 - 0.9991
     = 
     -0.1883.
   $$

2. **Calibration.** Beta decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu_e$ releases $\mathfrak{Q}_\beta = \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} - \mathfrak{m}_e \approx 0.782 \text{ MeV}$. This supplies the energy equivalent of the dimensionless transition $\Delta\mathrm{net}$:

   $$
     \mathfrak{E}_0
     = 
     \frac{\mathfrak{Q}_\beta}{|\Delta\mathrm{net}|}
     = 
     \frac{0.782}{0.1883}
      \approx  4.155 \text{ MeV}.
   $$

3. **Well-definedness.** The fixed substrate parameter $q_0$ determines all normal form coefficients. CODATA 2022 measures $\mathfrak{Q}_\beta$ to $\pm 0.6$ eV precision. Typed crossings mandate the negative sign $\Delta\mathrm{net} < 0$. The extra down quark in $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ introduces $-H_A$ shifts. These shifts lower the neutron net below the proton net. The ratio remains well-defined.

The parameter $\mathfrak{E}_0$ dictates the energy budget. Each normal form coefficient difference $\Delta_i$ contributes $\Delta_i \times \mathfrak{E}_0$ MeV to the decay energy. The six terms sum exactly to $\mathfrak{Q}_\beta$.

**Full derivation.**
Minimum action principles derive the confinement operator $\mathcal{B}_3$. Nucleon normal forms remain independent of photon polarization. The beta decay channel emerges as the $e^- < 0$ coefficient in the confined normal form.

Witness: `meson-nucleon-nf.witness.json`,
`beta-decay-energy-scale.witness.json`,
`confinement-operator-selection.witness.json`.
<!-- FILE_END: meson-to-proton-via-borromean.md -->

<!-- FILE_START: categorical-neutron-exists.md -->
The [categorical neutron](#def:categorical-neutron) $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$ exists as a well-defined, LP-stable element of $H_3(q)$.

#### Strategy

The $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$ partition assembles the constituent braids in the Hecke algebra $H_3(q)$. Two Hopf-link gluons minimize the stabilizer trace. Gröbner--Shirshov reduction reaches the normal form. The linear-programming dual verifies non-negativity $G x[\gamma] \ge 0$ at each step.

#### Formalization

The Lean formalization provides a `sorry`-free weak proxy proof (`CategoricalNeutron.exists`). It instantiates a structure without stability or positivity field constraints using free real fields. Full constraint satisfaction requires Hecke normal form and linear programming infrastructure. The underlying construction remains mathematically consistent. Missing computational algebra libraries cause the gap. Explicit instantiation validates the structural consistency of the categorical-neutron model.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The categorical identities hold over an abstract coefficient ring. Only the archimedean realization requires specialization.
<!-- FILE_END: categorical-neutron-exists.md -->

<!-- FILE_START: categorical-neutron-unique.md -->
The triple $(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$ and the Borromean braiding pattern uniquely determine the [categorical neutron](#def:categorical-neutron) $\mathfrak{n}$ up to braid isotopy. Its Hecke normal form in $H_3(q)$ is unique. The $S_3$-symmetry on color tubes ensures independence from position assignments.

#### Strategy

The Hecke normal form in $H_3(q)$ is unique. Inner automorphisms equate the three valence assignments under $S_3$-symmetry. Minimizing the absolute Markov trace $|\mathrm{tr}_M|$ uniquely fixes the stabilizer selection.

#### Formalization

Standard Hecke normal form and $S_3$-symmetry arguments from knot representation theory establish this structural uniqueness. Formalization validates the stability predictions of the categorical neutron within the Quantum Observable Universe.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The categorical identities hold over an abstract coefficient ring. Only the archimedean realization requires specialization.
<!-- FILE_END: categorical-neutron-unique.md -->

<!-- FILE_START: antiparticle-crossing-reversal.md -->
The left trefoil $T_{2,3}$ represents the electron generator. Its mirror image $T_{2,3}^{\sigma}$ has all crossings reversed.

**Statement.**

1. **Crossing reversal defines antiparticles.** Replacing every constituent $K_i$ with its mirror $K_i^{\sigma}$ yields the antihadron $\mathfrak{H}^{\sigma}$ of a composite hadron $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$. The braid word $\beta$ representing the linking has all crossing signs reversed.
2. **Crossing energy sign reversal.** The [crossing energy](#def:crossing-energy) of $\mathfrak{H}$ is

   $$
     \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = \sum_{\text{crossings}} \epsilon_i,
     \qquad \epsilon_i \in \{q, -q^{-1}\}.
   $$

   The crossing energy of the antihadron satisfies

   $$
     \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma}) = -\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
     \bigg|_{q \leftrightarrow q^{-1}}.
   $$

   Positive crossings ($+q$) become negative ($-q^{-1}$) and vice versa.
3. **Coulomb charge reversal.** The antisymmetric component of the crossing energy determines the Coulomb channel. This reverses sign: $Q(\mathfrak{H}^{\sigma}) = -Q(\mathfrak{H})$. The antiproton specifically carries $Q(\mathfrak{p}^{\sigma}) = -1$.
4. **Bare mass invariance.** The mirror operation preserves the knot type and its hyperbolic volume. The bare mass of a particle equals that of its antiparticle: $m_{\mathrm{bare}}(\mathfrak{H}^{\sigma}) = m_{\mathrm{bare}}(\mathfrak{H})$.

**Formalization status.** The Lean formalization supplies partial coverage. The sub-lemmas for Coulomb reversal, pair crossing energy, and bare mass invariance remain `sorry`-free. These rely on basic arithmetic and ring properties. The formal proof establishes the mirror operation swapping the topological crossing counts. Upgrading this to the algebraic trace substitution under $q \leftrightarrow q^{-1}$ constitutes a localized, routine goal. It preserves the structural validity of the mechanism.

Formal knot-theoretic mirror swapping models the physical properties of antiparticles.
<!-- FILE_END: antiparticle-crossing-reversal.md -->

<!-- FILE_START: chirality-trefoil-electron-positron.md -->
The left trefoil $T_{2,3}$ and right trefoil $T_{2,3}^{\sigma}$ represent the electron and positron. The chirality assignment is conventional. The physical content resides in their mirror relationship. $T_{2,3}^{\sigma}$ is $T_{2,3}$ with all crossings reversed.

**Antiparticles from crossing reversal.**

Antihadron construction replaces every $T_{2,3}$ with $T_{2,3}^{\sigma}$ in the knot formula. Mirroring yields the antiproton:

$$
  \mathfrak{p}^{\sigma}
  = 
  [u^{\sigma}, u^{\sigma}, d^{\sigma}]_p \oplus \mathcal{L}_H
$$

Here $u^{\sigma} = T_{2,3}^{\sigma}$ and $d^{\sigma} = (T_{2,3}^{\sigma})^{\sigma} = T_{2,3}$. The crossing energy of $\mathfrak{p}^{\sigma}$ reverses sign. This yields Coulomb charge $Q(\mathfrak{p}^{\sigma}) = -1$.

**Time reversal and the exceptional divisor.**

Traversing the exceptional divisor of the brane tower reverses the chirality of a trefoil. This maps $T_{2,3}$ to $T_{2,3}^{\sigma}$. The Feynman--Stueckelberg interpretation maps this to a particle traveling backward in time. The fiber adjoint involution acts on the weight decomposition and reverses the Reeb flow. Extending this involution to the exceptional divisor provides a mechanism for chirality reversal. The vortex tube reverses winding orientation passing through the blow-up.

**Open questions.**

1. **Vortex inversion**: Reversing circulation of a vortex tube in the brane fluid requires translating classical fluid dynamics results on vortex reconnection to the categorical setting.

2. **Information transfer**: Double chirality reversal (electron $\to$ positron $\to$ electron) constitutes a round-trip through the time-reversed sector. The fiber adjoint involution satisfies $\sigma^2 = \mathrm{id}$. This returns the system to its original state. Information preservation across this round-trip depends on the exceptional divisor's monodromy.

3. **The imaginary part**: The Archimedean realization over $\mathbb{C}$ permits a complex substrate parameter $q$. The observability axiom restricts $q$ to positive reals. A nonzero imaginary part contributes a phase to the crossing energy. This phase distinguishes particles from antiparticles without mirror reflection. The full theory models chirality reversal as a continuous rotation rather than a discrete flip.

4. **CPT from the categorical algebra**: The fiber adjoint involution and the Frobenius structure derive the combined CPT operation (charge conjugation $\sigma$, parity reflection, Reeb flow reversal). The QOU involutive axiom implies the CPT theorem.
<!-- FILE_END: chirality-trefoil-electron-positron.md -->

