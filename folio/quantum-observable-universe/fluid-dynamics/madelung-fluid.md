**The Madelung split.**
Decomposing $\psi = \sqrt{\rho}\exp(JS/\hbar_q)$ following Erwin Madelung \cite{madelung1927} separates the [q-deformed Schrödinger equation](#rem:schrodinger-jet-coaction) into two real equations. Setting the velocity $v = \nabla_A S$ and fluid density $\rho = |\psi|^2$ yields:

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
The [aether parameter](#def:aether-parameter) $q$ modulates the effective thickness of the quantum fluid. Near $q \approx 1$, the quantum pressure vanishes ($Q_q \approx 0$) and the system reduces to ordinary inviscid flow. At $q \gg 1$, $Q_q$ dominates; the fluid strongly resists compression. This resistance acts as the inertial mass of the brane.

**Zero-information state $|\psi|^2 = 0$.**
The vacuum $\psi = 0$ carries no medium, no vortex, and no fermion. It lies outside the support of all harmonic modes filtered by the [algebraic filter](#rem:algebraic-filter). As $q \to 1$, $\hbar_q \to 0$: the vacuum represents the state of maximal classical certainty.

**Geodesics as stable vortex filaments.**
Bosonic modes follow straight null geodesics of the acoustic metric $g_{\mathrm{ac}}$. Fermionic modes spiral around the zeros of $\psi$, forming stable vortex filaments $\varrho$ whose mass follows

$$
  m  \propto  \oint_\varrho \|\nabla_A q\|\cdot\|L \wedge F^+\|,
$$

reproducing the [mass identity](#def:mass-identity) as a line integral of the aether curvature around the vortex core. Because $\psi$ is a single complex amplitude rather than a two-component Pauli spinor, circulation is concentrated on nodal filaments $\psi = 0$ where $v = \nabla_A S$ is irrotational outside the core; this differs from the spinor hydrodynamics of Takehiko Takabayasi \cite{takabayasi1952,takabayasi1983}, in which local spin-triad gradients generate distributed bulk vorticity away from nodal lines.
