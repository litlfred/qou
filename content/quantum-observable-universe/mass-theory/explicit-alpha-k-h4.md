**Proposition (explicit $\alpha_\lambda(H_4)$ — closed forms in $\mathbb{Q}(q)$).**
*Let $z = 1/(\sqrt q + 1/\sqrt q)$ be the Markov parameter and
$\{T_{w_C}\}_C$ canonical Hecke representatives of the $p(4) = 5$
conjugacy classes of $S_4$:*

| label | cycle type | reduced word $w_C$ | length |
|--|:--:|:--:|:--:|
| $C_0 = e$ | $1^4$ | $\emptyset$ | $0$ |
| $C_1$ | $2 \cdot 1^2$ | $\sigma_1$ | $1$ |
| $C_2$ | $2^2$ | $\sigma_1 \sigma_3$ | $2$ |
| $C_3$ | $3 \cdot 1$ | $\sigma_1 \sigma_2$ | $2$ |
| $C_4$ | $4$ | $\sigma_1 \sigma_2 \sigma_3$ | $3$ |

*For each partition $\lambda \,\vdash\, 4$, the Wedderburn-orthogonal
representative $r_\lambda = \sum_C c_C \cdot T_{w_C}$ satisfying
$\chi_\mu(r_\lambda) = 0$ for every $\mu \neq \lambda$ has coefficients
$c_C(\lambda) \in \mathbb{Q}(q)$ given by:*

| $\lambda$ | $c_e$ | $c_{(12)}$ | $c_{(12)(34)}$ | $c_{(123)}$ | $c_{(1234)}$ |
|--|--|--|--|--|--|
| $(4)$ | $\dfrac{1}{q^3 \Phi_{(4)}}$ | $\dfrac{q^4 + 2q^2 + 3}{q^2 \Phi_{(4)}}$ | $\dfrac{1}{q(q^2+1)}$ | $\dfrac{q^4 + q^2 + 2}{q (q^4 + q^2 + 1)}$ | $1$ |
| $(3,1)$ | $-\dfrac{1}{q(q^2+1)}$ | $\dfrac{1 - 2q^2 - q^4}{q^2 (q^2+1)}$ | $\dfrac{1}{q(q^2+1)}$ | $\dfrac{1 - q^2}{q}$ | $1$ |
| $(2,2)$ | $-\dfrac{q^2}{(q^2+1)^2}$ | $\dfrac{q(1-q^2)}{(q^2+1)^2}$ | $-\dfrac{q^4 + q^2 + 1}{(q^2+1)^2}$ | $1$ | $0$ |
| $(2,1,1)$ | $\dfrac{q^3}{q^2+1}$ | $\dfrac{q^4 - 2q^2 - 1}{q^2+1}$ | $-\dfrac{q^3}{q^2+1}$ | $\dfrac{1 - q^2}{q}$ | $1$ |
| $(1^4)$ | $-\dfrac{q^9}{\Phi_{(4)}}$ | $\dfrac{q^4(3q^4 + 2q^2 + 1)}{\Phi_{(4)}}$ | $-\dfrac{q^3}{q^2+1}$ | $\dfrac{q(-2q^4 - q^2 - 1)}{q^4 + q^2 + 1}$ | $1$ |

*where $\Phi_{(4)} = q^6 + 2q^4 + 2q^2 + 1$.*

*The depth-stratum coefficients $\alpha_\lambda(H_4) := \mathrm{tr}_M(r_\lambda)
= y_\lambda \cdot \chi_\lambda(r_\lambda)$ evaluate at the substrate
value $q_0 \approx 1.110$ to numerical values in
[`wedderburn-orthogonal-r-3-h4.witness.json`](https://github.com/litlfred/qou/blob/main/computations/wedderburn-orthogonal-r-3-h4.witness.json),
verified to numerical precision against the Hoefsmit character matrix
and Jones-Markov $y_\lambda$ values (consistency residual $< 10^{-15}$).*

## Significance

This proposition extends the H_3 closure of
[explicit α_k at H_3](#prop:explicit-alpha-k-h3) to H_4, providing
the second concrete data point in the structural derivation of
$\alpha_k(H_n)$ for the unified mass formula.

The dramatic decrease from $\alpha_3(H_3) = h z^2 + z \approx 0.5514$
to $\alpha_3(H_4) \approx 0.003463$ (factor $159$) reflects the
**dilution of the depth-3 stratum** as $n$ grows — at $H_4$ the
depth-3 partition $(1^4)$ has Plancherel weight $y_{(1^4)} \approx
-8.4 \times 10^{-4}$ (sign-indefinite, see
[sign-pattern remark](#rem:y-lambda-sign-pattern)), while at $H_3$
it has weight $y_{(1^3)} \approx 0.0227$.

## Related results

The closed-form $\mathbb{Q}(q)$ expressions for the $r_\lambda$
coefficients are tabulated above (lines 21–31). The closed forms
factor through cyclotomic denominators $(q+1)$, $(q^2+1)^2$,
$q^3 \Phi_{(4)}$, etc. (standard Schur-element pattern). All five
partitions of 4 — including the self-conjugate $(2, 2)$ whose
numerical inverse is ill-conditioned — close via the sympy null-space
solve.

For $H_5$ and $H_6$, all $18$ partitions admit numerical $r_\lambda$
values via the adaptive-gauge selection in
[`r_k_h5_h6_adaptive.py`](#). Symbolic forms for $y_\lambda$ at
$n = 5, \ldots, 12$ are also available via the
[Wenzl bridge](#prop:y-lambda-closed-form-wenzl-bridge)
(270 partitions, 45 seconds total).

## Witness

[`computations/wedderburn_orthogonal_r_k.py`](#) —
implements the class-function basis construction, character
evaluation via `build_seminormal_matrices`, and 4$\times$5 linear-system
solve.  Output:
[`wedderburn-orthogonal-r-3-h4.witness.json`](#).
