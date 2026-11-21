import Mathlib.Tactic

/-!
# The ζ₄ bar-parity swap: translating bar-even ↔ bar-odd

The **explicit translator** between the mass (bar-even, `cosh`-like) and the
decay/binding (bar-odd, `sinh`-like) faces.  Complements the σ-parity *split*
(`QOU.QBeta.EkParitySplit`, which projects onto the two faces) and the ζ₄
f-map constraints — this file states the **swap map** they both use implicitly.

For any `x` in a field, put the two bar-parity shapes
$$\mathrm{barEven}(x) = x + x^{-1}\ (\cosh\text{-like}),\qquad
  \mathrm{barOdd}(x) = x - x^{-1}\ (\sinh\text{-like}),$$
symmetric / antisymmetric under the bar involution `x ↦ x⁻¹`.  A **quarter-turn
`x ↦ ζx`** by a primitive fourth root of unity (`ζ² = -1`) exchanges them:
$$\mathrm{barEven}(\zeta x) = \zeta\,\mathrm{barOdd}(x),\qquad
  \mathrm{barOdd}(\zeta x) = \zeta\,\mathrm{barEven}(x).$$

This is the algebraic `cosh ↔ sinh` realization `cosh(t) = -i\,\sinh(t+i\pi/2)`
(`x = eᵗ`, `ζ = e^{iπ/2} = i`): even ↔ odd is `Re ↔ Im` of the complex volume
`CVol = Vol + i·CS` (mass = `Re`/bar-even, decay=binding = `Im`/bar-odd), and the
translator is multiplication by `ζ₄ = i`.

**The swap is an algebraic / geometric-side operation, not an off-axis
continuation of the evaluation.**  Here `ζ` multiplies the (already complex)
*shape / coefficient* variable `x` — the geometric tetrahedron shape
(`z = e^{iπ/3}` for `4₁`) or the cyclotomic/Habiro coefficient — **not** the real
substrate evaluation point `q₀`.  So the bar-odd (decay/binding) object is
obtained by ζ₄-transporting the *solved* bar-even (geometric) object
**algebraically**, and then evaluating at the **same real `q₀`**.  No analytic
continuation of the `q₀` evaluation off the real axis is needed: the `ζ = i`
lives in the fibre/coefficient (where `c_k` legitimately live), while the
archimedean constraint `Im q₀ = 0` binds only the evaluation point.  This is why
the c₃ bar-odd `S` is "complex" (a `ζ₄` coefficient factor) yet observed at real
`q₀` — the transport happens on the algebraic/geometric side, the evaluation
stays real.

**Not a ζ₄-residue claim (coordination, §8 flip-flop guard).** This is a
functional-argument **swap** `x ↦ ζx`, orthogonal to the *residue* question
already settled by `QOU.QBeta.Zeta4Residue` (`QBetaZeta4ResidueRefutation`):
there `Φ₄ = q²+1` is proved **not** to divide the odd carrier, so the odd channel
has **no ζ₄-residue / no pole at `q = i`**.  Nothing here reopens that — the swap
`barEven(ζx) = ζ·barOdd(x)` is a parity-grading identity in the *argument*, not a
pole/divisibility statement in `q`, and it wires no `c_k`.

Generic field, no archimedean structure (§7c). No `c_k` wired.

-- Ref: [leitner2026] docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md
-- Ref: [leitner2026] docs/audits/2026-07-04-zeta4-fibre-cyclotomic-refutation.md
-/

namespace QOU.QBeta.BarParityZeta4Swap

variable {R : Type*} [Field R]

/-- Bar-even (`cosh`-like) shape: `x + x⁻¹`, fixed by the bar involution. -/
def barEven (x : R) : R := x + x⁻¹

/-- Bar-odd (`sinh`-like) shape: `x − x⁻¹`, negated by the bar involution. -/
def barOdd (x : R) : R := x - x⁻¹

/-- `barEven` is invariant under the bar involution `x ↦ x⁻¹`. -/
theorem barEven_bar (x : R) : barEven x⁻¹ = barEven x := by
  change x⁻¹ + (x⁻¹)⁻¹ = x + x⁻¹
  rw [inv_inv]
  exact add_comm x⁻¹ x

