---
# qou-3l2l
title: alpha_em chain (and the m_K/m_pi meson leg)
status: in-progress
type: epic
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:09:58Z
updated_at: 2026-11-16T17:58:00Z
parent: qou-10v9
---

Sub-epic P1.AEM of PROGRAM: L2 at 1 ppQ (mass and binding accuracy) (work-plan reorganisation 2026-10-04).

## 2026-11-16 — Owner Ruling `Q-3L2L-1 = 1` Executed (`litlfred/qou#8141`)

- **`qou-mxnu` & `qou-vbz4`:** Formalized in `folio/quantum-observable-universe/lean/QOU/AlphaEM/StdBlockHoefsmitMarkovSchur.lean` (`0` `sorry`, generic `R` per §7c, wired into `folio/quantum-observable-universe/lean/QOU.lean`) with 50-dps `mpmath` + exact rational/symbolic probe `computations/alpha_em/std_block_hoefsmit_markov_schur_probe.py` and witness `computations/alpha_em/std-block-hoefsmit-markov-schur.witness.json` (9/9 PASS; commit `593cd323f3c15de52fd2e46e8f2346c6fd815c68`, PR `https://github.com/litlfred/qou/pull/8141`).
- **`qou-jlto`, `qou-m117`, `qou-wf2v`, `qou-wrtv`, `qou-aemx`:** Verified all landed on-`main` Lean modules, 50-dps probes/witnesses, and audits (`TauS5EquivarianceReduction.lean`, `alpha_em_b2_cm_weierstrass_scale_probe.py`, `2026-07-25-alpha-em-b2-canonical-scale-ratio.md`, `PerLoopMeasureShadowAssembly.lean`, `em-coupling-chern-simons.{lean,md}`) and updated all child beans at `status: in-progress`.
