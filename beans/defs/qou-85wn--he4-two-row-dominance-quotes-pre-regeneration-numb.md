---
# qou-85wn
title: he4-two-row-dominance quotes pre-regeneration numbers — thesis survives, every table value is stale, one contribution flips sign
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T12:44:43Z
updated_at: 2026-10-04T15:20:44Z
parent: qou-10v9
---


## The finding

`folio/quantum-observable-universe/mass-theory/he4-two-row-dominance.md` is a
**reader-facing** content block whose table was computed against the
`chi-helium-4-h12-at-q0-50dps` cache as it stood before the 2026-09-06
regeneration (`qou-92u9`, owner ruling "regen").  Content blocks are not
re-run by any witness sweep, so nothing caught this.

## What SURVIVES — and it is the block's actual thesis

- The `y_λ` column is **identical**: `1.7441e-3`, `1.1941e-3`, `2.3704e-3`,
  `6.9619e-4`.  `w` is a function of the partition and `q` alone, so it could
  not move — the same invariance that held across the whole O3′ arc.
- The structural claim — *"the two-row-stratum ratio is **exactly 1**; all 70
  partitions of 12 with more than two rows contribute 0"* — **still holds**,
  measured 1.0 exactly.  The `≥ 0.80` bound is still satisfied.

**So the block's conclusion is not in question.**  Two-row dominance survives.

## What is STALE — every number in the table

    quantity            block says        regenerated      note
    tr_M(β_4He)(q0)     0.160974145442    0.0112374176598  factor 14.3248
    χ(9,3)              +27.3348          +4.14962
    χ(8,4)              +30.2676          −2.97948         SIGN FLIP
    χ(10,2)             +10.4630          +0.543341
    χ(7,5)              +21.7770          +0.424982
    contribution (9,3)  29.617 %          64.406 %
    contribution (8,4)  22.452 %          −31.659 %        NOW NEGATIVE
    contribution (10,2) 15.407 %          11.461 %
    contribution (7,5)  9.418 %           2.6329 %

## 🛑 The sign flip is not just a number — it changes the picture

Under the old data the table read as five positive blocks sharing the trace.
Under the regenerated data `(8,4)` contributes **−31.7 %**: the "dominance" is
now a partial cancellation between a large positive `(9,3)` and a large negative
`(8,4)`, not a straightforward concentration.  The *ratio* is still exactly 1,
so the stated claim is untouched — but a reader given the new table would draw a
different qualitative conclusion from the same sentence.

## Why this is not being edited unilaterally

Three reasons, in order of weight:

1. **It is the paper.** A math-bearing `.md` table is reader-facing content, and
   AGENTS.md gates such edits behind the render-QA battery (balanced delimiters,
   the align-family fencing rule, the expository pass) plus sidecar refresh.
2. **The sign flip is an interpretive change, not a transcription.** Rewriting
   `+22.452 %` to `−31.659 %` inside prose about "dominance" is a judgement about
   what the block should now *say*, which is the author's call.
3. The numbers can be regenerated mechanically at any time; the sentence around
   them cannot.

## What to check next

Whether other content blocks quote chi-cache-derived numbers.  The scan that
found this one covered `content/`, `docs/audits`, `docs/coordination` and
`.beans` for citations of the 78 witnesses this branch refreshed: **176 files
cite one**, of which **6 are under `content/`**.  Most citations are references
rather than quoted values — this block is the one confirmed to quote numbers
that moved.  The other five are unchecked.


## 🛑 CORRECTION 2026-09-06 — my own table above is INCOMPLETE, and what it omits is the finding

The stale-vs-regenerated table above lists four partitions. ⁴He has **seven**
nonzero blocks, and **the two I left out are the two that matter**. Full
regenerated table, all seven, computed from
`chi-helium-4-h12-at-q0-50dps.witness.json` (`computedAt` 2026-09-06T03:24:25):

