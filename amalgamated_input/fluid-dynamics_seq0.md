<!-- FILE_START: fluid-dynamics-intro.md -->
The brane of a quantum observable universe carries a natural fluid
dynamics whose viscosity, vortex spectrum, and turbulence structure
are determined by the substrate parameter $q$.  This chapter develops
the $q$-deformed Navier--Stokes system on the brane and extracts two
principal consequences: global regularity of the $q$-deformed equation
for $q > 1$, and a categorical obstruction that controls whether the
classical Navier--Stokes equation ($q = 1$) admits finite-time blowup.

The first three sections establish the hydrodynamic framework.  We
derive the $q$-Navier--Stokes equation from the Reeb derivation on
the Frobenius--Hopf algebra, characterise the discrete vortex spectrum
and helicity conservation forced by the braided monoidal structure,
and develop the turbulence theory including $q$-deformed Kolmogorov
scaling and acoustic horizons.

The final two sections contain the chapter's main results.  We prove
global well-posedness of the $q$-NS system for $q > 1$ via spectral
Sobolev estimates on the quantum Peter--Weyl decomposition, and we
identify the NS obstruction --- a categorical invariant that measures
the failure of regularity at $q = 1$.  The obstruction is computable
from the Hecke algebra and provides a new criterion for the classical
Navier--Stokes regularity problem.
<!-- FILE_END: fluid-dynamics-intro.md -->

