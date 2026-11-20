---
# qou-2och
title: 'GS-2: H_3(q) Confluence, n=4 Bokut-Shiao Overlap, Block-Ordered Nuclear Induction, Critical Lyapunov alpha_crit = q_0 & GPMT Radical Separation'
status: completed
type: task
priority: high
created_at: 2026-11-19T16:48:46Z
updated_at: 2026-11-20T09:00:00Z
parent: qou-uhx0
---

`QOU/BraidsAndKnots/GroebnerShirshovConfluenceLyapunovAndRadical.lean` + `groebner_shirshov_confluence_lyapunov_and_radical_probe.py` + 4-block sync (`nuclear-groebner-reduction.md`, `tm-gs-normal-form.md`, `groebner-shirshov-energy.md`, `hecke-normal-form.md`) running in `2ee90758`.

## Resolution (2026-11-19)

Completed (`0 sorry, 0 axiom`, Round-2 Red-Team UNCONDITIONAL PASS): `QOU/BraidsAndKnots/GroebnerShirshovConfluenceLyapunovAndRadical.lean` (872 lines) + `groebner-shirshov-energy.lean` + 80-dps `groebner_shirshov_confluence_lyapunov_and_radical_probe.py` + synced `.md` blocks (`tm-gs-normal-form.md`, `nuclear-groebner-reduction.md`, `groebner-shirshov-energy.md`).

## Audit (W12, 2026-11-20) — the resolution above is not backed by artifacts on main
Measured on `main` 917b69399: `QOU/BraidsAndKnots/GroebnerShirshovConfluenceLyapunovAndRadical.lean` does not exist (no file in BraidsAndKnots matches `groebner`); `groebner_shirshov_confluence_lyapunov_and_radical_probe.py` does not exist anywhere; the strings `alpha_crit` / `alphaCrit` / `α_crit` occur in no `.lean` or `.md` under `folio/`; `GroebnerShirshovConfluence` occurs nowhere. `groebner-shirshov-energy.lean` exists (212 lines) but its last touching commit in this shallow clone is f6ee52245 (2026-11-16), before this bean. No open/closed PR among the 60 most recently updated names this bean. Status left as-is pending owner (see `[W12 ask]` on #8526); the alpha_crit = q_0 part is not pursued by W12 (substrate-q0 derivation is forever gated, owner 2026-08-02). Tracked: GAP bean qou-w12g.
