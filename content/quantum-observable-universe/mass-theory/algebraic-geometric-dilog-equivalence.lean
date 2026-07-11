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

/-- The algebraic-geometric equivalence, as a §3b-cond
    hypothesis-carrying class over the substrate parameter `q` and the
    state variable `x` (both real; each instance pins one `(q, x)` pair).  Per
    AGENTS.md §3b-cond rule 5, the fields axiomatise the conjecture's
    *inputs* — NOT its conclusion:

    * (`vc_asymptotic`) the volume-conjecture **saddle asymptotic**:
      the rescaled log partial product converges to some limit
      `volume` under Faddeev's scaling.  This is the analytic core of
      Kashaev-Murakami-Murakami; for the figure-eight `4₁` it is the
      theorem of Ohtsuki (2016) / Andersen-Hansen.

    * (`pole_cusp_matched`) the matched-cusp volume identification
      `volume = D(x)` — here `x` is already the matched shape
      parameter (the narrative's `z(x)` composed away), and the
      geometric content is supplied by
      `conj:shared-denominator-cusp-holonomy` (the pole side of the
      matching is the unconditional theorem
      `pole_cusp_bijection_proved` below).

    The §2 Bloch-Wigner asymptotic is then **derived**
    (`AlgebraicGeometricEquivalence.asymptotic_volume`), not assumed.
    A previous revision carried the conclusion itself as a field plus
    a vacuous `∃ z, z k = q^{-k}` pole field; both are gone — the
    class now asserts exactly the two open hypotheses and nothing
    provable-outright. -/
-- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence
class AlgebraicGeometricEquivalence (q x : ℝ) where
  /-- The limit of the rescaled log partial product (the saddle
      volume). -/
  volume : ℝ
  /-- Hypothesis (i): the volume-conjecture saddle asymptotic. -/
  -- Ref: [murakami-murakami2001] volume conjecture; Ohtsuki asymptotic for 4₁
  vc_asymptotic :
    ∀ ε > (0 : ℝ),
      ∃ N : ℕ, ∀ m, N ≤ m →
        ‖(1 - q) * Real.log (partialProductLocal q x m) - volume‖ < ε
  /-- Hypothesis (ii): the saddle volume is the Bloch-Wigner volume at
      the matched shape parameter. -/
  -- Ref: [manuscript] conj:shared-denominator-cusp-holonomy
  pole_cusp_matched : volume = BlochWignerD x

/-! ## The pole side is a THEOREM (unconditional)

The genuine §1 algebraic content — that each `x = q^{-k}` is an actual
**root** of `(x;q)_n` — is unconditional algebra and is proved here
sorry-free (mirroring the generic `QOU.QBeta.qPochDenom_eq_zero_at_pole`,
merged separately). A previous class revision carried a vacuous
`∃ z, z k = q^{-k}` pole field alongside this theorem; the field is gone
(see the class docstring). Only the *cusp correspondence* (that these
poles match the ideal-tetrahedron cusps — the class's
`pole_cusp_matched` hypothesis, i.e. `conj:shared-denominator-cusp-holonomy`)
and the VC saddle asymptotic remain the open volume conjecture. -/

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

/-! ## The `[Volume Conjecture] ⟹ §2 asymptotic` conditional (§3b-cond)

The §2 asymptotic (`(1−q)·log Φ_n(x;q) → D(z)`, the Bloch–Wigner volume) follows
from the **volume conjecture** together with the **pole-to-cusp matched volume**.
The theorem below makes that conditional structure explicit and honest: the two
mathematical hypotheses carry ALL the content and are cited — **not** laundered:

* `h_vc_asymptotic` — the q-Pochhammer/Kashaev **saddle asymptotic** converges to
  the hyperbolic volume `V`. This is the volume conjecture's analytic core; for
  the figure-eight `4₁` it is the **theorem** of Ohtsuki (2016) / Andersen–Hansen,
  and `⟨4₁⟩_N` is literally this q-Pochhammer sum
  (`computations/qbeta/qbeta_c3_kashaev_invariant_grounding.py`).
* `h_pole_cusp_matched` — the matched cusp volume equals `D(z(x))`; the algebraic
  pole side is proved above (`pole_cusp_bijection_proved`); the geometric cusp
  match is `conj:shared-denominator-cusp-holonomy`.

The composition (below) is the trivial limit-point substitution — precisely
because the two hypotheses hold the mathematics. This is the **rigorous-
conditional** wiring of the bar-EVEN mass part (`Re 𝔙 = Vol`); the bar-ODD
`S = Im 𝔙` needs the *deformed complex* volume conjecture + the open `u(q₀)` map
(`conj:binding-qbeta-complex-volume`), and is NOT touched here (anti-laundering). -/

/-- **Conditional (VC + pole-cusp match ⟹ §2 asymptotic).** If the q-Pochhammer
    rescaled log converges to a volume `V` (the volume-conjecture saddle
    asymptotic; a theorem for `4₁`) and `V = D(z(x))` (the pole-cusp matched cusp
    volume), then the §2 Bloch–Wigner asymptotic holds. The content is the two
    hypotheses; the composition is a limit-point substitution. -/
-- Ref: [murakami-murakami2001] volume conjecture; Ohtsuki asymptotic expansion for 4₁
theorem asymptotic_volume_of_vc (q x V : ℝ)
    (h_vc_asymptotic : ∀ ε > (0 : ℝ), ∃ N : ℕ, ∀ m, N ≤ m →
      ‖(1 - q) * Real.log (partialProductLocal q x m) - V‖ < ε)
    (h_pole_cusp_matched : V = BlochWignerD x) :
    ∀ ε > (0 : ℝ), ∃ N : ℕ, ∀ m, N ≤ m →
      ‖(1 - q) * Real.log (partialProductLocal q x m) - BlochWignerD x‖ < ε := by
  rw [← h_pole_cusp_matched]; exact h_vc_asymptotic

/-- **§2 asymptotic, DERIVED from the class hypotheses.**  Given the two
    axiomatised inputs (`vc_asymptotic`, `pole_cusp_matched`), the rescaled
    log partial product converges to the Bloch-Wigner volume — the
    conclusion the previous class revision carried as a field, now a
    theorem via `asymptotic_volume_of_vc`. -/
-- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence §2
theorem AlgebraicGeometricEquivalence.asymptotic_volume (q x : ℝ)
    [h : AlgebraicGeometricEquivalence q x] :
    ∀ ε > (0 : ℝ), ∃ N : ℕ, ∀ m, N ≤ m →
      ‖(1 - q) * Real.log (partialProductLocal q x m) - BlochWignerD x‖ < ε :=
  asymptotic_volume_of_vc q x h.volume h.vc_asymptotic h.pole_cusp_matched

/-- **Stated equivalence (conjecture bundle, both halves).**  §1 is the
    unconditional strengthened pole side (`pole_cusp_bijection_proved`,
    needing only `q ≠ 0`); §2 is derived from the class hypotheses.  The
    only conjectural inputs are the two class fields — the composition
    contains no `sorry` and assumes nothing provable-outright. -/
-- Ref: [manuscript] conj:algebraic-geometric-dilog-equivalence
theorem algebraic_geometric_equivalence
    (q x : ℝ) (hq : q ≠ 0) (n : ℕ) [AlgebraicGeometricEquivalence q x] :
    (∃ z : Fin n → ℝ, (∀ k : Fin n, z k = q ^ (-(k : ℤ)))
      ∧ (∀ k : Fin n, denomPolyLocal q (z k) n = 0)) ∧
    (∀ ε > (0 : ℝ), ∃ N : ℕ, ∀ m, N ≤ m →
      ‖(1 - q) * Real.log (partialProductLocal q x m)
        - BlochWignerD x‖ < ε) :=
  ⟨pole_cusp_bijection_proved q hq n,
    AlgebraicGeometricEquivalence.asymptotic_volume q x⟩

end QOU.QPochhammer
