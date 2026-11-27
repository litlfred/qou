import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Algebra.Polynomial.BigOperators
import MathlibExt.CauchyBinet
import BraidKnotOctonion.SYTBetaGapVandermonde

/-!
# Exact 4×4 Hankel Determinant Identity for 4-Row SU(4) q-Plancherel Normalization

Bean `qou-br4t` (parent epic `qou-v2om`).

For a nucleus of mass number `A` (`n = 3A` quarks), the spin-isospin `SU(4)` sector restricts
Wedderburn blocks `λ ⊢ n` to Young diagrams of at most four rows (`ℓ(λ) ≤ 4`). The unnormalized
balanced `q`-Plancherel weight
`W_λ(q) = [n]_q! / ∏_{□ ∈ λ} [h(□)]_q²`
exceeds `1` for `A ≥ 20` at `q₀ > 1`, so `-ln W_λ(q₀)` flips sign unless normalized by the
exact 4-row `SU(4)` partition sum

`Z_n^{(4)}(q) := ∑_{λ ⊢ n, ℓ(λ) ≤ 4} W_λ(q)`.

This module proves, with `0 sorry` and generic algebraic typeclasses (§7c `BP005`):

1. **Exact bijection with strictly increasing 4-tuples (`FourRowPartition.equivSelector`)**:
   Padding `λ = (λ₁, λ₂, λ₃, λ₄) ⊢ n` (`λ₁ ≥ λ₂ ≥ λ₃ ≥ λ₄ ≥ 0`) with Frobenius shifted parts
   `(λ₄, λ₃ + 1, λ₂ + 2, λ₁ + 3)` gives an equivalence between `FourRowPartition n` and
   strictly monotone selectors `f : Selector 4 (n + 7)` summing to `n + 6`.
2. **Divisor-free Frobenius shifted-part hook identity (`fourRow_hook_shiftedPart_identity`)**:
   Over any `[CommMonoid M]` and weight `w : ℕ → M`,
   `∏_{□ ∈ λ} w(h(□)) · ∏_{1 ≤ i < j ≤ 4} w(ℓ_i - ℓ_j) = ∏_{i=1}^4 descFactF w ℓ_i`.
3. **Closed-form 4×4 Cauchy–Binet / Andréief Hankel determinant identity (`z4_eq_hankel_det_coeff`)**:
   Over any `[Field K]` (`q ≠ 0`, `q - q⁻¹ ≠ 0`, nonvanishing `[m]_q!` for `m ≤ n + 6`),
   `Z_n^{(4)}(q) = ([n]_q! / (q - q⁻¹)^12) * [X^{n+6}] det_{0 ≤ j, k ≤ 3} (F̃_{j+k}(X; q))`,
   where `F̃_m(X; q) = ∑_{ℓ=0}^{n+6} (q^{(2m - 6)ℓ} / ([ℓ]_q!)²) X^ℓ`.
4. **Strict positivity and unit-interval probability bounds (`w4Norm_mem_Ioo`,
   `w4Norm_nuclear_mem_Ioo`)**:
   Over any strict ordered field `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`, for all
   `q > 1` and `n ≥ 2` (in particular `n = 3A` for every `A ≥ 1`), every 4-row normalized weight
   `W̃_λ^{(4)}(q) = W_λ(q) / Z_n^{(4)}(q)` satisfies `0 < W̃_λ^{(4)}(q) < 1` and sums to `1`.
-/

set_option autoImplicit false

namespace QOU.Nuclear.SU4FourRowHankelNormalization

open Matrix Finset Polynomial
open QOU.MathlibExt.CauchyBinet (Selector minorA minorB det_mul_eq_sum_minors)
open QOU.Mathlib.SYTBeta (prodHooksF descFactF betaNum prodHooksF_mul_pair_prod)

/-! ## §1. Four-Row Partitions and the Frobenius Shifted-Part Selector Bijection -/

/-- A partition `λ = (λ₁, λ₂, λ₃, λ₄)` of `n` into at most four parts (`λ₁ ≥ λ₂ ≥ λ₃ ≥ λ₄ ≥ 0`),
padded with trailing zeros to length `4`. -/
structure FourRowPartition (n : ℕ) where
  lam1 : ℕ
  lam2 : ℕ
  lam3 : ℕ
  lam4 : ℕ
  h12 : lam2 ≤ lam1
  h23 : lam3 ≤ lam2
  h34 : lam4 ≤ lam3
  hsum : lam1 + lam2 + lam3 + lam4 = n
  deriving DecidableEq

namespace FourRowPartition

@[ext]
theorem ext {n : ℕ} {p q : FourRowPartition n}
    (h1 : p.lam1 = q.lam1) (h2 : p.lam2 = q.lam2)
    (h3 : p.lam3 = q.lam3) (h4 : p.lam4 = q.lam4) : p = q := by
  cases p; cases q; simp_all

/-- Underlying 4-element `List ℕ` `[λ₁, λ₂, λ₃, λ₄]`. Trailing zeros contribute empty row
products (`List.range 0 = []`) and zero column-length increments (`0 > j` is false), so
`prodHooksF` agrees with the unpadded partition. -/
def toList {n : ℕ} (p : FourRowPartition n) : List ℕ :=
  [p.lam1, p.lam2, p.lam3, p.lam4]

