import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic


/-!
# Algebraic-geometric dilogarithm equivalence (conjecture class)

The conjecture: under the Archimedean realization, the algebraic
partial product Φ_n(x; q) maps bijectively (via its denominator
zeros) to the ideal-tetrahedron cusps of the hyperbolic Φ_q-piece,
and its asymptotic recovers the Bloch-Wigner volume.

Per AGENTS.md §3b, downstream-of-conjecture statements are
themselves conjectures.  We package the assertion as a typeclass
that consumes `ArchimedeanLimit` and a `Kashaev`-style instance and
exposes the bijective + volumetric content.

-- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
-- Ref: [murakami-murakami2001] Murakami & Murakami, "The colored Jones polynomials and the simplicial volume of a knot," Acta Math. 186 (2001), arXiv:math/9905075
-/

namespace QOU.QPochhammer

/-- Local restatement of the q-Pochhammer denominator (mirrors the
    sibling `q-pochhammer-partial-product.lean`; kept self-contained
    so this file does not depend on cross-file elaboration). -/
-- Ref: [manuscript] def:q-pochhammer-partial-product
def denomPolyLocal (q x : ℝ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => (1 - x * q ^ n) * denomPolyLocal q x n

/-- Local restatement of the partial product `Φ_n(x; q) = 1 / (x; q)_n`. -/
-- Ref: [manuscript] def:q-pochhammer-partial-product
noncomputable def partialProductLocal (q x : ℝ) (n : ℕ) : ℝ :=
  (denomPolyLocal q x n)⁻¹

/-- Bloch-Wigner placeholder.  Like `LiTwo`, this stands in for the
    real-valued `Real.dilog`-derived Bloch-Wigner function `D(z)`
    until Mathlib provides a complete formalisation of the classical
    dilogarithm. -/
-- Ref: [manuscript] rem:kashaev-volume-density
opaque BlochWignerD : ℝ → ℝ

/-- The algebraic-geometric equivalence, as a typeclass over a state
    variable `x` and depth `n`.  An instance asserts:

    * (`pole_cusp_bijection`) Each denominator zero `x = q^{-k}` of
      `(x; q)_n` is matched with a unique cusp index of the
      Φ_q-piece's ideal-tetrahedron triangulation.

    * (`asymptotic_volume`) Under Faddeev's scaling, the rescaled
      log of the partial product converges to the Bloch-Wigner
      volume at the matched shape parameter.

    The two fields are the algebraic and asymptotic halves of the
    Kashaev-Murakami-Murakami theorem in the QOU-native form. -/
-- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence
class AlgebraicGeometricEquivalence
    (q x : ℝ) (n : ℕ) : Prop where
  /-- Algebraic side: a function from cusp indices `k < n` to the
      matching denominator zero `q^{-k}`. -/
  -- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence §1
  pole_cusp_bijection :
    ∃ z : Fin n → ℝ, ∀ k : Fin n, z k = q ^ (-(k : ℤ))
  /-- Asymptotic side: the rescaled log partial product converges to
      the Bloch-Wigner volume of the matched ideal tetrahedron. The
      hypothesis `(q, n)` ranges over Faddeev's joint scaling. -/
  -- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence §2
  asymptotic_volume :
    ∀ ε > (0 : ℝ),
      ∃ N : ℕ, ∀ m, N ≤ m →
        ‖(1 - q) * Real.log (partialProductLocal q x m)
          - BlochWignerD x‖ < ε

/-- Stated equivalence theorem (conjecture instance form). -/
-- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence
noncomputable def algebraic_geometric_equivalence
    (q x : ℝ) (n : ℕ) [h : AlgebraicGeometricEquivalence q x n] :
    (∃ z : Fin n → ℝ, ∀ k : Fin n, z k = q ^ (-(k : ℤ))) ∧
    (∀ ε > (0 : ℝ), ∃ N : ℕ, ∀ m, N ≤ m →
      ‖(1 - q) * Real.log (partialProductLocal q x m)
        - BlochWignerD x‖ < ε) :=
  ⟨h.pole_cusp_bijection, h.asymptotic_volume⟩

/-! ## The pole side is a THEOREM (not just the conjecture-class field)

The class field `pole_cusp_bijection` above asserts only
`∃ z, z k = q^{-k}` — vacuously true (it names the candidate zeros but never
asserts they *are* zeros of the denominator). The genuine §1 content — that each
`x = q^{-k}` is an actual **root** of `(x;q)_n` — is unconditional algebra and is
proved here sorry-free (mirroring the generic `QOU.QBeta.qPochDenom_eq_zero_at_pole`,
merged separately). Only the *cusp correspondence* (that these poles match the
ideal-tetrahedron cusps) and the §2 asymptotic remain the (open) volume
conjecture. -/

/-- Structural unfold of the `n+1` step (definitional). -/
theorem denomPolyLocal_succ (q x : ℝ) (n : ℕ) :
    denomPolyLocal q x (n + 1) = (1 - x * q ^ n) * denomPolyLocal q x n := rfl

/-- **Pole vanishing (theorem).** `(x; q)_n` vanishes at each pole `x = q^{-j}`,
    `j < n` (`q ≠ 0`) — the unconditional algebraic half of
    `conj:algebraic-geometric-dilog-equivalence §1`. -/
-- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence §1
theorem denomPolyLocal_eq_zero_at_pole (q : ℝ) (hq : q ≠ 0)
    (n j : ℕ) (hj : j < n) : denomPolyLocal q (q ^ (-(j : ℤ))) n = 0 := by
  induction n with
  | zero => exact absurd hj (Nat.not_lt_zero j)
  | succ m ih =>
    rw [denomPolyLocal_succ]
    rcases (Nat.lt_succ_iff.mp hj).lt_or_eq with h | h
    · rw [ih h, mul_zero]
    · have key : q ^ (-(j : ℤ)) * q ^ (m : ℕ) = 1 := by
        rw [h, ← zpow_natCast q m, ← zpow_add₀ hq, neg_add_cancel, zpow_zero]
      rw [key, sub_self, zero_mul]

/-- **Theorem-backed pole side.** The strengthened §1 statement the class field
    omits: the explicit root function `k ↦ q^{-k}` together with the proof that
    each value is a genuine zero of `(x; q)_n`. Unconditional for `q ≠ 0`. -/
-- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence §1
theorem pole_cusp_bijection_proved (q : ℝ) (hq : q ≠ 0) (n : ℕ) :
    ∃ z : Fin n → ℝ, (∀ k : Fin n, z k = q ^ (-(k : ℤ)))
      ∧ (∀ k : Fin n, denomPolyLocal q (z k) n = 0) :=
  ⟨fun k => q ^ (-(k : ℤ)), fun _ => rfl,
    fun k => denomPolyLocal_eq_zero_at_pole q hq n k k.isLt⟩

end QOU.QPochhammer
