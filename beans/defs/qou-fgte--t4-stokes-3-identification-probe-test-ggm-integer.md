---
# qou-fgte
title: 'T4: Stokes-3 identification probe — test GGM integer A_ω=3 against corpus κ-tower amplitude 2πC_n→3'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-27T14:57:31Z
updated_at: 2026-11-15T17:33:13Z
parent: qou-avtq
blocked_by:
    - qou-cds1
---

## Verdict note (2026-08-01, PR #4521)

Branch `claude/stokes3-identification-aomega-2026-08-01`. Resurgent large-order route — HONEST SPLIT result:

- **ACTION = Vol(4₁)/π CONFIRMED.** 12-order κ-tower (dps 300, two-ladder trust gate; κ₁–κ₄ = exact closed forms to 40+ digits). Ratio-slope A=0.6557, Aitken A_n→0.6443 vs Vol/π=0.6461 (~0.3%). Single REAL positive Borel singularity, monotone A_n (0.55→0.64), real Borel–Padé poles → **refutes** the 6-order 2026-07-07 conjugate-pair reading (scope-a re-scope of "action complex/preliminary").
- **AMPLITUDE = 3 NOT reproduced.** Naive large-order 2πP→≈1 (O(1)), not 3, in any natural normalization. A_ω=3 stays the GGM state-integral **algebraic** value (qbeta_g3_ggm_stokes_41) — cross-checked in structure, not re-derived from 12 real κ_n (entropy-limited, as the corpus predicted). No c_k wired; no Q_β wiring.
- **Lean** `Stokes3LargeOrderAmplitude.lean` sorry-free (lean-direct exit 0): honest action-carrier `GeometricKappaAction` (amplitude=3 deliberately NOT asserted) + extraction machinery + the conjugate-pair envelope the data ruled out.

NOT marking completed (owner-only per AGENTS §4a).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-01 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: EVIDENCE-UNRELIABLE.** The action ≈ Vol/π comes from a 12-term numeric fit, not a proof. The amplitude test is inconclusive. The magnitude test is a linear ansatz on convention-C empirical anchors. Redo in convention D with an exponential (bridge-equation) form, or retire it.

Evidence: The large-order fit re-run reproduces the witness: A_ratio 0.6557, Aitken 0.6443 vs Vol/π 0.6461, 2πP ≈ 0.995. This is 12 orders, and the `kappa` field is stored as ~16-digit floats despite the "54-digit" claim. The amplitude "≠3" is normalization-dependent, so it does not decide the bean. The magnitude half (`qbeta_stokes3_magnitude_identification_probe.py`) re-ran with exit 0 and the same verdict (inconsistent Im u). It uses the linear S = 3·Im𝔙 ansatz that dtd3 rejects, empirical CODATA anchors, and `c3_target_at` in convention C. The muon S in its docstring (0.00968298) ≠ the witness (0.0100229).

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

### Progress (Round 74 — PR litlfred/qou#8322)
- Formalized in PR `litlfred/qou#8322` (`feat/round74-kashaev-stokes3-stokesamp-ohtsukinz-pauli-43c1`, Commit 1 `82ec77a3b69cc6d79a85c01e64b63d422fa51c45`, Head `d13ffedea3175ba61da12a5b2abf5cf08d471608`, `scriptHash: 79ed375a0246`).
