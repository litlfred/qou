/-
  Neumann-Zagier cusp parity for 4₁, and the exact lattice identity.

  Formalises the ALGEBRAIC content of
  `computations/qbeta/qbeta_neumann_zagier_cusp_modulus_probe.py` (8/8).
  Three of that probe's eight assertions are theorems and are proved here;
  the other five are numerical measurements and are NOT dressed up as
  theorems — see the honest accounting at the bottom of this comment.

  SETTING. The figure-eight knot 4₁ has gluing variety `z w (z-1)(w-1) = 1`,
  deformed by Neumann-Zagier (65)-(66)

      z(1-z) = e^{ v/2}      w(1-w) = e^{-v/2}      u = log( w (1-z) )

  with `u` the meridian and `v` the longitude log-holonomy. NZ eq (52) states
  that the inverse series `v(u) = Σ cₙ uⁿ` has `cₙ = 0` for even `n`.

  WHAT IS PROVED, and why it matters.

  1. `gluing_swap_inverse` — the ALGEBRAIC CORE of NZ (52) for 4₁. Sending
     `v ↦ -v` swaps `z ↔ w`, sending `u = log(w(1-z))` to `log(z(1-w))`. The
     two arguments are reciprocal:

         (z(1-w)) · (w(1-z)) = 1

     so `u(-v) = -u(v)` and `u` is ODD. This follows from the gluing relation
     ALONE by `(1-w)(1-z) = (w-1)(z-1)`, with no analysis and no series. It
     is the reason NZ (52) holds for this knot, and the reason the leading
     correction to the cusp shape is second order in `u` rather than first --
     which is the whole quantitative claim of the probe.

  2. `oddFun_div_even` — an odd `v` gives an EVEN `τ(u) = v(u)/u`. Stated for
     a generic odd function, so it is a fact about parity and not about 4₁.
     Together with 1 this is the structural half of the probe's
     "the derived modulus drift is second order, not first".

  3. `tau0_eq_lattice_point` + `omega_primitive_sixth` — the exact cross-check
     between two independent sources. The corpus states the 4₁ cusp lattice
     as hexagonal `ℤ⟨1, ω⟩` with `ω` a primitive 6th root of unity
     (`CuspShapeBarParity`); NZ state the cusp SHAPE as `2√-3`. These are not
     in tension and are not the same statement:

         2 i s = -2 + 4 ω        (with s² = 3, i² = -1)

     EXACTLY, so NZ's meridian-longitude lattice `ℤ⟨1, τ₀⟩` is the index-4
     sublattice of the shortest-vector one. Parameterising on `s` with
     `s² = 3` rather than writing `Real.sqrt 3` is deliberate: it exhibits the
     hexagonal structure as a consequence of the DISCRIMINANT, which is the
     actual content, and keeps the import surface to `Complex.Basic`.

  4. `drift_ratio_exactly_four` — for an even quadratic shape
     `τ(u) = c₁ + c₃u²`, the drift at `2u` is exactly `4×` the drift at `u`.
     This is the probe's "the meridian-normalisation binary is carried, not
     settled": whether the substitution is `u = ln q₀` or `u = 2 ln q₀` is the
     open NZ-1/2 binary of bean `qou-yh67`, and the factor of 4 between the
     two branches is forced, not measured. Proved for arbitrary `c₁ c₃`, so it
     does not depend on their values -- which is the point, since those values
     are NOT proved here.

  WHAT IS NOT PROVED, stated plainly rather than omitted.

  - `τ₀ = c₁ = 2√-3` and `c₃/c₁ = 1/3` are NUMERICAL results: the probe
    computes the Taylor series of `u(v)` by quadrature at 40 dps, inverts it,
    and matches NZ eq (68). Proving them in Lean needs the analytic inversion
    of `u(v)` through a tracked square-root branch, which is real-analysis
    work this file does not attempt. They enter here only as the SHAPE
    `τ(u) = c₁ + c₃u² + …`, with `c₁` and `c₃` left free.
  - The O'Hara energy figures (122.2055…, and the 0.16 % / 0.64 % drifts) are
    quadrature measurements. Nothing here asserts them.

  Sorry-free. No `axiom`, no conditional class, no `native_decide`.

  -- Ref: [neumann-zagier1985] Volumes of hyperbolic three-manifolds,
  --      Topology 24 (1985) 307-332, eqs (52), (65)-(66), (68)
  -- Ref: [leitner2026] computations/qbeta/qbeta_neumann_zagier_cusp_modulus_probe.py
  -- Ref: [leitner2026] QOU/QBeta/CuspShapeBarParity.lean  (the hexagonal lattice)
  -- Ref: [leitner2026] .beans/qou-yh67 (the NZ-1/2 binary, OPEN)
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta.NeumannZagierCuspParity

