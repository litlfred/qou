---
# qou-ptgd
title: 'PRUNE: a groupoid with a terminal object is trivial — "EP is the terminal object of the Ptolemy groupoid" is false as stated'
status: todo
type: task
priority: high
created_at: 2026-09-06T10:55:26Z
updated_at: 2026-09-06T10:55:26Z
---

FORMALIZE-FIRST PRUNE (AGENTS.md §Formalize-first probe discipline): settle the
dialog's central categorical claim before any construction is built on it.

CLAIM TO PROVE (elementary, generic, sorry-free, no Mathlib gap):
  In a groupoid G, if T is terminal then Hom(X,Y) is a singleton for ALL X,Y.
  Proof: t_X : X -> T unique; for f : X -> Y, t_Y . f = t_X so f = t_Y^{-1} . t_X.
  Hence every automorphism group is trivial and G is equivalent to the terminal
  category.

CONSEQUENCE: the Ptolemy/Pachner groupoid has non-trivial automorphisms (the
mapping-class group / the symmetry group of the manifold; Sym(S^3 minus 4_1) is
non-trivial), so it has NO terminal object. EP is a CANONICAL CHOICE — a
distinguished object natural under isometry, i.e. a section of a forgetful
functor, or the unique minimiser of the EP convexity functional — NOT a limit.
Scope-(b) STRUCTURAL exclusion: the invariant cited is the proof above.

Does NOT refute the underlying idea (a canonical decomposition exists and is
unique); it refutes the WORD, which matters because "terminal object" is what
would have made the construction functorial for free.
