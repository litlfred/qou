/-
  The shape-parameter bridge: every `z` with `Im z > 0` IS an ideal-tetrahedron
  angle triple, so the concavity theorems apply at `z_q`.

  THE QUESTION THIS ANSWERS.  "How does an ideal tetrahedron map into Bring's
  surface under `z_q` coordinates?"  The corpus already had both halves and no
  link between them:

    * `BlochWignerLobachevsky` — the SHAPE side.  For `Im z > 0` the three
      Möbius images `z`, `1/(1−z)`, `1−1/z` have positive imaginary part
      (`tet_im_pos`), their args lie in `(0, π)` (`arg_mem_Ioo_of_im_pos`), and
      they sum to `π` (`tetAngles_sum_eq_pi`).
    * `IdealTetrahedronConcavity` — the ANGLE side.  `AngleTriple` is exactly
      "three positive reals summing to `π`", and the Hessian of the volume is
      negative definite at every such triple.

  `AngleTriple` is *precisely* the data `tetAngles_sum_eq_pi` produces, so the
  two files describe the same object from opposite ends.  `ofShape` below is the
  one-line constructor nobody had written, and with it the concavity result
  transports to the shape parameter for free (`hessian_neg_definite_ofShape`).

  WHY IT MATTERS FOR `z_q`.  `conj:crossing-graded-mass-expansion` fixes "the
  universal shape parameter `z_q` from the Descartes elliptic curve" and builds
  the depth scalar `ξ(q) = D(z_q)/ℏ_q²` from it — `D` being Bloch–Wigner, i.e.
  the volume of the ideal tetrahedron of shape `z_q`.  `𝓔_q` is the chiral
  fibration of Bring's surface, so the chain is

      Bring's surface → chiral fibration 𝓔_q → shape z_q
                      → ideal tetrahedron of shape z_q → volume D(z_q) → ξ(q)

  `ofShape` is the fourth arrow, made mechanical.  Given `Im z_q > 0`, the
  tetrahedron at `z_q` is a legitimate `AngleTriple` and every theorem in
  `IdealTetrahedronConcavity` applies to it with no further hypotheses.

  WHAT IS *NOT* CLAIMED — read before citing.

  * **No `Im z_q > 0` is proved here.**  `ofShape` takes it as a hypothesis.
    Whether the Descartes shape parameter lands in the upper half plane at the
    substrate `q₀` is a separate question this file does not touch, and it is
    the actual precondition for anything above to apply at `z_q`.
  * **Nothing about Bring's surface is proved here.**  The chain above is how
    the corpus's blocks connect in prose; only the fourth arrow is Lean.
  * **`Vol = Λ(α)+Λ(β)+Λ(γ)` is still not proved** (bean `qou-idvt` T2).  This
    file transports the *concavity of the cotangent Hessian* to shape
    coordinates; it does not identify that Hessian with a hyperbolic volume.
  * **No mass or binding claim.**  `conj:crossing-graded-mass-expansion` is a
    conjecture and is not wired to production; the canonical absolute-mass route
    is the muon-anchored Hecke energy via `computations/canonical_mass.py`, which
    does not pass through `ξ(q)` at all.

  Archimedean (ℝ, ℂ): `arg`, ordering — §7c.

  -- Ref: [leitner2026] beans qou-idvt (T1/T3), qou-krvm (iv)
  -- Ref: [thurston1978] Ch. 7 (shape parameters and ideal simplices)
-/

import Mathlib.Tactic
import QOU.Archimedean.BlochWignerLobachevsky
import QOU.Archimedean.IdealTetrahedronConcavity

namespace QOU.Archimedean.IdealTetrahedronConcavity

open QOU.Archimedean

/-- **The shape parameter of an ideal tetrahedron is an `AngleTriple`.**

For `Im z > 0`, the dihedral angles `(arg z, arg(1/(1−z)), arg(1−1/z))` are
positive and sum to `π` — exactly the `AngleTriple` data.  Every hypothesis is
discharged by a theorem that already existed; what was missing was the
observation that the two files describe the same object. -/
noncomputable def AngleTriple.ofShape (z : ℂ) (hz : 0 < z.im) : AngleTriple where
  α := tetAngle₁ z
  β := tetAngle₂ z
  γ := tetAngle₃ z
  hα := (arg_mem_Ioo_of_im_pos z hz).1
  hβ := (arg_mem_Ioo_of_im_pos _ (tet_im_pos z hz).1).1
  hγ := (arg_mem_Ioo_of_im_pos _ (tet_im_pos z hz).2).1
  sum := tetAngles_sum_eq_pi z hz

@[simp] theorem AngleTriple.ofShape_α (z : ℂ) (hz : 0 < z.im) :
    (AngleTriple.ofShape z hz).α = tetAngle₁ z := rfl

@[simp] theorem AngleTriple.ofShape_β (z : ℂ) (hz : 0 < z.im) :
    (AngleTriple.ofShape z hz).β = tetAngle₂ z := rfl

@[simp] theorem AngleTriple.ofShape_γ (z : ℂ) (hz : 0 < z.im) :
    (AngleTriple.ofShape z hz).γ = tetAngle₃ z := rfl

/-- **The concavity result, transported to shape coordinates.**

The cotangent Hessian is negative definite at the tetrahedron of *every* shape
`z` in the upper half plane — in particular at a substrate shape parameter `z_q`,
once `Im z_q > 0` is supplied.  No new mathematics: `ofShape` plus
`hessian_neg_definite`. -/
theorem hessian_neg_definite_ofShape (z : ℂ) (hz : 0 < z.im)
    {x y : ℝ} (hxy : x ≠ 0 ∨ y ≠ 0) :
    letI t := AngleTriple.ofShape z hz
    (-(Real.cos t.α / Real.sin t.α + Real.cos t.γ / Real.sin t.γ)) * x ^ 2
        + 2 * (-(Real.cos t.γ / Real.sin t.γ)) * x * y
        + (-(Real.cos t.β / Real.sin t.β + Real.cos t.γ / Real.sin t.γ)) * y ^ 2 < 0 :=
  hessian_neg_definite (AngleTriple.ofShape z hz) hxy

/-- **The determinant is exactly `1` at every shape.**  The `det H = 1`
rigidity, transported the same way — it does not degenerate anywhere in the
upper half plane. -/
theorem hessian_det_eq_one_ofShape (z : ℂ) (hz : 0 < z.im) :
    letI t := AngleTriple.ofShape z hz
    (-(Real.cos t.α / Real.sin t.α + Real.cos t.γ / Real.sin t.γ))
        * (-(Real.cos t.β / Real.sin t.β + Real.cos t.γ / Real.sin t.γ))
      - (-(Real.cos t.γ / Real.sin t.γ)) ^ 2 = 1 :=
  hessian_det_eq_one (AngleTriple.ofShape z hz)

end QOU.Archimedean.IdealTetrahedronConcavity
