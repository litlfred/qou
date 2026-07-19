---
# qou-2fdj
title: 'F3: Δ_λ binding closure — non-dup formalize-first slice (scoping agent running). Swarm-owned: PRs #3808/#3802/#4006. Jet-filtration graded-dim derivation route (owner-opened 2026-07-13); anti-fit stands.'
status: in-progress
type: task
priority: normal
created_at: 2026-07-19T00:42:34Z
updated_at: 2026-07-19T00:46:18Z
---


## Refined scope (scoping agent, 2026-07-19) — UNOWNED, best-fit
The whole Δ_λ growth bound reduces (via merged #3959 D-reduction → #3939) to ONE open sorry:
`QOU/BraidsAndKnots/YoungDiagramKernel.lean:69  covariance_kernel_conjecture (k) : kernelValue k ≤ 0 := sorry`
Equivalent: T₃ = Σ_{λ⊢k} (f^λ)² χ^λ(3-cycle) ≤ 0  ⇔  Cov_Planch(f^λ,R₄) ≤ 0  ⇔  Σ_{λ⊢k}(f^λ)³(Σ_□c(□)²−C(k,2)) ≤ 0.
`DeltaLambdaDReduction.lean::D_of_T3_nonpos` is sorry-free (chain from T₃≤0 to growth bound done).
Positive control kernelValue 3,4,5 = −4,−16,−320; numeric k≤40.
Bounded first commit: formalize Kerov reduction Σ̂₃(λ)=R₄(λ)+R₂(λ) + E_Planch[R₄]=−k as sorry-free lemmas over existing List ℕ machinery (contentSq/hookProd/sytDim). Then two-extreme-shapes SOS split (row/col each +1; balanced bulk C₂<C(k,2) dominates negative).
CAVEAT: full ∀k is research-grade (Biane–Śniady/Kerov CLT) — do NOT promise the whole sorry.
Non-dup: no open PR touches the character-sum kernel (#3808 envelope, #3802 PSD, #4006 icosahedral-m are different objects). Branch: claude/deltalambda-covariance-kernel-sos-2026-07-19.
