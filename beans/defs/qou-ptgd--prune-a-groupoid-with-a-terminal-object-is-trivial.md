---
# qou-ptgd
title: 'PRUNE: a groupoid with a terminal object is trivial — "EP is the terminal object of the Ptolemy groupoid" is false as stated'
status: completed
type: task
priority: high
created_at: 2026-09-06T10:55:26Z
updated_at: 2026-09-06T11:27:53Z
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

## CLOSED 2026-09-06 — proved, sorry-free

QOU/Mass/GroupoidTerminalDichotomy.lean, 5 declarations, commit 61f7efc74.
lean-direct -DautoImplicit=false -s 65536, exit 0, zero warnings; #print axioms
reports only [propext, Classical.choice, Quot.sound] on all five.

Both horns proved, so the claim fails on either reading of "the Ptolemy
groupoid": isTerminal_of_isTerminal (one terminal object makes EVERY object
terminal -> distinguishes nothing; the unquotiented flip groupoid) and
isEmpty_isTerminal_of_ne_id (one non-identity endomorphism rules out a terminal
object everywhere; Penner's MCG-orbit version). terminal_dichotomy states there
is no middle case.

Closing is correct under AGENTS.md 13a: the subject is a proved categorical
fact, not an open conjecture. What it does NOT settle is anything about whether
a cell decomposition can carry a many-body term -- that is qou-eptr, still open.
