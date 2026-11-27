import HeckeTemperleyLieb.TLPositiveLoopCrossingTwist
import HeckeTemperleyLieb.TLVacuumRowFromJonesWenzl

/-!
# The first off-vacuum row of `S` from a Hopf link of Jones–Wenzl projectors

Bean `hkmt`. `TLVacuumRowFromJonesWenzl` gives the vacuum row `S_{0,j}`. This file gives the row
`S_{1,j}`: one strand linked once with the Jones–Wenzl projector `p_n` on `n + 1` strands.

* `hopfW δ A n`: in `TL_{n+1}` (`TLFin K δ n`), the pure braid in which the last strand goes once
  around the other `n`, written as the positive word `σ_{n−1} ⋯ σ₀ σ₀ ⋯ σ_{n−1}` in the
  positive-loop crossings `σᵢ = A − A⁻¹eᵢ` of `TLPositiveLoopCrossingTwist`.
* `hopf_trace`: for every `MarkovTower δ ε` with `δε = 1`, `δ = A² + A⁻²`,
  `δ^{n+2}·τ_{n+1}((p_n ⊗ 1)·hopfW_{n+1}) = [n+2]·(A^{2(n+2)} + A^{−2(n+2)})`, which is the
  quantum integer `[2(n+2)]` at `q = A²`. The two components have linking number one and no
  self-crossings, so there is no framing correction.
* `hopf_row_eq_sMatrix`: at `A = ω` with `ζ = ω²` a primitive `2(k+2)`-th root of unity this is
  the entry `S_{1,n+1}` of `TLRootOfUnity.sMatrix`.

The proof is a recursion through the Wenzl identity
`e_n·(p_n ⊗ 1)·e_n = ([n+2]/[n+1])·(p_{n−1} ⊗ 1 ⊗ 1)·e_n`; no topology is assumed.

No empirical input; everything is over an arbitrary field.

-- Ref: [jones1983] https://doi.org/10.1007/BF01389127
-/

namespace QOU.HeckeTemperleyLieb.TLHopfRow

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLPositiveLoop

variable {K : Type*} [Field K] {δ A : K}

/-! ## The Hopf word -/

/-- The letters of `σ_{n−1} ⋯ σ₀ σ₀ ⋯ σ_{n−1}`. -/
def hopfList : ∀ n : ℕ, List (Fin n)
  | 0 => []
  | n + 1 => Fin.last n :: ((hopfList n).map Fin.castSucc ++ [Fin.last n])

theorem hopfList_length : ∀ n, (hopfList n).length = 2 * n
  | 0 => rfl
  | n + 1 => by simp [hopfList, hopfList_length n]; ring

variable (δ A) in
/-- The last strand of `n + 1` going once around the other `n`. -/
noncomputable def hopfW (n : ℕ) : TLFin K δ n := ((hopfList n).map (crossing δ A)).prod

theorem incl_crossing {n : ℕ} (i : Fin n) :
    incl δ n (crossing δ A i) = crossing δ A (Fin.castSucc i) := by
  simp [crossing, map_sub, map_smul, incl_e]

theorem incl_word {n : ℕ} (w : List (Fin n)) :
    incl δ n ((w.map (crossing δ A)).prod) = ((w.map Fin.castSucc).map (crossing δ A)).prod := by
  rw [map_list_prod, List.map_map, List.map_map]
  congr 1
  exact List.map_congr_left (fun i _ => incl_crossing i)

theorem hopfW_succ (n : ℕ) :
    hopfW δ A (n + 1) =
      crossing δ A (Fin.last n) * incl δ n (hopfW δ A n) * crossing δ A (Fin.last n) := by
  simp only [hopfW, hopfList, incl_word, List.map_cons, List.map_append, List.prod_cons,
    List.prod_append, List.map_nil, List.prod_nil, mul_one, List.map_singleton,
    List.prod_singleton, mul_assoc]

/-! ## Absorption -/

theorem crossing_mul_jw {n : ℕ} (hS : JWSpec δ n) (i : Fin n) :
    crossing δ A i * jw δ n = A • jw δ n := by
  unfold crossing
  rw [sub_mul, smul_mul_assoc, one_mul, smul_mul_assoc, hS.2.1 i, smul_zero, sub_zero]

theorem word_mul_jw {n : ℕ} (hS : JWSpec δ n) (w : List (Fin n)) :
    (w.map (crossing δ A)).prod * jw δ n = A ^ w.length • jw δ n := by
  induction w with
  | nil => simp
  | cons a w ih =>
    rw [List.map_cons, List.prod_cons, mul_assoc, ih, mul_smul_comm, crossing_mul_jw hS, smul_smul,
      List.length_cons, pow_succ]

