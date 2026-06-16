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

## General $n$ — resolved by the Macdonald hook-content telescope

**Update (closing the structural project):** the $n = 2$ collapse
$Z_2 = (1 - X)^2 / (1 - Q)^2$ is *not* a coincidence; it is the
$n = 2$ case of the principal specialisation of the
**regular-representation Frobenius identity**
$\sum_{\lambda \vdash n} f_\lambda \cdot s_\lambda = p_1^n$
(Stanley, *EC II* Cor. 7.12.5; Macdonald, *Symmetric Functions*
I.3 ex. 1).  Substituting $p_1 \mapsto (1 - q^r)/(1 - q)$,
$q \mapsto Q$, and identifying $X = Q^r$ gives the **Macdonald
hook-content telescope** at every $n$:

$$
  Z_n \;=\; \left(\frac{1 - X}{1 - Q}\right)^n.
$$

Consequently every $y_\lambda$ admits the single-product closed form

$$
  y_\lambda \;=\; Q^{n(\lambda)}
    \cdot \frac{(1 - Q)^n}{(1 - X)^n}
    \cdot \prod_{x \in \lambda}
      \frac{1 - X \cdot Q^{c(x)}}{1 - Q^{h(x)}}.
$$

This is $O(n)$ work per partition with **no `sympy.simplify`** and
no manual algebra: cell-by-cell evaluation of the hook-content
product is already canonical.  The full statement, proof sketch,
and numerical witness live in
[`prop:macdonald-hook-telescope`](../../content/quantum-observable-universe/braids-and-knots/macdonald-hook-telescope.md).

The previous "ratio of cyclotomic products" framing was a symptom
of doing the algebra without naming the underlying structure: the
telescope *is* the (decategorified) KLR-canonical-basis count of
the regular $S_n$-representation, i.e. the symmetric-crystal
shortcut listed in CLAUDE.md §7b item 2.  Naming the crystal
removes the manual algebra entirely.

## Witnesses

- [`y_lambda_macdonald_telescope.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_macdonald_telescope.py)
  — symbolic verification of the telescope identity for $n = 0,\ldots,8$
  (sympy reduces the difference to exactly $0$); per-partition closed-
  form collapse for $n = 0,\ldots,6$; emits all 272 closed forms for
  $n = 0,\ldots,12$; cross-checks against the MPFR witness with max
  $|\Delta| \approx 2.5 \times 10^{-51}$ across 191 samples.
- [`y-lambda-macdonald-telescope.witness.json`](https://github.com/litlfred/qou/blob/main/computations/y-lambda-macdonald-telescope.witness.json)
  — full output.
- The hand-derived $n = 2$ form above is preserved as the smallest
  worked example.
