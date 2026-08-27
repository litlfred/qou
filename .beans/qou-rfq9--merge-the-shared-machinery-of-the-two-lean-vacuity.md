---
# qou-rfq9
title: Merge the shared machinery of the two Lean vacuity text-detectors
status: todo
type: task
created_at: 2026-08-27T11:56:04Z
updated_at: 2026-08-27T11:56:04Z
---

Measured 2026-08-27. Two text-level detectors now exist for the same defect
FAMILY, built ~3 weeks apart, and I did not find the first before writing the
second — a corpus-grep failure on my part (bean qou-0avp; the existing one is
bean qou-k9yt, still at `todo`).

    scripts/lean-definition-collapsed-audit.py   (2026-08-08, qou-k9yt)
    scripts/lean-borrowed-name-audit.py          (2026-08-26, qou-0avp)

## They are NOT duplicates — measured, and this is the useful part

    my 19 CRITICAL flagged by the existing tool at any tier :  0 of 19
    my 115 major flagged by the existing tool at any tier    : 21 of 115  (18%)
    its 1 CRITICAL flagged by mine at any tier               :  0 of 1

The discriminating signals are different and find near-disjoint populations:

- definition-collapsed keys on docstring-says-OPEN + proof-is-definitional.
  Its CRITICAL count is 1 because the corpus was drained of that shape in #4741.
- borrowed-name keys on a name invoking a MATHEMATICIAN + local-only defs +
  cheap proof, with OVERCLAIM (docstring OVER-claims) as the mirror signal.

## What IS duplicated, and should be shared

The generic machinery, written twice:
  - the COLLAPSED signal (rfl / trivial / short simp-unfold over a same-file def)
  - the binder-field exclusion (proof discharges via `C.field` / `h.foo` ⇒ a real
    conditional derivation, skip). Both implementations arrived at this
    independently and it is the same rule.
  - docstring extraction above a decl; comment blanking; local-def resolution.

Proposal: factor these into one module both import, keeping the two
discriminating signals as separate front-ends. Do NOT merge the front-ends —
their populations barely overlap, and collapsing them would bury one tier's
signal in the other's ~1880/~1030 advisory noise.

## The Lean-side sharpening qou-k9yt asked for now EXISTS

That bean's "Caveat / future work" says the advisory tier could only be sharpened
by "a Lean-side check (does the statement still hold with the defs made
opaque?)". scripts/lean/BorrowedNameKernel.lean does exactly that, via
`Meta.isDefEq` under `forallTelescopeReducing` — 42 modules / 615 theorems / 102
collapses so far (docs/audits/2026-08-26-kernel-defeq-sample.witness.json).

It INDEPENDENTLY reproduced that tool's single surviving CRITICAL,
`qInt_eq_canonical` — which on inspection is a false positive for both of us:
its docstring says "The two are definitionally the same object, so the
consolidation here is this equation — checked, not asserted", i.e. a
compatibility lemma that SHOULD be `rfl`. Good calibration: defeq_collapse is a
candidate, never a verdict.

Blocked on nothing. Whoever takes it should also decide whether qou-k9yt's
`--strict` CRITICAL gate belongs in the (currently dispatch-only) CI.
