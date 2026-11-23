import QOU.QBeta.BorromeanFlavourPivotalUnification
import QOU.Eightfold.USpinColemanGlashowLambdaSigma
import QOU.Eightfold.GellMannOkuboIdentity
import QOU.Eightfold.GellMannOkuboSecondOrder
import QOU.EightfoldWay.SymmetricChannelDimension
import QOU.ParticleInteractions.MesonOperatorSelectionT3

/-!
# Framed `(V₂, W₃*)` Hyperbolic 3-Strand Meson Clasp, `H₃(q)` `S^{(2,1)}` Diquark Projector Split, and 2nd-Order Quantum Casimir Gell-Mann–Okubo Identity

Over generic commutative rings `[CommRing R]` and fields `[Field K]` (§7c base-ring discipline:
zero `ℝ`, zero empirical constants, zero proof placeholders), this module formalizes four coupled results
for Chapter 10 (*The Eightfold Way and Flavor Structure*) and the Standard Model appendix
(`qou-8fw2`, `qou-3ttt`, `qou-qpj9`, `qou-pwz4`, `qou-c9uj`, `qou-3oi0`):

1. **Split-Bundle `F = V₂ ⊕ W₃*` (`z₃ = q³ / [3]_q`), Framed Quark/Antiquark Charges, and Quantum `3 ⊗ 3 ⊗ 3 = 10 ⊕ 8 ⊕ 8 ⊕ 1` (`qou-3oi0`):**
   - Proves the `sl₅(K)` traceless centralizer condition `2 y₂ + 3 y₃ = 0 ↔ y₃ = -(2/3) y₂` on
     `F = V₂ ⊕ W₃*`, the induced exterior-pair doublet hypercharge `y₂ + y₃ = +1/3` at `y₂ = 1`,
     and the Killing-trace Weinberg ratio `tr(T₃²) / (tr(T₃²) + tr((Y_F/2)²)) = (1/2) / (1/2 + 5/6) = 3 / 8`.
   - Lifts single-strand quark/antiquark labels (`Quark × Bool`) to `(V₂, W₃*)`-framed charges
     `Q = I₃ + Y / 2`, separating `ū` (`-2/3`) from `d` (`-1/3`) by `+1/3 ≠ 0` despite identical
     crossing/weak sign `-1`.
   - Proves `z₃(q) = q³ / [3]_q = q⁵ / (q⁴ + q² + 1)`, `z₂(q) - z₃(q) = q³ / ((q²+1)(q⁴+q²+1)) ≠ 0`,
     the quantum Schur–Weyl `W₃^{⊗3}` identity `dim_q(10) + 2 dim_q(8) + dim_q(1) = [3]_q³`
     (paired with `SymmetricChannelDimension.decuplet_dim = 10`), and exact normalization of the
     rank-3 Ocneanu weights `w_{(3)}(q, z₃) + 2 w_{(2,1)}(q, z₃) + w_{(1³)}(q, z₃) = 1`.

2. **Ordered Content-to-Braid Map and 3-Strand Hyperbolic Gluon-Clasp (`qou-3ttt`, `qou-qpj9`):**
   - Maps ordered meson constituent pairs `(n₁, n₂) ∈ {3, 5, 7}²` to the parameter-free 3-strand
     gluon-clasp braid `β_clasp(n₁, n₂) = σ₁^{n₁} σ₂^{-n₂} σ₁ σ₂⁻¹ ∈ B₃`.
   - Proves over any `[CommRing R]` that the `SL₂` monodromy image `claspSL2 n₁ n₂` satisfies
     `det = 1` and `trace = 2 n₁ n₂ + n₁ + n₂ + 3` (`≥ 27 > 2` on `{3, 5, 7}²`, pseudo-Anosov /
     hyperbolic by Thurston's `B₃ / Z(B₃) ≅ PSL₂(ℤ)` classification, bypassing `Vol = 0` 2-strand
     torus closures).
   - Proves that while the `2 × 2` `SL₂` Hecke block trace `tr ρ_{(2,1)}(β_clasp(n₁, n₂))` is
     symmetric on `(5, 3)` vs `(3, 5)`, BOTH the rank-2 (`z₂`) and rank-3 (`z₃`) full `H₃(q)`
     Markov traces strictly separate `D̄⁰ = (-5, +3) ↦ (5, 3)` from `K⁰ = (+3, -5) ↦ (3, 5)` via
     exact closed-form multiples of `q² - q⁻²`, and that the `(V₂, W₃*)`-framed clasp datum is
     injective across all five dictionary mesons (`pion`, `kaon`, `etaPhi`, `Dmeson`, `K0`).

3. **`H₃(q)` `S^{(2,1)}` Diquark Spin-Isospin Projector Split (`qou-pwz4`):**
   - Constructs the mutually orthogonal rank-1 `ud`-diquark idempotents `projDiquarkLambda`
     (`I = 0`, `σ₁`-eigenvalue `-q⁻¹`) and `projDiquarkSigma0` (`I = 1`, `σ₁`-eigenvalue `+q`)
     inside the `2 × 2` mixed-symmetry Hecke module `S^{(2,1)}`, proves idempotency, orthogonality,
     commutativity of Jucys–Murphy twists `[J₂, J₃] = 0`, exact `J₂` eigenvalue split `q² - q⁻²`,
     single-step Borromean `V` ratio `q⁶`, full Borromean `V³` split
     `tr(P_Λ V³) - tr(P_{Σ⁰} V³) = (q - q⁻¹)³ (q² + q⁻²) [3]_q / [2]_q`, and exact agreement with
     the `3 × 3` baryon weight-space projectors `eLambda`, `eSigma0`.

4. **`O((q - q⁻¹)²)` 2nd-Order Quantum Casimir Correction to Gell-Mann–Okubo (`qou-c9uj`):**
   - Evaluates the rational quantum Casimir `d_q(I, Y) = [I]_q [I+1]_q - [Y/2]_q²` on any octet
     and proves that for `M(I, Y) = a + b Y + c d_q(I, Y)` (`c ≠ 0`), `(a, b, c)` cancel from the
     normalized GMO ratio to give the parameter-free bar-even law
     `(4 M_K - 3 M_η - M_π) / (M_π - M_η) = -((q - 1) / (q + 1))² = -(q - q⁻¹)² / ([2]_q + 2)²`.

-- Ref: [jimbo1986] Jimbo, Lett. Math. Phys. 11 (1986) 247–252.
-- Ref: [gellmann1962] Gell-Mann, Phys. Rev. 125 (1962) 1067.
-- Ref: [okubo1962] Okubo, Prog. Theor. Phys. 27 (1962) 949.
-- Ref: [kleinkreisler1996] Klein-Kreisler & Majid, hep-ph/9612303.
-/

namespace QOU.Eightfold.HyperbolicMesonClaspAndDiquarkSplit

open Matrix
open QOU.QBeta.BorromeanFlavourPivotalUnification
open QOU.Eightfold.USpinColemanGlashowLambdaSigma
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceSecondOrder
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.ParticleInteractions.MesonOperatorSelectionT3

/-! ## Section 1: Split-Bundle `F = V₂ ⊕ W₃*`, Framed Charges, and Quantum `W₃^{⊗3}` -/

section SplitBundleAndFraming

variable {K : Type*} [Field K]

/-- Diagonal block-scalar hypercharge generator `diag(y₂, y₂, y₃, y₃, y₃)` in `End(V₂ ⊕ W₃*)`. -/
def splitBundleHyperchargeDiag (y2 y3 : K) : Matrix (Fin 5) (Fin 5) K :=
  Matrix.diagonal ![y2, y2, y3, y3, y3]

/-- Diagonal weak-isospin Cartan generator `T₃ = diag(+1/2, -1/2, 0, 0, 0)` on `V₂ ⊕ W₃*`. -/
def splitBundleIsospinDiag (K : Type*) [Field K] : Matrix (Fin 5) (Fin 5) K :=
  Matrix.diagonal ![(1 : K) / 2, -(1 : K) / 2, 0, 0, 0]

