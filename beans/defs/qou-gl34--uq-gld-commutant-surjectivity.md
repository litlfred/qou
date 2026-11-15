---
# qou-gl34
title: 'G3.4: V^{⊗n} = ⊕ W_λ ⊗ S_λ and ρ(H) = End_{U_q(gl_d)}(V^{⊗n}) — the hard direction'
status: todo
type: task
priority: normal
tags:
    - quark-state
    - schur-weyl
created_at: 2026-11-15T10:10:00Z
updated_at: 2026-11-15T11:45:00Z
parent: qou-gld3
---

Needs: (i) complete reducibility of V^{⊗n} under U' = ⟨K, E, F⟩ at generic q; (ii) dim HW_λ = f^λ; then dim End_{U'} ≤ Σ_{ℓ(λ)≤d} (f^λ)² = dim ρ(H) (JimboGL.finrank_range_jimbo) gives equality. Mathlib has no quantum-group highest-weight theory and no complete reducibility for it. Feasibility flag: research-scale formalisation (weeks), not PR-sized. Possible shortcuts to weigh: q-Schur algebra (Dipper–James), or a dimension bound from the weight-space decomposition plus HW_λ ≅ S_λ.

Owner ruling 2026-11-15 ("G3: add infra"): build the highest-weight theory that Mathlib lacks, in PR-sized pieces.

2026-11-15 (q-Schur sibling, PR #7864): scoping done. Mathlib has no bicommutant or Jacobson density, and the Dipper–James/Du/Green generation proof would take weeks, so that route is not recommended. Cheaper route: lowerOp = raiseOpᵀ ⇒ B is transpose-closed ⇒ complete reducibility over an ordered field; V = B·N; dim B' ≤ Σ(dim N_μ)². G3.4 then reduces to (★): N_μ = 0 for non-dominant μ, dim N_λ ≤ f^λ (7a). P1–P3 are about 3 PRs, pending the coordinator's go. Still open.

2026-11-15 (PR #7864, merged on owner decision "Merge now, scoped wording"): `QuantumGLCommutant.range_jimbo_eq_commutant` proves, over a linearly ordered field with q not a root of unity and with no hypothesis left ((★) = `hstar_occWeights`, #7873), that the Jimbo image of H_{m+1}(q) equals the commutant of `uqGens` = {E_i = raiseOp, lowerOp, Cartan elements, weight projectors}. Verified by the old Stream 14 session: library sweep 217/217, `lean -DautoImplicit=false -s 65536` exit 0, axioms propext/Classical.choice/Quot.sound only, no sorry. STILL OPEN before it may be called the U_q(gl_d) commutant (do not close this bean on #7864): (1) weight projectors are polynomials in the Cartan elements at generic q; (2) lowerOp vs the standard Δ(F) of U_q(gl_d) (expected: a Cartan factor times F, unchecked); (3) optional, Stream 16: drop the ordered-field hypothesis (only isCompl_dotPerp uses it). Citation for the U_q(gl_n) → q-Schur surjectivity side: Du 1995 (uploads/weylweb.pdf, not yet ingested).

## 2026-11-15 follow-up 1 done (session_01Qmmkt9G83BWVJD2uM6cPfq, owner "1y")
`QOU/SchurWeyl/QuantumGLCartanProj.lean`: `weightProj_mem_adjoin_cartan` (any field, q ≠ 0 not a root of unity: weightProj μ = ∏_x ∏_{t≤n, t≠μx} (q^{μx}−q^t)⁻¹(K_x − q^t)); `commutant_uqGens_eq_cartan`; `range_jimbo_eq_commutant_cartan` (G3.4 for {E_i, lowerOp, Cartan}, ordered field). lean-direct exit 0; axioms propext/choice/Quot.sound. Remaining: follow-up 2 (lowerOp vs Δ(F)) and the any-field extension (#7874).

## 2026-11-15 follow-up 2 done (session_01Qmmkt9G83BWVJD2uM6cPfq, owner "Prove it in Lean, one PR")
`QOU/SchurWeyl/QuantumGLJantzen.lean`, Jantzen's coproduct Δ(E)=E⊗1+K⊗E, Δ(F)=F⊗K⁻¹+1⊗F, Δ(K)=K⊗K (Lectures on Quantum Groups §3.1), any `CommRing`, q·qi=1, every d, n: `raiseOp_eq_jDelta` (raiseOp i = Δ⁽ⁿ⁾(F_i) exactly); `lowerOp_eq_smul_cartan_mul_jDelta` (lowerOp i = q·Δ⁽ⁿ⁾(K_i)⁻¹·Δ⁽ⁿ⁾(E_i)); `jDelta_E_eq` (converse). So {raiseOp, lowerOp, cartan} and the iterated Jantzen images of {E_i, F_i, K_i^{±1}} generate the same algebra: item (2) is closed. NAMING: `raiseOp` sends e_i ↦ e_{i+1}, lowering the weight, so it is the standard F_i, not E_i as the entry above says; `lowerOp` is E_i up to the Cartan factor. Checked first exactly in sympy over ℚ(q) (d=2,3; n=2,3; every i). lean-direct `-DautoImplicit=false -s 65536` exit 0; axioms propext/Classical.choice/Quot.sound. Remaining: (3) and the any-field extension (#7874).
