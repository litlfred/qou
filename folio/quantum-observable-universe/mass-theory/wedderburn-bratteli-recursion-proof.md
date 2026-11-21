## Proof

Write $t = [2]_q = q + q^{-1}$ and $d = a - b + 1$. The balanced $q$-integers satisfy

$$
  [d+1]_q + [d-1]_q \;=\; t\,[d]_q,
$$

since $(q^{d+1} - q^{-d-1}) + (q^{d-1} - q^{1-d}) = (q + q^{-1})(q^d - q^{-d})$.

*Restriction.* $y_{(a+1,b)} + y_{(a,b+1)} = \bigl([d+1]_q + [d-1]_q\bigr)/t^{a+b+1} = t\,[d]_q / t^{a+b+1} = y_{(a,b)}$.

*Single edge.* Adding a cell to the first row raises $a - b$ by one and the total by one, so $t\,[d]_q\, y_{(a+1,b)} = [d+1]_q\,[d]_q / t^{a+b} = [d+1]_q\, y_{(a,b)}$. The second row is the same with $[d-1]_q$.

Three-row shapes carry weight $0$ under convention D, so the recursion on two-row shapes is the whole recursion. The divisions are by $[2]_q$ and $[d]_q$, non-zero at generic $q$. At $n = 3$ the weights are $([4]_q/[2]_q^3,\; 1/[2]_q^2,\; 0)$. $\square$

The normalisation $\sum_{\lambda \vdash n} f^\lambda y_\lambda = 1$ follows from the restriction form and the branching rule $f^\lambda = \sum_{\mu \nearrow \lambda} f^\mu$; it is not formalised.

> **The sections below are convention-C history.** They were computed with the Markov parameter $z = \sqrt{q}/(q+1)$, excised on 2026-08-15. Under convention D the sign-rep tower weights are $0$, not alternating, and the $n = 2$ weights are $y_{(2)} = [3]_q/[2]_q^2$, $y_{(1,1)} = 1/[2]_q^2$. They are kept as a record, not as statements about the canonical weights.

## Empirical extraction at generic $q_0$

A numerical tabulation lists all 270 weights for $n = 2, \ldots, 12$ at
$q_0 \approx 1.110$.  Per-edge ratios
$y_\lambda^{(n+1)} / (z \cdot y_\mu^{(n)})$ extracted from the witness
exhibit the following **structural regularities** (computed in
the canonical formalism):

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
$q$ ([Geck--Pfeiffer]).  Sympy and canonical witness agree to
$10^{-16}$ at $q_0$.

What is **already structurally fixed** without $F_q$ in closed form:

- **Existence** of the recursion (Markov property + multiplicity-free
  Bratteli);
- **Per-level invariant** $\sum y_\lambda d_\lambda = 1$ (Plancherel);
- **Sign pattern** along sign-rep tower (negative $q$-content);
- **Decay rate** along trivial-rep tower ($z/q$ asymptotic);
- **270 weights** computed and cached for $n = 2, \ldots, 12$.
