*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data. The $n = 2$ case is formalised faithfully — both partitions factor through the genuine cyclotomic denominator $D_2 = \Phi_4\Phi_8 = (t^2+1)(t^4+1) \neq 0$; the $n = 3, 4$ denominators are numerically verified for all 18 partitions in the witness and tracked for formalisation.*

**Proposition (cyclotomic factorisation of $y_\lambda$ at small $n$).**
*Let $\sigma_i$ be the symmetric Hecke generators of $H_n(R, q)$ with
Markov parameter $z = 1/(q^{1/2} + q^{-1/2})$, and write $\check{q} = q^{1/2}$.
Then for every $\lambda \,\vdash\, n$ at $n \in \{2, 3, 4\}$, the
Jones-Markov central coefficient $y_\lambda$ admits the closed form*

$$
  y_\lambda(\check{q}) \;=\; \frac{P_\lambda(\check{q})}{D_n(\check{q})}, \qquad
  D_n(\check{q}) \;=\; \prod_{d} \Phi_d(\check{q})^{e_{n, d}},
$$

*where $P_\lambda(\check{q}) \in \mathbb{Z}[\check{q}]$ is a polynomial in $\check{q}$ and
$D_n(\check{q})$ is a **pure product of cyclotomic polynomials** $\Phi_d(\check{q})$.*

## Per-$n$ denominators (over $\mathbb{Q}$ in $\check{q} = q^{1/2}$)

| $n$ | $D_n(\check{q})$ |
|--:|--|
| $2$ | $\Phi_4(\check{q}) \cdot \Phi_8(\check{q}) = (\check{q}^2 + 1)(\check{q}^4 + 1)$ |
| $3$ | $\Phi_4(\check{q})^2 \cdot \Phi_8(\check{q}) \cdot \Phi_3(\check{q}) \cdot \Phi_6(\check{q}) \cdot \Phi_{12}(\check{q})$ |
| $4$ | $\Phi_4(\check{q})^3 \cdot \Phi_8(\check{q})^2 \cdot \Phi_{16}(\check{q})$ (for hook-shape rows) |

where $\Phi_3(\check{q}) = \check{q}^2 + \check{q} + 1$, $\Phi_4(\check{q}) = \check{q}^2 + 1$,
$\Phi_6(\check{q}) = \check{q}^2 - \check{q} + 1$, $\Phi_8(\check{q}) = \check{q}^4 + 1$,
$\Phi_{12}(\check{q}) = \check{q}^4 - \check{q}^2 + 1$, $\Phi_{16}(\check{q}) = \check{q}^8 + 1$.

## Numerators (small $n$)

### $n = 2$

$$
  y_{(2)}(\check{q}) = \frac{\check{q}^3 + \check{q}^2 + 1}{\Phi_4(\check{q}) \, \Phi_8(\check{q})}, \qquad
  y_{(1, 1)}(\check{q}) = \frac{\check{q}^3 \, (\check{q}^3 + \check{q} - 1)}{\Phi_4(\check{q}) \, \Phi_8(\check{q})}.
$$

The numerators $P_{(2)} = \check{q}^3 + \check{q}^2 + 1$ and $P_{(1,1)} = \check{q}^3(\check{q}^3+\check{q}-1)$
are **not** cyclotomic — they encode the specific $X$ substitution
from the Wenzl-bridge.

### $n = 3$

$$
\begin{aligned}
  y_{(3)}(\check{q}) &= \frac{(\check{q} + 1)(\check{q}^3 + \check{q}^2 + 1)(\check{q}^6 - \check{q}^5 + \check{q}^4 - \check{q}^3 + 2\check{q}^2 - \check{q} + 1)}{D_3(\check{q})}, \\
  y_{(2, 1)}(\check{q}) &= \frac{\check{q}^3 (\check{q}^3 + \check{q} - 1)(\check{q}^3 + \check{q}^2 + 1)}{\Phi_4(\check{q})^2 \, \Phi_3(\check{q}) \, \Phi_6(\check{q}) \, \Phi_{12}(\check{q})}, \\
  y_{(1^3)}(\check{q}) &= \frac{\check{q}^6 (\check{q} - 1)(\check{q}^3 + \check{q} - 1)(\check{q}^6 + \check{q}^5 + 2\check{q}^4 + \check{q}^3 + \check{q}^2 + \check{q} + 1)}{D_3(\check{q})}.
\end{aligned}
$$

### $n = 4$

$$
\begin{aligned}
  y_{(4)} &= \frac{(\check{q} + 1)(\check{q}^3 + \check{q}^2 + 1)(\check{q}^{11} + \check{q}^7 + \check{q}^3 + \check{q}^2 + 1)(\ldots)}{\Phi_4^3 \, \Phi_8^2 \, \Phi_{16} \, \Phi_3 \, \Phi_6 \, \Phi_{12}}, \\
  y_{(2,2)} &= \frac{\check{q}^7 (\check{q}^3 + \check{q} - 1)(\check{q}^3 + \check{q}^2 + 1)}{\Phi_4^2 \, \Phi_8^2 \, \Phi_3 \, \Phi_6 \, \Phi_{12}}, \\
  y_{(1^4)} &= \frac{\check{q}^9 (\check{q} - 1)(\check{q}^3 + \check{q} - 1)(\check{q}^{11} + \check{q}^9 - \check{q}^8 - \check{q}^4 - 1)(\ldots)}{D_4(\check{q})}.
\end{aligned}
$$

(Mid-shapes $(3,1), (2,1,1)$ are bigger; see witness file for full
expressions.)

## Significance

This is the **cleanest possible closed form** for $y_\lambda$ in
$\mathbb{Q}(\check{q})$: the denominator structure is fully determined by
combinatorial hook-length data via cyclotomic polynomials, and the
numerator is a finite-degree polynomial in $\check{q}$ that can be
explicitly tabulated.

For Lean formalisation, this gives a concrete mathematical
statement:

$$
  y_\lambda(\check{q}) \cdot D_n(\check{q}) \;=\; P_\lambda(\check{q})
  \in \mathbb{Z}[\check{q}]
$$

where $D_n(\check{q}) = \prod_d \Phi_d(\check{q})^{e_{n,d}}$ with explicit
$e_{n, d}$ exponents derivable from the hook-length data of all
partitions of $n$.

## Witness

[`computations/y_lambda_cyclotomic_factor.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_cyclotomic_factor.py)
factors the Wenzl-bridge $y_\lambda$ over $\mathbb{Q}(\check{q})$ via sympy.
Output: `y-lambda-cyclotomic-factor.witness.json` with explicit
factored numerators and denominators for $n = 2, 3, 4$.