theorem toList_sorted {n : ℕ} (p : FourRowPartition n) :
    List.Sorted (· ≥ ·) p.toList := by
  simp [toList, p.h12, p.h23, p.h34, le_trans p.h23 p.h12,
    le_trans p.h34 p.h23, le_trans p.h34 (le_trans p.h23 p.h12)]

/-- Strictly increasing Frobenius shifted-part map `Fin 4 → Fin (n + 7)`:
`(λ₄, λ₃ + 1, λ₂ + 2, λ₁ + 3)`. -/
def selFun {n : ℕ} (p : FourRowPartition n) : Fin 4 → Fin (n + 7) :=
  ![⟨p.lam4, by have := p.hsum; omega⟩,
    ⟨p.lam3 + 1, by have := p.hsum; omega⟩,
    ⟨p.lam2 + 2, by have := p.hsum; omega⟩,
    ⟨p.lam1 + 3, by have := p.hsum; omega⟩]

theorem strictMono_selFun {n : ℕ} (p : FourRowPartition n) :
    StrictMono (selFun p) := by
  intro a b hab
  have h12 := p.h12
  have h23 := p.h23
  have h34 := p.h34
  fin_cases a <;> fin_cases b <;> simp_all [selFun, Fin.lt_def] <;> omega

/-- The `Selector 4 (n + 7)` associated to a 4-row partition of `n`. -/
def toSelector {n : ℕ} (p : FourRowPartition n) : Selector 4 (n + 7) :=
  ⟨selFun p, strictMono_selFun p⟩

@[simp]
theorem toSelector_val_0 {n : ℕ} (p : FourRowPartition n) :
    (p.toSelector.1 0).val = p.lam4 := rfl

@[simp]
theorem toSelector_val_1 {n : ℕ} (p : FourRowPartition n) :
    (p.toSelector.1 1).val = p.lam3 + 1 := rfl

@[simp]
theorem toSelector_val_2 {n : ℕ} (p : FourRowPartition n) :
    (p.toSelector.1 2).val = p.lam2 + 2 := rfl

@[simp]
theorem toSelector_val_3 {n : ℕ} (p : FourRowPartition n) :
    (p.toSelector.1 3).val = p.lam1 + 3 := rfl

theorem sum_toSelector {n : ℕ} (p : FourRowPartition n) :
    (∑ r : Fin 4, (p.toSelector.1 r).val) = n + 6 := by
  have hs := p.hsum
  rw [Fin.sum_univ_four]
  simp only [toSelector_val_0, toSelector_val_1, toSelector_val_2, toSelector_val_3]
  omega

/-- Inverse map reconstructing a `FourRowPartition n` from any `Selector 4 (n + 7)` whose
four entries sum to `n + 6`. -/
def ofSelectorSum {n : ℕ} (f : Selector 4 (n + 7))
    (hsum : (∑ r : Fin 4, (f.1 r).val) = n + 6) : FourRowPartition n :=
  have h01 : (f.1 0).val < (f.1 1).val := f.2 (by decide : (0 : Fin 4) < 1)
  have h12 : (f.1 1).val < (f.1 2).val := f.2 (by decide : (1 : Fin 4) < 2)
  have h23 : (f.1 2).val < (f.1 3).val := f.2 (by decide : (2 : Fin 4) < 3)
  have hs4 : (f.1 0).val + (f.1 1).val + (f.1 2).val + (f.1 3).val = n + 6 := by
    simpa [Fin.sum_univ_four, add_assoc] using hsum
  { lam1 := (f.1 3).val - 3
    lam2 := (f.1 2).val - 2
    lam3 := (f.1 1).val - 1
    lam4 := (f.1 0).val
    h12 := by omega
    h23 := by omega
    h34 := by omega
    hsum := by omega }

theorem ofSelectorSum_toSelector {n : ℕ} (p : FourRowPartition n) :
    ofSelectorSum p.toSelector p.sum_toSelector = p := by
  ext <;> simp [ofSelectorSum]

theorem toSelector_ofSelectorSum {n : ℕ} (f : Selector 4 (n + 7))
    (hsum : (∑ r : Fin 4, (f.1 r).val) = n + 6) :
    (ofSelectorSum f hsum).toSelector = f := by
  have h01 : (f.1 0).val < (f.1 1).val := f.2 (by decide : (0 : Fin 4) < 1)
  have h12 : (f.1 1).val < (f.1 2).val := f.2 (by decide : (1 : Fin 4) < 2)
  have h23 : (f.1 2).val < (f.1 3).val := f.2 (by decide : (2 : Fin 4) < 3)
  apply Subtype.ext
  funext r
  fin_cases r <;> apply Fin.ext <;> simp [ofSelectorSum, toSelector, selFun] <;> omega

