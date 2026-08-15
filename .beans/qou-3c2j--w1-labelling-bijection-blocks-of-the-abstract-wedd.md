---
# qou-3c2j
title: 'W1: labelling bijection — blocks of the abstract Wedderburn split <-> PartitionIndex n (uses specht_isSimple + specht_exhausts_irreducibles + spechtIso_imp_dom_both, all now closed)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T14:41:43Z
updated_at: 2026-08-15T20:59:57Z
---


## Entry note (2026-08-15, after W2 closed in PR #5139)

W2 supplies what W1 needs on the division-ring side: `simple_end_scalar` says
the commutant of *every* simple `k[S_n]`-module is `k`, so a block's `𝔇 i` is
already known to be the base field once the block is identified with a simple.

W1 is the identification itself. Available now, all sorry-free:

- `SpechtClassification.specht_exhausts_irreducibles` — every simple is a Specht
  module (surjectivity of the labelling);
- `spechtIso_imp_dom_both` + `partitionDom` antisymmetry — distinct partitions
  give non-isomorphic Specht modules (injectivity);
- `card_partitionIndex` / `card_irreducibles_eq_card_partitions` — the counts
  match;
- `WedderburnSn.sn_wedderburnArtin_alg` — the abstract split with `Fin N` blocks.

So the content is: build `Fin N ≃ PartitionIndex n` from the abstract split's
block set. The blocks of `∏ᵢ Matrix(𝔫ᵢ)(𝔇ᵢ)` correspond to the simple modules
(the simple right ideals), and the two maps above are inverse. The friction to
expect is *not* mathematical — it is getting from Mathlib's existentially-bound
`N`/`𝔫`/`𝔇` to a statement about simple modules, since the equivalence is
`Nonempty`-wrapped and carries no named simples.
