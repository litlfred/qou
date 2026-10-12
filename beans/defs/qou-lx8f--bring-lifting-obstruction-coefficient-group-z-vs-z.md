---
# qou-lx8f
title: 'Bring lifting obstruction: coefficient group (Z vs Z/2 vs O^x) and the Bring-specific vanishing claim'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T19:14:41Z
updated_at: 2026-10-12T19:14:41Z
parent: qou-vo9t
---

## Question
The brane-tower lifting obstruction kappa_n on Bring's surface Sigma_4 is written with three different coefficient groups in the corpus:
- **Z**: the Euler class e(xi) = -6 in H^2(Sigma_4, Z) (fluid-dynamics/ns-obstruction-*.md). Also the `persistence` field and `perpetual_obstruction` in lifting-and-descent/yekutieli-lifting.lean.
- **Z/2 = centre(SU_q(2))**: QOU/BringsSurface.lean `yekutieli_lifting`. Its docstring falsely said H^2(Sigma_4, Z/2) = 0; corrected in PR #7747.
- **O_M^x**: yekutieli-lifting.md and the archimedean band.

## The tension
-6 is nonzero in H^2(Sigma_4, Z) = Z, but -6 = 0 mod 2. So "the obstruction persists" (Z) and "the obstruction vanishes" (Z/2) can both be true of the same Euler class under different coefficient groups. The two readings imply opposite answers to "does the tower lift on Bring?".

## Facts already true
- H^2(Sigma_g, Z/2) = Z/2 and H^2(Sigma_g, Z) = Z for a closed orientable surface.
- w_2(T Sigma_g) = chi mod 2 = 0, so every closed orientable surface is spin; for Bring, chi = -6.

## To do
1. Identify which bundle or gerbe the tower lifts, and its band (corpus-grep is running).
2. Formalize (sorry-free) the reduction-mod-2 statement: the mod-2 image of an even Euler class vanishes.
3. Report which reading the corpus actually supports; do not choose one by fit.

## 2026-10-12: six-path corpus check (corpus-grepper) plus own verification

**Six coefficient groups, not three:** ℤ (Euler class), ℤ/2 (BringsSurface), 𝒪_M^× (yekutieli-lifting.md and others), 𝔾_m (Kummer blocks), Z(Aut A_n) (brings-is-qou-proof.md), and HH²(U_q, Ad) ≅ ℤ (qou_obstruction_reduction.lean). **The band 𝓑 is defined nowhere.** No file identifies which bundle or gerbe the tower lifts.

**The 𝒪^× band kills the obstruction on any surface (scope b; proved invariant: the exponential sequence).**
- 0 → ℤ → 𝒪 → 𝒪^× → 0 gives H²(Σ, 𝒪) → H²(Σ, 𝒪^×) → H³(Σ, ℤ). Both ends are 0 on a compact Riemann surface; for smooth 𝒪, the sheaf is fine and H²(𝒪) = 0 as well.
- So H²(Σ₄, 𝒪^×) = 0, and every κ_n vanishes under that band. This contradicts the "perpetual obstruction" (`persistence` field).
- The ℤ-valued κ₀ = e = −6 cannot live in H²(𝒪^×). It is naturally an element of H²(Σ, ℤ) ≅ ℤ, which receives Pic = H¹(Σ, 𝒪^×) via c₁ — one degree lower than H²(𝒪^×). The corpus mixes the degree.
- Also: `yekutieli-lifting-su2.md` writes H²(ℂP¹, 𝒪^×) ≅ H²(ℂP¹, ℤ) ≅ ℤ. Wrong: it is 0; the ℤ is Pic = H¹(𝒪^×).
- Also: `ns-obstruction-computation.md:30` says Bring "possesses real dimension 4"; it is 2.
These are corpus-content corrections and wait on the owner (AGENTS.md §ASK THE OWNER). Tracked in bean qou-v1np.

**ℤ vs ℤ/2.**
- For an oriented surface bundle, w₂ = e mod 2. For Bring's tangent bundle, e = χ = −6, so w₂ = 0 and Bring is spin.
- The bridge in the held source is Yekutieli 2010 `exa:27`: a central extension of sheaves of groups gives a central extension of torsor gerbes. With ℤ/2 → Spin → SO, that is exactly the w₂ lifting problem. No corpus file cites it.
- Mathlib has no Stiefel–Whitney or Euler classes, so "w₂ = χ mod 2" cannot yet be stated meaningfully in Lean. A bare `(-6) % 2 = 0` lemma would be integer arithmetic dressed as cohomology and is deliberately NOT added; `PNeqNpEquivalence.chi_mod_vanishes_iff` already covers the arithmetic.

**κ₀ = Euler class** is asserted (thm:qu-to-qou item 2; "via the Gysin sequence") and is a structure field in every Lean file. It is never derived.

**Theorem hypothesis dropped.** Yekutieli Thm 4.17 assumes the obstruction class "is defined". The corpus drops that everywhere.

**Status:** the coefficient question is answered *negatively*. The corpus has no consistent band, and the 𝒪^× reading makes the obstruction identically zero on Bring. The live Bring-specific question is therefore "which band", not "does it vanish". That is an owner decision about the framework's definition of 𝓑. Bean stays open.
