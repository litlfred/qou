import QOU.BraidsAndKnots.RationalAssociator.AssociatorChain

/-!
# A compatible tower of rational associators from a compatible tower of `K`-associators

`rational_associator_of_tower` (`AssociatorChain`) gives, for each `N ≥ 2`, a rational
group-like associator `Φ_N` in `U4 N`, but the `Φ_N` are chosen independently. This file gives
one sequence `Φ : ℕ → ℚ⟨X, Y⟩` with `Φ (N + 1) − Φ N ∈ FF N`, so that the truncations agree.

The hypothesis is strengthened from `GroupLikeKAssociatorTower` to
`CompatibleGroupLikeKAssociatorTower`: the `K`-associators `Ψ_N` must themselves agree,
`Ψ_{N+1} − Ψ_N ∈ FFK K N`. This is what the truncations of a single power series (such as the
KZ associator) satisfy. Removing this strengthening needs the transitivity of the `GRT₁` action on
group-like associators (Drinfeld, Prop. 5.5), which is not formalised here.

How the induction is made uniform in the level:

* `compKK_sub_mem` and `GK_sub_GK_mem`: the shift `Ψ ↦ compKK Ψ (GK H n c)` respects
  congruence modulo `FFK m` in `Ψ`, and in the truncation order `n` once `n ≥ m`.
* `shiftL`: a finite list of shifts, applied at truncation order `n`.
* `stepData`: the data of the induction step (`inductionStep_core`), extracted from the
  `K`-associator at one level only: a rational `x` and a list of shifts whose directions are in
  `grt` at **every** level. The same list is then applied to every member of the tower.
* `towerStep`: the induction step on the whole tower.
* `rational_associator_compatible_of_tower`: the sequence.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

open TensorProduct Friedrichs

local notation "F2" => FreeAlgebra ℚ (Fin 2)

variable {K : Type*} [Field K] [Algebra ℚ K]

/-! ### Congruence of the shift -/

