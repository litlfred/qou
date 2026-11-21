import QOU.Mass.QuantumSl2CupCap

/-!
# The clasp is a module map

The clasp `X = (cap ⊗ 1 ⊗ 1)(1 ⊗ M ⊗ 1)(1 ⊗ 1 ⊗ cup)` on `V_{m+1} ⊗ V_{m+1}` commutes with
`Δ(E)`, because the cup and cap are invariant and the monodromy `M = Ř′Ř` commutes with the
coproduct. So `X` sends the highest-weight vector `w_j` to a multiple of itself, and the
multiple is read off at the output `v_j ⊗ v_0` as the sum of the clasp terms of
`QuantumSl2Clasp`.

The four-fold tensor is indexed two ways: `(V ⊗ V) ⊗ (V ⊗ V)`, where cup and cap are Kronecker
factors, and `V ⊗ ((V ⊗ V) ⊗ V)`, where `1 ⊗ M ⊗ 1` is. `regroup` passes between them.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, proof of Lemma 1
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

/-- `Δ(E) = E ⊗ K + 1 ⊗ E` on `V_{m+1} ⊗ V_{m'+1}`. -/
def deltaE (q : 𝕜) (m m' : ℕ) :
    Matrix (Fin (m + 1) × Fin (m' + 1)) (Fin (m + 1) × Fin (m' + 1)) 𝕜 :=
  irrepE q m ⊗ₖ irrepKp q m' + 1 ⊗ₖ irrepE q m'

/-- `Δ(K) = K ⊗ K` on `V_{m+1} ⊗ V_{m'+1}`. -/
def deltaK (q : 𝕜) (m m' : ℕ) :
    Matrix (Fin (m + 1) × Fin (m' + 1)) (Fin (m + 1) × Fin (m' + 1)) 𝕜 :=
  irrepKp q m ⊗ₖ irrepKp q m'

section Intertwine

variable (s : 𝕜) (hs : s ≠ 0)

/-- **`Ř` is a module map for `K`.** -/
theorem rCheckMat_deltaK (m m' : ℕ) :
    rCheckMat s hs m m' * deltaK (s ^ 2) m m' = deltaK (s ^ 2) m' m * rCheckMat s hs m m' := by
  unfold rCheckMat deltaK
  rw [← submatrix_id_id (irrepKp (s ^ 2) m ⊗ₖ irrepKp (s ^ 2) m'),
    ← submatrix_mul _ _ _ _ _ Function.bijective_id, rMat_Kp s hs m m',
    submatrix_mul _ _ _ Prod.swap _ Prod.swap_bijective]
  congr 1
  ext x y
  simp only [submatrix_apply, Prod.swap, kroneckerMap_apply]
  ring

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

include hq2 in
/-- **`Ř` is a module map for `E`:** `Ř Δ(E) = Δ(E) Ř`. -/
theorem rCheckMat_deltaE (m m' : ℕ) (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0) :
    rCheckMat s hs m m' * deltaE (s ^ 2) m m' = deltaE (s ^ 2) m' m * rCheckMat s hs m m' := by
  unfold rCheckMat deltaE
  rw [← submatrix_id_id (irrepE (s ^ 2) m ⊗ₖ irrepKp (s ^ 2) m' + 1 ⊗ₖ irrepE (s ^ 2) m'),
    ← submatrix_mul _ _ _ _ _ Function.bijective_id, rMat_E s hs hq2 m m' hint,
    submatrix_mul _ _ _ Prod.swap _ Prod.swap_bijective]
  congr 1
  ext x y
  simp only [submatrix_apply, Prod.swap, add_apply, kroneckerMap_apply, one_apply]
  ring

/-- **The monodromy commutes with `Δ(K)`.** -/
theorem mono_deltaK (m m' : ℕ) :
    mono s hs m m' * deltaK (s ^ 2) m m' = deltaK (s ^ 2) m m' * mono s hs m m' := by
  unfold mono
  rw [Matrix.mul_assoc, rCheckMat_deltaK s hs m m', ← Matrix.mul_assoc,
    rCheckMat_deltaK s hs m' m, Matrix.mul_assoc]

include hq2 in
/-- **The monodromy commutes with `Δ(E)`.** -/
theorem mono_deltaE (m m' : ℕ) (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0) :
    mono s hs m m' * deltaE (s ^ 2) m m' = deltaE (s ^ 2) m m' * mono s hs m m' := by
  have hint' : ∀ k < rOrder m' m, qint (s ^ 2) (k + 1) ≠ 0 := by
    intro k hk; exact hint k (by unfold rOrder at *; omega)
  unfold mono
  rw [Matrix.mul_assoc, rCheckMat_deltaE s hs hq2 m m' hint, ← Matrix.mul_assoc,
    rCheckMat_deltaE s hs hq2 m' m hint', Matrix.mul_assoc]

end Intertwine

/-! ### Cup and cap as matrices -/

/-- The cup as a column `𝕜 → V ⊗ V`. -/
def cupCol (q : 𝕜) (m : ℕ) : Matrix (Fin (m + 1) × Fin (m + 1)) Unit 𝕜 :=
  Matrix.of fun x _ => cupVec q m x

/-- The cap as a row `V ⊗ V → 𝕜`. -/
def capRow (q : 𝕜) (m : ℕ) : Matrix Unit (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  Matrix.of fun _ x => capVec q m x

theorem deltaE_cupCol (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ p < m, qint q (m - p) ≠ 0) :
    deltaE q m m * cupCol q m = 0 := by
  have h : deltaE q m m *ᵥ cupVec q m = 0 := cupVec_E q hq m hint
  ext x u
  have := congrFun h x
  simp only [mulVec, dotProduct] at this
  simp only [mul_apply, cupCol, of_apply, zero_apply]
  exact this

theorem deltaK_cupCol (q : 𝕜) (hq : q ≠ 0) (m : ℕ) :
    deltaK q m m * cupCol q m = cupCol q m := by
  have h : deltaK q m m *ᵥ cupVec q m = cupVec q m := cupVec_K q hq m
  ext x u
  have := congrFun h x
  simp only [mulVec, dotProduct] at this
  simp only [mul_apply, cupCol, of_apply]
  exact this

theorem capRow_deltaE (q : 𝕜) (hq : q ≠ 0) (m : ℕ)
    (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0) :
    capRow q m * deltaE q m m = 0 := by
  have h : capVec q m ᵥ* deltaE q m m = 0 := capVec_E q hq m hint
  ext u x
  have := congrFun h x
  simp only [vecMul, dotProduct] at this
  simp only [mul_apply, capRow, of_apply, zero_apply]
  exact this

/-! ### The four-fold tensor -/

/-- `Δ³(E)` on `(V ⊗ V) ⊗ (V ⊗ V)`, split `2 + 2`. -/
def delta4E (q : 𝕜) (m : ℕ) :
    Matrix ((Fin (m + 1) × Fin (m + 1)) × (Fin (m + 1) × Fin (m + 1)))
      ((Fin (m + 1) × Fin (m + 1)) × (Fin (m + 1) × Fin (m + 1))) 𝕜 :=
  deltaE q m m ⊗ₖ deltaK q m m + 1 ⊗ₖ deltaE q m m

/-- `Δ³(E)` on `V ⊗ ((V ⊗ V) ⊗ V)`, split `1 + 2 + 1`. -/
def delta4E' (q : 𝕜) (m : ℕ) :
    Matrix (Fin (m + 1) × ((Fin (m + 1) × Fin (m + 1)) × Fin (m + 1)))
      (Fin (m + 1) × ((Fin (m + 1) × Fin (m + 1)) × Fin (m + 1))) 𝕜 :=
  irrepE q m ⊗ₖ (deltaK q m m ⊗ₖ irrepKp q m) + 1 ⊗ₖ (deltaE q m m ⊗ₖ irrepKp q m)
    + 1 ⊗ₖ (1 ⊗ₖ irrepE q m)

/-- `(c, d, p, g)` regrouped from `(c,d),(p,g)` to `c,((d,p),g)`. -/
def regroup (m : ℕ) :
    ((Fin (m + 1) × Fin (m + 1)) × (Fin (m + 1) × Fin (m + 1)))
      ≃ (Fin (m + 1) × ((Fin (m + 1) × Fin (m + 1)) × Fin (m + 1))) where
  toFun x := (x.1.1, ((x.1.2, x.2.1), x.2.2))
  invFun y := ((y.1, y.2.1.1), (y.2.1.2, y.2.2))
  left_inv _ := rfl
  right_inv _ := rfl

/-- The two splittings of `Δ³(E)` agree (coassociativity, entrywise). -/
theorem delta4E_regroup (q : 𝕜) (m : ℕ) :
    delta4E q m = (delta4E' q m).submatrix (regroup m) (regroup m) := by
  have h1 : (1 : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) = 1 ⊗ₖ 1 :=
    one_kronecker_one.symm
  unfold delta4E delta4E'
  rw [h1]
  ext ⟨⟨c, d⟩, ⟨p, g⟩⟩ ⟨⟨c', d'⟩, ⟨p', g'⟩⟩
  simp only [regroup, Equiv.coe_fn_mk, submatrix_apply, deltaE, deltaK, add_apply,
    kroneckerMap_apply]
  ring

/-- The cup in the last two slots: `1 ⊗ 1 ⊗ cup`. -/
def cup4 (q : 𝕜) (m : ℕ) :
    Matrix ((Fin (m + 1) × Fin (m + 1)) × (Fin (m + 1) × Fin (m + 1)))
      ((Fin (m + 1) × Fin (m + 1)) × Unit) 𝕜 :=
  (1 : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) ⊗ₖ cupCol q m

/-- The cap in the first two slots: `cap ⊗ 1 ⊗ 1`. -/
def cap4 (q : 𝕜) (m : ℕ) :
    Matrix (Unit × (Fin (m + 1) × Fin (m + 1)))
      ((Fin (m + 1) × Fin (m + 1)) × (Fin (m + 1) × Fin (m + 1))) 𝕜 :=
  capRow q m ⊗ₖ (1 : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)

theorem delta4E_cup4 (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ p < m, qint q (m - p) ≠ 0) :
    delta4E q m * cup4 q m = cup4 q m * (deltaE q m m ⊗ₖ (1 : Matrix Unit Unit 𝕜)) := by
  unfold delta4E cup4
  rw [Matrix.add_mul]
  simp only [← mul_kronecker_mul, mul_one, one_mul, Matrix.mul_one, deltaK_cupCol q hq m,
    deltaE_cupCol q hq m hint, kronecker_zero, add_zero]

theorem cap4_delta4E (q : 𝕜) (hq : q ≠ 0) (m : ℕ)
    (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0) :
    cap4 q m * delta4E q m = ((1 : Matrix Unit Unit 𝕜) ⊗ₖ deltaE q m m) * cap4 q m := by
  unfold delta4E cap4
  rw [Matrix.mul_add]
  simp only [← mul_kronecker_mul, mul_one, one_mul, Matrix.mul_one, Matrix.one_mul, capRow_deltaE q hq m hint, zero_kronecker,
    zero_add]

section Clasp

variable (s : 𝕜) (hs : s ≠ 0)

/-- The monodromy in the middle two slots: `1 ⊗ M ⊗ 1`. -/
def mid4 (m : ℕ) :
    Matrix ((Fin (m + 1) × Fin (m + 1)) × (Fin (m + 1) × Fin (m + 1)))
      ((Fin (m + 1) × Fin (m + 1)) × (Fin (m + 1) × Fin (m + 1))) 𝕜 :=
  ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ
    (mono s hs m m ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜))).submatrix
    (regroup m) (regroup m)

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

include hq2 in
theorem mid4_delta4E (m : ℕ) (hint : ∀ k < rOrder m m, qint (s ^ 2) (k + 1) ≠ 0) :
    mid4 s hs m * delta4E (s ^ 2) m = delta4E (s ^ 2) m * mid4 s hs m := by
  have hc : ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ
        (mono s hs m m ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜))) * delta4E' (s ^ 2) m
      = delta4E' (s ^ 2) m * ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ
        (mono s hs m m ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜))) := by
    unfold delta4E'
    simp only [mul_add, add_mul, ← mul_kronecker_mul, one_mul, mul_one,
      mono_deltaK s hs m m, mono_deltaE s hs hq2 m m hint]
  unfold mid4
  rw [delta4E_regroup, ← submatrix_mul _ _ _ _ _ (regroup m).bijective,
    ← submatrix_mul _ _ _ _ _ (regroup m).bijective, hc]

/-- The clasp on the four-fold tensor, before the unit factors are dropped. -/
def claspBig (m : ℕ) :
    Matrix (Unit × (Fin (m + 1) × Fin (m + 1))) ((Fin (m + 1) × Fin (m + 1)) × Unit) 𝕜 :=
  cap4 (s ^ 2) m * mid4 s hs m * cup4 (s ^ 2) m

include hq2 in
theorem claspBig_comm (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0) :
    claspBig s hs m * (deltaE (s ^ 2) m m ⊗ₖ (1 : Matrix Unit Unit 𝕜))
      = ((1 : Matrix Unit Unit 𝕜) ⊗ₖ deltaE (s ^ 2) m m) * claspBig s hs m := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hr : ∀ k < rOrder m m, qint (s ^ 2) (k + 1) ≠ 0 := fun k hk =>
    hint (k + 1) (by omega) (by unfold rOrder at hk; omega)
  have hc : ∀ p < m, qint (s ^ 2) (m - p) ≠ 0 := fun p hp => hint (m - p) (by omega) (by omega)
  unfold claspBig
  simp only [Matrix.mul_assoc]
  rw [← delta4E_cup4 (s ^ 2) hq m hc, ← Matrix.mul_assoc (mid4 s hs m),
    mid4_delta4E s hs hq2 m hr, Matrix.mul_assoc, ← Matrix.mul_assoc (cap4 (s ^ 2) m),
    cap4_delta4E (s ^ 2) hq m hint, Matrix.mul_assoc]

/-- **The clasp** `X = (cap ⊗ 1 ⊗ 1)(1 ⊗ M ⊗ 1)(1 ⊗ 1 ⊗ cup)` on `V_{m+1} ⊗ V_{m+1}`. -/
def clasp (m : ℕ) : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  (claspBig s hs m).submatrix (Equiv.punitProd _).symm (Equiv.prodPUnit _).symm

include hq2 in
/-- **The clasp commutes with `Δ(E)`.** -/
theorem clasp_deltaE (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0) :
    clasp s hs m * deltaE (s ^ 2) m m = deltaE (s ^ 2) m m * clasp s hs m := by
  have h1 : deltaE (s ^ 2) m m = (deltaE (s ^ 2) m m ⊗ₖ (1 : Matrix Unit Unit 𝕜)).submatrix
      (Equiv.prodPUnit _).symm (Equiv.prodPUnit _).symm := by
    ext a b; simp
  have h2 : deltaE (s ^ 2) m m = ((1 : Matrix Unit Unit 𝕜) ⊗ₖ deltaE (s ^ 2) m m).submatrix
      (Equiv.punitProd _).symm (Equiv.punitProd _).symm := by
    ext a b; simp
  unfold clasp
  conv_lhs => rw [h1]
  conv_rhs => rw [h2]
  rw [← submatrix_mul _ _ _ _ _ (Equiv.prodPUnit _).symm.bijective,
    ← submatrix_mul _ _ _ _ _ (Equiv.punitProd _).symm.bijective, claspBig_comm s hs hq2 m hint]

end Clasp

end QOU.Mass.QuantumSl2