/-- Exact bijection between 4-row partitions of `n` and strictly increasing 4-element subsets
of `{0, …, n + 6}` with sum `n + 6`. -/
def equivSelector (n : ℕ) :
    FourRowPartition n ≃ {f : Selector 4 (n + 7) // (∑ r : Fin 4, (f.1 r).val) = n + 6} where
  toFun p := ⟨p.toSelector, p.sum_toSelector⟩
  invFun f := ofSelectorSum f.1 f.2
  left_inv p := ofSelectorSum_toSelector p
  right_inv f := Subtype.ext (toSelector_ofSelectorSum f.1 f.2)

instance (n : ℕ) : Fintype (FourRowPartition n) :=
  Fintype.ofEquiv _ (equivSelector n).symm

end FourRowPartition

/-! ## §2. Divisor-Free Frobenius Shifted-Part Hook Identity (`[CommMonoid M]`) -/

/-- **Divisor-free Frobenius shifted-part hook identity for 4-row Young diagrams.**
Over any commutative monoid `M` and weight `w : ℕ → M`, for every `p : FourRowPartition n` with
shifted parts `ℓ₁ = λ₁ + 3 > ℓ₂ = λ₂ + 2 > ℓ₃ = λ₃ + 1 > ℓ₄ = λ₄`:
`∏_{□ ∈ p} w(h(□)) · ∏_{1 ≤ i < j ≤ 4} w(ℓ_i - ℓ_j) = ∏_{i=1}^4 descFactF w ℓ_i`. -/
theorem fourRow_hook_shiftedPart_identity {M : Type*} [CommMonoid M] {n : ℕ}
    (w : ℕ → M) (p : FourRowPartition n) :
    prodHooksF w p.toList *
      (w ((p.lam1 + 3) - (p.lam2 + 2)) *
       w ((p.lam1 + 3) - (p.lam3 + 1)) *
       w ((p.lam1 + 3) - p.lam4) *
       w ((p.lam2 + 2) - (p.lam3 + 1)) *
       w ((p.lam2 + 2) - p.lam4) *
       w ((p.lam3 + 1) - p.lam4))
      = descFactF w (p.lam1 + 3) *
        descFactF w (p.lam2 + 2) *
        descFactF w (p.lam3 + 1) *
        descFactF w p.lam4 := by
  have h := prodHooksF_mul_pair_prod w p.toList p.toList_sorted
  have hr4 : List.range 4 = [0, 1, 2, 3] := rfl
  simp only [FourRowPartition.toList, List.length_cons, List.length_nil] at h
  rw [hr4] at h
  simpa [betaNum, Finset.prod_range_succ, mul_assoc] using h

/-! ## §3. 4×4 Vandermonde & Column/Row Scaling Determinant Lemmas (`[CommRing R]`) -/

section CommRingDet

variable {R : Type*} [CommRing R]

/-- Explicit `4 × 4` Vandermonde determinant over any commutative ring `R`. -/
theorem det_vandermonde_four (u0 u1 u2 u3 : R) :
    (Matrix.of fun j r : Fin 4 => (![u0, u1, u2, u3] r) ^ (j : ℕ)).det =
      (u1 - u0) * (u2 - u0) * (u3 - u0) * (u2 - u1) * (u3 - u1) * (u3 - u2) := by
  simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ, Fin.succAbove]
  ring

/-- Column-scaling of a `4 × 4` determinant over any commutative ring `R`. -/
theorem det_colScale_four (M : Matrix (Fin 4) (Fin 4) R) (c : Fin 4 → R) :
    (Matrix.of fun j r : Fin 4 => c r * M j r).det =
      (c 0 * c 1 * c 2 * c 3) * M.det := by
  simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ, Fin.succAbove]
  ring

/-- Row-scaling of a `4 × 4` determinant over any commutative ring `R`. -/
theorem det_rowScale_four (M : Matrix (Fin 4) (Fin 4) R) (c : Fin 4 → R) :
    (Matrix.of fun r k : Fin 4 => M r k * c r).det =
      M.det * (c 0 * c 1 * c 2 * c 3) := by
  simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ, Fin.succAbove]
  ring

end CommRingDet

/-! ## §4. Balanced Quantum Integers, 4-Row q-Plancherel Weights, and the 4×4 Hankel Identity -/

section FieldHankel

noncomputable section

variable {K : Type*} [Field K]

/-- Balanced quantum integer `[k]_q = (q^k - q^{-k}) / (q - q⁻¹)`. -/
def qInt (q : K) (k : ℕ) : K :=
  (q ^ k - (q ^ k)⁻¹) / (q - q⁻¹)

/-- Balanced quantum factorial `[m]_q! = [m]_q [m-1]_q ⋯ [1]_q`. -/
def qFact (q : K) (m : ℕ) : K :=
  descFactF (qInt q) m

@[simp]
theorem qFact_zero (q : K) : qFact q 0 = 1 := rfl

/-- Unnormalized balanced `q`-Plancherel weight `W_λ(q) = [n]_q! / (∏_{□ ∈ λ} [h(□)]_q)²`
for a 4-row partition `p : FourRowPartition n`. -/
def w4 (q : K) {n : ℕ} (p : FourRowPartition n) : K :=
  qFact q n / (prodHooksF (qInt q) p.toList) ^ 2

/-- The 4-row `SU(4)` `q`-Plancherel normalization (partition function)
`Z_n^{(4)}(q) = ∑_{p : FourRowPartition n} W_p(q)`. -/
def z4 (q : K) (n : ℕ) : K :=
  ∑ p : FourRowPartition n, w4 q p

/-- Normalized 4-row `SU(4)` `q`-Plancherel probability `W̃_p^{(4)}(q) = W_p(q) / Z_n^{(4)}(q)`. -/
def w4Norm (q : K) {n : ℕ} (p : FourRowPartition n) : K :=
  w4 q p / z4 q n

