---
# qou-iayk
title: 'Habiro regeneration BLOCKED: fresh values break the landed D(u) closed-form law that the old witness satisfies exactly'
status: todo
type: task
priority: normal
created_at: 2026-08-21T16:21:00Z
updated_at: 2026-08-21T16:22:17Z
---

Attempted the qou-ls7l regeneration 2026-08-21. STOPPED and reverted: the fresh values contradict a landed corpus result, and my earlier claim that they were 'current-correct' is RETRACTED.

## What the regeneration does achieve

With the LaurentQ parser fix (PR #5376) plus pointing the producer at its
consumer's directory, it runs 4/4 clean and the L1 gate's Habiro column
moves onto convention D:

  atom      Habiro vs Hoefsmit BEFORE   AFTER
  deuteron  0.3249                      1.514e-07
  tritium   0.5462                      1.966e-07
  helium-3  0.4885                      2.517e-07
  helium-4  0.6562                      2.887e-07

Six orders of magnitude. Methods on D go 2-of-4 -> 3-of-4; only markov_peel
stays on C. That part is real and reproducible.

## Why it is blocked anyway

The corpus carries a landed closed-form law (computations/d_u_closed_form_proof.py,
docs/audits/2026-05-03-w3-habiro-unblocked.md):

  D(u) = 2^(2A+1) * u^(18Z+21N+1) * (1+u^2)^(3A-1)

The OLD witness satisfies it EXACTLY on every atom. The FRESH one satisfies
neither half:

  atom      law pref   old   new   new/law    law exp   old   new
  D             32     32    192      6         40      40    46
  T            128    128    768      6         61      61    66
  3He          128    128    768      6         58      58    58
  4He          512    512   3072      6         79      79    78

Prefactor is uniformly 6x -- structured, consistent with a normalisation
change. But the EXPONENTS are off by +6, +5, 0, -1. An irregular offset is
NOT explainable by a normalisation, and one atom (3He) matches exactly while
its A=3 partner (T) is off by 5.

## What I got wrong

In PR #5376 I argued from two landed commits (5564402795 canonical symbol,
6357615e11 denesting) that the committed witness is pre-fix stale, and
concluded 'the fresh values are the current-correct ones'. The first half
stands -- the witness DOES carry check_q strings under _in_u field names,
which is exactly the qou-0ndb defect. The conclusion does not follow from
it. Explaining WHY two witnesses differ is not evidence that the newer one
is RIGHT, and I over-read it as though it were.

The old data fitting a clean closed form 4-for-4 on both prefactor and
exponent, while the new data fits neither, is evidence in the opposite
direction and it is stronger than my convention argument.

## Two readings, and I cannot adjudicate

(a) The producer has a defect BEYOND the parser. It was totally broken until
    #5376, so nobody has validated its output in over a month; its own
    reconstruction check passing shows internal consistency, not correctness.
(b) A deeper convention change invalidates the law too, and the law needs
    re-deriving in the new frame.

Deciding needs the Habiro maths. Guessing is how a fix becomes a fit.

## State

Nothing landed. Witness, producer path change, and d-u-closed-form witness
all reverted. #5376 (the parser fix) is unaffected and still correct -- it is
a strict widening with 7 tests, and the blocking evidence here concerns the
VALUES the now-runnable producer emits, not the parser.

For whoever takes it: the reproduction is 'apply #5376, change out_path to
HERE.parent, run'. Compare denom_factored against the law before landing
anything.
