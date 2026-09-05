# The reflection-rep sign conjecture holds — its supporting evidence does not

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` (rescoped) · **Scope:** (a) scope-limited — A = 2, 3, 4
at one q₀, complete ≤2-row column, both elements. Nothing wired, no witness, no fit.
**A positive result and a correction to the evidence for it.**

## The conjecture

From `magnus_sign_row_truncation_probe.py`, the probe this bean came from:

> *"As A→∞, sign(P(A)) is determined by the reflection representation (n−1,1)."*

with `P(A) = Σ_λ y_λ tr(ρ_λ Ω₂^P)`. Its recorded evidence is a sign margin `|P| / Σ_λ|c_λ|` of
**69 % (A=2) → 99 % (A=3) → 99.9 % (A=4)**, described as *"GROWS with A"*.

Both halves needed re-measuring, for reasons independent of each other: those figures are
**convention C** (the ≥3-row terms they sum carry weight zero under D), and they are for the
**bare-σ ρ** (`atom_braid_word_3A` returns Hecke letters `c·σ_g + d·1`; the arc applied a bare `σ_g`,
wrong for 24 of 47 letters at A=4 — #6822).

## Result: the conjecture holds, at every A tested, under both elements

| A | n | `sign P` | `sign c_(n−1,1)` | verdict |
|---|---|---|---|---|
| 2 | 6 | − | − | **HOLDS ✓** |
| 3 | 9 | − | − | **HOLDS ✓** |
| 4 | 12 | − | − | **HOLDS ✓** |

Same verdict for ρ_bare and ρ_true. This is the arc's first clean positive on the corrected element,
and it is worth stating plainly after a run of negatives.

## But the evidence for it does not survive, in either direction

| A | margin, ρ_bare (D) | margin, ρ_true (D) | recorded (C, bare-σ) |
|---|---|---|---|
| 2 | **100.0 %** | 68.21 % | 69 % |
| 3 | 98.95 % | 64.65 % | 99 % |
| 4 | **100.0 %** | 67.02 % | 99.9 % |

**"Grows with A" is wrong under D on both elements, and wrong differently on each:**

- **ρ_true: flat at ~65–68 %.** No growth, and no trend across three sizes.
- **ρ_bare: saturated at ~99–100 % from A=2 onward.** It cannot grow because it starts at 100 %.

The recorded 69 % at A=2 is the C-frame figure; under D the same element gives **100 %**, because the
≥3-row terms that were cancelling against the two-row ones are exactly zero under D. So the reported
*growth* was the ≥3-row cancellation being progressively outweighed — an artifact of summing terms
that convention D removes.

## What actually holds the sign up, and it is not dominance

At A=4 under ρ_true, the reflection term carries **59.44 %** of `Σ|c_λ|` while the margin is
**67.02 %** — the margin *exceeds* the k=1 share. That is only possible if the remaining terms, on
net, **reinforce** the reflection term's sign rather than eroding it. They do: they sum to
`−0.012258` against `c_(n−1,1) = −0.096085`, same sign.

This matters because the two supports behave oppositely as `A` grows:

- the reflection term's **share is eroding** — 77.88 % → 73.50 % → **59.44 %**;
- the **margin is not** — 68.21 % → 64.65 % → 67.02 %.

So by A=4 the conjecture is being held up partly by the non-reflection terms happening to net the
right way, not by the reflection term dominating. **That is a weaker basis than the original framing
claims, and it is the configuration in which the conjecture fails first at some larger A** — a
cancellation that happens to reinforce is not one that has to keep reinforcing.

## The true element cancels; the bare element does not

The margin difference is a real structural fact about the two elements, not a scale effect:

| | between-term cancellation at A=2/3/4 |
|---|---|
| ρ_bare | **~0 %** (margin 100 / 98.9 / 100) |
| ρ_true | **~33 %** (margin 68.2 / 64.7 / 67.0) |

Under ρ_bare every two-row term carries the same sign, so nothing cancels between them. Under ρ_true
the signs genuinely alternate — at A=4: `− + − − + +` across k=1…6 — and about a third of the
absolute mass cancels.

**Do not read this as bearing on the bean's "concentration is a trace cancellation" claim**, which is
about cancellation *within* each `tr_λ` (from `tr(Ω₂) = 0`). The margin measures cancellation
*between* terms. They are different quantities and this document measures only the second.

## What is NOT established

- **A ≤ 4, one q₀.** Three sizes is not an "as A→∞" statement, in either direction. This session has
  already been caught once treating two agreeing sizes as a mechanism.
- **The conjecture is confirmed, not proved.** No argument is offered for why the signs agree.
- **Why the non-reflection terms net-reinforce at A=4 is unexplained.** It is measured, and I have no
  account of it; whether it is structural or incidental is exactly what would decide the conjecture.
- **A=5 is running** for the column and is not in this document.
- **The C-frame figures are not wrong** — they are correct for convention C and the bare element, and
  are kept above as the record of what was measured then, per the `qou-3nva` precedent.
