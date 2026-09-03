/-
  H4-5, obtuse case — the ANALYTIC reduction (setup for the open geometric proof).

  The acute Milnor Λ-sum is proved sorry-free:
  `QOU.Archimedean.HyperbolicVolume.hypVolume_chimney_milnorWedges` and its
  triangle form `hypVolume_chimney_inscribedTriangle` give, for an ideal
  tetrahedron with dihedral angles `(α, β, γ)` summing to `π` and ALL ACUTE,

      Vol  =  Λ(α) + Λ(β) + Λ(γ).

  Acuteness is used there ONLY to make the three circumcentre wedges pairwise
  disjoint (`disjoint_wedgeAt_adjacent`/`_wrap`, each wedge fits in a half-plane
  iff its half-angle `< π/2`).  When one angle is obtuse the circumcentre leaves
  the triangle and Milnor's subdivision has one piece enter with a MINUS sign;
  that signed geometry is `qou-w3eg` H4-5's remaining open step — it is NOT
  closed here, and nothing below claims a volume.

  What IS settled here is the analytic bookkeeping that step will consume, so the
  geometry has a clean target.  Three facts, all from `α + β + γ = π`,
  positivity, and the already-proved reflection `Lob_pi_sub : Λ(π − t) = −Λ(t)`
  (`IdealTetrahedronConcavity.Lob_pi_sub`):

  1. `at_most_one_obtuse` — an admissible triple has AT MOST ONE angle `≥ π/2`.
     So the obtuse case is a single case, not a combinatorial family.
  2. `third_angle_acute_of_obtuse` — if `γ ≥ π/2` then `α + β ≤ π/2`: the
     reflected argument `π − γ = α + β` is itself acute.
  3. `lob_sum_eq_reflected` — `Λ(α)+Λ(β)+Λ(γ) = Λ(α)+Λ(β) − Λ(α+β)`, so the
     obtuse contribution `Λ(γ)` is exactly MINUS an acute-argument term
     `Λ(α+β)`.  Composed with (2), when `γ` is obtuse EVERY Λ-argument on the
     right (`α`, `β`, `α+β`) lies in `(0, π/2]`.

  Together: the obtuse volume identity, once the signed subdivision is in hand,
  is a statement about three ACUTE Lobachevsky values with one subtracted — the
  form the acute wedge machinery already speaks.  This is the "one piece enters
  with a minus sign" of Milnor's Appendix, made precise at the `Λ` level, with
  every remaining gap kept in the geometry (which is why no `hypVolume` appears
  below).

  The identity itself is not in doubt — `Λ(α)+Λ(β)+Λ(γ)` reproduces the base
  integral over obtuse and right inscribed triangles to ~1e-17
  (`computations/milnor_subdivision_obtuse_scope_probe.py`, 15/15); only its
  Lean proof route is open.

  Archimedean (ℝ): ordering and `Real.pi` — §7c.

  -- Ref: [milnor1982] Appendix (the circumcentre subdivision; obtuse minus sign)
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [manuscript] beans qou-w3eg (H4-5, obtuse), qou-idvt
-/
import QOU.Archimedean.LobachevskyMaximum

namespace QOU.Archimedean

open Real
open QOU.Archimedean.IdealTetrahedronConcavity

/-- **An admissible angle triple has at most one obtuse angle.**  If two of
`α, β, γ > 0` summing to `π` were both `≥ π/2`, the third would be `≤ 0`.  So
Milnor's obtuse case is a single configuration, not a family. -/
theorem at_most_one_obtuse {α β γ : ℝ} (hγ : 0 < γ)
    (hsum : α + β + γ = π) : ¬ (π / 2 ≤ α ∧ π / 2 ≤ β) := by
  rintro ⟨hae, hbe⟩
  linarith

/-- **The reflected argument is acute.**  If `γ ≥ π/2` then `α + β = π − γ ≤ π/2`.
This is what makes the `−Λ(α+β)` term of `lob_sum_eq_reflected` an
acute-argument Lobachevsky value in the obtuse case. -/
theorem third_angle_acute_of_obtuse {α β γ : ℝ} (hγ : π / 2 ≤ γ)
    (hsum : α + β + γ = π) : α + β ≤ π / 2 := by
  linarith

/-- **The Λ-sum in reflected form.**  From `γ = π − (α+β)` and
`Lob_pi_sub : Λ(π − t) = −Λ(t)`,

    Λ(α) + Λ(β) + Λ(γ)  =  Λ(α) + Λ(β) − Λ(α+β).

No acuteness needed for the identity; combined with `third_angle_acute_of_obtuse`
the right-hand side has all three arguments (`α`, `β`, `α+β`) acute exactly when
`γ` is the obtuse one.  This is Milnor's "one piece enters with a minus sign" at
the analytic level — the geometric subdivision that realises it is `qou-w3eg`
H4-5 and stays open. -/
theorem lob_sum_eq_reflected {α β γ : ℝ} (hsum : α + β + γ = π) :
    Lob α + Lob β + Lob γ = Lob α + Lob β - Lob (α + β) := by
  have hγ : γ = π - (α + β) := by linarith
  rw [hγ, Lob_pi_sub]
  ring

end QOU.Archimedean
