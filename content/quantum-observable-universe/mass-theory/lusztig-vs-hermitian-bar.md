**Proposition** (Lusztig bar vs Hermitian $\ast$).
*On the complex Iwahori–Hecke algebra $H_n(\mathbb{C}, q)$ with
$q \in \mathbb{C}^\times$, the two ring anti-involutions*

$$
\beta_L \colon q \mapsto q^{-1},\quad \sigma_i \mapsto \sigma_i^{-1}
\qquad\text{(Lusztig bar)},
$$

$$
\beta_H \colon q \mapsto \overline{q}^{\,-1},\quad \sigma_i \mapsto \sigma_i^{-1}
\qquad\text{(Hermitian $\ast$)}
$$

*coincide on the parameter $q$ if and only if
$\mathrm{Im}(q) = 0$, equivalently $q \in \mathbb{R}$.*

The Lean formalization specialises to $\mathbb{R}$ for the archimedean evaluation at the substrate $q_0$.

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
[`commutative-chirality-vanishes`](#cor:commutative-chirality-vanishes).
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

## Significance

The framework's existing bar-symmetric / bar-anti-symmetric
decomposition ([`def:bar-involution`](#def:bar-involution),
cheat-sheet §4) is built around $\beta_L$ alone. On the real axis
this is the only available involution structure. On general
complex $q$ with $\lvert q \rvert > 1$ and $\mathrm{Im}(q) \neq 0$,
the algebra admits a *finer* decomposition by simultaneous
$\beta_L$- and $\beta_H$-eigenvalues, with four channels:

| $\beta_L$-eigenvalue | $\beta_H$-eigenvalue | Existing name | Comment |
|---|---|---|---|
| $+1$ | $+1$ | bar-symmetric, Hermitian | retained (current) |
| $+1$ | $-1$ | bar-symmetric, anti-Hermitian | new (CP-odd, parity-even?) |
| $-1$ | $+1$ | bar-anti-symmetric, Hermitian | new (CP-even, parity-odd?) |
| $-1$ | $-1$ | bar-anti-symmetric, anti-Hermitian | projected away |

The interpretation of the two new channels (and whether either
corresponds to physical structure) is **research-grade and open**.
This proposition only records the structural existence of the
decomposition; it does not claim either new channel is physically
realised.

## What this proposition does not claim (CAL-4 caveat)

- It does **not** claim $\mathrm{Im}(q_0) \neq 0$.
- It does **not** claim the two new channels carry physical content.
- It does **not** introduce a further calibration input.

It claims only that on complex $q$ with $\mathrm{Im}(q) \neq 0$ the
two anti-involutions split, and that the framework's current
real-axis convention makes the split invisible.
