---
# qou-cvru
title: 'C-5a: does the R-matrix obstruction share the Kummer zero set? (open)'
status: todo
type: task
priority: normal
created_at: 2026-11-15T17:35:00Z
updated_at: 2026-11-15T17:35:00Z
parent: qou-lx8f
---

Open conjecture-level question (keep open per AGENTS §13a). The owner chose
"keep open, scope it" on 2026-11-15. Issue litlfred/qou#7935, PR #7936.

**Question.** C-5 defines κ_n = tr_M(Ř_(n+1) − L₋₁Ř_(n)). Does it vanish
exactly for n | 6, the zero set of the Kummer obstruction χ mod n with χ = −6?

**Proved (PR #7936, `QOU/MathlibExt/KummerObstruction.lean`, sorry-free):**
- `bring_kummerObstruction_eq_zero_iff`: χ mod n = 0 iff n ∣ 6.
- `addMonoidHom_zmod_eq_zero`: every additive map ℤ/n → torsion-free group is 0.
  So the trace (in ℚ(q)) can share the zero set at most. It cannot be the
  class. This is a scope-(b) exclusion for "image under a homomorphism";
  the invariant is torsion-freeness.
- `kappa_eq_sub`: by J-3, κ_n = tr⁽ⁿ⁺¹⁾(Ř') − tr⁽ⁿ⁾(Ř).
- `kappa_eq_zero_of_descended`: κ_n = 0 if Ř' = ℓ_n Ř (e.g. Ř = σᵢ).
- `transient_eq_zero_of_surjective`: the JC-4 (1 − τ̂) form is 0 for every Ř'
  when ℓ_n is onto. Under J-1, ℓ_n is onto at fixed strand count.
- `kummerObstruction_eq_trace_id_mod` (route R1): the Kummer class equals
  tr_M(id) mod n, with C-4b as a hypothesis.

**Blocker.** Ř⁽ⁿ⁾ is defined nowhere, and the brane tower is a jet tower, not a
strand tower. With the relations as written, κ_n ≡ 0.

**Routes** (doc: /mnt/project-files/qou-leftovers/c5a-gap-routes.md):
- R1: done on #7936.
- R2: define a non-jet-image Ř⁽ⁿ⁾, fixed BEFORE computing (anti-fit).
- R3: the gerbe layer, qou-skn4 G1–G2, plus Ȟ²(S, μ_n) ≅ ℤ/n.
