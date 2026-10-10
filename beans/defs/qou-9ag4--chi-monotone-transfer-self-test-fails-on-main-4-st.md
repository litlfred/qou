---
# qou-9ag4
title: 'chi_monotone_transfer._self_test fails on main: 4 strict_averaged oracle witnesses are pre-convention artifacts'
status: completed
type: bug
priority: normal
created_at: 2026-08-22T20:44:16Z
updated_at: 2026-08-22T21:14:07Z
---

## What

`computations/chi_monotone_transfer.py::_self_test()` **exits 1 on `main`**,
and has nothing to do with any branch — verified by running it on a clean
`origin/main` checkout and getting byte-identical numbers.

    transfer = char_fast (color-weighted, n=6): max_rel=3.561e-15   OK
    transfer = oracle (strict_averaged) D    n=6   max_rel=0.0002625  MISMATCH
    transfer = oracle (strict_averaged) T    n=9   max_rel=0.0005482  MISMATCH
    transfer = oracle (strict_averaged) 3He  n=9   max_rel=0.0005281  MISMATCH
    transfer = oracle (strict_averaged) 4He  n=12  max_rel=0.001883   MISMATCH

## Reading it

Check (1) — the transfer matrix against `char_fast` on the CANONICAL
colour-weighted word — **passes at 3.6e-15**. So the transfer implementation
is fine and the canonical path agrees with itself.

Check (2) compares against four cached oracle witnesses
(`chi-deuteron-h6-at-q0-50dps`, `chi-tritium-h9-...`, `chi-helium-3-h9-...`,
and the ⁴He one). The script's own comment says those witnesses "used the
**strict_averaged** pn convention", and it deliberately compares on the
matching word for that reason.

The residuals are 2.6e-4 .. 1.9e-3 and grow with A — that is the
**colour-weighting** scale (the p-n interface differs by 7.19e-05 in `d`,
compounding per interface), not a precision scale. So the most likely reading
is that the oracle witnesses are pre-colour-weighted / pre-convention-D
artifacts and the comparison word no longer reproduces them.

**Stated as the likely reading, not established.** I have not confirmed which
convention each oracle was actually built under, nor whether the intended fix
is to regenerate the oracles, re-point the comparison, or drop check (2). That
triage is the work.

## Why it matters

A self-test that fails on `main` is worse than no self-test: it trains readers
to ignore it, and it cannot signal a real regression because it is already
red. It is also NOT wired into `precision-gates.sh`, so nothing surfaces it —
I only hit it by running the consumer set as a regression check for an
unrelated `char_fast` change.

## Next honest step

Determine what convention each of the four oracle witnesses was built under
(their `computedAt` / `commitSha` against the convention-D and
colour-weighting landings), then either regenerate them, re-point check (2)
at the canonical word, or delete the check with a note. Do not "fix" it by
widening the 1e-12 tolerance — the gap is 8 orders above it and is structural,
not numerical.


---

## RESOLVED (2026-08-22, PR #5493) — and the reading above is INVERTED

The hypothesis recorded above — "the oracle witnesses are pre-colour-weighted
artifacts" — is **wrong**. It was flagged as *likely, not established*, and
testing it reversed the conclusion.

Recomputed each oracle under BOTH conventions:

| atom | `strict_averaged` | `bring_color_weighted` |
|---|---|---|
| D (n=6) | 2.625e-04 | **5.743e-50** |
| T (n=9) | 5.482e-04 | **8.257e-50** |
| 3He (n=9) | 5.281e-04 | **7.487e-50** |
| 4He (n=12) | 1.883e-03 | **4.079e-49** |

The oracles reproduce **exactly**, to the full 50-dps working precision, under
the canonical colour-weighted convention. **The cached witnesses were always
canonical.** The stale thing was the SELF-TEST: it hardcoded
`pn_convention="strict_averaged"` for the comparison word, and its comment
asserted the witnesses used that convention.

Fix: the comparison word moves to `bring_color_weighted`, and the printed
label is corrected (it announced `(strict_averaged)` on every line, which is
what made the stale convention read as deliberate). All five checks now pass,
exit 0.

## Why the wrong reading was attractive

Worth recording, because the same shape will recur:

1. **The witnesses record no convention field and no `scriptFile`.** There was
   nothing to check the comment against — the claim could only be tested by
   recomputation, not by reading.
2. **Their `computedAt` is 2026-08-10**, five days before the 2026-08-15
   convention-D / colour-weighting ruling. "Predates the ruling" is suggestive
   and is NOT evidence of which convention the producer used; the code can
   lead the ruling. I nearly let that date do the work of a measurement.
3. **The residuals grow with A** (2.6e-4 at A=2 → 1.9e-3 at A=4) because the
   p-n interface `d` differs by 7.19e-05 and compounds per interface. That
   identifies the mismatch as *structural at the colour-weighting scale* — but
   it says nothing about WHICH SIDE is on the wrong convention, which is
   precisely the step I guessed instead of measuring.

The general lesson: when a consumer and a cached artifact disagree, the
artifact is not automatically the stale one. Test both sides against the
current canonical form before assigning blame — it is two runs.
