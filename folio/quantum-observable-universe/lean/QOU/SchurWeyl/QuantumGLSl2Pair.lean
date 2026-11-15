/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.QuantumGLAction
import QOU.Mass.QuantumSl2Fundamental

/-!
# Each Chevalley pair of `U_q(gl_d)` as a `U_q(sl₂)` representation on `(K^d)^{⊗n}`

G3.4a (bean `qou-gl341`).

`QOU.Mass.QuantumSl2.Rep` is `U_q(sl₂)` representation data (`E, F, K, K⁻¹` with the defining
relations) and `Rep.tensor` its tensor product with the coproduct
`Δ(E) = E ⊗ K + 1 ⊗ E`, `Δ(F) = F ⊗ 1 + K⁻¹ ⊗ F`, proved to respect the relations.

* `fundPair` — for a Chevalley pair `(i, j)`, `j = i + 1`, the vector representation `K^d`
  restricted to `U_q(sl₂)_i`: `E = E_{ji}`, `F = E_{ij}`, `K = κ_i = diag(q on e_j, q⁻¹ on e_i,
  1 elsewhere)`.
* `Rep.reindex` — transport along an equivalence of index types.
* `powRep n` — the `n`-fold tensor power, indexed by words `Fin n → Fin d`.
* `powRep_Kp` — its `K` is the Cartan element `cartan κ_i` of `QuantumGLAction`.
* `powRep_E` — its `E` is `raiseOp q q⁻¹ i j`, the `E_i` of `QuantumGLAction`.

So `raiseOp` together with `powRep.F` and `cartan κ_i` satisfy the `U_q(sl₂)` relations on
`(K^d)^{⊗n}`; in particular `[E, F] = (K − K⁻¹)/(q − q⁻¹)`.

**Note on `lowerOp`.**  `QuantumGLAction.lowerOp` uses the *tail* weight `κ` and commutes with
`Ř`, but it is **not** the `F` of this representation: the standard coproduct puts `κ⁻¹` on the
*earlier* sites.  Checked exactly in sympy at `d ∈ {2, 3}`, `n ≤ 3`: with the tail weight,
`[E, F] ≠ (K − K⁻¹)/(q − q⁻¹)`; with the head weight it holds (and that `F` also commutes with
`Ř`).  The `F` used for highest-weight theory is `(powRep n).F`.

## Base ring (§7c)

Any field, `q ≠ 0`, `q − q⁻¹ ≠ 0` (the relation `[E,F]` divides by it).

-- Ref: [jimbo1986] M. Jimbo, Lett. Math. Phys. 11 (1986) 247–252.
-- Ref: [kassel1995] C. Kassel, *Quantum Groups*, GTM 155, Ch. VII.
-/

namespace QOU.SchurWeyl.QuantumGL

open QOU.Mass.QuantumSl2 Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜] {d : ℕ}

/-- `κ_i⁻¹`. -/
def kapInv (q : 𝕜) (i j : Fin d) (x : Fin d) : 𝕜 := if x = j then q⁻¹ else if x = i then q else 1

section Fund

variable (q : 𝕜)

theorem kap_mul_kapInv (hq : q ≠ 0) (i j : Fin d) (x : Fin d) :
    kap q q⁻¹ i j x * kapInv q i j x = 1 := by
  unfold kap kapInv; split_ifs <;> field_simp

