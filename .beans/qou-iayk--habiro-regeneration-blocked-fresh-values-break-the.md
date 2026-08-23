---
# qou-iayk
title: 'Habiro regeneration BLOCKED: fresh values break the landed D(u) closed-form law that the old witness satisfies exactly'
status: completed
type: task
priority: normal
created_at: 2026-08-21T16:21:00Z
updated_at: 2026-08-23T19:06:58Z
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


## The blocking argument does not survive — 'irregular' is REFUTED (2026-08-23)

Probe: `computations/habiro/du_law_reparametrisation_probe.py` (exact
integer arithmetic, no float). Re-ran the producer to get the fresh values
from PRIMARY data rather than this bean's transcription; tree restored.

    atom   Z N A   OLD (committed)        FRESH (re-run 2026-08-23)
    D      1 1 2   32*u^40*(u^2+1)^5      192*u^46*(u^4+1)^5
    T      1 2 3   128*u^61*(u^2+1)^8     768*u^66*(u^4+1)^8
    3He    2 1 3   128*u^58*(u^2+1)^8     768*u^58*(u^4+1)^8
    4He    2 2 4   512*u^79*(u^2+1)^11    3072*u^78*(u^4+1)^11

This bean blocks on: *"the EXPONENTS are off by +6, +5, 0, -1. An irregular
offset is NOT explainable by a normalisation."* Three facts say otherwise.

**FACT 1 — the strongest, and it is not a fit.** The `(1+u^b)^k` exponent is
`k = 3A-1` in BOTH frames — 5, 8, 8, 11 — on all four atoms, with **zero
free parameters**. Only the BASE moves `u^2 -> u^4`, which is exactly the
signature of the substitution `u -> u^2` in that factor. The bean never
looked at this factor; it compared only the `u^shift` exponent.

**FACT 2.** The prefactor ratio is the constant **6** on all four atoms, and
the old prefactor is exactly `2^(2A+1)`. One parameter, four ratios.

**FACT 3 — and its honest weight.** The offset is **additive** in Z and N:
the 2x2 interaction vanishes exactly, `78 - 58 - 66 + 46 = 0`, giving
`offset = 13 - 6Z - N` and hence `u^(12Z + 20N + 14)`. Same functional
shape as the landed law. **But 4 points against a 3-parameter additive model
tests exactly ONE constraint** — that vanishing interaction. Weak alone;
corroborative alongside facts 1 and 2, which are not fits.

## The epistemic point, and it is decisive

This bean's stated reason to prefer the old data is *"the old data fitting a
clean closed form 4-for-4 ... is evidence in the opposite direction and it is
stronger than my convention argument."*

**`d_u_closed_form_proof.py` says in its own docstring that this law is NOT
a test of witness correctness** — the committed witness satisfies the law
exactly and nonetheless **FAILS the outer identity**
`p(u)/(u^shift*D(u)) == tr_M_atomic(u^2)` on all four atoms (exact rational
evaluation, PR #5418). So "old fits the law 4-for-4" is not evidence that
old is right, and the inference this bean rests on is the one its own
producer warns against.

## VERDICT — re-scope the block, do NOT lift it

'Irregular' is refuted, so the stated reason to block is gone. That removes an
argument AGAINST reading (b); it supplies no argument FOR the fresh values.

**Reading (a) — a producer defect beyond the #5376 parser — is untested here
and remains live.** Nothing above examines the producer's internals, and its
own reconstruction check passing shows internal consistency, not correctness.

So: this is not 'unblocked'. It is blocked for a *different and smaller*
reason than recorded — validate the producer, not the law-fit.


## UNBLOCKED and DONE, 2026-08-23 — the block compared D output against a C law

Owner directed me onto this. The recorded blocker — *fresh values break the
landed D(u) closed-form law* — **does not exist**. The landed law is
**convention C**, and `d_u_closed_form_proof.py` now says so in its own
header (lines 36-45): under D the Markov-Ocneanu argument gives
`(1+u^4)^(3A-1)` instead of `(1+u^2)^(3A-1)`, and the derived exponent
`3A-1 = n_strands - 1` survives the convention change.

Checked against the D-form law, 4/4 exact:

    D(u) = 6*2^(2A+1) . u^(12Z+20N+14) . (1+u^4)^(3A-1)

    atom  Z N A   pref  pred   u-exp pred   (1+u^4) pred
    D     1 1 2    192   192      46   46         5    5
    T     1 2 3    768   768      66   66         8    8
    3He   2 1 3    768   768      58   58         8    8
    4He   2 2 4   3072  3072      78   78        11   11

The fresh values **satisfy** the law. The 2026-08-21 attempt compared them to
its C form and read agreement-failure as corruption.

## The real defect was the OUTPUT PATH, and it is why the 25-atom sweep missed this

`habiro_coefficients_extended.py` wrote `HERE / "..."` — i.e.
`computations/habiro/`. Every consumer that matters reads the
`computations/` root: `cross_check_trM_1ppb` (the L1 gate),
`d_u_closed_form_proof`, `mass_formula_6term_mpfr_50dps`. So **the
producer refreshed a copy nobody reads while the copy everybody reads went
stale.**

That is why commit `cde2fbcd894` (*"regenerate all 25 atoms into convention
D"*) did not move the gate: it wrote the per-isotope files; the string
"extended" appears **zero** times in it, and the top-level witness stayed
convention C (`32*check_q^40*(check_q^2+1)^5` — the `(u^2+1)` of z_C).

Fixed: the producer now writes to the computations root, and the dead
`computations/habiro/` copy (4/4 error records, pre-#5376) is removed so
`witness_path`'s prefer-dir search falls through to the real file. That
removes the resolution hazard `qou-kcii` names and the one that made a
probe report the wrong q0Anchor in `667c9ab3f6`.

## Result — one of the two causes is drained

Regenerated under `QOU_Q0_ANCHOR=ideal` (the gate is muon-canonical and
correctly refused my first proton-pinned run):

    atom       hoef vs habiro   chi vs habiro   peel vs chi (GATE)
    deuteron        0.0            1.482e-7          0.3248
    helium-3        0.0            2.462e-7          0.4884
    helium-4         —             2.887e-7          0.6561
    tritium         0.0            1.908e-7          0.5462

Habiro has moved off the C/peel side (where it sat at 1.82e-4) onto the
D/Hoefsmit side — **exact on three atoms**. Both the convention half and the
pin half of this leg are now correct.

**The gate is still red, correctly.** `peel_vs_chi` is unchanged because
`markov_peel` remains convention C. That is `qou-cds2`'s Gram singularity
and the TL_3 rebuild (`qou-8iru`) — a different cause, untouched by this.
