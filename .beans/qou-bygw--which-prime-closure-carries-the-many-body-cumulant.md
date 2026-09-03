---
# qou-bygw
title: 'Which prime closure carries the many-body cumulants: the all-pairs band routing is not a chain'
status: todo
type: task
created_at: 2026-09-03T20:24:04Z
updated_at: 2026-09-03T20:24:04Z
---


Opened from `qou-m3sh` (2026-09-03), which ended with two theorems that
between them relocate the binding-gap search:

1. **The canonical closure is a chain** (linear connected sum of `(2, odd)`-
   torus knots, `prop:canonical-closure-torus-chain`), so its Markov trace is
   a PRODUCT of two-strand factors `z + d` (checked to 1e-59 at A ≤ 4,
   `the_canonical_mass_trace_factorises_over_the_chain_probe`; factor algebra
   in `QOU.Mass.ChainTraceFactor`). Its `L` is exactly additive over
   interfaces: the canonical closure carries NO many-body binding, by theorem.
2. The many-body cumulants the binding arc measures — `c₃ < 0`, `c₄ < 0`,
   `c₅ > 0`, the order-six datum (`qou-wx83`, `prop:subset-cumulant-recursion`)
   — belong to the ALL-PAIRS bond model, whose band-routed bonds interleave
   generators across blocks and destroy the chain form.

So the question is no longer "which invariant carries the twist" (answered:
none of the knot type, `rem:frenet-framing-is-not-an-invariant`) but **which
prime closure carries the cumulants.** Concretely:

- [ ] Take the all-pairs bond word for A = 3, 4 (both classical branches of
      the averaged letters, as in the chain probe) and decide whether its
      closure is composite. Test: does the Jones/HOMFLY polynomial factor as a
      product of the per-component or per-bond torus-link polynomials? Does
      the linking graph stop being a path? A prime, non-split closure is the
      first thing that COULD carry `c₃`.
- [ ] If prime: identify the link (spherogram / SnapPy identify, as in
      `the_curvature_floor_is_sharp_probe`), and check whether the component
      knot types are still `(2, odd)`-torus knots or change with A. Bridge
      number and Milnor's floor then follow, and the floor's slope per
      nucleon is the first invariant that can be compared with the extensive
      term `CoordinationSaturation` demands.
- [ ] Which cumulant order first fails to factor is a topological statement
      about the closure (a `k`-body term needs a sublink on `k` blocks that
      is not a connected sum); compare with the arc's sign pattern `+ − − + −`.
- [ ] Borromean-type linking (pairwise-unlinked, triple-linked) versus
      chain-type: `atom_closure_milnor_indeterminacy_probe` already showed the
      canonical closure is neither Brunnian nor unknotted per component. Redo
      that census on the all-pairs closure.

Not the question: any new bond model. The all-pairs model is the one whose
cumulants exist; this asks what link it is.
