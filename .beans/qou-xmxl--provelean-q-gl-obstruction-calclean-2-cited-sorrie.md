---
# qou-xmxl
title: 'PROVE(lean): q_gl_obstruction_calc.lean — 2 cited sorries [cited manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
created_at: 2026-08-01T23:31:09Z
updated_at: 2026-08-01T23:31:09Z
parent: qou-k1mq
---

**File:** `QOU/q_gl_obstruction_calc.lean` (QOU)  ·  2 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/q_gl_obstruction_calc.lean

### `q_gl_obstruction_calc`  —  line 111  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem q_gl_obstruction_calc (ctx : QGlObstructionCalcContext) : (¬ ctx.kappa_zero → ctx.F_intr ≠ 0) ∧ (ctx.q_flat ↔ ctx.R_connection = 0) ∧ (∀ n : ℕ, 1 ≤ n → (ctx.kappa_vanishes n ↔ (n : ℤ) ∣ ctx.chi_A)) ∧ (∀ N : ℕ, ∃ n : ℕ, N < n ∧ ¬ ((n : ℤ) ∣ ctx.chi_A) ∧ ¬ ctx.kappa_vanishes n) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] quantum-observable-universe/q-geometric-langlands/q-gl-obstruction-calc.ts
  - [manuscript] prop:q-gl-obstruction-calc
- **Tractability:** Obstruction calculus: curvature/flatness/divisibility/period equivalences over context; repo categorical infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

### `q_gl_obstruction_calc`  —  line 116  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem q_gl_obstruction_calc (ctx : QGlObstructionCalcContext) : (¬ ctx.kappa_zero → ctx.F_intr ≠ 0) ∧ (ctx.q_flat ↔ ctx.R_connection = 0) ∧ (∀ n : ℕ, 1 ≤ n → (ctx.kappa_vanishes n ↔ (n : ℤ) ∣ ctx.chi_A)) ∧ (∀ N : ℕ, ∃ n : ℕ, N < n ∧ ¬ ((n : ℤ) ∣ ctx.chi_A) ∧ ¬ ctx.kappa_vanishes n) `
- **Cited:** `[manuscript]`, `[manuscript]`, `[manuscript]`
  - [manuscript] quantum-observable-universe/q-geometric-langlands/q-gl-obstruction-calc.ts
  - [manuscript] prop:q-gl-obstruction-calc
- **Tractability:** Second conjunct of the q-GL obstruction calculation (same context theorem, distinct goal); repo categorical infra.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.
