/-
# Class B in `e = -ln b` letters: the `2 ln q` cap never used positivity

Archimedean specialisation (§7c) of `QOU/Hecke/BondCutSymmetryNoSignDefinite.lean`.
The generic file proves that a uniform energy shift leaves the p–n slope `δ`
exactly fixed and adds a pure volume term, and that beating the convex cap is
equivalent to putting the interface outside the convex hull. This file puts
those in bond-factor letters and composes them with the existing
`BondCutSymmetryLogBound.energySlope_convex_le_two_log`.

## The decisive reading of the existing bound

`energySlope_convex_le` takes `0 < b_nn`, `b_nn ≤ b_pp`, `0 ≤ w ≤ 1` — and
**nothing else**. In particular it never assumes `b ≤ 1`, which is what
`bondSum_nonneg` needs to make the energies non-negative. So invariant (1) of
`BondCutSymmetry` — `δ ≤ 2 ln q` for every convex interface, hence
`a_A^eff ≤ (k/2)·E₀·ln q` on a well-mixed degree-`k` graph — holds verbatim for
class B. `classB_symmetryCoeff_le_of_convex` and
`classB_rescaled_symmetryCoeff_le` state that composition explicitly, because
"the hypothesis is absent from the statement" is an observation and "the bound
still holds for a class-B instance" is a theorem.

**Positivity was never the binding constraint on the magnitude.** It was the
binding constraint on *one* thing only — the layout-free neutron-matter
argument, invariant (2) — and the generic sibling prices that escape as
`e_nn < 0`, i.e. `b_nn > 1`.

## Class B is reachable by a uniform rescaling, and costs exactly zero in `δ`

`exists_bondRescale_all_energies_neg`: for any positive bond factors there is a
common `c > 0` making all three energies strictly negative — a fully repulsive
law — with `δ` **unchanged**, because a common factor is a common additive shift
of the logarithms and `δ` is a second difference. So the uniform sub-class of B
is powerless on the symmetry term by an identity, not by an estimate.

Producer: `computations/qbeta/qbeta_class_b_nonsigndefinite_bond_probe.py`.
Bean `qou-brng`.
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.Hecke.BondCutSymmetryLogBound
import QOU.Hecke.BondCutSymmetryNoSignDefinite

namespace QOU.Hecke.BondCutSymmetryNoSignDefiniteLogBound

open QOU.Hecke.BondCutSymmetry
open QOU.Hecke.BondCutSymmetryLogBound
open QOU.Hecke.BondCutSymmetryNoSignDefinite

section Real

open Real

/-! ## Class B in bond-factor letters -/

/-- **Class B is `b > 1`.** A bond energy `e = -ln b` is negative — repulsive —
exactly when its bond factor exceeds one. This is the definition the enumeration
in bean `qou-brng` gives, made checkable against a derived number. -/
theorem energy_neg_iff_one_lt_bond {b : ℝ} (hb : 0 < b) :
    -Real.log b < 0 ↔ 1 < b := by
  constructor
  · intro h
    by_contra hc
    push_neg at hc
    have : Real.log b ≤ 0 := Real.log_nonpos hb.le hc
    linarith
  · intro h
    have : 0 < Real.log b := Real.log_pos h
    linarith

/-! ## A uniform bond rescaling leaves `δ` fixed -/

/-- **Rescaling all three bond factors by a common `c > 0` leaves `δ`
unchanged.** `ln (c·b) = ln c + ln b`, so every energy shifts by `-ln c` and the
generic `energySlope_energyShift` applies. -/
theorem energySlope_bondRescale {bpp bpn bnn c : ℝ}
    (hpp : 0 < bpp) (hpn : 0 < bpn) (hnn : 0 < bnn) (hc : 0 < c) :
    energySlope (-Real.log (c * bpp)) (-Real.log (c * bpn)) (-Real.log (c * bnn))
      = energySlope (-Real.log bpp) (-Real.log bpn) (-Real.log bnn) := by
  rw [Real.log_mul (ne_of_gt hc) (ne_of_gt hpp),
      Real.log_mul (ne_of_gt hc) (ne_of_gt hpn),
      Real.log_mul (ne_of_gt hc) (ne_of_gt hnn)]
  unfold energySlope
  ring

private lemma one_lt_scaled {x y z : ℝ} (hx : 0 < x) (hy : 0 < y) (hz : 0 < z) :
    1 < (1 / x + 1 / y + 1 / z) * x := by
  have h : (1 / x + 1 / y + 1 / z) * x = 1 + x / y + x / z := by
    field_simp
    ring
  have h1 : 0 < x / y := div_pos hx hy
  have h2 : 0 < x / z := div_pos hx hz
  rw [h]
  linarith

