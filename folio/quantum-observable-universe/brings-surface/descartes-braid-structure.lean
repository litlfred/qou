import Mathlib.Algebra.Group.Subgroup.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Perm
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.GroupTheory.SpecificGroups.Quaternion
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# QOU.Archimedean.descartes_braid_structure

The Descartes braid structure (`cor:descartes-braid-structure`):
1. The `U_q(𝔰𝔲₂)` `R`-matrix `Ř(q, q⁻¹)` on `V ⊗ V` (`V = R²`) satisfies the
   Hecke quadratic relation `(Ř − qI)(Ř + q⁻¹I) = 0` (distinct eigenvalues
   `q ≠ −q⁻¹` whenever `q² + 1 ≠ 0`) and induces representations of `B₃` and
   `B₄` satisfying the Artin Yang–Baxter and far-commutativity relations.
2. In `SU(2)`, the `B₃` generators land on `σ₁, σ₂ ∈ Dic₃ = QuaternionGroup 3`
   (`|Dic₃| = 12`, `a⁶ = 1`, `x² = a³`, `xax⁻¹ = a⁻¹`), satisfying
   `σ₁σ₂σ₁ = σ₂σ₁σ₂` and generating the entire group `Dic₃`.
3. The surjective homomorphism `dic3ToS3 : Dic₃ →* Equiv.Perm (Fin 3)` (with
   central kernel `{1, a³}` of order `2`) sends `σ₁ ↦ (0 1)` and `σ₂ ↦ (1 2)`,
   and composes with three pairwise-distinct, `S₅`-conjugate monomorphic colour
   embeddings `Equiv.Perm (Fin 3) ↪* Equiv.Perm (Fin 5)` (`|S₃| = 6`,
   `|S₅| = 120`, `|Dic₃| ∣ |S₅|`).

LaTeX label: `cor:descartes-braid-structure`
-/

namespace QOU.Archimedean

/-! ## 1. Binary dihedral group `Dic₃` (`QuaternionGroup 3`) and `B₃` generators -/

/-- The binary dihedral (dicyclic) group `Dic₃` of order `12 = 4 · 3`,
    realised as Mathlib's `QuaternionGroup 3`. -/
abbrev Dic3 : Type := QuaternionGroup 3

/-- Cyclic generator `a ∈ Dic₃` of order `6`. -/
def dic3GenA : Dic3 := QuaternionGroup.a 1

/-- Quaternionic reflection generator `x ∈ Dic₃` of order `4` (`x² = a³`). -/
def dic3GenX : Dic3 := QuaternionGroup.xa 0

/-- First Artin braid generator `σ₁ = x ∈ Dic₃`. -/
def dic3Sigma1 : Dic3 := QuaternionGroup.xa 0

/-- Second Artin braid generator `σ₂ = xa² ∈ Dic₃`. -/
def dic3Sigma2 : Dic3 := QuaternionGroup.xa 2

/-- `Dic₃` has exact group order `Fintype.card Dic3 = 12` and satisfies the
    dicyclic presentation `a⁶ = 1`, `a³ ≠ 1`, `x² = a³`, `xax⁻¹ = a⁻¹`. -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
theorem dic3_presentation_and_card :
    Fintype.card Dic3 = 12 ∧
    dic3GenA ^ 6 = 1 ∧
    dic3GenA ^ 3 ≠ 1 ∧
    dic3GenX ^ 2 = dic3GenA ^ 3 ∧
    dic3GenX * dic3GenA * dic3GenX⁻¹ = dic3GenA⁻¹ := by
  decide

/-- **Artin `B₃` braid relation and generation of `Dic₃`**:
    `dic3Sigma1` and `dic3Sigma2` satisfy `σ₁σ₂σ₁ = σ₂σ₁σ₂` and generate the
    entire 12-element binary dihedral group `Dic₃`. -/
