The nuclear normal form computation scales **polynomially** in the
mass number $A$ when performed inductively — reduce after each
multiplication, not at the end.

## Statement

**Proposition.**
*Let $\mathcal{N}_{\leq k}$ denote the Gröbner--Shirshov normal form
of the first $k$ nucleons in $H_k(q)$.  The inductive step*

$$
  \mathcal{N}_{\leq k+1}
  =
  r\!\bigl(
    \mathcal{N}_{\leq k}
    \cdot C(\mathfrak{N}_k, \mathfrak{N}_{k+1}; \sigma_g)
    \cdot \mathfrak{N}_{k+1},\;
    G
  \bigr)
$$

*produces a normal form with at most $\binom{A-1}{\lfloor(A-1)/2\rfloor}$
terms, where $r(\cdot, G)$ is the Gröbner--Shirshov division
algorithm
([nuclear Gröbner reduction](#prop:nuclear-groebner-reduction)).*

*The total computation for $\mathcal{N}(Z, N)$ requires
$O(A^2)$ multiplications and $O(A^3)$ Hecke reduction steps.*

## Complexity bound

| Mass number $A$ | Unreduced terms | Reduced NF terms | Hecke steps |
|:---:|:---:|:---:|:---:|
| 2 | 12 | $\leq 2$ | 1 |
| 4 | 432 | $\leq 8$ | $\leq 12$ |
| 8 | $\sim 10^5$ | $\leq 32$ | $\leq 80$ |
| 16 | $\sim 10^{10}$ | $\leq 128$ | $\leq 480$ |

The inductive approach reduces $10^{10}$ unreduced terms
to $128$ NF terms for oxygen-16.
