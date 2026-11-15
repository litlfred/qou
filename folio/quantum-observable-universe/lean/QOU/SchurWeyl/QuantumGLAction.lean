/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.IwahoriHecke.TensorEmbeddingGL

/-!
# `U_q(gl_d)` operators on `(R^d)^{⊗n}` and their commutation with `Ř`

G3.1 (bean `qou-gl31`), in the matrix model of `TensorEmbeddingGL`.

* `siteOp X w` — the iterated coproduct `Δ⁽ⁿ⁾(X) = Σ_s 1^{⊗s} ⊗ X ⊗ w^{⊗(n−s−1)}` of a one-site
  operator, for the coproduct `Δ(X) = X ⊗ w + 1 ⊗ X`.
* `embedPair_commute_factorOp` — `Ř` at sites `i, j` commutes with any operator `G ⊗ Z` whose
  kernel `G` does not read the sites `i, j`, as soon as `Ř Z = Z Ř`.
* `embedPair_commute_siteOp` — hence `Ř` on an adjacent pair commutes with `Δ⁽ⁿ⁾(X)` as soon as
  it commutes with `w ⊗ w` (`rCheckN_commute_wDiag2`: always) and with `Δ(X)` on `V ⊗ V`.
* `rCheckN_commute_delta2_single` — `Ř` commutes with `Δ(E_i)` and `Δ(F_i)` for the Chevalley
  pair `(i, i+1)` under the tail weight `κ_i = q` on `e_{i+1}`, `qi` on `e_i`, `1` elsewhere.
  This convention was selected by an exact sympy check at `d = 3`, `n = 3` (the opposite tail
  `κ_i⁻¹` fails); the Lean proof is for every `d`.
* `raiseOp`, `lowerOp`, `cartan` — `E_i`, `F_i` and the Cartan torus on `V^{⊗n}`;
  `strandBraid_commute_raise/lower/cartan` — every strand braiding commutes with all of them.

Generic `[CommRing R]`, `q · qi = 1` (§7c).

-- Ref: [jimbo1986] M. Jimbo, Lett. Math. Phys. 11 (1986) 247–252.
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.IwahoriHecke.TensorEmbedGL Matrix

variable {R : Type*} [CommRing R] {d n : ℕ}

/-- `a` and `b` agree off the sites `i, j`. -/
def OffAgree (i j : Fin n) (a b : Fin n → Fin d) : Prop := ∀ k, k ≠ i → k ≠ j → a k = b k

theorem upd_i {i j : Fin n} (hij : i ≠ j) (a : Fin n → Fin d) (x : Fin d × Fin d) :
    Function.update (Function.update a i x.1) j x.2 i = x.1 := by
  rw [Function.update_of_ne hij, Function.update_self]

theorem upd_j {i j : Fin n} (a : Fin n → Fin d) (x : Fin d × Fin d) :
    Function.update (Function.update a i x.1) j x.2 j = x.2 := Function.update_self ..

theorem upd_agree {i j : Fin n} (a : Fin n → Fin d) (x : Fin d × Fin d) :
    OffAgree i j a (Function.update (Function.update a i x.1) j x.2) := by
  intro k hki hkj
  rw [Function.update_of_ne hkj, Function.update_of_ne hki]

/-- An operator `G ⊗ Z`: `Z` on the sites `i, j`, and a kernel `G` that only reads the other
sites. -/
def factorOp (i j : Fin n) (G : (Fin n → Fin d) → (Fin n → Fin d) → R)
    (Z : Matrix (Fin d × Fin d) (Fin d × Fin d) R) : Matrix (Fin n → Fin d) (Fin n → Fin d) R :=
  Matrix.of fun a b => G a b * Z (a i, a j) (b i, b j)

