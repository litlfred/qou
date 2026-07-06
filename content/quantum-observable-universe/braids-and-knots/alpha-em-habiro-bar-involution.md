**Proposition.** *Let $H(q) = [2]_q\,(1 - h^2\alpha)$ be the $\alpha_{EM}$ Habiro element, where $[2]_q = q + q^{-1}$ and $h = q - q^{-1}$ is the Hecke differential. Then, over a generic commutative ring with $q$ a formal variable:*
1. *$H$ is a fixed point of the bar involution $q \mapsto q^{-1}$:*
   $$H(q^{-1}) = H(q).$$
2. *Its leading special values are*
   $$H(1) = 2, \qquad H(-1) = -2.$$

We define $H(q)$ as the next-order Habiro element for the fine-structure coupling $\alpha_{EM}$ ([`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)). The bar involution $q \mapsto q^{-1}$ operates on the formal fibre; we do not impose reality constraints until archimedean evaluation. 

The factor $[2]_q = q + q^{-1}$ is manifestly bar-symmetric, so $H$ lies entirely in the bar-fixed sector. This symmetry distinguishes the $\alpha_{EM}$ element from its $\mathfrak{Q}_\beta$ analog, which requires separate trace cancellation because it is not a bar fixed point. 

The special values $H(\zeta_1) = 2$ and $H(\zeta_2) = -2$ furnish the classical leading term $\alpha/(4\pi)$ and the bar mode. At the fourth root of unity, $H(\zeta_4) = 0$. This modular zero is the exact structural dual of the modular pole at $\zeta_4$ for the $\mathfrak{Q}_\beta$ Habiro element. 

## Formalization

We define `alphaEmHabiro q qi α := (q + qi)·(1 - (q - qi)²·α)` over a generic commutative ring using independent variables `q` and `qi`, invoking the inverse relation `q·qi = 1` only when needed. The formal property `alphaEmHabiro_bar_invariant` verifies that the swap `q ↔ qi` fixes $H$. The special values `alphaEmHabiro_at_one` and `alphaEmHabiro_at_neg_one` hold by evaluation at $q = q^{-1} = \pm 1$. We avoid archimedean fields; the proofs rely purely on the ring-level bar symmetry of $[2]_q(1-h^2 \alpha)$.