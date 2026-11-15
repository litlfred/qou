---
# qou-avra
title: 'q-Fourier mode-solve: fit D(m) cofactors to one Habiro element via contiguity ratio (root-of-unity spectrum)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-11T14:01:41Z
updated_at: 2026-11-15T17:33:12Z
parent: qou-avtq
blocked_by:
    - qou-cds1
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: EVIDENCE-UNRELIABLE.** The q-Fourier mode spectrum this bean would fit to was computed from the convention-C Δtr_M (its ζ₄ pole 1/(u²+1) is the z_C denominator). Under D the pole set differs ((q²+1)² denominator). Redo the mode decomposition on the D-frame Δtr_M before any mode-solve, and phrase the attempt as a derivation, not a fit.

Evidence: Its basis, `docs/audits/2026-06-01-habiro-q-difference-mode-solve.md`, decomposes Δtr_M with pole sector "B: 1/(u²+1) ζ₄ cyclotomic". That is the z_C denominator: the same convention-C Δtr_M as `habiro/habiro-mode-to-ladder-bridge.witness.json`. I checked that this Δtr_M ≠ the current convention-D atom-word tr_M(n)−tr_M(p) (see zqtv). The title also says "fit".

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
