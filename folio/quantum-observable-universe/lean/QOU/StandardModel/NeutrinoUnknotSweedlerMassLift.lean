/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.MassTheory.ParticleKnots
import QOU.Confinement.WeakScaleFactorisation
import QOU.BraidsAndKnots.WeakVertexT35TraceClosedForm
import TwistedFrobeniusHopf.SweedlerJet
import TwistedFrobeniusHopf.SweedlerFrobenius
import QOU.Nuclear.SweedlerWeakDegreeCount
import QOU.StandardModel.LeptonNumberCarrierChirality
import QOU.Confinement.YukawaVacuumPairing
import Mathlib.Data.ZMod.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

/-!
# Non-Zero Unknot `0₁` Neutrino Mass Lift, Sweedler Weak See-Saw Scaling, & Dirac vs Majorana Framing (`qou-nu01`)

Beans: `qou-nu01`, `qou-qydm`, `qou-sm8w` (`Q-Gap-10`).

Formalizes, with `0 sorry`, `0` custom axioms, and `0` empirical inputs (strictly following `§7c`
generic base-ring discipline over `[CommRing R]`, `[Field K]`, and `[Field F] [LinearOrder F]
[IsStrictOrderedRing F]`, with explicit `_real` specializations):

1. **Section 1 — Bare Unknot `0₁` Tree Vanishing vs Sweedler & 2-Loop `T(3,5)` Weak Mass Lift:**
   - The canonical `ParticleKnots.Neutrino` / `Antineutrino` unknot carrier has zero hyperbolic
     volume, zero crossings, zero genus, and zero tree-level volume-channel mass
     (`unknot_tree_invariants_and_volumeMass_zero`).
   - On the 2-state lepton doublet `(0 = ν_L, 1 = e_L⁻)` with Sweedler lowering `leptonF = E₁₀`
     and conjugate raising `leptonE = E₀₁`, like-chirality double insertions vanish
     (`leptonF * D * leptonF = 0`, `leptonE * D * leptonE = 0`), whereas the charged-current
     self-energy sandwich `leptonE * leptonDiag 0 me * leptonF = me • Pu` projects strictly onto
     the neutral `ν_L` projector `Pu = E₀₀` even when the bare neutrino slot is massless
     (`lepton_selfEnergy_projects_neutral_slot`).
   - Weighted by `k` Sweedler weak-passage channels `(q² - 1)^k` (`sweedlerMassLift`) or the
     two-vertex `T(3,5)` weak Markov trace `weakVertexTrace q ^ 2` (`t35TwoLoopSweedlerLift`),
     both lifts vanish at `q = 1` for `k ≥ 1`, are **strictly positive** for all `q > 1` and
     `me > 0`, and decrease strictly with `k` across the substrate regime `1 < q` and `q² < 2`
     (`sweedlerMassLift_pos`, `t35TwoLoopSweedlerLift_pos`, `sweedlerMassLift_strictAnti`).

2. **Section 2 — Dirac (`ℤ`-Framing) vs Majorana (`ℤ₂`-Quotient), Sweedler Order-4 Antipode,
   & Bare `ΔL = 2` Obstruction vs Dimension-5 Weinberg `(LH)²` Singlet:**
   - Oriented `ℤ`-framed unknots `(0₁, ±w)` (`w ≠ 0`) move under bar/mirror negation `w ↦ -w`,
     supporting lepton number `L = ±1` (`LeptonNumberCarrierChirality`), conserving framing on
     Dirac pairs `w + (-w) = 0`, and forbidding `ΔL = 2` pairs `w + w = 2w ≠ 0`. Passing to the
     unoriented `ℤ₂` framing quotient `ZMod 2` fixes every element (`-z = z`), triggering
     `no_lepton_number_on_amphichiral_carrier` while trivializing `z + z = 0`.
   - In `QOU.LiftingDescent.Sweedler k`, the squared antipode `S²` is the inner automorphism by `G`
     (`S²(a) = G a G`), satisfying **`S²(X) = -X`** (`S⁴ = id`, exact order `4` when `2` is a unit,
     `sweedler_antipode_sq_ne_id`), while `nakayama G = -G ≠ S²(G)` witnesses non-unimodularity.
   - On the neutral `Q = 0` slot (`2T₃ = +1, Y = -1`), any bare `ΔL = 2` bilinear invariant under
     `q^{2T₃}` kills `B(ν_L, ν_L) = 0` (`q² ≠ 1`), and invariance under `q^Y` kills `B = 0`
     identically (`bare_majorana_bilinear_forbidden`). Conversely, while the linear antisymmetric
     `(LH)` contraction `ε_ew(v, w) = v₀ w₁ - v₁ w₀` is odd (`-1`) under `Δ(G)`, its **quadratic
     dimension-5 Weinberg square** `O_W = ε_ew(L₁, H₁) · ε_ew(L₂, H₂)` is strictly invariant under
     the full 4-fold Sweedler coproduct (`Δ⁽³⁾(G)` and `Δ⁽³⁾(X)`), neutral under `(2T₃, Y, 3Q)`,
     and at the neutral Higgs vev `H = (0, v_EW)` reduces to `v_EW² (L₁)₀ (L₂)₀` purely on `ν_L`
     (`weinberg_quadratic_singlet_sweedler_invariant_and_vev`).

3. **Section 3 — 3-Generation `S₃ ⊃ S₂` Perturbation Algebra & NH vs IH Eigenvalue Ratios:**
   - Exact characterization of the `S₃ = Perm (Fin 3)` commutant as `a • 1 + b • demJ3`
     (`s3_commutant_iff`), diagonalization and determinant factorization
     `det(s3NeutralMass a b ε) = a (a + 6ε) (a + 3b)` of the `S₃ ⊃ S₂` neutral mass operator,
     closed-form NH and IH squared-splitting ratios, and the radical-free ordered-field theorem
     `∑ m_ν(NH) < ∑ m_ν(IH)` for any matched `(Δm₂₁², |Δm₃₂|²)` with `2 Δm₂₁² < |Δm₃₂|²`
     (`nh_mass_sum_lt_ih_of_matched_splittings`).

-- Ref: [leitner2026] beans qou-nu01, qou-qydm, qou-sm8w
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §III
-- Ref: [taft1971] Proc. Nat. Acad. Sci. USA 68 (1971) 2631–2633
-- Ref: [larson-sweedler1969] Amer. J. Math. 91 (1969) 75–94
-/

