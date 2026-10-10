---
# qou-g16t
title: 'mass_endomorphism.py script health: float64 Phi_q, non-Molien weights, crashing diagnosis caller'
status: todo
type: task
created_at: 2026-10-10T07:00:16Z
updated_at: 2026-10-10T07:00:16Z
parent: qou-d8c7
---

Carrier M7 of the mass-endomorphism epic. `computations/mass_endomorphism.py` (and its
generated mirror `qou-mass/src/qou_mass/_internal/mass_endomorphism.py`, which must not be
hand-edited — regenerate with `scripts/sync-qou-mass-vendor.py`) had defects spread across
five beans and owned by none of them.

Verified on `main` 2026-10-10:

- `Phi_q` computes in float64 (`product = 1.0`, `1e-300` guard) beside an mpmath twin
  `Phi_q_mp` (about lines 146 / 280). Source: `qou-47sx`.
- `w_sym`, `w_std`, `w_alt` are self-normalised `dim_q^2/[3]_q!` (about lines 136-138), not
  the owner-ruled Molien weights. They feed `m_p_m_e_li2q`, an already-recorded 407 % miss,
  so no published number moves. Source: `qou-oots`.
- `additive_wedderburn_volumes` is float64. Source: `qou-oots`.
- `brane_tower_isospin_diagnosis.py:180` still crashes against the module; `qou-47sx`'s
  verdict is retire or port, not patch.
- Already resolved, recorded for completeness: `z_mark` is convention D
  (`q^3/(q^2+1)`, `qou-lbgh`, `qou-bsec`); production binding uses `towerTerm`, not `Phi_q`
  (`qou-2tuv`).

Next honest step: decide retire-vs-port for the diagnosis script, then carry the module to
mpf end to end per the NO-FLOAT64 rule and run `scripts/precision-gates.sh --changed`.
Changing the weights is an owner-ruled change and moves no live number; say so in the PR.