/-- **Class B is reachable from any positive law, at zero cost in `δ`.** For any
positive bond factors there is a common scale `c > 0` making all three energies
strictly negative — every bond repulsive, `bondSum_nonneg` fully escaped — while
the p–n slope, and hence the whole symmetry coefficient, is *identically* the
one before the rescaling.

So the cheapest and most natural way into class B changes nothing the symmetry
term sees. Whatever class B can do, it cannot do it uniformly. -/
theorem exists_bondRescale_all_energies_neg {bpp bpn bnn : ℝ}
    (hpp : 0 < bpp) (hpn : 0 < bpn) (hnn : 0 < bnn) :
    ∃ c : ℝ, 0 < c
      ∧ -Real.log (c * bpp) < 0 ∧ -Real.log (c * bpn) < 0 ∧ -Real.log (c * bnn) < 0
      ∧ energySlope (-Real.log (c * bpp)) (-Real.log (c * bpn)) (-Real.log (c * bnn))
          = energySlope (-Real.log bpp) (-Real.log bpn) (-Real.log bnn) := by
  set c : ℝ := 1 / bpp + 1 / bpn + 1 / bnn with hcdef
  have hc : 0 < c := by rw [hcdef]; positivity
  refine ⟨c, hc, ?_, ?_, ?_, energySlope_bondRescale hpp hpn hnn hc⟩
  · exact (energy_neg_iff_one_lt_bond (mul_pos hc hpp)).2 (by
      rw [hcdef]; exact one_lt_scaled hpp hpn hnn)
  · exact (energy_neg_iff_one_lt_bond (mul_pos hc hpn)).2 (by
      have hperm : c = 1 / bpn + 1 / bpp + 1 / bnn := by rw [hcdef]; ring
      rw [hperm]; exact one_lt_scaled hpn hpp hnn)
  · exact (energy_neg_iff_one_lt_bond (mul_pos hc hnn)).2 (by
      have hperm : c = 1 / bnn + 1 / bpp + 1 / bpn := by rw [hcdef]; ring
      rw [hperm]; exact one_lt_scaled hnn hpp hpn)

/-! ## The `2 ln q` cap holds for class B -/

/-- The pinned like-species ordering `b_nn ≤ b_pp`, extracted from
`BondCutSymmetryLogBound.energySlope_convex_le_two_log`'s proof so the class-B
statements below can reuse it. -/
theorem pinned_bnn_le_bpp {q : ℝ} (hq : 1 ≤ q) :
    (q ^ 2)⁻¹ / (q + 1 / q) ≤ q ^ 2 / (q + 1 / q) := by
  have hq0 : 0 < q := by linarith
  have hsum : 0 < q + 1 / q := by positivity
  apply div_le_div_of_nonneg_right _ hsum.le
  have h1 : (1 : ℝ) ≤ q ^ 2 := by nlinarith
  calc (q ^ 2)⁻¹ ≤ 1 := inv_le_one_of_one_le₀ h1
    _ ≤ q ^ 2 := h1

/-- The convex interface of a positive pair of like-species bonds is positive —
needed to rescale it. -/
theorem interface_pos {bpp bnn w : ℝ} (hnn : 0 < bnn) (h : bnn ≤ bpp)
    (hw0 : 0 ≤ w) (hw1 : w ≤ 1) : 0 < interface bpp bnn w :=
  lt_of_lt_of_le hnn (interface_mem h hw0 hw1).1

/-- **Invariant (1) holds for class B: the symmetry coefficient of any convex
interface is at most `(μ/4)·2 ln q`, with no sign hypothesis on any energy.**
Composition of `energySlope_convex_le_two_log` with the generic monotonicity
`symmetryCoeff_le_of_energySlope_le`. On a well-mixed degree-`k` graph
(`μ = k/A`, `bondSum_wellMixed_symmetry`) this is `a_A^eff ≤ (k/2)·E₀·ln q`. -/
theorem classB_symmetryCoeff_le_of_convex {q w μ : ℝ} (hq : 1 ≤ q)
    (hw0 : 0 ≤ w) (hw1 : w ≤ 1) (hμ : 0 < μ) :
    symmetryCoeff (-Real.log (q ^ 2 / (q + 1 / q)))
        (-Real.log (interface (q ^ 2 / (q + 1 / q)) ((q ^ 2)⁻¹ / (q + 1 / q)) w))
        (-Real.log ((q ^ 2)⁻¹ / (q + 1 / q))) μ
      ≤ 2 * Real.log q * μ / 4 :=
  symmetryCoeff_le_of_energySlope_le hμ (energySlope_convex_le_two_log hq hw0 hw1)

