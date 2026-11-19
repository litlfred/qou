## Terminology: "condensation"

The vanishing $E_\infty^{p, >0}(n) = 0$ dictates that every higher
:refterm[descent]{#descent} residue collapses onto the diagonal. There are no
off-diagonal jet-tower contributions at saturated $n$. The shell
condenses into a single graded piece. For $n \notin \mathfrak{M}$
the off-diagonal pieces survive. They provide the algebraic content of
non-saturation (residual capacity to absorb crossing energy).

The phenomenology this picks up is standard. At
$n \in \mathfrak{M}$ the binding-energy curve flattens, the next
nucleon adds nearly-zero binding, and the shell is mathematically
"full". The refactor identifies this directly in the spectral sequence,
rather than via shell-model fitting.

## Conditional content via the categorical-neutrality conjecture

Conditional on
[categorical neutrality of saturated shells](categorical-neutrality-saturated-shells.md),
the full-twist $\Delta_n^2$ acts as the identity on $\Phi_n$ at
$n \in \mathfrak{M}$. The categorical neutrality forces the
Wedderburn support of $\Phi_n$ onto self-conjugate partitions. Pairing
this with Yekutieli rigidity \cite{yekutieli2010}, the :refterm[descent]{#descent}
involution $\hat\tau$ inherits the corresponding self-conjugacy on
$A_n$, and the BB stratification becomes self-dual: the strata above
the $E_2$ collapse line cancel pairwise. The conjectured
$E_\infty^{p, >0}(n) = 0$ forms the algebraic-geometry crystallisation
of this cancellation.

This conditional structure justifies authoring both conjectures
together. The categorical conjecture forms the Hecke-side
content; the homological conjecture forms its brane-tower-side image
under Yekutieli rigidity. A proof of either implies the other under
the substrate axioms.

## Relation to the Hoefsmit / matrix-evaluation programme

Numerical verification at $k = 3, \dots, 10$
([conj:magic-numbers-from-q](../observations/magic-numbers-from-q.md))
empirically confirms $E_\infty^{p, >0}(n) = 0$ at $n = 2, 8, 20$ via
direct computation of :refterm[descent]{#descent} residues from Hoefsmit matrices. The
combinatorial blow-up at $k \geq 12$ blocks the matrix-evaluation
approach. The homological framework analytically bypasses this
barrier by replacing per-partition matrix computation with
spectral-sequence arithmetic
([rem:k12-barrier-bypass](../observations/k12-barrier-bypass.md)).

## Operator-level support (clarification)

The "Wedderburn support of $\Phi_n$ onto self-conjugate
partitions" in §"Conditional content" above describes operator-level support.
$\Phi_n$ has zero matrix entries on non-self-conjugate isotypical
components, but the operator on the self-conjugate components is
generically non-trivial. It is not the Plancherel-weighted
character sum $\sum_{\lambda = \lambda'} w_\lambda \chi^\lambda$,
which vanishes identically at certain atomic-braid cycle types.
The $E_\infty^{p, >0}(n) = 0$ collapse condition stated above is
precisely operator-level (page collapse on the associated graded
algebra). It remains consistent with this reading.

## Discussion

This remains conjectural. The supporting evidence comprises:

1. Numerical verification at $n \in \{2, 8, 20\}$ via the
 matrix-evaluation programme.
2. Conditional equivalence with
 [categorical neutrality of saturated shells](categorical-neutrality-saturated-shells.md)
 under Yekutieli rigidity (the Hecke-side conjecture is stated
 independently).
3. Phenomenological agreement: the seven values
 $\{2, 8, 20, 28, 50, 82, 126\}$ form the only nucleon counts at
 which the experimental binding curve exhibits a discontinuous
 first-derivative drop (the empirical signature of shell closure).

The downstream cone affects the higher-magic-number predictions
$n \in \{50, 82, 126\}$ where matrix evaluation remains unavailable.
Any result quoting these higher-magic-number predictions therefore
depends on this conjecture, and stays conjectural until either the
conjecture is proved or the prediction is demoted to a numerical
empirical claim.
