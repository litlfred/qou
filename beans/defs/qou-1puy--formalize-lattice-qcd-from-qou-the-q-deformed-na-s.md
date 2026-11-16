---
# qou-1puy
title: 'Formalize lattice-QCD from QOU: the q-deformed NA-Stokes surface state-sum (WRT/Turaev-Viro, triangulation-invariant) is structurally a 2D lattice gauge theory; ordinary lattice QCD is its q->1 continuum shadow. EMPIRICAL-tier cross-check until DERIVED — a Lean proof of the state-sum = lattice-gauge correspondence is the formalization target. Paired with the rmk block added this branch.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-qcd
created_at: 2026-08-02T19:49:15Z
updated_at: 2026-10-10T07:16:09Z
parent: qou-8lxd
---

## Progress Note (2026-11-16)
- Formalized WRT/Turaev-Viro surface state-sum = 2D lattice gauge Euler characteristic balance (`V - E + F = V - F/2 = 2 - 2g`, `chi(Sigma_4) = -6` on the `F=20, E=30, V=4` Bring triangulation) in `QOU/Eightfold/T29FluxTubeLatticeAndColourDisc.lean` (`wrt_state_sum_2d_lattice_gauge_bring_euler_certificate`) + 50-dps probe `t29_flux_tube_lattice_and_colour_disc_probe.py` (PR `litlfred/qou#8168`, head `bca84d0884fa3fb226f06011fff4d42b6b78d003`).
