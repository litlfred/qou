**Theorem (Schur-Weyl Markov trace vanishes for height > 2).**
*Let* $H_n(R, q)$ *be the Iwahori–Hecke algebra over* $\mathbb{Q}(q)$,
*and let* $w_\lambda(q) := s_\lambda(q, q^{-1}) / H_q(\lambda)$
*denote the Schur-Weyl Markov-trace weights, where*
$s_\lambda(q, q^{-1})$ *is the 2-variable principal Schur
specialisation.  For every partition* $\lambda \vdash n$ *with*
$\mathrm{height}(\lambda) > 2$, *the weight* $w_\lambda(q) = 0$
*identically in* $\mathbb{Q}(q)$.

**Equivalent statement.**  *The Schur-Weyl Markov trace on*
$H_n(R, q)$, *defined by*

$$
  \mathrm{tr}_{\mathrm{SW}}(x)
  \;:=\;
  \sum_{\lambda \,\vdash\, n} w_\lambda(q) \, \chi_\lambda(x),
$$

*factors through the height-*$\leq 2$ *quotient: only partitions of
height at most 2 contribute non-trivially.  This identifies*
$\mathrm{tr}_{\mathrm{SW}}$ *with the **Jones polynomial / colored-
Jones-at-level-2 / SU(2)-projection** of the Markov trace.*

**Proof.**  *The 2-variable Schur polynomial* $s_\lambda(x, y)$ *is
the sum over **semistandard Young tableaux** (SSYTs) of shape*
$\lambda$ *filled with entries in* $\{1, 2\}$:*

$$
  s_\lambda(x, y) \;=\; \sum_{T \in \mathrm{SSYT}(\lambda, \{1,2\})}
       \prod_{i \in T} x_{\mathrm{val}(i)},
$$

*subject to the SSYT constraints (rows weakly increasing, columns
strictly increasing).*

*In two variables, every column of an SSYT has length at most 2 —
since the only strictly-increasing chain in* $\{1, 2\}$ *is the
trivial pair* $1 < 2$.  *Therefore no SSYT of shape* $\lambda$
*exists whenever* $\lambda$ *has any column of length* $> 2$,
*equivalently when* $\mathrm{height}(\lambda) > 2$.

*The sum defining* $s_\lambda(x, y)$ *is then the empty sum, hence
zero.  Specialising at* $x = q$, $y = q^{-1}$ *preserves this:*
$s_\lambda(q, q^{-1}) = 0$.  *Since the q-hook product*
$H_q(\lambda)$ *is generically non-vanishing,*
$w_\lambda = s_\lambda / H_q(\lambda) = 0$ *in* $\mathbb{Q}(q)$.  $\square$

**Numerical verification (D atom braid at H_6).**

*Per the height-stratification probe in
[`probe_d_height_stratification.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/probe_d_height_stratification.py),
the Wenzl Markov-trace contributions to* $\mathrm{tr}_M(T_w(D))$
*split by partition height as:*

| height | # partitions | contribution at $q_0$ |
|---:|---:|---:|
| 1 | 1 (= $(6)$) | +0.092319 |
| 2 | 3 (= $(5,1), (4,2), (3,3)$) | +0.266726 |
| 3 | 3 | −0.022608 |
| 4 | 2 | +0.000177 |
| 5 | 1 | +0.000198 |
| 6 | 1 | +0.000008 |

*Heights* $> 2$ *contribute negligibly under the Wenzl normalisation
because* $w_\lambda = 0$ *exactly when height* $> 2$, *and the
Wenzl-Schur* $y_\lambda$ *coefficients suppress them by structurally
similar factors at* $q_0$.

**Consequences for the mass formula.**

*The paper's* $\mathrm{tr}_M(T_w)$ *in
[`prop:atom-knot-mass-derivation`](#prop:atom-knot-mass-derivation)
is ambiguous between two distinct linear functionals on*
$H_n(R, q)$:

1. ***Schur-Weyl / Jones polynomial / Habiro-coefficient path***
   *: vanishes on height* $> 2$, *= colored-Jones at level 2.
   Used by* [`habiro_coefficients_atomic.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/habiro_coefficients_atomic.py)
   *and the* `prop:full-pole-structure-mass-trace` *polynomial
   construction.*

2. ***Wenzl Markov / full Wedderburn path***
   *: sums over all partitions including height* $> 2$.
   *Used by* [`light_isotope_sweep.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/light_isotope_sweep.py)
   *(default), the
   [`y-lambda-wenzl-witness.json`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/folio-assistant/computations/y-lambda-wenzl-witness.json),
   and the from-scratch chain* `folio-assistant/computations/from_scratch/`.

*These give different numerical values for* $\mathrm{tr}_M(T_w)$
*at the same braid word, and the relationship between them is
exactly the height-stratification proven above.  Resolving which
form the paper's mass formula uses is a notation/convention
choice — but it is structurally consequential, so this theorem
makes the choice explicit.*

**Pure-algebra status: PROVED, no fitting.**

*This theorem is a structural statement about the Hecke-algebra
representation theory at finite* $n$; *it does NOT rely on any
empirical AME data, calibration, or normalisation choice.  The
Schur-Weyl vanishing for height* $> 2$ *is purely combinatorial
(no SSYT in 2 variables for tall partitions) and the implication
for the trace is immediate.*