| λ | y_λ | χ^λ | c_λ | % of \|total\|, was → is |
|---|---|---|---|---|
| **(12)** | +3.9658e-3 | **+2.41984** | **+9.5965e-3** | 5.962 → **85.398** |
| (9,3) | +1.7441e-3 | +4.14962 | +7.2375e-3 | 29.617 → 64.406 |
| **(11,1)** | +3.1003e-3 | **−1.48208** | **−4.5950e-3** | +14.235 → **−40.890** |
| (8,4) | +1.1941e-3 | −2.97948 | −3.5577e-3 | +22.452 → −31.660 |
| (10,2) | +2.3704e-3 | +0.543341 | +1.2880e-3 | 15.407 → 11.461 |
| (6,6) | +2.2873e-4 | +4.25063 | +9.7225e-4 | 2.909 → 8.652 |
| (7,5) | +6.9619e-4 | +0.424982 | +2.9587e-4 | 9.418 → 2.633 |

Three corrections follow, and the third is the one with consequences.

### 1. TWO sign flips, not one — and the larger one is the one I missed

I recorded `(8,4)` flipping `+22.452 % → −31.659 %`. **`(11,1)` also flips, and
by more: `+14.235 % → −40.890 %.`** Its character goes `+7.3910 → −1.48208`.

### 2. THE RANK ORDER CHANGED, AND THE TOP BLOCK IS NO LONGER (9,3)

was: (9,3), (8,4), (10,2), (11,1), (7,5), (12), (6,6)
now: **(12)**, (9,3), (11,1), (8,4), (10,2), (6,6), (7,5)

This matters because the block's closing paragraph makes a **second claim**
that my note above did not examine at all:

> *"The canonical formalism predicts the top block λ\* = (9,3) via the Δ_λ
> empirical-tabulation route. This proposition derives the identical
> fingerprint from the Σ_λ y_λ·χ^λ_q Wedderburn sum."*

So when I wrote *"the block's conclusion is not in question"*, that was true of
the **Proposition** — the ≥ 0.80 stratum bound, still exactly 1 — and **false of
the block's closing claim**, which I had not checked. `λ* = (9,3)` is wrong
against the data the corpus now holds.

### 3. But the two routes STILL AGREE — which makes the fix mechanical, not interpretive

`delta-lambda-empirical-tabulation.witness.json` was itself regenerated
(`computedAt` 2026-09-06T06:47:25) and reports

```
cross_atom_pattern_ansatz_a.top3_by_atom["4He"] = [[12], [9,3], [11,1]]
```

against the Wedderburn-sum order **(12), (9,3), (11,1)** — **exact match on all
three**, and its `tr_M` field is byte-identical to the regenerated cache's
`0.0112374176597674215641995493744106072696626960812623175786`.

So the *agreement* the closing sentence asserts is **untouched, and in fact
strengthened**: the two independent routes tracked each other through a change
that moved every number in the block. Only the identity of λ\* moved, and it
moved in both routes together.

**This retracts reason 2 of "Why this is not being edited unilaterally" above.**
I wrote that rewriting `+22.452 %` to `−31.659 %` "is a judgement about what the
block should now say". For λ\* it is not a judgement — two independent routes
agree it is `(12)`. What remains genuinely interpretive is one sentence's worth
of qualitative wording, no more.

### 4. A structural check that SURVIVES, and is worth keeping

`(12)`'s character is **unchanged**: `+2.4198` before, `+2.41984` after, and
`c_(12) = +9.5965e-3` in both. The trivial representation sends every generator
to `q`, so **no reordering of the braid word can move it** — likewise the sign
representation `(1¹²)`, still 0. Its share rose 5.962 % → 85.398 % purely
because the total shrank by the ⁴He factor 14.3248, not because it moved.

That is an independent confirmation the regeneration did what it should: only
the genuinely order-sensitive characters moved. It is also *why* the top block
changed — `(12)` did not rise, everything else fell past it.

### 5. Blast radius of the λ\* claim: one file

`grep` over `content/` and `docs/` for a top-block claim naming `(9,3)` returns
**one line** — `he4-two-row-dominance.md:41`, the sentence quoted above. The
incomplete four-row figures from my note above did not propagate: the only
`.beans` hit is this bean.

### Remaining figures for the edit

