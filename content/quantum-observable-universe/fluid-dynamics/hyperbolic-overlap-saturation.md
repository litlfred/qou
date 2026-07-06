The [Biot–Savart prediction](#rem:townsend-biot-savart-strain) that the squared core ratio $\kappa^2 \to 0$ at collision holds only while the cores remain well-separated. Once the stretching coordinate $V_1$ reaches the squared separation $d^2$, the point-vortex kernel breaks down. The local stream function near the collision plane shifts from the superposition of two circular vortices to a **hyperbolic stagnation-point flow**. We evaluate the Townsend ODE in this hyperbolic regime. We find the apparent flattening $\kappa \to 0$ reverses. The squared Levi condition number locks to a strictly positive constant $\kappa^2 = \pi\nu/\Gamma$.

**Mechanism of the kernel change.**
The singular Biot–Savart strain $\alpha(t) = \Gamma/(2\pi d^2)$ diverges only because $d \to 0$ while the cores are small. Once $V_1 \gtrsim d^2$, the filaments merge. Their interaction is described by an elliptic-section vortex at a hyperbolic stagnation point of the macroscopic flow. The strain rate is bounded by the overlapping cores. The relevant length scale becomes $\sqrt{V_1}$:
$$
  \alpha(t) \;\longrightarrow\;
  \alpha_{\mathrm{hyp}}(t)
  \;=\;
  \frac{\Gamma}{\pi V_1(t)}.
$$
The kernel rotates from a $1/d^2$ Biot–Savart strain to a $1/V_1$ Burgers-like strain.

**Saturated Townsend system.**
Substituting $\alpha_{\mathrm{hyp}} = \Gamma/(\pi V_1)$ into the stretching equation gives
$$
  \frac{dV_1}{dt}
  = 2\,\alpha_{\mathrm{hyp}}\,V_1 + 2\nu
  = \frac{2\Gamma}{\pi V_1}\cdot V_1 + 2\nu
  = \frac{2\Gamma}{\pi} + 2\nu.
$$
The right-hand side is constant. The variable $V_1$ grows linearly with time rather than diverging, and remains finite through to the formal collision time $t_\ast$. Explicitly,
$$
  V_1(t) \;=\; V_1(t_\ast) +
  \left( \tfrac{2\Gamma}{\pi} + 2\nu \right)(t - t_\ast),
$$
where $t_\ast$ is the time at which the overlap regime begins. The exponential runaway predicted by the point-vortex approximation is replaced by a controlled linear growth. The strain saturates because the coordinate driving the stretching also sets the relevant length scale.

**Compression — proportionality ansatz.**
Substituting the saturated strain into the compression equation gives
$$
  \frac{dV_2}{dt}
  = -2\,\alpha_{\mathrm{hyp}}\,V_2 + 2\nu
  = -\frac{2\Gamma\,V_2}{\pi V_1} + 2\nu.
$$
Because $V_1$ is finite and increases linearly in $t$, the compressive sink is bounded. The constant viscous source $2\nu$ balances it. The quasi-steady ansatz $\dot V_2 = 0$ yields the standard Burgers vortex equilibrium thickness $V_2 = \pi\nu V_1/\Gamma$. However, the $V_2$ relaxation rate $2\Gamma/(\pi V_1)$ is comparable to the $V_1$ growth rate $b/V_1$. Specifically, $b/(2\Gamma/\pi) = 1 + \pi\nu/\Gamma$. Thus $V_2$ and $V_1$ evolve on the same timescale. The variable $V_2$ cannot equilibrate to an instantaneous target while $V_1$ varies.

**Asymptotic proportionality.**
We substitute the proportionality ansatz $V_2(t) = \lambda V_1(t)$, valid asymptotically once the transient $V_2$-mode decays. We have $\dot V_2 = \lambda \dot V_1 = \lambda b$. The ODE requires
$$
  \lambda b
  \;=\;
  -\frac{2\Gamma}{\pi}\,\lambda + 2\nu.
$$
This gives $\lambda(b + 2\Gamma/\pi) = 2\nu$. Substituting $b = 2\Gamma/\pi + 2\nu$ yields $b + 2\Gamma/\pi = 4\Gamma/\pi + 2\nu$, hence
$$
  \boxed{\;\;
  \kappa^2
  \;=\;
  \frac{V_2}{V_1}
  \;=\;
  \lambda
  \;=\;
  \frac{2\nu}{4\Gamma/\pi + 2\nu}
  \;=\;
  \frac{\pi\nu}{2\Gamma + \pi\nu}.
  \;\;}
$$
In the high-Reynolds limit $\nu \ll \Gamma$, $\kappa^2 \simeq \pi\nu/(2\Gamma)$. This is half the value produced by the quasi-steady ansatz.

Solving the inhomogeneous linear ODE with integrating factor $(V_1/V_{10})^{\beta}$, where $\beta = 2\Gamma/(\pi b)$, gives the exact solution
$$
  V_2(t)
  \;=\;
  \frac{2\nu\,V_1(t)}{b(\beta + 1)}
  \;+\;
  K\,V_1(t)^{-\beta},
$$
where the second term is a decaying transient. The particular term has the ratio $2\nu/(b(\beta+1)) = \pi\nu/(2\Gamma + \pi\nu)$, confirming the asymptotic limit.

By [prop:core-levi-form](#prop:core-levi-form)(b–c), $\kappa^2 > 0$ implies the Levi form remains non-degenerate at the collision locus $\Sigma$. Both eigenvalues $\lambda_\parallel, \lambda_\perp$ stay bounded away from zero. The local cohomology group $H^1_{\mathfrak{m}_p}(A)$ remains non-zero. The cohomological obstruction is preserved up to $T^\ast$, and the [NS obstruction](#def:ns-obstruction) does not dissolve under viscous diffusion. This corresponds to the [branch (A) outcome](#conj:levi-degeneracy) of the conjecture: classical 3D Navier–Stokes admits finite-time blowup.

**The dichotomy in one table.**

| Regime | Strain $\alpha$ | $V_1$ behaviour | $V_2$ behaviour | $\kappa^2$ at $T^\ast$ | Levi form | NS conclusion |
|---|---|---|---|---|---|---|
| Biot–Savart ([`rem:townsend-biot-savart-strain`](#rem:townsend-biot-savart-strain)) | $1/(2\tau)$ | $\sim C_1/\tau \to \infty$ | $\sim -2\nu\tau\ln\tau \to 0$ | $0$ | Degenerate | Regular (branch B) |
| Hyperbolic overlap | $\Gamma/(\pi V_1)$ | Linear in $t$, finite at $T^\ast$ | $\pi\nu V_1/(2\Gamma+\pi\nu) > 0$ | $\pi\nu/(2\Gamma + \pi\nu)$ | Non-degenerate | Blowup (branch A) |

The Biot–Savart prediction $\kappa \to 0$ is an artefact of the point-vortex approximation. It never reaches $\tau = 0$ because the approximation breaks down at the overlap time $\tau_\ast$. The hyperbolic-overlap calculation predicts the asymptotic core ratio $\kappa^2 = \pi\nu/(2\Gamma+\pi\nu) > 0$. The cores do not flatten into sheets; they lock into a finite elliptical profile supported by the hyperbolic strain. The vortex collision preserves the contact non-degeneracy, carrying the NS obstruction class intact to $T^\ast$.

**Caveats.**
1. The kernel switch $\alpha(t) \to \Gamma/(\pi V_1)$ is a phenomenological ansatz. The relevant length scale inside the overlap region is heuristically replaced by $\sqrt{V_1}$.
2. The asymptotic value $\kappa^2 = \pi\nu/(2\Gamma + \pi\nu)$ is the attracting proportionality ratio of the linear ODE. It differs from the quasi-steady Burgers equilibrium by a factor of 2 in the high-Reynolds limit.
3. The Townsend equations assume axisymmetric straining. Three-dimensional instabilities (Kelvin modes, [helical](#rem:helicity-physical) twisting) may modify this dynamic.
4. The conclusion $\kappa^2 > 0 \Rightarrow$ blowup routes through [`prop:core-levi-form`](#prop:core-levi-form). The ODE rigorously establishes the asymptotic core-shape constant $\kappa^2 = \pi\nu/(2\Gamma + \pi\nu)$; lifting this to NS blowup requires the [Levi degeneracy](#conj:levi-degeneracy) and [counter-example](#conj:ns-counterexample) conjectures.
