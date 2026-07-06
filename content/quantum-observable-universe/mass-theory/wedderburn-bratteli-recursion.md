**Proposition (Wedderburn–Bratteli recursion: existence and structure).**
*Let $H_n(R, q)$ be the Iwahori–Hecke algebra at generic $q$ with
Markov parameter $z = 1/(\sqrt q + 1/\sqrt q)$, and let
$\{y_\lambda^{(n)}\}_{\lambda \,\vdash\, n}$ be the Jones–Markov
weights of [α_k derivation procedure](#prop:alpha-k-derivation-procedure).
Then the family $\{y_\lambda^{(n)}\}_{n \geq 1}$ satisfies a
**multiplicity-free Bratteli recursion**: for every $\lambda \,\vdash\,
n + 1$,*

$$
  y_\lambda^{(n+1)}
  \;=\;
  z \cdot
  \sum_{\mu \nearrow \lambda}
    F_q\bigl(c(\lambda, \mu),\, \mathrm{hooks}(\lambda)\bigr)
  \cdot y_\mu^{(n)},
$$

*where $\mu \nearrow \lambda$ ranges over the Bratteli edges (partitions
$\mu \,\vdash\, n$ with $\mu \subset \lambda$, $|\lambda \setminus \mu|
= 1$), $c(\lambda, \mu) = j - i$ is the $q$-content of the added cell,
and $F_q$ is a $q$-rational function determined by the Hoefsmit seminormal
eigenvalues of $T_n$ on the per-edge idempotent.*
## Implication for $\alpha_k$ at $H_n > 3$

Even before $F_q$ is in closed form, the recursion gives the
qualitative structural shortcut: $\alpha_k(H_n)$ at fixed $k$
involves only finitely many strata, and the tower of Jones–Markov
weights propagates without re-solving the $p(n) \times p(n)$ linear
system — the witness is enough.  Combined with depth-$k$ representative
choices ([α_k derivation procedure](#prop:alpha-k-derivation-procedure)
step (i)), $\alpha_k(H_n)$ for arbitrary $n$ is then a finite sum
indexed by depth-$k$ partitions and their Bratteli-ancestors.

## Witness

[`computations/y-lambda-jones-markov-witness.json`](#) —
all 270 weights for $n = 2, \ldots, 12$.

[the formal derivation](#) —
extracts per-edge ratios and tests candidate closed forms $F_q$.

## Open

- **Sign pattern at $n \geq 4$**: $y_\lambda$ acquires negative
  components at $n \geq 4$ (e.g.\ $y_{(1^4)} \approx -8 \times 10^{-4}$
  at $q_0$); see [sign-pattern remark](#rem:y-lambda-sign-pattern)
  for empirical table and explanation via cancellation across
  Wedderburn blocks.  Implication: LP-positivity formulations of the
  Jones–Markov weights are infeasible at $n \geq 4$; SDP/cvxpy
  unconstrained least-squares cross-checks confirm the symbolic
  values.
- **Lean formalisation**: state the recursion in
  `wedderburn-bratteli-recursion.lean` against the symbolic
  $y_\lambda$ solutions.
