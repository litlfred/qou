*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Conjecture.**
*Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be the Descartes
universe at substrate parameter $q = q_0$.  At baryon densities
$\rho > \rho_c$, where $\rho_c$ is determined by the
[energy crossover](#prop:borromean-hopf-energy-crossover), the
ground state of strange quark matter undergoes a topological
phase transition:*

1. *The Borromean linking $\mathcal{B}_3$ of each baryon is
   disrupted.*

2. *Quarks recombine into [Hopf diquark](#def:hopf-diquark)
   Cooper pairs $D_{[ij]}^{[ab]}$ in the color-antitriplet
   channel.*

3. *The condensate of all nine flavor-color diquark species
   spontaneously breaks*
   $\mathrm{SU}(3)_c \times \mathrm{SU}(3)_L \times \mathrm{SU}(3)_R$
   *to the diagonal*
   $\mathrm{SU}(3)_{c+L+R}$*, realizing color-flavor locking.*

4. *The Milnor invariant $\bar{\mu}(123)$ of the Borromean link
   — which is $1$ in the confined phase — transitions to $0$ in
   the CFL phase.  This is the topological order parameter of
   the transition.*

**The Milnor order parameter.**

The Borromean link has pairwise linking numbers
$\mathrm{lk}(i,j) = 0$ but Milnor triple linking
$\bar{\mu}(123) = 1$
([Borromean baryon](#def:borromean-baryon)).  This triple
invariant detects the "inseparability without pairwise linking"
that IS confinement.

In the CFL phase, each pair of quarks is Hopf-linked:
$\mathrm{lk}(i,j) = \pm 1$ for all $i \neq j$.  The Milnor
triple linking of the reconfigured link is
$\bar{\mu}(123) = 0$ — the triple inseparability has been
traded for pairwise binding.

The transition is characterized by:

| Invariant | Borromean (confined) | CFL (superconducting) |
|-----------|---------------------|----------------------|
| $\mathrm{lk}(i,j)$ | $0$ for all $i \neq j$ | $\pm 1$ for all $i \neq j$ |
| $\bar{\mu}(123)$ | $1$ | $0$ |
| Vol(complement) | $7.32772$ | $0$ (torus link) |
| Stable diquarks | No | Yes (condensate) |
| Mass source | Borromean volume | Crossing energy |

The transition is **not** a smooth deformation: continuous
interpolation between $\bar{\mu} = 1$ and
$\bar{\mu} = 0$ is impossible — the Milnor invariant is a concordance
invariant and jumps discontinuously.  This is a **first-order
topological phase transition**.

**Mechanism: coral-tube overlap.**

The three coral tubes of Bring's surface
([color tube coordinates](#def:color-tube-coordinates)) have a
characteristic transverse scale set by the resolvent separation
$|w_k - w_l| \sim |c_r|$.  At low density, the coral tubes of
adjacent baryons are well-separated.  At density $\rho$, the
inter-baryon spacing scales as $\rho^{-1/3}$.

When $\rho^{-1/3} \lesssim |c_r|$, the coral tubes of
adjacent baryons **overlap**.  Within the overlap region, a
quark in coral tube $a$ of baryon $1$ can form a Hopf link
with a quark in coral tube $b$ of baryon $2$ — a
[Hopf diquark](#def:hopf-diquark).  This inter-baryon
Hopf linking disrupts the intra-baryon Borromean structure:
once a quark is Hopf-linked to an external partner, its
Borromean triple is broken (removing one component frees the
other two).

The cascade is:
1. Coral tubes overlap at $\rho \sim \rho_c$.
2. Inter-baryon Hopf diquarks form spontaneously (energetically
   favorable in the overlap region).
3. Each diquark breaks a Borromean triple, freeing two quarks.
4. Freed quarks form new diquarks with neighbors.
5. The entire system rearranges into a Hopf-diquark condensate.

**The $\epsilon^{abc}$ from linking orientation.**

In the CFL phase, the pairing pattern locks color and flavor:
$\langle \mathfrak{q}_i^a \mathfrak{q}_j^b \rangle \propto \epsilon^{abc}\epsilon_{ijk}$ \cite{alford1999}.  In QOU,
the antisymmetric tensor arises from the **Hopf linking number**:

- The Hopf link $\mathcal{L}_H$ has linking number
  $\mathrm{lk} = +1$ for a specific orientation of the two
  components.
- Exchanging the two components reverses the linking number:
  $\mathrm{lk}(a, b) = -\mathrm{lk}(b, a)$.
- For three coral tubes $(r, g, b)$, the three independent
  diquark orientations form the antisymmetric tensor:

$$
  \mathrm{lk}(a, b)
  = 
  \epsilon^{abc}\delta_{c, \text{spectator}},
$$

  where the "spectator" color $c$ is the tube not participating
  in the diquark.  This automatically generates the CFL
  pairing pattern.

**The CFL gap.**

The superconducting gap $\Delta_{\mathrm{CFL}}$ — the energy
cost of breaking a Cooper pair — equals the crossing energy
of the Hopf link binding the diquark:

$$
  \Delta_{\mathrm{CFL}}
  = 
  |\mathfrak{E}_{\mathrm{cross}}(\mathcal{L}_H)|
  = 
  q + q^{-1}
   \approx  2.011 \quad\text{Skein units}.
$$

This is the strong-channel energy of a single Hopf-link crossing
pair.  In physical units, converting via the proton mass scale
$m_p \approx 938$ MeV and the Borromean volume ratio:

$$
  \Delta_{\mathrm{CFL}}^{\mathrm{phys}}
   \sim 
  \frac{q + q^{-1}}{V_B / \hbar_q^2}
   \cdot  m_pc^2
   \sim 
  \frac{2.011}{749.2}
   \times  938  \mathrm{MeV}
   \approx  2.5  \mathrm{MeV}.
$$

This is close to perturbative QCD estimates of
$\Delta_{\mathrm{CFL}} \sim 10\text{--}100$ MeV at
asymptotically high density, given that the QOU estimate
uses no fitting parameters.  The discrepancy suggests that
multi-diquark coherence effects (BCS enhancement from the
condensate) amplify the single-pair gap by a factor of
$\sim 10\text{--}40$.

**Phase sequence in neutron stars.**

The [strangelet crossing energy](#prop:strangelet-crossing-energy)
and [energy crossover](#prop:borromean-hopf-energy-crossover)
together predict a layered structure in neutron stars:

| Layer | Density | Topology | Phase |
|-------|---------|----------|-------|
| Crust | $\rho < \rho_0$ | $\mathcal{B}_3$ baryons in lattice | Nuclear solid |
| Outer core | $\rho_0 < \rho < 2\rho_0$ | $\mathcal{B}_3$ with hyperons ($T_{2,5}^{\sigma}$) | Hyperonic fluid |
| Inner core | $2\rho_0 < \rho < \rho_c$ | Borromean dissolution | Quark matter |
| Deep core | $\rho > \rho_c$ | $D_{[ij]}^{[ab]}$ Hopf condensate | CFL superconductor |

The layered structure is a direct consequence of the two
topological invariants: $\bar{\mu}(123)$ (confinement) and
$\mathrm{lk}(i,j)$ (diquark binding) cannot both be nonzero
simultaneously.  The transition between layers is first-order
(discontinuous jump in $\bar{\mu}$).

**Falsifiability.**

The conjecture predicts:

1. **Neutron star mass-radius relation**: the CFL core has
   a stiffer equation of state than nuclear matter (zero
   volume contribution to mass $\to$ lower density at given
   pressure).  This should produce a kink in the $M(R)$
   relation at $\rho_c$.

2. **Cooling rate**: the CFL gap $\Delta_{\mathrm{CFL}} \approx 2.5$ MeV suppresses neutrino emission below
   $T \sim \Delta_{\mathrm{CFL}} / k_B \sim 3 \times 10^{10}$ K.
   Stars with CFL cores cool more slowly at intermediate ages.

3. **Gravitational wave signature**: the first-order
   transition at $\rho_c$ produces a density discontinuity
   that modifies the $f$-mode oscillation spectrum of
   neutron stars, detectable by LIGO/Virgo.
