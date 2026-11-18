---
# qou-3x8x
title: 'GAP: perknot-additive-sk-vs-kA probe is stale against a 31x upstream move, and its verdict prose hardcodes the OLD numbers'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T06:05:43Z
updated_at: 2026-10-04T15:20:17Z
parent: qou-5vkl
---

## What is measured

`computations/probes/perknot-additive-sk-vs-kA-extensivity.witness.json` does not reproduce from its own producer. A fresh run on `main` differs in **172 leaves**, and the disagreement is not rounding — it changes the probe's stated shape.

| quantity | committed | fresh |
|---|---:|---:|
| `mu_ext_order_desc` | `4He / D / T / 3He` | **`4He / T / D / 3He`** |
| `mu_ext_spread_max_over_min` | **2.83** | **59.12** |
| `best_real_spearman` | 0.40 | 0.80 |
| `best_junk_spearman` | 0.316 | 0.632 |

## The cause: a 31× move in one upstream entry

The probe reads `mu_ext_target` from `deltalambda/deltalambda-extensivity-gap-synthesis.witness.json`. Comparing the committed consumer's own recorded targets against that upstream today:

| atom | consumer recorded | upstream now | factor |
|---|---:|---:|---:|
| D | 5.8529 | 6.0677 | 1.04 |
| T | 4.4441 | 6.7061 | 1.51 |
| ³He | 3.2918 | 4.9054 | 1.49 |
| **⁴He** | **9.3133** | **290.0067** | **31.1** |

`9.3133 / 3.2918 = 2.83` — the committed spread is self-consistent with the values the consumer recorded. `290.0067 / 4.9054 = 59.12` — the fresh spread is self-consistent with the upstream today. **Both runs are internally correct; the input moved underneath.** D and T swap rank because T rose 51 % while D rose 4 %.

The one upstream change visible in this shallow clone (`831980f1ce6`, 2026-09-04) moves `mu_ext_target` only in the **8th significant digit** — it is *not* the 31× move. So the ⁴He change happened earlier, before the clone's horizon, and cannot be dated here (see `qou-kfeg`). The consumer witness was last touched at the shallow-boundary commit.

## The defect that is NOT staleness, and would survive fixing it

The verdict string interpolates the **computed** spread at one line and **hardcodes** the old one four lines later:

```python
f"×{float(mu_spread):.2f}, deuteron 2nd-largest from its tiny "     # line 251, computed
...
f"monotone/compressed (spread ×1.14 across the four) and cannot "   # line 257, HARDCODED
f"supply mu_ext's ×2.83 non-monotone range, ..."                    # line 258, HARDCODED
```

So a fresh run emits a `verdict` that **contradicts itself inside one string**: "spread ×59.12" and "cannot supply mu_ext's ×2.83 non-monotone range". The claim "deuteron 2nd-largest" (line 251, and again in the assertion `source` at line 335, "D 2nd, 4He max") is hardcoded prose too, and is now false — T is 2nd.

This is independent of the staleness. Even with correct inputs, three assertions in the conclusion text are literals that no longer track the computation they describe. A reader — or a content block quoting the verdict — gets the pre-move numbers with a post-move ordering.

## What SURVIVES

**The PRUNE conclusion holds.** The test is whether the best real candidate beats the best junk control by a meaningful n=4 margin, and on the fresh numbers it still does not: best real Spearman **0.80**, best junk **0.63**, margin **0.17 < 0.25**, so `beats_by_>0.25 = False`. The scope-(a) negative — the per-knot additive `S(K)/tr_M` reading does not inform the `k(A)` extensivity multiplier — is unaffected by the input move. Only its supporting figures were wrong.

That is worth stating plainly because it is the useful half: a 31× move in the dominant input did **not** overturn the verdict, which is evidence the verdict is about shape rather than magnitude.

## Disposition

Fixing the hardcoded literals to interpolate the computed values falls under the ASK-FIRST rule's exemption 2 (derived from the corpus — the producer computes the quantity one line above the literal that contradicts it), and regenerating a stale witness is ordinary upkeep. Both ride the raw-float64 drain of this producer.

**Not** in scope here, and left for the owner: whether the ⁴He `mu_ext_target` of 290 is itself right. It is 31× its previous value and 43× the next-largest isotope, which is a large enough discontinuity that it deserves its own look; this bean does not assume either value is correct, only that the consumer and the upstream disagree.

- **Round 94 (`litlfred/qou#8424`)**: Advanced in `feat/round94-parity-level-lever1depth2-tauclosed-chainlog-43c1` (Commit 1 `c1698951b30460bb111c1e97552482f0b0622bd0`, Commit 2 `5a166eac86b999ab31c9bdd39f5908e1c848e122`, probe sha256 `1438398dfd335d3f6e9ebdcaa8df8fdc4613a507b4d480b0c9dde22e4b3c8bcb`).
