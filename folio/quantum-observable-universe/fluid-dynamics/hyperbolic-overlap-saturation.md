Once the stretching coordinate $V_1$ reaches the squared separation $d^2$, the point-vortex kernel breaks down. The local stream function shifts to a hyperbolic stagnation-point flow. The apparent flattening $\kappa \to 0$ reverses. The squared core aspect ratio locks to a strictly positive constant, $\kappa^2 = \pi\nu/(2\Gamma + \pi\nu)$ (strictly below the naive quasi-steady estimate $\pi\nu/\Gamma$).

**Mechanism of the kernel change.**
The singular Biot–Savart strain diverges because $d \to 0$. Once $V_1 \gtrsim d^2$, the filaments are no longer distinct. Their merged interaction is an elliptic-section vortex sitting at a hyperbolic stagnation point. The strain rate is bounded by the overlapping cores themselves. The length scale is $\sqrt{V_1}$. The kernel rotates to a Burgers-like strain $\alpha_{\mathrm{hyp}}(t) = \Gamma/(\pi V_1(t))$.

**Saturated Townsend system.**
Substituting $\alpha_{\mathrm{hyp}}$ into the stretching equation gives a constant right-hand side. $V_1$ grows linearly with time and remains finite through to the formal collision time $T^\ast$. The exponential runaway is replaced by controlled linear growth. The strain saturates because the same coordinate driving the stretching also sets the length scale.

**Compression — proportionality ansatz.**
Substituting the saturated strain into the compression equation bounds the compressive sink. The $V_2$ relaxation rate is comparable to the $V_1$ growth rate, preventing quasi-steady equilibrium. Under the proportionality ansatz $V_2(t) = \lambda V_1(t)$, the ODE forces

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

Because $\kappa^2 > 0$, the cores do not flatten into sheets in this model: their cross-section locks into a finite ellipse.

**Reading.**
The Biot–Savart prediction $\kappa \to 0$ is an artefact of the point-vortex approximation. The hyperbolic-overlap calculation predicts the asymptotic core ratio is strictly positive. The cores lock into a finite elliptical profile supported by the hyperbolic strain.

**Quantities left undetermined by the overlap lock.** The core aspect ratio carries no Levi information. With the plane field $\ker\varTheta = \xi^\perp$ of the [core Levi form proposition](#prop:core-levi-form), the Levi datum is the single scalar $\xi\cdot\mathrm{curl}\,\xi$, and a straight anti-parallel pair has $\xi\cdot\mathrm{curl}\,\xi = 0$ whatever its core shape. So $\kappa^2 > 0$ does not establish Levi non-degeneracy, and by itself it carries no blow-up verdict; see the Beltrami counterexample in the [Levi degeneracy conjecture](#conj:levi-degeneracy).

**Caveats.**
1. The kernel switch at the overlap time is a phenomenological dimensional ansatz rather than a derivation from Euler/NS.
2. The asymptotic value is the attracting proportionality ratio rather than the naive Burgers equilibrium.
3. The Townsend equations assume axisymmetric straining. Three-dimensional instabilities may modify the picture.
4. The explicit ODE establishes the asymptotic core-shape constant and nothing more. No route from this constant to blow-up remains in the chapter.
