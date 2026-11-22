/-
  H4-5c-ii (partial): THE Λ-SUM — three disjoint wedges, and Milnor's
  configuration.

      H4-5b    Vol(chimney (wedge R ψ) R)     =  Λ(ψ)
      H4-5c-i  Vol(chimney (wedgeAt R θ ψ) R) =  Λ(ψ)        any axis
      HERE     Vol(chimney (W₁ ∪ W₂ ∪ W₃) R)  =  Λ(α)+Λ(β)+Λ(γ)

  **This is the first statement in the tier with `Λ(α)+Λ(β)+Λ(γ)` on the
  right** — the shape of Milnor's theorem.  It is stated for the explicit
  union of the three wedges of his circumcentre subdivision, at the axes and
  half-angles his construction produces from a triangle with inscribed angles
  `(α, β, γ)`.

  WHAT WAS STILL OPEN HERE, AND IT WAS EXACTLY ONE THING: that this union
  **is** the inscribed triangle.  `milnorWedges` is a union of three
  explicitly-described regions, not a triangle, and nothing in THIS file says
  otherwise.  That step — H4-5c-ii(b) — is now **proved**, in
  `QOU.Archimedean.OrthoschemeTiling`
  (`milnorWedges_ae_eq_inscribedTriangle`, and the Λ-sum restated on the
  triangle as `hypVolume_chimney_inscribedTriangle`).  The scope section at the
  bottom of this file records what that did and did not settle.

  THE DISJOINTNESS IS ALGEBRAIC, NOT ANGULAR — this is the technical point of
  the file, and it is what made the step tractable.  The obvious route is to
  read off each wedge's angular interval and show the intervals are disjoint
  mod `2π`; that drags in `arctan`, branch choices, and modular arithmetic on
  angles.  Instead, `inner_perp_rotL` gives the identity

      ⟨rot_θ v , (−sin(θ+ψ), cos(θ+ψ))⟩  =  −v₁ sin ψ + v₂ cos ψ,

  from which each wedge lies **strictly inside a half-plane through the
  origin** bounded by each of its two edge directions (`wedgeAt_upper`,
  `wedgeAt_lower`).  Two wedges sharing an edge direction are then separated
  by that one line — a linear inequality, no angles, no `arctan`, no `mod 2π`.
  The wrap-around pair is handled by `2π`-periodicity of `sin`/`cos`, which is
  the only place periodicity appears at all.

  WHERE ACUTENESS ENTERS, precisely.  A wedge of half-angle `ψ` fits strictly
  inside a half-plane bounded by its own edge exactly when its full opening
  `2ψ` is less than `π`, i.e. `ψ < π/2`.  For Milnor's configuration the
  half-angles ARE the inscribed angles, so `ψ < π/2` for all three is exactly
  "all three angles acute" — Milnor's stated hypothesis, arrived at from the
  separation argument rather than imported.  This is the honest reason the
  acute case is easier; it is NOT a reason the identity would fail otherwise
  (see the scope note).

  Archimedean (ℝ): `sin`, `cos`, `tan`, Lebesgue measure, ordering — §7c.

  -- Ref: [milnor1982] Appendix (the circumcentre subdivision)
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [leitner2026] beans qou-w3eg (H4-5), qou-5gai (H4)
-/

import QOU.Archimedean.OrthoschemeRotation

namespace QOU.Archimedean.HyperbolicVolume

open Real MeasureTheory Set
open QOU.Archimedean QOU.Archimedean.IdealTetrahedronConcavity

/-! ### 1. Each wedge sits strictly inside a half-plane through each edge

The identity that removes all angular reasoning from what follows. -/

/-- **Rotating, then testing against the perpendicular of the `(θ+ψ)`
direction, sees only `ψ`.**  The `θ` cancels — which is why the separation
below is a linear inequality rather than an angular comparison. -/
theorem inner_perp_rotL (θ ψ : ℝ) (v : ℝ × ℝ) :
    -((rotL θ v).1 * Real.sin (θ + ψ)) + (rotL θ v).2 * Real.cos (θ + ψ)
      = -(v.1 * Real.sin ψ) + v.2 * Real.cos ψ := by
  have hpyth := Real.sin_sq_add_cos_sq θ
  simp only [rotL_apply, Real.sin_add, Real.cos_add]
  linear_combination (-(v.1 * Real.sin ψ) + v.2 * Real.cos ψ) * hpyth

