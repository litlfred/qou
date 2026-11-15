Write $M$ for the character matrix whose rows are the torus knots $T_{r_i, s_i}$ with $r_i \in \{2, 3\}$ available at a given genus and whose columns are the five irreducibles of $H_2(q) \oplus H_3(q)$.

A torus knot $T_{r,s}$ is the closure of a braid word on $r$ strands, so its evaluation is supported in the $H_r(q)$ columns alone: a row with $r_i = 2$ vanishes on the three $H_3(q)$ columns, and a row with $r_i = 3$ vanishes on the two $H_2(q)$ columns. So $M$ is block-diagonal, and rank is additive over the blocks. Each block is bounded by the smaller of its two dimensions, giving

$$
\mathrm{rank}(M) \;\leq\; \min(\#\{i : r_i = 2\},\, 2) \;+\; \min(\#\{i : r_i = 3\},\, 3).
$$

At $g = 4$ there are four rows with $r_i = 2$ and two with $r_i = 3$, so the bound reads $2 + 2 = 4$. The rank is therefore at most $4$, and this holds for every $q$ — it is a statement about the support pattern, not about the values of the characters, so no choice of $q$ and no appeal to $q$ avoiding a root of unity can raise it.

The bound is met with equality at $g = 4$: exact symbolic computation over $\mathbb{Q}(q)$ gives rank $4$, and the ranks by genus are $1, 2, 3, 4, 4, 5, 5$ at $g = 1, \dots, 7$. Reaching rank $5$ needs a third row with $r_i = 3$, i.e. a third torus knot $T_{3,s}$; the first three are $T_{3,4}$, $T_{3,5}$, $T_{3,7}$ of genus $3$, $4$, $6$, so rank $5$ is first available at $g = 6$.

**This does not fix the genus at $6$ either.** At $g = 6$ the restriction to $r \in \{2, 3\}$ lapses, because $T_{4,5}$ has genus $6$ and so $H_4(q)$ enters with five further irreducibles; the target dimension moves from $5$ to $10$ and the criterion is again unmet. Pushed self-consistently the criterion escalates rather than closing, so it has no fixed point and does not determine a genus.

**Scope.** This is a structural exclusion of one *route*, with a named invariant — rank subadditivity over a block decomposition. It says nothing about whether the genus is $4$; two other routes to $g = 4$ are untouched by it. What it excludes is the use of *this* criterion as the step that derives the genus from the algebra.
