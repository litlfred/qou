import Mathlib.Tactic

/-!
# The link of the Bring cone: a circle bundle over the curve, Euler number `−6`

Bean `qou-rydq`. The affine cone over Bring's curve `B ⊂ ℙ³` (the canonical model,
a complete intersection of a quadric and a cubic) is a quasi-homogeneous surface
singularity, and its link is the Seifert-fibred 3-manifold given by the unit circle
bundle of the embedding line bundle restricted to the curve (Orlik–Wagreich). For a
curve of genus `g` embedded by a line bundle of degree `d` the Seifert Euler number
of that circle bundle is `−d`. The canonical embedding has `d = deg K_B = 2g − 2`,
so the link has Euler number `−(2g − 2) = 2 − 2g = χ_eu(B)`; at `g = 4` this is
`−6`, and the total space is the unit tangent bundle `UT(Σ₄)` (the circle bundle of
`K⁻¹ = T_B`, orientation reversed), whose fundamental group is infinite.

Two consequences recorded here as the arithmetic they rest on:

* `canonical_link_euler_eq_chi`: for a canonically embedded curve the link's Euler
  number *is* the topological Euler characteristic — the `−6` of
  `lem:brings-euler-characteristic` has a third face, as a Seifert invariant.
* `hopf_link_euler`: the model `QOU.Tetraplectic.BringCone R = Quaternion R` is the
  cone over the Hopf circle
  bundle `S³ → S² = ℙ¹`, degree `1`, Euler number `−1`, finite (trivial) `π₁`.
  The two links differ in Euler number by the factor `6` and in `π₁` by
  finite-versus-infinite, which is why the quaternionic (3-Sasakian) description
  of the Bring cone is a local model of the fibre and not a global statement about
  the link. The content change that rewords the corpus's lemma accordingly is
  owner-gated (bean `qou-rydq`); the arithmetic is not.

Integers only; no `sorry`.

-- Ref: [orlik-wagreich1971] https://doi.org/10.2307/1970772
-- Ref: [milnor1968] Singular points of complex hypersurfaces (link of an isolated singularity)
-/

namespace QOU.Brings

/-- Degree of the canonical bundle of a curve of genus `g`. -/
def canonicalDegree (g : ℤ) : ℤ := 2 * g - 2

/-- Seifert Euler number of the link of the cone over a curve embedded by a line
bundle of degree `d`: `−d` (Orlik–Wagreich). -/
def linkEulerNumber (d : ℤ) : ℤ := -d

/-- Topological Euler characteristic of a curve of genus `g`. -/
def chiEu (g : ℤ) : ℤ := 2 - 2 * g

/-- **For a canonically embedded curve the link's Euler number is `χ_eu`.** -/
theorem canonical_link_euler_eq_chi (g : ℤ) :
    linkEulerNumber (canonicalDegree g) = chiEu g := by
  unfold linkEulerNumber canonicalDegree chiEu; ring

/-- **Bring's curve, `g = 4`:** the link of its cone has Euler number `−6`. -/
theorem bring_link_euler : linkEulerNumber (canonicalDegree 4) = -6 := by
  rw [canonical_link_euler_eq_chi]; rfl

/-- **The quaternionic model is the cone over the Hopf bundle:** degree `1`, Euler
number `−1`. Not the Bring cone's link. -/
theorem hopf_link_euler : linkEulerNumber 1 = -1 := rfl

/-- The two differ by the factor `6`: the ratio of the canonical degree of Bring's
curve to the degree of the Hopf bundle. -/
theorem bring_over_hopf : linkEulerNumber (canonicalDegree 4) = 6 * linkEulerNumber 1 := by
  rw [bring_link_euler, hopf_link_euler]; norm_num

end QOU.Brings
