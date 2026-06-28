The categorical Laplace
([categorical Laplace transform](#def:categorical-laplace)) and
categorical Fourier
([categorical Fourier transform](#def:categorical-fourier))
transforms are **two real forms of a single complex spectral
pairing**. Both are defined by pairing against the $q$-exponential
grouplike $\exp_q \in G(\mathcal{H}_q)$ ([$q$-exponential](#def:q-exponential));
they differ only in which character of the Reeb-translation object
one evaluates:

$$
  \mathcal{L}[f](s) \;=\; \mathrm{tr}_M\bigl(\exp_q(-s\cdot) \cdot f\bigr),
  \qquad
  \mathcal{F}[f](\xi) \;=\; \mathrm{tr}_M\bigl(\exp_q(i\xi\cdot) \cdot f\bigr).
$$

Setting $s = -i\xi$ (equivalently $\xi = is$) identifies them:

$$
  \boxed{\;\mathcal{F}[f](\xi) \;=\; \mathcal{L}[f](i\xi)\;}
$$

— the *categorical Wick rotation*. The two transforms are related
by an automorphism of the spectral plane (rotation by $\pi/2$) acting
on the single abstract grouplike.

**Structural picture.**

| Side | Grouplike | Flow equation | Physics |
|------|-----------|---------------|---------|
| Laplace (real) | $\exp_q(-s\cdot)$ | $\partial_t u = \Delta_q u$ | Heat / dissipation |
| Fourier (imag.) | $\exp_q(i\xi\cdot)$ | $i\partial_t u = \Delta_q u$ | Schrödinger / oscillation |

The heat equation
([$q$-heat equation](#def:q-heat-equation)) and the Schrödinger-type
jet-coaction equation
([Schrödinger jet coaction](#rem:schrodinger-jet-coaction))
are **sibling dynamics** — the two real slices of a single complex
evolution $(\partial_\tau - \Delta_q) u = 0$ with
$\tau = t + i\varTheta$, a complex Reeb-time.

**Exchanges under Wick rotation.**

1. **Heat kernel $\leftrightarrow$ propagator.** The $q$-heat kernel
 $K_q(t; x, y)$ and the Schrödinger propagator
 $P_q(t; x, y)$ satisfy $P_q(t) = K_q(it)$ as formal objects in
 the complex time plane.
2. **Gaussian $\leftrightarrow$ plane wave.** The Reeb-invariant $q$-Gaussian
 ([$q$-Gaussian solves the $q$-heat equation](#prop:q-gaussian-solves-q-heat))
 becomes a plane-wave ansatz under $t \mapsto it$; the variance
 $\sigma^2 = t/q^2$ becomes an imaginary "spread" — the phase of a
 stationary wave packet.
3. **Laplace poles $\leftrightarrow$ Fourier spectrum.** The resolvent poles of
 $\mathcal{L}$ at $s = -\mu_\lambda(q)$
 ([Peter--Weyl heat kernel](#prop:q-heat-kernel-peter-weyl)) become,
 under $s \to i\xi$, the continuous Fourier spectrum
 $\xi_\lambda = i\mu_\lambda(q)$ — complex eigenvalues of the
 non-self-adjoint Schrödinger evolution.

**Base-ring independence of Wick rotation.** Because Wick rotation
acts only on the spectral parameter (not on the grouplike itself),
it is meaningful in *any* base ring in which $i$ (a primitive fourth
root of unity) exists: over $\mathbb{C}$ by definition, over
$\mathbb{F}_p$ when $p \equiv 1 \pmod{4}$, over $\mathbb{Q}_p$ for
the same primes. In finite-field realisations, the Laplace--Fourier
duality becomes a concrete symmetry of character tables under
Frobenius twists.

**Role in the $q$-heat story.** Wick rotation says: *everything we
derive about the $q$-heat equation — the Reeb-invariant Gaussian,
the Peter--Weyl spectral decomposition, the Mercer kernel, the
content-Casimir eigenvalues $\mu_\lambda(q)$ — has a mirror
statement about the quantum-mechanical $q$-Schrödinger evolution,
obtained by $t \mapsto it$*. Together they are the full analytic
shadow of the single Hopf-algebraic object $\exp_q \in G(\mathcal{H}_q)$.