/-- **Traceless `sl₅(K)` Centralizer Slope (`2 y₂ + 3 y₃ = 0 ↔ y₃ = -(2/3) y₂`):**
Over any field with `3 ≠ 0`, tracelessness of `diag(y₂, y₂, y₃, y₃, y₃)` uniquely pins the
`W₃*` block weight `y₃` to `-(2/3) y₂`. -/
theorem splitBundle_traceless_iff (h3 : (3 : K) ≠ 0) (y2 y3 : K) :
    (splitBundleHyperchargeDiag y2 y3).trace = 0 ↔ y3 = -((2 : K) / 3) * y2 := by
  have htr : (splitBundleHyperchargeDiag y2 y3).trace = 2 * y2 + 3 * y3 := by
    simp [splitBundleHyperchargeDiag, Matrix.trace, Matrix.diag, Fin.sum_univ_five]
    ring
  rw [htr]
  constructor
  · intro h0
    apply mul_left_cancel₀ h3
    have hrhs : 3 * (-((2 : K) / 3) * y2) = -(2 * y2) := by
      rw [div_eq_mul_inv]
      linear_combination -(2 * y2) * mul_inv_cancel₀ h3
    rw [hrhs]
    linear_combination h0
  · intro hy
    rw [hy, div_eq_mul_inv]
    linear_combination -(2 * y2) * mul_inv_cancel₀ h3

