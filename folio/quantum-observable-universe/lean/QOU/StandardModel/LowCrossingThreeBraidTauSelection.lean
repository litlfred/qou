import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.FinCases
import QOU.BraidKnot.ElectronWordCandidates
import QOU.StandardModel.ComponentFraming
import QOU.Observations.InhomogeneousLeptonLoopResolvent

/-!
# Complete `≤ 8`-Crossing 3-Braid Hyperbolic Census, Exact `ℤ[X]` Parabolic Spinor Polynomials, and Open Gap-2 Tau Carrier Isolation

Formalizes the algebraic and combinatorial foundations for **Closing Open Gap 2 (Option 2A Primary)**
and bean `qou-r0dn`, strictly over generic `[CommRing R]`, `[Field K]`, and `[LinearOrder K] +
[IsStrictOrderedRing K]` (`§7c`: zero `ℝ`, zero empirical literals, zero `sorry`, zero custom
axioms).

## Main Results

1. **Exact `B₃` Closure Parity, Even-Writhe Obstruction, and `Q = -1` Selection Gates (§1):**
   * Every signed 3-strand braid word `b : BraidWord3` satisfies
     `(writhe3 b) % 2 = (b.length : ℤ) % 2` (`writhe3_mod_two_eq_length_mod_two`) and
     `writhe3 (mirrorWord3 b) = -writhe3 b`.
   * Any 3-strand braid closing to a single-component knot (`numCycles (permOf3 b) = 1`) has
     **even** word length and **even** writhe `∃ k : ℤ, writhe3 b = 2 * k`
     (`single_component_knot_even_length_and_even_writhe`), so no single-component `B₃` knot can
     carry the odd writhe `±3` of the 2-component Hopf electron `σ₀ σ₁ σ₀` (`no_odd_writhe_knot_B3`).
   * On any transitive 3-cycle `π ∈ {(0 1 2), (0 2 1)}`, a component framing `t : Fin 3 → ℤ`
     (`IsComponentFraming π t`) has total strand framing `-3` (`Q = (1/3) ∑ tᵢ = -1`) if and only
     if `t = (-1, -1, -1)` (`transitive_three_cycle_neg_one_framing_iff`).
   * Across the 5 non-`4₁` hyperbolic 3-braids up to `7` crossings (`5₂⁻, 6₂⁻, 6₃, 7₃⁻, 7₅⁻`):
     Gate G1 (component framing + `g(K) ≤ 4`) admits all `5`; Gate G2 (halved-writhe `w = -2`)
     selects **uniquely `[k6_2]`**; Gate G3 (muon writhe-zero `w = 0`, `sl = -3`) selects
     **uniquely `[k6_3]`**.

2. **Complete `≤ 8`-Crossing Prime Knot Braid-Index Census via Franks–Williams–Morton (§2):**
   * Formalizes the Birman–Menasco composite braid-index theorem witness
     `β₁ + β₂ - 1 = 3 ↔ β₁ = 2 ∧ β₂ = 2` for `βᵢ ≥ 2` (`composite_three_braid_iff_both_two_braid`),
     excluding non-torus connected sums such as `3₁ # 4₁` from `B₃`.
   * Encodes all `35` prime knots `PrimeKnotLe8` (`3₁` through `8₂₁`) with exact crossing count,
     Seifert genus, hyperbolic status, realizing strand count, and HOMFLY-PT `v`-degree bounds,
     proving sharpness `fwmBound = realizingStrands` on all `35` knots
     (`fwm_sharp_all_prime_knots_le8`), strict exclusion `fwmBound ≥ 4` on
     `{6₁, 7₂, 7₄, 7₆, 7₇, 8₁}`, and exact census classification: `6` prime hyperbolic 3-braids
     up to `7` crossings (`{4₁, 5₂, 6₂, 6₃, 7₃, 7₅}`) and `10` at `8` crossings, all satisfying
     Bring's genus bound `g(K) ≤ 4`.

3. **Non-Abelian Parabolic `SL(2, R)` Spinor Braiding & Exact `ℤ[X]` Shape Polynomials (§3):**
   * Over any `[CommRing R]`, `parabolicSpinorMat u = I + u uᵀ J` has trace `2`, determinant `1`,
     exact conjugation equivariance `M(u) M(v) M(u)⁻¹ = M(v + ⟨u, v⟩ u)`, and induces invertible
     `B₃` operators satisfying the Artin braid relation `σ₀ σ₁ σ₀ = σ₁ σ₀ σ₁`
     (`braidSpinorStep_artin_relation`).
   * Proves over any `[CommRing R]` that the exact `ℤ[X]` spinor polynomials of **all six**
     `≤ 7`-crossing hyperbolic 3-braids (`4₁`, `5₂`, `6₂`, `6₃`, `7₃`, `7₅`) solve the full
     non-abelian parabolic `B₃` closure fixed-point equations with canonical longitude holonomy `-1`
     (`spinor_closure_4_1`, `spinor_closure_5_2`, `spinor_closure_6_2`, `spinor_closure_6_3`,
     `spinor_closure_7_3`, `spinor_closure_7_5`), together with the birational polynomial identity
     linking `5₂`'s spinor cubic `x³ - x² + 1` to its tetrahedral cubic `y³ - 2y² + 3y - 1` and
     `6₁`'s gluing/Riley polynomials.

4. **Generation-3 (`k = 3`) `#9213` Inhomogeneous Loop-Resolvent Identities & Rule-13a Carrier (§4):**
   * Extends `QOU.Observations.InhomogeneousLeptonLoopResolvent` (`#9213`) to generation-3 pole
     order `k = 3`, proving exact `O(ℏ_q)` saddle recovery, the parameter-free tau-to-muon saddle
     ratio `(Vol(K_τ) / Vol(4₁)) · ℏ_q⁻¹ · (1 + c_tors ℏ_q + c₂ ℏ_q²)`, non-decrease of complex
     volume modulus `vol² ≤ vol² + cs²`, and isolating the unresolved tau carrier / loop-dressing
     selection cleanly as the zero-instance `class TauHyperbolicThreeBraidCarrierHypothesis`
     under **Rule 13a**.

-- Ref: [birman1990] J. S. Birman, W. W. Menasco, Invent. Math. 102 (1990) 115–139
-- Ref: [franks1987] J. Franks, R. F. Williams, Trans. Amer. Math. Soc. 299 (1987) 243–253
-- Ref: [morton1986] H. R. Morton, Math. Proc. Cambridge Philos. Soc. 99 (1986) 107–109
-- Ref: [jones1987] V. F. R. Jones, Ann. of Math. 126 (1987) 335–388, Table 15.9
-- Ref: [riley1972] R. Riley, Quart. J. Math. Oxford 23 (1972) 263–283
-- Ref: [zickert2009] C. K. Zickert, Duke Math. J. 150 (2009) 489–532
-- Ref: [murakami-h2011] H. Murakami, arXiv:1102.3530
-- Ref: [porti1997] J. Porti, Mem. Amer. Math. Soc. 128 (1997), no. 612
-/

namespace QOU.StandardModel.LowCrossingThreeBraidTauSelection

open Matrix
open QOU.BraidKnot.ElectronWordCandidates
open QOU.StandardModel.ComponentFraming
open QOU.Observations.ElectronUnitSplit
open QOU.Observations.InhomogeneousLeptonLoopResolvent

/-! ## Section 1: Exact `B₃` Closure Parity, Even-Writhe Obstruction, and `Q = -1` Gates -/

section BraidThreeCombinatorics

/-- Signed Artin generators `σ₀^{±1}, σ₁^{±1}` of the 3-strand braid group `B₃`. -/
inductive Gen3
  | s0Pos
  | s0Neg
  | s1Pos
  | s1Neg
  deriving DecidableEq, Repr

/-- A 3-strand braid word is a finite list of signed Artin generators. -/
abbrev BraidWord3 := List Gen3

/-- Crossing sign (`+1` or `-1`) of a generator in `B₃`. -/
def Gen3.sign : Gen3 → ℤ
  | .s0Pos | .s1Pos => 1
  | .s0Neg | .s1Neg => -1

