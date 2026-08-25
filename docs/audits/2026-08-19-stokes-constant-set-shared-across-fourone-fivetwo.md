# RETRACTED — the `4₁`/`5₂` `{3,4}` "cross-knot prune" duplicates PR #4567, and its framing misstated the corpus

**Date:** 2026-08-19 · **Bean:** `qou-xpgq` (RETRACTED) · **Parent:** `qou-qnnq`
**Status:** the probe is **deleted**; the claims below are **withdrawn**. Recorded
rather than removed because the *way* the corpus-grep failed is the reusable part.

## What I claimed, and why it was wrong

I claimed that `4₁` and `5₂` share the Stokes-factorization constant set `{3,4}`,
that this was a new cross-knot observation, and that the corpus had read `5₂`'s
sandwich "for its matrix **shape** (3×3), not its **constants**."

**That last sentence is false**, and it was the load-bearing one. The corpus had
already done exactly this work, on 2026-08-02, in PR #4567:

- [`computations/probes/fivetwo_crossknot_34_distinguisher.py`](../../computations/probes/fivetwo_crossknot_34_distinguisher.py)
  — *"the 5₂ cross-knot {3,4} structural distinguisher"*, which reads the same two
  witnesses for the same purpose.
- [`FiveTwoDTSpectrumSplit.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/FiveTwoDTSpectrumSplit.lean)
  — Lean-proved, and named for the constants, not the shape.
- [`2026-08-02-fivetwo-crossknot-34-resolution.md`](2026-08-02-fivetwo-crossknot-34-resolution.md)
  — the audit.

My probe was a re-derivation of a landed result, presented as new.

## The corpus reading I misrepresented

Worse than duplication: I attacked a position the corpus does not hold.

1. **`5₂` does not simply "carry the set `{3,4}`" — it splits it across
   chirality.** `S⁺(0)` carries the `4`, `S⁻(0)` carries the `3`
   (`FiveTwoDTSpectrumSplit.dt_spectrum_two_element`). `4₁` is amphichiral and its
   single 2×2 block carries `3`. Flattening both to "the same set" erases the
   distinction the corpus built `5₂` to expose.
2. **The `3` and the `4` are not two values of one index — they are two different
   `4₁` quantities.** Per the attack-options memo §2c: **the `4` is a boundary
   slope** (`4₁`'s slopes are `{0,±4}`), and **the `3` is the number of
   boundary-parabolic `SL₂(ℂ)` flat connections** `{0,g,ḡ}`. My table treated
   "#connections" as a candidate index for the *whole set* and "pruned" it; the
   corpus never proposed that.
3. **The distinguisher already found the stronger negative** I thought I was
   contributing: the literal `4₁` symmetry constant `(S₁₂+S₂₁)/S₁₁` is **not**
   q-exact for either `5₂` block, so **no single scalar clones across the two
   knots**. My "shared constant set ⇒ a knot-independent index" reading runs
   against that, and I did not engage it because I had not read it.

## Why the corpus-grep missed it — the reusable part

I ran the §"Before declaring 'open'" checklist and it returned clean, because I
grepped for the **vocabulary of my own framing**: `5₂.*Stokes` across
`docs/audits/`, and `5two` across `computations/probes/`. The landed work is filed
under **`fivetwo`** and **`crossknot`**, and its Lean lives in a tree I never
grepped at all.

- `grep -rln "5two" computations/probes/` → hits, none named for the constants
- `grep -rln "fivetwo\|crossknot" .` → the probe, the audit, and the Lean, at once
- **I never grepped `content/**/lean/`** despite the target being a Lean-recorded fact.

This is the same defect PR #5293 self-reported three weeks of corpus-time earlier —
*"a corpus sweep keyed on the vocabulary of the answer you expect will miss the
paper that answers in different words"* — and I repeated it, in the same arc, on
the same knot pair, having read that sentence. **Grep the object's alternate
spellings (`4₁`/`4_1`/`fourone`, `5₂`/`5_2`/`fivetwo`) and grep the Lean tree.**

## What survives — one guess, explicitly unsupported

The Wedderburn pair of `H_n` at the braid index,
`(#blocks, Σ_λ dim V_λ) = (p(n), I(n))`, equals `(3,4)` at `n = 3`, and both `4₁`
and `5₂` have braid index 3. I have **not** found this specific `F` in the corpus,
and the attack-options memo states the target's *shape* (`F(Wedderburn mult of
H_n, Markov-trace data, Bring embedding) = DT-spectrum(K)`) without naming it.

But its evidential support is far weaker than I presented:

- it is consistent with two knots of **equal** braid index, which is no test at all
  of a braid-index-indexed rule;
- it does not reproduce the **chirality split**, which is the actual structure at
  `5₂`;
- it competes with a corpus reading in which the two integers have **separate
  geometric origins** (slope; connection count), and it offers no reason they
  should instead be a Wedderburn pair.

It yields one falsifiable prediction: `6₁` has braid index 4, so `(p(4), I(4)) =
(5, 10)` — the `10` being absent from the `#connections` reading, which predicts
`5`. Bean `qou-btvl` and PR #5293 both name `6₁`'s independent resurgence DT count
as the missing datum. **Recorded as a bare guess to be shot at, not as a result.**
`⚠ The braid index of `6₁` is taken from standard knot tables and is NOT verified
against any in-repo primary source — the corpus braid database carries 3-strand
knots only. Verify before relying on it.`

## Discipline

`qou-qnnq` was open before this and is open after it. Nothing was wired, no `c_k`
touched, no tier changed. The correction is also posted to PR #5293, where I had
sent the prediction with the over-stated support attached.
