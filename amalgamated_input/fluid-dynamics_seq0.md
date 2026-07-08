<!-- FILE_START: fluid-dynamics-intro.md -->
The brane of a quantum observable universe carries a natural fluid dynamics whose viscosity, vortex spectrum, and turbulence structure depend on the substrate parameter $q$. This chapter develops the $q$-deformed Navier--Stokes system on the brane and extracts two principal consequences: global regularity of the $q$-deformed equation for $q > 1$, and a categorical obstruction that controls finite-time blowup in the classical Navier--Stokes equation ($q = 1$).

The first three sections establish the hydrodynamic framework. We derive the $q$-Navier--Stokes equation from the Reeb derivation on the Frobenius--Hopf algebra. We then characterise the discrete vortex spectrum and helicity conservation forced by the braided monoidal structure. Finally, we construct the turbulence theory, including $q$-deformed Kolmogorov scaling and acoustic horizons.

The final two sections prove the chapter's main results. We prove global well-posedness of the $q$-NS system for $q > 1$ via spectral Sobolev estimates on the quantum Peter--Weyl decomposition. We then identify the NS obstruction—a categorical invariant that measures the failure of regularity at $q = 1$. The Hecke algebra computes this obstruction, providing a purely algebraic criterion for the classical Navier--Stokes regularity problem.
<!-- FILE_END: fluid-dynamics-intro.md -->

