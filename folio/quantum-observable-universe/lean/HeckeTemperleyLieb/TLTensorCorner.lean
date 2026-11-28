import HeckeTemperleyLieb.TLQuotientTensor
import HeckeTemperleyLieb.TLRectangularHom

/-!
# Moving cups out of the middle of a tensor product

Bean `hkmt`. The object `[a]` on `N + 1` strands is the corner `P_a^N`: identity on the first
`a + 1` strands, then nested cups. The tensor product `P_a^N ⊗ P_c^M` has the cups of the first
factor in the middle. This file shows that it is isomorphic, as an idempotent, to the standard
corner `P_{a+c+1}^{N+M+1}`, where all the cups sit at the right.

* `cupIter x j`: `j` nested cups to the right of `x`; `P_cupIter`: `P_a^{a+2j} = cupIter 1 j`.
* `mvn_incl_capEmb`: **one strand past one cup**, `ι(cup x) ≅ cup(ι x)`, with explicit
  partial isometries `X e_{n+1} e_{n+2}` and `δ⁻¹ X e_{n+2} e_{n+1}`.
* `mvn_inclIter_cupIter`: any number of strands past any number of cups.
* `mvn_tens_P`: **`P_a^{a+2i} ⊗ P_c^{c+2j} ≅ P_{a+c+1}^{a+c+1+2(i+j)}`** (up to reindexing).

All in `TL` itself; it passes to the quotient by `coe_mvn`. Over any field with `δ ≠ 0`.

-- Ref: [jones1983] Index for subfactors, §4.
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLTensorCorner

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLCable QOU.HeckeTemperleyLieb.TLCupCap
open QOU.HeckeTemperleyLieb.TLQuotientTensor QOU.HeckeTemperleyLieb.TLRectHom

variable {K : Type*} [Field K] {δ : K}

/-! ## Generalities -/

theorem MvN.map {A B : Type*} [Ring A] [Ring B] (φ : A →+* B) {f g : A} (h : MvN f g) :
    MvN (φ f) (φ g) := by
  obtain ⟨hf, hg, a, b, ha, hb, hab, hba⟩ := h
  exact ⟨by rw [← map_mul, hf], by rw [← map_mul, hg], φ a, φ b,
    by rw [← map_mul, ← map_mul, ha], by rw [← map_mul, ← map_mul, hb],
    by rw [← map_mul, hab], by rw [← map_mul, hba]⟩

theorem mvn_recast {N N' : ℕ} (h : N = N') {f g : TLFin K δ N} (hfg : MvN f g) :
    MvN (recast δ h f) (recast δ h g) := by subst h; exact hfg

theorem recast_recast {N N' N'' : ℕ} (h : N = N') (h' : N' = N'') (x : TLFin K δ N) :
    recast δ h' (recast δ h x) = recast δ (h.trans h') x := by subst h; subst h'; rfl

theorem recast_rfl {N : ℕ} (h : N = N) (x : TLFin K δ N) : recast δ h x = x := rfl

theorem incl_recast {N N' : ℕ} (h : N = N') (x : TLFin K δ N) :
    incl δ N' (recast δ h x) = recast δ (by omega) (incl δ N x) := by subst h; rfl

theorem capEmb_recast {N N' : ℕ} (h : N = N') (x : TLFin K δ N) :
    capEmb δ N' (recast δ h x) = recast δ (by omega) (capEmb δ N x) := by subst h; rfl

theorem mvn_recast_iff {N N' : ℕ} (h : N = N') {f g : TLFin K δ N} :
    MvN (recast δ h f) (recast δ h g) ↔ MvN f g := by subst h; rfl

/-! ## Iterated cups -/

variable (δ) in
/-- `j` nested cups to the right of `x`. -/
noncomputable def cupIter {n : ℕ} (x : TLFin K δ n) : ∀ j : ℕ, TLFin K δ (n + 2 * j)
  | 0 => x
  | j + 1 => capEmb δ (n + 2 * j) (cupIter x j)

theorem cupIter_succ {n : ℕ} (x : TLFin K δ n) (j : ℕ) :
    cupIter δ x (j + 1) = capEmb δ (n + 2 * j) (cupIter δ x j) := rfl

theorem P_cupIter (a : ℕ) : ∀ j, P δ a (a + 2 * j) = cupIter δ (1 : TLFin K δ a) j
  | 0 => P_self δ a
  | j + 1 => by
    rw [cupIter_succ, ← P_cupIter a j]
    exact P_succ_succ δ (a := a) (n := a + 2 * j) (by omega)

theorem cupIter_idem (hδ : δ ≠ 0) {n : ℕ} {x : TLFin K δ n} (hx : x * x = x) :
    ∀ j, cupIter δ x j * cupIter δ x j = cupIter δ x j
  | 0 => hx
  | j + 1 => by rw [cupIter_succ, ← capEmb_mul δ hδ, cupIter_idem hδ hx j]

