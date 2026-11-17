---
# qou-6eke
title: Remark interpreting 2510.04782v2.pdf at rem:quantum-bloch-group-framework-connection
status: in-progress
pr: 8305
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:36:33Z
updated_at: 2026-11-17T10:36:00Z
parent: qou-aqfj
---

The K_3 -> Pic regulator on the Habiro ring, with Chern-Simons q-series as sections, is a literature statement in the same shape as the corpus's Bloch-group/regulator picture; a remark recording the parallel (and its limits) is the honest linkage. Explicitly NOT aid-proof: the descent theorem is not the universality claim motivic-substrate-canonicity makes.

**From the source**
- sec. 1.4 — The Habiro ring of a number field carries a regulator from K_3 into its Picard group, whose image line bundles have sections given by q-series from perturbative Chern-Simons theory; this geometry is invisible after (q-1)-completion.
  Use here: Directly parallels rem:quantum-bloch-group-framework-connection, which places the framework's traced volumes in a quantum Bloch group with a regulator to R and tags itself 'habiro'; it also identifies a missing primary reference (the number-field Habiro ring paper).

Source: `library/arxiv-2510.04782v2/2510.04782v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/arxiv-2510.04782v2/  ->  [wagner2025]
  q-Hodge complexes over the Habiro ring

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [wagner2025] as the citation key when you do it.


## Round 59 Update (PR #8305)
- **Status:** `in-progress` (PR `litlfred/qou#8305`, head `98e30d9440f58c58d66f2b657eecfe4c410e9ecd`, Commit 1 `9ff4dd7a1c80c9d8b789a5abcfa8c63a9bb600dc`).
- **Lean 4.24.0 Modules:** `folio/quantum-observable-universe/lean/QOU/QBeta/OneLoopEdgeLatticeAndWindingGFContinuation.lean` and `folio/quantum-observable-universe/lean/QOU/QBeta/MedianResummationEichlerAndHabiroPicardRegulator.lean` (`0` `sorry`, `0` `axiom`, `0` warnings, `0` advisories across all static vacuity/borrowed-name/sorry detectors).
- **80-dps Probe & Witness:** `computations/probes/round59_oneloop_edge_winding_gf_eichler_median_habiro_picard_probe.py` and `computations/probes/round59-oneloop-edge-winding-gf-eichler-median-habiro-picard.witness.json` (`allPassed: true`, `0` raw `float64`).