/-- The shift `compKK` respects congruence modulo `FFK m` in both arguments. -/
theorem compKK_sub_mem {m : ℕ} {Ψ Ψ' G G' : K ⊗[ℚ] F2} (hΨ : Ψ - Ψ' ∈ FFK K m)
    (hG : G - G' ∈ FFK K m) : compKK Ψ G - compKK Ψ' G' ∈ FFK K m := by
  set a := G * X1 K * evK (Y1 K) (X1 K) G
  set a' := G' * X1 K * evK (Y1 K) (X1 K) G'
  have hGs : evK (Y1 K) (X1 K) G - evK (Y1 K) (X1 K) G' ∈ FFK K m := by
    have := evK_mem_FFK Y1_mem_FFK X1_mem_FFK hG
    rwa [map_sub] at this
  have ha : a - a' ∈ FFK K m := by
    have e : a - a' = (G - G') * X1 K * evK (Y1 K) (X1 K) G +
        G' * X1 K * (evK (Y1 K) (X1 K) G - evK (Y1 K) (X1 K) G') := by
      simp only [a, a', sub_mul, mul_sub]; abel
    rw [e]
    exact add_mem (FFK_mul_right _ (FFK_mul_right _ hG)) (FFK_mul_left _ hGs)
  have ha'1 : a' ∈ FFK K 1 :=
    FFK_mul_right _ (FFK_mul_left _ X1_mem_FFK)
  have hev : evK a (Y1 K) Ψ - evK a' (Y1 K) Ψ' ∈ FFK K m := by
    have e : evK a (Y1 K) Ψ - evK a' (Y1 K) Ψ' =
        (evK a (Y1 K) Ψ - evK a' (Y1 K) Ψ) + evK a' (Y1 K) (Ψ - Ψ') := by
      rw [map_sub]; abel
    rw [e]
    exact add_mem (evK_sub_mem_FFK a a' (Y1 K) ha Ψ) (evK_mem_FFK ha'1 Y1_mem_FFK hΨ)
  have e : compKK Ψ G - compKK Ψ' G' =
      (evK a (Y1 K) Ψ - evK a' (Y1 K) Ψ') * G + evK a' (Y1 K) Ψ' * (G - G') := by
    simp only [compKK, a, a', sub_mul, mul_sub]; abel
  rw [e]
  exact add_mem (FFK_mul_right _ hev) (FFK_mul_left _ hG)

/-- Raising the truncation order of `GK h · c` from `m` changes it by `FFK m` (`h ∈ FF 1`). -/
theorem GK_add_sub_mem {h : F2} (hh : h ∈ FF 1) (m j : ℕ) (c : K) :
    GK h (m + j) c - GK h m c ∈ FFK K m := by
  induction j with
  | zero => simp
  | succ j ih =>
    have e : GK h (m + (j + 1)) c - GK h m c =
        (GK h (m + j) c - GK h m c) + (c ^ (m + j)) ⊗ₜ expTerm h (m + j) := by
      rw [← add_assoc, GK, Finset.sum_range_succ, ← GK]; abel
    rw [e]
    refine add_mem ih (tmul_mem_FFK _ (FF_anti ?_ (expTerm_mem_FF_mul hh (m + j))))
    omega

/-- Two truncation orders `n, n' ≥ m` agree modulo `FFK m`. -/
theorem GK_sub_GK_mem {h : F2} (hh : h ∈ FF 1) {m n n' : ℕ} (hn : m ≤ n) (hn' : m ≤ n')
    (c : K) : GK h n c - GK h n' c ∈ FFK K m := by
  obtain ⟨j, rfl⟩ := Nat.exists_eq_add_of_le hn
  obtain ⟨j', rfl⟩ := Nat.exists_eq_add_of_le hn'
  have e : GK h (m + j) c - GK h (m + j') c =
      (GK h (m + j) c - GK h m c) - (GK h (m + j') c - GK h m c) := by abel
  rw [e]
  exact sub_mem (GK_add_sub_mem hh m j c) (GK_add_sub_mem hh m j' c)

/-! ### A list of shifts -/

/-- Apply the shifts `exp(c H)`, `(c, H) ∈ L`, at truncation order `n`. -/
noncomputable def shiftL (n : ℕ) : List (K × F2) → K ⊗[ℚ] F2 → K ⊗[ℚ] F2
  | [], Ψ => Ψ
  | p :: L, Ψ => compKK (shiftL n L Ψ) (GK p.2 n p.1)

/-- A list of shifts keeps any predicate that each single shift keeps. -/
theorem shiftL_pred {n : ℕ} (Q : K ⊗[ℚ] F2 → Prop) (L : List (K × F2))
    (hQ : ∀ p ∈ L, ∀ Ψ, Q Ψ → Q (compKK Ψ (GK p.2 n p.1))) {Ψ : K ⊗[ℚ] F2} (hΨ : Q Ψ) :
    Q (shiftL n L Ψ) := by
  induction L with
  | nil => exact hΨ
  | cons p L ih =>
    exact hQ p List.mem_cons_self _
      (ih fun q hq => hQ q (List.mem_cons_of_mem _ hq))

/-- A list of shifts respects congruence modulo `FFK m`, at any two truncation orders `≥ m`. -/
theorem shiftL_sub_mem {m n n' : ℕ} (hn : m ≤ n) (hn' : m ≤ n') (L : List (K × F2))
    (hL : ∀ p ∈ L, p.2 ∈ FF 1) {Ψ Ψ' : K ⊗[ℚ] F2} (h : Ψ - Ψ' ∈ FFK K m) :
    shiftL n L Ψ - shiftL n' L Ψ' ∈ FFK K m := by
  induction L with
  | nil => exact h
  | cons p L ih =>
    exact compKK_sub_mem (ih fun q hq => hL q (List.mem_cons_of_mem _ hq))
      (GK_sub_GK_mem (hL p List.mem_cons_self) hn hn' p.1)

/-- A list of shifts along `FF d` adds `Σ c ⊗ H` modulo `FFK (d + 1)`. -/
theorem shiftL_sum {d n : ℕ} (hd : 1 ≤ d) (hn : 2 ≤ n) (L : List (K × F2))
    (hL : ∀ p ∈ L, p.2 ∈ FF d) {Ψ : K ⊗[ℚ] F2} (h1 : Ψ - 1 ∈ FFK K 1) :
    shiftL n L Ψ - Ψ - (L.map fun p => p.1 ⊗ₜ p.2).sum ∈ FFK K (d + 1) := by
  induction L with
  | nil => simp [shiftL]
  | cons p L ih =>
    have ih := ih fun q hq => hL q (List.mem_cons_of_mem _ hq)
    have hsum : (L.map fun p => p.1 ⊗ₜ[ℚ] p.2).sum ∈ FFK K 1 := by
      refine list_sum_mem fun y hy => ?_
      obtain ⟨q, hq, rfl⟩ := List.mem_map.1 hy
      exact tmul_mem_FFK _ (FF_anti hd (hL q (List.mem_cons_of_mem _ hq)))
    have hS1 : shiftL n L Ψ - 1 ∈ FFK K 1 := by
      have e : shiftL n L Ψ - 1 = (shiftL n L Ψ - Ψ - (L.map fun p => p.1 ⊗ₜ[ℚ] p.2).sum) +
          (L.map fun p => p.1 ⊗ₜ[ℚ] p.2).sum + (Ψ - 1) := by abel
      rw [e]; exact add_mem (add_mem (FFK_anti (by omega) ih) hsum) h1
    have hc := compKK_congr hd hn (hL p List.mem_cons_self) hS1 p.1
    have e : shiftL n (p :: L) Ψ - Ψ - ((p :: L).map fun p => p.1 ⊗ₜ[ℚ] p.2).sum =
        (compKK (shiftL n L Ψ) (GK p.2 n p.1) - shiftL n L Ψ - p.1 ⊗ₜ p.2) +
          (shiftL n L Ψ - Ψ - (L.map fun p => p.1 ⊗ₜ[ℚ] p.2).sum) := by
      simp only [shiftL, List.map_cons, List.sum_cons]; abel
    rw [e]; exact add_mem hc ih

/-! ### The data of the induction step, extracted at one level -/

/-- **The induction step as data.** From a `K`-associator `1 ⊗ Φ + z` in `U4 (d + 1)` whose
top layer is primitive (`hprim`, supplied by `primLayer_of_GLK`), there is a rational `x ∈ FF d`
with `Φ + x` an associator in `U4 (d + 1)`, and a list of shifts `(c, H)` with `H ∈ FF d`
primitive and in `grt` in **every** `U4 M`, such that `Σ c ⊗ H ≡ 1 ⊗ x − z` modulo `FFK (d + 1)`.
This is the content of `inductionStep_core`, with the shifts returned instead of applied. -/
theorem stepData {d : ℕ} (hd : 1 ≤ d) {E Φ : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hΦ : FreeAlgebra.algebraMapInv Φ = 1) (z : K ⊗[ℚ] FF d)
    (hK : AssocK K (d + 1) E ((1 : K) ⊗ₜ Φ + LinearMap.lTensor K (FF d).subtype z))
    (hprim : ∀ μ ν : K →ₗ[ℚ] ℚ, ∃ h : F2, Homog d h ∧
      (μ 1 • (contract ν (FF d) z : F2) - ν 1 • (contract μ (FF d) z : F2) - h ∈ FF (d + 1)) ∧
        Friedrichs.IsPrimitive h) :
    ∃ x ∈ FF d, AssocU4 (d + 1) E (Φ + x) ∧ ∃ L : List (K × F2),
      (∀ p ∈ L, p.2 ∈ FF d ∧ Friedrichs.IsPrimitive p.2 ∧ ∀ M, GrtU4 M p.2) ∧
      (L.map fun p => p.1 ⊗ₜ p.2).sum + LinearMap.lTensor K (FF d).subtype z -
        (1 : K) ⊗ₜ x ∈ FFK K (d + 1) := by
  classical
  obtain ⟨π, hπ⟩ := exists_retraction (k := ℚ) (K := K)
  obtain ⟨x0, hx0, hw⟩ := rational_lift_of_assocK hd hE hΦ z hK
  set x : FF d := contract π (FF d) z with hx
  set u : K ⊗[ℚ] FF d := (1 : K) ⊗ₜ x - z with hu
  have hcw : ∀ μ : K →ₗ[ℚ] ℚ, μ 1 • linFF d x0 - linFF d (contract μ (FF d) z) = 0 := by
    intro μ
    have := linFF_contract_eq_zero hw μ
    rwa [map_sub, contract_tmul, map_sub, map_smul] at this
  have hxx0 : linFF d x = linFF d x0 := by
    have := hcw π
    rw [hπ, one_smul, sub_eq_zero] at this
    exact this.symm
  have hcu : ∀ μ : K →ₗ[ℚ] ℚ, linFF d (contract μ (FF d) u) = 0 := by
    intro μ
    rw [hu, map_sub, contract_tmul, map_sub, map_smul, hxx0]
    exact hcw μ
  have hassoc : AssocU4 (d + 1) E (Φ + x) := by
    have h0 := (assocU4_add_iff hd hE hΦ x0.2).1 hx0
    refine (assocU4_add_iff hd hE hΦ x.2).2 ?_
    rw [← h0]
    exact hxx0
  choose hμ hHom hdiff hP using hprim
  let H : (K →ₗ[ℚ] ℚ) → F2 := fun μ => hμ μ π
  have hHdiff : ∀ μ, (contract μ (FF d) u : F2) - H μ ∈ FF (d + 1) := by
    intro μ
    have e : (contract μ (FF d) u : F2) =
        μ 1 • (contract π (FF d) z : F2) - π 1 • (contract μ (FF d) z : F2) := by
      simp only [hu, hx, map_sub, contract_tmul, Submodule.coe_sub, Submodule.coe_smul, hπ,
        one_smul]
    rw [e]
    exact hdiff μ π
  have hHF : ∀ μ, H μ ∈ FF d := by
    intro μ
    have e : H μ = (contract μ (FF d) u : F2) - ((contract μ (FF d) u : F2) - H μ) := by abel
    rw [e]
    exact sub_mem (contract μ (FF d) u).2 (FF_anti (by omega) (hHdiff μ))
  have hHlin : ∀ μ, assocLin (d + 1) (H μ) = 0 := by
    intro μ
    have e : H μ = (contract μ (FF d) u : F2) - ((contract μ (FF d) u : F2) - H μ) := by abel
    rw [e, map_sub, assocLin_eq_zero_of_mem_FF (hHdiff μ), sub_zero]
    exact hcu μ
  have hHgrt : ∀ μ M, GrtU4 M (H μ) := fun μ _ =>
    grtU4_of_lin_primitive (hHom μ π) (hHlin μ) (hP μ π)
  set B := Module.Basis.ofVectorSpace ℚ K
  set f := TensorProduct.equivFinsuppOfBasisLeft B u
  have hf : ∀ i, (f i : F2) = contract (B.coord i) (FF d) u := fun i => by
    rw [equivFinsuppOfBasisLeft_eq_contract]
  let g : _ → K × F2 := fun i => (B i, H (B.coord i))
  refine ⟨x, x.2, hassoc, f.support.toList.map g, ?_, ?_⟩
  · intro p hp
    obtain ⟨i, -, rfl⟩ := List.mem_map.1 hp
    exact ⟨hHF _, hP _ _, hHgrt _⟩
  · have hsum : ((f.support.toList.map g).map fun p => p.1 ⊗ₜ[ℚ] p.2).sum =
        ∑ i ∈ f.support, B i ⊗ₜ H (B.coord i) := by
      rw [List.map_map, Finset.sum_map_toList]
      rfl
    have hLu : LinearMap.lTensor K (FF d).subtype u =
        ∑ i ∈ f.support, B i ⊗ₜ (f i : F2) := by
      conv_lhs => rw [basis_sum_eq B u]
      rw [map_sum]
      rfl
    have hLu' : LinearMap.lTensor K (FF d).subtype u =
        (1 : K) ⊗ₜ (x : F2) - LinearMap.lTensor K (FF d).subtype z := by
      rw [hu, map_sub, LinearMap.lTensor_tmul]
      rfl
    have e : ((f.support.toList.map g).map fun p => p.1 ⊗ₜ[ℚ] p.2).sum +
        LinearMap.lTensor K (FF d).subtype z - (1 : K) ⊗ₜ (x : F2) =
        -∑ i ∈ f.support, B i ⊗ₜ ((f i : F2) - H (B.coord i)) := by
      have e2 : ∑ i ∈ f.support, B i ⊗ₜ ((f i : F2) - H (B.coord i)) =
          LinearMap.lTensor K (FF d).subtype u - ∑ i ∈ f.support, B i ⊗ₜ H (B.coord i) := by
        rw [hLu, ← Finset.sum_sub_distrib]
        simp only [TensorProduct.tmul_sub]
      rw [e2, hLu', hsum]
      abel
    rw [e]
    refine neg_mem (Submodule.sum_mem _ fun i _ => tmul_mem_FFK _ ?_)
    rw [hf]
    exact hHdiff _

/-! ### The tower invariant and its step -/

variable (K) in
/-- **The tower invariant at degree `d`.** From level `d + 1` on, every `Ψ N` is a group-like
`K`-associator in `U4 N`, agrees with `1 ⊗ Φ` modulo `FFK d`, and agrees with the next member of
the tower modulo `FFK N`. -/
def TowerInv (E : F2) (d : ℕ) (Φ : F2) (Ψ : ℕ → K ⊗[ℚ] F2) : Prop :=
  FreeAlgebra.algebraMapInv Φ = 1 ∧ ∀ N, d + 1 ≤ N →
    AssocK K N E (Ψ N) ∧ GLK K N (Ψ N) ∧ Ψ N - (1 : K) ⊗ₜ Φ ∈ FFK K d ∧
      Ψ (N + 1) - Ψ N ∈ FFK K N

/-- Consecutive agreement gives agreement with any earlier member, modulo its level. -/
theorem sub_mem_FFK_of_consecutive {a : ℕ} {Ψ : ℕ → K ⊗[ℚ] F2}
    (h : ∀ N, a ≤ N → Ψ (N + 1) - Ψ N ∈ FFK K N) {N : ℕ} (hN : a ≤ N) :
    Ψ N - Ψ a ∈ FFK K a := by
  induction N, hN using Nat.le_induction with
  | base => simp
  | succ N hN ih =>
    have e : Ψ (N + 1) - Ψ a = (Ψ (N + 1) - Ψ N) + (Ψ N - Ψ a) := by abel
    rw [e]; exact add_mem (FFK_anti hN (h N hN)) ih

/-- **The induction step on the whole tower.** The same rational `x ∈ FF d` and the same list of
shifts work at every level, because the list is extracted from level `d + 1` alone and its
directions are in `grt` at every level. -/
theorem towerStep {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1) {d : ℕ} (hd : 1 ≤ d)
    {Φ : F2} {Ψ : ℕ → K ⊗[ℚ] F2} (h : TowerInv K E d Φ Ψ) :
    ∃ x ∈ FF d, AssocU4 (d + 1) E (Φ + x) ∧ GL (d + 1) (Φ + x) ∧
      ∃ Ψ' : ℕ → K ⊗[ℚ] F2, TowerInv K E (d + 1) (Φ + x) Ψ' := by
  obtain ⟨hΦ, hT⟩ := h
  obtain ⟨hK1, hGL1, hm1, -⟩ := hT (d + 1) le_rfl
  obtain ⟨z, hz⟩ := exists_lTensor_of_mem_FFK (FFK_anti (le_refl d) hm1)
  rw [hz] at hK1 hGL1
  obtain ⟨x, hx, hassoc, L, hL, hLsum⟩ := stepData hd hE hΦ z hK1
    (primLayer_of_GLK hd hΦ z hGL1)
  have hcons : ∀ N, d + 1 ≤ N → Ψ (N + 1) - Ψ N ∈ FFK K N := fun N hN => (hT N hN).2.2.2
  let Ψ' : ℕ → K ⊗[ℚ] F2 := fun N => shiftL (N + 2) L (Ψ N)
  have hL1 : ∀ p ∈ L, p.2 ∈ FF 1 := fun p hp => FF_anti hd (hL p hp).1
  have hgrt : ∀ p ∈ L, ∀ N (r : ℚ), GRT1U4 N (expPoly (r • p.2) (N + 2)) :=
    fun p hp N r => grt1U4_expPoly ((hL p hp).2.2 N) (by omega) (by omega) r
  have key : ∀ N, d + 1 ≤ N → AssocK K N E (Ψ' N) ∧ GLK K N (Ψ' N) ∧
      Ψ' N - (1 : K) ⊗ₜ (Φ + x) ∈ FFK K (d + 1) := by
    intro N hN
    obtain ⟨M, rfl⟩ : ∃ M, N = M + 1 := ⟨N - 1, by omega⟩
    obtain ⟨hK, hGL, -, -⟩ := hT (M + 1) hN
    have hAG : AssocK K (M + 1) E (Ψ' (M + 1)) ∧ GLK K (M + 1) (Ψ' (M + 1)) :=
      shiftL_pred (fun Ψ => AssocK K (M + 1) E Ψ ∧ GLK K (M + 1) Ψ) L
        (fun p hp Ψ hΨ => ⟨assocK_shiftK hΨ.1 (hgrt p hp (M + 1)) p.1,
          GLK.compKK_GK hΨ.2 (hL1 p hp) (hL p hp).2.1 (by omega) (hgrt p hp (M + 1)) p.1⟩)
        ⟨hK, hGL⟩
    refine ⟨hAG.1, hAG.2, ?_⟩
    have hs := shiftL_sum hd (n := M + 1 + 2) (by omega) L (fun p hp => (hL p hp).1)
      hK.sub_one_mem_FFK
    have hc := sub_mem_FFK_of_consecutive hcons hN
    have e : Ψ' (M + 1) - (1 : K) ⊗ₜ (Φ + (x : F2)) =
        (shiftL (M + 1 + 2) L (Ψ (M + 1)) - Ψ (M + 1) -
            (L.map fun p => p.1 ⊗ₜ[ℚ] p.2).sum) +
          (Ψ (M + 1) - Ψ (d + 1)) +
          ((L.map fun p => p.1 ⊗ₜ[ℚ] p.2).sum + LinearMap.lTensor K (FF d).subtype z -
            (1 : K) ⊗ₜ x) := by
      rw [hz, TensorProduct.tmul_add]; abel
    rw [e]
    exact add_mem (add_mem hs hc) hLsum
  refine ⟨x, hx, hassoc, ?_, Ψ', algebraMapInv_add_of_mem_FF hd hΦ hx, fun N hN => ?_⟩
  · obtain ⟨-, hGL, hm⟩ := key (d + 2) (by omega)
    exact GL_of_GLK (GLK.congr (GLK.anti (by omega) hGL) hm)
  · obtain ⟨hA, hG, hm⟩ := key N (by omega)
    refine ⟨hA, hG, hm, ?_⟩
    exact shiftL_sub_mem (by omega) (by omega) L hL1 (hcons N (by omega))

/-! ### Dependent choice along `ℕ` -/

/-- A sequence built by choosing a successor at each step. -/
theorem exists_seq_of_step {α : Type*} (P : ℕ → α → Prop) (R : ℕ → α → α → Prop) {a₀ : α}
    (h₀ : P 0 a₀) (h : ∀ k a, P k a → ∃ b, P (k + 1) b ∧ R k a b) :
    ∃ f : ℕ → α, f 0 = a₀ ∧ ∀ k, P k (f k) ∧ R k (f k) (f (k + 1)) := by
  choose g hg using h
  let F : (k : ℕ) → {a : α // P k a} := fun k =>
    Nat.rec (motive := fun k => {a : α // P k a}) ⟨a₀, h₀⟩
      (fun k ih => ⟨g k ih.1 ih.2, (hg k ih.1 ih.2).1⟩) k
  exact ⟨fun k => (F k).1, rfl, fun k => ⟨(F k).2, (hg k (F k).1 (F k).2).2⟩⟩

/-! ### The compatible tower -/

variable (K) in
/-- **The analytic input, strengthened to a compatible tower.** A sequence of `K`-associators
`Ψ N`, group-like, for every `N ≥ 2`, whose consecutive members agree modulo `FFK K N`. The
truncations of one group-like associator in the completed algebra (for `K = ℂ`, `E = exp`:
Drinfeld's KZ associator) form such a sequence; nothing in this repository constructs it, and it
is not asserted here. -/
structure CompatibleGroupLikeKAssociatorTower (E : F2) : Prop where
  exists_tower : ∃ Ψ : ℕ → K ⊗[ℚ] F2, ∀ N : ℕ, 2 ≤ N →
    AssocK K N E (Ψ N) ∧ GLK K N (Ψ N) ∧ Ψ (N + 1) - Ψ N ∈ FFK K N

/-- A compatible tower is in particular a tower. -/
theorem CompatibleGroupLikeKAssociatorTower.toTower {E : F2}
    (hT : CompatibleGroupLikeKAssociatorTower K E) : GroupLikeKAssociatorTower K E := by
  obtain ⟨Ψ, hΨ⟩ := hT.exists_tower
  exact ⟨fun N hN => ⟨Ψ N, (hΨ N hN).1, (hΨ N hN).2.1⟩⟩

/-- **A compatible sequence of rational associators, conditional on a compatible tower of
`K`-associators.** If for some field extension `K/ℚ` there is a compatible tower of group-like
`K`-associators for `E` (`ε(E) = 1`), then there is one sequence `Φ : ℕ → ℚ⟨X, Y⟩` with
`Φ N` an associator in `U4 N` for `E` and group-like modulo `FF2 N` for every `N ≥ 2`, and with
`Φ (N + 1) − Φ N ∈ FF N` for every `N ≥ 1` (compatible truncations). -/
theorem rational_associator_compatible_of_tower {E : F2} (hE : FreeAlgebra.algebraMapInv E = 1)
    (hT : CompatibleGroupLikeKAssociatorTower K E) :
    ∃ Φ : ℕ → F2, (∀ N, 2 ≤ N → AssocU4 N E (Φ N) ∧ GL N (Φ N)) ∧
      ∀ N, 1 ≤ N → Φ (N + 1) - Φ N ∈ FF N := by
  obtain ⟨Ψ₀, hΨ₀⟩ := hT.exists_tower
  have h₀ : TowerInv K E 1 1 Ψ₀ := by
    refine ⟨map_one _, fun N hN => ⟨(hΨ₀ N hN).1, (hΨ₀ N hN).2.1, ?_, (hΨ₀ N hN).2.2⟩⟩
    rw [← Algebra.TensorProduct.one_def]
    exact (hΨ₀ N hN).1.sub_one_mem_FFK
  obtain ⟨f, -, hf⟩ := exists_seq_of_step (α := F2 × (ℕ → K ⊗[ℚ] F2))
    (fun k a => TowerInv K E (k + 1) a.1 a.2)
    (fun k a b => b.1 - a.1 ∈ FF (k + 1) ∧ AssocU4 (k + 2) E b.1 ∧ GL (k + 2) b.1)
    (a₀ := (1, Ψ₀)) h₀ (fun k a ha => by
      obtain ⟨x, hx, hA, hG, Ψ', hΨ'⟩ := towerStep hE (by omega) ha
      exact ⟨(a.1 + x, Ψ'), hΨ', by simpa using hx, hA, hG⟩)
  refine ⟨fun N => (f (N - 1)).1, fun N hN => ?_, fun N hN => ?_⟩
  · obtain ⟨k, rfl⟩ : ∃ k, N = k + 2 := ⟨N - 2, by omega⟩
    have := (hf k).2
    simpa using this.2
  · obtain ⟨k, rfl⟩ : ∃ k, N = k + 1 := ⟨N - 1, by omega⟩
    simpa using (hf k).2.1

end QOU.BraidsAndKnots.RationalAssociator