/-- Rectangular Cauchy–Binet factor entry `a_{j, m}(q) = (q^{2m})^j / (q^{3m} [m]_q!)`. -/
def hankelFactorEntry (q : K) (j : Fin 4) (m : ℕ) : K :=
  ((q ^ (2 * m)) ^ (j : ℕ)) / (q ^ (3 * m) * qFact q m)

/-- Truncated Hankel power series `F̃_m^{[≤ N]}(X; q) ∈ K[X]` (`m = 0, …, 6`):
`∑_{ℓ=0}^N ((q^{2ℓ})^m / (q^{6ℓ} ([ℓ]_q!)²)) X^ℓ`. -/
def hankelSeries (q : K) (N m : ℕ) : Polynomial K :=
  ∑ ell ∈ Finset.range (N + 1),
    Polynomial.C (((q ^ (2 * ell)) ^ m) / (q ^ (6 * ell) * (qFact q ell) ^ 2)) *
      Polynomial.X ^ ell

/-- Bridge to the integer-exponent form `q^{(2m - 6)ℓ} / ([ℓ]_q!)²` for `q ≠ 0`. -/
theorem hankelSeries_coeff_eq_zpow (q : K) (hq0 : q ≠ 0) (m ell : ℕ) :
    (((q ^ (2 * ell)) ^ m) / (q ^ (6 * ell) * (qFact q ell) ^ 2)) =
      (q ^ (((2 * (m : ℤ) - 6) * (ell : ℤ)))) / (qFact q ell) ^ 2 := by
  have h1 : (q ^ (2 * ell)) ^ m = q ^ ((2 * m * ell : ℕ) : ℤ) := by
    rw [← pow_mul, zpow_natCast]
    ring_nf
  have h2 : q ^ (6 * ell) = q ^ ((6 * ell : ℕ) : ℤ) := (zpow_natCast q (6 * ell)).symm
  have hexp : ((2 * (m : ℤ) - 6) * (ell : ℤ)) =
      ((2 * m * ell : ℕ) : ℤ) - ((6 * ell : ℕ) : ℤ) := by
    push_cast
    ring
  rw [h1, h2, hexp, zpow_sub₀ hq0, div_div]

/-- Difference identity `[b - a]_q = ((q^b)² - (q^a)²) / ((q - q⁻¹) q^a q^b)` for `a ≤ b`. -/
theorem qInt_sub_eq (q : K) (hq0 : q ≠ 0) {a b : ℕ} (hab : a ≤ b) :
    qInt q (b - a) = ((q ^ b) ^ 2 - (q ^ a) ^ 2) / ((q - q⁻¹) * (q ^ a * q ^ b)) := by
  unfold qInt
  have hb : b = a + (b - a) := (Nat.add_sub_of_le hab).symm
  conv_rhs => rw [hb]
  rw [pow_add]
  have hqa : q ^ a ≠ 0 := pow_ne_zero a hq0
  have hqd : q ^ (b - a) ≠ 0 := pow_ne_zero (b - a) hq0
  generalize q - q⁻¹ = h
  by_cases hh : h = 0
  · simp [hh]
  · field_simp

