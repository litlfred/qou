The [Biot–Savart prediction](#rem:townsend-biot-savart-strain)
that the squared core ratio $\kappa^2 \to 0$ at the collision
holds only while the cores remain well separated. Once the
stretching coordinate $V_1$ reaches the squared separation
$d^2$, the point-vortex kernel breaks down and the local
stream function near the collision plane shifts from the
superposition of two circular vortices to a **hyperbolic
stagnation-point flow** (Saffman \cite{saffman1992} §6.3; Moffatt–
Kida–Ohkitani \cite{moffatt1994}). This remark works the Townsend
ODE in the hyperbolic regime and finds that the apparent
flattening $\kappa \to 0$ is reversed: the squared Levi
condition number **locks** to a strictly positive constant
$\kappa^2 = \pi\nu/\Gamma$.

**Why the kernel changes.**
The singular Biot–Savart strain $\alpha(t) = \Gamma/(2\pi d^2)$
diverges *only* because $d \to 0$ while the cores are held
small. Once $V_1 \gtrsim d^2$ the filaments are no longer two
distinct objects; their merged interaction is described by an
elliptic-section vortex sitting at a hyperbolic stagnation
point of the *macroscopic* flow. In that geometry the strain
rate is bounded by the overlapping cores themselves and the
relevant length scale is no longer $d$ but $\sqrt{V_1}$:
$$
  \alpha(t) \;\longrightarrow\;
  \alpha_{\mathrm{hyp}}(t)
  \;=\;
  \frac{\Gamma}{\pi V_1(t)}.
$$
The kernel rotates from a $1/d^2$ Biot–Savart strain (point-
vortex superposition) to a $1/V_1$ Burgers-like strain
(elliptic vortex in a stagnation flow). This is the standard
"vortex in strain" model of Townsend / Moffatt–Kida–Ohkitani.

**Saturated Townsend system.**
Substituting $\alpha_{\mathrm{hyp}} = \Gamma/(\pi V_1)$ into
the stretching equation,
$$
  \frac{dV_1}{dt}
  = 2\,\alpha_{\mathrm{hyp}}\,V_1 + 2\nu
  = \frac{2\Gamma}{\pi V_1}\cdot V_1 + 2\nu
  = \frac{2\Gamma}{\pi} + 2\nu.
$$
The right-hand side is now a **constant**: $V_1$ grows
linearly with time rather than diverging, and remains finite
through to the formal collision time $T^\ast$. Explicitly,
$$
  V_1(t) \;=\; V_1(t_\ast) +
  \left( \tfrac{2\Gamma}{\pi} + 2\nu \right)(t - t_\ast),
$$
where $t_\ast$ is the time at which the overlap regime
begins. The exponential runaway predicted by the point-vortex
approximation is replaced by a controlled linear growth — the
strain saturates because the same coordinate that drives the
stretching also sets the relevant length scale.

**Compression equilibrium.**
Substituting the same saturated strain into the compression
equation,
$$
  \frac{dV_2}{dt}
  = -2\,\alpha_{\mathrm{hyp}}\,V_2 + 2\nu
  = -\frac{2\Gamma\,V_2}{\pi V_1} + 2\nu.
$$
Because $V_1$ is finite and smoothly increasing, the
compressive sink is bounded and the constant viscous source
$2\nu$ catches it. The core thickness reaches a quasi-steady
equilibrium at $dV_2/dt = 0$, giving
$$
  V_2 \;=\; \frac{\pi\nu V_1}{\Gamma}.
$$
This is the **Burgers vortex equilibrium thickness**, here in
the asymmetric Townsend form: the compressed direction does
not vanish but balances viscous diffusion against hyperbolic
straining at a strictly positive width.

**Levi non-degeneracy is preserved.**
The squared core aspect ratio
$\kappa^2 = V_2/V_1$ at the hyperbolic equilibrium is
$$
  \boxed{\;\;
  \kappa^2
  \;=\;
  \frac{V_2}{V_1}
  \;=\;
  \frac{\pi\nu V_1 / \Gamma}{V_1}
  \;=\;
  \frac{\pi\nu}{\Gamma}.
  \;\;}
$$
The aspect ratio does **not** go to zero. It locks into a
strictly positive constant determined entirely by the ratio
of the classical viscosity to the initial circulation —
**independent of the time-to-collision $\tau$**.

Through
[prop:core-levi-form](#prop:core-levi-form)(b–c), $\kappa^2 > 0$
is equivalent to the Levi form remaining non-degenerate at the
collision locus $\Sigma$: both eigenvalues
$\lambda_\parallel, \lambda_\perp$ stay bounded away from zero.
Therefore the local cohomology group
$H^1_{\mathfrak{m}_p}(A)$ remains non-zero, the cohomological
obstruction is preserved right up to $T^\ast$, and the
[NS obstruction](#def:ns-obstruction) does not dissolve under
the viscous diffusion mechanism the point-vortex picture
seemed to provide. This is the
[branch (A) outcome](#conj:levi-degeneracy) of the conjecture
— **classical 3D Navier–Stokes admits finite-time blowup**.

**The dichotomy in one table.**

| Regime | Strain $\alpha$ | $V_1$ behaviour | $V_2$ behaviour | $\kappa^2$ at $T^\ast$ | Levi form | NS conclusion |
|---|---|---|---|---|---|---|
| Biot–Savart ([`rem:townsend-biot-savart-strain`](#rem:townsend-biot-savart-strain)) | $1/(2\tau)$ | $\sim C_1/\tau \to \infty$ | $\sim -2\nu\tau\ln\tau \to 0$ | $0$ | Degenerate | Regular (branch B) |
| Hyperbolic overlap (this remark) | $\Gamma/(\pi V_1)$ | Linear in $t$, finite at $T^\ast$ | $\pi\nu V_1/\Gamma > 0$ | $\pi\nu/\Gamma$ | Non-degenerate | Blowup (branch A) |

**Reading.**
The Biot–Savart prediction $\kappa \to 0$ is an artefact of
the point-vortex approximation; it never reaches $\tau = 0$
because the approximation breaks down at the overlap time
$\tau_\ast$. The hyperbolic-overlap calculation, valid past
$\tau_\ast$ through to the formal collision, predicts
$\kappa^2 = \pi\nu/\Gamma > 0$ — the cores do **not** flatten
into sheets; they lock into a finite elliptical profile
supported by the hyperbolic strain. The vortex collision
preserves the contact non-degeneracy and the NS obstruction
class is carried intact to $T^\ast$. This is the analytical
bridge that the
[Levi degeneracy conjecture](#conj:levi-degeneracy) calls
for: the geometric obstruction survives the viscous regularity
mechanism, leaving finite-time blowup for the classical
viscous Navier–Stokes system as the expected outcome.

**Caveats.**
1. The hyperbolic strain $\Gamma/(\pi V_1)$ is the
   leading-order Burgers approximation for a strained
   elliptic vortex; corrections of order $V_2/V_1 = \kappa^2$
   appear in the next order and shift the equilibrium by
   $O((\pi\nu/\Gamma)^2)$. For the high-Reynolds regime
   $\nu \ll \Gamma$ — the regime relevant to blowup —
   the correction is small.
2. The Townsend equations assume axisymmetric straining
   *within* the elliptic cross-section. Three-dimensional
   instabilities (Kelvin modes,
   [helical](#rem:helicity-physical) twisting) may modify the
   picture; see
   [`rem:vortex-reconnection`](#rem:vortex-reconnection) for
   the divisor-surgery view of these instabilities.
3. The conclusion "$\kappa^2 > 0 \Rightarrow$ blowup" routes
   through [`prop:core-levi-form`](#prop:core-levi-form),
   which is itself conditional on the regularity-breakdown
   programme (see its conjectural-dependency banner).
   What the explicit ODE establishes rigorously is the
   asymptotic core-shape constant
   $\kappa^2 = \pi\nu/\Gamma$; lifting this to NS blowup
   requires the
   [Levi degeneracy](#conj:levi-degeneracy) and
   [counter-example](#conj:ns-counterexample) conjectures.
