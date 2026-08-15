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

### Correction to my own entry note, same session — measured, not assumed

I wrote above that W1 is "build `Fin N ≃ PartitionIndex n` from the abstract
split's block set". Having now read the actual signature, that framing is wrong
and would waste the next session.

`IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing` binds **`n`, `D`, `d`
and the equivalence all existentially**, and its statement mentions no simple
module at all. There is no handle on which block is which — nothing to reindex.
Any `Fin N ≃ PartitionIndex n` extracted from it would be a choice with no
stated relation to `S^μ`, which is exactly the over-generality trap
`SnWedderburnPartitionBridge` already documents (`sn_block_dim_eq_specht` is
false as a ∀-over-splits claim).

**So W1/W3 should build the split directly, not reindex Mathlib's.** The target
map is the action map `k[S_n] → ∏_{μ} Module.End k (S^μ)`; it is partition-indexed
by construction, so the labelling is not a separate step. Then:

- each factor becomes `Matrix (Fin dᵢ) (Fin dᵢ) k` via `LinearMap.toMatrix` on
  `SpechtStandardBasis` (which is indexed by `StandardYoungTableau μ`, so the
  size is `dim S^μ` by construction — that is W3, mechanically);
- W2's `simple_end_scalar` is what makes the factor `End_k` rather than an
  algebra over a larger `𝔇`;
- the real work moves to **surjectivity** of the action map (Jacobson density /
  the double-centraliser theorem), plus injectivity from faithfulness.

Re-scope W1 and W3 accordingly before starting: they are one construction, not
two, and the hard core is the density argument.
