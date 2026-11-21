import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import QOU.QBeta.CrossingWeightAffine

/-!
# G2 form-clash — the proved affine transport vs the axiomatised cosine (qou-avt1)

`QOU.QBeta.CrossingWeightAffine.evalMap_affine` proves the counit→trace transport
factor is **affine** in the crossing weight `w`, hence — reparametrised by the
counit-minus-trace gap `α := (z−1)h/2` (so that `ε − tr_M = evalMap h 1 −
evalMap h z = −h(z−1) = −2α`, the exact qou-avt1 identity) — the transport factor

  `T(α) = evalMap h z / evalMap h 1 = 1 − 4α / (h(h−2))`

is **linear** in `α`. Its even part `(T(α)+T(−α))/2` is therefore the constant `1`:
the affine transport carries **no** even-order content.

`QOU.Interactions.QBetaCosResummation` (axiomatised via the class
`TransferMatrixEigenphase`) asserts the Q_β correction is `cos α`, whose even part
is `cos α` itself, `= 1 − α²/2 + O(α⁴)` — **nonconstant**.

**Consequence (G2).** The two even parts agree only where `cos α = 1`, i.e.
`α ∈ 2πℤ` (`α = 0` at `q = 1`). So the entire `O(α²)` content of the cosine
resummation is carried by the axiom **alone**; nothing in the proved (KC19) affine
transport sources it — sharpening qou-avt1's "the cosine is the thing to drop"
into "the cosine is the *sole* carrier of the even-order correction", and
explaining the ~300× overshoot (a transport linear in `α` cannot source a
quadratic `α²` term).

This is a statement about functional **form** in `α`, independent of the Markov-`z`
convention (C vs D): `evalMap` is over a generic field and `α` is a free parameter,
so the form-clash is upstream of the C/D question that gates the *numerical* w*
(qou-cds1). Base ring: generic field for the affine half (§7c), `ℝ` only for the
cosine half (archimedean).

Companion: `computations/qbeta/qbeta_counit_trace_transport_overshoot_probe.py`
(G1–G5, 6/6). Verified `T` even-part = 1 symbolically (sympy) two ways before
formalising.

-- Ref: [leitner2026] prop:q-beta-cos-resummation
-/

namespace QOU.QBeta.LadderCosClash

open QOU.QBeta.CrossingWeightAffine

/-- The affine counit→trace transport factor as a function of the gap `α`, with a
    fixed kernel `k`: `T(α) = 1 − k·α`. Linear in `α`. -/
def transportFactor {R : Type*} [Ring R] (k α : R) : R := 1 - k * α

/-- **Even part of the affine transport is the constant `1`.** `T` is affine in
    `α`, so symmetrising `α ↦ −α` cancels the linear term: `T(α)+T(−α) = 2`. -/
theorem transport_even_sum {R : Type*} [CommRing R] (k α : R) :
    transportFactor k α + transportFactor k (-α) = 2 := by
  unfold transportFactor; ring

/-- The affine transport's odd part is `−k·α`: `T(α)−T(−α) = −2·k·α`, nonzero
    exactly when `k·α ≠ 0`. -/
theorem transport_odd_diff {R : Type*} [CommRing R] (k α : R) :
    transportFactor k α - transportFactor k (-α) = -(2 * (k * α)) := by
  unfold transportFactor; ring

/-- **The KC19 transport IS this affine `T`.** The proved ladder ratio
    `evalMap h z / evalMap h 1` (Möbius in `w`, `evalMap_ratio` at `w₀ = 1`),
    reparametrised by the gap `α = (z−1)h/2`, equals `transportFactor (4/(h(h−2))) α`.
    So `transportFactor` is not an abstract stand-in — it is the KC19 transport. -/
theorem evalMap_ratio_eq_transportFactor {R : Type*} [Field R] (h z : R)
    (hh : h ≠ 0) (htwo : (2 : R) ≠ 0) (hh2 : h - 2 ≠ 0) :
    evalMap h z / evalMap h 1
      = transportFactor (4 / (h * (h - 2))) ((z - 1) * h / 2) := by
  have hh2' : h - 2 * 1 ≠ 0 := by rwa [mul_one]
  rw [evalMap_ratio h z 1 hh htwo hh2', mul_one]
  unfold transportFactor
  have hprod : h * (h - 2) ≠ 0 := mul_ne_zero hh hh2
  field_simp
  ring

/-- `cos α < 1` on `(0, 2π)` — the cosine correction's even part is nonconstant. -/
theorem cos_lt_one_pos {α : ℝ} (h0 : 0 < α) (h2 : α < 2 * Real.pi) :
    Real.cos α < 1 := by
  rcases lt_or_eq_of_le (Real.cos_le_one α) with h | h
  · exact h
  · exfalso
    have hlt : -(2 * Real.pi) < α := by linarith [Real.pi_pos]
    have : α = 0 := (Real.cos_eq_one_iff_of_lt_of_lt hlt h2).mp h
    linarith

/-- **G2 form-clash.** At any gap `α ∈ (0, 2π)` the axiomatised cosine correction
    (even part `cos α < 1`) differs from the even part of the proved affine
    transport (the constant `1`). Hence the cosine's `O(α²)` content is unsourced
    by the KC19 transport and is carried by the axiom alone. -/
theorem cos_correction_ne_affine_even_part {α : ℝ} (h0 : 0 < α)
    (h2 : α < 2 * Real.pi) (k : ℝ) :
    Real.cos α ≠ (transportFactor k α + transportFactor k (-α)) / 2 := by
  have he : (transportFactor k α + transportFactor k (-α)) / 2 = 1 := by
    rw [transport_even_sum]; norm_num
  rw [he]
  exact ne_of_lt (cos_lt_one_pos h0 h2)

end QOU.QBeta.LadderCosClash

#print axioms QOU.QBeta.LadderCosClash.cos_correction_ne_affine_even_part
#print axioms QOU.QBeta.LadderCosClash.evalMap_ratio_eq_transportFactor
#print axioms QOU.QBeta.LadderCosClash.transport_even_sum
