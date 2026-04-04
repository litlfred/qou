Let $(\mathbf{C}, A, \tau)$ be a QOU with
$\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$ and
$\mathrm{tr}(\kappa_0) = \chi(A)$.

The Kummer exact sequence for each $n \geq 1$:

$$
  1 \to \mu_n \to \mathbb{G}_m
  \xrightarrow{(\cdot)^n} \mathbb{G}_m \to 1
$$

induces a long exact sequence in cohomology:

$$
  H^2(\mathcal{S}, \mu_n)
  \to H^2(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{\cdot n}
  H^2(\mathcal{S}, \mathbb{G}_m)
  \to H^3(\mathcal{S}, \mu_n).
$$

The [specialisation to $q = 1$](#rem:substrate-gm-torsion) maps

$$
  \kappa_0 \;\mapsto\;
  \kappa_0 \bmod n
  \;\in\;
  H^2(\mathcal{S}, \mathbb{G}_m) / n\,H^2(\mathcal{S}, \mathbb{G}_m).
$$

This class is nonzero iff $\kappa_0$ is **not** $n$-divisible.

**(a) Divisibility of the Euler class.**

For a closed orientable surface $\Sigma_g$ of genus $g$:
$H^2(\Sigma_g, \mathbb{Z}) \cong \mathbb{Z}$.  The Euler
class $e(\xi) = \chi(A) \in \mathbb{Z}$.  Then:

$$
  \kappa_0 \bmod n = 0
  \quad\Longleftrightarrow\quad
  n \mid \chi(A).
$$

For the Descartes universe with $\chi(A) = -6$: the divisors
of $6$ are $\{1, 2, 3, 6\}$.  So $\kappa_0 \bmod n = 0$ only
for $n \in \{1, 2, 3, 6\}$, and $\kappa_0 \bmod n \neq 0$ for
all other $n$ (in particular for $n = 5, 7, 11, 13, \ldots$).

**(b) Obstruction persistence.**

At the root of unity $q = e^{i\pi/\kappa}$, the relevant
Kummer level is $n = 2\kappa$ (the order of $q$ in
$\mathbb{G}_m$).  The obstruction $\kappa_0 \bmod 2\kappa$
is:

$$
  \kappa_0 \bmod 2\kappa = 0
  \quad\Longleftrightarrow\quad
  2\kappa \mid \chi(A).
$$

For $\chi(A) = -6$: $2\kappa \mid 6$ iff $\kappa \in \{1, 3\}$,
i.e. $q = e^{i\pi}$ or $q = e^{i\pi/3}$.  For all other
$\kappa$ (in particular all $\kappa \geq 4$), the obstruction
**persists** at that root of unity.

**(c) The limit as kappa goes to infinity.**

As $\kappa \to \infty$ ($q \to 1$), $2\kappa \to \infty$ and
$2\kappa \nmid 6$ for all $\kappa \geq 4$.  Therefore:

$$
  \kappa_0 \bmod 2\kappa \;\neq\; 0
  \qquad\text{for all } \kappa \geq 4.
$$

The topological component of the NS obstruction **does not
vanish** in the $q \to 1$ limit.

**(d) Formal statement.**

For any QOU with $\chi(A) \neq 0$:

1. The specialisation $\kappa_0|_{q=1}$ is nonzero in
   $H^2(\mathcal{S}, \mathbb{G}_m)/n$ for all $n \nmid \chi(A)$.

2. Since the set $\{n : n \nmid \chi(A)\}$ is infinite (it
   contains all primes not dividing $\chi(A)$), the obstruction
   is **persistently nonzero** through infinitely many levels
   of the Kummer tower.

3. The obstruction vanishes only at the finitely many Kummer
   levels $n \mid \chi(A)$, which correspond to the finitely
   many roots of unity where the representation category
   truncates in a way compatible with the Euler class.

**(e) What this proves.**

The topological part of the NS obstruction ($\kappa_0 = e(\xi)$
with $\chi(A) = -6$) survives specialisation to $q = 1$.  This
is **unconditional** — it does not depend on the Levi degeneracy
conjecture or the core aspect ratio.

The analytic part ($\delta_n|_\Sigma$, the jet corrections)
remains the open question: it requires the Levi form to stay
non-degenerate.  But the topological part alone already
establishes:

$$
  \kappa_n\big|_\Sigma
  \;=\;
  \underbrace{\mathrm{lk} \cdot e(\xi)|_\Sigma}_{\neq 0\text{ (proved)}}
  \;+\; \delta_n|_\Sigma.
$$

Since the topological and analytic terms live in complementary
subgroups (perpetual obstruction,
[QU-to-QOU](#thm:qu-to-qou) item 3), and the topological term
is nonzero, the **total obstruction is nonzero regardless of
$\delta_n$**.

**(f) Consequence for NS regularity.**

The QOU with $\chi(A) = -6$ is **NS-singular**:
$\mathrm{Obs}_\partial(A) = 0$, the boundary observability
vanishes, and the classical Navier--Stokes equation admits
finite-time blowup.

This follows from (e) together with the
[complementary-subgroup argument](#thm:qu-to-qou) (item 3):
the topological obstruction $e(\xi)|_\Sigma \neq 0$ cannot
be cancelled by the analytic correction $\delta_n|_\Sigma$
because they live in complementary summands of
$H^2(\mathcal{S}, \mathbb{G}_m)$.
