import QOU.Nuclear.IsospinCasimirTwist

/-!
# `QOU.Nuclear.IsospinTwistWrithe` — the `A`-scaling of the braid-channel `T(T+1)` term

Follow-up to `QOU.Nuclear.IsospinCasimirTwist` (PR #9685), gap **G2** of the term-completeness
ledger (bean `qou-tcl2`, epic `qou-myts`).  That file proves that the Murphy product
`Φ = L_0 ⋯ L_n ∈ H_{n+1}(q)` acts on every block by `q^{2c(λ)}`, and that on a two-row block
`c = T(T+1) + N(N−4)/4` (`N = n + 1` strands).  Wiring `Φ` itself into the mass table (#9706)
gives a term `κ·T(T+1)` with no `1/A`.

This file answers *where a `1/A` can come from* without inserting one by hand.  The answer is
the **writhe**: every multiplicative invariant of a block sees a braid word only through its
exponent sum, and `Φ` is a word of `N(N−1)` letters.

## What is proved (no hypothesis beyond `q · qi = 1`, and genericity of `q` for §3)

1. `chi_σ_eq` — for **any** monoid hom `χ : H_{n+1}(q) →* M` into a commutative monoid, `χ`
   takes the same value on every generator `σ_i`.  (Braid relation `aba = bab` in a
   commutative monoid with `a, b` units forces `a = b`.)
2. `chi_qJM`, `chi_murphyProd_full` — `χ(L_k) = a^{2k}`, hence `χ(Φ) = a^{n(n+1)} = a^{N(N−1)}`,
   `a = χ(σ_0)`.  This uses only the definition `L_{k+1} = σ_k L_k σ_k`; the identity
   `Φ = Δ²` (cited in #9685) is **not** needed.
3. `chi_word` — for every word `w` of the free group on the generators, sent to `H_{n+1}(q)ˣ`,
   `χ(w) = a^{e(w)}`, where `e(w) ∈ ℤ` is the **writhe** (exponent sum).
4. `seminormal_det_word_pow` — on the seminormal block `ρ_μ` of dimension `d = #SYT(μ)`,
   with `χ = det ∘ ρ_μ`:

       det ρ_μ(w) ^ (N(N−1)) = (q^{2c(μ)})^{d · e(w)}          (stated for e(w) ≥ 0;
                                                              `chi_word` covers every e ∈ ℤ)
5. `perLetter_twoRow` — the per-letter, per-dimension exponent of `q` on a two-row block is

       2c / (N(N−1))  =  2T(T+1)/(N(N−1))  +  (N−4)/(2(N−1)).

   So a word of writhe `e` carries `e·2T(T+1)/(N(N−1))` on `T(T+1)`: the coefficient is the
   **writhe over `N(N−1)`**.  The `n`-only part `e(N−4)/(2(N−1))` is extensive when `e ∝ N`.
6. `chain_coeff_bounds` — for the chain word of the ruled law (`e = A − 1` bond letters at
   `N = 3A`) the `T(T+1)` coefficient `2(A−1)/(3A(3A−1))` lies between `1/(9A)` and `2/(9A)`
   for every `A ≥ 2`: it is `Θ(1/A)`.  `fullTwist_coeff` — for the full twist `e = N(N−1)` it
   is `2`, independent of `A`, which is #9706.

## What this does NOT settle

* **Which word.**  The writhe of the nucleus word is the word axis (gap G5).  The ruled law's
  chain has `A − 1` bond letters; their signs are not derived here.  The nucleon core
  `V³ = (σ_0 σ_1⁻¹)³` has writhe `0`, so under this reading it carries no `T(T+1)`.
* **Which block functional.**  §3–§5 use the block log-determinant (the sum of
  `ln|eigenvalue|` over the block), which is what the log law computes block by block.  A
  different functional of a non-central word (for example the largest eigenvalue) need not
  factor through the writhe.
* **Energies.**  No `ln`, no energy scale and no measured value appears.  The probe
  `computations/probes/isospin_twist_writhe_scaling_probe.py` carries the result through the
  #9706 energy map, as a comparison only.

Refs: [murphy1992]; [ram1997] Theorem 4.1; [kassel-turaev2008] §1 (exponent sum as the
abelianisation `B_n → ℤ`).
-/

namespace QOU.Nuclear.IsospinTwistWrithe

open QOU.SchurWeyl QOU.SchurWeyl.Hecke QOU.SchurWeyl.SeminormalRep
open TableauCells
open QOU.Nuclear.IsospinCasimirTwist
open QOU.Mathlib (StandardYoungTableau)

/-! ## 1. A multiplicative map sees one value on all generators -/

section Character

variable {K : Type*} [CommRing K] {q qi : K} {n : ℕ} {M : Type*} [CommMonoid M]

/-- Neighbouring generators have the same image under any multiplicative map. -/
theorem chi_σ_succ (χ : Hecke K q qi n →* M) (hqi : q * qi = 1) (i : Fin n)
    (hi : (i : ℕ) + 1 < n) :
    χ (σ K q qi n ⟨(i : ℕ) + 1, hi⟩) = χ (σ K q qi n i) := by
  have hb := congrArg χ (σ_braid K q qi n i hi)
  simp only [map_mul] at hb
  set a := χ (σ K q qi n i)
  set b := χ (σ K q qi n ⟨(i : ℕ) + 1, hi⟩)
  have ha : IsUnit a := (isUnit_σ K q qi n hqi i).map χ
  have hb' : IsUnit b := (isUnit_σ K q qi n hqi _).map χ
  -- a b a = b a b  ⇒  (a b) a = (a b) b  ⇒  a = b
  have h2 : (a * b) * a = (a * b) * b := by
    calc (a * b) * a = a * b * a := rfl
      _ = b * a * b := hb
      _ = (a * b) * b := by ac_rfl
  exact ((ha.mul hb').mul_left_cancel h2).symm

/-- Every generator has the image of `σ_0`. -/
theorem chi_σ_eq_zero (χ : Hecke K q qi n →* M) (hqi : q * qi = 1) (h0 : 0 < n) :
    ∀ (k : ℕ) (hk : k < n), χ (σ K q qi n ⟨k, hk⟩) = χ (σ K q qi n ⟨0, h0⟩)
  | 0, _ => rfl
  | k + 1, hk => by
      rw [chi_σ_succ χ hqi ⟨k, by omega⟩ hk]
      exact chi_σ_eq_zero χ hqi h0 k (by omega)

/-- **All generators have one image** under a multiplicative map. -/
theorem chi_σ_eq (χ : Hecke K q qi n →* M) (hqi : q * qi = 1) (i j : Fin n) :
    χ (σ K q qi n i) = χ (σ K q qi n j) := by
  have h0 : 0 < n := Nat.lt_of_le_of_lt (Nat.zero_le _) i.isLt
  rw [chi_σ_eq_zero χ hqi h0 i i.isLt, chi_σ_eq_zero χ hqi h0 j j.isLt]

/-! ## 2. The Murphy product is a word of `N(N−1)` letters -/

/-- `χ(L_k) = a^{2k}` for `k ≤ n`, where `a = χ(σ_0)`. -/
theorem chi_qJM (χ : Hecke K q qi n →* M) (hqi : q * qi = 1) (h0 : 0 < n) :
    ∀ k : ℕ, k ≤ n → χ (qJM K q qi n k) = χ (σ K q qi n ⟨0, h0⟩) ^ (2 * k)
  | 0, _ => by simp
  | k + 1, hk => by
      rw [qJM_succ K q qi n (by omega : k < n), map_mul, map_mul,
        chi_qJM χ hqi h0 k (by omega), chi_σ_eq_zero χ hqi h0 k (by omega), ← pow_succ',
        ← pow_succ]
      congr 1

/-- `χ(L_0 ⋯ L_k) = a^{k(k+1)}` for `k ≤ n`. -/
theorem chi_murphyProd (χ : Hecke K q qi n →* M) (hqi : q * qi = 1) (h0 : 0 < n) :
    ∀ k : ℕ, k ≤ n → χ (murphyProd K q qi n k) = χ (σ K q qi n ⟨0, h0⟩) ^ (k * (k + 1))
  | 0, _ => by simp [murphyProd_zero]
  | k + 1, hk => by
      rw [murphyProd_succ, map_mul, chi_murphyProd χ hqi h0 k (by omega),
        chi_qJM χ hqi h0 (k + 1) hk, ← pow_add]
      congr 1
      ring

/-- **The Murphy product has `N(N−1)` letters** (`N = n + 1`):  `χ(Φ) = a^{n(n+1)}`. -/
theorem chi_murphyProd_full (χ : Hecke K q qi n →* M) (hqi : q * qi = 1) (h0 : 0 < n) :
    χ (murphyProd K q qi n n) = χ (σ K q qi n ⟨0, h0⟩) ^ (n * (n + 1)) :=
  chi_murphyProd χ hqi h0 n le_rfl

/-! ## 3. Any braid word is seen through its writhe -/

/-- The writhe (exponent sum) of a word in the generators. -/
def writhe {n : ℕ} : FreeGroup (Fin n) →* Multiplicative ℤ :=
  FreeGroup.lift (fun _ => Multiplicative.ofAdd 1)

/-- The Hecke image of a braid word (the generators go to the units `σ_i`). -/
noncomputable def heckeWord (hqi : q * qi = 1) : FreeGroup (Fin n) →* (Hecke K q qi n)ˣ :=
  FreeGroup.lift (σUnit K q qi n hqi)

/-- **A multiplicative map sees a word only through its writhe:**
`χ(w) = a^{e(w)}` in `Mˣ`, with `a = χ(σ_i)` for any `i`. -/
theorem chi_word (χ : Hecke K q qi n →* M) (hqi : q * qi = 1) (i : Fin n)
    (w : FreeGroup (Fin n)) :
    Units.map χ (heckeWord hqi w)
      = ((isUnit_σ K q qi n hqi i).map χ).unit ^ (Multiplicative.toAdd (writhe w)) := by
  set u := ((isUnit_σ K q qi n hqi i).map χ).unit
  have : (Units.map χ).comp (heckeWord (K := K) (q := q) (qi := qi) hqi)
      = (zpowersHom Mˣ u).comp writhe := by
    ext j
    simp only [MonoidHom.comp_apply, heckeWord, writhe, FreeGroup.lift_apply_of,
      zpowersHom_apply, toAdd_ofAdd, zpow_one, Units.coe_map, σUnit]
    simp only [u, IsUnit.unit_spec]
    exact chi_σ_eq χ hqi j i
  exact DFunLike.congr_fun this w

end Character

/-! ## 4. On a seminormal block: `det ρ(w)^{N(N−1)} = (q^{2c})^{d·e}` -/

section Block

variable {K : Type*} [Field K] {μ : YoungDiagram}

/-- The block determinant as a multiplicative map. -/
noncomputable def blockDet (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (n : ℕ) (hN : μ.cells.card = n + 1) : Hecke K q q⁻¹ n →* K :=
  (Matrix.detMonoidHom).comp (seminormalRep q hq0 hq2 n hN).toMonoidHom

theorem blockDet_apply (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (n : ℕ) (hN : μ.cells.card = n + 1) (x : Hecke K q q⁻¹ n) :
    blockDet q hq0 hq2 n hN x = (seminormalRep q hq0 hq2 n hN x).det := rfl

/-- **Per-letter block determinant.**  `det ρ_μ(σ_i)^{n(n+1)} = (q^{2c(μ)})^{d}`,
`d = #SYT(μ)`: the `N(N−1)` letters of `Φ` share its block scalar equally. -/
theorem seminormal_det_σ_pow (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (n : ℕ) (hN : μ.cells.card = n + 1) (i : Fin n) :
    (seminormalRep q hq0 hq2 n hN (σ K q q⁻¹ n i)).det ^ (n * (n + 1))
      = (q ^ (2 * ∑ c ∈ μ.cells, cellContent c)) ^ Fintype.card (StandardYoungTableau μ) := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq0
  have h0 : 0 < n := Nat.lt_of_le_of_lt (Nat.zero_le _) i.isLt
  have h := chi_murphyProd_full (blockDet q hq0 hq2 n hN) hqi h0
  rw [blockDet_apply, seminormalRep_murphyProd_scalar q hq0 hq2 n hN, Matrix.det_smul,
    Matrix.det_one, mul_one] at h
  rw [← blockDet_apply, chi_σ_eq (blockDet q hq0 hq2 n hN) hqi i ⟨0, h0⟩, ← h]

/-- **A word of writhe `e ≥ 0` on a block:** `det ρ_μ(w)^{N(N−1)} = (q^{2c})^{d·e}`. -/
theorem seminormal_det_word_pow (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ) (hN : μ.cells.card = n + 1) (h0 : 0 < n)
    (w : FreeGroup (Fin n)) (e : ℕ) (he : Multiplicative.toAdd (writhe w) = (e : ℤ)) :
    (seminormalRep q hq0 hq2 n hN (heckeWord (mul_inv_cancel₀ hq0) w : Hecke K q q⁻¹ n)).det
        ^ (n * (n + 1))
      = (q ^ (2 * ∑ c ∈ μ.cells, cellContent c))
          ^ (Fintype.card (StandardYoungTableau μ) * e) := by
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq0
  have h := congrArg Units.val (chi_word (blockDet q hq0 hq2 n hN) hqi ⟨0, h0⟩ w)
  rw [he, zpow_natCast, Units.val_pow_eq_pow_val, IsUnit.unit_spec, Units.coe_map] at h
  have h' : (blockDet q hq0 hq2 n hN) (heckeWord hqi w : Hecke K q q⁻¹ n)
      = (blockDet q hq0 hq2 n hN (σ K q q⁻¹ n ⟨0, h0⟩)) ^ e := h
  rw [← blockDet_apply, h', ← pow_mul, mul_comm e, pow_mul, blockDet_apply,
    seminormal_det_σ_pow q hq0 hq2 n hN ⟨0, h0⟩, ← pow_mul]

end Block

/-! ## 5. Per-letter exponent on a two-row block -/

/-- **Per-letter, per-dimension exponent of `q` on the two-row block** of `N` strands and
isospin `T = t/2`: with `4c = t(t+2) + N(N−4)` (`four_contentSum_twoRow`),

    2c / (N(N−1)) = 2T(T+1)/(N(N−1)) + (N−4)/(2(N−1)).

Written with `t = 2T`, so `2T(T+1) = t(t+2)/2`. -/
theorem perLetter_twoRow (N t c : ℚ) (hN : N * (N - 1) ≠ 0) (hN1 : N - 1 ≠ 0)
    (hc : 4 * c = t * (t + 2) + N * (N - 4)) :
    2 * c / (N * (N - 1)) = t * (t + 2) / 2 / (N * (N - 1)) + (N - 4) / (2 * (N - 1)) := by
  have hN0 : N ≠ 0 := by
    intro h; apply hN; simp [h]
  have hc' : c = (t * (t + 2) + N * (N - 4)) / 4 := by linarith
  subst hc'
  field_simp
  ring

/-- **`T(T+1)` coefficient of a word of writhe `e`**, in powers of `q` per block dimension. -/
def ttCoeff (N e : ℚ) : ℚ := 2 * e / (N * (N - 1))

/-- The full twist (`e = N(N−1)`) has coefficient `2`, independent of `N`: this is #9706. -/
theorem fullTwist_coeff (N : ℚ) (hN : N * (N - 1) ≠ 0) : ttCoeff N (N * (N - 1)) = 2 := by
  unfold ttCoeff; rw [mul_div_assoc, div_self hN, mul_one]

/-- **The chain word is `Θ(1/A)`.**  With `e = A − 1` bond letters on `N = 3A` strands, the
`T(T+1)` coefficient lies in `[1/(9A), 2/(9A)]` for every `A ≥ 2`. -/
theorem chain_coeff_bounds (A : ℚ) (hA : 2 ≤ A) :
    1 / (9 * A) ≤ ttCoeff (3 * A) (A - 1) ∧ ttCoeff (3 * A) (A - 1) ≤ 2 / (9 * A) := by
  unfold ttCoeff
  have hA0 : 0 < A := by linarith
  have hden : 0 < 3 * A * (3 * A - 1) := by nlinarith
  have h9 : 0 < 9 * A := by linarith
  constructor
  · rw [div_le_div_iff₀ h9 hden]; nlinarith
  · rw [div_le_div_iff₀ hden h9]; nlinarith

/-- `A · coeff → 2/9` from below: for the chain word, `A · ttCoeff(3A, A−1) = 2(A−1)/(3(3A−1))`. -/
theorem chain_coeff_mul_A (A : ℚ) (hA : 2 ≤ A) :
    A * ttCoeff (3 * A) (A - 1) = 2 * (A - 1) / (3 * (3 * A - 1)) := by
  unfold ttCoeff
  have hA0 : A ≠ 0 := by intro h; linarith
  have h3 : 3 * A - 1 ≠ 0 := by intro h; linarith
  field_simp

/-- Non-vacuity at `A = 2` (`²H`, `N = 6`, one bond): coefficient `2/30 = 1/15`. -/
example : ttCoeff (3 * 2) (2 - 1) = 1 / 15 := by norm_num [ttCoeff]

end QOU.Nuclear.IsospinTwistWrithe

