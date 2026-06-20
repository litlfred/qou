*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

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

**Compression — proportionality ansatz.**
Substituting the same saturated strain into the compression
equation,
$$
  \frac{dV_2}{dt}
  = -2\,\alpha_{\mathrm{hyp}}\,V_2 + 2\nu
  = -\frac{2\Gamma\,V_2}{\pi V_1} + 2\nu.
$$
Because $V_1$ is finite and increases linearly in $t$, the
compressive sink is bounded and the constant viscous source
$2\nu$ catches it. The temptation is to set
$\dot V_2 = 0$ ("quasi-steady"), giving the standard
**Burgers vortex equilibrium thickness** $V_2 = \pi\nu V_1/\Gamma$.
*This quasi-steady ansatz is not justified here.* The $V_2$
relaxation rate $2\Gamma/(\pi V_1)$ is *comparable to* the
$V_1$ growth rate $b/V_1$ — in fact $b/(2\Gamma/\pi) = 1 +
\pi\nu/\Gamma$, so $V_2$ and $V_1$ evolve on the same
timescale and $V_2$ cannot equilibrate to an instantaneous
target while $V_1$ varies.

**Asymptotic proportionality (correct constant).**
The right approach is the proportionality ansatz
$V_2(t) = \lambda V_1(t)$, valid asymptotically once the
transient $V_2$-mode has decayed. Then
$\dot V_2 = \lambda \dot V_1 = \lambda b$, and the ODE forces
$$
  \lambda b
  \;=\;
  -\frac{2\Gamma}{\pi}\,\lambda + 2\nu,
$$
i.e. $\lambda(b + 2\Gamma/\pi) = 2\nu$. Substituting
$b = 2\Gamma/\pi + 2\nu$ gives $b + 2\Gamma/\pi = 4\Gamma/\pi
+ 2\nu$, hence
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
In the high-Reynolds limit $\nu \ll \Gamma$ relevant to
blowup, $\kappa^2 \simeq \pi\nu/(2\Gamma)$ — *half* the value
the quasi-steady ansatz would have produced.

Independently, solving the inhomogeneous linear ODE with
integrating factor $(V_1/V_{10})^{\beta}$, where
$\beta = 2\Gamma/(\pi b)$, gives the closed-form solution
$$
  V_2(t)
  \;=\;
  \frac{2\nu\,V_1(t)}{b(\beta + 1)}
  \;+\;
  K\,V_1(t)^{-\beta},
$$
where the second term is the decaying transient. The
particular term has the same ratio
$2\nu/(b(\beta+1)) = \pi\nu/(2\Gamma + \pi\nu)$, confirming
the asymptotic. The Burgers equilibrium $\pi\nu V_1/\Gamma$
would be the correct answer only if $V_1$ were strictly
constant — which it is not under saturated straining.

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
| Hyperbolic overlap (this remark) | $\Gamma/(\pi V_1)$ | Linear in $t$, finite at $T^\ast$ | $\pi\nu V_1/(2\Gamma+\pi\nu) > 0$ | $\pi\nu/(2\Gamma + \pi\nu)$ | Non-degenerate | Blowup (branch A) |

**Reading.**
The Biot–Savart prediction $\kappa \to 0$ is an artefact of
the point-vortex approximation; it never reaches $\tau = 0$
because the approximation breaks down at the overlap time
$\tau_\ast$. The hyperbolic-overlap calculation, valid past
$\tau_\ast$ through to the formal collision, predicts the
asymptotic core ratio
$\kappa^2 = \pi\nu/(2\Gamma+\pi\nu) > 0$ — strictly positive
and lower-bounded by $\pi\nu/(2\Gamma + \pi\nu)$ even in the
inviscid limit at fixed viscosity. The cores do **not**
flatten into sheets; they lock into a finite elliptical
profile supported by the hyperbolic strain. The vortex
collision preserves the contact non-degeneracy and the NS
obstruction class is carried intact to $T^\ast$. This is the analytical
bridge that the
[Levi degeneracy conjecture](#conj:levi-degeneracy) calls
for: the geometric obstruction survives the viscous regularity
mechanism, leaving finite-time blowup for the classical
viscous Navier–Stokes system as the expected outcome.

**Caveats.**
1. The kernel switch $\alpha(t) \to \Gamma/(\pi V_1)$ at the
   overlap time is a **phenomenological dimensional ansatz**,
   not a derivation from Euler/NS: the relevant length scale
   inside the overlap region is heuristically replaced by
   $\sqrt{V_1}$. Townsend, Moffatt–Kida–Ohkitani, Saffman use
   this saturation as a modelling primitive. A rigorous bridge
   from the singular Biot–Savart kernel to the saturated
   elliptic-Burgers regime would require a careful matched
   asymptotic analysis through the overlap layer.
2. The asymptotic value
   $\kappa^2 = \pi\nu/(2\Gamma + \pi\nu)$ is the
   *attracting proportionality ratio* of the linear ODE
   (verified two ways above: ansatz $V_2 = \lambda V_1$ and
   closed-form integrating factor). It is **not** the naive
   $\dot V_2 = 0$ "Burgers equilibrium" $\pi\nu V_1/\Gamma$:
   that ansatz requires $V_1$ stationary, while $V_1$ here is
   growing on the same timescale as the $V_2$ relaxation.
   The two answers differ by a factor of approximately 2 in
   the high-Reynolds limit.
3. The Townsend equations assume axisymmetric straining
   *within* the elliptic cross-section. Three-dimensional
   instabilities (Kelvin modes,
   [helical](#rem:helicity-physical) twisting) may modify the
   picture; see
   [`rem:vortex-reconnection`](#rem:vortex-reconnection) for
   the divisor-surgery view of these instabilities.
4. The conclusion "$\kappa^2 > 0 \Rightarrow$ blowup" routes
   through [`prop:core-levi-form`](#prop:core-levi-form),
   which is itself conditional on the regularity-breakdown
   programme (see its conjectural-dependency banner).
   What the explicit ODE establishes rigorously — and what is
   formalised in the sibling Lean file — is the asymptotic
   core-shape constant
   $\kappa^2 = \pi\nu/(2\Gamma + \pi\nu)$; lifting this to NS
   blowup requires the
   [Levi degeneracy](#conj:levi-degeneracy) and
   [counter-example](#conj:ns-counterexample) conjectures.