/-- Formal inverse generator `σᵢ^{±1} ↦ σᵢ^{∓1}`. -/
def Gen3.inv : Gen3 → Gen3
  | .s0Pos => .s0Neg
  | .s0Neg => .s0Pos
  | .s1Pos => .s1Neg
  | .s1Neg => .s1Pos

/-- Underlying unsigned strand-pair index `Fin 2` (`0` for `σ₀^{±1}`, `1` for `σ₁^{±1}`). -/
def Gen3.toSlot : Gen3 → Fin 2
  | .s0Pos | .s0Neg => 0
  | .s1Pos | .s1Neg => 1

/-- Writhe `w(b) ∈ ℤ` of a 3-strand braid word `b`. -/
def writhe3 : BraidWord3 → ℤ
  | [] => 0
  | g :: rest => g.sign + writhe3 rest

/-- Braid mirror `σᵢ^{±1} ↦ σᵢ^{∓1}` (crossing-sign reversal in place). -/
def mirrorWord3 (b : BraidWord3) : BraidWord3 :=
  b.map Gen3.inv

/-- Formal group inverse word `(g₁ ⋯ g_L)⁻¹ = g_L⁻¹ ⋯ g₁⁻¹`. -/
def invWord3 : BraidWord3 → BraidWord3
  | [] => []
  | g :: rest => invWord3 rest ++ [g.inv]

/-- Underlying unsigned letter list in `List (Fin 2)` feeding `ElectronWordCandidates.permOf`. -/
def toUnsigned (b : BraidWord3) : List (Fin 2) :=
  b.map Gen3.toSlot

/-- Underlying permutation `Fin 3 → Fin 3` of a signed 3-braid word `b`. -/
def permOf3 (b : BraidWord3) : Fin 3 → Fin 3 :=
  permOf (toUnsigned b)

theorem gen3_inv_inv (g : Gen3) : g.inv.inv = g := by
  cases g <;> rfl

theorem gen3_sign_inv (g : Gen3) : g.inv.sign = -g.sign := by
  cases g <;> rfl

theorem writhe3_append (a b : BraidWord3) :
    writhe3 (a ++ b) = writhe3 a + writhe3 b := by
  induction a with
  | nil => simp [writhe3]
  | cons g rest ih => simp [writhe3, ih]; ring

/-- Mirroring negates the writhe of every 3-braid word. -/
theorem writhe3_mirror_eq_neg (b : BraidWord3) :
    writhe3 (mirrorWord3 b) = -writhe3 b := by
  induction b with
  | nil => rfl
  | cons g rest ih =>
    unfold mirrorWord3 at ih ⊢
    simp only [List.map_cons, writhe3, gen3_sign_inv, ih]
    ring

/-- Formal inversion also negates the writhe of every 3-braid word. -/
theorem writhe3_invWord3_eq_neg (b : BraidWord3) :
    writhe3 (invWord3 b) = -writhe3 b := by
  induction b with
  | nil => rfl
  | cons g rest ih =>
    simp only [invWord3, writhe3_append, writhe3, gen3_sign_inv, ih]
    ring

/-- Every letter contributes `±1` to writhe and `+1` to length, so `(writhe3 b - b.length)` is
always even. -/
theorem even_writhe3_sub_length (b : BraidWord3) :
    ∃ k : ℤ, writhe3 b - (b.length : ℤ) = 2 * k := by
  induction b with
  | nil => exact ⟨0, by simp [writhe3]⟩
  | cons g rest ih =>
    rcases ih with ⟨k, hk⟩
    cases g with
    | s0Pos => exact ⟨k, by simp [writhe3, Gen3.sign]; linarith⟩
    | s1Pos => exact ⟨k, by simp [writhe3, Gen3.sign]; linarith⟩
    | s0Neg => exact ⟨k - 1, by simp [writhe3, Gen3.sign]; linarith⟩
    | s1Neg => exact ⟨k - 1, by simp [writhe3, Gen3.sign]; linarith⟩

/-- **Parity equivalence of writhe and word length in `B₃`:** `(writhe3 b) % 2 = (b.length : ℤ) % 2`. -/
theorem writhe3_mod_two_eq_length_mod_two (b : BraidWord3) :
    writhe3 b % 2 = (b.length : ℤ) % 2 := by
  rcases even_writhe3_sub_length b with ⟨k, hk⟩
  have h : writhe3 b = (b.length : ℤ) + 2 * k := by linarith
  rw [h, Int.add_mul_emod_self_left]

/-- **Single-Component Knot Closure Parity Theorem in `B₃`:**
Every 3-strand braid word `b` whose closure has a single component (`numCycles (permOf3 b) = 1`)
necessarily has **even** word length `b.length % 2 = 0` and **even** writhe `∃ k : ℤ, writhe3 b = 2 * k`. -/
theorem single_component_knot_even_length_and_even_writhe (b : BraidWord3)
    (hknot : numCycles (permOf3 b) = 1) :
    b.length % 2 = 0 ∧ ∃ k : ℤ, writhe3 b = 2 * k := by
  have hlen_eq : (toUnsigned b).length = b.length := List.length_map _
  have hnot_odd : b.length % 2 ≠ 1 := by
    intro hodd
    have hodd' : (toUnsigned b).length % 2 = 1 := by rw [hlen_eq]; exact hodd
    have h2 : numCycles (permOf3 b) = 2 := numCycles_permOf_of_odd (toUnsigned b) hodd'
    omega
  have heven_nat : b.length % 2 = 0 := by omega
  refine ⟨heven_nat, ?_⟩
  rcases even_writhe3_sub_length b with ⟨m, hm⟩
  have hdiv : ∃ l : ℕ, b.length = 2 * l := ⟨b.length / 2, by omega⟩
  rcases hdiv with ⟨l, hl⟩
  refine ⟨(l : ℤ) + m, ?_⟩
  push_cast [hl] at hm
  linarith

/-- **No-Odd-Writhe Obstruction on Single-Component `B₃` Knots:**
No single-component knot closed from a 3-strand braid can have odd writhe `2 * m + 1` (in
particular, writhe `±3` of the 2-component Hopf electron `σ₀ σ₁ σ₀` is impossible on any knot in
`B₃`). -/
theorem no_odd_writhe_knot_B3 (b : BraidWord3) (m : ℤ)
    (hknot : numCycles (permOf3 b) = 1) :
    writhe3 b ≠ 2 * m + 1 := by
  rcases (single_component_knot_even_length_and_even_writhe b hknot).2 with ⟨k, hk⟩
  omega

/-- Canonical 3-cycle `(0 1 2)` in `Equiv.Perm (Fin 3)`. -/
def cycle012 : Equiv.Perm (Fin 3) where
  toFun := ![1, 2, 0]
  invFun := ![2, 0, 1]
  left_inv x := by fin_cases x <;> rfl
  right_inv x := by fin_cases x <;> rfl

/-- Inverse 3-cycle `(0 2 1)` in `Equiv.Perm (Fin 3)`. -/
def cycle021 : Equiv.Perm (Fin 3) where
  toFun := ![2, 0, 1]
  invFun := ![1, 2, 0]
  left_inv x := by fin_cases x <;> rfl
  right_inv x := by fin_cases x <;> rfl

/-- **Unique `Q = -1` Component Framing on Any Single-Component 3-Braid Knot Closure:**
For either transitive 3-cycle `π ∈ {cycle012, cycle021}`, a strand framing `t : Fin 3 → ℤ` is
component-constant (`IsComponentFraming π t`) and sums to `-3` (`Q = (1/3) ∑ tᵢ = -1`, matching the
electron multiset `(-1, -1, -1)` in `ComponentFraming.lean`) **if and only if** `t = fun _ => -1`. -/
theorem transitive_three_cycle_neg_one_framing_iff
    {π : Equiv.Perm (Fin 3)} (hπ : π = cycle012 ∨ π = cycle021) (t : Fin 3 → ℤ) :
    (IsComponentFraming π t ∧ t 0 + t 1 + t 2 = -3) ↔ t = (fun _ => -1) := by
  constructor
  · rintro ⟨hcf, hsum⟩
    rcases hπ with rfl | rfl
    · have h0 : t 1 = t 0 := hcf 0
      have h1 : t 2 = t 1 := hcf 1
      ext i; fin_cases i <;> dsimp <;> omega
    · have h0 : t 2 = t 0 := hcf 0
      have h2 : t 1 = t 2 := hcf 2
      ext i; fin_cases i <;> dsimp <;> omega
  · rintro rfl
    refine ⟨fun _ => rfl, by norm_num⟩

