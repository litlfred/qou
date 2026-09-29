**Conjecture.**
*The word-length histogram of the quotient atom NF is palindromic (Poincaré-dual) if and only if all occupied sub-shells have angular momentum $\ell = 0$ ($s$-type). Palindromicity breaks at the first electron with $\ell \geq 1$ ($p$-type or higher).*

## Computational evidence

From the [quotient atom model](#conj:shell-closure-nf-term-count), the palindromicity status at each $Z$:

See [Table 1](#tbl:palindromicity-orbital-type-table1-data).

**Transition at $Z = 5$**: the first $p$-electron breaks palindromicity. Through $Z = 4$ (pure $s$-shells), the histogram is perfectly symmetric.

## Physical interpretation

Palindromicity of the NF histogram is Poincaré duality in the Bruhat lattice of $S_{Z+1}$. The word-length distribution $\{n_0, n_1, \ldots, n_L\}$ satisfies $n_k = n_{L-k}$. This duality holds when the NF occupies a self-dual sub-lattice. This happens precisely when the electron chain has no angular momentum (pure $s$-orbitals).

The $p$-electron introduces a chiral crossing that breaks the left-right symmetry of the braid word. In the Hecke algebra, this corresponds to a representation that is not self-dual under the longest-element involution $w \mapsto w_0 w$.

## Conjectured grading

The degree of palindromic defect is the minimum number of histogram entries that must be removed to restore palindromicity. This should equal $2\ell$, where $\ell$ is the angular momentum quantum number of the outermost occupied sub-shell:

See [Table 2](#tbl:palindromicity-orbital-type-table2-data).

This provides a purely algebraic definition of orbital angular momentum: $\ell$ is half the palindromic defect of the Hecke algebra NF histogram.
