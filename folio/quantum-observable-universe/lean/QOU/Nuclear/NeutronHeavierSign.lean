import QOU.Nuclear.FlavourWeightSplit
import QOU.MassTheory.UrsellPartitionFunctionB3

/-!
# Which reading of trace → mass makes the neutron heavier?

Thread "Settle the neutron-heavier sign", bean `qou-99qc`. The owner ruling of 2026-11-20 (D2)
fixed that `|ε_flavour(V³)|·E₀ = 0.3254 MeV` is `Q_β`, and left the sign of the mass ordering
open (np-splitting audit §23). Under "mass ∝ trace" the ruled trace makes the neutron lighter
(`FlavourWeightSplit.epsFlavour_V3_neg`). This file asks the question for every reading of
trace → mass that the corpus contains, and answers it.

## Setting (all owner rulings in force)

* Photon `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`; nucleon element `V³ = (σ₀σ₁⁻¹)³`, the two-photon
  product `γ(0,0,qh)·γ(0,0,−q⁻¹h)`; electron `σ₀σ₁σ₀ ∈ B₃` (Hopf-link closure); up quark an
  unknot strand, `u = e₁`.
* Two-term Lagrangian trace `τ(𝒟²) + τ(ψ*𝒟ψ)`, evaluated with the quantum trace
  `Tr(K^{⊗3}·)/[2]³`, `K = diag(q, q⁻¹)`.
* On the proton weight space `W_p = (2,1)` the Cartan weight `K^{⊗3}` is `q`; on
  `W_n = (1,2)` it is `q⁻¹`. For every element `X` of the braid-group algebra the plain traces on
  `W_p` and `W_n` agree (`NucleonWeightSpaceTraces.trace_word_eq` for positive words; for
  `V³` by `trace_borromeanV3A` / `trace_borromeanV3B`; the probe checks all 1364 signed words of
  length ≤ 5, the symbolic photon product and the electron word inserted).

So every sector value is `ε_p = q·t/[2]³`, `ε_n = q⁻¹·t/[2]³` with one common `t`. That is the
whole of the flavour content, and it is what decides every reading below.

## The readings, and what each gives (q > 1, the wall side the corpus evaluates on)

| reading (corpus source) | m_n > m_p? | theorem |
|---|---|---|
| R1 signed linear, `m ∝ ε` (`Q_β = |ε(Δ)|·E₀` without `|·|`) | iff `t < 0`; on `V³`, no | `signed_reading_iff`, `V3_signed_reading_neutron_lighter` |
| R2 any increasing function of `|sector trace|` (m_p identity uses `|tr_M|`) | never | `increasing_reading_neutron_lighter`, `V3_increasing_reading_neutron_lighter` |
| R3 any decreasing function (old n–p block: "more negative Φ is more confinement") | always | `antitone_reading_neutron_heavier` |
| R4 bar side `0 < q < 1` | reverses R2 | `bar_side_reverses` |
| R5 one flip of the pivot `K ↦ K⁻¹` or of the label `u = e₂` | swaps p and n | `single_flip_swaps` |
| R6 both flips (Cartan involution ω) | same as R2 | `cartan_involution_invariant` |
| R7 two-term static matter term `c·Q_pair` or `c·Q_self` | flips only if `c < −3(q − q⁻¹)` | `twoTerm_diff_eq`, `twoTerm_neutron_lighter`, `twoTerm_flip_iff` |
| R8 electron as a spectator tensor factor, trace `c_e > 0` | same as R2 | `spectator_preserves` |
| R9 kinematic `m_n − m_p = Q_β + m_e`, `Q_β = |ε|·E₀` | yes, but blind to the sign of `ε` | `kinematic_reading_sign_blind` |

The ruled covariant matter term (all pairs, connected) is exactly `0` on `V³` (main,
`deltaT_allPairs_connected_eq_zero`), so the two-term trace equals the one-term trace there and
R7 is about the static (unscored) charge terms only.

## What this settles (scope)

* **Structural (scope (b)) for R2:** no reading of the form `mass = f(|sector trace|)` with `f`
  increasing makes the neutron heavier, for any element of the braid-group algebra and any
  `q > 1`. The invariant is the equality of plain traces on `W_p`, `W_n` (the intertwiner `P(q)`)
  plus `q⁻¹ < q`. Adding the electron as a spectator, or the static two-term charge terms with
  `c ≥ 0`, does not change this.
