# Operator-magnitude binding — replacing the refuted scalar Δ_λ (workplan, 2026-06-17)

**Branch:** `claude/operator-magnitude-binding-2026-06-17`
**Picks up:** the #2417 verdict — every *scalar* per-block magnitude in
`B = m_e·|Σ_{λ⊢3A} y_λ χ^λ Δ_λ|` fails (trace decays for `Δ_λ∈{1,sgn}`, diverges
for `{dim,dim_q}`); the *linear* functional is refuted at the **A-scaling** level.
**Discipline:** derive-or-refute; no fit, no production rewire until validated.

## Motivation (why operator, not scalar)

#2417 established: sign = chirality (proved/closed); but **no scalar magnitude**
`w_λ` makes `Σ_λ y_λ χ^λ w_λ` track AME's ~linear-in-A binding. The only
structurally-open direction is an **operator-valued** per-block factor — the
sibling **`A^λ_{ξν}(I)`** combiner (branch `wenzl-a3-intertwiner-or3`,
"the A≥4 unlock"), which reconstructs
`χ^λ(β_in·I·β_out) = Σ_{ξ,ν} Tr[A^λ_{ξν}(I)·(ρ_ξ(β_in)⊗ρ_ν(β_out))]`.

## The KEY open question (gates the whole build)

`A^λ_{ξν}(I)` is, as landed, a **χ^λ reconstruction kernel** (a faster route to
the *same* trace), **not** a binding magnitude. So the premise "use the operator
combiner as the binding weight" may require **constructing** an
operator-magnitude binding functional, not just wiring an existing one. The
triage resolves: is there a defined operator-valued `Δ_λ` (e.g. a norm/trace of
the interface operator `A^λ_{ξν}(I)`) that grows ~linearly in A — or does it
need to be built (and is that a fit risk)?

## Plan

1. **Triage** the `A^λ_{ξν}(I)` API + the `a_operator_gauge_align` infra +
   feasibility (A=2,3,4 vs the r=64 λ⊢9 OOM wall). [running]
2. **Coordinate** with the sibling PR that owns the kernel (`wenzl-a3-intertwiner-or3`)
   — post intent; the kernel is not yet on main.
3. **Resolve the key question** — is an operator-magnitude binding formula
   defined or must it be constructed? Record honestly.
4. **If defined + tractable:** evaluate it for D/T/³He/⁴He; does it track AME
   where the scalar failed? Derive-or-refute.
5. **Fallback:** if the operator route needs unbuilt construction, scope the
   **α-cluster recursion** (⁴He magic input) as the other sanctioned non-fit
   direction.

## Status

Opened; triage running. Findings + the resolved scope below as they land.
