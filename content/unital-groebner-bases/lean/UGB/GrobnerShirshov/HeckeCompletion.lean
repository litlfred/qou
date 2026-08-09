import UGB.GrobnerShirshov.HeckeGS

/-!
# The Bokut–Shiao completion, and the fact that the counterexample *is* the missing rule

`HeckeGS.lean` §4e refutes `hecke_is_gs_basis`: at `n = 4` the overlap of the
Yang–Baxter rule for `(σ₂, σ₃)` with the far-commutation rule for `(σ₃, σ₁)`,
over the ambient word `σ₃σ₂σ₃σ₁`, has S-polynomial

  `σ₂σ₃σ₂σ₁ − σ₃σ₂σ₁σ₃`

and both words are irreducible for `heckeRewritingSystem`. That module also says
what is missing — Bokut & Shiao complete the presentation with the family

  `σᵢ σᵢ₋₁ ⋯ σⱼ σᵢ → σᵢ₋₁ σᵢ σᵢ₋₁ ⋯ σⱼ`   (`j ≤ i − 1`)

This file makes that family a definition and checks the claim that connects the
two: **the refuting S-polynomial is, up to sign, exactly the missing rule at
`(i, j) = (3, 1)`.** `bsWord₁ 3 1 = σ₃σ₂σ₁σ₃` and `bsWord₂ 2 3 1 = σ₂σ₃σ₂σ₁` are
precisely `NotAGSBasis.w₂` and `NotAGSBasis.w₁`. So for the completed system the
S-polynomial is no longer a normal form (`spoly_not_isNormalForm_completed`), and
the specific obstruction §4e exhibits is gone.

## The family carries no `q`

Unlike the quadratic relation, the Bokut–Shiao words need no deformation: the
identity is a *braid-group* identity, provable from the braid and
far-commutation relations alone, with the quadratic relation never used. Two
lines, in the algebra:

  `σᵢ σᵢ₋₁ ⋯ σⱼ σᵢ = σᵢ σᵢ₋₁ σᵢ σᵢ₋₂ ⋯ σⱼ`   (σᵢ commutes past σᵢ₋₂ … σⱼ)
  `                = σᵢ₋₁ σᵢ σᵢ₋₁ σᵢ₋₂ ⋯ σⱼ`   (braid)

so the rule is the same two-term shape as `yangBaxterRelation`, which it
subsumes at `j = i − 1`.

## Indices

`bokutShiaoRelation` takes `i'`, `i`, `j` with `i'` standing for `i − 1`,
related by the side condition `i'.val + 1 = i.val` carried on the enumeration
rather than by `Fin` arithmetic. That keeps every word here free of subtraction
and every membership proof in the same `flatMap`/`filterMap` shape the existing
system uses.

## What is **not** established here

The completed system is defined and the §4e obstruction is checked to be
resolved by it. Neither of the two harder statements is proved:

* **DONE (§4h).** The general leading monomial
  `bokutShiaoRelation_lm : lm (bokutShiaoRelation i' i j) = bsWord₁ i j`, via
  `descWord_cons : descWord i j = ⟨i⟩ :: descWord i' j`. As predicted, no length
  computation was needed: the cons lemma gives both words a visible common tail
  (`σᵢ :: (w ++ [σᵢ])` against `σᵢ₋₁ :: σᵢ :: w`, same `w`), so the lengths agree
  by `simp` and the comparison is one `List.Lex.rel` on the first letter.
  `descWord_cons` reduces to a statement about `List.finRange n` being
  `Pairwise (· < ·)`: once the head is `i` every later index exceeds it and both
  filters annihilate the tail, and before the head is reached the two predicates
  agree because `a < i = i' + 1` forces `a ≤ i'`.
* * that the completed system **is** a Gröbner–Shirshov basis. That is the whole
  of Bokut & Shiao's theorem, and it needs the overlap analysis re-run against
  the completed rule set — a strictly larger set of compositions, since the new
  family overlaps itself. Resolving the one overlap that refutes the
  uncompleted system is necessary, not sufficient.

Bean qou-auq3.
-/

namespace UGB.GrobnerShirshov.Hecke

/-! ## §4f  The completion family -/

