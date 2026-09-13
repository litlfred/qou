---
# qou-9nn0
title: 'two q-integer outliers: keystone_qhankel_eq2_vacuum_row.py uses (q^n-1)/(sqrt q - 1/sqrt q); qbeta_5two_colored_tower_barodd_qstar_probe.py is symmetric in q^2 — deliberate or defect?'
status: completed
type: task
priority: normal
created_at: 2026-09-07T14:02:19Z
updated_at: 2026-09-13T05:55:51Z
---

RESOLVED 2026-09-13. BOTH 'outliers' were the symmetric bracket written in a square-root variable, and MY OWN AUDIT MISCLASSIFIED BOTH. Verified symbolically at n = 2,3,5,7 (sympy, exact).

OUTLIER 2 -- qbeta_5two_colored_tower_barodd_qstar_probe.py:93-95
  body: (a**(2m) - a**(-2m)) / (a**2 - a**-2)
  This is EXACTLY the symmetric bracket in the variable a^2 (difference 0 at
  every n tested), and with a = sqrt(q) it is EXACTLY the canonical [m]_q
  (difference 0). NOT an outlier, NOT a defect, no change made -- it is the
  standard colored-Jones spelling where a = q^(1/2). My audit reported it as
  'symmetric in q^2', which is the same function under a different name.

OUTLIER 1 -- keystone_qhankel_eq2_vacuum_row.py:66-69  *** REAL DEFECT ***
  My bean said it used (q^n - 1)/(sqrt q - 1/sqrt q). THAT IS WRONG -- measured,
  the difference from that form is nonzero and grows with n. The body is
  (s^n - s^-n)/(s - 1/s) with s = sqrt(q), i.e. the symmetric bracket in sqrt(q):
  [n]_{sqrt q}. Same CONVENTION, different ARGUMENT -- which as a function of q
  is a different function, and that is the distinction my audit collapsed.

  It was nonetheless a genuine defect, decided by the file against itself. Its
  module docstring publishes the target the probe exists to reproduce,
      d_q = ([1],[4],[5],[4][3]/[2]) ~ (1, 4.10968, 5.22044, 6.22044)
  citing PR #3292 FACT 1. Canonical [n]_q reproduces it to 2.4e-6 (that vector's
  own rounding); the old body gave (1, 4.0273, 5.0546, 6.0546), off by 0.166.
  The probe's gate is 1% and the target error was 2.0% on [4] / 3.2% on [5], so
  the committed witness recorded REFUTED-as-is (scope a) against a target the
  file's own docstring does not name. Fixed; verdict re-run and UNCHANGED (still
  REFUTED-as-is, coherent_4vector_match False) -- right answer, wrong reason,
  now right reason.

CONSEQUENCE FOR THE PUBLISHED FIGURE, and I owe this correction:
  reported (PR #7077, audit sec 21, beans qou-c041 / qou-3ul5):
      366 definitions, FOUR distinct symbolic forms --
      126 symmetric / 30 classical / 1 sqrt-normalised / 1 symmetric-in-q^2
  correct:
      366 definitions, TWO conventions --
      128 symmetric / 30 classical / ZERO outliers
  The two 'extra forms' were sqrt-variable spellings of the symmetric bracket.
  This is detector-blindness row 17-21 (the qou-t9r1 family, 'the sqrt-variable
  spelling with the variable equal to sqrt q') hitting my own audit -- the exact
  class my sec-21.3 roast named, one level up: I compared representations
  without substituting the variable's definition.

  The Lean (QOU/Substrate/QIntegerConventions.lean) claims only TWO forms and is
  UNAFFECTED -- it never asserted four.