theorem mvn_cupIter (hδ : δ ≠ 0) {n : ℕ} {f g : TLFin K δ n} (h : MvN f g) :
    ∀ j, MvN (cupIter δ f j) (cupIter δ g j)
  | 0 => h
  | j + 1 => mvn_capEmb δ hδ (mvn_cupIter hδ h j)

theorem cupIter_recast {N N' : ℕ} (h : N = N') (x : TLFin K δ N) (j : ℕ) :
    cupIter δ (recast δ h x) j = recast δ (by omega) (cupIter δ x j) := by subst h; rfl

theorem cupIter_add {n : ℕ} (x : TLFin K δ n) (i : ℕ) : ∀ j,
    cupIter δ (cupIter δ x i) j = recast δ (by omega) (cupIter δ x (i + j))
  | 0 => rfl
  | j + 1 => by
    rw [cupIter_succ, cupIter_add x i j, capEmb_recast]
    rfl

/-! ## One strand past one cup -/

theorem mvn_incl_capEmb (hδ : δ ≠ 0) {n : ℕ} {x : TLFin K δ n} (hx : x * x = x) :
    MvN (incl δ (n + 1 + 1) (capEmb δ n x)) (capEmb δ (n + 1) (incl δ n x)) := by
  set X : TLFin K δ (n + 1 + 1 + 1) := incl δ (n + 1 + 1) (incl δ (n + 1) (incl δ n x)) with hXdef
  set g : TLFin K δ (n + 1 + 1 + 1) := e K δ adjFin (Fin.castSucc (Fin.last (n + 1)))
  set h : TLFin K δ (n + 1 + 1 + 1) := e K δ adjFin (Fin.last (n + 1 + 1))
  have hXX : X * X = X := by rw [hXdef, ← map_mul, ← map_mul, ← map_mul, hx]
  have hXg : X * g = g * X := by
    have := congrArg (incl δ (n + 1 + 1)) (incl_incl_commute δ n x).eq
    simpa only [map_mul, incl_e] using this
  have hXh : X * h = h * X := (incl_incl_commute δ (n + 1) (incl δ n x)).eq
  have hgg : g * g = δ • g := e_sq' δ _
  have hhh : h * h = δ • h := e_sq' δ _
  have hghg : g * h * g = g := e_adjacent (by simp [adjFin])
  have hhgh : h * g * h = h := e_adjacent (by simp [adjFin])
  have hL : incl δ (n + 1 + 1) (capEmb δ n x) = δ⁻¹ • (X * g) := by
    simp only [capEmb, map_smul, map_mul, incl_e]; rfl
  have hR : capEmb δ (n + 1) (incl δ n x) = δ⁻¹ • (X * h) := rfl
  rw [hL, hR]
  have cg : Commute X g := hXg
  have ch : Commute X h := hXh
  have hm : ∀ u v : TLFin K δ (n + 1 + 1 + 1), Commute X u → X * u * (X * v) = X * (u * v) := by
    intro u v hu
    rw [mul_assoc, ← mul_assoc u, ← hu.eq, mul_assoc, ← mul_assoc X, hXX]
  have w1 : g * (g * h) * h = δ ^ 2 • (g * h) := by
    rw [← mul_assoc, hgg, smul_mul_assoc, smul_mul_assoc, mul_assoc, hhh, mul_smul_comm, smul_smul,
      sq]
  have w2 : h * (h * g) * g = δ ^ 2 • (h * g) := by
    rw [← mul_assoc, hhh, smul_mul_assoc, smul_mul_assoc, mul_assoc, hgg, mul_smul_comm, smul_smul,
      sq]
  have w3 : g * h * (h * g) = δ • g := by
    rw [mul_assoc, ← mul_assoc h, hhh, smul_mul_assoc, mul_smul_comm, ← mul_assoc, hghg]
  have w4 : h * g * (g * h) = δ • h := by
    rw [mul_assoc, ← mul_assoc g, hgg, smul_mul_assoc, mul_smul_comm, ← mul_assoc, hhgh]
  have hd2 : δ⁻¹ * δ⁻¹ * δ ^ 2 = 1 := by field_simp
  refine ⟨?_, ?_, X * (g * h), δ⁻¹ ^ 2 • (X * (h * g)), ?_, ?_, ?_, ?_⟩
  · rw [smul_mul_smul_comm, hm _ _ cg, hgg, mul_smul_comm, smul_smul, mul_assoc,
      inv_mul_cancel₀ hδ, mul_one]
  · rw [smul_mul_smul_comm, hm _ _ ch, hhh, mul_smul_comm, smul_smul, mul_assoc,
      inv_mul_cancel₀ hδ, mul_one]
  · simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
    rw [hm _ _ cg, hm _ _ (cg.mul_right (cg.mul_right ch)), w1, mul_smul_comm, smul_smul, hd2,
      one_smul]
  · simp only [smul_mul_assoc, mul_smul_comm, smul_smul]
    rw [hm _ _ ch, hm _ _ (ch.mul_right (ch.mul_right cg)), w2, mul_smul_comm, smul_smul]
    congr 1; field_simp
  · rw [mul_smul_comm, hm _ _ (cg.mul_right ch), w3, mul_smul_comm, smul_smul]
    congr 1; field_simp
  · rw [smul_mul_assoc, hm _ _ (ch.mul_right cg), w4, mul_smul_comm, smul_smul]
    congr 1; field_simp