namespace QOU.StandardModel.NeutrinoUnknotSweedlerMassLift

open Matrix
open QOU.Archimedean (Neutrino Antineutrino R_q)
open QOU.QuarkState.WeakScaleFactorisation (volumeMass)
open QOU.Braiding.WeakVertexT35 (weakVertexTrace weakVertexTrace_one)
open QOU.LiftingDescent (Sweedler)
open QOU.QBeta.SweedlerWeakDegreeCount
  (leptonF leptonG leptonDiag leptonSweedlerHom singlePassageAmp singlePassageAmp_eq
    multiChannelAmp sweedler_weak_degree_ladder)
open QOU.StandardModel
  (no_lepton_number_on_amphichiral_carrier mirror_must_move_the_carrier
    chiral_carrier_admits_lepton_number)
open QOU.QuarkState.YukawaVacuumPairing (Pu Pd Invariant)

/-! ## Section 1: Bare Unknot `0₁` Tree Vanishing vs Sweedler & 2-Loop `T(3,5)` Weak Lift -/

section TreeVanishingAndSelfEnergy

/-- **Tree-Level Unknot `0₁` Vanishing (`ParticleKnots.Neutrino` & `volumeMass`):**
the canonical neutrino and antineutrino unknot carriers have zero hyperbolic volume, zero crossing
number, zero Seifert genus, zero electric charge, and identically zero tree-level volume-channel
mass `volumeMass me 0 ρ ħ = 0` over any field `K`. -/
theorem unknot_tree_invariants_and_volumeMass_zero {K : Type*} [Field K] (me ρ ħ : K) :
    ({} : Neutrino).volume = (0 : R_q) ∧
    ({} : Antineutrino).volume = (0 : R_q) ∧
    ({} : Neutrino).crossing_number = 0 ∧
    ({} : Neutrino).genus = 0 ∧
    ({} : Neutrino).charge = 0 ∧
    volumeMass me 0 ρ ħ = 0 := by
  refine ⟨rfl, rfl, rfl, rfl, rfl, ?_⟩
  unfold volumeMass
  ring

/-- Single-lepton raising transition `E : e⁻ (1) ↦ ν (0)` on `Matrix (Fin 2) (Fin 2) R`,
conjugate transpose of `SweedlerWeakDegreeCount.leptonF`. -/
def leptonE {R : Type*} [CommRing R] : Matrix (Fin 2) (Fin 2) R := !![0, 1; 0, 0]

theorem leptonE_eq_transpose_leptonF {R : Type*} [CommRing R] :
    (leptonE : Matrix (Fin 2) (Fin 2) R) = (leptonF : Matrix (Fin 2) (Fin 2) R)ᵀ := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [leptonE, leptonF]

/-- **Charged-Current Self-Energy Projects Strictly onto the Neutral `ν_L` Slot (`Pu = E₀₀`):**
over any commutative ring `R`, while like-sign weak transitions `F · D · F = 0` and `E · D · E = 0`
annihilate every diagonal lepton propagator `D = diag(a, b)`, the self-energy sandwich
`E · diag(a, b) · F` (`ν_L → e⁻ → ν_L`) equals `b • !![1, 0; 0, 0]`, which depends **solely** on
the charged-lepton mass slot `b` and remains nonzero (`me • E₀₀`) even at bare `a = 0`! -/
theorem lepton_selfEnergy_projects_neutral_slot {R : Type*} [CommRing R] (a b : R) :
    (leptonF : Matrix (Fin 2) (Fin 2) R) * leptonDiag a b * leptonF = 0 ∧
    (leptonE : Matrix (Fin 2) (Fin 2) R) * leptonDiag a b * leptonE = 0 ∧
    (leptonE : Matrix (Fin 2) (Fin 2) R) * leptonDiag a b * leptonF =
      b • !![(1 : R), 0; 0, 0] := by
  refine ⟨QOU.QBeta.SweedlerWeakDegreeCount.leptonF_mul_diag_mul_leptonF_eq_zero a b, ?_, ?_⟩
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [leptonE, leptonDiag, Matrix.mul_apply, Fin.sum_univ_two]
  · ext i j
    fin_cases i <;> fin_cases j <;>
      simp [leptonE, leptonF, leptonDiag, Matrix.mul_apply, Fin.sum_univ_two]

/-- Over a field `K`, `leptonE * leptonDiag 0 me * leptonF = me • Pu` (using `YukawaVacuumPairing.Pu`). -/
theorem lepton_selfEnergy_zero_bare_nu_eq_Pu {K : Type*} [Field K] (me : K) :
    (leptonE : Matrix (Fin 2) (Fin 2) K) * leptonDiag 0 me * leptonF = me • Pu := by
  rw [(lepton_selfEnergy_projects_neutral_slot (0 : K) me).2.2]
  rfl

end TreeVanishingAndSelfEnergy

section SweedlerMassLiftGenericField

variable {K : Type*} [Field K]

/-- Zero-parameter Sweedler `k`-channel weak-jet neutrino mass scale `m_e · (q (q - q⁻¹))^k`. -/
def sweedlerMassLift (k : ℕ) (me q : K) : K :=
  me * multiChannelAmp k q

/-- Two-vertex `T(3,5)` weak Markov-trace self-energy dressed Sweedler lift
`m_e · W_{T(3,5)}(q)² · (q (q - q⁻¹))^k`. -/
noncomputable def t35TwoLoopSweedlerLift (k : ℕ) (me q : K) : K :=
  me * weakVertexTrace q ^ 2 * multiChannelAmp k q

/-- Dimension-5 Weinberg see-saw mass scale `v_EW² / M_UV`. -/
def weinbergSeesawScale (vEW mUV : K) : K :=
  vEW ^ 2 / mUV

/-- Exact `(q² - 1)^k` closed form for `sweedlerMassLift` and `t35TwoLoopSweedlerLift` (`q ≠ 0`). -/
theorem sweedlerMassLift_eq (k : ℕ) (me q : K) (hq : q ≠ 0) :
    sweedlerMassLift k me q = me * (q ^ 2 - 1) ^ k ∧
    t35TwoLoopSweedlerLift k me q = me * weakVertexTrace q ^ 2 * (q ^ 2 - 1) ^ k := by
  unfold sweedlerMassLift t35TwoLoopSweedlerLift multiChannelAmp
  rw [singlePassageAmp_eq q hq]
  exact ⟨rfl, rfl⟩

