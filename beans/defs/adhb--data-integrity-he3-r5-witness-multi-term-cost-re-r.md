---
# adhb
title: 'Data-integrity: He3 R5 witness multi-term-cost re-run (regen winner diverged)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-26T03:39:52Z
updated_at: 2026-10-04T15:18:35Z
parent: qou-5vkl
---

## 2026-06-30 — "wire Term-5 into R5" is a FIT; DO NOT do it. Stays research-grade.

A no-fit provenance check (gating a proposed Term-5 wiring) returned **FITTED**:
`Term 5 = a_K·B_bulk`, and `B_bulk` (`bw_chirality_isotopes.py:100-109`) is the literal
Bethe–Weizsäcker liquid-drop formula whose coefficients (λ_V,λ_S,a_asym,δ_P) are q-integer
products **matched to the historically AME-fitted BW values** (0.2–2.1%; source block
`conj:q-integer-mass-formula` has a column literally labeled "Fitted (MeV)", Lean not_checked).
**Do NOT add `a_K·B_bulk` to `cost_for_candidate` in `r5_full_canonical_knot_solver.py`** — it
would make the canonical solver's binding a BW fit dressed as a derivation.

The fit-free chirality is a DIFFERENT object — the dashboard `B_qCLT_fac`
(`mass_binding_dashboard.py:269`, `B_chir = α·(A−1)·(L̄−L_pn)`, only q₀+m_e+Markov trace) — but
even it doesn't close adhb: under-binds ⁴He ~2.4×, and the deuteron stays blocked (`6₂`
PSD-infeasible, `tr_M(β_D)≡0`; needs the H₆ binding-operator search, `conj:canonical-knot-id-sdp`
leg b). adhb remains research-grade. Audit: `docs/audits/2026-06-30-adhb-term5-bw-fit-do-not-wire.md`.

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
- Lean: `folio/quantum-observable-universe/lean/QOU/BraidKnot/Helium3Witness.lean`
  (*Witness divergence* note)
- Producer: `computations/r5_full_canonical_knot_solver.py` — `cost_for_candidate`
  uses single-term `B_pred = ρ · m_e · |tr_M|` (line ~491)
- Sibling root cause: deuteron same single-term-cost under-constraint (audit §2)

## SCOPE (2026-06-26) — BLOCKED: research-gated, NOT a clean wire-up

Grounding the "multi-term-cost re-run" found it is **gated on an open derivation
question**, not a straightforward implementation. Per
`folio/quantum-observable-universe/mass-theory/six-term-mass-formula-complete.md`
the formula is
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