/-! ### 1. The algebraic core of NZ (52): the gluing relation forces oddness -/

/-- **The reciprocal-argument identity.**

If `z, w` lie on the 4₁ gluing variety `z w (z-1)(w-1) = 1`, then the two
logarithm arguments produced by `v ↦ -v` (which swaps `z ↔ w`) are reciprocal:

    (z(1-w)) · (w(1-z)) = 1.

Hence `u(-v) = log(z(1-w)) = -log(w(1-z)) = -u(v)`: the meridian
log-holonomy is an ODD function of the longitude one, which is NZ eq (52)
for this knot. Stated over a generic commutative ring because the identity
is algebraic — it uses only `(1-w)(1-z) = (w-1)(z-1)` and needs no analysis,
no branch choice, and no series. -/
theorem gluing_swap_inverse {R : Type*} [CommRing R] (z w : R)
    (h : z * w * (z - 1) * (w - 1) = 1) :
    (z * (1 - w)) * (w * (1 - z)) = 1 := by
  linear_combination h

/-- The swap is an involution on the gluing variety: if `(z, w)` is a
solution then so is `(w, z)`. This is what makes `v ↦ -v` a symmetry of the
deformation rather than merely a reparametrisation. -/
theorem gluing_symm {R : Type*} [CommRing R] (z w : R)
    (h : z * w * (z - 1) * (w - 1) = 1) :
    w * z * (w - 1) * (z - 1) = 1 := by
  linear_combination h

/-! ### 2. Odd numerator ⇒ even cusp shape ⇒ the correction is second order -/

/-- **An odd `v` gives an even `τ(u) = v(u)/u`.**

The cusp shape is the ratio of the longitude to the meridian log-holonomy.
When the numerator is odd — which §1 establishes for 4₁ — the ratio is even,
so its expansion about `u = 0` has no linear term and the leading correction
to `τ₀` is `O(u²)`.

This is the structural half of the probe's finding that the real modulus
drift is second order: the quadratic suppression is forced by parity, not
observed in the numbers. -/
theorem oddFun_div_even {v : ℝ → ℝ} (hodd : ∀ x, v (-x) = -v x) (u : ℝ) :
    v (-u) / (-u) = v u / u := by
  rw [hodd u, neg_div_neg_eq]

/-- The even-ness of `τ` in the form actually used downstream: the first-order
coefficient of an even function vanishes, so writing `τ(u) = c₁ + c₃u²` omits
no `u¹` term. Stated as the parity identity for the quadratic shape. -/
theorem tauShape_even (c₁ c₃ u : ℝ) :
    c₁ + c₃ * (-u) ^ 2 = c₁ + c₃ * u ^ 2 := by
  ring

/-! ### 3. The exact lattice identity: NZ's cusp shape sits in the hexagonal
lattice as an index-4 point -/

variable (s : ℂ)