/-- Explicit `#9204` `k = 8` (4-hop weak norm) and `k = 12` (6-hop / 2-loop weak radical) scales. -/
theorem sweedlerMassLift_eight_and_twelve (me q : K) (hq : q ≠ 0) :
    sweedlerMassLift 8 me q = me * (q ^ 2 - 1) ^ 8 ∧
    sweedlerMassLift 12 me q = me * (q ^ 2 - 1) ^ 12 :=
  ⟨(sweedlerMassLift_eq 8 me q hq).1, (sweedlerMassLift_eq 12 me q hq).1⟩

/-- **Classical `q = 1` Vacuum Vanishing:** for every positive channel count `k ≥ 1`, both
`sweedlerMassLift` and `t35TwoLoopSweedlerLift` vanish identically at `q = 1`. -/
theorem sweedlerMassLift_at_one_eq_zero {k : ℕ} (hk : 1 ≤ k) (me : K) :
    sweedlerMassLift k me 1 = 0 ∧ t35TwoLoopSweedlerLift k me 1 = 0 := by
  have hk0 : k ≠ 0 := Nat.one_le_iff_ne_zero.mp hk
  unfold sweedlerMassLift t35TwoLoopSweedlerLift multiChannelAmp singlePassageAmp
  simp [zero_pow hk0]

end SweedlerMassLiftGenericField

section SweedlerMassLiftOrderedField

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- For `1 ≤ q` in any strict ordered field, the `T(3,5)` Convention-D weak vertex trace
`W(q) = q²(q¹² + q⁸ - 1)/(q² + 1)²` is strictly positive. -/
theorem weakVertexTrace_pos_of_one_le (q : F) (hq1 : 1 ≤ q) :
    0 < weakVertexTrace q := by
  have hq0 : 0 < q := lt_of_lt_of_le zero_lt_one hq1
  have hq8 : 1 ≤ q ^ 8 := one_le_pow₀ hq1
  have hq12 : 1 ≤ q ^ 12 := one_le_pow₀ hq1
  have hnum : 0 < q ^ 2 * (q ^ 12 + q ^ 8 - 1) :=
    mul_pos (pow_pos hq0 2) (by linarith)
  have hden : 0 < (q ^ 2 + 1) ^ 2 := by positivity
  unfold weakVertexTrace
  exact div_pos hnum hden

/-- **Strict Positivity of the Sweedler Neutrino Mass Lift (`q > 1`):**
for `0 < me` and `1 < q` in any strict ordered field `F`, `0 < sweedlerMassLift k me q` for all `k`. -/
theorem sweedlerMassLift_pos (k : ℕ) {me q : F} (hme : 0 < me) (hq1 : 1 < q) :
    0 < sweedlerMassLift k me q := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq1
  rw [(sweedlerMassLift_eq k me q (ne_of_gt hq0)).1]
  have hq2 : 0 < q ^ 2 - 1 := by nlinarith
  exact mul_pos hme (pow_pos hq2 k)

/-- **Strict Positivity of the 2-Loop `T(3,5)` Weak Self-Energy Neutrino Mass Lift (`q > 1`).** -/
theorem t35TwoLoopSweedlerLift_pos (k : ℕ) {me q : F} (hme : 0 < me) (hq1 : 1 < q) :
    0 < t35TwoLoopSweedlerLift k me q := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq1
  rw [(sweedlerMassLift_eq k me q (ne_of_gt hq0)).2]
  have hw : 0 < weakVertexTrace q := weakVertexTrace_pos_of_one_le q (le_of_lt hq1)
  have hq2 : 0 < q ^ 2 - 1 := by nlinarith
  exact mul_pos (mul_pos hme (pow_pos hw 2)) (pow_pos hq2 k)

/-- **Strict Positivity of the Weinberg See-Saw Scale (`v_EW ≠ 0`, `M_UV > 0`).** -/
theorem weinbergSeesawScale_pos {vEW mUV : F} (hv : vEW ≠ 0) (hm : 0 < mUV) :
    0 < weinbergSeesawScale vEW mUV := by
  unfold weinbergSeesawScale
  exact div_pos (sq_pos_of_ne_zero hv) hm

/-- **Strict Exponential Suppression Across Channel Count `k` (`1 < q`, `q² < 2`):**
in the sub-unit Sweedler deformation window `1 < q` and `q² < 2` (`0 < q² - 1 < 1`), higher
channel counts strictly suppress the induced neutrino scale: `k₁ < k₂ → m_ν^{(k₂)} < m_ν^{(k₁)}`. -/
theorem sweedlerMassLift_strictAnti {k₁ k₂ : ℕ} {me q : F}
    (hk : k₁ < k₂) (hme : 0 < me) (hq1 : 1 < q) (hq2 : q ^ 2 < 2) :
    sweedlerMassLift k₂ me q < sweedlerMassLift k₁ me q := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq1
  rw [(sweedlerMassLift_eq k₂ me q (ne_of_gt hq0)).1,
    (sweedlerMassLift_eq k₁ me q (ne_of_gt hq0)).1]
  have hs0 : 0 < q ^ 2 - 1 := by nlinarith
  have hs1 : q ^ 2 - 1 < 1 := by linarith
  exact mul_lt_mul_of_pos_left (pow_lt_pow_right_of_lt_one₀ hs0 hs1 hk) hme

end SweedlerMassLiftOrderedField

section ArchimedeanSpecialization

/-- Prescribed `§7c` archimedean `ℝ` specialization of `sweedlerMassLift_pos`. -/
theorem sweedlerMassLift_pos_real (k : ℕ) {me q : ℝ} (hme : 0 < me) (hq1 : 1 < q) :
    0 < sweedlerMassLift k me q :=
  sweedlerMassLift_pos (F := ℝ) k hme hq1

/-- Prescribed `§7c` archimedean `ℝ` specialization of `t35TwoLoopSweedlerLift_pos`. -/
theorem t35TwoLoopSweedlerLift_pos_real (k : ℕ) {me q : ℝ} (hme : 0 < me) (hq1 : 1 < q) :
    0 < t35TwoLoopSweedlerLift k me q :=
  t35TwoLoopSweedlerLift_pos (F := ℝ) k hme hq1