* The readings that do give `m_n > m_p` are: R3 (an orientation asserted in one sentence of the
  old n–p block, opposite to the production `m_p` identity, which is increasing in `|tr_M|`);
  R4 (the sub-wall side, which the corpus does not evaluate on); R5 (each single flip is excluded
  by a proved corpus theorem: `OverStrandWeight.ptr_other_not_scalar` for `K⁻¹`, and the
  over/under rule of `OverStrandWeight` for `u = e₂`); R1 on an element with `t < 0` (`V³` has
  `t > 0`); R9 (the sign is supplied by `|·|` and kinematics, not by the trace).
* Not covered here: the FE-alone second-order insertion of np-splitting §22, which gives
  `t_n > t_p` but is a choice between FE and EF (the symmetric FE + EF gives `q⁻²` exactly,
  `NucleonWeightSpaceTwoTerm.trace_twoTerm_with_secondOrder_eq`).
* No numerical value enters. The abstract part is over any ordered field; the `V³` instances
  use `ℝ` because `polyP_neg` does (§7c).
-/

namespace QOU.QBeta.NeutronHeavierSign

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.QBeta.FlavourWeightSplit

section Abstract

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- Normalisation `[2]³ = (q + q⁻¹)³`. -/
def d3 (q : R) : R := (q + q⁻¹) ^ 3

/-- Proton sector value of a common plain trace `t`: `K^{⊗3} = q` on `W_p`. -/
def secP (q t : R) : R := q * t / d3 q

/-- Neutron sector value of a common plain trace `t`: `K^{⊗3} = q⁻¹` on `W_n`. -/
def secN (q t : R) : R := q⁻¹ * t / d3 q

theorem d3_pos {q : R} (hq : 0 < q) : 0 < d3 q := by
  unfold d3; have := inv_pos.mpr hq; positivity

theorem inv_lt_self_of_one_lt {q : R} (hq : 1 < q) : q⁻¹ < q :=
  lt_trans (inv_lt_one_of_one_lt₀ hq) hq

theorem abs_secP {q : R} (hq : 0 < q) (t : R) : |secP q t| = q * |t| / d3 q := by
  unfold secP
  rw [abs_div, abs_mul, abs_of_pos hq, abs_of_pos (d3_pos hq)]

theorem abs_secN {q : R} (hq : 0 < q) (t : R) : |secN q t| = q⁻¹ * |t| / d3 q := by
  unfold secN
  rw [abs_div, abs_mul, abs_of_pos (inv_pos.mpr hq), abs_of_pos (d3_pos hq)]

/-- **Core inequality.** Above the wall, the neutron sector value is strictly smaller in
absolute value whenever the common trace is non-zero. -/
theorem abs_secN_lt_abs_secP {q t : R} (hq : 1 < q) (ht : t ≠ 0) :
    |secN q t| < |secP q t| := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  rw [abs_secN hq0, abs_secP hq0]
  apply div_lt_div_of_pos_right _ (d3_pos hq0)
  exact mul_lt_mul_of_pos_right (inv_lt_self_of_one_lt hq) (abs_pos.mpr ht)

theorem abs_secN_le_abs_secP {q : R} (hq : 1 < q) (t : R) : |secN q t| ≤ |secP q t| := by
  rcases eq_or_ne t 0 with h | h
  · subst h; simp [secN, secP]
  · exact (abs_secN_lt_abs_secP hq h).le

/-- **R2.** Every strictly increasing reading of the absolute sector trace makes the
neutron lighter. -/
theorem increasing_reading_neutron_lighter {q t : R} (hq : 1 < q) (ht : t ≠ 0)
    (f : R → R) (hf : StrictMono f) : f |secN q t| < f |secP q t| :=
  hf (abs_secN_lt_abs_secP hq ht)

/-- **R2, weak form.** A merely monotone reading never makes the neutron heavier. -/
theorem monotone_reading_neutron_not_heavier {q : R} (hq : 1 < q) (t : R)
    (f : R → R) (hf : Monotone f) : f |secN q t| ≤ f |secP q t| :=
  hf (abs_secN_le_abs_secP hq t)

/-- **R3.** Every strictly decreasing reading makes the neutron heavier. -/
theorem antitone_reading_neutron_heavier {q t : R} (hq : 1 < q) (ht : t ≠ 0)
    (f : R → R) (hf : StrictAnti f) : f |secP q t| < f |secN q t| :=
  hf (abs_secN_lt_abs_secP hq ht)

/-- The signed difference, closed form. -/
theorem secN_sub_secP (q t : R) : secN q t - secP q t = (q⁻¹ - q) * t / d3 q := by
  unfold secN secP; ring

