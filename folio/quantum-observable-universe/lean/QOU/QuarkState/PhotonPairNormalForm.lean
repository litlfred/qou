/-
# The γγ normal form, its two gradings, and the quark-state hypothesis

Bean `qou-qs1d` (epic `qou-qs0e`). Formalize-first test of the agent working
hypothesis — NOT a finding, and NOT adopted —

  quark state := the degree ≥ 1 part of `NF(γ(φ)·γ(ψ))` in `H₃(q)`,
                 projected to the `(2,1)` Wedderburn channel,

with `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁` (`rem:knot-basis-color-content`).

The hypothesis needs three things to be non-vacuous. This file proves what
holds and records, as theorems, where it fails.

## Two gradings, which the hypothesis conflates

* **word degree** — length of the Gröbner–Shirshov normal-form word
  (`1` : 0; `σ₀, σ₁` : 1; `σ₁σ₀, σ₀σ₁` : 2; `σ₀σ₁σ₀` : 3);
* **order in the tower** — the power of `h = q − q⁻¹ = 2t + O(t²)`, `t = q − 1`.

`results.md:9-13` (`computations/probes/quark_template/`) is a statement about
the SECOND grading. The hypothesis is phrased in the FIRST. They agree on the
γγ product itself and disagree as soon as a flavour flip is applied:

* `pairNF_affine` : `NF(γγ)` is EXACTLY affine in `h`, `NF = NF|_{h=0} + h·N₁`;
* `N₁_deg0`, `N₁_bilin_*` : the `h`-coefficient `N₁` lives in word degree ≥ 1
  and is homogeneous bilinear in `(φ, ψ)` — so on `γγ` the order-1 part
  satisfies all three non-vacuity requirements;
* `pairNF_deg0_h_free` : the word-degree-0 coordinate `1 + φ₀ψ₀ + φ₁ψ₁` is
  `h`-free;
* **but** `flavour_reaches_deg0` : under the flavour flip of
  `results.md` (`σᵢ ↦ σᵢ⁻¹ = σᵢ − h`), the word-degree-0 coordinate moves at
  order `h¹` (by exactly `−h` on the witness `flavour_reaches_deg0_witness`).
  So requirement (1), "the degree-0 part carries no flavour", holds only
  modulo `h` (scope (a)); it is FALSE at order `t¹` in the word-degree reading.
* `degPos_not_bilinear` : requirement (3) FAILS as stated — the degree ≥ 1
  part contains the pass-through terms `φ₀ + ψ₀`, `φ₁ + ψ₁`, `φ₀₁ + ψ₀₁`, so it
  is affine-bilinear, not bilinear. The connected part
  `NF((γ(φ)−1)(γ(ψ)−1))` IS bilinear (`pairNF_eq_connected`).

## Re-derivation of `results.md:9-13` (the `(2,1)` channel)

With the reduced-Burau `(2,1)` representation `ρ` of the probe
(`rho_mul` : `ρ` is multiplicative on the NF algebra at `h = q − q⁻¹`):

* `template_order_zero` : at `q = 1` the `(2,1)` character of the nucleon word
  is `0` for EVERY choice of quark shifts — flavour is invisible at `t⁰`;
* `template_S0_zero` : the flavour-blind template's character is identically 0;
* `template_SplusAVG_proton` : the corpus template's character is
  `(q − 1)·g(q)` with `g(1) = −1` — flavour is decided at order `t¹`.

Base ring (§7c): the NF algebra is over generic `[CommRing R]`; the `(2,1)`
representation needs `q⁻¹` and is over `[Field R]` with `q ≠ 0`. No `ℝ`.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-/
import QOU.Machinery.MarkovTraceOnHecke
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

namespace QOU.QuarkState

open QOU.Machinery.H3

/-! ## The normal-form algebra over a generic commutative ring -/

section Generic

variable {R : Type*} [CommRing R]

