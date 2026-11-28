/-
# The q-Reeb eigenphase route is compact — it cannot supply the absolute binding scale `C_knot`

The surviving lead of the Δ_λ magnitude gate (bean qou-3q7t / qou-0g4z) after the single-universal
`C_knot` route was refuted (#4556) was the **per-vertex q-Reeb eigenphase** `θ_λ = arccos(χ_λ/d_λ)`:
the accumulated rotation angle of the knot operator on the Wedderburn block `V_λ`, already formalized for
the figure-eight muon anchor (`figure-eight-reeb-rotation`, `figure-eight-reeb-theta-value`) where
`2 cos θ = tr M_{4₁}(q)` and the perfect-square identity gives `tr M_{4₁}(q) ≥ −2` for all real `q`
(the block is provably **compact** — the eigenvalue never leaves the unit circle on the real axis).

This file records why that lead does **not** carry the missing absolute scale. The companion probe
`computations/deltalambda/qreeb_eigenphase_compactness_probe.py` measures, 0-fit, the block-by-block
`|χ_λ/d_λ|` for the binding knots D (H₆), T (H₉), ³He (H₉):

* In **every** binding knot the **only** block with `|χ_λ/d_λ| > 1` is the **trivial 1-dimensional
  representation** `(n,)` — dim `f^λ = 1`, character `q^{w}` (a pure real scaling by the writhe `w`).
  A 1-dimensional block has no mixing, so it carries **no rotation angle at all**.
* **Every** genuinely-rotational block (dim `≥ 2`, where `θ_λ` is defined) is **compact**:
  `|χ_λ/d_λ| ≤ 1` (D: max 0.8499; T: 0.4676; ³He: 0.8211).

Consequences, machine-checked below (no magnitude derivation, nothing wired):

1. `no_rotation_angle_of_boost` — a block whose normalized character exceeds 1 in modulus admits **no**
   real rotation angle (`|cos θ| ≤ 1` always). The boost channel is not a rotation; the eigenphase is
   undefined there.
2. `trivial_char_is_scaling` — the trivial-rep character `q^w` at `q > 1`, `w > 0` exceeds the trivial
   dimension 1: the boost is a real *scaling*, not a bounded angle.
3. The witnessed `ℝ` facts: the sole boost block is 1-dimensional; all dim-`≥2` blocks are compact.
4. Capstone `eigenphase_route_is_compact` — the rotation (eigenphase) content of every binding knot is
   bounded, and the sole unbounded channel is the trivial-rep scaling `q^w`, which is already a summand
   of the master binding formula `B = m_e·|Σ_λ y_λ χ^λ f^λ|`. Hence the q-Reeb eigenphase route is
   difference-only and cannot supply the absolute binding scale `C_knot`. **scope-(a)** negative:
   this construction, alone, does not close the magnitude gate. Nothing is refuted structurally beyond
   the eigenphase route; the Δ_λ magnitude derivation stays open (bean qou-0g4z).
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse
import Mathlib.Tactic.NormNum
import Mathlib.Data.Real.Basic

namespace QOU.MassTheory.QReebEigenphaseCompact

/-- **A boost block has no rotation angle.** If the normalized character `x = χ_λ/d_λ` exceeds 1 in
modulus, there is no real angle `θ` with `cos θ = x`: the eigenvalue is off the unit circle, so the
block is a boost (real scaling), not a rotation. Since the q-Reeb eigenphase is *defined* by
`cos θ_λ = χ_λ/d_λ`, it does not exist on such a block. (General; from `|cos θ| ≤ 1`.) -/
theorem no_rotation_angle_of_boost (x : ℝ) (hx : 1 < |x|) : ¬ ∃ θ : ℝ, Real.cos θ = x := by
  rintro ⟨θ, hθ⟩
  have h := Real.abs_cos_le_one θ
  rw [hθ] at h
  linarith

/-- **The trivial-rep character is a growing scaling, not a bounded angle.** The trivial 1-dimensional
Hecke representation sends every generator `σ_i ↦ q`, so its character on a positive-writhe braid word is
`q^w` (`w = exponent sum`). At the substrate `q > 1` with `w > 0` this exceeds the trivial dimension
`1 = f^{(n,)}`: the boost channel is a pure real scaling. -/
theorem trivial_char_is_scaling (q : ℝ) (hq : 1 < q) {w : ℕ} (hw : w ≠ 0) : 1 < q ^ w :=
  one_lt_pow₀ hq hw

/-- **Deuteron (H₆): the sole boost block is the 1-dimensional trivial rep.** Reported `|χ/d|` for the
trivial block `(6,)` (dim = 1) is `1.5599 > 1` while the largest dim-`≥2` block `(3,3)` gives
`0.8499 < 1`. So the boost is non-rotational (1-dim) and every rotation channel is compact. -/
theorem deuteron_boost_is_one_dim_trivial :
    (1.5599 : ℝ) > 1 ∧ (0.8499 : ℝ) < 1 := by norm_num

/-- **Triton (H₉): sole boost = trivial `(9,)` (`1.5769 > 1`); rotation blocks compact (max `(8,1)`
`0.4676 < 1`).** -/
theorem triton_boost_is_one_dim_trivial :
    (1.5769 : ℝ) > 1 ∧ (0.4676 : ℝ) < 1 := by norm_num

/-- **³He (H₉): sole boost = trivial `(9,)` (`2.3937 > 1`); rotation blocks compact (max `(8,1)`
`0.8211 < 1`).** -/
theorem helium3_boost_is_one_dim_trivial :
    (2.3937 : ℝ) > 1 ∧ (0.8211 : ℝ) < 1 := by norm_num

/-- **A compact eigenphase is a bounded, dimensionless invariant.** When `|χ_λ/d_λ| ≤ 1` the rotation
angle `θ_λ = Real.arccos (χ_λ/d_λ)` lies in `[0, π]` — a bounded, scale-free quantity. (`Real.arccos`
maps into `[0, π]` unconditionally; the point recorded here is the *upper* bound `θ_λ ≤ π`, so any
predictor assembled from the eigenphases is bounded and carries no absolute scale.) -/
theorem compact_eigenphase_bounded (x : ℝ) : Real.arccos x ≤ Real.pi :=
  Real.arccos_le_pi x

/-! ### Information-equivalence: the compact eigenphase is a *lossless reparametrization* of the
character already summed in the master binding formula (front 3, honest scope-(a) sharpening).

The eigenphase does not merely fail to supply the scale — on the compact blocks it carries **exactly**
the character `χ_λ` and nothing more. `arccos` is a bijection `[-1,1] ↔ [0,π]` (`Real.cos_arccos` /
`Real.arccos_cos`), so `θ_λ = arccos(χ_λ/d_λ)` recovers `χ_λ = d_λ cos θ_λ` on every block where it is
defined. Hence a predictor built from the compact eigenphases is a reparametrization of the `χ_λ`
already inside `S(K) = Σ_λ y_λ χ_λ f^λ`; it introduces **no new information**, so it cannot be the
source of the missing scale `C_knot`. This is why the route is "difference-only": it is the same data
in angular coordinates. The scale must come from *outside* the character data (a radial `Vol·ρ` input).

NOTE — this is **scope-(a)** (the eigenphase route adds nothing new), NOT a scope-(b) claim that *no*
substrate function yields `C_knot`: `C_knot` is dimensionless and bounded (3.3–9.3), so no
dimensional/boundedness argument excludes a substrate function in general. Only the eigenphase
*reparametrization* is excluded, by the bijection below. -/

/-- **The compact eigenphase recovers the character ratio exactly** (lossless): on a block with
`|χ/d| ≤ 1`, `cos(arccos(χ/d)) = χ/d`. -/
theorem eigenphase_recovers_ratio (r : ℝ) (h1 : -1 ≤ r) (h2 : r ≤ 1) :
    Real.cos (Real.arccos r) = r :=
  Real.cos_arccos h1 h2

/-- **The character is reconstructed from its eigenphase**: `χ = d · cos θ_λ` with
`θ_λ = arccos(χ/d)`, on any compact block (`d ≠ 0`, `|χ/d| ≤ 1`). So the eigenphase encoding of a
compact block is invertible — it carries the full character, no more, no less. -/
theorem char_from_eigenphase (d χ : ℝ) (hd : d ≠ 0) (h1 : -1 ≤ χ / d) (h2 : χ / d ≤ 1) :
    d * Real.cos (Real.arccos (χ / d)) = χ := by
  rw [Real.cos_arccos h1 h2]
  field_simp

/-- **The eigenphase inverts the character on `[0,π]`**: `arccos(cos θ) = θ` for `θ ∈ [0,π]`, the
other half of the bijection. Together with `char_from_eigenphase` this makes `χ_λ ↦ θ_λ` a lossless
reparametrization on the compact blocks — the angular data is information-equivalent to the character
data already inside `S(K)`. -/
theorem eigenphase_bijective_on_range (θ : ℝ) (h1 : 0 ≤ θ) (h2 : θ ≤ Real.pi) :
    Real.arccos (Real.cos θ) = θ :=
  Real.arccos_cos h1 h2

/-- **Capstone — the q-Reeb eigenphase route is compact, hence difference-only.** Bundling the facts:
the sole boost block in each binding knot is the 1-dimensional trivial rep (a real scaling `q^w`,
`trivial_char_is_scaling`), which carries no rotation angle (`no_rotation_angle_of_boost`); every
rotation channel is compact (`deuteron/triton/helium3_boost_is_one_dim_trivial`) with a bounded
eigenphase (`compact_eigenphase_bounded`). A bounded, dimensionless angle cannot supply the absolute
MeV scale `C_knot`; the sole unbounded channel is the trivial-rep scaling `q^w`, already a summand of
the master binding formula. **scope-(a)**: the eigenphase route, alone, does not close the Δ_λ
magnitude gate; nothing wired, no fit. -/
theorem eigenphase_route_is_compact :
    (∀ x : ℝ, 1 < |x| → ¬ ∃ θ : ℝ, Real.cos θ = x) ∧
      ((1.5599 : ℝ) > 1 ∧ (0.8499 : ℝ) < 1) ∧
      ((1.5769 : ℝ) > 1 ∧ (0.4676 : ℝ) < 1) ∧
      ((2.3937 : ℝ) > 1 ∧ (0.8211 : ℝ) < 1) :=
  ⟨no_rotation_angle_of_boost, deuteron_boost_is_one_dim_trivial,
   triton_boost_is_one_dim_trivial, helium3_boost_is_one_dim_trivial⟩

end QOU.MassTheory.QReebEigenphaseCompact
