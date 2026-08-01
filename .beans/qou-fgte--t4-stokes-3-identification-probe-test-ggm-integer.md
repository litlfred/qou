---
# qou-fgte
title: 'T4: Stokes-3 identification probe — test GGM integer A_ω=3 against corpus κ-tower amplitude 2πC_n→3'
status: in-progress
type: task
priority: normal
created_at: 2026-07-27T14:57:31Z
updated_at: 2026-08-01T22:59:02Z
---

## Verdict note (2026-08-01, PR #4521)

Branch `claude/stokes3-identification-aomega-2026-08-01`. Resurgent large-order route — HONEST SPLIT result:

- **ACTION = Vol(4₁)/π CONFIRMED.** 12-order κ-tower (dps 300, two-ladder trust gate; κ₁–κ₄ = exact closed forms to 40+ digits). Ratio-slope A=0.6557, Aitken A_n→0.6443 vs Vol/π=0.6461 (~0.3%). Single REAL positive Borel singularity, monotone A_n (0.55→0.64), real Borel–Padé poles → **refutes** the 6-order 2026-07-07 conjugate-pair reading (scope-a re-scope of "action complex/preliminary").
- **AMPLITUDE = 3 NOT reproduced.** Naive large-order 2πP→≈1 (O(1)), not 3, in any natural normalization. A_ω=3 stays the GGM state-integral **algebraic** value (qbeta_g3_ggm_stokes_41) — cross-checked in structure, not re-derived from 12 real κ_n (entropy-limited, as the corpus predicted). No c_k wired; no Q_β wiring.
- **Lean** `Stokes3LargeOrderAmplitude.lean` sorry-free (lean-direct exit 0): honest action-carrier `GeometricKappaAction` (amplitude=3 deliberately NOT asserted) + extraction machinery + the conjugate-pair envelope the data ruled out.

NOT marking completed (owner-only per AGENTS §4a).
