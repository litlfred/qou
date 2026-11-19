*Within a QOU $(\mathbf{C}, A, \tau)$.* The statements below concern the QOU's internal $q$-Navier--Stokes flow; identifying that internal flow with the classical $\mathbb{R}^3$ equation is the separate open categorical-to-classical bridge and is not asserted here.

The global regularity theorem holds for every $q > 1$. The classical Navier--Stokes regularity problem asks what happens at $q = 1$. The QOU framework dictates that $q = 1$ is a **critical point** where regularity undergoes a phase transition.

**Conjecture (regularity breakdown).**
There exist smooth, finite-energy initial data $v_0$ such that the classical Navier--Stokes equation develops a singularity in finite time. Specifically:

1. **Blowup of enstrophy.** There exists a time $T^* < \infty$ such that $\lim_{t \to T^{*-}} \int_{\mathbb{R}^3} |\omega(x, t)|^2dx = +\infty$, where $\omega = \nabla \times v$ is the vorticity.
2. **Vortex sheet concentration.** The blowup occurs by concentration of vorticity onto a codimension-1 surface (vortex sheet). The *spatial* Hausdorff dimension of the sheet is $d_H = 2$. This is not, a priori, in contradiction with the Caffarelli--Kohn--Nirenberg bound (the *parabolic* Hausdorff dimension of the space--time singular set of a suitable weak solution is $\leq 1$): the two measure different sets. A single-instant $2$-dimensional spatial concentration would violate the CKN bound, so compatibility requires the sheet to be read scale-by-scale along the discretely self-similar approach (item 3), which spreads the concentration through space--time rather than onto one time slice; establishing that the resulting space--time set stays within the CKN bound is a required reconciliation that has not yet been carried out.
3. **Discretely self-similar asymptotics.** Near the blowup time, the solution approaches a *discretely* self-similar profile: in Leray's similarity variables $y = (x - x_0)/\sqrt{T^* - t}$, $s = -\log(T^* - t)$, the profile is periodic in $s$ (with period set by the root-of-unity scaling $\lambda_\kappa$) rather than steady. The continuous ($s$-independent) self-similar profile solving the Leray equations is excluded \cite{necas-ruzicka-sverak1996}; see the [Leray profile proposition](#prop:leray-profile).

**The three obstructions.**

**Obstruction 1: Loss of UV regularisation.** At $q = 1$, the $q$-Laplacian eigenvalues degenerate from exponential to polynomial: $[k]_1 = k$. The dissipation rate grows only quadratically, insufficient to control the cubic nonlinearity in the enstrophy equation. The $q$-deformation provides a spectral gap that closes at $q = 1$.

**Obstruction 2: Viscosity vanishes.** The quantum viscosity $\nu_q = (q-1)/(2q) \to 0$ as $q \to 1$. The classical limit is infinitely turbulent. The finite-dimensional reduction fails because $N_{\mathrm{eff}} \to \infty$.

**Obstruction 3: Cascade becomes continuous.** The $q$-turbulence spectrum has discrete transfer rates with exponentially decreasing amplitude. At $q = 1$, the cascade becomes continuous and the transfer rate $T_{k \to k+1} \to \varepsilon_k^{-1/3}$, allowing energy to reach arbitrarily high wavenumbers in finite time.

**Critical exponents.**
The transition at $q = 1$ has the structure of a second-order phase transition, characterised by three quantities:
- **Enstrophy order parameter**: $\Omega(q) = \sup_{t \geq 0} \sum_k [k]_q^2|\hat{v}_k(t)|^2$. For $q > 1$, $\Omega(q) < \infty$. At $q = 1$, $\Omega(1) = +\infty$.
- **Critical exponent**: $\Omega(q) \sim (q - 1)^{-\alpha}$ as $q \to 1^+$.
- **Correlation length**: The maximum active wavenumber $k_{\max}(q) \sim \log_q(\mathrm{Re}_q^{3/4}) \to \infty$ as $q \to 1^+$.

**Relation to the Clay problem.**
The QOU framework reframes the Clay formulation as a degeneration problem. The $q$-NS equation is globally regular for all $q > 1$, and the Clay question asks whether this regularity survives the limit $q \to 1$. The three obstructions above suggest it does not. The classical Navier--Stokes equation is the critical point of a one-parameter family of well-posed equations. Singularity formation is the mechanism by which infinite-dimensional classical dynamics emerge from finite-dimensional $q$-deformed dynamics.
