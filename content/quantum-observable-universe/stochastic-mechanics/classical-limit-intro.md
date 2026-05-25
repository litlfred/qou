The preceding sections established that the algebraic substrate is
unconditionally stable at the $q$-scale: the Hasse--Weil bound
guarantees that all Frobenius eigenvalues lie on the critical circle
$|\alpha_i| = q^{1/2}$, and the Reeb spectrum inherits this alignment
through the spectral coordinate mapping. The substrate-side
prime-counting estimate holds with the optimal square-root
error term --- a finite-field Riemann hypothesis, proven, not
conjectured.

We now ask what happens when we pass to the macroscopic continuum.
The classical limit $q \to 1$ collapses the quantum gap
$\hbar_q \to 0$, smooths the Jackson $q$-derivative into the ordinary
derivative, and degrades the braided tensor category into a symmetric
one. The local $q$-geometries at each prime fiber glue into an adelic
global object --- the classical Riemann zeta function $\zeta(s)$.
Whether the macroscopic continuum inherits the stability of the
$q$-scale is precisely the content of the Riemann hypothesis.

**Skeleton of this section.** The remaining results below all
share one piece of machinery: the
[surreal rate calculus](#prop:surreal-rate-calculus). Treating
the Reeb infinitesimal $\varepsilon$
([Reeb infinitesimal](#def:reeb-epsilon))
as a strictly positive infinitesimal in the ordered field
$\mathbb{R}(\varepsilon) \subset \mathbf{No}$, we obtain two
categorical invariants of the rigid braided monoidal substrate,

$$
  \Delta_q \;\asymp\; \varepsilon^3
  \qquad\text{(mass-gap dissipation, infinitesimal),}
$$
$$
  \Omega_q \;\asymp\; \varepsilon^{-1}
  \qquad\text{(Reeb period, transfinite),}
$$

and the [surreal squeeze](#lem:surreal-squeeze)
$\delta^2 \cdot \Omega_q > \Delta_q$ holds strictly for every
standard real $\delta > 0$. Each of the millennium-problem
remarks below
([RH](#rem:rh-surreal-bound),
[BSD](#rem:bsd-surreal-bound),
[Yang--Mills](#rem:yang-mills-surreal-bound),
[NS](../fluid-dynamics/ns-surreal-bound.md),
[Collatz](#rem:collatz-surreal-bound),
[P vs NP](#rem:p-vs-np-surreal-bound))
fits this same template: identify the "drift" $\delta$ proper to
the problem, then apply the squeeze. The
[adelic--Tate squeeze](#rem:adelic-tate-squeeze) refines the
inequality place-by-place; the
[unification remark](#rem:millennium-unification) collects the
six instantiations side by side.
