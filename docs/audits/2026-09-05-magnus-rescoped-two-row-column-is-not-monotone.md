# The rescoped claim is false too: the ≤2-row column does not decay for the true element

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` (rescoped this session on owner instruction) ·
**Scope:** (a) scope-limited — A = 2, 3, 4 at one q₀, complete ≤2-row column. Nothing wired, no
witness, no fit. **Negative result, and it kills a route I proposed in the same session.**

## Why this column and not the census

Under **convention D** (owner ruling 2026-08-09) `y_λ = 0` for `ℓ(λ) > 2`, so
`P(A) = Σ_λ y_λ tr(ρ_λ Ω₂^P)` runs over ≤2-row shapes `(n−k, k)` only — exactly `⌊n/2⌋+1` of them
(#6822). The two-row column used to be one handle among several; it is now **the entire object**, and
everything off it carries weight zero. That is what the bean was rescoped to on 2026-09-05.

It is also cheap: at n=12 the largest two-row dim is `(7,5)` at 297, against 792 for `(4,3,3,2)` in
the full census, so all three sizes cost less than one level of the old census.

Both elements are computed, because every pre-#6822 number in this arc used a bare `σ_g` per letter
where `atom_braid_word_3A` returns the Hecke element `c·σ_g + d·1` — wrong for 24 of 47 letters at
A=4.

## The result

`|tr_{(n−k,k)}(ρ·Ω₂^P)| / dim`, and the y-weighted mass `|c_λ| = y_λ·|tr|`, monotonicity in `k`
measured from `k=1` (`k=0` is the trivial rep, where `Ω₂` vanishes identically — proved, Lean
sorry-free, #6387):

| A | n | `\|tr\|/dim` ρ_bare | `\|tr\|/dim` ρ_true | `\|c_λ\|` ρ_bare | `\|c_λ\|` ρ_true |
|---|---|---|---|---|---|
| 2 | 6 | decreasing ✓ | **1 rise** ✗ (k=3, ×2.144) | decreasing ✓ | decreasing ✓ |
| 3 | 9 | decreasing ✓ | **1 rise** ✗ (k=4, ×1.416) | decreasing ✓ | decreasing ✓ |
| 4 | 12 | **1 rise** ✗ (k=6, ×1.179) | **2 rises** ✗ (k=4 ×3.006, k=6 ×7.553) | decreasing ✓ | **2 rises** ✗ (k=4 ×3.675, k=6 ×1.103) |

**Three statements, in order of how much they cost:**

1. **`|tr|/dim` on the column is not monotone for the true element at any A tested.** One rise at
   A=2 and A=3, two at A=4.
2. **The y-weighted mass — the quantity the sum actually weights by — is monotone at A=2 and A=3 and
   NOT at A=4.** This is the one that matters, and it is the one that fails in the direction of
   increasing `A`, which is the direction the physics runs.
3. **Even ρ_bare fails on this column at A=4** (`k=6`, ×1.179). The arc's clean monotone results were
   for the full-census *envelope*, a different quantity; on the column the old element is not
   monotone either once `A` is large enough.

## The route this kills, which I proposed an hour earlier

From A=2 and A=3 alone the picture looked tractable and I said so. The bumps sat at the **squarest
shape** (the last `k`), and the weight ratio there is large, so the y-weighting dominated:

| A | trace rise at last k | `y_k/y_{k+1}` | margin |
|---|---|---|---|
| 2 | ×2.144 | 3.044 | 1.42× |
| 3 | ×1.416 | 2.044 | 1.44× |

Two nearly identical margins across different `n` looked like a mechanism, and the mechanism has an
exact closed form. Under convention D the two-row `y_λ` are SU(2) quantum dimensions, so

```
y_k / y_{k+1}  =  [n − 2k + 1]_q / [n − 2k − 1]_q
```

verified against the measured ratios rather than assumed. Its profile at `q₀`:

```
[3]/[1] = 3.0436    [4]/[2] = 2.0437    [5]/[3] = 1.7152    [6]/[4] = 1.5544    [7]/[5] = 1.4607   → q² = 1.2321
```

**Largest at the square end, falling toward `q²` at the long end** — so the weight protection is
strongest exactly where the A=2 and A=3 bumps were. That is why the route looked good.

**A=4 kills it, and the way it dies is worse than "the bump moved".** Both A=4 rises lose:

| step | position | trace rise | weight ratio | margin |
|---|---|---|---|---|
| `k=3→4` | mid-column | ×3.006 | `[7]/[5]` = 1.4607 | **×0.486 — weight loses** |
| `k=5→6` | **square end** | ×7.5531 | `[3]/[1]` = **3.0437** | **×0.403 — weight loses** |

My first reading of this was that the A=2/A=3 margins were a column-length artifact — those columns
being short enough that their only bump *had* to land at the protected end. That is true of the
mid-column rise and it is **not the main point**, because the square-end rise loses too, at the very
place where protection is maximal.

**The sharper statement, and it is the reusable one.** The weight ratio is
`[n−2k+1]_q/[n−2k−1]_q`, which is maximised over the whole column at the square end, where it is
`[3]_q/[1]_q = [3]_q ≈ 3.0437` — **a constant, independent of `n`**. So the y-weighting can absorb a
trace rise of at most `[3]_q` anywhere, ever. That gives a clean necessary condition:

> y-weighted monotonicity on the ≤2-row column requires **every** `|tr|/dim` rise to be
> `< [3]_q ≈ 3.0437`.

Measured, the square-end trace rise runs **×2.144 (A=2) → ×1.416 (A=3) → ×7.553 (A=4)**. It breaks
through the ceiling at A=4. The route does not fail by a small margin that a sharper analysis might
recover — it fails against a fixed bound that cannot be raised, because `[3]_q` is where the weight
family tops out.

## What survives

**Concentration, which is not monotonicity.** The mass share at `k=1` under the true element is
77.9 % (A=2), 73.5 % (A=3), **59.4 %** (A=4) — falling with `A`, but still the dominant term. So a
statement of the form *"the tail beyond `k=1` is bounded by X"* is not excluded by anything here;
what is excluded is *"the terms decrease in `k`"*.

That is a genuinely weaker target than the bean has been pursuing, and it is the honest one: **the
next attempt should bound the tail, not order the terms.**

## What is NOT established

- **A ≤ 4, one q₀.** The A=4 counterexample refutes monotonicity at that size; it says nothing about
  whether some weaker bound holds, and nothing about large `A`.
- **The `k=6` rise at A=4 is at the square shape `(6,6)`**, where `dim` drops sharply (297 → 132), so
  `|tr|/dim` can rise from the denominator alone; I have not separated the two. **This matters for
  the ceiling argument**, since that rise is the one that breaks `[3]_q` by the largest factor. The
  `k=3→4` rise has no such ambiguity (dim 154 → 275, *rising*, so the ×3.006 is the trace) and it
  independently loses its own margin at ×0.486 — so the conclusion survives even if the `k=6` rise
  turns out to be a dimension effect. Separating them is the first thing to check next.
- **Nothing here bounds anything.** No tail bound is attempted, and the surviving concentration
  statement is measured at three sizes, not proved.
- **Whether the y-weighted failure persists at A=5** is unmeasured and is the obvious next check —
  n=15 has 8 two-row shapes with max dim ~1000, still tractable.

## Method note

This is the second route I have killed in this session by measuring one size past where the pattern
looked clean, and both times the extra size was cheap. The A=2/A=3 margin table above is the kind of
thing that reads as a finding — two independent sizes, agreeing to 1 %, with a closed-form mechanism
behind it — and it was wrong because both columns were too short to place a bump anywhere but the
protected end. **A pattern that can only manifest one way is not evidence that it manifests that
way.** The cost of checking was about ten minutes.
