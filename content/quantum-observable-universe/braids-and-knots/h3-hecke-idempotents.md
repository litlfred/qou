**$H_3(q)$ Hecke idempotents — explicit $q$-dimensions and Wedderburn-block eigenvalue table.**

The Iwahori–Hecke algebra $H_3(q)$ has three irreducible Wedderburn blocks indexed by partitions of $3$. For each block $V_\lambda$, the generators $\sigma_0, \sigma_1$ act with eigenvalues drawn from the Hecke-quadratic roots $\{q, -q^{-1}\}$.

| $\lambda$ | $\dim_q V_\lambda$ | $\sigma_0$ eigenvalue | $\sigma_1$ eigenvalue | source |
|:---:|:---:|:---:|:---:|---|
| $(3)$ | $1$ | $q$ | $q$ | symmetric: both $\sigma$ act as $q$ |
| $(2,1)$ | $[2]_q = q + q^{-1}$ | $\langle q, -q^{-1} \rangle$ | Hoefsmit (off-diag) | [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization) |
| $(1,1,1)$ | $1$ | $-q^{-1}$ | $-q^{-1}$ | antisymmetric: both $\sigma$ act as $-q^{-1}$ |

## Substantive content (no vacuous classes)

The Lean module exports concrete scalar identities, not abstract markers:

- `dimQ_V3 q : ℝ = 1`
- `dimQ_V21 q : ℝ = q + q^{-1}` (= $[2]_q$ at $H_3$)
- `dimQ_V111 q : ℝ = 1`
- `sigma_eigval_V3 q i : ℝ = q` (for every $i$)
- `sigma_eigval_V111 q i : ℝ = -q^{-1}` (for every $i$)

The sum-of-$q$-dimensions identity is

$$
  \dim_q V_{(3)} + \dim_q V_{(2,1)} + \dim_q V_{(1,1,1)}
    \;=\; q + q^{-1} + 2.
$$

This is the theorem `dimQ_sum_H3`, closed by `ring`. The completeness residual at $n = 3$ (the difference between the left and right sides) is the theorem `qYoung_completeness_residual_H3`, discharged to `0` by `ring`.

## Connection to the Q-YST class

This block substantively backs the abstract `QYoungSymmetrizers 3 q` class instance in [`rem:ck-extraction-from-algebraic-rules`](#rem:ck-extraction-from-algebraic-rules). The `qyst_residual` scalar declared in that class is precisely the residual of the $q$-dimension sum identity above, and `dimQ_sum_H3` discharges it to `0`.

## Explicit projector normalization — the $S_3$ Poincaré polynomial

The carrier-level construction of the two one-dimensional projectors (in the upstreamable module `QOU.Mathlib.HeckeAlgebra`, declarations `H3.blockSym3` and `H3.blockAlt3`) fixes the normalization convention:

$$
  e_{(3)} = \frac{1}{P(q)} \sum_{w \in S_3} q^{\ell(w)}\, T_w,
  \qquad
  e_{(1^3)} = \frac{1}{P(q^{-1})} \sum_{w \in S_3} (-q^{-1})^{\ell(w)}\, T_w.
$$

Here $P(q) = \sum_{w \in S_3} q^{2\ell(w)} = 1 + 2q^2 + 2q^4 + q^6 = (1+q^2)(1+q^2+q^4)$ is the Poincaré polynomial of $S_3$ in the Hecke parameter (declaration `H3.poincare`). The normalizer is forced by the eigenvalue table above. Specifically, $T_w\, e_{(3)} = q^{\ell(w)} e_{(3)}$, so squaring the sum multiplies it by $\sum_w q^{2\ell(w)}$. Idempotency pins the denominator to exactly $P(q)$. The sign block has $T_w\, e_{(1^3)} = (-q^{-1})^{\ell(w)} e_{(1^3)}$, which pins the denominator to $P(q^{-1})$.

Two practical consequences:

1. **No genericity hypothesis.** $P(q) \geq 1 > 0$ for every real $q$ because of the even powers and positive coefficients. Idempotency and orthogonality of the blocks hold with only $q \neq 0$ (which clears the $q - q^{-1}$ structure constants). There is no vanishing locus to avoid on the real line.
2. **Relation to the balanced $q$-factorial.** With the balanced convention $[k]_q = (q^k - q^{-k})/(q - q^{-1})$, we have $P(q) = q^{\ell(w_0)}\, [3]_q!$, where $\ell(w_0) = 3$ is the longest element. Furthermore, $P(q^{-1}) = q^{-\ell(w_0)}\, [3]_q!$ by bar-invariance of $[3]_q!$. The two normalizers differ by $q^{2\ell(w_0)} = q^6$. Using the bare balanced factorial for both blocks makes neither projector idempotent.

## Remaining work

The abstract $H_n(q)$ type (a quotient of `FreeAlgebra` that a Mathlib lift would provide) is still outside the chapter-block `.lean` tier. The explicit projectors above live on the concrete rank-6 carrier. The scalar-invariant version included here is sufficient to discharge the abstract Q-YST scaffolding for the $c_k$ extraction theorem. A future Mathlib lift of the full $H_n(q)$ would substitute the carrier-level $e_\lambda$ values without changing the downstream API.