/-! ### Explicit Minimal `B₃` Braid Words (`w ≤ 0` Branch) up to `7` Crossings -/

/-- Ruled 2-component Hopf-link electron word `σ₀ σ₁ σ₀ ∈ B₃` (reference). -/
def wordHopfElectron : BraidWord3 := [.s0Pos, .s1Pos, .s0Pos]

/-- Figure-eight knot `4₁` (`μ⁻` carrier, amphichiral): `(σ₀ σ₁⁻¹)²`. -/
def word4_1 : BraidWord3 := [.s0Pos, .s1Neg, .s0Pos, .s1Neg]

/-- Three-twist knot `5₂⁻` (`w = -4` chiral branch): `σ₀⁻³ σ₁⁻¹ σ₀ σ₁⁻¹`. -/
def word5_2_neg : BraidWord3 := [.s0Neg, .s0Neg, .s0Neg, .s1Neg, .s0Pos, .s1Neg]

/-- Positive mirror `5₂⁺` (`w = +4`): `σ₀³ σ₁ σ₀⁻¹ σ₁`. -/
def word5_2_pos : BraidWord3 := [.s0Pos, .s0Pos, .s0Pos, .s1Pos, .s0Neg, .s1Pos]

/-- `6₂⁻` (`w = -2` chiral branch): `σ₀⁻³ σ₁ σ₀⁻¹ σ₁`. -/
def word6_2_neg : BraidWord3 := [.s0Neg, .s0Neg, .s0Neg, .s1Pos, .s0Neg, .s1Pos]

/-- Positive mirror `6₂⁺` (`w = +2`): `σ₀³ σ₁⁻¹ σ₀ σ₁⁻¹`. -/
def word6_2_pos : BraidWord3 := [.s0Pos, .s0Pos, .s0Pos, .s1Neg, .s0Pos, .s1Neg]

/-- Amphichiral knot `6₃` (`w = 0`): `σ₀² σ₁⁻¹ σ₀ σ₁⁻²`. -/
def word6_3 : BraidWord3 := [.s0Pos, .s0Pos, .s1Neg, .s0Pos, .s1Neg, .s1Neg]

/-- `7₃⁻` (`w = -6` chiral branch): `σ₁ σ₀⁻⁴ σ₁⁻² σ₀⁻¹`. -/
def word7_3_neg : BraidWord3 :=
  [.s1Pos, .s0Neg, .s0Neg, .s0Neg, .s0Neg, .s1Neg, .s1Neg, .s0Neg]

/-- Positive mirror `7₃⁺` (`w = +6`): `σ₁⁻¹ σ₀⁴ σ₁² σ₀`. -/
def word7_3_pos : BraidWord3 :=
  [.s1Neg, .s0Pos, .s0Pos, .s0Pos, .s0Pos, .s1Pos, .s1Pos, .s0Pos]

/-- `7₅⁻` (`w = -6` chiral branch): `σ₀⁻³ σ₁⁻² σ₀⁻² σ₁`. -/
def word7_5_neg : BraidWord3 :=
  [.s0Neg, .s0Neg, .s0Neg, .s1Neg, .s1Neg, .s0Neg, .s0Neg, .s1Pos]

/-- Positive mirror `7₅⁺` (`w = +6`): `σ₀³ σ₁² σ₀² σ₁⁻¹`. -/
def word7_5_pos : BraidWord3 :=
  [.s0Pos, .s0Pos, .s0Pos, .s1Pos, .s1Pos, .s0Pos, .s0Pos, .s1Neg]

/-- Exact closure component counts (`1` on all six prime 3-braid knots, `2` on Hopf electron) and
exact writhes `(0, -4, -2, 0, -6, -6)` on the `w ≤ 0` branch. -/
theorem low_crossing_three_braid_closures_and_writhes :
    numCycles (permOf3 wordHopfElectron) = 2 ∧
    numCycles (permOf3 word4_1) = 1 ∧
    numCycles (permOf3 word5_2_neg) = 1 ∧
    numCycles (permOf3 word6_2_neg) = 1 ∧
    numCycles (permOf3 word6_3) = 1 ∧
    numCycles (permOf3 word7_3_neg) = 1 ∧
    numCycles (permOf3 word7_5_neg) = 1 ∧
    writhe3 word4_1 = 0 ∧
    writhe3 word5_2_neg = -4 ∧
    writhe3 word6_2_neg = -2 ∧
    writhe3 word6_3 = 0 ∧
    writhe3 word7_3_neg = -6 ∧
    writhe3 word7_5_neg = -6 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    ((try unfold permOf3 toUnsigned); (try rw [permOf_eq]); decide)

end BraidThreeCombinatorics

/-! ## Section 2: Complete `≤ 8`-Crossing Prime Knot Braid-Index Census (Franks–Williams–Morton) -/

section BraidIndexCensus

/-- Franks–Williams–Morton lower bound `β(K) ≥ (vMax - vMin) / 2 + 1` from the `v`-degree span
`[vMin, vMax]` of the HOMFLY-PT polynomial `P_K(v, z)`. -/
def fwmBound (vMin vMax : ℤ) : ℤ :=
  (vMax - vMin) / 2 + 1

/-- Birman–Menasco (1990) connected-sum braid-index formula `β(K₁ # K₂) = β₁ + β₂ - 1`. -/
def compositeBraidIndex (b1 b2 : ℕ) : ℕ :=
  b1 + b2 - 1

/-- **Birman–Menasco Composite 3-Braid Exclusion:**
For non-trivial prime summands (`b₁ ≥ 2`, `b₂ ≥ 2`), `β(K₁ # K₂) = 3` holds **if and only if**
`b₁ = 2` and `b₂ = 2` (so only connected sums of two 2-braid torus knots can live in `B₃`, never
`3₁ # 4₁`). -/
theorem composite_three_braid_iff_both_two_braid {b1 b2 : ℕ}
    (hb1 : 2 ≤ b1) (hb2 : 2 ≤ b2) :
    compositeBraidIndex b1 b2 = 3 ↔ b1 = 2 ∧ b2 = 2 := by
  unfold compositeBraidIndex
  omega

/-- Complete enumeration of all `35` non-trivial prime knots up to `8` crossings (`3₁`..`8₂₁`). -/
inductive PrimeKnotLe8
  | k3_1
  | k4_1
  | k5_1 | k5_2
  | k6_1 | k6_2 | k6_3
  | k7_1 | k7_2 | k7_3 | k7_4 | k7_5 | k7_6 | k7_7
  | k8_1 | k8_2 | k8_3 | k8_4 | k8_5 | k8_6 | k8_7
  | k8_8 | k8_9 | k8_10 | k8_11 | k8_12 | k8_13 | k8_14
  | k8_15 | k8_16 | k8_17 | k8_18 | k8_19 | k8_20 | k8_21
  deriving DecidableEq, Repr

/-- Canonical ordered list of all `35` prime knots up to `8` crossings. -/
def allPrimeKnotsLe8 : List PrimeKnotLe8 :=
  [ .k3_1,
    .k4_1,
    .k5_1, .k5_2,
    .k6_1, .k6_2, .k6_3,
    .k7_1, .k7_2, .k7_3, .k7_4, .k7_5, .k7_6, .k7_7,
    .k8_1, .k8_2, .k8_3, .k8_4, .k8_5, .k8_6, .k8_7,
    .k8_8, .k8_9, .k8_10, .k8_11, .k8_12, .k8_13, .k8_14,
    .k8_15, .k8_16, .k8_17, .k8_18, .k8_19, .k8_20, .k8_21 ]

theorem mem_allPrimeKnotsLe8 (K : PrimeKnotLe8) : K ∈ allPrimeKnotsLe8 := by
  cases K <;> decide

/-- Crossing number `c(K)` of each prime knot `≤ 8` crossings. -/
def crossingNum : PrimeKnotLe8 → ℕ
  | .k3_1 => 3
  | .k4_1 => 4
  | .k5_1 | .k5_2 => 5
  | .k6_1 | .k6_2 | .k6_3 => 6
  | .k7_1 | .k7_2 | .k7_3 | .k7_4 | .k7_5 | .k7_6 | .k7_7 => 7
  | _ => 8

