import Mathlib.Algebra.Group.Subgroup.Basic
import Mathlib.Algebra.Group.Center
import Mathlib.GroupTheory.Subgroup.Center

/-!
# In a crossed module the 2-holonomy is its boundary 1-holonomy up to a central element

Check C1 of the 2026-09-05 binding-gap survey (route D's first prune, bean `qou-20bk`). The
survey's §4.4 guessed that Yekutieli's 2-dimensional multiplicative integral is "structurally
pair-local" *because* every kite is tethered to the basepoint. Read against the held text
(`library/arxiv-1007.1250v4`, Def. 4.1.1, 4.3.3, 4.4.16; Thm 0.4.2 and 0.9.1), the tether is a
gauge choice; the mechanism is the **2-dimensional Stokes theorem**: for a connection–curvature
pair (fake-flat), `Φ(MI(α,β|σ,τ)) = MI(α|∂(σ,τ))` — the surface holonomy `h ∈ H` maps under the
feedback `Φ : H → G` to the boundary path holonomy `g ∈ G`.

This file records the group-theoretic core, which needs nothing from geometry: in a crossed
module `(G, H, Φ, Ψ)` the kernel of the feedback is **central** in `H` (a consequence of the
Peiffer identity), so any two elements of `H` with the same image under `Φ` differ by a central
element. Read back into the geometry:

* the **non-abelian** content of a 2-holonomy is entirely its boundary 1-holonomy — a
  path-ordered product, i.e. *word/ordering* data, the degree-0 class the survey's §7b–7d already
  characterised;
* everything beyond it lives in `ker Φ` (Yekutieli's inertia subgroup `H₀`), which is abelian and
  central — and the 3-dimensional Stokes theorem (Thm 8.6.6) says that on the boundary of a
  balloon this remainder is the *abelian* integral of the inert 3-curvature `γ`.

So no 2-dimensional Yekutieli object carries a non-abelian many-body term beyond word ordering,
and the only 3-body-shaped object in the book is the abelian volume term `∫γ` over a 3-cell — which
is additive over 3-cells (extensive), exactly the "super-pairwise additive extensive object" the
Δ_λ audit asks for, **if** `γ ≠ 0` for the framework's connection. That last condition cannot be
evaluated: the framework's Step-2 curvature is stipulated, not a form (cheat-sheet §2a). Recorded
in the survey §7e; this file proves only the algebra.

Base ring §7c: none — pure group theory over arbitrary `Group G`, `Group H`.

-- Ref: [yekutieli2015] https://arxiv.org/abs/1007.1250 — Thm 0.4.2 (2-dim Stokes), Thm 0.9.1
--      (fundamental relation `Ψ(g) = Ad_H(h)`), §0.5 (inertia subgroup `H₀ = ker Φ`, central).
-- Ref: [leitner2026] docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md §7e
-/

namespace QOU.LiftingDescent.CrossedModuleSurfaceHolonomy

/-- A crossed module `(G, H, Φ, Ψ)`: a group homomorphism `Φ : H → G` (the *feedback*), an action
`Ψ` of `G` on `H` by automorphisms (the *twisting*), such that `Φ` is `G`-equivariant and the
Peiffer identity `Ψ(Φ h) h' = h h' h⁻¹` holds. -/
structure CrossedModule (G H : Type*) [Group G] [Group H] where
  /-- The feedback `Φ : H → G`. -/
  Φ : H →* G
  /-- The twisting `Ψ : G → Aut(H)`. -/
  Ψ : G →* MulAut H
  /-- `Φ` is `G`-equivariant for the conjugation action on `G`. -/
  equivariant : ∀ (g : G) (h : H), Φ (Ψ g h) = g * Φ h * g⁻¹
  /-- The Peiffer identity `Ψ(Φ h) = Ad_H(h)`. -/
  peiffer : ∀ h h' : H, Ψ (Φ h) h' = h * h' * h⁻¹

variable {G H : Type*} [Group G] [Group H] (C : CrossedModule G H)

/-- **The inertia subgroup is central.** In any crossed module, `ker Φ ≤ Z(H)`: for `k` with
`Φ k = 1` the Peiffer identity reads `h' = k h' k⁻¹`. -/
theorem ker_le_center : C.Φ.ker ≤ Subgroup.center H := by
  intro k hk
  rw [Subgroup.mem_center_iff]
  intro h'
  have hP := C.peiffer k h'
  rw [MonoidHom.mem_ker.mp hk, map_one, MulAut.one_apply] at hP
  -- hP : h' = k * h' * k⁻¹
  calc h' * k = k * h' * k⁻¹ * k := by rw [← hP]
    _ = k * h' := inv_mul_cancel_right (k * h') k


/-- **A surface holonomy is its boundary holonomy up to a central element.** If two elements of
`H` have the same image under the feedback (as the 2-dim Stokes theorem forces for two
2-holonomies over surfaces with the same boundary path), they differ by an element of `Z(H)`. -/
theorem eq_mul_center_of_feedback_eq {h h' : H} (hΦ : C.Φ h = C.Φ h') :
    h' * h⁻¹ ∈ Subgroup.center H := by
  apply ker_le_center C
  rw [MonoidHom.mem_ker, map_mul, map_inv, hΦ, mul_inv_cancel]

/-- The same statement with the central factor made explicit:
`h' = z * h` for some central `z`. -/
theorem exists_center_mul_of_feedback_eq {h h' : H} (hΦ : C.Φ h = C.Φ h') :
    ∃ z ∈ Subgroup.center H, h' = z * h :=
  ⟨h' * h⁻¹, eq_mul_center_of_feedback_eq C hΦ, (inv_mul_cancel_right h' h).symm⟩

/-- **The fundamental relation, one direction.** Writing `g := Φ h` for a surface holonomy `h`,
the twisting by the boundary holonomy is conjugation by the surface holonomy:
`Ψ(g) = Ad_H(h)` (Yekutieli Thm 0.9.1, here immediate from Peiffer). -/
theorem twist_boundary_eq_conj (h h' : H) : C.Ψ (C.Φ h) h' = h * h' * h⁻¹ :=
  C.peiffer h h'

/-- **Consequence for any conjugation-invariant reading.** A class function `f : H → R` (one
that cannot see conjugation) evaluated on a surface holonomy is determined by the boundary path
holonomy *only through* the central factor: if `f` is also invariant under multiplication by
central elements, then `f` is a function of `Φ h` alone. This is the precise sense in which a
2-dimensional multiplicative integral carries no non-abelian content beyond its boundary. -/
theorem classFn_factors_through_feedback {R : Type*} (f : H → R)
    (hf : ∀ z ∈ Subgroup.center H, ∀ h, f (z * h) = f h)
    {h h' : H} (hΦ : C.Φ h = C.Φ h') : f h = f h' := by
  obtain ⟨z, hz, rfl⟩ := exists_center_mul_of_feedback_eq C hΦ
  exact (hf z hz h).symm

end QOU.LiftingDescent.CrossedModuleSurfaceHolonomy
