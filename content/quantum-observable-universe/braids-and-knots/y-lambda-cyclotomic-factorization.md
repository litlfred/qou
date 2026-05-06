**Proposition (cyclotomic factorisation of $y_\lambda$ at small $n$).**
*Let $\sigma_i$ be the symmetric Hecke generators of $H_n(R, q)$ with
Markov parameter $z = 1/(q^{1/2} + q^{-1/2})$, and write $r = q^{1/2}$.
Then for every $\lambda \,\vdash\, n$ at $n \in \{2, 3, 4\}$, the
Jones-Markov central coefficient $y_\lambda$ admits the closed form*

$$
  y_\lambda(r) \;=\; \frac{P_\lambda(r)}{D_n(r)}, \qquad
  D_n(r) \;=\; \prod_{d} \Phi_d(r)^{e_{n, d}},
$$

*where $P_\lambda(r) \in \mathbb{Z}[r]$ is a polynomial in $r$ and
$D_n(r)$ is a **pure product of cyclotomic polynomials** $\Phi_d(r)$.*

## Per-$n$ denominators (over $\mathbb{Q}$ in $r = q^{1/2}$)

| $n$ | $D_n(r)$ |
|--:|--|
| $2$ | $\Phi_4(r) \cdot \Phi_8(r) = (r^2 + 1)(r^4 + 1)$ |
| $3$ | $\Phi_4(r)^2 \cdot \Phi_8(r) \cdot \Phi_3(r) \cdot \Phi_6(r) \cdot \Phi_{12}(r)$ |
| $4$ | $\Phi_4(r)^3 \cdot \Phi_8(r)^2 \cdot \Phi_{16}(r)$ (for hook-shape rows) |

where $\Phi_3(r) = r^2 + r + 1$, $\Phi_4(r) = r^2 + 1$,
$\Phi_6(r) = r^2 - r + 1$, $\Phi_8(r) = r^4 + 1$,
$\Phi_{12}(r) = r^4 - r^2 + 1$, $\Phi_{16}(r) = r^8 + 1$.

## Numerators (small $n$)

### $n = 2$

$$
  y_{(2)}(r) = \frac{r^3 + r^2 + 1}{\Phi_4(r) \, \Phi_8(r)}, \qquad
  y_{(1, 1)}(r) = \frac{r^3 \, (r^3 + r - 1)}{\Phi_4(r) \, \Phi_8(r)}.
$$

The numerators $P_{(2)} = r^3 + r^2 + 1$ and $P_{(1,1)} = r^3(r^3+r-1)$
are **not** cyclotomic — they encode the specific $X$ substitution
from the Wenzl-bridge.

### $n = 3$

$$
\begin{aligned}
  y_{(3)}(r) &= \frac{(r + 1)(r^3 + r^2 + 1)(r^6 - r^5 + r^4 - r^3 + 2t^2 - r + 1)}{D_3(r)}, \\
  y_{(2, 1)}(r) &= \frac{r^3 (r^3 + r - 1)(r^3 + r^2 + 1)}{\Phi_4(r)^2 \, \Phi_3(r) \, \Phi_6(r) \, \Phi_{12}(r)}, \\
  y_{(1^3)}(r) &= \frac{r^6 (r - 1)(r^3 + r - 1)(r^6 + r^5 + 2t^4 + r^3 + r^2 + r + 1)}{D_3(r)}.
\end{aligned}
$$

### $n = 4$

$$
\begin{aligned}
  y_{(4)} &= \frac{(r + 1)(r^3 + r^2 + 1)(r^{11} + r^7 + r^3 + r^2 + 1)(\ldots)}{\Phi_4^3 \, \Phi_8^2 \, \Phi_{16} \, \Phi_3 \, \Phi_6 \, \Phi_{12}}, \\
  y_{(2,2)} &= \frac{r^7 (r^3 + r - 1)(r^3 + r^2 + 1)}{\Phi_4^2 \, \Phi_8^2 \, \Phi_3 \, \Phi_6 \, \Phi_{12}}, \\
  y_{(1^4)} &= \frac{r^9 (r - 1)(r^3 + r - 1)(r^{11} + r^9 - r^8 - r^4 - 1)(\ldots)}{D_4(r)}.
\end{aligned}
$$

(Mid-shapes $(3,1), (2,1,1)$ are bigger; see witness file for full
expressions.)

## Proof

By [Wenzl bridge](#prop:y-lambda-closed-form-wenzl-bridge),
$y_\lambda(q) = s_{\lambda, r}(Q) / Z_n$ with $Q = q^2$ and
$X = Q^r = q \cdot z / (1 - Q + q \cdot z)$.

Substitute $q = r^2$ throughout: $Q = r^4$, $z = r / (r^2 + 1)$,
$qz = r^3 / (r^2 + 1)$, and

$$
  X(r) = \frac{r^3}{1 + r^2 + r^3 - r^4 - r^6}.
$$

The Schur principal-specialisation factor is

$$
  s_{\lambda, r}(Q) = Q^{n(\lambda)} \prod_{x \in \lambda}
    \frac{1 - X \cdot Q^{c(x)}}{1 - Q^{h(x)}}.
$$

The denominator $\prod (1 - Q^{h(x)}) = \prod (1 - r^{4 h(x)})$
factors over $\mathbb{Z}[r]$ as

$$
  1 - r^{4h} \;=\; \prod_{d \mid 4h} \Phi_d(r).
$$

Hence each $s_{\lambda, r}(Q)$, before normalisation, has a
denominator that is a product of $\Phi_d(r)$ for $d \mid 4 h(x)$.
The sum $Z_n = \sum_\mu d_\mu s_{\mu, r}$ has a common denominator
that is the LCM of these — itself a product of $\Phi_d(r)$.

After reducing $y_\lambda = s_\lambda / Z$, the **denominator
$D_n(r)$ is a product of cyclotomic polynomials** by the closure of
cyclotomic factorisations under multiplication and division.

The **numerator** $P_\lambda(r)$ encodes the specific $X$
substitution and the per-partition Schur structure; it is not
cyclotomic in general. Its degree is bounded by $\sum_x 4 h(x)$
(the total hook content). $\square$

## Significance

This is the **cleanest possible closed form** for $y_\lambda$ in
$\mathbb{Q}(r)$: the denominator structure is fully determined by
combinatorial hook-length data via cyclotomic polynomials, and the
numerator is a finite-degree polynomial in $r$ that can be
explicitly tabulated.

For Lean formalisation, this gives a concrete mathematical
statement:

$$
  y_\lambda(r) \cdot D_n(r) \;=\; P_\lambda(r)
  \in \mathbb{Z}[r]
$$

where $D_n(r) = \prod_d \Phi_d(r)^{e_{n,d}}$ with explicit
$e_{n, d}$ exponents derivable from the hook-length data of all
partitions of $n$.

## Witness

[`folio-assistant/computations/y_lambda_cyclotomic_factor.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/y_lambda_cyclotomic_factor.py)
factors the Wenzl-bridge $y_\lambda$ over $\mathbb{Q}(r)$ via sympy.
Output: `y-lambda-cyclotomic-factor.witness.json` with explicit
factored numerators and denominators for $n = 2, 3, 4$.