theorem mvn_incl_cupIter (hδ : δ ≠ 0) {n : ℕ} {x : TLFin K δ n} (hx : x * x = x) : ∀ j,
    MvN (incl δ (n + 2 * j) (cupIter δ x j)) (recast δ (by omega) (cupIter δ (incl δ n x) j))
  | 0 => MvN.refl (by rw [← map_mul]; exact congrArg _ hx)
  | j + 1 => by
    refine (mvn_incl_capEmb hδ (cupIter_idem hδ hx j)).trans ?_
    convert mvn_capEmb δ hδ (mvn_incl_cupIter hδ hx j) using 1
    rw [capEmb_recast]; rfl

/-! ## Many strands past many cups -/

theorem mvn_inclIter_cupIter (hδ : δ ≠ 0) {n : ℕ} {x : TLFin K δ n} (hx : x * x = x) (j : ℕ) :
    ∀ m, MvN (inclIter (δ := δ) (n + 2 * j) m (cupIter δ x j))
      (recast δ (by omega) (cupIter δ (inclIter (δ := δ) n m x) j))
  | 0 => MvN.refl (cupIter_idem hδ hx j)
  | m + 1 => by
    have hx' : inclIter (δ := δ) n m x * inclIter (δ := δ) n m x = inclIter (δ := δ) n m x := by
      rw [← map_mul, hx]
    refine (MvN.map (incl δ (n + 2 * j + m)).toRingHom (mvn_inclIter_cupIter hδ hx j m)).trans ?_
    have h2 := mvn_recast (show n + m + 2 * j + 1 = n + 2 * j + m + 1 by omega)
      (mvn_incl_cupIter hδ hx' j)
    convert h2 using 1
    · show incl δ (n + 2 * j + m) (recast δ _ _) = _
      rw [incl_recast]
    · rw [recast_recast]; rfl

/-! ## The tensor product with a cup on the right -/

theorem tens_capEmb_right {n m : ℕ} (x : TLFin K δ n) (y : TLFin K δ m) :
    tens δ x (capEmb δ m y) = capEmb δ (n + m + 1) (tens δ x y) := by
  unfold tens capEmb
  rw [map_smul, mul_smul_comm, map_mul, sh_incl, sh_incl, sh_last, map_mul, map_mul]
  congr 1
  rw [mul_assoc]; rfl

theorem tens_cupIter_right {n m : ℕ} (x : TLFin K δ n) (y : TLFin K δ m) : ∀ j,
    tens δ x (cupIter δ y j) = recast δ (by omega) (cupIter δ (tens δ x y) j)
  | 0 => rfl
  | j + 1 => by
    rw [cupIter_succ, tens_capEmb_right, tens_cupIter_right x y j, capEmb_recast]; rfl

/-! ## The main isomorphism -/

/-- **`P_a^{a+2i} ⊗ P_c^{c+2j} ≅ P_{a+c+1}^{a+c+1+2(i+j)}`**: tensoring two standard corners
gives, up to Murray–von Neumann equivalence, the standard corner of the summed strand count. -/
theorem mvn_tens_P (hδ : δ ≠ 0) (a c i j : ℕ) :
    MvN (tens δ (P δ a (a + 2 * i)) (P δ c (c + 2 * j)))
      (recast δ (by omega) (P δ (a + c + 1) (a + c + 1 + 2 * (i + j)))) := by
  rw [P_cupIter, P_cupIter, P_cupIter, tens_cupIter_right]
  have h1 : tens δ (cupIter δ (1 : TLFin K δ a) i) (1 : TLFin K δ c) =
      inclIter (δ := δ) (a + 2 * i) (c + 1) (cupIter δ (1 : TLFin K δ a) i) := by
    rw [tens, map_one, mul_one]
  rw [h1]
  have hI := mvn_inclIter_cupIter hδ (mul_one (1 : TLFin K δ a)) i (c + 1)
  rw [map_one] at hI
  have hJ := mvn_cupIter hδ hI j
  rw [cupIter_recast, cupIter_add] at hJ
  refine (mvn_recast (by omega) hJ).trans ?_
  rw [recast_recast, recast_recast]
  exact MvN.refl (by rw [← map_mul, ← P_cupIter, P_idem δ hδ])

end QOU.HeckeTemperleyLieb.TLTensorCorner
