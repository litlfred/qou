---
# qou-68uk
title: Cross-check s40687-023-00400-3.pdf at computations/probes/borromean_nz_adjoint_torsion.py
status: todo
pr: 8305
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:37:02Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8hur
---

Recompute the 4_1 NZ matrices by the document's combinatorial recipe and compare against the corpus's corrected one-loop torsion producer, including the retriangulation-invariance test the earlier construction failed. This is a verification of the corpus's own corrected value, not an adoption of an external one. Restrict strictly to the one-cusped case; do not extend the comparison to the Borromean complement.

**From the source**
- Abstract and the construction of twisted NZ matrices from triangulation combinatorics — Twisted Neumann--Zagier matrices are defined, shown to retain the symplectic properties of the untwisted ones, and computed directly from the combinatorics of an ideal triangulation.
  Use here: The reference construction against which the corpus's corrected NZ determinant should be checked, in a form that is explicitly combinatorial and therefore testable for the retriangulation invariance the corpus's earlier version failed.

Source: `library/s40687-023-00400-3/s40687-023-00400-3.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/s40687-023-00400-3/  ->  [garoufalidis2021]
  TWISTED NEUMANN–ZAGIER MATRICES

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [garoufalidis2021] as the citation key when you do it.


## Round 59 Update (PR #8305)
- **Status:** `in-progress` (PR `litlfred/qou#8305`, head `98e30d9440f58c58d66f2b657eecfe4c410e9ecd`, Commit 1 `9ff4dd7a1c80c9d8b789a5abcfa8c63a9bb600dc`).
- **Lean 4.24.0 Modules:** `folio/quantum-observable-universe/lean/QOU/QBeta/OneLoopEdgeLatticeAndWindingGFContinuation.lean` and `folio/quantum-observable-universe/lean/QOU/QBeta/MedianResummationEichlerAndHabiroPicardRegulator.lean` (`0` `sorry`, `0` `axiom`, `0` warnings, `0` advisories across all static vacuity/borrowed-name/sorry detectors).
- **80-dps Probe & Witness:** `computations/probes/round59_oneloop_edge_winding_gf_eichler_median_habiro_picard_probe.py` and `computations/probes/round59-oneloop-edge-winding-gf-eichler-median-habiro-picard.witness.json` (`allPassed: true`, `0` raw `float64`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8305, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
