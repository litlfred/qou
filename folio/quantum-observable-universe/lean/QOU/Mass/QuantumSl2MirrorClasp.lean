import QOU.Mass.QuantumSl2MirrorConj

/-!
# The mirror clasp and van der Veen's `C(n, t⁻¹)`

Stage 4d-iii of the derivation of Zheng's tangle formula (van der Veen 2008, Lemma 1). The
mirror clasp is the clasp with its crossings reversed:

    X̄ = (cap ⊗ 1 ⊗ 1)(1 ⊗ M⁻¹ ⊗ 1)(1 ⊗ 1 ⊗ cup)     on `V_{m+1} ⊗ V_{m+1}`.

We show it acts on the summand `V_{2n+1}` (`n = m − j`) by `claspSc` at `s⁻¹`, i.e. by van der
Veen's `C(n, t⁻¹)` before the framing factor and up to the sign `(−1)^{N−1}` from the cup and
cap (`claspBar_strVec`). The proof:

* `claspWith Y` is the clasp with any middle operator `Y`; it commutes with `Δ(E)`, `Δ(F)` when
  `Y` commutes with `Δ(E)`, `Δ(F)`, `Δ(K^{±1})`. With `Y = M⁻¹ = D P M(s⁻¹) P D⁻¹`
  (`monoBar_eq_inv`) this holds, so `X̄` fixes each highest-weight line.
* Its scalar on `w_j` is read off at the output `v_0 ⊗ v_j`. There the inner `Ř` meets the row
  `v_{m−c} ⊗ v_0` of `S`, which is a unit row, so each summand is a single product
  (`mono_mirror_entry`). Its closed form is van der Veen's term `vdvTerm s⁻¹ (j−c) c n`
  (`mirrorTerm_eq_vdvTerm`), and reflecting the sum gives `claspSc` at `s⁻¹`.

Finally the trace of `T^a B^b X^c X̄^d` is Zheng's sum (`trace_twist_belt_clasp_mirror`).

All statements are over a generic field `𝕜`.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1 and its proof
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

section ClaspWith

variable (q : 𝕜) (m : ℕ)
  (Y : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)

/-- `1 ⊗ Y ⊗ 1` in the middle two slots. -/
def midWith :
    Matrix ((Fin (m + 1) × Fin (m + 1)) × (Fin (m + 1) × Fin (m + 1)))
      ((Fin (m + 1) × Fin (m + 1)) × (Fin (m + 1) × Fin (m + 1))) 𝕜 :=
  ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ
    (Y ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜))).submatrix (regroup m) (regroup m)

/-- The clasp with middle operator `Y`: `(cap ⊗ 1 ⊗ 1)(1 ⊗ Y ⊗ 1)(1 ⊗ 1 ⊗ cup)`. -/
def claspWith : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  (cap4 q m * midWith m Y * cup4 q m).submatrix (Equiv.punitProd _).symm (Equiv.prodPUnit _).symm

theorem clasp_eq_claspWith (s : 𝕜) (hs : s ≠ 0) :
    clasp s hs m = claspWith (s ^ 2) m (mono s hs m m) := rfl

variable {q m Y}

theorem claspWith_deltaE (hq : q ≠ 0) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)
    (hK : Y * deltaK q m m = deltaK q m m * Y) (hE : Y * deltaE q m m = deltaE q m m * Y) :
    claspWith q m Y * deltaE q m m = deltaE q m m * claspWith q m Y := by
  have hc : ∀ p < m, qint q (m - p) ≠ 0 := fun p hp => hint (m - p) (by omega) (by omega)
  have hmid : midWith m Y * delta4E q m = delta4E q m * midWith m Y := by
    have h : ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ
          (Y ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜))) * delta4E' q m
        = delta4E' q m * ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ
          (Y ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜))) := by
      unfold delta4E'
      simp only [mul_add, add_mul, ← mul_kronecker_mul, one_mul, mul_one, hK, hE]
    unfold midWith
    rw [delta4E_regroup, ← submatrix_mul _ _ _ _ _ (regroup m).bijective,
      ← submatrix_mul _ _ _ _ _ (regroup m).bijective, h]
  have hbig : (cap4 q m * midWith m Y * cup4 q m) * (deltaE q m m ⊗ₖ (1 : Matrix Unit Unit 𝕜))
      = ((1 : Matrix Unit Unit 𝕜) ⊗ₖ deltaE q m m) * (cap4 q m * midWith m Y * cup4 q m) := by
    simp only [Matrix.mul_assoc]
    rw [← delta4E_cup4 q hq m hc, ← Matrix.mul_assoc (midWith m Y), hmid, Matrix.mul_assoc,
      ← Matrix.mul_assoc (cap4 q m), cap4_delta4E q hq m hint, Matrix.mul_assoc]
  have h1 : deltaE q m m = (deltaE q m m ⊗ₖ (1 : Matrix Unit Unit 𝕜)).submatrix
      (Equiv.prodPUnit _).symm (Equiv.prodPUnit _).symm := by
    ext a b; simp
  have h2 : deltaE q m m = ((1 : Matrix Unit Unit 𝕜) ⊗ₖ deltaE q m m).submatrix
      (Equiv.punitProd _).symm (Equiv.punitProd _).symm := by
    ext a b; simp
  unfold claspWith
  conv_lhs => rw [h1]
  conv_rhs => rw [h2]
  rw [← submatrix_mul _ _ _ _ _ (Equiv.prodPUnit _).symm.bijective,
    ← submatrix_mul _ _ _ _ _ (Equiv.punitProd _).symm.bijective, hbig]

