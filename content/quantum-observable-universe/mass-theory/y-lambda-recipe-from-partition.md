**Proposition (recipe: $\lambda \mapsto y_\lambda(q)$ as q-rational).**
*Given a partition $\lambda \,\vdash\, n$, the Jones-Markov central
coefficient $y_\lambda(q)$ is determined by the following algorithm,
yielding a rational function in $\sqrt q$ with cyclotomic
denominator.*

## Step 1: Compute partition data

For each cell $(i, j) \in \lambda$ (1-indexed, $i$ = row, $j$ = column):

- **Content** $c(i, j) := j - i$
- **Hook length** $h(i, j) := \mathrm{arm}(i, j) + \mathrm{leg}(i, j) + 1$
  where $\mathrm{arm}(i, j) := \lambda_i - j$ (cells right of $(i, j)$
  in row $i$) and $\mathrm{leg}(i, j) := |\{r > i : \lambda_r > j\}|$
  (cells below $(i, j)$ in column $j$).

Define $n(\lambda) := \sum_i (i - 1) \lambda_i$.

## Step 2: Compute the universal $X$ substitution

Let $z := 1/(\sqrt q + 1/\sqrt q)$ (Markov parameter). Then

$$
  z \;=\; \frac{\sqrt q}{q + 1},
  \qquad
  q \cdot z \;=\; \frac{q^{3/2}}{q + 1},
$$

and the Wenzl-bridge level $r$ satisfies $q \cdot z = Q^r (1 - Q) /
(1 - Q^r)$ with $Q := q^2$. Solving:

$$
  \boxed{\;
    X \;:=\; Q^r \;=\; \frac{q^{3/2}}{1 + q - q^2 - q^3 + q^{3/2}}.
  \;}
$$

Numerically at $q_0 \approx 1.110$: $X \approx 1.7203$.

## Step 3: Compute the Schur principal-specialisation

For partition $\lambda$, define

$$
  \boxed{\;
    s_{\lambda, r}(Q) \;=\; Q^{n(\lambda)} \cdot
    \prod_{(i, j) \in \lambda}
    \frac{1 - X \cdot Q^{c(i, j)}}{1 - Q^{h(i, j)}}
  \;}
$$

with $Q = q^2$ and $X$ from Step 2.  Each cell contributes one
factor of the form $(1 - X \cdot q^{2 c}) / (1 - q^{2 h})$ — both
polynomial in $\sqrt q$ after substitution.

## Step 4: Normalise

Compute the **partition-function denominator**

$$
  Z_n \;:=\; \sum_{\mu \,\vdash\, n} d_\mu \cdot s_{\mu, r}(Q),
$$

where $d_\mu = f^\mu$ is the classical $S_n$-irrep dimension via
hook-length formula

$$
  f^\mu \;=\; \frac{n!}{\prod_{(i, j) \in \mu} h(i, j)}.
$$

Then

$$
  \boxed{\;
    y_\lambda(q) \;=\; \frac{s_{\lambda, r}(Q)}{Z_n}.
  \;}
$$

## Step 5: Factor over $\mathbb{Q}$ in $\sqrt q$

Substitute $X = q^{3/2} / (1 + q - q^2 - q^3 + q^{3/2})$ explicitly
and reduce via cancellation. The denominator factors as a pure
product of cyclotomic polynomials in $\sqrt q$:

$$
  D_n(\sqrt q) \;=\; \prod_d \Phi_d(\sqrt q)^{e_{n, d}}
$$

where the exponents $e_{n, d}$ are determined by the hook-length
data of all partitions of $n$ via

$$
  1 - q^k \;=\; \prod_{d \mid 2k} \Phi_d(\sqrt q)
$$

(since $q^k = (\sqrt q)^{2k}$).  The numerator $P_\lambda(\sqrt q)$
is a polynomial encoding the $X$ substitution; it is generally
**not** cyclotomic.

## Worked example: $\lambda = (2)$ at $H_2$