/-- **R1.** Under the signed linear reading the neutron is heavier iff the common trace is
negative. -/
theorem signed_reading_iff {q t : R} (hq : 1 < q) : secP q t < secN q t ↔ t < 0 := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hd := d3_pos hq0
  have hneg : q⁻¹ - q < 0 := sub_neg.mpr (inv_lt_self_of_one_lt hq)
  rw [← sub_pos, secN_sub_secP, div_pos_iff_of_pos_right hd]
  constructor
  · intro h; by_contra h'; push_neg at h'
    exact absurd h (not_lt.mpr (mul_nonpos_of_nonpos_of_nonneg hneg.le h'))
  · intro h; exact mul_pos_of_neg_of_neg hneg h

/-- **R4.** On the bar side `0 < q < 1` the inequality of R2 reverses. -/
theorem bar_side_reverses {q t : R} (hq0 : 0 < q) (hq1 : q < 1) (ht : t ≠ 0) :
    |secP q t| < |secN q t| := by
  rw [abs_secN hq0, abs_secP hq0]
  apply div_lt_div_of_pos_right _ (d3_pos hq0)
  have : q < q⁻¹ := lt_trans hq1 (one_lt_inv_iff₀.mpr ⟨hq0, hq1⟩)
  exact mul_lt_mul_of_pos_right this (abs_pos.mpr ht)

/-- Sector value with a pivot sign `s` (`+1`: `K`, `−1`: `K⁻¹`) and a label sign `l`
(`+1`: `u = e₁`, `−1`: `u = e₂`). The proton weight space has `K^{⊗3}`-eigenvalue
`q^{s·l}`, the neutron one `q^{−s·l}`. -/
def secGen (q : R) (s l : ℤ) (isProton : Bool) (t : R) : R :=
  (if isProton then q ^ (s * l) else q ^ (-(s * l))) * t / d3 q

omit [LinearOrder R] [IsStrictOrderedRing R] in
theorem secGen_ruled (q t : R) :
    secGen q 1 1 true t = secP q t ∧ secGen q 1 1 false t = secN q t := by
  refine ⟨?_, ?_⟩ <;> simp [secGen, secP, secN, zpow_neg]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **R6.** The Cartan involution (both flips at once) leaves both sector values unchanged. -/
theorem cartan_involution_invariant (q t : R) :
    secGen q (-1) (-1) true t = secP q t ∧ secGen q (-1) (-1) false t = secN q t := by
  refine ⟨?_, ?_⟩ <;> simp [secGen, secP, secN, zpow_neg]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **R5.** One flip alone (pivot or label) swaps the proton and neutron sector values. -/
theorem single_flip_swaps (q t : R) :
    secGen q (-1) 1 true t = secN q t ∧ secGen q (-1) 1 false t = secP q t ∧
    secGen q 1 (-1) true t = secN q t ∧ secGen q 1 (-1) false t = secP q t := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> simp [secGen, secP, secN, zpow_neg]

/-- Two-term static charge insertion: `Q_pair` (or `Q_self`) adds `c·(−1/3)·t` on the neutron
relative to the proton (`trace_twoTerm_QPair_diff_word`). -/
def twoTermN (q c t : R) : R := (q⁻¹ + c * (-1 / 3)) * t / d3 q

theorem twoTerm_diff_eq (q c t : R) :
    twoTermN q c t - secP q t = (q⁻¹ - q - c / 3) * t / d3 q := by
  unfold twoTermN secP; ring

/-- **R7.** With a non-negative static charge coupling, the two-term neutron value stays below
the proton value on a positive trace. -/
theorem twoTerm_neutron_lighter {q c t : R} (hq : 1 < q) (hc : 0 ≤ c) (ht : 0 < t) :
    twoTermN q c t < secP q t := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  rw [← sub_neg, twoTerm_diff_eq]
  apply div_neg_of_neg_of_pos _ (d3_pos hq0)
  apply mul_neg_of_neg_of_pos _ ht
  have := inv_lt_self_of_one_lt hq
  linarith

/-- **R7, threshold.** On a positive trace the two-term static charge term reverses the sign
exactly when `c < −3(q − q⁻¹)`. -/
theorem twoTerm_flip_iff {q c t : R} (hq : 0 < q) (ht : 0 < t) :
    secP q t < twoTermN q c t ↔ c < -3 * (q - q⁻¹) := by
  rw [← sub_pos, twoTerm_diff_eq, div_pos_iff_of_pos_right (d3_pos hq),
    mul_pos_iff_of_pos_right ht]
  constructor <;> intro h <;> linarith

/-- **R8.** An electron (or any spectator) carried as a common tensor factor with positive
trace `c_e` keeps the R2 inequality and the sign of the signed difference. -/
theorem spectator_preserves {q t ce : R} (hq : 1 < q) (ht : t ≠ 0) (hce : 0 < ce) :
    |secN q (ce * t)| < |secP q (ce * t)| ∧
    (secP q (ce * t) < secN q (ce * t) ↔ secP q t < secN q t) := by
  refine ⟨abs_secN_lt_abs_secP hq (mul_ne_zero hce.ne' ht), ?_⟩
  rw [signed_reading_iff hq, signed_reading_iff hq]
  exact ⟨fun h => neg_of_mul_neg_right h hce.le, fun h => mul_neg_of_pos_of_neg hce h⟩

/-- **R9.** The kinematic reading `m_n − m_p = |ε|·E₀ + m_e` is positive, and it takes the same
value for `ε` and `−ε`: the sign comes from `|·|`, not from the trace. -/
theorem kinematic_reading_sign_blind {eps E0 me : R} (hE : 0 < E0) (hm : 0 < me) :
    0 < |eps| * E0 + me ∧ |-eps| * E0 + me = |eps| * E0 + me := by
  refine ⟨by positivity, by rw [abs_neg]⟩

end Abstract

/-! ## Instances on the ruled element `V³` and on every positive word -/


/-! ## Coloured strands (two-colour Yokonuma–Hecke `Y₂,₃`), owner choice 2026-11-21

Flavour as a strand colour: `u ↦ t = +1`, `d ↦ t = −1`. The colour flip `φ : t ↦ −t, g ↦ g` is an
algebra automorphism, and the Juyumaya trace at `x = 0` is `φ`-invariant. Both facts are checked
exactly and exhaustively over `ℚ(q, z, x)` by `np_yokonuma_flip_probe.py` (all 48 × 48 basis
products, all 48 basis traces; pre-registered in `np_yokonuma_flip_preregistration.md`). They enter
below as hypotheses, not as Lean facts. Given them, the neutron sector trace equals the proton one
for every flip-fixed element, so no reading of trace → mass orders the two. -/

section Coloured

variable {S A : Type*} [CommRing S] [Ring A] [Algebra S A]

/-- A flip-invariant trace gives the flipped colour sector the same value on every flip-fixed
element: `τ(φ(π)·W) = τ(π·W)`. -/
theorem flip_sector_eq (φ : A ≃ₐ[S] A) (τ : A →ₗ[S] S) (hτ : ∀ a, τ (φ a) = τ a)
    (π W : A) (hW : φ W = W) : τ (φ π * W) = τ (π * W) := by
  conv_lhs => rw [← hW, ← map_mul]
  exact hτ _

/-- Hence no reading `m` of trace → mass, monotone or not, makes the neutron heavier (or lighter)
under coloured strands at the admissible trace. -/
theorem coloured_no_order {T : Type*} [Preorder T] (φ : A ≃ₐ[S] A) (τ : A →ₗ[S] S)
    (hτ : ∀ a, τ (φ a) = τ a) (πp W : A) (hW : φ W = W) (m : S → T) :
    m (τ (φ πp * W)) = m (τ (πp * W)) := by
  rw [flip_sector_eq φ τ hτ πp W hW]

end Coloured

section ColouredX

variable {R : Type*} [CommRing R]

/-- The probe's symbolic `n − p` (for every listed word except the half twist, where it is `0`):
`x(x−1)(x+1)/4`. It is odd in `x`, so the sign of `n − p` is the sign choice of `x`. -/
theorem colouredDiff_odd (x : R) :
    (-x) * (-x - 1) * (-x + 1) = -(x * (x - 1) * (x + 1)) := by ring

/-- It vanishes at all three E-system values `x ∈ {1, 0, −1}`; so no admissible `x` orders `n`
and `p`. -/
theorem colouredDiff_eSystem (x : R) (hx : x = 1 ∨ x = 0 ∨ x = -1) :
    x * (x - 1) * (x + 1) = 0 := by
  rcases hx with rfl | rfl | rfl <;> ring

end ColouredX

section ColouredBonds

open QOU.MassTheory.UrsellPartitionFunctionB3 in
/-- **Coloured bonds, 2026-11-22 (`np_mirror_and_bonds_probe.py`).** With isospin as a Yokonuma
colour, every candidate bond letter (g², the γγ bond G³, with or without the mirror rule) gives
the unlike bond factor `μ_pn = 1` exactly (the single crossing g gives `μ_pn = 0`, no log). The
probe's value enters as a hypothesis. Given it, an `A = 3` nucleus has the two unlike pairs at
`f = 1`, and the connected three-body cumulant vanishes whatever the like bond is: neither sign. -/
theorem coloured_unlike_unit_b3_zero {R : Type*} [CommRing R] (fLike : R) :
    b3corpus 1 fLike 1 = 0 := by
  unfold b3corpus W Z3; ring

end ColouredBonds

section Ruled

/-- The ruled sector values on `V³` are the abstract ones with the common trace `tr(V³)`. -/
theorem V3_sectors (q : ℝ) (hq : q ≠ 0) :
    epsP q (borromeanV3A q) = secP q (trace (borromeanV3A q)) ∧
    epsN q (borromeanV3B q) = secN q (trace (borromeanV3A q)) := by
  refine ⟨rfl, ?_⟩
  unfold epsN secN d3 qd2
  rw [trace_borromeanV3B q hq, trace_borromeanV3A q hq]

theorem trace_V3_pos {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) : 0 < trace (borromeanV3A q) := by
  have hq : q ≠ 0 := by positivity
  rw [trace_borromeanV3A q hq]
  have := polyP_neg hq1 hq2
  unfold polyP at this
  apply div_pos _ (by positivity)
  linarith

/-- **R2 on `V³`.** -/
theorem V3_increasing_reading_neutron_lighter {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (f : ℝ → ℝ) (hf : StrictMono f) :
    f |epsN q (borromeanV3B q)| < f |epsP q (borromeanV3A q)| := by
  obtain ⟨hp, hn⟩ := V3_sectors q (by positivity)
  rw [hp, hn]
  exact increasing_reading_neutron_lighter hq1 (trace_V3_pos hq1 hq2).ne' f hf

/-- **R1 on `V³`.** -/
theorem V3_signed_reading_neutron_lighter {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) :
    epsN q (borromeanV3B q) < epsP q (borromeanV3A q) := by
  obtain ⟨hp, hn⟩ := V3_sectors q (by positivity)
  rw [hp, hn]
  rcases lt_trichotomy (secN q (trace (borromeanV3A q))) (secP q (trace (borromeanV3A q)))
    with h | h | h
  · exact h
  · have := sub_eq_zero.mpr h
    rw [secN_sub_secP] at this
    have hq0 : (0 : ℝ) < q := by linarith
    have hne : (q⁻¹ - q) * trace (borromeanV3A q) ≠ 0 :=
      mul_ne_zero (sub_neg.mpr (inv_lt_self_of_one_lt hq1)).ne (trace_V3_pos hq1 hq2).ne'
    exact absurd this (div_ne_zero hne (d3_pos hq0).ne')
  · exact absurd ((signed_reading_iff hq1).mp h) (not_lt.mpr (trace_V3_pos hq1 hq2).le)

/-- **R2 on every positive braid word.** For any word `w` in `σ₁, σ₂` and any strictly
increasing reading `f`, the neutron is not heavier, and strictly lighter when `tr(w) ≠ 0`. -/
theorem word_increasing_reading_neutron_lighter {q : ℝ} (hq1 : 1 < q) (w : List Bool)
    (ht : trace (word (A₁ q) (A₂ q) w) ≠ 0) (f : ℝ → ℝ) (hf : StrictMono f) :
    f |secN q (trace (word (B₁ q) (B₂ q) w))| < f |secP q (trace (word (A₁ q) (A₂ q) w))| := by
  have hq : q ≠ 0 := by positivity
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  rw [← trace_word_eq q hq hq2 w]
  exact increasing_reading_neutron_lighter hq1 ht f hf

/-! Axiom audit. -/
#print axioms V3_increasing_reading_neutron_lighter
#print axioms V3_signed_reading_neutron_lighter
#print axioms word_increasing_reading_neutron_lighter
#print axioms antitone_reading_neutron_heavier
#print axioms twoTerm_flip_iff
#print axioms cartan_involution_invariant
#print axioms single_flip_swaps
#print axioms bar_side_reverses
#print axioms spectator_preserves
#print axioms kinematic_reading_sign_blind
#print axioms flip_sector_eq
#print axioms coloured_no_order
#print axioms colouredDiff_eSystem
#print axioms coloured_unlike_unit_b3_zero

end Ruled

end QOU.QBeta.NeutronHeavierSign