theorem claspWith_deltaF (hq : q ≠ 0) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)
    (hK : Y * deltaKm q m m = deltaKm q m m * Y) (hF : Y * deltaF q m m = deltaF q m m * Y) :
    claspWith q m Y * deltaF q m m = deltaF q m m * claspWith q m Y := by
  have hc : ∀ p < m, qint q (m - p) ≠ 0 := fun p hp => hint (m - p) (by omega) (by omega)
  have hmid : midWith m Y * delta4F q m = delta4F q m * midWith m Y := by
    have h : ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ
          (Y ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜))) * delta4F' q m
        = delta4F' q m * ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ
          (Y ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜))) := by
      unfold delta4F'
      simp only [mul_add, add_mul, ← mul_kronecker_mul, one_mul, mul_one, one_kronecker_one,
        hK, hF]
    unfold midWith
    rw [delta4F_regroup, ← submatrix_mul _ _ _ _ _ (regroup m).bijective,
      ← submatrix_mul _ _ _ _ _ (regroup m).bijective, h]
  have hbig : (cap4 q m * midWith m Y * cup4 q m) * (deltaF q m m ⊗ₖ (1 : Matrix Unit Unit 𝕜))
      = ((1 : Matrix Unit Unit 𝕜) ⊗ₖ deltaF q m m) * (cap4 q m * midWith m Y * cup4 q m) := by
    simp only [Matrix.mul_assoc]
    rw [← delta4F_cup4 q hq m hc, ← Matrix.mul_assoc (midWith m Y), hmid, Matrix.mul_assoc,
      ← Matrix.mul_assoc (cap4 q m), cap4_delta4F q hq m hint, Matrix.mul_assoc]
  have h1 : deltaF q m m = (deltaF q m m ⊗ₖ (1 : Matrix Unit Unit 𝕜)).submatrix
      (Equiv.prodPUnit _).symm (Equiv.prodPUnit _).symm := by
    ext a b; simp
  have h2 : deltaF q m m = ((1 : Matrix Unit Unit 𝕜) ⊗ₖ deltaF q m m).submatrix
      (Equiv.punitProd _).symm (Equiv.punitProd _).symm := by
    ext a b; simp
  unfold claspWith
  conv_lhs => rw [h1]
  conv_rhs => rw [h2]
  rw [← submatrix_mul _ _ _ _ _ (Equiv.prodPUnit _).symm.bijective,
    ← submatrix_mul _ _ _ _ _ (Equiv.punitProd _).symm.bijective, hbig]

/-- Coordinates of `claspWith`. -/
theorem claspWith_apply (f g c d : Fin (m + 1)) :
    claspWith q m Y (f, g) (c, d)
      = ∑ e : Fin (m + 1), ∑ p : Fin (m + 1),
          capVec q m (c, e) * Y (e, f) (d, p) * cupVec q m (p, g) := by
  simp only [claspWith, cap4, midWith, cup4, capRow, cupCol, regroup, submatrix_apply,
    Equiv.coe_fn_mk, mul_apply, kroneckerMap_apply, of_apply, one_apply, Fintype.sum_prod_type,
    Equiv.punitProd_symm_apply, Equiv.prodPUnit_symm_apply, Prod.mk.injEq, ite_and, mul_ite,
    ite_mul, mul_one, one_mul, mul_zero, zero_mul, Finset.sum_ite_eq',
    Finset.mem_univ, if_true]
  simp only [Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_ite_eq, Finset.sum_ite_eq',
    Finset.mem_univ, if_true, Finset.sum_mul, ite_mul, zero_mul]
  rw [Finset.sum_comm]

