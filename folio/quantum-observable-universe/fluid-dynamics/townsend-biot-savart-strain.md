We compute the asymptotic behaviour of the core aspect ratio at the vortex-collision time $T^\ast$. First, we use the singular Biot–Savart strain valid when cores are well separated. Next, we use the hyperbolic saturation that takes over when cores overlap.

**Setup.**
Two anti-parallel vortex filaments with circulation $\Gamma$ approach head-on at collision time $T^\ast$. We model the cross-section of each viscous core by the Townsend covariance matrix: $V_1(t)$ is the squared core radius in the stretching direction, and $V_2(t)$ is the squared core radius in the compression direction. The external strain rate induced by one filament on the other is $\alpha(t) = 1/(2(T^\ast - t))$. The leading behaviour is convention-independent. The strain rate is independent of $\Gamma$.

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

**The first-order Levi prediction.**
The squared Levi condition number is $\kappa^2(\tau) = V_2(\tau)/V_1(\tau) \to 0$. Viscous diffusion flattens the core into a two-dimensional sheet. The Levi form is strictly degenerate at the collision locus. The local cohomology group vanishes, the cohomological obstruction dissolves, and the system maintains global regularity. This is branch (B) of the conjecture under the point-vortex assumption.

**Breakdown of the approximation.**
The Biot–Savart strain rate assumes a point-vortex geometry. But $V_1(\tau) \to \infty$ while $d(\tau)^2 \to 0$. The two cross over at a finite $\tau_\ast$, after which the filaments overlap. The Biot–Savart kernel is no longer valid. The strain field near the collision plane is the merged flow of a single interaction zone. The apparent flattening $\kappa \to 0$ is an artefact of the failed approximation.
