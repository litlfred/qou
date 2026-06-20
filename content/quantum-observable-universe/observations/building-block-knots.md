*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Every particle in the Descartes universe is built from knots and
links embeddable on the genus-$4$ Bring's surface.  This remark
collects the complete set of building blocks: their classical
knot names, visual conventions, Jones polynomials, hyperbolic
volumes, and the energy (mass) each contributes.

## Visual convention

- **Solid** (filled ●) = particle (positive time orientation)
- **Outlined** (hollow ○) = antiparticle (negative time / mirror)
- **Dashed** (⊙) = neutral antiparticle (amphichiral mirror)

The mirror operation $\sigma$ reverses all crossings:
$\sigma_i \mapsto \sigma_i^{-1}$.  For chiral knots this
produces a distinct knot type; for amphichiral knots
($0_1$, $4_1$) it returns the same knot.

## Table 1: Fundamental knots (single-component, torus-embeddable)

See [Table 1](#tbl:building-block-knots-table1-data).

**Key observation**: All torus knots have $\mathrm{Vol} = 0$.
They contribute no bare mass from hyperbolic volume.  Their
mass arises entirely from **crossing energy** at $q \neq 1$.

## Table 2: Derived knots (from Skein operations on generators)

See [Table 2](#tbl:building-block-knots-table2-data).

The figure-eight knot $4_1$ is **amphichiral** (self-mirror),
The Higgs field is its own antiparticle ($H = H^{\sigma}$).
Its hyperbolic volume $\mathrm{Vol}(4_1) = 2.0299$ drives the
mass mechanism
([cohomological embedding](#prop:cohomological-embedding)):
it couples to every knot-particle with crossings $> 0$.

## Table 3: Links (multi-component, for force carriers and composites)

See [Table 3](#tbl:building-block-knots-table3-data).

## Table 4: Antiparticle completion

Every particle has an antiparticle obtained by the mirror
operation $\sigma$.  For completeness:

See [Table 4](#tbl:building-block-knots-table4-data).

## Mass from knot energy

The mass of a knot $K$ is:

$$
  \mathfrak{m}(K) =  \frac{\mathrm{Vol}(K)}{\hbar_q^2}
  +  \sum_{\text{crossings}} \mathfrak{E}_{\times}(q)
$$

where $\hbar_q = 1 - q^{-1}$ and
$\mathfrak{E}_{\times}(q) = \tfrac{1}{2}(q - q^{-1})$ is the crossing
energy at each self-crossing.

- **Torus knots** ($\mathrm{Vol} = 0$): mass comes entirely
  from crossing energy.  The trefoil has 3 crossings, so
  $m_{e} = 3 \cdot \mathfrak{E}_{\times}(q) \cdot \mu_0$ where $\mu_0$ is
  the mass scale.
- **Hyperbolic knots** ($\mathrm{Vol} > 0$): mass has both
  a volume term and a crossing term.  The figure-eight (Higgs
  boson) has $\mathrm{Vol} = 2.0299$ and 4 crossings; the Higgs
  mass mechanism determines the muon--electron mass ratio
  $m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^2$, which fixes $q = q_0$.
- **Links** ($> 1$ component): the linking number contributes
  additional inter-component crossing energy (binding).

## Jones polynomial at $q = q_0$

See [Table 5](#tbl:building-block-knots-table5-data).

The Jones polynomial at $q = 1$ gives the number of
components: $J(1) = (-2)^{c-1}$ where $c$ is the
component count.  At $q = q_0$, the polynomial
encodes the $q$-deformation of the knot's contribution
to the categorical action.

## Table 5: Categorical action at $q = q_0$

The categorical action $\mathfrak{S}_q(K) = \mathrm{tr}_\tau(\rho(\mathcal{B}_K))$
decomposes into a hyperbolic volume term and a crossing energy
term.  For torus knots ($\mathrm{Vol} = 0$), the entire action
comes from crossings.  All quantities below are functions of
$q$ alone (plus one dimensional scale $\mu_0$ for mass).

**Fundamental constants from $q$:**

See [Table 6](#tbl:building-block-knots-table6-data).

**Categorical action per building block:**

See [Table 7](#tbl:building-block-knots-table7-data).

The neutron--proton mass difference $\delta_{\mathrm{Skein}} = \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q) - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) \approx 1.293$ MeV
arises from the pair Skein asymmetry between $\mathfrak{d}\mathfrak{d}$ and $\mathfrak{u}\mathfrak{u}$
crossings — a pure function of $q$.

**Key consequence for beta decay.**  The electron's categorical
action $\mathfrak{S}_q(e) = 3\mathfrak{E}_{\times}(q) \cdot \mu_0$, the neutrino's
$\mathfrak{S}_q(\nu) = 0$, and the nuclear actions $\mathfrak{S}_q(\mathcal{N})$
from the Markov trace product are all computable from $q$.
The $Q$-value
([transition energy](#def:Q-value-transition))
$Q = \mathfrak{S}_q(\mathrm{par}) - \mathfrak{S}_q(\mathrm{dau}) - \mathfrak{S}_q(e)$
therefore depends on $q$ and $\mu_0$ alone — no external
constants.