/-- **The same cap after the class-B rescaling.** Rescale all three pinned bonds
by any `c > 0` — in particular by one large enough to make every energy negative
(`exists_bondRescale_all_energies_neg`) — and the bound is *the same number*.
Class B's cap equals the positive class's cap, identically, not approximately. -/
theorem classB_rescaled_symmetryCoeff_le {q w μ c : ℝ} (hq : 1 ≤ q)
    (hw0 : 0 ≤ w) (hw1 : w ≤ 1) (hμ : 0 < μ) (hc : 0 < c) :
    symmetryCoeff (-Real.log (c * (q ^ 2 / (q + 1 / q))))
        (-Real.log (c * interface (q ^ 2 / (q + 1 / q)) ((q ^ 2)⁻¹ / (q + 1 / q)) w))
        (-Real.log (c * ((q ^ 2)⁻¹ / (q + 1 / q)))) μ
      ≤ 2 * Real.log q * μ / 4 := by
  have hq0 : 0 < q := by linarith
  have hsum : 0 < q + 1 / q := by positivity
  have hbpp : 0 < q ^ 2 / (q + 1 / q) := by positivity
  have hbnn : 0 < (q ^ 2)⁻¹ / (q + 1 / q) := by positivity
  have hbpn : 0 < interface (q ^ 2 / (q + 1 / q)) ((q ^ 2)⁻¹ / (q + 1 / q)) w :=
    interface_pos hbnn (pinned_bnn_le_bpp hq) hw0 hw1
  refine symmetryCoeff_le_of_energySlope_le hμ ?_
  rw [energySlope_bondRescale hbpp hbpn hbnn hc]
  exact energySlope_convex_le_two_log hq hw0 hw1

/-! ## The dichotomy in bond-factor letters -/

/-- **Beating the convex cap forces the interface below *both* like-species
bonds.** If `δ` exceeds `(ln b_pp - ln b_nn)/2` then `b_pn < b_nn`: the p–n bond
factor is strictly smaller than the smaller like-species factor, so it is not a
convex combination of them and is not derived by
`SymmetrySignAmGm.weight_of_convention`. No sign hypothesis is used, so class B
does not change this. -/
theorem interface_below_of_gt_convexCap {bpp bpn bnn : ℝ} (hnn : 0 < bnn)
    (h : (Real.log bpp - Real.log bnn) / 2
          < energySlope (-Real.log bpp) (-Real.log bpn) (-Real.log bnn)) :
    bpn < bnn := by
  have h' : (-Real.log bnn - -Real.log bpp) / 2
      < energySlope (-Real.log bpp) (-Real.log bpn) (-Real.log bnn) := by linarith
  have hlt := (energySlope_gt_convexCap_iff (-Real.log bpp) (-Real.log bpn)
    (-Real.log bnn)).mp h'
  by_contra hcon
  push_neg at hcon
  have := Real.log_le_log hnn hcon
  linarith

/-- **The pinned form.** With `b_pp = q²/[2]_q`, `b_nn = q⁻²/[2]_q`, the cap is
exactly `2 ln q` (`half_splitting_pinned`), so any law whose slope exceeds
`2 ln q` — which is what supplying the SEMF `a_A` requires, by
`bondSum_wellMixed_symmetry` — has its interface strictly below `b_nn`. -/
theorem interface_below_of_gt_two_log {q bpn : ℝ} (hq : 0 < q)
    (h : 2 * Real.log q
          < energySlope (-Real.log (q ^ 2 / (q + 1 / q))) (-Real.log bpn)
              (-Real.log ((q ^ 2)⁻¹ / (q + 1 / q)))) :
    bpn < (q ^ 2)⁻¹ / (q + 1 / q) := by
  have hsum : 0 < q + 1 / q := by positivity
  have hbnn : 0 < (q ^ 2)⁻¹ / (q + 1 / q) := by positivity
  refine interface_below_of_gt_convexCap hbnn ?_
  rw [show (Real.log (q ^ 2 / (q + 1 / q)) - Real.log ((q ^ 2)⁻¹ / (q + 1 / q))) / 2
        = 2 * Real.log q from half_splitting_pinned hq]
  exact h

end Real

end QOU.Hecke.BondCutSymmetryNoSignDefiniteLogBound