/-- **Killing-Trace Weinberg Ratio `3 / 8` and Exterior-Pair Quark Doublet Hypercharge `+1/3`:**
At the traceless `V₂ ⊕ W₃*` generator `Y_F = diag(1, 1, -2/3, -2/3, -2/3)` (`y₂ = 1`, `y₃ = -2/3`):
1. The induced exterior-pair hypercharge on `Q_L ∈ V₂ ⊗ W₃*` is `y₂ + y₃ = +1/3`;
2. `tr(T₃²) = 1/2` and `tr((Y_F / 2)²) = 5/6`;
3. The unrenormalized Weinberg ratio `tr(T₃²) / (tr(T₃²) + tr((Y_F / 2)²))` equals `3 / 8`. -/
theorem splitBundle_killing_traces (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    let YF := splitBundleHyperchargeDiag (1 : K) (-((2 : K) / 3))
    let T3M := splitBundleIsospinDiag K
    (1 : K) + (-((2 : K) / 3)) = (1 : K) / 3 ∧
      (T3M * T3M).trace = (1 : K) / 2 ∧
      (((1 / 2 : K) • YF) * ((1 / 2 : K) • YF)).trace = (5 : K) / 6 ∧
      ((T3M * T3M).trace) /
        ((T3M * T3M).trace + (((1 / 2 : K) • YF) * ((1 / 2 : K) • YF)).trace) =
        (3 : K) / 8 := by
  intro YF T3M
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by ring
    rw [e]; exact mul_ne_zero h2 h2
  have h6 : (6 : K) ≠ 0 := by
    have e : (6 : K) = 2 * 3 := by ring
    rw [e]; exact mul_ne_zero h2 h3
  have h8 : (8 : K) ≠ 0 := by
    have e : (8 : K) = 4 * 2 := by ring
    rw [e]; exact mul_ne_zero h4 h2
  have hy_sum : (1 : K) + (-((2 : K) / 3)) = (1 : K) / 3 := by
    field_simp; ring
  have hT : (T3M * T3M).trace = (1 : K) / 2 := by
    have hraw : (T3M * T3M).trace =
        ((1 : K) / 2) * ((1 : K) / 2) + (-(1 : K) / 2) * (-(1 : K) / 2) := by
      simp [T3M, splitBundleIsospinDiag, Matrix.trace, Matrix.diag, Fin.sum_univ_five]
    rw [hraw]
    field_simp; ring
  have hY : (((1 / 2 : K) • YF) * ((1 / 2 : K) • YF)).trace = (5 : K) / 6 := by
    have hraw : (((1 / 2 : K) • YF) * ((1 / 2 : K) • YF)).trace =
        ((1 : K) / 2) * ((1 : K) / 2) + ((1 : K) / 2) * ((1 : K) / 2) +
          (((1 : K) / 2) * (-((2 : K) / 3))) * (((1 : K) / 2) * (-((2 : K) / 3))) +
          (((1 : K) / 2) * (-((2 : K) / 3))) * (((1 : K) / 2) * (-((2 : K) / 3))) +
          (((1 : K) / 2) * (-((2 : K) / 3))) * (((1 : K) / 2) * (-((2 : K) / 3))) := by
      simp [YF, splitBundleHyperchargeDiag, Matrix.diagonal_mul_diagonal, Matrix.trace,
        Matrix.diag, Fin.sum_univ_five]
      ring
    rw [hraw]
    field_simp; ring
  refine ⟨hy_sum, hT, hY, ?_⟩
  rw [hT, hY]
  have hden : (1 : K) / 2 + (5 : K) / 6 = (4 : K) / 3 := by
    field_simp; ring
  have hden_ne : (4 : K) / 3 ≠ 0 := div_ne_zero h4 h3
  rw [hden]
  field_simp; ring

/-- Weak-crossing sign `±1` of a `(V₂, W₃*)`-framed quark (`b = true`) or antiquark (`b = false`). -/
def framedWeakSign (s : Quark × Bool) : ℤ :=
  if s.2 then (signedWrithe s.1).sign else -(signedWrithe s.1).sign

/-- `W₃` (`+1`) vs `W₃*` (`-1`) triality orientation sign. -/
def framedTrialitySign (s : Quark × Bool) : ℤ :=
  if s.2 then 1 else -1

/-- Integer `6 Q = 3 * framedWeakSign + framedTrialitySign` clearing the factor `6` over `ℤ`. -/
def framedSixCharge (s : Quark × Bool) : ℤ :=
  3 * framedWeakSign s + framedTrialitySign s

/-- **Parameter-free `(V₂, W₃*)`-framed electric charge:**
`Q(q, b) = (1/2) framedWeakSign + (1/6) framedTrialitySign` (`= I₃ + B/2` on doublet strands). -/
def framedStrandCharge (s : Quark × Bool) : K :=
  (framedWeakSign s : K) / 2 + (framedTrialitySign s : K) / 6

theorem framedStrandCharge_eq_sixCharge_div (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0)
    (s : Quark × Bool) :
    framedStrandCharge (K := K) s = (framedSixCharge s : K) / 6 := by
  have h6 : (6 : K) ≠ 0 := by
    have e : (6 : K) = 2 * 3 := by ring
    rw [e]; exact mul_ne_zero h2 h3
  unfold framedStrandCharge framedSixCharge
  rw [div_add_div _ _ h2 h6, div_eq_div_iff (mul_ne_zero h2 h6) h6]
  push_cast
  ring

/-- **Categorical Separation of Anti-Up (`ū`, `-2/3`) from Down (`d`, `-1/3`):**
Although `ū = (.up, false)` and `d = (.down, true)` share the identical weak/crossing sign `-1`
(which blocked bare single-fibre writhe charge maps), the `(V₂, W₃*)` triality sign separates
their electric charges by `+1/3 ≠ 0` and reproduces all four distinct doublet charges
`(+2/3, -1/3, +1/3, -2/3)`. -/
theorem antiUp_down_same_weakSign_yet_distinct_charge (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    framedWeakSign (.up, false) = framedWeakSign (.down, true) ∧
      framedStrandCharge (K := K) (.up, true) = (2 : K) / 3 ∧
      framedStrandCharge (K := K) (.down, true) = -(1 : K) / 3 ∧
      framedStrandCharge (K := K) (.down, false) = (1 : K) / 3 ∧
      framedStrandCharge (K := K) (.up, false) = -(2 : K) / 3 ∧
      framedStrandCharge (K := K) (.down, true) - framedStrandCharge (K := K) (.up, false) =
        (1 : K) / 3 ∧
      framedStrandCharge (K := K) (.up, false) ≠ framedStrandCharge (K := K) (.down, true) := by
  have h6 : (6 : K) ≠ 0 := by
    have e : (6 : K) = 2 * 3 := by ring
    rw [e]; exact mul_ne_zero h2 h3
  have hws : framedWeakSign (.up, false) = framedWeakSign (.down, true) := by decide
  have hc_u : framedSixCharge (.up, true) = 4 := by decide
  have hc_d : framedSixCharge (.down, true) = -2 := by decide
  have hc_db : framedSixCharge (.down, false) = 2 := by decide
  have hc_ub : framedSixCharge (.up, false) = -4 := by decide
  have hu : framedStrandCharge (K := K) (.up, true) = (2 : K) / 3 := by
    rw [framedStrandCharge_eq_sixCharge_div h2 h3, hc_u, div_eq_div_iff h6 h3]; push_cast; ring
  have hd : framedStrandCharge (K := K) (.down, true) = -(1 : K) / 3 := by
    rw [framedStrandCharge_eq_sixCharge_div h2 h3, hc_d, div_eq_div_iff h6 h3]; push_cast; ring
  have hdb : framedStrandCharge (K := K) (.down, false) = (1 : K) / 3 := by
    rw [framedStrandCharge_eq_sixCharge_div h2 h3, hc_db, div_eq_div_iff h6 h3]; push_cast; ring
  have hub : framedStrandCharge (K := K) (.up, false) = -(2 : K) / 3 := by
    rw [framedStrandCharge_eq_sixCharge_div h2 h3, hc_ub, div_eq_div_iff h6 h3]; push_cast; ring
  have hdiff :
      framedStrandCharge (K := K) (.down, true) - framedStrandCharge (K := K) (.up, false) =
        (1 : K) / 3 := by
    rw [hd, hub, div_sub_div_same, div_eq_div_iff h3 h3]; ring
  refine ⟨hws, hu, hd, hdb, hub, hdiff, ?_⟩
  intro heq
  have h0 : (1 : K) / 3 = 0 := by
    rw [← hdiff, heq, sub_self]
  exact one_ne_zero ((div_eq_zero_iff.mp h0).resolve_right h3)

/-- Balanced quantum integer `[3]_q = q² + 1 + q⁻²`. -/
def qBracket3 (q : K) : K := q ^ 2 + 1 + q⁻¹ ^ 2

/-- Rank-2 (Convention-D / `V₂`) Markov trace parameter `z₂(q) = q³ / (q² + 1) = q² / [2]_q`. -/
def zRank2 (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- Rank-3 (`W₃*` flavour/colour bundle) Markov trace parameter `z₃(q) = q³ / [3]_q`. -/
def zRank3 (q : K) : K := q ^ 3 / qBracket3 q

/-- Equivalence of `z₃(q) = q³ / [3]_q` with `q⁵ / (q⁴ + q² + 1)` (`SecondMarkovTrace.colourTower_z`). -/
theorem zRank3_eq_rational {q : K} (hq : q ≠ 0) :
    zRank3 q = q ^ 5 / (q ^ 4 + q ^ 2 + 1) := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  have hmul : q ^ 2 * qBracket3 q = q ^ 4 + q ^ 2 + 1 := by
    unfold qBracket3
    linear_combination (q * q⁻¹ + 1) * hqi
  unfold zRank3
  by_cases hden : q ^ 4 + q ^ 2 + 1 = 0
  · have hbr : qBracket3 q = 0 :=
      (mul_eq_zero.mp (hmul.trans hden)).resolve_left (pow_ne_zero 2 hq)
    rw [hbr, hden, div_zero, div_zero]
  · have hbr : qBracket3 q ≠ 0 := by
      intro h0; apply hden; rw [← hmul, h0, mul_zero]
    rw [div_eq_div_iff hbr hden, ← hmul]
    ring

/-- **Exact Separation `z₂(q) - z₃(q) = q³ / ((q² + 1)(q⁴ + q² + 1)) ≠ 0`:**
The `V₂` mass trace parameter `z₂` and the `W₃*` flavour/colour trace parameter `z₃` are never
equal for `q ≠ 0` with non-vanishing `[2]_q` and `[3]_q`. -/
theorem zRank2_sub_zRank3 {q : K} (hq : q ≠ 0)
    (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    zRank2 q - zRank3 q = q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) ∧
      zRank2 q ≠ zRank3 q := by
  have hdiff : zRank2 q - zRank3 q =
      q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
    rw [zRank3_eq_rational hq]
    unfold zRank2
    rw [div_sub_div _ _ h2 h3, div_eq_div_iff (mul_ne_zero h2 h3) (mul_ne_zero h2 h3)]
    ring
  refine ⟨hdiff, ?_⟩
  intro heq
  have h0 : q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) = 0 := by
    rw [← hdiff, heq, sub_self]
  exact pow_ne_zero 3 hq ((div_eq_zero_iff.mp h0).resolve_right (mul_ne_zero h2 h3))

/-- Quantum `U_q(gl₃)` symmetric decuplet dimension `dim_q(10) = (q² + q⁻²) [5]_q`. -/
def qDimDecuplet10 (q : K) : K :=
  (q ^ 2 + q⁻¹ ^ 2) * (q ^ 4 + q ^ 2 + 1 + q⁻¹ ^ 2 + q⁻¹ ^ 4)

/-- Quantum `U_q(gl₃)` mixed-symmetry octet dimension `dim_q(8) = [2]_q [4]_q`. -/
def qDimOctet8 (q : K) : K :=
  (q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3)

/-- Quantum `U_q(gl₃)` antisymmetric singlet dimension `dim_q(1) = 1`. -/
def qDimSinglet1 (_q : K) : K := 1

/-- Rank-3 Ocneanu weights on `H₃(q)` at `z₃ = q³ / [3]_q`. -/
def ocneanuW3_sym (q : K) : K := qDimDecuplet10 q / (qBracket3 q) ^ 3
def ocneanuW3_mix (q : K) : K := qDimOctet8 q / (qBracket3 q) ^ 3
def ocneanuW3_alt (q : K) : K := qDimSinglet1 q / (qBracket3 q) ^ 3

/-- Rank-2 (Convention-D) Ocneanu weights on `H₃(q)` at `z₂ = q³ / (q² + 1)` (`w_{(1³)} = 0`). -/
def ocneanuW2_sym (q : K) : K := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2
def ocneanuW2_mix (q : K) : K := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- **Unconditional `W₃` Decuplet Dimension `dim Sym³(W₃) = 10` & Quantum `3 ⊗ 3 ⊗ 3 = 10 ⊕ 8 ⊕ 8 ⊕ 1` (`qou-3oi0`):**
1. Over `MvPolynomial` (`QOU.EightfoldWay.SymmetricChannelDimension`), `dim_K Sym³(W₃*) = 10`
   while `dim_K Sym³(V₂*) = 4`.
2. At `q = 1`, `(qDimDecuplet10 1, qDimOctet8 1, qDimSinglet1 1) = (10, 8, 1)`.
3. For every `q ≠ 0`, `dim_q(10) + 2 dim_q(8) + dim_q(1) = [3]_q³`, and whenever `[3]_q ≠ 0`,
   the rank-3 Ocneanu trace weights normalize identically:
   `ocneanuW3_sym q + 2 * ocneanuW3_mix q + ocneanuW3_alt q = 1`. -/
theorem quantum_cube_3x3x3_and_decuplet_10 {q : K} (hq : q ≠ 0) (hb3 : qBracket3 q ≠ 0) :
    Module.finrank K (MvPolynomial.homogeneousSubmodule (Fin 3) K 3) = 10 ∧
      Module.finrank K (MvPolynomial.homogeneousSubmodule (Fin 2) K 3) = 4 ∧
      qDimDecuplet10 (1 : K) = 10 ∧
      qDimOctet8 (1 : K) = 8 ∧
      qDimSinglet1 (1 : K) = 1 ∧
      qDimDecuplet10 q + 2 * qDimOctet8 q + qDimSinglet1 q = (qBracket3 q) ^ 3 ∧
      ocneanuW3_sym q + 2 * ocneanuW3_mix q + ocneanuW3_alt q = 1 := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  have h2 : q ^ 2 * qBracket3 q = q ^ 4 + q ^ 2 + 1 := by
    unfold qBracket3; linear_combination (q * q⁻¹ + 1) * hqi
  have h10 : q ^ 6 * qDimDecuplet10 q =
      (q ^ 4 + 1) * (q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1) := by
    unfold qDimDecuplet10
    have ha : q ^ 2 * (q ^ 2 + q⁻¹ ^ 2) = q ^ 4 + 1 := by
      linear_combination (q * q⁻¹ + 1) * hqi
    have hb : q ^ 4 * (q ^ 4 + q ^ 2 + 1 + q⁻¹ ^ 2 + q⁻¹ ^ 4) =
        q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1 := by
      linear_combination (q ^ 2 * (q * q⁻¹ + 1) + (q * q⁻¹) ^ 3 + (q * q⁻¹) ^ 2 + q * q⁻¹ + 1) * hqi
    calc
      q ^ 6 * ((q ^ 2 + q⁻¹ ^ 2) * (q ^ 4 + q ^ 2 + 1 + q⁻¹ ^ 2 + q⁻¹ ^ 4))
          = (q ^ 2 * (q ^ 2 + q⁻¹ ^ 2)) *
              (q ^ 4 * (q ^ 4 + q ^ 2 + 1 + q⁻¹ ^ 2 + q⁻¹ ^ 4)) := by ring
      _ = (q ^ 4 + 1) * (q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1) := by rw [ha, hb]
  have h8 : q ^ 6 * qDimOctet8 q =
      q ^ 2 * (q ^ 2 + 1) * (q ^ 6 + q ^ 4 + q ^ 2 + 1) := by
    unfold qDimOctet8
    have ha : q * (q + q⁻¹) = q ^ 2 + 1 := by linear_combination hqi
    have hb : q ^ 3 * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) = q ^ 6 + q ^ 4 + q ^ 2 + 1 := by
      linear_combination (q ^ 2 + (q * q⁻¹) ^ 2 + q * q⁻¹ + 1) * hqi
    calc
      q ^ 6 * ((q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3))
          = q ^ 2 * (q * (q + q⁻¹)) * (q ^ 3 * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3)) := by ring
      _ = q ^ 2 * (q ^ 2 + 1) * (q ^ 6 + q ^ 4 + q ^ 2 + 1) := by rw [ha, hb]
  have hcube : qDimDecuplet10 q + 2 * qDimOctet8 q + qDimSinglet1 q = (qBracket3 q) ^ 3 := by
    apply mul_left_cancel₀ (pow_ne_zero 6 hq)
    have hrhs : q ^ 6 * (qBracket3 q) ^ 3 = (q ^ 4 + q ^ 2 + 1) ^ 3 := by
      calc
        q ^ 6 * (qBracket3 q) ^ 3 = (q ^ 2 * qBracket3 q) ^ 3 := by ring
        _ = (q ^ 4 + q ^ 2 + 1) ^ 3 := by rw [h2]
    rw [hrhs]
    calc
      q ^ 6 * (qDimDecuplet10 q + 2 * qDimOctet8 q + qDimSinglet1 q)
          = q ^ 6 * qDimDecuplet10 q + 2 * (q ^ 6 * qDimOctet8 q) + q ^ 6 := by
            unfold qDimSinglet1; ring
      _ = (q ^ 4 + 1) * (q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1) +
            2 * (q ^ 2 * (q ^ 2 + 1) * (q ^ 6 + q ^ 4 + q ^ 2 + 1)) + q ^ 6 := by
            rw [h10, h8]
      _ = (q ^ 4 + q ^ 2 + 1) ^ 3 := by ring
  refine ⟨QOU.EightfoldWay.SymmetricChannelDimension.decuplet_dim,
    QOU.EightfoldWay.SymmetricChannelDimension.quadruplet_dim,
    by unfold qDimDecuplet10; ring,
    by unfold qDimOctet8; ring,
    rfl,
    hcube,
    ?_⟩
  unfold ocneanuW3_sym ocneanuW3_mix ocneanuW3_alt
  have hsum :
      qDimDecuplet10 q / qBracket3 q ^ 3 + 2 * (qDimOctet8 q / qBracket3 q ^ 3) +
        qDimSinglet1 q / qBracket3 q ^ 3 =
      (qDimDecuplet10 q + 2 * qDimOctet8 q + qDimSinglet1 q) / qBracket3 q ^ 3 := by
    ring
  rw [hsum, hcube, div_self (pow_ne_zero 3 hb3)]

