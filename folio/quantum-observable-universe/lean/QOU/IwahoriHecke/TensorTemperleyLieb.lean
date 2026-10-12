import QOU.IwahoriHecke.TensorMarkovModel
import QOU.MathlibExt.TemperleyLiebAlgebra

/-!
# QOU.IwahoriHecke.TensorTemperleyLieb — `V^{⊗(N+1)}` is a Temperley–Lieb module

The Hecke action of `QOU.IwahoriHecke.TensorMarkovModel` (Jimbo's `Ř` on `V^{⊗(N+1)}`,
`V = R²`) factors through the Temperley–Lieb algebra `TL_{N+1}(δ)`, `δ = [2] = q + q⁻¹`,
by the map `σᵢ ↦ q − eᵢ`. This file proves it:

* `tlGen q N i := q • 1 − S q N i` (the image of `eᵢ`);
* `tlGen_sq` — `eᵢ² = (q + q⁻¹) eᵢ`;
* `tlGen_adj_up`, `tlGen_adj_down` — `eᵢ eᵢ₊₁ eᵢ = eᵢ` and `eᵢ₊₁ eᵢ eᵢ₊₁ = eᵢ₊₁`;
* `tlGen_comm` — `eᵢ eⱼ = eⱼ eᵢ` for `|i − j| ≥ 2`;
* `tlRep` — the resulting `R`-algebra map `TLFin R (q + q⁻¹) N → End(V^{⊗(N+1)})`
  out of the presented Temperley–Lieb algebra of `QOU.MathlibExt.TemperleyLieb`, with
  `tlRep_e : tlRep (e i) = q • 1 − σᵢ`, i.e. `σᵢ = q − ρ(eᵢ)` (`S_eq_q_sub_tlRep`).

The quadratic relation is the Hecke quadratic rewritten; the adjacency relation is **not** a
consequence of the Hecke relations — it is the vanishing of the `q`-antisymmetriser on three
sites, true because `dim V = 2`, and it is checked here as an `8 × 8` matrix identity
(`F12F`, `F21F`) transported to every position by the three-site embedding.

## Relation to the standard modules

`TL_{r}(δ)` acts on `V^{⊗r}` with `V^{⊗r} ≅ ⊕_j W_{r,j} ⊗ L_j`, `dim L_j = j + 1`, and the
quantum trace of `TensorMarkovModel` restricts to `Σ_j [j+1] tr_{W_{r,j}} / [2]^r`. That
decomposition (quantum Schur–Weyl duality) is **not** proved here, and the standard modules
`W_{r,j}` are not constructed as separate objects.

-- Ref: [jones1987] Jones, Ann. of Math. 126 (1987); [jimbo1986]
-/

namespace QOU.IwahoriHecke.TensorTemperleyLieb

open QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.RMatrix QOU.IwahoriHecke.TensorMarkovModel
open QOU.MathlibExt.TemperleyLieb

variable {R : Type*} [Field R]

/-! ## Two and three sites -/

/-- `e = q − Ř` on `V ⊗ V`. -/
noncomputable def E2 (q : R) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) R :=
  q • 1 - rCheck q q⁻¹

/-- `e ⊗ 1` on `V^{⊗3}`. -/
noncomputable def F1 (q : R) : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R :=
  Matrix.of fun u v => E2 q (u.1, u.2.1) (v.1, v.2.1) * (if u.2.2 = v.2.2 then 1 else 0)

/-- `1 ⊗ e` on `V^{⊗3}`. -/
noncomputable def F2 (q : R) : Matrix (Fin 2 × Fin 2 × Fin 2) (Fin 2 × Fin 2 × Fin 2) R :=
  Matrix.of fun u v => (if u.1 = v.1 then 1 else 0) * E2 q (u.2.1, u.2.2) (v.2.1, v.2.2)

/-- The image of `eₐ` on `V^{⊗(N+1)}`: `e = q − Ř` at the sites `a, a + 1`. -/
noncomputable def tlGen (q : R) {N : ℕ} (a : Fin N) :
    Matrix (Fin (N + 1) → Fin 2) (Fin (N + 1) → Fin 2) R :=
  embedPair a.castSucc a.succ (E2 q)

theorem castSucc_ne_succ' {N : ℕ} (a : Fin N) : a.castSucc ≠ a.succ := by
  simp [Fin.ext_iff]

variable {q : R}

theorem E2_sq (hq : q ≠ 0) : E2 q * E2 q = (q + q⁻¹) • E2 q := by
  have h : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [E2, rCheck, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Prod.ext_iff, Matrix.one_apply]
  all_goals first | ring1 | (field_simp; done) | (field_simp; ring1)

set_option maxHeartbeats 4000000 in
/-- The Temperley–Lieb relation `e₁ e₂ e₁ = e₁` on `V^{⊗3}`. -/
theorem F12F (hq : q ≠ 0) : F1 q * F2 q * F1 q = F1 q := by
  have h : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [F1, F2, E2, rCheck, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Prod.ext_iff, Matrix.one_apply]
  all_goals first | ring1 | (field_simp; done) | (field_simp; ring1)

set_option maxHeartbeats 4000000 in
/-- The Temperley–Lieb relation `e₂ e₁ e₂ = e₂` on `V^{⊗3}`. -/
theorem F21F (hq : q ≠ 0) : F2 q * F1 q * F2 q = F2 q := by
  have h : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [F1, F2, E2, rCheck, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Prod.ext_iff, Matrix.one_apply]
  all_goals first | ring1 | (field_simp; done) | (field_simp; ring1)