end ArchimedeanSpecialization

/-! ## Section 2: Dirac vs Majorana Framing, Sweedler `S²(X) = -X`, & Weinberg `(LH)²` Singlet -/

section FramingDiracVsMajorana

/-- Orientation / bar reversal `w ↦ -w` on integer unknot framings (`TwistDatum.totalTwist_bar`). -/
def framedMirror (w : ℤ) : ℤ := -w

/-- **Oriented `ℤ`-Framing Supports Dirac Lepton Number & Forbids `ΔL = 2` Framing Violation:**
for every nonzero integer framing `w ≠ 0` (such as `(0₁, +1)` vs `(0₁, -1)`),
1. `framedMirror w ≠ w`, so `chiral_carrier_admits_lepton_number` provides `L(w) = 1`, `L(-w) = -1`;
2. Dirac particle–antiparticle pairing conserves total framing (`w + framedMirror w = 0`);
3. Majorana self-pairing violates `ℤ`-framing conservation (`w + w ≠ 0`). -/
theorem dirac_framing_conserves_and_forbids_majorana (w : ℤ) (hw : w ≠ 0) :
    framedMirror w ≠ w ∧
    (∃ L : ℤ → ℤ, L w = 1 ∧ L (framedMirror w) = -1) ∧
    w + framedMirror w = 0 ∧
    w + w ≠ 0 := by
  have hchiral : framedMirror w ≠ w := by
    unfold framedMirror
    omega
  exact ⟨hchiral, chiral_carrier_admits_lepton_number framedMirror w hchiral,
    by unfold framedMirror; omega, by omega⟩

/-- **Unoriented `ℤ₂` Framing Quotient (`w mod 2`) Obstructs `ℤ`-Lepton Number & Permits `Δw ≡ 0`:**
in `ZMod 2` (Kauffman/ribbon framing modulo Reidemeister-I double twists `±2`), negation fixes
every class (`-z = z`), identifying `(1 : ZMod 2) = (-1 : ZMod 2)` so
`no_lepton_number_on_amphichiral_carrier` rules out any `L(z) = +1, L(-z) = -1`, while every
self-pair satisfies `z + z = 0`. -/
theorem majorana_zmod2_quotient_kills_lepton_number_and_permits_pair :
    (∀ z : ZMod 2, -z = z) ∧
    ((1 : ZMod 2) = (-1 : ZMod 2)) ∧
    (∀ (L : ZMod 2 → ℤ) (z : ZMod 2), ¬ (L z = 1 ∧ L (-z) = -1)) ∧
    (∀ z : ZMod 2, z + z = 0) := by
  have hfix : ∀ z : ZMod 2, -z = z := by decide
  refine ⟨hfix, by decide, ?_, by decide⟩
  intro L z ⟨hp, ha⟩
  exact no_lepton_number_on_amphichiral_carrier (fun x : ZMod 2 => -x) L z (hfix z) hp ha

end FramingDiracVsMajorana

section SweedlerOrderFourAntipodeAndWeinberg

/-- **Squared Antipode `S²` on Sweedler's `H₄` Basis (`S²(X) = -X`, `S²(G) = G`):**
over any commutative ring `k`, `S²` fixes `{1, G}` and negates `{X, G X}`. -/
theorem sweedler_antipode_sq_basis (k : Type*) [CommRing k] :
    Sweedler.antipode k (Sweedler.antipode k 1) = 1 ∧
    Sweedler.antipode k (Sweedler.antipode k (Sweedler.G k)) = Sweedler.G k ∧
    Sweedler.antipode k (Sweedler.antipode k (Sweedler.X k)) = -Sweedler.X k ∧
    Sweedler.antipode k (Sweedler.antipode k (Sweedler.G k * Sweedler.X k)) =
      -(Sweedler.G k * Sweedler.X k) := by
  simp [Sweedler.antipode_one, Sweedler.antipode_G, Sweedler.antipode_X, Sweedler.antipode_GX]

/-- **Pivotal Inner Automorphism Law (`S²(a) = G a G`) & Order-4 Identity (`S⁴(a) = a`) on `H₄`:**
for every element `a : Sweedler k` over any commutative ring `k`:
1. `S²(a) = G * a * G` (`G` is the canonical group-like pivotal element of `H₄`),
2. `S⁴(a) = a`. -/
theorem sweedler_antipode_sq_eq_conj_G_and_pow_four (k : Type*) [CommRing k] (a : Sweedler k) :
    Sweedler.antipode k (Sweedler.antipode k a) = Sweedler.G k * a * Sweedler.G k ∧
    Sweedler.antipode k (Sweedler.antipode k (Sweedler.antipode k (Sweedler.antipode k a))) = a := by
  obtain ⟨c₀, c₁, c₂, c₃, rfl⟩ := Sweedler.exists_coords k a
  have h1 : Sweedler.G k * (1 : Sweedler k) * Sweedler.G k = 1 := by
    rw [mul_one, Sweedler.G_mul_G]
  have hG : Sweedler.G k * Sweedler.G k * Sweedler.G k = Sweedler.G k := by
    rw [Sweedler.G_mul_G, one_mul]
  have hX : Sweedler.G k * Sweedler.X k * Sweedler.G k = -Sweedler.X k := Sweedler.GX_mul_G k
  have hGX : Sweedler.G k * (Sweedler.G k * Sweedler.X k) * Sweedler.G k =
      -(Sweedler.G k * Sweedler.X k) := by
    rw [Sweedler.G_mul_GX, Sweedler.X_mul_G]
  refine ⟨?_, ?_⟩
  · simp only [map_add, map_smul, Sweedler.antipode_one, Sweedler.antipode_G,
      Sweedler.antipode_X, Sweedler.antipode_GX, map_neg]
    simp only [mul_add, add_mul, Algebra.mul_smul_comm, Algebra.smul_mul_assoc, h1, hG, hX, hGX,
      smul_neg]
  · simp only [map_add, map_smul, Sweedler.antipode_one, Sweedler.antipode_G,
      Sweedler.antipode_X, Sweedler.antipode_GX, map_neg, neg_neg]

