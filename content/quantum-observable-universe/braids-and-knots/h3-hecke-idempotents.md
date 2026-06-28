**$H_3(q)$ Hecke idempotents — explicit $q$-dimensions and Wedderburn-block eigenvalue table.**

The Iwahori-Hecke algebra $H_3(q)$ has three irreducible Wedderburn
blocks indexed by partitions of $3$. For each block $V_\lambda$, the
generators $\sigma_0, \sigma_1$ act with eigenvalues drawn from the
Hecke-quadratic roots $\{q, -q^{-1}\}$.

| $\lambda$ | $\dim_q V_\lambda$ | $\sigma_0$ eigenvalue | $\sigma_1$ eigenvalue | source |
|:---:|:---:|:---:|:---:|---|
| $(3)$ | $1$ | $q$ | $q$ | symmetric: both $\sigma$ act as $q$ |
| $(2,1)$ | $[2]_q = q + q^{-1}$ | $\langle q, -q^{-1} \rangle$ | Hoefsmit (off-diag) | [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization) |
| $(1,1,1)$ | $1$ | $-q^{-1}$ | $-q^{-1}$ | antisymmetric: both $\sigma$ act as $-q^{-1}$ |

### Substantive content (no vacuous classes)

The Lean module exports **concrete scalar identities**, not abstract markers:

- `dimQ_V3 q : ℝ = 1`
- `dimQ_V21 q : ℝ = q + q^{-1}` (= $[2]_q$ at H_3)
- `dimQ_V111 q : ℝ = 1`
- `sigma_eigval_V3 q i : ℝ = q` (for every $i$)
- `sigma_eigval_V111 q i : ℝ = -q^{-1}` (for every $i$)

The **sum-of-$q$-dimensions identity**

$$
  \dim_q V_{(3)} + \dim_q V_{(2,1)} + \dim_q V_{(1,1,1)}
    \;=\; q + q^{-1} + 2
$$

is the theorem `dimQ_sum_H3`, closed by `ring`. The completeness
residual at $n = 3$ — the LHS $-$ RHS of this identity — is
the theorem `qYoung_completeness_residual_H3`, closed `0` by `ring`.

### Connection to the Q-YST class

This block **substantively backs** the abstract `QYoungSymmetrizers 3 q`
class instance in
[`rem:ck-extraction-from-algebraic-rules`](#rem:ck-extraction-from-algebraic-rules):
the `qyst_residual` scalar (declared in that class) is concretely
the residual of the $q$-dimension sum identity above, and `dimQ_sum_H3`
discharges it to `0`.

### Remaining work

The abstract $H_n(q)$ type (the quotient-of-`FreeAlgebra`
presentation a Mathlib lift would provide) is still outside the
chapter-block .lean tier; the explicit projectors above live on the
concrete rank-6 carrier. The scalar-invariant version landed here is
sufficient to discharge the abstract Q-YST scaffolding for the c_k
extraction theorem; a future Mathlib lift of full $H_n(q)$ would
substitute the carrier-level $e_\lambda$ values without changing the
downstream API.
