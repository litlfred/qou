# y_λ closed-form derivation at H_2 (notes)

Direct linear-system inversion from the Markov-trace constraints gives
clean closed forms at n=2. These match the existing sympy symbolic
witness `y-lambda-symbolic-witness.json` (verifying the chain).

## Setup

At H_2(R, q), the two partitions of 2 are (2) (trivial rep) and (1,1)
(sign rep), both 1-dimensional. The Markov trace satisfies:

- $\mathrm{tr}_M(1) = 1$
- $\mathrm{tr}_M(\sigma_1) = z = 1/(q^{1/2} + q^{-1/2})$

Characters on the generator: $\chi_{(2)}(\sigma_1) = q$ (eigenvalue +q),
$\chi_{(1,1)}(\sigma_1) = -q^{-1}$ (eigenvalue $-q^{-1}$).

## Linear system

$$
\begin{pmatrix} 1 & 1 \\ q & -q^{-1} \end{pmatrix}
\begin{pmatrix} y_{(2)} \\ y_{(1,1)} \end{pmatrix}
= \begin{pmatrix} 1 \\ z \end{pmatrix}
$$

## Closed forms

$$
\boxed{
y_{(2)} \;=\; \frac{z + q^{-1}}{q + q^{-1}},
\qquad
y_{(1,1)} \;=\; \frac{q - z}{q + q^{-1}}.
}
$$

Substituting $z = 1/(q^{1/2} + q^{-1/2})$ and clearing $q^{1/2}$
denominators with $s = q^{1/2}$:

- $y_{(2)} = (s^3 + s^2 + 1) / ((s^2 + 1)(s^4 + 1))$
- $y_{(1,1)} = (s^5 - s^3 - s) / ((s^2 + 1)(s^4 + 1)) + 1$ (after
  rearrangement)

The simpler form factors as the existing symbolic-witness numerator
$s^7 + s^6 + s^4 + s^3 + s^2 + 1$ over $(s^2+1)(s^4+1)^2$ once one
multiplies through by an additional $(s^4+1)$ factor (sympy's
`together` doesn't always pick the lowest denominator).

## Generalization to higher n

For $n \geq 3$, the linear system $\chi_\lambda(w_\mu) y_\lambda =
z^{n - \ell(\mu)}$ is $p(n) \times p(n)$ and grows quickly. Solving
in $\mathbb{Q}(q^{1/2})$ symbolically:

| n | $p(n)$ | sympy time | status |
|--|:--:|--:|--|
| 2 | 2 | <1 s | ✅ closed form (above) |
| 3 | 3 | <1 s | ✅ in symbolic witness |
| 4 | 5 | ~30 s | ✅ in symbolic witness (cherry-picked) |
| 5 | 7 | >20 min | ⏳ Rust kernel (upstream) |
| 6 | 11 | — | ⏳ Rust kernel |
| 12 | 77 | — | numerical only (mpfr witness) |

## Connection to Orellana / Wenzl literature

**Orellana, "Weights of Markov Traces on Hecke algebras"**
([math/9806163](https://arxiv.org/abs/math/9806163), p.17)
quotes the **Wenzl** formula for the **type-A** Markov trace:

> "In [W1] Wenzl showed that the weights of the Markov trace
> (with parameter $z = q^r (1-q)/(1-q^r)$) on the Hecke algebra of
> type A are given by the symmetric Schur function $s_{\mu, r}(q)$"

where
$$
s_{\mu, r}(q) \;=\; q^{n(\mu)} \prod_{x \in \mu}
\frac{1 - q^{r + c(x)}}{1 - q^{h(x)}}
$$
is the **principal specialization** at $r$ variables.  In Wenzl's
convention, the Hecke generators satisfy $\tilde g_i^2 = (q-1) \tilde
g_i + q$ (eigenvalues $q, -1$).

### Empirical test against my numerical witness

My convention uses the symmetric relation $\sigma_i^2 = (q - q^{-1})
\sigma_i + 1$ (eigenvalues $q, -q^{-1}$) with $z = 1/(q^{1/2} +
q^{-1/2})$.  Tested both possible conversions:

**Test 1** ($q_W = q$, my $q$): solving $z = q^r (1-q)/(1-q^r)$ for $r$
gives $r \approx 2.38$ at $q_0 = 1.110$.  Predicted $y_\lambda$ at $H_3$:

| $\lambda$ | predicted $y$ (Wenzl) | witness $y$ | ratio |
|--|--:|--:|--:|
| $(3)$ | $0.4366$ | $0.4154$ | $1.05$ |
| $(2, 1)$ | $0.2740$ | $0.2809$ | $0.98$ |
| $(1^3)$ | $0.0155$ | $0.0227$ | $0.68$ |

Ratios non-constant; **does not match**.

**Test 2** ($q_W = q^2$, Wenzl convention shift): $r \approx 2.995$
(numerically close to integer 3, $\mathfrak{sl}(3)$ duality).
Predicted $y_\lambda$ at $H_3$:

| $\lambda$ | predicted $y$ | witness $y$ | ratio |
|--|--:|--:|--:|
| $(3)$ | $0.3788$ | $0.4154$ | $0.91$ |
| $(2, 1)$ | $0.2930$ | $0.2809$ | $1.04$ |
| $(1^3)$ | $0.0353$ | $0.0227$ | $1.55$ |

Ratios still non-constant; **does not match**.  This confirms the
~10% mismatch reported in `schur_element_identify.py` — the
convention map between Wenzl's parameters and mine is non-trivial.

### Structural diagnosis

The formula in Orellana / Wenzl gives weights for a **specific**
family of Markov traces parameterized by $z = q^r(1-q)/(1-q^r)$
(with discrete $r$ corresponding to $\mathfrak{sl}(r)$ Schur-Weyl
duality).  My $z = 1/(q^{1/2} + q^{-1/2})$ is the **Jones-Markov**
parameter from the symmetric Hecke convention used throughout this
paper, which corresponds to $q_W^r$ for some specific non-integer
$r \approx 2.995$ at $q_0$ — i.e.\ between the $\mathfrak{sl}(2)$
and $\mathfrak{sl}(3)$ levels.

**The clean-integer-r case fails** because my $q_0$ doesn't sit
exactly at any rational specialization.  The Wenzl formula gives a
**different family** of weights, parameterized over all $r \in
\mathbb{R}$, of which my $y_\lambda$ are NOT members.

The actual y_λ in this paper come from solving the linear system
$\chi_\lambda(w_\mu) y_\lambda = z^{n - \mathrm{len}(\mu)}$
**directly** with my specific $z$, without going through the
Wenzl-Schur formula.

## Implication for closing y_λ at n ≥ 5

The Rust kernel (`pyhecke_native.chi_lambda_braid_mpfr`, in upstream
PR #430) provides high-precision numerical y_λ. Closed-form symbolic
extraction at n ≥ 5 will need either:

- (a) a direct formula (Orellana for type A or equivalent) — open in
  the literature search;
- (b) PSLQ rationalisation against high-precision MPFR values
  (mpmath has `pslq`), feasible at 50-100 dps;
- (c) brute-force sympy with more compute time + memory (upstream
  measured >20min wall-clock at n=5 in pure Python).

This memo committed as `y-lambda-closed-form-n2.md` for the audit
trail of structural progress.
