# Which committed witnesses are exposed to the two landed precision fixes

Owner-selected 2026-11-20 (option 1 of four). Bean `qou-oiz3`. **Read-only: no
producer was run and no witness was written.**

## 0. Why this was asked

`docs/audits/2026-09-12-uic-float64-excision.md` S3 recorded that
`q_hook_product` / `q_factorial` / `wedderburn_weight` were left `mpf`-typed and
float64-**valued**, worst relative **1.0212424e-15** against **2.4946976e-16**
removed -- *"the residual is 4x what was removed"* -- and deferred the root fix
to the owner on a quoted blast radius of **124 Python files / 243 committed
witnesses**.

Both halves of that deferral have since been overtaken:

- **The residual is closed.** The root `q_int` fix landed (`83ede53aad7`) and the
  same arc gave each primitive an explicit precision context with a floor
  (`_DPS_FLOOR = 50`, `mp.workdps(d + 10)`, return rounded to `d`). Measured on
  `main` over **125 quantities** (every partition of n = 3, 6, 9, 12 plus the
  four `q_factorial`), as self-consistency across ambient precision -- which
  needs no reference `q` and so cannot be contaminated by the input question:

      worst | f(ambient dps 15) - f(ambient dps 120) | / f(ambient 120)
          = 1.1575853e-51   at lambda = (5,3,2,2), n = 12

  Had the `mp.mpf("1.0")` ambient trap still been live this would sit near
  1e-16. **It bounds the arithmetic, not the absolute accuracy against the true
  `q`** -- that is the separate, still-open input ceiling (S3a).

- **`_DPS_DEFAULT` is 70**, not 50 (`14a9e822427`).

So the live question is not whether to fix the cone but which recorded witnesses
still carry pre-fix values. That is what this audit measures.

## 1. The predicate, and the two ways I got it wrong first

[`computations/audits/exposed_witness_identification.py`](../../computations/audits/exposed_witness_identification.py).
A witness is a **refresh candidate** when BOTH hold:

1. its producer **calls** a fixed surface -- `q_int(`, or one of
   `q_hook_product` / `wedderburn_weight` / `q_factorial` / `q_dimension`;
2. the witness publishes a number with **> 50 significant digits**, so the
   change is visible at the precision actually recorded.

A third family, **C**, is measured alongside for the *pending* input ceiling: a
producer that builds `q` with `mpf(Q_50_DIGIT_STR)` caps itself at 50
significant digits while `OUTPUT_DPS` is 60.

Condition 2 is load-bearing and is usually left out: a producer can sit squarely
on the fixed surface and publish nothing finer than the fix, in which case a
refresh produces a **no-op diff**. 33 witnesses are in exactly that state.

**First attempt over-matched 6x** -- 1519 candidates against the audit's ~243 --
because its one-hop rule flagged any producer importing `q_parameter`, which
*defines* `q_int`. That measures exposure to the **module**, not to the **fix**:
2463 of 4773 producers, 52 %. Direct calls only.

**Second attempt failed its own calibration, and that was the check working.**
The band was set from the audit's "124 files", which is a **whole-repo** figure.
Split by tree, 132 files reference the trio: 23 `fsh-guts/deprecated` + 10
`docs/audits` (prose) + **99 live code** (90 `computations`, 6 `tools`, 3
`qou-mass`). This scan excludes the `qou-mass` generated mirror and
`tools/sage-examples`, so it must read exactly **99 - 4 = 95**. It does. The
band is replaced by that **derived identity**, asserted -- the run exits 2 and
prints nothing if it misses, because an audit that self-certifies its
calibration cannot discover its own blind spot (taxonomy row 45).

## 2. Result

Measured on `main` `549b39a643c`, 3625 tracked
`computations/**.witness.json`, 4773 scanned `.py`.

| surface | producers | witnesses > 50 digits | witnesses coarse |
|---|---:|---:|---:|
| A -- wedderburn trio / `q_dimension` | 77 | -- | -- |
| B -- `q_int(` | 142 | -- | -- |
| **A u B (the landed fixes)** | **182** | **88** | **33** |
| C -- `mpf(Q_50_DIGIT_STR)` (input ceiling) | 811 | **461** | 134 |

