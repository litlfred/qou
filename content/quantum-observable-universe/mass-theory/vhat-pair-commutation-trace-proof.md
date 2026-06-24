The traced volume $\hat V_i(q) = z(q)\,a_i(q) + b_i(q)$ is, by
construction
([def:algebraic-quantum-volume §partial-product expansion](#def\:algebraic-quantum-volume)),
an element of the **commutative** Laurent polynomial ring
$\mathbb{Z}[q^{\pm 1/2}, z]$ — the coefficients $a_i, b_i$ are
polynomials in $q^{\pm 1/2}$ and $z$ is a single transcendental
parameter (the Markov parameter, eliminated by
$z = 1/(q^{1/2} + q^{-1/2})$ at the end of every Markov peel,
[`thm:jones-markov-trace`](#thm\:jones-markov-trace)).

Two elements of a commutative ring commute. Hence

$$
  \hat V_i \cdot \hat V_j \;=\; \hat V_j \cdot \hat V_i.
$$

Applying $\mathrm{tr}_M$ (which is $\mathbb{Z}[q^{\pm 1/2}, z]$-
linear) and invoking the pair Markov-trace identity
([prop:markov-pair-z2](#prop\:markov-pair-z2)) gives the second
equality $\mathrm{tr}_M(\hat V_i \hat V_j) = z^2$ for **all**
$i, j$ — adjacent or not. $\square$
