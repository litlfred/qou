Let $(\mathbf{C}, A, \tau)$ isolate a valid QOU bearing $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$ constrained by $\mathrm{tr}(\kappa_0) = \chi(A)$.

The strict Kummer exact sequence evaluated at any integer $n \geq 1$:

$$
  1 \to \mu_n \to \mathbb{G}_m
  \xrightarrow{(\cdot)^n} \mathbb{G}_m \to 1
$$

forces a long exact sequence mapping through cohomology:

$$
  H^2(\mathcal{S}, \mu_n)
  \to H^2(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{\cdot n}
  H^2(\mathcal{S}, \mathbb{G}_m)
  \to H^3(\mathcal{S}, \mu_n).
$$

The [specialisation driving $q = 1$](#rem:substrate-gm-torsion) projects cleanly:

$$
  \kappa_0 \mapsto
  \kappa_0 \bmod n
   \in 
  H^2(\mathcal{S}, \mathbb{G}_m) / nH^2(\mathcal{S}, \mathbb{G}_m).
$$

This resulting class safely avoids zero if and only if $\kappa_0$ fundamentally **resists** $n$-divisibility.

**(a) Divisibility of the Euler class.**

Constrained over a closed orientable surface $\Sigma_g$ anchored at genus $g$: $H^2(\Sigma_g, \mathbb{Z}) \cong \mathbb{Z}$. The bare Euler class scales as $e(\xi) = \chi(A) \in \mathbb{Z}$. Therefore:

$$
  \kappa_0 \bmod n = 0
  \quad\Longleftrightarrow\quad
  n \mid \chi(A).
$$

Applied to the Descartes universe at $\chi(A) = -6$, the valid divisors restrict strictly to $\{1, 2, 3, 6\}$. $\kappa_0 \bmod n$ mathematically zeroes out only spanning $n \in \{1, 2, 3, 6\}$. It rigorously evades zero for all other $n$ (verifiably holding for $n = 5, 7, 11, 13, \ldots$).

**(b) Obstruction persistence.**

Evaluating at the root of unity $q = e^{i\pi/\kappa}$, the operating Kummer level isolates strictly to $n = 2\kappa$ (reflecting the exact order mapping $q$ inside $\mathbb{G}_m$). The functional obstruction $\kappa_0 \bmod 2\kappa$ reduces to:

$$
  \kappa_0 \bmod 2\kappa = 0
  \quad\Longleftrightarrow\quad
  2\kappa \mid \chi(A).
$$

For $\chi(A) = -6$, $2\kappa \mid 6$ permits exclusively $\kappa \in \{1, 3\}$, corresponding to $q = e^{i\pi}$ or $q = e^{i\pi/3}$. At every other valid $\kappa$ (universally capturing all $\kappa \geq 4$), the obstruction fundamentally **persists** squarely at that root of unity.

**(c) The limit as kappa goes to infinity.**

Pushing $\kappa \to \infty$ ($q \to 1$) forces $2\kappa \to \infty$. Consequently, $2\kappa \nmid 6$ governs unconditionally for all $\kappa \geq 4$. The math yields:

$$
  \kappa_0 \bmod 2\kappa  \neq  0
  \qquad\text{for all } \kappa \geq 4.
$$

The topological component driving the NS obstruction **rigorously avoids vanishing** through the $q \to 1$ classical limit.

**(d) Formal statement.**

Evaluated against any QOU possessing $\chi(A) \neq 0$:

1. The exact specialisation $\kappa_0|_{q=1}$ rigidly avoids zero within $H^2(\mathcal{S}, \mathbb{G}_m)/n$ universally for all integers $n \nmid \chi(A)$.
2. The integer set $\{n : n \nmid \chi(A)\}$ strictly extends to infinity (safely encompassing all primes avoiding $\chi(A)$). The overall obstruction must remain **persistently nonzero** structurally piercing infinitely many levels inside the Kummer tower.
3. The absolute obstruction zeroes out exclusively at the finite, isolated Kummer levels matching $n \mid \chi(A)$. These align perfectly with the finite set of roots of unity where the category's truncation operates compatibly alongside the fixed Euler class.

**(e) Consequence for NS regularity.**

A valid QOU constrained by $\chi(A) = -6$ universally executes as **NS-singular**: $\mathrm{Obs}_\partial(A) = 0$. The boundary observability systematically vanishes. The classical Navier--Stokes equation inherently permits finite-time blowup.

This result stems absolutely from (e) bonded to the [complementary-subgroup argument](#thm:qu-to-qou) (item 3). The core topological obstruction $e(\xi)|_\Sigma \neq 0$ lacks any mathematical channel to suffer cancellation against the operative analytic correction $\delta_n|_\Sigma$. They strictly populate complementary summands inside $H^2(\mathcal{S}, \mathbb{G}_m)$.
