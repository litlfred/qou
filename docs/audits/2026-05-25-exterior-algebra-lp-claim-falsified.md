# Falsification: exterior-algebra → LP/SDP under-determination claim

**Date:** 2026-05-25
**Trigger:** `atom_braid_active_partitions.py` probe (this session)
**Status:** NEGATIVE finding — partial conjecture refinement required

## What was claimed

In `conj:atom-braid-exterior-algebra` (PR #1271 → main) §"Implications for LP/SDP under-determination", I claimed:

> Under the conjecture: the physical content lives in the sub-algebra
> Λ*(R^(3A−Z)) of dimension 2^(3A−Z). The non-trivial Wedderburn
> channels (those with y_λ ≠ 0 on the atom-braid's image) are a
> proper subset of the p(3A) partitions — exactly those λ
> corresponding to non-zero homogeneous components of Λ^k(R^(3A−Z))
> under the projection H_{3A}(q) → Λ*(R^(3A−Z)).
>
> For ⁴He: at most (3A − Z + 1) − δ = 10 active channels (one per
> non-zero binomial position), down from 77 — a ~7× constraint
> tightening.

This is **FALSE**.

## What the probe found

`atom_braid_active_partitions.py` computed χ_λ(T_w(Z, N)) for every λ ⊢ 3A across D, T, ³He via linear-expansion of the σ_avg crossings (2^(#Avg) branches × full chi_lambda per branch):

| Atom | (Z, N) | n₀ | p(n₀) | Predicted active (n*+1) | **Observed active** | Match? |
|---|---|---|---|---|---|---|
| D | (1,1) | 6 | 11 | 6 | **11** | ✗ |
| T | (1,2) | 9 | 30 | 9 | **30** | ✗ |
| ³He | (2,1) | 9 | 30 | 8 | **30** | ✗ |

(⁴He deferred: 2^9 × 77 chi calls ~11 hr; trends already clear from lighter atoms.)

**All p(n₀) partitions have non-trivial χ_λ.** The "≤ n* + 1 active partitions" prediction was wrong.

## What's still valid

The **filtration-shape claim** from the Rust solver (PR #1271) IS empirically correct:

| Atom | Rust GB-NF filtration shape | Pascal-row C(n*, k) prediction | Match |
|---|---|---|---|
| D | (1, 5, 10, 10, 5, 1) | C(5, k) | ✓ exact |
| T | (1, 8, 28, 56, 70, 56, 28, 8, 1) | C(8, k) | ✓ exact |
| ³He | (1, 7, 21, 35, 35, 21, 7, 1) | C(7, k−1) | ✓ exact |
| ⁴He | (1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1) | C(10, k−1) | ✓ exact |

The 2^(3A−Z) total dimension and binomial-row structure on the **NF basis** (permutation-indexed, filtration by Coxeter length) is real.

## Why my inference was wrong

I conflated two different bases of H_{3A}(q):

1. **NF basis** (permutation-indexed, ordered by Coxeter length) — the filtration shape on this basis IS Pascal-row C(n*, k). The Rust solver works on this basis.
2. **Wedderburn basis** (irreducible-representation-indexed, one block per λ ⊢ 3A) — the LP/SDP y_λ variables live here. χ_λ(T_w) is the trace projection on this basis.

These are **different decompositions**. The atom-braid IS in a 2^(3A−Z) subspace under the NF-basis filtration, but it is NOT in a low-dim subspace under the Wedderburn decomposition — it has non-zero overlap with every irreducible.

The LP/SDP works on the Wedderburn side; my claim that the LP active set shrinks to n* + 1 was structurally unsupported.

## Corrective actions

1. **Update `conj:atom-braid-exterior-algebra.md`** — replace the LP/SDP-implications section with an honest statement: the filtration-shape claim is empirical; it does NOT imply an LP/SDP active-set reduction (the two bases are different).
2. **Update `conj-atom-braid-exterior-algebra.lean`** — remove the `lp_channel_reduction_verified` + `helium4_lp_reduction` theorems (they assert a falsified claim).
3. **Cite this audit** from the conjecture block.

## What the structural finding still implies

The Pascal-row C(n*, k) shape on the NF basis IS structurally meaningful:

- The atom-braid generates a **sub-algebra of H_{3A}(q) of dim 2^(3A−Z)** — much smaller than 3A!
- This sub-algebra is **graded-isomorphic to Λ*(R^(3A−Z))** as a vector space
- The grading is by Coxeter length (NF basis), with shift δ = Z − 1

The remaining open question: what is the categorical relationship between this NF-basis sub-algebra and the per-partition Wedderburn structure? They are evidently related (both describe the same braid's action) but NOT the simple bijection I claimed.

## Lesson

The conjecture's empirical filtration-shape finding is correct and substantive. The inferred LP/SDP implication was a category error — I assumed the NF-basis filtration could be re-indexed by Wedderburn partitions, which is false in general.

Sibling-PR coord posts on #1272, #1276, #1273 that referenced the LP/SDP reduction prediction should be acknowledged as referencing a falsified claim; the **filtration-shape correlation** with their h² / Bring + compact-q-dilog findings still holds, just not through the LP/SDP path I described.