/-- Minor determinant of `hankelFactorEntry` on any strictly monotone `f : Selector 4 (N + 1)`. -/
theorem det_hankelFactor_minor (q : K) {N : ℕ} (hq0 : q ≠ 0) (hqh : q - q⁻¹ ≠ 0)
    (f : Selector 4 (N + 1)) :
    (Matrix.of fun j r : Fin 4 => hankelFactorEntry q j (f.1 r).val).det =
      ((q - q⁻¹) ^ 6 *
        (qInt q ((f.1 1).val - (f.1 0).val) *
         qInt q ((f.1 2).val - (f.1 0).val) *
         qInt q ((f.1 3).val - (f.1 0).val) *
         qInt q ((f.1 2).val - (f.1 1).val) *
         qInt q ((f.1 3).val - (f.1 1).val) *
         qInt q ((f.1 3).val - (f.1 2).val))) /
      (qFact q (f.1 0).val * qFact q (f.1 1).val *
       qFact q (f.1 2).val * qFact q (f.1 3).val) := by
  have h01 : (f.1 0).val ≤ (f.1 1).val := le_of_lt (f.2 (by decide : (0 : Fin 4) < 1))
  have h02 : (f.1 0).val ≤ (f.1 2).val := le_of_lt (f.2 (by decide : (0 : Fin 4) < 2))
  have h03 : (f.1 0).val ≤ (f.1 3).val := le_of_lt (f.2 (by decide : (0 : Fin 4) < 3))
  have h12 : (f.1 1).val ≤ (f.1 2).val := le_of_lt (f.2 (by decide : (1 : Fin 4) < 2))
  have h13 : (f.1 1).val ≤ (f.1 3).val := le_of_lt (f.2 (by decide : (1 : Fin 4) < 3))
  have h23 : (f.1 2).val ≤ (f.1 3).val := le_of_lt (f.2 (by decide : (2 : Fin 4) < 3))
  let c : Fin 4 → K := fun r => 1 / (q ^ (3 * (f.1 r).val) * qFact q (f.1 r).val)
  let V : Matrix (Fin 4) (Fin 4) K :=
    Matrix.of fun j r : Fin 4 => ((q ^ (f.1 r).val) ^ 2) ^ (j : ℕ)
  have hpow2 : ∀ m : ℕ, q ^ (2 * m) = (q ^ m) ^ 2 := fun m => by rw [mul_comm, pow_mul]
  have hM : (Matrix.of fun j r : Fin 4 => hankelFactorEntry q j (f.1 r).val) =
      Matrix.of fun j r : Fin 4 => c r * V j r := by
    apply Matrix.ext
    intro j r
    simp only [hankelFactorEntry, c, V, Matrix.of_apply, hpow2, div_eq_mul_inv]
    ring
  have hVeq : V = Matrix.of fun j r : Fin 4 =>
      (![(q ^ (f.1 0).val) ^ 2, (q ^ (f.1 1).val) ^ 2,
         (q ^ (f.1 2).val) ^ 2, (q ^ (f.1 3).val) ^ 2] r) ^ (j : ℕ) := by
    apply Matrix.ext
    intro j r
    fin_cases r <;> rfl
  rw [hM, det_colScale_four V c]
  have hV := det_vandermonde_four
    ((q ^ (f.1 0).val) ^ 2) ((q ^ (f.1 1).val) ^ 2)
    ((q ^ (f.1 2).val) ^ 2) ((q ^ (f.1 3).val) ^ 2)
  change (c 0 * c 1 * c 2 * c 3) * V.det = _
  rw [hVeq, hV]
  rw [qInt_sub_eq q hq0 h01, qInt_sub_eq q hq0 h02, qInt_sub_eq q hq0 h03,
      qInt_sub_eq q hq0 h12, qInt_sub_eq q hq0 h13, qInt_sub_eq q hq0 h23]
  simp only [c]
  have hp0 : q ^ (f.1 0).val ≠ 0 := pow_ne_zero _ hq0
  have hp1 : q ^ (f.1 1).val ≠ 0 := pow_ne_zero _ hq0
  have hp2 : q ^ (f.1 2).val ≠ 0 := pow_ne_zero _ hq0
  have hp3 : q ^ (f.1 3).val ≠ 0 := pow_ne_zero _ hq0
  have hp30 : q ^ (3 * (f.1 0).val) = (q ^ (f.1 0).val) ^ 3 := by rw [mul_comm, pow_mul]
  have hp31 : q ^ (3 * (f.1 1).val) = (q ^ (f.1 1).val) ^ 3 := by rw [mul_comm, pow_mul]
  have hp32 : q ^ (3 * (f.1 2).val) = (q ^ (f.1 2).val) ^ 3 := by rw [mul_comm, pow_mul]
  have hp33 : q ^ (3 * (f.1 3).val) = (q ^ (f.1 3).val) ^ 3 := by rw [mul_comm, pow_mul]
  rw [hp30, hp31, hp32, hp33]
  generalize q - q⁻¹ = h at hqh ⊢
  by_cases hdf :
      qFact q (f.1 0).val * qFact q (f.1 1).val *
        qFact q (f.1 2).val * qFact q (f.1 3).val = 0
  · rcases mul_eq_zero.mp hdf with h012 | h3
    · rcases mul_eq_zero.mp h012 with h01' | h2
      · rcases mul_eq_zero.mp h01' with h0 | h1
        · simp [h0]
        · simp [h1]
      · simp [h2]
    · simp [h3]
  · have hf0 : qFact q (f.1 0).val ≠ 0 := fun hz => hdf (by simp [hz])
    have hf1 : qFact q (f.1 1).val ≠ 0 := fun hz => hdf (by simp [hz])
    have hf2 : qFact q (f.1 2).val ≠ 0 := fun hz => hdf (by simp [hz])
    have hf3 : qFact q (f.1 3).val ≠ 0 := fun hz => hdf (by simp [hz])
    field_simp

/-- Shifted-part closed form for `W_λ(q)` and equality with the squared `4 × 4` minor of
`hankelFactorEntry`. -/
theorem w4_eq_minor_sq (q : K) {n : ℕ} (hq0 : q ≠ 0) (hqh : q - q⁻¹ ≠ 0)
    (hfact : ∀ m ≤ n + 6, qFact q m ≠ 0) (p : FourRowPartition n) :
    w4 q p =
      (qFact q n / (q - q⁻¹) ^ 12) *
        ((Matrix.of fun j r : Fin 4 =>
            hankelFactorEntry q j (p.toSelector.1 r).val).det) ^ 2 := by
  have hhook := fourRow_hook_shiftedPart_identity (qInt q) p
  have hs := p.hsum
  have hf1 : qFact q (p.lam1 + 3) ≠ 0 := hfact _ (by omega)
  have hf2 : qFact q (p.lam2 + 2) ≠ 0 := hfact _ (by omega)
  have hf3 : qFact q (p.lam3 + 1) ≠ 0 := hfact _ (by omega)
  have hf4 : qFact q p.lam4 ≠ 0 := hfact _ (by omega)
  have hrhs_ne :
      qFact q (p.lam1 + 3) * qFact q (p.lam2 + 2) *
        qFact q (p.lam3 + 1) * qFact q p.lam4 ≠ 0 :=
    mul_ne_zero (mul_ne_zero (mul_ne_zero hf1 hf2) hf3) hf4
  have hhooks_ne : prodHooksF (qInt q) p.toList ≠ 0 := by
    intro hz
    rw [hz, zero_mul] at hhook
    exact hrhs_ne hhook.symm
  rw [det_hankelFactor_minor q hq0 hqh p.toSelector]
  simp only [FourRowPartition.toSelector_val_0, FourRowPartition.toSelector_val_1,
    FourRowPartition.toSelector_val_2, FourRowPartition.toSelector_val_3]
  unfold w4 qFact at *
  have hhook_sq :
      (descFactF (qInt q) (p.lam1 + 3) * descFactF (qInt q) (p.lam2 + 2) *
        descFactF (qInt q) (p.lam3 + 1) * descFactF (qInt q) p.lam4) ^ 2 =
      (prodHooksF (qInt q) p.toList) ^ 2 *
        (qInt q ((p.lam1 + 3) - (p.lam2 + 2)) *
         qInt q ((p.lam1 + 3) - (p.lam3 + 1)) *
         qInt q ((p.lam1 + 3) - p.lam4) *
         qInt q ((p.lam2 + 2) - (p.lam3 + 1)) *
         qInt q ((p.lam2 + 2) - p.lam4) *
         qInt q ((p.lam3 + 1) - p.lam4)) ^ 2 := by
    rw [← mul_pow, hhook]
  generalize q - q⁻¹ = h at hqh ⊢
  field_simp
  linear_combination (descFactF (qInt q) n) * hhook_sq