end SplitBundleAndFraming

/-! ## Section 2: Ordered Content-to-Braid Map & 3-Strand Hyperbolic Meson Clasp (`qou-3ttt`, `qou-qpj9`) -/

section HyperbolicMesonClasp

/-- Ordered generation pair `(n₁, n₂) = (|-κ(antiquark)|, |+κ(quark)|) ∈ {3, 5, 7}²` of a `Meson`. -/
def mesonGenerationPair (m : Meson) : ℕ × ℕ :=
  ((orderedContent m).1.natAbs, (orderedContent m).2.natAbs)

/-- **Ordered Generation Pair Separates `D̄⁰ = (-5, +3)` from `K⁰ = (+3, -5)`:**
Keeping the antiquark-first / quark-second order maps `D̄⁰` to `(5, 3)` and `K⁰` to `(3, 5)`. -/
theorem Dmeson_K0_generationPair_swapped :
    mesonGenerationPair .Dmeson = (5, 3) ∧
      mesonGenerationPair .K0 = (3, 5) ∧
      mesonGenerationPair .Dmeson ≠ mesonGenerationPair .K0 := by
  refine ⟨by decide, by decide, by decide⟩

/-- Standard `SL₂(R)` generator `A = !![1, 1; 0, 1]` representing `σ₁` in `B₃ / Z(B₃) ≅ PSL₂(ℤ)`. -/
def sl2Gen1 {R : Type*} [CommRing R] : Matrix (Fin 2) (Fin 2) R :=
  !![1, 1; 0, 1]

/-- Standard `SL₂(R)` generator `B⁻¹ = !![1, 0; 1, 1]` representing `σ₂⁻¹` in `B₃ / Z(B₃) ≅ PSL₂(ℤ)`. -/
def sl2Gen2Inv {R : Type*} [CommRing R] : Matrix (Fin 2) (Fin 2) R :=
  !![1, 0; 1, 1]

/-- **3-Strand Gluon-Clasp `SL₂(R)` Monodromy:**
Image of `β_clasp(n₁, n₂) = σ₁^{n₁} σ₂^{-n₂} σ₁ σ₂⁻¹ ∈ B₃` in `SL₂(R)`. -/
def claspSL2 {R : Type*} [CommRing R] (n1 n2 : ℕ) : Matrix (Fin 2) (Fin 2) R :=
  ((sl2Gen1 : Matrix (Fin 2) (Fin 2) R) ^ n1) *
    ((sl2Gen2Inv : Matrix (Fin 2) (Fin 2) R) ^ n2) * sl2Gen1 * sl2Gen2Inv

theorem sl2Gen1_pow {R : Type*} [CommRing R] (n : ℕ) :
    (sl2Gen1 : Matrix (Fin 2) (Fin 2) R) ^ n = !![1, (n : R); 0, 1] := by
  induction n with
  | zero =>
    ext i j
    fin_cases i <;> fin_cases j <;> simp
  | succ k ih =>
    rw [pow_succ, ih]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (simp [sl2Gen1, Matrix.mul_apply, Fin.sum_univ_two, Nat.cast_add]; try ring)

theorem sl2Gen2Inv_pow {R : Type*} [CommRing R] (n : ℕ) :
    (sl2Gen2Inv : Matrix (Fin 2) (Fin 2) R) ^ n = !![1, 0; (n : R), 1] := by
  induction n with
  | zero =>
    ext i j
    fin_cases i <;> fin_cases j <;> simp
  | succ k ih =>
    rw [pow_succ, ih]
    ext i j
    fin_cases i <;> fin_cases j <;>
      (simp [sl2Gen2Inv, Matrix.mul_apply, Fin.sum_univ_two, Nat.cast_add]; try ring)

/-- **Closed-Form Determinant and Hyperbolic Trace of the 3-Strand Gluon-Clasp (`claspSL2`):**
Over ANY commutative ring `R` and for all `n₁, n₂ : ℕ`,
`det(claspSL2 n₁ n₂) = 1` and `tr(claspSL2 n₁ n₂) = 2 n₁ n₂ + n₁ + n₂ + 3`. -/
theorem claspSL2_det_and_trace {R : Type*} [CommRing R] (n1 n2 : ℕ) :
    (claspSL2 (R := R) n1 n2).det = 1 ∧
      (claspSL2 (R := R) n1 n2).trace = 2 * (n1 : R) * (n2 : R) + (n1 : R) + (n2 : R) + 3 := by
  unfold claspSL2
  rw [sl2Gen1_pow, sl2Gen2Inv_pow]
  refine ⟨?_, ?_⟩
  · simp [sl2Gen1, sl2Gen2Inv, Matrix.det_fin_two]
    ring
  · simp [sl2Gen1, sl2Gen2Inv, Matrix.trace_fin_two]
    ring

