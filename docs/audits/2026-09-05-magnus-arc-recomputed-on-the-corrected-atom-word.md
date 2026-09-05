# The whole Magnus arc was measured on a superseded braid word — every number moves, every conclusion survives

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` · **Scope:** (a) scope-limited — complete n=9 census,
recomputed. Nothing wired, no witness, no fit.

## The claim

Every measurement in this arc before **2026-09-05 07:53 UTC** was computed against a braid word `ρ`
that a sibling has since corrected. `7db032fb48` (bean `qou-hu1f`, owner ruling) fixed
`atom_braid_word_3A` to emit the interleaved `β_Bor` where it had been emitting the same letters
**bucketed by generator**. Since `σ₀` and `σ₁` do not commute, that is a different element of
`H_n(q)`, and the sibling measures the two **82 % apart at q₀**.

Verified directly, same commit boundary, A=3 (`n=9`), both words length 35:

```
old: 0 0 0 0 0 0 0 1 1 1 1 2 3 3 3 3 3 3 3 4 4 4 4 5 6 6 6 6 6 6 6 7 7 7 7
new: 0 1 0 1 0 1 0 0 1 0 0 2 3 4 3 4 3 4 3 3 4 3 3 5 6 7 6 7 6 7 6 6 7 6 6
```

Same multiset of letters, different order. A=4 (`n=12`, length 47) differs the same way. So this is
not a q₀ re-pin or a precision question — **the arc was tracing a different operator**, and this
document recomputes it.

**Result: the numbers all move, and every structural conclusion survives.** Two of them strengthen.

## How it surfaced, which is the part worth keeping

Not by anyone checking. I quoted `291.4×` for the hook column's fall from a run of the hook-κ probe,
and the *committed* probe printed `263.16×`. Chasing that 10 % gap is what found the word change —
the discrepancy was between two runs of **my own code** on either side of a sibling's merge.

The tell was mechanical and worth recording: the output I had quoted carried an **ASCII header**
(`kappa`, `S|eig|`) where the committed probe prints unicode (`κ`, `Σ|eig|`). That is what
distinguished a stale draft run from a current one, not the numbers.

**A 10 % discrepancy is exactly the size that reads as a rounding or precision artifact.** Had the
word moved a number by 3 % instead, I would have had no reason to look, and this arc would have gone
on quoting two incompatible families of numbers as though they were one.

## What moves

All at `n=9`, dps 65, complete 30-shape census, `q₀` unchanged.

| quantity | old word | corrected word |
|---|---|---|
| `\|tr\|/dim` at `(8,1)` | 33.648 | **29.00125** |
| `\|tr\|/dim` at `(2,1⁷)` | 0.11547 | **0.110202** |
| hook column fall, `b=1→7` | 291.4× | **263.16×** |
| `Σ\|eig\|/dim` fall | 213.3× | **215.54×** |
| hook κ minimum | `b=5` | **`b=4`** |
| envelope `√E(b)`, `b=1` | — | **64.4015** |
| link-1 slack range | 2.04 – 550× | **2.221 – 1217×** |
| worst-slack shape | `(3,2,1⁴)` | **`(5,2,1,1)`** |

## What survives

**1. The chain still closes, on every shape.** `|tr_λ|/dim_λ ≤ √(tr_λ(X*X)/dim_λ) ≤ √(E(b))`, both
links ✓ across all 30 shapes.

**2. The envelope is still strictly decreasing in `b`, over all 7 complete levels:**

```
64.4015 > 50.2782 > 30.9082 > 22.2643 > 16.3081 > 7.91075 > 1.7048
```

**3. The hook crossing is at `b=4` — the same `b` as before.** Ranking each level by the majorant
`√(tr(X*X)/dim)`, the hook is its level's **maximum** at `b=2,3` and its **minimum** at `b=4,5,6,7`.
That the crossing lands on the same interior `b` under a different operator is the strongest single
piece of evidence the arc has that the hook split is structural rather than incidental.

**4. The hook κ column is still U-shaped** — 0.8834, 0.3204, 0.04976, 0.02365, 0.08988, 0.15743,
0.72353. The minimum moves `b=5 → b=4`; the shape does not.

**5. The #6785 correction survives and strengthens.** That correction said hooks are the
**best**-bounded family and non-hooks the worst — the opposite of what the ordering measurements had
suggested. Recomputed:

| family | slack range | median |
|---|---|---|
| hooks (7 shapes) | 2.221 – 171.0 | **24.51** |
| non-hooks (21 shapes) | 12.05 – **1217.0** | **100.5** |

4.1× worse at the median and 7.1× at the maximum, against 3.3× / 6.7× on the old word.

**6. The #6754 headline strengthens.** "The chain closes but the majorant route cannot carry the
size" is *more* true: worst-case link-1 slack goes 550× → **1217×**.

**7. The Féray–Śniady prune is unaffected** — `magnus_fs_transpose_prune_probe.py` was written after
the fix and its 263.16× is on the corrected word throughout.

## What this does NOT establish

- **The `n=12` legs are not recomputed here.** The A=4 word changed identically, so the `n=12`
  hook-rank crossing (#6748) is measured on the old word and is **unverified** under the correction.
  It is the one surviving load-bearing claim in the arc that this document does not cover.
- **Nothing is proved for general `n`.** As before, these are measurements at one size.
- **"Survives" is not "was unaffected".** Every number quoted in five merged audit docs is wrong by
  4–16 %, and those docs need correcting whatever their conclusions do.
- **The 82 % figure is the sibling's**, measured on the confinement element, not re-derived here.
  What is re-derived here is that the words differ and what that does to this arc.

## Affected merged artifacts

Carrying old-word numbers, conclusions intact but figures wrong:

- `2026-09-05-magnus-three-independent-measurements-one-hook-split.md` — the whole hook column table,
  `213.3×`, `291.4×`, `550.20`, and the `b=5` κ minimum
- `2026-09-05-magnus-kappa-census-two-questions-disentangled.md` — `33.648`, `0.936176`
- `2026-09-05-magnus-chain-closes-but-the-majorant-route-cannot-carry-the-size.md` — `550.2`
- `2026-09-05-magnus-sl3-kostka-third-handle-and-first-complete-levels.md` — `4718.62`
- `2026-09-04-magnus-hook-vs-tworow-reverses-and-the-cap-comes-off.md` — `4718.62`
- bean `qou-o6ov` — `4718.62`

## The method note this cost

**A probe that reads a shared producer is dated by that producer, and nothing in its output says so.**
Every probe here prints its `q₀`, its `dps` and its `n` — the three things that were never in doubt —
and none prints the braid word or a hash of it. The `_assert_dps` guard (#6710) exists because
exactly this class of silent-input drift had already bitten this arc once, and it guards the one
input that had already been caught.

The cheap fix is to print `hash(tuple(gens))` alongside the dps line, so two runs are comparable
without re-deriving where their inputs came from. Recorded as follow-up work in the bean rather than
done here, since it touches every probe in the arc.
