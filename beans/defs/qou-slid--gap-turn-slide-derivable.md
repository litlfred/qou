---
# qou-slid
title: 'GAP: is the turn slide derivable from R1/R2/R3 and the join moves on diagram codes'
status: todo
type: task
priority: normal
tags:
    - pl-knots
created_at: 2026-11-21T22:45:00Z
updated_at: 2026-11-21T22:45:00Z
---

Issue #8902, PR #8962. `Move.slide` in `QOU/MathlibExt/LinkDiagramCode.lean` moves `t` turns from
both incoming edges of a crossing to both outgoing edges. Markov invariance of braid closures
(`reidemeisterEquiv_of_markovEquiv`, `LinkDiagramBraidMarkov.lean`) uses it, through conjugation and
far commutation. The owner chose to try to derive it before keeping it as a primitive (2026-11-21).

Status: neither derived nor shown independent.

- Direct route fails as attempted: a turn can be pushed into an antiparallel bigon (`r2anti`), but
  moving the crossing through that bigon needs R3, and R3 needs three strands. A lone crossing has two.
- Model search, exact (sympy Groebner, scratch only): no state-sum model whose crossings shift
  labels by a fixed cyclic permutation with label-dependent phases (n = 2, 3) satisfies the r1,
  r2par, r2anti and r3 identities of `Model.Invariant` while having non-constant `K`. So these
  models cannot show the slide is independent. A wider model class is untested.
- A linear invariant of the form sum over segments of turn times an end-type weight is not
  invariant under r2par or r2anti, which split segments at arbitrary points.

Next honest steps: (1) look for a derivation that uses a third strand already present in a braid
closure (enough for Markov invariance, though not for all codes); (2) search a wider model class,
e.g. general 2-label tensors, for an independence proof.
