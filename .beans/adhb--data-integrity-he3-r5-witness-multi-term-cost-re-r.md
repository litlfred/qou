---
# adhb
title: 'Data-integrity: He3 R5 witness multi-term-cost re-run (regen winner diverged)'
status: todo
type: task
created_at: 2026-06-26T03:39:52Z
updated_at: 2026-06-26T03:39:52Z
---

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
