# Hand-derived clean closed forms for $y_\lambda$ at small $n$

Using the Wenzl-bridge formula
([prop:y-lambda-closed-form-wenzl-bridge](#prop:y-lambda-closed-form-wenzl-bridge))
with the explicit substitution

$$
  X \;=\; Q^r \;=\; \frac{q^{3/2}}{1 + q - q^2 - q^3 + q^{3/2}},
  \qquad Q = q^2,
$$

the central coefficients $y_\lambda$ admit very clean
**hand-derivable** closed forms at small $n$.  Sympy's
automatic `together` / `cancel` does **not** find these reductions
— they require manual algebra exploiting cancellations with the
denominator $Z = \sum_\mu d_\mu \, s_{\mu, r}(Q)$.

## $n = 0$ (empty)

The empty partition has $y_\emptyset = 1$ by convention
(normalisation).

## $n = 1$ (single)

Only one partition $(1)$, $\dim = 1$. Markov-trace normalisation
$\mathrm{tr}_M(1_{H_1}) = 1$ forces

$$
  \boxed{\;y_{(1)} \;=\; 1.\;}
$$

## $n = 2$ (clean two-line derivation)

Two partitions: $(2), (1,1)$, both dim 1. Schur elements:

$$
  s_{(2),r}(Q) = \frac{(1 - X)(1 - X Q)}{(1 - Q^2)(1 - Q)}, \qquad
  s_{(1,1),r}(Q) = \frac{Q (1 - X)(1 - X/Q)}{(1 - Q^2)(1 - Q)}.
$$

Sum:

$$
\begin{aligned}
  Z_2 &= s_{(2)} + s_{(1,1)}
       = \frac{(1 - X)\bigl[(1 - XQ) + Q(1 - X/Q)\bigr]}{(1 - Q^2)(1 - Q)} \\
      &= \frac{(1 - X)(1 + Q)(1 - X)}{(1 - Q^2)(1 - Q)}
       = \frac{(1 - X)^2}{(1 - Q)^2}.
\end{aligned}
$$

Hence

$$
  \boxed{\;
    y_{(2)} = \frac{1 - X q^2}{(1 - X)(1 + q^2)}, \qquad
    y_{(1,1)} = \frac{q^2 - X}{(1 - X)(1 + q^2)}.
  \;}
$$

Plancherel completeness:
$y_{(2)} + y_{(1,1)} = \dfrac{(1 + q^2)(1 - X)}{(1 - X)(1 + q^2)} = 1$ ✓

Numerical at $q_0 \approx 1.110$, $X \approx 1.7203$:
$y_{(2)} \approx 0.6963$, $y_{(1,1)} \approx 0.3037$.

## $n = 3$ — hand-simplification not as compact

At $n = 3$ the analogous sum doesn't telescope to a single ratio.
The witness `y-lambda-symbolic-witness.json` records the unsimplified
sympy form (numerator/denominator polynomials of degree $\sim 25$).
Possible compact form: ratio of cyclotomic products, but
hand-derivation requires more bookkeeping.

## $n = 4$ — extremely large unsimplified

77 partitions at $n = 12$ generate denominators of degree $> 80$ in
$q^{1/2}$. The compact form (if any) requires symbolic algebra
beyond sympy's default reduction strategy — likely needs **partial-
fraction expansion in $\Phi_d(q)$** (cyclotomic polynomials), since
all denominators factor through cyclotomic structure (Schur-element
pattern).

## Open: a "telescope" for general $n$?

The clean $n = 2$ result $Z_2 = (1 - X)^2 / (1 - Q)^2$ suggests a
general identity

$$
  Z_n \stackrel{?}{=} \frac{(1 - X)^{?}}{(1 - Q)^{?(n)}}
$$

with combinatorial exponents.  This is the **q-analogue** of the
Frobenius-determinant identity for symmetric-group character
tables.  At $n = 3$ it doesn't simplify to such a form directly;
the more general identity is likely encoded by **Macdonald's hook
formula** for principal specialisations of Schur functions.

If a closed $Z_n$ identity holds, the per-partition $y_\lambda$
forms become trivially compact:
$y_\lambda = s_{\lambda, r} \cdot \prod (1 - Q^h) / (\text{stuff})$.
Open structural project.

## Witness

[`y_lambda_simplified_small_n.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/y_lambda_simplified_small_n.py)
generates symbolic forms via sympy and verifies numerical agreement
with the MPFR / Wenzl-bridge witness at $q_0$ to machine precision.
The hand-derivation above for $n = 2$ produces a much more compact
form than sympy's automatic simplification.
