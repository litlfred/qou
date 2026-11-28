/-
# The convolution flow's half-turn is the fibre rotation of the relative direction

Owner, 2026-10-12: prove or refute "the convolution flow's half-turn = the fibre rotation" (bean
`qou-jfx8`; ruling: particle strands follow the fibre Reeb flow of `UT(Σ₄)`).

## The identification, and which parts are proved

Two nearby fibre strands sit over points `p` and `p + r` of `Σ₄`. Their relative position `r` lies in
the base direction `T_pΣ₄ ≅ ℂ`, so its DIRECTION `r/|r|` is a point of the fibre circle `UT_pΣ₄`. This
is the reading of the owner's "relative vector in computation velocity space" (2026-10-12); it is a
modelling statement, stated here, not proved.

Given it, the following are proved:

1. **Exchange acts on the relative coordinate by `−1`** (`exchange_center`, `exchange_relative`):
   swapping the two strands fixes the centre `c = (z₁ + z₂)/2` and sends `r = z₁ − z₂ ↦ −r`. So `c`
   spans the trivial and `r` the sign representation of `S₂`, which are the `q = 1` limits of the
   Sym (`q`) and Alt (`−q⁻¹`) channels of the bridge letter.
2. **The half twist rotates `r` by `π`** (`halfTwist_one`), two half twists are a full turn
   (`fullTwist`), and the twist is a one-parameter flow (`halfTwist_add`).
3. **On the direction it IS the fibre flow** (`halfTwist_unit`): for `r = e^{iθ}`, the half twist at time
   `t` is `e^{i(θ + πt)}`, the fibre Reeb flow `θ ↦ θ + πt` of `∂_θ`.
4. **The Alt eigenvalue carries exactly this phase** (`alt_eigen_arg`, `alt_eigen_norm`,
   `altEigen_one`): `−q⁻¹ = q⁻¹ e^{iπ}` for `q > 0`, with phase `π` and modulus `q⁻¹`. The flow
   `altEigen t = q^{−t} e^{iπt}` restricts at `t = 1` to `−q⁻¹`, and its phase factor is the same
   `e^{iπt}` that rotates `r`.

**Verdict.** The phase of the convolution flow on the Alt channel is the fibre rotation of the
relative direction; the `q`-deformation contributes only the modulus `q^{−t}`. The branch is fixed,
not chosen: a positive crossing is a right-handed half twist about the strand direction (the
standard right-hand rule). With strands along `+∂_θ` and the ruled orientation `+dx ∧ dy ∧ dθ`, that
rotates `r` counter-clockwise in the base, i.e. moves its direction along `+∂_θ`: `σ ↔ e^{+iπ}`.

**Not established:** that the Hecke `q`-modulus `q^{−t}` has a geometric meaning on the fibre (it is
scaling, not rotation); and that strands far apart (not nearby fibres) behave the same way.

§7c: over `ℂ`/`ℝ` because the statement is about rotation angles (archimedean).

-- Ref: [manuscript] bean qou-jfx8; ConvolutionFlowParity.lean; BringUTContactChirality.lean §6
   (fibre ruling); standard: configuration space of two points, centre/relative split.
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Arg
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace QOU.MassTheory.ConvolutionFlowFibre

open Complex Real

/-- **Exchange fixes the centre.** -/
theorem exchange_center (z₁ z₂ : ℂ) : (z₂ + z₁) / 2 = (z₁ + z₂) / 2 := by ring

/-- **Exchange negates the relative coordinate**: `r` spans the sign representation. -/
theorem exchange_relative (z₁ z₂ : ℂ) : z₂ - z₁ = -(z₁ - z₂) := by ring

/-- The half twist at time `t`: rotate the relative coordinate by `π t`. -/
noncomputable def halfTwist (t : ℝ) (r : ℂ) : ℂ := r * exp (↑(π * t) * I)

/-- **One half twist exchanges**: `r ↦ −r`. -/
theorem halfTwist_one (r : ℂ) : halfTwist 1 r = -r := by
  unfold halfTwist
  rw [mul_one, exp_pi_mul_I]; ring

/-- **The half twist is a flow.** -/
theorem halfTwist_add (s t : ℝ) (r : ℂ) : halfTwist (s + t) r = halfTwist t (halfTwist s r) := by
  unfold halfTwist
  rw [mul_assoc, ← Complex.exp_add]
  congr 2
  push_cast; ring

/-- **Two half twists are a full turn.** -/
theorem fullTwist (r : ℂ) : halfTwist 2 r = r := by
  rw [show (2 : ℝ) = 1 + 1 by norm_num, halfTwist_add, halfTwist_one, halfTwist_one, neg_neg]

/-- **On the direction, the half twist is the fibre flow `θ ↦ θ + πt`.** -/
theorem halfTwist_unit (θ t : ℝ) :
    halfTwist t (exp (↑θ * I)) = exp (↑(θ + π * t) * I) := by
  unfold halfTwist
  rw [← Complex.exp_add]
  congr 1
  push_cast; ring

/-- **The Alt eigenvalue has phase `π`** for `q > 0`. -/
theorem alt_eigen_arg (q : ℝ) (hq : 0 < q) : arg (-(q : ℂ)⁻¹) = π := by
  have : (-(q : ℂ)⁻¹) = ((-q⁻¹ : ℝ) : ℂ) := by push_cast; ring
  rw [this, arg_ofReal_of_neg (by simpa using inv_pos.2 hq)]

/-- **The Alt eigenvalue has modulus `q⁻¹`.** -/
theorem alt_eigen_norm (q : ℝ) (hq : 0 < q) : ‖(-(q : ℂ)⁻¹)‖ = q⁻¹ := by
  rw [norm_neg, norm_inv, Complex.norm_real, Real.norm_of_nonneg hq.le]

/-- The Alt-channel flow `q^{−t} e^{iπt}`. -/
noncomputable def altEigen (q t : ℝ) : ℂ := ((q ^ (-t) : ℝ) : ℂ) * exp (↑(π * t) * I)

/-- **At `t = 1` the flow is the Alt eigenvalue `−q⁻¹`.** -/
theorem altEigen_one (q : ℝ) (hq : 0 < q) : altEigen q 1 = -(q : ℂ)⁻¹ := by
  unfold altEigen
  rw [Real.rpow_neg hq.le, Real.rpow_one, mul_one, exp_pi_mul_I]
  push_cast; ring

/-- **The flow's phase factor is the half twist's**: `altEigen q t = q^{−t} · (halfTwist t 1)`. -/
theorem altEigen_eq_scale_halfTwist (q t : ℝ) :
    altEigen q t = ((q ^ (-t) : ℝ) : ℂ) * halfTwist t 1 := by
  unfold altEigen halfTwist; ring

end QOU.MassTheory.ConvolutionFlowFibre