/-- Left rectangular matrix `A ∈ K[X]^{4 × (N+1)}` for the Hankel factorization. -/
def hankelMatA (q : K) (N : ℕ) : Matrix (Fin 4) (Fin (N + 1)) (Polynomial K) :=
  Matrix.of fun j ell => Polynomial.C (hankelFactorEntry q j ell.val)

/-- Right rectangular matrix `B ∈ K[X]^{(N+1) × 4}` for the Hankel factorization. -/
def hankelMatB (q : K) (N : ℕ) : Matrix (Fin (N + 1)) (Fin 4) (Polynomial K) :=
  Matrix.of fun ell k => Polynomial.C (hankelFactorEntry q k ell.val) * Polynomial.X ^ ell.val

/-- Product `(A * B)_{j, k} = F̃_{j+k}^{[≤ N]}(X; q)` is the `4 × 4` Hankel matrix. -/
theorem hankelMatA_mul_hankelMatB (q : K) (N : ℕ) :
    hankelMatA q N * hankelMatB q N =
      Matrix.of fun j k : Fin 4 => hankelSeries q N ((j : ℕ) + (k : ℕ)) := by
  apply Matrix.ext
  intro j k
  rw [Matrix.mul_apply, Matrix.of_apply, hankelSeries]
  simp only [hankelMatA, hankelMatB, Matrix.of_apply]
  rw [Fin.sum_univ_eq_sum_range
    (fun ell => Polynomial.C (hankelFactorEntry q j ell) *
      (Polynomial.C (hankelFactorEntry q k ell) * Polynomial.X ^ ell)) (N + 1)]
  refine Finset.sum_congr rfl fun ell _ => ?_
  simp only [hankelFactorEntry]
  rw [← mul_assoc, ← Polynomial.C_mul]
  congr 2
  rw [pow_add]
  have hpow6 : q ^ (6 * ell) = q ^ (3 * ell) * q ^ (3 * ell) := by
    rw [← pow_add]
    congr 1
    omega
  rw [hpow6]
  ring

/-- Each Cauchy–Binet minor pair `(minorA A f, minorB B f)` evaluates to
`C ((det M_f)²) * X^{∑ r, f(r)}`. -/
theorem minorA_mul_minorB_hankel (q : K) (N : ℕ) (f : Selector 4 (N + 1)) :
    (minorA (hankelMatA q N) f).det * (minorB (hankelMatB q N) f).det =
      Polynomial.C (((Matrix.of fun j r : Fin 4 => hankelFactorEntry q j (f.1 r).val).det) ^ 2) *
        Polynomial.X ^ (∑ r : Fin 4, (f.1 r).val) := by
  let M : Matrix (Fin 4) (Fin 4) K :=
    Matrix.of fun j r : Fin 4 => hankelFactorEntry q j (f.1 r).val
  have hA : minorA (hankelMatA q N) f = Polynomial.C.mapMatrix M := by
    apply Matrix.ext
    intro j r
    rfl
  have hAdet : (minorA (hankelMatA q N) f).det = Polynomial.C M.det := by
    rw [hA, ← RingHom.map_det]
  have hB : minorB (hankelMatB q N) f =
      Matrix.of fun r k : Fin 4 =>
        (Polynomial.C.mapMatrix Mᵀ) r k * Polynomial.X ^ (f.1 r).val := by
    apply Matrix.ext
    intro r k
    rfl
  have hBdet : (minorB (hankelMatB q N) f).det =
      Polynomial.C M.det *
        (Polynomial.X ^ (f.1 0).val * Polynomial.X ^ (f.1 1).val *
         Polynomial.X ^ (f.1 2).val * Polynomial.X ^ (f.1 3).val) := by
    rw [hB, det_rowScale_four (Polynomial.C.mapMatrix Mᵀ) (fun r => Polynomial.X ^ (f.1 r).val),
        ← RingHom.map_det, Matrix.det_transpose]
  rw [hAdet, hBdet, ← mul_assoc, ← Polynomial.C_mul, sq, Fin.sum_univ_four]
  simp only [pow_add, mul_assoc]
  rfl

