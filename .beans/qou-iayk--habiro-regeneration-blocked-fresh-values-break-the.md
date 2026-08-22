---
# qou-iayk
title: 'Habiro regeneration BLOCKED: fresh values break the landed D(u) closed-form law that the old witness satisfies exactly'
status: todo
type: task
priority: normal
created_at: 2026-08-21T16:21:00Z
updated_at: 2026-08-21T16:59:55Z
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


---

## 2026-08-21 — BLOCK LIFTED. The two witnesses are two CONVENTIONS.

Adjudicated by `computations/habiro/habiro_witness_convention_adjudication_probe.py`
(6/6, symbolic-exact, witness `habiro-witness-convention-adjudication.witness.json`).
My block above was wrong. Two measurements overturn it.

**1. The committed witness does not describe tr_M.** Its own
`reconstruction_matches: true` checks only the INNER identity
`p(u) == reconstruct(a_m)`. It never checks the OUTER one,

    p(u) / (u^shift * D(u))  ==  tr_M_atomic(Z,N)|_{q -> u^2}

which is the only thing making the file a statement about the Markov trace.
Checked by exact rational evaluation (no float): the committed witness FAILS
it on all four atoms; the fresh values SATISFY it on all four.

So "the committed witness satisfies the D(u) law" was never evidence it is
correct. It is a self-consistent object that does not represent today's tr_M.

**2. The disagreement is exactly C-vs-D.** The Markov-Ocneanu prefactor
contributes the denominator of z raised to `3A-1`:

    committed : (u^2+1)^(3A-1) = (1+q)^(3A-1)    <- z_C = q^(1/2)/(q+1)
    fresh     : (u^4+1)^(3A-1) = (1+q^2)^(3A-1)  <- z_D = q^3/(q^2+1)

Both carry the DERIVED exponent 3A-1 exactly; only the BASE moves. The
committed witness is dated 2026-07-18; `pyhecke/gram.py:15` records
"TRACE CONVENTION D (z = q^3/(q^2+1)) since 2026-08-15". The committed file
is a convention-C object; the fresh values are convention D. That is also why
regenerating moves the L1 gate's Habiro column onto D (~0.5 -> ~2e-7 vs
Hoefsmit).

**Why the D(u) law is not a counter-argument.** It is C-frame itself --
`(1+u^2)` IS the z_C denominator -- and its exponent is FITTED. The module
says verbatim that `u^shift` is "the only piece this script does NOT close",
and its `EMPIRICAL_D_U` table is by its own comment "extracted from
habiro-coefficients-extended.witness.json" -- the disputed file.
`18Z+21N+1` reproduces that table on all six atoms because it was fitted to
it. So my "old matches the law exactly 4-for-4" was CIRCULAR on the exponent,
and non-discriminating on the cyclotomic exponent (both frames carry 3A-1).

**What I got wrong, precisely.** I treated "fresh breaks a landed law" as
evidence of corruption without asking whether the law was derived or fitted,
or which convention it belonged to. It restates "the fresh values are not
convention C" -- which, after the 2026-08-15 ruling, is the expected and
desired outcome.

## Open residual (NOT a blocker)

Fresh prefactor is a uniform 6x the C-frame one on all four atoms
(192/32, 768/128, 768/128, 3072/512). Uniform-in-A rules out a per-strand or
per-crossing factor, and 6 = 2*3 cannot come from the averaged-crossing
(sigma+sigma^-1)/2 mechanism that produces 2^(2A+1), since 3 is not a power
of 2. Unexplained. It is a question about the D-frame normalisation, and it
is not a reason to retain a witness that fails its own outer identity.

## Next

The regeneration is unblocked as a C->D migration. It still changes a physics
gate's input, so it wants its own reviewed PR with before/after tabulated --
not a drive-by here. The D(u) closed form wants a convention-C SCOPE label
(correct for C; scope it, do not "fix" it).
