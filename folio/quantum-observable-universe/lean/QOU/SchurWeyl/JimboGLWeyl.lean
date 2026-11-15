/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.JimboGL

/-!
# Wenzl's weights from the tensor representation

`JimboGL.jimboTrace_eq_wenzl` identifies the normalised `K`-weighted trace of the `gl_d` Jimbo
action on `V^{⊗n}`, `V = K^d`, with the level-`d` Wenzl trace
`Σ_λ wenzlWeight d (q²) λ · χ_λ`.  This file reads the weights off the representation.

For a partition `λ ⊢ n` and a standard tableau `t` of shape `λ`, let `E ∈ H_n(q)` be the element
whose seminormal image is the matrix unit `E_{tt}` in block `λ` and `0` in every other block (it
exists and is unique because the seminormal product map is bijective).  Then `E` is idempotent and

`Tr(K^{⊗n} ρ(E)) = s_λ(1, q², …, q^{2(d−1)})`   (`qtr_jimbo_blockIdempotent`),

the principal specialisation `schurPrincipal d (q²) λ`.  `ρ(E)` is an idempotent commuting with
`K^{⊗n}` (`dMat_commute_jimbo`), so the left side is the trace of `K^{⊗n}` on the subspace
`ρ(E) V^{⊗n}`: a copy of the multiplicity space of `S_λ` in `V^{⊗n}`.  This is the `q`-Weyl
character formula for the multiplicity spaces, proved from the trace identification alone.

## What this does and does not discharge

* Wenzl's weights are here a **theorem about the tensor representation**: the `K`-graded
  multiplicities are `s_λ(1, q², …)`, unnormalised; the normalised Markov weight is
  `s_λ / [d]_{q²}^{|λ|}`.
* `QBeta.WenzlWeight.IsOcneanuWeightSystem` asks for a **single** normaliser `Z` for all sizes.
  The normalised weights cannot satisfy it (`SchurWeyl.not_isOcneanuWeightSystem`, at `d = 2`); the
  unnormalised ones satisfy it with `Z = 1`, which is already
  `QBeta.WenzlWeight.isOcneanuWeightSystem_schurPrincipal`.  So this file
  does not change which `[IsOcneanuWeightSystem]` hypotheses can be dropped; the class's
  normalisation is an authoring question (see the PR).
* Surjectivity onto the `U_q(gl_d)` commutant is not used and not proved.

## Base ring (§7c)

Any field of characteristic zero (the seminormal product map needs `CharZero`), `q` not a root of
unity.  No order.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
-- Ref: [jimbo1986] M. Jimbo, Lett. Math. Phys. 11 (1986) 247–252.
-/

namespace QOU.SchurWeyl.JimboGL

open QOU.SchurWeyl QOU.Mathlib YoungDiagram SeminormalRep

variable {K : Type*} [Field K] [CharZero K] {d : ℕ} [NeZero d]

/-- **The `K`-graded multiplicity of `S_λ` in `(K^d)^{⊗n}` is `s_λ(1, q², …, q^{2(d−1)})`.**

