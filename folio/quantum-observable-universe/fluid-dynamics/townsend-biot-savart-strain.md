The asymptotic behaviour of the core aspect ratio at the vortex-collision time $T^\ast$ splits into two regimes: first, the singular Biot–Savart strain valid when cores are well separated; second, the hyperbolic saturation that takes over when cores overlap.

**Setup.**
Two anti-parallel vortex filaments with circulation $\Gamma$ approach head-on at collision time $T^\ast$. Each viscous core cross-section is modelled by the Townsend covariance matrix: $V_1(t)$ is the squared core radius in the stretching direction, and $V_2(t)$ is the squared core radius in the compression direction. The external strain rate induced by one filament on the other is $\alpha(t) = 1/(2(T^\ast - t))$. The leading behaviour is convention-independent. The strain rate is independent of $\Gamma$.

**Townsend evolution.**
Under axisymmetric viscous strain, the squared core radii satisfy
$$
  \frac{dV_1}{dt} = +2\,\alpha(t)\,V_1 + 2\nu,
  \qquad
  \frac{dV_2}{dt} = -2\,\alpha(t)\,V_2 + 2\nu.
$$
Substituting $\alpha(t) = 1/(2\tau)$ for the time remaining $\tau = T^\ast - t$ gives a linear system.

**Exact solutions.**
As the collision is approached ($\tau \to 0$), the stretching coordinate diverges ($V_1(\tau) \sim C_1/\tau \to \infty$) and the compressing coordinate vanishes ($V_2(\tau) \sim -2\nu\,\tau \ln\tau \to 0$).

**The first-order shape prediction.**
The squared core aspect ratio is $\kappa^2(\tau) = V_2(\tau)/V_1(\tau) \to 0$. Viscous diffusion flattens the core into a two-dimensional sheet. This is a statement about the shape of the core cross-section, under the point-vortex assumption. It carries no Levi information. With the plane field $\ker\varTheta = \xi^\perp$ of the [core Levi form proposition](#prop:core-levi-form), a straight anti-parallel pair has $\xi = \pm e_z$ on each core, so its Levi scalar $\xi\cdot\mathrm{curl}\,\xi$ is $0$ whatever the core shape. Flattening therefore neither creates nor removes a Levi degeneration. The straight pair satisfies the hypothesis of branch (B) of the [Levi degeneracy conjecture](#conj:levi-degeneracy) for every core shape, and it is regular for a different reason: its vorticity is $\omega_z(x, y)\,e_z$, so the flow is two-dimensional.

**Breakdown of the approximation.**
The Biot–Savart strain rate assumes a point-vortex geometry. But $V_1(\tau) \to \infty$ while $d(\tau)^2 \to 0$. The two cross over at a finite $\tau_\ast$, after which the filaments overlap. The Biot–Savart kernel is no longer valid. The strain field near the collision plane is the merged flow of a single interaction zone. The apparent flattening $\kappa \to 0$ is an artefact of the failed approximation.