private theorem poly_finset_sum_coeff {ι : Type*} (s : Finset ι)
    (g : ι → Polynomial K) (m : ℕ) :
    (∑ x ∈ s, g x).coeff m = ∑ x ∈ s, (g x).coeff m := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s ha ih => simp [Finset.sum_insert ha, ih]

/-- **Closed-Form 4×4 Hankel Determinant Identity for `Z_n^{(4)}(q)` (`[Field K]`).**
For any field `K` and `q : K` with `q ≠ 0`, `q - q⁻¹ ≠ 0`, and `[m]_q! ≠ 0` for `m ≤ n + 6`,
`Z_n^{(4)}(q) = ([n]_q! / (q - q⁻¹)^12) * [X^{n+6}] det_{0 ≤ j, k ≤ 3} (F̃_{j+k}^{[≤ n+6]}(X; q))`. -/
theorem z4_eq_hankel_det_coeff (q : K) (n : ℕ)
    (hq0 : q ≠ 0) (hqh : q - q⁻¹ ≠ 0)
    (hfact : ∀ m ≤ n + 6, qFact q m ≠ 0) :
    z4 q n =
      (qFact q n / (q - q⁻¹) ^ 12) *
        ((Matrix.of fun j k : Fin 4 =>
            hankelSeries q (n + 6) ((j : ℕ) + (k : ℕ))).det).coeff (n + 6) := by
  rw [← hankelMatA_mul_hankelMatB q (n + 6),
      det_mul_eq_sum_minors (hankelMatA q (n + 6)) (hankelMatB q (n + 6))]
  simp_rw [minorA_mul_minorB_hankel q (n + 6)]
  rw [poly_finset_sum_coeff]
  simp_rw [Polynomial.coeff_C_mul_X_pow]
  rw [← Finset.sum_filter, Finset.mul_sum]
  unfold z4
  rw [Fintype.sum_equiv (FourRowPartition.equivSelector n)
        (fun p => w4 q p)
        (fun s => (qFact q n / (q - q⁻¹) ^ 12) *
          ((Matrix.of fun j r : Fin 4 => hankelFactorEntry q j (s.1.1 r).val).det) ^ 2)
        (fun p => w4_eq_minor_sq q hq0 hqh hfact p)]
  symm
  refine Finset.sum_bij'
    (fun f hf => ⟨f, (Finset.mem_filter.mp hf).2.symm⟩)
    (fun s _ => s.1)
    (fun _ _ => Finset.mem_univ _)
    (fun s _ => Finset.mem_filter.mpr ⟨Finset.mem_univ _, s.2.symm⟩)
    (fun _ _ => rfl)
    (fun _ _ => rfl)
    (fun _ _ => rfl)

end

end FieldHankel

/-! ## §5. Strict Positivity & Unit-Interval Bound `0 < W̃_λ^{(4)}(q) < 1` for `q > 1` -/

section OrderedField

noncomputable section

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- One-row partition `(n, 0, 0, 0) : FourRowPartition n`. -/
def oneRowPartition (n : ℕ) : FourRowPartition n where
  lam1 := n
  lam2 := 0
  lam3 := 0
  lam4 := 0
  h12 := Nat.zero_le n
  h23 := le_rfl
  h34 := le_rfl
  hsum := by omega

/-- Second distinct 4-row partition `(n - 1, 1, 0, 0)` for `n ≥ 2`. -/
def twoRowHookPartition (n : ℕ) (hn : 2 ≤ n) : FourRowPartition n where
  lam1 := n - 1
  lam2 := 1
  lam3 := 0
  lam4 := 0
  h12 := by omega
  h23 := by omega
  h34 := le_rfl
  hsum := by omega

theorem oneRowPartition_ne_twoRowHookPartition {n : ℕ} (hn : 2 ≤ n) :
    oneRowPartition n ≠ twoRowHookPartition n hn := by
  intro h
  have h2 := congrArg FourRowPartition.lam2 h
  simp [oneRowPartition, twoRowHookPartition] at h2

theorem qInt_pos_of_one_lt {q : K} (hq : 1 < q) {k : ℕ} (hk : 0 < k) :
    0 < qInt q k := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hinv_lt : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have hden : 0 < q - q⁻¹ := sub_pos.mpr (lt_trans hinv_lt hq)
  have hpow : 1 < q ^ k := one_lt_pow₀ hq hk.ne'
  have hpow_inv : (q ^ k)⁻¹ < 1 := inv_lt_one_of_one_lt₀ hpow
  have hnum : 0 < q ^ k - (q ^ k)⁻¹ := sub_pos.mpr (lt_trans hpow_inv hpow)
  exact div_pos hnum hden

theorem qFact_pos_of_one_lt {q : K} (hq : 1 < q) (m : ℕ) :
    0 < qFact q m := by
  unfold qFact descFactF
  refine Finset.prod_pos fun j hj => ?_
  rw [Finset.mem_range] at hj
  exact qInt_pos_of_one_lt hq (by omega)

