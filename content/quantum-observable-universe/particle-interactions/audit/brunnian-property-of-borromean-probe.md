# Brunnian Property of Borromean Link Probe

## Consequences of discharging it

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