/-- **Strict Hyperbolicity (`tr ≥ 7 > 2`, `≥ 27` on `{3, 5, 7}²`) Bypassing `Vol = 0` Torus Braids:**
For all positive windings `1 ≤ n₁, 1 ≤ n₂`, `(claspSL2 (R := ℤ) n₁ n₂).trace ≥ 7 > 2` (so the
3-braid is strictly pseudo-Anosov / hyperbolic in `PSL₂(ℤ)`, never periodic or reducible), and
across the nine generation pairs `(n₁, n₂) ∈ {3, 5, 7}²` its traces equal `{27, 41, 55, 63, 85, 115}`. -/
theorem claspSL2_hyperbolic_all_generations :
    (∀ n1 n2 : ℕ, 1 ≤ n1 → 1 ≤ n2 → 7 ≤ (claspSL2 (R := ℤ) n1 n2).trace) ∧
      (claspSL2 (R := ℤ) 3 3).trace = 27 ∧
      (claspSL2 (R := ℤ) 3 5).trace = 41 ∧
      (claspSL2 (R := ℤ) 5 3).trace = 41 ∧
      (claspSL2 (R := ℤ) 3 7).trace = 55 ∧
      (claspSL2 (R := ℤ) 7 3).trace = 55 ∧
      (claspSL2 (R := ℤ) 5 5).trace = 63 ∧
      (claspSL2 (R := ℤ) 5 7).trace = 85 ∧
      (claspSL2 (R := ℤ) 7 5).trace = 85 ∧
      (claspSL2 (R := ℤ) 7 7).trace = 115 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro n1 n2 h1 h2
    rw [(claspSL2_det_and_trace (R := ℤ) n1 n2).2, mul_assoc]
    have hn1 : (1 : ℤ) ≤ (n1 : ℤ) := Int.ofNat_le.mpr h1
    have hn2 : (1 : ℤ) ≤ (n2 : ℤ) := Int.ofNat_le.mpr h2
    have hp : (1 : ℤ) ≤ (n1 : ℤ) * (n2 : ℤ) := by
      simpa using mul_le_mul hn1 hn2 (by decide : (0 : ℤ) ≤ 1) (by omega)
    omega
  all_goals
    rw [(claspSL2_det_and_trace (R := ℤ) _ _).2]
    decide

/-- **Hecke `H₃(q)` `S^{(2,1)}` `2 × 2` Image of `β_clasp(n₁, n₂) = σ₁^{n₁} σ₂^{-n₂} σ₁ σ₂⁻¹`:** -/
def claspHecke21 {K : Type*} [Field K] (q : K) (n1 n2 : ℕ) : Matrix (Fin 2) (Fin 2) K :=
  (rho21_sigma0 q ^ n1) * (rho21_sigma1_inv q ^ n2) * rho21_sigma0 q * rho21_sigma1_inv q

/-- Rank-2 (Convention-D) full `H₃(q)` Markov trace of `β_clasp(n₁, n₂)`. -/
def claspMarkovTrace2 {K : Type*} [Field K] (q : K) (n1 n2 : ℕ) : K :=
  ocneanuW2_sym q * (q ^ n1 * q⁻¹ ^ n2) +
    ocneanuW2_mix q * (claspHecke21 q n1 n2).trace

/-- Rank-3 (`W₃*`, `z₃ = q³/[3]_q`) full `H₃(q)` Markov trace of `β_clasp(n₁, n₂)`. -/
def claspMarkovTrace3 {K : Type*} [Field K] (q : K) (n1 n2 : ℕ) : K :=
  ocneanuW3_sym q * (q ^ n1 * q⁻¹ ^ n2) +
    ocneanuW3_mix q * (claspHecke21 q n1 n2).trace +
    ocneanuW3_alt q * ((-q⁻¹) ^ n1 * (-q) ^ n2)

theorem rho21_V_eq {K : Type*} [Field K] {q : K} (hq : q ≠ 0) :
    rho21_V q = !![1 - q⁻¹ ^ 2, q; -q, -q ^ 2] := by
  unfold rho21_V
  rw [rho21_sigma0_eq, rho21_sigma1_inv_eq]
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)

theorem rho21_sigma0_pow3 {K : Type*} [Field K] {q : K} (hq : q ≠ 0) :
    rho21_sigma0 q ^ 3 = !![-q⁻¹ ^ 3, -(q ^ 2 - 1 + q⁻¹ ^ 2); 0, q ^ 3] := by
  have hp3 : rho21_sigma0 q ^ 3 = (rho21_sigma0 q * rho21_sigma0 q) * rho21_sigma0 q := by
    simp [pow_succ, Matrix.mul_assoc]
  rw [hp3, rho21_sigma0_eq]
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)

theorem rho21_sigma0_pow5 {K : Type*} [Field K] {q : K} (hq : q ≠ 0) :
    rho21_sigma0 q ^ 5 =
      !![-q⁻¹ ^ 5, -(q ^ 4 - q ^ 2 + 1 - q⁻¹ ^ 2 + q⁻¹ ^ 4); 0, q ^ 5] := by
  have hp5 : rho21_sigma0 q ^ 5 = (rho21_sigma0 q ^ 3 * rho21_sigma0 q) * rho21_sigma0 q := by
    simp [pow_succ, Matrix.mul_assoc]
  rw [hp5, rho21_sigma0_pow3 hq, rho21_sigma0_eq]
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)

theorem rho21_sigma1_inv_pow3 {K : Type*} [Field K] {q : K} (hq : q ≠ 0) :
    rho21_sigma1_inv q ^ 3 = !![q⁻¹ ^ 3, 0; -(q ^ 2 - 1 + q⁻¹ ^ 2), -q ^ 3] := by
  have hp3 : rho21_sigma1_inv q ^ 3 =
      (rho21_sigma1_inv q * rho21_sigma1_inv q) * rho21_sigma1_inv q := by
    simp [pow_succ, Matrix.mul_assoc]
  rw [hp3, rho21_sigma1_inv_eq]
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)

theorem rho21_sigma1_inv_pow5 {K : Type*} [Field K] {q : K} (hq : q ≠ 0) :
    rho21_sigma1_inv q ^ 5 =
      !![q⁻¹ ^ 5, 0; -(q ^ 4 - q ^ 2 + 1 - q⁻¹ ^ 2 + q⁻¹ ^ 4), -q ^ 5] := by
  have hp5 : rho21_sigma1_inv q ^ 5 =
      (rho21_sigma1_inv q ^ 3 * rho21_sigma1_inv q) * rho21_sigma1_inv q := by
    simp [pow_succ, Matrix.mul_assoc]
  rw [hp5, rho21_sigma1_inv_pow3 hq, rho21_sigma1_inv_eq]
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)

/-- **`S^{(2,1)}` Symmetry vs Full `H₃(q)` Markov-Trace Separation of `D̄⁰ = (5, 3)` and `K⁰ = (3, 5)`:**
1. Both `claspHecke21 q 5 3` and `claspHecke21 q 3 5` lie in `SL₂(K)` (`det = 1`) and have
   **identical** `2 × 2` `S^{(2,1)}` trace (`tr_{(2,1)}(5, 3) = tr_{(2,1)}(3, 5)`).
2. Consequently, in BOTH the rank-2 (`z₂`) and rank-3 (`z₃`) full `H₃(q)` Markov traces, the
   `S^{(2,1)}` term cancels identically and `D̄⁰ = (5, 3)` separates from `K⁰ = (3, 5)` by exact
   closed-form multiples of `q² - q⁻²`. -/
