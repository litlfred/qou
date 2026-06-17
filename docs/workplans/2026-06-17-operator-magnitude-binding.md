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
   feasibility (A=2,3,4). Note: #2403's O(r³) intertwiner already **cleared** its
   `r=64` λ⊢9 OOM bottleneck (the 4 affected λ now run ~50 s), where `r` is the
   combiner's **inner-tensor dimension** (#2403's "inner×block | r" table) —
   **not** `dim(V_λ⊢9)`, whose max is 216 (at `(4,3,1,1)`,`(4,2,2,1)`); the four
   `r=64` λ have `dim = 168/216`. So feasibility looks favourable for A≤4. [running]
2. **Coordinate** with the sibling PR that owns the kernel (`wenzl-a3-intertwiner-or3`)
   — post intent; the kernel is not yet on main.
3. **Resolve the key question** — is an operator-magnitude binding formula
   defined or must it be constructed? Record honestly.
4. **If defined + tractable:** evaluate it for D/T/³He/⁴He; does it track AME
   where the scalar failed? Derive-or-refute.
5. **Fallback:** if the operator route needs unbuilt construction, scope the
   **α-cluster recursion** (⁴He magic input) as the other sanctioned non-fit
   direction.

## Status — triage complete: a research-level open, NOT a wiring

- **`A^λ_{ξν}(I)` entry point:**
  `computations/a_operator/a_operator_recursive.py::interface_blocks(lam, n_inner,
  n_block, q_str, d_coef)` → `{(ξ,ν): {A, c, d_μ, d_ν}}`. On sibling `f393badec0`
  (**not** on main); self-contained (no Rust dep); runs **A≤4 (H₁₂)** at
  ~0.01–0.02 s/partition. **Feasibility favourable for A≤4** (the OOM wall is the
  combiner inner-dim `r`, already cleared — see §Plan 1, not `dim(V_λ)`).
- **Confirmed (the gating question, answered):** `A^λ_{ξν}(I)` is a χ^λ
  **reconstruction** kernel (same `tr_M`, faster route), **NOT a binding
  magnitude**. So an operator-magnitude *binding functional* must be
  **constructed**, not wired.
- **Candidates exist but no formula:** `2026-05-17-structural-diagnosis-operator-valued.md`
  floated `‖A^λ_{ξν}(I)‖_F` / `Tr[A^λ_{ξν}(I)]` (and found the operator correction's
  Frobenius norm 3.603 > scalar 3.517 — non-scalar blocks matter for χ^λ). But
  **no binding formula is defined**, and choosing among norm/trace variants to
  match AME is a **fit-risk** — the same trap as the refuted scalar variants,
  with more knobs.
- **A-scaling caveat (decisive):** the operator binding is still the **linear**
  functional `Σ_λ y_λ χ^λ A^op`; its entries grow with A (like `dim`), so it
  likely **inherits the #2417 divergence** unless the functional specifically
  tames the growth. The functional with correct A-scaling is the **log** one
  (`B_sym`). The operator route does **not** automatically fix this.
- **α-cluster fallback:** all in `computations/_deprecated/` — needs
  reconstruction.

**Verdict.** Both sanctioned directions (operator-magnitude *construction*;
α-cluster *revival*) are research-level opens requiring substantial new build;
the most direct operator path (norm/trace) is fit-risk **and** likely inherits
the A-scaling failure. There is **no ready-to-wire component**. Disciplined
recommendation: do **not** run a norm/trace fit-search (rainbow-chasing). The
genuine non-fit paths are (a) a **principled** operator-magnitude *derivation*
that provably fixes the linear-functional A-scaling, or (b) reviving the
**α-cluster recursion** (⁴He magic input, #1706-sanctioned), or (c) **parking**
with the gate now precisely characterized (which is itself a complete, honest
outcome of the LP→quadratic→Bring→chirality→magnitude→operator arc). Owner call.
