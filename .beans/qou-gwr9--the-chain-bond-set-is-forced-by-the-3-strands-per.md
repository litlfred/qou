---
# qou-gwr9
title: The chain bond set is FORCED by the 3-strands-per-nucleon layout, not chosen
status: completed
type: task
priority: normal
created_at: 2026-08-31T04:14:33Z
updated_at: 2026-08-31T04:15:17Z
---

## Proved and measured (branch `claude/nf-bonds-are-counts-not-graph-2026-08-31`, PR #6346)

Follows `qou-zryq`, which showed the NF word's inter-nucleon block encodes a bond
COUNT rather than a graph. This asks the same question of the *other* word, the
one that does have strand geometry — and the answer is sharper.

**Measured** (`computations/bridge_generator_index_probe.py`, exit 0):
diffing `atom_braid_word_3A(include_inter=False)` against `(=True)` gives the
bridge generators directly off the producer:

    2H  [2]                          4He [2,5,8]
    3H  [2,5]                        6Li [2,5,8,11,14]
    12C [2,5,8,11,14,17,20,23,26,29,32]

Exactly `3k+2` for `k = 0…A−2`, exactly `A−1` of them, on all 8 nuclei tried.

**Proved** (`QOU.Mass.StrandLayoutForcesChain`, `lean`-direct exit 0, five
declarations, `#print axioms` shows only `propext` / `Classical.choice` /
`Quot.sound` — no `sorryAx`; registered in `QOU.lean`):

    crossesBlocks_iff                     block m ≠ block (m+1)  ↔  m % 3 = 2
    adjacent_of_crosses                   m % 3 = 2  →  block (m+1) = block m + 1
    no_single_generator_joins_nonadjacent  i ≠ j  →  j = i + 1
    bridge_crosses, bridge_joins_consecutive   (the producer's 3k+2 instantiated)

with `block m = m / 3`, the nucleon owning strand `m` under the layout in which
nucleon `k` owns strands `3k, 3k+1, 3k+2`.

**So the chain is FORCED, not chosen.** A single generator `σ_m` joins two
different nucleons only when `m % 3 = 2`, and then only *consecutive* ones. A
non-adjacent bond is not a different edge set one could equally have written — it
is not a single crossing at all, and would need a word transporting strands past
each other, which the producer does not write and which would not sit at a
Markov-removable position the same way.

**The consequence worth carrying.** The layout is a **linear order on nucleons**.
So the chain bond set and the nucleon-ordering convention are the *same*
unlicensed choice, not two independent ones — which merges this arc's bond-set
question into `qou-48is`, where that ordering is measured to move `tr_M` by
O(10 %) at `A ≥ 3`.

Combined with `qou-zryq`, the two live "bond sets" are now both explained and
neither is a free modelling choice: the NF word's `C(A,2)` is a repeated scalar
factor with no strand assignment, and the 3A word's `A−1` is forced by the strand
layout. Comparing them as competing coordination hypotheses was a category error.

**Scope (a).** Pure ℕ arithmetic about `m ↦ m / 3`; says nothing about which bond
set the physics wants.
