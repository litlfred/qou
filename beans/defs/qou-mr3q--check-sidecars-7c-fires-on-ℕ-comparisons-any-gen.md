---
# qou-mr3q
title: 'check-sidecars §7c fires on ℕ comparisons: any generic file with ≤ is flagged archimedean'
status: completed
type: task
priority: normal
created_at: 2026-08-22T19:56:16Z
updated_at: 2026-08-22T20:34:58Z
---

MEASURED 2026-08-22 on
content/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicPerpetualObstructionFromTrace.lean
after adding a generic-ring theorem to it (bean qou-lrnd).

scripts/check-sidecars.sh fires:
  '§7c MIXED generic + archimedean -> split into two files per §7c'

on a file containing NO real number at all. Running the detector's own logic:

  hasR   = 0     no matches for RTYPE — there is no ℝ in the file
  hasGen = 1     from the added {R : ... Type*} / [CommRing (R p)]
  hasJ   = 1     matched on:
                   (h_bound : forall p : Nat.Primes, (p : N) >= N -> ...)
                   have hpN : N <= (p : N) := by

The two JUST matches are comparisons of NATURALS — prime indices against a
bound — in the pre-existing perpetual_obstruction_from_trace. They have
nothing to do with the base ring.

THE RULE the check implements (§7c) is ℝ-versus-generic: use a generic
{R : Type*} unless an archimedean construct (Real.sqrt, ordering ON THE BASE
RING like 0 < q, linarith over ℝ) is genuinely needed. The JUST pattern
approximates 'archimedean construct' with, among others, bare '<=' / '>=' /
'0 <' / '< 1'. Ordering on N or Z is not archimedean-specific, so the
approximation over-fires.

CONSEQUENCE, and why it is worth fixing rather than living with: the flag
fires precisely when a file does the RIGHT thing. hasGen only becomes 1 when
someone writes a generic ring — the thing §7c asks for — so any generic file
that also compares two naturals is flagged. Before the generic theorem was
added, hasGen was 0 and the same ℕ comparisons raised nothing. The check
therefore penalises §7c compliance.

NOT fixed here: the file is left as-is, because the code is §7c-correct
(generic [CommRing], Z, no ℝ) and weakening correct code to silence a
checker is the wrong direction. The fix belongs in the JUST pattern —
require the comparison to involve ℝ, or drop the bare relational operators
and keep the Real.* / linarith / LinearOrdered / CODATA / MeV signals which
do indicate archimedean content.

FIXED 2026-08-22 (this branch). scripts/check-sidecars.sh now splits the
archimedean justification into two strengths:

  STRONG  Real.*, linarith, positivity, nlinarith, LinearOrdered, CODATA, MeV
          — archimedean wherever they appear
  WEAK    0 <, < 1, <=, >=  — counted ONLY alongside RTYPE, because '0 < q'
          is the §7c tell when q : R-real (the §7c table says so) and means
          nothing when there is no real number in the file

  MIXED is now hasGen && (hasR || hasS); base-ring-minimal keeps the
  combined test so its behaviour is unchanged.

Measured over all 2063 library .lean files:

                       before   after
    MIXED                 258     129
    base-ring-minimal     163     163
    total flags           421     292

129 files change verdict and every one has hasR=0 — no real number anywhere.
93 files carrying BOTH a real and a generic ring still report MIXED, so
nothing that deserves the flag lost it.

The obvious fix was measured first and REJECTED: simply deleting the
operators from JUST trades 129 fewer MIXED for 143 MORE base-ring-minimal,
because those files have their real justified only by a bare '0 <'. Net
flags would have gone 421 -> 435 — worse. Keeping the operators as a WEAK
signal is exactly what leaves that second branch untouched.