/-- `σ₀` as an NF vector on the basis `[1, σ₀, σ₁, σ₁σ₀, σ₀σ₁, σ₀σ₁σ₀]`. -/
def s0 : Fin 6 → R := ![0, 1, 0, 0, 0, 0]
/-- `σ₁` as an NF vector. -/
def s1 : Fin 6 → R := ![0, 0, 1, 0, 0, 0]

/-- The basis labels are DERIVED, not asserted: `σ₀·σ₁` is coordinate 4.
(Trap: `MarkovTraceOnHecke` labels coordinate 3 `L₊` although it is `σ₁σ₀`,
while `rem:knot-basis-color-content` writes `L₊ = σ₀σ₁`, i.e. coordinate 4.) -/
theorem s0_mul_s1 (h : R) : mulNF h s0 s1 = ![0, 0, 0, 0, 1, 0] := by
  funext i; fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, s0, s1]

theorem s1_mul_s0 (h : R) : mulNF h s1 s0 = ![0, 0, 0, 1, 0, 0] := by
  funext i; fin_cases i <;> simp [mulNF, mulσ₀, mulσ₁, s0, s1]

/-- The photon with colour content: `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁`,
built with the algebra product (no basis label is trusted). -/
def photon (h a0 a1 a2 : R) : Fin 6 → R :=
  unitNF + a0 • s0 + a1 • s1 + a2 • mulNF h s0 s1

/-- The flavour-flipped photon: every letter `σᵢ` replaced by
`σᵢ⁻¹ = σᵢ − h` (the sign bit of `quark_template`). -/
def photonBar (h a0 a1 a2 : R) : Fin 6 → R :=
  unitNF + a0 • (s0 - h • unitNF) + a1 • (s1 - h • unitNF)
    + a2 • mulNF h (s0 - h • unitNF) (s1 - h • unitNF)

/-- `NF(γ(φ)·γ(ψ))`. -/
def pairNF (h a0 a1 a2 b0 b1 b2 : R) : Fin 6 → R :=
  mulNF h (photon h a0 a1 a2) (photon h b0 b1 b2)

/-- **The γγ normal form** — reproduces table 5 of
`trivial-knot-photon-interpretation` coordinate by coordinate (with
`L₋ = σ₁σ₀` at index 3 and `L₊ = σ₀σ₁` at index 4). -/
theorem pairNF_eq (h a0 a1 a2 b0 b1 b2 : R) :
    pairNF h a0 a1 a2 b0 b1 b2 =
      ![1 + a0 * b0 + a1 * b1,
        a0 + b0 + h * a0 * b0 + a2 * b1,
        a1 + b1 + h * a1 * b1 + a0 * b2,
        a2 * b2 + a1 * b0,
        a2 + b2 + a0 * b1 + h * (a0 * b2 + a2 * b1),
        a2 * b0 + a1 * b2 + h * a2 * b2] := by
  funext i
  fin_cases i <;>
    simp [pairNF, photon, mulNF, mulσ₀, mulσ₁, unitNF, s0, s1] <;> ring

/-- The order-`h¹` coefficient of `NF(γγ)`. -/
def N1 (a0 a1 a2 b0 b1 b2 : R) : Fin 6 → R :=
  ![0, a0 * b0, a1 * b1, 0, a0 * b2 + a2 * b1, a2 * b2]

/-- **`NF(γγ)` is exactly affine in `h`**: no `h²` term. -/
theorem pairNF_affine (h a0 a1 a2 b0 b1 b2 : R) :
    pairNF h a0 a1 a2 b0 b1 b2 =
      pairNF 0 a0 a1 a2 b0 b1 b2 + h • N1 a0 a1 a2 b0 b1 b2 := by
  rw [pairNF_eq, pairNF_eq]
  funext i; fin_cases i <;> simp [N1] <;> ring

/-- The order-1 part lies in word degree ≥ 1. -/
theorem N1_deg0 (a0 a1 a2 b0 b1 b2 : R) : N1 a0 a1 a2 b0 b1 b2 0 = 0 := rfl