theorem claspWith_grade
    (hY : ∀ x y : Fin (m + 1) × Fin (m + 1), (x.1 : ℕ) + x.2 ≠ y.1 + y.2 → Y x y = 0)
    (x y : Fin (m + 1) × Fin (m + 1)) (h : (x.1 : ℕ) + x.2 ≠ y.1 + y.2) :
    claspWith q m Y x y = 0 := by
  obtain ⟨f, g⟩ := x
  obtain ⟨c, d⟩ := y
  rw [claspWith_apply]
  refine Finset.sum_eq_zero fun e _ => Finset.sum_eq_zero fun p _ => ?_
  unfold capVec cupVec hwVec
  by_cases h1 : (c : ℕ) + e = m
  · by_cases h2 : (p : ℕ) + g = m
    · rw [hY _ _ (by dsimp only at h ⊢; omega)]; simp
    · simp [h2]
  · simp [h1]

/-- The `c`-th summand of `claspWith Y` at output `v_0 ⊗ v_j` on `w_j`. -/
theorem claspWith_hw_row0 (j : ℕ) (hj : j ≤ m) (c : Fin (m + 1)) :
    ∑ d : Fin (m + 1), claspWith q m Y (⟨0, by omega⟩, ⟨j, by omega⟩) (c, d) * hwVec q m m j (c, d)
      = if h : (c : ℕ) ≤ j then
          hwCoef q m m j c * capCoefQ q m c * hwCoef q m m m (m - j)
            * Y (⟨m - c, by omega⟩, ⟨0, by omega⟩) (⟨j - c, by omega⟩, ⟨m - j, by omega⟩)
        else 0 := by
  split_ifs with hc
  · have hd : ∀ d : Fin (m + 1), d ≠ ⟨j - c, by omega⟩ →
        claspWith q m Y (⟨0, by omega⟩, ⟨j, by omega⟩) (c, d) * hwVec q m m j (c, d) = 0 := by
      intro d hd
      have : (c : ℕ) + d ≠ j := fun h => hd (Fin.ext (by simp only; omega))
      simp [hwVec, this]
    have he : ∀ e : Fin (m + 1), e ≠ ⟨m - c, by omega⟩ →
        ∑ p : Fin (m + 1), capVec q m (c, e) * Y (e, ⟨0, by omega⟩) (⟨j - c, by omega⟩, p)
          * cupVec q m (p, ⟨j, by omega⟩) = 0 := by
      intro e he
      have : (c : ℕ) + e ≠ m := fun h => he (Fin.ext (by simp only; omega))
      simp [capVec, this]
    have hp : ∀ p : Fin (m + 1), p ≠ ⟨m - j, by omega⟩ →
        capVec q m (c, ⟨m - c, by omega⟩) * Y (⟨m - c, by omega⟩, ⟨0, by omega⟩) (⟨j - c, by omega⟩, p)
          * cupVec q m (p, ⟨j, by omega⟩) = 0 := by
      intro p hp
      have : (p : ℕ) + j ≠ m := fun h => hp (Fin.ext (by simp only; omega))
      simp [cupVec, hwVec, this]
    rw [Fintype.sum_eq_single _ hd, claspWith_apply, Fintype.sum_eq_single _ he,
      Fintype.sum_eq_single _ hp]
    simp only [capVec, cupVec, hwVec,
      if_pos (show (c : ℕ) + (m - c) = m by omega),
      if_pos (show m - j + j = m by omega), if_pos (show (c : ℕ) + (j - c) = j by omega)]
    ring
  · refine Finset.sum_eq_zero fun d _ => ?_
    simp [hwVec, show ¬ ((c : ℕ) + d = j) by omega]

end ClaspWith

section MirrorEntry

variable (s : 𝕜) (hs : s ≠ 0)

