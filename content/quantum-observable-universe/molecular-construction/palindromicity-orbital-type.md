**Conjecture.**
*The word-length histogram of the quotient atom NF is palindromic (Poincaré-dual) if and only if all occupied sub-shells have angular momentum $\ell = 0$ ($s$-type). Palindromicity breaks at the first electron with $\ell \geq 1$ ($p$-type or higher).*

## Computational evidence

The palindromicity status at each $Z$ evaluates under the [quotient atom model](#conj:shell-closure-nf-term-count) as follows:

See [Table 1](#tbl:palindromicity-orbital-type-table1-data).

A transition occurs at $Z = 5$. The first $p$-electron breaks palindromicity. Through $Z = 4$ (pure $s$-shells), the histogram exhibits perfect symmetry.

## Physical interpretation

Palindromicity of the NF histogram corresponds to Poincaré duality in the Bruhat lattice of $S_{Z+1}$. The word-length distribution $\{n_0, n_1, \ldots, n_L\}$ satisfies $n_k = n_{L-k}$. This duality holds when the NF occupies a self-dual sub-lattice. This condition is met precisely when the electron chain carries no angular momentum (pure $s$-orbitals).

The $p$-electron introduces a chiral crossing. This breaks the left-right symmetry of the braid word. In the Hecke algebra, this corresponds to a representation that fails to be self-dual under the longest-element involution $w \mapsto w_0 w$.

## Conjectured grading

We define the degree of palindromic defect as the minimum number of histogram entries requiring removal to restore palindromicity. This defect should equal $2\ell$, where $\ell$ is the angular momentum quantum number of the outermost occupied sub-shell:

See [Table 2](#tbl:palindromicity-orbital-type-table2-data).

This yields a purely algebraic definition of orbital angular momentum. We identify $\ell$ as half the palindromic defect of the Hecke algebra NF histogram.