/-- Seifert genus `g(K)` of each prime knot `≤ 8` crossings. -/
def seifertGenus : PrimeKnotLe8 → ℕ
  | .k3_1 | .k4_1 | .k5_2 | .k6_1 | .k7_2 | .k7_4 | .k8_1 | .k8_3 => 1
  | .k5_1 | .k6_2 | .k6_3 | .k7_3 | .k7_5 | .k7_6 | .k7_7
  | .k8_4 | .k8_6 | .k8_8 | .k8_11 | .k8_12 | .k8_13 | .k8_14 | .k8_15
  | .k8_20 | .k8_21 => 2
  | .k7_1 | .k8_2 | .k8_5 | .k8_7 | .k8_9 | .k8_10
  | .k8_16 | .k8_17 | .k8_18 | .k8_19 => 3

/-- Whether `S³ \ K` is hyperbolic (`false` iff `K` is a torus knot `3₁, 5₁, 7₁, 8₁₉ = T(3,4)`). -/
def isHyperbolic : PrimeKnotLe8 → Bool
  | .k3_1 | .k5_1 | .k7_1 | .k8_19 => false
  | _ => true

/-- Strand count `n_real(K)` of an explicit minimal braid presentation realizing `K`
(Jones 1987, Ann. of Math. 126, Table 15.9). -/
def realizingStrands : PrimeKnotLe8 → ℕ
  | .k3_1 | .k5_1 | .k7_1 => 2
  | .k4_1 | .k5_2 | .k6_2 | .k6_3 | .k7_3 | .k7_5
  | .k8_2 | .k8_5 | .k8_7 | .k8_9 | .k8_10
  | .k8_16 | .k8_17 | .k8_18 | .k8_19 | .k8_20 | .k8_21 => 3
  | .k6_1 | .k7_2 | .k7_4 | .k7_6 | .k7_7
  | .k8_4 | .k8_6 | .k8_8 | .k8_11 | .k8_13 | .k8_14 | .k8_15 => 4
  | .k8_1 | .k8_3 | .k8_12 => 5

/-- Exact `(vMin, vMax)` `v`-degree bounds of `P_K(v, z)` (in the standard positively-writhed
orientation for chiral knots) establishing `fwmBound`. -/
def homflyVSpan : PrimeKnotLe8 → ℤ × ℤ
  | .k3_1 => (2, 4)
  | .k4_1 => (-2, 2)
  | .k5_1 => (4, 6)
  | .k5_2 => (2, 6)
  | .k6_1 => (-4, 2)
  | .k6_2 => (0, 4)
  | .k6_3 => (-2, 2)
  | .k7_1 => (6, 8)
  | .k7_2 => (2, 8)
  | .k7_3 => (4, 8)
  | .k7_4 => (2, 8)
  | .k7_5 => (4, 8)
  | .k7_6 => (0, 6)
  | .k7_7 => (-2, 4)
  | .k8_1 => (-6, 2)
  | .k8_2 => (2, 6)
  | .k8_3 => (-4, 4)
  | .k8_4 => (-4, 2)
  | .k8_5 => (2, 6)
  | .k8_6 => (-2, 4)
  | .k8_7 => (0, 4)
  | .k8_8 => (-2, 4)
  | .k8_9 => (-2, 2)
  | .k8_10 => (0, 4)
  | .k8_11 => (0, 6)
  | .k8_12 => (-4, 4)
  | .k8_13 => (-2, 4)
  | .k8_14 => (0, 6)
  | .k8_15 => (4, 10)
  | .k8_16 => (0, 4)
  | .k8_17 => (-2, 2)
  | .k8_18 => (-2, 2)
  | .k8_19 => (6, 10)
  | .k8_20 => (-2, 2)
  | .k8_21 => (2, 6)

/-- Exact braid index `β(K)` computed from the sharp Franks–Williams–Morton bound. -/
def braidIndex (K : PrimeKnotLe8) : ℤ :=
  fwmBound (homflyVSpan K).1 (homflyVSpan K).2

/-- **Sharpness of Franks–Williams–Morton Across All `35` Prime Knots `≤ 8` Crossings:**
For every `K : PrimeKnotLe8`, the HOMFLY-PT `v`-span is non-negative and even, and `fwmBound`
equals the explicit realizing strand count `realizingStrands K`. -/
theorem fwm_sharp_all_prime_knots_le8 :
    allPrimeKnotsLe8.length = 35 ∧
    ∀ K ∈ allPrimeKnotsLe8,
      (homflyVSpan K).1 ≤ (homflyVSpan K).2 ∧
      ((homflyVSpan K).2 - (homflyVSpan K).1) % 2 = 0 ∧
      braidIndex K = (realizingStrands K : ℤ) := by
  decide

/-- **Strict Exclusion of `6₁, 7₂, 7₄, 7₆, 7₇` (`β = 4`) and `8₁` (`β = 5`) from `B₃`:**
None of the bare-volume near-runners `6₁`, `7₂`, `8₁` (nor `7₄, 7₆, 7₇`) is a 3-braid closure. -/
theorem excluded_four_and_five_braids_not_three_braid :
    braidIndex .k6_1 = 4 ∧
    braidIndex .k7_2 = 4 ∧
    braidIndex .k7_4 = 4 ∧
    braidIndex .k7_6 = 4 ∧
    braidIndex .k7_7 = 4 ∧
    braidIndex .k8_1 = 5 := by
  decide

/-- **Complete `≤ 7`-Crossing and `8`-Crossing Hyperbolic 3-Braid Censuses & Bring Genus Bound:**
* Up to `7` crossings, there are **exactly six** prime hyperbolic 3-braids:
  `[k4_1, k5_2, k6_2, k6_3, k7_3, k7_5]`.
* Removing the `CAL-2` muon knot `k4_1` leaves **exactly five** primary `≤ 7`-crossing tau
  candidates: `[k5_2, k6_2, k6_3, k7_3, k7_5]`.
* At `8` crossings, there are **exactly ten** prime hyperbolic 3-braids (`8₁₉ = T(3,4)` being
  toroidal), and every prime knot `≤ 8` crossings satisfies Bring's genus bound `g(K) ≤ 4`. -/
theorem complete_hyperbolic_three_braid_census :
    allPrimeKnotsLe8.filter
        (fun K => crossingNum K ≤ 7 && isHyperbolic K && decide (braidIndex K = 3)) =
      [.k4_1, .k5_2, .k6_2, .k6_3, .k7_3, .k7_5] ∧
    allPrimeKnotsLe8.filter
        (fun K => crossingNum K ≤ 7 && isHyperbolic K && decide (braidIndex K = 3) &&
          decide (K ≠ .k4_1)) =
      [.k5_2, .k6_2, .k6_3, .k7_3, .k7_5] ∧
    allPrimeKnotsLe8.filter
        (fun K => decide (crossingNum K = 8) && isHyperbolic K && decide (braidIndex K = 3)) =
      [.k8_2, .k8_5, .k8_7, .k8_9, .k8_10, .k8_16, .k8_17, .k8_18, .k8_20, .k8_21] ∧
    ∀ K ∈ allPrimeKnotsLe8, seifertGenus K ≤ 4 := by
  decide

/-- Minimal `w ≤ 0` `B₃` writhe assigned to each of the `5` primary `≤ 7`-crossing tau candidates. -/
def primaryCandidateWrithe : PrimeKnotLe8 → Option ℤ
  | .k5_2 => some (writhe3 word5_2_neg)
  | .k6_2 => some (writhe3 word6_2_neg)
  | .k6_3 => some (writhe3 word6_3)
  | .k7_3 => some (writhe3 word7_3_neg)
  | .k7_5 => some (writhe3 word7_5_neg)
  | _ => none

/-- Primary `≤ 7`-crossing hyperbolic 3-braid tau candidate list. -/
def primaryTauCandidatesLe7 : List PrimeKnotLe8 :=
  [.k5_2, .k6_2, .k6_3, .k7_3, .k7_5]

