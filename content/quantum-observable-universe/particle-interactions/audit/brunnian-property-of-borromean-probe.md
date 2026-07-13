# Brunnian Property of Borromean Link Probe

## Consequences of discharging it

A proof of `borromean_brunnian` upgrades the [topological mechanism of color confinement](#rem:borromean-topological-confinement) from an interpretive remark to a formal theorem. This strengthens several downstream results:

- [Borromean baryon mass formula](#conj:borromean-baryon-mass-formula): We invoke the formal property to justify why the volume contribution equals the full bare topological mass (with no residual sub-link binding to subtract).
- [Borromean Bloch-group element](#conj:borromean-bloch-group-element): We pin the dilog identities to formal sub-link triviality.
- Conditional-class hypotheses on downstream blocks citing this conjecture discharge automatically.

## Path to formalisation

The Mathlib implementation requires three components:

1. **Reidemeister moves on braid words.** Define R1, R2, and R3 as rewriting rules on `BraidWord.letters`. Prove they preserve link topology.
2. **Markov closure equivalence.** Two braid words represent the same link if and only if they are related by R-moves and stabilisation (conjugation and addition of $\sigma_{n}$ or $\sigma_{n}^{-1}$).
3. **`isUnlink` via Markov normal form.** Show that the empty braid in $B_n$ closes to $U_n$. Prove this property is preserved under the equivalence relation.

With these components, the proof of `borromean_brunnian` reduces to finite computation. We exhibit an explicit R-move sequence taking $(\sigma_0^{-1})^3 \in B_2$ to the empty braid in $B_2$.

## Location of the computation

The energetic cost of the unlinking move defines the bare topological mass. This distinguishes a confined Borromean baryon from three free unknots. We compute this hyperbolic-volume contribution in the [Borromean baryon mass formula](#conj:borromean-baryon-mass-formula). The corresponding Bloch-group element appears in [Borromean Bloch-group element](#conj:borromean-bloch-group-element). 

The formal Lean counterpart is [Brunnian property of $\mathcal{B}_3$](#conj:brunnian-property-of-borromean). It states that every two-component sub-link of the Borromean rings is the unlink. It traces the formalisation gap to the absence of Mathlib Reidemeister-move primitives.
