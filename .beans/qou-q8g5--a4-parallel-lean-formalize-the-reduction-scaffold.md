---
# qou-q8g5
title: 'A4 (parallel): Lean-formalize the reduction scaffold (tau3=3/n eigenfn, Dirichlet id, Var=|C3|)'
status: todo
type: task
priority: normal
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T03:31:40Z
parent: qou-v8t7
---

## A4 — Lean-formalize the reduction scaffold (parallel; achievable now via lean-lsp)
IDEA. Lean-prove the EXACT reduction facts (independent of the open sign) to harden the conditional
structure and make 'what remains' machine-precise:
  (i)  Var_P(ω₃) = n(n−1)(n−2)/3  (= |C_3|, 3-cycle class size) — finite-sum identity;
  (ii) ω₃ eigenfunction of the down-up chain, eigenvalue 1−3/n (per-n decidable / #eval-checked);
  (iii) Dirichlet identity ℰ(f,ω₃) = (3/n)·⟨f,ω₃⟩_P;
  (iv) transfer decomposition g(1)=g'(0)+R (algebraic).
FIRST STEP. Extend content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernel.lean:
add `varOmega3 (k)` and a sorry-free lemma `varOmega3 k = k*(k-1)*(k-2)/3` (elementary), verified via
lean-lsp lean_goal/lean_multi_attempt against restored oleans. Then the τ₃=3/n eigenvalue as a
per-partition #eval control.
SUCCESS. Sorry-free scaffold lemmas landed.
NOTE. Does NOT close the kernel (infrastructure). Cheapest concrete win; do in parallel with A2.