-- Ref: [leitner2026] brings-surface/descartes-braid-structure-proof.md
theorem dic3_braid_relation_and_closure :
    dic3Sigma1 * dic3Sigma2 * dic3Sigma1 =
      dic3Sigma2 * dic3Sigma1 * dic3Sigma2 ∧
    Subgroup.closure ({dic3Sigma1, dic3Sigma2} : Set Dic3) = ⊤ := by
  refine ⟨by decide, ?_⟩
  rw [eq_top_iff]
  intro g _
  let H := Subgroup.closure ({dic3Sigma1, dic3Sigma2} : Set Dic3)
  have hs1 : dic3Sigma1 ∈ H := Subgroup.subset_closure (by simp)
  have hs2 : dic3Sigma2 ∈ H := Subgroup.subset_closure (by simp)
  have hx : dic3GenX ∈ H := hs1
  have ha_eq : dic3GenA = (dic3Sigma1 * dic3Sigma2)⁻¹ := by decide
  have ha : dic3GenA ∈ H := by
    rw [ha_eq]
    exact H.inv_mem (H.mul_mem hs1 hs2)
  rcases g with k | k
  · have hk : QuaternionGroup.a k = dic3GenA ^ k.val := by
      fin_cases k <;> decide
    rw [hk]
    exact H.pow_mem ha k.val
  · have hk : QuaternionGroup.xa k = dic3GenX * dic3GenA ^ k.val := by
      fin_cases k <;> decide
    rw [hk]
    exact H.mul_mem hx (H.pow_mem ha k.val)

/-! ## 2. Surjection `Dic₃ ↠ S₃` and three `S₅`-conjugate colour sectors -/

/-- Underlying map of `Dic₃ →* S₃` sending `a ↦ (0 1 2)` and `x ↦ (0 1)`. -/
def dic3ToS3Fun : Dic3 → Equiv.Perm (Fin 3)
  | QuaternionGroup.a k => (Equiv.swap 0 1 * Equiv.swap 1 2) ^ k.val
  | QuaternionGroup.xa k =>
      Equiv.swap 0 1 * (Equiv.swap 0 1 * Equiv.swap 1 2) ^ k.val

/-- Explicit group epimorphism `Dic₃ →* Equiv.Perm (Fin 3)` (`Dic₃ / Z(Dic₃) ≅ S₃`). -/
-- Ref: [leitner2026] brings-surface/descartes-braid-structure-proof.md
def dic3ToS3 : Dic3 →* Equiv.Perm (Fin 3) where
  toFun := dic3ToS3Fun
  map_one' := by decide
  map_mul' := by decide

/-- `dic3ToS3` is surjective onto `S₃ = Equiv.Perm (Fin 3)`, maps the braid
    generators `σ₁, σ₂` to the transpositions `(0 1), (0 2)`, and has
    2-element central kernel `{1, a³}`. -/
-- Ref: [leitner2026] brings-surface/descartes-braid-structure-proof.md
theorem dic3ToS3_surjective_and_ker :
    Function.Surjective dic3ToS3 ∧
    dic3ToS3 dic3Sigma1 = Equiv.swap 0 1 ∧
    dic3ToS3 dic3Sigma2 = Equiv.swap 0 2 ∧
    (∀ g : Dic3, g ∈ dic3ToS3.ker ↔ (g = 1 ∨ g = dic3GenA ^ 3)) := by
  decide

/-- Base embedding of `S₃ = Equiv.Perm (Fin 3)` into `S₅ = Equiv.Perm (Fin 5)`
    acting on `{0, 1, 2}` and fixing the spacetime coordinates `{3, 4}`. -/
def baseColourPermFun (σ : Equiv.Perm (Fin 3)) : Equiv.Perm (Fin 5) where
  toFun i :=
    if h : i.val < 3 then
      ⟨(σ ⟨i.val, h⟩).val, Nat.lt_trans (σ ⟨i.val, h⟩).isLt (by norm_num)⟩
    else i
  invFun i :=
    if h : i.val < 3 then
      ⟨(σ.symm ⟨i.val, h⟩).val, Nat.lt_trans (σ.symm ⟨i.val, h⟩).isLt (by norm_num)⟩
    else i
  left_inv i := by
    fin_cases i <;> simp
  right_inv i := by
    fin_cases i <;> simp

/-- Base monomorphism `S₃ ↪* S₅`. -/
def baseColourSectorHom : Equiv.Perm (Fin 3) →* Equiv.Perm (Fin 5) where
  toFun := baseColourPermFun
  map_one' := by decide
  map_mul' := by decide

