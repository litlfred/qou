---
# qou-t4fe
title: Remark interpreting [deturck-gluck2008] at rem:helicity-physical
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:27Z
updated_at: 2026-10-04T15:23:44Z
parent: qou-vva9
---

Before relying on any bound from this note, record that it states 'we give only a hint of the proofs' - the full proofs are in the journal version, and the constants would need checking there.

**From the source**
- front matter, bullets 1 and 3 — Explicit isometry-invariant integral formulas for linking, twisting, writhing and helicity in S^3 and H^3, with the Biot-Savart formula yielding upper bounds for helicity and lower bounds for the first eigenvalue of curl on subdomains.
  Use here: The hyperbolic-space version is the setting the framework actually works in; a helicity upper bound in H^3 is the natural comparison for the vorticity lower-bound argument, which currently argues in the Euclidean setting.

Source: `library/0406276v1/0406276v1.pdf` (`deturck-gluck2008`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-21 — cite-remarks bean drain (thread "Interpret citation remarks", issue litlfred/qou#8806)

rem:helicity-physical now cites deturck-gluck2008 §13 Thm 7 (|H(V)| <= N(R)|V|^2) and records the source's own 'only a hint of the proofs' caveat.

Done on branch `claude/cite-remarks-2026-11-21` at 3b2491716; status stays in-progress until that branch merges.
Owner-ruling check (docs/coordination/owner-rulings.md, main 2ae54ab40): no superseded premise found; this is a citation item and touches none of the photon, electron, trace, convention, chi or T(2,n_s) rulings.
