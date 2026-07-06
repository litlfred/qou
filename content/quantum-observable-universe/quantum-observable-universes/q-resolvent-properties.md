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
