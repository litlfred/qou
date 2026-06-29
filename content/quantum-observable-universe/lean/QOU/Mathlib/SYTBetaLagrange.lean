import QOU.Mathlib.SYTLagrangeInterp

/-!
# QOU.Mathlib.SYTBetaLagrange — the β-Lagrange identity

The Greene–Nijenhuis–Wilf hook-summation identity reduces, in β-number coordinates, to the
self-contained `ℚ` **β-Lagrange identity**

    ∑ᵢ βᵢ · ∏_{j≠i} (βᵢ − 1 − βⱼ)/(βᵢ − βⱼ)  =  (∑ᵢ βᵢ) − C(k,2).

This file assembles it on the Lagrange leading-coefficient keystone
(`SYTLagrangeInterp.interp_leadingCoeff`).

**Route.** Let `Q(X) = ∏ⱼ (X − βⱼ)` (vanishes at every node `βᵢ`, since the `j=i` factor is `0`) and
`G(X) = X · ∏ⱼ (X − (βⱼ+1))`, so `G(βᵢ) = βᵢ ∏ⱼ(βᵢ − 1 − βⱼ)`.  Removing the `j=i` factor flips a sign,
`∏_{j≠i}(βᵢ−1−βⱼ) = −∏ⱼ(βᵢ−1−βⱼ)`, so the left side is `−∑ᵢ G(βᵢ)/Dᵢ` with `Dᵢ = ∏_{j≠i}(βᵢ−βⱼ)`.
Writing `G = R + (X − C k)·Q` with `deg R < k` (the top two coefficients cancel by Vieta), the keystone
gives `∑ᵢ G(βᵢ)/Dᵢ = R.coeff (k−1) = C(k,2) − ∑βᵢ`, whence the identity.

Pure `ℚ` polynomial algebra; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.SYTBetaLagrange

open Polynomial Finset

variable {k : ℕ}

/-- `Q(X) = ∏ⱼ (X − βⱼ)` — the node polynomial. It vanishes at every node. -/
noncomputable def nodePoly (β : Fin k → ℚ) : ℚ[X] :=
  ∏ j, (X - C (β j))

/-- `Q` vanishes at every node `βᵢ` (the `j = i` factor is `βᵢ − βᵢ = 0`). -/
theorem nodePoly_eval (β : Fin k → ℚ) (i : Fin k) : (nodePoly β).eval (β i) = 0 := by
  unfold nodePoly
  rw [eval_prod]
  apply Finset.prod_eq_zero (mem_univ i)
  rw [eval_sub, eval_X, eval_C, sub_self]

/-- **Decomposition reduction.** If `G = R + H·Q` with `deg R < k`, then `∑ᵢ G(βᵢ)/Dᵢ = R.coeff (k−1)`:
`Q` kills the `H·Q` part at every node, and the keystone evaluates the `R` part. -/
theorem sum_eval_div_eq_of_decomp (β : Fin k → ℚ) (hβ : Function.Injective β) (hk : 0 < k)
    (G R H : ℚ[X]) (hR : R.natDegree < k) (hdec : G = R + H * nodePoly β) :
    ∑ i, G.eval (β i) / vWeight β i = R.coeff (k - 1) := by
  have hval : ∀ i, G.eval (β i) = R.eval (β i) := by
    intro i
    rw [hdec, eval_add, eval_mul, nodePoly_eval, mul_zero, add_zero]
  rw [Finset.sum_congr rfl (fun i _ => by rw [hval i])]
  exact interp_leadingCoeff β hβ hk R hR

/-- The shifted-node polynomial `∏ⱼ (X − (βⱼ+1))`, whose value at `βᵢ` is `∏ⱼ(βᵢ − 1 − βⱼ)`. -/
noncomputable def shiftPoly (β : Fin k → ℚ) : ℚ[X] :=
  ∏ j, (X - C (β j + 1))

/-- `G(X) = X · ∏ⱼ (X − (βⱼ+1))`: at a node, `G(βᵢ) = βᵢ · ∏ⱼ(βᵢ − 1 − βⱼ)`. -/
noncomputable def bigPoly (β : Fin k → ℚ) : ℚ[X] := X * shiftPoly β

/-- The residual `R = G − (X − C k)·Q`. -/
noncomputable def residPoly (β : Fin k → ℚ) : ℚ[X] :=
  bigPoly β - (X - C (k : ℚ)) * nodePoly β

theorem bigPoly_decomp (β : Fin k → ℚ) :
    bigPoly β = residPoly β + (X - C (k : ℚ)) * nodePoly β := by
  unfold residPoly; ring

