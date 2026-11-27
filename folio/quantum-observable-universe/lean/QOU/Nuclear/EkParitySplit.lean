import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Tactic

/-!
# The σ-parity (mass / decay) split of the compact q-Pochhammer coefficient

The Faddeev residue expansion lands the elementary-symmetric coefficient
`e_k(q, q³, q⁵, …) = [x^k] ∏(1 + q^{2n+1} x)` on the framework's Hecke / λ⊢n
spine (tetraplectic → Bruhat → Young → partitions; see
`docs/scope/2026-07-11-qbeta-c3-barodd-tetraplectic-combinatorial-reduction.md`).

Two **distinct** involutions act on it and must not be conflated:

* the **transpose** `λ ↔ λ'` (self-conjugate diagrams) is the *modular*
  self-duality `Φ_b = Φ_{1/b}`;
* the **bar** `σ : q ↦ q⁻¹` (on `|q| = 1`, complex conjugation) is the
  *sinh/cosh = bar-odd/bar-even* split.

`e_k` is transpose-symmetric but **not** `σ`-even. This file formalises the
`σ`-parity split as named projections and proves — sorry-free — that

  * `massProj` (cosh / mass / `−Vol(4₁)` face) is `σ`-fixed,
  * `decayProj` (sinh / decay / the Q_β `c₃` bar-odd `S` face) is `σ`-negated,
  * the two reconstruct `f` (and `σ f`),
  * `decayProj f = 0 ↔ σ f = f`, and — **non-vacuously** — `decayProj f ≠ 0`
    exactly when `f` is not bar-even (`σ f ≠ f`); for the compact
    `e_k(q,q³,…)` this holds (`e_k` is not palindromic under `q ↦ q⁻¹`,
    verified in the probe), so the sinh/decay/`S` face genuinely carries content.

This is the algebraic core (`FaddeevModularDouble.bar_parity_decomposition`
promoted to named projections + the elementary-symmetric application). It does
**not** derive the `S`-values: pinning the argument `z(q₀)` (the CS phase /
complex volume, at the root-of-unity accumulation) is the open `z→c_k`
evaluation map — this file closes the *structure*, not the *observable*.

Base ring: `[CommRing R] [Invertible (2 : R)]` — the natural home is
`LaurentPolynomial ℚ` (where `2` is a unit but the ring is **not** a field), so
`Field` would over-specialise. **No `ℝ`/`ℂ` (§7c): purely categorical/algebraic;**
the archimedean instance (`σ = conj` on `ℂ`, where `decayProj = i·Im`) lives
*post*-archimedean-wall, not here.
-/

namespace QOU.QBeta

variable {R : Type*} [CommRing R]

/-- **Mass (cosh / bar-even) projection** under a ring involution `σ`:
    `½(f + σ f)`. On `|q| = 1` (`σ = conj`) this is `Re f` — the real / mass /
    `−Vol(4₁)` face. -/
noncomputable def massProj [Invertible (2 : R)] (σ : R →+* R) (f : R) : R :=
  ⅟(2 : R) * (f + σ f)

/-- **Decay (sinh / bar-odd) projection** under a ring involution `σ`:
    `½(f − σ f)`. On `|q| = 1` (`σ = conj`) this is `i·Im f` — the phase /
    decay / Q_β `c₃` bar-odd `S` face. -/
noncomputable def decayProj [Invertible (2 : R)] (σ : R →+* R) (f : R) : R :=
  ⅟(2 : R) * (f - σ f)

theorem two_mul_massProj [Invertible (2 : R)] (σ : R →+* R) (f : R) :
    (2 : R) * massProj σ f = f + σ f := by
  unfold massProj; rw [← mul_assoc, mul_invOf_self, one_mul]

theorem two_mul_decayProj [Invertible (2 : R)] (σ : R →+* R) (f : R) :
    (2 : R) * decayProj σ f = f - σ f := by
  unfold decayProj; rw [← mul_assoc, mul_invOf_self, one_mul]

/-- Cancel a factor of `2` using the `Invertible 2` instance (no `2 ≠ 0`
    hypothesis needed). -/
private theorem cancel_two [Invertible (2 : R)] {a b : R}
    (h : (2 : R) * a = (2 : R) * b) : a = b := by
  calc a = ⅟(2 : R) * ((2 : R) * a) := by rw [← mul_assoc, invOf_mul_self, one_mul]
    _ = ⅟(2 : R) * ((2 : R) * b) := by rw [h]
    _ = b := by rw [← mul_assoc, invOf_mul_self, one_mul]

/-- The two projections reconstruct `f`: `massProj f + decayProj f = f`. -/
theorem massProj_add_decayProj [Invertible (2 : R)] (σ : R →+* R) (f : R) :
    massProj σ f + decayProj σ f = f := by
  apply cancel_two
  rw [mul_add, two_mul_massProj, two_mul_decayProj]; ring

/-- The `σ`-partner is recovered as the difference:
    `massProj f − decayProj f = σ f`. -/
theorem massProj_sub_decayProj [Invertible (2 : R)] (σ : R →+* R) (f : R) :
    massProj σ f - decayProj σ f = σ f := by
  apply cancel_two
  rw [mul_sub, two_mul_massProj, two_mul_decayProj]; ring

