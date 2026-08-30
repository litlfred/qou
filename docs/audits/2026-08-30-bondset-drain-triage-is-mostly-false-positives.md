# The `C(A,2)` drain is much smaller than the grep — triage, not a defect list

**Date:** 2026-08-30 · **Bean:** `qou-gecf` (parent `qou-y2l3`) · **Type:** triage

## Why this exists

`qou-k12x` reported a grep-level upper bound of **67** files touching a
`C(A,2)`/clique bond set, after the corpus superseded that convention with the
linear-chain `A−1` count (`theta_mn_linearchain_vs_allpairs.py`,
`prop:linear-chain-bond-count` Lean-proved). **67 is not a defect count**, and
this unit measures how far it is from one.

## The narrowing, with the criterion at each step

| step | criterion | count |
|---|---|---:|
| grep | `comb(A,2)` / `C(A,2)` / `clique`, excl. `_deprecated` | **67** |
| − convention-aware | file mentions chain / all-pairs / superseded / convention | 37 → **30** |
| − cumulant use | file uses `C` in an Ursell / cumulant / body-order / Mayer context | 13 → **17** |

**The cumulant exclusion is the important one.** `C(A,n)` in an Ursell
inversion is **definitionally** the all-subsets multiplicity of the body-order
expansion — it is not a claim about which nucleons are bonded, and it is
correct whatever the braid's bond set is. Thirteen files use it that way,
including four of my own from this session. A drain that "fixed" those would
be introducing errors, not removing them.

## Then the residual 17 was sampled by hand, and it mostly does not survive

An automated candidate list is not a verdict. Three of the 17 were read:

| file | verdict |
|---|---|
| `binding_edge_set_selection.py` | **false positive** — it explicitly compares "the linear chain (A−1 edges) and the complete graph (C(A,2) edges)". Convention-aware; my regex missed it because it writes "complete graph" rather than "all-pairs". |
| `two_row_vs_higher_row_binding_split.py` | **false positive** — `ρ_A ≤ C(A,2)` is a **proved cap**, an inequality bound, not a bond-set assertion. |
| `per_bond_growth_a3.py` | **unresolved** — `B = Σ_{C(A,2)} B_b` reads as a genuine bond-set sum; needs a full read. |

**Measured precision on that sample: 1 of 3.** So the true residual is plausibly
**~5–6 files**, not 67, not 30, not 17 — and every one still needs reading.

Two of the 17 are also my own probes (`bonded_pair_linking_inconsistency_probe`,
`gap2_irreducible_triple_bracket_probe`), which use clique counts deliberately to
reproduce the July GAP-2 result. They are correct as written.

## What this establishes

- The drain is real but **small**, and none of the four numbers above is its size.
- The single most important discriminator is **cumulant multiplicity vs bond
  set**, and no grep can make it — it needs the surrounding argument.
- **No defect list is shipped here**, deliberately. Acting on any of these
  counts without reading each file would corrupt correct code, and the sample
  says most of the candidates are correct.

## What is NOT established

Which files are actually wrong. That requires reading ~15 files properly, which
this unit did not do and does not claim to have done.
