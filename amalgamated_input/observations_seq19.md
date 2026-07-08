<!-- FILE_START: complexity-interpretation-intro.md -->
Breit–Wheeler pair creation necessitates a categorical reading of the photon-photon vertex. We assemble the interpretive consequences: chirality, virtual pairs, CP violation, and electron stability.

We first treat structural components. The $q$-projective bundle chart-glue yields the fermion-boson distinction. We model chirality as a continuous phase rotation in the pre-observable sector. We examine trefoil vortex stability against chirality flips. Crossing energy decomposes into a strong channel (confinement) and a Coulomb channel (electromagnetism). This decomposition creates an infinite-energy obstruction to time reversal in the observable sector.

We conclude with virtual particles and CP violation. Virtual particles are excitations of the exceptional divisor. Skein relations resolve vacuum-polarization diagrams from the Breit–Wheeler vertex. We summarize CP violation constraints and conjecturally identify the CP phase with the alternating-block character imaginary part. We extrapolate chirality to cosmological extremes. Finally, we establish the electron trefoil as a stable building block under the Markov trace. This forbids beta decay.
<!-- FILE_END: complexity-interpretation-intro.md -->

<!-- FILE_START: fermion-boson-chart-localization.md -->
The [fermion--boson decomposition](#def:fermion-boson-decomposition) provides a geometric reading on the quantum projective line. Bosons are horizontal ($\alpha_V = 0$). Fermions carry non-trivial vertical projections.

By the [spectral--chart correspondence](#prop:spectral-chart-correspondence), the symmetric and antisymmetric eigenspaces $S^2 V \oplus \Lambda^2 V$ of the braiding $c_{V,V}$ form the spectral data. This pins the chart-transition coefficient of $\mathbb{P}_q(V)$ to $\kappa = q^{-1}$. The bosonic sector occupies $S^2 V$ with eigenvalue $\lambda_+ = q$. This classical channel degenerates to $\mathbb{P}(V)$ at $q = 1$. The fermionic sector occupies the unit summand $\Lambda^2 V \cong \mathbf{1}$ with eigenvalue $\lambda_- = -q^{-1}$. The chart-glue concentrates here.

We identify $\kappa = q^{-1} = \lambda_+^{-1} = -\lambda_-$ as the parameter determined by the antisymmetric channel. The parameter $q$ measures surviving vertical (fermionic) content between charts. At $q = 1$, we recover $\kappa = 1$, decoupling the sectors into the classical inversion $z \cdot w = 1$. When $q \neq 1$, geometry deforms the glue, linking fermionic content to the substrate parameter via the Hecke data of $c_{V,V}$ on $V \otimes V$. This is the geometric action from [observation fermion action](#rem:observation-fermion-action). The chart-transition carries the fermionic backreaction of an observation. The substrate parameter acts as the chart-glue.
<!-- FILE_END: fermion-boson-chart-localization.md -->

<!-- FILE_START: complex-chirality-rotation.md -->
Let $q = |q|e^{i\theta}$ be a complex substrate parameter with $|q| > 1$ and $\theta \in (-\pi, \pi]$ ([complex substrate interpretation](#rem:complex-substrate-interpretation)).

**Conjecture.**
In the pre-observable sector (before the dagger positive-definiteness axiom), the phase $\theta$ controls the particle-antiparticle distinction:

1. **Crossing energy phase.** For a torus knot $T_{p,k}$ with [crossing energy](#def:crossing-energy) $\mathcal{S}_c(T_{p,k}; q)$, the complex extension is:

   $$
     \mathcal{S}_c(T_{p,k}; |q|e^{i\theta})
     = 
     \mathcal{S}_c(T_{p,k}; |q|)e^{in_c\theta},
   $$

   where $n_c$ is the crossing number. The mirror $T_{p,k}^{\sigma}$ carries crossing number $-n_c$, so $\mathcal{S}_c(T_{p,k}^{\sigma}) = \mathcal{S}_c(T_{p,k}; |q|)e^{-in_c\theta}$.

2. **Chirality interpolation.** The chirality operator $\mathcal{X}_\varphi \colon \theta \mapsto \theta + \varphi$ acts on the phase of $q$:
   - $\varphi = 0$: Identity action.
   - $\varphi = \pi / n_c$: Particle and antiparticle crossing energies equalize in magnitude and oppose in phase.
   - $\varphi = \pi$: Full chirality reversal ($q \mapsto |q|e^{i(\theta + \pi)}$).
   
   The discrete electron/positron flip ([chirality remark](#rem:chirality-trefoil-electron-positron)) is the endpoint $\varphi = \pi$ of this rotation.

3. **CPT as $\mathbb{Z}_2$ quotient.** The observable sector ($\theta = 0$) detects only the $\mathbb{Z}_2$ quotient of this $\mathrm{U}(1)$ action. Charge conjugation C is the residue of continuous chirality rotation. Parity P and time reversal T descend from pre-observable continuous operations. The CPT theorem means the total rotation $\mathcal{X}_\pi \circ P \circ T$ is a symmetry of the categorical action ([categorical action](#def:categorical-action)).

**Experimental discriminant.** Any pre-observable phase $\theta$ surviving in the observable sector appears as a CP-violating phase in crossing-energy ratios. For the electron-positron system:

$$
  \delta_{\mathrm{CP}}
  = 
  \frac{|\mathcal{S}_c(T_{2,3})| - |\mathcal{S}_c(T_{2,3}^{\sigma})|}{|\mathcal{S}_c(T_{2,3})| + |\mathcal{S}_c(T_{2,3}^{\sigma})|}
   \sim 
  \mathcal{O}(\theta^2).
$$

This vanishes to first order, matching electron-positron mass equality. It contributes at second order to hadronic CP violation, where multiple crossing numbers interact.
<!-- FILE_END: complex-chirality-rotation.md -->

<!-- FILE_START: trefoil-vortex-chirality-flip.md -->
Can a vortex tube reverse its circulation? ([chirality remark](#rem:chirality-trefoil-electron-positron)). Classical fluid dynamics provides a sharp contrast to the categorical framework.

**Classical result: trefoil vortices are unstable.**
Kleckner and Irvine \cite{kleckner2013} observed trefoil-knotted vortex loops in water. A trefoil vortex unties within few circulation timescales via reconnections. Two anti-parallel segments approach, reconnect, and separate, exchanging topology. Scheeler et al. \cite{scheeler2014} demonstrated helicity $\mathcal{H} = \int \mathbf{v} \cdot \boldsymbol{\omega} dV$ conservation during reconnection. It redistributes from writhe to twist:

$$
  \mathcal{H} =  \underbrace{Wr}_{\text{writhe}}
  +  \underbrace{Tw}_{\text{twist}}, \qquad
  \Delta Wr = -\Delta Tw \quad (\text{during reconnection}).
$$

Reconnections reduce the trefoil to unknotted loops. No chirality flip occurs. The trefoil dissolves.

**Obstructions to classical chirality reversal.**

Three obstructions prevent smooth chirality reversal in Navier--Stokes fluids:

1. **Kelvin's theorem.** Ideal fluid circulation $\Gamma = \oint \mathbf{v} \cdot d\mathbf{l}$ is conserved. Reversing $\Gamma$ requires external forcing.
2. **Topological protection of writhe sign.** A trefoil has writhe $Wr = \pm 3$. Flipping from $+3$ to $-3$ requires passing through $Wr = 0$ (unknot). Reconnections only decrease $|Wr|$.
3. **Dissipation.** Reconnections convert kinetic energy to heat. Untying dissipates energy $\sim 3 \Gamma^2 \rho$. Re-tying lacks an energy budget.

**The categorical trefoil is different.**
In the QOU framework, the trefoil is an element of the representation ring of $\mathrm{SU}_q(2)$, not a fluid filament.

| Property | Classical vortex | Categorical trefoil |
|----------|-----------------|---------------------|
| Identity | Embedding $S^1 \hookrightarrow \mathbb{R}^3$ | Knot type (isotopy class) |
| Stability | Reconnection-unstable | Topologically protected |
| Circulation | Continuous $\Gamma \in \mathbb{R}$ | Quantised by Casimir $[j]_q[j+1]_q$ |
| Chirality | Sign of $Wr$ | Knot invariant (left vs right trefoil) |
| Helicity transfer | $Wr \leftrightarrow Tw$ | Encoded in $R$-matrix |

The categorical trefoil's chirality is a knot invariant. The Jones polynomial distinguishes $T_{2,3}$ from $T_{2,3}^{\sigma}$: $J_{T_{2,3}}(q) \neq J_{T_{2,3}^{\sigma}}(q)$. Continuous deformation cannot interconvert them.

**Three routes to chirality reversal in the QOU.**

The theory admits three mechanisms:

1. **Passage through the exceptional divisor.** The [fiber adjoint involution](#prop:fiber-adjoint-involution) reverses Reeb flow. Extended to the [exceptional divisor](#def:exceptional-divisor), it maps $T_{2,3}$ to $T_{2,3}^{\sigma}$. This is a discrete jump (pair creation), destroying the knot type and creating its mirror.
2. **Complex substrate rotation.** The pre-observable sector ([complex substrate interpretation](#rem:complex-substrate-interpretation)) allows continuous phase rotation of $q$ via $\mathcal{X}_\varphi$. The [chirality rotation conjecture](#conj:complex-chirality-rotation) identifies the discrete flip $T_{2,3} \leftrightarrow T_{2,3}^{\sigma}$ as the $\mathbb{Z}_2$ shadow of this $\mathrm{U}(1)$ rotation.
3. **Reconnection as Reidemeister move.** Classical reconnections represent local Reidemeister moves (R-II). R-II moves alter embedding and crossing energy without changing knot type. Writhe changes by $\pm 2$, corresponding to orbital shell transitions. Changing knot type requires surpassing a topological barrier.

**Summary.**
A classical trefoil vortex unties and dissipates. The categorical trefoil is topologically stable. Its chirality is protected against continuous deformation. Reversal requires either discrete passage through the exceptional divisor or continuous pre-observable complex rotation.
<!-- FILE_END: trefoil-vortex-chirality-flip.md -->

<!-- FILE_START: crossing-energy-decomposition.md -->
The [crossing energy](#def:crossing-energy) assigns $+q$ to positive crossings and $-q^{-1}$ to negative crossings ($q > 1$). Writing $q = e^\lambda$ with $\lambda = \ln q > 0$, the weights decompose into symmetric and antisymmetric components under the mirror operation $\sigma$:

$$
  q = \cosh\lambda + \sinh\lambda, \qquad
  q^{-1} = \cosh\lambda - \sinh\lambda.
$$

**Statement.**
Let $\mathfrak{H}$ be a knot composite with crossing energy $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = \sum_i \epsilon_i$, where $\epsilon_i \in \{q, -q^{-1}\}$.

1. **Symmetric channel.** The component $E_{\mathrm{sym}}(\mathfrak{H}) = \sum_i |\epsilon_i| \cdot \cosh(\ln q) \cdot \mathrm{sgn}(\epsilon_i)$ is invariant under $\sigma$.
2. **Antisymmetric channel.** The component $E_{\mathrm{asym}}(\mathfrak{H}) = \sum_i |\epsilon_i| \cdot \sinh(\ln q) \cdot \mathrm{sgn}(\epsilon_i)$ reverses sign under $\sigma$.
3. **Pair cancellation.** For a particle-antiparticle pair $(\mathfrak{H}, \mathfrak{H}^{\sigma})$, the combined crossing energy is antisymmetric:

   $$
     \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) + \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma})
     = 2E_{\mathrm{asym}}(\mathfrak{H}).
   $$

4. **Ratio identity.** The antisymmetric-to-symmetric ratio is

   $$
     \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}}
     = \tanh(\ln q),
   $$

   which is independent of $\mathfrak{H}$.

## Algebraic-to-hyperbolic bridge

Writing $\lambda = \ln q$, every algebraic $q$-power maps to a hyperbolic exponential:

$$
  q^{n} = \cosh(n\lambda) + \sinh(n\lambda),
  \qquad
  q^{n} - q^{-n} = 2\sinh(n\lambda).
$$

The quantum integer evaluates to a ratio of hyperbolic sines:

$$
  [n]_q \;=\; \frac{q^{n} - q^{-n}}{q - q^{-1}}
  \;=\; \frac{\sinh(n\lambda)}{\sinh(\lambda)}.
$$

This Archimedean evaluation of the Hecke datum seeds the Kashaev volume realization ([Kashaev as Archimedean realisation](#rem:kashaev-as-archimedean-realization)). The limit $N \to \infty$ of the colored Jones polynomial integrates these lengths into the knot volume. The symmetric $\cosh$ and antisymmetric $\sinh$ channels denote the real and rotational parts.

We formalized these identities in Lean (`q_pow_eq_cosh_add_sinh`, `two_sinh_nat_log`, `qbracket_eq_sinh_ratio`) for $q > 0$.
<!-- FILE_END: crossing-energy-decomposition.md -->

<!-- FILE_START: crossing-energy-interpretation.md -->
The [decomposition](#prop:crossing-energy-decomposition) separates crossing energy into two channels.

**Channel identification.**

| Channel | Weight per crossing | Mirror behaviour | Physical force |
|---------|-------------------|-----------------|----------------|
| Symmetric | $\cosh(\ln q)$ | Invariant under $\sigma$ | **Strong binding** |
| Antisymmetric | $\sinh(\ln q)$ | Reverses under $\sigma$ | **Coulomb (electromagnetic)** |

The symmetric part binds regardless of charge. The antisymmetric part distinguishes charges.

**Pair creation.**

When creating an $e^- e^+$ pair, cancellation yields:

$$
  \mathfrak{E}_{\mathrm{cross}}(e^-) + \mathfrak{E}_{\mathrm{cross}}(e^+)
  = 6\sinh(\ln q)
  \approx 0.630 \quad (\text{Skein units}).
$$

Symmetric contributions cancel. The residual $6\sinh\lambda > 0$ yields pure Coulomb repulsion, separating the pair.

**EM/strong ratio.**

At $q = q_0$:

$$
  \tanh(\ln q_0) \approx 0.104.
$$

Electromagnetism operates at roughly $10\%$ of the strong force magnitude at the Skein scale.

**Crossing energy table** for a particle with $n_c$ positive crossings:

| Quantity | Formula | $T_{2,3}$ ($n_c = 3$) | Value |
|----------|---------|----------------------|-------|
| Total energy | $n_cq$ | $3q$ | $3.330$ |
| Strong component | $n_c\cosh(\ln q)$ | $3\cosh(\ln q)$ | $3.015$ |
| Coulomb component | $n_c\sinh(\ln q)$ | $3\sinh(\ln q)$ | $0.315$ |
| Pair net energy | $n_c(q - q^{-1})$ | $3(q - q^{-1})$ | $0.630$ |
| EM/strong ratio | $\tanh(\ln q)$ | $\tanh(\ln q)$ | $0.104$ |

By [Hopf stability](#prop:torus-hopf-stability), $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$. The strong symmetric channel dominates the Coulomb antisymmetric channel, ensuring proton stability.
<!-- FILE_END: crossing-energy-interpretation.md -->

<!-- FILE_START: time-reversal-energy-barrier.md -->
The Feynman--Stueckelberg interpretation frames the [positron](#def:positron-knot) as a backward-traveling electron. In QOU, time reversal corresponds to chirality reversal. We replace every $T_{2,3}$ with $T_{2,3}^{\sigma}$. This demands infinite energy in the observable sector.

**Elementary fermions (electron).**
The electron is the left trefoil $T_{2,3}$. No continuous deformation links $T_{2,3}$ to $T_{2,3}^{\sigma}$ ([trefoil vortex chirality flip](#rem:trefoil-vortex-chirality-flip)). The Jones polynomial distinguishes their connected components. In the observable sector ($q \in \mathbb{R}$, $q \geq 1$), crossing this topological barrier requires infinite energy:

$$
  \mathfrak{E}_{\text{flip}}(e^-) =  +\infty.
$$

No finite-energy process converts an electron into a positron. The only accessible channel is [pair creation](#rem:pair-creation-energy) at the exceptional divisor, costing $2m_e \approx 1.022$ MeV.

**Composite fermions (proton, neutron).**
The proton is a [Borromean baryon](#def:borromean-baryon): $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \oplus \mathcal{L}_H$. Its antiparticle $\mathfrak{p}^{\sigma}$ replaces every $T_{2,3}$ with $T_{2,3}^{\sigma}$ ([chirality remark](#rem:chirality-trefoil-electron-positron)).

Topological protection applies equally:

1. **Link type invariance.** The Milnor triple linking number $\bar{\mu}(123) = \pm 1$ distinguishes the Borromean link $\mathcal{B}_3$ from its mirror $\mathcal{B}_3^{\sigma}$. No Reidemeister sequence connects them.
2. **Constituent protection.** Every constituent trefoil requires an infinite-energy chirality flip.
3. **Chirality-sensitive linking.** The Hopf link $\mathcal{L}_H$ carries linking number $+1$. Its mirror carries $-1$. Reversal requires link destruction and recreation.

Consequently:

$$
  \mathfrak{E}_{\text{flip}}(\mathfrak{p}) =  +\infty, \qquad
  \mathfrak{E}_{\text{flip}}(\mathfrak{n}) =  +\infty.
$$

Antiproton production requires pair creation costing $2m_p \approx 1876.5$ MeV.

**Beta decay is not chirality reversal.**
The neutron decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar{\nu}_e^{\sigma}$ changes the crossing orientation partition (from $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ to $[\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]$). This R-I embedding move preserves link type and trefoil chirality. No trefoil flips.

**Summary.**

| Particle | Chirality reversal energy | Pair creation threshold |
|----------|--------------------------|----------------------|
| Electron $e^-$ | $\infty$ | $2m_e \approx 1.022$ MeV |
| Proton $\mathfrak{p}$ | $\infty$ | $2m_p \approx 1876.5$ MeV |
| Neutron $\mathfrak{n}$ | $\infty$ | $2m_n \approx 1879.1$ MeV |
| Neutrino $\nu$ | $\infty$ | $\approx 0$ |

Sending a particle backward in time corresponds to chirality reversal. The infinite energy barrier applies to all trefoil-generated particles. Pair creation alone produces time-reversed partners.
<!-- FILE_END: time-reversal-energy-barrier.md -->

<!-- FILE_START: virtual-particles-exceptional-divisor.md -->
Virtual particles mediate forces as off-shell excitations. The Heisenberg relation $\Delta E \cdot \Delta t \gtrsim \hbar$ limits their existence. The QOU framework localizes them geometrically.

**The exceptional divisor as the virtual stage.**

The blow-up replaces each brane point $p \in M$ with an [exceptional divisor](#def:exceptional-divisor) $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$. This sphere parametrizes internal departure directions invisible from the base manifold.

A virtual particle operates within the Reeb bundle over $\mathcal{S}_p$. This is the Hopf fibration $U(1) \hookrightarrow S^3 \to \mathcal{S}_p$ where braiding occurs ([vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)). The excitation originates at the blow-up locus, propagates through the [brane tower](#def:recursive-brane-tower), and is reabsorbed before reaching the base level $A_0$.

**Brane tower levels as virtual depth.**

The [recursive brane tower](#def:recursive-brane-tower) $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ stratifies excitations by [jet prolongation](#prop:jet-prolongation) level:

| Tower level | Algebra | Physical interpretation |
|-------------|---------|----------------------|
| $A_0 = A$ | $\mathcal{O}(\mathrm{SU}(2))$ | On-shell particles |
| $A_1 = J^1(A_0)$ | Frame bundle sections | 1-virtual (gauge bosons) |
| $A_2 = J^1(A_1)$ | Second jet sections | 2-virtual (curvature fluctuations) |
| $A_n$ | $n$-th jet sections | $n$-virtual |

The state space expands with virtual depth. Projection to $A_0$ collapses this structure.

**Non-observability of virtual particles.**

Level $A_n$ ($n \geq 1$) excitations remain invisible at $A_0$. The canonical projection $\pi_0 \colon A_n \to A_0$ annihilates $\Omega^1$ components:

$$
  \pi_0(f \otimes \omega_1 \otimes \cdots \otimes \omega_n)
  = 
  f \cdot \varepsilon(\omega_1) \cdots \varepsilon(\omega_n).
$$

For a form $\omega$ lacking a constant part ($\varepsilon(\omega) = 0$), the projection yields zero. The excitation projects no shadow onto $A_0$. This mimics "off-shell" behaviour.

**Lifetime from the Heisenberg commutator.**

The [Heisenberg commutator](#rem:heisenberg-commutator) at level $n$ is

$$
  [\hat{X}, \hat{P}]_{q_n} =  J\hbar_{q_n}, \qquad
  \hbar_{q_n} =  1 - q_n^{-1}.
$$

The uncertainty bound $\Delta E \cdot \Delta t \geq \hbar_{q_n} / 2$ restricts the level-$n$ excitation lifetime:

$$
  \Delta t_{\text{virtual}}
   \leq 
  \frac{\hbar_{q_n}}{2\Delta E}.
$$

The excitation remains within the tower, never descending to $A_0$.
<!-- FILE_END: virtual-particles-exceptional-divisor.md -->

<!-- FILE_START: vacuum-polarization-virtual-pairs.md -->
**Virtual pairs at the exceptional divisor.**

A photon with $E \geq 2m_e$ generates a real $e^-e^+$ pair at the exceptional divisor ([pair creation energy](#rem:pair-creation-energy)). A photon with $E < 2m_e$ generates a virtual pair. This pair exists within $\mathcal{S}_p$ for $\Delta t \leq \hbar_q / (2m_e - E)$ before annihilation.

This describes vacuum polarization. The photon temporarily resolves into a virtual pair within the exceptional divisor, altering the effective coupling constant. The pair lives and dies in the blow-up geometry without reaching $A_0$.

**Virtual exchange as Skein resolution.**

In the [Reidemeister mass invariance](#conj:reidemeister-mass-invariance) framework, an R-II move models a virtual pair. The Skein resolution of this pair produces $(q - q^{-1}) \cdot L_0$. This perturbatively corrects the crossing energy without modifying knot type.

**Summary.**
We summarize QOU realizations of QFT concepts in [Table: QFT concepts and their QOU brane-tower realizations](#tbl:vacuum-polarization-virtual-pairs-table-data). Virtual particles are invisible brane-tower excitations confined to the exceptional divisor.
<!-- FILE_END: vacuum-polarization-virtual-pairs.md -->

<!-- FILE_START: cp-violation-evidence.md -->
**Definition of CP violation.**
CP symmetry enforces perfect mirroring between matter and antimatter. CP violation fundamentally distinguishes them.

**Experimental evidence.**

Three systems establish CP violation:

1. **Neutral kaons** (1964). Cronin and Fitch observed $K_L \to \pi^+\pi^-$ at a rate of $\sim 2 \times 10^{-3}$ \cite{christenson1964}.
2. **$B$ mesons** (2001). BaBar \cite{aubert2001} and Belle measured CP-violating asymmetries in $B^0 \to J/\psi\, K_S$, confirming the complex CKM phase $\delta_{\mathrm{CKM}}$.
3. **$D$ mesons** (2019). LHCb measured CP violation in charm decays.

**The matter-antimatter asymmetry.**

Sakharov required C and CP violation for baryogenesis. The Standard Model CKM phase is quantitatively insufficient to explain the $n_B / n_\gamma \sim 6 \times 10^{-10}$ ratio.

**QOU interpretation.**

In the [complex chirality rotation](#conj:complex-chirality-rotation) framework, CP violation stems from a residual phase $\theta_{\mathrm{res}}$ of the complex parameter $q = |q|e^{i\theta}$:

- The observable sector projects $\theta \to 0$. An imperfect projection leaves $\theta_{\mathrm{res}}$.
- The discriminant scales as $\delta_{\mathrm{CP}} \sim \mathcal{O}(\theta_{\mathrm{res}}^2)$ for single-crossing systems ($e^-e^+$).
- For multi-crossing composites (kaons), phase accumulates linearly: $\delta_{\mathrm{CP}} \sim n_c\theta_{\mathrm{res}}$.
- This supplies a geometric origin for the CKM phase.

**Quantitative gap.**

The [crossing energy decomposition](#prop:crossing-energy-decomposition) provides an EM-to-strong ratio of $\tanh(\ln q) \approx 0.104$. If $\theta_{\mathrm{res}} \sim \tanh(\ln q) \cdot \alpha_{\mathrm{EM}}$, then $\delta_{\mathrm{CP}} \sim 10^{-3}$. This matches kaon systems but fails to explain baryogenesis. Cosmological regimes must provide the required enhancement.
<!-- FILE_END: cp-violation-evidence.md -->

<!-- FILE_START: cp-violation-spectral-form.md -->
**Conjecture (spectral form of $\delta_{\mathrm{CP}}$).**
*Let $A = H_n(R_\mathbb{C}, q)$ with complexified ground ring $R_\mathbb{C} = R \otimes \mathbb{Z}[i]$, accommodating $q = |q| \exp(i\theta)$ ([complex chirality rotation](#conj:complex-chirality-rotation)). For a hadronic braid $\beta_\mathcal{K} \in B_n$, the CP-violating discriminant equals the imaginary part of the alternating/symmetric Wedderburn-block trace ratio:*

$$
  \delta_{\mathrm{CP}}(\beta_\mathcal{K})
  \;=\;
  \mathrm{Im}\bigl(F_{\mathrm{Pauli}}(\beta_\mathcal{K})\bigr)
  \;=\;
  \mathrm{Im}\!\left(
    \frac{\chi_{(1^n)}(\beta_\mathcal{K})}
         {\chi_{(n)}(\beta_\mathcal{K})}
  \right) \,\in\, R_\mathbb{C}.
$$

*The real part supplies the Pauli statistical weight ([Pauli factor](#prop:pauli-factor-wedderburn)). The imaginary part isolates CP violation. Amphicheiral or real-$q$ configurations have $\mathrm{Im}(\chi_\lambda) = 0$ and $\delta_{\mathrm{CP}} = 0$.*

**Phase accumulation.**
*For multi-crossing composites, $\theta_{\mathrm{res}}$ accumulates linearly. With $\chi_\lambda(q) = \chi_\lambda(|q|) \exp(i\, n_\lambda \theta)$:*

$$
  \mathrm{Im}\!\left(
    \frac{\chi_{(1^n)}(\beta_\mathcal{K})}
         {\chi_{(n)}(\beta_\mathcal{K})}
  \right)
  \;\sim\; \bigl(n_{(1^n)} - n_{(n)}\bigr) \cdot \theta_{\mathrm{res}}
$$

*to leading order. The difference $n_{(1^n)} - n_{(n)}$ scales with total crossing number, recovering $\delta_{\mathrm{CP}} \sim n_c \theta_{\mathrm{res}}$.*

**Sketch.**
Spectral completeness over $R_\mathbb{C}$ decomposes $F_{\mathrm{Pauli}}$. The alternating block $V_{(1^n)}$ provides phase asymmetry, carrying $(-q)^{-w}$ on a writhe-$w$ crossing ([antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)). The symmetric block carries $q^w$. Their ratio's imaginary part isolates the CP-violating amplitude.

**Falsifiability.**
Amphicheiral knots must yield exactly $\delta_{\mathrm{CP}} = 0$. Any amphicheiral hadron exhibiting CP violation falsifies this characterization.

*Remark.* This relies on ([complex chirality rotation](#conj:complex-chirality-rotation)). Proof requires demonstrating $R_\mathbb{C}$-enrichment uniqueness and matching $\theta_{\mathrm{res}}$ to the Wolfenstein parameterization.

**Archimedean specialisation (§7c).** This block depends on archimedean components: real-valued observables and numerical evaluation at $q_0$. Categorical identities hold over abstract rings.
<!-- FILE_END: cp-violation-spectral-form.md -->

<!-- FILE_START: cosmological-chirality-flip.md -->
The [time reversal barrier](#rem:time-reversal-energy-barrier) dictates infinite energy for chirality reversal in the observable sector. The [cosmological limits](#ex:cosmological-limits) specify two regimes lacking this topological protection.

**Formalization status.** These claims are conjectural. We lack Lean formalization for the Frobenius degeneration at $q \to \infty$.

**At the Big Bang ($q \to \infty$).**

The Frobenius form degenerates: $\int_A(f^\dagger f) \sim q^{-1} \to 0$. The [Heisenberg commutator](#rem:heisenberg-commutator) $[\hat{X}, \hat{P}]_q \to J$ is maximal. Observables become maximally non-commutative. The positive-definiteness axiom vanishes.

Here, $q$ acquires an imaginary part $\theta \neq 0$. The [complex substrate interpretation](#rem:complex-substrate-interpretation) allows continuous fiber chirality rotation. The [exceptional divisor](#def:exceptional-divisor) $\mathcal{S}_p$ supports phase rotation $\mathcal{X}_\varphi$ between trefoils and their mirrors. Chirality flips occur in the fibers.

This meets Sakharov's conditions:
1. Frobenius degeneration enables baryon number violation.
2. Complex phase $\theta$ supplies CP violation.
3. The Big Bang provides non-equilibrium.

**At heat death ($q \to 1$).**

The Hopf algebra becomes cocommutative. The [quantum Planck constant](#def:substrate-parameter) vanishes. The Descartes color tubes collapse to a single $\mathrm{U}(1)$ phase tube ([prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction)). The crossing-energy asymmetry $q - q^{-1} \to 0$ disappears. The electron and muon survive as indistinguishable topological excitations ([rem:symmetry-preserving-leptons](#rem:symmetry-preserving-leptons)) with vanishing masses.

**Categorical picture (conjectural).**

We require a category of QOU degenerations $\mathbf{QOU}_{\mathrm{deg}}$ with morphisms preserving structure while selectively degrading axioms:

- The **initial object** represents the Big Bang ($q = \infty$, degenerate Frobenius form).
- The **terminal object** is [Bring's surface](#thm:descartes) ($q = 1$).
- The **observable era** is the full subcategory with $1 < q < \infty$.

**The aeon boundary.**

The $1 < q < \infty$ regime enforces chirality conservation:

1. **Big Bang**: Frobenius degeneration lifts the observability constraint. Chirality flips occur freely.
2. **Observable era**: Chirality is frozen.
3. **Heat death**: The $q \to 1$ limit erases chirality distinctions.

In a cyclic universe, exceptional divisors reset topology at the aeon boundary. We conjecture this transition as a morphism from the terminal object of one $\mathbf{QOU}_{\mathrm{deg}}$ to the initial object of the next.
<!-- FILE_END: cosmological-chirality-flip.md -->

<!-- FILE_START: electron-immortality.md -->
Beta decay rearranges the crossing orientation partition of the [Borromean baryon](#def:borromean-baryon) (e.g., $[u,d,d] \to [u,u,d]$). It relies on internal composite structure rearranged via R-I moves.

## Stability of the electron against beta decay

The electron avoids beta decay through topological necessity. The electron trefoil $T_{2,3}$ possesses no internal constituents or crossing orientation partition. Its single degree of freedom is its topological knot invariant.

| Particle | Structure | Internal d.o.f. | Beta decay? |
|----------|-----------|----------------|-------------|
| Neutron | $[u,d,d]_p \oplus \mathcal{L}_H$ | Quark flavour partition | Yes: $\mathfrak{n} \to \mathfrak{p} + e^- + \nu^{\sigma}$ |
| Proton | $[u,u,d]_p \oplus \mathcal{L}_H$ | Quark flavour partition | Yes (in nuclei): $\mathfrak{p} \to \mathfrak{n} + e^+ + \nu$ |
| Electron | $T_{2,3}$ | None | **No** |
| Neutrino | $T_{1,0}$ (unknot) | None | **No** |

No lighter charged lepton exists. The neutrino $T_{1,0}$ cannot absorb the electron's topological charge.

## Electron survival to heat death

The [time reversal barrier](#rem:time-reversal-energy-barrier) prevents chirality reversal during the observable era ($1 < q < \infty$). The electron persists immortally from pair production to the cosmological boundary.

As the universe approaches heat death ($q \to 1$):

1. **Bound electrons are liberated**: Binding energy dissipates while bare mass remains invariant.
2. **Free electrons become radiation**: The crossing energy asymmetry $q - q^{-1} \to 0$ erases Coulomb charge. The electron becomes a massless topological excitation.
3. **Radiation becomes CMB**: The thermal photon bath redshifts to the CMB. The [CMB torsion signature](#rem:cmb-q-torsion) records the $q$-deformed Reeb flow.

## Into the next aeon

If the [cosmological chirality flip](#rem:cosmological-chirality-flip) holds, CMB radiation carries topological data across the heat-death boundary. Frobenius degeneration governs this aeon transition. Exceptional divisors reset the topology. The electron trefoil persists until existence dissolves at $q = 1$.
<!-- FILE_END: electron-immortality.md -->