theorem claspMarkovTrace_separates_Dbar0_K0 {K : Type*} [Field K] {q : K} (hq : q ≠ 0) :
    (claspHecke21 q 5 3).det = 1 ∧
      (claspHecke21 q 3 5).det = 1 ∧
      (claspHecke21 q 5 3).trace = (claspHecke21 q 3 5).trace ∧
      claspMarkovTrace2 q 5 3 - claspMarkovTrace2 q 3 5 =
        ocneanuW2_sym q * (q ^ 2 - q⁻¹ ^ 2) ∧
      claspMarkovTrace3 q 5 3 - claspMarkovTrace3 q 3 5 =
        (ocneanuW3_sym q - ocneanuW3_alt q) * (q ^ 2 - q⁻¹ ^ 2) := by
  have hV_det : (rho21_V q).det = 1 := det_V_21 hq
  have hc53 : claspHecke21 q 5 3 = (rho21_sigma0 q ^ 5) * (rho21_sigma1_inv q ^ 3) * rho21_V q := by
    unfold claspHecke21 rho21_V; simp [Matrix.mul_assoc]
  have hc35 : claspHecke21 q 3 5 = (rho21_sigma0 q ^ 3) * (rho21_sigma1_inv q ^ 5) * rho21_V q := by
    unfold claspHecke21 rho21_V; simp [Matrix.mul_assoc]
  have hdet53 : (claspHecke21 q 5 3).det = 1 := by
    rw [hc53, Matrix.det_mul, Matrix.det_mul, hV_det, rho21_sigma0_pow5 hq, rho21_sigma1_inv_pow3 hq]
    simp [Matrix.det_fin_two]
    field_simp
  have hdet35 : (claspHecke21 q 3 5).det = 1 := by
    rw [hc35, Matrix.det_mul, Matrix.det_mul, hV_det, rho21_sigma0_pow3 hq, rho21_sigma1_inv_pow5 hq]
    simp [Matrix.det_fin_two]
    field_simp
  have htr : (claspHecke21 q 5 3).trace = (claspHecke21 q 3 5).trace := by
    rw [hc53, hc35, rho21_sigma0_pow5 hq, rho21_sigma1_inv_pow3 hq,
        rho21_sigma0_pow3 hq, rho21_sigma1_inv_pow5 hq, rho21_V_eq hq]
    simp [Matrix.trace_fin_two]
    field_simp; ring
  have hpow53 : q ^ 5 * q⁻¹ ^ 3 - q ^ 3 * q⁻¹ ^ 5 = q ^ 2 - q⁻¹ ^ 2 := by
    field_simp
  have hpow53_alt : (-q⁻¹) ^ 5 * (-q) ^ 3 - (-q⁻¹) ^ 3 * (-q) ^ 5 = -(q ^ 2 - q⁻¹ ^ 2) := by
    field_simp; ring
  refine ⟨hdet53, hdet35, htr, ?_, ?_⟩
  · unfold claspMarkovTrace2
    rw [htr]
    linear_combination ocneanuW2_sym q * hpow53
  · unfold claspMarkovTrace3
    rw [htr]
    linear_combination ocneanuW3_sym q * hpow53 + ocneanuW3_alt q * hpow53_alt

/-- Integer-scaled `(V₂, W₃*)`-framed meson clasp invariant `(mesonGenerationPair, 6 Q₁, 6 Q₂)`. -/
def framedMesonSixClaspDatum (m : Meson) : (ℕ × ℕ) × ℤ × ℤ :=
  (mesonGenerationPair m,
   framedSixCharge ((constituents m).1, false),
   framedSixCharge ((constituents m).2, true))

/-- Complete `(V₂, W₃*)`-framed meson clasp invariant over `ℚ`:
`(mesonGenerationPair m, framedStrandCharge (antiquark, false), framedStrandCharge (quark, true))`. -/
def framedMesonClaspDatum (m : Meson) : (ℕ × ℕ) × ℚ × ℚ :=
  (mesonGenerationPair m,
   framedStrandCharge (K := ℚ) ((constituents m).1, false),
   framedStrandCharge (K := ℚ) ((constituents m).2, true))

theorem framedMesonSixClaspDatum_injective : Function.Injective framedMesonSixClaspDatum := by
  decide

/-- **Global Injectivity on All Five Dictionary Mesons (`pion`, `kaon`, `etaPhi`, `Dmeson`, `K0`):**
Combining the ordered 3-strand clasp pair `(n₁, n₂)` with the `(V₂, W₃*)`-framed constituent
charges separates `D̄⁰` (`((5,3), -2/3, +2/3)`) from `K⁰` (`((3,5), +1/3, -1/3)`) AND separates
`K⁻` (`((3,5), -2/3, -1/3)`) from `K⁰` (`((3,5), +1/3, -1/3)`), making `framedMesonClaspDatum`
injective on `Meson`. -/
theorem framedMesonClaspDatum_injective : Function.Injective framedMesonClaspDatum := by
  have h2 : (2 : ℚ) ≠ 0 := by intro h; exact absurd (Rat.num_eq_zero.mpr h) (by decide)
  have h3 : (3 : ℚ) ≠ 0 := by intro h; exact absurd (Rat.num_eq_zero.mpr h) (by decide)
  have h6 : (6 : ℚ) ≠ 0 := by intro h; exact absurd (Rat.num_eq_zero.mpr h) (by decide)
  intro m1 m2 h
  apply framedMesonSixClaspDatum_injective
  unfold framedMesonClaspDatum at h
  rw [framedStrandCharge_eq_sixCharge_div h2 h3,
      framedStrandCharge_eq_sixCharge_div h2 h3,
      framedStrandCharge_eq_sixCharge_div h2 h3,
      framedStrandCharge_eq_sixCharge_div h2 h3] at h
  injection h with hp hrest
  injection hrest with hq1 hq2
  have hz1 : (framedSixCharge ((constituents m1).1, false) : ℚ) =
      (framedSixCharge ((constituents m2).1, false) : ℚ) :=
    (div_left_inj' h6).mp hq1
  have hz2 : (framedSixCharge ((constituents m1).2, true) : ℚ) =
      (framedSixCharge ((constituents m2).2, true) : ℚ) :=
    (div_left_inj' h6).mp hq2
  exact Prod.ext hp (Prod.ext (Int.cast_injective hz1) (Int.cast_injective hz2))

end HyperbolicMesonClasp

/-! ## Section 3: `H₃(q)` Diquark Spin-Isospin Projector Split on `S^{(2,1)}` (`qou-pwz4`) -/

section DiquarkProjectorSplit

variable {K : Type*} [Field K]

/-- `I = 0` (`Λ`-type, antisymmetric `ud` diquark, `σ₁`-eigenvalue `-q⁻¹`) rank-1 projector on `S^{(2,1)}`. -/
def projDiquarkLambda (q : K) : Matrix (Fin 2) (Fin 2) K :=
  (q + q⁻¹)⁻¹ • (q • (1 : Matrix (Fin 2) (Fin 2) K) - rho21_sigma0 q)

/-- `I = 1` (`Σ⁰`-type, symmetric `ud` diquark, `σ₁`-eigenvalue `+q`) rank-1 projector on `S^{(2,1)}`. -/
def projDiquarkSigma0 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  (q + q⁻¹)⁻¹ • (rho21_sigma0 q + q⁻¹ • (1 : Matrix (Fin 2) (Fin 2) K))

/-- Jucys–Murphy diquark full-twist operator `J₂ = σ₁²` on `S^{(2,1)}`. -/
def jm2 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  rho21_sigma0 q ^ 2

/-- Jucys–Murphy strange-spectator twist operator `J₃ = σ₂ σ₁² σ₂` on `S^{(2,1)}`. -/
def jm3 (q : K) : Matrix (Fin 2) (Fin 2) K :=
  rho21_sigma1 q * (rho21_sigma0 q ^ 2) * rho21_sigma1 q

theorem projDiquarkLambda_eq {q : K} (hq2 : q + q⁻¹ ≠ 0) :
    projDiquarkLambda q = !![1, (q + q⁻¹)⁻¹; 0, 0] := by
  have hid : (q + q⁻¹)⁻¹ * (q + q⁻¹) = 1 := inv_mul_cancel₀ hq2
  unfold projDiquarkLambda
  rw [rho21_sigma0_eq]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sub_neg_eq_add, hid]

theorem projDiquarkSigma0_eq {q : K} (hq2 : q + q⁻¹ ≠ 0) :
    projDiquarkSigma0 q = !![0, -(q + q⁻¹)⁻¹; 0, 1] := by
  have hid : (q + q⁻¹)⁻¹ * (q + q⁻¹) = 1 := inv_mul_cancel₀ hq2
  unfold projDiquarkSigma0
  rw [rho21_sigma0_eq]
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [hid]

/-- **Complete Orthogonal Idempotent Decomposition of `S^{(2,1)}` into `Λ` (`I = 0`) and `Σ⁰` (`I = 1`) Diquarks:** -/
theorem projDiquark_complete_orthogonal_idempotents {q : K} (hq2 : q + q⁻¹ ≠ 0) :
    projDiquarkLambda q + projDiquarkSigma0 q = 1 ∧
      projDiquarkLambda q * projDiquarkLambda q = projDiquarkLambda q ∧
      projDiquarkSigma0 q * projDiquarkSigma0 q = projDiquarkSigma0 q ∧
      projDiquarkLambda q * projDiquarkSigma0 q = 0 ∧
      projDiquarkSigma0 q * projDiquarkLambda q = 0 ∧
      (projDiquarkLambda q).trace = 1 ∧
      (projDiquarkSigma0 q).trace = 1 := by
  rw [projDiquarkLambda_eq hq2, projDiquarkSigma0_eq hq2]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · ext i j; fin_cases i <;> fin_cases j <;> simp
  · ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]
  · ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]
  · ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]
  · ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]
  · simp [Matrix.trace_fin_two]
  · simp [Matrix.trace_fin_two]

