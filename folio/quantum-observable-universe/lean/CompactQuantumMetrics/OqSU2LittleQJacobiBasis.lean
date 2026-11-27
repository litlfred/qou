import CompactQuantumMetrics.OqSU2CartanPairingNondegenerate
import Mathlib.RingTheory.Polynomial.Basic

/-!
# The little q-Jacobi eigenbasis exhausts the Cartan block

Thread "Audit the q-Bessel special-function dictionary" (2026-11-27). The owner asked for a
Lean proof that the sphere harmonics are **exhaustive**. On the Cartan (torus-biinvariant)
block `K[ζ]`, `ζ = βγ`, the q-Casimir `L = X₊X₋` acts lower-bidiagonally
(`lap_zeta_pow`). This file proves that its eigenpolynomials, the little q-Jacobi polynomials,
form a basis of `K[ζ]`, and that they are an orthogonal basis for the Haar pairing with
**nonzero** norms.

## Results (over a field `K`, `q : Kˣ`, `p = q²` not a root of unity)

* `Lp`: the operator `L` transported to `K[X]`, with `ev_Lp : ev (Lp P) = L (ev P)`.
* `lam n = [n]_{q⁻²} [n+1]_{q²}`: the diagonal of `L` (`lam_zero : lam 0 = 0`).
* `lam_mul_eq`: `lam k · (p − 1)² · p^k = p (p^k − 1)(p^{k+1} − 1)`.
* `lam_injective_of_not_root`: the eigenvalues are pairwise distinct.
* `charPoly_annihilates`: `Π_{k ≤ m} (L − lam k)` kills every polynomial of degree `≤ m`
  (the triangular Cayley–Hamilton step).
* `jacobiPoly n := Π_{k < n} (L − lam k) (X^n)`, with
  - `Lp_jacobiPoly`: `L p_n = lam n · p_n`,
  - `jacobiPoly_mem`, `coeff_jacobiPoly`: `deg p_n ≤ n` and the `X^n` coefficient is
    `Π_{k<n} (lam n − lam k) ≠ 0`.
* `jacobiPoly_span`: **the `p_n` span `K[X]`**. Every element of the Cartan block is a finite
  combination of little q-Jacobi polynomials. This is the exhaustiveness statement.
* `haarState_jacobiPoly_orthogonal`: `h(p_m p_n) = 0` for `m ≠ n`.
* `haarState_jacobiPoly_sq_ne_zero`: `h(p_n²) ≠ 0`.

So on the Cartan block the little q-Jacobi polynomials are a complete orthogonal system with
nonzero norms, and the q-NS budget `h(X₊a · X₋a) = −q⁻² Σ_n lam_n c_n² h(p_n²)`
(`OqSU2BudgetLittleQJacobi`) is a genuine diagonalisation.

## Not established

