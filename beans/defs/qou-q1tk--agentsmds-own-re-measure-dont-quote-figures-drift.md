---
# qou-q1tk
title: 'AGENTS.md''s own re-measure-don''t-quote figures drift: 3 instances measured in one session, 12 of 13 numbers stale'
status: todo
type: task
priority: normal
created_at: 2026-09-27T10:52:15Z
updated_at: 2026-09-27T10:55:47Z
---

## The pattern, measured 2026-09-27

AGENTS.md carries several figures with an explicit instruction attached —
*"re-count, do not quote"*, *"measure, do not quote"*, *"measured, not
maintained"*, *"Re-count the table; do not trust this sentence"*. I ran three of
those instructions in one session. **12 of the 13 numbers were stale.**

### 1. Detector-blindness taxonomy row count — `qou-8dzi`, landed `5a6afef6f3`

| | |
|---|---|
| said | forty-**six** |
| measured | **47** rows, ids 1..47, no gaps |
| authority | the artifact self-reports at `2026-08-15-detector-blindness-taxonomy.md:994` |

Row 47 landed as `f75b27e70f` (a sibling's) and the AGENTS.md count did not move
with it. **The SEVENTH staleness of this one line** — its own parenthesis keeps
the tally: thirteen at 15 rows, sixteen at 17, eighteen at 21, twenty-two at 26,
thirty-five at 39, forty-five at 46, forty-six at 47.

### 2. Library / corpus-grep path-5 block — `qou-8l9i`, landed `105f45b017`

**Seven for seven stale**, and one by 2.8×:

    ingested chars    24.7 M   ->  69.0 M sections/ + 1.1 M ocr/
    INDEX.md          ~513 briefs / 527 lines  ->  693 rows / 710 lines
    directories       576      ->  715
    section files     11,528   ->  14,026
    index rows        552      ->  693
    duplicate copies  "23"     ->  21 copies over 20 distinct works
    ocr/ tier         25 of 576 -> 26 of 715

The character count is not decoration: it is the **entire argument** for that
block's cheapest-first tier order (*"do not grep straight into them when a line
will do"*), so understating it 2.8× understates the advice it justifies.

This one also **surfaced a live defect** rather than only a stale number — see
`qou-8l9i` for Neumann–Zagier 1985 being held twice with all three duplicate
guards missing it.

### 3. Package importer counts — landed `c75f4df1fc`

**Four of five stale, the fifth absent**, and this is the **third generation** of
drift on the same row:

    generation 1   1 / 7 / 19 / 15 / 1        ("wrong by up to two orders of magnitude")
    generation 2   5 / 309 / 70 / 89 / —
    measured       7 / 1349 / 203 / 113 / 1

`qou_substrate` 309 → **1349**, i.e. **1322 of the hits are in `computations/`**,
roughly a quarter of the repo's 5492 tracked `.py` files. "309" reads as a
large-but-ordinary dependency; 1349 reads as a substrate.

**The sharpest instance in the three.** The note above that table exists *to warn
that these numbers decay*, and its worked example is *"`qou-substrate` was 7, is
309"*. That example was itself stale by **4.4×** while being quoted as the
cautionary tale. A hand-kept number inside a warning about hand-kept numbers
decays no slower.

### The one figure that was CORRECT

The L1 precision row (`COMPUTE_DPS 70 / OUTPUT_DPS 60 / PRECISION_GUARD 10`),
checked per its own *"Measure, do not quote"* instruction. Left untouched. Worth
recording: the instruction is not evidence the number is wrong, and three-for-four
is the measured hit rate, not four-for-four.

## Decision for the owner — NOT taken

**Should AGENTS.md stop restating counts it tells the reader to re-measure, and
cite the artifact plus its command instead?**

- **What it means.** Replace *"catalogues **forty-seven** rows"* with
  *"catalogues the number of rows its own line 994 reports — count it"*, and the
  importer table's five figures with the command alone. The prose stops carrying
  a value that can go stale.
- **What it costs.** A wording pass over ~4 passages in one heavily-read file.
  No code, no producer, no witness.
- **What it risks.** Legibility. Several of these figures are load-bearing
  *as magnitudes* — "69.0 M characters" is what makes the tier order obviously
  right, and "1349 importers" is what makes `qou_substrate` obviously a
  substrate. A reader who has to run a command to learn the order of magnitude
  may simply not, and the advice loses its force. That is the real trade-off,
  not effort.
- **What it commits to.** Nothing structural; reversible.

**Default if you say nothing:** all three are correct today and go stale again.
The taxonomy line's own tally says the eighth time is coming; the importer row is
on its third generation in what looks like a few months.

**My recommendation, marked as judgement:** a middle option neither of the two
obvious ones — keep the magnitude, drop the precision, and always stamp the date.
*"~70 M characters (2026-09-27; re-measure)"* stays useful for a year and cannot
be quoted as exact; *"715 directories"* cannot. The figures that are genuinely
load-bearing as exact values are few — the taxonomy row count is one, because it
indexes a table — and those are the ones worth citing the artifact for instead.

I am **not** enacting any of it: the 2026-09-07 override names a wording change
to a heavily-read passage as exactly what waits, and the three corrections above
went ahead only because each artifact decides its own number and a reviewer
re-runs one command.

## Method notes worth keeping

- **Check the harness before believing a 4× jump.** The documented importer
  command walks the WORKING TREE (`grep -r … .`), so a venv or build dir would
  inflate it. Measured: it does not here — 5506 `.py` on disk against 5492
  tracked, and the tracked-only form via `git ls-files` returns **exactly the
  same five numbers**. So this count is method-independent, which the library and
  muon-pin counts are **not**.
- **The documented command has a trap.** Its `^./tools/<pkg-dir>/` exclusion is
  what stops a package counting its own files, and two of the five packages are
  not under `tools/` (`qou-mass/`, `schemas/witness-schema/`). Following the
  template literally counts those two packages' internals as importers of
  themselves.
- **State the method with the number** where method matters. The library block
  already learned this the hard way (the muon-pin prefix table) and the lesson
  generalises: a count without its method invites the next reader to "correct"
  it to the answer to a different question.

Left **`todo`**: the three instances are corrected but the decision above is
open, and the pattern will recur until it is taken either way.


## Two more families CHECKED and CURRENT — the rate is family-level 3 of 5, not 12 of 13

The "12 of 13" above is a count of *numbers inside the three families that were
stale*. Quoted alone it overstates the problem, because two further families were
checked in the same session and **both were correct**. Recording them, since an
absence-of-drift result is evidence about the same question.

**L1 precision row — CORRECT.** Its instruction is *"Measure, do not quote:
`python3 -c "import qou_substrate.precision as P; print(P.COMPUTE_DPS,
P.OUTPUT_DPS, P.PRECISION_GUARD)"`"*. Run: `70 60 10`, exactly as written. Left
untouched.

**L2 per-observable dashboard — CORRECT, all nine figures.** Its instruction is
*"Quote the witness, not this paragraph"*. Read
`computations/per-observable-100x-status.witness.json`:

| field / row | witness | AGENTS.md |
|---|---|---|
| `beats_100x_scoreable` | 1 | 1 ✓ |
| `scoreable_total` | 6 | 6 ✓ |
| `beats_100x_count` | 2 | 2 ✓ |
| `m_mu` | 211.2 ppb, target 0.2177, miss **970.2** | 970.2 ✓ |
| `Q_beta` | **1.668e+8** ppb, miss **2.139e+7** | 1.668e+8 / 2.139e+7 ✓ |
| `m_n` | 1.389e+5 ppb, miss 2.718e+7 | ✓ |
| `Delta_pn` | 1.009e+8 ppb, miss 2.327e+7 | ✓ |
| `alpha_em_inv` | miss 238.3 | 238.3 ✓ |
| `m_K/m_pi` | miss 0.1952 | 0.195 ✓ |

**This is the interesting half of the result.** The L2 block is the most
*consequential* set of figures in the document — they are the physics-facing
accuracy claims, several of them re-scored twice this month under owner rulings —
and it is the one family with **zero** drift. The three that had drifted are all
*infrastructure* counts: a table's row count, a library's file counts, a package's
importer counts.

So the pattern is narrower and more actionable than "AGENTS.md figures go stale".
**A figure whose producer is a witness stays current, because re-running the
producer rewrites it and the doc is told to quote the witness rather than a
value.** A figure whose "producer" is a shell command nobody is obliged to run
goes stale silently. That distinction is what the decision above should turn on,
and it argues for the middle option recorded there rather than for a blanket
rewrite: the L2 block already solves this problem correctly, by pointing at the
artifact instead of restating it.

Family-level rate: **3 stale of 5 checked.** Quote that alongside 12-of-13, or
the document reads as less reliable than it measures.
