---
# qou-mr3q
title: 'check-sidecars §7c fires on ℕ comparisons: any generic file with ≤ is flagged archimedean'
status: todo
type: task
priority: normal
created_at: 2026-08-22T19:56:16Z
updated_at: 2026-08-22T19:56:36Z
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
