---
# qou-x64l
title: Retire the ASCII H4 basis — it is the subscript basis relabelled, and the permutation is explicit
status: todo
type: task
created_at: 2026-08-09T17:21:10Z
updated_at: 2026-08-09T17:21:10Z
---


The tree carries **two** 24-word normal-form bases for `H₄(q)`:

| | module | has | lacks |
|---|---|---|---|
| **ASCII** | `QOU/Machinery/MarkovTraceH4.lean` + `MarkovTraceH4Gram0..7` | `trM`, `gram_symm`, **`trM_cyclic`** (all sorry-free) | associativity, `Ring`, `Algebra` |
| **subscript** | `HeckeH4StabilizationRung` + `HeckeH4AlgebraLaws` | the presentation, `mulNF₄_assoc`, `H4A` `Ring`/`Algebra`, `wedderburn₄`, semisimplicity, the `HeckeAlgebra` + `IsHeckeOfFullRank` instances | **cyclicity** |

`HeckeH4AlgebraLaws` deliberately does not import `MarkovTraceH4`, so the two have
never been connected, and the only thing keeping the ASCII chain alive is that it
owns cyclicity.

## They are the same basis, relabelled

Checked by mapping each reduced word to its `S₄` element (`s_k` = adjacent
transposition):

* both word lists give **24 distinct** `S₄` elements, and **the same 24**;
* the index permutation ASCII → subscript is
  `[0,6,2,1,7,9,8,4,3,12,10,13,11,5,14,16,15,17,18,19,20,21,22,23]`;
* the trace weights agree exactly under it — `TRM[i] = TRM4[perm i]` for all `i`;
* only **6 of 24** words differ at all, and every difference is a single
  far-commutation swap `σ₂σ₀ ↔ σ₀σ₂`:

  | i | ASCII | subscript |
  |---|---|---|
  | 12 | `σ₁σ₂σ₀` | `σ₁σ₀σ₂` |
  | 16 | `σ₀σ₁σ₂σ₀` | `σ₀σ₁σ₀σ₂` |
  | 17 | `σ₁σ₂σ₀σ₁` | `σ₁σ₀σ₂σ₁` |
  | 20 | `σ₀σ₁σ₂σ₀σ₁` | `σ₀σ₁σ₀σ₂σ₁` |
  | 22 | `σ₁σ₂σ₀σ₁σ₀` | `σ₁σ₀σ₂σ₁σ₀` |
  | 23 | `σ₀σ₁σ₂σ₀σ₁σ₀` | `σ₀σ₁σ₀σ₂σ₁σ₀` |

  and `far_commute_σ₀σ₂` is proved, so those are equal *in the algebra*, not only
  as group elements.

Two earlier readings of this comparison were wrong and are recorded so nobody
repeats them: comparing the word *tuples* says the sets differ (they do — 6
entries — but the elements do not), and comparing the weight strings without
normalising whitespace says the multisets differ (the subscript `TRM4` literal is
multi-line, so its entries carry newlines).

## The task

1. Define the permutation `π : Fin 24 → Fin 24` above, prove it is a bijection,
   and prove the two bases correspond under it — the 6 differing words need
   `far_commute_σ₀σ₂`, the other 18 are `rfl`.
2. Transport `QOU.Machinery.H4.trM_cyclic` along `π` to give cyclicity for
   `trM4` on the subscript basis. **No second Gram closure.**
3. That unblocks `QOU.Hecke.MarkovTrace 4 q (H4A K (q − q⁻¹))` and a
   `MarkovTraceContext` at `n = 4` — the last open Hecke item below `n = 5`.
4. Then retire the ASCII chain: `MarkovTraceH4.lean` and `MarkovTraceH4Gram0..7`,
   ~6.5k generated lines. `QOU/Hecke/InstanceH4.lean` goes with it — it is built
   on the ASCII actions and qou-ti7p already lists it as a redundant carrier.

## Why this is worth doing beyond tidiness

The ASCII Gram chain is **the tree's build pole**: eight chained modules, ~4.3 GB
peak, and the reason a full `lake build` takes ~55 minutes instead of ~5. Retiring
it after the transport removes that cost permanently, and removes a standing
drift hazard — two hand-maintained tables for the same algebra, which is the
defect class this whole audit keeps turning up.