/-- **Jucys–Murphy Commutativity, Twist Eigenvalue Split (`q²` vs `q⁻²`), and `3 × 3` Weight-Space Bridge:** -/
theorem jm2_jm3_comm_and_diquark_split {q : K}
    (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    jm2 q * jm3 q = jm3 q * jm2 q ∧
      (projDiquarkSigma0 q * jm2 q).trace = q ^ 2 ∧
      (projDiquarkLambda q * jm2 q).trace = q⁻¹ ^ 2 ∧
      (projDiquarkSigma0 q * jm2 q).trace - (projDiquarkLambda q * jm2 q).trace =
        (q - q⁻¹) * (q + q⁻¹) ∧
      (projDiquarkLambda q * rho21_sigma1 q).trace =
        (eLambda q * A₂ q).trace ∧
      (projDiquarkSigma0 q * rho21_sigma1 q).trace =
        (eSigma0 q * A₂ q).trace := by
  have hq2' : q + q⁻¹ ≠ 0 := hq2
  have hqp : q ^ 2 + 1 ≠ 0 := q2_add_one_ne_zero q hq hq2
  have hjm2 : jm2 q = !![q⁻¹ ^ 2, -(q - q⁻¹); 0, q ^ 2] := (A12_and_inv_explicit hq).1
  have hjm3 : jm3 q = !![q ^ 2, q - q⁻¹; 0, q⁻¹ ^ 2] := by
    unfold jm3
    change rho21_sigma1 q * jm2 q * rho21_sigma1 q = _
    rw [hjm2, rho21_sigma1_eq]
    ext i j; fin_cases i <;> fin_cases j <;>
      (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)
  have htr_s : (projDiquarkSigma0 q * jm2 q).trace = q ^ 2 := by
    rw [projDiquarkSigma0_eq hq2', hjm2]
    simp [Matrix.trace_fin_two]
  have htr_l : (projDiquarkLambda q * jm2 q).trace = q⁻¹ ^ 2 := by
    rw [projDiquarkLambda_eq hq2', hjm2]
    simp [Matrix.trace_fin_two]
  refine ⟨?_, htr_s, htr_l, ?_, ?_, ?_⟩
  · rw [hjm2, hjm3]
    ext i j; fin_cases i <;> fin_cases j <;>
      (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)
  · rw [htr_s, htr_l]; ring
  · rw [trace_eLambda_A2_eq_zD q hq, projDiquarkLambda_eq hq2', rho21_sigma1_eq]
    simp [Matrix.trace_fin_two]
    field_simp; ring
  · rw [trace_eSigma0_A2 q hq hq2 hq3, projDiquarkSigma0_eq hq2', rho21_sigma1_eq]
    simp [Matrix.trace_fin_two]
    field_simp; ring

/-- **Borromean Single-Step (`V`) Ratio `q⁶` and Full Borromean (`V³`) `Λ–Σ⁰` Diquark Split:**
1. On the single Borromean step `V = σ₁ σ₂⁻¹`, `tr(P_{Σ⁰} V) = -q⁴ / (q² + 1)` and
   `tr(P_Λ V) = -1 / (q² (q² + 1))`, so `tr(P_{Σ⁰} V) = q⁶ * tr(P_Λ V)`.
2. On the full Borromean baryon braid `V³ = (σ₁ σ₂⁻¹)³`, the zero-parameter `Λ–Σ⁰` diquark
   splitting factors cleanly as:
   `tr(P_Λ V³) - tr(P_{Σ⁰} V³) = (q - q⁻¹)³ * (q² + q⁻²) * [3]_q / (q + q⁻¹)`. -/
theorem trace_projDiquark_V_and_V3_split {q : K} (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) :
    (projDiquarkSigma0 q * rho21_V q).trace = -q ^ 4 / (q ^ 2 + 1) ∧
      (projDiquarkLambda q * rho21_V q).trace = -1 / (q ^ 2 * (q ^ 2 + 1)) ∧
      (projDiquarkSigma0 q * rho21_V q).trace =
        q ^ 6 * (projDiquarkLambda q * rho21_V q).trace ∧
      (projDiquarkLambda q * (rho21_V q ^ 3)).trace -
        (projDiquarkSigma0 q * (rho21_V q ^ 3)).trace =
        (q - q⁻¹) ^ 3 * (q ^ 2 + q⁻¹ ^ 2) * qBracket3 q / (q + q⁻¹) := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  have hqp : q ^ 2 + 1 ≠ 0 := by
    intro h0; apply hq2
    have hm : q * (q + q⁻¹) = q ^ 2 + 1 := by linear_combination hqi
    exact (mul_eq_zero.mp (hm.trans h0)).resolve_left hq
  have hVs : (projDiquarkSigma0 q * rho21_V q).trace = -q ^ 4 / (q ^ 2 + 1) := by
    rw [projDiquarkSigma0_eq hq2, rho21_V_eq hq]
    simp [Matrix.trace_fin_two]
    field_simp; ring
  have hVl : (projDiquarkLambda q * rho21_V q).trace = -1 / (q ^ 2 * (q ^ 2 + 1)) := by
    rw [projDiquarkLambda_eq hq2, rho21_V_eq hq]
    simp [Matrix.trace_fin_two]
    field_simp; ring
  have hV2 : rho21_V q ^ 2 =
      !![1 - 2 * q⁻¹ ^ 2 + q⁻¹ ^ 4 - q ^ 2, q - q⁻¹ - q ^ 3;
         -q + q⁻¹ + q ^ 3, -q ^ 2 + q ^ 4] := by
    rw [sq, rho21_V_eq hq]
    ext i j; fin_cases i <;> fin_cases j <;>
      (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)
  have hV3 : rho21_V q ^ 3 =
      !![3 - 3 * q⁻¹ ^ 2 + 3 * q⁻¹ ^ 4 - q⁻¹ ^ 6 - 2 * q ^ 2 + q ^ 4,
         2 * q - 2 * q⁻¹ + q⁻¹ ^ 3 - 2 * q ^ 3 + q ^ 5;
         -2 * q + 2 * q⁻¹ - q⁻¹ ^ 3 + 2 * q ^ 3 - q ^ 5,
         -q ^ 2 + 1 + 2 * q ^ 4 - q ^ 6] := by
    have hp3 : rho21_V q ^ 3 = rho21_V q ^ 2 * rho21_V q := by rw [pow_succ]
    rw [hp3, hV2, rho21_V_eq hq]
    ext i j; fin_cases i <;> fin_cases j <;>
      (simp [Matrix.mul_apply, Fin.sum_univ_two]; try field_simp; try ring)
  refine ⟨hVs, hVl, ?_, ?_⟩
  · rw [hVs, hVl]
    field_simp
  · rw [projDiquarkLambda_eq hq2, projDiquarkSigma0_eq hq2, hV3]
    unfold qBracket3
    simp [Matrix.trace_fin_two]
    field_simp; ring

end DiquarkProjectorSplit

/-! ## Section 4: `O((q - q⁻¹)²)` 2nd-Order Quantum Casimir Gell-Mann–Okubo Identity (`qou-c9uj`) -/

section QuantumCasimirGMO

variable {K : Type*} [Field K]

/-- Rational quantum Casimir `d_q(1, 0) = [1]_q [2]_q - [0]_q² = q + q⁻¹` on `I = 1, Y = 0` (`π` / `Σ`). -/
def qCasimirIsospinOne (q : K) : K := q + q⁻¹

/-- Rational quantum Casimir `d_q(0, 0) = 0` on `I = 0, Y = 0` (`η` / `Λ`). -/
def qCasimirSinglet (_q : K) : K := 0

/-- Rational quantum Casimir `d_q(1/2, ±1) = [1/2]_q [3/2]_q - [1/2]_q² = (q + q⁻¹) / (q + 2 + q⁻¹)`
on `I = 1/2, Y = ±1` (`K`, `K̄`, `N`, `Ξ`) — square-root-free over any field! -/
def qCasimirDoublet (q : K) : K := (q + q⁻¹) / (q + 2 + q⁻¹)

/-- Octet mass (or mass-squared) operator `M(I, Y) = a + b Y + c d_q(I, Y)`. -/
def qOctetMass (a b c dVal Y : K) : K := a + b * Y + c * dVal

/-- Doubled hypercharge-averaged Gell-Mann–Okubo combination
`2 (M(1/2, +1) + M(1/2, -1)) - 3 M(0, 0) - M(1, 0)` (`= 4 M_K - 3 M_η - M_π`). -/
def qCasimirGMOCombination (a b c q : K) : K :=
  2 * (qOctetMass a b c (qCasimirDoublet q) 1 + qOctetMass a b c (qCasimirDoublet q) (-1)) -
    3 * qOctetMass a b c (qCasimirSinglet q) 0 -
    qOctetMass a b c (qCasimirIsospinOne q) 0

/-- **Classical `q = 1` Recovery and `O((q - q⁻¹)²)` Parameter-Free Quantum Casimir GMO Law (`qou-c9uj`):**
1. At `q = 1` (`2 ≠ 0`), `(qCasimirIsospinOne 1, qCasimirSinglet 1, qCasimirDoublet 1) = (2, 0, 1/2)`
   and `qCasimirGMOCombination a b c 1 = 0` for all `a, b, c` (recovering `GellMannOkuboIdentity`).
2. For generic `q` (`q ≠ 0`, `q + 1 ≠ 0`), `a` and `b` cancel identically and
   `qCasimirGMOCombination a b c q = -c * (q - q⁻¹)² * (q + q⁻¹) / (q + 2 + q⁻¹)²`.
3. Whenever `c ≠ 0` and `q + q⁻¹ ≠ 0`, `c` ALSO cancels in the normalized GMO ratio against the
   `Y = 0` isospin split `M(1, 0) - M(0, 0)` (`m_π² - m_η²` for mesons, `m_Σ - m_Λ` for baryons),
   giving the universal bar-invariant `(a, b, c)`-free law:
   `qCasimirGMOCombination a b c q / (M(1,0) - M(0,0)) = -((q - 1) / (q + 1))² = -(q - q⁻¹)² / ((q + q⁻¹) + 2)²`. -/
theorem qCasimir_gmo_second_order_and_universal_ratio (a b c q : K)
    (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) (hqp1 : q + 1 ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hc : c ≠ 0) :
    (qCasimirIsospinOne (1 : K) = 2 ∧
      qCasimirDoublet (1 : K) = (1 : K) / 2 ∧
      qCasimirGMOCombination a b c (1 : K) = 0) ∧
      qCasimirGMOCombination a b c q =
        -c * (q - q⁻¹) ^ 2 * (q + q⁻¹) / (q + 2 + q⁻¹) ^ 2 ∧
      qCasimirGMOCombination a b c q /
        (qOctetMass a b c (qCasimirIsospinOne q) 0 - qOctetMass a b c (qCasimirSinglet q) 0) =
        -((q - 1) / (q + 1)) ^ 2 ∧
      -((q - 1) / (q + 1)) ^ 2 = -(q - q⁻¹) ^ 2 / ((q + q⁻¹) + 2) ^ 2 := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  have h4 : (4 : K) ≠ 0 := by
    have e : (4 : K) = 2 * 2 := by ring
    rw [e]; exact mul_ne_zero h2 h2
  have hden1_val : (1 : K) + 2 + (1 : K)⁻¹ = 4 := by ring
  have hm_den : q * (q + 2 + q⁻¹) = (q + 1) ^ 2 := by linear_combination hqi
  have hdenq : q + 2 + q⁻¹ ≠ 0 := by
    intro h0
    have hsq0 : (q + 1) ^ 2 = 0 := hm_den.symm.trans (by rw [h0, mul_zero])
    exact pow_ne_zero 2 hqp1 hsq0
  have hdenq' : (q + q⁻¹) + 2 ≠ 0 := by
    intro h0; apply hdenq; linear_combination h0
  have hcd_one : qCasimirDoublet (1 : K) = (1 : K) / 2 := by
    unfold qCasimirDoublet
    rw [hden1_val, show (1 : K) + (1 : K)⁻¹ = 2 by ring, div_eq_div_iff h4 h2]
    ring
  have hq1 : (qCasimirIsospinOne (1 : K) = 2 ∧
      qCasimirDoublet (1 : K) = (1 : K) / 2 ∧
      qCasimirGMOCombination a b c (1 : K) = 0) := by
    refine ⟨by unfold qCasimirIsospinOne; ring, hcd_one, ?_⟩
    unfold qCasimirGMOCombination qOctetMass qCasimirSinglet qCasimirIsospinOne
    rw [hcd_one, show (1 : K) + (1 : K)⁻¹ = 2 by ring]
    have h2i : (2 : K) * (2 : K)⁻¹ = 1 := mul_inv_cancel₀ h2
    simp only [div_eq_mul_inv]
    linear_combination 2 * c * h2i
  have hgmo :
      qCasimirGMOCombination a b c q =
        -c * (q - q⁻¹) ^ 2 * (q + q⁻¹) / (q + 2 + q⁻¹) ^ 2 := by
    unfold qCasimirGMOCombination qOctetMass qCasimirSinglet qCasimirIsospinOne
    have hexp :
        2 * (a + b * 1 + c * qCasimirDoublet q + (a + b * -1 + c * qCasimirDoublet q)) -
            3 * (a + b * 0 + c * 0) - (a + b * 0 + c * (q + q⁻¹)) =
          c * (4 * qCasimirDoublet q - (q + q⁻¹)) := by ring
    rw [hexp]
    unfold qCasimirDoublet
    rw [eq_div_iff (pow_ne_zero 2 hdenq)]
    have hd_inv : (q + 2 + q⁻¹) * ((q + q⁻¹) / (q + 2 + q⁻¹)) = q + q⁻¹ :=
      mul_div_cancel₀ _ hdenq
    calc
      c * (4 * ((q + q⁻¹) / (q + 2 + q⁻¹)) - (q + q⁻¹)) * (q + 2 + q⁻¹) ^ 2
          = c * (q + 2 + q⁻¹) * (4 * ((q + 2 + q⁻¹) * ((q + q⁻¹) / (q + 2 + q⁻¹))) -
              (q + q⁻¹) * (q + 2 + q⁻¹)) := by ring
      _ = c * (q + 2 + q⁻¹) * (4 * (q + q⁻¹) - (q + q⁻¹) * (q + 2 + q⁻¹)) := by rw [hd_inv]
      _ = -c * (q - q⁻¹) ^ 2 * (q + q⁻¹) := by
            linear_combination -4 * c * (q + q⁻¹) * hqi
  have hsplit :
      qOctetMass a b c (qCasimirIsospinOne q) 0 - qOctetMass a b c (qCasimirSinglet q) 0 =
        c * (q + q⁻¹) := by
    unfold qOctetMass qCasimirIsospinOne qCasimirSinglet; ring
  have hratio_bar : -((q - 1) / (q + 1)) ^ 2 = -(q - q⁻¹) ^ 2 / ((q + q⁻¹) + 2) ^ 2 := by
    rw [div_pow, ← neg_div, div_eq_div_iff (pow_ne_zero 2 hqp1) (pow_ne_zero 2 hdenq')]
    have hm1 : q * (q - q⁻¹) = q ^ 2 - 1 := by linear_combination -hqi
    have hm2 : q * ((q + q⁻¹) + 2) = (q + 1) ^ 2 := by linear_combination hqi
    apply mul_left_cancel₀ (pow_ne_zero 2 hq)
    calc
      q ^ 2 * (-(q - 1) ^ 2 * (q + q⁻¹ + 2) ^ 2)
          = -(q - 1) ^ 2 * (q * ((q + q⁻¹) + 2)) ^ 2 := by ring
      _ = -(q - 1) ^ 2 * ((q + 1) ^ 2) ^ 2 := by rw [hm2]
      _ = -((q ^ 2 - 1) ^ 2) * (q + 1) ^ 2 := by ring
      _ = -(q * (q - q⁻¹)) ^ 2 * (q + 1) ^ 2 := by rw [hm1]
      _ = q ^ 2 * (-(q - q⁻¹) ^ 2 * (q + 1) ^ 2) := by ring
  refine ⟨hq1, hgmo, ?_, hratio_bar⟩
  rw [hgmo, hsplit, hratio_bar, div_div,
      div_eq_div_iff (mul_ne_zero (pow_ne_zero 2 hdenq) (mul_ne_zero hc hq2))
        (pow_ne_zero 2 hdenq')]
  ring

end QuantumCasimirGMO

end QOU.Eightfold.HyperbolicMesonClaspAndDiquarkSplit
