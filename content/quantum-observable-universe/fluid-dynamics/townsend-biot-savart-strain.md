The [Levi degeneracy conjecture](#conj:levi-degeneracy) reduces the $q \to 1$ Navier--Stokes regularity question to the asymptotic behaviour of the core aspect ratio $\kappa^2 = a_\perp^2 / a_\parallel^2 = V_2 / V_1$ at the vortex-collision time $T^\ast$ ([prop:core-levi-form](#prop:core-levi-form)). This section and its [hyperbolic-overlap companion](#rem:hyperbolic-overlap-saturation) solve the ODE for $(V_1, V_2)$ in two physical regimes. We first consider the singular Biot--Savart strain, valid when cores are well-separated. We then analyze the hyperbolic saturation that takes over when cores overlap.

**Setup.**
Consider two anti-parallel vortex filaments with circulation $\Gamma$ approaching head-on at a collision time $T^\ast$. We model the cross-section of each viscous core using the Townsend covariance matrix \cite{townsend1951}. Let $V_1(t)$ denote the squared core radius in the direction of advective stretching, and $V_2(t)$ the squared core radius in the perpendicular direction of compression. The Biot--Savart derivation (Saffman \cite{saffman1992} §11.2; Moffatt--Kida--Ohkitani \cite{moffatt1994}) gives the evolution of the squared separation:

$$
  d(t)^2 = \frac{c\,\Gamma (T^\ast - t)}{\pi},
$$

where the constant $c$ depends on whether $\Gamma/(2\pi d)$ measures a single filament's induced velocity ($c = 1$) or the relative approach speed ($c = 2$). The time scaling remains identical. We fix $c = 1$. The external strain rate induced by one filament on the other is:

$$
  \alpha(t)
  \;=\;
  \frac{\Gamma}{2\pi d(t)^2}
  \;=\;
  \frac{1}{2c\,(T^\ast - t)}.
$$

The leading behaviour $\alpha \propto 1/(T^\ast - t)$ is independent of $c$. The strain rate $\alpha(t)$ is independent of the circulation $\Gamma$. Under the point-vortex approximation, the circulation cancels between numerator and denominator. The time-to-collision strictly determines the strain rate.

**Townsend evolution.**
Under axisymmetric viscous strain, the squared core radii evolve as \cite{townsend1951,moffatt1994}:

$$
  \frac{dV_1}{dt} = +2\,\alpha(t)\,V_1 + 2\nu,
  \qquad
  \frac{dV_2}{dt} = -2\,\alpha(t)\,V_2 + 2\nu,
$$

where $\nu$ is the kinematic viscosity. We introduce the remaining time $\tau = T^\ast - t$. Substituting $d/dt = -d/d\tau$ and $\alpha(t) = 1/(2\tau)$ yields the linear system:

$$
  \frac{dV_1}{d\tau} + \frac{V_1}{\tau} = -2\nu,
  \qquad
  \frac{dV_2}{d\tau} - \frac{V_2}{\tau} = -2\nu.
$$

**Exact solutions.**
We apply the integrating factor $\tau$ for $V_1$ and $1/\tau$ for $V_2$:

$$
  \frac{d(\tau V_1)}{d\tau} = -2\nu\tau
  \quad\Longrightarrow\quad
  V_1(\tau) = \frac{C_1}{\tau} - \nu\tau,
$$

$$
  \frac{d(V_2/\tau)}{d\tau} = -\frac{2\nu}{\tau}
  \quad\Longrightarrow\quad
  V_2(\tau) = -2\nu\,\tau\ln\tau + C_2\,\tau.
$$

The constants $C_1, C_2$ are determined by the initial cross-section in the close-approach window. As the collision approaches ($\tau \to 0$):

- The stretching coordinate diverges: $V_1(\tau) \sim C_1/\tau \to \infty$.
- The compressing coordinate vanishes: $V_2(\tau) \sim -2\nu\,\tau \ln\tau \to 0$.

**The first-order Levi prediction.**
The squared Levi condition number is:

$$
  \kappa^2(\tau)
  = \frac{V_2(\tau)}{V_1(\tau)}
  \;\sim\;
  \frac{-2\nu\,\tau^2\ln\tau}{C_1}
  \;\xrightarrow[\tau \to 0]{}\; 0.
$$

In this approximation, viscous diffusion completely flattens the core into a two-dimensional sheet just before collision. By [prop:core-levi-form](#prop:core-levi-form)(c), $\kappa \to 0$ forces the Levi form to become strictly degenerate at the collision locus. The contact eigenvalue $\lambda_\parallel \to 0$ while $\lambda_\perp$ remains bounded. The local cohomology group $H^1_{\mathfrak{m}_p}(A)$ vanishes, dissolving the cohomological obstruction. The system maintains global regularity. This realizes the [branch (B) outcome](#conj:levi-degeneracy) of the conjecture (global Navier--Stokes regularity) under the point-vortex assumption.

**Breakdown of the approximation.**
The Biot--Savart strain rate $\alpha(t) = \Gamma / (2\pi d(t)^2)$ assumes a point-vortex geometry where cores are much smaller than their separation ($V_1 \ll d^2$). However, as $\tau \to 0$, $V_1(\tau) \sim C_1/\tau \to \infty$, whereas $d(\tau)^2 = \Gamma\tau/\pi \to 0$. A crossover occurs at a finite time $\tau_\ast$ defined by $V_1(\tau_\ast) = d(\tau_\ast)^2$. Beyond this point, the filaments overlap and the Biot--Savart kernel fails. The strain field near the collision plane is no longer a superposition of well-separated vortices; it becomes the merged flow of a single interaction zone. The [hyperbolic-overlap saturation](#rem:hyperbolic-overlap-saturation) computes the strain field in the overlap regime. It demonstrates that the apparent flattening ($\kappa \to 0$) is an artefact of the failed approximation.