/-- Value of `G` at a node: `G(βᵢ) = βᵢ · ∏ⱼ(βᵢ − 1 − βⱼ)`. -/
theorem bigPoly_eval (β : Fin k → ℚ) (i : Fin k) :
    (bigPoly β).eval (β i) = β i * ∏ j, (β i - 1 - β j) := by
  unfold bigPoly shiftPoly
  rw [eval_mul, eval_X, eval_prod]
  congr 1
  apply Finset.prod_congr rfl
  intro j _
  rw [eval_sub, eval_X, eval_C]
  ring

/-! ## Vieta coefficients of a product of monic linears -/

/-- `esymm s 1 = s.sum` (the singletons are the cardinality-`1` subsets). -/
theorem esymm_one (s : Multiset ℚ) : s.esymm 1 = s.sum := by
  unfold Multiset.esymm
  rw [Multiset.powersetCard_one, Multiset.map_map]
  simp [Function.comp]

/-- `∏ⱼ (X − fⱼ)` as a product over the node multiset, for Vieta. -/
theorem prodLin_eq (f : Fin k → ℚ) :
    (∏ j, (X - C (f j))) = ((Finset.univ.val.map f).map (fun a => X - C a)).prod := by
  have h : (∏ j, (X - C (f j))) = (Finset.univ.val.map (fun j => X - C (f j))).prod := rfl
  rw [h, Multiset.map_map]
  exact congrArg Multiset.prod (Multiset.map_congr rfl (fun x _ => rfl))

/-- The node multiset has cardinality `k`. -/
theorem nodes_card (f : Fin k → ℚ) : Multiset.card (Finset.univ.val.map f) = k := by
  rw [Multiset.card_map]; exact Finset.card_fin k

/-- `∏ⱼ (X − fⱼ)` is monic. -/
theorem prodLin_monic (f : Fin k → ℚ) : (∏ j, (X - C (f j))).Monic :=
  monic_prod_of_monic _ _ (fun j _ => monic_X_sub_C (f j))

/-- `∏ⱼ (X − fⱼ)` has degree `k`. -/
theorem prodLin_natDegree (f : Fin k → ℚ) : (∏ j, (X - C (f j))).natDegree = k := by
  rw [natDegree_prod _ _ (fun j _ => X_sub_C_ne_zero (f j))]
  simp [natDegree_X_sub_C, Finset.card_univ]

/-- The `Xᵏ` coefficient is `1` (monic of degree `k`). -/
theorem prodLin_coeff_k (f : Fin k → ℚ) : (∏ j, (X - C (f j))).coeff k = 1 := by
  have h := (prodLin_monic f).coeff_natDegree
  rwa [prodLin_natDegree f] at h

/-- Coefficients strictly above `k` vanish. -/
theorem prodLin_coeff_gt (f : Fin k → ℚ) {n : ℕ} (hn : k < n) :
    (∏ j, (X - C (f j))).coeff n = 0 :=
  coeff_eq_zero_of_natDegree_lt (by rw [prodLin_natDegree f]; exact hn)

/-- **Vieta top coefficient.** `[Xᵏ⁻¹] ∏ⱼ(X − fⱼ) = −∑ⱼ fⱼ`. -/
theorem prodLin_coeff_top (f : Fin k → ℚ) (hk : 0 < k) :
    (∏ j, (X - C (f j))).coeff (k - 1) = - ∑ j, f j := by
  have hs : ((Finset.univ.val.map f).esymm 1) = ∑ j, f j := esymm_one _
  rw [prodLin_eq f, Multiset.prod_X_sub_C_coeff _ (by rw [nodes_card f]; omega), nodes_card f,
      show k - (k - 1) = 1 from by omega, pow_one, hs, neg_one_mul]

/-- `∑ⱼ (βⱼ + 1) = (∑ⱼ βⱼ) + k`. -/
theorem sum_shift (β : Fin k → ℚ) : (∑ j, (β j + 1)) = (∑ j, β j) + k := by
  rw [Finset.sum_add_distrib]; simp [Finset.card_univ]

/-! ## Coefficient wrappers for `nodePoly` (roots `βⱼ`) and `shiftPoly` (roots `βⱼ+1`) -/

theorem nodePoly_coeff_top (β : Fin k → ℚ) (hk : 0 < k) :
    (nodePoly β).coeff (k - 1) = - ∑ j, β j := prodLin_coeff_top β hk
