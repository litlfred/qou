---
# qou-3l2l
title: alpha_em chain (and the m_K/m_pi meson leg)
status: todo
type: epic
priority: normal
tags:
    - reorg-2026-10-04
    - compute-accuracy
created_at: 2026-10-04T15:09:58Z
updated_at: 2026-11-27T14:18:17Z
parent: qou-10v9
---

Sub-epic P1.AEM of PROGRAM: L2 at 1 ppQ (mass and binding accuracy) (work-plan reorganisation 2026-10-04).

## 2026-11-16 — Owner Ruling `Q-3L2L-1 = 1` Executed (`litlfred/qou#8141`)

- **`qou-mxnu` & `qou-vbz4`:** Formalized in `folio/quantum-observable-universe/lean/QOU/AlphaEM/StdBlockHoefsmitMarkovSchur.lean` (`0` `sorry`, generic `R` per §7c, wired into `folio/quantum-observable-universe/lean/QOU.lean`) with 50-dps `mpmath` + exact rational/symbolic probe `computations/alpha_em/std_block_hoefsmit_markov_schur_probe.py` and witness `computations/alpha_em/std-block-hoefsmit-markov-schur.witness.json` (9/9 PASS; commit `593cd323f3c15de52fd2e46e8f2346c6fd815c68`, PR `https://github.com/litlfred/qou/pull/8141`).
- **`qou-jlto`, `qou-m117`, `qou-wf2v`, `qou-wrtv`, `qou-aemx`:** Verified all landed on-`main` Lean modules, 50-dps probes/witnesses, and audits (`TauS5EquivarianceReduction.lean`, `alpha_em_b2_cm_weierstrass_scale_probe.py`, `2026-07-25-alpha-em-b2-canonical-scale-ratio.md`, `PerLoopMeasureShadowAssembly.lean`, `em-coupling-chern-simons.{lean,md}`) and updated all child beans at `status: in-progress`.



## Claim reset 2026-11-22
In-progress only through an untouched batch PR / no live branch (applicability review, thread "Coordinate the L2 1-ppQ derivation plan"; plan doc /mnt/project-files/l2-1ppq-coordination/). Reset to todo under the stalled-claim policy; nothing in the work was judged. Re-claim if you pick it up.