theorem jw_mul_hopfW {n : ℕ} (hS : JWSpec δ n) : jw δ n * hopfW δ A n = A ^ (2 * n) • jw δ n := by
  rw [hopfW, jw_mul_word hS, hopfList_length]

theorem hopfW_mul_jw {n : ℕ} (hS : JWSpec δ n) : hopfW δ A n * jw δ n = A ^ (2 * n) • jw δ n := by
  rw [hopfW, word_mul_jw hS, hopfList_length]

/-! ## The Wenzl identity with its witness named -/

variable (δ) in
/-- `Q₀ = 1`, `Q_{n+1} = p_n ⊗ 1`. -/
noncomputable def wQ : ∀ n : ℕ, TLFin K δ n
  | 0 => 1
  | n + 1 => incl δ n (jw δ n)

/-- `e_n·(p_n ⊗ 1)·e_n = ([n+2]/[n+1])·(Q_n ⊗ 1)·e_n`. -/
theorem e_jw_e : ∀ (n : ℕ), (∀ k ≤ n, qint δ (k + 1) ≠ 0) →
    e K δ adjFin (Fin.last n) * (incl δ n (jw δ n) * e K δ adjFin (Fin.last n)) =
      (qint δ (n + 2) / qint δ (n + 1)) • (incl δ n (wQ δ n) * e K δ adjFin (Fin.last n))
  | 0, _ => by
    simp only [jw, wQ, map_one, one_mul, e_sq']
    congr 1
    simp [qint]
  | n + 1, hg => by
    obtain ⟨-, -, hidem, -⟩ := jw_spec δ n (fun k hk => hg k (by omega))
    have h2 : qint δ (n + 2) ≠ 0 := hg (n + 1) le_rfl
    set P := jw δ n
    set c := qint δ (n + 1) / qint δ (n + 2)
    set g := e K δ adjFin (Fin.last n)
    set ιP := incl δ n P
    have hιPP : ιP * ιP = ιP := by rw [← map_mul, hidem]
    set g' := e K δ adjFin (Fin.last (n + 1))
    have hc : incl δ (n + 1) ιP * g' = g' * incl δ (n + 1) ιP := (incl_incl_commute δ n P).eq
    have hg' : incl δ (n + 1) g = e K δ adjFin (Fin.castSucc (Fin.last n)) := incl_e _ _ _
    have hA : g' * (incl δ (n + 1) ιP * g') = δ • (incl δ (n + 1) ιP * g') := by
      rw [hc, ← mul_assoc, e_sq', smul_mul_assoc]
    have hB : g' * (incl δ (n + 1) (ιP * g * ιP) * g') = incl δ (n + 1) ιP * g' := by
      rw [map_mul, map_mul, hg']
      calc g' * (incl δ (n + 1) ιP * e K δ adjFin (Fin.castSucc (Fin.last n))
              * incl δ (n + 1) ιP * g')
          = incl δ (n + 1) ιP * (g' * e K δ adjFin (Fin.castSucc (Fin.last n)) * g')
              * incl δ (n + 1) ιP := by
            simp only [mul_assoc]; rw [← mul_assoc g', ← hc, mul_assoc, hc]
        _ = incl δ (n + 1) ιP * g' := by
            rw [last_adj, mul_assoc, ← hc, ← mul_assoc, ← map_mul, hιPP]
    have hδc : δ - c = qint δ (n + 3) / qint δ (n + 2) := by
      rw [eq_div_iff h2, sub_mul,
        show qint δ (n + 3) = δ * qint δ (n + 2) - qint δ (n + 1) from rfl]
      simp only [c]
      rw [div_mul_cancel₀ _ h2]
    simp only [show n + 1 + 2 = n + 3 from rfl, show n + 1 + 1 = n + 2 from rfl, wQ]
    rw [jw_succ, map_sub, map_smul, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, hA, hB, ← hδc,
      sub_smul]

/-! ## The Hopf trace -/

variable {ε : K} (T : MarkovTower δ ε)

/-- **The Hopf link of one strand with `p_n`.** With `Q₀ = 1` and `Q_{n+1} = p_n ⊗ 1`,
`δ^{n+1}·τ_n(Q_n·hopfW_n) = [n+1]·(A^{2(n+1)} + A^{−2(n+1)})`. -/
theorem hopf_trace (hA : A ≠ 0) (hδ : δ = A ^ 2 + A⁻¹ ^ 2) (hε : δ * ε = 1) :
    ∀ n : ℕ, (∀ k < n, qint δ (k + 1) ≠ 0) →
      δ ^ (n + 1) * T.τ n (wQ δ n * hopfW δ A n) =
        qint δ (n + 1) * (A ^ (2 * (n + 1)) + A⁻¹ ^ (2 * (n + 1)))
  | 0, _ => by
    simp only [wQ, hopfW, hopfList, List.map_nil, List.prod_nil, mul_one, T.tr_one, qint_one,
      zero_add, pow_one, one_mul, mul_one, hδ]
  | n + 1, hg => by
    have hg' : ∀ k ≤ n, qint δ (k + 1) ≠ 0 := fun k hk => hg k (by omega)
    have hS := jw_spec δ n hg'
    have ih := hopf_trace hA hδ hε n (fun k hk => hg' k (by omega))
    have htj := tau_jw T hε n hg' (fun m hm => jw_spec δ m (fun k hk => hg' k (by omega)))
    have hkey := e_jw_e n hg'
    have h1 : qint δ (n + 1) ≠ 0 := hg' n le_rfl
    rw [hopfW_succ, show wQ δ (n + 1) = incl δ n (jw δ n) from rfl]
    set J := incl δ n (jw δ n)
    set M := incl δ n (hopfW δ A n)
    set g := e K δ adjFin (Fin.last n)
    set σ := crossing δ A (Fin.last n)
    have hσ : σ = A • 1 - A⁻¹ • g := rfl
    -- `τ(J σ M σ) = τ(σ J σ M)`
    have hcyc : T.τ (n + 1) (J * (σ * M * σ)) = T.τ (n + 1) (σ * J * σ * M) := by
      rw [show J * (σ * M * σ) = (J * σ * M) * σ by noncomm_ring, T.tr_comm]
      congr 1; noncomm_ring
    have hexp : σ * J * σ * M = (A ^ 2) • (J * M) - J * g * M - g * J * M +
        (A⁻¹ ^ 2) • (g * (J * g) * M) := by
      rw [hσ]
      have hAA : A * A⁻¹ = 1 := mul_inv_cancel₀ hA
      simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_sub,
        smul_smul]
      rw [show A⁻¹ * A = 1 by rw [mul_comm, hAA], hAA, one_smul, one_smul]
      simp only [mul_assoc, pow_two]
      abel
    have hJM : J * M = incl δ n (A ^ (2 * n) • jw δ n) := by
      simp only [J, M, ← map_mul, jw_mul_hopfW hS]
    have hMJ : M * J = incl δ n (A ^ (2 * n) • jw δ n) := by
      simp only [J, M, ← map_mul, hopfW_mul_jw hS]
    have t1 : T.τ (n + 1) (J * M) = A ^ (2 * n) * T.τ n (jw δ n) := by
      rw [hJM, T.tr_incl, map_smul, smul_eq_mul]
    have t2 : T.τ (n + 1) (J * g * M) = ε * (A ^ (2 * n) * T.τ n (jw δ n)) := by
      rw [T.tr_comm, ← mul_assoc, hMJ, T.tr_markov, map_smul, smul_eq_mul]
    have t3 : T.τ (n + 1) (g * J * M) = ε * (A ^ (2 * n) * T.τ n (jw δ n)) := by
      rw [mul_assoc, T.tr_comm, hJM, T.tr_markov, map_smul, smul_eq_mul]
    have t4 : T.τ (n + 1) (g * (J * g) * M) =
        (qint δ (n + 2) / qint δ (n + 1)) * (ε * T.τ n (wQ δ n * hopfW δ A n)) := by
      rw [hkey, smul_mul_assoc, map_smul, smul_eq_mul, T.tr_comm, ← mul_assoc, ← map_mul,
        T.tr_markov, T.tr_comm]
    rw [hcyc, hexp, map_add, map_sub,
      map_sub, map_smul, map_smul, smul_eq_mul, smul_eq_mul, t1, t2, t3, t4, htj]
    generalize T.τ n (wQ δ n * hopfW δ A n) = h at ih ⊢
    have hAA : A * A⁻¹ = 1 := mul_inv_cancel₀ hA
    have hq : qint δ (n + 2) / qint δ (n + 1) * qint δ (n + 1) = qint δ (n + 2) :=
      div_mul_cancel₀ _ h1
    have hpow : δ ^ (n + 1) * ε ^ (n + 1) = 1 := by rw [← mul_pow, hε, one_pow]
    simp only [show n + 1 + 1 = n + 2 from rfl]
    linear_combination (δ * A ^ (2 * n + 2) * qint δ (n + 2)
        - 2 * A ^ (2 * n) * qint δ (n + 2) * (δ * ε)) * hpow
      + (-2 * A ^ (2 * n) * qint δ (n + 2)
        + A⁻¹ ^ 2 * (qint δ (n + 2) / qint δ (n + 1)) * (δ ^ (n + 1) * h)) * hε
      + A⁻¹ ^ 2 * (qint δ (n + 2) / qint δ (n + 1)) * ih
      + A⁻¹ ^ 2 * (A ^ (2 * (n + 1)) + A⁻¹ ^ (2 * (n + 1))) * hq
      + A ^ (2 * n + 2) * qint δ (n + 2) * hδ
      + 2 * qint δ (n + 2) * A ^ (2 * n) * (A * A⁻¹ + 1) * hAA

/-! ## At a root of unity: the row `S_{1,j}` -/

section RootOfUnity

open QOU.HeckeTemperleyLieb.TLRootOfUnity QOU.HeckeTemperleyLieb.TLVacuumRow

theorem coe_sq_zpow (ω : Kˣ) (m : ℕ) : (((ω ^ 2) ^ (m : ℤ) : Kˣ) : K) = (ω : K) ^ (2 * m) := by
  rw [zpow_natCast, ← pow_mul, Units.val_pow_eq_pow_val]

theorem coe_sq_zpow_neg (ω : Kˣ) (m : ℕ) :
    (((ω ^ 2) ^ (-(m : ℤ)) : Kˣ) : K) = (ω : K)⁻¹ ^ (2 * m) := by
  rw [zpow_neg, zpow_natCast, ← pow_mul, Units.val_inv_eq_inv_val, Units.val_pow_eq_pow_val,
    inv_pow]

/-- `[2m] = [m]·(ζ^m + ζ^{−m})` with `ζ = ω²`. -/
theorem qInt_two_mul (ω : Kˣ) (k : ℕ) (hζ : IsPrimitiveRoot (ω ^ 2) (2 * (k + 2))) (m : ℕ) :
    qInt (ω ^ 2) (2 * m) = qInt (ω ^ 2) m * ((ω : K) ^ (2 * m) + (ω : K)⁻¹ ^ (2 * m)) := by
  apply mul_left_cancel₀ (qDelta_ne_zero k hζ)
  rw [qDelta_mul_qInt, ← mul_assoc, qDelta_mul_qInt, coe_sq_zpow, coe_sq_zpow_neg, coe_sq_zpow,
    coe_sq_zpow_neg]
  ring

/-- **The row `S_{1,j}` from braiding.** At `A = ω`, `ζ = ω²` a primitive `2(k+2)`-th root of
unity, for any Markov trace with `δε = 1`, the Hopf link of one strand with `p_n` on `n + 1 ≤ k`
strands is the `S`-matrix entry `S_{1,n+1} = [2(n+2)]`. -/
theorem hopf_row_eq_sMatrix (ω : Kˣ) (k : ℕ) (hζ : IsPrimitiveRoot (ω ^ 2) (2 * (k + 2)))
    {ε : K} (T : MarkovTower (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) ε)
    (hε : (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) * ε = 1) (n : ℕ) (hn : n + 1 ≤ k) :
    (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) ^ (n + 2) *
        T.τ (n + 1) (incl _ n (jw _ n) *
          hopfW (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) (ω : K) (n + 1)) =
      sMatrix (ω ^ 2) k ⟨1, by omega⟩ ⟨n + 1, by omega⟩ := by
  have hδ : ((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K) = (ω : K) ^ 2 + (ω : K)⁻¹ ^ 2 := by
    rw [Units.val_inv_eq_inv_val, Units.val_pow_eq_pow_val, inv_pow]
  have hg : ∀ j < n + 1, qint (((ω ^ 2 : Kˣ) : K) + (((ω ^ 2)⁻¹ : Kˣ) : K)) (j + 1) ≠ 0 :=
    fun j hj => by rw [qint_eq_qInt]; exact qInt_ne_zero k hζ (by omega) (by omega)
  have h := hopf_trace T ω.ne_zero hδ hε (n + 1) hg
  rw [show wQ _ (n + 1) = incl _ n (jw _ n) from rfl] at h
  rw [h, qint_eq_qInt]
  simp only [sMatrix]
  rw [show (1 + 1) * (n + 1 + 1) = 2 * (n + 1 + 1) by ring, qInt_two_mul ω k hζ]

end RootOfUnity

end QOU.HeckeTemperleyLieb.TLHopfRow
