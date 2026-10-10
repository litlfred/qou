import QOU.Hecke.TwTrace

/-!
# QOU.Hecke.TwGramRankOne — the `T_w` Gram determinant at rank one

Fifth brick of bean `qou-0y6h`.  `TwGram` reduced semisimplicity of
`H_n(q)` to `det (twGram) ≠ 0` at every rank; `TwTrace` made the trace of a
generator explicit.  This file closes the first rank end to end:

  `det (twGram K q 1) = (1 + q)² = [2]_q²`,

hence `H_1(q)` — the honest `IwahoriHecke K q 1`, a `RingQuot` of a free
algebra, not a presentation chosen for convenience — is semisimple whenever
`1 + q ≠ 0`, with **no cited class and no `sorry`**.

## Why this is not a duplicate of `H2TraceForm`

`QOU.Hecke.H2TraceForm.h2_regTraceGram_det` proves the same determinant
`[2]_q²` for `AdjoinRoot (X² - (q-1)X - q)`, which is a *model* of the rank-one
Hecke algebra reached through a power basis.  The `T_w` route reaches
`IwahoriHecke K q 1` itself, and reaches it by machinery that is stated at
every rank — nothing here is special to `n = 1` except the enumeration of
`S₂`.  The two determinants agreeing is therefore a genuine cross-check of the
whole `TwRep → TwIndependent → TwBasisField → TwGram → TwTrace` stack against
an independently derived value, not a restatement of it.

## What is proved

* `Tw_swap` — `T_{s_i} = σ_i`, at every rank.
* `trace_lmul_one` — `tr(L_1) = (n+1)!`, at every rank.
* `trace_lmul_σ_sq` — `tr(L_{σ_i²})` from the quadratic relation, at every rank.
* `perm_two_cases` — `S₂ = {1, s}`.
* `twGram_det_rank_one` — `det (twGram K q 1) = (1 + q)²`.
* `isSemisimpleRing_rank_one` — the discharge.

## What is NOT here

The determinant at rank ≥ 2.  That needs `tr(L_{T_u})` for a general `u`,
which is not a corollary of the generator case: the diagonal coefficient
`[T_u T_w : T_w]` has no closed form in the corpus yet.
-/

namespace QOU.Hecke.TwBasis

open QOU.Hecke.IwahoriHecke (σ σ_quadratic)

variable (K : Type*) [Field K] (q : K) (n : ℕ)

/-- **`T_{s_i} = σ_i` (sorry-free).**  The chosen reduced word for a simple
    transposition is a single letter, whatever choice `reducedWord` made:
    left multiplication of `T_1 = 1` by `σ_i` lands on `T_{s_i}` because the
    identity ascends at every `i`. -/
theorem Tw_swap (i : Fin n) :
    Tw K q n (Equiv.swap i.castSucc i.succ) = σ K q n i := by
  have h := σ_mul_Tw_of_lt K q n i 1 (by simp)
  simpa using h.symm

/-- **`tr(L_1) = (n+1)!` (sorry-free).**  Left multiplication by `1` is the
    identity endomorphism, whose trace is the dimension. -/
theorem trace_lmul_one :
    LinearMap.trace K _ (Algebra.lmul K (QOU.Hecke.IwahoriHecke K q n) 1)
      = (Nat.factorial (n + 1) : K) := by
  rw [map_one, Module.End.one_eq_id, LinearMap.trace_id, finrank_eq_factorial]

/-- **`tr(L_{σ_i²})` from the quadratic relation (sorry-free).** -/
theorem trace_lmul_σ_sq (i : Fin n) :
    LinearMap.trace K _
        (Algebra.lmul K (QOU.Hecke.IwahoriHecke K q n) (σ K q n i * σ K q n i))
      = (q - 1) * LinearMap.trace K _
          (Algebra.lmul K (QOU.Hecke.IwahoriHecke K q n) (σ K q n i))
        + q * (Nat.factorial (n + 1) : K) := by
  rw [σ_quadratic, map_add, map_smul, map_smul, map_one, map_add, map_smul,
    map_smul, Module.End.one_eq_id, LinearMap.trace_id, finrank_eq_factorial,
    smul_eq_mul, smul_eq_mul]

section RankOne

variable {K : Type*} [Field K] (q : K)

/-- **`S₂ = {1, s}` (sorry-free).** -/
theorem perm_two_cases (w : Equiv.Perm (Fin 2)) : w = 1 ∨ w = Equiv.swap 0 1 := by
  have hval : ∀ x : Fin 2, x = 0 ∨ x = 1 := by decide
  rcases hval (w 0) with h0 | h0
  · left
    refine Equiv.ext fun x => ?_
    rcases hval x with hx | hx <;> subst hx
    · simpa using h0
    · rcases hval (w 1) with h1 | h1
      · exact absurd (h0.trans h1.symm) (w.injective.ne (by decide))
      · simpa using h1
  · right
    refine Equiv.ext fun x => ?_
    rcases hval x with hx | hx <;> subst hx
    · simpa using h0
    · rcases hval (w 1) with h1 | h1
      · simpa using h1
      · exact absurd (h0.trans h1.symm) (w.injective.ne (by decide))