/-- **A Chevalley pair of the vector representation of `U_q(gl_d)`, as a `U_q(sl₂)` rep.** -/
noncomputable def fundPair (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) {i j : Fin d} (hij : i ≠ j) :
    Rep q (Fin d) where
  E := Matrix.single j i 1
  F := Matrix.single i j 1
  Kp := Matrix.diagonal (kap q q⁻¹ i j)
  Km := Matrix.diagonal (kapInv q i j)
  Kp_Km := by
    rw [Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
    congr 1; funext x; exact kap_mul_kapInv q hq i j x
  Km_Kp := by
    rw [Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
    congr 1; funext x; rw [mul_comm]; exact kap_mul_kapInv q hq i j x
  KE := by
    ext a b
    rw [Matrix.mul_diagonal, Matrix.diagonal_mul, Matrix.smul_apply, single_apply', smul_eq_mul]
    split_ifs with h
    · obtain ⟨rfl, rfl⟩ := h
      simp only [kap, kapInv, if_true, if_neg hij, if_neg (Ne.symm hij)]
      field_simp
    · simp
  KF := by
    ext a b
    rw [Matrix.mul_diagonal, Matrix.diagonal_mul, Matrix.smul_apply, single_apply', smul_eq_mul]
    split_ifs with h
    · obtain ⟨rfl, rfl⟩ := h
      simp only [kap, kapInv, if_true, if_neg hij, if_neg (Ne.symm hij)]
      field_simp
    · simp
  EF := by
    have h1 : (q - q⁻¹)⁻¹ * (q - q⁻¹) = 1 := inv_mul_cancel₀ hq2
    ext a b
    simp only [Matrix.sub_apply, Matrix.mul_apply, single_apply', Matrix.smul_apply, smul_eq_mul,
      Matrix.diagonal_apply]
    by_cases hab : a = b
    · subst hab
      simp only [if_true]
      by_cases ha : a = j
      · subst ha
        simp [hij, Ne.symm hij, kap, kapInv, Finset.sum_ite_eq', h1]
      · by_cases ha' : a = i
        · subst ha'
          simp only [kap, kapInv, if_neg ha, if_true]
          simp [hij, Ne.symm hij, Finset.sum_ite_eq']
          rw [show q⁻¹ - q = -(q - q⁻¹) by ring, mul_neg, h1]
        · simp [ha, ha', kap, kapInv]
    · simp only [if_neg hab, mul_zero, sub_zero]
      rw [sub_eq_zero]
      refine Finset.sum_congr rfl fun c _ => ?_
      split_ifs <;> simp_all

end Fund

namespace Rep

variable {q : 𝕜} {ι ι' : Type*} [Fintype ι] [DecidableEq ι] [Fintype ι'] [DecidableEq ι']

/-- **Transport a representation along an equivalence of index types.** -/
noncomputable def reindex (e : ι ≃ ι') (ρ : Rep q ι) : Rep q ι' where
  E := Matrix.reindexAlgEquiv 𝕜 𝕜 e ρ.E
  F := Matrix.reindexAlgEquiv 𝕜 𝕜 e ρ.F
  Kp := Matrix.reindexAlgEquiv 𝕜 𝕜 e ρ.Kp
  Km := Matrix.reindexAlgEquiv 𝕜 𝕜 e ρ.Km
  Kp_Km := by rw [← map_mul, ρ.Kp_Km, map_one]
  Km_Kp := by rw [← map_mul, ρ.Km_Kp, map_one]
  KE := by rw [← map_mul, ← map_mul, ρ.KE, map_smul]
  KF := by rw [← map_mul, ← map_mul, ρ.KF, map_smul]
  EF := by rw [← map_mul, ← map_mul, ← map_sub, ρ.EF, map_smul, map_sub]

theorem reindex_apply_E (e : ι ≃ ι') (ρ : Rep q ι) (a b : ι') :
    (reindex e ρ).E a b = ρ.E (e.symm a) (e.symm b) := rfl

theorem reindex_apply_Kp (e : ι ≃ ι') (ρ : Rep q ι) (a b : ι') :
    (reindex e ρ).Kp a b = ρ.Kp (e.symm a) (e.symm b) := rfl

end Rep

section Power

variable (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) {i j : Fin d} (hij : i ≠ j)

/-- `(Fin n → Fin d) × Fin d ≃ (Fin (n+1) → Fin d)`, the new site appended last. -/
def snocW (n : ℕ) : (Fin n → Fin d) × Fin d ≃ (Fin (n + 1) → Fin d) :=
  (Equiv.prodComm _ _).trans (Fin.snocEquiv fun _ => Fin d)

theorem snocW_symm_apply {n : ℕ} (a : Fin (n + 1) → Fin d) :
    (snocW n).symm a = (Fin.init a, a (Fin.last n)) := rfl

/-- The empty word. -/
def unitW : Unit ≃ (Fin 0 → Fin d) where
  toFun _ := Fin.elim0
  invFun _ := ()
  left_inv _ := rfl
  right_inv _ := funext fun x => x.elim0

/-- **The `n`-fold tensor power of the pair representation**, on words `Fin n → Fin d`. -/
noncomputable def powRep : (n : ℕ) → Rep q (Fin n → Fin d)
  | 0 => Rep.reindex unitW (Rep.trivial q)
  | n + 1 => Rep.reindex (snocW n) (Rep.tensor hq (powRep n) (fundPair q hq hq2 hij))

theorem prod_Ioi_castSucc {M : Type*} [CommMonoid M] {n : ℕ} (s : Fin n) (f : Fin (n + 1) → M) :
    ∏ k ∈ Finset.Ioi s.castSucc, f k = (∏ k ∈ Finset.Ioi s, f k.castSucc) * f (Fin.last n) := by
  classical
  rw [← Finset.prod_filter_mul_prod_filter_not (Finset.Ioi s.castSucc)
    (fun k : Fin (n + 1) => k = Fin.last n)]
  have h1 : (Finset.Ioi s.castSucc).filter (fun k : Fin (n + 1) => k = Fin.last n)
      = {Fin.last n} := by
    ext k
    simp only [Finset.mem_filter, Finset.mem_Ioi, Finset.mem_singleton]
    constructor
    · exact fun h => h.2
    · rintro rfl; exact ⟨Fin.castSucc_lt_last s, rfl⟩
  have h2 : (Finset.Ioi s.castSucc).filter (fun k : Fin (n + 1) => ¬ k = Fin.last n)
      = (Finset.Ioi s).map Fin.castSuccEmb := by
    ext k
    simp only [Finset.mem_filter, Finset.mem_Ioi, Finset.mem_map, Fin.castSuccEmb_apply]
    constructor
    · rintro ⟨hk, hkl⟩
      obtain ⟨k', rfl⟩ := Fin.exists_castSucc_eq.mpr hkl
      exact ⟨k', Fin.castSucc_lt_castSucc_iff.mp hk, rfl⟩
    · rintro ⟨k', hk', rfl⟩
      exact ⟨Fin.castSucc_lt_castSucc_iff.mpr hk', (Fin.castSucc_lt_last k').ne⟩
  rw [h1, h2, Finset.prod_singleton, Finset.prod_map, mul_comm]
  rfl

/-- **The `K` of the tensor power is the Cartan element `cartan κ_i`.** -/
theorem powRep_Kp : ∀ n : ℕ, (powRep q hq hq2 hij n).Kp = cartan (kap q q⁻¹ i j)
  | 0 => by
      ext a b
      have hab : a = b := funext fun x => x.elim0
      subst hab
      simp [powRep, Rep.reindex_apply_Kp, Rep.trivial, cartan]
  | n + 1 => by
      ext a b
      rw [powRep, Rep.reindex_apply_Kp, snocW_symm_apply, snocW_symm_apply]
      change ((powRep q hq hq2 hij n).Kp ⊗ₖ (fundPair q hq hq2 hij).Kp)
        (Fin.init a, a (Fin.last n)) (Fin.init b, b (Fin.last n)) = _
      rw [Matrix.kronecker_apply, powRep_Kp n]
      simp only [fundPair, cartan, Matrix.diagonal_apply]
      by_cases hab : a = b
      · subst hab
        simp only [if_true, Fin.prod_univ_castSucc, Fin.init]
      · have : ¬ (Fin.init a = Fin.init b ∧ a (Fin.last n) = b (Fin.last n)) := by
          rintro ⟨h1, h2⟩
          apply hab
          funext k
          induction k using Fin.lastCases with
          | last => exact h2
          | cast k => exact congrFun h1 k
        by_cases h1 : Fin.init a = Fin.init b
        · rw [if_neg (fun h2 => this ⟨h1, h2⟩), mul_zero, if_neg hab]
        · rw [if_neg h1, zero_mul, if_neg hab]

theorem forall_ne_castSucc_iff {n : ℕ} (s : Fin n) (a b : Fin (n + 1) → Fin d) :
    (∀ k, k ≠ s.castSucc → a k = b k)
      ↔ (∀ k, k ≠ s → Fin.init a k = Fin.init b k) ∧ a (Fin.last n) = b (Fin.last n) := by
  constructor
  · intro h
    exact ⟨fun k hk => h k.castSucc (fun e => hk (Fin.castSucc_injective _ e)),
      h _ (Fin.castSucc_lt_last s).ne'⟩
  · rintro ⟨h1, h2⟩ k hk
    induction k using Fin.lastCases with
    | last => exact h2
    | cast k => exact h1 k (fun e => hk (by rw [e]))

theorem forall_ne_last_iff {n : ℕ} (a b : Fin (n + 1) → Fin d) :
    (∀ k, k ≠ Fin.last n → a k = b k) ↔ Fin.init a = Fin.init b := by
  constructor
  · intro h; funext k; exact h k.castSucc (Fin.castSucc_lt_last k).ne
  · intro h k hk
    obtain ⟨k', rfl⟩ := Fin.exists_castSucc_eq.mpr hk
    exact congrFun h k'

/-- **`Δ⁽ⁿ⁺¹⁾(X) = Δ⁽ⁿ⁾(X) ⊗ w + 1 ⊗ X`**, entrywise, splitting off the last site. -/
theorem siteOp_succ_apply {R : Type*} [CommRing R] {n : ℕ} (X : Matrix (Fin d) (Fin d) R)
    (w : Fin d → R) (a b : Fin (n + 1) → Fin d) :
    siteOp X w a b
      = siteOp X w (Fin.init a) (Fin.init b)
          * (if a (Fin.last n) = b (Fin.last n) then w (b (Fin.last n)) else 0)
        + (if Fin.init a = Fin.init b then X (a (Fin.last n)) (b (Fin.last n)) else 0) := by
  classical
  have hIoi : Finset.Ioi (Fin.last n) = ∅ := by
    ext k; simp [Fin.le_last]
  rw [siteOp, siteOp, Matrix.sum_apply, Matrix.sum_apply, Fin.sum_univ_castSucc, Finset.sum_mul]
  congr 1
  · refine Finset.sum_congr rfl fun s _ => ?_
    simp only [siteTerm, Matrix.of_apply, forall_ne_castSucc_iff, prod_Ioi_castSucc]
    by_cases h1 : ∀ k, k ≠ s → Fin.init a k = Fin.init b k
    · by_cases h2 : a (Fin.last n) = b (Fin.last n)
      · rw [if_pos ⟨h1, h2⟩, if_pos h1, if_pos h2]
        simp only [Fin.init]
        ring
      · rw [if_neg (fun h => h2 h.2), if_neg h2, mul_zero]
    · rw [if_neg (fun h => h1 h.1), if_neg h1, zero_mul]
  · simp only [siteTerm, Matrix.of_apply, forall_ne_last_iff, hIoi, Finset.prod_empty, mul_one]

/-- **The `E` of the tensor power is `raiseOp`**, the `E_i` of `QuantumGLAction`. -/
theorem powRep_E : ∀ n : ℕ, (powRep q hq hq2 hij n).E = raiseOp q q⁻¹ i j
  | 0 => by
      ext a b
      have hab : a = b := funext fun x => x.elim0
      subst hab
      simp [powRep, Rep.reindex_apply_E, Rep.trivial, raiseOp, siteOp]
  | n + 1 => by
      ext a b
      rw [powRep, Rep.reindex_apply_E, snocW_symm_apply, snocW_symm_apply]
      change (((powRep q hq hq2 hij n).E ⊗ₖ (fundPair q hq hq2 hij).Kp
          + (1 : Matrix (Fin n → Fin d) (Fin n → Fin d) 𝕜) ⊗ₖ (fundPair q hq hq2 hij).E :
            Matrix ((Fin n → Fin d) × Fin d) ((Fin n → Fin d) × Fin d) 𝕜))
        (Fin.init a, a (Fin.last n)) (Fin.init b, b (Fin.last n)) = _
      rw [Matrix.add_apply, Matrix.kronecker_apply, Matrix.kronecker_apply, powRep_E n]
      change _ = siteOp (Matrix.single j i (1 : 𝕜)) (kap q q⁻¹ i j) a b
      rw [siteOp_succ_apply]
      change siteOp (Matrix.single j i (1 : 𝕜)) (kap q q⁻¹ i j) (Fin.init a) (Fin.init b) * _ + _
        = _
      simp only [fundPair, Matrix.diagonal_apply, Matrix.one_apply]
      congr 1
      · by_cases h : a (Fin.last n) = b (Fin.last n)
        · rw [if_pos h, if_pos h, h]
        · rw [if_neg h, if_neg h]
      · by_cases h : Fin.init a = Fin.init b
        · rw [if_pos h, if_pos h, one_mul]
        · rw [if_neg h, if_neg h, zero_mul]

end Power

end QOU.SchurWeyl.QuantumGL