* Positivity of `h(p_n²)` over an ordered field (#9646 has `h(a*a) ≥ 0`).
* The `q`-Bessel contraction limit (`E_q(2)`, Koelink 1994): analytic, outside this file.
* The other weight blocks: their pairing reduces to this one; see
  `QOU/FluidDynamics/q_ns_block_pairing_nondegenerate.lean`.

Everything is algebraic. No empirical value enters any proof. Sorry-free.
-/

namespace QOU.AlgebraicSubstrate.OqSU2

open Polynomial Finset

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

/-! ## The operator on `K[X]` -/

/-- Diagonal entry `lam k = [k]_{q⁻²} [k+1]_{q²}`. -/
noncomputable def lam (k : ℕ) : K := jk (qi * qi) k * jk ((q : K) * q) (k + 1)

/-- Subdiagonal entry of `L ζ^{k+1}`. -/
noncomputable def subd (k : ℕ) : K := jk (qi * qi) (k + 1) * ((q : K) * jk ((q : K) * q) (k + 1))

theorem lam_zero : lam q 0 = 0 := by simp [lam, jk]

/-- `L` on `X^n`. -/
noncomputable def lapX : ℕ → K[X]
  | 0 => 0
  | k + 1 => C (subd q k) * X ^ k + C (lam q (k + 1)) * X ^ (k + 1)

/-- `L` transported to `K[X]`. -/
noncomputable def Lp : K[X] →ₗ[K] K[X] :=
  lsum fun n => LinearMap.smulRight LinearMap.id (lapX q n)

theorem Lp_monomial (n : ℕ) (c : K) : Lp q (monomial n c) = c • lapX q n := by
  simp [Lp, lsum_apply, sum_monomial_index]

theorem Lp_X_pow (n : ℕ) : Lp q (X ^ n) = lapX q n := by
  rw [← monomial_one_right_eq_X_pow, Lp_monomial, one_smul]

theorem ev_lapX (n : ℕ) : ev q (lapX q n) = lap q (zetaB q ^ n) := by
  cases n with
  | zero => simp [lapX, lap_one]
  | succ k =>
    rw [lap_zeta_pow, lapX, map_add, map_mul, map_mul, map_pow, map_pow]
    simp only [ev, aeval_C, aeval_X, Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul,
      lam, subd]

/-- `ev ∘ Lp = L ∘ ev`. -/
theorem ev_Lp (P : K[X]) : ev q (Lp q P) = lap q (ev q P) := by
  induction P using Polynomial.induction_on' with
  | add P₁ P₂ h₁ h₂ => simp only [map_add, h₁, h₂]
  | monomial n c => rw [Lp_monomial, map_smul, ev_lapX, ev_monomial, map_smul]

/-! ## Triangularity -/

theorem CX_mem (a : K) {j n : ℕ} (h : j < n) : C a * X ^ j ∈ degreeLT K n := by
  rw [mem_degreeLT]
  exact (degree_C_mul_X_pow_le j a).trans_lt (by exact_mod_cast h)

theorem X_pow_mem {j n : ℕ} (h : j < n) : (X ^ j : K[X]) ∈ degreeLT K n := by
  simpa using CX_mem (1 : K) h

theorem lapX_mem (k : ℕ) : lapX q k ∈ degreeLT K (k + 1) := by
  cases k with
  | zero => simp [lapX]
  | succ k =>
    exact Submodule.add_mem _ (CX_mem _ (by omega)) (CX_mem _ (by omega))

/-- `(L − lam m)` maps degree `≤ m` into degree `< m`. -/
theorem Lp_sub_mem (m : ℕ) {P : K[X]} (hP : P ∈ degreeLT K (m + 1)) :
    Lp q P - lam q m • P ∈ degreeLT K m := by
  classical
  let M : K[X] →ₗ[K] K[X] := Lp q - lam q m • LinearMap.id
  have hM : ∀ R, M R = Lp q R - lam q m • R := fun R => rfl
  suffices h : degreeLT K (m + 1) ≤ (degreeLT K m).comap M by
    have := h hP; rwa [Submodule.mem_comap, hM] at this
  rw [degreeLT_eq_span_X_pow, Submodule.span_le]
  intro x hx
  simp only [coe_image, coe_range, Set.mem_image, Set.mem_Iio] at hx
  obtain ⟨k, hk, rfl⟩ := hx
  rw [SetLike.mem_coe, Submodule.mem_comap, hM, Lp_X_pow]
  rcases Nat.lt_or_ge k m with hkm | hkm
  · exact Submodule.sub_mem _ ((degreeLT_mono hkm) (lapX_mem q k))
      (Submodule.smul_mem _ _ (X_pow_mem hkm))
  · have hk' : k = m := by omega
    subst hk'
    cases k with
    | zero => simp [lapX, lam_zero]
    | succ j =>
      have : lapX q (j + 1) - lam q (j + 1) • X ^ (j + 1) = C (subd q j) * X ^ j := by
        rw [lapX, smul_eq_C_mul]; ring
      rw [this]; exact CX_mem _ (by omega)

theorem eq_zero_of_mem_degreeLT_zero {P : K[X]} (h : P ∈ degreeLT K 0) : P = 0 := by
  rw [mem_degreeLT, Nat.cast_zero] at h
  by_contra hP
  exact absurd h (not_lt.mpr (zero_le_degree_iff.mpr hP))

/-- `L − a` as an endomorphism: `aeval Lp (X − C a)`. -/
theorem aeval_X_sub_C_apply (a : K) (P : K[X]) :
    aeval (Lp q) (X - C a) P = Lp q P - a • P := by
  simp [Algebra.algebraMap_eq_smul_one]

/-- `Π_{k ≤ m} (X − lam k)`. -/
noncomputable def charPoly (m : ℕ) : K[X] := ∏ k ∈ range (m + 1), (X - C (lam q k))

/-- **Triangular Cayley–Hamilton.** `Π_{k ≤ m}(L − lam k)` kills degree `≤ m`. -/
theorem charPoly_annihilates (m : ℕ) {P : K[X]} (hP : P ∈ degreeLT K (m + 1)) :
    aeval (Lp q) (charPoly q m) P = 0 := by
  induction m generalizing P with
  | zero =>
    have := Lp_sub_mem q 0 hP
    rw [charPoly, prod_range_one, aeval_X_sub_C_apply]
    exact eq_zero_of_mem_degreeLT_zero this
  | succ m ih =>
    rw [charPoly, prod_range_succ, map_mul, Module.End.mul_apply, aeval_X_sub_C_apply]
    exact ih (Lp_sub_mem q (m + 1) hP)

/-- `(L − a)` keeps degree `≤ m` and scales the `X^m` coefficient by `lam m − a`. -/
theorem Lp_sub_coeff (m : ℕ) (a : K) {P : K[X]} (hP : P ∈ degreeLT K (m + 1)) :
    Lp q P - a • P ∈ degreeLT K (m + 1) ∧
      (Lp q P - a • P).coeff m = (lam q m - a) * P.coeff m := by
  have h1 := Lp_sub_mem q m hP
  have hsplit : Lp q P - a • P = (Lp q P - lam q m • P) + (lam q m - a) • P := by
    rw [sub_smul]; abel
  refine ⟨?_, ?_⟩
  · rw [hsplit]
    exact Submodule.add_mem _ (degreeLT_mono (Nat.le_succ m) h1) (Submodule.smul_mem _ _ hP)
  · rw [hsplit, coeff_add, coeff_smul, smul_eq_mul]
    have : (Lp q P - lam q m • P).coeff m = 0 :=
      coeff_eq_zero_of_degree_lt ((mem_degreeLT.mp h1).trans_le le_rfl)
    rw [this, zero_add]

/-! ## The eigenpolynomials -/

/-- The little q-Jacobi polynomial `p_n = Π_{k<n} (L − lam k) X^n`. -/
noncomputable def jacobiPoly (n : ℕ) : K[X] :=
  aeval (Lp q) (∏ k ∈ range n, (X - C (lam q k))) (X ^ n)

theorem jacobiPoly_aux (n j : ℕ) :
    aeval (Lp q) (∏ k ∈ range j, (X - C (lam q k))) (X ^ n) ∈ degreeLT K (n + 1) ∧
      (aeval (Lp q) (∏ k ∈ range j, (X - C (lam q k))) (X ^ n)).coeff n =
        ∏ k ∈ range j, (lam q n - lam q k) := by
  induction j with
  | zero => simp [X_pow_mem (Nat.lt_succ_self n)]
  | succ j ih =>
    rw [prod_range_succ, mul_comm, map_mul, Module.End.mul_apply, aeval_X_sub_C_apply,
      prod_range_succ]
    obtain ⟨h1, h2⟩ := Lp_sub_coeff q n (lam q j) ih.1
    exact ⟨h1, by rw [h2, ih.2, mul_comm]⟩

theorem jacobiPoly_mem (n : ℕ) : jacobiPoly q n ∈ degreeLT K (n + 1) := (jacobiPoly_aux q n n).1

theorem coeff_jacobiPoly (n : ℕ) :
    (jacobiPoly q n).coeff n = ∏ k ∈ range n, (lam q n - lam q k) := (jacobiPoly_aux q n n).2

/-- **Eigen-equation.** `L p_n = lam n · p_n`. -/
theorem Lp_jacobiPoly (n : ℕ) : Lp q (jacobiPoly q n) = lam q n • jacobiPoly q n := by
  have h := charPoly_annihilates q n (X_pow_mem (K := K) (Nat.lt_succ_self n))
  rw [charPoly, prod_range_succ, mul_comm, map_mul, Module.End.mul_apply,
    aeval_X_sub_C_apply] at h
  exact sub_eq_zero.mp h

/-! ## Distinct eigenvalues -/

theorem lam_mul_eq (k : ℕ) :
    lam q k * ((q : K) * q - 1) ^ 2 * ((q : K) * q) ^ k =
      (q : K) * q * (((q : K) * q) ^ k - 1) * (((q : K) * q) ^ (k + 1) - 1) := by
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  have hA := jk_mul_sub_one (qi * qi) k
  have hB := jk_mul_sub_one ((q : K) * q) (k + 1)
  have hqi : qi * (q : K) = 1 := by simp
  have hr : (qi * qi) ^ k * ((q : K) * q) ^ k = 1 := by
    rw [← mul_pow]; rw [show qi * qi * ((q : K) * q) = (qi * q) * (qi * q) by ring, hqi]; simp
  have hrp : (qi * qi) * ((q : K) * q) = 1 := by
    rw [show qi * qi * ((q : K) * q) = (qi * q) * (qi * q) by ring, hqi, one_mul]
  have hA' : jk (qi * qi) k * ((q : K) * q) ^ k * ((q : K) * q - 1) =
      (q : K) * q * (((q : K) * q) ^ k - 1) := by
    linear_combination (-(((q : K) * q) ^ (k + 1))) * hA +
      (jk (qi * qi) k * ((q : K) * q) ^ k) * hrp + (-((q : K) * q)) * hr
  unfold lam
  linear_combination ((q : K) * q - 1) * jk ((q : K) * q) (k + 1) * hA' +
    ((q : K) * q * (((q : K) * q) ^ k - 1)) * hB

theorem lam_injective_of_not_root (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1)
    {k n : ℕ} (hkn : k < n) : lam q n ≠ lam q k := by
  intro heq
  set p : K := (q : K) * q
  have hq0 : (q : K) ≠ 0 := q.ne_zero
  have hp0 : p ≠ 0 := mul_ne_zero hq0 hq0
  have hp1 : p - 1 ≠ 0 := fun h0 => hp 0 (by rw [zero_add, pow_one]; exact sub_eq_zero.mp h0)
  obtain ⟨d, rfl⟩ := Nat.exists_eq_add_of_lt hkn
  have en := lam_mul_eq q (k + d + 1)
  have ek := lam_mul_eq q k
  set u := p ^ k
  set v := p ^ (d + 1)
  have hu : p ^ (k + d + 1) = u * v := by rw [add_assoc, pow_add]
  have hu1 : p ^ (k + d + 1 + 1) = p * u * v := by rw [pow_succ, hu]; ring
  have hk1 : p ^ (k + 1) = p * u := by rw [pow_succ]; ring
  rw [hu, hu1] at en
  rw [hk1] at ek
  have hu0 : u ≠ 0 := pow_ne_zero _ hp0
  have key : p * ((v - 1) * (p * u ^ 2 * v - 1)) = 0 := by
    rw [heq] at en
    linear_combination (-1 : K) * en + v * ek
  have hv : v - 1 ≠ 0 := fun h0 => hp d (sub_eq_zero.mp h0)
  have hw : p * u ^ 2 * v - 1 ≠ 0 := by
    intro h0
    have : p ^ (2 * k + d + 1 + 1) = 1 := by
      have e : p ^ (2 * k + d + 1 + 1) = p * u ^ 2 * v := by
        simp only [u, v]; ring
      rw [e]; exact sub_eq_zero.mp h0
    exact hp _ this
  exact mul_ne_zero hp0 (mul_ne_zero hv hw) key

theorem coeff_jacobiPoly_ne_zero (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) (n : ℕ) :
    (jacobiPoly q n).coeff n ≠ 0 := by
  rw [coeff_jacobiPoly, prod_ne_zero_iff]
  intro k hk
  exact sub_ne_zero.mpr (lam_injective_of_not_root q hp (mem_range.mp hk))

/-! ## Exhaustiveness -/

/-- **The little q-Jacobi polynomials span `K[X]`.** -/
theorem jacobiPoly_span (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) :
    Submodule.span K (Set.range (jacobiPoly q)) = ⊤ := by
  classical
  set S := Submodule.span K (Set.range (jacobiPoly q))
  have hlt : ∀ n, degreeLT K n ≤ S := by
    intro n
    induction n with
    | zero => intro P hP; rw [eq_zero_of_mem_degreeLT_zero hP]; exact S.zero_mem
    | succ n ih =>
      rw [degreeLT_eq_span_X_pow, Submodule.span_le]
      intro x hx
      simp only [coe_image, coe_range, Set.mem_image, Set.mem_Iio] at hx
      obtain ⟨k, hk, rfl⟩ := hx
      rcases Nat.lt_or_ge k n with hkn | hkn
      · exact ih (X_pow_mem hkn)
      · have hk' : k = n := by omega
        subst hk'
        set c := (jacobiPoly q k).coeff k
        have hc : c ≠ 0 := coeff_jacobiPoly_ne_zero q hp k
        have hrest : jacobiPoly q k - c • X ^ k ∈ degreeLT K k := by
          rw [mem_degreeLT, degree_lt_iff_coeff_zero]
          intro m hm
          have hmem := mem_degreeLT.mp (jacobiPoly_mem q k)
          rcases Nat.lt_or_ge k m with h | h
          · rw [coeff_sub, coeff_smul, coeff_X_pow, if_neg (by omega), smul_zero, sub_zero]
            exact coeff_eq_zero_of_degree_lt (hmem.trans_le (by exact_mod_cast h))
          · have : m = k := by omega
            subst this
            rw [coeff_sub, coeff_smul, coeff_X_pow, if_pos rfl, smul_eq_mul, mul_one, sub_self]
        have hx : (X ^ k : K[X]) = c⁻¹ • (jacobiPoly q k - (jacobiPoly q k - c • X ^ k)) := by
          rw [sub_sub_cancel, smul_smul, inv_mul_cancel₀ hc, one_smul]
        rw [SetLike.mem_coe, hx]
        exact S.smul_mem _ (S.sub_mem (Submodule.subset_span ⟨k, rfl⟩) (ih hrest))
  rw [eq_top_iff]
  intro P _
  exact hlt (P.natDegree + 1)
    (mem_degreeLT.mpr (degree_le_natDegree.trans_lt (by exact_mod_cast Nat.lt_succ_self _)))

/-! ## Orthogonality with nonzero norms -/

theorem lap_ev_jacobiPoly (n : ℕ) :
    lap q (ev q (jacobiPoly q n)) = lam q n • ev q (jacobiPoly q n) := by
  rw [← ev_Lp, Lp_jacobiPoly, map_smul]

theorem haarState_jacobiPoly_orthogonal (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1)
    {m n : ℕ} (hmn : m ≠ n) :
    haarState q (ev q (jacobiPoly q m) * ev q (jacobiPoly q n)) = 0 := by
  have hq : ∀ n, qSqNum q n ≠ 0 := qSqNum_ne_zero_of_not_root q hp
  refine haarState_eigen_orthogonal q hq (lap_ev_jacobiPoly q m) (lap_ev_jacobiPoly q n) ?_
  rcases Nat.lt_or_gt_of_ne hmn with h | h
  · exact (lam_injective_of_not_root q hp h).symm
  · exact lam_injective_of_not_root q hp h

/-- **Nonzero norms.** `h(p_n²) ≠ 0`. -/
theorem haarState_jacobiPoly_sq_ne_zero (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1) (n : ℕ) :
    haarState q (ev q (jacobiPoly q n) * ev q (jacobiPoly q n)) ≠ 0 := by
  intro h0
  have hall : ∀ Q : K[X], haarState q (ev q (jacobiPoly q n) * ev q Q) = 0 := by
    intro Q
    have hQ : Q ∈ Submodule.span K (Set.range (jacobiPoly q)) := by
      rw [jacobiPoly_span q hp]; trivial
    induction hQ using Submodule.span_induction with
    | mem x hx =>
      obtain ⟨m, rfl⟩ := hx
      by_cases hmn : n = m
      · subst hmn; exact h0
      · exact haarState_jacobiPoly_orthogonal q hp hmn
    | zero => simp
    | add x y _ _ hx hy => rw [map_add, mul_add, map_add, hx, hy, add_zero]
    | smul a x _ hx => rw [map_smul, mul_smul_comm, map_smul, hx, smul_zero]
  have hz := cartan_pairing_nondegenerate' q hp _ hall
  exact coeff_jacobiPoly_ne_zero q hp n (by rw [hz, coeff_zero])

end QOU.AlgebraicSubstrate.OqSU2
