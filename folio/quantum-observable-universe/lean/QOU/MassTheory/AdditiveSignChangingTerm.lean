/-
# The additive sign-changing many-body term M(A): the bond−frustration mechanism
# is structurally CAPABLE of the sign change, but pinning both residuals is a FIT.

`QOU.MassTheory.DampingNonMonotoneWall` (#4307) proved the pure-damping class is
walled: the residual `M(A) = ρ_strong(A) − ρ_grad(A)` **changes sign** — positive
at A=3 (graded undershoots) and negative at A=4 (graded overshoots).  Per the
permanence principle the closure is therefore an **additive** term `M(A)`, not a
multiplicative damping.

This file formalizes, sorry-free, the honest status of the natural DERIVED
candidate — the **bond−frustration simplex term** on the A-nucleon coordination
graph `K_A` (edges `C(A,2)` = 2-body bonds, triangular faces `C(A,3)` =
geometrically-frustrated 3-cycles):

    M(A) = s · (C(A,2) − κ · C(A,3)),   s > 0,   κ ≥ 0.

At A=3: `C(3,2)=3, C(3,3)=1` ⇒ `M(3) = s(3 − κ)`.
At A=4: `C(4,2)=6, C(4,3)=4` ⇒ `M(4) = s(6 − 4κ)`.

Two facts, both certificates about *evidence*, not fits:

* **(W) Structural sign-change window.**  `M(3) > 0 ∧ M(4) < 0  ↔  3/2 < κ < 3`.
  The bond−frustration mechanism reproduces the #4307 sign pattern (`+` at A=3,
  `−` at A=4) for a genuine open interval of the frustration-per-triangle weight
  `κ` — a **parameter-free structural capability**, not a tuned coincidence.  So
  the *sign* the data requires is *derived* from the simplex bond structure.

* **(V) Anti-fit identifiability (the magnitude match is VACUOUS).**  The map
  `(s, t) ↦ (M(3), M(4)) = (3s − t, 6s − 4t)` (writing `t = κs` for the raw
  triangle weight) is a **linear isomorphism** — its `2×2` matrix has
  determinant `3·(−4) − (−1)·6 = −6 ≠ 0`.  Hence for *any* target pair
  `(m₃, m₄)` there is a **unique** `(s, t)` reproducing it.  Matching both
  residuals `(+0.4708, −2.7080)` is therefore **guaranteed** for the two-weight
  form and carries **zero predictive content**: it is a 2-parameter fit to 2
  points, not a derivation.  This is the anti-fit certificate that forbids
  reading the magnitude match as evidence.

**Combined reading.** The *sign* is a real, 0-parameter structural lead (W); the
*magnitude* is a fit (V).  A genuine derivation would need `κ` (and the scale)
fixed by structure to `0`–`1` free parameters, turning the ratio `M(3)/M(4)` into
a *prediction*.  The companion probe checks the pre-registered 0-shape-parameter
candidates (`κ ∈ {1,2,3,[3]_q}`, tetrahedral penalty) at the fixed canonical `q₀`:
**none** lands both residuals (`deltalambda_additive_signchanging_term_probe.py`).
So this file records a scope-(a) *partial* result — sign derived, magnitude open —
**nothing wired**.

