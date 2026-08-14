The two-regime collision model of [the Biot–Savart approach](#rem:townsend-biot-savart-strain) and [the hyperbolic-overlap saturation](#rem:hyperbolic-overlap-saturation) treats the anti-parallel pair as two-dimensional. The named three-dimensional effect outside the model is the Crow instability: sinusoidal displacement perturbations of an anti-parallel filament pair grow by mutual induction at rate

$$
  \sigma \approx s^* \, \frac{\Gamma}{2\pi d^2},
$$

with $s^* \approx 0.8$ at the classical optimal wavelength for core-to-separation ratio $\approx 0.1$.

Along the phase-1 approach $d^2(t) = d_0^2 - (\Gamma/\pi)\,t$, the accumulated perturbation growth to the overlap engagement $d^2_{\mathrm{ov}}$ integrates in closed form:

$$
  N_e \;=\; \int_0^{t_{\mathrm{ov}}} \sigma \, dt
      \;=\; \frac{s^*}{2}\,\ln\!\frac{d_0^2}{d^2_{\mathrm{ov}}},
$$

and with the circulation-independent strain-race engagement $d^2_{\mathrm{ov}} = d_0^2\,(V_{1,0}/d_0^2)^{2/3}$ the total linear amplification is the power law

$$
  A \;=\; e^{N_e} \;=\; \left(\frac{d_0^2}{V_{1,0}}\right)^{s^*/3}
  \;\approx\; \left(\frac{d_0^2}{V_{1,0}}\right)^{0.27}.
$$

Three consequences for the branch question of the Levi degeneracy conjecture. First, the e-fold count is logarithmic in the core ratio, so within linear theory there is no finite-time three-dimensional runaway during the approach: the perturbation amplification is bounded for every finite core. Second, viscosity tightens the bound further — when the viscous core-growth engagement precedes the strain-race engagement, the amplification is capped at the viscous crossing (numerically $A \approx 6$ at $s^* = 0.8$, $\nu = 10^{-3}$, independent of the core ratio below $10^{-4}$). Third, what the bounded linear amplification does not settle is the fate of perturbations that enter the overlap regime at finite amplitude: the nonlinear stage of the Crow instability drives vortex reconnection, a topology-changing process outside the two-regime model entirely. The three-dimensional escape from the model's regularisation picture therefore requires either large seed perturbations or the nonlinear regime; the linear stage alone degrades the two-dimensional reduction only polynomially in the core ratio.