<!-- FILE_START: brane-fluid.md -->
The brane of a [quantum observable universe](#def:quantum-observable-universe)
carries a natural fluid dynamics.  The [substrate parameter](#def:substrate-parameter)
$q$ sets the effective brane thickness: at $q = 1$ the brane is
infinitely thin (classical vacuum); at $q > 1$ it acquires a finite
transverse extent controlled by the $q$-deformed contact geometry.
The resulting dynamics inherits three features absent from ordinary
Navier--Stokes theory:

1. **Algebraic viscosity.**  The $q$-Laplacian $\Delta_q$
   ([q-Laplacian interpretation](#rem:q-laplacian-interpretation))
   replaces the classical Laplacian, and its eigenvalues are
   $q$-integers $[k]_q$.  The viscous dissipation rate is therefore
   algebraically quantised rather than continuously variable.

2. **Gauge-covariant advection.**  The velocity field
   $v = \nabla_A S$ is defined via the $\mathrm{SU}(2)$ connection
   $A$ rather than a flat gradient.  Advection along $v$ preserves
   the horizontal self-duality $F_A|_H = {*_H}F_A|_H$, coupling
   the fluid motion to the gauge structure.

3. **Topological vortex quantisation.**  The circulation around any
   closed vortex filament $\varrho$ is constrained by the
   $\mathrm{SU}_q(2)$ holonomy to discrete values
   $[j]_q[j+1]_q$, producing the
   [discrete vortex spectrum](#prop:discrete-vortex-spectrum).

<!-- FILE_END: brane-fluid.md -->

<!-- FILE_START: madelung-fluid.md -->
**The Madelung split.**
Write $\psi = \sqrt{\rho}\exp(JS/\hbar_q)$ to decompose the
[q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction) into two
real equations.  Setting $v = \nabla_A S$ and fluid density
$\rho = |\psi|^2$:

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
The [substrate parameter](#def:substrate-parameter) $q$ modulates the
effective thickness of the quantum fluid: near $q \approx 1$ one recovers
ordinary inviscid flow (quantum pressure $Q_q \approx 0$); at $q \gg 1$,
$Q_q$ dominates and the fluid strongly resists compression — this
resistance is the inertial mass of the brane.

**Zero-information state $|\psi|^2 = 0$.**
The vacuum $\psi = 0$ carries no medium, no vortex, and no fermion.  It
lies outside the support of all harmonic modes filtered by the
[algebraic filter](#rem:algebraic-filter).  As $q \to 1$, $\hbar_q \to 0$:
the vacuum is the state of maximal classical certainty.

**Geodesics as stable vortex filaments.**
Bosonic modes follow straight null geodesics of the acoustic metric
$g_{\mathrm{ac}}$.
Fermionic modes spiral around the zeros of $\psi$, forming stable vortex
filaments $\varrho$ whose mass is controlled by

$$
  m  \propto  \oint_\varrho \|\nabla_A q\|\cdot\|L \wedge F^+\|,
$$

reproducing the [mass identity](#def:mass-identity) as a line integral of
the substrate curvature around the vortex core.
<!-- FILE_END: madelung-fluid.md -->

<!-- FILE_START: madelung-acoustic-metric.md -->
**Acoustic metric and analogue gravity.**
Perturbations $\delta\psi$ around a background flow satisfy
$\Box_{g_{\mathrm{ac}}}\delta\psi = 0$ with the acoustic metric

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

An acoustic horizon forms wherever $|v| = c_s$, coinciding with a
gravitational horizon in the substrate geometry.  General relativity
emerges as the geometry of non-uniform brane flow: the
[GR substrate geometry](#rem:gr-substrate-geometry) is the acoustic
manifold.  Bosonic modes (with $[F_A, \alpha] = 0$) travel on null
acoustic geodesics; fermionic modes (with $[F_A, \alpha] \neq 0$)
spiral into vortex filaments of $\psi$.
<!-- FILE_END: madelung-acoustic-metric.md -->

<!-- FILE_START: madelung-divisor-topology.md -->
**Linking and splitting in the divisor.**
The zero-locus $\{\psi = 0\}$ is a Weil divisor.  Each blowup at a
ramification point replaces a zero $z_i$ with an exceptional divisor
$E_i \cong \mathbb{CP}^1$:

- **Splitting:** a single zero resolves into multiple components
  $E_{i_1}, \ldots, E_{i_k}$; the vortex filament bifurcates and
  the mass decomposes as
  $\sum_j \lambda_j|\Phi_q(z_{i_j})|$,
  recovering the [topological decomposition](#prop:topological-decomposition-mass).

- **Linking:** $E_i \cdot E_j \neq 0$ in homology if and only if the
  corresponding vortex filaments are Hopf-linked; the intersection
  pairing measures the strong-force binding energy from mutual velocity
  induction between the linked filaments.

The divisor structure of $\{\psi = 0\}$ — not $|\psi|^2$ itself — is
therefore the correct object for tracking vortex topology and the
associated particle content.
<!-- FILE_END: madelung-divisor-topology.md -->

<!-- FILE_START: hamilton-jacobi-phase.md -->
The [Madelung decomposition](#rem:madelung-fluid)
$\psi = \sqrt{\rho}\exp(JS/\hbar_q)$ yields two real equations:
one for $\rho$ (continuity) and one for $v = \nabla_A S$ (quantum
Euler).  The equation for the phase $S$ itself — the **quantum
Hamilton--Jacobi equation** — is the other face of the Madelung
picture and connects the brane fluid directly to classical
mechanics.

**The $q$-deformed Hamilton--Jacobi equation.**
Substituting $\psi = \sqrt{\rho}\exp(JS/\hbar_q)$ into the
[q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction) and
separating real parts gives

$$
  \partial_t S
  + 
  \frac{1}{2}\lVert\nabla_A S\rVert^2
  +  V
  +  Q_q
  =  0,
$$

where $V$ is the external potential (curvature of the
$\mathrm{SU}(2)$ connection) and $Q_q = -(\hbar_q^2/2)
\Delta_q\sqrt{\rho}/\sqrt{\rho}$ is the quantum pressure.  This
is the Hamilton--Jacobi equation for a classical particle in the
potential $V + Q_q$: the quantum correction is entirely captured
by the additional potential $Q_q$.

**Classical trajectories.**
The characteristics of the Hamilton--Jacobi equation are the
classical trajectories

$$
  \dot{x} = \nabla_A S(x, t),
  \qquad
  \dot{p} = -\nabla_A(V + Q_q),
$$

which are precisely the geodesics of the
[acoustic metric](#rem:madelung-fluid) $g_{\mathrm{ac}}$ when
$Q_q$ is included in the effective potential.  The velocity field
$v = \nabla_A S$ is therefore simultaneously:

- the **fluid velocity** of the Madelung fluid,
- the **momentum field** of the Hamilton--Jacobi flow,
- the **tangent vector** to the acoustic geodesics.

This triple identification is the reason that
[geodesic vortices](#rem:geodesic-vortices) — critical points of the
$q$-energy functional — are also classical particle trajectories.

**WKB hierarchy and the $q$-expansion.**
Expanding $S = S_0 + \hbar_qS_1 + \hbar_q^2S_2 + \cdots$
produces a hierarchy:

- **$O(1)$: Eikonal equation.**
  $\partial_t S_0 + \frac{1}{2}\lVert\nabla_A S_0\rVert^2 + V = 0$.
  This is the classical Hamilton--Jacobi equation without quantum
  corrections.  Its characteristics are the classical geodesics of
  the [GR substrate geometry](#rem:gr-substrate-geometry).

- **$O(\hbar_q)$: Transport equation.**
  $\partial_t S_1 + \nabla_A S_0 \cdot \nabla_A S_1 =
  -\frac{1}{2}\Delta_q S_0$.
  This governs the amplitude modulation along classical rays and
  is the origin of the [algebraic filter](#rem:algebraic-filter):
  the $q$-Laplacian $\Delta_q$ selects which modes propagate.

- **$O(\hbar_q^2)$: Quantum pressure.**
  $S_2$ encodes the quantum pressure $Q_q$.  At this order the
  trajectories deviate from classical geodesics and spiral into
  vortex filaments — the onset of fermionic behaviour.

**Caustics and vortex nucleation.**
The Hamilton--Jacobi solution $S$ develops caustics — loci where
$\nabla_A^2 S$ diverges and $\rho \to \infty$.  In classical
optics these are focal points; in the brane fluid they are
**vortex nucleation sites**.  At a caustic, the eikonal
approximation breaks down and the full $q$-Schrödinger equation
must be used.  The resolution replaces the caustic with a vortex
filament carrying quantised circulation $[j]_q[j+1]_q$ — the
transition from wave optics to particle physics.

**Connection to the discrete spectrum.**
The Hamilton--Jacobi phase $S$ is single-valued only modulo
$2\pi\hbar_q$.  Around a vortex filament $\varrho$, the phase
accumulates

$$
  \oint_\varrho \nabla_A S \cdot dl
  = 
  2\pi\hbar_qn,
  \qquad n \in \mathbb{Z},
$$

which is the Bohr--Sommerfeld quantisation condition.  In the
$q$-deformed setting, the integer $n$ is promoted to the spin
label $j$ via the $\mathrm{SU}_q(2)$ representation theory:
the allowed phase windings are $2\pi\hbar_q[j]_q$ rather than
$2\pi\hbar_qn$.  This connects the Hamilton--Jacobi picture
to the [discrete vortex spectrum](#prop:discrete-vortex-spectrum)
and completes the circle between wave mechanics, fluid dynamics,
and the particle picture.
<!-- FILE_END: hamilton-jacobi-phase.md -->

<!-- FILE_START: q-navier-stokes.md -->
The [quantum Euler equation](#rem:madelung-fluid) describes
inviscid flow in the brane fluid. To account for dissipation —
the irreversible transfer of kinetic energy from coherent vortex
motion to incoherent thermal fluctuations — we introduce the
**$q$-deformed Navier--Stokes equation**, first in categorical
language and then in coordinates.

**Categorical formulation.**
Let $(\mathbf{C}, A, \tau)$ be a
[QOU](#def:quantum-observable-universe) with
[substrate parameter](#def:substrate-parameter)
$q \in \mathrm{End}(\mathbf{1})$, $q > 1$. Let
$\Omega^k(A)$ denote the [differential forms](#def:higher-forms)
on the Frobenius--Hopf object $A$, with
[q-exterior derivative](#def:categorical-q-ext-deriv)
$d_q \colon \Omega^k(A) \to \Omega^{k+1}(A)$ and its adjoint
$\delta_q \colon \Omega^{k+1}(A) \to \Omega^k(A)$ with respect to
the [Frobenius pairing](#def:frobenius-pairing). The
[$q$-Laplacian](#rem:q-laplacian-interpretation) is
$\Delta_q = d_q\delta_q + \delta_q d_q$.

The **$q$-Navier--Stokes system** is the pair of morphisms in
$\mathbf{C}$:

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
- $\rho \in A$ is the density (a 0-form),
- $p \in A$ is the pressure,
- $\nabla_q$ is the [q-connection](#def:categorical-q-connection),
- $\mu \colon A \otimes A \to A$ is the multiplication on $A$,
- $Q_q = -\tfrac{1}{2}(1-q^{-1})^2
  \Delta_q(\rho^{1/2}) \cdot \rho^{-1/2} \in A$
 is the quantum pressure,
- $\boldsymbol{\sigma}_q = (1-q^{-1})\rho
  \bigl(d_q v + (d_q v)^\dagger
  - \tfrac{2}{3}(\delta_q v)\mathrm{id}_A\bigr)
  \in \Omega^2(A)$
 is the viscous stress,
- and the dagger $(-)^\dagger$ uses the
 [Frobenius pairing](#def:frobenius-pairing).

The kinematic viscosity $\nu_q = \frac{1}{2}(1 - q^{-1})
= \hbar_q/2$ arises from the
[substrate parameter](#def:substrate-parameter) alone — it is not
an independent physical constant.

**Incompressibility.**
The constraint $\delta_q v = 0$ (divergence-free, i.e.
$v \in \ker(\delta_q|_{\Omega^1})$) replaces the classical
$\nabla \cdot v = 0$. The [observability
condition](#def:quantum-observable-universe)
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
ensures this constraint is non-degenerate: there are no gauge
modes that could by definition satisfy it.

**Archimedean realisation.**
Under the [categorical--archimedean
bridge](#prop:categorical-archimedean-bridge), the fibre functor
$\tau$ sends the categorical system to coordinates on the
[state bundle](#ex:c-quantum-observable-universe) $\mathcal{S}$:

$$
  \partial_t v + (v \cdot \nabla_A)v
  = 
  -\frac{1}{\rho}\nabla_A p
  -  \nabla_A Q_q
  +  \nu_q\Delta_q v
  +  \frac{1}{\rho}
  \nabla_A \cdot \boldsymbol{\sigma}_q,
$$

where $\nabla_A$ is the $\mathrm{SU}(2)$ covariant derivative
(the geometric image of $\nabla_q$ under $\tau$), and the
$q$-deformed viscous stress tensor in coordinates is

$$
  (\boldsymbol{\sigma}_q)_{ij}
  = 
  \nu_q\rho
  \bigl(
    \nabla_{A,i}v_j + \nabla_{A,j}v_i
    - \tfrac{2}{3}(\nabla_A \cdot v)\delta_{ij}
  \bigr),
$$

with the continuity equation
$\partial_t\rho + \nabla_A \cdot (\rho v) = 0$.
<!-- FILE_END: q-navier-stokes.md -->

<!-- FILE_START: q-ns-properties.md -->
**Properties.**

1. **Algebraic dissipation spectrum.** The viscous term
 $\nu_q\Delta_q v$ damps mode $k$ at rate
 $\nu_q[k]_q^2 / L_q^2$. Because the $q$-integers
 grow as $[k]_q \sim q^k / (q - q^{-1})$ for large $k$,
 high-wavenumber modes are damped **exponentially** rather than
 polynomially, providing a natural UV regularisation absent from
 classical Navier--Stokes.

2. **Gauge-covariant diffusion.** The connection $A$ appears in
 every derivative. Viscous diffusion transports not only momentum
 but also colour charge: a vortex filament that decays by viscous
 damping radiates its $\mathrm{SU}_q(2)$ quantum numbers into
 neighbouring filaments via the connection.

3. **Quantum pressure as negative viscosity.** The $Q_q$ term
 acts as a negative viscosity at short wavelengths: it
 **opposes** compression of the fluid below the scale
 $\ell_q = (q-1)/q$. The balance between $\nu_q\Delta_q v$
 (dissipation) and $\nabla_A Q_q$ (quantum repulsion) determines
 the minimum vortex core radius.

**Energy dissipation rate.**
The global energy dissipation rate of the $q$-Navier--Stokes
equation is

$$
  \varepsilon_q
  = 
  \nu_q \int_{\mathcal{S}}
  \rho\lVert\nabla_A v\rVert^2d\mu
  = 
  \nu_q \sum_{k=1}^{\infty}
  [k]_q^2|v_k|^2,
$$

where $v_k$ are the Fourier coefficients in the $q$-integer
eigenbasis. For $q > 1$, the sum converges absolutely
(exponential damping of high modes), resolving the classical
difficulty of proving energy estimates for 3d Navier--Stokes.

**Classical and quantum limits.**

| Limit | $\nu_q$ | $Q_q$ | Equation reduces to |
|---|---|---|---|
| $q \to 1$ | $0$ | $0$ | Euler equation (inviscid, no quantum pressure) |
| $q \to 1^+$ with $\hbar_q$ held | $\hbar_q/2$ | $-\hbar^2\Delta\sqrt{\rho}/(2\sqrt{\rho})$ | Ordinary Navier--Stokes + Bohm potential |
| $q \gg 1$ | $(1 - 1/q)/2$ | Dominant | Quantum pressure dominates; flow frozen to ground state |

**Well-posedness.**
The exponential damping of high-wavenumber modes by the
$q$-Laplacian ensures that the $q$-Navier--Stokes equation is
globally well-posed in 3d for any $q > 1$ (see
[the well-posedness theorem](#thm:q-ns-wellposedness)): the energy estimate
$\frac{d}{dt}\lVert v\rVert^2 \leq -\nu_q[1]_q^2\lVert v\rVert^2$
gives exponential decay of the total kinetic energy, and the
$q$-integer growth prevents the enstrophy blowup that obstructs
classical regularity proofs. The classical 3d Navier--Stokes
regularity problem is thus an artefact of the $q \to 1$
degeneration.
<!-- FILE_END: q-ns-properties.md -->

<!-- FILE_START: q-metric-contact-deformation.md -->
The Cardona–Miranda–Peralta-Salas–Presas
\cite{cardona2021} route from steady
Euler flow to contact-Reeb flow proceeds by a **conformal change
of metric**: a divergence-free, non-vanishing Euler field $X$ on
$(M^3, g)$ becomes, after rescaling $X \mapsto X / |X|_g^2$ and
applying a conformal factor, the Reeb vector field of a contact
form on $(M^3, \tilde g)$. Universality of the dynamics is a
property of the contact structure, not of the original metric.

This is the *exact* operation the QOU performs through its
substrate parameter $q$. The
[$q$-Navier–Stokes equation](#def:q-navier-stokes) replaces the
classical Riemannian inner product on the brane with the
$q$-deformed Frobenius pairing
([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate));
this is a one-parameter family of metric changes, smoothly
interpolating between
- the **full Levi-Civita connection** (the "Euler-side" geometry
  in which the substrate looks like a Riemannian fluid), and
- its **Reeb projection** along $\xi_q$ (the "contact-side"
  geometry in which the flow is purely along the Reeb field of
  $\varTheta_q$).

The interpolation parameter is $q$ itself. Two regimes are
useful to keep in mind.

| Parameter limit | Geometric picture | Dynamical content |
|---|---|---|
| $q \to 1^+$ | Full Riemannian metric; contact form $\varTheta_q$ becomes degenerate | Classical Navier–Stokes; Reeb projection collapses |
| $q > 1$ generic | Genuine contact metric on $\mathcal{S}$ | $q$-NS regular ([thm:q-ns-wellposedness](#thm:q-ns-wellposedness)); Reeb flow Turing-complete ([rem:reeb-contact-universal-computer](#rem:reeb-contact-universal-computer)) |
| $q \to \infty$ | Pure Reeb (horizontal vanishes) | Hamiltonian first-return on Poincaré section; tape-only dynamics |

**A geometric reading of the $q$-NS obstruction.**
The
[NS obstruction class](#def:ns-obstruction) measures the failure
of the classical $q = 1$ contact form to remain non-degenerate at
a vortex-collision locus. Miranda's metric-change argument
provides the geometric content: increasing $q$ above $1$ rescales
the Riemannian metric so as to push the contact form away from
degeneracy. The
[Levi form condition number](#prop:core-levi-form), which
diagnoses contact degeneracy, is precisely the metric invariant
that the $q$-deformation flattens. Concretely, the
[quantum pressure](#rem:madelung-fluid) term in $q$-NS is the
isotropic "padding" that prevents the Levi eigenvalues from
crossing zero — which is the metric-change face of the
deformation.

**Location in the proof strategy.**
Two consequences for the
[q-NS research programme](#rem:q-ns-research-programme):

1. The well-posedness of $q$-NS for $q > 1$
   ([thm:q-ns-wellposedness](#thm:q-ns-wellposedness)) and the
   classical breakdown at $q = 1$ are *not* a quantum
   phenomenon; they are the smooth-vs-degenerate dichotomy in
   contact geometry, viewed through Miranda's lens.

2. The
   [Levi degeneracy conjecture](#conj:levi-degeneracy) becomes
   a question about which limit a particular vortex collision
   takes — the metric-Riemannian (NS regular) limit, in which
   the contact form genuinely degenerates and the flow flattens,
   or the contact (NS blowup) limit, in which the metric change
   leaves the contact structure non-degenerate. The two
   subsequent remarks
   ([Biot–Savart](#rem:townsend-biot-savart-strain) and
   [hyperbolic overlap](#rem:hyperbolic-overlap-saturation))
   examine the two regimes in explicit ODE form.

In the Cardona–Miranda language: the $q$-deformation chooses
*which contact metric* the substrate carries, and the choice
controls whether the Reeb dynamics is regular or runs into a
contact-degenerate singularity.
<!-- FILE_END: q-metric-contact-deformation.md -->

<!-- FILE_START: geodesic-vortices.md -->
Geodesics of the [acoustic metric](#rem:madelung-fluid) coincide
with critical points of a $q$-deformed energy functional on closed
curves in the [state bundle](#ex:c-quantum-observable-universe) $\mathcal{S}$.

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

where $\dot\varrho^H$ is the horizontal velocity, $Q_q$ the
[quantum pressure](#rem:madelung-fluid), and $F_A(\dot\varrho)$
the curvature along the filament.

**Critical points are geodesics.**
$\delta\mathcal{E}_q / \delta\varrho = 0$ gives

$$
  \nabla_{\dot\varrho}\dot\varrho
  = -\nabla^\perp Q_q - \iota_{\dot\varrho}{*F_A}.
$$

At $q \to 1$: $Q_q \to 0$, the gauge term reduces to Biot--Savart
self-induction (Hasimoto soliton).

**Stability.**
The second variation $\delta^2\mathcal{E}_q$ decomposes via the
[weight-space decomposition](#def:weight-decomposition):

- **Longitudinal** (Cartan): stable, eigenvalues
  $[k]_q^2 \hbar_q / L_q^2$ ([discrete
  spectrum](#prop:discrete-vortex-spectrum)).
- **Ladder** ($E_\pm$): barrier
  $\Delta E = \hbar_q([j\!+\!1]_q[j\!+\!2]_q - [j]_q[j\!+\!1]_q)/(2I_q)
  > 0$ for $q > 1$.
- **Gauge**: quotiented out by symmetry.

**Index theorem.**
The Morse index of the fundamental vortex ($j = 1/2$) is zero:
no lower state exists.  The lightest fermion is an absolute
minimum of $\mathcal{E}_q$ in its topological class.

**Connection to mass.**
$\mathcal{E}_q[\gamma_0] = \oint_{\gamma_0}
\lVert\nabla_A q\rVert \cdot \lVert L \wedge F^+\rVert
\propto m$, reproducing the [mass identity](#def:mass-identity).
The [geometric drag](#rem:geometric-drag) is the static limit
of $\mathcal{E}_q$.
<!-- FILE_END: geodesic-vortices.md -->

<!-- FILE_START: two-vortex-channel-algebra.md -->
*Lean sibling: generic commutative ring, no archimedean input (AGENTS.md §7c);
library module `QOU.FluidDynamics.TwoVortexChannelAlgebra`.*

**Proposition (channel algebra of the two-vortex interaction).** *Let $R$ be a
commutative ring carrying elements $e_+, e_-, \sigma, q, u$ satisfying*

1. *(partition of unity)* $e_+ + e_- = 1$;
2. *(orthogonality)* $e_+ e_- = 0$;
3. *(inverse witness)* $q\,u = 1$;
4. *(spectral form)* $\sigma = q\,e_+ - u\,e_-$.

*Then:*

- *(derived idempotency)* $e_+^2 = e_+$ *and* $e_-^2 = e_-$;
- *(spectral square)* $\sigma^2 = q^2\,e_+ + u^2\,e_-$, *using only (1)–(2)*;
- *(Hecke relation)* $\sigma^2 = (q - u)\,\sigma + 1$.

The three conclusions are bundled as the single Lean theorem
`channel_algebra` (the `lean` reference of this block). The companion
identity $(-q^{-1})/q = -(q^2)^{-1}$ — the per-crossing eigenvalue ratio,
over any field, needing no channel data — is the separate lemma
`eigenvalue_ratio` in the same module.

The intended model is the commutant of $\sigma_1$ in the two-strand Hecke
algebra $H_2(q)$, with $e_\pm$ the Wedderburn pair of the
[Hopf channel](#def:van-der-waals-hopf-channel) and $\sigma$ the braid
operator of the [$R$-matrix braiding](#prop:r-matrix-braiding-structure);
there $u = q^{-1}$ and the spectral form is the eigenvalue decomposition of
$\sigma_1$ with channel eigenvalues $q$ and $-q^{-1}$. The Hecke relation
shows the abstract channel data (1)–(4) already forces the skein relation:
no further presentation input is required.
<!-- FILE_END: two-vortex-channel-algebra.md -->

<!-- FILE_START: two-vortex-scattering-channels.md -->
The channel algebra of
[the two-vortex proposition](#prop:two-vortex-channel-algebra) is the
scattering theory of interacting vortex loops, read physically.

**The $R$-matrix is the two-vortex $S$-matrix.** Two
[geodesic vortices](#rem:geodesic-vortices) — soliton-like critical points of
$\mathcal{E}_q$, reducing to Hasimoto solitons at $q \to 1$ — interact
through the braid operator of the
[$R$-matrix braiding](#prop:r-matrix-braiding-structure). The Yang--Baxter
equation is precisely the factorization of the multi-vortex scattering: the
outcome of a three-loop interaction is independent of the order of pairwise
exchanges, so the loops pass through one another with only a phase
reassignment in each channel and no internal-state production. This is the
algebraic form of the observation that the interaction is weak enough not to
disrupt each loop's internal dynamics: a factorized $S$-matrix has no
mechanism by which it could.

**The Hopf link is the minimal scattering event.** Two loops with linking
number one close the braid $\sigma_1^2$; by the spectral square of the
proposition the event decomposes over the
[Hopf channel](#def:van-der-waals-hopf-channel) pair as
$\sigma_1^2 = q^2 e_+ + q^{-2} e_-$. The vanishing hyperbolic volume of the
Hopf link — linked but not bonded — matches the soliton picture: the two
loops disturb each other's path while sharing no bonded volume.

**Channel decay is the eigenvalue ratio.** Per crossing, the antisymmetric
channel is carried with weight $-q^{-1}$ against the symmetric channel's $q$,
a relative factor $-q^{-2}$ (the eigenvalue-ratio identity of the
proposition). At the substrate anchor $q_0 > 1$ this is a contraction,
$q_0^{-2} \approx 0.81$: each crossing damps the antisymmetric disturbance by
about a fifth. Together with the gapped second variation of $\mathcal{E}_q$
along each filament ([geodesic vortices](#rem:geodesic-vortices)), this is
the two-mechanism sense in which crossing disturbances decay in the substrate
rapidly enough that the soliton solutions persist: a per-crossing algebraic
contraction between loops, and a spectral gap within each loop.
<!-- FILE_END: two-vortex-scattering-channels.md -->

<!-- FILE_START: braid-fluid.md -->
The categorical [braid-group action](#prop:braid-action-tensor)
acquires a hydrodynamic interpretation in the brane fluid.

**Arnold's geodesic framework.**
Arnold (1966) showed that the Euler equation on $(M, g)$ is the
geodesic equation on $\mathrm{SDiff}(M)$ with the $L^2$ metric:
$\nabla_{\dot\phi}\dot\phi = 0$.  The velocity
$v = \dot\phi \circ \phi^{-1}$ solves
$\partial_t v + \nabla_v v = -\nabla p$.

**$q$-deformed diffeomorphisms.**
The classical $\mathrm{SDiff}(M)$ is replaced by
$\mathrm{SDiff}_q(\mathcal{S})$ on the
[state bundle](#ex:c-quantum-observable-universe), with two consequences:

1. The $L^2$ metric becomes the
   [Webster inner product](#sec:webster-inner-product).
   Geodesics solve the [quantum Euler
   equation](#rem:madelung-fluid) with pressure $Q_q$.

2. Restricting to flows with vorticity on $n$ filaments gives
   a quotient onto $B_n$: the configuration space
   $\mathrm{Conf}_n(M)/S_n$ has fundamental group $B_n$.

**Braid generators as vortex exchanges.**
Each Artin generator $\sigma_i$ is a half-twist exchange of
filaments $i$ and $i+1$.  The
[representation](#prop:braid-action-tensor)
$\rho_n(\sigma_i) = \mathrm{id}^{\otimes(i-1)} \otimes c_{V,V}
\otimes \mathrm{id}^{\otimes(n-i-1)}$
is realised as holonomy of the $\mathrm{SU}(2)$ connection around
the exchange path.  The [Yang--Baxter
equation](#prop:r-matrix-braiding-structure) ensures braiding
three vortices is path-independent (Reidemeister III).

**The dictionary.**

See [Table](#tbl:braid-fluid-table-data).

**Hecke relation as scattering.**
$(T - q)(T + q^{-1}) = 0$ means two vortex tubes interact with
exactly two eigenvalues: $q$ (symmetric pass-through) and
$-q^{-1}$ (antisymmetric reconnection).  The universal ratio

$$
  \frac{\text{reconnection}}{\text{pass-through}}
  = q^{-2}
$$

depends only on the substrate parameter.  This is the
fluid-dynamical origin of the
[skein crossing asymmetry](#rem:skein-crossing-asymmetry).

**Helicity as Markov trace.**
The [Jones polynomial](#thm:jones-markov-trace) $J_L(q)$ is
the **topological helicity** of the vortex tangle — a refinement
of classical helicity $H = \int v \cdot \omegadV$ that
distinguishes configurations invisible to $H$ (e.g. trefoil
from unknot).
<!-- FILE_END: braid-fluid.md -->

<!-- FILE_START: planck-reynolds.md -->
In the brane fluid all three Reynolds-number ingredients are set
by the [substrate parameter](#def:substrate-parameter) $q$:
velocity $c_q = 1/(q-1)$, length $\ell_q = (q-1)/q$, viscosity
$\nu_q = \hbar_q/2 = (q-1)/(2q)$.  The **Planck--Reynolds number**
is

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

The substrate parameter is the inverse turbulence dial: at $q = 1$
the Reynolds number diverges and the full Kolmogorov cascade
operates, but the contact structure degenerates and no particles
exist.  At $q \approx 1.110$ the fluid is transitional — enough
turbulence for a rich [discrete vortex
spectrum](#prop:discrete-vortex-spectrum), not so much that the
spectrum becomes continuous.

The laminar--turbulent transition is at $\mathrm{Re}_q \sim 1$,
i.e. $q \sim 3$.  Active Kelvin modes satisfy
$[k]_q \leq \mathrm{Re}_q^{1/2}$; at $q \approx 1.110$ this gives
$k_{\max} \approx 4$, consistent with four
[intensity levels](#rem:vortex-intensity-modes)
($j = \frac{1}{2}, 1, \frac{3}{2}, 2$).
<!-- FILE_END: planck-reynolds.md -->