/-- **Mass projection is bar-even** (`σ`-fixed / cosh). -/
theorem sigma_massProj [Invertible (2 : R)] (σ : R →+* R)
    (hσ : Function.Involutive σ) (f : R) : σ (massProj σ f) = massProj σ f := by
  apply cancel_two
  calc (2 : R) * σ (massProj σ f)
      = σ ((2 : R) * massProj σ f) := by rw [map_mul, map_ofNat]
    _ = σ (f + σ f) := by rw [two_mul_massProj]
    _ = f + σ f := by rw [map_add, hσ f]; ring
    _ = (2 : R) * massProj σ f := by rw [two_mul_massProj]

/-- **Decay projection is bar-odd** (`σ`-negated / sinh). -/
theorem sigma_decayProj [Invertible (2 : R)] (σ : R →+* R)
    (hσ : Function.Involutive σ) (f : R) :
    σ (decayProj σ f) = -(decayProj σ f) := by
  apply cancel_two
  calc (2 : R) * σ (decayProj σ f)
      = σ ((2 : R) * decayProj σ f) := by rw [map_mul, map_ofNat]
    _ = σ (f - σ f) := by rw [two_mul_decayProj]
    _ = -(f - σ f) := by rw [map_sub, hσ f]; ring
    _ = (2 : R) * -(decayProj σ f) := by rw [mul_neg, two_mul_decayProj]

/-- **Decay part vanishes iff `f` is bar-even** (`σ`-fixed). The mass face
    (self-conjugate / real) is exactly the kernel of the decay projection. -/
theorem decayProj_eq_zero_iff [Invertible (2 : R)] (σ : R →+* R) (f : R) :
    decayProj σ f = 0 ↔ σ f = f := by
  constructor
  · intro h
    have h2 : (2 : R) * decayProj σ f = 0 := by rw [h, mul_zero]
    rw [two_mul_decayProj] at h2
    exact (sub_eq_zero.mp h2).symm
  · intro h
    show ⅟(2 : R) * (f - σ f) = 0
    rw [h, sub_self, mul_zero]

/-- **Non-vacuity (generic / categorical, §7c — no `ℂ`).** The decay (bar-odd)
    face is nonzero *exactly* when `f` is not bar-even. In the canonical instance
    `R = LaurentPolynomial ℚ`, `σ : q ↦ q⁻¹` (the bar) and `f = e_k(q,q³,…)`:
    since `e_k` is not palindromic (`σ f ≠ f`, verified numerically in
    `qbeta_c3_barodd_tetraplectic_reduction_probe.py`), `decayProj σ f ≠ 0` —
    the sinh/decay/`S` carrier genuinely holds content, without leaving the
    categorical ring `R` for the archimedean `ℂ`. -/
theorem decayProj_ne_zero_iff [Invertible (2 : R)] (σ : R →+* R) (f : R) :
    decayProj σ f ≠ 0 ↔ σ f ≠ f :=
  not_congr (decayProj_eq_zero_iff σ f)

/-! ## Mass ⊥ decay under any `σ`-invariant form — the Gram signature splits

The algebraic reason the bar-odd carrier sits in its **own** block of the
Frobenius/Gram form (numerically the unique negative-norm *ghost* direction of
the indefinite `G_{ij}=tr_M(b_i b_j)` in `H₃(q)`, witnessed by
`qbeta_c3_barodd_knot_operator_gram_probe.py`): a **bar-even** vector and a
**bar-odd** vector are **orthogonal** under *any* `σ`-invariant bilinear form.
Hence the mass (`σ`-even) and decay (`σ`-odd) projections never mix under the
Gram pairing, and the signature splits cleanly along the parity — the ghost
mode is Gram-orthogonal to the mass cone. Generic (no `ℝ`/`ℂ`, §7c): `B` is an
abstract pairing, additive in its second argument and `σ`-invariant. -/

/-- **Bar-even ⊥ bar-odd.** For a pairing `B` additive in its second slot and
    invariant under the involution `σ`, a `σ`-fixed vector `e` and a
    `σ`-negated vector `o` are `B`-orthogonal. -/
theorem barEven_barOdd_orthogonal [Invertible (2 : R)] (σ : R →+* R)
    (B : R → R → R) (hBneg : ∀ x y, B x (-y) = -(B x y))
    (hBinv : ∀ x y, B (σ x) (σ y) = B x y)
    {e o : R} (he : σ e = e) (ho : σ o = -o) : B e o = 0 := by
  have h : B e o = -(B e o) := by
    have hi := hBinv e o
    rw [he, ho, hBneg] at hi
    exact hi.symm
  apply cancel_two
  rw [mul_zero, two_mul]
  nth_rewrite 1 [h]; ring

/-- **Mass ⊥ decay under the Gram form.** The mass (bar-even) and decay
    (bar-odd) projections of any elements are orthogonal under every
    `σ`-invariant pairing `B` — the structural reason the Frobenius/Gram
    signature splits along the bar parity (the decay ghost mode occupies its
    own block). -/
theorem massProj_barOrth_decayProj [Invertible (2 : R)] (σ : R →+* R)
    (hσ : Function.Involutive σ) (B : R → R → R)
    (hBneg : ∀ x y, B x (-y) = -(B x y)) (hBinv : ∀ x y, B (σ x) (σ y) = B x y)
    (f g : R) : B (massProj σ f) (decayProj σ g) = 0 :=
  barEven_barOdd_orthogonal σ B hBneg hBinv (sigma_massProj σ hσ f)
    (sigma_decayProj σ hσ g)

end QOU.QBeta