/-- **Sweedler `S² ≠ id` Chirality Obstruction & Non-Unimodularity (`nakayama G ≠ S²(G)`):**
over any nontrivial commutative ring `k` in which `2` is a unit:
1. `S²(X) ≠ X` (`S` has exact order `4`, not `2`, obstructing an untwisted `S² = id` Majorana
   involution on the weak differential `X`);
2. `nakayama(G) = -G ≠ G = S²(G)` (`H₄` is non-unimodular: its Frobenius Nakayama twist differs
   from `S²` by the distinguished modulus on `G`). -/
theorem sweedler_antipode_sq_ne_id_and_nakayama_ne (k : Type*) [CommRing k] [Nontrivial k]
    (h2 : IsUnit (2 : k)) :
    Sweedler.antipode k (Sweedler.antipode k (Sweedler.X k)) ≠ Sweedler.X k ∧
    Sweedler.nakayama k (Sweedler.G k) ≠
      Sweedler.antipode k (Sweedler.antipode k (Sweedler.G k)) := by
  refine ⟨?_, ?_⟩
  · intro heq
    rw [(sweedler_antipode_sq_basis k).2.2.1] at heq
    have h2X : (2 : k) • Sweedler.X k = 0 := by
      calc (2 : k) • Sweedler.X k
          = Sweedler.X k + Sweedler.X k := two_smul k _
        _ = -Sweedler.X k + Sweedler.X k := by nth_rw 1 [← heq]
        _ = 0 := neg_add_cancel _
    have hf : Sweedler.frob k (Sweedler.G k * ((2 : k) • Sweedler.X k)) =
        Sweedler.frob k (Sweedler.G k * 0) := by rw [h2X]
    rw [Algebra.mul_smul_comm, mul_zero, map_smul, map_zero, Sweedler.frob_GX, smul_eq_mul,
      mul_one] at hf
    exact h2.ne_zero hf
  · intro hnak
    have hG : Sweedler.nakayama k (Sweedler.G k) = -Sweedler.G k := by
      unfold Sweedler.nakayama
      exact Sweedler.lift_G ..
    rw [hG, (sweedler_antipode_sq_basis k).2.1] at hnak
    have h2G : (2 : k) • Sweedler.G k = 0 := by
      calc (2 : k) • Sweedler.G k
          = Sweedler.G k + Sweedler.G k := two_smul k _
        _ = -Sweedler.G k + Sweedler.G k := by nth_rw 1 [← hnak]
        _ = 0 := neg_add_cancel _
    have hf : Sweedler.frob k (((2 : k) • Sweedler.G k) * Sweedler.X k) =
        Sweedler.frob k (0 * Sweedler.X k) := by rw [h2G]
    rw [Algebra.smul_mul_assoc, zero_mul, map_smul, map_zero, Sweedler.frob_GX, smul_eq_mul,
      mul_one] at hf
    exact h2.ne_zero hf

/-- **Bare `ΔL = 2` Bilinear Obstruction on the `Q = 0` Lepton Doublet (`2T₃ = ±1, Y = -1`):**
let `c2T3 = ![1, -1]` (`2T₃` on `(ν_L, e_L⁻)`) and `cY = ![-1, -1]` (`Y = -1` on `(ν_L, e_L⁻)`).
Although `ν_L` is electrically neutral (`2T₃ + Y = 0`), over any field `K` with `q² ≠ 1`:
1. Every `q^{2T₃}`-invariant bilinear `B : L ⊗ L → K` satisfies `B 0 0 = 0` (`ν_L ν_L` killed)
   and `B 1 1 = 0`;
2. Every `q^Y`-invariant bilinear `B : L ⊗ L → K` vanishes identically (`B = 0`). -/
theorem bare_majorana_bilinear_forbidden {K : Type*} [Field K]
    (q : K) (hq2 : q ^ 2 ≠ 1) (B : Matrix (Fin 2) (Fin 2) K) :
    (Invariant q ![1, -1] ![1, -1] B → B 0 0 = 0 ∧ B 1 1 = 0) ∧
    (Invariant q ![-1, -1] ![-1, -1] B → B = 0) := by
  have hsub : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hq2
  have hinv2 : (q⁻¹) ^ 2 - 1 ≠ 0 := by
    intro hz
    have h1 : (q⁻¹) ^ 2 = 1 := sub_eq_zero.mp hz
    apply hq2
    calc q ^ 2 = ((q⁻¹) ^ 2)⁻¹ := by rw [inv_pow, inv_inv]
      _ = 1 := by rw [h1, inv_one]
  refine ⟨?_, ?_⟩
  · intro hT3
    have h00 := hT3 0 0
    have h11 := hT3 1 1
    simp only [Matrix.cons_val_zero, Matrix.cons_val_one, zpow_one, zpow_neg_one,
      ← sq] at h00 h11
    have e00 : (q ^ 2 - 1) * B 0 0 = 0 := by linear_combination h00
    have e11 : ((q⁻¹) ^ 2 - 1) * B 1 1 = 0 := by linear_combination h11
    exact ⟨(mul_eq_zero.mp e00).resolve_left hsub, (mul_eq_zero.mp e11).resolve_left hinv2⟩
  · intro hY
    have cell0 : ∀ i j : Fin 2, q ^ (-1 : ℤ) * q ^ (-1 : ℤ) * B i j = B i j → B i j = 0 := by
      intro i j hij
      rw [zpow_neg_one, ← sq] at hij
      have eij : ((q⁻¹) ^ 2 - 1) * B i j = 0 := by linear_combination hij
      exact (mul_eq_zero.mp eij).resolve_left hinv2
    ext i j
    have hij := hY i j
    fin_cases i <;> fin_cases j <;> exact cell0 _ _ hij

/-- Antisymmetric `SU(2)_L` doublet contraction `ε_ew(v, w) = v₀ w₁ - v₁ w₀` between a lepton
doublet `v = (ν_L, e_L⁻)` and Higgs doublet `w = (H⁺, H⁰)`. -/
def ewEps {R : Type*} [CommRing R] (v w : Fin 2 → R) : R :=
  v 0 * w 1 - v 1 * w 0

/-- Dimension-5 Weinberg operator `O_W(L₁, H₁, L₂, H₂) = ε_ew(L₁, H₁) · ε_ew(L₂, H₂)`. -/
def weinbergOp {R : Type*} [CommRing R] (L₁ H₁ L₂ H₂ : Fin 2 → R) : R :=
  ewEps L₁ H₁ * ewEps L₂ H₂

