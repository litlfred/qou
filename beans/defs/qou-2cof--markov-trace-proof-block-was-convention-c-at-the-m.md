---
# qou-2cof
title: markov-trace proof block was convention C at the muon pin while its statement was D at proton — 15% disagreement
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T04:46:54Z
updated_at: 2026-10-10T10:30:37Z
parent: qou-d8c7
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


## 2026-10-10 — reparented to the mass-endomorphism epic

This bean is carrier M6 of epic `qou-d8c7` (issue litlfred/qou#7547). Parent moved from `qou-cdx1` to `qou-d8c7`; nothing in the body above was changed by the move.



## 2026-10-10 — measured: 21 live survivors (6 in the D-statement/C-sibling pattern, 15 in unmarked blocks), ~38 deliberate, 4 undetermined groups

Read-only scan of all 3635 content .md blocks, values recomputed under C and D in mpmath at the proton pin (calculator calibrated against this bean's 1.63315 / 1.88432). Full table and blind spots: /mnt/project-files/mass-endomorphism/m6-convention-c-count.md (issue #7558). Notable: `markov-trace-product-proof.md:43` calls a C value 'canonical'; `frobenius-s-classification` claims q→1/q invariance of z, true only for z_C. No edits made: a sweep needs the owner's go (ask-first rule).


2026-10-10: Group A (6 sites, statement D / sibling C) fixed in PR #7562, commit bbd38f07. Each D value recomputed at the proton pin (mpmath 30 dps); old C figure kept in a dated note. Remaining: 15 Group B unmarked sites + 4 undetermined groups, per-file plan awaiting owner approval (mass-endomorphism/m6-group-b-plan.md in project files).


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

A proof block whose numerical witness was C at the muon pin under a D
statement at proton. The CODE surface is clean, but a published proof block's
recorded numbers are not code -- re-deriving them is the `qou-cds1` ladder
work or a scoped note. Not closeable by a value audit.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.



## 2026-10-10: undetermined groups measured and partly applied
Measurement: /mnt/project-files/mass-endomorphism/m6-undetermined-measured.md.
- **Group 1 (Pair-Skein), applied (1a):** the denominator q^{1/2}+q^{-1/2} is 1/z_C. Four .md blocks now say so (pair-skein-mass-formula + proof, flavor-split-substrate-proof, flavor-dressed-mass-from-substrate-split, beta-decay-skein-properties). The re-derivation is qou-cds1's. The fit flag in flavor-split Step 2 is beaned separately.
- **Group 3 (six muon literals), applied (3a):** the labels now name the pin each producer actually recorded (CODATA-2018 muon, or none). The proton re-pin is queued on qou-1c4y.
- **Group 4:** moot under the owner's 2a pick.
- **Group 2 (GNS positivity), OPEN, needs an owner pick.** Under D the trace is positive for every q>0 (numeric check n=2..8; Jones, [2]_q>=2). Rewriting the proof is a math-claim change.
Stays open for group 2.


## 2026-10-10 closed (session_01ST9RpvTF7JHNdUNafrjf9J)
Fix landed. Residual sweep of other proof siblings for C survivors moved into thread qou-moj0.
