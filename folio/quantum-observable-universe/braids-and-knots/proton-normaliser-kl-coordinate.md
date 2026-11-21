**Conjecture.** Let $x_- \in H_2(q)$ be the sign quasi-idempotent and let $\mathrm{tr}_z$ be the Markov trace with $\mathrm{tr}_z(\sigma_1) = z$. Then $t(z) = \mathrm{tr}_z(x_-)$ vanishes at the convention-D point $z_D = q^3/(q^2+1)$. Reparametrise the family by $c = \mathrm{tr}_z(b)$ for an element $b = u\,\sigma_1 + v$ of $H_2$. The conjecture is that the factor $q^{-3}$ in the normaliser $c_{\mathrm{sign}} = [3]_q!\,q^{-3}$ of [the Borromean observable](f-bor-borromean-observable.md) equals $-\partial_c t$ at $z_D$, where $b$ satisfies:

1. $b$ and $1$ span $H_2$ over $\mathbb{Z}[q, q^{-1}]$, that is, $u$ is a unit of $\mathbb{Z}[q, q^{-1}]$;
2. $b$ is fixed by the [bar involution](bar-involution.md) $\sigma_1 \mapsto \sigma_1^{-1}$, $q \mapsto q^{-1}$.

**What is proved.** The elements satisfying (1) and (2) are exactly $b = \pm(\sigma_1 - q) + c$ with $c$ bar-invariant. For these, $-\partial_c t(z_D) = \pm q^{-3}$. Each condition is needed. Condition (1) alone allows $u = q^m$ for every $m \in \mathbb{Z}$, which gives $\pm q^{-3-m}$. Condition (2) alone allows $u = [2]_q$, which gives $q^{-3}/[2]_q$. The same rule applied to the trivial quasi-idempotent $x_+$, whose trace vanishes at $z_+ = -1/(q^3+q)$, gives derivative $q^3$. That is the $q$-power of the trivial Schur element $c_{\mathrm{triv}} = q^3\,[3]_q!$. So in these coordinates both linear Schur elements equal $\pm$(derivative)$\cdot[3]_q!$.

**What is open.** No axiom requires the trace family to be read in a coordinate satisfying (1) and (2). Both ingredients are defined: the bar involution, and the integral form $\mathbb{Z}[q, q^{-1}]$ over which traces are evaluated. The step that is not established is that the observable's normaliser is computed in such a coordinate. Deriving it would need a principle that observables factor through the integral, bar-symmetric form, which is not on record.

The Lean sibling states conditions (1) and (2) as a class and derives $u = \pm 1$ from them.
