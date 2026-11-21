**Definition (finite LP-duality hypothesis).**
*An operator-selection LP, given by its objective $t$, Gram matrix $G$, net target $n_{\mathrm{target}}$ and box bound $M$, satisfies the finite LP-duality hypothesis if it has a primal-feasible point $x$ and a dual-feasible point $(y_0, y, w)$ with zero duality gap.*

Complementary slackness then follows: a constraint with positive shadow price $y_\lambda > 0$ is tight, $(Gx)_\lambda = 0$. The converse, that every tight constraint has positive shadow price, is strict complementarity (Goldman–Tucker). It holds for some optimal pair but not for every one, so it is a separate hypothesis.

This isolates the standard finite-dimensional LP strong-duality and complementary-slackness theorems, which are cited rather than re-proved here, as an explicit hypothesis. Results that rely on them are stated conditional on it; discharging it changes no downstream mathematical commitment.