/-- Action of `Sweedler R` generator `G` (`leptonG`) and `X` (`h • leptonF`) on `Fin 2 → R`. -/
def actG {R : Type*} [CommRing R] (v : Fin 2 → R) : Fin 2 → R :=
  (leptonG : Matrix (Fin 2) (Fin 2) R).mulVec v

def actX {R : Type*} [CommRing R] (h : R) (v : Fin 2 → R) : Fin 2 → R :=
  ((h • (leptonF : Matrix (Fin 2) (Fin 2) R))).mulVec v

/-- **Linear `(LH)` Oddness vs Quadratic Dimension-5 Weinberg `(LH)²` Sweedler Invariance & VEV:**
over any commutative ring `R`, under the canonical `Sweedler R` doublet action (`ΔG = G ⊗ G`,
`ΔX = X ⊗ 1 + G ⊗ X`, `ε(G) = 1`, `ε(X) = 0`):
1. **Linear `(LH)` contraction:** killed by `Δ(X)` (`ε_ew(X v, w) + ε_ew(G v, X w) = 0`), **but odd
   under `Δ(G)`** (`ε_ew(G v, G w) = -ε_ew(v, w)`);
2. **Quadratic Weinberg `(LH)²` operator:** **strictly invariant under the full 4-fold Sweedler
   coproduct** — both `Δ⁽³⁾(G)` (`O_W(G L₁, G H₁, G L₂, G H₂) = O_W(L₁, H₁, L₂, H₂)`) and
   `Δ⁽³⁾(X)` (`= 0`) — while carrying zero total `(2T₃, Y, 3Q)` on `(ν_L, H⁰)²`;
3. **Selective Majorana Mass at the Neutral Higgs VEV `H_vev = ![0, v_EW]`:**
   `weinbergOp L₁ ![0, vEW] L₂ ![0, vEW] = vEW² * L₁ 0 * L₂ 0`, giving a symmetric Majorana
   mass bilinear strictly on the `Q = 0` neutrino component `L 0 = ν_L` and zero on `e_L⁻`. -/
theorem weinberg_quadratic_singlet_sweedler_invariant_and_vev
    {R : Type*} [CommRing R] (h vEW : R) (L₁ H₁ L₂ H₂ : Fin 2 → R) :
    ewEps (actG L₁) (actG H₁) = -ewEps L₁ H₁ ∧
    ewEps (actX h L₁) H₁ + ewEps (actG L₁) (actX h H₁) = 0 ∧
    weinbergOp (actG L₁) (actG H₁) (actG L₂) (actG H₂) = weinbergOp L₁ H₁ L₂ H₂ ∧
    (weinbergOp (actX h L₁) H₁ L₂ H₂ +
      weinbergOp (actG L₁) (actX h H₁) L₂ H₂ +
      weinbergOp (actG L₁) (actG H₁) (actX h L₂) H₂ +
      weinbergOp (actG L₁) (actG H₁) (actG L₂) (actX h H₂) = 0) ∧
    weinbergOp L₁ ![0, vEW] L₂ ![0, vEW] = vEW ^ 2 * L₁ 0 * L₂ 0 ∧
    weinbergOp ![0, L₁ 1] ![0, vEW] L₂ ![0, vEW] = 0 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    simp [weinbergOp, ewEps, actG, actX, leptonG, leptonF, Matrix.mulVec, dotProduct,
      Fin.sum_univ_two] <;>
    ring

end SweedlerOrderFourAntipodeAndWeinberg

/-! ## Section 3: 3-Generation `S₃ ⊃ S₂` Perturbation Algebra & NH vs IH Eigenvalue Ratios -/

section ThreeGenerationS3Algebra

section CommRingS3

variable {R : Type*} [CommRing R]

/-- Generation permutation matrix `P_σ` for `σ : Equiv.Perm (Fin 3)` (`(P_σ)_{i,j} = δ_{i, σ j}`). -/
def permMat3 (σ : Equiv.Perm (Fin 3)) : Matrix (Fin 3) (Fin 3) R :=
  fun i j => if i = σ j then 1 else 0

/-- All-ones `3 × 3` democratic matrix `J₃`. -/
def demJ3 : Matrix (Fin 3) (Fin 3) R :=
  !![1, 1, 1; 1, 1, 1; 1, 1, 1]

/-- Symmetric `S₂`-preserving (`0 ↔ 1` invariant) traceless-orthogonal spurion `B₁₂ = v₂ v₂ᵀ`
inside the 2D standard representation `2` of `S₃`. -/
def s2SpurionB : Matrix (Fin 3) (Fin 3) R :=
  !![1, 1, -2; 1, 1, -2; -2, -2, 4]

/-- Three-parameter `S₃ ⊃ S₂` neutral-sector mass matrix `M_ν(a, b, ε) = a I₃ + b J₃ + ε B₁₂`. -/
def s3NeutralMass (a b ε : R) : Matrix (Fin 3) (Fin 3) R :=
  a • (1 : Matrix (Fin 3) (Fin 3) R) + b • demJ3 + ε • s2SpurionB

/-- Orthogonal tri-bimaximal eigenmodes `v₁ = (1, -1, 0)`, `v₂ = (1, 1, -2)`, `v₃ = (1, 1, 1)`. -/
def vMode1 : Fin 3 → R := ![1, -1, 0]
def vMode2 : Fin 3 → R := ![1, 1, -2]
def vMode3 : Fin 3 → R := ![1, 1, 1]