theorem nodePoly_coeff_k (β : Fin k → ℚ) : (nodePoly β).coeff k = 1 := prodLin_coeff_k β
theorem nodePoly_coeff_gt (β : Fin k → ℚ) {n : ℕ} (hn : k < n) : (nodePoly β).coeff n = 0 :=
  prodLin_coeff_gt β hn
theorem shiftPoly_coeff_top (β : Fin k → ℚ) (hk : 0 < k) :
    (shiftPoly β).coeff (k - 1) = - (∑ j, β j) - k := by
  have h : (shiftPoly β).coeff (k - 1) = - ∑ j, (β j + 1) := prodLin_coeff_top (fun j => β j + 1) hk
  rw [h, sum_shift]; ring
theorem shiftPoly_coeff_k (β : Fin k → ℚ) : (shiftPoly β).coeff k = 1 := prodLin_coeff_k _
theorem shiftPoly_coeff_gt (β : Fin k → ℚ) {n : ℕ} (hn : k < n) : (shiftPoly β).coeff n = 0 :=
  prodLin_coeff_gt _ hn

/-- **(Vieta, residual degree)** The residual has degree `< k`: the `Xᵏ⁺¹` and `Xᵏ` coefficients of
`G` and `(X − C k)·Q` cancel. -/
theorem residPoly_natDegree_lt (β : Fin k → ℚ) (hk : 0 < k) :
    (residPoly β).natDegree < k := by
  have hle : (residPoly β).natDegree ≤ k - 1 := by
    rw [natDegree_le_iff_coeff_eq_zero]
    intro m hm
    have hmk : k ≤ m := by omega
    obtain ⟨j, rfl⟩ : ∃ j, m = j + 1 := ⟨m - 1, by omega⟩
    have hjk : k - 1 ≤ j := by omega
    unfold residPoly bigPoly
    rw [coeff_sub, coeff_X_mul,
        show (X - C (k:ℚ)) * nodePoly β = X * nodePoly β - C (k:ℚ) * nodePoly β from by ring,
        coeff_sub, coeff_X_mul, coeff_C_mul]
    rcases Nat.lt_trichotomy j k with hlt | heq | hgt
    · have hj : j = k - 1 := by omega
      subst hj
      rw [shiftPoly_coeff_top β hk, nodePoly_coeff_top β hk,
          show (k - 1) + 1 = k from by omega, nodePoly_coeff_k β]
      ring
    · subst heq
      rw [shiftPoly_coeff_k β, nodePoly_coeff_k β, nodePoly_coeff_gt β (by omega)]
      ring
    · rw [shiftPoly_coeff_gt β hgt, nodePoly_coeff_gt β hgt, nodePoly_coeff_gt β (by omega)]
      ring
  exact lt_of_le_of_lt hle (by omega)

/-! ## The `e₂` Vieta shift — proved from scratch (no `NewtonIdentities`/`Taylor`/`HasseDeriv` olean) -/

/-- The number of `2`-subsets of `Fin k` containing a fixed element is `k − 1` (bijection with the
other element, `j ↦ {i, j}` over `univ.erase i`). -/
theorem count_pairs (i : Fin k) :
    (((univ : Finset (Fin k)).powersetCard 2).filter (fun t => i ∈ t)).card = k - 1 := by
  have hset : ((univ : Finset (Fin k)).powersetCard 2).filter (fun t => i ∈ t)
      = (univ.erase i).image (fun j => ({i, j} : Finset (Fin k))) := by
    ext t
    simp only [mem_filter, mem_powersetCard, mem_image, mem_erase]
    constructor
    · rintro ⟨⟨-, hcard⟩, hi⟩
      obtain ⟨a, b, hab, rfl⟩ := card_eq_two.mp hcard
      rcases mem_insert.mp hi with h | h
      · exact ⟨b, ⟨(by rintro rfl; exact hab h.symm), mem_univ b⟩, by rw [h]⟩
      · rw [mem_singleton] at h
        exact ⟨a, ⟨(by rintro rfl; exact hab h), mem_univ a⟩, by rw [h, Finset.pair_comm]⟩
    · rintro ⟨j, ⟨hji, -⟩, rfl⟩
      refine ⟨⟨subset_univ _, ?_⟩, mem_insert_self i {j}⟩
      rw [card_insert_of_not_mem (by simp [Ne.symm hji]), card_singleton]
  have hinj : Set.InjOn (fun j => ({i, j} : Finset (Fin k))) ↑(univ.erase i) := by
    intro a ha b hb hab
    simp only [mem_coe, mem_erase] at ha hb
    dsimp only at hab
    have hb2 : b ∈ ({i, a} : Finset (Fin k)) := by
      rw [hab]; exact mem_insert_of_mem (mem_singleton_self b)
    rcases mem_insert.mp hb2 with h | h
    · exact absurd h hb.1
    · exact (mem_singleton.mp h).symm
  rw [hset, Finset.card_image_of_injOn hinj, Finset.card_erase_of_mem (mem_univ i), card_univ,
      Fintype.card_fin]