/-- The corpus's cusp shape: a primitive 6th root of unity, written with its
discriminant explicit. With `s² = 3` this is `e^{iπ/3} = (1 + i√3)/2`. -/
noncomputable def omega : ℂ := (1 + Complex.I * s) / 2

/-- Neumann-Zagier's cusp shape for 4₁: `τ₀ = 2√-3`, written with the
discriminant explicit. With `s² = 3` this is `2i√3`. -/
noncomputable def tau0 : ℂ := 2 * Complex.I * s

/-- **`ω` is a primitive 6th root of unity**, i.e. a root of the 6th
cyclotomic polynomial `X² - X + 1`. Needs the discriminant `s² = 3`; this is
where the hexagonal structure comes from. -/
theorem omega_primitive_sixth (hs : s ^ 2 = 3) :
    (omega s) ^ 2 - omega s + 1 = 0 := by
  have hI : Complex.I ^ 2 = -1 := Complex.I_sq
  unfold omega
  linear_combination (s ^ 2 / 4) * hI - (1 / 4 : ℂ) * hs

/-- **The exact cross-check: `τ₀ = -2 + 4ω`.**

Two independent sources describe one lattice. The corpus proves the 4₁ cusp
lattice is the hexagonal `ℤ⟨1, ω⟩`; NZ give the cusp SHAPE as `2√-3`. This
identity says NZ's meridian-longitude lattice `ℤ⟨1, τ₀⟩` is a SUBLATTICE of
it, generated by `1` and `-2 + 4ω`.

Note it holds for EVERY `s` — no discriminant hypothesis — because it is a
statement about the change of basis, not about which quadratic field one is
in. That is why it is an exact integer relation rather than a numerical
agreement. -/
theorem tau0_eq_lattice_point : tau0 s = -2 + 4 * omega s := by
  unfold tau0 omega
  ring

/-- The index of that sublattice is 4: the change-of-basis matrix from
`(1, ω)` to `(1, τ₀)` is `[[1, 0], [-2, 4]]`, of determinant 4. -/
theorem lattice_index_four : (1 : ℤ) * 4 - 0 * (-2) = 4 := by
  norm_num

/-! ### 4. The meridian-normalisation binary: the two branches differ by
exactly 4, whichever is right -/

/-- The cusp shape to second order, with both coefficients free. Deliberately
NOT specialised to `c₁ = 2√-3`, `c₃ = c₁/3` — those are numerical results of
the probe, not theorems of this file. -/
def tauQuad (c₁ c₃ u : ℝ) : ℝ := c₁ + c₃ * u ^ 2

/-- **The `u` vs `2u` branches differ by exactly a factor of 4.**

Whether the substitution is `u = ln q₀` or `u = 2 ln q₀` is the NZ-1/2 binary
recorded in bean `qou-yh67`, which states it cannot be settled numerically.
This theorem says the RATIO of the two resulting drifts is forced to be 4
regardless — because the normalisation enters `τ` squared — so the binary
moves the drift by a known factor and nothing else.

Holds for all `c₁ c₃ u`, including the degenerate cases, since both sides
scale together. -/
theorem drift_ratio_exactly_four (c₁ c₃ u : ℝ) :
    |tauQuad c₁ c₃ (2 * u) - c₁| = 4 * |tauQuad c₁ c₃ u - c₁| := by
  unfold tauQuad
  have h : c₁ + c₃ * (2 * u) ^ 2 - c₁ = 4 * (c₁ + c₃ * u ^ 2 - c₁) := by ring
  rw [h, abs_mul]
  norm_num

/-- The drift itself is second order: it vanishes to first order in `u`.
Stated as the exact quadratic dependence, which is what makes the derived
drift an order of magnitude smaller than a first-order one. -/
theorem drift_is_quadratic (c₁ c₃ u : ℝ) :
    tauQuad c₁ c₃ u - c₁ = c₃ * u ^ 2 := by
  unfold tauQuad; ring

end QOU.QBeta.NeumannZagierCuspParity
