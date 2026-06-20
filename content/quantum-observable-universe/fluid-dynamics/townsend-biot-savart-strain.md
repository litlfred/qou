*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The
[Levi degeneracy conjecture](#conj:levi-degeneracy) reduces the
$q \to 1$ Navier–Stokes regularity question to the asymptotic
behaviour of the core aspect ratio
$\kappa^2 = a_\perp^2 / a_\parallel^2 = V_2 / V_1$
at the vortex-collision time $T^\ast$
([prop:core-levi-form](#prop:core-levi-form)).
This remark and its
[hyperbolic-overlap companion](#rem:hyperbolic-overlap-saturation)
work the ODE for $(V_1, V_2)$ explicitly in the two physical
regimes — first under the singular Biot–Savart strain valid
when cores are well separated, then under the hyperbolic
saturation that takes over when the cores overlap.

**Setup.**
Consider two anti-parallel vortex filaments with circulation
$\Gamma$ approaching head-on at a collision time $T^\ast$.
Model the cross-section of each viscous core by the
**Townsend covariance matrix** \cite{townsend1951}:
let $V_1(t)$ be the squared core radius in the direction of
advective stretching, and $V_2(t)$ the squared core radius in
the perpendicular direction of compression. From the
Biot–Savart derivation (Saffman \cite{saffman1992} §11.2; Moffatt–
Kida–Ohkitani \cite{moffatt1994}) the separation squared evolves
as
$$
  d(t)^2 = \frac{c\,\Gamma (T^\ast - t)}{\pi},
$$
with a convention constant $c$ that depends on whether $\Gamma/(2\pi d)$
is read as a single filament's induced velocity ($c = 1$) or as
the relative approach speed of the two filaments ($c = 2$).
Either way the time scaling is the same.
The external strain rate induced by one filament on the other
is then
$$
  \alpha(t)
  \;=\;
  \frac{\Gamma}{2\pi d(t)^2}
  \;=\;
  \frac{1}{2c\,(T^\ast - t)},
$$
and only the constants depend on $c$; the leading behaviour
$\alpha \propto 1/(T^\ast - t)$ is convention-independent. For
definiteness, and to match the user's setup, we adopt $c = 1$
below — the corresponding Lean formalisation
([`townsend-biot-savart-strain.lean`](townsend-biot-savart-strain.lean))
states the result in a $c$-agnostic form.
The remarkable feature is that $\alpha(t)$ is **independent of
$\Gamma$**: under the point-vortex approximation, the
circulation cancels between numerator and denominator and the
strain rate is fixed by the time-to-collision alone.

**Townsend evolution.**
Under axisymmetric viscous strain the squared core radii satisfy
\cite{townsend1951,moffatt1994}
$$
  \frac{dV_1}{dt} = +2\,\alpha(t)\,V_1 + 2\nu,
  \qquad
  \frac{dV_2}{dt} = -2\,\alpha(t)\,V_2 + 2\nu,
$$
with $\nu$ the kinematic viscosity. Let $\tau = T^\ast - t$ be
the time remaining. Then $d/dt = -d/d\tau$ and substituting
$\alpha(t) = 1/(2\tau)$ gives the linear system
$$
  \frac{dV_1}{d\tau} + \frac{V_1}{\tau} = -2\nu,
  \qquad
  \frac{dV_2}{d\tau} - \frac{V_2}{\tau} = -2\nu.
$$

**Exact solutions.**
Using the integrating factor $\tau$ for $V_1$ and $1/\tau$ for
$V_2$:
$$
  \frac{d(\tau V_1)}{d\tau} = -2\nu\tau
  \quad\Longrightarrow\quad
  V_1(\tau) = \frac{C_1}{\tau} - \nu\tau,
$$
$$
  \frac{d(V_2/\tau)}{d\tau} = -\frac{2\nu}{\tau}
  \quad\Longrightarrow\quad
  V_2(\tau) = -2\nu\,\tau\ln\tau + C_2\,\tau,
$$
with constants $C_1, C_2$ fixed by the cross-section at the
start of the close-approach window. As the collision is
approached ($\tau \to 0$):
- the stretching coordinate diverges,
  $V_1(\tau) \sim C_1/\tau \to \infty$,
- the compressing coordinate vanishes,
  $V_2(\tau) \sim -2\nu\,\tau \ln\tau \to 0$.

**The first-order Levi prediction.**
The squared Levi condition number is therefore
$$
  \kappa^2(\tau)
  = \frac{V_2(\tau)}{V_1(\tau)}
  \;\sim\;
  \frac{-2\nu\,\tau^2\ln\tau}{C_1}
  \;\xrightarrow[\tau \to 0]{}\; 0.
$$
At this level of approximation the viscous diffusion completely
flattens the core into a two-dimensional sheet just before
collision. Via
[prop:core-levi-form](#prop:core-levi-form)(c), $\kappa \to 0$
forces the Levi form to be **strictly degenerate** at the
collision locus: the contact eigenvalue
$\lambda_\parallel \to 0$ while $\lambda_\perp$ stays bounded.
The local cohomology group $H^1_{\mathfrak{m}_p}(A)$ vanishes,
the cohomological obstruction dissolves, and the system
maintains global regularity. This is the
[branch (B) outcome](#conj:levi-degeneracy) of the conjecture
— **NS globally regular** — under the point-vortex assumption.

**Where the approximation fails.**
The Biot–Savart strain rate
$\alpha(t) = \Gamma / (2\pi d(t)^2)$ assumes a point-vortex
geometry: the cores are much smaller than the separation,
$V_1 \ll d^2$. But $V_1(\tau) \sim C_1/\tau \to \infty$ as
$\tau \to 0$, whereas $d(\tau)^2 = \Gamma\tau/\pi \to 0$. The
two cross over at a finite $\tau_\ast$ defined by
$V_1(\tau_\ast) = d(\tau_\ast)^2$, after which the filaments
**overlap** and the Biot–Savart kernel is no longer valid: the
strain field near the collision plane is no longer the
superposition of two well-separated circular vortices, but
the merged flow of a single interaction zone. The next
remark — [hyperbolic-overlap saturation](#rem:hyperbolic-overlap-saturation) — computes what the strain field actually does in
the overlap regime, and finds that the apparent flattening
$\kappa \to 0$ is an artefact of the failed approximation.