/-- `∑_{t : 2-subset} (∑_{i∈t} βᵢ + 1) = (k−1)·∑β + C(k,2)` — the double-count: each element lies in
`k−1` of the `2`-subsets, and there are `C(k,2)` of them. -/
theorem sum_pairs_eval (β : Fin k → ℚ) :
    ∑ t ∈ univ.powersetCard 2, ((∑ i ∈ t, β i) + 1)
      = ((k - 1 : ℕ) : ℚ) * (∑ i, β i) + (k.choose 2 : ℚ) := by
  rw [Finset.sum_add_distrib]
  congr 1
  · have hin : ∀ t ∈ univ.powersetCard 2, (∑ i ∈ t, β i)
        = ∑ i, (if i ∈ t then β i else 0) := by
      intro t _
      rw [Finset.sum_ite_mem, Finset.univ_inter]
    rw [Finset.sum_congr rfl hin, Finset.sum_comm, Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i _
    rw [← Finset.sum_filter, Finset.sum_const, count_pairs i, nsmul_eq_mul]
  · rw [Finset.sum_const, Finset.card_powersetCard, card_univ, Fintype.card_fin, nsmul_eq_mul,
        mul_one]

/-- On a `2`-element set, `∏(βᵢ+1) − ∏βᵢ = (∑βᵢ) + 1`. -/
theorem pair_diff (β : Fin k → ℚ) {t : Finset (Fin k)} (ht : t.card = 2) :
    (∏ i ∈ t, (β i + 1)) - (∏ i ∈ t, β i) = (∑ i ∈ t, β i) + 1 := by
  obtain ⟨a, b, hab, rfl⟩ := Finset.card_eq_two.mp ht
  rw [Finset.prod_pair hab, Finset.prod_pair hab, Finset.sum_pair hab]; ring

/-- **The `e₂` shift.** `e₂(β+1) − e₂(β) = (k−1)·∑β + C(k,2)`, via the `powersetCard 2` definition of
`esymm` (`esymm_map_val`), `pair_diff` per `2`-subset, and `sum_pairs_eval`. -/
theorem esymm2_shift (β : Fin k → ℚ) :
    (univ.val.map (fun i => β i + 1)).esymm 2 - (univ.val.map β).esymm 2
      = ((k - 1 : ℕ) : ℚ) * (∑ i, β i) + (k.choose 2 : ℚ) := by
  rw [esymm_map_val, esymm_map_val, ← Finset.sum_sub_distrib,
      Finset.sum_congr rfl (fun t ht => pair_diff β (Finset.mem_powersetCard.mp ht).2),
      sum_pairs_eval]

/-- **Vieta at index `k−2`.** `[Xᵏ⁻²] ∏ⱼ(X − fⱼ) = e₂(f)`. -/
theorem prodLin_coeff_2 (f : Fin k → ℚ) (hk : 2 ≤ k) :
    (∏ j, (X - C (f j))).coeff (k - 2) = (univ.val.map f).esymm 2 := by
  rw [prodLin_eq f, Multiset.prod_X_sub_C_coeff _ (by rw [nodes_card f]; omega), nodes_card f,
      show k - (k - 2) = 2 from by omega]
  norm_num

/-- **(Vieta, residual leading coefficient — proved.)** `R.coeff (k−1) = C(k,2) − ∑ⱼ βⱼ`.  This was the
last open step of the β-Lagrange identity; the whole cone is now sorry-free.

For `k ≥ 2`, `R.coeff (k−1) = shiftPoly.coeff (k−2) − nodePoly.coeff (k−2) + k·nodePoly.coeff (k−1)`
(`coeff_X_mul`/`coeff_C_mul`); by Vieta the two `coeff (k−2)` are `e₂(β+1)`/`e₂(β)`, whose difference is
`esymm2_shift`; with `nodePoly.coeff (k−1) = −∑β` the result is `(k−1)∑β + C(k,2) − k∑β = C(k,2) − ∑β`.
`k = 1` is the direct `R.coeff 0 = −β₀ = C(1,2) − β₀`. -/
theorem residPoly_coeff (β : Fin k → ℚ) (hk : 0 < k) :
    (residPoly β).coeff (k - 1) = (k.choose 2 : ℚ) - ∑ j, β j := by
  rcases Nat.lt_or_ge k 2 with hk1 | hk2
  · have hk1' : k = 1 := by omega
    subst hk1'
    have hnode : (nodePoly β).coeff 0 = - ∑ j, β j := nodePoly_coeff_top β hk
    unfold residPoly bigPoly
    simp only [Nat.sub_self, coeff_sub, Polynomial.mul_coeff_zero, coeff_X_zero, zero_mul,
      Polynomial.coeff_C_zero]
    rw [hnode]
    norm_num
  · have hsc2 : (shiftPoly β).coeff (k - 2) = (univ.val.map (fun i => β i + 1)).esymm 2 :=
      prodLin_coeff_2 (fun i => β i + 1) hk2
    have hnc2 : (nodePoly β).coeff (k - 2) = (univ.val.map β).esymm 2 := prodLin_coeff_2 β hk2
    have hnc1 : (nodePoly β).coeff (k - 1) = - ∑ j, β j := nodePoly_coeff_top β hk
    have hk1eq : k - 1 = (k - 2) + 1 := by omega
    unfold residPoly bigPoly
    rw [coeff_sub, hk1eq, coeff_X_mul,
        show (X - C (k:ℚ)) * nodePoly β = X * nodePoly β - C (k:ℚ) * nodePoly β from by ring,
        coeff_sub, coeff_X_mul, coeff_C_mul, ← hk1eq, hsc2, hnc2, hnc1]
    have hs := esymm2_shift β
    rw [Nat.cast_sub (by omega : (1:ℕ) ≤ k)] at hs
    push_cast at hs
    rw [show (univ.val.map (fun i => β i + 1)).esymm 2
          = (univ.val.map β).esymm 2 + (((k:ℚ) - 1) * (∑ i, β i) + (k.choose 2 : ℚ)) from by
        rw [← hs]; ring]
    ring

/-- Removing the `j = i` factor from `∏ⱼ(βᵢ − 1 − βⱼ)` flips a sign (that factor is `βᵢ−1−βᵢ = −1`). -/
theorem prod_erase_eq_neg (β : Fin k → ℚ) (i : Fin k) :
    ∏ j ∈ univ.erase i, (β i - 1 - β j) = - ∏ j, (β i - 1 - β j) := by
  rw [← Finset.mul_prod_erase univ _ (mem_univ i)]
  have : β i - 1 - β i = -1 := by ring
  rw [this]
  ring

/-- **The β-Lagrange identity.** For distinct nodes `β : Fin k → ℚ` (`k ≥ 1`),

    ∑ᵢ βᵢ · ∏_{j≠i}(βᵢ − 1 − βⱼ)/(βᵢ − βⱼ)  =  (∑ⱼ βⱼ) − C(k,2).

The self-contained `ℚ` partial-fractions identity the GNW hook-summation identity reduces to. -/
theorem betaLagrange (β : Fin k → ℚ) (hβ : Function.Injective β) (hk : 0 < k) :
    ∑ i, β i * (∏ j ∈ univ.erase i, (β i - 1 - β j)) / vWeight β i
      = (∑ j, β j) - (k.choose 2 : ℚ) := by
  -- rewrite each summand to −G(βᵢ)/Dᵢ via the sign flip
  have hrw : ∀ i, β i * (∏ j ∈ univ.erase i, (β i - 1 - β j)) / vWeight β i
      = - ((bigPoly β).eval (β i) / vWeight β i) := by
    intro i
    rw [prod_erase_eq_neg, bigPoly_eval, mul_neg, neg_div]
  calc ∑ i, β i * (∏ j ∈ univ.erase i, (β i - 1 - β j)) / vWeight β i
      = ∑ i, - ((bigPoly β).eval (β i) / vWeight β i) :=
        Finset.sum_congr rfl (fun i _ => hrw i)
    _ = - ∑ i, (bigPoly β).eval (β i) / vWeight β i := by rw [Finset.sum_neg_distrib]
    _ = - (residPoly β).coeff (k - 1) := by
        rw [sum_eval_div_eq_of_decomp β hβ hk (bigPoly β) (residPoly β) (X - C (k : ℚ))
              (residPoly_natDegree_lt β hk) (bigPoly_decomp β)]
    _ = (∑ j, β j) - (k.choose 2 : ℚ) := by rw [residPoly_coeff β hk]; ring

end QOU.Mathlib.SYTBetaLagrange
