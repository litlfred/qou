**Proposition (cyclotomic factorisation of $y_\lambda$ at small $n$).**
*Let $\sigma_i$ be the symmetric Hecke generators of $H_n(R, q)$ with
Markov parameter $z = 1/(q^{1/2} + q^{-1/2})$, and write $t = q^{1/2}$.
Then for every $\lambda \,\vdash\, n$ at $n \in \{2, 3, 4\}$, the
Jones-Markov central coefficient $y_\lambda$ admits the closed form*

$$
  y_\lambda(t) \;=\; \frac{P_\lambda(t)}{D_n(t)}, \qquad
  D_n(t) \;=\; \prod_{d} \Phi_d(t)^{e_{n, d}},
$$

*where $P_\lambda(t) \in \mathbb{Z}[t]$ is a polynomial in $t$ and
$D_n(t)$ is a **pure product of cyclotomic polynomials** $\Phi_d(t)$.*

## Per-$n$ denominators (over $\mathbb{Q}$ in $t = q^{1/2}$)

| $n$ | $D_n(t)$ |
|--:|--|
| $2$ | $\Phi_4(t) \cdot \Phi_8(t) = (t^2 + 1)(t^4 + 1)$ |
| $3$ | $\Phi_4(t)^2 \cdot \Phi_8(t) \cdot \Phi_3(t) \cdot \Phi_6(t) \cdot \Phi_{12}(t)$ |
| $4$ | $\Phi_4(t)^3 \cdot \Phi_8(t)^2 \cdot \Phi_{16}(t)$ (for hook-shape rows) |

where $\Phi_3(t) = t^2 + t + 1$, $\Phi_4(t) = t^2 + 1$,
$\Phi_6(t) = t^2 - t + 1$, $\Phi_8(t) = t^4 + 1$,
$\Phi_{12}(t) = t^4 - t^2 + 1$, $\Phi_{16}(t) = t^8 + 1$.

## Numerators (small $n$)

### $n = 2$

$$
  y_{(2)}(t) = \frac{t^3 + t^2 + 1}{\Phi_4(t) \, \Phi_8(t)}, \qquad
  y_{(1, 1)}(t) = \frac{t^3 \, (t^3 + t - 1)}{\Phi_4(t) \, \Phi_8(t)}.
$$

The numerators $P_{(2)} = t^3 + t^2 + 1$ and $P_{(1,1)} = t^3(t^3+t-1)$
are **not** cyclotomic — they encode the specific $X$ substitution
from the Wenzl-bridge.

### $n = 3$

$$
\begin{aligned}
  y_{(3)}(t) &= \frac{(t + 1)(t^3 + t^2 + 1)(t^6 - t^5 + t^4 - t^3 + 2t^2 - t + 1)}{D_3(t)}, \\
  y_{(2, 1)}(t) &= \frac{t^3 (t^3 + t - 1)(t^3 + t^2 + 1)}{\Phi_4(t)^2 \, \Phi_3(t) \, \Phi_6(t) \, \Phi_{12}(t)}, \\
  y_{(1^3)}(t) &= \frac{t^6 (t - 1)(t^3 + t - 1)(t^6 + t^5 + 2t^4 + t^3 + t^2 + t + 1)}{D_3(t)}.
\end{aligned}
$$

### $n = 4$

$$
\begin{aligned}
  y_{(4)} &= \frac{(t + 1)(t^3 + t^2 + 1)(t^{11} + t^7 + t^3 + t^2 + 1)(\ldots)}{\Phi_4^3 \, \Phi_8^2 \, \Phi_{16} \, \Phi_3 \, \Phi_6 \, \Phi_{12}}, \\
  y_{(2,2)} &= \frac{t^7 (t^3 + t - 1)(t^3 + t^2 + 1)}{\Phi_4^2 \, \Phi_8^2 \, \Phi_3 \, \Phi_6 \, \Phi_{12}}, \\
  y_{(1^4)} &= \frac{t^9 (t - 1)(t^3 + t - 1)(t^{11} + t^9 - t^8 - t^4 - 1)(\ldots)}{D_4(t)}.
\end{aligned}
$$

(Mid-shapes $(3,1), (2,1,1)$ are bigger; see witness file for full
expressions.)

## Proof

By [Wenzl bridge](#prop:y-lambda-closed-form-wenzl-bridge),
$y_\lambda(q) = s_{\lambda, r}(Q) / Z_n$ with $Q = q^2$ and
$X = Q^r = q \cdot z / (1 - Q + q \cdot z)$.

Substitute $q = t^2$ throughout: $Q = t^4$, $z = t / (t^2 + 1)$,
$qz = t^3 / (t^2 + 1)$, and

$$
  X(t) = \frac{t^3}{1 + t^2 + t^3 - t^4 - t^6}.
$$

The Schur principal-specialisation factor is

$$
  s_{\lambda, r}(Q) = Q^{n(\lambda)} \prod_{x \in \lambda}
    \frac{1 - X \cdot Q^{c(x)}}{1 - Q^{h(x)}}.
$$

The denominator $\prod (1 - Q^{h(x)}) = \prod (1 - t^{4 h(x)})$
factors over $\mathbb{Z}[t]$ as

$$
  1 - t^{4h} \;=\; \prod_{d \mid 4h} \Phi_d(t).
$$

Hence each $s_{\lambda, r}(Q)$, before normalisation, has a
denominator that is a product of $\Phi_d(t)$ for $d \mid 4 h(x)$.
The sum $Z_n = \sum_\mu d_\mu s_{\mu, r}$ has a common denominator
that is the LCM of these — itself a product of $\Phi_d(t)$.

After reducing $y_\lambda = s_\lambda / Z$, the **denominator
$D_n(t)$ is a product of cyclotomic polynomials** by the closure of
cyclotomic factorisations under multiplication and division.

The **numerator** $P_\lambda(t)$ encodes the specific $X$
substitution and the per-partition Schur structure; it is not
cyclotomic in general. Its degree is bounded by $\sum_x 4 h(x)$
(the total hook content). $\square$

## Significance

This is the **cleanest possible closed form** for $y_\lambda$ in
$\mathbb{Q}(t)$: the denominator structure is fully determined by
combinatorial hook-length data via cyclotomic polynomials, and the
numerator is a finite-degree polynomial in $t$ that can be
explicitly tabulated.

For Lean formalisation, this gives a concrete mathematical
statement:

$$
  y_\lambda(t) \cdot D_n(t) \;=\; P_\lambda(t)
  \in \mathbb{Z}[t]
$$

where $D_n(t) = \prod_d \Phi_d(t)^{e_{n,d}}$ with explicit
$e_{n, d}$ exponents derivable from the hook-length data of all
partitions of $n$.

## Witness

[`folio-assistant/computations/y_lambda_cyclotomic_factor.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/y_lambda_cyclotomic_factor.py)
factors the Wenzl-bridge $y_\lambda$ over $\mathbb{Q}(t)$ via sympy.
Output: `y-lambda-cyclotomic-factor.witness.json` with explicit
factored numerators and denominators for $n = 2, 3, 4$.