<!-- FILE_START: brane-fluid.md -->
The brane of a [quantum observable universe](#def:quantum-observable-universe) carries a natural fluid dynamics. The [substrate parameter](#def:substrate-parameter) $q$ sets the effective brane thickness. At $q = 1$, the brane is infinitely thin (classical vacuum). At $q > 1$, it acquires a finite transverse extent governed by the $q$-deformed contact geometry. The resulting dynamics inherits three features absent from classical Navier--Stokes theory:

1. **Algebraic viscosity.** The $q$-Laplacian $\Delta_q$ ([q-Laplacian interpretation](#rem:q-laplacian-interpretation)) replaces the classical Laplacian, and its eigenvalues are $q$-integers $[k]_q$. The viscous dissipation rate is therefore algebraically quantised rather than continuously variable.
2. **Gauge-covariant advection.** The $\mathrm{SU}(2)$ connection $A$ defines the velocity field $v = \nabla_A S$ rather than a flat gradient. Advection along $v$ preserves the horizontal self-duality $F_A|_H = {*_H}F_A|_H$, coupling the fluid motion to the gauge structure.
3. **Topological vortex quantisation.** The $\mathrm{SU}_q(2)$ holonomy constrains the circulation around any closed vortex filament $\varrho$ to discrete values $[j]_q[j+1]_q$, yielding the [discrete vortex spectrum](#prop:discrete-vortex-spectrum).
<!-- FILE_END: brane-fluid.md -->

<!-- FILE_START: madelung-fluid.md -->
**The Madelung split.**
Decomposing $\psi = \sqrt{\rho}\exp(JS/\hbar_q)$ separates the [q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction) into two real equations. Setting the velocity $v = \nabla_A S$ and fluid density $\rho = |\psi|^2$ yields:

- **Continuity:** $\partial_t \rho + \nabla_A\cdot(\rho v) = 0$.
- **Quantum Euler equation:**

$$
  \partial_t v + (v\cdot\nabla_A)v
  =  -\nabla_A\!\left(\frac{\delta\mathcal{H}}{\delta\rho}\right)
  -  \nabla_A Q_q,
  \qquad
  Q_q =  -\frac{\hbar_q^2}{2}\frac{\Delta_q\sqrt{\rho}}{\sqrt{\rho}},
$$

where $Q_q$ is the $q$-deformed quantum pressure.

**$|\psi|^2$ as fluid density; $q$ as brane thickness.**
The [substrate parameter](#def:substrate-parameter) $q$ modulates the effective thickness of the quantum fluid. Near $q \approx 1$, the quantum pressure vanishes ($Q_q \approx 0$) and the system reduces to ordinary inviscid flow. At $q \gg 1$, $Q_q$ dominates; the fluid strongly resists compression. This resistance acts as the inertial mass of the brane.

**Zero-information state $|\psi|^2 = 0$.**
The vacuum $\psi = 0$ carries no medium, no vortex, and no fermion. It lies outside the support of all harmonic modes filtered by the [algebraic filter](#rem:algebraic-filter). As $q \to 1$, $\hbar_q \to 0$: the vacuum represents the state of maximal classical certainty.

**Geodesics as stable vortex filaments.**
Bosonic modes follow straight null geodesics of the acoustic metric $g_{\mathrm{ac}}$. Fermionic modes spiral around the zeros of $\psi$, forming stable vortex filaments $\varrho$ whose mass follows

$$
  m  \propto  \oint_\varrho \|\nabla_A q\|\cdot\|L \wedge F^+\|,
$$

reproducing the [mass identity](#def:mass-identity) as a line integral of the substrate curvature around the vortex core.
<!-- FILE_END: madelung-fluid.md -->

<!-- FILE_START: madelung-acoustic-metric.md -->
**Acoustic metric and analogue gravity.**
Perturbations $\delta\psi$ around a background flow satisfy $\Box_{g_{\mathrm{ac}}}\delta\psi = 0$ for the acoustic metric

$$
  g_{\mathrm{ac}}
  = 
  \frac{\rho}{c_s}
  \begin{pmatrix}
    -(c_s^2 - v^2) & -v^T \\
    -v & \mathbf{1}
  \end{pmatrix},
  \qquad
  c_s^2 = \frac{\partial P}{\partial\rho}\bigg|_{Q_q}.
$$

An acoustic horizon forms wherever $|v| = c_s$, coinciding with a gravitational horizon in the substrate geometry. General relativity emerges as the geometry of non-uniform brane flow: the [GR substrate geometry](#rem:gr-substrate-geometry) is precisely the acoustic manifold. Bosonic modes (where $[F_A, \alpha] = 0$) travel along null acoustic geodesics; fermionic modes ($[F_A, \alpha] \neq 0$) spiral into the vortex filaments of $\psi$.
<!-- FILE_END: madelung-acoustic-metric.md -->

<!-- FILE_START: madelung-divisor-topology.md -->
**Linking and splitting in the divisor.**
The zero-locus $\{\psi = 0\}$ forms a Weil divisor. Each blowup at a ramification point replaces a zero $z_i$ with an exceptional divisor $E_i \cong \mathbb{CP}^1$:

- **Splitting:** A single zero resolves into multiple components $E_{i_1}, \ldots, E_{i_k}$. The vortex filament bifurcates and the mass decomposes as $\sum_j \lambda_j|\Phi_q(z_{i_j})|$, reproducing the [topological decomposition](#prop:topological-decomposition-mass).
- **Linking:** The intersection $E_i \cdot E_j \neq 0$ in homology if and only if the corresponding vortex filaments are Hopf-linked. The intersection pairing measures the strong-force binding energy generated by the mutual velocity induction between linked filaments.

The divisor structure of $\{\psi = 0\}$ — not the real density $|\psi|^2$ — correctly tracks vortex topology and particle content.
<!-- FILE_END: madelung-divisor-topology.md -->

<!-- FILE_START: hamilton-jacobi-phase.md -->
The [Madelung decomposition](#rem:madelung-fluid) $\psi = \sqrt{\rho}\exp(JS/\hbar_q)$ separates the Schrödinger equation into continuity (for $\rho$) and quantum Euler (for $v = \nabla_A S$) equations. The equation for the phase $S$ itself — the **quantum Hamilton--Jacobi equation** — forms the other face of the Madelung picture, linking the brane fluid directly to classical mechanics.

**The $q$-deformed Hamilton--Jacobi equation.**
Substituting $\psi$ into the [q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction) and isolating the real part yields

$$
  \partial_t S
  + 
  \frac{1}{2}\lVert\nabla_A S\rVert^2
  +  V
  +  Q_q
  =  0,
$$

where $V$ is the external potential (curvature of the $\mathrm{SU}(2)$ connection) and $Q_q = -(\hbar_q^2/2)\Delta_q\sqrt{\rho}/\sqrt{\rho}$ is the quantum pressure. This constitutes the Hamilton--Jacobi equation for a classical particle in the potential $V + Q_q$. The term $Q_q$ completely absorbs the quantum correction.

**Classical trajectories.**
The characteristics of the Hamilton--Jacobi equation define the classical trajectories

$$
  \dot{x} = \nabla_A S(x, t),
  \qquad
  \dot{p} = -\nabla_A(V + Q_q).
$$

These correspond precisely to the geodesics of the [acoustic metric](#rem:madelung-fluid) $g_{\mathrm{ac}}$ once $Q_q$ acts as an effective potential. The velocity field $v = \nabla_A S$ is therefore simultaneously:

1. the **fluid velocity** of the Madelung fluid,
2. the **momentum field** of the Hamilton--Jacobi flow,
3. the **tangent vector** to the acoustic geodesics.

This triple equivalence explains why [geodesic vortices](#rem:geodesic-vortices) — critical points of the $q$-energy functional — also trace classical particle trajectories.

**WKB hierarchy and the $q$-expansion.**
Expanding $S = S_0 + \hbar_qS_1 + \hbar_q^2S_2 + \cdots$ produces a functional hierarchy:

- **$O(1)$: Eikonal equation.** $\partial_t S_0 + \frac{1}{2}\lVert\nabla_A S_0\rVert^2 + V = 0$. This gives the classical Hamilton--Jacobi equation without quantum corrections. Its characteristics trace the classical geodesics of the [GR substrate geometry](#rem:gr-substrate-geometry).
- **$O(\hbar_q)$: Transport equation.** $\partial_t S_1 + \nabla_A S_0 \cdot \nabla_A S_1 = -\frac{1}{2}\Delta_q S_0$. This governs amplitude modulation along classical rays and originates the [algebraic filter](#rem:algebraic-filter): the $q$-Laplacian $\Delta_q$ selects which modes propagate.
- **$O(\hbar_q^2)$: Quantum pressure.** $S_2$ introduces the quantum pressure $Q_q$. Trajectories at this order deviate from classical geodesics and spiral into vortex filaments, marking the onset of fermionic behaviour.

**Caustics and vortex nucleation.**
The Hamilton--Jacobi solution $S$ naturally develops caustics — loci where $\nabla_A^2 S$ diverges and $\rho \to \infty$. In classical optics, these act as focal points; in the brane fluid, they act as **vortex nucleation sites**. At a caustic, the eikonal approximation fails and the full $q$-Schrödinger equation takes over. The resolution replaces the caustic with a vortex filament carrying quantised circulation $[j]_q[j+1]_q$, managing the transition from wave optics to particle physics.

**Connection to the discrete spectrum.**
The Hamilton--Jacobi phase $S$ is single-valued modulo $2\pi\hbar_q$. The phase winding around a vortex filament $\varrho$ accrues

$$
  \oint_\varrho \nabla_A S \cdot dl
  = 
  2\pi\hbar_qn,
  \qquad n \in \mathbb{Z},
$$

enforcing the Bohr--Sommerfeld quantisation condition. The $q$-deformation upgrades the integer $n$ to the spin label $j$ under $\mathrm{SU}_q(2)$ representation theory: permitted phase windings measure $2\pi\hbar_q[j]_q$ rather than $2\pi\hbar_qn$. This grounds the Hamilton--Jacobi picture in the [discrete vortex spectrum](#prop:discrete-vortex-spectrum) and formally seals the correspondence between wave mechanics, fluid dynamics, and knot particles.
<!-- FILE_END: hamilton-jacobi-phase.md -->

<!-- FILE_START: q-navier-stokes.md -->
The [quantum Euler equation](#rem:madelung-fluid) models inviscid flow in the brane fluid. To account for dissipation — the irreversible degradation of coherent vortex motion into thermal fluctuations — we introduce the **$q$-deformed Navier--Stokes equation**.

**Categorical formulation.**
Let $(\mathbf{C}, A, \tau)$ be a [QOU](#def:quantum-observable-universe) with [substrate parameter](#def:substrate-parameter) $q \in \mathrm{End}(\mathbf{1})$, where $q > 1$. Let $\Omega^k(A)$ be the [differential forms](#def:higher-forms) on the Frobenius--Hopf object $A$, governed by the [q-exterior derivative](#def:categorical-q-ext-deriv) $d_q \colon \Omega^k(A) \to \Omega^{k+1}(A)$ and its adjoint $\delta_q \colon \Omega^{k+1}(A) \to \Omega^k(A)$ under the [Frobenius pairing](#def:frobenius-pairing). The [$q$-Laplacian](#rem:q-laplacian-interpretation) operates as $\Delta_q = d_q\delta_q + \delta_q d_q$.

The **$q$-Navier--Stokes system** is the pair of morphisms in $\mathbf{C}$:

$$
  \partial_t v
  + \mu \circ (v \otimes \nabla_q v)
  = 
  -\rho^{-1}d_qp
  -  d_qQ_q
  +  \tfrac{1}{2}(1 - q^{-1})\Delta_qv
  +  \rho^{-1}\delta_q\boldsymbol{\sigma}_q,
$$

$$
  \partial_t\rho + \delta_q(\rho \cdot v) = 0,
$$

where:

- $v \in \Omega^1(A)$ is the velocity 1-form,
- $\rho \in A$ is the density (0-form),
- $p \in A$ is the pressure,
- $\nabla_q$ is the [q-connection](#def:categorical-q-connection),
- $\mu \colon A \otimes A \to A$ is the multiplication on $A$,
- $Q_q = -\tfrac{1}{2}(1-q^{-1})^2 \Delta_q(\rho^{1/2}) \cdot \rho^{-1/2} \in A$ represents the quantum pressure,
- $\boldsymbol{\sigma}_q = (1-q^{-1})\rho \bigl(d_q v + (d_q v)^\dagger - \tfrac{2}{3}(\delta_q v)\mathrm{id}_A\bigr) \in \Omega^2(A)$ supplies the viscous stress,
- and the dagger $(-)^\dagger$ signals the [Frobenius pairing](#def:frobenius-pairing).

The kinematic viscosity $\nu_q = \frac{1}{2}(1 - q^{-1}) = \hbar_q/2$ stems exclusively from the [substrate parameter](#def:substrate-parameter); it is an induced parameter, not an independent physical constant.

**Incompressibility.**
The constraint $\delta_q v = 0$ ($v \in \ker(\delta_q|_{\Omega^1})$) stands in for the classical $\nabla \cdot v = 0$. The [observability condition](#def:quantum-observable-universe) $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ prevents trivial gauge modes from fulfilling this constraint.

**Archimedean realisation.**
Following the [categorical--archimedean bridge](#prop:categorical-archimedean-bridge), the fibre functor $\tau$ maps the categorical system to coordinates on the [state bundle](#ex:c-quantum-observable-universe) $\mathcal{S}$:

$$
  \partial_t v + (v \cdot \nabla_A)v
  = 
  -\frac{1}{\rho}\nabla_A p
  -  \nabla_A Q_q
  +  \nu_q\Delta_q v
  +  \frac{1}{\rho}
  \nabla_A \cdot \boldsymbol{\sigma}_q,
$$

where $\nabla_A$ is the $\mathrm{SU}(2)$ covariant derivative, and the coordinates of the $q$-deformed viscous stress tensor are

$$
  (\boldsymbol{\sigma}_q)_{ij}
  = 
  \nu_q\rho
  \bigl(
    \nabla_{A,i}v_j + \nabla_{A,j}v_i
    - \tfrac{2}{3}(\nabla_A \cdot v)\delta_{ij}
  \bigr),
$$

joined by the continuity equation $\partial_t\rho + \nabla_A \cdot (\rho v) = 0$.
<!-- FILE_END: q-navier-stokes.md -->

<!-- FILE_START: q-ns-properties.md -->
**Properties.**

1. **Algebraic dissipation spectrum.** The term $\nu_q\Delta_q v$ damps mode $k$ at the rate $\nu_q[k]_q^2 / L_q^2$. The $q$-integers increase as $[k]_q \sim q^k / (q - q^{-1})$, causing high-wavenumber modes to undergo **exponential** rather than polynomial damping. This serves as a structural UV regularisation.
2. **Gauge-covariant diffusion.** The connection $A$ governs every derivative. Viscous diffusion thus transports colour charge alongside momentum: as a vortex filament decays, it radiates its $\mathrm{SU}_q(2)$ quantum numbers into nearby filaments via the connection.
3. **Quantum pressure as negative viscosity.** At short wavelengths, $Q_q$ acts as negative viscosity, **opposing** fluid compression below the length scale $\ell_q = (q-1)/q$. The equilibrium between dissipation ($\nu_q\Delta_q v$) and quantum repulsion ($\nabla_A Q_q$) sets the minimum vortex core radius.

**Energy dissipation rate.**
The global energy dissipation rate for the $q$-Navier--Stokes equation is

$$
  \varepsilon_q
  = 
  \nu_q \int_{\mathcal{S}}
  \rho\lVert\nabla_A v\rVert^2d\mu
  = 
  \nu_q \sum_{k=1}^{\infty}
  [k]_q^2|v_k|^2,
$$

where $v_k$ denotes the Fourier coefficients in the $q$-integer eigenbasis. For $q > 1$, the exponential damping guarantees the sum converges absolutely, circumventing the standard barriers to proving classical 3D energy estimates.

**Classical and quantum limits.**

| Limit | $\nu_q$ | $Q_q$ | Equation reduces to |
|---|---|---|---|
| $q \to 1$ | $0$ | $0$ | Euler equation (inviscid, zero quantum pressure) |
| $q \to 1^+$ (fixed $\hbar_q$) | $\hbar_q/2$ | $-\hbar^2\Delta\sqrt{\rho}/(2\sqrt{\rho})$ | Navier--Stokes + Bohm potential |
| $q \gg 1$ | $(1 - 1/q)/2$ | Dominant | Flow freezes to ground state due to extreme pressure |

**Well-posedness.**
The exponential decay of high-wavenumber modes globally bounds the 3D $q$-Navier--Stokes equation for any $q > 1$ ([thm:q-ns-wellposedness](#thm:q-ns-wellposedness)). The energy estimate $\frac{d}{dt}\lVert v\rVert^2 \leq -\nu_q[1]_q^2\lVert v\rVert^2$ yields exponential decay of the total kinetic energy, and the exponential $q$-growth halts the enstrophy blowup that sabotages classical proofs. The classical 3D Navier--Stokes regularity problem is strictly an artefact of the $q \to 1$ singularity.
<!-- FILE_END: q-ns-properties.md -->

<!-- FILE_START: q-metric-contact-deformation.md -->
The Cardona–Miranda–Peralta-Salas–Presas \cite{cardona2021} procedure bridges steady Euler flow and contact-Reeb flow through a **conformal change of metric**. Given a divergence-free, non-vanishing Euler field $X$ on $(M^3, g)$, rescaling $X \mapsto X / |X|_g^2$ and factoring the metric maps $X$ to the Reeb vector field of a contact form on $(M^3, \tilde g)$. The dynamical universality derives from the contact structure, not the initial metric.

The QOU executes exactly this operation via the substrate parameter $q$. The [$q$-Navier–Stokes equation](#def:q-navier-stokes) replaces the classical Riemannian inner product with the $q$-deformed Frobenius pairing ([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)). This constitutes a one-parameter family of metric adjustments, smoothly modulating between:

- the **full Levi-Civita connection** (the "Euler-side" geometry representing Riemannian fluid flow), and
- its **Reeb projection** along $\xi_q$ (the "contact-side" geometry isolating pure Reeb flow).

The parameter $q$ acts as the dial. Three regimes govern the behaviour:

| Parameter limit | Geometric picture | Dynamical content |
|---|---|---|
| $q \to 1^+$ | Full Riemannian metric; $\varTheta_q$ degenerates | Classical Navier–Stokes; Reeb projection vanishes |
| $q > 1$ generic | Strict contact metric on $\mathcal{S}$ | $q$-NS globally regular ([thm:q-ns-wellposedness](#thm:q-ns-wellposedness)); Reeb flow Turing-complete ([rem:reeb-contact-universal-computer](#rem:reeb-contact-universal-computer)) |
| $q \to \infty$ | Pure Reeb (horizontal components vanish) | Hamiltonian first-return; bare tape-reading dynamics |

**A geometric reading of the $q$-NS obstruction.**
The [NS obstruction class](#def:ns-obstruction) gauges how the classical $q = 1$ contact form collapses at a vortex-collision locus. Through Miranda's framework, increasing $q$ past $1$ rescales the Riemannian metric to buoy the contact form against degeneracy. The [Levi form condition number](#prop:core-levi-form) isolates this contact degeneracy; it is the exact metric property that the $q$-deformation corrects. The [quantum pressure](#rem:madelung-fluid) term acts as an isotropic buffer preventing the Levi eigenvalues from crossing zero.

**Location in the proof strategy.**
The [q-NS research programme](#rem:q-ns-research-programme) incorporates two implications:

1. Global well-posedness for $q > 1$ ([thm:q-ns-wellposedness](#thm:q-ns-wellposedness)) versus breakdown at $q = 1$ is a feature of the smooth-vs-degenerate contact dichotomy, not an independent quantum effect.
2. The [Levi degeneracy conjecture](#conj:levi-degeneracy) isolates whether a given vortex collision targets the metric-Riemannian (regular) limit, where the contact form dies and the flow flattens, or the contact (blowup) limit, where the metric isolates non-degenerate dynamics. The [Biot–Savart](#rem:townsend-biot-savart-strain) and [hyperbolic overlap](#rem:hyperbolic-overlap-saturation) remarks frame these regimes explicitly as ODEs.

In the Cardona–Miranda grammar: the parameter $q$ selects the contact metric, and that choice determines whether the Reeb dynamics persists or triggers a contact-degenerate singularity.
<!-- FILE_END: q-metric-contact-deformation.md -->

<!-- FILE_START: geodesic-vortices.md -->
Geodesics of the [acoustic metric](#rem:madelung-fluid) exactly map to the critical points of the $q$-deformed energy functional evaluated over closed curves in the [state bundle](#ex:c-quantum-observable-universe) $\mathcal{S}$.

**The $q$-energy functional.**
For $\varrho \colon S^1 \to \mathcal{S}$:

$$
  \mathcal{E}_q[\varrho]
  = 
  \oint_\varrho
  \bigl(
    \tfrac{1}{2}\lVert\dot\varrho^H\rVert^2
    + Q_q(\varrho)
    + \lVert F_A(\dot\varrho)\rVert^2
  \bigr)ds,
$$

where $\dot\varrho^H$ specifies the horizontal velocity, $Q_q$ the [quantum pressure](#rem:madelung-fluid), and $F_A(\dot\varrho)$ the filament curvature.

**Critical points are geodesics.**
Evaluating $\delta\mathcal{E}_q / \delta\varrho = 0$ produces

$$
  \nabla_{\dot\varrho}\dot\varrho
  = -\nabla^\perp Q_q - \iota_{\dot\varrho}{*F_A}.
$$

As $q \to 1$, $Q_q \to 0$ and the gauge term simplifies into Biot--Savart self-induction (the classical Hasimoto soliton).

**Stability.**
The second variation $\delta^2\mathcal{E}_q$ resolves via the [weight-space decomposition](#def:weight-decomposition):

- **Longitudinal** (Cartan): Stable, carrying eigenvalues $[k]_q^2 \hbar_q / L_q^2$ ([discrete spectrum](#prop:discrete-vortex-spectrum)).
- **Ladder** ($E_\pm$): Protected by an energetic barrier $\Delta E = \hbar_q([j\!+\!1]_q[j\!+\!2]_q - [j]_q[j\!+\!1]_q)/(2I_q) > 0$ strictly when $q > 1$.
- **Gauge**: Trivially zero (quotiented out by symmetry).

**Index theorem.**
The Morse index of the fundamental vortex ($j = 1/2$) evaluates to zero: no subordinate energy state exists. The lightest fermion acts as the absolute minimum of $\mathcal{E}_q$ within its topological class.

**Connection to mass.**
$\mathcal{E}_q[\gamma_0] = \oint_{\gamma_0} \lVert\nabla_A q\rVert \cdot \lVert L \wedge F^+\rVert \propto m$ explicitly generates the [mass identity](#def:mass-identity). The static limit of $\mathcal{E}_q$ functions as the [geometric drag](#rem:geometric-drag).
<!-- FILE_END: geodesic-vortices.md -->

<!-- FILE_START: two-vortex-channel-algebra.md -->
*Lean sibling: generic commutative ring, no archimedean input (AGENTS.md §7c); library module `QOU.FluidDynamics.TwoVortexChannelAlgebra`.*

**Proposition (channel algebra of the two-vortex interaction).** *Let $R$ be a commutative ring carrying elements $e_+, e_-, \sigma, q, u$ satisfying:*

1. *(partition of unity)* $e_+ + e_- = 1$;
2. *(orthogonality)* $e_+ e_- = 0$;
3. *(inverse witness)* $q\,u = 1$;
4. *(spectral form)* $\sigma = q\,e_+ - u\,e_-$.

*These axioms imply:*

- *(derived idempotency)* $e_+^2 = e_+$ and $e_-^2 = e_-$;
- *(spectral square)* $\sigma^2 = q^2\,e_+ + u^2\,e_-$, derived strictly from (1)–(2);
- *(Hecke relation)* $\sigma^2 = (q - u)\,\sigma + 1$.

The theorem `channel_algebra` unites these derivations. The parallel identity $(-q^{-1})/q = -(q^2)^{-1}$ — defining the per-crossing eigenvalue ratio over any field without channel data — resides in the standalone lemma `eigenvalue_ratio`.

The primary model assigns these elements to the commutant of $\sigma_1$ in the two-strand Hecke algebra $H_2(q)$. Here $e_\pm$ represents the Wedderburn pair of the [Hopf channel](#def:van-der-waals-hopf-channel) and $\sigma$ represents the braid operator of the [$R$-matrix braiding](#prop:r-matrix-braiding-structure). Setting $u = q^{-1}$ casts the spectral form as the eigenvalue decomposition of $\sigma_1$ supporting eigenvalues $q$ and $-q^{-1}$. The resulting Hecke relation proves that the abstract channel data logically forces the Skein relation without external topological presentation.
<!-- FILE_END: two-vortex-channel-algebra.md -->

<!-- FILE_START: two-vortex-scattering-channels.md -->
The channel algebra developed in [the two-vortex proposition](#prop:two-vortex-channel-algebra) governs the scattering theory of interacting vortex loops.

**The $R$-matrix as the two-vortex $S$-matrix.**
Two [geodesic vortices](#rem:geodesic-vortices) — soliton critical points of $\mathcal{E}_q$ that devolve to Hasimoto solitons at $q \to 1$ — interact exclusively via the braid operator of the [$R$-matrix braiding](#prop:r-matrix-braiding-structure). The Yang--Baxter equation codifies the complete factorization of the multi-vortex scattering event. A three-loop interaction remains strictly independent of the internal ordering of pairwise exchanges. The loops transit each other acquiring only channel phase shifts, never generating internal-state debris. This factorization mathematically guarantees that the weak scattering event cannot shred the internal dynamics of an individual loop.

**The Hopf link as the minimal scattering event.**
Two loops bearing linking number one complete the braid $\sigma_1^2$. Per the spectral square proposition, the interaction decomposes over the [Hopf channel](#def:van-der-waals-hopf-channel) pair into $\sigma_1^2 = q^2 e_+ + q^{-2} e_-$. The Hopf link demands zero hyperbolic volume, perfectly mirroring the soliton constraint: the two loops perturb each other's trajectories while avoiding strictly bonded volume.

**Channel decay equals the eigenvalue ratio.**
At each crossing, the antisymmetric channel carries weight $-q^{-1}$ against the symmetric channel's weight $q$. This extracts a relative ratio of $-q^{-2}$ ([eigenvalue-ratio identity](#prop:two-vortex-channel-algebra)). At the physical substrate anchor $q_0 > 1$, this ratio represents a strict contraction, $q_0^{-2} \approx 0.81$. Every crossing diminishes the antisymmetric perturbation by nearly twenty percent. Bound alongside the gapped second variation of $\mathcal{E}_q$ ([geodesic vortices](#rem:geodesic-vortices)), this defines the dual mechanism guaranteeing soliton stability: the substrate exponentially dampens inter-loop disturbances at every crossing, while the spectral gap isolates disturbances within the loops themselves.
<!-- FILE_END: two-vortex-scattering-channels.md -->

<!-- FILE_START: braid-fluid.md -->
The categorical [braid-group action](#prop:braid-action-tensor) possesses a direct hydrodynamic interpretation on the brane fluid.

**Arnold's geodesic framework.**
Arnold demonstrated that the Euler equation on $(M, g)$ behaves exactly as the geodesic equation over $\mathrm{SDiff}(M)$ acting under the $L^2$ metric: $\nabla_{\dot\phi}\dot\phi = 0$. The velocity vector $v = \dot\phi \circ \phi^{-1}$ reliably solves $\partial_t v + \nabla_v v = -\nabla p$.

**$q$-deformed diffeomorphisms.**
The [state bundle](#ex:c-quantum-observable-universe) promotes the classical $\mathrm{SDiff}(M)$ group to $\mathrm{SDiff}_q(\mathcal{S})$. This imposes two structural shifts:

1. The $L^2$ metric upgrades to the [Webster inner product](#sec:webster-inner-product). The resulting geodesics solve the [quantum Euler equation](#rem:madelung-fluid) subject to pressure $Q_q$.
2. Confining the state space to flows exhibiting concentrated vorticity across $n$ filaments forces a strict topological quotient onto $B_n$. The fundamental group of the configuration space $\mathrm{Conf}_n(M)/S_n$ resolves uniquely to $B_n$.

**Braid generators as vortex exchanges.**
The Artin generator $\sigma_i$ dictates the half-twist spatial exchange of filaments $i$ and $i+1$. The representation $\rho_n(\sigma_i) = \mathrm{id}^{\otimes(i-1)} \otimes c_{V,V} \otimes \mathrm{id}^{\otimes(n-i-1)}$ ([prop:braid-action-tensor](#prop:braid-action-tensor)) manifests physically as the $\mathrm{SU}(2)$ holonomy traversing the exchange path. The [Yang--Baxter equation](#prop:r-matrix-braiding-structure) enforces Reidemeister III, ensuring three-vortex braiding stays rigorously path-independent.

**The dictionary.**

See [Table](#tbl:braid-fluid-table-data).

**Hecke relation as scattering.**
The quadratic rule $(T - q)(T + q^{-1}) = 0$ restricts two-vortex interactions to exactly two terminal eigenvalues: $q$ (symmetric unperturbed pass-through) and $-q^{-1}$ (antisymmetric core reconnection). The universal intensity ratio

$$
  \frac{\text{reconnection}}{\text{pass-through}}
  = q^{-2}
$$

relies entirely on the substrate parameter. This ratio establishes the fluid-dynamical source mechanism for the [skein crossing asymmetry](#rem:skein-crossing-asymmetry).

**Helicity as Markov trace.**
The [Jones polynomial](#thm:jones-markov-trace) $J_L(q)$ operates as the **topological helicity** governing the vortex tangle. This categorical metric comprehensively refines classical helicity $H = \int v \cdot \omega \, dV$, successfully distinguishing topological states utterly invisible to $H$ (separating the trefoil from the unknot).
<!-- FILE_END: braid-fluid.md -->

<!-- FILE_START: planck-reynolds.md -->
The [substrate parameter](#def:substrate-parameter) $q$ strictly specifies the three Reynolds-number variables in the brane fluid: characteristic velocity $c_q = 1/(q-1)$, characteristic length $\ell_q = (q-1)/q$, and dynamic viscosity $\nu_q = \hbar_q/2 = (q-1)/(2q)$. The corresponding **Planck--Reynolds number** is:

$$
  \mathrm{Re}_q
  = \frac{c_q \cdot \ell_q}{\nu_q}
  = \frac{2}{q-1}.
$$

| Regime | $q$ | $\mathrm{Re}_q$ | Character |
|---|---|---|---|
| Classical | $\to 1^+$ | $\to \infty$ | Fully turbulent |
| Physical | $\approx 1.110$ | $\approx 18.2$ | Transitional |
| Deep quantum | $\gg 1$ | $\to 0$ | Laminar |

The substrate parameter functions as an inverse turbulence dial. At $q = 1$, the Reynolds number diverges and unleashes the full Kolmogorov cascade, but the contact structure collapses and particle states vanish. At the physical anchor $q \approx 1.110$, the fluid operates in the transitional zone: turbulence supports the structured [discrete vortex spectrum](#prop:discrete-vortex-spectrum) without obliterating it into a continuum.

The laminar--turbulent boundary emerges at $\mathrm{Re}_q \sim 1$, corresponding to $q \sim 3$. Active Kelvin modes require $[k]_q \leq \mathrm{Re}_q^{1/2}$. At the physical anchor $q \approx 1.110$, this constraint dictates a cutoff $k_{\max} \approx 4$, matching exactly the four observed [intensity levels](#rem:vortex-intensity-modes) ($j = \frac{1}{2}, 1, \frac{3}{2}, 2$).
<!-- FILE_END: planck-reynolds.md -->