- trace `0.160974145442` → `0.011237417659767421564199549374410607269662696081262`
- top-five cumulative `91.130 %` → `88.715 %`
- `(12)` "contributes 5.962 %" → `85.398 %`
- stratum ratio **exactly 1**, nonzero blocks **7 of 77** — both unchanged


## APPLIED 2026-09-06 — and the block was stale in FOUR places, not one

The `.md` table was the visible defect. Editing it surfaced three more, two of
which predate this regeneration entirely.

### 1. The `.md` — numbers, and one sentence I got wrong first

Table replaced with all seven blocks, generated programmatically from the
regenerated cache rather than transcribed. Trace `0.160974145442` →
`0.011237417660`; summary sentence now names both sign flips and reports the
cancellation as `+172.549 %` positive against `−72.549 %` negative.

**I first wrote `\lambda^* = (12)` into the paper and that was an over-reach.**
I called the substitution "mechanical, corroborated by two routes". It is
corroborated *arithmetically* and is not mechanical, because it silently
redefines what "dominant block" means. Measured before the edit was finished:
the trivial representation leads in **six of the eight atoms** in
`delta-lambda-empirical-tabulation.witness.json` — p, n, ²H, ³H, ³He, ⁴He —
**and those six are exactly the ones whose chi caches were regenerated.** ⁵Li
and ⁶Li, not regenerated, still lead with `[12,3]` and `[14,4]`. A "fingerprint"
that six atoms share is not a fingerprint.

The block now states the ranking, says the trivial rep leads because its
character cannot move under a reordering while everything else fell past it,
and identifies `(9,3)` as the leading **non-trivial** block — which both routes
agree on and which is the reading under which the magic-shell interpretation
has content.

### 2. The `.ts` was TWO generations stale, including the TITLE

Independent of this regeneration, and reader-visible:

- **title:** `"… at $q_0$ (86.6\% empirically)"` — contradicted by the block's
  own 2026-08-23 `authorNote`, which records the ratio as **exactly 1**. A
  reader saw `86.6 %` in the rendered proposition heading against `exactly 1`
  three lines into the body. Now `(exactly $1$ empirically)`.
- **docstring:** carried `0.05534835` and the pre-2026-08-23 table.
- **§3b-cond paragraph:** "the instance encodes the witness-verified 86.6 %
  figure" — the instance's `ratio := 866/1000` is documentary; the class axioms
  are the structural bounds `4/5 ≤ ratio ≤ 1`.

All three fixed, with the superseded figures kept and **dated** so a reader
meeting them elsewhere can place them.

### 3. The producer's cross-check was RED, and that is what caught the rest

`scripts/check-sidecars.sh` reported `computation.status: verified` against a
cited witness with `allPassed: false` — failing on `tr_M_at_q0`,
`top5_cumulative_pct`, `trivial_rep_pct`, `pct_block_9_3`, `pct_block_8_4`,
`pct_block_10_2` and three more. `probe_he4_canonical_tr_m_fingerprint.py`
asserts the block's prose by design (2026-08-23 note: *"these constants track
the block, so the cross-check stays live for future drift"*), and it worked —
this is that mechanism firing.

`CITED_PCT` and `CITED_TR_M` updated; all seven blocks listed, not six.
**14 assertions, all passed.**

### 4. A definitional divergence the old data hid

The producer computes every percentage as `abs(c_λ)/|tr_M|` and its top-5
cumulative as a sum of **magnitudes**. The block's table rows are **signed**.
While every block was positive the two were the same number — `91.130` — and
nothing named the difference. They now differ by a factor of 2.6:

| | value |
|---|---|
| sum of `\|c_λ\|` over the top five | **233.814 %** |
| sum of the table's five rows | **88.715 %** |

Fixed by emitting **both**, under distinct names, each with its own cited
constant and a `source` string saying which is which. The existing field
`top5_cumulative_pct` keeps its existing meaning so no consumer changes
underneath; `top5_signed_cumulative_pct` is new. The per-block assertions now
compare against the **signed** share — `abs` there would have passed a sign flip
silently, and two blocks had just flipped.