/-- **Exact Characterization of the `S₃` Flavour Commutant (`End_{S₃}(R³) = R · I₃ + R · J₃`):**
a `3 × 3` matrix `M` over any commutative ring `R` commutes with every permutation matrix
`permMat3 σ` (`σ : Equiv.Perm (Fin 3)`) **if and only if** `M = a • 1 + b • demJ3` for some `a, b`. -/
theorem s3_commutant_iff (M : Matrix (Fin 3) (Fin 3) R) :
    (∀ σ : Equiv.Perm (Fin 3), permMat3 σ * M = M * permMat3 σ) ↔
      ∃ a b : R, M = a • (1 : Matrix (Fin 3) (Fin 3) R) + b • demJ3 := by
  constructor
  · intro hcomm
    have hs01 := hcomm (Equiv.swap 0 1)
    have hs12 := hcomm (Equiv.swap 1 2)
    have d11 : M 1 1 = M 0 0 := by
      have h := congrFun (congrFun hs01 0) 1
      simpa [permMat3, Matrix.mul_apply, Fin.sum_univ_three, Equiv.swap_apply_def] using h
    have d22 : M 2 2 = M 0 0 := by
      have h := congrFun (congrFun hs12 1) 2
      have h21 : M 2 2 = M 1 1 := by
        simpa [permMat3, Matrix.mul_apply, Fin.sum_univ_three, Equiv.swap_apply_def] using h
      exact h21.trans d11
    have o10 : M 1 0 = M 0 1 := by
      have h := congrFun (congrFun hs01 0) 0
      simpa [permMat3, Matrix.mul_apply, Fin.sum_univ_three, Equiv.swap_apply_def] using h
    have o02 : M 0 2 = M 0 1 := by
      have h := congrFun (congrFun hs12 0) 1
      simpa [permMat3, Matrix.mul_apply, Fin.sum_univ_three, Equiv.swap_apply_def] using h.symm
    have o20 : M 2 0 = M 0 1 := by
      have h := congrFun (congrFun hs12 2) 0
      have h20 : M 2 0 = M 1 0 := by
        simpa [permMat3, Matrix.mul_apply, Fin.sum_univ_three, Equiv.swap_apply_def] using h.symm
      exact h20.trans o10
    have o12 : M 1 2 = M 0 1 := by
      have h := congrFun (congrFun hs01 1) 2
      have h12 : M 1 2 = M 0 2 := by
        simpa [permMat3, Matrix.mul_apply, Fin.sum_univ_three, Equiv.swap_apply_def] using h.symm
      exact h12.trans o02
    have o21 : M 2 1 = M 0 1 := by
      have h := congrFun (congrFun hs01 2) 0
      have h21 : M 2 1 = M 2 0 := by
        simpa [permMat3, Matrix.mul_apply, Fin.sum_univ_three, Equiv.swap_apply_def] using h.symm
      exact h21.trans o20
    refine ⟨M 0 0 - M 0 1, M 0 1, ?_⟩
    ext i j
    fin_cases i <;> fin_cases j <;>
      simp [demJ3, d11, d22, o10, o02, o20, o12, o21]
  · rintro ⟨a, b, rfl⟩ σ
    have hj : ∀ x y : Fin 3, demJ3 (R := R) x y = 1 := fun x y => by
      fin_cases x <;> fin_cases y <;> rfl
    ext i j
    have hdem : ((permMat3 (R := R) σ * demJ3 : Matrix (Fin 3) (Fin 3) R)) i j =
        ((demJ3 * permMat3 (R := R) σ : Matrix (Fin 3) (Fin 3) R)) i j := by
      have hL : ∑ k : Fin 3, (if i = σ k then (1 : R) else 0) = 1 := by
        rw [← Equiv.sum_comp σ.symm (fun k => if i = σ k then (1 : R) else 0)]
        simp
      have hR : ∑ k : Fin 3, (if k = σ j then (1 : R) else 0) = 1 := by simp
      simp only [permMat3, Matrix.mul_apply, hj, mul_one, one_mul, hL, hR]
    simp [Matrix.mul_add, Matrix.add_mul, hdem]

/-- **Exact Eigensystem, Orthogonality, Trace, & Determinant of `s3NeutralMass a b ε`:**
over any commutative ring `R`, `vMode1, vMode2, vMode3` are pairwise orthogonal eigenvectors of
`s3NeutralMass a b ε` with eigenvalues `(a, a + 6ε, a + 3b)`, matching both `trace` and `det`! -/
theorem s3NeutralMass_spectrum_trace_det (a b ε : R) :
    dotProduct (vMode1 (R := R)) vMode2 = 0 ∧
    dotProduct (vMode1 (R := R)) vMode3 = 0 ∧
    dotProduct (vMode2 (R := R)) vMode3 = 0 ∧
    (s3NeutralMass a b ε).mulVec vMode1 = a • vMode1 ∧
    (s3NeutralMass a b ε).mulVec vMode2 = (a + 6 * ε) • vMode2 ∧
    (s3NeutralMass a b ε).mulVec vMode3 = (a + 3 * b) • vMode3 ∧
    (s3NeutralMass a b ε).trace = a + (a + 6 * ε) + (a + 3 * b) ∧
    (s3NeutralMass a b ε).det = a * (a + 6 * ε) * (a + 3 * b) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · simp [vMode1, vMode2, dotProduct, Fin.sum_univ_three]
  · simp [vMode1, vMode3, dotProduct, Fin.sum_univ_three]
  · simp [vMode2, vMode3, dotProduct, Fin.sum_univ_three]; ring
  · ext i; fin_cases i <;>
      simp [s3NeutralMass, demJ3, s2SpurionB, vMode1, Matrix.mulVec, dotProduct,
        Fin.sum_univ_three] <;> ring
  · ext i; fin_cases i <;>
      simp [s3NeutralMass, demJ3, s2SpurionB, vMode2, Matrix.mulVec, dotProduct,
        Fin.sum_univ_three] <;> ring
  · ext i; fin_cases i <;>
      simp [s3NeutralMass, demJ3, s2SpurionB, vMode3, Matrix.mulVec, dotProduct,
        Fin.sum_univ_three] <;> ring
  · simp [s3NeutralMass, demJ3, s2SpurionB, Matrix.trace_fin_three]; ring
  · rw [Matrix.det_fin_three]
    simp [s3NeutralMass, demJ3, s2SpurionB]
    ring

/-- Squared-mass splittings `Δm₂₁² = m₂² - m₁²`, `Δm₃₂² = m₃² - m₂²`, `Δm₃₁² = m₃² - m₁²`. -/
def dm21Sq (m₁ m₂ : R) : R := m₂ ^ 2 - m₁ ^ 2
def dm32Sq (m₂ m₃ : R) : R := m₃ ^ 2 - m₂ ^ 2
def dm31Sq (m₁ m₃ : R) : R := m₃ ^ 2 - m₁ ^ 2

