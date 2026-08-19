---
# qou-u33z
title: Cross-check cspaper.pdf at computations/one_loop_torsion.py
status: todo
type: task
created_at: 2026-08-08T23:36:22Z
updated_at: 2026-08-08T23:36:22Z
---

Check whether the parity condition of Theorem 2 is the normalisation the corpus records as the dropped flattening monomial, by comparing the resulting ambiguity lattice against the unit-group-of-the-trace-field characterisation already recorded in one-loop-ambiguity-group.witness.json. A match would explain the observed ambiguity; a mismatch is equally informative. No external constant may be adopted either way.

**From the source**
- Theorem 2 (with the parity condition; Theorem 2.4 / Sects. 4-6) — Integral solutions satisfying a parity condition exist, and for such solutions the constant alpha of Theorem 1 is independent of the solution modulo an explicit lattice; dropping the parity condition weakens the conclusion.
  Use here: Directly addresses the corpus's live problem of a triangulation-dependent constant in the one-loop / det J chain. What would need checking before claiming more: whether Neumann's parity condition is the same normalisation as the Dimofte-Garoufalidis flattening monomial the corpus records as dropped, and whether it says anything about the multi-cusp per-cusp factor that borromean_nz_adjoint_torsion.py flags as unpinned at c >= 2. Proposed as compute-check plus remark, NOT aid-proof, because neither of those has been verified.

Source: `library/cspaper/cspaper.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
