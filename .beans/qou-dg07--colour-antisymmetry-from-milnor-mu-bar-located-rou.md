---
# qou-dg07
title: 'Colour antisymmetry from Milnor mu-bar: located route for eightfold items 4 and 7, gap is one identification'
status: todo
type: task
priority: normal
created_at: 2026-08-29T10:11:14Z
updated_at: 2026-08-29T10:11:14Z
---

## Summary

Audit: `docs/audits/2026-08-29-colour-antisymmetry-from-milnor-mu-bar.md`

The 2026-08-26 discriminator search settled the negative (no object-level gate
separates colour from flavour) and located the discriminator in the Young
channel, naming its own circularity: assigning colour the antisymmetric channel
is an INPUT. It said deriving that input "would supply the one input item 4 is
missing".

This is a candidate route to that input, assembled from things already in the
corpus plus one cited standard fact:

  corpus  the three B_3 components ARE the colours (r,g,b)   borromean-quark.md
  corpus  S_3 acts by permuting the colour assignment        borromean-quark.md
  corpus  mu-bar_123 = +-1 "encodes confinement"             borromean-quark.md
  corpus  mu-bar_123 is the candidate second invariant       SecondCrossingInvariant.lean
  LIBRARY mu-bar_ijk is TOTALLY ANTISYMMETRIC in its indices library/0110001v3

Total antisymmetry in three indices IS the sign representation of S_3. So the
invariant the corpus says encodes confinement transforms in the sign rep of the
S_3 the corpus says permutes colour -- a topological fact, not a QCD import,
and the right shape for colour sitting in lambda = (1^3).

## The gap, NOT closed

  A  mu-bar_123 transforms in the sign rep of S_3        ESTABLISHED (cited)
  B  the state's COLOUR CHANNEL is lambda = (1^3)        NOT established

A is about an invariant of the link; B is about which Young channel the state
occupies. A -> B needs the premise that the state's colour content is READ OFF
mu-bar. The corpus does not assert that and I did not assume it. Item 7 is NOT
derived here and item 4's missing input is NOT supplied.

Claiming B from A would be exactly the arity-conflation failure the
devils-advocate criterion names: a statement about an invariant read as a
statement about a state.

## Why it is still worth having

Replaces "colour antisymmetry is an input" with "colour antisymmetry follows
from ONE identification" -- a strictly smaller ask, and falsifiable in the
useful direction. If the colour degree of freedom is shown not to be carried by
mu-bar, the route dies cleanly.

Also: mu-bar_123 is already SecondCrossingInvariant.lean's candidate for the
hypercharge programme's missing second invariant. If the identification holds,
one object serves both open problems.

## Next

Settle the identification: is the colour degree of freedom carried by mu-bar, or
is mu-bar merely an invariant that happens to be alternating? That is the whole
remaining question on this route.