/-- **`Ř` at sites `i, j` commutes with `G ⊗ Z` whenever it commutes with `Z`.** -/
theorem embedPair_commute_factorOp {i j : Fin n} (hij : i ≠ j)
    (M Z : Matrix (Fin d × Fin d) (Fin d × Fin d) R)
    (G : (Fin n → Fin d) → (Fin n → Fin d) → R)
    (hGl : ∀ a a' b, OffAgree i j a a' → G a b = G a' b)
    (hGr : ∀ a b b', OffAgree i j b b' → G a b = G a b')
    (hMZ : M * Z = Z * M) :
    embedPair i j M * factorOp i j G Z = factorOp i j G Z * embedPair i j M := by
  classical
  ext a b
  rw [Matrix.mul_apply, Matrix.mul_apply]
  rw [sum_collapse hij a (fun c => embedPair i j M a c * factorOp i j G Z c b)
    (fun c hc => by dsimp only; rw [embedPair_apply, if_neg hc, zero_mul])]
  rw [sum_collapse hij b (fun c => factorOp i j G Z a c * embedPair i j M c b)
    (fun c hc => by
      dsimp only
      rw [embedPair_apply, if_neg (fun h => hc fun k hki hkj => (h k hki hkj).symm), mul_zero])]
  have hL : ∀ x : Fin d × Fin d,
      embedPair i j M a (Function.update (Function.update a i x.1) j x.2)
          * factorOp i j G Z (Function.update (Function.update a i x.1) j x.2) b
        = G a b * (M (a i, a j) x * Z x (b i, b j)) := by
    intro x
    rw [embedPair_apply, if_pos (show ∀ k, k ≠ i → k ≠ j → _ = _ from upd_agree a x), upd_i hij, upd_j, factorOp, Matrix.of_apply,
      upd_i hij, upd_j, ← hGl a _ b (upd_agree a x)]
    ring
  have hR : ∀ x : Fin d × Fin d,
      factorOp i j G Z a (Function.update (Function.update b i x.1) j x.2)
          * embedPair i j M (Function.update (Function.update b i x.1) j x.2) b
        = G a b * (Z (a i, a j) x * M x (b i, b j)) := by
    intro x
    rw [embedPair_apply, if_pos (fun k hki hkj => ((upd_agree b x) k hki hkj).symm), upd_i hij,
      upd_j, factorOp, Matrix.of_apply, upd_i hij, upd_j, ← hGr a b _ (upd_agree b x)]
    ring
  simp only [hL, hR, ← Finset.mul_sum]
  congr 1
  have h1 := congrFun (congrFun hMZ (a i, a j)) (b i, b j)
  simpa [Matrix.mul_apply] using h1

/-! ## The iterated coproduct of a one-site operator -/

/-- `X` at site `s`, the weight `w` on every later site, the identity before. -/
def siteTerm (X : Matrix (Fin d) (Fin d) R) (w : Fin d → R) (s : Fin n) :
    Matrix (Fin n → Fin d) (Fin n → Fin d) R :=
  Matrix.of fun a b =>
    if (∀ k, k ≠ s → a k = b k) then X (a s) (b s) * ∏ k ∈ Finset.Ioi s, w (b k) else 0

/-- **The iterated coproduct** `Δ⁽ⁿ⁾(X) = Σ_s 1^{⊗(s)} ⊗ X ⊗ w^{⊗(n−s−1)}`, i.e. the coproduct
`Δ(X) = X ⊗ w + 1 ⊗ X` iterated. -/
def siteOp (X : Matrix (Fin d) (Fin d) R) (w : Fin d → R) :
    Matrix (Fin n → Fin d) (Fin n → Fin d) R :=
  ∑ s, siteTerm X w s

/-- `w ⊗ w`, diagonal on `V ⊗ V`. -/
def wDiag2 (w : Fin d → R) : Matrix (Fin d × Fin d) (Fin d × Fin d) R :=
  Matrix.diagonal fun x => w x.1 * w x.2

/-- `Δ(X) = X ⊗ w + 1 ⊗ X` on `V ⊗ V`. -/
def delta2 (X : Matrix (Fin d) (Fin d) R) (w : Fin d → R) :
    Matrix (Fin d × Fin d) (Fin d × Fin d) R :=
  Matrix.of fun x y => X x.1 y.1 * (if x.2 = y.2 then w y.2 else 0)
    + (if x.1 = y.1 then 1 else 0) * X x.2 y.2

section Split

variable {i j : Fin n}

/-- A term strictly before the pair sees `w ⊗ w` on it. -/
theorem siteTerm_eq_factor_lt (X : Matrix (Fin d) (Fin d) R) (w : Fin d → R) {s : Fin n}
    (hsi : s < i) (hij : i < j) :
    siteTerm X w s = factorOp i j
      (fun a b => if (∀ k, k ≠ s → k ≠ i → k ≠ j → a k = b k)
        then X (a s) (b s) * ∏ k ∈ ((Finset.Ioi s).erase i).erase j, w (b k) else 0)
      (wDiag2 w) := by
  classical
  have hi : i ∈ Finset.Ioi s := Finset.mem_Ioi.mpr hsi
  have hj : j ∈ (Finset.Ioi s).erase i :=
    Finset.mem_erase.mpr ⟨hij.ne', Finset.mem_Ioi.mpr (hsi.trans hij)⟩
  ext a b
  simp only [siteTerm, factorOp, Matrix.of_apply, wDiag2, Matrix.diagonal_apply]
  by_cases h : ∀ k, k ≠ s → a k = b k
  · have h1 : a i = b i := h i hsi.ne'
    have h2 : a j = b j := h j (hsi.trans hij).ne'
    rw [if_pos h, if_pos (fun k hks _ _ => h k hks), if_pos (by rw [h1, h2]),
      ← Finset.mul_prod_erase _ _ hi, ← Finset.mul_prod_erase _ _ hj, h1, h2]
    ring
  · rw [if_neg h]
    by_cases h' : ∀ k, k ≠ s → k ≠ i → k ≠ j → a k = b k
    · have hne : (a i, a j) ≠ (b i, b j) := by
        intro he
        apply h
        intro k hks
        by_cases hki : k = i
        · subst hki; exact (Prod.ext_iff.mp he).1
        · by_cases hkj : k = j
          · subst hkj; exact (Prod.ext_iff.mp he).2
          · exact h' k hks hki hkj
      rw [if_neg hne, mul_zero]
    · rw [if_neg h', zero_mul]

/-- A term strictly after the pair sees the identity on it. -/
theorem siteTerm_eq_factor_gt (X : Matrix (Fin d) (Fin d) R) (w : Fin d → R) {s : Fin n}
    (hjs : j < s) (hij : i < j) :
    siteTerm X w s = factorOp i j
      (fun a b => if (∀ k, k ≠ s → k ≠ i → k ≠ j → a k = b k)
        then X (a s) (b s) * ∏ k ∈ Finset.Ioi s, w (b k) else 0)
      (1 : Matrix (Fin d × Fin d) (Fin d × Fin d) R) := by
  classical
  ext a b
  simp only [siteTerm, factorOp, Matrix.of_apply, Matrix.one_apply]
  by_cases h : ∀ k, k ≠ s → a k = b k
  · have h1 : a i = b i := h i (hij.trans hjs).ne
    have h2 : a j = b j := h j hjs.ne
    rw [if_pos h, if_pos (fun k hks _ _ => h k hks), if_pos (by rw [h1, h2]), mul_one]
  · rw [if_neg h]
    by_cases h' : ∀ k, k ≠ s → k ≠ i → k ≠ j → a k = b k
    · have hne : (a i, a j) ≠ (b i, b j) := by
        intro he
        apply h
        intro k hks
        by_cases hki : k = i
        · subst hki; exact (Prod.ext_iff.mp he).1
        · by_cases hkj : k = j
          · subst hkj; exact (Prod.ext_iff.mp he).2
          · exact h' k hks hki hkj
      rw [if_neg hne, mul_zero]
    · rw [if_neg h', zero_mul]

/-- The two terms on the pair combine to `Δ(X)` on it. -/
theorem siteTerm_pair_eq_factor (X : Matrix (Fin d) (Fin d) R) (w : Fin d → R)
    (hij : (j : ℕ) = i + 1) :
    siteTerm X w i + siteTerm X w j = factorOp i j
      (fun a b => if (∀ k, k ≠ i → k ≠ j → a k = b k)
        then ∏ k ∈ Finset.Ioi j, w (b k) else 0)
      (delta2 X w) := by
  classical
  have hlt : i < j := by rw [Fin.lt_iff_val_lt_val]; omega
  have hne : i ≠ j := hlt.ne
  have hIoi : Finset.Ioi i = insert j (Finset.Ioi j) := by
    ext k
    simp only [Finset.mem_Ioi, Finset.mem_insert, Fin.lt_iff_val_lt_val, Fin.ext_iff]
    omega
  have hjn : j ∉ Finset.Ioi j := by simp
  ext a b
  simp only [siteTerm, factorOp, Matrix.of_apply, Matrix.add_apply, delta2]
  rw [hIoi, Finset.prod_insert hjn]
  by_cases h : ∀ k, k ≠ i → k ≠ j → a k = b k
  · rw [if_pos h]
    have hiff1 : (∀ k, k ≠ i → a k = b k) ↔ a j = b j :=
      ⟨fun h' => h' j hne.symm, fun hj k hki => by
        by_cases hkj : k = j
        · subst hkj; exact hj
        · exact h k hki hkj⟩
    have hiff2 : (∀ k, k ≠ j → a k = b k) ↔ a i = b i :=
      ⟨fun h' => h' i hne, fun hi k hkj => by
        by_cases hki : k = i
        · subst hki; exact hi
        · exact h k hki hkj⟩
    simp only [hiff1, hiff2]
    by_cases hj : a j = b j <;> by_cases hi : a i = b i <;> simp [hj, hi] <;> ring
  · rw [if_neg h, zero_mul]
    have h1 : ¬ ∀ k, k ≠ i → a k = b k := fun h' => h fun k hki _ => h' k hki
    have h2 : ¬ ∀ k, k ≠ j → a k = b k := fun h' => h fun k _ hkj => h' k hkj
    rw [if_neg h1, if_neg h2, add_zero]

end Split

section Commute

variable {i j : Fin n}

theorem agree3_congr_left {s : Fin n} {a a' b : Fin n → Fin d} (h : OffAgree i j a a') :
    (∀ k, k ≠ s → k ≠ i → k ≠ j → a k = b k) ↔ (∀ k, k ≠ s → k ≠ i → k ≠ j → a' k = b k) :=
  forall_congr' fun k => by
    constructor
    · intro hk hks hki hkj; rw [← h k hki hkj]; exact hk hks hki hkj
    · intro hk hks hki hkj; rw [h k hki hkj]; exact hk hks hki hkj

theorem agree3_congr_right {s : Fin n} {a b b' : Fin n → Fin d} (h : OffAgree i j b b') :
    (∀ k, k ≠ s → k ≠ i → k ≠ j → a k = b k) ↔ (∀ k, k ≠ s → k ≠ i → k ≠ j → a k = b' k) :=
  forall_congr' fun k => by
    constructor
    · intro hk hks hki hkj; rw [← h k hki hkj]; exact hk hks hki hkj
    · intro hk hks hki hkj; rw [h k hki hkj]; exact hk hks hki hkj

theorem agree2_congr_left {a a' b : Fin n → Fin d} (h : OffAgree i j a a') :
    (∀ k, k ≠ i → k ≠ j → a k = b k) ↔ (∀ k, k ≠ i → k ≠ j → a' k = b k) :=
  forall_congr' fun k => by
    constructor
    · intro hk hki hkj; rw [← h k hki hkj]; exact hk hki hkj
    · intro hk hki hkj; rw [h k hki hkj]; exact hk hki hkj

theorem agree2_congr_right {a b b' : Fin n → Fin d} (h : OffAgree i j b b') :
    (∀ k, k ≠ i → k ≠ j → a k = b k) ↔ (∀ k, k ≠ i → k ≠ j → a k = b' k) :=
  forall_congr' fun k => by
    constructor
    · intro hk hki hkj; rw [← h k hki hkj]; exact hk hki hkj
    · intro hk hki hkj; rw [h k hki hkj]; exact hk hki hkj

/-- **`Ř` on an adjacent pair commutes with the iterated coproduct `Δ⁽ⁿ⁾(X)`**, given the two
two-site facts: `Ř` commutes with `w ⊗ w` and with `Δ(X) = X ⊗ w + 1 ⊗ X`. -/
theorem embedPair_commute_siteOp (q qi : R) (X : Matrix (Fin d) (Fin d) R) (w : Fin d → R)
    (hij : (j : ℕ) = i + 1)
    (hW : rCheckN q qi * wDiag2 w = wDiag2 w * rCheckN q qi)
    (hD : rCheckN q qi * delta2 X w = delta2 X w * rCheckN q qi) :
    embedPair i j (rCheckN q qi) * siteOp X w = siteOp X w * embedPair i j (rCheckN q qi) := by
  classical
  have hlt : i < j := by rw [Fin.lt_iff_val_lt_val]; omega
  have hne : i ≠ j := hlt.ne
  have hsplit : siteOp (n := n) X w
      = (siteTerm X w i + siteTerm X w j) + ∑ s ∈ (Finset.univ.erase i).erase j, siteTerm X w s := by
    rw [siteOp, ← Finset.add_sum_erase _ _ (Finset.mem_univ i),
      ← Finset.add_sum_erase _ _ (Finset.mem_erase.mpr ⟨hne.symm, Finset.mem_univ j⟩), add_assoc]
  suffices Commute (embedPair i j (rCheckN q qi)) (siteOp (n := n) X w) from this.eq
  rw [hsplit]
  refine Commute.add_right ?_ (Commute.sum_right _ _ _ fun s hs => ?_)
  · rw [siteTerm_pair_eq_factor X w hij]
    refine embedPair_commute_factorOp hne _ _ _ (fun a a' b h => ?_) (fun a b b' h => ?_) hD
    · simp only [agree2_congr_left (b := b) h]
    · simp only [agree2_congr_right (a := a) h]
      congr 1
      refine Finset.prod_congr rfl fun k hk => ?_
      have hk' : j < k := Finset.mem_Ioi.mp hk
      rw [h k (hlt.trans hk').ne' hk'.ne']
  · have hsi : s ≠ i := (Finset.mem_erase.mp (Finset.mem_erase.mp hs).2).1
    have hsj : s ≠ j := (Finset.mem_erase.mp hs).1
    rcases lt_or_gt_of_ne hsi with h1 | h1
    · rw [siteTerm_eq_factor_lt X w h1 hlt]
      refine embedPair_commute_factorOp hne _ _ _ (fun a a' b h => ?_) (fun a b b' h => ?_) hW
      · simp only [agree3_congr_left (b := b) (s := s) h, h s hsi hsj]
      · simp only [agree3_congr_right (a := a) (s := s) h, h s hsi hsj]
        congr 1
        refine congrArg _ (Finset.prod_congr rfl fun k hk => ?_)
        simp only [Finset.mem_erase] at hk
        rw [h k hk.2.1 hk.1]
    · have h2 : j < s := by
        rw [Fin.lt_iff_val_lt_val] at h1 ⊢
        have : (s : ℕ) ≠ j := fun e => hsj (Fin.ext e)
        omega
      rw [siteTerm_eq_factor_gt X w h2 hlt]
      refine embedPair_commute_factorOp hne _ _ _ (fun a a' b h => ?_) (fun a b b' h => ?_)
        (by rw [mul_one, one_mul])
      · simp only [agree3_congr_left (b := b) (s := s) h, h s hsi hsj]
      · simp only [agree3_congr_right (a := a) (s := s) h, h s hsi hsj]
        congr 1
        refine congrArg _ (Finset.prod_congr rfl fun k hk => ?_)
        have hk' : s < k := Finset.mem_Ioi.mp hk
        rw [h k (hlt.trans (h2.trans hk')).ne' (h2.trans hk').ne']

end Commute

/-! ## The two-site facts for `U_q(gl_d)` -/

section TwoSite

/-- **`Ř` commutes with `w ⊗ w` for every weight `w`**: it only permutes the two factors. -/
theorem rCheckN_commute_wDiag2 (q qi : R) (w : Fin d → R) :
    rCheckN q qi * wDiag2 w = wDiag2 w * rCheckN q qi := by
  ext u v
  rw [wDiag2, Matrix.mul_diagonal, Matrix.diagonal_mul]
  by_cases h : rCheckN q qi u v = 0
  · rw [h, zero_mul, mul_zero]
  · rcases rCheckN_ne_zero' h with e | e
    · rw [e, mul_comm]
    · rw [e]; simp only; ring
where
  rCheckN_ne_zero' {u v : Fin d × Fin d} (h : rCheckN q qi u v ≠ 0) : u = v ∨ u = (v.2, v.1) := by
    by_contra hc
    push_neg at hc
    exact h (by simp [rCheckN_apply, hc.1, hc.2])

/-- The weight of the Chevalley pair `(i, j)`, `j = i + 1`: `q` on `e_j`, `qi` on `e_i`, `1`
elsewhere. -/
def kap (q qi : R) (i j : Fin d) (x : Fin d) : R := if x = j then q else if x = i then qi else 1

theorem delta2_col (X : Matrix (Fin d) (Fin d) R) (w : Fin d → R) (y : Fin d × Fin d) :
    delta2 X w *ᵥ δ y = fun x => X x.1 y.1 * (if x.2 = y.2 then w y.2 else 0)
      + (if x.1 = y.1 then 1 else 0) * X x.2 y.2 := by
  funext x
  simp [mulVec_single, delta2, δ]

theorem single_apply' (r c x y : Fin d) :
    (Matrix.single r c (1 : R)) x y = if x = r ∧ y = c then 1 else 0 := by
  simp [Matrix.single, Matrix.of_apply, eq_comm]

/-- The column of `Δ(X)` for a matrix unit `X = E_{rc}`. -/
theorem delta2_single_col (r c : Fin d) (w : Fin d → R) (y1 y2 : Fin d) :
    delta2 (Matrix.single r c (1 : R)) w *ᵥ δ (y1, y2)
      = (if y1 = c then w y2 • δ (r, y2) else 0) + (if y2 = c then δ (y1, r) else 0) := by
  rw [delta2_col]
  funext x
  rcases x with ⟨x1, x2⟩
  simp only [single_apply', Pi.add_apply, Pi.smul_apply, smul_eq_mul, δ, Pi.single_apply,
    Prod.mk.injEq]
  split_ifs <;> simp_all [Pi.single_apply, Prod.ext_iff]

set_option maxHeartbeats 4000000 in
/-- **`Ř` commutes with `Δ(E_{rc})` under the tail `κ`**, for `(r, c) = (j, i)` (raising,
`e_i ↦ e_j`) and `(r, c) = (i, j)` (lowering), `j = i + 1`.  Checked in sympy at `d = 3` before
being proved here for every `d`. -/
theorem rCheckN_commute_delta2_single (q qi : R) (hqi : q * qi = 1) {i j : Fin d}
    (hij : (j : ℕ) = i + 1) {r c : Fin d} (hrc : (r = j ∧ c = i) ∨ (r = i ∧ c = j)) :
    rCheckN q qi * delta2 (Matrix.single r c (1 : R)) (kap q qi i j)
      = delta2 (Matrix.single r c (1 : R)) (kap q qi i j) * rCheckN q qi := by
  have hji : j ≠ i := fun h => by rw [h] at hij; omega
  have hlt : i < j := by rw [Fin.lt_iff_val_lt_val]; omega
  have hadj : ∀ x : Fin d, ¬ (i < x ∧ x < j) := fun x hx => by
    rw [Fin.lt_iff_val_lt_val, Fin.lt_iff_val_lt_val] at hx; omega
  have tri : ∀ x : Fin d, x = i ∨ x = j ∨ x < i ∨ j < x := fun x => by
    rcases lt_trichotomy x i with h | h | h
    · exact Or.inr (Or.inr (Or.inl h))
    · exact Or.inl h
    · rcases lt_trichotomy x j with h' | h' | h'
      · exact absurd ⟨h, h'⟩ (hadj x)
      · exact Or.inr (Or.inl h')
      · exact Or.inr (Or.inr (Or.inr h'))
  apply QOU.IwahoriHecke.TensorEmbedGL.ext_col
  rintro ⟨y1, y2⟩
  simp only [← mulVec_mulVec]
  rcases hrc with ⟨hr, hc⟩ | ⟨hr, hc⟩ <;> rw [hr, hc] <;>
  rcases tri y1 with h1 | h1 | h1 | h1 <;> rcases tri y2 with h2 | h2 | h2 | h2 <;>
  rcases lt_trichotomy y1 y2 with h12 | h12 | h12 <;>
  (try (exfalso; fin_omega)) <;> (try rw [h1]) <;> (try rw [h2]) <;> (try rw [h12]) <;>
  simp (disch := fin_omega) only [col_self, col_lt, col_gt, mulVec_add, mulVec_smul, mulVec_zero,
    delta2_single_col, kap] <;>
  split_ifs <;> (try (exfalso; fin_omega)) <;>
  simp (disch := fin_omega) only [col_self, col_lt, col_gt, mulVec_add, mulVec_smul, mulVec_zero,
    smul_add, smul_zero, add_zero, zero_add, smul_smul] <;>
  (try match_scalars) <;>
  first | ring1 | linear_combination hqi | linear_combination -hqi | linear_combination (q - qi) * hqi | linear_combination (qi - q) * hqi

end TwoSite

/-! ## The `U_q(gl_d)` operators on `V^{⊗n}` and the intertwining -/

section Operators

variable (q qi : R)

/-- `Δ⁽ⁿ⁾(E_i)`, raising `e_i ↦ e_j` (`j = i + 1`), tail weight `κ_i`. -/
def raiseOp (i j : Fin d) : Matrix (Fin n → Fin d) (Fin n → Fin d) R :=
  siteOp (Matrix.single j i 1) (kap q qi i j)

/-- `Δ⁽ⁿ⁾(F_i)`, lowering `e_j ↦ e_i` (`j = i + 1`), tail weight `κ_i`. -/
def lowerOp (i j : Fin d) : Matrix (Fin n → Fin d) (Fin n → Fin d) R :=
  siteOp (Matrix.single i j 1) (kap q qi i j)

/-- A product-weight diagonal operator `e_a ↦ (∏_k c(a_k)) e_a`.  The Cartan `K_j` is
`c = fun x => if x = j then q else 1`. -/
def cartan (c : Fin d → R) : Matrix (Fin n → Fin d) (Fin n → Fin d) R :=
  Matrix.diagonal fun a => ∏ k, c (a k)

theorem cartan_entry_eq {c : Fin d → R} {i j : Fin n} (hij : i ≠ j) {a b : Fin n → Fin d}
    (h : embedPair i j (rCheckN q qi) a b ≠ 0) : (∏ k, c (a k)) = ∏ k, c (b k) := by
  classical
  rw [embedPair_apply] at h
  by_cases hab : ∀ k, k ≠ i → k ≠ j → a k = b k
  · rw [if_pos hab] at h
    have hpair : c (a i) * c (a j) = c (b i) * c (b j) := by
      rcases rCheckN_commute_wDiag2.rCheckN_ne_zero' q qi h with e | e
      · simp only [Prod.ext_iff] at e; rw [e.1, e.2]
      · simp only [Prod.ext_iff] at e; rw [e.1, e.2, mul_comm]
    rw [← Finset.prod_mul_prod_compl {i, j} (fun s => c (a s)),
      ← Finset.prod_mul_prod_compl {i, j} (fun s => c (b s)),
      Finset.prod_pair hij, Finset.prod_pair hij, hpair]
    congr 1
    refine Finset.prod_congr rfl fun s hs => ?_
    simp only [Finset.mem_compl, Finset.mem_insert, Finset.mem_singleton, not_or] at hs
    rw [hab s hs.1 hs.2]
  · rw [if_neg hab] at h; exact absurd rfl h

/-- **Every product-weight diagonal (in particular every Cartan `K_j`) commutes with `Ř`** at
any two distinct sites. -/
theorem embedPair_commute_cartan (c : Fin d → R) {i j : Fin n} (hij : i ≠ j) :
    embedPair i j (rCheckN q qi) * cartan c = cartan c * embedPair i j (rCheckN q qi) := by
  ext a b
  rw [cartan, Matrix.mul_diagonal, Matrix.diagonal_mul]
  by_cases h : embedPair i j (rCheckN q qi) a b = 0
  · rw [h, zero_mul, mul_zero]
  · rw [cartan_entry_eq q qi hij h, mul_comm]

variable {q qi}

/-- **`Ř` on strand `a` commutes with `Δ⁽ⁿ⁾(E_i)`.** -/
theorem strandBraid_commute_raise (hqi : q * qi = 1) {m : ℕ} (a : Fin m) {i j : Fin d}
    (hij : (j : ℕ) = i + 1) :
    strandBraid q qi a * raiseOp q qi i j = raiseOp q qi i j * strandBraid q qi a := by
  rw [strandBraid, braidAt]
  exact embedPair_commute_siteOp q qi _ _ (by simp)
    (rCheckN_commute_wDiag2 q qi _)
    (rCheckN_commute_delta2_single q qi hqi hij (Or.inl ⟨rfl, rfl⟩))

/-- **`Ř` on strand `a` commutes with `Δ⁽ⁿ⁾(F_i)`.** -/
theorem strandBraid_commute_lower (hqi : q * qi = 1) {m : ℕ} (a : Fin m) {i j : Fin d}
    (hij : (j : ℕ) = i + 1) :
    strandBraid q qi a * lowerOp q qi i j = lowerOp q qi i j * strandBraid q qi a := by
  rw [strandBraid, braidAt]
  exact embedPair_commute_siteOp q qi _ _ (by simp)
    (rCheckN_commute_wDiag2 q qi _)
    (rCheckN_commute_delta2_single q qi hqi hij (Or.inr ⟨rfl, rfl⟩))

/-- **`Ř` on strand `a` commutes with every product-weight diagonal.** -/
theorem strandBraid_commute_cartan {m : ℕ} (a : Fin m) (c : Fin d → R) :
    strandBraid q qi a * cartan c = cartan c * strandBraid q qi a := by
  rw [strandBraid, braidAt]
  exact embedPair_commute_cartan q qi c (by simp [Fin.ext_iff])

end Operators

end QOU.SchurWeyl.QuantumGL
