---
# qou-j1e5
title: 'c1: the six values are GROUPED-word — re-derive under Borromean, or scope them (blocks the probe going green)'
status: todo
type: task
priority: high
created_at: 2026-09-06T03:58:42Z
updated_at: 2026-09-06T03:59:28Z
---

## The situation, measured

`7db032fb48` (owner ruling, bean `qou-hu1f`) changed `atom_braid_word_3A`'s
default intra ordering `grouped -> borromean`. The `c1` probe never pinned the
ordering, so it inherited the new default and now **asserts against an object it
no longer computes** — 6 of 6 recorded mismatches on `main`:

    c1 = 1/8   vs recorded 19/8      c1 = 1/64  vs 163/64
    c1 = 1/16  vs recorded 37/16     c1 = 1/8   vs 85/32
    c1 = 0     vs recorded 9/4       (4He likewise)

`c0` passes under BOTH orderings (1/8, 3/32) — the floor is ordering-invariant,
the difference coefficient is not.

## Why pinning to `grouped` does NOT work — the finding that closed #6874

The obvious containment (pin the probe to `grouped`) was implemented, verified,
and **abandoned**. It makes the six `c1` assertions pass and then fails a
different one:

    exact_fraction_pipeline_matches_transfer_kernel_at_q_8_over_7
      computed 22.8473    expected 0

That assertion exists to tie the probe's exact-Fraction pipeline to the
production kernel `tr_m_atom_zn`. Production is now Borromean (via `qou-wdij`'s
monotonicity dispatch, `818a244f13`). Pinning the probe to `grouped` therefore
puts the two sides on **different words by construction** — the probe cannot be
green while pinned away from production. This is structural, not a tolerance.

Pinning production to `grouped` as well was also implemented and dropped: it
reverts to the word the owner ruled incorrect, and `qou-wdij` had already fixed
that path the right way.

## So the only route that ends green

Re-derive the six `c1` values under the Borromean word. Scope, in increasing
order of difficulty:

1. **Recompute + update `RECORDED`** — mechanical, ~500 s per probe run.
2. **Update `QOU.MassTheory.PairwiseChainLeadingOrder`** — it carries the six as
   **defs, now conditional theorems** per `qou-pdg9`'s own closing note. Not a
   table edit.
3. **Establish whether `c1_from_letters` survives.** THIS IS THE RESEARCH PART.
   Its per-letter derivation is measured **grouped-specific**:
   `the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe` finds
   grouped factorises to `~3e-59` while interleaved fails by `2.8x`-`13.3x`.
   So the DERIVATION, not merely the numbers, may need rebuilding. Cannot be
   scoped without attempting it.
4. **Three merged audit docs** (#6538, #6559, #6607) quote the old values and
   need scoping notes.

## Not covered by the existing regen sweep

`ecfe945b5c` (owner-approved "go") re-ran 53 producers and found 9 genuinely
stale. The `c1` probe is **not among them** — checked. That sweep regenerated
*witnesses*; this needs `RECORDED` + Lean + possibly the derivation, which is
why it falls outside it.

## Related

- `qou-hu1f` — the ordering ruling and the regen sweep.
- `qou-wdij` — the non-monotone dispatch that fixed the production crash.
- `qou-pdg9` — completed; derived the six values under the grouped word.
- #6874 — closed. Contains the measurements above and the two abandoned routes.
