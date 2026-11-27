import Mathlib.Analysis.Convex.Jensen
import Mathlib.RepresentationTheory.Basic
import Mathlib.Tactic

/-!
# QOU.Knot.SymmetricOptimum — why the angle-structure offset vanishes at a symmetric point

`qbeta_sdp_angle_offset_theta_probe.py` measured, for the two corpus anchors,
the offset between two canonical points of the generalised angle-structure
polytope:

* `x_geom` — the complete hyperbolic structure's angles (Rivin's critical point
  of the volume functional), and
* `x_LP` — the Casson–Rivin max-strictness LP optimum.

It found `‖x_geom − x_LP‖ = 2.4·10⁻¹⁶` and `5.0·10⁻¹⁶` — zero — because 4₁ is
two *regular* ideal tetrahedra (every angle `1/3` in π-units) and the Borromean
rings complement is the regular ideal *octahedron* decomposition (`1/4`, `1/2`).
Both anchors sit at the symmetric point.

That was a numerical observation with a structural explanation offered only in
prose. This file proves the explanation, in the generality that makes it
reusable: **a concave, symmetry-invariant objective on a convex, symmetry-stable
feasible set is always maximised at a symmetric point.** Two such optimisations
therefore cannot be separated by symmetry alone — which is exactly why the
offset vanishes, and equally why any offset that *does* carry information must
come from an objective that BREAKS the symmetry (the confinement SDP, whose
objective is the braid's Markov-trace data — the probe's named next step).

Route: orbit averaging. `orbitAvg` lands in the feasible set by convexity
(`orbitAvg_mem`), is fixed by the group because left translation permutes it
(`orbitAvg_fixed`), and does not decrease the objective by Jensen
(`le_apply_orbitAvg`). Hence `exists_symmetric_maximiser`, and — when the
symmetric point is unique — `symmetric_point_optimal`.

Scope. This is the *symmetry* half of the story and nothing more. It does not
prove that the angle-structure polytope's symmetric point is unique for any
particular triangulation, nor anything about hyperbolic volume (Mathlib has no
ideal-tetrahedron volume theory); those stay numerical. What it does establish
is that the vanishing offset is forced whenever the symmetry is present, rather
than a coincidence of two knots.

Archimedean (ℝ): genuinely archimedean — convexity and Jensen over `ℝ` (§7c).

-- Ref: [leitner2026] computations/probes/qbeta_sdp_angle_offset_theta_probe.py
-- Ref: [garoufalidis2012] arXiv:1208.1663 §2.2–2.3 (generalised angle structures)
-/

namespace QOU.Knot.SymmetricOptimum

variable {G V : Type*} [Group G] [Fintype G]
variable [AddCommGroup V] [Module ℝ V]

/-- The orbit average of `x` under a representation `ρ`: the barycentre of the
`G`-orbit, with equal weights. -/
noncomputable def orbitAvg (ρ : Representation ℝ G V) (x : V) : V :=
  ∑ g : G, ((Fintype.card G : ℝ)⁻¹) • ρ g x

section
variable (ρ : Representation ℝ G V) {K : Set V} {f : V → ℝ} {x : V}

/-- The equal weights sum to one. -/
private theorem weights_sum_one :
    ∑ _g : G, ((Fintype.card G : ℝ)⁻¹) = 1 := by
  have hcard : (Fintype.card G : ℝ) ≠ 0 := by
    have : 0 < Fintype.card G := Fintype.card_pos
    positivity
  simp [Finset.sum_const, nsmul_eq_mul]

/-- **The orbit average stays feasible.** Convexity of `K` plus stability under
the action. -/
theorem orbitAvg_mem (hK : Convex ℝ K) (hstab : ∀ g : G, ∀ y ∈ K, ρ g y ∈ K)
    (hx : x ∈ K) : orbitAvg ρ x ∈ K := by
  refine hK.sum_mem (fun g _ => ?_) ?_ (fun g _ => hstab g x hx)
  · positivity
  · exact weights_sum_one

/-- **The orbit average is symmetric.** Acting by `h` permutes the sum, because
left translation `g ↦ h * g` is a bijection of `G`. -/
theorem orbitAvg_fixed (h : G) : ρ h (orbitAvg ρ x) = orbitAvg ρ x := by
  unfold orbitAvg
  rw [map_sum]
  simp only [map_smul]
  refine Fintype.sum_equiv (Equiv.mulLeft h) _ _ (fun g => ?_)
  simp [Equiv.coe_mulLeft]

/-- **Averaging never hurts a concave invariant objective** (Jensen). -/
theorem le_apply_orbitAvg (hf : ConcaveOn ℝ K f)
    (hstab : ∀ g : G, ∀ y ∈ K, ρ g y ∈ K)
    (hinv : ∀ (g : G) (y : V), f (ρ g y) = f y) (hx : x ∈ K) :
    f x ≤ f (orbitAvg ρ x) := by
  have hjensen :
      ∑ g : G, ((Fintype.card G : ℝ)⁻¹) • f (ρ g x)
        ≤ f (∑ g : G, ((Fintype.card G : ℝ)⁻¹) • ρ g x) :=
    hf.le_map_sum (fun g _ => by positivity) weights_sum_one
      (fun g _ => hstab g x hx)
  have hlhs : ∑ g : G, ((Fintype.card G : ℝ)⁻¹) • f (ρ g x) = f x := by
    simp only [hinv, smul_eq_mul]
    rw [← Finset.sum_mul, weights_sum_one, one_mul]
  rwa [hlhs] at hjensen

