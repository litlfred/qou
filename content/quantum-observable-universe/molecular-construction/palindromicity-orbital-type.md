**Conjecture.**
*The word-length histogram of the quotient atom NF is
palindromic (Poincaré-dual) if and only if all occupied
sub-shells have angular momentum $\ell = 0$ ($s$-type).
Palindromicity breaks at the first electron with $\ell \geq 1$
($p$-type or higher).*

## Computational evidence

From the [quotient atom model](#conj:shell-closure-nf-term-count),
the palindromicity status at each $Z$:

| $Z$ | Config | Histogram | Palindromic |
|:----|:-------|:----------|:------------|
| 1 | $1s^1$ | $\{0{:}1,\; 1{:}1\}$ | $\star$ |
| 2 | $1s^2$ | $\{1{:}1,\; 2{:}1\}$ | $\star$ |
| 3 | $[He]\,2s^1$ | $\{1{:}1,\; 2{:}2,\; 3{:}2,\; 4{:}1\}$ | $\star$ |
| 4 | $[He]\,2s^2$ | $\{3{:}1,\; 4{:}2,\; 5{:}2,\; 6{:}1\}$ | $\star$ |
| 5 | $[He]\,2s^2 2p^1$ | $\{3{:}1,\; 4{:}3,\; 5{:}5,\; \ldots\}$ | **no** |
| 6 | $[He]\,2s^2 2p^2$ | $\{7{:}1,\; 8{:}3,\; 9{:}5,\; \ldots\}$ | **no** |

**Transition at $Z = 5$**: the first $p$-electron breaks
palindromicity.  Through $Z = 4$ (pure $s$-shells), the
histogram is perfectly symmetric.

## Physical interpretation

Palindromicity of the NF histogram is **Poincaré duality**
in the Bruhat lattice of $S_{Z+1}$: the word-length
distribution $\{n_0, n_1, \ldots, n_L\}$ satisfies
$n_k = n_{L-k}$.  This duality holds when the NF occupies
a **self-dual sub-lattice** — which happens precisely when
the electron chain has no angular momentum (pure $s$-orbitals).

The $p$-electron introduces a **chiral crossing** that breaks
the left-right symmetry of the braid word.  In the Hecke
algebra, this corresponds to a representation that is not
self-dual under the longest-element involution $w \mapsto w_0 w$.

## Conjectured grading

The **degree of palindromic defect** — the minimum number of
histogram entries that must be removed to restore palindromicity
— should equal $2\ell$, where $\ell$ is the angular momentum
quantum number of the outermost occupied sub-shell:

| Sub-shell | $\ell$ | Defect |
|:----------|:-------|:-------|
| $s$ | 0 | 0 (palindromic) |
| $p$ | 1 | 2 |
| $d$ | 2 | 4 |
| $f$ | 3 | 6 |

This would give a purely algebraic definition of orbital
angular momentum: $\ell$ is half the palindromic defect of the
Hecke algebra NF histogram.
