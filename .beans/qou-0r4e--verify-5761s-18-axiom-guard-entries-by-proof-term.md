---
# qou-0r4e
title: 'Verify #5761''s 18 axiom-guard entries by proof term — build the 30-module cone'
status: completed
type: task
priority: normal
created_at: 2026-08-25T19:03:35Z
updated_at: 2026-08-25T19:19:43Z
---

## RESULT 2026-08-25 — all 27 entries verified clean; one real guard bug found

**Verdict: main's #5761 entries were accurate.** One batch run over exactly
those entries (`--registry`, so `missing` detection is live): **27/27 `clean`,
rc=0, zero regressions, zero promotions.** Build cost was 30 modules / 260 s,
all exit 0 — far cheaper than the "16 further modules" I had guessed.

**Two of my own figures were wrong:**
- "16 further modules" — it is 33 in the cone, 30 needing a build, and #5761
  added FIVE module groups (Rivin, KummerRadial, IdealTriangulation,
  HyperrealLimitTransfer, FiveTwoComplexPentagon), not just IdealTriangulation.
- "8/11 registry modules verifiable" — wrong, that counted only ABSENT oleans.
  With staleness it is **6/11**; the backlog is 70 builds (21 absent + 49
  present-but-stale), not 21.

## The real find: a primed declaration was UNVERIFIABLE by this gate

`#print axioms` wraps names in single quotes and does not escape a prime, so
`tendstoReal_le_of_eventuallyLE'` prints with TWO closing quotes:

    'QOU...tendstoReal_le_of_eventuallyLE'' depends on axioms: [...]

The parser's `'([^']+)'` stopped at the prime and matched nothing. That
declaration could not be verified at all — the one thing a sorryAx gate must
never do. It also fails *quietly* on a single-entry filter: `found` is empty
and the exit-2 "no output parsed" path reads as an environment problem rather
than a declaration the gate cannot see. (In a mixed batch `missing` would have
caught it, so the blast radius was narrow — but nonzero.)

Fixed by confining the name to one line (`^'([^\n]+)'`, `re.M`) so it
backtracks to the quote actually followed by " depends on axioms:". Added
`--selftest` over five output shapes; **verified it FAILS on the old regex**,
so it is a regression test rather than a tautology.