/-- **A symmetric maximiser always exists.** Given any feasible `x`, the orbit
average is feasible, symmetric, and at least as good. -/
theorem exists_symmetric_maximiser (hK : Convex ℝ K) (hf : ConcaveOn ℝ K f)
    (hstab : ∀ g : G, ∀ y ∈ K, ρ g y ∈ K)
    (hinv : ∀ (g : G) (y : V), f (ρ g y) = f y) (hx : x ∈ K) :
    ∃ y ∈ K, (∀ g : G, ρ g y = y) ∧ f x ≤ f y :=
  ⟨orbitAvg ρ x, orbitAvg_mem ρ hK hstab hx, fun g => orbitAvg_fixed ρ g,
    le_apply_orbitAvg ρ hf hstab hinv hx⟩

/-- **The symmetric point is optimal when it is unique.**

If `p` is the only symmetric feasible point, then no feasible point beats it:
every `x ∈ K` averages into a symmetric feasible point, which must be `p`, and
averaging did not decrease `f`.

This is the statement behind the vanishing offset. Two different concave
invariant objectives on the same symmetric convex feasible set are both
maximised at `p`, so their optima coincide and the offset between them is `0` —
no matter what the objectives are. Consequently an informative offset requires
an objective that is **not** invariant. -/
theorem symmetric_point_optimal {p : V} (hK : Convex ℝ K) (hf : ConcaveOn ℝ K f)
    (hstab : ∀ g : G, ∀ y ∈ K, ρ g y ∈ K)
    (hinv : ∀ (g : G) (y : V), f (ρ g y) = f y)
    (huniq : ∀ y ∈ K, (∀ g : G, ρ g y = y) → y = p) :
    ∀ x ∈ K, f x ≤ f p := by
  intro x hx
  obtain ⟨y, hyK, hysym, hxy⟩ := exists_symmetric_maximiser ρ hK hf hstab hinv hx
  rwa [huniq y hyK hysym] at hxy

/-- **The offset vanishes — two invariant objectives share their optimum.**

This is the statement the angle-structure probe needs. Let `f₁` and `f₂` be any
two concave objectives on the same symmetric convex feasible set, each invariant
under the symmetry and each with a unique maximiser. Then both maximisers equal
the symmetric point `p`, hence equal each other: **the offset between the two
optima is zero, whatever the two objectives are.**

Applied to the angle-structure polytope, `f₁` is the Casson-Rivin minimum-angle
objective and `f₂` the volume functional; both are concave and invariant under
the triangulation's symmetry, so no offset between `x_LP` and `x_geom` can exist
— which is what the probe measured as `2.4·10⁻¹⁶` and `5.0·10⁻¹⁶`.

The contrapositive is the useful half going forward: an offset that carries
information requires an objective that is **not** invariant. The confinement
SDP's objective is the braid's Markov-trace data, which breaks the symmetry —
so that is where a nonzero offset can live. -/
theorem optima_coincide {p x₁ x₂ : V} {f₁ f₂ : V → ℝ} (hK : Convex ℝ K)
    (hf₁ : ConcaveOn ℝ K f₁) (hf₂ : ConcaveOn ℝ K f₂)
    (hstab : ∀ g : G, ∀ y ∈ K, ρ g y ∈ K)
    (hinv₁ : ∀ (g : G) (y : V), f₁ (ρ g y) = f₁ y)
    (hinv₂ : ∀ (g : G) (y : V), f₂ (ρ g y) = f₂ y)
    (huniq : ∀ y ∈ K, (∀ g : G, ρ g y = y) → y = p)
    (h₁K : x₁ ∈ K) (h₁ : ∀ z ∈ K, f₁ x₁ ≤ f₁ z → z = x₁)
    (h₂K : x₂ ∈ K) (h₂ : ∀ z ∈ K, f₂ x₂ ≤ f₂ z → z = x₂) :
    x₁ = p ∧ x₂ = p ∧ x₁ = x₂ := by
  have hpK : p ∈ K := by
    obtain ⟨y, hyK, hysym, _⟩ :=
      exists_symmetric_maximiser ρ hK hf₁ hstab hinv₁ h₁K
    rwa [huniq y hyK hysym] at hyK
  have e₁ : x₁ = p :=
    (h₁ p hpK (symmetric_point_optimal ρ hK hf₁ hstab hinv₁ huniq x₁ h₁K)).symm
  have e₂ : x₂ = p :=
    (h₂ p hpK (symmetric_point_optimal ρ hK hf₂ hstab hinv₂ huniq x₂ h₂K)).symm
  exact ⟨e₁, e₂, e₁.trans e₂.symm⟩

end

end QOU.Knot.SymmetricOptimum
