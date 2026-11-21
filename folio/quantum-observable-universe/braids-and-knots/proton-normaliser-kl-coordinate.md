**Conjecture (retired 2026-11-21).** Let $x_- = \sum_{w \in S_3} (-q)^{-\ell(w)}\,\sigma_w \in H_3(q)$ be the sign quasi-idempotent, scaled to have coefficient $1$ on the identity. Let $\mathrm{tr}_z$ be the Markov trace with $\mathrm{tr}_z(\sigma_i) = z$. Then $t(z) = \mathrm{tr}_z(x_-)$ vanishes at the convention-D point $z_D = q^3/(q^2+1)$. Reparametrise the family by $c = \mathrm{tr}_z(b)$ for an element $b = u\,\sigma_1 + v$ of $H_2$. The conjecture was that the factor $q^{-3}$ in the normaliser $c_{\mathrm{sign}} = [3]_q!\,q^{-3}$ of [the Borromean observable](f-bor-borromean-observable.md) equals $-\partial_c t$ at $z_D$, where $b$ satisfies:

1. $b$ and $1$ span $H_2$ over $\mathbb{Z}[q, q^{-1}]$, that is, $u$ is a unit of $\mathbb{Z}[q, q^{-1}]$;
2. $b$ is fixed by the [bar involution](bar-involution.md) $\sigma_1 \mapsto \sigma_1^{-1}$, $q \mapsto q^{-1}$.

Stated this way, conditions (1) and (2) apply to the coordinate $b$ only. The element $x_-$ is fixed by its identity coefficient, which is integral but not bar-invariant. The results below show that this split carries the whole $q^{-3}$. The conjecture is therefore retired as a derivation of the normaliser and kept as a record of the negative result. The normaliser of $F_{\mathrm{Bor}}$ remains asserted.

**What is proved.** The elements satisfying (1) and (2) are exactly $b = \pm(\sigma_1 - q) + c$ with $c$ bar-invariant. For these, $-\partial_c t(z_D) = \pm q^{-3}$. Each condition is needed. Condition (1) alone allows $u = q^m$ for every $m \in \mathbb{Z}$, which gives $\pm q^{-3-m}$. Condition (2) alone allows $u = [2]_q$, which gives $q^{-3}/[2]_q$. The same rule applied to the trivial quasi-idempotent $x_+$, whose trace vanishes at $z_+ = -1/(q^3+q)$, gives derivative $q^3$. That is the $q$-power of the trivial Schur element $c_{\mathrm{triv}} = q^3\,[3]_q!$.

**What weakens the conjecture.** Three further results bear against it.

- *The derivative does not select the power of $q$.* The Markov trace decomposes as $\mathrm{tr}_z = y_{(3)}\chi_{\mathrm{triv}} + y_{(1^3)}\chi_{\mathrm{sign}} + y_{(2,1)}\chi_{\mathrm{refl}}$. Each linear weight $y$ has slope $\pm 1/[3]_q!$ at its zeros. For any element $x$ of a linear block, $\mathrm{tr}_z(x)$ is the square constant of $x$ times $y$, so its derivative is that constant divided by $[3]_q!$. The value $-q^{-3}$ is $c_{\mathrm{sign}}/[3]_q!$ because $x_-$ was scaled to have coefficient $1$ on the identity. The trivial-block result above follows the same way, so it is not an independent check.
- *Applied to the element too, the criterion gives $k = 0$.* The bar involution maps $x_-$ to $q^6 x_-$. So among the generators $\pm q^m x_-$ of the integral sign line, only $\pm q^3 x_-$ is bar-invariant. Its derivative at $z_D$ is $-1$, and its square constant is $q^3 c_{\mathrm{sign}} = [3]_q!$, the bar-symmetric normaliser. The conjecture holds only if the criterion applies to the coordinate but not to the element.
- *The reflection block does not follow the rule.* Its weight $y_{(2,1)}$ vanishes at $z = q$ with slope $-[2]_q^2/[3]_q!$, not $\pm 1/[3]_q!$.

These results are proved in `QOU/MassTheory/ProtonQ3OcneanuSlopes.lean`, except the step that $\overline{x_-}$ lies in the sign line, which is argued from $\sigma_i x_- = -q^{-1} x_-$.

**What is open.** No axiom requires the trace family to be read in a coordinate satisfying (1) and (2). Both ingredients are defined: the bar involution, and the integral form $\mathbb{Z}[q, q^{-1}]$ over which traces are evaluated. The step that is not established is that the observable's normaliser is computed in such a coordinate. Deriving it would need a principle that observables factor through the integral, bar-symmetric form, which is not on record. Such a principle, applied uniformly, would select $k = 0$ rather than $k = -3$.

The Lean sibling states conditions (1) and (2) as a class and derives $u = \pm 1$ from them.
