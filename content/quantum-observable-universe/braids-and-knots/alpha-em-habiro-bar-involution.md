**Proposition.** *Let $H(q) = [2]_q\,(1 - h^2\alpha)$ be the
$\alpha_{EM}$ Habiro element, where $[2]_q = q + q^{-1}$ and
$h = q - q^{-1}$ is the Hecke differential. Then, over a generic
commutative ring with $q$ a formal variable:*

1. *$H$ is a **fixed point of the bar involution** $q \mapsto q^{-1}$:*
   $$H(q^{-1}) = H(q).$$
2. *Its leading **special values** are*
   $$H(1) = 2, \qquad H(-1) = -2.$$

These are **fibre-level** statements: $q$ is a formal variable with no
reality or archimedean constraint imposed. The operative symmetry is
the bar involution $q \mapsto q^{-1}$ — the framework/tower involution
structure — not a reality assumption. Only the *observable* component,
read off at the archimedean substrate evaluation, is real; the
involution structure itself holds over the formal fibre.

## Significance

The factor $H = [2]_q(1 - h^2\alpha)$ is the $\alpha_{EM}$ next-order
Habiro element ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)).
Because $[2]_q = q + q^{-1}$ is manifestly bar-symmetric, $H$ lies
**entirely** in the charge-conjugation-symmetric (bar-fixed) sector.
This is the same sector that the analogous $\mathfrak{Q}_\beta$ scaling map must
occupy, and it is precisely the structural reason the $\alpha_{EM}$
next-order form was identifiable as a Habiro element while the
$\mathfrak{Q}_\beta$ analogue — whose trace difference is *not* a bar fixed point
— required a separate cancellation analysis.

The two special values are the lowest root-of-unity evaluations of
$H$: $H(\zeta_1) = H(1) = 2$ is the classical leading term that gives
$\alpha/(4\pi)$, and $H(\zeta_2) = H(-1) = -2$ is the bar mode. The
full root-of-unity spectrum of $H$ (exact in the cyclotomic field, with
$\alpha$ kept formal) is recorded in the computational witness;
$H(\zeta_4) = 0$, a modular **zero** that is the exact structural dual
of the $\mathfrak{Q}_\beta$ Habiro element's modular **pole** at $\zeta_4$.

## Lean structure

`alphaEmHabiro q qi α := (q + qi)·(1 - (q - qi)²·α)` is defined over a
generic `CommRing` with `q`, `qi` independent variables (the inverse
relation `q·qi = 1` is invoked only where needed). The bar involution
is the swap `q ↔ qi`; `alphaEmHabiro_bar_invariant` proves the swap
fixes `H` by `ring` (the sum `q + qi` is symmetric and `(q − qi)²`
absorbs the sign). The special values `alphaEmHabiro_at_one` and
`alphaEmHabiro_at_neg_one` evaluate at `q = qi = ±1` by `ring`. No
`ℝ`, no ordering, no complex numbers — the statements are
involution-level, not archimedean.
