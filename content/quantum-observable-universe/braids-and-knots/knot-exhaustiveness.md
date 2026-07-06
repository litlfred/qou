**Open question.**
The knot eigenbasis completeness theorem ([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)) establishes that every irreducible summand of $V^{\otimes n}$ is detected by some braid closure via the Markov trace ([Jones–Markov trace](#thm:jones-markov-trace)). This guarantees surjectivity of detection: no summand remains invisible.

A stronger question emerges: do the knot types appearing in the Descartes universe exhaust the space of states?

The generation completeness theorem proves that every knot with Seifert genus $g(\mathfrak{K}) \leq 4$ appears in the spectrum. The genus bound of Bring's surface captures all embeddable knots in that range. Knots with $g > 4$ are excluded by the spectral filter.

This does not confirm whether the Jones polynomial is a faithful invariant—whether distinct knot types always produce distinct polynomials. We use the Jones polynomial only for detection (non-degeneracy on irreducibles), never for classification. Our framework avoids the classical open question of whether $J_K(q) = 1$ implies $K$ is the unknot. The Markov trace non-degeneracy theorem suffices for the knot eigenbasis.

Three nested questions remain:

1. **(Detection.)** Does a knot label every irreducible summand? **Yes.** Alexander surjectivity and Markov non-degeneracy prove this.
2. **(Generation.)** Does every knot with $g \leq 4$ appear? **Yes.** Generation completeness from the seven torus knot generators and Skein crossing changes proves this.
3. **(Faithfulness.)** Do distinct knots always produce distinct states? **Open.** If two distinct knots $\mathfrak{K} \neq \mathfrak{K}'$ yield the same Jones polynomial $J_{\mathfrak{K}}(q) = J_{\mathfrak{K}'}(q)$, they would be physically indistinguishable in the Descartes universe—representing the same particle. Whether this occurs, and its physical consequence, remains an open question.

Existing theorems settle the first two questions. The third relies on progress in classical knot theory. The full HOMFLY-PT polynomial (which carries strictly more information than the Jones specialisation) may already provide the answer.
