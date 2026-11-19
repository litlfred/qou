## Proof

The two involutions act identically on the braid generators
$\sigma_i$ (both send $\sigma_i \mapsto \sigma_i^{-1}$), so the
question reduces to the parameter action: $\beta_L(q) = q^{-1}$
and $\beta_H(q) = \overline{q}^{\,-1}$. For $q \in \mathbb{C}^\times$,

$$q^{-1} \;=\; \overline{q}^{\,-1} \;\iff\; q \;=\; \overline{q} \;\iff\; \mathrm{Im}(q) = 0. \quad\square$$

## Three cases of complex $q$

The following table organises the relationship between the three
relevant involutions on $\mathbb{C}^\times$ — the Lusztig bar
$\beta_L$, the Hermitian $\ast$ ($\beta_H$), and complex conjugation
$\beta_C \colon q \mapsto \overline{q}$ — as $q$ moves through the
three structural regimes:

| Regime | $\beta_L(q)$ | $\beta_H(q)$ | $\beta_C(q)$ | Equalities |
|---|---|---|---|---|
| **Real axis** $\mathrm{Im}(q) = 0$ | $q^{-1}$ | $q^{-1}$ | $q$ | $\beta_L = \beta_H$; $\beta_C = \mathrm{id}$ |
| **Unit circle** $\lvert q \rvert = 1$ | $q^{-1}$ | $q$ | $q^{-1}$ | $\beta_L = \beta_C$ (on parameter); $\beta_H = \mathrm{id}$ on parameter |
| **General** $\lvert q \rvert > 1$, $\mathrm{Im}(q) \neq 0$ | $q^{-1}$ | $\overline{q}^{\,-1}$ | $\overline{q}$ | all three distinct on parameter |

The "real-axis" row is the current framework convention. The
"unit-circle" row is the regime already discussed in
[commutative chirality vanishing](#cor:commutative-chirality-vanishes).
The "general" row is uncharted; it is the categorical home for any
future $\mathrm{Im}(q_0) \neq 0$ hypothesis.

## Decomposition law

The three involutions satisfy

$$\beta_H \;=\; \beta_C \circ \beta_L \;=\; \beta_L \circ \beta_C$$

as automorphisms of the coefficient ring $\mathbb{C}$ extended
identically over the braid generators. On the real axis $\beta_C$ is
the identity, so $\beta_H$ collapses to $\beta_L$. On the unit
circle $\beta_C = \beta_L$ on the parameter (both send
$q \mapsto q^{-1}$), so $\beta_H$ becomes the identity on the
parameter. Off both, the three are independent.
