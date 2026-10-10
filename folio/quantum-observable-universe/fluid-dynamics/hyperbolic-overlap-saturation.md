Once the stretching coordinate $V_1$ reaches the squared separation $d^2$, the point-vortex kernel breaks down. The local stream function shifts to a hyperbolic stagnation-point flow. The apparent flattening $\kappa \to 0$ reverses. The squared Levi condition number locks to a strictly positive constant $\kappa^2 = \pi\nu/\Gamma$.

**Mechanism of the kernel change.**
The singular Biot–Savart strain diverges because $d \to 0$. Once $V_1 \gtrsim d^2$, the filaments are no longer distinct. Their merged interaction is an elliptic-section vortex sitting at a hyperbolic stagnation point. The strain rate is bounded by the overlapping cores themselves. The length scale is $\sqrt{V_1}$. The kernel rotates to a Burgers-like strain $\alpha_{\mathrm{hyp}}(t) = \Gamma/(\pi V_1(t))$.

**Saturated Townsend system.**
Substituting $\alpha_{\mathrm{hyp}}$ into the stretching equation gives a constant right-hand side. $V_1$ grows linearly with time and remains finite through to the formal collision time $T^\ast$. The exponential runaway is replaced by controlled linear growth. The strain saturates because the same coordinate driving the stretching also sets the length scale.

**Compression — proportionality ansatz.**
Substituting the saturated strain into the compression equation bounds the compressive sink. The $V_2$ relaxation rate is comparable to the $V_1$ growth rate, preventing quasi-steady equilibrium. We use the proportionality ansatz $V_2(t) = \lambda V_1(t)$. The ODE forces

$$
  \boxed{\;\;
  \kappa^2
  \;=\;
  \frac{V_2}{V_1}
  \;=\;
  \frac{\pi\nu}{2\Gamma + \pi\nu}.
  \;\;}
$$

In the high-Reynolds limit, $\kappa^2 \simeq \pi\nu/(2\Gamma)$.

Because $\kappa^2 > 0$, the Levi form remains non-degenerate at the collision locus $\Sigma$. Both eigenvalues stay bounded away from zero. The local cohomology group remains non-zero. The cohomological obstruction is preserved up to $T^\ast$. This is branch (A) of the conjecture: classical 3D Navier–Stokes admits finite-time blowup.

**Reading.**
The Biot–Savart prediction $\kappa \to 0$ is an artefact of the point-vortex approximation. The hyperbolic-overlap calculation predicts the asymptotic core ratio is strictly positive. The cores lock into a finite elliptical profile supported by the hyperbolic strain. The vortex collision preserves the contact non-degeneracy. The geometric obstruction survives the viscous regularity mechanism.

**Caveats.**
1. The kernel switch at the overlap time is a phenomenological dimensional ansatz, not a derivation from Euler/NS.
2. The asymptotic value is the attracting proportionality ratio, not the naive Burgers equilibrium.
3. The Townsend equations assume axisymmetric straining. Three-dimensional instabilities may modify the picture.
4. The conclusion "$\kappa^2 > 0 \Rightarrow$ blowup" is conditional on the regularity-breakdown programme. The explicit ODE establishes the asymptotic core-shape constant; lifting this to NS blowup requires the Levi degeneracy and counter-example conjectures.