Also de-hardcoded two `[cited …]` literals in the producer's own print
statements, which is the same staleness class this bean is about.

### Verification run

- render-QA grep battery on the `.md`: **9/9**, twice (before and after the
  λ\* revision).
- `run-validate folio/quantum-observable-universe`: **✓ Valid — 4 issue(s)**,
  all pre-existing and none in this block. Platform **`8475c83`**, which is
  **not** the pin `428ca5c` — stating it per the pin discipline.
- `qa-sweep` on the block: **92 pass / 19 n/a / 0 fail**, sidecar refreshed.
- producer re-run: **14/14**.
- raw-float64 ratchet: **0 new**; this witness went 90 → **89** raw floats
  (the two fields I added serialize through `mp.nstr`, not `float()`). The 4
  files the ratchet reports as regressed are untouched by this change — they
  were regenerated in the earlier post-regeneration sweep.

### Left deliberately, and it is the author's call

`he4-two-row-dominance.lean` carries `dominant_partition := [9, 3]` and
`dominant_eq : dominant_partition = [9, 3]` — the latter **in the class
signature**, not the instance. That is correct under the *leading non-trivial
block* reading and wrong under *largest `|c_λ|`*. **Nothing depends on which:**
every downstream theorem derives from `4/5 ≤ ratio ≤ 1`, and `IsTwoRow` is
`length ≤ 2`, so `[12]` is in `Λ²(12)` and `by decide` discharges either way.
The instance's `ratio := 866/1000` is likewise documentary and two generations
stale. Recorded in the block's `authorNotes` with the exact edit required if
the author wants `[12]`; not changed here, because choosing is a judgement
about what the class means, not a transcription.



## Q2 RESOLVED 2026-09-07 — owner picked BOTH, so the class now carries both

The two options were mutually exclusive for one field, so "both" reads as:
**make the distinction explicit rather than choose.** That is the better
answer, and it is what the conflation had been hiding.

`HasHe4DominantBlock` now has:

- `dominant_partition := [9, 3]` — **unchanged**, redocumented as the leading
  **non-trivial** block, the quantity the magic-shell reading refers to.
- `largest_partition := [12]` — new, the largest `|c_λ|` **overall**, with its
  own `largest_is_two_row` and `largest_sums_to_12`.
- `leading_ne_largest : dominant_partition ≠ largest_partition` — the field
  that **asserts** the distinction rather than merely recording two values.

Two derived results give the new fields consequence instead of leaving them
inert: `largest_in_two_row_stratum` (the trivial rep is a ONE-row partition and
`IsTwoRow` is `length ≤ 2`, which is why the stratum ratio is exactly 1 with it
included) and `dominant_ne_trivial_rep`, proved from `leading_ne_largest` and
`largest_eq` so it holds for any instance rather than being read off this one.

**Why both, in one sentence:** before the 2026-09-05 ruling the two notions
picked out the same block, so one field expressed both and nothing recorded
which was meant — the conflation only became visible when the data moved.

### Verification

`lean`-direct with `-DautoImplicit=false -s 65536` against the restored
v4.24.0 cache: **exit 0** (1m50s cold on the unmodified file as a baseline,
3.4s warm after the edit). `#print axioms` on `dominant_ne_trivial_rep`,
`largest_in_two_row_stratum` and `dominant_eq_nine_three_in_stratum` reports
**`[propext]`** on all three — no `sorryAx`, no `Classical.choice`. The single
`sorry` the grep finds is in a docstring. `qa-sweep`: **92 pass / 19 n/a / 0
fail**.

`dominant_partition` is unchanged, so every existing downstream theorem —
`dominant_in_two_row_stratum`, `dominant_eq_nine_three_in_stratum` — is
untouched.

- **Round 55 Progress (`2026-11-16T21:09:27Z`)**: Opened [`litlfred/qou#8202`](https://github.com/litlfred/qou/pull/8202) (`61d4706edbc97c195108082e38b072c982ba2984`, Commit 1 `842a8da69cdb997861cc48f6f16593cc33e1e707`). Keeping bean at `status: in-progress` pending owner review.
