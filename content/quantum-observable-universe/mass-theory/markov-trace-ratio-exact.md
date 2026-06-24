**Proposition (normalization-independence of Markov-trace ratios).**
*For braids $\beta_1, \beta_2 \in B_n$ with $\operatorname{tr}_M(\beta_2) \neq 0$,
and for the Jones normalisation factor
$C(n, q) = (-q^{1/2} - q^{-1/2})^{n-1}$:*

$$
  \frac{J_{K_1}(q)}{J_{K_2}(q)}
  \;=\;
  \frac{C(n, q) \cdot \operatorname{tr}_M(\beta_1)}{C(n, q) \cdot \operatorname{tr}_M(\beta_2)}
  \;=\;
  \frac{\operatorname{tr}_M(\beta_1)}{\operatorname{tr}_M(\beta_2)}.
$$

*In particular, the Gram matrix $G_{ij} = \operatorname{tr}_M(b_i \cdot b_j)$,
the LP cost vectors $t_k = \operatorname{tr}_M(b_k)$, and the shadow
prices $y^*$ from the operator-selection LP are all exact up to a global
scalar that cancels in every ratio, inner product, and optimality
condition.*

**Consequence for the HOMFLYPT engine.** The
[`homflypt_engine.py`](../../computations/homflypt_engine.py)
returns Markov-trace-normalised values at SU(2) (row 3 of
[`rem:archimedean-image-table`](#rem:archimedean-image-table)), which
are proportional to the Jones polynomial. For all optimisation
consumers — [`gram-matrix-dual.py`](../../computations/gram-matrix-dual.py),
[`confinement-operator-selection.py`](../../computations/confinement-operator-selection.py),
[`lp_dual_solver.py`](../../computations/lp_dual_solver.py) — the
ratios are exact and the LP shadow prices, Gram inverse, and Frobenius
duals are normalisation-independent.

At SU($N > 2$), the engine uses the quantum Schur function weights,
which give a DIFFERENT invariant (the SU($N$) quantum invariant, row 5
of the Archimedean-image table). The same ratio-exactness holds within
each $N$-channel: the normalisation factor $C_N(n, q)$ cancels in ratios.
