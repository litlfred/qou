/-
  The golden-ratio threshold and the convention-C Toffoli diagonal.

  SCOPE CORRECTED 2026-08-30 (bean qou-3j5m).  This file used to be
  titled "LP-dual stability of the q-Toffoli braid" and to state that
  the q-Toffoli diagonal numerator is P₇₇(q) = q + q^(1/2) - 1, whose
  zero q⋆ = 1/φ² = (3 - √5)/2 is the stability threshold.  That
  numerator belongs to the EXCISED convention C (z_C = √q/(q+1)).
  Under the canonical convention D (z_D = q³/(q²+1)) the diagonal is

      P₇₇(q) = q³(q⁴+1)/(q²+1)²,

  strictly positive on q > 0 with NO positive zero — so the golden
  threshold is a property of the excised frame, not of the gate, and
  LP-stability is not equivalent to the positivity below.  See
  content/quantum-observable-universe/information-theory/
  toffoli-lp-stability.md items 1-2 and the derivation probe
  computations/probes/toffoli_trio_rederivation.py.

  What survives, and is what this file actually proves, is the real
  analysis:      q > q⋆   ↔   q + √q - 1 > 0.
  It is a true and self-contained fact about f(q) = q + √q - 1; only
  the identification of f with a live Toffoli amplitude is withdrawn.

  Proof structure:
    1. Golden-ratio identity: (√5 - 1)/2 squared equals q⋆, so
       √q⋆ = (√5 - 1)/2 and q⋆ + √q⋆ - 1 = 0.
    2. Monotonicity: f(q) := q + √q - 1 is strictly increasing on
       [0, ∞) since both q ↦ q and q ↦ √q are monotone.
    3. Combine: f(q) > 0 ↔ q > q⋆ (via strict monotonicity and
       evaluation at q⋆).
    4. For q ≤ 0, Real.sqrt returns 0, so f(q) = q - 1 ≤ -1 < 0,
       and q⋆ > 0 > q, so both sides false.

**Ground ring**: R_q = ℤ[q, q⁻¹]. Under convention D the diagonal
numerator is q³(q⁴+1) = q⁷ + q³, an honest element of R_q — no
q^(1/2) and hence no extension is needed. The convention-C numerator
q + q^(1/2) - 1 was what required R_q[q^(1/2)].
-/
import QOU.QuantumObservableUniverse
import QOU.GroundRingCore
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt

namespace QOU.Information

noncomputable section

/-- The Toffoli diagonal numerator in the base ring `R_q`, under the
    canonical convention D: `P₇₇(q) = q³(q⁴+1)/(q²+1)²` has numerator
    `q³(q⁴+1) = q⁷ + q³`.  This is exact, not a stub — the convention-D
    diagonal is a Laurent polynomial over a positive denominator, so
    unlike its convention-C predecessor `q + q^(1/2) - 1` it needs no
    square-root extension of `R_q`. -/
def toffoli_diag_numerator : QOU.GroundRing.R_q :=
  QOU.GroundRing.q_param ^ 7 + QOU.GroundRing.q_param ^ 3

/-- The golden ratio `φ = (1 + √5) / 2`. -/
noncomputable def phi_golden : ℝ := (1 + Real.sqrt 5) / 2

/-- The golden-ratio threshold `q⋆ = (3 - √5) / 2 = 1 / φ²`. -/
noncomputable def q_star_threshold : ℝ := (3 - Real.sqrt 5) / 2

/-- **Golden-ratio threshold identity.** `q⋆ · φ² = 1`.
    Closed-form identity underpinning `prop:toffoli-lp-stability`. -/
theorem q_star_golden_square :
    q_star_threshold * phi_golden ^ 2 = 1 := by
  unfold q_star_threshold phi_golden
  have h5 : Real.sqrt 5 * Real.sqrt 5 = 5 :=
    Real.mul_self_sqrt (by norm_num : (0 : ℝ) ≤ 5)
  nlinarith [h5, Real.sqrt_nonneg 5]

/-- `0 < q⋆`: the golden-ratio threshold is strictly positive. -/
theorem q_star_pos : 0 < q_star_threshold := by
  unfold q_star_threshold
  have h5_lt_9 : Real.sqrt 5 < 3 := by
    have h : Real.sqrt 5 < Real.sqrt 9 := by
      apply Real.sqrt_lt_sqrt <;> norm_num
    simpa [show Real.sqrt 9 = 3 from by
      rw [show (9 : ℝ) = 3 ^ 2 from by norm_num, Real.sqrt_sq (by norm_num : (0 : ℝ) ≤ 3)]] using h
  linarith

