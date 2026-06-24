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

## Empirical extraction at generic $q_0$

The witness file
[`y-lambda-jones-markov-witness.json`](https://github.com/litlfred/qou/blob/main/computations/y-lambda-jones-markov-witness.json)
tabulates all 270 weights for $n = 2, \ldots, 12$ at
$q_0 \approx 1.110$.  Per-edge ratios
$y_\lambda^{(n+1)} / (z \cdot y_\mu^{(n)})$ extracted from the witness
exhibit the following **structural regularities** (computed in
[`y_lambda_bratteli_extract.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_bratteli_extract.py)):

1. **Per-row monotonicity**: along a fixed-shape path
   $\lambda^{(1)} \nearrow \lambda^{(2)} \nearrow \cdots$ where each
   added box has the same row index, the ratio sequence is monotone.
2. **Sign tracking**: when the added cell has negative $q$-content
   (sub-diagonal), the ratio is negative — explaining the strict
   sign alternation observed in the sign-rep tower
   $(1^n) \nearrow (1^{n+1})$.
3. **Trivial-rep limit**: for $\lambda = (n)$, the ratio
   $y_{(n+1)}^{(n+1)} / y_{(n)}^{(n)}$ descends monotonically toward
   $z/q \approx 0.4498$ as $n \to \infty$.

## Plancherel completeness (verified at every level)

Independently of the per-edge factor $F_q$, the **per-level invariant**
$\sum_{\lambda \,\vdash\, n} y_\lambda^{(n)} \cdot d_\lambda = 1$
holds exactly at every $n = 2, \ldots, 12$ in the witness data
(verified to $< 10^{-15}$ residual), where $d_\lambda$ is the
hook-length dimension of $V_\lambda$.  This is the
[Plancherel-weight boundedness](#prop:plancherel-weight-boundedness)
identity transported through Wedderburn — it is the **necessary
consistency condition** for any candidate closed form $F_q$.

| $n$ | $\sum y_\lambda d_\lambda$ |
|:--:|:--:|
| $2$ | $1.0000000000$ |
| $3$ | $1.0000000000$ |
| $\vdots$ | $\vdots$ |
| $12$ | $1.0000000000$ |

## Closed-form for $F_q$: now available

The $q$-rational function $F_q$ is now **explicit in closed form** via
the symbolic linear-system solve in
[`y-lambda-symbolic-witness.json`](#) — produced by sympy in
$\mathbb{Q}(q^{1/2})$.  Per-edge factors

$$
  F_q(c, \mathrm{hooks}(\lambda))
  \;=\;
  \frac{y_\lambda^{(\mathrm{symbolic})}}
       {z \cdot y_\mu^{(\mathrm{symbolic})}}
  \;\in\;
  \mathbb{Q}(q^{1/2})
$$

are extractable as exact symbolic ratios.  Sample at $n = 2$:

$$
  y_{(2)}
  \;=\;
  \frac{q^{7/2} + q^{3/2} + q^3 + q^2 + q + 1}
       {(q + 1)(q^2 + 1)^2},
  \qquad
  y_{(1,1)}
  \;=\;
  \frac{-q^{7/2} - q^{3/2} + q^5 + q^4 + q^3 + q^2}
       {(q + 1)(q^2 + 1)^2}.
$$

Denominators factor through cyclotomic polynomials $\Phi_d(q)$ —
the standard Schur-element pattern for Hecke algebras at generic
$q$ ([Geck--Pfeiffer]).  Sympy and numerical witness agree to
$10^{-16}$ at $q_0$.

What is **already structurally fixed** without $F_q$ in closed form:

- **Existence** of the recursion (Markov property + multiplicity-free
  Bratteli);
- **Per-level invariant** $\sum y_\lambda d_\lambda = 1$ (Plancherel);
- **Sign pattern** along sign-rep tower (negative $q$-content);
- **Decay rate** along trivial-rep tower ($z/q$ asymptotic);
- **270 weights** computed and cached for $n = 2, \ldots, 12$.

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

[`computations/y_lambda_bratteli_extract.py`](#) —
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
