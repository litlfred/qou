The [quantum Euler equation](#rem:madelung-fluid) describes
inviscid flow in the brane fluid.  To account for dissipation —
the irreversible transfer of kinetic energy from coherent vortex
motion to incoherent thermal fluctuations — we introduce the
**$q$-deformed Navier--Stokes equation**.

Let $v = \nabla_A S$ be the velocity field, $\rho = |\psi|^2$ the
density, $p$ the pressure, and $\nu_q = \hbar_q / 2 = (q-1)/(2q)$
the [kinematic viscosity](#rem:planck-reynolds).  The $q$-deformed
Navier--Stokes equation is

$$
  \partial_t v + (v \cdot \nabla_A)v
  \;=\;
  -\frac{1}{\rho}\,\nabla_A p
  \;-\; \nabla_A Q_q
  \;+\; \nu_q\,\Delta_q v
  \;+\; \frac{1}{\rho}\,
  \nabla_A \cdot \boldsymbol{\sigma}_q,
$$

where $Q_q = -(\hbar_q^2/2)\,\Delta_q\sqrt{\rho}/\sqrt{\rho}$ is
the quantum pressure, $\Delta_q v$ is the $q$-Laplacian applied to
the velocity field, and $\boldsymbol{\sigma}_q$ is the $q$-deformed
viscous stress tensor

$$
  (\boldsymbol{\sigma}_q)_{ij}
  \;=\;
  \nu_q\,\rho\,
  \bigl(
    \nabla_{A,i}\,v_j + \nabla_{A,j}\,v_i
    - \tfrac{2}{3}\,(\nabla_A \cdot v)\,\delta_{ij}
  \bigr),
$$

with all derivatives taken with respect to the $\mathrm{SU}(2)$
connection $A$.

The equation is supplemented by the continuity equation
$\partial_t\rho + \nabla_A \cdot (\rho v) = 0$.

**Distinguishing features.**
Three properties separate this from the classical Navier--Stokes
equation:

1. **Algebraic dissipation spectrum.**  The viscous term
   $\nu_q\,\Delta_q v$ damps mode $k$ at rate
   $\nu_q\,[k]_q^2 / L_q^2$.  Because the $q$-integers
   grow as $[k]_q \sim q^k / (q - q^{-1})$ for large $k$,
   high-wavenumber modes are damped **exponentially** rather than
   polynomially, providing a natural UV regularisation absent from
   classical Navier--Stokes.

2. **Gauge-covariant diffusion.**  The connection $A$ appears in
   every derivative.  Viscous diffusion transports not only momentum
   but also colour charge: a vortex filament that decays by viscous
   damping radiates its $\mathrm{SU}_q(2)$ quantum numbers into
   neighbouring filaments via the connection.

3. **Quantum pressure as negative viscosity.**  The $Q_q$ term
   acts as a negative viscosity at short wavelengths: it
   **opposes** compression of the fluid below the scale
   $\ell_q = (q-1)/q$.  The balance between $\nu_q\,\Delta_q v$
   (dissipation) and $\nabla_A Q_q$ (quantum repulsion) determines
   the minimum vortex core radius.

**Energy dissipation rate.**
The global energy dissipation rate of the $q$-Navier--Stokes
equation is

$$
  \varepsilon_q
  \;=\;
  \nu_q \int_{\mathcal{S}}
  \rho\,\lVert\nabla_A v\rVert^2\,d\mu
  \;=\;
  \nu_q \sum_{k=1}^{\infty}
  [k]_q^2\,|v_k|^2,
$$

where $v_k$ are the Fourier coefficients in the $q$-integer
eigenbasis.  For $q > 1$, the sum converges absolutely
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
globally well-posed in 3d for any $q > 1$: the energy estimate
$\frac{d}{dt}\lVert v\rVert^2 \leq -\nu_q\,[1]_q^2\,\lVert v\rVert^2$
gives exponential decay of the total kinetic energy, and the
$q$-integer growth prevents the enstrophy blowup that obstructs
classical regularity proofs.  The classical 3d Navier--Stokes
regularity problem is thus an artefact of the $q \to 1$
degeneration.