**Anti-fit (STRICT).**  The residual targets `+0.4708 = ρ_strong(3) − [3]_{q₀}`,
`−2.7080 = ρ_strong(4) − [3][4]_{q₀}` (isospin/Coulomb-corrected AME, #3986/#3990)
appear here ONLY inside `(V)` as the illustration `(m₃, m₄)` of an arbitrary target
the invertible map hits — never solved into a canonical weight.  Base ring `ℝ`
per §7c (ordering inequalities).

Companion probe: `computations/deltalambda/deltalambda_additive_signchanging_term_probe.py`.
-/
import Mathlib.Tactic

namespace QOU.MassTheory

/-- The bond−frustration simplex term at A=3: `M(3)/s = C(3,2) − κ·C(3,3) = 3 − κ`. -/
def bondFrustA3 (κ : ℝ) : ℝ := 3 - κ

/-- The bond−frustration simplex term at A=4: `M(4)/s = C(4,2) − κ·C(4,3) = 6 − 4κ`. -/
def bondFrustA4 (κ : ℝ) : ℝ := 6 - 4 * κ

/-- **(W→) Sign change forces `κ ∈ (3/2, 3)`.**  If the (positively-scaled,
`s > 0`) bond−frustration term is `> 0` at A=3 and `< 0` at A=4, then the
frustration-per-triangle weight lies strictly in `(3/2, 3)`. -/
theorem signChange_forces_window {s κ : ℝ} (hs : 0 < s)
    (h3 : 0 < s * bondFrustA3 κ) (h4 : s * bondFrustA4 κ < 0) :
    3 / 2 < κ ∧ κ < 3 := by
  unfold bondFrustA3 at h3
  unfold bondFrustA4 at h4
  -- `s > 0` divides out: `3 − κ > 0` and `6 − 4κ < 0`.
  have hp3 : 0 < 3 - κ := by
    by_contra h
    push_neg at h
    nlinarith [mul_nonpos_of_nonneg_of_nonpos (le_of_lt hs) (by linarith : 3 - κ ≤ 0)]
  have hn4 : 6 - 4 * κ < 0 := by
    by_contra h
    push_neg at h
    nlinarith [mul_nonneg (le_of_lt hs) h]
  constructor <;> linarith

/-- **(W←) Any `κ ∈ (3/2, 3)` realises the sign change.**  For `s > 0` and
`3/2 < κ < 3`, the term is positive at A=3 and negative at A=4 — the #4307 sign
pattern.  So the bond−frustration mechanism is structurally *capable* of the
required sign change on the whole open interval `(3/2, 3)`. -/
theorem window_gives_signChange {s κ : ℝ} (hs : 0 < s)
    (hlo : 3 / 2 < κ) (hhi : κ < 3) :
    0 < s * bondFrustA3 κ ∧ s * bondFrustA4 κ < 0 := by
  unfold bondFrustA3 bondFrustA4
  refine ⟨?_, ?_⟩
  · have : 0 < 3 - κ := by linarith
    positivity
  · have : 6 - 4 * κ < 0 := by linarith
    nlinarith [mul_pos hs (by linarith : 0 < 4 * κ - 6)]

/-- **(W) The sign-change window is exactly `(3/2, 3)`** — a parameter-free
structural characterisation.  The bond−frustration additive term reproduces the
#4307 sign pattern (`+` at A=3, `−` at A=4) **iff** the frustration weight
`κ ∈ (3/2, 3)`.  The *sign* the data requires is thus derived from the simplex
bond/face counts, with no appeal to the residual magnitudes. -/
theorem signChange_iff_window {s : ℝ} (hs : 0 < s) (κ : ℝ) :
    (0 < s * bondFrustA3 κ ∧ s * bondFrustA4 κ < 0) ↔ (3 / 2 < κ ∧ κ < 3) := by
  constructor
  · rintro ⟨h3, h4⟩; exact signChange_forces_window hs h3 h4
  · rintro ⟨hlo, hhi⟩; exact window_gives_signChange hs hlo hhi

/-- **(V) Anti-fit identifiability — the two-weight map is a linear isomorphism.**
The map `(s, t) ↦ (3s − t, 6s − 4t)` sending the (edge, triangle) weights to the
`(M(3), M(4))` residual pair is **surjective**: for *any* target `(m₃, m₄)` there
exist weights reproducing it — explicitly `s = (2/3)(m₃ − m₄/4)·(3/2)`… (the closed
inverse below).  Because the target is always hit, matching both residuals is
**guaranteed** and carries no predictive content.

The witnesses are the exact inverse of the `det = −6` system:
`s = (4·m₃ − m₄)/6`, `t = (6·m₃ − 3·m₄)/6 = m₃ − m₄/2`. -/
theorem fit_hits_any_target (m₃ m₄ : ℝ) :
    ∃ s t : ℝ, 3 * s - t = m₃ ∧ 6 * s - 4 * t = m₄ := by
  refine ⟨(4 * m₃ - m₄) / 6, (6 * m₃ - 3 * m₄) / 6, ?_, ?_⟩ <;> ring

/-- **(V′) Uniqueness — the fit is fully determined, i.e. it has NO residual
freedom.**  Two weight pairs producing the same `(M(3), M(4))` are equal.  With
(V) this says the two-weight form is a *bijection* onto residual pairs: 2 free
parameters, 2 constraints, exactly one solution.  Reproducing the physical
residuals `(+0.4708, −2.7080)` consumes both degrees of freedom and predicts
nothing — the anti-fit certificate. -/
theorem fit_is_unique {s t s' t' : ℝ}
    (h1 : 3 * s - t = 3 * s' - t') (h2 : 6 * s - 4 * t = 6 * s' - 4 * t') :
    s = s' ∧ t = t' := by
  constructor <;> linarith

/-- **(V″) Concrete instance at the physical residuals.**  The #4307 target pair
`(m₃, m₄) = (0.4708, −2.7080)` is hit by the two-weight fit — witnessing that the
magnitude match is *guaranteed*, hence non-evidential.  (The values `0.4708`,
`−2.7080` enter ONLY as an arbitrary target of the surjective map; nothing is
solved *from* them into a canonical structural weight.) -/
theorem fit_hits_physical_residuals :
    ∃ s t : ℝ, 3 * s - t = (4708 : ℝ) / 10000 ∧ 6 * s - 4 * t = -(27080 : ℝ) / 10000 :=
  fit_hits_any_target _ _

/-- **Parameter-free `κ`-elimination invariant across `A = 3` and `A = 4` (`qou-kok7`):**
For every triangle frustration weight `κ`, `4 · bondFrustA3 κ - bondFrustA4 κ = 6`. -/
theorem bondFrust_linear_comb_invariant (κ : ℝ) :
    4 * bondFrustA3 κ - bondFrustA4 κ = 6 := by
  unfold bondFrustA3 bondFrustA4
  ring

/-- **Boundary and midpoint evaluations of the `(3/2, 3)` sign-change window (`qou-kok7`):**
At `κ = 3/2`, `bondFrustA4` vanishes while `bondFrustA3 = 3/2 > 0`; at `κ = 3`, `bondFrustA3`
vanishes while `bondFrustA4 = -6 < 0`; at the midpoint `κ = 9/4`, `bondFrustA3 = 3/4 > 0`
and `bondFrustA4 = -3 < 0`. -/
theorem bondFrust_window_endpoints_and_midpoint :
    bondFrustA3 (3 / 2) = 3 / 2 ∧
    bondFrustA4 (3 / 2) = 0 ∧
    bondFrustA3 3 = 0 ∧
    bondFrustA4 3 = -6 ∧
    bondFrustA3 (9 / 4) = 3 / 4 ∧
    bondFrustA4 (9 / 4) = -3 := by
  unfold bondFrustA3 bondFrustA4
  norm_num

end QOU.MassTheory