/-- The rank-one simple transposition, in the `Fin 1`-indexed spelling the
    generator uses. -/
theorem swap_zero_one_eq :
    (Equiv.swap (0 : Fin 2) 1)
      = Equiv.swap (Fin.castSucc (0 : Fin 1)) (Fin.succ (0 : Fin 1)) := rfl

/-- **Exactly one permutation of `Fin 2` descends at the single position.** -/
theorem card_descent_rank_one :
    (Finset.univ.filter (fun w : Equiv.Perm (Fin (1 + 1)) =>
        ¬ w (0 : Fin 1).castSucc < w (0 : Fin 1).succ)).card = 1 := by
  have h := two_mul_card_descent 1 0
  have h2 : Nat.factorial (1 + 1) = 2 := rfl
  omega

/-- The four Gram entries at rank one. -/
theorem twGram_rank_one_one_one : twGram K q 1 1 1 = (2 : K) := by
  rw [twGram_apply, MathlibExt.regTraceForm, Tw_one, one_mul, trace_lmul_one,
    show Nat.factorial (1 + 1) = 2 from rfl]
  norm_num

theorem twGram_rank_one_one_swap :
    twGram K q 1 1 (Equiv.swap 0 1) = q - 1 := by
  rw [twGram_apply, MathlibExt.regTraceForm, Tw_one, one_mul, swap_zero_one_eq, Tw_swap,
    trace_lmul_σ, card_descent_rank_one]
  norm_num

theorem twGram_rank_one_swap_one :
    twGram K q 1 (Equiv.swap 0 1) 1 = q - 1 := by
  rw [twGram_apply, MathlibExt.regTraceForm, Tw_one, mul_one, swap_zero_one_eq, Tw_swap,
    trace_lmul_σ, card_descent_rank_one]
  norm_num

theorem twGram_rank_one_swap_swap :
    twGram K q 1 (Equiv.swap 0 1) (Equiv.swap 0 1) = q ^ 2 + 1 := by
  rw [twGram_apply, MathlibExt.regTraceForm, swap_zero_one_eq, Tw_swap, trace_lmul_σ_sq,
    trace_lmul_σ, card_descent_rank_one, show Nat.factorial (1 + 1) = 2 from rfl]
  push_cast
  ring

/-- **`det (twGram K q 1) = (1 + q)² = [2]_q²` (sorry-free).** -/
theorem twGram_det_rank_one : (twGram K q 1).det = (1 + q) ^ 2 := by
  classical
  have hcard : Fintype.card (Equiv.Perm (Fin 2)) = 2 := by
    rw [Fintype.card_perm, Fintype.card_fin]; rfl
  set e : Fin 2 ≃ Equiv.Perm (Fin 2) := (Fintype.equivFinOfCardEq hcard).symm with he
  have hne : e 0 ≠ e 1 := fun h => by simpa using e.injective h
  rw [← Matrix.det_submatrix_equiv_self e (twGram K q 1), Matrix.det_fin_two]
  simp only [Matrix.submatrix_apply]
  rcases perm_two_cases (e 0) with h0 | h0 <;> rcases perm_two_cases (e 1) with h1 | h1
  · exact absurd (h0.trans h1.symm) hne
  · rw [h0, h1, twGram_rank_one_one_one, twGram_rank_one_swap_swap,
      twGram_rank_one_one_swap, twGram_rank_one_swap_one]; ring
  · rw [h0, h1, twGram_rank_one_one_one, twGram_rank_one_swap_swap,
      twGram_rank_one_one_swap, twGram_rank_one_swap_one]; ring
  · exact absurd (h0.trans h1.symm) hne

/-- **`H_1(q)` is semisimple whenever `1 + q ≠ 0` (sorry-free, no cited
    class).**  The first rank at which the `T_w` basis discharges
    `WenzlCriterion` on `IwahoriHecke` itself. -/
theorem isSemisimpleRing_rank_one (hq : (1 : K) + q ≠ 0) :
    IsSemisimpleRing (QOU.Hecke.IwahoriHecke K q 1) :=
  isSemisimpleRing_of_twGram_det_ne_zero K q 1
    (by rw [twGram_det_rank_one]; exact pow_ne_zero 2 hq)

/-- **The substrate discharges rank-one semisimplicity (sorry-free).**  For
    any real `q > 0` — in particular the substrate `q₀ ≈ 1.10998`. -/
theorem isSemisimpleRing_rank_one_of_pos {q : ℝ} (hq : 0 < q) :
    IsSemisimpleRing (QOU.Hecke.IwahoriHecke ℝ q 1) :=
  isSemisimpleRing_rank_one q (by positivity)

end RankOne

end QOU.Hecke.TwBasis
