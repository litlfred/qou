The [global regularity theorem](#thm:q-ns-wellposedness) holds for $q > 1$. The classical Navier--Stokes regularity problem concerns the limit $q \to 1$. We identify $q = 1$ as a critical point for a regularity phase transition.

**Conjecture (regularity breakdown).**
There exist smooth, finite-energy initial data $v_0$ such that the classical Navier--Stokes equation (the $q = 1$ limit of the [q-Navier--Stokes equation](#def:q-navier-stokes)) develops a singularity in finite time. Specifically:

1. **Blowup of enstrophy.** There exists a time $T^* < \infty$ such that

   $$
     \lim_{t \to T^{*-}}
     \int_{\mathbb{R}^3} |\omega(x, t)|^2dx
     =  +\infty,
   $$

   where $\omega = \nabla \times v$ is the vorticity.

2. **Vortex sheet concentration.** The blowup occurs by concentration of vorticity onto a codimension-1 surface (vortex sheet). The Hausdorff dimension of the singular set is $d_H = 2$.

3. **Self-similar asymptotics.** Near the blowup time, the solution approaches a self-similar profile

   $$
     v(x, t)
      \approx 
     \frac{1}{\sqrt{T^* - t}}
     V\!\left(\frac{x - x_0}{\sqrt{T^* - t}}\right),
   $$

   where $V(\xi)$ solves the Leray equations $-\frac{1}{2}V - \frac{1}{2}(\xi \cdot \nabla)V + (V \cdot \nabla)V = -\nabla P + \nu\Delta V$.

**Three obstructions to regularity at $q = 1$.**

**Obstruction 1: Loss of UV regularisation.**
At $q = 1$, the $q$-Laplacian eigenvalues degenerate from exponential to polynomial: $[k]_1 = k$. The dissipation rate $\gamma_k = \nuk^2/L^2$ grows quadratically. This growth is insufficient to control the cubic nonlinearity in the enstrophy equation. The $q$-deformation provides a spectral gap $[k+1]_q - [k]_q = q^k$ between consecutive modes. This gap closes as $q \to 1$.

**Obstruction 2: Viscosity vanishes.**
The quantum viscosity $\nu_q = (q-1)/(2q)$ vanishes as $q \to 1$. In the [Planck--Reynolds](#rem:planck-reynolds) formulation, $\mathrm{Re}_q = 2/(q-1) \to \infty$. The classical limit implies infinite turbulence. The finite-dimensional reduction in the well-posedness proof fails because $N_{\mathrm{eff}} \to \infty$.

**Obstruction 3: Cascade becomes continuous.**
The [q-turbulence spectrum](#prop:q-turbulence-spectrum) exhibits discrete transfer rates with exponentially decreasing amplitude. At $q = 1$, the cascade becomes continuous. The transfer rate approaches the Kolmogorov scaling $T_{k \to k+1} \to \varepsilonk^{-1/3}$. Energy reaches arbitrarily high wavenumbers in finite time.

**Critical exponents.**
The transition at $q = 1$ behaves as a second-order phase transition. We define:

- **Enstrophy order parameter**:
  $\Omega(q) = \sup_{t \geq 0} \sum_k [k]_q^2|\hat{v}_k(t)|^2$.
  For $q > 1$, $\Omega(q) < \infty$. At $q = 1$, $\Omega(1) = +\infty$.

- **Critical exponent**:
  $\Omega(q) \sim (q - 1)^{-\alpha}$ as $q \to 1^+$,
  with $\alpha > 0$.

- **Correlation length**:
  The maximum active wavenumber
  $k_{\max}(q) \sim \log_q(\mathrm{Re}_q^{3/4})
  \sim \ln(q-1)^{-1} / \ln q \to \infty$ as $q \to 1^+$.

The [Hamilton--Jacobi picture](#rem:hamilton-jacobi-phase) identifies caustics of the phase $S$ as vortex nucleation sites. These caustics proliferate as $q \to 1$ because the regularising quantum pressure $Q_q$ vanishes. In the classical limit, infinitely many caustics merge into a vortex sheet to form the singularity.

**Relation to the Clay problem.**
The QOU framework reframes the Clay Mathematics Institute Navier--Stokes problem as a degeneration problem. The q-NS equation is globally regular for $q > 1$ ([Theorem](#thm:q-ns-wellposedness)). The Clay problem asks if this regularity survives the limit $q \to 1$. The three obstructions indicate it does not. The classical Navier--Stokes equation is the critical point of a one-parameter family of well-posed equations. Singularity formation is the mechanism by which infinite-dimensional classical dynamics emerge from finite-dimensional $q$-deformed dynamics.

**Analogy with statistical mechanics.**
The regularity phase transition at $q = 1$ parallels the Ising model at the critical temperature $T_c$:

See [Table](#tbl:regularity-breakdown-table-data).

The Ising model is exactly solvable away from $T_c$ but exhibits critical phenomena at $T_c$. Similarly, the $q$-Navier--Stokes equation is globally regular for $q > 1$ but develops singularities at the critical point $q = 1$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