/-- **The wedge lies strictly below its upper edge**: the line through the
origin in direction `θ + ψ`. -/
theorem wedgeAt_upper {R θ ψ : ℝ} (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    ∀ w ∈ wedgeAt R θ ψ,
      -(w.1 * Real.sin (θ + ψ)) + w.2 * Real.cos (θ + ψ) < 0 := by
  intro w hw
  rw [wedgeAt_eq_image] at hw
  obtain ⟨v, hv, rfl⟩ := hw
  rw [inner_perp_rotL]
  have hπ : 0 < π := Real.pi_pos
  have hcos : 0 < Real.cos ψ := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ⟩
  have hx : 0 < v.1 := wedge_fst_pos hψ0 hψ hv
  have habs : |v.2| < v.1 * Real.tan ψ := hv.2
  rw [Real.tan_eq_sin_div_cos,
    show v.1 * (Real.sin ψ / Real.cos ψ) = v.1 * Real.sin ψ / Real.cos ψ by ring,
    lt_div_iff₀ hcos] at habs
  have := mul_le_mul_of_nonneg_right (le_abs_self v.2) hcos.le
  linarith

/-- **The wedge lies strictly above its lower edge**: the line through the
origin in direction `θ − ψ`. -/
theorem wedgeAt_lower {R θ ψ : ℝ} (hψ0 : 0 < ψ) (hψ : ψ < π / 2) :
    ∀ w ∈ wedgeAt R θ ψ,
      0 < -(w.1 * Real.sin (θ - ψ)) + w.2 * Real.cos (θ - ψ) := by
  intro w hw
  rw [wedgeAt_eq_image] at hw
  obtain ⟨v, hv, rfl⟩ := hw
  have h := inner_perp_rotL θ (-ψ) v
  rw [show θ + -ψ = θ - ψ by ring, Real.sin_neg, Real.cos_neg] at h
  rw [h]
  have hπ : 0 < π := Real.pi_pos
  have hcos : 0 < Real.cos ψ := Real.cos_pos_of_mem_Ioo ⟨by linarith, hψ⟩
  have hx : 0 < v.1 := wedge_fst_pos hψ0 hψ hv
  have habs : |v.2| < v.1 * Real.tan ψ := hv.2
  rw [Real.tan_eq_sin_div_cos,
    show v.1 * (Real.sin ψ / Real.cos ψ) = v.1 * Real.sin ψ / Real.cos ψ by ring,
    lt_div_iff₀ hcos] at habs
  have := mul_le_mul_of_nonneg_right (neg_le_abs v.2) hcos.le
  linarith

/-! ### 2. Adjacent wedges are disjoint — separated by one line -/

/-- **Two wedges sharing an edge direction are disjoint.**

`W₁`'s upper edge and `W₂`'s lower edge are the same line through the origin;
`W₁` is strictly on one side of it and `W₂` strictly on the other.  No angular
arithmetic: the hypothesis `θ₁ + ψ₁ = θ₂ - ψ₂` is an equation between reals. -/
theorem disjoint_wedgeAt_adjacent {R θ₁ ψ₁ θ₂ ψ₂ : ℝ}
    (hψ₁0 : 0 < ψ₁) (hψ₁ : ψ₁ < π / 2) (hψ₂0 : 0 < ψ₂) (hψ₂ : ψ₂ < π / 2)
    (hadj : θ₁ + ψ₁ = θ₂ - ψ₂) :
    Disjoint (wedgeAt R θ₁ ψ₁) (wedgeAt R θ₂ ψ₂) := by
  rw [Set.disjoint_left]
  intro w hw₁ hw₂
  have h₁ := wedgeAt_upper hψ₁0 hψ₁ w hw₁
  have h₂ := wedgeAt_lower hψ₂0 hψ₂ w hw₂
  rw [← hadj] at h₂
  linarith

/-- The wrap-around case: `W₂`'s upper edge is `W₁`'s lower edge, one turn on.
`2π`-periodicity of `sin`/`cos` is the only place periodicity is used. -/
theorem disjoint_wedgeAt_wrap {R θ₁ ψ₁ θ₂ ψ₂ : ℝ}
    (hψ₁0 : 0 < ψ₁) (hψ₁ : ψ₁ < π / 2) (hψ₂0 : 0 < ψ₂) (hψ₂ : ψ₂ < π / 2)
    (hwrap : θ₂ + ψ₂ = θ₁ - ψ₁ + 2 * π) :
    Disjoint (wedgeAt R θ₁ ψ₁) (wedgeAt R θ₂ ψ₂) := by
  rw [Set.disjoint_left]
  intro w hw₁ hw₂
  have h₁ := wedgeAt_lower hψ₁0 hψ₁ w hw₁
  have h₂ := wedgeAt_upper hψ₂0 hψ₂ w hw₂
  rw [hwrap, Real.sin_add_two_pi, Real.cos_add_two_pi] at h₂
  linarith

/-! ### 3. Three disjoint wedges carry the Λ-sum -/

/-- **The Λ-sum for three pairwise-disjoint wedges.**

Nothing here says the union is a triangle; the geometry lives entirely in the
disjointness hypotheses and in whatever supplies the three axes. -/
theorem hypVolume_chimney_union₃ {R θ₁ ψ₁ θ₂ ψ₂ θ₃ ψ₃ : ℝ} (hR : 0 < R)
    (h₁0 : 0 < ψ₁) (h₁ : ψ₁ < π / 2) (h₂0 : 0 < ψ₂) (h₂ : ψ₂ < π / 2)
    (h₃0 : 0 < ψ₃) (h₃ : ψ₃ < π / 2)
    (d₁₂ : Disjoint (wedgeAt R θ₁ ψ₁) (wedgeAt R θ₂ ψ₂))
    (d₁₃ : Disjoint (wedgeAt R θ₁ ψ₁) (wedgeAt R θ₃ ψ₃))
    (d₂₃ : Disjoint (wedgeAt R θ₂ ψ₂) (wedgeAt R θ₃ ψ₃)) :
    hypVolume (chimney (wedgeAt R θ₁ ψ₁ ∪ wedgeAt R θ₂ ψ₂ ∪ wedgeAt R θ₃ ψ₃) R)
      = ENNReal.ofReal (Lob ψ₁ + Lob ψ₂ + Lob ψ₃) := by
  have m₁ := measurableSet_wedgeAt R θ₁ ψ₁
  have m₂ := measurableSet_wedgeAt R θ₂ ψ₂
  have m₃ := measurableSet_wedgeAt R θ₃ ψ₃
  have hsub : ∀ w ∈ wedgeAt R θ₁ ψ₁ ∪ wedgeAt R θ₂ ψ₂ ∪ wedgeAt R θ₃ ψ₃,
      w.1 ^ 2 + w.2 ^ 2 < R ^ 2 := by
    rintro w ((hw | hw) | hw)
    · exact wedgeAt_subset_disk h₁0 h₁ w hw
    · exact wedgeAt_subset_disk h₂0 h₂ w hw
    · exact wedgeAt_subset_disk h₃0 h₃ w hw
  rw [hypVolume_chimney_of_subset_disk ((m₁.union m₂).union m₃) hsub,
    lintegral_union m₃ (Set.disjoint_union_left.mpr ⟨d₁₃, d₂₃⟩),
    lintegral_union m₂ d₁₂,
    lintegral_wedgeAt hR h₁0 h₁, lintegral_wedgeAt hR h₂0 h₂,
    lintegral_wedgeAt hR h₃0 h₃]
  have n₁ := Lob_nonneg_of_lt_pi_div_two h₁0 h₁
  have n₂ := Lob_nonneg_of_lt_pi_div_two h₂0 h₂
  have n₃ := Lob_nonneg_of_lt_pi_div_two h₃0 h₃
  rw [← ENNReal.ofReal_add n₁ n₂, ← ENNReal.ofReal_add (by linarith) n₃]

/-! ### 4. Milnor's configuration

The three wedges his circumcentre subdivision produces from a triangle
inscribed in the circle of radius `R` with inscribed angles `(α, β, γ)`.

The axes and half-angles are read off the inscribed-angle theorem: the side
opposite the vertex with inscribed angle `α` subtends the CENTRAL angle `2α`,
so the wedge on that side has half-angle `α` and its axis points at that
side's midpoint.  Starting the first vertex at `t`, the three wedges occupy
the consecutive angular ranges

    [t, t+2γ],  [t+2γ, t+2γ+2α],  [t+2γ+2α, t+2γ+2α+2β = t+2π],

which is why `α + β + γ = π` is what closes the circle. -/

/-- The three wedges of Milnor's subdivision, for a triangle inscribed in the
circle of radius `R` with inscribed angles `(α, β, γ)` and first vertex at
angle `t`. -/
def milnorWedges (R t α β γ : ℝ) : Set (ℝ × ℝ) :=
  wedgeAt R (t + γ) γ ∪ wedgeAt R (t + 2 * γ + α) α ∪
    wedgeAt R (t + 2 * γ + 2 * α + β) β

/-- **Milnor's Λ-sum, for the union of the three wedges.**

    Vol(chimney (milnorWedges R t α β γ) R)  =  Λ(α) + Λ(β) + Λ(γ)

The hypotheses are exactly his: the three angles are positive, sum to `π`, and
are acute.  Acuteness is used **only** through `disjoint_wedgeAt_adjacent` /
`disjoint_wedgeAt_wrap` — a wedge fits strictly inside a half-plane bounded by
its own edge exactly when `2ψ < π`.

**This is not yet a statement about a triangle.**  `milnorWedges` is a union of
three explicitly-described regions of the plane.  That it EQUALS the closed
triangle inscribed in the circle, up to null sets, is the one remaining step —
see the scope note below. -/
theorem hypVolume_chimney_milnorWedges {R t α β γ : ℝ} (hR : 0 < R)
    (hα0 : 0 < α) (hβ0 : 0 < β) (hγ0 : 0 < γ)
    (hα : α < π / 2) (hβ : β < π / 2) (hγ : γ < π / 2)
    (hsum : α + β + γ = π) :
    hypVolume (chimney (milnorWedges R t α β γ) R)
      = ENNReal.ofReal (Lob α + Lob β + Lob γ) := by
  rw [show Lob α + Lob β + Lob γ = Lob γ + Lob α + Lob β by ring]
  refine hypVolume_chimney_union₃ hR hγ0 hγ hα0 hα hβ0 hβ ?_ ?_ ?_
  · -- wedge γ meets wedge α along the ray to the second vertex
    exact disjoint_wedgeAt_adjacent hγ0 hγ hα0 hα (by ring)
  · -- wedge γ and wedge β close the circle: this is where `α+β+γ = π` is used
    refine disjoint_wedgeAt_wrap hγ0 hγ hβ0 hβ ?_
    rw [← hsum]; ring
  · -- wedge α meets wedge β along the ray to the third vertex
    exact disjoint_wedgeAt_adjacent hα0 hα hβ0 hβ (by ring)

/-! ### 5. Scope — and what closed the remaining step

`hypVolume_chimney_milnorWedges` is Milnor's value on Milnor's pieces.  What it
is **not**, on its own, is a statement about a triangle.  The gap was precise:

    milnorWedges R t α β γ  =ᵐ  (the closed triangle inscribed in the circle
                                 of radius R with inscribed angles α, β, γ
                                 and first vertex at angle t)

and it is now **proved** — `milnorWedges_ae_eq_inscribedTriangle` in
`QOU.Archimedean.OrthoschemeTiling`, which also restates the Λ-sum on the
triangle (`hypVolume_chimney_inscribedTriangle`).  Both inclusions were genuine
work, and neither needed the machinery one might expect:

* `⊆` — each wedge inside the triangle.  NOT a convexity argument: the single
  identity `cos ψ · F = sin(ψ+ψ') · G₂ + cos ψ' · G₃` puts a wedge inside a
  neighbour's chord half-plane as a two-term positive combination
  (`wedgeAt_lt_chord_next` / `_prev`).
* `⊇` — the three wedges cover.  NOT a covering computation: the sign relation
  `sin 2α·x + sin 2β·y + sin 2γ·z = 0` (`perp_sign_relation`) has positive
  coefficients, so the edge functionals are never all-positive or all-negative,
  and the six surviving sign patterns each land in one sector.

The exceptional set taken there is the three edge LINES rather than the three
spine segments — larger than necessary, but null for a cheaper reason (each is
the kernel of a nonzero linear functional) — hence `=ᵐ`.

The pre-Lean set-level evidence that made it worth starting is in
`computations/milnor_subdivision_obtuse_scope_probe.py`; the identities the
proof actually rests on are certified in
`computations/milnor_tiling_certificate_probe.py` (9/9 at 50 dps).

What that step did **not** settle is the triangle's *definition*:
`inscribedTriangle` is defined as an intersection of three chord half-planes,
anchored to the intended triangle by `inscribedTriangle_vertex_incidence` and
not by a `convexHull` identification.

Beyond that, and unchanged: this says nothing about ideal tetrahedra.  That a
chimney over the inscribed triangle IS the ideal tetrahedron of the
corresponding dihedral angles is Milnor's geometric identification, and Mathlib
has no ideal tetrahedra.

**On the obtuse case.**  Acuteness is used here only to separate the wedges.
It is NOT evidence that the identity fails for obtuse triangles — it does not:
`Λ(α)+Λ(β)+Λ(γ)` reproduces the base integral over obtuse and right inscribed
triangles to `~1e-17`
(`computations/milnor_subdivision_obtuse_scope_probe.py`, 15/15).  What fails
for obtuse triangles is this SUBDIVISION: the circumcentre leaves the triangle
and one wedge must be subtracted rather than added.  Scope-(a) — a statement
about a proof route, not about the theorem. -/

end QOU.Archimedean.HyperbolicVolume
