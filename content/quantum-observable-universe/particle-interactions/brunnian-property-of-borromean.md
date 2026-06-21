**Conjecture (Brunnian property of $\mathcal{B}_3$).**  *Let
$\mathcal{B}_3 \subset \mathbb{R}^3$ be the standard Borromean link
([Borromean baryon](#def:borromean-baryon)) presented as the closed
braid $\overline{(\sigma_0\sigma_1^{-1})^3}$ in $B_3$.  For each
$i \in \{0, 1, 2\}$ let $\mathcal{B}_3 \setminus K_i$ denote the
two-component sub-link obtained by removing the $i$-th component.
Then $\mathcal{B}_3 \setminus K_i$ is the trivial two-component
unlink $U_2$.*

This is the formal counterpart of the topological-confinement
observation in
[topological mechanism of color confinement](#rem:borromean-topological-confinement):
removing any one of the three components dissolves the binding
between the remaining two.  It is the *defining* property of
Brunnian links \cite{kawauchi1996}.

## Lean structure

The statement is co-located with `def:borromean-baryon` under the
`qou` Lake package.  The substantive declarations live at
[`QOU.KnotTheory.Brunnian`](../lean/QOU/KnotTheory/Brunnian.lean):

```lean
-- BraidWord-level naive component deletion.
def BraidWord.deleteComponent (β : BraidWord) (i : Fin β.strands) : BraidWord

-- Predicate: closure of β is the n-component trivial unlink.
def isUnlink (β : BraidWord) : Prop

-- The Brunnian property as a conjectural class instance.
theorem borromean_brunnian :
  ∀ i : Fin 3,
    isUnlink (borromeanRings.deleteComponent i) := by
  sorry  -- Ref: [kawauchi1996] Survey of Knot Theory §1.5
```

The `sorry` is the conjectural witness per
[AGENTS.md §3b-cond]; the gap is **not** a missing arithmetic
fact but the absence of Mathlib primitives for Reidemeister /
Markov-move equivalence at the level of braid-word closures.
Naive strand-deletion does not yield the unlink at the
BraidWord level (e.g. removing strand 0 from $(\sigma_0\sigma_1^{-1})^3$
yields $(\sigma_0^{-1})^3 \in B_2$, whose closure is the negative
trefoil $\overline{3_1}$, not the unlink); the topological
equivalence to $U_2$ is by an explicit sequence of two R2 moves +
one R3 move that requires the link-equivalence relation to be
formalised first.

## What discharging it would buy

A sorry-free `borromean_brunnian` upgrades
[topological mechanism of color confinement](#rem:borromean-topological-confinement)
from interpretive remark to formal theorem, which in turn lets
several downstream blocks tighten:

- [Borromean baryon mass formula](#conj:borromean-baryon-mass-formula)
  could cite the formal property when justifying why the volume
  contribution is *all* of the bare topological mass (no residual
  sub-link binding to subtract).
- [Borromean Bloch-group element](#conj:borromean-bloch-group-element)
  could pin the dilog identities to the formal sub-link triviality
  rather than to its narrative version.
- The conditional-class hypothesis on any downstream provable
  block citing this conjecture would discharge automatically.

## Path to formalisation

The Mathlib gap is in three pieces:

1. **Reidemeister moves on braid words.** Define R1/R2/R3 as
   rewriting rules on `BraidWord.letters` (or on the closure-class
   equivalent), prove they preserve link topology.
2. **Markov closure equivalence.** Two braid words represent the
   same link iff related by R-moves + stabilisation (conjugation +
   adding a single $\sigma_{n}$ or $\sigma_{n}^{-1}$).
3. **`isUnlink` via Markov normal form.** Show that the empty
   braid in $B_n$ has closure = $U_n$ and that this property is
   preserved under the equivalence relation.

Once those three pieces exist, the proof of
`borromean_brunnian` is a finite computation: exhibit the
explicit R-move sequence taking $(\sigma_0^{-1})^3 \in B_2$ to
the empty braid in $B_2$ (which closes to $U_2$).
