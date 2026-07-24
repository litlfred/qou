# Week-review + workplan reconciliation — the Δ_λ covariance-kernel chain vs the 2026-07-24 landscape

**Date:** 2026-07-24 · **Scope:** reconcile the merged Δ_λ growth-bound → covariance-kernel chain
(this session's 9 PRs, 2026-07-18) with ~490 main commits + open siblings that landed since. No
new results — coordination only.

## What landed on main (last week, themes)

Heavy **Lean-proving** push, most of it adjacent to or supporting the Δ_λ / keystone frontier:

- **Argument-principle residue-sum engine — CLOSED sorry-free** (#4139/#4140): `argument_principle`
  + `entire_zero_count` via Mathlib `MeromorphicOn.extract_zeros_poles`. Unblocks the dilog /
  elliptic-divisor legs.
- **q-D-module symbol calculus (QDM-1..2) sorry-free**; **Specht/S_n formalization** program (epic
  `sp00`); **Markov-trace cyclicity** bricks (abstract `cyclic_of_gram_symm` #4110, inductive
  #4126); **Wenzl** rank-4 Wedderburn / semisimplicity (#4114); **dilog archimedean-limit** bricks.
- **Binding applications**: 6Li/4He/deuteron `B_gate` corrections (#4136/#4135/#4134), Δ_λ H3/H4
  resolution (#4132), Δ_λ q-dilog action (#4131).
- **Keystone multi-vector attack map** #4058 (7 coordinated vectors; V5 = Δ_λ closure, V7 = Lean
  carriers).

## How my merged chain slots in

My 2026-07-18 chain (all merged): (D)-reduction #3959 → super-exp growth bound + Lean #3939 →
covariance-kernel frontier + Lean infra #3998 → proof-epic Phase 1 (route elimination) #4008.

| my artifact | relationship to the landscape |
|---|---|
| `WstdSuperExpBound` growth bound → `k(A)=O(log A)` | the **GAP-A-3 magnitude leg** of Δ_λ — vector **V5** of #4058; upstream of the binding `B_gate` work (#4132/#4135/#4136) |
| covariance kernel `Cov(f^λ,Σc²)≤0` (open) | epic **`qou-x631`**; a Kerov-CLT-class problem |
| `YoungDiagramKernel.lean` (elementary S_n-free statement) + `DeltaLambdaDReduction` (sorry-free) | Lean **carrier** (vector V7); the *proof* would use the **Specht/S_n Lean infra of `sp00` / #4110 / #4114 / #4126** |

## Workplan update (beans)

- **`qou-x631`** (my epic) → **in-progress**; Phase 0+1 done (merged), Phase 2 = Śniady genus
  expansion, **now depends on the Specht Lean infra** (`sp00`, #4110/#4114/#4126) for any Lean
  proof. Recorded in the bean.
- **No duplication risk**: no sibling is working the *covariance kernel* itself; the Specht/Markov
  siblings build general S_n machinery (complementary, not overlapping). The Δ_λ siblings
  (#4131/#4132) work the *magnitude closure* downstream of my growth bound, not the growth bound.

## Next-session priority order (Phase 2)

1. **Literature check** — is `Cov_Planch(f^λ, Σc²) ≤ 0` (or the sign of `Σ_w χ^{sh(w)}(3-cycle)`) a
   known Fulman / Biane / Śniady result? If so, the kernel closes by citation.
2. If open: **genus-expansion attack** via the RSK form, coordinating with `sp00` for the Lean side.
3. Keep the growth-bound → V5 → binding-`B_gate` link visible so the magnitude-leg siblings can cite
   `k(A)=O(log A)` rather than re-derive it.

## Cross-references

- Epic bean: `qou-x631`; Specht epic: `sp00`; keystone map: #4058
- My merged chain: #3939, #3959, #3998, #4008 (audits under `docs/audits/2026-07-18-*deltalambda*`, `*wstd*`, `*covariance*`)
