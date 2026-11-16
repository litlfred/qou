---
# qou-3cgi
title: 'GAP: C1↔SW geometric leg — finite content exhausted, residual is W1-W3 geometric-analysis program'
status: in-progress
pr: 8191
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T01:10:50Z
updated_at: 2026-10-04T15:19:47Z
parent: qou-frzo
---


## Status (2026-08-01 survey)

The C1↔SW geometric leg (`conj:qdifference-kernel-prolongation-symbol`) has its
**finite/algebraic content exhausted** — both finite sub-claims the coordination
doc scoped are already PROVED sorry-free on main:

- **S1** (ramification monodromy = (−1)ⁿ character): `QOU/Brings/RamificationParityMonodromy.lean` (`classical_jet_not_door_v`, etc.).
- **"brick #7"** (Newton-polygon slope yes/no, C1 slope-½ vs GGM Stokes {−1,+1}): `QOU/Mass/ThetaSlopeArithmetic.lean` (`ggm_anisoclinic`, `pullback_cannot_reach_ggm`, `sinhcosh_reaches_ggm`).
- Supporting: `ColorSpectralCubicGeometry.lean` (discriminant = −branchSextic, palindromic), `ColorCubicPowerSums.lean` (power sums q-free), `sw-classical-jet-exactness.lean` (classical-jet residues = 0).

**Residual = irreducibly open geometry (W1–W3, per `docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md`):**
- W1: construct the q-difference prolongation `D_q` *from Σ* (no q-jet-bundle / q-D-module symbol calculus in Mathlib or corpus).

> 🛑 **Scope correction (2026-09-06, bean `qou-p6m1`).** The claim above bundles two objects. The **q-D-module symbol calculus is PRESENT** — `QOU.Machinery.QuantumTorusSymbol` (QDM-1/2, 19 decls, sorry-free, on `main` by 2026-07-24) and `QOU.Mathlib.RamifiedShiftCalculus` (the same calculus at the ramified pole `z = z_c + t²`, sorry-free, 2026-09-03, and it *imports* `RamificationParityMonodromy`, the file that declared it absent). Only the **q-jet bundle over `Σ`** is absent. **W1 (construct `D_q` from `Σ`) still stands** — this is a scoping split, not a downgrade.

- W2: extract its principal symbol at a ramified pole (Ramis–Sauloy–Zhang local classification — cited only for the obstruction).
- W3: anti-fit obligation — symbol must be computed from Σ without target-matching C1.

Verdict: multi-month geometric-analysis program; NOT closeable by a probe or short
Lean lemma. Not a finite sub-brick. Sibling `qCubicGradedSplit` (PR #4140, off-main)
is the same class of open geometry.

## Progress (PR #8191)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/ResurgenceCasoratianAndBarSymmetrization.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/resurgence-casoratian-and-bar-symmetrization.witness.json` (`scriptHash: 2c8e09c0d6af`, `scriptCommitSha: e9de8818430aa7aa5b7c9bf66d2b0bab443b968f`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8191 (`8351218487c53d0f60e66b9d4c335ccaab315d98`).