/-- `barOdd` is negated by the bar involution `x ↦ x⁻¹`. -/
theorem barOdd_bar (x : R) : barOdd x⁻¹ = -barOdd x := by
  change x⁻¹ - (x⁻¹)⁻¹ = -(x - x⁻¹)
  rw [inv_inv]
  exact (neg_sub x x⁻¹).symm

/-- The inverse of a primitive fourth root of unity is its negative: `ζ⁻¹ = -ζ`. -/
theorem inv_eq_neg_of_sq_eq_neg_one {ζ : R} (hζ : ζ ^ 2 = -1) : ζ⁻¹ = -ζ := by
  -- `ζ * (-ζ) = -(ζ * ζ) = -(ζ ^ 2) = -(-1) = 1`, spelled with `mul_neg`/`pow_two`.
  have h1 : ζ * (-ζ) = 1 := by rw [mul_neg, ← pow_two, hζ, neg_neg]
  exact inv_eq_of_mul_eq_one_right h1

/-- **ζ₄ swap, even → odd.** With `ζ² = -1`, the quarter-turn `x ↦ ζx` carries the
bar-EVEN (mass) shape to `ζ` times the bar-ODD (decay/binding) shape. -/
theorem barEven_zeta_mul {ζ : R} (hζ : ζ ^ 2 = -1) (x : R) :
    barEven (ζ * x) = ζ * barOdd x := by
  have hζinv := inv_eq_neg_of_sq_eq_neg_one hζ
  simp only [barEven, barOdd, mul_inv, hζinv]
  ring

/-- **ζ₄ swap, odd → even.** The companion: the quarter-turn carries the bar-ODD
shape to `ζ` times the bar-EVEN shape. -/
theorem barOdd_zeta_mul {ζ : R} (hζ : ζ ^ 2 = -1) (x : R) :
    barOdd (ζ * x) = ζ * barEven x := by
  have hζinv := inv_eq_neg_of_sq_eq_neg_one hζ
  simp only [barEven, barOdd, mul_inv, hζinv]
  ring

/-- Two quarter-turns (`ζ²x = -x`) negate the bar-even shape — the `ζ₄` period-4
rotation `even → ζ·odd → -even → -ζ·odd → even`. -/
theorem barEven_zeta_sq_mul {ζ : R} (hζ : ζ ^ 2 = -1) (x : R) :
    barEven (ζ * (ζ * x)) = -barEven x := by
  rw [barEven_zeta_mul hζ, barOdd_zeta_mul hζ, ← mul_assoc, ← pow_two, hζ]
  ring

/-- **Rapidities add (cosh law).** Composing turns multiplies the arguments; the
bar-even (mass / `cosh`) shape obeys the addition formula. Generic bar-involution
multiplicativity — lives with `barEven`/`barOdd` (moved here from the cusp module). -/
theorem barEven_mul (x y : R) :
    2 * barEven (x * y) = barEven x * barEven y + barOdd x * barOdd y := by
  change 2 * (x * y + (x * y)⁻¹) = (x + x⁻¹) * (y + y⁻¹) + (x - x⁻¹) * (y - y⁻¹)
  rw [mul_inv]
  ring

/-- **Rapidities add (sinh law).** The bar-odd (decay–binding / `sinh`) companion
of `barEven_mul`. -/
theorem barOdd_mul (x y : R) :
    2 * barOdd (x * y) = barOdd x * barEven y + barEven x * barOdd y := by
  change 2 * (x * y - (x * y)⁻¹) = (x - x⁻¹) * (y + y⁻¹) + (x + x⁻¹) * (y - y⁻¹)
  rw [mul_inv]
  ring

/-- **Universal bar-parity hyperbola (`qou-rutm`).**
    For any `x ≠ 0` in `R`, `(barEven x)² − (barOdd x)² = 4`. -/
theorem barEven_sq_sub_barOdd_sq {x : R} (hx : x ≠ 0) :
    (barEven x) ^ 2 - (barOdd x) ^ 2 = 4 := by
  have hmul : x * x⁻¹ = 1 := mul_inv_cancel₀ hx
  change (x + x⁻¹) ^ 2 - (x - x⁻¹) ^ 2 = 4
  linear_combination 4 * hmul

