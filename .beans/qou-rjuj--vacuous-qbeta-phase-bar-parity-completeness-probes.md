---
# qou-rjuj
title: 'VACUOUS: qbeta_phase_bar_parity_completeness_probe''s two defect assertions cannot fail'
status: todo
type: task
priority: normal
created_at: 2026-08-30T08:05:06Z
updated_at: 2026-08-30T08:08:28Z
---

## 2026-08-30 — FIXED, and my own framing corrected

**My framing in this bean's title was too strong.** I called the two assertions
'vacuous'. Read against the probe's stated finding they are not a mistake: the
probe's whole conclusion is that the defect is INDEPENDENT of a --

    'Hence for ANY bar-odd a, bar(a - u/2) + (a - u/2) = -u(1+q^2)/2,
     IDENTICAL in C and D -- the defect is convention-independent.'

so assertions that check that identity are checking the claim.

**The real gap was narrower and is what I fixed.** The probe wrote

    bar_phase = -a - (q**2 * u) / 2      # bar(a) = -a for both

i.e. it SUBSTITUTED the assumption from its own comment. That made  cancel
algebraically, so the assertions held whether or not the assumption was true,
and the one hypothesis carrying the content -- that each arm's  really is
bar-odd -- was never tested.

Fix: compute bar(a) = a_of(1/q) per arm and assert bar(a) + a = 0 BEFORE using
it. The assumption was in fact TRUE (C: 5.66e-73, D: 0.0, both under 1e-40), so
the probe's conclusion stands unchanged -- it is now checked rather than
asserted.

**Verified by mutation, not by eye.** Dropping the forced -h^2/4 projection from
the D arm makes it non-bar-odd; the probe then reports 'NOT BAR-ODD' with
bar(a)+a = 0.0218531 and exits ASSERTIONS FAILED. Restored, it passes. So the
new check can fail, which is what distinguishes it from the version it
replaces.
