# Conjecture: per-irrep character differences factor via $\Phi_{4 f_\lambda}(q)$

The closed-form data from [`rem:chi-per-irrep-cyclotomic-closed-forms`](#rem:chi-per-irrep-cyclotomic-closed-forms) exposes a specific pattern for the per-irrep character differences:

$$
  \boxed{\,
    d_\lambda \;=\; 4 \cdot f_\lambda
   \,}
$$

where $f_\lambda = n! / H(\lambda)$ is the number of standard Young tableaux of shape $\lambda$. This is equivalently the dimension of $V_\lambda$ as a representation of $S_n$. The character differences factor via $\Phi_d(q)$ with $d$ tied to the irrep's content sum or Frobenius rank.

## $n = 3$ verification

| $\lambda$ | $H(\lambda)$ | $f_\lambda = 3!/H$ | $d_\lambda = 4 f_\lambda$ | $\Phi_{d_\lambda}(q)$ | Observed factor |
|---|---:|---:|---:|---|---|
| $(3)$ | $6$ | $1$ | $4$ | $q^2 + 1$ | $\Phi_4(q)^2$ |
| $(2,1)$ | $3$ | $2$ | $8$ | $q^4 + 1$ | $\Phi_8(q)^1$ |
| $(1,1,1)$ | $6$ | $1$ | $4$ | $q^2 + 1$ | $\Phi_4(q)^2$ |

All three match the proved closed-form numerators $-(q^2-1) \cdot \Phi_{d_\lambda}^{m_\lambda}$ exactly.

## Multiplicity formula

At $n = 3$, the total numerator degree is 6 over a $(q^2-1)$ factor of degree 2. The exponent $m_\lambda$ satisfies:

$$
  m_\lambda \cdot \varphi(d_\lambda) \;=\; 4
$$

This total cyclotomic degree is fixed at 4 by the typed-$B_3$ word length. We verify this for each representation:

- $V_{(3)}$: $\varphi(4) = 2$, $m_{(3)} = 4/2 = 2$.
- $V_{(2,1)}$: $\varphi(8) = 4$, $m_{(2,1)} = 4/4 = 1$.
- $V_{(1,1,1)}$: $\varphi(4) = 2$, $m_{(1,1,1)} = 4/2 = 2$.

## Predicted cyclotomic structure at $n = 4$

The conjecture extrapolates to the five $H_4(q)$ irreps:

| $\lambda \vdash 4$ | $H(\lambda)$ | $f_\lambda$ | $d_\lambda = 4 f_\lambda$ | $\Phi_{d_\lambda}(q)$ |
|---|---:|---:|---:|---|
| $(4)$ | $24$ | $1$ | $4$ | $q^2 + 1$ |
| $(3,1)$ | $8$ | $3$ | $12$ | $q^4 - q^2 + 1$ |
| $(2,2)$ | $12$ | $2$ | $8$ | $q^4 + 1$ |
| $(2,1,1)$ | $8$ | $3$ | $12$ | $q^4 - q^2 + 1$ |
| $(1,1,1,1)$ | $24$ | $1$ | $4$ | $q^2 + 1$ |


## Significance

If the conjecture holds at all $n$, it provides a structural prediction for the per-irrep contribution to $\mathrm{tr}_M$ as a function of purely combinatorial partition data ($f_\lambda$, $H(\lambda)$, $c(\lambda)$). Combined with the Wenzl-bridge $y_\lambda$ weights and the precision-ladder $c_k$ extraction, this closes the categorical-chain derivation at every order for arbitrary multi-baryon typed braids. For example, $B_3 \to c_k$ for the proton/neutron, $B_6 \to c_k$ for the deuteron, $B_9 \to c_k$ for tritium or ${}^3$He, and $B_{12} \to c_k$ for the $\alpha$-particle (${}^{4}$He).

This cyclotomic structure also provides a literature bridge to Ariki-Koike cyclotomic Hecke algebras, where Specht modules decompose along $\Phi_d(q)$ factors.

## Lean theorems exported

| Theorem | Content |
|---|---|
| `chi_V3_numerator_matches` | Conjecture's $V_{(3)}$ numerator equals proved closed-form numerator |
| `chi_V21_numerator_matches` | Conjecture's $V_{(2,1)}$ numerator equals proved closed-form numerator |
| `chi_V111_numerator_matches` | Conjecture's $V_{(1,1,1)}$ numerator equals proved closed-form numerator |
| `class PhiD4FConjecture (n λ_syt_count q)` | Abstract conjecture class with $d_\lambda$ field and residual (no instances) |

These theorems are closed by `ring` after unfolding.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs, physical observables, and numerical evaluation at the substrate parameter $q_0$. Generic categorical or $q$-deformation identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
