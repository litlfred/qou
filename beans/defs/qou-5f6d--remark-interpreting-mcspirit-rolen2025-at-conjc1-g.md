---
# qou-5f6d
title: Remark interpreting [mcspirit-rolen2025] at conj:c1-ggm-bar-parity-faces
status: in-progress
pr: 8305
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:35Z
updated_at: 2026-11-17T10:36:00Z
parent: qou-vva9
---

Record what must be checked before any of its theorems are used: whether the folio's divergent series sit in the half-integer-weight Eichler-integral class the median-resummation results cover. Without that check the connection is thematic only.

**From the source**
- Sec. 1, 'main addition to the literature' (median resummation results) — The holomorphic quantum modular forms treated can be recovered from their asymptotic expansions (or those of closely related functions) by median resummation.
  Use here: A recovery-from-asymptotics statement is the resurgence-side counterpart of the Habiro/Stokes framing; it would give the c1/GGM bar-parity and Stokes-DT blocks a citable resummation result instead of an informal appeal to resurgence.

Source: `library/arxiv-2505.00799v2/2505.00799v2.pdf` (`mcspirit-rolen2025`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## Round 59 Update (PR #8305)
- **Status:** `in-progress` (PR `litlfred/qou#8305`, head `98e30d9440f58c58d66f2b657eecfe4c410e9ecd`, Commit 1 `9ff4dd7a1c80c9d8b789a5abcfa8c63a9bb600dc`).
- **Lean 4.24.0 Modules:** `folio/quantum-observable-universe/lean/QOU/QBeta/OneLoopEdgeLatticeAndWindingGFContinuation.lean` and `folio/quantum-observable-universe/lean/QOU/QBeta/MedianResummationEichlerAndHabiroPicardRegulator.lean` (`0` `sorry`, `0` `axiom`, `0` warnings, `0` advisories across all static vacuity/borrowed-name/sorry detectors).
- **80-dps Probe & Witness:** `computations/probes/round59_oneloop_edge_winding_gf_eichler_median_habiro_picard_probe.py` and `computations/probes/round59-oneloop-edge-winding-gf-eichler-median-habiro-picard.witness.json` (`allPassed: true`, `0` raw `float64`).
