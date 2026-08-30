---
# qou-twwf
title: 'det(Gram)=[n]_q! GENERAL: needs n!-dim T_w basis (Bott-Samelson, qou-lrz1) + Schur-element product formula. Deep classical piece'
status: in-progress
type: task
priority: normal
created_at: 2026-07-25T03:29:22Z
updated_at: 2026-08-30T03:46:45Z
---

## 2026-08-30 — the whole Hecke presentation now holds for the `T_w` operators

Branch `claude/p-neq-np-gaps-n8dxxl`, PR #6053. All sorry-free, `lean`-direct
exit 0, `#print axioms` clean (propext / Classical.choice / Quot.sound).

* `QOU/Hecke/TwBasis.lean` — `Rs i` (right multiplication by `T_{s_i}` on
  `W →₀ R`, any Coxeter system) and the **quadratic** relation `Rs_sq`.
* `QOU/Hecke/TwBasisPerm.lean` — `rsFun_perm`: for type `A` the branch is the
  comparison `w(i) < w(i+1)`.
* `QOU/Hecke/TwBasisBraid.lean` — **commuting** (`Rs_comm_of_lt`) and
  **braid** (`Rs_braid`) relations.

So the three constructors of `QOU.Hecke.HeckeRel` are all discharged for `Rs`.

### Why the concrete type-A route

Abstractly the braid case needs the strong exchange property, parabolic
subgroups and minimal coset representatives; Mathlib's `GroupTheory/Coxeter/`
is four files and has none of them, and lists Matsumoto's theorem as an open
TODO (`Coxeter/Basic.lean:78`). The Bourbaki free-module route avoids
Matsumoto entirely, and `permCoxeterSystem` (this same PR) put `cs.length`
within reach of `Equiv.Perm` so the branch could be made concrete.

### Still open on this bean

1. The algebra map `H_n(q) → Module.End K (S_{n+1} →₀ K)` (`TwRep.lean`,
   in flight) — mechanical from the three relations via `RingQuot.liftAlgHom`.
2. Spanning: `single 1 1` generates the module under the `Rs`, by induction
   on `cs.length`.
3. Independence of the `T_w`, read off 1 + 2 — this is what makes the rank
   `n!` and is what `det(Gram)` must be stated against.
