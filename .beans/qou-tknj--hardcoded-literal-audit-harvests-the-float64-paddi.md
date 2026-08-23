---
# qou-tknj
title: hardcoded_literal_audit harvests the float64-padding audit's own fixture, turning a blocking gate red
status: todo
type: task
created_at: 2026-08-23T10:09:44Z
updated_at: 2026-08-23T10:09:44Z
---

Two audits reference each other's example data, and the pair trips a BLOCKING gate.

`witness_float64_padding_audit.py` carries, as its own documentation and test
fixture, the canonical example of the defect it detects:

    witness_float64_padding_audit.py:12    "B_AME_MeV": "8.48179620000000156210262503009289503097534179687500..."
    witness_float64_padding_audit.py:194   ("8.4817962000000015621026250300928950309753417968750...", True)
    strip_float64_padding.py:10            same string, documenting the same defect

`hardcoded_literal_audit.py` scans `computations/` for numerical literals matching
registered constants. It harvests that fixture string, matches it against
`AME_B_TRITIUM_MEV_VALIDATION` at rel_err 1.8e-16, and records it in
`hardcoded-literal-audit.witness.json`. The padding audit then flags THAT recorded
value as NEW fake precision, turning the `float64-padding ratchet` red.

Nothing is actually wrong: no producer is emitting fabricated precision. One
audit's illustration of a bug is being read as an instance of the bug.

## Repro

Run `python3 computations/audits/hardcoded_literal_audit.py`, then
`python3 computations/witness_float64_padding_audit.py --strict` — the latter
reports 1 NEW, naming `data.rows[*].hits[0].literal`.

## Why it surfaced now

The row is absent from the witness at HEAD and appears after a re-run. Neither
`witness_float64_padding_audit.py` nor `strip_float64_padding.py` was modified by
the dps sweep (bean qou-fl9i) that prompted the re-run, so the trigger is the
re-run itself rather than a source change — the committed witness simply predates
the fixture, or predates a change in what the literal scan covers. Worth pinning
down before fixing, since it decides whether other audit witnesses are similarly
stale-but-green.

## Fix, at the producer — NOT by baselining

`hardcoded_literal_audit.py` should not harvest literals from files whose purpose
is to *document* bad literals. Add the two self-referential audit sources to its
exclusion set (it already has `EXCLUSION_LINE_RX` / `ASSERTION_KW_RX` machinery
for exactly this class), or teach it to skip any file under a `*_audit.py` /
`strip_*.py` name whose match is inside a test fixture.

Do NOT silence it by adding the witness to the padding baseline — both gates say
so in their own output, and the finding would then be hidden rather than fixed.

## Interim state

`computations/audits/hardcoded-literal-audit.witness.json` was reverted to HEAD so
the blocking gate stays green. That witness is therefore knowingly stale against
its producer until this is fixed.
