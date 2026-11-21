import Mathlib.Algebra.Polynomial.AlgebraMap
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.Tactic

/-!
# Formal Fuchsian theory at a regular singular point

Step 1 of `docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md` (Drinfeld's KZ associator),
first brick: the **formal** half of the local theory of a linear ODE with a simple pole.

## The equation and the ansatz

Let `R` be a ring (in the application, `R = End(V^{⊗3})`), and consider

  `z F'(z) = M(z) F(z)`,   `M(z) = ∑_{k ≥ 0} M_k z^k`,   `A := M_0`.

The classical ansatz is `F(z) = H(z) z^A` with `H(z) = ∑ H_k z^k`, `H_0 = 1`. Since `z^A`
commutes with `A` and `z (z^A)' = A z^A`, the equation becomes the **gauge equation**

  `z H'(z) + H(z) A = M(z) H(z)`,

whose `z^k` coefficient is `k H_k + H_k A = ∑_{j ≤ k} M_{k-j} H_j` (`IsFormalGauge`). With
`H_0 = 1` this is equivalent to the recursion

  `(k − ad_A)(H_k) = ∑_{j < k} M_{k-j} H_j`   for `k ≥ 1`,   `ad_A X = A X − X A`

(`isFormalGauge_iff`). So the **non-resonance** condition — each `k − ad_A` (`k ≥ 1`) is
bijective — gives a unique formal solution (`exists_unique_formalGauge`). Over a field, if `ad_A`
is annihilated by a polynomial `p` with `p(k) ≠ 0` for all `k ≥ 1`, non-resonance holds
(`nonResonant_of_aeval`): for diagonalisable `A` this is the usual "no two eigenvalues of `A`
differ by a positive integer".

## The KZ instance

For the three-point KZ system `G' = (A/z + B/(z−1)) G` near `z = 0`, `M_0 = A` and
`M_k = −B` (`k ≥ 1`), because `z B/(z−1) = −B ∑_{k≥1} z^k` (`kzM0`). For `𝔤𝔩_n` with the
trace form, the Casimir on `V ⊗ V` is the flip (`casimir_eq_flip`), so
`A = ℏ P₁₂`, `B = ℏ P₂₃` on `V^{⊗3}`. Every element `P` with `P² = 1` has
`ad_P³ = 4 ad_P` (`ad_cube_of_involution`), hence `ad_{ℏP}` is annihilated by `X(X² − 4ℏ²)` and
`ℏ P` is non-resonant iff no positive integer `k` has `k² = 4ℏ²`
(`nonResonant_smul_involution`). In particular `ℏ ∉ ℚ` suffices (`kz_nonResonant_of_irrational`),
which is the hypothesis of the Drinfeld–Kohno route.

## What is NOT here

Convergence of `∑ H_k z^k` (radius ≥ 1 for KZ), the analytic solution `H(z) z^A` on `(0,1)`, the
renormalised monodromy `Φ_KZ`, and the pentagon / hexagon identities. Those are the later bricks
of Step 1 and are tracked separately; nothing here is used as a substitute for them.

Base ring (§7c): generic `Ring R` for the recursion; generic `Field K` with `[CharZero K]` only
where a polynomial is evaluated at the integers. Nothing archimedean. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1, §5
-- Ref: [drinfeld1991] (renormalised KZ monodromy; this file is only the formal local step)
-/

namespace QOU.KZ.FuchsianFormal

open Finset Polynomial

section Recursion

variable {R : Type*} [Ring R]

/-- The commutator `ad_A X = A X − X A`. -/
def ad (A X : R) : R := A * X - X * A

/-- The `k`-th indicial operator `X ↦ k X − ad_A X`. -/
def indicial (A : R) (k : ℕ) (X : R) : R := (k : R) * X - ad A X

/-- **Non-resonance at the singular point**: every indicial operator with `k ≥ 1` is bijective. -/
def NonResonant (A : R) : Prop :=
  ∀ k : ℕ, 0 < k → Function.Bijective (indicial A k)

/-- `H` is a formal solution of the gauge equation `z H' + H M₀ = M H`, coefficientwise. -/
def IsFormalGauge (M H : ℕ → R) : Prop :=
  ∀ k : ℕ, (k : R) * H k + H k * M 0 = ∑ j ∈ range (k + 1), M (k - j) * H j

/-- With `H₀ = 1`, the gauge equation is exactly the indicial recursion. -/
theorem isFormalGauge_iff (M H : ℕ → R) (h0 : H 0 = 1) :
    IsFormalGauge M H ↔
      ∀ k : ℕ, 0 < k → indicial (M 0) k (H k) = ∑ j ∈ range k, M (k - j) * H j := by
  constructor
  · intro h k hk
    have := h k
    rw [sum_range_succ, Nat.sub_self] at this
    simp only [indicial, ad]
    rw [← sub_eq_iff_eq_add] at this
    rw [← this]; abel
  · intro h k
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · simp [h0]
    · have := h k hk
      rw [sum_range_succ, Nat.sub_self, ← this]
      simp only [indicial, ad]; abel

/-- The formal solution, built by recursion from the inverses of the indicial operators. -/
noncomputable def formalSol (M : ℕ → R) (h : NonResonant (M 0)) : ℕ → R
  | 0 => 1
  | k + 1 => (Equiv.ofBijective _ (h (k + 1) k.succ_pos)).symm
      (∑ j : Fin (k + 1), M (k + 1 - j) * formalSol M h j)
  decreasing_by exact j.isLt

theorem formalSol_zero (M : ℕ → R) (h : NonResonant (M 0)) : formalSol M h 0 = 1 := by
  rw [formalSol]

theorem indicial_formalSol (M : ℕ → R) (h : NonResonant (M 0)) (k : ℕ) (hk : 0 < k) :
    indicial (M 0) k (formalSol M h k) = ∑ j ∈ range k, M (k - j) * formalSol M h j := by
  obtain ⟨k, rfl⟩ : ∃ m, k = m + 1 := ⟨k - 1, by omega⟩
  rw [formalSol]
  have := (Equiv.ofBijective _ (h (k + 1) k.succ_pos)).apply_symm_apply
    (∑ j : Fin (k + 1), M (k + 1 - j) * formalSol M h j)
  rw [Equiv.ofBijective_apply] at this
  rw [this, Fin.sum_univ_eq_sum_range (fun j => M (k + 1 - j) * formalSol M h j) (k + 1)]

/-- **Existence** of a formal solution with `H₀ = 1` under non-resonance. -/
theorem formalSol_isFormalGauge (M : ℕ → R) (h : NonResonant (M 0)) :
    IsFormalGauge M (formalSol M h) :=
  (isFormalGauge_iff M _ (formalSol_zero M h)).2 (indicial_formalSol M h)

/-- **Uniqueness**: two formal solutions with `H₀ = 1` agree, given injectivity of the indicial
operators (half of non-resonance). -/
theorem formalGauge_unique (M H H' : ℕ → R)
    (hinj : ∀ k : ℕ, 0 < k → Function.Injective (indicial (M 0) k))
    (h0 : H 0 = 1) (h0' : H' 0 = 1) (hH : IsFormalGauge M H) (hH' : IsFormalGauge M H') :
    H = H' := by
  rw [isFormalGauge_iff M H h0] at hH
  rw [isFormalGauge_iff M H' h0'] at hH'
  funext k
  induction k using Nat.strong_induction_on with
  | _ k ih =>
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · rw [h0, h0']
    · apply hinj k hk
      rw [hH k hk, hH' k hk]
      exact sum_congr rfl fun j hj => by rw [ih j (mem_range.1 hj)]

/-- **Existence and uniqueness** of the normalised formal solution at a non-resonant
regular singular point. -/
theorem exists_unique_formalGauge (M : ℕ → R) (h : NonResonant (M 0)) :
    ∃! H : ℕ → R, H 0 = 1 ∧ IsFormalGauge M H :=
  ⟨formalSol M h, ⟨formalSol_zero M h, formalSol_isFormalGauge M h⟩,
    fun H' ⟨h0', hH'⟩ => formalGauge_unique M H' (formalSol M h)
      (fun k hk => (h k hk).1) h0' (formalSol_zero M h) hH' (formalSol_isFormalGauge M h)⟩

end Recursion

section Resolvent

/-- **Resolvent from an annihilating polynomial.** In an algebra over a field, if `p(T) = 0` and
`p(k) ≠ 0`, then `k − T` is a unit; its inverse is `q(T)/p(k)` where
`p − p(k) = (X − k) q`. -/
theorem isUnit_algebraMap_sub_of_aeval {K V : Type*} [Field K] [Ring V] [Algebra K V]
    (T : V) (p : K[X]) (hp : aeval T p = 0) (k : K) (hk : p.eval k ≠ 0) :
    IsUnit (algebraMap K V k - T) := by
  obtain ⟨q, hq⟩ := X_sub_C_dvd_sub_C_eval (a := k) (p := p)
  have hq' : p - C (p.eval k) = q * (X - C k) := by rw [hq, mul_comm]
  have e1 := congrArg (aeval T) hq
  have e2 := congrArg (aeval T) hq'
  simp only [map_sub, map_mul, aeval_X, aeval_C, hp, zero_sub] at e1 e2
  have key : (algebraMap K V k - T) * aeval T q = algebraMap K V (p.eval k) := by
    rw [← neg_neg (algebraMap K V (p.eval k)), e1]; noncomm_ring
  have key' : aeval T q * (algebraMap K V k - T) = algebraMap K V (p.eval k) := by
    rw [← neg_neg (algebraMap K V (p.eval k)), e2]; noncomm_ring
  refine ⟨⟨algebraMap K V k - T, algebraMap K V (p.eval k)⁻¹ * aeval T q, ?_, ?_⟩, rfl⟩
  · rw [← mul_assoc, ← Algebra.commutes, mul_assoc, key, ← map_mul, inv_mul_cancel₀ hk, map_one]
  · rw [mul_assoc, key', ← map_mul, inv_mul_cancel₀ hk, map_one]

variable {K R : Type*} [Field K] [Ring R] [Algebra K R]

/-- `ad_A` as a `K`-linear endomorphism of `R`. -/
def adL (A : R) : Module.End K R := LinearMap.mulLeft K A - LinearMap.mulRight K A

theorem adL_apply (A X : R) : adL (K := K) A X = ad A X := rfl

theorem indicial_eq (A : R) (k : ℕ) :
    indicial A k = ⇑(algebraMap K (Module.End K R) (k : K) - adL (K := K) A : Module.End K R) := by
  funext X
  rw [LinearMap.sub_apply, Module.algebraMap_end_apply, adL_apply, Nat.cast_smul_eq_nsmul,
    nsmul_eq_mul]
  rfl

/-- **Non-resonance from an annihilating polynomial of `ad_A`.** -/
theorem nonResonant_of_aeval (A : R) (p : K[X]) (hp : aeval (adL (K := K) A) p = 0)
    (hk : ∀ k : ℕ, 0 < k → p.eval (k : K) ≠ 0) : NonResonant A := by
  intro k hk0
  rw [indicial_eq (K := K)]
  exact (Module.End.isUnit_iff _).1 (isUnit_algebraMap_sub_of_aeval _ p hp _ (hk k hk0))

end Resolvent

section Involution

variable {R : Type*} [Ring R]

/-- For an involution `P`, `ad_P³ = 4 ad_P`. -/
theorem ad_cube_of_involution (P X : R) (hP : P * P = 1) :
    ad P (ad P (ad P X)) = 4 * ad P X := by
  have hP' : ∀ Y : R, Y * P * P = Y := fun Y => by rw [mul_assoc, hP, mul_one]
  simp only [ad, mul_sub, sub_mul, ← mul_assoc, hP, hP', one_mul]
  noncomm_ring

variable {K : Type*} [Field K] [Algebra K R]

theorem aeval_adL_smul_involution (P : R) (hP : P * P = 1) (c : K) :
    aeval (adL (K := K) (c • P)) (X ^ 3 - C (4 * c ^ 2) * X) = 0 := by
  ext Y
  simp only [map_sub, map_mul, aeval_X, aeval_C, LinearMap.sub_apply,
    Module.End.mul_apply, Module.algebraMap_end_apply, pow_succ, pow_zero, one_mul,
    LinearMap.zero_apply, adL_apply]
  have hs : ∀ Z : R, ad (c • P) Z = c • ad P Z := fun Z => by
    simp only [ad, smul_mul_assoc, mul_smul_comm, smul_sub]
  have hs2 : ∀ Z : R, ad P (c • Z) = c • ad P Z := fun Z => by
    simp only [ad, smul_mul_assoc, mul_smul_comm, smul_sub]
  simp only [hs, hs2]
  rw [ad_cube_of_involution P Y hP,
    show (4 : R) * ad P Y = (4 : K) • ad P Y by rw [Algebra.smul_def, map_ofNat]]
  module

/-- **Non-resonance for `ℏ P`, `P² = 1`**: it suffices that `k² ≠ 4ℏ²` for every integer `k ≥ 1`. -/
theorem nonResonant_smul_involution [CharZero K] (P : R) (hP : P * P = 1) (c : K)
    (hc : ∀ k : ℕ, 0 < k → (k : K) ^ 2 ≠ 4 * c ^ 2) : NonResonant (c • P) := by
  refine nonResonant_of_aeval (K := K) _ _ (aeval_adL_smul_involution P hP c) fun k hk => ?_
  simp only [eval_sub, eval_pow, eval_X, eval_mul, eval_C]
  rw [show (k : K) ^ 3 - 4 * c ^ 2 * k = k * ((k : K) ^ 2 - 4 * c ^ 2) by ring]
  exact mul_ne_zero (Nat.cast_ne_zero.2 hk.ne') (sub_ne_zero.2 (hc k hk))

/-- **Irrational coupling is non-resonant.** If `ℏ` is not the image of a rational, then `ℏ P`
is non-resonant for every involution `P`. -/
theorem nonResonant_smul_involution_of_irrational [CharZero K] (P : R) (hP : P * P = 1) (c : K)
    (hc : ∀ r : ℚ, (r : K) ≠ c) : NonResonant (c • P) := by
  refine nonResonant_smul_involution P hP c fun k hk h => ?_
  have : ((k : K) - 2 * c) * ((k : K) + 2 * c) = 0 := by linear_combination h
  rcases mul_eq_zero.1 this with h1 | h1
  · exact hc ((k : ℚ) / 2) (by push_cast; linear_combination h1 / 2)
  · exact hc (-(k : ℚ) / 2) (by push_cast; linear_combination -h1 / 2)

end Involution

section GLn

/-! ### The `𝔤𝔩_n` data: Casimir = flip, and the KZ residues on `V^{⊗3}` -/

variable (K : Type*) [Field K] (n : ℕ)

/-- The permutation matrix of `σ`: column `j` is the basis vector `e_{σ j}`. -/
def permMat {ι : Type*} [DecidableEq ι] (σ : ι → ι) : Matrix ι ι K :=
  Matrix.of fun i j => if σ j = i then 1 else 0

theorem permMat_mul {ι : Type*} [Fintype ι] [DecidableEq ι] (σ τ : ι → ι) :
    permMat K σ * permMat K τ = permMat K (σ ∘ τ) := by
  ext i j
  simp [permMat, Matrix.mul_apply, Finset.sum_ite_eq', eq_comm]

theorem permMat_mul_self {ι : Type*} [Fintype ι] [DecidableEq ι] (σ : ι → ι)
    (hσ : ∀ x, σ (σ x) = x) : permMat K σ * permMat K σ = 1 := by
  rw [permMat_mul]
  ext i j
  simp [permMat, Matrix.one_apply, hσ, eq_comm]

theorem single_apply' {ι : Type*} [DecidableEq ι] (a b i j : ι) :
    (Matrix.single a b (1 : K) : Matrix ι ι K) i j = if a = i ∧ b = j then 1 else 0 := rfl

/-- The flip on `V ⊗ V`, `V = K^n`, as a matrix indexed by `Fin n × Fin n`. -/
def flip2 : Matrix (Fin n × Fin n) (Fin n × Fin n) K := permMat K Prod.swap

/-- The `𝔤𝔩_n` Casimir `Ω = ∑_{a,b} E_{ab} ⊗ E_{ba}` (trace form) on `V ⊗ V`. -/
def casimir2 : Matrix (Fin n × Fin n) (Fin n × Fin n) K :=
  ∑ a : Fin n, ∑ b : Fin n,
    Matrix.kroneckerMap (· * ·) (Matrix.single a b (1 : K)) (Matrix.single b a (1 : K))

/-- **The `𝔤𝔩_n` Casimir on `V ⊗ V` is the flip.** -/
theorem casimir_eq_flip : casimir2 K n = flip2 K n := by
  ext ⟨i, j⟩ ⟨k, l⟩
  simp only [casimir2, flip2, permMat, Matrix.sum_apply, Matrix.kroneckerMap_apply,
    single_apply', Matrix.of_apply, Prod.swap_prod_mk, Prod.mk.injEq]
  by_cases h1 : l = i <;> by_cases h2 : k = j <;>
    (simp [h1, h2, ite_and, eq_comm]; try exact fun h => h1 h.symm)

/-- The flip of the first two factors of `V^{⊗3}`. -/
def swap12 (x : Fin n × Fin n × Fin n) : Fin n × Fin n × Fin n := (x.2.1, x.1, x.2.2)

/-- The flip of the last two factors of `V^{⊗3}`. -/
def swap23 (x : Fin n × Fin n × Fin n) : Fin n × Fin n × Fin n := (x.1, x.2.2, x.2.1)

/-- `P₁₂` and `P₂₃` on `V^{⊗3}`. -/
def P12 : Matrix (Fin n × Fin n × Fin n) (Fin n × Fin n × Fin n) K := permMat K (swap12 n)
def P23 : Matrix (Fin n × Fin n × Fin n) (Fin n × Fin n × Fin n) K := permMat K (swap23 n)

theorem P12_mul_self : P12 K n * P12 K n = 1 :=
  permMat_mul_self K _ fun _ => rfl

theorem P23_mul_self : P23 K n * P23 K n = 1 :=
  permMat_mul_self K _ fun _ => rfl

/-- The coefficient sequence of `z · (A/z + B/(z−1)) = A − B ∑_{k≥1} z^k` at `z = 0`. -/
def kzM0 {R : Type*} [Ring R] (A B : R) : ℕ → R
  | 0 => A
  | _ + 1 => -B

/-- **The three-point `𝔤𝔩_n` KZ system has a unique normalised formal solution at `z = 0`**
(residue `A = ℏ P₁₂`) **and at `z = 1`** (residue `B = ℏ P₂₃`, after `w = 1 − z`, which swaps
the roles of `A` and `B`), whenever `ℏ` is not rational. -/
theorem kz_formal_solutions [CharZero K] (ℏ : K) (hℏ : ∀ r : ℚ, (r : K) ≠ ℏ) :
    (∃! H : ℕ → Matrix (Fin n × Fin n × Fin n) (Fin n × Fin n × Fin n) K,
        H 0 = 1 ∧ IsFormalGauge (kzM0 (ℏ • P12 K n) (ℏ • P23 K n)) H) ∧
    (∃! H : ℕ → Matrix (Fin n × Fin n × Fin n) (Fin n × Fin n × Fin n) K,
        H 0 = 1 ∧ IsFormalGauge (kzM0 (ℏ • P23 K n) (ℏ • P12 K n)) H) :=
  ⟨exists_unique_formalGauge _
      (nonResonant_smul_involution_of_irrational (K := K) _ (P12_mul_self K n) ℏ hℏ),
    exists_unique_formalGauge _
      (nonResonant_smul_involution_of_irrational (K := K) _ (P23_mul_self K n) ℏ hℏ)⟩

end GLn

end QOU.KZ.FuchsianFormal
