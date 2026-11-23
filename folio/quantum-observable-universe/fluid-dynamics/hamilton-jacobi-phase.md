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

enforcing the Bohr--Sommerfeld quantisation condition. The $q$-deformation upgrades the integer $n$ to the spin label $j$ under $\mathrm{SU}_q(2)$ representation theory: permitted phase windings measure $2\pi\hbar_q[j]_q$ rather than $2\pi\hbar_qn$.