/-- `√q⋆ = (√5 - 1) / 2`.  Equivalently, `q⋆ = ((√5 - 1)/2)²`. -/
theorem sqrt_q_star :
    Real.sqrt q_star_threshold = (Real.sqrt 5 - 1) / 2 := by
  have h5_ge_1 : (1 : ℝ) ≤ Real.sqrt 5 := by
    have : Real.sqrt 1 ≤ Real.sqrt 5 := Real.sqrt_le_sqrt (by norm_num)
    simpa [Real.sqrt_one] using this
  have h_nn : 0 ≤ (Real.sqrt 5 - 1) / 2 := by linarith
  have h_sq : ((Real.sqrt 5 - 1) / 2) ^ 2 = q_star_threshold := by
    unfold q_star_threshold
    have h5 : Real.sqrt 5 * Real.sqrt 5 = 5 :=
      Real.mul_self_sqrt (by norm_num : (0 : ℝ) ≤ 5)
    nlinarith [h5]
  calc Real.sqrt q_star_threshold
      = Real.sqrt (((Real.sqrt 5 - 1) / 2) ^ 2) := by rw [h_sq]
    _ = (Real.sqrt 5 - 1) / 2 := Real.sqrt_sq h_nn

/-- **Value at the threshold**: `q⋆ + √q⋆ - 1 = 0`. -/
theorem f_at_q_star :
    q_star_threshold + Real.sqrt q_star_threshold - 1 = 0 := by
  rw [sqrt_q_star]
  unfold q_star_threshold
  ring

/-- **Monotonicity of `f(q) = q + √q - 1` on `[0, ∞)`.** Strict. -/
theorem f_strict_mono {a b : ℝ} (ha : 0 ≤ a) (hab : a < b) :
    a + Real.sqrt a - 1 < b + Real.sqrt b - 1 := by
  have hsqrt_le : Real.sqrt a ≤ Real.sqrt b :=
    Real.sqrt_le_sqrt (le_of_lt hab)
  linarith

/-- **The golden-ratio threshold of `f(q) = q + √q - 1`.**
    `f` is positive exactly above q⋆ = (3 - √5) / 2 = 1 / φ².

    SCOPE (2026-08-30): this is a statement about the real function `f`
    and nothing else.  `f` is the numerator of the **convention-C**
    Toffoli diagonal, which is excised; the canonical convention-D
    diagonal `q³(q⁴+1)/(q²+1)²` is positive for every `q > 0` and has
    no threshold.  So this theorem no longer establishes LP-stability
    of the q-Toffoli, and must not be cited for it — see the file
    header.  The proof below is unchanged and remains correct.
    Label: prop:toffoli-lp-stability
    Ref: [manuscript] Chapter 8, prop:toffoli-transfer-matrix
    Ref: [manuscript] Chapter 4, prop:lp-dual-stability -/
theorem toffoli_lp_stable (q : ℝ) :
    q_star_threshold < q ↔ 0 < q + Real.sqrt q - 1 := by
  constructor
  · -- Forward: q > q⋆ ⇒ f(q) > 0.
    intro hq
    have hqstar_nn : 0 ≤ q_star_threshold := le_of_lt q_star_pos
    have := f_strict_mono hqstar_nn hq
    linarith [f_at_q_star]
  · -- Reverse: f(q) > 0 ⇒ q > q⋆. Contrapositive on q ≤ q⋆.
    intro hf
    by_contra hle
    push_neg at hle
    rcases lt_or_eq_of_le hle with hlt | heq
    · -- q < q⋆.
      by_cases hq_nn : 0 ≤ q
      · have := f_strict_mono hq_nn hlt
        linarith [f_at_q_star]
      · -- q < 0: √q = 0 by Real.sqrt convention.
        push_neg at hq_nn
        have hsqrt_zero : Real.sqrt q = 0 :=
          Real.sqrt_eq_zero'.mpr (le_of_lt hq_nn)
        rw [hsqrt_zero] at hf
        linarith
    · -- q = q⋆: f = 0, contradicts hf.
      rw [heq] at hf
      linarith [f_at_q_star]

/-  REMOVED 2026-08-30 (bean qou-3j5m): `toffoli_shadow_bounded`.

    It read `∃ κ : ℝ, 0 < κ ∧ κ < 10`, discharged by `⟨303/100, …⟩`.
    Two independent reasons it had to go.

    (1) It was vacuous in the sense of AGENTS.md §"No trivial trues":
        the statement mentions no Toffoli, no Gram matrix and no q, so
        it is provable without any hypothesis about the objects it
        claims to be about.  Exhibiting 3.03 proves that 3.03 lies in
        (0, 10), nothing more.

    (2) The number itself is withdrawn.  κ(G(q₀)) ≈ 3.03 came from a
        Gram matrix built with the retracted naive length rule
        tr_M(T_w) = z^ℓ(w) under the excised convention C, in float64,
        at a superseded q₀; under convention D the Markov–Gram form is
        singular, so λ_max/|λ_min| is not a condition number at all.
        The content block withdrew the figure on 2026-08-09
        (toffoli-lp-stability.md item 3); this file kept it.

    There is nothing to restate here: a real shadow-price bound needs
    the radical-quotient ruling first.
-/

end

end QOU.Information
