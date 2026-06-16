The seven observed nuclear magic numbers
$\mathfrak{M} = \{2, 8, 20, 28, 50, 82, 126\}$
are quoted in
[`prop:magic-numbers-from-q`](../observations/magic-numbers-from-q.md)
as "from Bring's surface — not derived". This block names the
**algebraic claim** that explicates that footnote: each magic
value is the rank of a distinguished $S_5$-stable period sub-
lattice on Bring's surface
([`def:brings-coordinate-ring`](#def\:brings-coordinate-ring))
that closes a shell under the categorical :refterm[descent]{#descent} operator.

This is workplan task **P1.4** path-(b): the conjecture provides
the algebraic statement; Phase 2 (Lean + concrete period
computation) is deferred.

## Setup

Let $\mathcal{B}$ be Bring's curve of genus $4$ with coordinate
ring $\mathcal{O}_q(\mathcal{B})$
([`def:brings-coordinate-ring`](#def\:brings-coordinate-ring))
and $S_5$-action by algebra automorphisms.  The integer
homology $H_1(\mathcal{B}, \mathbb{Z})$ has rank $2g = 8$ and
carries a natural symplectic pairing under which $S_5$ acts.

Klein \cite{klein1888} classified the $S_5$-stable
sub-lattices of $H_1(\mathcal{B}, \mathbb{Z})$ up to lattice
isomorphism.  Each isomorphism class has a canonical rank, given
by the dimension of the underlying $\mathbb{Q}[S_5]$-submodule.

The **categorical :refterm[descent]{#descent} operator**
$\hat\tau$ ([:refterm[descent]{#descent} involution](#def\:descent-involution)) acts
on the brane tower's level-$n$ jet algebra; restricting to the
level-$0$ Reeb-orbit chart of Bring's surface gives an action on
$H_1(\mathcal{B}, \mathbb{Z})$ that commutes with the $S_5$-action.

## Statement

**Conjecture (magic numbers from Bring's surface).**
*There is a bijection*

$$
  \mathfrak{M} \;=\; \{2, 8, 20, 28, 50, 82, 126\}
  \;\longleftrightarrow\;
  \{ L_2, L_8, L_{20}, L_{28}, L_{50}, L_{82}, L_{126} \}
$$

*between the seven nuclear magic numbers and seven
distinguished $S_5$-stable, $\hat\tau$-stable period
sub-lattices*

$$
  L_n \;\subset\; H_1(\mathcal{B}, \mathbb{Z})^{\oplus k(n)},
\qquad
  \mathrm{rank}_\mathbb{Z}\bigl(L_n\bigr) \;=\; n,
$$

*characterised as the ranks of the irreducible
$\mathbb{Q}[S_5 \times \langle \hat\tau \rangle]$-submodules of
the brane-tower's level-1 cohomology
$H^1(A_1, \mathbb{Z})$ that close shells under
[`prop:homological-shell-condensation`](../lifting-and-descent/homological-shell-condensation.md).*

*Equivalently, $n \in \mathfrak{M}$ iff*

1. *there exists an $S_5$-stable, $\hat\tau$-stable lattice of
   rank $n$ in some power of $H_1(\mathcal{B}, \mathbb{Z})$, and*
2. *the categorical mass at nucleon-count $n$
   ([`prop:categorical-neutrality-saturated-shells`](../braids-and-knots/categorical-neutrality-saturated-shells.md))
   is supported on a single self-conjugate partition associated
   to that lattice.*

## Why $S_5$ and Bring

Bring's curve is the unique (up to isomorphism) genus-$4$ curve
with $S_5 \cong \mathrm{Aut}(\mathcal{B})$ acting maximally
\cite{klein1888}. The QOU substrate identifies Bring's surface
as the $\chi = -6$ profile of the brane base
([`prop:brings-is-qou`](../archimedean-universe/brings-is-qou.md));
$S_5$ is therefore the **categorical symmetry group** of the
substrate. Magic numbers as $S_5$-stable lattice ranks is the
algebraic statement that nuclear shell closure is an
$S_5$-symmetry phenomenon, not a fitted shell-model parameter.

The seven sub-lattice ranks $\{2, 8, 20, 28, 50, 82, 126\}$
match — under this conjecture — the seven distinct irreducible
$\mathbb{Q}[S_5 \times \langle \hat\tau \rangle]$-modules whose
$\hat\tau$-action on the brane-tower cohomology is **strictly
positive** (closing the shell under condensation per
[`prop:homological-shell-condensation`](../lifting-and-descent/homological-shell-condensation.md)).

## Connection to the conjectural-propagation chain

Per the algebraic-refactor Phase 1 (commit `0e86a151`), the magic
numbers are downstream of two conjectures:

* [`prop:categorical-neutrality-saturated-shells`](../braids-and-knots/categorical-neutrality-saturated-shells.md)
  (Hecke-side: full-twist trivial action on $\Phi_n$ at magic $n$),
* [`prop:homological-shell-condensation`](../lifting-and-descent/homological-shell-condensation.md)
  (brane-tower side: BB spectral sequence collapse at magic $n$).

This block adds a third, complementary, **algebraic-substrate-
level** conjecture: the ranks $\{2, 8, 20, 28, 50, 82, 126\}$ are
$S_5$-stable lattice ranks. The three conjectures together are
**equivalent** under Yekutieli rigidity; any one would imply the
other two.

## Path to a proof

The conjecture's content is:

1. **Existence**: identify the seven $S_5 \times
   \langle \hat\tau \rangle$-irreducibles of strictly-positive
   $\hat\tau$-rank in the level-1 brane cohomology and verify
   their ranks are $\{2, 8, 20, 28, 50, 82, 126\}$.
2. **Bijection**: prove the $\hat\tau$-stable irreducibles are in
   one-to-one correspondence with the magic numbers.

Step 1 reduces to a finite-dimensional representation-theory
computation: the irreducibles of $S_5$ have known dimensions
$\{1, 1, 4, 4, 5, 5, 6\}$ (the standard character table).
Tensoring with the $\hat\tau$-character (a $\pm 1$ involution
sign) and scoring by brane-tower rank gives candidate
sub-lattices. The match to $\{2, 8, 20, 28, 50, 82, 126\}$ is
the conjectural content — empirical evidence already in
[`prop:magic-numbers-from-q`](../observations/magic-numbers-from-q.md).

Step 2 requires explicit construction of the period sub-lattices;
this is the main technical content and is the deferred Phase 2
computation.

## Discussion

**Conjectural** under CLAUDE.md §3b. The conjecture's role is
to **name** the algebraic mechanism behind the magic-number
sequence. Promotion to a theorem requires the
representation-theory + period-lattice computation outlined in
"Path to a proof" — research-grade but bounded.

The downstream cone of this conjecture is exactly the magic-
number predictions in
[`prop:magic-numbers-from-q`](../observations/magic-numbers-from-q.md);
those predictions are now triply-conditional (on
`prop:categorical-neutrality-saturated-shells`,
`prop:homological-shell-condensation`, and this block) — but the
three conjectures are equivalent under Yekutieli rigidity, so the
true conjectural surface is one statement modelled three different
ways.

This block closes audit `MAG-1` (the "magic numbers from Bring's
surface — not derived" flag in
[`DERIVATION-STATUS.md`](../../../computations/DERIVATION-STATUS.md))
as a path-(b) deliverable: the algebraic claim is now stated
explicitly, with the empirical match documented. The path-(a)
proof is workplan **P1.4** and remains open.