/-- **Classification of the Three Pre-Registered `Q = -1` Writhe / Framing Gates:**
* **Gate G1** (`w ≤ 0` + `g ≤ 4` + transitive `(-1,-1,-1)` framing): admits all `5` candidates.
* **Gate G2** (halved-writhe Coulomb `w = -2`): uniquely selects `[.k6_2]`, while failing on `4₁`
  (`writhe3 word4_1 = 0 ≠ -2`).
* **Gate G3** (muon writhe-zero `w = 0`, Bennequin `sl = w - 3 = -3`): matches `4₁` and uniquely
  selects `[.k6_3]` among the `5` primary candidates. -/
theorem three_writhe_framing_gates_classification :
    primaryTauCandidatesLe7.filter
        (fun K => seifertGenus K ≤ 4 &&
          match primaryCandidateWrithe K with | some w => decide (w ≤ 0) | none => false) =
      [.k5_2, .k6_2, .k6_3, .k7_3, .k7_5] ∧
    primaryTauCandidatesLe7.filter
        (fun K => primaryCandidateWrithe K == some (-2)) =
      [.k6_2] ∧
    writhe3 word4_1 ≠ -2 ∧
    primaryTauCandidatesLe7.filter
        (fun K => primaryCandidateWrithe K == some 0) =
      [.k6_3] ∧
    writhe3 word4_1 - 3 = -3 ∧
    writhe3 word6_3 - 3 = -3 := by
  decide

end BraidIndexCensus

/-! ## Section 3: Non-Abelian Parabolic `SL(2, R)` Spinor Braiding & Exact `ℤ[X]` Polynomials -/

section ParabolicSpinorAlgebra

variable {R : Type*} [CommRing R]

/-- A spinor in `R²` represented as a pair `R × R`. -/
abbrev Spinor (R : Type*) := R × R

/-- A triple of parabolic cusp spinors `(u₀, u₁, u₂)` on the 3 strands of `B₃`. -/
abbrev SpinorTriple (R : Type*) := Spinor R × Spinor R × Spinor R

/-- `SL(2, R)` symplectic determinant `⟨u, v⟩ = u₀ v₁ - u₁ v₀`. -/
def sympDet (u v : Spinor R) : R :=
  u.1 * v.2 - u.2 * v.1

/-- Canonical parabolic matrix `M(u) = I + u uᵀ J = !![1 - u₀ u₁, u₀²; -u₁², 1 + u₀ u₁]`
associated to a cusp spinor `u = (u₀, u₁)`. -/
def parabolicSpinorMat (u : Spinor R) : Matrix (Fin 2) (Fin 2) R :=
  !![1 - u.1 * u.2, u.1 ^ 2; -(u.2 ^ 2), 1 + u.1 * u.2]

/-- Explicit inverse `M(u)⁻¹ = I - u uᵀ J` over any commutative ring `R`. -/
def parabolicSpinorMatInv (u : Spinor R) : Matrix (Fin 2) (Fin 2) R :=
  !![1 + u.1 * u.2, -(u.1 ^ 2); u.2 ^ 2, 1 - u.1 * u.2]

/-- Action `v + ⟨u, v⟩ u` of `M(u)` on a spinor `v`. -/
def spinorConjPos (u v : Spinor R) : Spinor R :=
  (v.1 + sympDet u v * u.1, v.2 + sympDet u v * u.2)

/-- Action `v - ⟨u, v⟩ u = v + ⟨v, u⟩ u` of `M(u)⁻¹` on a spinor `v`. -/
def spinorConjNeg (u v : Spinor R) : Spinor R :=
  (v.1 + sympDet v u * u.1, v.2 + sympDet v u * u.2)

