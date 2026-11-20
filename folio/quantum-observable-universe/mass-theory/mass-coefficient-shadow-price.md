*Each coefficient of the QOU mass formula
([six-term mass formula](#conj:six-term-mass-formula-complete))
is the shadow price (LP dual variable) of the corresponding
partition's Frobenius positivity constraint in a
partition-indexed operator-selection program.*

**Note (scope of the program).** The statement is about a program whose
Frobenius positivity constraints are indexed by **partitions** $\lambda \vdash n$
— one per Wedderburn block. It is **not** a claim about
[the operator-selection LP](#prop:operator-selection-lp) as that block states
it, which indexes its constraints by **NF basis element** ($d = n!$ of them, so
six against three partitions at $n = 3$). Two consequences follow, and neither
is a claim that the coefficients are wrong:

1. **The net-constraint dual of the NF-indexed LP is identically zero.** Since
   the NF basis contains the identity, its first Frobenius row *is* the
   objective vector, so that program minimises $t \cdot x$ subject to
   $t \cdot x \ge 0$; its optimal value is $0$ for every $n_{\mathrm{target}}$,
   and by strong duality $y_0^\ast = 0$. Any quantity recovered by dividing by
   $y_0^\ast$ is undefined — see
   [the degeneracy section](#prop:operator-selection-lp).
2. **The per-partition Frobenius duals are a separate question and are not
   contradicted.** At $H_3$ the committed partition-indexed solve gives
   $y^\ast_{(3)} = y^\ast_{(2,1)} = 1$ and $y^\ast_{(1^3)} = 0$, so
   $c_\lambda = y^\ast_\lambda\, m_e$ is satisfiable on the nonzero blocks. The
   vanishing block is the $\mathrm{SU}(2)$ specialisation, not a failure of the
   pairing: every $\ell(\lambda) \ge 3$ weight vanishes identically, which is
   why a partition-indexed program must be posed on the two-row quotient.

**Note (what the binding compute actually calls).** The function named for this
proposition, `hecke_core_legacy.lp_shadow_price`, evaluates
$y_\lambda = w_\lambda/d_\lambda - 1/[k]_q!$ in closed form and **solves no
program**. Its $1/[k]_q!$ term is $\min_\lambda (w_\lambda/d_\lambda)$, so it
subtracts a constant that zeroes exactly the two one-dimensional blocks
$(k)$ and $(1^k)$ at every level; it is not the dual variable of any
normalisation constraint, and it is not $y_0^\ast$, which is $0$.
