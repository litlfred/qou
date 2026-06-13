Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal
([Reeb infinitesimal](#def:reeb-epsilon))
and let $q = 1 + \varepsilon$
([$q$ from $\varepsilon$](#def:q-from-epsilon))
be the associated substrate parameter.  Work inside the ordered field
$\mathbb{R}(\varepsilon)$ of rational functions of $\varepsilon$, and
treat $\varepsilon$ as a **strictly positive infinitesimal**: for every
standard real $\lambda > 0$ and every $n \in \mathbb{N}$,
$n \cdot \varepsilon < \lambda$.

Equivalently, via the surreal appendix
([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon),
[surreal blow-up calculus](#def:surreal-blowup-calculus)),
$\varepsilon = 1 / \omega$ inside Conway's surreal field $\mathbf{No}$.
The asymptotic symbols $\asymp$, $O(\cdot)$, $o(\cdot)$, $\Theta(\cdot)$
below are the surreal-valuation forms of
[Big-O surreal](#rem:conway-normal-form) — equality up to a standard-real
prefactor (for $\asymp$) or leading-exponent comparison (for the others).

**Rate table.** Each scaling law of the classical-limit degenerations
of
[collapse of the quantum gap](#thm:quantum-gap-collapse)
has a literal value as an element of $\mathbb{R}(\varepsilon) \subset \mathbf{No}$:

| Classical-limit quantity | Surreal value | Order in $\varepsilon$ |
|---|---|---|
| Mass gap $\Delta_q$ of the $q$-Laplacian | $\asymp \tfrac{1}{2}\,\varepsilon^3$ | $+3$ (positive infinitesimal) |
| Reeb period $\Omega_q$ | $\asymp \varepsilon^{-1}$ | $-1$ (positive transfinite) |
| Enstrophy ceiling (fluid-dynamics $\S 3$) | $\asymp \varepsilon^{-4/3}$ | $-4/3$ (transfinite) |
| Rogue-zero energy cost $E(\delta)$ for standard $\delta > 0$ | $\asymp \delta^2 \cdot \varepsilon^{-1}$ | $-1$ (transfinite scaled by $\delta^2$) |

Here $\asymp$ means "equal up to a strictly positive standard-real
prefactor", so the **order** of each quantity in $\varepsilon$ is an
invariant of the substrate, independent of normalization conventions.

**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Surreal rate calculus").** *In $\mathbb{R}(\varepsilon)$,
the following strict inequalities hold:*

1. *Positivity:* $\Delta_q > 0$ and $\Omega_q > 0$.
2. *Infinitesimal gap:* $\Delta_q < \lambda$ for every standard
   real $\lambda > 0$.
3. *Transfinite period:* $\Omega_q > \lambda$ for every standard
   real $\lambda > 0$.
4. *Squeeze (see
   [surreal squeeze](#lem:surreal-squeeze)):*
   *for every standard real $\delta > 0$, $\delta^2 \cdot \Omega_q > \Delta_q$
   strictly in $\mathbb{R}(\varepsilon)$.*

**Proof.** All four claims reduce to order comparisons in
$\mathbb{R}(\varepsilon)$.  Items (1)--(3) are immediate from
the definitions and the positivity / archimedean-smallness of
$\varepsilon$
([Reeb infinitesimal](#def:reeb-epsilon)).
For item (4), since $\delta^2$ is a strictly positive standard real
and $\varepsilon^{-1} - \varepsilon^3$ is strictly positive in the
ordered field (its leading term $\varepsilon^{-1}$ dominates any
positive infinitesimal), we have

$$
\delta^2 \cdot \varepsilon^{-1} - \varepsilon^3
 =  \varepsilon^{-1}\bigl(\delta^2 - \varepsilon^4\bigr) > 0,
$$

because $\delta^2$ is a *standard real* and $\varepsilon^4$ is
infinitesimal, so $\delta^2 - \varepsilon^4 > 0$ in
$\mathbb{R}(\varepsilon)$.  $\square$

**Interpretation.** Item (4) is the mechanism underlying every
millennium-problem squeeze in Chapter~8 and Chapter~7: the "cost" of
any standard-scale perturbation (a rogue zero off the critical line,
a rogue vortex spike, a rogue Collatz trajectory, a rogue oracle
separation) **strictly exceeds** the available mass-gap dissipation.
The cost is transfinite, the dissipation is infinitesimal; no cancellation
is possible in an ordered field.

This is the algebraic content that replaces the informal
"$O(\varepsilon^{-1})$ exceeds $O(\varepsilon^3)$ as $\varepsilon \to 0$":
we do not need a limit, only an inequality inside $\mathbf{No}$.