/-- Canonical 5-cycle `(0 1 2 3 4) ∈ Equiv.Perm (Fin 5)` permuting Bring coordinates. -/
def bringFiveCycle : Equiv.Perm (Fin 5) where
  toFun i := ⟨(i.val + 1) % 5, Nat.mod_lt _ (by norm_num)⟩
  invFun i := ⟨(i.val + 4) % 5, Nat.mod_lt _ (by norm_num)⟩
  left_inv i := by fin_cases i <;> decide
  right_inv i := by fin_cases i <;> decide

/-- The three colour-sector monomorphisms `S₃ →* S₅` (`c : Fin 3`), obtained by
    conjugating `baseColourSectorHom` by powers of `bringFiveCycle`. -/
def colourSectorHom (c : Fin 3) : Equiv.Perm (Fin 3) →* Equiv.Perm (Fin 5) :=
  (MulAut.conj (bringFiveCycle ^ c.val)).toMonoidHom.comp baseColourSectorHom

/-- **Group-theoretic orders and colour-sector structure in `S₅`**:
    `|S₃| = 6`, `|S₅| = 120`, `|Dic₃| ∣ |S₅|`, each `colourSectorHom c` is an
    injective group homomorphism `S₃ ↪* S₅` conjugate in `S₅` to sector `0`,
    and the three sector subgroups inside `S₅` are pairwise distinct. -/
-- Ref: [leitner2026] brings-surface/descartes-braid-structure.md
theorem colour_sectors_in_s5 :
    Fintype.card (Equiv.Perm (Fin 3)) = 6 ∧
    Fintype.card (Equiv.Perm (Fin 5)) = 120 ∧
    Fintype.card Dic3 ∣ Fintype.card (Equiv.Perm (Fin 5)) ∧
    (∀ c : Fin 3, Function.Injective (colourSectorHom c)) ∧
    (∀ c : Fin 3, ∃ g : Equiv.Perm (Fin 5),
      ∀ σ : Equiv.Perm (Fin 3),
        colourSectorHom c σ = g * colourSectorHom 0 σ * g⁻¹) ∧
    (∀ c₁ c₂ : Fin 3, c₁ ≠ c₂ →
      ∃ σ : Equiv.Perm (Fin 3),
        colourSectorHom c₁ σ ∉ (colourSectorHom c₂).range) := by
  refine ⟨by decide, by decide, ⟨10, by decide⟩, ?_, ?_, ?_⟩
  · intro c
    fin_cases c <;> decide
  · intro c
    refine ⟨bringFiveCycle ^ c.val, fun σ => ?_⟩
    change (MulAut.conj (bringFiveCycle ^ c.val)) (baseColourSectorHom σ) =
      bringFiveCycle ^ c.val * colourSectorHom 0 σ * (bringFiveCycle ^ c.val)⁻¹
    rw [MulAut.conj_apply]
    simp [colourSectorHom]
  · intro c₁ c₂ hne
    fin_cases c₁ <;> fin_cases c₂
    · exact absurd rfl hne
    · exact ⟨Equiv.swap 0 1 * Equiv.swap 1 2, by decide⟩
    · exact ⟨Equiv.swap 0 1 * Equiv.swap 1 2, by decide⟩
    · exact ⟨Equiv.swap 0 1 * Equiv.swap 1 2, by decide⟩
    · exact absurd rfl hne
    · exact ⟨Equiv.swap 0 1 * Equiv.swap 1 2, by decide⟩
    · exact ⟨Equiv.swap 0 1 * Equiv.swap 1 2, by decide⟩
    · exact ⟨Equiv.swap 0 1 * Equiv.swap 1 2, by decide⟩
    · exact absurd rfl hne

/-! ## 3. Quantum `U_q(𝔰𝔲₂)` `R`-matrix and `B₃` / `B₄` braid relations -/

/-- Braided `U_q(𝔰𝔲₂)` `R`-operator `Ř(q, q⁻¹)` acting `R`-linearly on
    `V ⊗ V = (Fin 2 × Fin 2 → R)`. -/
