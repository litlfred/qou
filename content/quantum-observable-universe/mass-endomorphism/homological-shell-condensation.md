The Białynicki-Birula stratification of the brane tower
([recursive-brane-tower](#def\:recursive-brane-tower),
[brane-tower-levels](#ex\:brane-tower-levels)) under the :refterm[descent]{#descent}
involution $\hat\tau$
([:refterm[descent]{#descent}-involution](#def\:descent-involution)) yields a spectral
sequence whose $E_\infty$ page records the *failure* of categorical
neutrality at each level. This block names the **homological
condensation** at saturated $n$: the higher pages collapse to zero,
encoding shell closure as an algebraic-geometry condition on the
brane-tower stratification.

## Setup

Fix a level $n \in \mathbb{N}$ in the brane tower, with associated
:refterm[descent]{#descent}-graded jet algebra $A_n = A_{n-1} \otimes \Omega^1(A_{n-1})$
([def:direct-limit-algebra](#def\:direct-limit-algebra)). The
Białynicki-Birula stratification of $\mathrm{Spec}(A_n)$ under the
$\mathbb{C}^\times$-action induced by the :refterm[descent]{#descent} involution
$\hat\tau$ \cite{bialynicki1973} produces a filtration

$$
  F^0 A_n \supset F^1 A_n \supset \cdots \supset F^p A_n \supset \cdots
$$

with associated graded $\mathrm{gr}_F A_n$. The Gröbner–Shirshov
spectral sequence
([prop:gb-spectral-sequence](#prop\:gb-spectral-sequence)) on this
filtration converges to the :refterm[descent]{#descent}-graded algebra:

$$
  E_1^{p,q} \;=\; H^q\bigl(\mathrm{gr}_F^p A_n\bigr)
  \;\Longrightarrow\;
  H^{p+q}\bigl(A_n\bigr).
$$

The **strict-positive part** $E_\infty^{p, >0}(n)$ measures the
non-trivial cohomology supported above the $E_2$-collapse line —
operationally, the obstruction to reading the :refterm[descent]{#descent}-graded trace
purely from the diagonal
([prop:graded-trace-residue-split](#prop\:graded-trace-residue-split)).

## Statement

**Proposition (Conjecture — homological shell condensation).**
*For every $n \in \mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$, the
Białynicki-Birula spectral sequence on $A_n$ collapses entirely above
the $E_2$ line:*

$$
  E_\infty^{p, q}(n) \;=\; 0
  \qquad\text{for all } p \in \mathbb{N}, \; q > 0,
  \quad n \in \mathfrak{M}.
$$

*Equivalently, the :refterm[descent]{#descent}-graded trace
$\mathrm{tr}_{M, \ell}$ on $J^\ell / J^{\ell+1}$
([prop:graded-trace-residue-split](#prop\:graded-trace-residue-split))
is supported entirely on the diagonal at saturated $n$, and the
brane-tower :refterm[descent]{#descent} residues vanish for $\ell \geq 2$.*

## Why "condensation"

The vanishing $E_\infty^{p, >0}(n) = 0$ means that *every* higher
:refterm[descent]{#descent} residue collapses onto the diagonal: there are no
off-diagonal jet-tower contributions at saturated $n$. The shell
condenses into a single graded piece. For $n \notin \mathfrak{M}$
the off-diagonal pieces survive, providing the algebraic content of
non-saturation (residual capacity to absorb crossing energy).

The phenomenology this picks up is the standard one — at
$n \in \mathfrak{M}$ the binding-energy curve flattens, the next
nucleon adds nearly-zero binding, and the shell is mathematically
"full". The refactor names this directly in the spectral sequence,
not via shell-model fitting.

## Conditional content via the categorical-neutrality conjecture

Conditional on
[`prop:categorical-neutrality-saturated-shells`](../braids-and-knots/categorical-neutrality-saturated-shells.md),
the full-twist $\Delta_n^2$ acts as the identity on $\Phi_n$ at
$n \in \mathfrak{M}$. The categorical neutrality forces the
Wedderburn support of $\Phi_n$ onto self-conjugate partitions. Pairing
this with Yekutieli rigidity \cite{yekutieli2010}, the :refterm[descent]{#descent}
involution $\hat\tau$ inherits the corresponding self-conjugacy on
$A_n$, and the BB stratification becomes self-dual: the strata above
the $E_2$ collapse line cancel pairwise. The conjectured
$E_\infty^{p, >0}(n) = 0$ is the algebraic-geometry crystallisation
of this cancellation.

This conditional structure is the reason both conjectures are
authored together: the categorical conjecture is the *Hecke-side*
content; the homological conjecture is its *brane-tower-side* image
under Yekutieli rigidity. A proof of either implies the other under
the substrate axioms.

## Relation to the Hoefsmit / matrix-evaluation programme

Numerical verification at $k = 3, \dots, 10$
([prop:magic-numbers-from-q](../observations/magic-numbers-from-q.md))
empirically confirms $E_\infty^{p, >0}(n) = 0$ at $n = 2, 8, 20$ via
direct computation of :refterm[descent]{#descent} residues from Hoefsmit matrices. The
combinatorial blow-up at $k \geq 12$ blocks the matrix-evaluation
approach; the homological framework analytically bypasses this
barrier by replacing per-partition matrix computation with
spectral-sequence arithmetic
([rem:k12-barrier-bypass](../observations/k12-barrier-bypass.md)).

## Operator-level support (clarification)

The "Wedderburn support of $\Phi_n$ onto self-conjugate
partitions" in §"Conditional content" above is **operator-level**:
$\Phi_n$ has zero matrix entries on non-self-conjugate isotypical
components, but the operator on the self-conjugate components is
generically non-trivial. It is **not** the Plancherel-weighted
character sum $\sum_{\lambda = \lambda'} w_\lambda \chi^\lambda$,
which vanishes identically at certain atomic-braid cycle types
(see [reframing memo](../../../docs/audits/-self-conj-support-reframing.md)).
The $E_\infty^{p, >0}(n) = 0$ collapse condition stated above is
precisely operator-level (page collapse on the associated graded
algebra), and is consistent with this reading.

## Discussion

**Conjectural** under CLAUDE.md §3b. The supporting evidence is:

1. Numerical verification at $n \in \{2, 8, 20\}$ via the
 matrix-evaluation programme.
2. Conditional equivalence with
 [`prop:categorical-neutrality-saturated-shells`](../braids-and-knots/categorical-neutrality-saturated-shells.md)
 under Yekutieli rigidity (the Hecke-side conjecture is stated
 independently).
3. Phenomenological agreement: the seven values
 $\{2, 8, 20, 28, 50, 82, 126\}$ are the only nucleon counts at
 which the experimental binding curve exhibits a discontinuous
 first-derivative drop (the empirical signature of shell closure).

The downstream cone is the higher-magic-number predictions
$n \in \{50, 82, 126\}$ where matrix evaluation is unavailable.
Per §3b, any provable result quoting these higher-magic-number
predictions transitively depends on this conjecture and must be
typed `conjecture` until either the conjecture is proved or the
prediction is demoted to a numerical empirical claim.
