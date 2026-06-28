Per user direction: "per-irrep character differences should factor
via $\Phi_d(q)$ with $d$ tied to the irrep's content sum / Frobenius
rank". The closed-form data from
[`rem:chi-per-irrep-cyclotomic-closed-forms`](#rem:chi-per-irrep-cyclotomic-closed-forms)
exposes a **specific pattern**: for each partition $\lambda \vdash n$,

$$
  \boxed{\,
    d_\lambda \;=\; 4 \cdot f_\lambda
   \,}
$$

where $f_\lambda = n! / H(\lambda)$ is the **number of standard
Young tableaux** of shape $\lambda$ (equivalently, the dimension of
$V_\lambda$ as a representation of $S_n$), so that the per-irrep
character difference factors through the cyclotomic polynomial
$\Phi_{d_\lambda}(q)$.

## n = 3 verification

| $\lambda$ | $H(\lambda)$ | $f_\lambda = 3!/H$ | $d_\lambda = 4 f_\lambda$ | $\Phi_{d_\lambda}(q)$ | observed factor |
|---|---:|---:|---:|---|---|
| $(3)$ | $6$ | $1$ | $4$ | $q^2 + 1$ | $\Phi_4(q)^2$ |
| $(2,1)$ | $3$ | $2$ | $8$ | $q^4 + 1$ | $\Phi_8(q)^1$ |
| $(1,1,1)$ | $6$ | $1$ | $4$ | $q^2 + 1$ | $\Phi_4(q)^2$ |

All three match the proved closed-form numerators
$-(q^2-1) \cdot \Phi_{d_\lambda}^{m_\lambda}$ exactly.

## Multiplicity formula

The exponent $m_\lambda$ satisfies (at $n = 3$, total numerator degree 6 over $(q^2-1)$ degree 2):

$$
  m_\lambda \cdot \varphi(d_\lambda) \;=\; 4
  \qquad (\text{total cyclotomic degree, fixed at 4 by typed-}B_3\text{ word length})
$$

Verified:

- $V_{(3)}$: $\varphi(4) = 2$, $m_{(3)} = 4/2 = 2$ (yes)
- $V_{(2,1)}$: $\varphi(8) = 4$, $m_{(2,1)} = 4/4 = 1$ (yes)
- $V_{(1,1,1)}$: $\varphi(4) = 2$, $m_{(1,1,1)} = 4/2 = 2$ (yes)

## Predicted cyclotomic structure at $n = 4$

The conjecture extrapolates to the five $H_4(q)$ irreps:

| $\lambda \vdash 4$ | $H(\lambda)$ | $f_\lambda$ | $d_\lambda = 4 f_\lambda$ | $\Phi_{d_\lambda}(q)$ |
|---|---:|---:|---:|---|
| $(4)$ | $24$ | $1$ | $4$ | $q^2 + 1$ |
| $(3,1)$ | $8$ | $3$ | $12$ | $q^4 - q^2 + 1$ |
| $(2,2)$ | $12$ | $2$ | $8$ | $q^4 + 1$ |
| $(2,1,1)$ | $8$ | $3$ | $12$ | $q^4 - q^2 + 1$ |
| $(1,1,1,1)$ | $24$ | $1$ | $4$ | $q^2 + 1$ |

Testing this is the next concrete R&D step: extend
`probe_per_wedderburn_block_ck.py` from n=3 to n=4 with the
canonical typed-B_4 braid recipe.

## Lean theorems exported

| theorem | content |
|---|---|
| `chi_V3_numerator_matches` | conjecture's V_(3) numerator = proved closed-form numerator |
| `chi_V21_numerator_matches` | conjecture's V_(2,1) numerator = proved closed-form numerator |
| `chi_V111_numerator_matches` | conjecture's V_(1,1,1) numerator = proved closed-form numerator |
| `class PhiD4FConjecture (n λ_syt_count q)` | abstract conjecture class with $d_\lambda$ field + residual |
| `instance phiDConj_V3, phiDConj_V21, phiDConj_V111` | n=3 discharges |

All sorry-free, closed by `ring` after unfolding.