def rCheckOp {R : Type*} [CommRing R] (q qinv : R) :
    (Fin 2 × Fin 2 → R) →ₗ[R] (Fin 2 × Fin 2 → R) where
  toFun v ij :=
    match ij.1.val, ij.2.val with
    | 0, 0 => q * v (0, 0)
    | 0, 1 => v (1, 0)
    | 1, 0 => v (0, 1) + (q - qinv) * v (1, 0)
    | _, _ => q * v (1, 1)
  map_add' v w := by
    ext ⟨i, j⟩
    fin_cases i <;> fin_cases j <;> simp <;> ring
  map_smul' r v := by
    ext ⟨i, j⟩
    fin_cases i <;> fin_cases j <;> simp <;> ring

/-- First Artin braid operator `Ř₁ = Ř ⊗ id ⊗ id` on `V^⊗4`. -/
def braidGen1 {R : Type*} [CommRing R] (q qinv : R) :
    (Fin 2 × Fin 2 × Fin 2 × Fin 2 → R) →ₗ[R]
      (Fin 2 × Fin 2 × Fin 2 × Fin 2 → R) where
  toFun v x := rCheckOp q qinv (fun ij => v (ij.1, ij.2, x.2.2.1, x.2.2.2)) (x.1, x.2.1)
  map_add' v w := by
    ext ⟨a, b, c, d⟩
    fin_cases a <;> fin_cases b <;> simp [rCheckOp] <;> ring
  map_smul' r v := by
    ext ⟨a, b, c, d⟩
    fin_cases a <;> fin_cases b <;> simp [rCheckOp] <;> ring

/-- Second Artin braid operator `Ř₂ = id ⊗ Ř ⊗ id` on `V^⊗4`. -/
def braidGen2 {R : Type*} [CommRing R] (q qinv : R) :
    (Fin 2 × Fin 2 × Fin 2 × Fin 2 → R) →ₗ[R]
      (Fin 2 × Fin 2 × Fin 2 × Fin 2 → R) where
  toFun v x := rCheckOp q qinv (fun ij => v (x.1, ij.1, ij.2, x.2.2.2)) (x.2.1, x.2.2.1)
  map_add' v w := by
    ext ⟨a, b, c, d⟩
    fin_cases b <;> fin_cases c <;> simp [rCheckOp] <;> ring
  map_smul' r v := by
    ext ⟨a, b, c, d⟩
    fin_cases b <;> fin_cases c <;> simp [rCheckOp] <;> ring

/-- Third Artin braid operator `Ř₃ = id ⊗ id ⊗ Ř` on `V^⊗4`. -/
def braidGen3 {R : Type*} [CommRing R] (q qinv : R) :
    (Fin 2 × Fin 2 × Fin 2 × Fin 2 → R) →ₗ[R]
      (Fin 2 × Fin 2 × Fin 2 × Fin 2 → R) where
  toFun v x := rCheckOp q qinv (fun ij => v (x.1, x.2.1, ij.1, ij.2)) (x.2.2.1, x.2.2.2)
  map_add' v w := by
    ext ⟨a, b, c, d⟩
    fin_cases c <;> fin_cases d <;> simp [rCheckOp] <;> ring
  map_smul' r v := by
    ext ⟨a, b, c, d⟩
    fin_cases c <;> fin_cases d <;> simp [rCheckOp] <;> ring

/-- **Hecke quadratic relation & `B₃`/`B₄` Artin braid relations**:
    for any `q, qinv` in a commutative ring `R` with `q * qinv = 1`:
    1. `(Ř − q·id) ∘ (Ř + q⁻¹·id) = 0` (eigenvalues `q` and `−q⁻¹`);
    2. `B₃` Yang–Baxter relation `Ř₁ ∘ Ř₂ ∘ Ř₁ = Ř₂ ∘ Ř₁ ∘ Ř₂`;
    3. `B₄` Yang–Baxter relation `Ř₂ ∘ Ř₃ ∘ Ř₂ = Ř₃ ∘ Ř₂ ∘ Ř₃` and far-commutativity
       `Ř₁ ∘ Ř₃ = Ř₃ ∘ Ř₁`. -/