theorem dm_splitting_sum_rule (m₁ m₂ m₃ : R) :
    dm31Sq m₁ m₃ = dm32Sq m₂ m₃ + dm21Sq m₁ m₂ := by
  unfold dm31Sq dm32Sq dm21Sq
  ring

end CommRingS3

section HierarchyRatiosOrderedField

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- **Minimal Normal Hierarchy (`NH`, `a = 0`, `0 < ε`, `2ε < b`) Signs & Exact Ratios:**
for eigenvalues `(m₁, m₂, m₃) = (0, 6ε, 3b)`, both `Δm₂₁² > 0` and `Δm₃₂² > 0`, with exact ratios
`Δm₂₁² / Δm₃₁² = (2ε / b)²` and `Δm₂₁² / Δm₃₂² = (2ε)² / (b² - (2ε)²)`. -/
theorem nh_splittings_pos_and_ratios {b ε : F} (hε : 0 < ε) (hb : 2 * ε < b) :
    0 < dm21Sq (0 : F) (6 * ε) ∧
    0 < dm32Sq (6 * ε) (3 * b) ∧
    dm21Sq (0 : F) (6 * ε) / dm31Sq (0 : F) (3 * b) = (2 * ε / b) ^ 2 ∧
    dm21Sq (0 : F) (6 * ε) / dm32Sq (6 * ε) (3 * b) = (2 * ε) ^ 2 / (b ^ 2 - (2 * ε) ^ 2) := by
  have hb0 : 0 < b := by linarith
  have hdiff : 0 < b ^ 2 - (2 * ε) ^ 2 := by nlinarith
  unfold dm21Sq dm32Sq dm31Sq
  refine ⟨by nlinarith, by nlinarith, ?_, ?_⟩
  · field_simp [ne_of_gt hb0]
    ring
  · have hden9 : (3 * b) ^ 2 - (6 * ε) ^ 2 = 9 * (b ^ 2 - (2 * ε) ^ 2) := by ring
    rw [hden9]
    field_simp [ne_of_gt hdiff]
    ring

/-- **Minimal Inverted Hierarchy (`IH`, `m₃ = 0`, `0 < a`, `0 < ε`) Sign Flip & Exact Ratio:**
for eigenvalues `(m₁, m₂, m₃) = (a, a + 6ε, 0)`, `Δm₂₁² > 0` while `Δm₃₂² < 0`, and
`Δm₂₁² / (-Δm₃₂²) = 1 - (a / (a + 6ε))² < 1`. -/
theorem ih_splittings_sign_and_ratio {a ε : F} (ha : 0 < a) (hε : 0 < ε) :
    0 < dm21Sq a (a + 6 * ε) ∧
    dm32Sq (a + 6 * ε) 0 < 0 ∧
    dm21Sq a (a + 6 * ε) / (-dm32Sq (a + 6 * ε) 0) = 1 - (a / (a + 6 * ε)) ^ 2 := by
  have hsum : 0 < a + 6 * ε := by linarith
  unfold dm21Sq dm32Sq
  refine ⟨by nlinarith, by nlinarith, ?_⟩
  field_simp [ne_of_gt hsum]
  ring

/-- **Strict Cosmological Mass-Sum Inequality (`∑ m_ν(NH) < ∑ m_ν(IH)` at Matched Splittings):**
over any strict ordered field `F`, let `(0, m₂, m₃)` (`0 < m₂`, `0 < m₃`) be a minimal NH mass
triple and `(n₁, n₂, 0)` (`0 < n₁`, `0 < n₂`) a minimal IH mass triple sharing the same solar
splitting `m₂² = n₂² - n₁²` and atmospheric scale `m₃² = n₂²` in the hierarchical regime
`2 m₂² < m₃²` (`Δm₂₁² / |Δm₃₂|² < 1/2`). Then `m₃ = n₂`, `m₂ < n₁`, and `m₂ + m₃ < n₁ + n₂`. -/
theorem nh_mass_sum_lt_ih_of_matched_splittings {m₂ m₃ n₁ n₂ : F}
    (hm₂ : 0 < m₂) (hm₃ : 0 < m₃) (hn₁ : 0 < n₁) (hn₂ : 0 < n₂)
    (hsol : m₂ ^ 2 = n₂ ^ 2 - n₁ ^ 2) (hatm : m₃ ^ 2 = n₂ ^ 2)
    (hhier : 2 * m₂ ^ 2 < m₃ ^ 2) :
    m₃ = n₂ ∧ m₂ < n₁ ∧ (0 + m₂ + m₃) < (n₁ + n₂ + 0) := by
  have hm3_eq : m₃ = n₂ := by
    have hdiff : (m₃ - n₂) * (m₃ + n₂) = 0 := by linear_combination hatm
    rcases mul_eq_zero.mp hdiff with h | h
    · exact sub_eq_zero.mp h
    · exfalso; linarith
  have hn1_gt : m₂ ^ 2 < n₁ ^ 2 := by linarith
  have hm2_lt : m₂ < n₁ := by
    by_contra hle
    push_neg at hle
    have hsq : n₁ ^ 2 ≤ m₂ ^ 2 := by nlinarith
    linarith
  exact ⟨hm3_eq, hm2_lt, by linarith⟩

end HierarchyRatiosOrderedField

section HierarchyArchimedean

/-- Prescribed `§7c` archimedean `ℝ` specialization of `nh_mass_sum_lt_ih_of_matched_splittings`. -/
theorem nh_mass_sum_lt_ih_of_matched_splittings_real {m₂ m₃ n₁ n₂ : ℝ}
    (hm₂ : 0 < m₂) (hm₃ : 0 < m₃) (hn₁ : 0 < n₁) (hn₂ : 0 < n₂)
    (hsol : m₂ ^ 2 = n₂ ^ 2 - n₁ ^ 2) (hatm : m₃ ^ 2 = n₂ ^ 2)
    (hhier : 2 * m₂ ^ 2 < m₃ ^ 2) :
    m₃ = n₂ ∧ m₂ < n₁ ∧ (0 + m₂ + m₃) < (n₁ + n₂ + 0) :=
  nh_mass_sum_lt_ih_of_matched_splittings (F := ℝ) hm₂ hm₃ hn₁ hn₂ hsol hatm hhier

end HierarchyArchimedean

end ThreeGenerationS3Algebra

end QOU.StandardModel.NeutrinoUnknotSweedlerMassLift
