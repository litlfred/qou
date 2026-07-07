<!-- FILE_START: complexity-interpretation-intro.md -->
Breit–Wheeler pair creation forces a categorical reading of the photon-photon vertex. This section assembles the resulting interpretive consequences: chirality, virtual pairs, CP violation, and electron stability.

The structural components appear first. The fermion-boson distinction emerges from the chart-glue data of the $q$-projective bundle. Chirality is modeled as a continuous phase rotation in the pre-observable sector. The stability of the trefoil vortex against chirality flips is examined. The crossing energy decomposes into a strong channel and a Coulomb channel, which physically correspond to confinement and electromagnetism. This decomposition imposes an infinite-energy obstruction to time reversal in the observable sector.

The section concludes with virtual particles and CP violation. Virtual particles are identified as excitations of the exceptional divisor. The vacuum-polarization diagrams required by the Breit–Wheeler vertex are resolved via Skein relations. Experimental constraints on CP violation are summarized, and the CP phase is conjecturally identified with the imaginary part of the alternating-block character. The chirality picture is extrapolated to cosmological extremes. Finally, the electron trefoil is shown to be a stable building block under the Markov trace, forbidding beta decay.

_(draft.)_
<!-- FILE_END: complexity-interpretation-intro.md -->

<!-- FILE_START: fermion-boson-chart-localization.md -->
The [fermion--boson decomposition](#def:fermion-boson-decomposition) specifies that bosons are purely horizontal ($\alpha_V = 0$) while fermions possess non-trivial vertical projections. This admits a transparent geometric reading on the quantum projective line.

By the [spectral--chart correspondence](#prop:spectral-chart-correspondence), the symmetric and antisymmetric eigenspaces $S^2 V \oplus \Lambda^2 V$ of the braiding $c_{V,V}$ form the spectral data that pin the chart-transition coefficient of $\mathbb{P}_q(V)$ to $\kappa = q^{-1}$. The bosonic sector lives on $S^2 V$ with eigenvalue $\lambda_+ = q$. This is the classical channel that degenerates to the symmetric monoidal $\mathbb{P}(V)$ at $q = 1$. The fermionic sector lives on the unit summand $\Lambda^2 V \cong \mathbf{1}$ with eigenvalue $\lambda_- = -q^{-1}$, where the chart-glue is concentrated.

We read $\kappa = q^{-1} = \lambda_+^{-1} = -\lambda_-$ as the parameter determined by the antisymmetric channel. This makes precise the colloquial statement that $q$ calibrates how much vertical (fermionic) content survives passage between charts. At $q = 1$, we recover $\kappa = 1$, and the two sectors decouple into the classical inversion $z \cdot w = 1$. When $q \neq 1$, the geometry deforms the glue and ties the fermionic content to the substrate parameter via the Hecke data that fixes $c_{V,V}$ on $V \otimes V$. This constitutes the geometric face of the action computed in [observation fermion action](#rem:observation-fermion-action). The non-trivial chart-transition carries the fermionic backreaction of an observation, and the substrate parameter acts as the chart-glue itself.
<!-- FILE_END: fermion-boson-chart-localization.md -->

<!-- FILE_START: complex-chirality-rotation.md -->
Let $q = |q|e^{i\theta}$ be a complex substrate parameter with $|q| > 1$ and $\theta \in (-\pi, \pi]$, as described in the [complex substrate interpretation](#rem:complex-substrate-interpretation).

**Conjecture.**
In the pre-observable sector (prior to imposing the dagger positive-definiteness axiom), the phase $\theta$ governs the particle-antiparticle distinction:

1. **Crossing energy acquires a phase.** For a torus knot $T_{p,k}$ with [crossing energy](#def:crossing-energy) $\mathcal{S}_c(T_{p,k}; q)$, the complex extension satisfies

   $$
     \mathcal{S}_c(T_{p,k}; |q|e^{i\theta})
     = 
     \mathcal{S}_c(T_{p,k}; |q|)e^{in_c\theta},
   $$

   where $n_c$ denotes the crossing number. The mirror image $T_{p,k}^{\sigma}$ carries crossing number $-n_c$, yielding $\mathcal{S}_c(T_{p,k}^{\sigma}) = \mathcal{S}_c(T_{p,k}; |q|)e^{-in_c\theta}$.

2. **Chirality interpolation.** Define the chirality operator $\mathcal{X}_\varphi \colon \theta \mapsto \theta + \varphi$ acting on the phase of $q$. Then:
   - At $\varphi = 0$: the operation acts as the identity.
   - At $\varphi = \pi / n_c$: crossing energies of particle and antiparticle equalize in magnitude and oppose in phase.
   - At $\varphi = \pi$: full chirality reversal occurs ($q \mapsto |q|e^{i(\theta + \pi)}$).
   
   The discrete electron/positron flip detailed in the [chirality remark](#rem:chirality-trefoil-electron-positron) emerges as the endpoint $\varphi = \pi$ of this continuous rotation.

3. **CPT as $\mathbb{Z}_2$ quotient.** The observable sector ($\theta = 0$) accesses only the $\mathbb{Z}_2$ quotient of this $\mathrm{U}(1)$ action. Charge conjugation C operates as the residue of the continuous chirality rotation, modulo the observability constraint. Parity P and time reversal T descend from continuous operations in the pre-observable sector. The CPT theorem asserts that the total rotation $\mathcal{X}_\pi \circ P \circ T$ acts as a symmetry of the categorical action ([categorical action](#def:categorical-action)).

**Experimental discriminant.** Any residual signature of the pre-observable phase $\theta$ surviving projection to the observable sector manifests as a CP-violating phase in crossing-energy ratios. For the electron-positron system:

$$
  \delta_{\mathrm{CP}}
  = 
  \frac{|\mathcal{S}_c(T_{2,3})| - |\mathcal{S}_c(T_{2,3}^{\sigma})|}{|\mathcal{S}_c(T_{2,3})| + |\mathcal{S}_c(T_{2,3}^{\sigma})|}
   \sim 
  \mathcal{O}(\theta^2).
$$

This vanishes to first order, aligning with the near-exact equality of electron and positron masses. It contributes at second order to CP violation in hadronic systems where multiple crossing numbers interact.
<!-- FILE_END: complex-chirality-rotation.md -->

<!-- FILE_START: trefoil-vortex-chirality-flip.md -->
The open question posed in the [chirality remark](#rem:chirality-trefoil-electron-positron) — *can a vortex tube in the brane fluid reverse its circulation?* — has a sharp answer in classical fluid dynamics. The gap between that answer and the categorical framework is itself informative.

**Classical result: trefoil vortices are unstable.**
Kleckner and Irvine \cite{kleckner2013} created trefoil-knotted vortex loops in water and tracked their evolution. The trefoil vortex unties itself within a few circulation timescales via vortex reconnection events. Two anti-parallel filament segments approach, reconnect, and separate with exchanged topology. Scheeler et al. \cite{scheeler2014} showed that helicity $\mathcal{H} = \int \mathbf{v} \cdot \boldsymbol{\omega} dV$ is approximately conserved during reconnection but redistributes from writhe (global coiling) to twist (local spinning):

$$
  \mathcal{H} =  \underbrace{Wr}_{\text{writhe}}
  +  \underbrace{Tw}_{\text{twist}}, \qquad
  \Delta Wr = -\Delta Tw \quad (\text{during reconnection}).
$$

After several reconnections the trefoil reduces to unknotted loops. Each loop carries a portion of the original helicity as twist. No chirality flip occurs. The trefoil dissolves.

**Obstructions to classical chirality reversal.**

Three obstructions prevent a smooth chirality reversal in Navier--Stokes fluid dynamics:

1. **Kelvin's theorem.** In ideal fluids, circulation $\Gamma = \oint \mathbf{v} \cdot d\mathbf{l}$ around a material loop is conserved. Reversing the sign of $\Gamma$ requires external forcing or viscous dissipation. It cannot happen spontaneously in an inviscid flow.
2. **Topological protection of writhe sign.** The writhe $Wr$ of a trefoil is $\pm 3$. To flip from $+3$ to $-3$ requires passing through $Wr = 0$ (the unknot). The trefoil must first untie completely and then re-tie with opposite handedness. Reconnection events only reduce $|Wr|$.
3. **Dissipation at reconnection sites.** Each reconnection event converts kinetic energy into heat via viscous dissipation. The trefoil has three essential crossings. Complete untying dissipates energy $\sim 3 \Gamma^2 \rho$ (per unit length). There is no energy budget for re-tying.

**The categorical trefoil is different.**
In the QOU framework, the trefoil is not a fluid-dynamical vortex filament. It is an element of the representation ring of $\mathrm{SU}_q(2)$.

| Property | Classical vortex | Categorical trefoil |
|----------|-----------------|---------------------|
| Identity | Embedding $S^1 \hookrightarrow \mathbb{R}^3$ | Knot type (isotopy class) |
| Stability | Reconnection-unstable | Topologically protected |
| Circulation | Continuous $\Gamma \in \mathbb{R}$ | Quantised by Casimir $[j]_q[j+1]_q$ |
| Chirality | Sign of $Wr$ (embedding-dependent) | Knot invariant (left vs right trefoil) |
| Helicity transfer | $Wr \leftrightarrow Tw$ | No classical analogue; encoded in $R$-matrix |

The categorical trefoil's chirality is a knot invariant, not an embedding property. The Jones polynomial distinguishes $T_{2,3}$ from $T_{2,3}^{\sigma}$: $J_{T_{2,3}}(q) \neq J_{T_{2,3}^{\sigma}}(q)$. No continuous deformation can convert one to the other.

**Three routes to chirality reversal in the QOU.**

The theory offers three mechanisms for chirality reversal:

1. **Passage through the exceptional divisor.** The [fiber adjoint involution](#prop:fiber-adjoint-involution) reverses the Reeb flow direction. If it extends to the [exceptional divisor](#def:exceptional-divisor), it maps $T_{2,3}$ to $T_{2,3}^{\sigma}$. This is not a continuous deformation but a discrete jump at the blow-up locus. It is the categorical analogue of a pair-creation event. The knot type is destroyed and its mirror is created.
2. **Complex substrate rotation.** In the pre-observable sector ([complex substrate interpretation](#rem:complex-substrate-interpretation)), the chirality operator $\mathcal{X}_\varphi$ rotates the phase of $q$ continuously. The [chirality rotation conjecture](#conj:complex-chirality-rotation) proposes that the discrete flip $T_{2,3} \leftrightarrow T_{2,3}^{\sigma}$ is the $\mathbb{Z}_2$ shadow of a continuous $\mathrm{U}(1)$ rotation in the $\theta$-direction. Upon projection to the observable sector ($\theta = 0$), only the endpoints of this rotation survive as particle and antiparticle.
3. **Reconnection as Reidemeister move.** The classical reconnection events correspond to local Reidemeister moves (R-II). In the categorical setting, R-II moves do not change the knot type. They change the embedding, altering crossing energy and binding energy while leaving the bare mass and particle identity invariant. The writhe $Wr$ changes by $\pm 2$ per R-II move. This physically corresponds to orbital shell transitions, not chirality reversal. To change the knot type requires crossing a topological barrier that R-II moves cannot surmount.

**Summary.**
A classical trefoil vortex in a real fluid cannot flip chirality. It unties and dissipates. The categorical trefoil is topologically stable and its chirality is a knot invariant, protected against continuous deformation. Chirality reversal requires either a discrete passage through the exceptional divisor (pair creation), a continuous rotation in the pre-observable complex-$q$ sector, or both. The classical vortex reconnection phenomenon maps to shell transitions (R-II Reidemeister moves), not chirality reversal.
<!-- FILE_END: trefoil-vortex-chirality-flip.md -->

<!-- FILE_START: crossing-energy-decomposition.md -->
The [crossing energy](#def:crossing-energy) assigns weight $+q$ to positive crossings and $-q^{-1}$ to negative crossings, where $q > 1$. Writing $q = e^\lambda$ with $\lambda = \ln q > 0$, the crossing weights decompose into symmetric and antisymmetric components under the mirror operation $\sigma$:

$$
  q = \cosh\lambda + \sinh\lambda, \qquad
  q^{-1} = \cosh\lambda - \sinh\lambda.
$$

**Statement.**
Let $\mathfrak{H}$ be a knot composite with crossing energy $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = \sum_i \epsilon_i$, where $\epsilon_i \in \{q, -q^{-1}\}$.

1. **Symmetric channel.** The component $E_{\mathrm{sym}}(\mathfrak{H}) = \sum_i |\epsilon_i| \cdot \cosh(\ln q) \cdot \mathrm{sgn}(\epsilon_i)$ remains invariant under the mirror operation $\sigma$, which reverses all crossing signs.
2. **Antisymmetric channel.** The component $E_{\mathrm{asym}}(\mathfrak{H}) = \sum_i |\epsilon_i| \cdot \sinh(\ln q) \cdot \mathrm{sgn}(\epsilon_i)$ reverses sign under $\sigma$.
3. **Pair cancellation.** For a particle-antiparticle pair $(\mathfrak{H}, \mathfrak{H}^{\sigma})$, the combined crossing energy is strictly antisymmetric:

   $$
     \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) + \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}^{\sigma})
     = 2E_{\mathrm{asym}}(\mathfrak{H}).
   $$

4. **Ratio identity.** The antisymmetric-to-symmetric ratio is

   $$
     \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}}
     = \tanh(\ln q),
   $$

   which is independent of the specific knot composite $\mathfrak{H}$.

## Algebraic-to-hyperbolic bridge

This decomposition serves as the per-crossing instance of a general identity. Writing $\lambda = \ln q$, every algebraic $q$-power maps to a hyperbolic exponential:

$$
  q^{n} = \cosh(n\lambda) + \sinh(n\lambda),
  \qquad
  q^{n} - q^{-n} = 2\sinh(n\lambda).
$$

Consequently, the **quantum integer expresses a ratio of hyperbolic sines**:

$$
  [n]_q \;=\; \frac{q^{n} - q^{-n}}{q - q^{-1}}
  \;=\; \frac{\sinh(n\lambda)}{\sinh(\lambda)}.
$$

This details how the Hecke datum is archimedean: the discrete algebraic invariant $[n]_q \in \mathbb{Z}[q^{\pm 1/2}]$ evaluates the transcendental hyperbolic sine at the crossing rapidity $\lambda$. It functions as the $q$-deformed seed of the Kashaev volume realization ([Kashaev as Archimedean realisation](#rem:kashaev-as-archimedean-realization)), where the $N \to \infty$ limit of the colored Jones polynomial integrates these hyperbolic lengths into the transcendental knot volume. The $\cosh = q^{n} + q^{-n}$ symmetric (strong) and $\sinh = q^{n} - q^{-n}$ antisymmetric (Coulomb) channels represent the real and "rotational" parts of that exponential.

These identities are formalized in the Lean sibling (`q_pow_eq_cosh_add_sinh`, `two_sinh_nat_log`, `qbracket_eq_sinh_ratio`), holding valid for all $q > 0$.
<!-- FILE_END: crossing-energy-decomposition.md -->

<!-- FILE_START: crossing-energy-interpretation.md -->
The [decomposition](#prop:crossing-energy-decomposition) isolates crossing energy into two physically distinct channels.

**Channel identification.**

| Channel | Weight per crossing | Mirror behaviour | Physical force |
|---------|-------------------|-----------------|----------------|
| Symmetric | $\cosh(\ln q)$ | Invariant under $\sigma$ | **Strong binding** |
| Antisymmetric | $\sinh(\ln q)$ | Reverses under $\sigma$ | **Coulomb (electromagnetic)** |

The symmetric part contributes identically to particle and antiparticle. It binds regardless of charge. The antisymmetric part imposes opposing effects on particle and antiparticle. It distinguishes charges.

**Pair creation: why the pair flies apart.**

When an $e^- e^+$ pair is created, pair cancellation yields:

$$
  \mathfrak{E}_{\mathrm{cross}}(e^-) + \mathfrak{E}_{\mathrm{cross}}(e^+)
  = 6\sinh(\ln q)
  \approx 0.630 \quad (\text{Skein units}).
$$

The symmetric (strong) contributions perfectly cancel. The residual $6\sinh\lambda > 0$ provides pure Coulomb repulsion, driving the pair apart.

**EM/strong ratio.**

At $q = q_0$:

$$
  \tanh(\ln q_0) \approx 0.104.
$$

Electromagnetism operates at roughly **10\%** of the strong force magnitude at the constituent (Skein) scale.

**Crossing energy table** for a particle with $n_c$ positive crossings:

| Quantity | Formula | $T_{2,3}$ ($n_c = 3$) | Value |
|----------|---------|----------------------|-------|
| Total crossing energy | $n_cq$ | $3q$ | $3.330$ |
| Strong component | $n_c\cosh(\ln q)$ | $3\cosh(\ln q)$ | $3.015$ |
| Coulomb component | $n_c\sinh(\ln q)$ | $3\sinh(\ln q)$ | $0.315$ |
| Pair net energy | $n_c(q - q^{-1})$ | $3(q - q^{-1})$ | $0.630$ |
| EM/strong ratio | $\tanh(\ln q)$ | $\tanh(\ln q)$ | $0.104$ |

The [Hopf stability](#prop:torus-hopf-stability) result $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$ dictates that the strong symmetric channel dominates the Coulomb antisymmetric channel for the proton, ensuring structural stability.
<!-- FILE_END: crossing-energy-interpretation.md -->

<!-- FILE_START: time-reversal-energy-barrier.md -->
The Feynman--Stueckelberg interpretation identifies the [positron](#def:positron-knot) as an electron traveling backward in time. In the QOU framework, "time reversal" of a particle means chirality reversal of its constituent knots. It replaces every $T_{2,3}$ with $T_{2,3}^{\sigma}$. This operation requires infinite energy in the observable sector for all stable particles.

**Elementary fermions (electron).**
The electron is the left trefoil $T_{2,3}$. No continuous deformation connects $T_{2,3}$ to $T_{2,3}^{\sigma}$ ([trefoil vortex chirality flip](#rem:trefoil-vortex-chirality-flip)). They lie in different connected components of knot space, distinguished by the Jones polynomial. In the observable sector ($q \in \mathbb{R}$, $q \geq 1$), crossing a topological barrier between connected components requires energy

$$
  \mathfrak{E}_{\text{flip}}(e^-) =  +\infty.
$$

No finite-energy process can convert a single electron into a single positron. The only accessible process is [pair creation](#rem:pair-creation-energy) at the exceptional divisor. This creates a new pair at a cost of $2m_e \approx 1.022$ MeV while leaving the original electron unchanged.

**Composite fermions (proton, neutron).**
The proton is a [Borromean baryon](#def:borromean-baryon): $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \oplus \mathcal{L}_H$. It is built from trefoils linked by the Hopf link. Its antiparticle $\mathfrak{p}^{\sigma}$ replaces every $T_{2,3}$ with $T_{2,3}^{\sigma}$ ([chirality remark](#rem:chirality-trefoil-electron-positron)).

The topological protection is equally strong for composites:

1. **Link type is a topological invariant.** The Borromean link $\mathcal{B}_3$ and its mirror $\mathcal{B}_3^{\sigma}$ are distinguished by the Milnor triple linking number $\bar{\mu}(123) = \pm 1$. No Reidemeister sequence connects them.
2. **Each constituent is independently protected.** Every quark trefoil in the proton would need to flip chirality independently. Each flip costs infinite energy.
3. **The Hopf linking is chirality-sensitive.** The Hopf link $\mathcal{L}_H$ binding the quarks has linking number $+1$. Its mirror has $-1$. Reversing this requires destroying and recreating the link.

Therefore:

$$
  \mathfrak{E}_{\text{flip}}(\mathfrak{p}) =  +\infty, \qquad
  \mathfrak{E}_{\text{flip}}(\mathfrak{n}) =  +\infty.
$$

The only way to produce $\mathfrak{p}^{\sigma}$ is pair creation at the exceptional divisor. This costs $2m_p \approx 1876.5$ MeV. Similarly, antineutron creation costs $2m_n \approx 1879.1$ MeV.

**Beta decay is not chirality reversal.**
A neutron can convert to a proton via $\mathfrak{n} \to \mathfrak{p} + e^- + \bar{\nu}_e^{\sigma}$, but this is not time reversal. Beta decay changes the crossing orientation partition of the Borromean link (from $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ to $[\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]$). This is an R-I embedding move that alters binding energy while preserving both the Borromean link type and the chirality of each constituent trefoil. No trefoil flips from left to right. Instead, one quark flavor changes ($\mathfrak{d} \to \mathfrak{u}$) within the same chirality sector.

**Summary.**

| Particle | Chirality reversal energy | Pair creation threshold |
|----------|--------------------------|----------------------|
| Electron $e^-$ | $\infty$ | $2m_e \approx 1.022$ MeV |
| Proton $\mathfrak{p}$ | $\infty$ | $2m_p \approx 1876.5$ MeV |
| Neutron $\mathfrak{n}$ | $\infty$ | $2m_n \approx 1879.1$ MeV |
| Neutrino $\nu$ | $\infty$ | $\approx 0$ (massless to leading order) |

Sending a particle backward in time is indistinguishable from chirality reversal. The infinite energy barrier applies universally to all particles built from trefoil generators. The only physical process that produces the time-reversed partner is pair creation. This creates a new pair from the vacuum at the exceptional divisor without reversing the original particle.
<!-- FILE_END: time-reversal-energy-barrier.md -->

<!-- FILE_START: virtual-particles-exceptional-divisor.md -->
In quantum field theory, virtual particles are internal lines in Feynman diagrams: off-shell excitations that mediate forces and contribute to loop corrections but are never directly detected. Their existence is bounded by the Heisenberg uncertainty relation $\Delta E \cdot \Delta t \gtrsim \hbar$. The QOU framework provides a geometric home for this phenomenon.

**The exceptional divisor as the virtual stage.**

At each brane point $p \in M$, the blow-up replaces $p$ with an [exceptional divisor](#def:exceptional-divisor) $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$. This sphere parametrizes the directions of departure from the base manifold — the internal degrees of freedom invisible to the base-level observer.

A virtual particle is an excitation that lives within the Reeb bundle over $\mathcal{S}_p$, which is the Hopf fibration $U(1) \hookrightarrow S^3 \to \mathcal{S}_p$ where all braiding takes place ([vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)). It is created at the blow-up locus, propagates along the exceptional divisor (or up into the [brane tower](#def:recursive-brane-tower) rooted at $\mathcal{S}_p$), and is reabsorbed before it can descend to the base level $A_0$.

**Brane tower levels as virtual depth.**

The [recursive brane tower](#def:recursive-brane-tower) $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ stratifies excitations by their [jet prolongation](#prop:jet-prolongation) level. Physical (on-shell) particles live at level $A_0$ as knot configurations in the base algebra. Virtual particles live at levels $A_n$ with $n \geq 1$:

| Tower level | Algebra | Physical interpretation |
|-------------|---------|----------------------|
| $A_0 = A$ | Coordinate ring $\mathcal{O}(\mathrm{SU}(2))$ | On-shell particles: knots in base manifold |
| $A_1 = J^1(A_0)$ | Sections of frame bundle | 1-virtual: connection fluctuations (gauge bosons) |
| $A_2 = J^1(A_1)$ | Second jet sections | 2-virtual: curvature fluctuations (graviton-like) |
| $A_n$ | $n$-th jet sections | $n$-virtual: $n$-th derivative corrections |

Each level $A_n$ has dimension $3^n \cdot \dim A_0$ (for $\mathrm{SU}(2)$). The state space grows exponentially with virtual depth, but the projection back to $A_0$ collapses all higher-level structure.

**Non-observability of virtual particles.**

An excitation at level $A_n$ ($n \geq 1$) is invisible at $A_0$ because the canonical projection $\pi_0 \colon A_n \to A_0$ annihilates the $\Omega^1$ components:

$$
  \pi_0(f \otimes \omega_1 \otimes \cdots \otimes \omega_n)
  = 
  f \cdot \varepsilon(\omega_1) \cdots \varepsilon(\omega_n),
$$

where $\varepsilon$ is the counit. For a form $\omega$ with no constant part ($\varepsilon(\omega) = 0$), the entire excitation projects to zero at the base level. The virtual particle exists in the tower but casts no shadow on $A_0$.

This is the categorical analogue of the statement that virtual particles are "off-shell". They satisfy the equations of motion at their tower level but not at the base level. The base-level observer sees only the net effect: a correction to the propagator, an effective force, a shift in energy levels. They never observe the virtual excitation itself.

**Lifetime from the Heisenberg commutator.**

The [Heisenberg commutator](#rem:heisenberg-commutator) at level $n$ of the tower is

$$
  [\hat{X}, \hat{P}]_{q_n} =  J\hbar_{q_n}, \qquad
  \hbar_{q_n} =  1 - q_n^{-1},
$$

where $q_n$ is the substrate parameter at the $n$-th level. The uncertainty bound $\Delta E \cdot \Delta t \geq \hbar_{q_n} / 2$ limits the lifetime of a virtual excitation at level $n$:

$$
  \Delta t_{\text{virtual}}
   \leq 
  \frac{\hbar_{q_n}}{2\Delta E}.
$$

For an excitation that borrows energy $\Delta E$ from the vacuum at the exceptional divisor, this is the maximum time before the excitation must be reabsorbed. The excitation's worldline stays within the tower. It is created at $\mathcal{S}_p$, propagates through $A_1, A_2, \ldots$, and returns to $\mathcal{S}_p$ without ever descending to $A_0$.
<!-- FILE_END: virtual-particles-exceptional-divisor.md -->

<!-- FILE_START: vacuum-polarization-virtual-pairs.md -->
**Virtual pairs at the exceptional divisor.**

The [pair creation energy](#rem:pair-creation-energy) analysis shows that a photon with $E \geq 2m_e$ can create a real $e^-e^+$ pair at the exceptional divisor. Photons with $E < 2m_e$ create a virtual pair. This is a trefoil and its mirror that exist within $\mathcal{S}_p$ for a time $\Delta t \leq \hbar_q / (2m_e - E)$ before annihilating back.

This is the QOU description of vacuum polarization. The photon briefly resolves into a virtual $e^-e^+$ pair within the exceptional divisor. This modifies the effective coupling constant. The pair never reaches $A_0$. It lives and dies in the blow-up geometry.

**Virtual exchange as Skein resolution.**

In the [Reidemeister mass invariance](#conj:reidemeister-mass-invariance) framework, a virtual pair corresponds to an R-II move. Two crossings of opposite sign are temporarily introduced and then removed. The Skein resolution of this pair produces a correction term $(q - q^{-1}) \cdot L_0$. This modifies the crossing energy without changing the knot type. This is precisely a virtual exchange: the topology remains unchanged while the energy receives a perturbative correction from the transient crossing pair.

**Summary.**
The QOU realization of each QFT concept is summarized in [Table: QFT concepts and their QOU brane-tower realizations](#tbl:vacuum-polarization-virtual-pairs-table-data).

Virtual particles are genuine excitations of the brane tower that happen to be invisible at the base level. Their home is the exceptional divisor and the tower growing from it. They mediate forces, correct energies, and polarize the vacuum. They are never seen because their worldlines never descend to $A_0$.
<!-- FILE_END: vacuum-polarization-virtual-pairs.md -->

<!-- FILE_START: cp-violation-evidence.md -->
**Definition of CP violation.**
CP symmetry combines charge conjugation C (swapping particles with antiparticles) and parity P (mirroring spatial coordinates). Under exact CP symmetry, matter and antimatter would behave as perfect mirror images. **CP violation** occurs when processes distinguish matter from antimatter fundamentally.

**Experimental evidence.**

CP violation is established in three systems:

1. **Neutral kaons** (1964). Cronin and Fitch observed the long-lived kaon $K_L$ decaying to two pions: $K_L \to \pi^+\pi^-$ at a rate of $\sim 2 \times 10^{-3}$ \cite{christenson1964}. CP symmetry dictates decay to three pions only. This was the first evidence of CP violation.
2. **$B$ mesons** (2001). The BaBar \cite{aubert2001} and Belle experiments measured CP-violating asymmetries in $B^0 \to J/\psi\, K_S$ decays. This confirmed the Kobayashi-Maskawa mechanism: the CKM quark-mixing matrix contains an irreducible complex phase $\delta_{\mathrm{CKM}}$.
3. **$D$ mesons** (2019). LHCb observed CP violation in charm decays ($D^0 \to K^+K^-$ versus $D^0 \to \pi^+\pi^-$) at the $10^{-4}$ level.

**The matter-antimatter asymmetry.**

Sakharov (1967) identified three necessary conditions for the universe's baryon asymmetry:
1. Baryon number violation.
2. C and CP violation.
3. Departure from thermal equilibrium.

The Standard Model CKM phase satisfies the second condition but remains quantitatively insufficient to explain the observed ratio $n_B / n_\gamma \sim 6 \times 10^{-10}$. Additional sources of CP violation are necessary.

**QOU interpretation.**

Under the [complex chirality rotation](#conj:complex-chirality-rotation) framework, CP violation originates from a residual phase $\theta$ of the complex substrate parameter $q = |q|e^{i\theta}$:

- The observable sector projects $\theta \to 0$, but a small residual phase $\theta_{\mathrm{res}}$ may survive an imperfect projection.
- The CP-violating discriminant scales as $\delta_{\mathrm{CP}} \sim \mathcal{O}(\theta_{\mathrm{res}}^2)$ for single-crossing systems like the electron-positron pair.
- For **multi-crossing composites** such as kaons (quark-antiquark pairs with multiple internal crossings), the phase accumulates linearly: $\delta_{\mathrm{CP}} \sim n_c\theta_{\mathrm{res}}$, where $n_c$ is the total crossing number of the hadronic braid word.
- This gives a **geometric origin** for the CKM phase. It represents the total accumulated crossing phase from the complex-$q$ sector, projected onto the observable quark-mixing matrix.

**Quantitative gap.**

The [crossing energy decomposition](#prop:crossing-energy-decomposition) yields an electromagnetic-to-strong ratio of $\tanh(\ln q) \approx 0.104$. If the residual phase scales similarly — $\theta_{\mathrm{res}} \sim \tanh(\ln q) \cdot \alpha_{\mathrm{EM}}$ — then $\delta_{\mathrm{CP}} \sim 10^{-3}$. This magnitude correctly aligns with kaon CP violation but falls short of explaining baryogenesis. The required enhancement likely emerges from the **cosmological regime**, where the observability constraint itself breaks down.
<!-- FILE_END: cp-violation-evidence.md -->

<!-- FILE_START: cp-violation-spectral-form.md -->
**Conjecture (spectral form of $\delta_{\mathrm{CP}}$).**
*Let $A = H_n(R_\mathbb{C}, q)$ with complexified ground ring $R_\mathbb{C} = R \otimes \mathbb{Z}[i]$, permitting $q = |q| \exp(i\theta)$ as detailed in ([complex chirality rotation](#conj:complex-chirality-rotation)). For a hadronic braid $\beta_\mathcal{K} \in B_n$, the CP-violating discriminant is the imaginary part of the alternating/symmetric Wedderburn-block trace ratio:*

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

*The real part recovers the Pauli statistical weight ([Pauli factor](#prop:pauli-factor-wedderburn)). The imaginary part isolates CP violation. CP-symmetric configurations (amphicheiral or real-$q$) have $\mathrm{Im}(\chi_\lambda) = 0$ and $\delta_{\mathrm{CP}} = 0$.*

**Phase accumulation.**
*For multi-crossing composites, the residual phase $\theta_{\mathrm{res}}$ of $q$ accumulates linearly in the crossing count. Writing the leading character behavior as $\chi_\lambda(q) = \chi_\lambda(|q|) \exp(i\, n_\lambda \theta)$:*

$$
  \mathrm{Im}\!\left(
    \frac{\chi_{(1^n)}(\beta_\mathcal{K})}
         {\chi_{(n)}(\beta_\mathcal{K})}
  \right)
  \;\sim\; \bigl(n_{(1^n)} - n_{(n)}\bigr) \cdot \theta_{\mathrm{res}}
$$

*to leading order in $\theta_{\mathrm{res}}$. The term $n_{(1^n)} - n_{(n)}$ is the difference of phase exponents on the two extremal blocks. For multi-crossing structures like kaons, this difference scales with the total crossing number. This recovers the empirical $\delta_{\mathrm{CP}} \sim n_c \theta_{\mathrm{res}}$ relation from ([CP violation](#sec:cp-violation-evidence)).*

**Sketch.**
Spectral completeness over $R_\mathbb{C}$ (the complexified analogue of the real spectral completeness for $\alpha_{\mathrm{EM}}$) decomposes $F_{\mathrm{Pauli}}$ into central-idempotent characters. The alternating block $V_{(1^n)}$ provides the sole source of phase asymmetry. Its character carries $(-q)^{-w}$ on a writhe-$w$ crossing ([antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)), while the symmetric block carries $q^w$. The imaginary part of their ratio isolates the CP-violating amplitude.

**Falsifiability.**
This framework mandates that amphicheiral knots yield exactly $\delta_{\mathrm{CP}} = 0$. Any observed CP violation in a single amphicheiral hadron strictly falsifies this spectral characterization. The non-amphicheiral $\bar{u}s$ configuration of the kaon system ($K_L \to \pi\pi$ at $\sim 2 \times 10^{-3}$) serves as the primary empirical test.

*Remark.* This conjecture depends on ([complex chirality rotation](#conj:complex-chirality-rotation)). Promoting it to a formal proposition requires:
(a) A categorical proof that $R_\mathbb{C}$-enrichment is the unique CP-violating extension.
(b) A quantitative match between $\theta_{\mathrm{res}}$ and the Wolfenstein parameterization of the CKM matrix.

**Archimedean specialisation (§7c).** This block relies on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs: real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical or $q$-deformation identities it draws on remain valid over an abstract coefficient ring. Only their archimedean realization is specialized here.
<!-- FILE_END: cp-violation-spectral-form.md -->

<!-- FILE_START: cosmological-chirality-flip.md -->
The [time reversal barrier](#rem:time-reversal-energy-barrier) shows that chirality reversal requires infinite energy **in the observable sector**. Here, the Frobenius form is non-degenerate and $q$ must be real. The [cosmological limits](#ex:cosmological-limits) identify two regimes where this topological protection fails.

**Formalization status.** The claims below are conjectural. The cosmological limits block provides an example with a conjectural interpretation. The Frobenius degeneration at $q \to \infty$ is not formalized in Lean. The only proven limits are the trivial evaluations $\hbar_q(1) = 0$ and $|\hbar_q(q) - 1| < \epsilon$ for large $q$. The categorical description of initial and terminal objects in a category of degenerations remains a research direction.

**At the Big Bang ($q \to \infty$).**

The Frobenius form degenerates: $\int_A(f^\dagger f) \sim q^{-1} \to 0$. The [Heisenberg commutator](#rem:heisenberg-commutator) $[\hat{X}, \hat{P}]_q \to J$ reaches its maximum, rendering all observables maximally non-commutative. The positive-definiteness axiom that forces $q$ to be real no longer constrains the system. With a degenerate Frobenius pairing, the dagger structure has no norm to be positive-definite against.

In this regime, $q$ can acquire an imaginary part $\theta \neq 0$. The [complex substrate interpretation](#rem:complex-substrate-interpretation) permits continuous chirality rotation in the fibers. At each blow-up point, the [exceptional divisor](#def:exceptional-divisor) $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ acts as the space where trefoils and their mirrors interconvert via the phase rotation $\mathcal{X}_\varphi$. The chirality flip occurs **in the fibers**, not at the base level.

Sakharov's conditions are met here:
1. Frobenius form degeneration permits baryon number violation (topological protection weakens when the pairing degenerates).
2. The complex phase $\theta$ provides CP violation.
3. The Big Bang itself supplies the departure from equilibrium.

**At heat death ($q \to 1$).**

The Hopf algebra becomes cocommutative ($\sigma \circ \Delta = \Delta$), [$\hbar_q \to 0$](#def:substrate-parameter), and by [prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction) the three Descartes color tubes collapse to a single $\mathrm{U}(1)$ phase tube on $\mathcal{X}_5$. The crossing-energy asymmetry $q - q^{-1} = 2\sinh(\ln q) \to 0$ vanishes. Chirality becomes undetectable: $T_{2,3}$ and $T_{2,3}^{\sigma}$ merge, and the strong and Coulomb channels unify. Only the two $S_5$-equivariant generators ([rem:symmetry-preserving-leptons](#rem:symmetry-preserving-leptons)) — the electron and muon — survive as distinguishable topological excitations. Their masses vanish alongside $q - q^{-1}$.

**Categorical picture (conjectural).**

The correct categorical framework for these limits requires a **category of QOU degenerations** $\mathbf{QOU}_{\mathrm{deg}}$. Its objects are triples $(\mathbf{C}, A, \tau)$ equipped with a substrate parameter $q$. Its morphisms are structure-preserving maps that may selectively degrade axioms:

- The **initial object** represents the Big Bang state. This is the maximally degenerate state where $q = \infty$, the Frobenius form vanishes, and the only data is the [bundle initial condition](#def:bundle-initial-conditions) $E_0 = \sum_i (p_i, H_i)$ (positions without momenta). Every state with finite $q$ receives a unique morphism from this initial object (time evolution from the singularity).
- The **terminal object** is [Bring's surface](#thm:descartes) $\Sigma_4$, which is terminal in $\mathbf{C}_{-6}$. In the degeneration category, the $q = 1$ classical limit acts as the terminal object. Every state admits a unique morphism to the fully cocommutative structure by sending $q \mapsto 1$.
- The **observable era** forms the full subcategory on objects with $1 < q < \infty$, where all axioms hold non-degenerately.

This picture lacks formalization. The necessary steps are:
1. Defining "degenerate QOU" precisely by weakening the Frobenius non-degeneracy axiom.
2. Proving the $q \to \infty$ limit is initial (showing the bundle initial condition determines all subsequent time evolution).
3. Proving $q \to 1$ is terminal (showing the classical projection is unique and structure-preserving).
4. Formalizing these definitions and proofs in Lean.

**The aeon boundary.**

At both cosmological extremes, the fiber geometry permits actions forbidden in the observable interior. Between these endpoints, the physically meaningful regime $1 < q < \infty$ enforces strict chirality conservation:

1. **Big Bang** (initial object): Frobenius degeneration removes the observability constraint. Chirality flips occur freely in the fibers at the exceptional divisors. The residual complex phase $\theta$ generates matter-antimatter asymmetry via CP violation before the Frobenius form stabilizes.
2. **Observable era** (full subcategory, $1 < q < \infty$): Chirality is frozen. Electrons, protons, and neutrons maintain their handedness. The topological barrier remains infinite.
3. **Heat death** (terminal object): The $q \to 1$ limit erases the chirality distinction. Particles and antiparticles become indistinguishable. Crossing energy vanishes. Matter and radiation merge in the frozen geometry.

If the universe is cyclic — where heat death transitions into the next Big Bang — the chirality flip occurs at the **aeon boundary**. Here the Frobenius form either degenerates ($q \to \infty$) or trivializes ($q \to 1$). The exceptional divisors are the geometric locus of this transition. They provide the space where fibers reset, assigning fresh chirality for the next aeon.

The categorical conjecture frames the aeon transition as a morphism from the terminal object of one copy of $\mathbf{QOU}_{\mathrm{deg}}$ to the initial object of the next. This categorical recycling map preserves topological data (knot types) while resetting metric data (masses, charges).
<!-- FILE_END: cosmological-chirality-flip.md -->

<!-- FILE_START: electron-immortality.md -->
Beta decay converts a neutron to a proton (or vice versa) by changing the crossing orientation partition of the [Borromean baryon](#def:borromean-baryon): $[u,d,d] \to [u,u,d]$. This relies on baryons being composite. They possess internal degrees of freedom (the quark flavour assignments) that rearrange via R-I embedding moves while preserving the Borromean link type.

## Stability of the electron against beta decay

The electron does not beta decay. The reason is topological, not energetic. The electron is the trefoil $T_{2,3}$, an elementary knot with no internal constituents. It lacks a crossing orientation partition to rearrange or substructure to reorganise. No embedding move changes its identity. The electron possesses exactly one degree of freedom—its knot type—which is a topological invariant.

| Particle | Structure | Internal d.o.f. | Beta decay? |
|----------|-----------|----------------|-------------|
| Neutron | $[u,d,d]_p \oplus \mathcal{L}_H$ | Quark flavour partition | Yes: $\mathfrak{n} \to \mathfrak{p} + e^- + \nu^{\sigma}$ |
| Proton | $[u,u,d]_p \oplus \mathcal{L}_H$ | Quark flavour partition | Yes (in nuclei): $\mathfrak{p} \to \mathfrak{n} + e^+ + \nu$ |
| Electron | $T_{2,3}$ | None | **No** |
| Neutrino | $T_{1,0}$ (unknot) | None | **No** |

The electron cannot decay into anything lighter while conserving lepton number and charge. There is no lighter charged lepton. The neutrino (unknot $T_{1,0}$) has zero crossing energy and zero mass, thus it cannot absorb the electron's topological charge.

## Electron survival to heat death

In the observable era ($1 < q < \infty$), the [time reversal barrier](#rem:time-reversal-energy-barrier) prevents chirality reversal. The absence of beta decay prevents flavour change. The electron is therefore immortal in the observable sector. It persists from the moment of its creation (pair production at the exceptional divisor) until the cosmological boundary.

As the universe evolves toward heat death ($q \to 1$):

1. **Bound electrons are liberated**: Atoms ionise as the ambient energy drops below binding thresholds. The electron itself remains unchanged. Its bare mass (a knot invariant) is eternal. Only its binding energy (an embedding property) dissipates.
2. **Free electrons become radiation**: In the $q \to 1$ limit, the crossing energy asymmetry $q - q^{-1} \to 0$ erases the Coulomb distinction. The electron's electromagnetic charge effectively vanishes. What remains is a massless topological excitation, indistinguishable from a photon in the frozen geometry.
3. **Radiation becomes CMB**: The thermal photon bath (including the absorbed electron contribution) redshifts to the cosmic microwave background. The [CMB torsion signature](#rem:cmb-q-torsion) carries the imprint of the $q$-deformed Reeb flow—a fossil record of the substrate parameter's value during earlier epochs.

## Into the next aeon

If the [cosmological chirality flip](#rem:cosmological-chirality-flip) holds, the heat-death boundary marks where chirality distinction collapses ($q \to 1$) and the next aeon's big bang marks where it re-emerges ($q \to \infty$). The CMB radiation from one aeon becomes the initial condition for the next. It carries topological information (knot type) through the boundary, even as metric information (mass, charge) is erased.

In the language of Penrose's Conformal Cyclic Cosmology, the massless, chargeless radiation at heat death is conformally equivalent to the initial singularity of the next aeon. In the QOU framework, this equivalence represents Frobenius degeneration rather than conformal rescaling. The same mathematical structure (the Frobenius form becoming trivial or singular) governs both endpoints, and the exceptional divisors at the boundary reset the topology.

The electron, as a trefoil, is not subject to beta decay. It persists until the concept of existence dissolves into the frozen geometry of the classical limit at $q = 1$.
<!-- FILE_END: electron-immortality.md -->

