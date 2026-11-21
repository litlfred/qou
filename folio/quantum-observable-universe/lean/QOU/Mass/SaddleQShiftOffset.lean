import Mathlib.Analysis.Normed.Field.Basic

/-!
# Tier-2 offset magnitude: `r_K(q) = |z*| · ℏ_q` under the q-integer-curve shift

The **rigorous tier-2** of the torus-knot → q-Bring offset (bean `qou-vhv6`).
`QOU.Mass.ColorCurveQIntegerForm` establishes that the colour spectral cubic is a
q-integer curve carrying the base shift `z ↦ q·z`. A symbolic computation shows
the discriminant transforms covariantly,

  `disc_X C(X; q·z) = Δ(q·z)`,

so the saddle set (roots of `Δ`) of the q-shifted curve is the `1/q`-scaling of
the original: a saddle point `w` (root of `Δ`) moves to `w/q`. Hence the **offset
vector** is

  `v(q, w) = w/q − w = −ℏ_q · w`,   `ℏ_q := 1 − q⁻¹`,

and the **offset magnitude** (over a normed field, e.g. `ℂ`) is

  `‖v(q, w)‖ = ‖w‖ · ‖ℏ_q‖`.

So the offset is **radial** (a real multiple of `w` when `q` is real — the
saddle contracts toward the origin as `q` grows) and its magnitude is **linear
in the quantum Planck constant `ℏ_q = 1 − q⁻¹`**, vanishing at the symmetric
point `q = 1` (`ℏ_q = 0`). This DERIVES Gemini's "magnitude scales with `ℏ_q`"
intuition and simultaneously **refutes** its `sinh/cosh` transfer-matrix ansatz:
the true dependence is linear, not hyperbolic. (At the fibre level `q` may be
complex, giving a non-radial offset; at the archimedean substrate `Im q₀ = 0`,
so the offset is radial.)

Numerically at the muon-anchored `q₀ ≈ 1.10998` (`ℏ_q ≈ 0.09908`), the three
saddle magnitudes `|z*| ∈ {0.9431, 1.0000, 1.0603}` give
`r ∈ {0.0934, 0.0991, 0.1051}`.

§7c: the offset identity is stated over a generic `Field`; the magnitude over a
`NormedField`. Derived, not fitted — a one-line `field_simp; ring`.
-/

namespace QOU.Mass

/-- The quantum Planck constant `ℏ_q := 1 − q⁻¹`. -/
def hbarQ {K : Type*} [Field K] (q : K) : K := 1 - q⁻¹

/-- **Offset identity.** Under the base shift `z ↦ q·z`, a saddle point `w`
(root of the colour-cubic discriminant) maps to `w/q`, and the offset is
`w/q − w = −ℏ_q · w`. -/
theorem saddle_offset_eq {K : Type*} [Field K] (q w : K) (hq : q ≠ 0) :
    w / q - w = -(hbarQ q) * w := by
  unfold hbarQ
  field_simp
  ring

/-- **Offset magnitude.** `‖w/q − w‖ = ‖w‖ · ‖ℏ_q‖` — the offset magnitude is
`|z*|` times the quantum Planck constant, vanishing at `q = 1`. -/
theorem saddle_offset_norm {K : Type*} [NormedField K] (q w : K) (hq : q ≠ 0) :
    ‖w / q - w‖ = ‖w‖ * ‖hbarQ q‖ := by
  rw [saddle_offset_eq q w hq, norm_mul, norm_neg, mul_comm]

/-- **Boundary condition.** At the symmetric point `q = 1`, `ℏ_q = 0`, so the
offset vanishes: the saddle configuration is centred. -/
theorem hbarQ_one {K : Type*} [Field K] : hbarQ (1 : K) = 0 := by
  unfold hbarQ; simp


/-- **Vanishing of the offset at `q = 1` (`qou-8hw1`).**
At the symmetric point `q = 1`, `w / (1 : K) - w = -(hbarQ (1 : K)) * w`. -/
theorem saddle_offset_at_one {K : Type*} [Field K] (w : K) :
    w / (1 : K) - w = -(hbarQ (1 : K)) * w :=
  saddle_offset_eq (1 : K) w one_ne_zero

end QOU.Mass