/-- **Sum of squares of bar-parity coordinates (`qou-rutm`).**
    `(barEven x)² + (barOdd x)² = 2 · barEven(x²)`. -/
theorem barEven_sq_add_barOdd_sq (x : R) :
    (barEven x) ^ 2 + (barOdd x) ^ 2 = 2 * barEven (x ^ 2) := by
  change (x + x⁻¹) ^ 2 + (x - x⁻¹) ^ 2 = 2 * (x ^ 2 + (x ^ 2)⁻¹)
  rw [← inv_pow]
  ring

/-- **Quarter-turn `ζ₄` exchanges `(barEven)²` and `-(barOdd)²` while preserving
    the hyperbola `(barEven)² − (barOdd)²` (`qou-rutm`).** -/
theorem barParity_sq_zeta_swap {ζ x : R} (hζ : ζ ^ 2 = -1) :
    (barEven (ζ * x)) ^ 2 = -(barOdd x) ^ 2 ∧
    (barOdd (ζ * x)) ^ 2 = -(barEven x) ^ 2 ∧
    (barEven (ζ * x)) ^ 2 - (barOdd (ζ * x)) ^ 2 =
      (barEven x) ^ 2 - (barOdd x) ^ 2 := by
  rw [barEven_zeta_mul hζ, barOdd_zeta_mul hζ]
  refine ⟨by linear_combination (barOdd x) ^ 2 * hζ,
          by linear_combination (barEven x) ^ 2 * hζ,
          by linear_combination ((barOdd x) ^ 2 - (barEven x) ^ 2) * hζ⟩

/-! ## GGM eq. (100) mirror-symmetric radical of a 3×3 antisymmetric pairing (`qou-rutm`)

Bean `qou-rutm` proves that any 3×3 antisymmetric matrix
`M(a, b, c) = [[0, c, -b], [-c, 0, a], [b, -a, 0]]` annihilates its axis vector
`(a, b, c)`, and that imposing GGM eq. (100) (`M_{1,3} = -M_{2,3}`, i.e. `-b = -a`
under `φ = (1 2)`) forces `a = b`, making the null direction `(a, a, c)`
fixed by the mirror involution `φ(x, y, z) = (y, x, z)` (instantiated by
eq. (98)'s axis `(-3, -3, 4)`). -/

/-- Action of the 3×3 antisymmetric matrix `M(a, b, c)` on `v ∈ R³`. -/
def antisymCrossApply (a b c : R) (v : R × R × R) : R × R × R :=
  (c * v.2.1 - b * v.2.2, -c * v.1 + a * v.2.2, b * v.1 - a * v.2.1)

/-- The mirror involution `φ = (1 2)` swapping the first two coordinates of `R³`. -/
def mirrorSwap12 (v : R × R × R) : R × R × R :=
  (v.2.1, v.1, v.2.2)

/-- **The axis vector `(a, b, c)` always lies in the kernel of `M(a, b, c)` (`qou-rutm`).** -/
theorem antisymCrossApply_axis_eq_zero (a b c : R) :
    antisymCrossApply a b c (a, b, c) = (0, 0, 0) := by
  change (c * b - b * c, -c * a + a * c, b * a - a * b) = (0, 0, 0)
  ext <;> dsimp <;> ring

/-- **GGM eq. (100) (`-b = -a`) forces the null axis `(a, b, c)` to be fixed by
    `mirrorSwap12` and to annihilate `M(a, b, c)` (`qou-rutm`).** -/
theorem ggm_eq100_axis_mirror_invariant {a b : R} (c : R) (h100 : -b = -a) :
    a = b ∧
    mirrorSwap12 (a, b, c) = (a, b, c) ∧
    antisymCrossApply a b c (a, b, c) = (0, 0, 0) := by
  have hab : a = b := neg_inj.mp h100.symm
  refine ⟨hab, ?_, antisymCrossApply_axis_eq_zero a b c⟩
  subst hab
  rfl

end QOU.QBeta.BarParityZeta4Swap
