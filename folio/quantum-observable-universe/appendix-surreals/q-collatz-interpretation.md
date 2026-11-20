The $q$-Collatz conjecture ([conj:q-collatz](#conj:q-collatz)) lives in the Skein module $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$.

| Identity | Formula | Role |
|----------|---------|------|
| Skein divisibility | $[3]_q = q[2]_q + 1$ | "$3n+1$ is even for odd $n$" |
| Contraction gap | $[2]_q^2 - [3]_q = q$ | Two halvings beat one tripling |
| Hecke reduction | $T^2 = (q-q^{-1})T + 1$ | Crossing words reduce |

The Skein relation rewrites as:

$$
J(L_+) = q^{-2}J(L_-) + (1-q^{-2})J(L_0).
$$

For $q > 1$, this is a convex combination. Crossing resolution is non-expansive on Jones polynomial values.

The Collatz map $(2, 3)$ belongs to a family of generalized maps $(p_1, p_2)$. The $q$-deformed contraction condition requires $k_1$ halvings to overpower $k_2$ triplings:

$$
[p_1]_q^{k_1} > [p_2]_q^{k_2}.
$$

The contraction gap $[p_1]_q^{k_1} - [p_2]_q^{k_2}$ determines the contraction regime.

At the classical boundary $p_1^{k_1} = p_2^{k_2} + 1$, the $q$-gap polynomial may develop negative high-degree coefficients:

| $(p_1^{k_1}, p_2^{k_2})$ | Classical gap | $q$-gap | All $q > 0$? |
|--------------------------|--------------|---------|-------------|
| $(2^2, 3^1)$ — **Collatz** | $4 - 3 = 1$ | $q$ | **Yes** (monomial) |
| $(3^2, 8^1)$ | $9 - 8 = 1$ | $q + 2q^2 + q^3 - q^5 - q^6 - q^7$ | No |
| $(4^2, 15^1)$ | $16 - 15 = 1$ | negative high-degree terms | No |

Collatz $(2^2, 3^1)$ is the unique critical case where the $q$-gap is a monomial. The identity $[2]_q^2 - [3]_q = q$ produces a gap with a single term $q$, positive for all $q > 0$. Every other critical case produces a gap polynomial with negative terms that dominate for large $q$.

Proved results:
- $[3]_q = q[2]_q + 1$
- $[2]_q^2 - [3]_q = q$
- $[3]_q < [2]_q^2$ for $q > 0$
- $\sqrt{[3]_q/[2]_q^2} < 1$
- $(3, 4)$ gap positive for $q > 0$
- $(3, 8)$ gap fails for $q > 2$

The orbit structure provides the two halvings. The $[2]_q$-adic valuation of $\mathcal{C}_q(P)$ must average to at least $2$ ([contact boundary](#prop:collatz-contact-boundary)). At $q = 1$, this average is exactly $2$. The conjecture asserts this holds for all $q > 1$.
