The [Madelung decomposition](#rem:madelung-fluid)
$\psi = \sqrt{\rho}\,\exp(JS/\hbar_q)$ yields two real equations:
one for $\rho$ (continuity) and one for $v = \nabla_A S$ (quantum
Euler).  The equation for the phase $S$ itself — the **quantum
Hamilton--Jacobi equation** — is the other face of the Madelung
picture and connects the brane fluid directly to classical
mechanics.

**The $q$-deformed Hamilton--Jacobi equation.**
Substituting $\psi = \sqrt{\rho}\,\exp(JS/\hbar_q)$ into the
[q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction) and
separating real parts gives

$$
  \partial_t S
  \;+\;
  \frac{1}{2}\,\lVert\nabla_A S\rVert^2
  \;+\; V
  \;+\; Q_q
  \;=\; 0,
$$

where $V$ is the external potential (curvature of the
$\mathrm{SU}(2)$ connection) and $Q_q = -(\hbar_q^2/2)\,
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
Expanding $S = S_0 + \hbar_q\,S_1 + \hbar_q^2\,S_2 + \cdots$
produces a hierarchy:

- **$O(1)$: Eikonal equation.**
  $\partial_t S_0 + \frac{1}{2}\lVert\nabla_A S_0\rVert^2 + V = 0$.
  This is the classical Hamilton--Jacobi equation without quantum
  corrections.  Its characteristics are the classical geodesics of
  the [GR substrate geometry](#rem:gr-substrate-geometry).

- **$O(\hbar_q)$: Transport equation.**
  $\partial_t S_1 + \nabla_A S_0 \cdot \nabla_A S_1 =
  -\frac{1}{2}\,\Delta_q S_0$.
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
  \;=\;
  2\pi\hbar_q\,n,
  \qquad n \in \mathbb{Z},
$$

which is the Bohr--Sommerfeld quantisation condition.  In the
$q$-deformed setting, the integer $n$ is promoted to the spin
label $j$ via the $\mathrm{SU}_q(2)$ representation theory:
the allowed phase windings are $2\pi\hbar_q\,[j]_q$ rather than
$2\pi\hbar_q\,n$.  This connects the Hamilton--Jacobi picture
to the [discrete vortex spectrum](#prop:discrete-vortex-spectrum)
and completes the circle between wave mechanics, fluid dynamics,
and the particle picture.