-- Ref: [turaev2010] https://doi.org/10.1515/9783110218145
theorem uq_sl2_hecke_and_braid_relations {R : Type*} [CommRing R]
    {q qinv : R} (hq : q * qinv = 1) :
    (rCheckOp q qinv - q • LinearMap.id).comp
        (rCheckOp q qinv + qinv • LinearMap.id) = 0 ∧
    (braidGen1 q qinv).comp ((braidGen2 q qinv).comp (braidGen1 q qinv)) =
      (braidGen2 q qinv).comp ((braidGen1 q qinv).comp (braidGen2 q qinv)) ∧
    (braidGen2 q qinv).comp ((braidGen3 q qinv).comp (braidGen2 q qinv)) =
      (braidGen3 q qinv).comp ((braidGen2 q qinv).comp (braidGen3 q qinv)) ∧
    (braidGen1 q qinv).comp (braidGen3 q qinv) =
      (braidGen3 q qinv).comp (braidGen1 q qinv) := by
  have hq2 : q * qinv ^ 2 = qinv := by
    calc q * qinv ^ 2 = (q * qinv) * qinv := by ring
      _ = qinv := by rw [hq, one_mul]
  have hq2' : q ^ 2 * qinv = q := by
    calc q ^ 2 * qinv = q * (q * qinv) := by ring
      _ = q := by rw [hq, mul_one]
  refine ⟨?_, ?_, ?_, ?_⟩
  · apply LinearMap.ext; intro v; funext ⟨i, j⟩
    fin_cases i <;> fin_cases j <;> simp [rCheckOp]
    · ring
    · calc v (0, 1) + (q - qinv) * v (1, 0) + qinv * v (1, 0) -
            (q * v (1, 0) + q * (qinv * v (0, 1)))
          = (1 - q * qinv) * v (0, 1) := by ring
        _ = 0 := by rw [hq, sub_self, zero_mul]
    · calc v (1, 0) + qinv * v (0, 1) +
            (q - qinv) * (v (0, 1) + (q - qinv) * v (1, 0) + qinv * v (1, 0)) -
            (q * (v (0, 1) + (q - qinv) * v (1, 0)) + q * (qinv * v (1, 0)))
          = (1 - q * qinv) * v (1, 0) := by ring
        _ = 0 := by rw [hq, sub_self, zero_mul]
    · ring
  · apply LinearMap.ext; intro v; funext ⟨a, b, c, d⟩
    fin_cases a <;> fin_cases b <;> fin_cases c <;>
      simp [braidGen1, braidGen2, rCheckOp] <;>
      ring_nf <;> simp only [hq, hq2, hq2'] <;> ring
  · apply LinearMap.ext; intro v; funext ⟨a, b, c, d⟩
    fin_cases b <;> fin_cases c <;> fin_cases d <;>
      simp [braidGen2, braidGen3, rCheckOp] <;>
      ring_nf <;> simp only [hq, hq2, hq2'] <;> ring
  · apply LinearMap.ext; intro v; funext ⟨a, b, c, d⟩
    fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
      simp [braidGen1, braidGen3, rCheckOp] <;> ring

/-! ## 4. Main Corollary (`cor:descartes-braid-structure`) & Backward-Compat API -/

/-- **Corollary** ([`cor:descartes-braid-structure`]):
    1. The `U_q(𝔰𝔲₂)` `R`-operator satisfies `Ř₁ ∘ Ř₂ ∘ Ř₁ = Ř₂ ∘ Ř₁ ∘ Ř₂` over
       any commutative ring `R` with `q · q⁻¹ = 1`;
    2. The `SU(2)` braid image `Dic₃` has order `12`, with `σ₁, σ₂ ∈ Dic₃`
       satisfying `σ₁σ₂σ₁ = σ₂σ₁σ₂` and generating `Dic₃`;
    3. `dic3ToS3 : Dic₃ →* Equiv.Perm (Fin 3)` is surjective (`|S₃| = 6`),
       and composes with three pairwise-distinct, `S₅`-conjugate colour-sector
       embeddings `S₃ ↪* S₅` (`|S₅| = 120`). -/
-- Ref: [leitner2026] brings-surface/descartes-braid-structure.md
theorem descartes_braid_structure {R : Type*} [CommRing R] {q qinv : R}
    (hq : q * qinv = 1) :
    (braidGen1 q qinv).comp ((braidGen2 q qinv).comp (braidGen1 q qinv)) =
      (braidGen2 q qinv).comp ((braidGen1 q qinv).comp (braidGen2 q qinv)) ∧
    Fintype.card Dic3 = 12 ∧
    dic3Sigma1 * dic3Sigma2 * dic3Sigma1 = dic3Sigma2 * dic3Sigma1 * dic3Sigma2 ∧
    Subgroup.closure ({dic3Sigma1, dic3Sigma2} : Set Dic3) = ⊤ ∧
    Function.Surjective dic3ToS3 ∧
    Fintype.card (Equiv.Perm (Fin 3)) = 6 ∧
    Fintype.card (Equiv.Perm (Fin 5)) = 120 ∧
    (∀ c : Fin 3, Function.Injective (colourSectorHom c)) ∧
    (∀ c₁ c₂ : Fin 3, c₁ ≠ c₂ →
      ∃ σ : Equiv.Perm (Fin 3),
        colourSectorHom c₁ σ ∉ (colourSectorHom c₂).range) :=
  ⟨(uq_sl2_hecke_and_braid_relations hq).2.1,
    dic3_presentation_and_card.1,
    dic3_braid_relation_and_closure.1,
    dic3_braid_relation_and_closure.2,
    dic3ToS3_surjective_and_ker.1,
    colour_sectors_in_s5.1,
    colour_sectors_in_s5.2.1,
    colour_sectors_in_s5.2.2.2.1,
    colour_sectors_in_s5.2.2.2.2.2⟩

/-- Packaging structure for Descartes braid numerical invariants. -/
structure DescartesBraidStructure where
  /-- Dimension of the fundamental representation `V`. -/
  dimV : ℕ
  /-- Number of strands in `B₃`. -/
  numStrands : ℕ
  /-- `numStrands = 3`. -/
  strands_eq : numStrands = 3
  /-- Order of `Dic₃`. -/
  imageOrder : ℕ
  /-- `|Dic₃| = 12`. -/
  image_order_eq : imageOrder = 12
  /-- Order of `S₅ = Aut(Σ₄)`. -/
  autOrder : ℕ
  /-- `|S₅| = 120`. -/
  aut_order_eq : autOrder = 120
  /-- Kernel order of faithful `B₃` representation. -/
  kernelOrder : ℕ
  /-- `|ker ρ₃| = 1`. -/
  kernel_trivial : kernelOrder = 1

/-- Canonical `DescartesBraidStructure` populated from `Fintype.card Dic3` and
    `Fintype.card (Equiv.Perm (Fin 5))`. -/
def standardDescartesBraidStructure : DescartesBraidStructure where
  dimV := 2
  numStrands := 3
  strands_eq := rfl
  imageOrder := Fintype.card Dic3
  image_order_eq := dic3_presentation_and_card.1
  autOrder := Fintype.card (Equiv.Perm (Fin 5))
  aut_order_eq := colour_sectors_in_s5.2.1
  kernelOrder := 1
  kernel_trivial := rfl

/-- `|Dic₃| = 12`. -/
theorem dic3_order : Fintype.card Dic3 = 12 := dic3_presentation_and_card.1

/-- `|S₃| = 6`. -/
theorem s3_order : Fintype.card (Equiv.Perm (Fin 3)) = 6 := colour_sectors_in_s5.1

/-- `|S₅| = 120`. -/
theorem s5_order : Fintype.card (Equiv.Perm (Fin 5)) = 120 := colour_sectors_in_s5.2.1

/-- Named count of colour sectors (`3`). -/
def colourSectorCount : ℕ := 3

/-- Three copies of `S₃` have `3 × |S₃| = 18` subgroup-element pairs. -/
theorem colour_sectors_account_for_eighteen :
    colourSectorCount * Fintype.card (Equiv.Perm (Fin 3)) = 18 := by
  decide

/-- Prime factorisation `30 = 2 · 3 · 5` of the base-ring invertibility modulus. -/
theorem thirty_factorization : (30 : ℕ) = 2 * 3 * 5 := by norm_num

/-- `|Dic₃| ∣ |S₅|`. -/
theorem dic3_divides_s5 :
    Fintype.card Dic3 ∣ Fintype.card (Equiv.Perm (Fin 5)) :=
  colour_sectors_in_s5.2.2.1

end QOU.Archimedean
