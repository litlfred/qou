---
# qou-2cof
title: markov-trace proof block was convention C at the muon pin while its statement was D at proton — 15% disagreement
status: todo
type: task
created_at: 2026-08-26T04:46:54Z
updated_at: 2026-08-26T04:46:54Z
---

## What it is

`markov-trace-axiomatic-closed-form-proof.md` — the proof block for
`prop:markov-trace-axiomatic-closed-form` — carried a numerical witness
computed under **convention C** (`z = sqrt(q)/(q+1)`) at the **muon** pin,
while the statement block it proves had already been migrated to
**convention D** (`z = q^3/(q^2+1)`) at the **proton** pin.

    statement block   tr_M(σ₁⁷σ₂⁴)(q₀) ≈ 1.88432    ρ_p^CODATA ≈ 974.44
    proof block       tr_M(σ₁⁷σ₂⁴)(q₀) ≈ 1.63315357 ρ_p^CODATA ≈ 1124.3

A 15 % disagreement between a theorem and its own proof, both live in
`content/` on `main`.

## Why the cause is the convention and not a stale evaluation

The block's **own Step-4 closed form** reproduces both numbers exactly.
Evaluating `a₇a₄z² + (a₇b₄ + b₇a₄)z + b₇b₄` with the block's own
recurrence at the proton pin:

    z_C = 0.499320334184  ->  1.63315337745
    z_D = 0.612688037146  ->  1.88431946725

So the two numbers are not two evaluations of one quantity at different
precisions — they are one formula under two different `z`. The pin is
identifiable too: convention C at the **muon** pin gives 1.6331535653,
matching the proof's `1.63315357…` to 8 digits, where convention C at the
proton pin gives 1.6331533774. Both migrations — 2026-08-09 (D) and the
proton re-pin — were applied to the statement and not to the proof.

## How it surfaced

Not by a convention scan. `computations/audits/braid_encoding_audit.py`
crashed on `mpf.__format__` and could not run at all; once fixed, its
`phase_1_6_closed_form` field (read from
`option-b-proton-mass-full-chain.witness.json`, regenerated 2026-08-24)
moved 1.6331535640 -> 1.8843194673, and the same file carried a hardcoded
`axiomatic_content_block: 1.63315` citing the content block by name.

This is the general point worth keeping: **a crashing producer cannot
report drift.** Its committed witness keeps looking authoritative while
the code under it changes. Every one of the CRASH bucket in `qou-wlaf`
is a witness whose staleness is unmeasurable until the crash is fixed —
they are not neutral exclusions from that denominator.

## Fixed here

- proof block's numerical witness migrated to D-at-proton (`1.884319467…`,
  `974.44`), cross-checked against the production witness
  `option-b-proton-mass-full-chain.witness.json`
  (`tr_M_at_q0.proton = 1.884319467254976`) — agrees to 12 digits.
- the superseded `char_fast ≈ 1.6334` / "matches to 4 significant digits" /
  "reflects floating-point roundoff" paragraph removed: it compared two
  convention-C evaluations, so its agreement claim was about C, and the
  statement already records the seminormal route's agreement under D.
- provenance recorded in the `.ts` `authorNotes` rather than in prose (§4d).
- `braid_encoding_audit.py`'s hardcoded `1.63315` -> `1.88432`.

## Not done

No scan for further C-frame survivors in `content/` proof blocks. The one
here was found incidentally; AGENTS.md's R1 already directs that the
remaining C surface be treated as **unmeasured**, and this is one more
data point for that, not a measurement of it. A targeted sweep would be:
for each migrated statement block, check whether its proof sibling's
numbers still evaluate under C.
