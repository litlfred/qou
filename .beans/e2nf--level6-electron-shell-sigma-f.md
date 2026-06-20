---
# e2nf
title: Level-6 electron shell — σ_F dual, shell-closure fix, 2n² gap
status: in_progress
type: task
priority: normal
created_at: 2026-06-16T02:16:00Z
updated_at: 2026-06-20T03:00:00Z
---

Branch `claude/zealous-hypatia-05xyp9` → PR #2348. Picked up a stalled
electron-shell / atomic-mass discussion; tracked via docs/audits + the
low-isotope-mass-anatomy ledger before adopting this bean.

## Delivered

- **Level-6 atom→electron mass** (`computations/atom_electron_mass.py`):
  `m_atom = m_sym + Z·m_e − E_e_binding` vs AME atomic; ¹H exact; residual is
  ~100% nuclear B_sym. e-Hartree scale is canonical (`E_HARTREE_EV=27.21 eV`),
  correcting a prior 25-MeV/electron blunder.
- **SDP-capacity formalize-first correction** (`electron_shell_sdp_capacity.py`):
  "add electrons until SDP infeasible" is wrong — σ_F (dual) is monotone; the
  raw-Gram H=5/He=8 "capacity" is the excluded interlacing branch.
- **σ_F(Z) dual chain** (`electron_sigma_f_chain.py`, cvxpy cross-check) +
  **marginal demo** (`electron_sigma_f_marginal.py`).
- **Resolved a σ_F inconsistency** in `prop:shell-closure-stability` (claim 1
  monotone vs claim 2 strict-local-max) → marginal Δσ_F=I₁ peaks; σ_F monotone.
- **Coordinate §6 align**: reconciled with main's more-rigorous
  `sigma_f_electron_shell_chain.py` (8ecbbca9) + caveat (ae7e0813); made the
  noble-gas-peak LOCATION conditional on the open 2n²/Madelung derivation.
- **2n² diagnosis** (`docs/audits/2026-06-16-2n2-shell-capacity-derivation-gap.md`):
  genuinely open — 2×2 T_γe gives spin-2, not the orbital n²; needs an absent
  SO(4)/Runge-Lenz degeneracy; softened the unsupported overclaim.
- Removed a vacuous shadowing Lean stub (no-shadowing-stubs).

## Open

- [ ] Rebase #2348 onto current main (~479 commits ahead; only the ledger
      both-appends — keep both). `/prepare-merge` at merge time.
- [ ] Research: derive the SO(4)/Runge-Lenz n²-bundling, or accept 2n² as a
      topological input — the blocker for emergent shell peaks (not a model tweak).
- [ ] (env) content validator + Lean build absent in this sparse checkout; CI to
      confirm content validation + lean.ref resolution after the stub removal.

## Notes

- Audits: docs/audits/2026-06-16-{level6-atom-electron-wiring, electron-shell-sdp-
  capacity-formalize-first, sigma-f-electron-dressing-chain, shell-closure-sigma-f-
  inconsistency-resolved, 2n2-shell-capacity-derivation-gap}.md
- Ledger: docs/coordination/2026-05-24-low-isotope-mass-anatomy-ledger.md
- Bean adopted 2026-06-20 per owner ("are you using beans?"). bean-coordination
  skill redirects to folio-assistant (not in this checkout) — following observed
  file format, not the full protocol.