For the block idempotent `E` (seminormal image `E_{tt}` in block `λ`, `0` in every other block),
`E² = E` and `Tr(K^{⊗(m+1)} ρ(E)) = schurPrincipal d (q²) λ`. -/
theorem qtr_jimbo_blockIdempotent (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (lam : Nat.Partition (m + 1)) (t : StandardYoungTableau (partitionShape lam)) :
    ∃ E : Hecke K q q⁻¹ m,
      E * E = E ∧
      heckeProduct q hq hq2 m E lam = Matrix.single t t 1 ∧
      (∀ mu, mu ≠ lam → heckeProduct q hq hq2 m E mu = 0) ∧
      qtr q (jimbo d q hq m E) = QBeta.WenzlWeight.schurPrincipal d (q ^ 2) (partitionShape lam) := by
  classical
  obtain ⟨E, hE⟩ := heckeProduct_surjective q hq hq2 m (Function.update 0 lam (Matrix.single t t 1))
  refine ⟨E, ?_, by rw [hE]; simp, fun mu hmu => by rw [hE]; simp [Function.update_of_ne hmu], ?_⟩
  · apply heckeProduct_injective q hq hq2 m
    rw [map_mul, hE]
    funext mu
    by_cases h : mu = lam
    · subst h; simp
    · simp [Function.update_of_ne h]
  · have hL : levelBracket d (q ^ 2) ≠ 0 :=
      levelBracket_ne_zero_of_gen (gen_of_notRootOfUnity hq2) (NeZero.ne d)
    have htr := jimboTrace_eq_wenzl (d := d) q hq hq2 m E
    rw [jimboTrace_apply, wtraceW_apply] at htr
    rw [← Equiv.sum_comp (partitionShapeEquiv (m + 1))
      (fun ν : {ν : YoungDiagram // ν.cells.card = m + 1} =>
        wenzlWeight d (q ^ 2) ν.1 * (seminormalRep q hq hq2 m ν.2 E).trace)] at htr
    have hρ : ∀ (mu : Nat.Partition (m + 1)),
        seminormalRep q hq hq2 m (partitionShapeEquiv (m + 1) mu).2 E
          = heckeProduct q hq hq2 m E mu := fun _ => rfl
    simp only [hρ, hE] at htr
    rw [Finset.sum_eq_single_of_mem lam (Finset.mem_univ lam)
      (fun mu _ hmu => by simp [Function.update_of_ne hmu])] at htr
    have h1 : wenzlWeight d (q ^ 2) (partitionShapeEquiv (m + 1) lam).1
        = wenzlWeight d (q ^ 2) (partitionShape lam) := rfl
    rw [h1, Function.update_self, Matrix.trace_single_eq_same, mul_one] at htr
    rw [wenzlWeight, partitionShape_card_succ] at htr
    have hp : levelBracket d (q ^ 2) ^ (m + 1) ≠ 0 := pow_ne_zero _ hL
    field_simp at htr
    exact htr

/-! ## The size-indexed normalisation, derived

`IsOcneanuWeightSystem` asked for one normaliser `Z` for every size, which no normalised family can
satisfy.  The correct normaliser depends on the size `n = m + 1`, and it is not chosen: it is forced.

* `blockE` — a fixed choice of block idempotent `E_{λ,t}` for every `λ ⊢ n` and standard tableau
  `t`; `sum_blockE`: they sum to `1` (semisimplicity: `heckeProduct` is bijective).
* `sum_card_mul_schurPrincipal` — applying `X ↦ Tr(K^{⊗n} ρ(X))` to `Σ E_{λ,t} = 1` gives the
  principal specialisation of the Schur–Weyl character identity
  `Σ_λ f^λ s_λ(1, q², …, q^{2(d−1)}) = [d]_{q²}^n = (Tr K)^n`.
* `markov_tr_blockE` — for **any** Markov trace family at Wenzl's level-`d` parameter,
  `tr(E_{λ,t}) = s_λ(1, q², …) / [d]_{q²}^n`: the actual Ocneanu weight of `λ`.
* `normaliser_eq` — if the weights of such a trace are `s_λ / Z` for one `Z ≠ 0` at size `n`,
  then `Z = [d]_{q²}^n`.  The normalisation `tr(1) = 1` leaves no freedom.

Inputs: G1 (`jimboMarkov`, `jimboTrace_eq_wenzl`), G2 (`qtr_jimbo_blockIdempotent`),
`heckeProduct` bijectivity and `markovTrace_unique`.  No fitted quantity enters. -/

/-- A fixed block idempotent `E_{λ,t}`. -/
noncomputable def blockE (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ)
    (lam : Nat.Partition (m + 1)) (t : StandardYoungTableau (partitionShape lam)) :
    Hecke K q q⁻¹ m :=
  Classical.choose
    (heckeProduct_surjective q hq hq2 m (Function.update 0 lam (Matrix.single t t 1)))

theorem heckeProduct_blockE (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (lam : Nat.Partition (m + 1)) (t : StandardYoungTableau (partitionShape lam))
    (mu : Nat.Partition (m + 1)) :
    heckeProduct q hq hq2 m (blockE q hq hq2 m lam t) mu
      = Function.update (0 : ∀ ν : Nat.Partition (m + 1),
          Matrix (StandardYoungTableau (partitionShape ν))
            (StandardYoungTableau (partitionShape ν)) K) lam (Matrix.single t t 1) mu :=
  congrFun (Classical.choose_spec
    (heckeProduct_surjective q hq hq2 m (Function.update 0 lam (Matrix.single t t 1)))) mu

theorem qtr_jimbo_blockE (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (lam : Nat.Partition (m + 1)) (t : StandardYoungTableau (partitionShape lam)) :
    qtr q (jimbo d q hq m (blockE q hq hq2 m lam t))
      = QBeta.WenzlWeight.schurPrincipal d (q ^ 2) (partitionShape lam) := by
  classical
  obtain ⟨E, -, h1, h2, hv⟩ := qtr_jimbo_blockIdempotent (d := d) q hq hq2 m lam t
  have hEq : blockE q hq hq2 m lam t = E := by
    apply heckeProduct_injective q hq hq2 m
    funext mu
    rw [heckeProduct_blockE]
    by_cases h : mu = lam
    · subst h; rw [Function.update_self, h1]
    · rw [Function.update_of_ne h, h2 mu h]; rfl
  rw [hEq, hv]

theorem sum_single_diag {ι : Type*} [Fintype ι] [DecidableEq ι] :
    (∑ t : ι, Matrix.single t t (1 : K)) = 1 := by
  ext i j
  rw [Matrix.sum_apply]
  by_cases h : i = j
  · subst h; simp [Matrix.single]
  · rw [Matrix.one_apply_ne h]
    refine Finset.sum_eq_zero fun x _ => ?_
    simp only [Matrix.single, Matrix.of_apply]
    rw [if_neg]
    rintro ⟨rfl, rfl⟩; exact h rfl

/-- **The block idempotents sum to `1`.** -/
theorem sum_blockE (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    (∑ lam : Nat.Partition (m + 1), ∑ t : StandardYoungTableau (partitionShape lam),
      blockE q hq hq2 m lam t) = 1 := by
  classical
  apply heckeProduct_injective q hq hq2 m
  rw [map_one, map_sum]
  funext mu
  simp only [Finset.sum_apply, map_sum, heckeProduct_blockE, Pi.one_apply]
  rw [Finset.sum_eq_single_of_mem mu (Finset.mem_univ mu)]
  · simp only [Function.update_self]
    exact sum_single_diag
  · intro lam _ hlam
    exact Finset.sum_eq_zero fun t _ => by rw [Function.update_of_ne (Ne.symm hlam)]; rfl

/-- **The Schur–Weyl character identity at the principal specialisation, derived**:
`Σ_{λ ⊢ n} f^λ s_λ(1, q², …, q^{2(d−1)}) = [d]_{q²}^n`. -/
theorem sum_card_mul_schurPrincipal (q : K) (hq : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) :
    ∑ lam : Nat.Partition (m + 1),
        (Fintype.card (StandardYoungTableau (partitionShape lam)) : K)
          * QBeta.WenzlWeight.schurPrincipal d (q ^ 2) (partitionShape lam)
      = levelBracket d (q ^ 2) ^ (m + 1) := by
  have h := congrArg (fun X => qtrLin d q (m + 1) (jimbo d q hq m X)) (sum_blockE q hq hq2 m)
  simp only [map_sum, map_one] at h
  change ∑ lam, ∑ t, qtr q (jimbo d q hq m (blockE q hq hq2 m lam t)) = qtr q 1 at h
  rw [qtr_one] at h
  rw [← h]
  refine Finset.sum_congr rfl fun lam _ => ?_
  simp only [qtr_jimbo_blockE, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]

/-- **The actual Ocneanu weight of `λ`** under any Markov trace at Wenzl's level-`d` parameter:
`tr(E_{λ,t}) = s_λ(1, q², …, q^{2(d−1)}) / [d]_{q²}^n`. -/
theorem markov_tr_blockE (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ ((q ^ 2) ^ d / (q * levelBracket d (q ^ 2))))
    (m : ℕ) (lam : Nat.Partition (m + 1)) (t : StandardYoungTableau (partitionShape lam)) :
    T.tr m (blockE q hq hq2 m lam t)
      = QBeta.WenzlWeight.schurPrincipal d (q ^ 2) (partitionShape lam)
          / levelBracket d (q ^ 2) ^ (m + 1) := by
  have hL : levelBracket d (q ^ 2) ≠ 0 :=
    levelBracket_ne_zero_of_gen (gen_of_notRootOfUnity hq2) (NeZero.ne d)
  rw [HeckeCoset.markovTrace_unique T (jimboMarkov q hq hL) m, jimboMarkov]
  show jimboTrace d q hq m _ = _
  rw [jimboTrace_apply, qtr_jimbo_blockE, inv_mul_eq_div]

/-- **The normaliser is forced to be `[d]_{q²}^n`.**  If at size `n = m + 1` the weights of a Markov
trace are `s_λ / Z` for a single `Z ≠ 0`, then `Z = [d]_{q²}^n`: `tr(1) = 1` and the character
identity leave no freedom. -/
theorem normaliser_eq (q : K) (hq : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ ((q ^ 2) ^ d / (q * levelBracket d (q ^ 2))))
    (m : ℕ) (Z : K) (hZ : Z ≠ 0)
    (hw : ∀ lam t, T.tr m (blockE q hq hq2 m lam t)
      = QBeta.WenzlWeight.schurPrincipal d (q ^ 2) (partitionShape lam) / Z) :
    Z = levelBracket d (q ^ 2) ^ (m + 1) := by
  have h1 := congrArg (T.tr m) (sum_blockE q hq hq2 m)
  rw [T.tr_one, map_sum] at h1
  simp only [map_sum, hw, Finset.sum_const, Finset.card_univ, nsmul_eq_mul] at h1
  rw [← sum_card_mul_schurPrincipal (d := d) q hq hq2 m]
  have h2 : (∑ lam : Nat.Partition (m + 1),
      (Fintype.card (StandardYoungTableau (partitionShape lam)) : K)
        * QBeta.WenzlWeight.schurPrincipal d (q ^ 2) (partitionShape lam)) / Z = 1 := by
    rw [Finset.sum_div]; rw [← h1]
    exact Finset.sum_congr rfl fun _ _ => by ring
  field_simp at h2
  exact h2.symm

end QOU.SchurWeyl.JimboGL
