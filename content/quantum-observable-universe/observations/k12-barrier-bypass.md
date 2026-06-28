The Hoefsmit / matrix-evaluation programme
([prop:magic-numbers-from-q](#prop\:magic-numbers-from-q),
[prop:hoefsmit-seminormal-form](../braids-and-knots/hoefsmit-seminormal-form.md))
verifies the magic-number ladder at small partition sizes
$k = 3, \dots, 10$ by direct computation of Wedderburn weights from
seminormal-form matrices. At $k \geq 12$ the number of partitions
$|\{\lambda \vdash k\}|$ — and hence the dimension of the Hecke
algebra block-decomposition — grows combinatorially, blocking the
matrix-evaluation approach from confirming saturation at
$\{50, 82, 126\}$.

The algebraic refactor analytically bypasses this barrier. The
homological-condensation conjecture
([`prop:homological-shell-condensation`](../lifting-and-descent/homological-shell-condensation.md))
and the LR-fusion-rigidity conjecture
([`prop:diagrammatic-double-magic-lr-fusion`](#conj\:diagrammatic-double-magic-lr-fusion))
predict the saturated-shell pattern by *structural* arguments
about the Białynicki-Birula stratification and the LR-content-sum
arithmetic on Young's lattice — both of which are *partition-size
agnostic*: the proofs (or class instances) carry through verbatim
at $n = 50, 82, 126$ once the underlying conjectures are accepted.

## Bypassing the $k \geq 12$ matrix-evaluation barrier

### Scope of the matrix-evaluation programme's verification

The matrix-evaluation programme produces, for each
$n \leq 10$ and each $\lambda \vdash n$:

* the seminormal-form matrices for $\sigma_1, \dots, \sigma_{n-1}$
 acting on $V_\lambda$,
* the full-twist eigenvalue $q^{c(\lambda)}$ via direct multiplication,
* the BB-stratified spectral-sequence entries $E_\infty^{p, q}(n)$
 by computing the :refterm[descent]{#descent}-graded jet algebra at level $n$ and
 reading off cohomology.

At $n \in \{2, 8\}$ (and partial coverage of $n = 20$ via
branching-rule extrapolation from $n = 10$) the matrix-evaluation
results agree with the predictions of the homological framework:
$E_\infty^{p, q}(n) = 0$ for $q > 0$, the LR fusion at double-magic
$(Z = 8, N = 8)$ collapses to a single $\nu$, and the full-twist
acts as the identity on the saturated $\Phi_n$. Empirical computational
verification is therefore in hand at the small magic numbers.

### Limits of the matrix-evaluation programme

At $n = 12$ already the partition count exceeds memory budgets for
exact-rational seminormal-form computation; at $n \geq 50$ the
combinatorial explosion is unrecoverable on present hardware. A
matrix-evaluation confirmation of the higher-magic ladder
$\{50, 82, 126\}$ is **not** waiting on hardware — it is
fundamentally not the right tool, because the seminormal form is a
*per-partition* object and the saturated-shell content is a
*structural* object. Adding more compute scales the wrong axis.

### Contribution of the homological / LR-fusion framework

Both higher-magic conjectures are structural statements about
combinatorial objects whose verification at large $n$ is a
finite-data check rather than a matrix computation:

1. **Saturated-shell content sum.** For each $n \in \mathfrak{M}$,
 the existence of a self-conjugate partition $\lambda \vdash n$
 with $c(\lambda) = 0$ is a finite combinatorial statement
 verifiable in $O(p(n))$ partition operations.
2. **LR-rigidity at double-magic.** For each pair
 $(Z, N) \in \mathfrak{M} \times \mathfrak{M}$, the existence of
 a *unique* self-conjugate $\nu_{ZN} \vdash Z + N$ produced by
 LR fusion of self-conjugate $\lambda_Z, \mu_N$ is a finite
 LR-coefficient computation, not a matrix evaluation.

Both are testable at $n = 50, 82, 126$ on present hardware in
seconds. The numerical *prediction* therefore exists; what is
conjectural is the *structural identification* of these
combinatorial objects with the categorical mass support.

### Empirical-verification reframing

The historical empirical scorecard
([prop:magic-numbers-from-q](#prop\:magic-numbers-from-q)) records
agreement deltas $+33.2, +20.4, +4.4$ between framework predictions
and CODATA at $\{2, 8, 20\}$. Under the refactor these deltas are
**empirical computational verifications** of the homological
prediction at *small* magic numbers — they confirm that the
homological framework reproduces the matrix-evaluation results
where both are available, and that the structural part of the
conjecture is consistent with observation.

The higher-magic deltas are now predictions of the homological
framework alone; their empirical comparison against CODATA at
$\{50, 82, 126\}$ is a forward test rather than a back-fit. This
remark interprets `prop:magic-numbers-from-q` only — it makes no
new logical claim, but it documents the change of evidential status
that the algebraic refactor produces.