/-- The order-1 part is additive in `φ` … -/
theorem N1_bilin_left (a0 a1 a2 a0' a1' a2' b0 b1 b2 : R) :
    N1 (a0 + a0') (a1 + a1') (a2 + a2') b0 b1 b2 =
      N1 a0 a1 a2 b0 b1 b2 + N1 a0' a1' a2' b0 b1 b2 := by
  funext i; fin_cases i <;> simp [N1] <;> ring

/-- … additive in `ψ` … -/
theorem N1_bilin_right (a0 a1 a2 b0 b1 b2 b0' b1' b2' : R) :
    N1 a0 a1 a2 (b0 + b0') (b1 + b1') (b2 + b2') =
      N1 a0 a1 a2 b0 b1 b2 + N1 a0 a1 a2 b0' b1' b2' := by
  funext i; fin_cases i <;> simp [N1] <;> ring

/-- … and homogeneous in each slot. -/
theorem N1_smul (c a0 a1 a2 b0 b1 b2 : R) :
    N1 (c * a0) (c * a1) (c * a2) b0 b1 b2 = c • N1 a0 a1 a2 b0 b1 b2 ∧
    N1 a0 a1 a2 (c * b0) (c * b1) (c * b2) = c • N1 a0 a1 a2 b0 b1 b2 := by
  constructor <;> (funext i; fin_cases i <;> simp [N1] <;> ring)

/-- The order-1 part is not zero (two horizontal polarizations). -/
theorem N1_nonzero [Nontrivial R] : N1 (1 : R) 0 0 1 0 0 ≠ 0 := by
  intro h; have := congrFun h 1; simp [N1] at this

/-- **Word degree 0 is `h`-free** on the γγ product. -/
theorem pairNF_deg0_h_free (h h' a0 a1 a2 b0 b1 b2 : R) :
    pairNF h a0 a1 a2 b0 b1 b2 0 = pairNF h' a0 a1 a2 b0 b1 b2 0 := by
  simp [pairNF_eq]

/-- Flavour is invisible at order zero: at `h = 0` the flipped photon IS the
photon. -/
theorem photonBar_order_zero (a0 a1 a2 : R) :
    photonBar 0 a0 a1 a2 = photon 0 a0 a1 a2 := by
  simp [photonBar, photon]

/-- **Flavour reaches word degree 0 at order `h¹`.** Flipping `ψ`'s letters
moves the degree-0 coordinate by `h·(h ψ₀₁ − φ₀ψ₀₁ − φ₁ψ₀₁ − ψ₀ − ψ₁)`. -/
theorem flavour_reaches_deg0 (h a0 a1 a2 b0 b1 b2 : R) :
    mulNF h (photon h a0 a1 a2) (photonBar h b0 b1 b2) 0
      - pairNF h a0 a1 a2 b0 b1 b2 0
      = h * (h * b2 - a0 * b2 - a1 * b2 - b0 - b1) := by
  simp [pairNF, photon, photonBar, mulNF, mulσ₀, mulσ₁, unitNF, s0, s1]; ring

/-- The witness: a horizontal photon `ψ = σ₀` against the bare core. The
degree-0 coordinate moves by exactly `−h`, so "word degree 0 carries no
flavour" fails whenever `h ≠ 0` (scope (a): true only modulo `h`). -/
theorem flavour_reaches_deg0_witness (h : R) :
    mulNF h (photon h 0 0 0) (photonBar h 1 0 0) 0 - pairNF h 0 0 0 1 0 0 0 = -h := by
  rw [flavour_reaches_deg0]; ring

/-- The word-degree ≥ 1 part. -/
def degPos (v : Fin 6 → R) : Fin 6 → R := v - v 0 • unitNF

/-- **Requirement (3) fails as stated**: with `φ = 0` the degree ≥ 1 part of
`NF(γγ)` is `ψ`'s own polarization, not `0`; a bilinear form vanishes at
`φ = 0`. -/
theorem degPos_not_bilinear [Nontrivial R] (h : R) :
    degPos (pairNF h 0 0 0 1 0 0) 1 ≠ 0 := by
  simp [degPos, pairNF_eq, unitNF]

/-- The connected part `NF((γ(φ)−1)(γ(ψ)−1))` — explicit, homogeneous
bilinear in `(φ, ψ)` — and `NF(γγ) = γ(φ) + γ(ψ) − 1 + connected`. -/
def connected (h a0 a1 a2 b0 b1 b2 : R) : Fin 6 → R :=
  ![a0 * b0 + a1 * b1, h * a0 * b0 + a2 * b1, h * a1 * b1 + a0 * b2,
    a2 * b2 + a1 * b0, a0 * b1 + h * (a0 * b2 + a2 * b1), a2 * b0 + a1 * b2 + h * a2 * b2]

theorem pairNF_eq_connected (h a0 a1 a2 b0 b1 b2 : R) :
    pairNF h a0 a1 a2 b0 b1 b2 =
      photon h a0 a1 a2 + photon h b0 b1 b2 - unitNF + connected h a0 a1 a2 b0 b1 b2 := by
  rw [pairNF_eq]
  funext i; fin_cases i <;> simp [photon, mulNF, mulσ₀, mulσ₁, unitNF, s0, s1, connected] <;> ring

theorem connected_eq_mulNF (h a0 a1 a2 b0 b1 b2 : R) :
    connected h a0 a1 a2 b0 b1 b2 =
      mulNF h (photon h a0 a1 a2 - unitNF) (photon h b0 b1 b2 - unitNF) := by
  funext i; fin_cases i <;>
    simp [connected, photon, mulNF, mulσ₀, mulσ₁, unitNF, s0, s1] <;> ring

end Generic

/-! ## The `(2,1)` channel -/

section Rep

variable {R : Type*} [Field R]

/-- `ρ(σ₀)` in the reduced-Burau `(2,1)` representation of the probe. -/
def rA (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, -q⁻¹; 0, -q⁻¹]
/-- `ρ(σ₁)`. -/
def rB (q : R) : Matrix (Fin 2) (Fin 2) R := !![-q⁻¹, 0; -q, q]

/-- `ρ` on the NF module, basis images `1, A, B, BA, AB, ABA`. -/
def rho (q : R) (v : Fin 6 → R) : Matrix (Fin 2) (Fin 2) R :=
  v 0 • 1 + v 1 • rA q + v 2 • rB q + v 3 • (rB q * rA q) + v 4 • (rA q * rB q)
    + v 5 • (rA q * rB q * rA q)

/-- **`ρ` is multiplicative** on the NF algebra at `h = q − q⁻¹`, so the
`(2,1)` projection of a normal form is well defined. -/
theorem rho_mul (q : R) (hq : q ≠ 0) (u v : Fin 6 → R) :
    rho q (mulNF (q - q⁻¹) u v) = rho q u * rho q v := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rho, rA, rB, mulNF, mulσ₀, mulσ₁, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

theorem rho_unit (q : R) : rho q unitNF = 1 := by simp [rho, unitNF]

/-- The quark state of the hypothesis: the `(2,1)` projection of the word-degree
≥ 1 part of `NF(γ(φ)γ(ψ))`. A DEFINITION under test, not an adopted one. -/
def quarkState (q a0 a1 a2 b0 b1 b2 : R) : Matrix (Fin 2) (Fin 2) R :=
  rho q (degPos (pairNF (q - q⁻¹) a0 a1 a2 b0 b1 b2))

/-- The γγ product's `(2,1)` image splits as the degree-0 scalar plus the
quark state. -/
theorem rho_pairNF_split (q a0 a1 a2 b0 b1 b2 : R) :
    rho q (pairNF (q - q⁻¹) a0 a1 a2 b0 b1 b2) =
      (1 + a0 * b0 + a1 * b1) • 1 + quarkState q a0 a1 a2 b0 b1 b2 := by
  have : pairNF (q - q⁻¹) a0 a1 a2 b0 b1 b2 0 = 1 + a0 * b0 + a1 * b1 := by
    simp [pairNF_eq]
  simp only [quarkState, degPos, this]
  ext i j; fin_cases i <;> fin_cases j <;> simp [rho, unitNF] <;> ring

/-! ### `results.md:9-13` as theorems

A template letter is `ρ(σ_g) + c·h·1` (every `σ^{±1}` and every averaged pair
is of this form, since `σ⁻¹ = σ − h`). The nucleon word is the Borromean core
`(σ₀σ₁⁻¹)³` followed by three quark letters on generators `0, 0, 1`. -/

/-- A template letter. -/
def letter (q : R) (M : Matrix (Fin 2) (Fin 2) R) (c : R) : Matrix (Fin 2) (Fin 2) R :=
  M + (c * (q - q⁻¹)) • 1

/-- The core-plus-quarks word with quark shifts `c₁ c₂ c₃`. -/
def nucleonWord (q c1 c2 c3 : R) : Matrix (Fin 2) (Fin 2) R :=
  (letter q (rA q) 0 * letter q (rB q) (-1)) * (letter q (rA q) 0 * letter q (rB q) (-1))
    * (letter q (rA q) 0 * letter q (rB q) (-1))
    * letter q (rA q) c1 * letter q (rA q) c2 * letter q (rB q) c3

/-- **Order `t⁰`: flavour is invisible.** At `q = 1` the `(2,1)` character of
the nucleon word is `0` for EVERY choice of quark shifts. -/
theorem template_order_zero (c1 c2 c3 : R) :
    (nucleonWord (1 : R) c1 c2 c3).trace = 0 := by
  simp [nucleonWord, letter, rA, rB, Matrix.trace_fin_two, Matrix.mul_fin_two]
  ring

/-- The flavour-blind template `S0` (all quark letters `σ`): character
identically `0`. -/
theorem template_S0_zero (q : R) (hq : q ≠ 0) :
    (nucleonWord q 0 0 0).trace = 0 := by
  simp only [nucleonWord, letter, rA, rB, Matrix.trace_fin_two, Matrix.mul_fin_two,
    Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, Matrix.of_apply,
    Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
    Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_fin_const, smul_eq_mul]
  field_simp
  ring

/-- The cofactor `g(q) = (q+1)(q⁴+1)P(q)/(4q⁹)` of the corpus template. -/
noncomputable def gSplus (q : R) : R :=
  (q + 1) * (q ^ 4 + 1)
    * (q ^ 12 - 2 * q ^ 10 + 2 * q ^ 8 - 3 * q ^ 6 + 2 * q ^ 4 - 2 * q ^ 2 + 1)
    / (4 * q ^ 9)

/-- **Order `t¹`: flavour is decided.** For the corpus template `S+ AVG` on the
proton (shifts `0, −½, −½`) the `(2,1)` character is `(q − 1)·g(q)`. -/
theorem template_SplusAVG_proton (q : R) (hq : q ≠ 0) (h2 : (2 : R) ≠ 0) :
    (nucleonWord q 0 (-1 / 2) (-1 / 2)).trace = (q - 1) * gSplus q := by
  simp only [nucleonWord, letter, rA, rB, gSplus, Matrix.trace_fin_two, Matrix.mul_fin_two,
    Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, Matrix.of_apply,
    Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons,
    Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_fin_const, smul_eq_mul]
  field_simp
  ring

/-- …and the `t¹` coefficient is nonzero: `g(1) = −1`. -/
theorem gSplus_one (h2 : (2 : R) ≠ 0) : gSplus (1 : R) = -1 := by
  have h4 : (4 : R) ≠ 0 := by
    have : (4 : R) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  simp [gSplus]
  field_simp
  norm_num

end Rep

end QOU.QuarkState