/-- The descending word `σᵢ σᵢ₋₁ ⋯ σⱼ`, built by filtering `List.finRange n`
so that no index arithmetic is needed. Empty when `i < j`. -/
def descWord {n : ℕ} (i j : Fin n) : Monomial (HeckeGen n) :=
  ((List.finRange n).filter
      (fun k => decide (j.val ≤ k.val ∧ k.val ≤ i.val))).reverse.map
    (fun k => (⟨k⟩ : HeckeGen n))

/-- `σᵢ σᵢ₋₁ ⋯ σⱼ σᵢ` — the left-hand side of the Bokut–Shiao rule, and (for
`j < i`) its leading monomial. -/
def bsWord₁ {n : ℕ} (i j : Fin n) : Monomial (HeckeGen n) :=
  descWord i j ++ [⟨i⟩]

/-- `σᵢ₋₁ σᵢ σᵢ₋₁ ⋯ σⱼ` — the right-hand side. `i'` stands for `i − 1`. -/
def bsWord₂ {n : ℕ} (i' i j : Fin n) : Monomial (HeckeGen n) :=
  ⟨i'⟩ :: ⟨i⟩ :: descWord i' j

/-- **The Bokut–Shiao rule** `σᵢσᵢ₋₁⋯σⱼσᵢ − σᵢ₋₁σᵢσᵢ₋₁⋯σⱼ`, with `i'` standing
for `i − 1`. Undeformed: see the module docstring. -/
noncomputable def bokutShiaoRelation {n : ℕ} (i' i j : Fin n) :
    ReductionRule (HeckeGen n) ℝ where
  relation := AlgElement.ofTerms [
    (bsWord₁ i j, 1),
    (bsWord₂ i' i j, -1)
  ]
  nonzero := AlgElement.ofTerms_support_nonempty (by simp)

/-- The Hecke rewriting system **completed** with the Bokut–Shiao family.
Every rule of `heckeRewritingSystem` is kept, so every membership and
leading-monomial fact proved there still applies verbatim; the new block adds
`bokutShiaoRelation i' i j` for each `i' + 1 = i` and `j ≤ i'`. -/
noncomputable def heckeCompletedRewritingSystem
    (n : ℕ) (hn : 0 < n) (hp : HeckeParams) : RewritingSystem (HeckeGen n) ℝ where
  rules :=
    (heckeRewritingSystem n hn hp).rules ++
    ((List.finRange n).flatMap (fun i =>
      (List.finRange n).flatMap (fun i' =>
        (List.finRange n).filterMap (fun j =>
          if i'.val + 1 = i.val ∧ j.val ≤ i'.val then
            some (bokutShiaoRelation i' i j) else none))))
  nonempty := by
    intro h
    exact (heckeRewritingSystem n hn hp).nonempty (List.append_eq_nil_iff.mp h).1

/-! ## §4g  The refuting overlap, against the completed system

Everything below is about the very composition `NotAGSBasis.oc` that refutes the
uncompleted system, so the two sections are directly comparable. -/

namespace Completion

open NotAGSBasis

/-- The Bokut–Shiao rule at `(i, j) = (3, 1)`: `σ₃σ₂σ₁σ₃ → σ₂σ₃σ₂σ₁`. -/
noncomputable def bs31 : ReductionRule (HeckeGen 4) ℝ :=
  bokutShiaoRelation 2 3 1

/-- Its left-hand word is `w₂`, one of the two words §4e shows irreducible. -/
theorem bsWord₁_31 : bsWord₁ (3 : Fin 4) (1 : Fin 4) = w₂ := by decide

/-- Its right-hand word is `w₁`, the other one. -/
theorem bsWord₂_231 : bsWord₂ (2 : Fin 4) (3 : Fin 4) (1 : Fin 4) = w₁ := by decide

theorem bs31_relation :
    bs31.relation = AlgElement.ofTerms [(w₂, (1 : ℝ)), (w₁, -1)] := by
  show AlgElement.ofTerms
      [(bsWord₁ (3 : Fin 4) (1 : Fin 4), (1 : ℝ)),
       (bsWord₂ (2 : Fin 4) (3 : Fin 4) (1 : Fin 4), -1)] = _
  rw [bsWord₁_31, bsWord₂_231]

/-- `lm(bs31) = σ₃σ₂σ₁σ₃`. Both words have length 4, and deg-lex ranks `σ₃`
above `σ₂`, so the word starting with `σ₃` is the larger. -/
theorem bs31_lm : bs31.lm (heckeOrder 4) = w₂ := by
  apply leadingMonomial_eq_of_max
  · simp [bs31, bokutShiaoRelation, bsWord₁_31, bsWord₂_231, w₁, w₂,
      AlgElement.ofTerms]
  · intro m hm hne
    simp [bs31, bokutShiaoRelation, bsWord₁_31, bsWord₂_231, AlgElement.ofTerms] at hm
    rcases hm with rfl | rfl
    · exact absurd rfl hne
    · exact heckeOrder_lt_of_lex (by simp [w₁, w₂])
        (List.Lex.rel (by simp [HeckeGen.rank]))

theorem bs31_mem (hp : HeckeParams) :
    bs31 ∈ (heckeCompletedRewritingSystem 4 hn4 hp).rules := by
  refine List.mem_append_right _ ?_
  refine List.mem_flatMap.mpr ⟨3, List.mem_finRange 3, ?_⟩
  refine List.mem_flatMap.mpr ⟨2, List.mem_finRange 2, ?_⟩
  exact List.mem_filterMap.mpr ⟨1, List.mem_finRange 1, rfl⟩

/-! ### The S-polynomial's coefficient at `w₂`

§4e proves `spoly.coeff w₁ = 1`. The other word carries `−1`, by the mirror
argument: the Yang–Baxter half of the S-polynomial has shape `_ ++ [σ₁]` and
`w₂` ends in `σ₃`, so that half contributes nothing; the far-commutation half
has shape `[σ₃, σ₂] ++ _` and contributes `σ₁σ₃`'s coefficient, which is `−1`. -/

theorem spoly_coeff_w₂ : oc.spoly.coeff w₂ = -1 := by
  have h1 : w₂ = [⟨3⟩, ⟨2⟩] ++ [⟨1⟩, ⟨3⟩] ++ ([] : Monomial (HeckeGen 4)) := by
    simp [w₂]
  have h2 : (AlgElement.contextMul [] yb.relation [⟨1⟩]).coeff w₂ = 0 := by
    refine AlgElement.contextMul_coeff_of_not_shape _ (fun w => fun hc => ?_)
    -- `w₂` ends in `σ₃`, every word of this shape ends in `σ₁`.
    have hrev := congrArg List.reverse hc
    simp [w₂] at hrev
  simp only [OverlapComposition.spoly, AlgElement.sub_coeff, AlgElement.smul_coeff]
  show fc.lc (heckeOrder 4) * (AlgElement.contextMul [] yb.relation [⟨1⟩]).coeff w₂
      - yb.lc (heckeOrder 4)
        * (AlgElement.contextMul [⟨3⟩, ⟨2⟩] fc.relation []).coeff w₂ = -1
  rw [h2, fc_lc, yb_lc, h1, AlgElement.contextMul_coeff_middle]
  simp [fc, farCommRelation, AlgElement.ofTerms_coeff]

/-- **The completed system reduces the S-polynomial that refutes the
uncompleted one.** `w₂` carries a non-zero coefficient and is the leading
monomial of `bs31`, hence an infix of itself — so the S-polynomial is not a
normal form, and the obstruction of §4e is gone.

Contrast `NotAGSBasis.spoly_isNormalForm`, which is the same S-polynomial
against `heckeRewritingSystem`. -/
theorem spoly_not_isNormalForm_completed (hp : HeckeParams) :
    ¬ isNormalForm (heckeOrder 4) (heckeCompletedRewritingSystem 4 hn4 hp)
        oc.spoly := by
  intro hnf
  refine hnf bs31 (bs31_mem hp) w₂ (by rw [spoly_coeff_w₂]; norm_num) ?_
  rw [bs31_lm]

/-! ### The refuting overlap **resolves** in the completed system

`spoly_not_isNormalForm_completed` says only that the S-polynomial is no longer
irreducible. The Gröbner–Shirshov condition asks for more — that it *reduces to
zero* — and here it does, in a single step, for a reason worth seeing:

    oc.spoly       =  w₁ − w₂        (§4e: coeff w₁ = 1, coeff w₂ = −1)
    bs31.relation  =  w₂ − w₁        (bsWord₁ 3 1 = w₂, bsWord₂ 2 3 1 = w₁)

They are negatives of each other. So one application of `bs31` in empty context
with coefficient `−1` annihilates it exactly. The obstruction and its repair are
the same two words with opposite signs. -/

theorem bs31_lc : bs31.lc (heckeOrder 4) = 1 := by
  show bs31.relation.coeff (bs31.lm (heckeOrder 4)) = 1
  rw [bs31_lm, bs31_relation]
  simp [AlgElement.ofTerms_coeff, w₁, w₂]

/-- `w₁`, `w₂` and the ambient word `σ₃σ₂σ₃σ₁` are three distinct words. -/
theorem three_words_distinct :
    w₁ ≠ w₂ ∧ oc.word ≠ w₁ ∧ oc.word ≠ w₂ := by
  refine ⟨by decide, ?_, ?_⟩
  · show ([⟨3⟩, ⟨2⟩, ⟨3⟩, ⟨1⟩] : Monomial (HeckeGen 4)) ≠ w₁
    decide
  · show ([⟨3⟩, ⟨2⟩, ⟨3⟩, ⟨1⟩] : Monomial (HeckeGen 4)) ≠ w₂
    decide

/-- The S-polynomial and the Bokut–Shiao relation cancel coefficient by
coefficient. -/
theorem spoly_add_relation_eq_zero (m : Monomial (HeckeGen 4)) :
    oc.spoly.coeff m + bs31.relation.coeff m = 0 := by
  obtain ⟨h12, hw1, hw2⟩ := three_words_distinct
  by_cases h : oc.spoly.coeff m = 0
  · rw [h, zero_add, bs31_relation]
    have hm1 : m ≠ w₁ := by rintro rfl; rw [spoly_coeff_w₁] at h; exact one_ne_zero h
    have hm2 : m ≠ w₂ := by
      rintro rfl; rw [spoly_coeff_w₂] at h; exact absurd h (by norm_num)
    simp [AlgElement.ofTerms_coeff, Ne.symm hm1, Ne.symm hm2]
  · rcases spoly_support m (by exact h) with rfl | rfl | rfl
    · rw [spoly_coeff_w₁, bs31_relation]
      simp [AlgElement.ofTerms_coeff, Ne.symm h12]
    · rw [spoly_coeff_w₂, bs31_relation]
      simp [AlgElement.ofTerms_coeff, h12]
    · exact absurd (OverlapComposition.spoly_coeff_word_eq_zero oc) h

/-- **The overlap that refutes the uncompleted system resolves in the completed
one** — one step, to zero.

This is the Gröbner–Shirshov condition for this composition, and it is strictly
stronger than `spoly_not_isNormalForm_completed`: not merely "reducible" but
"reduces to zero". Contrast `NotAGSBasis.spoly_isNormalForm`, which is the same
S-polynomial against `heckeRewritingSystem` and cannot be reduced at all. -/
theorem refuting_overlap_resolves (hp : HeckeParams) :
    SingleStepReduction (heckeOrder 4) (heckeCompletedRewritingSystem 4 hn4 hp)
      oc.spoly AlgElement.zero := by
  refine ⟨bs31, bs31_mem hp, [], [], -1, ?_, ?_, ?_⟩
  · rw [bs31_lm]
    show oc.spoly.coeff w₂ ≠ 0
    rw [spoly_coeff_w₂]; norm_num
  · rw [bs31_lm, bs31_lc]
    show (-1 : ℝ) * 1 = oc.spoly.coeff w₂
    rw [spoly_coeff_w₂]; norm_num
  · intro m
    show (0 : ℝ) = oc.spoly.coeff m - (-1) * (AlgElement.contextMul [] bs31.relation []).coeff m
    have hctx : (AlgElement.contextMul [] bs31.relation []).coeff m
        = bs31.relation.coeff m := by
      have : m = [] ++ m ++ ([] : Monomial (HeckeGen 4)) := by simp
      rw [this, AlgElement.contextMul_coeff_middle]
      simp
    rw [hctx]
    have := spoly_add_relation_eq_zero m
    linarith

end Completion

/-! ## §4h  The general leading monomial

The cons lemma the module docstring names as the one thing missing. With it,
`bokutShiaoRelation_lm` needs no length computation: both words acquire a visible
common tail and the deg-lex comparison is one `List.Lex.rel` on the first letter. -/

/-- `List.finRange n` is `Pairwise (· < ·)`, so once the head is `i` every later
index exceeds it and both filters annihilate the tail; before the head is reached
the two predicates agree, because `a < i = i' + 1` forces `a ≤ i'`. -/
theorem filter_desc_cons {n : ℕ} {i' i j : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) :
    ∀ l : List (Fin n), l.Pairwise (fun a b => a.val < b.val) → i ∈ l →
      l.filter (fun k => decide (j.val ≤ k.val ∧ k.val ≤ i.val))
        = l.filter (fun k => decide (j.val ≤ k.val ∧ k.val ≤ i'.val)) ++ [i] := by
  intro l
  induction l with
  | nil => intro _ hm; simp at hm
  | cons a t ih =>
    intro hp hm
    rw [List.pairwise_cons] at hp
    obtain ⟨halt, hpt⟩ := hp
    rcases List.mem_cons.mp hm with hai | hmt
    · -- the head is `i`; every later index is strictly larger, so both tails die
      subst hai
      have h1 : t.filter (fun k => decide (j.val ≤ k.val ∧ k.val ≤ i.val)) = [] := by
        refine List.filter_eq_nil_iff.mpr (fun b hb hd => ?_)
        have := halt b hb
        have hd' := of_decide_eq_true hd
        omega
      have h2 : t.filter (fun k => decide (j.val ≤ k.val ∧ k.val ≤ i'.val)) = [] := by
        refine List.filter_eq_nil_iff.mpr (fun b hb hd => ?_)
        have := halt b hb
        have hd' := of_decide_eq_true hd
        omega
      simp only [List.filter_cons, h1, h2, decide_eq_true_eq]
      rw [if_pos (by omega : j.val ≤ i.val ∧ i.val ≤ i.val),
        if_neg (by omega : ¬ (j.val ≤ i.val ∧ i.val ≤ i'.val))]
      rfl
    · -- the head is below `i`, so the two predicates agree on it
      have hlt : a.val < i.val := halt i hmt
      simp only [List.filter_cons, decide_eq_true_eq]
      by_cases hpos : j.val ≤ a.val ∧ a.val ≤ i.val
      · rw [if_pos hpos, if_pos (by omega : j.val ≤ a.val ∧ a.val ≤ i'.val)]
        simp only [List.cons_append]
        exact congrArg (a :: ·) (ih hpt hmt)
      · rw [if_neg hpos, if_neg (by omega : ¬ (j.val ≤ a.val ∧ a.val ≤ i'.val))]
        exact ih hpt hmt

/-- **The cons lemma**: dropping the top index drops the first letter. -/
theorem descWord_cons {n : ℕ} {i' i j : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) :
    descWord i j = (⟨i⟩ : HeckeGen n) :: descWord i' j := by
  simp only [descWord, filter_desc_cons hi hj (List.finRange n)
    (List.pairwise_lt_finRange n) (List.mem_finRange i),
    List.reverse_append, List.reverse_cons, List.reverse_nil, List.nil_append,
    List.singleton_append, List.map_cons]

/-- Both Bokut–Shiao words in cons form, sharing a visible tail. This is what
makes the leading-monomial comparison a one-letter lex step with no length
arithmetic: `σᵢ :: (w ++ [σᵢ])` against `σᵢ₋₁ :: σᵢ :: w`, same `w`. -/
theorem bsWord₁_cons {n : ℕ} {i' i j : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) :
    bsWord₁ i j = (⟨i⟩ : HeckeGen n) :: (descWord i' j ++ [⟨i⟩]) := by
  simp [bsWord₁, descWord_cons hi hj]

/-- **The general leading monomial** `lm(bokutShiaoRelation i' i j) = bsWord₁ i j`.

Both words have length `|descWord i' j| + 2` — visible from `bsWord₁_cons`, with
no length computation — and deg-lex ranks `σᵢ` above `σᵢ₋₁`, so the word starting
with `σᵢ` is the larger. Compare `Completion.bs31_lm`, which is this at
`(i', i, j) = (2, 3, 1)` and was proved by `fin_cases` before this existed. -/
theorem bokutShiaoRelation_lm {n : ℕ} {i' i j : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) :
    (bokutShiaoRelation i' i j).lm (heckeOrder n) = bsWord₁ i j := by
  apply leadingMonomial_eq_of_max
  · simp [bokutShiaoRelation, AlgElement.ofTerms]
  · intro m hm hne
    simp [bokutShiaoRelation, AlgElement.ofTerms] at hm
    rcases hm with rfl | rfl
    · exact absurd rfl hne
    · refine heckeOrder_lt_of_lex ?_ ?_
      · simp [bsWord₁_cons hi hj, bsWord₂]
      · rw [bsWord₁_cons hi hj]
        exact List.Lex.rel (by simp only [HeckeGen.rank]; omega)

/-! ## §4i  Every rule of the completed system, classified

The analogue of `heckeRewritingSystem_lm_cases` for the completed system. That
classification is what §4e's irreducibility machinery runs on — `no_rule_infix_w₁`
and friends dispatch on it — so the completed system needs its own before any of
that can be redone against it. -/

/-- **Every rule of `heckeCompletedRewritingSystem` is one of four families**, and
its leading monomial is the explicit word listed here. The first three cases are
`heckeRewritingSystem_lm_cases` verbatim, since the completed system keeps every
original rule; the fourth is the Bokut–Shiao family, via the general
`bokutShiaoRelation_lm`. -/
theorem heckeCompletedRewritingSystem_lm_cases {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    (r : ReductionRule (HeckeGen n) ℝ)
    (hr : r ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    (∃ i : Fin n, r.lm (heckeOrder n) = [⟨i⟩, ⟨i⟩]) ∨
    (∃ i j : Fin n, j.val = i.val + 1 ∧ r.lm (heckeOrder n) = [⟨j⟩, ⟨i⟩, ⟨j⟩]) ∨
    (∃ i j : Fin n, j.val + 1 < i.val ∧ r.lm (heckeOrder n) = [⟨i⟩, ⟨j⟩]) ∨
    (∃ i' i j : Fin n, i'.val + 1 = i.val ∧ j.val ≤ i'.val ∧
        r.lm (heckeOrder n) = bsWord₁ i j) := by
  rcases List.mem_append.mp hr with hr' | hr'
  · rcases heckeRewritingSystem_lm_cases hn hp r hr' with h | h | h
    · exact Or.inl h
    · exact Or.inr (Or.inl h)
    · exact Or.inr (Or.inr (Or.inl h))
  · -- the Bokut–Shiao block: three nested enumerations, then the side condition
    obtain ⟨i, -, hi⟩ := List.mem_flatMap.mp hr'
    obtain ⟨i', -, hi'⟩ := List.mem_flatMap.mp hi
    obtain ⟨j, -, hj⟩ := List.mem_filterMap.mp hi'
    by_cases hc : i'.val + 1 = i.val ∧ j.val ≤ i'.val
    · rw [if_pos hc] at hj
      cases hj
      exact Or.inr (Or.inr (Or.inr
        ⟨i', i, j, hc.1, hc.2, bokutShiaoRelation_lm hc.1 hc.2⟩))
    · rw [if_neg hc] at hj; exact absurd hj (by simp)

/-- No rule of the completed system has an empty leading monomial — the
non-degeneracy `gs_basis_of_empty_lm` shows is essential, re-established for the
larger rule set. The Bokut–Shiao words are never empty: `bsWord₁ i j` ends in
`σᵢ`. -/
theorem heckeCompletedRewritingSystem_lm_ne_nil {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    (r : ReductionRule (HeckeGen n) ℝ)
    (hr : r ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    r.lm (heckeOrder n) ≠ [] := by
  rcases heckeCompletedRewritingSystem_lm_cases hn hp r hr with
    ⟨i, h⟩ | ⟨i, j, -, h⟩ | ⟨i, j, -, h⟩ | ⟨i', i, j, -, -, h⟩ <;> rw [h] <;>
    simp [bsWord₁]

end UGB.GrobnerShirshov.Hecke
