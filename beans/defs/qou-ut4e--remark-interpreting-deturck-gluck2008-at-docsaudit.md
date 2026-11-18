---
# qou-ut4e
title: Remark interpreting [deturck-gluck2008] at docs/audits/2026-08-01-em-linking-reads-round1.md
status: in-progress
pr: 8420
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:10Z
updated_at: 2026-11-18T10:09:26Z
parent: qou-aqfj
---

Correct the audit doc's 'mixed/corrupted; only tail pages recovered' verdict for this file and remove the source from the re-upload list — the PDF reads cleanly and all three cited theorems are verifiable in-repo.

**From the source**
- Thm 1(3), p. 8 (statements at p. 3) — The H³ Gauss linking integral in parallel-transport format, with kernel φ(α) = (−1/4π) csch α — stated on the same page to be the fundamental solution of a SHIFTED Laplacian on H³, not of the plain Laplacian.
  Use here: The H³ analogue of the Euclidean 1/r linking kernel for the EM-linking attack; the 'shifted' qualifier matters.
- §5, p. 14–15 — The scalar Green's operator on H³ is convolution with φ₀(α) = (−1/4π)(coth α − 1), satisfying Δ Gr(f) = f and Gr(f)(y) → 0 at infinity.
  Use here: Corrects the registry note's φ₀ = −coth(α)/4π; the −1 is what enforces decay at infinity.
- Thm 2(3), p. 11 — The H³ Biot–Savart operator BS(V)(y) = ∫_{H³} P_yx V(x) × ∇_y φ(x,y) dx with the same csch kernel; the authors state they do not yet know how to characterise BS in H³.
  Use here: The magnetic-field half of the pair-energy construction, with its stated limitation.

Source: `library/0510388v1/0510388v1.pdf` (`deturck-gluck2008`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## Implementation Progress (PR #8420)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/HyperbolicGreenConormalFoldedTraceRound70.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`).
- Verified at 80-dps precision in `computations/probes/round70_hyperbolic_green_conormal_folded_trace_probe.py` with 2-commit witness `computations/probes/round70-hyperbolic-green-conormal-folded-trace.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8420 (`ready: f49a1cf2981f96f2f1ad64b7c08e14fa43ef96ca`).
