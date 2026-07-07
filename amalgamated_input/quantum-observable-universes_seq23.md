<!-- FILE_START: intro-q-resolvent-wick.md -->
The previous section developed the three linear $q$-transforms — heat,
Laplace, and Fourier — as morphisms in $\mathrm{End}_{\mathbf{C}}(A)$.
This section adds the **resolvent** to that family and shows that the
Laplace and Fourier transforms are two real forms of a single complex
spectral pairing, related by an explicit rotation of the spectral
parameter.

We first define the $q$-resolvent
$R_q(s) = (s + \widehat{\Delta_q})^{-1}$ as a categorical Laplace
transform of the $q$-heat semigroup, then prove existence and
uniqueness in the convolution algebra $\mathcal{H}_q$.  The closing
block collapses the Laplace–Fourier distinction into a single
grouplike pairing against $\exp_q \in G(\mathcal{H}_q)$ evaluated at
either $s$ or $i\xi$.  That identification — the *categorical Wick
rotation* — is the substrate-level prototype of the rotation between
real-time evolution and imaginary-time partition functions that
organises the physical-observation chapter.
<!-- FILE_END: intro-q-resolvent-wick.md -->

<!-- FILE_START: q-resolvent.md -->
Let $\widehat{\Delta_q}$ be the $q$-Laplacian acting on
$\mathrm{End}_{\mathbf{C}}(A)$
([$q$-heat equation](#def:q-heat-equation)), and let
$s \in \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A)$ be a categorical
spectral parameter.  The **$q$-resolvent** is the morphism

$$
  R_q(s) \;=\; \bigl(s + \widehat{\Delta_q}\bigr)^{-1}
  \;\in\; \mathrm{End}_{\mathbf{C}}(A),
$$

defined wherever $s + \widehat{\Delta_q}$ is invertible in the
convolution algebra $\mathcal{H}_q$.  The set of $s$ for which the
resolvent is *not* defined is the categorical spectrum
$\mathrm{Spec}(\widehat{\Delta_q}) \subseteq \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A)$.
<!-- FILE_END: q-resolvent.md -->

<!-- FILE_START: q-resolvent-properties.md -->
This remark collects the Laplace-transform characterisation,
resolvent identity, Peter--Weyl spectral decomposition, base-ring,
and physical realisations of the [$q$-resolvent](#def:q-resolvent).

**Laplace-transform characterisation.**  $R_q(s)$ is the categorical
Laplace transform
([categorical Laplace transform](#def:categorical-laplace)) of the
$q$-heat semigroup $\exp(-t \widehat{\Delta_q})$:

$$
  R_q(s)
  \;=\;
  \mathcal{L}\bigl[\exp(-t \widehat{\Delta_q})\bigr](s)
  \;=\;
  \mathrm{tr}_M\bigl(\exp_q(-s \cdot)  \cdot  \exp(-t \widehat{\Delta_q})\bigr),
$$

so $R_q(s)$ is the spectral-parameter companion of the
$q$-exponential grouplike: pairing $\exp_q(-s\cdot) \in G(\mathcal{H}_q)$
against the heat flow produces the resolvent diagonally.

**Resolvent identity.**  The first resolvent identity holds
categorically:

$$
  R_q(s_1) - R_q(s_2)
  \;=\;
  (s_2 - s_1) R_q(s_1) R_q(s_2),
$$

which is the Hopf-algebraic shadow of the comultiplication axiom on
$\mathcal{H}_q$: the mate of the coproduct $\Delta_q$ under the
Laplace pairing.

**Peter--Weyl spectral decomposition.**  Under the categorical Fourier
transform ([categorical Fourier
transform](#def:categorical-fourier)) with
$G = \mathrm{SU}_q(2)$, the resolvent diagonalises over
irreducibles:

$$
  R_q(s)
  \;=\;
  \bigoplus_{j \in \widehat{G}} \frac{\pi_j}{s + \lambda_j(q)},
$$

where $\lambda_j(q) = [j]_q[j+1]_q (1 - q^{-1})^2$ is the
$j$-isotypic eigenvalue of $\widehat{\Delta_q}$
([Peter--Weyl heat kernel](#prop:q-heat-kernel-peter-weyl)).  The
spectrum is therefore the discrete set
$\{-\lambda_j(q) : j \in \widehat{G}\}$; the resolvent is meromorphic
in $s$ with simple poles at each spectral value.

**Base-ring behaviour.**  As with $\exp_q$ and the Laplace
transform, $R_q(s)$ is defined categorically over any base ring where
$\mathcal{H}_q$ has grouplikes and $s + \widehat{\Delta_q}$ is
invertible in $\mathcal{H}_q$:

- **$\mathbb{F}_p$.**  Invertibility fails when $s \equiv -\lambda_j(q)
  \pmod{p}$ for some $j \le$ cutoff; $R_q(s)$ is defined on the
  Zariski-open complement.  The finite-spectrum description makes the
  resolvent a rational function of $s$ over $\mathbb{F}_p$.
- **$\mathbb{Q}_p$, $\mathbb{C}_p$.**  $R_q(s)$ is rigid-analytic on
  the complement of the $p$-adic spectrum, with the resolvent
  identity holding on the intersection of domains.
- **$\mathbb{C}$ (archimedean).**  Standard operator-theoretic
  resolvent on $L^2(G, \mathrm{Haar}_q)$; the inverse Laplace recovers
  the heat kernel.

**Physical meaning.**  The resolvent is the $s$-domain Green's
function of the $q$-heat flow: given an initial state $u_0$, the
quantity $R_q(s) u_0$ is the Laplace transform of the time evolution
$u(t) = \exp(-t \widehat{\Delta_q}) u_0$.  Contour-integrating
$R_q(s)$ around a pole at $-\lambda_j(q)$ extracts the projector
$\pi_j$ onto the $j$-isotypic subspace — the categorical
analogue of spectral projection via Cauchy's formula.
<!-- FILE_END: q-resolvent-properties.md -->

<!-- FILE_START: q-resolvent-exists.md -->
For $s \in \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A)$ outside the
categorical spectrum of $\widehat{\Delta_q}$, the
[$q$-resolvent](#def:q-resolvent)
$R_q(s) = (s + \widehat{\Delta_q})^{-1}$ exists as an endomorphism of
$\mathrm{End}_{\mathbf{C}}(A)$.

Uniqueness is
([uniqueness of $q$-resolvent](#prop:q-resolvent-unique)).
<!-- FILE_END: q-resolvent-exists.md -->

<!-- FILE_START: q-resolvent-unique.md -->
The [$q$-resolvent](#def:q-resolvent) $R_q(s)$ is the unique morphism
satisfying $(s + \widehat{\Delta_q}) \circ R_q(s) = \mathrm{id}$ on
the domain.  Any two inverses of the same invertible morphism
$s + \widehat{\Delta_q}$ coincide.
<!-- FILE_END: q-resolvent-unique.md -->

<!-- FILE_START: laplace-fourier-wick-rotation.md -->
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
<!-- FILE_END: laplace-fourier-wick-rotation.md -->