The 88 and the 461 are **disjoint by construction**: C counts only witnesses
whose producer is not already in A u B. Counted without that exclusion, C is
498, so the two surfaces overlap on 37. 86 distinct producers sit behind the 88;
486 behind C.

| witness disposition | count |
|---|---:|
| producer not on any exposed surface | 2798 |
| **no producer recorded at all** | **434** |
| producer recorded but not tracked | 8 |
| exposed to the landed fixes, > 50 digits | 88 |
| exposed, coarse (refresh is a no-op diff) | 33 |
| input-ceiling surface only, > 50 digits | 461 |

## 3. What this changes for the other three options

- **The refresh is 88 witnesses, not 243.** The older figure was a different
  predicate at a different scope two months ago, before the fixes landed.
- **The input ceiling is the larger population by 5x** (461 against 88), so
  refreshing before closing it means refreshing part of that 461 twice. Close
  the ceiling first.
- **The ceiling costs 486 producers, not two files.** It was put to the owner as
  "`constants.py` + `wedderburn.py` plus the consumers that serialize at 60";
  that estimate was wrong and is corrected here. 809 producers call
  `mpf(Q_50_DIGIT_STR)`; 486 of them back a witness fine enough for it to show.
- **434 witnesses (12 %) carry no producer**, so no triage of this shape can
  reach them. They are neither cleared nor implicated here; `scriptFile` would
  have to be backfilled at the producer first.

## 3a. Two blind spots in THIS audit, found by running it

Both were in the detector, not the corpus, and both are fixed in the committed
version. They are recorded because the audit's own numbers would otherwise read
as corpus facts.

**Family C was measuring the wrong thing.** It began as
`\b[A-Z][A-Z0-9_]*_MP\b` -- "references an `_MP` constant" -- on the belief that
the `_MP` family was truncated at 50. It is not: `Q_MP = q_at(_DPS_DEFAULT)`
with `_DPS_DEFAULT = 70` since `14a9e822427`, and the other ten derive from it
inside `workdps(70)`. So referencing an `_MP` constant is the FULL-precision
path, not a ceiling. Worse, that regex cannot match `Q_50_DIGIT_STR`, which does
not end in `_MP`, so the one real ceiling channel was invisible to it. Family C
now keys on `mpf(Q_50_DIGIT_STR)`, and its count moved 401 -> 811 producers,
264 -> 461 witnesses.

**The auditor counted itself.** The moment this file became tracked, the derived
calibration read 96 against 95 and the run refused to print verdicts: the script
names every family-A function in its own `A_FUNCS` tuple, so it classified
itself as a producer on the fixed surface. An auditor is not a producer; it is
now excluded by path. Neither blind spot would have been visible by reading the
script -- the calibration assertion is what surfaced the second, and using the
script on the real question is what surfaced the first.

Also bounded, not fixed: `_DPS_FLOOR = 50` in `pyhecke/wedderburn.py` is a
**floor, not a cap** -- `_wdps()` returns `max(mp.mp.dps, 50)`, raising
precision when ambient is low and never lowering it, which is why the S1 ambient
sweep is flat at 1.158e-51 across dps 15/50/70/100. It is not part of the
ceiling and no change to it is needed.

## 4. What is NOT established

- That all 88 **move**. The predicate is static; it says the fix is in their
  call path and their recorded precision is fine enough to show it. The measured
  mover rate on an earlier 9-producer sample was 8 of 9, but that sample was on
  the `*_MP` surface, not this one, and is not transferable.
- Anything about the 434 provenance-less witnesses.
- Any absolute-accuracy claim. S1's 1.158e-51 bounds the arithmetic against
  itself; the input ceiling (`Q_50_DIGIT_STR` ~50 significant digits,
  `pyhecke.wedderburn._DPS_FLOOR = 50`, against `OUTPUT_DPS = 60`) is untouched
  and is option 3.
