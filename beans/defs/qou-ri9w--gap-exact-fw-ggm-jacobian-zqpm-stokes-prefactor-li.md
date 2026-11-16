---
# qou-ri9w
title: 'GAP: exact FW->GGM Jacobian + Z[q^pm] Stokes prefactor linking 5₂ I_{0,0} to median-Borel resummation of Phi_{5₂}'
status: in-progress
pr: 8204
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T19:03:18Z
updated_at: 2026-10-04T15:19:59Z
parent: qou-frzo
---

## QUEUED — launch a dedicated agent AFTER the two in-flight agents land

Do **not** start this while `claude/fw-thm14-realness-brick-2026-08-01` (FW Thm
1.4 realness) and `claude/rhoF-vs-adjoint-torsion-2026-08-01` (torsion
cross-check) are running — the realness brick is in the same FW↔GGM Stokes
territory and would collide. Launch on the second completion, own branch, own
draft PR, base main. It builds on the realness lemma (if it lands) and the
5₂ AK integral I_{0,0} (PR #4475).

## Lit is IN HAND (do the corpus-grep + read these BEFORE any wide derivation)

- **Primary source — GGM, *The resurgent structure of quantum knot invariants*,
  [arXiv:2007.10190](https://arxiv.org/abs/2007.10190) (CMP 2021).** The Stokes
  automorphism is a **pair of matrices of q-series with integer coefficients**,
  fixed by a pair of linear q-difference equations, and the paper **matches the
  explicit integers for 4₁ and 5₂**. This is the exact `Z[q^±]` Stokes
  prefactor. (Confirm it's registered in `references.ts`; the corpus already
  references GGM resurgent-structure work.)
- **[arXiv:2304.07001](https://arxiv.org/abs/2304.07001) *Resurgence, Habiro
  elements and strange identities*** — Habiro elements ↔ the corpus c₃
  Habiro-tower framing.
- **Read the existing corpus GGM-Stokes audits FIRST** (corpus-grep discipline —
  a lot may be derived already):
  `docs/audits/2026-07-18-g3-stokes-keystone-evidence-base.md`,
  `docs/audits/2026-07-18-aomega-stokes3-is-dt-invariant-not-tracefield-disc.md`,
  the `docs/audits/2026-07-20-qlift-*.md` set,
  `docs/audits/2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md`.
- FW (2410.20973) §4 gives the algorithm; note 5₂ = (A,B)=(2,3) (max 3, a 3×3
  Stokes matrix), while FW's fully-worked §4.2 example is a *different* (4,1)
  knot — take the 5₂ integers from GGM 2007.10190, not the §4.2 example.

## Scope
Transcribe the explicit 5₂ (and 4₁ cross-check) `Z[q^±]` Stokes matrices from
GGM 2007.10190, connect them to the median-Borel resummation of Φ_{5₂} and the
FW↔GGM Jacobian R(τ) (the realness half is `qou-ri9w`'s companion in the
realness brick), and emit a witness. This is a **literature transcription +
identification**, not a QOU c₃ derivation — the c₃ read-off is downstream and
stays honest (no fit, nothing wired).

## Progress Note (2026-11-16, PR #8204)
- Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/QGevreyCauchyAndFWGGMStokes.lean` (wired into `QOU.lean`, `0` `sorry`, `0` `axiom`, `0 CRITICAL / 0 advisory` across all 8 Lean static vacuity/borrowed-name audits).
- Verified by 80-dps `mpmath` / exact rational probe `computations/probes/qgevrey_cauchy_and_fw_ggm_stokes_probe.py` and witness `computations/probes/qgevrey-cauchy-and-fw-ggm-stokes.witness.json` (`scriptCommitSha: 8ee650e779786706f931cf4f825d18b2810370eb`, `scriptHash: 7ed9e0953101`, `allPassed: true`, `0` raw `float64` fields).
- PR: https://github.com/litlfred/qou/pull/8204 (`6b9e46ecf45f518a03c0a6fb1de251bf59b285da`).
