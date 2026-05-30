**Conjecture (next-order Faddeev WKB gives the categorical Green's function).**
*Let $q$ be the substrate parameter and $\hbar_q = 1 - q^{-1}$ the
quantum Planck constant. Under the joint Faddeev scaling $q \to 1$, $n \to \infty$, $n|1-q| \to \infty$ of
[the archimedean limit conjecture](#conj:dilogarithm-archimedean-limit),
the partial product $\Phi_n(x; q)$
([$q$-Pochhammer partial product](#def:q-pochhammer-partial-product))
admits a stationary-phase expansion at the dominant saddle $x_0$ of
the form*

$$
  \Phi_n(x; q)
  \;\sim\;
  \exp\!\Bigl(
    \hbar_q^{-1} S_0(x_0)
    + S_1(x_0)
    + \hbar_q \, S_2(x_0)
    + \cdots
  \Bigr),
$$

*where the leading term is the classical dilogarithm,*

$$
  S_0(x_0)  =  \mathrm{Li}_2(x_0)
  \qquad \text{(} = \text{[archimedean limit](#conj:dilogarithm-archimedean-limit)}\text{),}
$$

*and the next-to-leading term is the half-log-determinant of the
[categorical Dirac operator](#def:categorical-dirac-operator)
$\mathfrak{D}_\nabla = q^{-1}\nabla + \hbar_q \, \iota_\xi \nabla$
restricted to the
[categorical-instanton moduli](#def:categorical-instanton) at
$x_0$:*

$$
  \boxed{\;
  S_1(x_0)
  \;=\;
  -\tfrac{1}{2} \log \det\!\bigl(\mathfrak{D}_\nabla\big|_{x_0}\bigr).
  \;}
$$

*Equivalently, the
[archimedean realization](#def:archimedean-realization-functor)
$\tau_{\mathrm{arch}}$ of the one-loop fluctuation factor
$\exp S_1(x_0)$ is the two-point Green's function of $\mathfrak{D}_\nabla$
evaluated at the corresponding hyperbolic cusp:*

$$
  \tau_{\mathrm{arch}}\!\bigl(\exp S_1(x_0)\bigr)
  \;=\;
  G_\nabla(x_0)
  \;:=\;
  \langle  \mathfrak{D}_\nabla^{-1}  \rangle_{x_0}.
$$

## Saddle-point story

Taking logs inside the partial product,

$$
  \log \Phi_n(x; q)
  \;=\;
  -\!\sum_{k=0}^{n-1} \log\!\bigl(1 - x q^k\bigr).
$$

After the [archimedean limit](#conj:dilogarithm-archimedean-limit)
extracts $\mathrm{Li}_2(x_0)/\hbar_q$ as the leading saddle phase, the
remaining stationary-phase Gaussian integral around $x_0$ produces a
prefactor

$$
  \int \!\! \exp\!\Bigl(\!-\tfrac{1}{2\hbar_q}
    \Phi^{\prime\prime}(x_0)(x - x_0)^2\Bigr) dx
  \;=\;
  \sqrt{\frac{2\pi \hbar_q}{\Phi^{\prime\prime}(x_0)}}.
$$

The second derivative of the action at the saddle is the Hessian of
the categorical action $S_q[\nabla]$ restricted to the instanton
moduli — and, by the
[categorical Yang–Mills variational principle](#def:categorical-instanton),
this Hessian *is* the [categorical Dirac operator](#def:categorical-dirac-operator)
$\mathfrak{D}_\nabla$ acting on the tangent space at $\nabla$. Hence

$$
  S_1(x_0)
  \;=\;
  -\tfrac{1}{2} \log \Phi^{\prime\prime}(x_0)
  \;=\;
  -\tfrac{1}{2} \log \det\!\bigl(\mathfrak{D}_\nabla\big|_{x_0}\bigr).
$$

The one-loop log-determinant is, by standard heat-kernel
regularisation, the trace-log of the propagator: $-\tfrac{1}{2}\log\det
\mathfrak{D}_\nabla = -\tfrac{1}{2}\mathrm{tr}\log \mathfrak{D}_\nabla$,
whose functional derivative w.r.t.\ the connection is the diagonal of
$\mathfrak{D}_\nabla^{-1}$ — the Green's function.

## One algebraic object, two analytic outputs

The conjecture sharpens the Φ$_q$ (product form) vs
$-\mathrm{Li}_2^q(-z)$ (Kashaev integration limit) split: the same
algebraic state $\Phi_n(x; q_0)$ produces *both* of the
geometric features required for an observable QFT, separated cleanly
by their order in $\hbar_q$:

| WKB order | Symbol | Archimedean output | Role |
|-----------|--------|-------------------|------|
| $\hbar_q^{-1}$ | $S_0 = \mathrm{Li}_2(x_0)$ | Bloch–Wigner volume $D(z)$ | classical action / CS phase |
| $\hbar_q^{0}$ | $S_1 = -\tfrac{1}{2}\log\det \mathfrak{D}_\nabla$ | Green's function $G_\nabla(x_0)$ | one-loop propagator |
| $\hbar_q^{+1}$ | $S_2$ | curvature corrections | higher-loop |

For force-carrier torus knots $T_{m,n}$ the
$S_0$ piece evaluated at the corresponding flat-$\mathrm{SU}(2)$
critical point recovers the classical Chern–Simons invariant
(see [Chern–Simons as knot invariant](#rem:chern-simons-as-knot-invariant))

$$
  \mathrm{CS}(T_{m,n})
  \;=\;
  \frac{\pi^2 (m^2 - 1)(n^2 - 1)}{12\,m\,n}
$$

via Faddeev–Kashaev (the imaginary half of the volume conjecture, since
$\mathrm{Vol}(T_{m,n}) = 0$); the $S_1$ piece supplies the matching
one-loop propagator factor of the same algebraic state.

## Why it is conjectural

Beyond the open ingredients of the
[archimedean limit conjecture](#conj:dilogarithm-archimedean-limit),
the $S_1$ statement requires:

1. **Uniform stationary-phase control.** Standard stationary-phase
   gives the prefactor pointwise at $x_0$; the conjecture asserts the
   asymptotic is uniform in a neighbourhood of $x_0$ along Faddeev's
   joint scaling, strong enough to commute with $\tau_{\mathrm{arch}}$.

2. **Determinant–propagator identification.** The identification
   $-\tfrac{1}{2}\log\det\mathfrak{D}_\nabla \mapsto G_\nabla$ uses a
   choice of heat-kernel / zeta-function regularisation. The
   conjecture asserts that the regularisation prescription that makes
   the adelic-product structure
   ([adelic substrate](#def:adelic-substrate)) hold on the algebraic
   side selects the same regularisation that makes
   $G_\nabla$ the diagonal of $\mathfrak{D}_\nabla^{-1}$ on the
   archimedean side — equivalently, that the local-global compatibility
   of the Arakelov pairing is preserved at $S_1$ order.

3. **Mathlib infrastructure.** A complete Lean proof needs heat-kernel
   determinant theory and stationary-phase asymptotics — neither
   currently in Mathlib. The conjecture is packaged as the typeclass
   `QOU.QPochhammer.WKBGreensFunction`, extending
   `QOU.QPochhammer.ArchimedeanLimit` with one additional field
   stating the $\hbar_q^0$ stationary-phase identity.

## Why this matters

The categorical Green's function $G_\nabla$ is the kernel that controls
the exponential decay of correlations in the categorical action — i.e.,
the mass-gap statement
([Yang–Mills surreal bound](#rem:yang-mills-surreal-bound)). The
$S_0 \leftrightarrow S_1$ split exhibited here is the structural
reason both the
Chern–Simons phase ([Chern–Simons as knot invariant](#rem:chern-simons-as-knot-invariant)) and the
mass-gap propagator emerge from a *single* algebraic state $\Phi_n(x;
q_0)$ at $q = q_0$ — without separately postulating a metric. The
Φ_q-piece [`def:phi-q-piece`](#def:phi-q-piece) thus carries both the
geometry (S_0) and the metric (S_1) of the corresponding hyperbolic
brane configuration; they are the leading and subleading analytic
shadows of the same algebraic datum, related by the WKB hierarchy in
$\hbar_q$.