**Step 1**: Cells $(1, 1), (1, 2)$.
- $c(1, 1) = 0$, $c(1, 2) = 1$.
- $h(1, 1) = 2$, $h(1, 2) = 1$.
- $n((2)) = 0$.

**Step 2**: $X = q^{3/2} / (1 + q - q^2 - q^3 + q^{3/2})$.

**Step 3**: $Q^0 = 1$, so

$$
  s_{(2), r}(Q) \;=\; \frac{(1 - X)(1 - X \cdot Q)}{(1 - Q^2)(1 - Q)}.
$$

**Step 4**: Other partition is $(1, 1)$ with $n = 1$, contents $0, -1$, hooks $2, 1$:

$$
  s_{(1, 1), r}(Q) \;=\; \frac{Q (1 - X)(1 - X / Q)}{(1 - Q^2)(1 - Q)}.
$$

$d_{(2)} = d_{(1, 1)} = 1$, so

$$
\begin{aligned}
  Z_2 &= s_{(2)} + s_{(1, 1)}
       = \frac{(1 - X)\bigl[(1 - XQ) + Q(1 - X/Q)\bigr]}{(1 - Q^2)(1 - Q)} \\
      &= \frac{(1 - X)(1 + Q)(1 - X)}{(1 - Q^2)(1 - Q)}
       = \frac{(1 - X)^2}{(1 - Q)^2}.
\end{aligned}
$$

**Step 5**: $y_{(2)}(q) = s_{(2)} / Z_2 = (1 - X q^2) / ((1 - X)(1 + q^2))$.

After substituting $X$ and factoring over $\mathbb{Q}$ in $\sqrt q$:

$$
  \boxed{\;
    y_{(2)}(q) \;=\;
    \frac{(\sqrt q)^3 + (\sqrt q)^2 + 1}
         {\Phi_4(\sqrt q) \, \Phi_8(\sqrt q)}
    \;=\;
    \frac{q^{3/2} + q + 1}{(q + 1)(q^2 + 1)}.
  \;}
$$

(Using $\Phi_4(\sqrt q) = q + 1$ and $\Phi_8(\sqrt q) = q^2 + 1$.)

## Numerical sanity at $q_0 \approx 1.110$

$y_{(2)}(q_0) = (1.1097 + 1.110 + 1) / ((1.110 + 1)(1.232 + 1))
             = 3.220 / (2.110 \cdot 2.232) = 3.220 / 4.708 = 0.6839$ ?

Re-evaluating exactly: $q^{3/2} \approx 1.169$, so the numerator
is $1.169 + 1.110 + 1 = 3.279$ and the denominator is
$2.110 \cdot 2.232 = 4.710$, giving $y_{(2)} \approx 0.6963$, in
agreement with the witness value $0.69632542$.

## Algorithm summary (pseudocode)

```
function y_lambda(λ):
    # Step 1
    cells   = [(i, j) for i in 1..len(λ), j in 1..λ[i]]
    content = j - i for each cell
    hook    = arm + leg + 1 for each cell
    n_lam   = Σ (i-1) λ_i

    # Step 2 (universal)
    X = q^(3/2) / (1 + q - q² - q³ + q^(3/2))

    # Step 3
    s_λ = q^(2 n_lam) · ∏ (1 - X·q^(2c)) / (1 - q^(2h))

    # Step 4
    Z_n = Σ_µ (n! / ∏ h_µ) · s_µ
    y_λ = s_λ / Z_n

    # Step 5 (optional cleanup)
    return factor_over_Q_in_sqrt_q(y_λ)
```

This is **fully mechanical**: any partition $\lambda$ at any $n$
yields its $y_\lambda(q)$ in closed q-rational form via this recipe
in $O(p(n) \cdot \max \text{hooks})$ time.

## Code

[`computations/y_lambda_recipe_from_partition.py`](https://github.com/litlfred/qou/blob/main/computations/y_lambda_recipe_from_partition.py)
implements the full recipe end-to-end; takes a partition as input
and returns $(P_\lambda, D_n)$ in $\sqrt q$ with cyclotomic
denominator.
