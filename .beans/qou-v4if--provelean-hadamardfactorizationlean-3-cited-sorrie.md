---
# qou-v4if
title: 'PROVE(lean): HadamardFactorization.lean — 3 cited sorries [cited manuscript]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - repo-infra
    - tractable
created_at: 2026-08-01T23:31:06Z
updated_at: 2026-08-01T23:31:06Z
parent: qou-k1mq
---

**File:** `QOU/Mathlib/HadamardFactorization.lean` (QOU)  ·  3 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/Mathlib/HadamardFactorization.lean

### `norm_one_sub_weierstrassFactor_le`  —  line 134  ·  tier **T** (tractable-in-Mathlib-today)
- **Proposition:** `theorem norm_one_sub_weierstrassFactor_le (p : ℕ) {z : ℂ} (hz : ‖z‖ ≤ 1) : ‖1 - weierstrassFactor p z‖ ≤ ‖z‖ ^ (p + 1) `
- **Cited:** `[manuscript]`
  - [manuscript] Ahlfors
- **Tractability:** Elementary bound ‖1 − weierstrassFactor p z‖ ≤ ‖z‖^{p+1} for ‖z‖≤1; concrete complex-analysis inequality, Mathlib ingredients suffice.
- **Next step:** Formalize now — Mathlib ingredients exist. Prove the stated goal directly, keep sorry-free.

### `multipliable_canonicalProduct`  —  line 144  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem multipliable_canonicalProduct {a : ℕ → ℂ} (p : ℕ) (ha : ∀ n, a n ≠ 0) (hsum : Summable (fun n => 1 / ‖a n‖ ^ (p + 1))) (z : ℂ) : Multipliable (fun n => weierstrassFactor p (z / a n)) `
- **Cited:** `[manuscript]`, `[manuscript]`
  - [manuscript] Ahlfors
- **Tractability:** Multipliability of the canonical Weierstrass product; Mathlib has Multipliable + the summability hypothesis is given — needs the tail estimate wired to L134.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

### `hadamard_factorization`  —  line 170  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem hadamard_factorization {f : ℂ → ℂ} {ρ : ℝ} (hf : IsEntireOfOrderLE f ρ) (hf0 : f 0 ≠ 0) : ∃ (p : ℕ) (g : Polynomial ℂ) (a : ℕ → ℂ), (p : ℝ) ≤ ρ ∧ (g.natDegree : ℝ) ≤ ρ ∧ (∀ n, a n ≠ 0) ∧ (∀ n, f (a n) = 0) ∧ (∀ z, Multipliable (fun n => weierstrassFactor p (z / a n)) ∧ f z = Complex.exp (g.e`
- **Cited:** `[manuscript]`
  - [manuscript] Ahlfors
- **Tractability:** Full Hadamard factorization theorem for entire functions of finite order; not in Mathlib.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.
