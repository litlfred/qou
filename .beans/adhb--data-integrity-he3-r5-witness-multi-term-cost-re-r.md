---
# adhb
title: 'Data-integrity: He3 R5 witness multi-term-cost re-run (regen winner diverged)'
status: todo
type: task
created_at: 2026-06-26T03:39:52Z
updated_at: 2026-06-28T23:30:00Z
---

## Empirical diagnosis (2026-06-28) — "re-run with multi-term cost recovers canonical" is REFUTED

Ran the CURRENT `r5_full_canonical_knot_solver.py` (which ALREADY wires a multi-term offset
`b23 + t4` from `mass_formula_6term`, lines 562–590) for he3 + deuteron — H₃ Wenzl weights read
from `y-lambda-wenzl-witness.json` (pyhecke_native unavailable, same Clarabel.rs scope block as b0vf;
cache matches native to 3e-16). `solve_atom_b3` called directly; committed witness NOT touched.

Result — canonical winner does NOT emerge for either atom:
- **deuteron**: canonical `6_2` is NOT PSD-feasible (α_gap=0.89, rank 1051) — cannot win an
  α-gap-driven search at all. Winner `[1,-2,1,-2,-1,-1,-1,-2]` ρ=2.
- **he3**: canonical `L6a4` IS PSD-feasible but ranks 381st (rel_resid 0.74). `B_AME=7.718` MeV but
  L6a4 predicts only ~2.04 MeV even WITH the ~1 MeV multi-term offset; best B₃ candidate reaches 4.58.
  The offset is far too small to close the ~5.7 MeV deficit (the documented ~87–100% single-term
  magnitude offset).

So the bean's mechanical-re-run hypothesis fails. Tuning w_resid/offset to force canonical = fitting
to the known answer (FORBIDDEN no-fit). The real fix is research-grade: (a) a feasibility criterion
admitting deuteron `6_2`, and (b) a multi-term formula whose MAGNITUDE actually reaches B_AME — not a
weight tune. Committed witness correctly stays frozen (PR #2836). No production change. Audit:
`docs/audits/2026-06-28-adhb-r5-multiterm-insufficient-b0vf-native-blocked.md`.

## Problem (2026-06-26, PR #2836)

`Helium3Witness.lean` is pinned to PR #608's canonical `L_6a4` solve, but
`r5-full-canonical-knot-solver.witness.json` was **regenerated 2026-06-22**
(`scriptCommitSha c4ab12b6`) with a **single-term** binding cost
`B = m_e·ρ·|tr_M(T_w)|` that under-constrains the search. The regen `he3` winner
diverged to a degraded, non-canonical result:

- word `σ₁⁶σ₂² = [1,1,1,1,1,1,2,2]` (≠ canonical `L_6a4 = (σ₁σ₂⁻¹)³`)
- `rho_star=4` (≠ 3), `cost=0.14291`, **`rel_residual=0.5716` (57 % off `B_AME`)**.

PR #2836 documented the divergence and **kept the frozen PR #608 values** (wiring to
the regen would regress). This bean tracks the **real fix**.

## Task

Re-run the R5-full canonical knot solver for `he3` (and `deuteron`, same root cause —
audit §2) with the **full multi-term cost** (T2–T6 of `thm:knot-mass-formula-unified`),
which re-selects the canonical winner. Then refresh `Helium3Witness.lean` to the
re-witnessed values under the witnessed-values discipline (and re-derive the
strict-complementarity cert from the re-emitted per-block min-eigs).

## Refs

- Audit: `docs/audits/2026-06-25-r5-witness-staleness-and-rescoped-todo-triage.md` §1–2
- Lean: `content/quantum-observable-universe/lean/QOU/BraidKnot/Helium3Witness.lean`
  (*Witness divergence* note)
- Producer: the r5-full canonical knot solver (`computations/`) + cost function
- Sibling root cause: deuteron same single-term-cost under-constraint (audit §2)
