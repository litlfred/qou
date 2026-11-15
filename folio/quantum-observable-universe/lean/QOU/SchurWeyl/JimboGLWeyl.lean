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

end QOU.SchurWeyl.JimboGL