/-- Hypothesis-free specialization of the 4×4 Hankel determinant identity for all `q > 1`. -/
theorem z4_eq_hankel_det_coeff_of_one_lt {q : K} (hq : 1 < q) (n : ℕ) :
    z4 q n =
      (qFact q n / (q - q⁻¹) ^ 12) *
        ((Matrix.of fun j k : Fin 4 =>
            hankelSeries q (n + 6) ((j : ℕ) + (k : ℕ))).det).coeff (n + 6) := by
  have hq0 : q ≠ 0 := (lt_trans zero_lt_one hq).ne'
  have hqh : q - q⁻¹ ≠ 0 :=
    (sub_pos.mpr (lt_trans (inv_lt_one_of_one_lt₀ hq) hq)).ne'
  exact z4_eq_hankel_det_coeff q n hq0 hqh (fun m _ => (qFact_pos_of_one_lt hq m).ne')

theorem w4_pos_of_one_lt {q : K} (hq : 1 < q) {n : ℕ} (p : FourRowPartition n) :
    0 < w4 q p := by
  have hhook := fourRow_hook_shiftedPart_identity (qInt q) p
  have hrhs_pos :
      0 < descFactF (qInt q) (p.lam1 + 3) * descFactF (qInt q) (p.lam2 + 2) *
          descFactF (qInt q) (p.lam3 + 1) * descFactF (qInt q) p.lam4 := by
    exact mul_pos (mul_pos (mul_pos
      (qFact_pos_of_one_lt hq _) (qFact_pos_of_one_lt hq _))
      (qFact_pos_of_one_lt hq _)) (qFact_pos_of_one_lt hq _)
  have hhooks_ne : prodHooksF (qInt q) p.toList ≠ 0 := by
    intro hz
    rw [hz, zero_mul] at hhook
    exact hrhs_pos.ne' hhook.symm
  unfold w4
  exact div_pos (qFact_pos_of_one_lt hq n) (sq_pos_of_ne_zero hhooks_ne)

theorem z4_pos_of_one_lt {q : K} (hq : 1 < q) (n : ℕ) :
    0 < z4 q n := by
  unfold z4
  exact Finset.sum_pos'
    (fun q_p _ => le_of_lt (w4_pos_of_one_lt hq q_p))
    ⟨oneRowPartition n, Finset.mem_univ _, w4_pos_of_one_lt hq (oneRowPartition n)⟩

/-- Total probability mass of the 4-row `SU(4)` `q`-Plancherel distribution equals `1` for `q > 1`. -/
theorem sum_w4Norm_eq_one {q : K} (hq : 1 < q) (n : ℕ) :
    (∑ p : FourRowPartition n, w4Norm q p) = 1 := by
  unfold w4Norm
  rw [← Finset.sum_div]
  exact div_self (z4_pos_of_one_lt hq n).ne'

/-- **Strict Unit-Interval Bound `0 < W̃_λ^{(4)}(q) < 1`** for all `q > 1` and `n ≥ 2`. -/
theorem w4Norm_mem_Ioo {q : K} (hq : 1 < q) {n : ℕ} (hn : 2 ≤ n)
    (p : FourRowPartition n) :
    0 < w4Norm q p ∧ w4Norm q p < 1 := by
  have hZpos : 0 < z4 q n := z4_pos_of_one_lt hq n
  have hWpos : 0 < w4 q p := w4_pos_of_one_lt hq p
  refine ⟨div_pos hWpos hZpos, ?_⟩
  rw [w4Norm, div_lt_one hZpos]
  obtain ⟨p', hp'ne⟩ : ∃ p' : FourRowPartition n, p' ≠ p := by
    by_cases h : p = oneRowPartition n
    · exact ⟨twoRowHookPartition n hn, fun heq =>
        oneRowPartition_ne_twoRowHookPartition hn (h.symm.trans heq.symm)⟩
    · exact ⟨oneRowPartition n, Ne.symm h⟩
  have hpair : w4 q p + w4 q p' ≤ z4 q n := by
    unfold z4
    have hsub : ({p, p'} : Finset (FourRowPartition n)) ⊆ Finset.univ :=
      Finset.subset_univ _
    calc
      w4 q p + w4 q p'
          = ∑ x ∈ ({p, p'} : Finset (FourRowPartition n)), w4 q x := by
            rw [Finset.sum_pair hp'ne.symm]
      _ ≤ ∑ x : FourRowPartition n, w4 q x :=
            Finset.sum_le_sum_of_subset_of_nonneg hsub
              (fun x _ _ => le_of_lt (w4_pos_of_one_lt hq x))
  linarith [w4_pos_of_one_lt hq p']

/-- **Nuclear `n = 3A` Specialization**: for every baryon number `A ≥ 1` (`n = 3A ≥ 3 ≥ 2`) and
every `q > 1`, the normalized 4-row `SU(4)` `q`-Plancherel weight satisfies
`0 < W̃_λ^{(4)}(q) < 1`. -/
theorem w4Norm_nuclear_mem_Ioo {q : K} (hq : 1 < q) {A : ℕ} (hA : 1 ≤ A)
    (p : FourRowPartition (3 * A)) :
    0 < w4Norm q p ∧ w4Norm q p < 1 :=
  w4Norm_mem_Ioo hq (by omega) p

end

end OrderedField

end QOU.Nuclear.SU4FourRowHankelNormalization