/-- The row of `S` at `v_p ⊗ v_0` is the unit row (`F` never lands on `v_0`). -/
theorem rSum_apply_row0 (m m' M : ℕ) (p : Fin (m + 1)) (x : Fin (m + 1) × Fin (m' + 1)) :
    Rep.rSum s (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m') M (p, ⟨0, by omega⟩) x
      = if x = (p, ⟨0, by omega⟩) then 1 else 0 := by
  unfold Rep.rSum
  rw [Matrix.sum_apply, Finset.sum_eq_single 0]
  · simp only [Matrix.smul_apply, kroneckerMap_apply, pow_zero, one_apply, smul_eq_mul]
    have hc : rcoef s 0 = 1 := by simp [rcoef, qfact]
    rw [hc, one_mul]
    by_cases hx : x = (p, ⟨0, by omega⟩)
    · subst hx; simp
    · rw [if_neg hx]
      by_cases h1 : p = x.1
      · have h2 : (⟨0, by omega⟩ : Fin (m' + 1)) ≠ x.2 := by
          intro h2; apply hx; rw [h1, h2]
        rw [if_pos h1, if_neg h2, mul_zero]
      · rw [if_neg h1, zero_mul]
  · intro n _ hn
    rw [Matrix.smul_apply, kroneckerMap_apply,
      show (irrep (pow_ne_zero 2 hs) m').F = irrepF (s ^ 2) m' from rfl,
      irrepF_pow_apply (s ^ 2) m' n _ x.2 (by simp; omega), mul_zero, smul_zero]
  · simp

/-- **The mirror entry of the monodromy**, a single product:
`M_{(0, m−c),(m−j, j−c)} = s^{wt(m−c) wt(0)} s^{wt(0) wt(m−c)} c_{m−j} (E^{m−j})_{0,m−j}
(F^{m−j})_{m−c,j−c}`. -/
theorem mono_mirror_entry (m j c : ℕ) (hcj : c ≤ j) (hjm : j ≤ m) :
    mono s hs m m (⟨0, by omega⟩, ⟨m - c, by omega⟩) (⟨m - j, by omega⟩, ⟨j - c, by omega⟩)
      = s ^ (wt m (m - c) * wt m 0) * s ^ (wt m 0 * wt m (m - c)) * rcoef s (m - j)
        * (irrepE (s ^ 2) m ^ (m - j)) ⟨0, by omega⟩ ⟨m - j, by omega⟩
        * (irrepF (s ^ 2) m ^ (m - j)) ⟨m - c, by omega⟩ ⟨j - c, by omega⟩ := by
  unfold mono
  rw [mul_apply, Finset.sum_eq_single (⟨m - c, by omega⟩, ⟨0, by omega⟩)]
  · unfold rCheckMat rMat cartanTheta
    simp only [submatrix_apply, diagonal_mul, Prod.swap, id]
    rw [rSum_apply_row0 s hs m m _ _ (⟨m - c, by omega⟩, ⟨0, by omega⟩), if_pos rfl, mul_one]
    unfold Rep.rSum
    rw [Matrix.sum_apply, Finset.sum_eq_single (m - j)]
    · simp only [Matrix.smul_apply, kroneckerMap_apply, smul_eq_mul]
      rw [show (irrep (pow_ne_zero 2 hs) m).E = irrepE (s ^ 2) m from rfl,
        show (irrep (pow_ne_zero 2 hs) m).F = irrepF (s ^ 2) m from rfl]
      ring
    · intro n _ hn
      rw [Matrix.smul_apply, kroneckerMap_apply,
        show (irrep (pow_ne_zero 2 hs) m).E = irrepE (s ^ 2) m from rfl,
        irrepE_pow_apply (s ^ 2) m n _ _ (by simp; omega), zero_mul, smul_zero]
    · intro h; exfalso; exact h (Finset.mem_range.mpr (by unfold rOrder; omega))
  · intro z _ hz
    unfold rCheckMat rMat cartanTheta
    simp only [submatrix_apply, diagonal_mul, id, Prod.swap]
    rw [rSum_apply_row0 s hs m m _ _ z, if_neg, mul_zero, zero_mul]
    intro h; apply hz; rw [h]
  · simp

theorem qfact_inv (q : 𝕜) (n : ℕ) : qfact q⁻¹ n = qfact q n := by
  unfold qfact
  exact Finset.prod_congr rfl fun i _ => qint_inv q (i + 1)

/-- The mirror entry of `M⁻¹ = D P M(s⁻¹) P D⁻¹`. -/
theorem monoBar_mirror_entry (m j c : ℕ) (hcj : c ≤ j) (hjm : j ≤ m) :
    monoBar s hs m (⟨m - c, by omega⟩, ⟨0, by omega⟩) (⟨j - c, by omega⟩, ⟨m - j, by omega⟩)
      = (s⁻¹) ^ (wt m (m - c) * wt m 0) * (s⁻¹) ^ (wt m 0 * wt m (m - c)) * rcoef s⁻¹ (m - j)
        * (irrepE (s ^ 2) m ^ (m - j)) ⟨0, by omega⟩ ⟨m - j, by omega⟩
        * (irrepF (s ^ 2) m ^ (m - j)) ⟨m - c, by omega⟩ ⟨j - c, by omega⟩
        / (s ^ 2) ^ (2 * ((j - c : ℕ) : ℤ) * ((m - j : ℕ) : ℤ)) := by
  unfold monoBar conjM dw
  simp only [Prod.swap_prod_mk]
  rw [mono_mirror_entry s⁻¹ (inv_ne_zero hs) m j c hcj hjm, inv_pow s 2, irrepE_inv, irrepF_inv]
  simp only [Nat.cast_zero, mul_zero, zpow_zero]
  ring

include hs in
/-- **The mirror clasp term is van der Veen's term at `s⁻¹`.** The `c`-th summand of
`cap (1 ⊗ M⁻¹ ⊗ 1) cup` read at `v_0 ⊗ v_j` on `w_j` is `vdvTerm s⁻¹ (j−c) c (m−j)`. -/
theorem mirrorTerm_eq_vdvTerm (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (m j c : ℕ) (hcj : c ≤ j)
    (hjm : j ≤ m) (hint : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0) :
    hwCoef (s ^ 2) m m j c * capCoefQ (s ^ 2) m c * hwCoef (s ^ 2) m m m (m - j)
      * monoBar s hs m (⟨m - c, by omega⟩, ⟨0, by omega⟩) (⟨j - c, by omega⟩, ⟨m - j, by omega⟩)
      = vdvTerm s⁻¹ (j - c) c (m - j) := by
  obtain ⟨k, rfl⟩ : ∃ k, j = c + k := ⟨j - c, by omega⟩
  obtain ⟨n, rfl⟩ : ∃ n, m = c + k + n := ⟨m - (c + k), by omega⟩
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hf := qfact_ne_zero' s (c + k + n) hint
  have hfm := hf (c + k + n) le_rfl
  have hfn := hf n (by omega)
  have hfk := hf k (by omega)
  have hfc := hf c (by omega)
  have hfck := hf (c + k) (by omega)
  have hfkn := hf (k + n) (by omega)
  have hfnc := hf (n + c) (by omega)
  have hf0 : qfact (s ^ 2) 0 = 1 := by simp [qfact]
  rw [monoBar_mirror_entry s hs (c + k + n) (c + k) c (by omega) (by omega)]
  have hE : (irrepE (s ^ 2) (c + k + n) ^ (c + k + n - (c + k))) ⟨0, by omega⟩
      ⟨c + k + n - (c + k), by omega⟩ = qfact (s ^ 2) (c + k + n) / qfact (s ^ 2) (c + k) := by
    rw [irrepE_pow_entry _ _ _ _ _ (by simp), eq_div_iff hfck]
    have hd := qfact_mul_prod_down (s ^ 2) (c + k + n) n (by omega)
    rw [show c + k + n - n = c + k by omega] at hd
    rw [← hd, show c + k + n - (c + k) = n by omega, mul_comm]
    exact congrArg _ (Finset.prod_congr rfl (fun l _ => by congr 1))
  have hF : (irrepF (s ^ 2) (c + k + n) ^ (c + k + n - (c + k))) ⟨c + k + n - c, by omega⟩
      ⟨c + k - c, by omega⟩ = qfact (s ^ 2) (k + n) / qfact (s ^ 2) k := by
    rw [irrepF_pow_entry _ _ _ _ _ (by simp; omega), eq_div_iff hfk]
    have hu := qfact_mul_prod_up (s ^ 2) k n
    rw [← hu, show c + k + n - (c + k) = n by omega, mul_comm]
    exact congrArg _ (Finset.prod_congr rfl (fun l _ => by congr 1; simp))
  rw [hE, hF]
  have h1 : hwCoef (s ^ 2) (c + k + n) (c + k + n) (c + k) c
      = (-1) ^ c * (s ^ (2 * (c * k)) / s ^ (2 * (c * (n + 1)))) * qfact (s ^ 2) (k + n)
        * qfact (s ^ 2) (n + c) / (qfact (s ^ 2) (c + k + n) * qfact (s ^ 2) n) := by
    have h := hwCoef_closed (s ^ 2) hq (c + k + n) (c + k) c (by omega) (by omega)
      (fun i hi => hint _ (by omega) (by omega))
    rw [show c + k + n - (c + k) = n by omega, show c + k + n - c = k + n by omega,
      sq_zpow_split s hs _ (c * k) (c * (n + 1))] at h
    · rw [eq_div_iff (mul_ne_zero hfm hfn), ← h]; ring
    · push_cast; ring
  have h3 : hwCoef (s ^ 2) (c + k + n) (c + k + n) (c + k + n) c
      = (-1) ^ c * (s ^ (2 * (c * (k + n))) / s ^ (2 * c)) * qfact (s ^ 2) (k + n)
        * qfact (s ^ 2) c / qfact (s ^ 2) (c + k + n) := by
    have h := hwCoef_closed (s ^ 2) hq (c + k + n) (c + k + n) c (by omega) le_rfl
      (fun i hi => hint _ (by omega) (by omega))
    rw [Nat.sub_self, zero_add, hf0, mul_one, show c + k + n - c = k + n by omega,
      sq_zpow_split s hs _ (c * (k + n)) c] at h
    · rw [eq_div_iff hfm, h]
    · push_cast; ring
  have h4 : hwCoef (s ^ 2) (c + k + n) (c + k + n) (c + k + n) n
      = (-1) ^ n * (s ^ (2 * (n * (c + k))) / s ^ (2 * n)) * qfact (s ^ 2) (c + k)
        * qfact (s ^ 2) n / qfact (s ^ 2) (c + k + n) := by
    have h := hwCoef_closed (s ^ 2) hq (c + k + n) (c + k + n) n (by omega) le_rfl
      (fun i hi => hint _ (by omega) (by omega))
    rw [Nat.sub_self, zero_add, hf0, mul_one, show c + k + n - n = c + k by omega,
      sq_zpow_split s hs _ (n * (c + k)) n] at h
    · rw [eq_div_iff hfm, h]
    · push_cast; ring
  have hcap : (s ^ 2) ^ (((c + k + n : ℕ) : ℤ) - 2 * (c : ℤ)) = s ^ (2 * (k + n)) / s ^ (2 * c) :=
    sq_zpow_split s hs _ _ _ (by push_cast; ring)
  have hdw : (s ^ 2) ^ (2 * ((k : ℕ) : ℤ) * ((n : ℕ) : ℤ)) = s ^ (2 * (2 * k * n)) / s ^ (2 * 0) :=
    sq_zpow_split s hs _ _ _ (by push_cast; ring)
  have ht1 : s⁻¹ ^ (wt (c + k + n) (k + n) * wt (c + k + n) 0)
      = s⁻¹ ^ (c * c) / s⁻¹ ^ ((k + n) * (k + n)) :=
    s_zpow_split s⁻¹ (inv_ne_zero hs) _ _ _ (by unfold wt; push_cast; ring)
  have ht2 : s⁻¹ ^ (wt (c + k + n) 0 * wt (c + k + n) (k + n))
      = s⁻¹ ^ (c * c) / s⁻¹ ^ ((k + n) * (k + n)) :=
    s_zpow_split s⁻¹ (inv_ne_zero hs) _ _ _ (by unfold wt; push_cast; ring)
  rw [show c + k + n - (c + k) = n by omega, show c + k - c = k by omega,
    show c + k + n - c = k + n by omega, h1, h4, hdw, ht1, ht2,
    vdvTerm_closed s⁻¹ (inv_ne_zero hs) (hq2_inv s hq2) k c n
      (hint_inv s (k + c + n) (fun i h1 h2 => hint i h1 (by omega)))]
  unfold capCoefQ rcoef
  rw [h3, hcap]
  have hnn : s ^ (n * (n - 1)) = s ^ (n * n) / s ^ n := by
    rcases n with _ | n
    · simp
    · rw [eq_div_iff (pow_ne_zero _ hs), ← pow_add]; congr 1
  simp only [inv_pow, inv_inv, qfact_inv]
  rw [hnn, show (s ^ 2)⁻¹ - s ^ 2 = -(s ^ 2 - (s ^ 2)⁻¹) by ring,
    neg_pow (s ^ 2 - (s ^ 2)⁻¹) n, show n + k = k + n from add_comm _ _,
    show c + n = n + c from add_comm _ _,
    show ((-1 : 𝕜)) ^ (c + k + n) = (-1) ^ k * (-1) ^ c * (-1) ^ n by ring,
    show ((-1 : 𝕜)) ^ (k + c) = (-1) ^ k * (-1) ^ c from pow_add _ _ _]
  generalize s ^ 2 - (s ^ 2)⁻¹ = X
  generalize qfact (s ^ 2) (k + n) = A at hfkn
  generalize qfact (s ^ 2) (n + c) = B at hfnc
  generalize qfact (s ^ 2) (c + k + n) = C at hfm
  generalize qfact (s ^ 2) (c + k) = G at hfck
  generalize hD : qfact (s ^ 2) n = D at hfn
  generalize qfact (s ^ 2) k = E at hfk
  generalize qfact (s ^ 2) c = F at hfc
  rcases Nat.even_or_odd k with hk | hk <;> rcases Nat.even_or_odd c with ha | ha <;>
    rcases Nat.even_or_odd n with hn | hn <;>
    rw [hk.neg_one_pow, ha.neg_one_pow, hn.neg_one_pow] <;> field_simp <;> ring

end MirrorEntry

/-! ### The mirror clasp is scalar on each summand -/

section MirrorEigen

variable (s : 𝕜) (hs : s ≠ 0) (m : ℕ)

/-- **The mirror clasp** `(cap ⊗ 1 ⊗ 1)(1 ⊗ M⁻¹ ⊗ 1)(1 ⊗ 1 ⊗ cup)` on `V_{m+1} ⊗ V_{m+1}`,
with `M⁻¹` written as `D P M(s⁻¹) P D⁻¹`. -/
def claspBar : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  claspWith (s ^ 2) m (monoBar s hs m)

theorem monoBar_grade (x y : Fin (m + 1) × Fin (m + 1)) (h : (x.1 : ℕ) + x.2 ≠ y.1 + y.2) :
    monoBar s hs m x y = 0 := by
  unfold monoBar conjM
  rw [mono_grade s⁻¹ (inv_ne_zero hs) m m x.swap y.swap
    (by simp only [Prod.fst_swap, Prod.snd_swap]; omega), mul_zero]

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (hint : ∀ i, 0 < i → i ≤ 2 * m → qint (s ^ 2) i ≠ 0)

include hq2 hint in
/-- The mirror clasp is the clasp with `M⁻¹` in the middle. -/
theorem claspBar_eq : claspBar s hs m = claspWith (s ^ 2) m (mono s hs m m)⁻¹ := by
  rw [monoBar_eq_inv s hs m hq2 hint]; rfl

include hq2 hint in
/-- **The mirror clasp acts on `w_j` by `claspSc` at `s⁻¹`**, van der Veen's `C(m−j, t⁻¹)`
before the framing factor. -/
theorem claspBar_hwVec (j : ℕ) (hj : j ≤ m) :
    claspBar s hs m *ᵥ hwVec (s ^ 2) m m j = claspSc s⁻¹ m j • hwVec (s ^ 2) m m j := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hm : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0 := fun i h1 h2 => hint i h1 (by omega)
  have hint' : ∀ p < j, qint (s ^ 2) (m - p) ≠ 0 := fun p hp => hm _ (by omega) (by omega)
  have hE : deltaE (s ^ 2) m m *ᵥ (claspBar s hs m *ᵥ hwVec (s ^ 2) m m j) = 0 := by
    rw [mulVec_mulVec, claspBar, ← claspWith_deltaE hq hm (monoBar_deltaK s hs m hq2 hint)
      (monoBar_deltaE s hs m hq2 hint), ← mulVec_mulVec]
    rw [show deltaE (s ^ 2) m m *ᵥ hwVec (s ^ 2) m m j = 0 from
      hwVec_E (s ^ 2) hq m m j hj hj hint', mulVec_zero]
  have hsupp : ∀ x : Fin (m + 1) × Fin (m + 1), (x.1 : ℕ) + x.2 ≠ j →
      (claspBar s hs m *ᵥ hwVec (s ^ 2) m m j) x = 0 := by
    intro x hx
    simp only [mulVec, dotProduct]
    refine Finset.sum_eq_zero fun y _ => ?_
    by_cases hy : (y.1 : ℕ) + y.2 = j
    · rw [claspBar, claspWith_grade (monoBar_grade s hs m) x y (by omega), zero_mul]
    · simp [hwVec, hy]
  have hu := hw_unique (s ^ 2) hq m m j hj hint' _ hsupp hE
  rw [hu]
  congr 1
  rw [show (claspBar s hs m *ᵥ hwVec (s ^ 2) m m j) (⟨0, by omega⟩, ⟨j, by omega⟩)
      = ∑ c : Fin (m + 1), ∑ d : Fin (m + 1),
          claspWith (s ^ 2) m (monoBar s hs m) (⟨0, by omega⟩, ⟨j, by omega⟩) (c, d)
            * hwVec (s ^ 2) m m j (c, d) by
    simp only [claspBar, mulVec, dotProduct, Fintype.sum_prod_type]]
  simp only [claspWith_hw_row0 j hj]
  rw [Finset.sum_congr rfl (g := fun c : Fin (m + 1) =>
      if (c : ℕ) ≤ j then vdvTerm s⁻¹ (j - c) c (m - j) else 0) (fun c _ => by
    dsimp only
    split_ifs with hc
    · exact mirrorTerm_eq_vdvTerm s hs hq2 m j c hc hj hm
    · rfl)]
  rw [Fin.sum_univ_eq_sum_range (fun c => if c ≤ j then vdvTerm s⁻¹ (j - c) c (m - j) else 0),
    Finset.sum_ite, Finset.sum_const_zero, add_zero,
    show (Finset.range (m + 1)).filter (· ≤ j) = Finset.range (j + 1) by
      ext c; simp only [Finset.mem_filter, Finset.mem_range]; omega]
  unfold claspSc
  rw [← Finset.sum_range_reflect]
  exact Finset.sum_congr rfl fun c hc => by
    have := Finset.mem_range.mp hc
    rw [show j + 1 - 1 - c = j - c by omega, show j - (j - c) = c by omega]

include hq2 hint in
/-- **The mirror clasp is scalar on each string**, with van der Veen's `C(n, t⁻¹)`. -/
theorem claspBar_strVec (x : StrIdx m) :
    claspBar s hs m *ᵥ strVec (s ^ 2) m x = claspSc s⁻¹ m x.1 • strVec (s ^ 2) m x := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hm : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0 := fun i h1 h2 => hint i h1 (by omega)
  have hc : Commute (claspBar s hs m) (deltaF (s ^ 2) m m ^ (x.2 : ℕ)) :=
    Commute.pow_right (claspWith_deltaF hq hm (monoBar_deltaKm s hs m hq2 hint)
      (monoBar_deltaF s hs m hq2 hint)) _
  rw [strVec, mulVec_mulVec, hc.eq, ← mulVec_mulVec,
    claspBar_hwVec s hs m hq2 hint x.1 (by omega), mulVec_smul]

include hs in
/-- **Zheng's sum for twists, belts, clasps and mirror clasps.** On `V_{m+1} ⊗ V_{m+1}`,
`tr_q(T^a B^b X^c X̄^d) = Σ_j T_j^a B_j^b C_j(s)^c C_j(s⁻¹)^d [2(m−j)+1]`; this is the sum of
van der Veen's Lemma 1 before the framing factor and the normalisation `1/[N]`. -/
theorem trace_twist_belt_clasp_mirror (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (m : ℕ)
    (hint : ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (s ^ 2) i ≠ 0) (a b c d : ℕ) :
    trace (deltaK (s ^ 2) m m * (twist0 s hs m ^ a * beltW s hs m ^ b * clasp s hs m ^ c
        * claspBar s hs m ^ d))
      = ∑ j : Fin (m + 1), twistSc s m j ^ a * beltSc s m j ^ b * claspSc s m j ^ c
          * claspSc s⁻¹ m j ^ d * qint (s ^ 2) (2 * (m - j) + 1) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hint' : ∀ i, 0 < i → i ≤ 2 * m → qint (s ^ 2) i ≠ 0 := fun i h1 h2 => hint i h1 (by omega)
  refine trace_deltaK_mul (s ^ 2) hq m hq2 hint' _
    (fun j => twistSc s m j ^ a * beltSc s m j ^ b * claspSc s m j ^ c * claspSc s⁻¹ m j ^ d)
    fun x => ?_
  rw [← mulVec_mulVec, mulVec_pow_of_eigen m _ _ _ (claspBar_strVec s hs m hq2 hint' x) d,
    mulVec_smul, ← mulVec_mulVec, mulVec_pow_of_eigen m _ _ _ (clasp_strVec s hs hq2 m hint' x) c,
    mulVec_smul, ← mulVec_mulVec, mulVec_pow_of_eigen m _ _ _ (beltW_strVec s hs hq2 m hint x) b,
    mulVec_smul, mulVec_pow_of_eigen m _ _ _ (twist0_strVec s hs hq2 m hint' x) a, smul_smul,
    smul_smul, smul_smul]
  congr 1
  ring

end MirrorEigen

end QOU.Mass.QuantumSl2
