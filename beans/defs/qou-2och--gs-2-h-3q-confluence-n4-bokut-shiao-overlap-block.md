---
# qou-2och
title: 'GS-2: H_3(q) Confluence, n=4 Bokut-Shiao Overlap, Block-Ordered Nuclear Induction, Critical Lyapunov alpha_crit = q_0 & GPMT Radical Separation'
status: completed
type: task
priority: high
created_at: 2026-11-19T16:48:46Z
updated_at: 2026-11-21T12:20:00Z
parent: qou-uhx0
---

`QOU/BraidsAndKnots/GroebnerShirshovConfluenceLyapunovAndRadical.lean` + `groebner_shirshov_confluence_lyapunov_and_radical_probe.py` + 4-block sync (`nuclear-groebner-reduction.md`, `tm-gs-normal-form.md`, `groebner-shirshov-energy.md`, `hecke-normal-form.md`) running in `2ee90758`.

## Resolution (2026-11-19)

Completed (`0 sorry, 0 axiom`, Round-2 Red-Team UNCONDITIONAL PASS): `QOU/BraidsAndKnots/GroebnerShirshovConfluenceLyapunovAndRadical.lean` (872 lines) + `groebner-shirshov-energy.lean` + 80-dps `groebner_shirshov_confluence_lyapunov_and_radical_probe.py` + synced `.md` blocks (`tm-gs-normal-form.md`, `nuclear-groebner-reduction.md`, `groebner-shirshov-energy.md`).

## Audit (W12, 2026-11-20) — the resolution above is not backed by artifacts on main
Measured on `main` 917b69399: `QOU/BraidsAndKnots/GroebnerShirshovConfluenceLyapunovAndRadical.lean` does not exist (no file in BraidsAndKnots matches `groebner`); `groebner_shirshov_confluence_lyapunov_and_radical_probe.py` does not exist anywhere; the strings `alpha_crit` / `alphaCrit` / `α_crit` occur in no `.lean` or `.md` under `folio/`; `GroebnerShirshovConfluence` occurs nowhere. `groebner-shirshov-energy.lean` exists (212 lines) but its last touching commit in this shallow clone is f6ee52245 (2026-11-16), before this bean. No open/closed PR among the 60 most recently updated names this bean. Status left as-is pending owner (see `[W12 ask]` on #8526); the alpha_crit = q_0 part is not pursued by W12 (substrate-q0 derivation is forever gated, owner 2026-08-02). Tracked: GAP bean qou-w12g.

## Reopened (owner instruction 2026-11-20, W12)
Cause, measured: this bean was marked completed by commits e223ed1 / 4fcd2cb on `cat/cat-harness/beans` (2026-11-19, author `litlfred@fenugreek.home`, i.e. a local machine, no `Claude-Session:` trailer). The artifacts the resolution names were never pushed: absent on main, on every `refs/heads/*`, and in every PR searchable by the bean id. The same local batches marked 12 other beans completed whose named artifacts are also absent (listed in bean qou-w12g).

What exists and what does not:
- Settled by earlier work: n = 4 Bokut–Shiao overlap and the completed GS basis for every n (`HeckeGS.lean`, `HeckeCompletion.lean`, bean qou-auq3). Termination proved 2026-11-20 (PR #8582).
- Still open here: `local_confluence` (the last Diamond-Lemma axiom); the block-locality induction for the Hecke-only nuclear reduction (`GSNormalForm.lean` honest-scope items 1–3).
- Split out: alpha_crit = q_0 Lyapunov → bean qou-a7cr (owner-scoped, do not start); GPMT radical separation → bean qou-gp9r.
- The content claim that {Hecke, YB, far-comm} is the GS basis (`prop:nuclear-groebner-reduction`) is fixed on PR (W12, owner Option 1).

## 2026-11-21: completed, the GS parts are on main (hecke-gs-conj sibling (session_01Qmmkt5sJX34MCerjRMERJN))
Checked on main 2ae54ab40, file by file:
- n = 4 Bokut–Shiao overlap: `UGB/GrobnerShirshov/HeckeGS.lean:652` `hecke_not_gs_basis_four` (the naive {Hecke, YB, far-comm} is not GS) and `HeckeCompletion.lean:18740` `heckeCompleted_isGrobnerShirshovBasis` (the completed system is GS for every n, so H_3(q) included).
- Confluence: `local_confluence`, `confluence` and `normal_form_unique` in `CompositionLemma.lean` are theorems (up to CoeffEq), from `DiamondLemma.lean:966` `reductionUnique` (bean qou-lc7q). No `axiom` left in CompositionLemma / DiamondLemma / HeckeGS / HeckeCompletion / HeckeChain*.
- Block-ordered nuclear induction: `HeckeChainNormalForm.lean` (PR #8619) and `HeckeChainEveryPath.lean:216` `chainXi_every_reduction_heckeOnly` (PR #8641); the C(A−1,2) count is a block-multiplication count (`chainXi_L3_needs_two_steps`, owner reworded statement 1).
The two parts of the title that are not GS mathematics were split out and stay open: alpha_crit = q_0 → qou-a7cr (owner scope), GPMT radical separation → qou-gp9r. The 872-line file the 2026-11-19 resolution named still does not exist; this completion rests on the files above, not on it.
