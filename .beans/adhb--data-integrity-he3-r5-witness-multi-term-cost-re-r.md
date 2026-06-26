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
- Producer: `computations/r5_full_canonical_knot_solver.py` — `cost_for_candidate`
  uses single-term `B_pred = ρ · m_e · |tr_M|` (line ~491)
- Sibling root cause: deuteron same single-term-cost under-constraint (audit §2)

## SCOPE (2026-06-26) — BLOCKED: research-gated, NOT a clean wire-up

Grounding the "multi-term-cost re-run" found it is **gated on an open derivation
question**, not a straightforward implementation. Per
`mass-theory/six-term-mass-formula-complete.md` the formula is
`m(ρ) = |tr_M(T_w)| [T1] + Σ Φ_q(|V_i|) [T2] + z² Σ Φ_q(|V_iV_j|) [T3]
+ m_e·τ(C_dimq) [T4] + a_K·C_K [T5] + Σ Res_ζ [T6]`:

| term | status for the solver `B_pred` |
|---|---|
| T1 `\|tr_M\|` | already wired (the current single-term cost) |
| **T2/T3** (brane tower — the **dominant** terms) | **PATHOLOGICAL at q₀.** The archimedean `Φ_q` specialisation is NOT Markov-invariant; `Φ_q(0.99) ≈ 6.7e5`, per-generator amplitudes blow up, tiny p/n asymmetries amplify ~1e5×, giving **T − ³He ≈ −737 MeV vs CODATA +0.019 MeV** (`brane-tower-isospin-diagnosis.witness.json`). Restoring T2/T3 trace-invariance at q₀ is an **OPEN derivation question** (PR #526; the binding-closure frontier — beans `z2bn`/`w5tg`/`thb7`). |
| T4 `(2+1/[2]_q)·m_e` | clean (derived + Lean `frobenius_codim_universal`); sub-dominant (~1.3 MeV) |
| T5 `tr_M(β·β*⁻¹)` | clean (Markov pairing); sub-dominant |
| T6 `Σ Res_ζ` | clean (cyclotomic); tiny at real q₀ |

**Verdict.** Wiring the *implementable* multi-term `B_pred` would make ³He (a mirror
nucleus, 2p+1n) ~1e5× **worse**, not fix the 57 % residual; the clean sub-dominant
T4/T5/T6 cannot close the ~4 MeV gap without T2/T3. So this bean is **gated on the
open T2/T3 trace-invariant reformulation**, not an isolated compute task — the ³He
57 % residual is a *symptom* of that frontier. **Do NOT wire the pathological Φ_q
T2/T3 into the solver.** Keep ³He frozen + documented (PR #2836). Re-open when the
binding-closure frontier resolves T2/T3 at q₀.