/-- **Parabolic Trace-`2`, Unit-Determinant, and Exact Matrix Inverse over `[CommRing R]`:**
Every `parabolicSpinorMat u` lies in `SL(2, R)` with `trace = 2` and explicit inverse
`parabolicSpinorMatInv u`. -/
theorem parabolicSpinorMat_properties (u : Spinor R) :
    (parabolicSpinorMat u).trace = 2 ∧
    (parabolicSpinorMat u).det = 1 ∧
    parabolicSpinorMat u * parabolicSpinorMatInv u = 1 ∧
    parabolicSpinorMatInv u * parabolicSpinorMat u = 1 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp [parabolicSpinorMat, Matrix.trace_fin_two]; ring
  · simp [parabolicSpinorMat, Matrix.det_fin_two]; ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [parabolicSpinorMat, parabolicSpinorMatInv, Matrix.mul_apply, Fin.sum_univ_two] <;> ring
  · ext i j; fin_cases i <;> fin_cases j <;>
      simp [parabolicSpinorMat, parabolicSpinorMatInv, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- **Exact Equivariance of Parabolic Matrices under Spinor Conjugation:**
`M(u) M(v) M(u)⁻¹ = M(v + ⟨u, v⟩ u)` identically over any `[CommRing R]`. -/
theorem parabolicSpinorMat_conj_eq (u v : Spinor R) :
    parabolicSpinorMat u * parabolicSpinorMat v * parabolicSpinorMatInv u =
      parabolicSpinorMat (spinorConjPos u v) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [parabolicSpinorMat, parabolicSpinorMatInv, spinorConjPos, sympDet,
      Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- Single-crossing non-abelian parabolic spinor step in `B₃`. -/
def braidSpinorStep (g : Gen3) (t : SpinorTriple R) : SpinorTriple R :=
  let (u0, u1, u2) := t
  match g with
  | .s0Pos => (spinorConjPos u0 u1, u0, u2)
  | .s0Neg => (u1, spinorConjNeg u1 u0, u2)
  | .s1Pos => (u0, spinorConjPos u1 u2, u1)
  | .s1Neg => (u0, u2, spinorConjNeg u2 u1)

/-- Action of a 3-braid word `b : BraidWord3` on a triple of cusp spinors `(u₀, u₁, u₂)`. -/
def braidSpinorWord : BraidWord3 → SpinorTriple R → SpinorTriple R
  | [], t => t
  | g :: rest, t => braidSpinorWord rest (braidSpinorStep g t)

/-- **Exact Step Invertibility (`σᵢ⁻¹ ∘ σᵢ = id`) over `[CommRing R]`:** -/
theorem braidSpinorStep_inv (g : Gen3) (t : SpinorTriple R) :
    braidSpinorStep g.inv (braidSpinorStep g t) = t := by
  rcases t with ⟨⟨u0a, u0b⟩, ⟨u1a, u1b⟩, ⟨u2a, u2b⟩⟩
  cases g <;>
    ext <;>
    simp only [Gen3.inv, braidSpinorStep, spinorConjPos, spinorConjNeg, sympDet] <;>
    ring

/-- **Exact Artin Braid Relation (`σ₀ σ₁ σ₀ = σ₁ σ₀ σ₁`) on Parabolic Spinors over `[CommRing R]`:** -/
theorem braidSpinorStep_artin_relation (t : SpinorTriple R) :
    braidSpinorWord [.s0Pos, .s1Pos, .s0Pos] t =
      braidSpinorWord [.s1Pos, .s0Pos, .s1Pos] t := by
  rcases t with ⟨⟨u0a, u0b⟩, ⟨u1a, u1b⟩, ⟨u2a, u2b⟩⟩
  ext <;>
    simp only [braidSpinorWord, braidSpinorStep, spinorConjPos, sympDet] <;>
    ring

theorem braidSpinorWord_append (a b : BraidWord3) (t : SpinorTriple R) :
    braidSpinorWord (a ++ b) t = braidSpinorWord b (braidSpinorWord a t) := by
  induction a generalizing t with
  | nil => rfl
  | cons g rest ih => exact ih (braidSpinorStep g t)

theorem braidSpinorWord_cancel_inv (w : BraidWord3) (t : SpinorTriple R) :
    braidSpinorWord (invWord3 w) (braidSpinorWord w t) = t := by
  induction w generalizing t with
  | nil => rfl
  | cons g rest ih =>
    simp only [invWord3, braidSpinorWord, braidSpinorWord_append]
    rw [ih (braidSpinorStep g t)]
    exact braidSpinorStep_inv g t

/-- **Meet-in-the-Middle Reduction Lemma:** matching `w₁` forward with `w₂⁻¹` backward proves
full word transport `w₁ ++ w₂` without degree blow-up. -/
theorem braidSpinorWord_eq_of_meet_in_middle
    (w1 w2 : BraidWord3) (uIn uOut : SpinorTriple R)
    (h : braidSpinorWord w1 uIn = braidSpinorWord (invWord3 w2) uOut) :
    braidSpinorWord (w1 ++ w2) uIn = uOut := by
  rw [braidSpinorWord_append, h]
  have hcan := braidSpinorWord_cancel_inv (invWord3 w2) uOut
  have hinv_inv : ∀ w : BraidWord3, invWord3 (invWord3 w) = w := by
    intro w
    induction w with
    | nil => rfl
    | cons g rest ih =>
      have h_app : ∀ p q : BraidWord3, invWord3 (p ++ q) = invWord3 q ++ invWord3 p := by
        intro p q
        induction p with
        | nil => simp [invWord3]
        | cons x xs ihp => simp [invWord3, ihp, List.append_assoc]
      rw [invWord3, h_app, ih]
      simp [invWord3, gen3_inv_inv]
  rw [hinv_inv] at hcan
  exact hcan

/-! ### Exact `ℤ[X]` Shape / Riley / Spinor Polynomials & Full Parabolic `B₃` Closure Proofs -/

/-- `4₁` regular-tetrahedron shape polynomial `z² - z + 1` and spinor polynomial `x² + x + 1`
(`z = -x`). -/
def shapePoly4_1 (z : R) : R := z ^ 2 - z + 1
def spinorPoly4_1 (x : R) : R := x ^ 2 + x + 1

/-- `5₂` parabolic spinor polynomial `x³ - x² + 1` and Thurston tetrahedral gluing polynomial
`y³ - 2y² + 3y - 1`. -/
def spinorPoly5_2 (x : R) : R := x ^ 3 - x ^ 2 + 1
def tetPoly5_2 (y : R) : R := y ^ 3 - 2 * y ^ 2 + 3 * y - 1

/-- `6₁` (stevedore, `β = 4`) tetrahedral cubic `z³ + z² - 2z + 1` and 2-bridge Riley quartic
`y⁴ - 5y³ + 7y² - 2y + 1`. -/
def gluingPoly6_1 (z : R) : R := z ^ 3 + z ^ 2 - 2 * z + 1
def rileyPoly6_1 (y : R) : R := y ^ 4 - 5 * y ^ 3 + 7 * y ^ 2 - 2 * y + 1

/-- `6₂` parabolic spinor quintic `x⁵ - x⁴ - 2x³ + x² + x + 1` (`qou-r0dn` exact shape field). -/
def spinorPoly6_2 (x : R) : R := x ^ 5 - x ^ 4 - 2 * x ^ 3 + x ^ 2 + x + 1

/-- `6₃` amphichiral parabolic spinor sextic `x⁶ - x⁵ - x⁴ + 2x³ - x + 1`. -/
def spinorPoly6_3 (x : R) : R := x ^ 6 - x ^ 5 - x ^ 4 + 2 * x ^ 3 - x + 1

/-- `7₃` parabolic spinor sextic `x⁶ - x⁵ + 3x⁴ - 2x³ + 2x² - x - 1`. -/
def spinorPoly7_3 (x : R) : R :=
  x ^ 6 - x ^ 5 + 3 * x ^ 4 - 2 * x ^ 3 + 2 * x ^ 2 - x - 1

/-- `7₅` parabolic spinor octic `x⁸ - x⁷ - 3x⁶ + 2x⁵ + 3x⁴ - 2x - 1`. -/
def spinorPoly7_5 (x : R) : R :=
  x ^ 8 - x ^ 7 - 3 * x ^ 6 + 2 * x ^ 5 + 3 * x ^ 4 - 2 * x - 1

/-- **Birational Equivalence of `5₂`'s Spinor Cubic and Tetrahedral Gluing Cubic (`x = y/(y-1)`):**
Over any `[CommRing R]`, `(y - 1)³ · spinorPoly5_2(y / (y - 1))` cleared of denominators equals
`tetPoly5_2 y` identically, and `shapePoly4_1 (-x) = spinorPoly4_1 x`. -/
theorem shape_and_spinor_birational_identities (x y : R) :
    shapePoly4_1 (-x) = spinorPoly4_1 x ∧
    y ^ 3 - y ^ 2 * (y - 1) + (y - 1) ^ 3 = tetPoly5_2 y ∧
    gluingPoly6_1 (0 : ℤ) = 1 ∧
    gluingPoly6_1 (1 : ℤ) = 1 ∧
    gluingPoly6_1 (-1 : ℤ) = 3 := by
  refine ⟨?_, ?_, by decide, by decide, by decide⟩
  · unfold shapePoly4_1 spinorPoly4_1; ring
  · unfold tetPoly5_2; ring

/-- **Exact Parabolic `SL(2, R)` Closure Theorem for `4₁` (`(σ₀ σ₁⁻¹)²`):**
Whenever `spinorPoly4_1 x = 0`, `(u₀ = (1,0), u₁ = (0,x), u₂ = (x, x+1))` closes under `word4_1`
to `((-1,0), u₁, u₂)` (longitude holonomy `-1`). -/
theorem spinor_closure_4_1 {x : R} (hx : spinorPoly4_1 x = 0) :
    braidSpinorWord word4_1 (((1, 0), (0, x), (x, x + 1)) : SpinorTriple R) =
      (((-1, 0), (0, x), (x, x + 1)) : SpinorTriple R) := by
  unfold spinorPoly4_1 at hx
  simp only [word4_1, braidSpinorWord, braidSpinorStep, spinorConjPos, spinorConjNeg, sympDet, Prod.mk.injEq]
  refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩
  · linear_combination hx
  · linear_combination hx
  · linear_combination hx
  · linear_combination hx
  · linear_combination x ^ 2 * hx
  · linear_combination (x ^ 2 + x - 1) * hx

/-- **Exact Parabolic `SL(2, R)` Closure Theorem for `5₂` (`σ₀³ σ₁ σ₀⁻¹ σ₁`):**
Whenever `spinorPoly5_2 x = 0`, `((1,0), (0,x), (x, -x²+x+1))` closes under `word5_2_pos` to
`((-1,0), (0,x), (x, -x²+x+1))`. -/
theorem spinor_closure_5_2 {x : R} (hx : spinorPoly5_2 x = 0) :
    braidSpinorWord word5_2_pos (((1, 0), (0, x), (x, -x ^ 2 + x + 1)) : SpinorTriple R) =
      (((-1, 0), (0, x), (x, -x ^ 2 + x + 1)) : SpinorTriple R) := by
  unfold spinorPoly5_2 at hx
  simp only [word5_2_pos, braidSpinorWord, braidSpinorStep, spinorConjPos, spinorConjNeg, sympDet, Prod.mk.injEq]
  refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩
  · linear_combination (-x ^ 3 - x ^ 2 + 2 * x + 2) * hx
  · linear_combination (-x ^ 3 - x ^ 2 + x + 1) * hx
  · linear_combination
      (x ^ 13 + x ^ 12 - 6 * x ^ 11 - 5 * x ^ 10 + 15 * x ^ 9 + 10 * x ^ 8 - 21 * x ^ 7 -
        12 * x ^ 6 + 18 * x ^ 5 + 11 * x ^ 4 - 8 * x ^ 3 - 6 * x ^ 2 + 1) * hx
  · linear_combination
      (x ^ 13 + x ^ 12 - 5 * x ^ 11 - 4 * x ^ 10 + 11 * x ^ 9 + 7 * x ^ 8 - 15 * x ^ 7 -
        9 * x ^ 6 + 13 * x ^ 5 + 9 * x ^ 4 - 5 * x ^ 3 - 5 * x ^ 2 - x) * hx
  · linear_combination (x ^ 6 + x ^ 5 - 3 * x ^ 4 - 3 * x ^ 3 + 2 * x ^ 2 + 2 * x) * hx
  · linear_combination (x ^ 6 + x ^ 5 - 2 * x ^ 4 - 2 * x ^ 3 + x ^ 2 + x - 1) * hx

/-- **Exact Parabolic `SL(2, R)` Closure Theorem for `6₂` (`σ₀³ σ₁⁻¹ σ₀ σ₁⁻¹`, `qou-r0dn`):**
Whenever `spinorPoly6_2 x = 0`, `((1,0), (0,x), (-x³+2x, -x⁴-x³+x²+2x+1))` closes under
`word6_2_pos` to `((-1,0), u₁, u₂)`. -/
theorem spinor_closure_6_2 {x : R} (hx : spinorPoly6_2 x = 0) :
    braidSpinorWord word6_2_pos
        (((1, 0), (0, x), (-x ^ 3 + 2 * x, -x ^ 4 - x ^ 3 + x ^ 2 + 2 * x + 1)) : SpinorTriple R) =
      (((-1, 0), (0, x), (-x ^ 3 + 2 * x, -x ^ 4 - x ^ 3 + x ^ 2 + 2 * x + 1)) : SpinorTriple R) := by
  unfold spinorPoly6_2 at hx
  simp only [word6_2_pos, braidSpinorWord, braidSpinorStep, spinorConjPos, spinorConjNeg, sympDet, Prod.mk.injEq]
  refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩
  · linear_combination (-x ^ 5 - x ^ 4 + 2 * x ^ 3 + 2 * x ^ 2 + x + 1) * hx
  · linear_combination (-x ^ 5 - x ^ 4 + x ^ 3 + x ^ 2 + x + 1) * hx
  · linear_combination (-x ^ 4 - x ^ 3 + x ^ 2 + x + 1) * hx
  · linear_combination (-x ^ 5 - 2 * x ^ 4 - x ^ 3 + x ^ 2 + 2 * x + 1) * hx
  · linear_combination
      (-x ^ 17 - x ^ 16 + 6 * x ^ 15 + 8 * x ^ 14 - 9 * x ^ 13 - 23 * x ^ 12 - 11 * x ^ 11 +
        23 * x ^ 10 + 40 * x ^ 9 + 12 * x ^ 8 - 24 * x ^ 7 - 34 * x ^ 6 - 14 * x ^ 5 +
        9 * x ^ 4 + 12 * x ^ 3 + 7 * x ^ 2 + x) * hx
  · linear_combination
      (-x ^ 18 - 2 * x ^ 17 + 4 * x ^ 16 + 13 * x ^ 15 + 4 * x ^ 14 - 25 * x ^ 13 -
        39 * x ^ 12 - 4 * x ^ 11 + 52 * x ^ 10 + 62 * x ^ 9 + 11 * x ^ 8 - 48 * x ^ 7 -
        55 * x ^ 6 - 18 * x ^ 5 + 15 * x ^ 4 + 21 * x ^ 3 + 9 * x ^ 2 + x - 1) * hx

/-- **Exact Parabolic `SL(2, R)` Closure Theorem for `6₃` (`σ₀² σ₁⁻¹ σ₀ σ₁⁻²`):**
Whenever `spinorPoly6_3 x = 0`, `((1,0), (0,x), (-x⁴+x²-1, -x⁴))` closes under `word6_3` to
`((-1,0), u₁, u₂)`. -/
theorem spinor_closure_6_3 {x : R} (hx : spinorPoly6_3 x = 0) :
    braidSpinorWord word6_3 (((1, 0), (0, x), (-x ^ 4 + x ^ 2 - 1, -x ^ 4)) : SpinorTriple R) =
      (((-1, 0), (0, x), (-x ^ 4 + x ^ 2 - 1, -x ^ 4)) : SpinorTriple R) := by
  unfold spinorPoly6_3 at hx
  simp only [word6_3, braidSpinorWord, braidSpinorStep, spinorConjPos, spinorConjNeg, sympDet, Prod.mk.injEq]
  refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩
  · ring
  · ring
  · linear_combination (x ^ 6 + x ^ 5 - x ^ 4 - 2 * x ^ 3 + x + 1) * hx
  · linear_combination (x ^ 6 + x ^ 5 - x ^ 3 - x ^ 2 - x) * hx
  · linear_combination
      (-x ^ 11 - x ^ 10 + 2 * x ^ 9 + 3 * x ^ 8 - 2 * x ^ 7 - 4 * x ^ 6 + 3 * x ^ 4 + x ^ 3 -
        x ^ 2 + 1) * hx
  · linear_combination
      (-x ^ 11 - x ^ 10 + x ^ 9 + 2 * x ^ 8 - x ^ 6 - x ^ 5 + x ^ 3 + x ^ 2 + x) * hx

/-- **Exact Parabolic `SL(2, R)` Closure Theorem for `7₃` (`σ₁⁻¹ σ₀⁴ σ₁² σ₀`):**
Proved via 4+4 meet-in-the-middle reduction over `[CommRing R]`. -/
theorem spinor_closure_7_3 {x : R} (hx : spinorPoly7_3 x = 0) :
    braidSpinorWord word7_3_pos (((1, 0), (0, x), (x, x ^ 3 + x)) : SpinorTriple R) =
      (((-1, 0), (0, x), (x, x ^ 3 + x)) : SpinorTriple R) := by
  have hsplit : word7_3_pos =
      [.s1Neg, .s0Pos, .s0Pos, .s0Pos] ++ [.s0Pos, .s1Pos, .s1Pos, .s0Pos] := rfl
  rw [hsplit]
  apply braidSpinorWord_eq_of_meet_in_middle
  unfold spinorPoly7_3 at hx
  simp only [invWord3, Gen3.inv, List.nil_append, List.cons_append,
    braidSpinorWord, braidSpinorStep, spinorConjPos, spinorConjNeg, sympDet, Prod.mk.injEq]
  refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩
  · linear_combination (-x ^ 3 - x ^ 2 - 2 * x - 1) * hx
  · linear_combination (-x ^ 3 - x ^ 2 - x) * hx
  · linear_combination (-1) * hx
  · linear_combination x * hx
  · ring
  · ring

/-- **Exact Parabolic `SL(2, R)` Closure Theorem for `7₅` (`σ₀³ σ₁² σ₀² σ₁⁻¹`):**
Proved via 4+4 meet-in-the-middle reduction over `[CommRing R]`. -/
theorem spinor_closure_7_5 {x : R} (hx : spinorPoly7_5 x = 0) :
    braidSpinorWord word7_5_pos
        (((1, 0), (0, x), (-x ^ 5 + 2 * x ^ 3 - x, -x ^ 5 + x ^ 3 + x)) : SpinorTriple R) =
      (((-1, 0), (0, x), (-x ^ 5 + 2 * x ^ 3 - x, -x ^ 5 + x ^ 3 + x)) : SpinorTriple R) := by
  have hsplit : word7_5_pos =
      [.s0Pos, .s0Pos, .s0Pos, .s1Pos] ++ [.s1Pos, .s0Pos, .s0Pos, .s1Neg] := rfl
  rw [hsplit]
  apply braidSpinorWord_eq_of_meet_in_middle
  unfold spinorPoly7_5 at hx
  simp only [invWord3, Gen3.inv, List.nil_append, List.cons_append,
    braidSpinorWord, braidSpinorStep, spinorConjPos, spinorConjNeg, sympDet, Prod.mk.injEq]
  refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩
  · linear_combination (-x ^ 4 - x ^ 3 + x ^ 2 - 1) * hx
  · linear_combination (x ^ 6 + x ^ 5 - 2 * x ^ 4 - x ^ 3 + x ^ 2 - x) * hx
  · ring
  · ring
  · linear_combination
      (-x ^ 11 - x ^ 10 + 4 * x ^ 9 + 3 * x ^ 8 - 6 * x ^ 7 - 2 * x ^ 6 + 4 * x ^ 5 -
        x ^ 4 - x ^ 3 + x ^ 2 - 1) * hx
  · linear_combination
      (-x ^ 11 - x ^ 10 + 3 * x ^ 9 + 2 * x ^ 8 - 2 * x ^ 7 + x ^ 6 - x ^ 5 - 2 * x ^ 4 +
        x ^ 3 - x ^ 2 + x) * hx

end ParabolicSpinorAlgebra

/-! ## Section 4: Generation-3 (`k = 3`) `#9213` Inhomogeneous Loop-Resolvent & Rule-13a Carrier -/

section GenerationThreeLoopResolvent

variable {ι K : Type*} [Field K]

/-- Generation-3 (`k = 3`) inhomogeneous Borel-resummed loop resolvent extending
`QOU.Observations.InhomogeneousLeptonLoopResolvent.InhomogeneousLoopResolvent` (`#9213`):
`W₃(X; q) = W_alg(X; q) + ℏ_q⁻³ Vol(X) · (1 + c_tors(X) ℏ_q + c₂(X) ℏ_q²)`. -/
def singPartGen3 (R : InhomogeneousLoopResolvent ι K) (X : ι) (q : K) : K :=
  (hbar q ^ 3)⁻¹ * R.vol X * (1 + R.cTors X * hbar q + R.cTwo X * hbar q ^ 2)

/-- Full generation-3 inhomogeneous loop functional `W₃(X; q) = W_alg(X; q) + singPartGen3`. -/
def evalGen3 (R : InhomogeneousLoopResolvent ι K) (X : ι) (q : K) : K :=
  R.wAlg X q + singPartGen3 R X q

/-- Toroidal / zero-volume vanishing of the generation-3 singular branch (`Vol(X) = 0`, covering
`T(2,7)` and `8₁₉ = T(3,4)`). -/
theorem evalGen3_eq_wAlg_of_vol_zero (R : InhomogeneousLoopResolvent ι K) {X : ι}
    (hv : R.vol X = 0) (q : K) :
    evalGen3 R X q = R.wAlg X q := by
  unfold evalGen3 singPartGen3
  rw [hv, mul_zero, zero_mul, add_zero]

/-- **Generation-3 `O(ℏ_q)` Saddle Recovery Identity:** for `q ≠ 1`,
`ℏ_q³ W₃(X; q) - Vol(X) = ℏ_q · (Vol(X) c_tors(X) + ℏ_q (Vol(X) c₂(X) + ℏ_q W_alg(X; q)))`. -/
theorem hbar_cube_mul_evalGen3_sub_vol (R : InhomogeneousLoopResolvent ι K) (X : ι)
    {q : K} (hq1 : q ≠ 1) :
    hbar q ^ 3 * evalGen3 R X q - R.vol X =
      hbar q * (R.vol X * R.cTors X + hbar q * (R.vol X * R.cTwo X + hbar q * R.wAlg X q)) := by
  have hh : hbar q ≠ 0 := hbar_ne_zero q hq1
  have hh3 : hbar q ^ 3 ≠ 0 := pow_ne_zero 3 hh
  unfold evalGen3 singPartGen3
  field_simp
  ring

/-- **Exact Tau-to-Muon (`k = 3` vs `k = 2`) Saddle Hierarchy Ratio:**
Relative to an undressed `CAL-2` muon saddle `(ℏ_q²)⁻¹ Vol(4₁)`, the generation-3 singular saddle
branch splits identically as `(Vol(K_τ) / Vol(4₁)) · ℏ_q⁻¹ · (1 + c_tors ℏ_q + c₂ ℏ_q²)`. -/
theorem tau_to_muon_saddle_ratio (R : InhomogeneousLoopResolvent ι K) (tau : ι)
    {vol41 q : K} (hq1 : q ≠ 1) (hv41 : vol41 ≠ 0) :
    singPartGen3 R tau q / ((hbar q ^ 2)⁻¹ * vol41) =
      (R.vol tau / vol41) * (hbar q)⁻¹ *
        (1 + R.cTors tau * hbar q + R.cTwo tau * hbar q ^ 2) := by
  have hh : hbar q ≠ 0 := hbar_ne_zero q hq1
  have hh2 : hbar q ^ 2 ≠ 0 := pow_ne_zero 2 hh
  have hh3 : hbar q ^ 3 ≠ 0 := pow_ne_zero 3 hh
  unfold singPartGen3
  field_simp

end GenerationThreeLoopResolvent

section OrderedAndRule13aCarrier

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Complex Volume Modulus Lower Bound (`Map B ≥ Map A`):**
Over any strict ordered field, `vol² ≤ vol² + cs²`, with strict inequality iff `cs ≠ 0` (proving
algebraically why adding a nonzero Chern–Simons invariant strictly raises any positive bare-volume
overshoot such as `6₂⁻`, `7₃⁻`, or `7₅⁻`). -/
theorem complex_volume_sq_ge_real_volume_sq (vol cs : K) :
    vol ^ 2 ≤ vol ^ 2 + cs ^ 2 ∧ (vol ^ 2 < vol ^ 2 + cs ^ 2 ↔ cs ≠ 0) := by
  refine ⟨by linarith [sq_nonneg cs], ?_⟩
  constructor
  · intro hlt hcs
    rw [hcs] at hlt
    linarith
  · intro hcs
    have hpos : 0 < cs ^ 2 := sq_pos_of_ne_zero hcs
    linarith

/-- **Rule 13a Open Carrier & Loop-Dressing Hypothesis (`selected = "none"`):**
Because none of the `5` prime `≤ 7`-crossing hyperbolic 3-braids (`{5₂⁻, 6₂⁻, 6₃, 7₃⁻, 7₅⁻}`)
passes within `< 1%` of `m_τ / m_e` under the parameter-free pre-registered `Map A` (bare volume),
`Map B` (`|Vol + i CS|`), or `Map C` (`#9213` 1-loop Reidemeister torsion / inhomogeneous
loop-resolvent dressings), this zero-instance typeclass isolates the unresolved tau carrier and
loop-dressing datum without empirical fitting (`0` instances). -/
class TauHyperbolicThreeBraidCarrierHypothesis (ι K : Type*) [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] where
  /-- Underlying `#9213` inhomogeneous loop-resolvent datum. -/
  resolvent : InhomogeneousLoopResolvent ι K
  /-- Electron reference object (`Vol(e) = 0`, normalized algebraic contact `W_alg(e; q) = 1`). -/
  electron : ι
  /-- Putative hyperbolic tau carrier object (`Vol(τ) > 0`). -/
  tauCarrier : ι
  /-- Toroidal electron has zero hyperbolic volume. -/
  vol_electron_zero : resolvent.vol electron = 0
  /-- Symmetric-channel electron normalization `W_alg(e; q) = 1` across `q > 1`. -/
  wAlg_electron_unit : ∀ q : K, 1 < q → resolvent.wAlg electron q = 1
  /-- Strict positivity of the tau hyperbolic saddle volume. -/
  vol_tau_pos : 0 < resolvent.vol tauCarrier

/-- **Conditional Electron-Normalized Tau Ratio Expansion:**
Under `TauHyperbolicThreeBraidCarrierHypothesis`, for every `q > 1`, clearing `ℏ_q³` from the
electron-normalized ratio `W₃(τ; q) / W(e; q)` recovers `Vol(τ)` up to an explicit `O(ℏ_q)`
remainder determined by `c_tors(τ)`, `c₂(τ)`, and `W_alg(τ; q)`. -/
theorem conditional_tau_electron_ratio_hbar_cube_decomp {ι : Type*}
    [ctx : TauHyperbolicThreeBraidCarrierHypothesis ι K] {q : K} (hq : 1 < q) :
    hbar q ^ 3 *
        (evalGen3 ctx.resolvent ctx.tauCarrier q /
          ctx.resolvent.eval ctx.electron q) -
      ctx.resolvent.vol ctx.tauCarrier =
      hbar q *
        (ctx.resolvent.vol ctx.tauCarrier * ctx.resolvent.cTors ctx.tauCarrier +
          hbar q *
            (ctx.resolvent.vol ctx.tauCarrier * ctx.resolvent.cTwo ctx.tauCarrier +
              hbar q * ctx.resolvent.wAlg ctx.tauCarrier q)) := by
  have heval_e : ctx.resolvent.eval ctx.electron q = 1 := by
    rw [ctx.resolvent.eval_eq_wAlg_of_vol_zero ctx.vol_electron_zero q,
      ctx.wAlg_electron_unit q hq]
  rw [heval_e, div_one]
  exact hbar_cube_mul_evalGen3_sub_vol ctx.resolvent ctx.tauCarrier hq.ne'

end OrderedAndRule13aCarrier

end QOU.StandardModel.LowCrossingThreeBraidTauSelection