/-! ## At every position -/

/-- `eₐ = q − σₐ` on `V^{⊗(N+1)}`. -/
theorem tlGen_eq {N : ℕ} (a : Fin N) : tlGen q a = q • 1 - strandBraid q q⁻¹ a := by
  show embedPairHom (R := R) (castSucc_ne_succ' a) (q • 1 - rCheck q q⁻¹) = _
  rw [map_sub, map_smul, map_one]
  rfl

/-- `eₐ² = (q + q⁻¹) eₐ`. -/
theorem tlGen_sq (hq : q ≠ 0) {N : ℕ} (a : Fin N) :
    tlGen q a * tlGen q a = (q + q⁻¹) • tlGen q a := by
  show embedPairHom (R := R) (castSucc_ne_succ' a) (E2 q)
      * embedPairHom (R := R) (castSucc_ne_succ' a) (E2 q)
      = (q + q⁻¹) • embedPairHom (R := R) (castSucc_ne_succ' a) (E2 q)
  rw [← map_mul, E2_sq hq, map_smul]

/-- `eₐ e_b eₐ = eₐ` and `e_b eₐ e_b = e_b` for `b = a + 1`. -/
theorem tlGen_adj (hq : q ≠ 0) {N : ℕ} (a b : Fin N) (h : a.val + 1 = b.val) :
    tlGen q a * tlGen q b * tlGen q a = tlGen q a ∧
      tlGen q b * tlGen q a * tlGen q b = tlGen q b := by
  have hb : b.castSucc = a.succ := Fin.ext (by simp only [Fin.coe_castSucc, Fin.val_succ]; omega)
  have hij : a.castSucc ≠ a.succ := castSucc_ne_succ' a
  have hik : a.castSucc ≠ b.succ := by
    simp only [Ne, Fin.ext_iff, Fin.coe_castSucc, Fin.val_succ]; omega
  have hjk : a.succ ≠ b.succ := by
    simp only [Ne, Fin.ext_iff, Fin.val_succ]; omega
  have e1 : tlGen q a = embedTriple a.castSucc a.succ b.succ (F1 q) :=
    embedPair_eq_embedTriple_left hik hjk (E2 q)
  have e2 : tlGen q b = embedTriple a.castSucc a.succ b.succ (F2 q) := by
    rw [tlGen, hb]
    exact embedPair_eq_embedTriple_right hij hik (E2 q)
  rw [e1, e2]
  refine ⟨?_, ?_⟩
  · rw [embedTriple_mul hij hik hjk, embedTriple_mul hij hik hjk, F12F hq]
  · rw [embedTriple_mul hij hik hjk, embedTriple_mul hij hik hjk, F21F hq]

/-- `eₐ e_b = e_b eₐ` when `|a − b| ≠ 1`. -/
theorem tlGen_comm {N : ℕ} (a b : Fin N) (h : ¬ adjFin a b) :
    tlGen q a * tlGen q b = tlGen q b * tlGen q a := by
  by_cases hab : a = b
  · rw [hab]
  · have hv : a.val ≠ b.val := fun e => hab (Fin.ext e)
    simp only [adjFin, not_or] at h
    obtain ⟨h1, h2⟩ := h
    exact embedPair_commute (castSucc_ne_succ' a) (castSucc_ne_succ' b)
      (by simp only [Ne, Fin.ext_iff, Fin.coe_castSucc]; omega)
      (by simp only [Ne, Fin.ext_iff, Fin.coe_castSucc, Fin.val_succ]; omega)
      (by simp only [Ne, Fin.ext_iff, Fin.coe_castSucc, Fin.val_succ]; omega)
      (by simp only [Ne, Fin.ext_iff, Fin.val_succ]; omega) _ _

/-- **`V^{⊗(N+1)}` is a `TL_{N+1}(q + q⁻¹)`-module**: the algebra map out of the presented
Temperley–Lieb algebra sending `eₐ` to `q − σₐ`. -/
noncomputable def tlRep (hq : q ≠ 0) (N : ℕ) :
    TLFin R (q + q⁻¹) N →ₐ[R] Matrix (Fin (N + 1) → Fin 2) (Fin (N + 1) → Fin 2) R :=
  lift R (q + q⁻¹) (adjFin (n := N)) (tlGen q)
    (fun a => by rw [tlGen_sq hq, Algebra.smul_def])
    (fun a b h => by
      rcases h with h | h
      · exact (tlGen_adj hq a b h).1
      · exact (tlGen_adj hq b a h).2)
    (fun a b h => tlGen_comm a b h)

@[simp] theorem tlRep_e (hq : q ≠ 0) {N : ℕ} (a : Fin N) :
    tlRep hq N (e R (q + q⁻¹) (adjFin (n := N)) a) = q • 1 - strandBraid q q⁻¹ a := by
  rw [tlRep, lift_e, tlGen_eq]

/-- **The Hecke generators factor through Temperley–Lieb**: `σₐ = q − ρ(eₐ)`. -/
theorem S_eq_q_sub_tlRep (hq : q ≠ 0) {N : ℕ} (a : Fin N) :
    S q N a = q • 1 - tlRep hq N (e R (q + q⁻¹) (adjFin (n := N)) a) := by
  rw [tlRep_e, S_of_lt q a.isLt, sub_sub_cancel]

end QOU.IwahoriHecke.TensorTemperleyLieb
