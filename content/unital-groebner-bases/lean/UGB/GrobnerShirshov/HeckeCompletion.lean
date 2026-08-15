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

/-! ## §4j  The family subsumes Yang–Baxter

At `j = i − 1` the Bokut–Shiao words are the braid words. So the completed
system's Yang–Baxter rules are not new information relative to the family — which
matters for the overlap analysis ahead, since it means YB × BS overlaps are a
special case of BS × BS rather than a separate family to enumerate. -/

/-- The filter that defines `descWord i i` keeps exactly the one index `i`:
everything after `i` in a `Pairwise (· < ·)` list exceeds it, and everything
before it is below. Same shape as `filter_desc_cons`. -/
theorem filter_desc_self {n : ℕ} (i : Fin n) :
    ∀ l : List (Fin n), l.Pairwise (fun a b => a.val < b.val) → i ∈ l →
      l.filter (fun k => decide (i.val ≤ k.val ∧ k.val ≤ i.val)) = [i] := by
  intro l
  induction l with
  | nil => intro _ hm; simp at hm
  | cons a t ih =>
    intro hp hm
    rw [List.pairwise_cons] at hp
    obtain ⟨halt, hpt⟩ := hp
    rcases List.mem_cons.mp hm with hai | hmt
    · subst hai
      have h1 : t.filter (fun k => decide (i.val ≤ k.val ∧ k.val ≤ i.val)) = [] := by
        refine List.filter_eq_nil_iff.mpr (fun b hb hd => ?_)
        have := halt b hb
        have hd' := of_decide_eq_true hd
        omega
      simp only [List.filter_cons, h1, decide_eq_true_eq]
      rw [if_pos (by omega : i.val ≤ i.val ∧ i.val ≤ i.val)]
    · have hlt : a.val < i.val := halt i hmt
      simp only [List.filter_cons, decide_eq_true_eq]
      rw [if_neg (by omega : ¬ (i.val ≤ a.val ∧ a.val ≤ i.val))]
      exact ih hpt hmt

/-- The descending word from `i` down to `i` is the single letter `σᵢ`. -/
theorem descWord_self {n : ℕ} (i : Fin n) : descWord i i = [(⟨i⟩ : HeckeGen n)] := by
  simp only [descWord, filter_desc_self i (List.finRange n)
    (List.pairwise_lt_finRange n) (List.mem_finRange i),
    List.reverse_cons, List.reverse_nil, List.nil_append, List.map_cons, List.map_nil]

/-- At `j = i − 1` the left Bokut–Shiao word is the braid word `σᵢσᵢ₋₁σᵢ`. -/
theorem bsWord₁_at_pred {n : ℕ} {i' i : Fin n} (hi : i'.val + 1 = i.val) :
    bsWord₁ i i' = [(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩] := by
  rw [bsWord₁, descWord_cons hi (le_refl _), descWord_self]
  rfl

/-- …and the right one is `σᵢ₋₁σᵢσᵢ₋₁`.

Note this needs **no** relation between `i'` and `i`: `bsWord₂ i' i j` is
`σᵢ₋₁ σᵢ` followed by `descWord i' j`, so at `j = i'` the tail collapses by
`descWord_self` whatever `i` is. It is the *left* word that needs `i' + 1 = i`,
because that is where `descWord_cons` is used. -/
theorem bsWord₂_at_pred {n : ℕ} (i' i : Fin n) :
    bsWord₂ i' i i' = [(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩] := by
  rw [bsWord₂, descWord_self]

/-- **The Bokut–Shiao rule at `j = i − 1` is the Yang–Baxter rule**, up to the
sign convention: its relation is `σᵢσᵢ₋₁σᵢ − σᵢ₋₁σᵢσᵢ₋₁`, and
`yangBaxterRelation i' i` is the negative of that.

So the family really does extend the presentation rather than sit beside it, and
the two rules share a leading monomial (`bokutShiao_lm_eq_yangBaxter_lm`). -/
theorem bokutShiaoRelation_at_pred {n : ℕ} {i' i : Fin n} (hi : i'.val + 1 = i.val) :
    (bokutShiaoRelation i' i i').relation
      = AlgElement.ofTerms [([⟨i⟩, ⟨i'⟩, ⟨i⟩], (1 : ℝ)), ([⟨i'⟩, ⟨i⟩, ⟨i'⟩], -1)] := by
  show AlgElement.ofTerms [(bsWord₁ i i', (1 : ℝ)), (bsWord₂ i' i i', -1)] = _
  rw [bsWord₁_at_pred hi, bsWord₂_at_pred i' i]

/-- Both rules lead on `σᵢσᵢ₋₁σᵢ` — deg-lex ranks `σᵢ` above `σᵢ₋₁`, so the word
starting with the larger generator wins, exactly as in `yangBaxterRelation_lm`. -/
theorem bokutShiao_lm_eq_yangBaxter_lm {n : ℕ} {i' i : Fin n} (hi : i'.val + 1 = i.val) :
    (bokutShiaoRelation i' i i').lm (heckeOrder n)
      = (yangBaxterRelation i' i).lm (heckeOrder n) := by
  rw [bokutShiaoRelation_lm hi (le_refl _), bsWord₁_at_pred hi,
    yangBaxterRelation_lm i' i (by omega)]

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

/-! ## §4k  The overlap set of the completed system, enumerated

§4g resolves **one** overlap. Completeness needs every one of them, and until now
"how many are there" was prose: four families, and the new family overlaps
itself — a shape, not a number. This section produces the number.

An `OverlapComposition` is pinned by three words: `lm₁ = left ++ overlap`,
`lm₂ = overlap ++ right`, `overlap ≠ []`. The *rules* never enter, only their
leading monomials — so once those are a list, the overlap shapes are a
computation, and `mem_overlapTriples` is the bridge carrying any composition of
the completed system into that list.

Two rules with the same leading monomial give the same shape, and §4j says that
is not hypothetical: at `j = i − 1` the Bokut–Shiao and Yang–Baxter rules lead on
the same word. `completedLMSet` deduplicates, so `overlapTriples` counts
*shapes*; the rule-level multiplicity at those three words is a separate
question.

At `n = 4` the numbers are **16 rules, 13 distinct leading monomials, 58 overlap
shapes** — of which 13 are the degenerate `lm₁ = lm₂` self-pairings with both
contexts empty and 45 have both contexts non-empty. `NotAGSBasis.oc` is one of
the 45. -/

/-- Leading monomials of the quadratic family, `σᵢσᵢ`. -/
def quadLMs (n : ℕ) : List (Monomial (HeckeGen n)) :=
  (List.finRange n).map (fun i => [(⟨i⟩ : HeckeGen n), ⟨i⟩])

/-- Leading monomials of the Yang–Baxter family, `σⱼσᵢσⱼ` with `j = i + 1`
(`yangBaxterRelation_lm`: deg-lex puts the larger generator first). -/
def yangBaxterLMs (n : ℕ) : List (Monomial (HeckeGen n)) :=
  (List.finRange n).flatMap (fun i =>
    (List.finRange n).filterMap (fun j =>
      if j.val = i.val + 1 then some [(⟨j⟩ : HeckeGen n), ⟨i⟩, ⟨j⟩] else none))

/-- Leading monomials of the far-commutation family, `σᵢσⱼ` with `j + 1 < i`. -/
def farCommLMs (n : ℕ) : List (Monomial (HeckeGen n)) :=
  (List.finRange n).flatMap (fun i =>
    (List.finRange n).filterMap (fun j =>
      if j.val + 1 < i.val then some [(⟨i⟩ : HeckeGen n), ⟨j⟩] else none))

/-- Leading monomials of the Bokut–Shiao family, `bsWord₁ i j`.

The rule is indexed by `(i', i, j)` with `i' + 1 = i` and `j ≤ i'`, but its
leading monomial depends only on `(i, j)` and the two side conditions collapse to
`j < i` — so this list has exactly one entry per rule. -/
def bokutShiaoLMs (n : ℕ) : List (Monomial (HeckeGen n)) :=
  (List.finRange n).flatMap (fun i =>
    (List.finRange n).filterMap (fun j =>
      if j.val < i.val then some (bsWord₁ i j) else none))

/-- Every leading monomial of the completed system, as an explicit list, with the
duplicates the four families produce between them still present. -/
def completedLMWords (n : ℕ) : List (Monomial (HeckeGen n)) :=
  quadLMs n ++ yangBaxterLMs n ++ farCommLMs n ++ bokutShiaoLMs n

/-- The *distinct* leading monomials. §4j is why this is shorter than
`completedLMWords`. -/
def completedLMSet (n : ℕ) : List (Monomial (HeckeGen n)) :=
  (completedLMWords n).dedup

/-- **Soundness of the enumeration**: every rule of the completed system leads on
a word in the list. This is `heckeCompletedRewritingSystem_lm_cases` with the
existentials discharged into list membership, which is what makes the overlap
count downstream a statement about the actual rule set. -/
theorem heckeCompletedRewritingSystem_lm_mem {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    (r : ReductionRule (HeckeGen n) ℝ)
    (hr : r ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    r.lm (heckeOrder n) ∈ completedLMSet n := by
  refine List.mem_dedup.mpr ?_
  rcases heckeCompletedRewritingSystem_lm_cases hn hp r hr with
    ⟨i, h⟩ | ⟨i, j, hji, h⟩ | ⟨i, j, hji, h⟩ | ⟨i', i, j, hi, hj, h⟩
  · exact List.mem_append_left _ (List.mem_append_left _ (List.mem_append_left _
      (List.mem_map.mpr ⟨i, List.mem_finRange i, h.symm⟩)))
  · refine List.mem_append_left _ (List.mem_append_left _ (List.mem_append_right _
      (List.mem_flatMap.mpr ⟨i, List.mem_finRange i,
        List.mem_filterMap.mpr ⟨j, List.mem_finRange j, ?_⟩⟩)))
    rw [if_pos hji, h]
  · refine List.mem_append_left _ (List.mem_append_right _
      (List.mem_flatMap.mpr ⟨i, List.mem_finRange i,
        List.mem_filterMap.mpr ⟨j, List.mem_finRange j, ?_⟩⟩))
    rw [if_pos hji, h]
  · refine List.mem_append_right _
      (List.mem_flatMap.mpr ⟨i, List.mem_finRange i,
        List.mem_filterMap.mpr ⟨j, List.mem_finRange j, ?_⟩⟩)
    rw [if_pos (show j.val < i.val by omega), h]

/-- **The overlap shapes** of the completed system at rank `n`: every triple
`(left, overlap, right)` whose `left ++ overlap` and `overlap ++ right` are both
leading monomials and whose `overlap` is non-empty.

The degenerate shapes are deliberately kept. `OverlapComposition` places no
condition on `left` or `right`, so `left = right = []` (the two rules lead on the
*same* word) is a legal composition, and at the three words of §4j it is an
inhabited one. -/
def overlapTriples (n : ℕ) :
    List (Monomial (HeckeGen n) × Monomial (HeckeGen n) × Monomial (HeckeGen n)) :=
  (completedLMSet n).flatMap (fun a =>
    (completedLMSet n).flatMap (fun b =>
      (a.tails.filter (fun o => !o.isEmpty && o.isPrefixOf b)).map (fun o =>
        (a.take (a.length - o.length), o, b.drop o.length))))

/-- **The bridge.** Any splitting of two leading monomials that meets the
`OverlapComposition` conditions is in the enumerated list. Stated on words rather
than on compositions so that it applies to a composition of *any* two rules with
those leading monomials — including two distinct rules leading on the same
word. -/
theorem mem_overlapTriples {n : ℕ} {a b left o right : Monomial (HeckeGen n)}
    (ha : a ∈ completedLMSet n) (hb : b ∈ completedLMSet n)
    (hne : o ≠ []) (hA : a = left ++ o) (hB : b = o ++ right) :
    (left, o, right) ∈ overlapTriples n := by
  have hlen : a.length - o.length = left.length := by
    rw [hA, List.length_append]; omega
  refine List.mem_flatMap.mpr ⟨a, ha, List.mem_flatMap.mpr ⟨b, hb, ?_⟩⟩
  refine List.mem_map.mpr ⟨o, List.mem_filter.mpr ⟨(List.mem_tails o a).mpr ⟨left, hA.symm⟩, ?_⟩, ?_⟩
  · simp only [Bool.and_eq_true, Bool.not_eq_eq_eq_not, Bool.not_true,
      List.isEmpty_eq_false_iff, List.isPrefixOf_iff_prefix]
    exact ⟨hne, ⟨right, hB.symm⟩⟩
  · rw [hlen, hA, hB, List.take_left', List.drop_left'] <;> rfl

/-! ### The count at `n = 4`

Kernel-checked, no `native_decide`. -/

/-- Sixteen rules — 4 quadratic, 3 Yang–Baxter, 3 far-commutation, 6
Bokut–Shiao. -/
theorem completedLMWords_four_length : (completedLMWords 4).length = 16 := by decide

/-- …but only thirteen distinct leading monomials. The three lost are exactly the
Yang–Baxter words, which §4j identifies with the Bokut–Shiao rules at
`j = i − 1`. -/
theorem completedLMSet_four_length : (completedLMSet 4).length = 13 := by decide

/-- **Fifty-eight overlap shapes at `n = 4`.** The number the completeness proof
has to work through, in place of an estimate. -/
theorem overlapTriples_four_length : (overlapTriples 4).length = 58 := by decide

/-- Thirteen of the fifty-eight are the degenerate self-pairings, one per
leading monomial: `left = right = []`, `overlap = lm₁ = lm₂`. -/
theorem overlapTriples_four_degenerate_count :
    ((overlapTriples 4).filter (fun t => t.1.isEmpty && t.2.2.isEmpty)).length = 13 := by
  decide

/-- The other forty-five have both contexts non-empty. `NotAGSBasis.oc` — the
composition that refutes the uncompleted system — is one of them. -/
theorem overlapTriples_four_proper_count :
    ((overlapTriples 4).filter (fun t => !t.1.isEmpty && !t.2.2.isEmpty)).length = 45 := by
  decide

/-! ## §4l  The degenerate shapes resolve

Thirteen of the fifty-eight shapes are degenerate: both contexts empty, the two
rules leading on the same word. They are still proof obligations —
`OverlapComposition` admits them — and they split in two.

*When the two rules coincide* the S-polynomial is the difference of an element
with itself: `OverlapComposition.spoly_isZero_of_self`, proved in the framework
because nothing about it is Hecke-specific.

*When they do not*, something has to be checked, and at `n = 4` the case is
inhabited: §4j puts the Yang–Baxter rule and the Bokut–Shiao rule at `j = i − 1`
on the same leading monomial `σᵢσᵢ₋₁σᵢ`. It resolves for a sharper reason than
the first case — the two rules are **exact negatives**, and the leading
coefficients are `−1` and `+1`, so the S-polynomial

    lc₂ • YB − lc₁ • BS  =  1 • YB − (−1) • BS  =  YB + BS

vanishes identically. Both orderings of the pair, since the sign flips with them.

Together these cover every degenerate shape at `n = 4`: ten of the thirteen words
carry a single rule, and at the other three the only pair of distinct rules is
the Yang–Baxter/Bokut–Shiao one. That last sentence is a fact about the rule
list, not something proved here — the rule-level converse of
`heckeCompletedRewritingSystem_lm_cases` — so what is machine-checked is the two
mechanisms, not the covering claim. -/

namespace DegenerateYbBs

variable {n : ℕ} {i' i : Fin n}

theorem ne_of_succ (hi : i'.val + 1 = i.val) : i' ≠ i := by
  intro h; subst h; omega

/-- The Yang–Baxter rule leads with coefficient `−1`: deg-lex picks the word
starting with the larger generator, which is the *subtracted* term. -/
theorem yangBaxter_lc (hi : i'.val + 1 = i.val) :
    (yangBaxterRelation i' i).lc (heckeOrder n) = -1 := by
  show (yangBaxterRelation i' i).relation.coeff
    ((yangBaxterRelation i' i).lm (heckeOrder n)) = -1
  rw [yangBaxterRelation_lm i' i (by omega)]
  simp [yangBaxterRelation, AlgElement.ofTerms_coeff, ne_of_succ hi]

/-- The Bokut–Shiao rule at `j = i − 1` leads with coefficient `+1` on the same
word — it is oriented the other way round. -/
theorem bokutShiao_lc (hi : i'.val + 1 = i.val) :
    (bokutShiaoRelation i' i i').lc (heckeOrder n) = 1 := by
  show (bokutShiaoRelation i' i i').relation.coeff
    ((bokutShiaoRelation i' i i').lm (heckeOrder n)) = 1
  rw [bokutShiaoRelation_lm hi (le_refl _), bsWord₁_at_pred hi,
    bokutShiaoRelation_at_pred hi]
  simp [AlgElement.ofTerms_coeff, (ne_of_succ hi).symm]

/-- The two relations sum to zero, coefficient by coefficient. -/
theorem relations_add_eq_zero (hi : i'.val + 1 = i.val) (m : Monomial (HeckeGen n)) :
    (yangBaxterRelation i' i).relation.coeff m
      + (bokutShiaoRelation i' i i').relation.coeff m = 0 := by
  rw [bokutShiaoRelation_at_pred hi]
  show (AlgElement.ofTerms [([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], (1 : ℝ)),
        ([(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩], -1)]).coeff m + _ = 0
  rw [AlgElement.ofTerms_coeff, AlgElement.ofTerms_coeff]
  have hne := ne_of_succ hi
  by_cases h₁ : ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩] : Monomial (HeckeGen n)) = m
  · subst h₁; simp [hne]
  · by_cases h₂ : ([(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩] : Monomial (HeckeGen n)) = m
    · subst h₂; simp [hne, hne.symm]
    · simp [h₁, h₂]

/-- The degenerate composition of the two rules that share a leading monomial,
Yang–Baxter first. -/
noncomputable def ybBsOverlap (hi : i'.val + 1 = i.val) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := yangBaxterRelation i' i
  rule₂ := bokutShiaoRelation i' i i'
  left := []
  overlap := [⟨i⟩, ⟨i'⟩, ⟨i⟩]
  right := []
  lm₁_decomp := by rw [yangBaxterRelation_lm i' i (by omega)]; simp
  lm₂_decomp := by rw [bokutShiaoRelation_lm hi (le_refl _), bsWord₁_at_pred hi]; simp
  overlap_nonempty := by simp

/-- …and the same pair the other way round. -/
noncomputable def bsYbOverlap (hi : i'.val + 1 = i.val) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := bokutShiaoRelation i' i i'
  rule₂ := yangBaxterRelation i' i
  left := []
  overlap := [⟨i⟩, ⟨i'⟩, ⟨i⟩]
  right := []
  lm₁_decomp := by rw [bokutShiaoRelation_lm hi (le_refl _), bsWord₁_at_pred hi]; simp
  lm₂_decomp := by rw [yangBaxterRelation_lm i' i (by omega)]; simp
  overlap_nonempty := by simp

/-- **The Yang–Baxter/Bokut–Shiao S-polynomial is zero.** Not "reduces to zero" —
zero. -/
theorem ybBsOverlap_spoly_isZero (hi : i'.val + 1 = i.val) :
    (ybBsOverlap hi).spoly.isZero := by
  intro m
  show (bokutShiaoRelation i' i i').lc (heckeOrder n)
      * (AlgElement.contextMul [] (yangBaxterRelation i' i).relation []).coeff m
    - (yangBaxterRelation i' i).lc (heckeOrder n)
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i i').relation []).coeff m = 0
  rw [AlgElement.contextMul_nil_nil_coeff, AlgElement.contextMul_nil_nil_coeff,
    bokutShiao_lc hi, yangBaxter_lc hi]
  have := relations_add_eq_zero hi m
  linarith

/-- The other ordering, for the same reason with the signs exchanged. -/
theorem bsYbOverlap_spoly_isZero (hi : i'.val + 1 = i.val) :
    (bsYbOverlap hi).spoly.isZero := by
  intro m
  show (yangBaxterRelation i' i).lc (heckeOrder n)
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i i').relation []).coeff m
    - (bokutShiaoRelation i' i i').lc (heckeOrder n)
      * (AlgElement.contextMul [] (yangBaxterRelation i' i).relation []).coeff m = 0
  rw [AlgElement.contextMul_nil_nil_coeff, AlgElement.contextMul_nil_nil_coeff,
    bokutShiao_lc hi, yangBaxter_lc hi]
  have := relations_add_eq_zero hi m
  linarith

/-- **The Gröbner–Shirshov obligation for these compositions, discharged.** -/
theorem ybBsOverlap_resolves (hn : 0 < n) (hp : HeckeParams) (hi : i'.val + 1 = i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (ybBsOverlap hi).spoly nf ∧ nf.isZero :=
  reducesToNF_self_of_isZero (ybBsOverlap_spoly_isZero hi)

theorem bsYbOverlap_resolves (hn : 0 < n) (hp : HeckeParams) (hi : i'.val + 1 = i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (bsYbOverlap hi).spoly nf ∧ nf.isZero :=
  reducesToNF_self_of_isZero (bsYbOverlap_spoly_isZero hi)

/-! ### The same two rules, as an *inclusion* composition

`IsGrobnerShirshovBasis` has two halves. The inclusion half asks about a rule
whose leading monomial is a factor of another's — and a shared leading monomial
is the degenerate instance of that, with both contexts empty. So the Yang–Baxter
/ Bokut–Shiao pair appears there too, and resolves for the same reason. -/

/-- The inclusion composition of the two rules that share a leading monomial. -/
noncomputable def ybBsInclusion (hi : i'.val + 1 = i.val) :
    InclusionComposition (HeckeGen n) ℝ (heckeOrder n) where
  inner := yangBaxterRelation i' i
  outer := bokutShiaoRelation i' i i'
  left := []
  right := []
  decomposition := by
    rw [bokutShiaoRelation_lm hi (le_refl _), bsWord₁_at_pred hi,
      yangBaxterRelation_lm i' i (by omega)]
    simp

/-- …and the other way round. -/
noncomputable def bsYbInclusion (hi : i'.val + 1 = i.val) :
    InclusionComposition (HeckeGen n) ℝ (heckeOrder n) where
  inner := bokutShiaoRelation i' i i'
  outer := yangBaxterRelation i' i
  left := []
  right := []
  decomposition := by
    rw [bokutShiaoRelation_lm hi (le_refl _), bsWord₁_at_pred hi,
      yangBaxterRelation_lm i' i (by omega)]
    simp

theorem ybBsInclusion_spoly_isZero (hi : i'.val + 1 = i.val) :
    (ybBsInclusion hi).spoly.isZero := by
  refine (ybBsInclusion hi).spoly_isZero_of_scaled rfl rfl ?_
  intro m
  show (yangBaxterRelation i' i).lc (heckeOrder n)
      * (bokutShiaoRelation i' i i').relation.coeff m
    = (bokutShiaoRelation i' i i').lc (heckeOrder n)
      * (yangBaxterRelation i' i).relation.coeff m
  rw [yangBaxter_lc hi, bokutShiao_lc hi]
  have := relations_add_eq_zero hi m
  linarith

theorem bsYbInclusion_spoly_isZero (hi : i'.val + 1 = i.val) :
    (bsYbInclusion hi).spoly.isZero := by
  refine (bsYbInclusion hi).spoly_isZero_of_scaled rfl rfl ?_
  intro m
  show (bokutShiaoRelation i' i i').lc (heckeOrder n)
      * (yangBaxterRelation i' i).relation.coeff m
    = (yangBaxterRelation i' i).lc (heckeOrder n)
      * (bokutShiaoRelation i' i i').relation.coeff m
  rw [yangBaxter_lc hi, bokutShiao_lc hi]
  have := relations_add_eq_zero hi m
  linarith

theorem ybBsInclusion_resolves (hn : 0 < n) (hp : HeckeParams) (hi : i'.val + 1 = i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (ybBsInclusion hi).spoly nf ∧ nf.isZero :=
  reducesToNF_self_of_isZero (ybBsInclusion_spoly_isZero hi)

theorem bsYbInclusion_resolves (hn : 0 < n) (hp : HeckeParams) (hi : i'.val + 1 = i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (bsYbInclusion hi).spoly nf ∧ nf.isZero :=
  reducesToNF_self_of_isZero (bsYbInclusion_spoly_isZero hi)

end DegenerateYbBs

/-! ## §4m  Two structural facts, and what they leave

Both decided by the kernel at `n = 4`. Together they say the remaining work has a
much narrower shape than the enumeration alone suggests.

**Every proper overlap is a single letter.** Not one of the forty-five
non-degenerate shapes overlaps in two or more generators. The reason is visible
in the four families: every leading monomial is *descending after its first
letter* (`σᵢσᵢ`, `σⱼσᵢσⱼ` with `j = i+1`, `σᵢσⱼ` with `j < i`, and `bsWord₁`),
so a suffix of length ≥ 2 ends low-then-high while every prefix of length ≥ 2
starts high-then-low. Only a single letter can be both. Every composition is
therefore "`lm₁` ends with `x`, `lm₂` begins with `x`" — one shared generator.

**The leading monomials form an infix antichain**: none is a proper factor of
another. This is the stronger statement, and it settles the *inclusion* half of
`IsGrobnerShirshovBasis` structurally — `inclusion_contexts_empty` below shows
every inclusion composition of the completed system has both contexts empty,
with no hypothesis about which rules are involved. The inclusion half is then
exactly the shared-leading-monomial case, which `DegenerateYbBs` and
`InclusionComposition.spoly_isZero_of_self` between them handle.

What is left after this section is the forty-five proper overlap shapes, minus
the one #4879 resolved. -/

/-- **Every proper overlap is a single letter.** -/
theorem overlapTriples_four_proper_overlap_length_one :
    ((overlapTriples 4).filter (fun t => !t.1.isEmpty && !t.2.2.isEmpty)).all
      (fun t => t.2.1.length == 1) = true := by decide

/-- **No leading monomial of the completed system is a proper factor of
another.** -/
theorem completedLMSet_four_infix_antichain :
    ∀ a ∈ completedLMSet 4, ∀ b ∈ completedLMSet 4, a <:+: b → a = b := by decide

/-- **Every inclusion composition of the completed system has empty contexts.**

No hypothesis about *which* rules: `decomposition` exhibits `inner.lm` as an
infix of `outer.lm`, the antichain forces them equal, and lengths do the rest.
So the inclusion half of the Gröbner–Shirshov condition at `n = 4` is entirely
the shared-leading-monomial case — `InclusionComposition.spoly_isZero_of_self`
when the two rules coincide, `DegenerateYbBs.ybBsInclusion_spoly_isZero` when
they are the Yang–Baxter/Bokut–Shiao pair. -/
theorem inclusion_contexts_empty (hn : 0 < 4) (hp : HeckeParams)
    (ic : InclusionComposition (HeckeGen 4) ℝ (heckeOrder 4))
    (hin : ic.inner ∈ (heckeCompletedRewritingSystem 4 hn hp).rules)
    (hout : ic.outer ∈ (heckeCompletedRewritingSystem 4 hn hp).rules) :
    ic.left = [] ∧ ic.right = [] ∧
      ic.inner.lm (heckeOrder 4) = ic.outer.lm (heckeOrder 4) := by
  have heq : ic.inner.lm (heckeOrder 4) = ic.outer.lm (heckeOrder 4) :=
    completedLMSet_four_infix_antichain _ (heckeCompletedRewritingSystem_lm_mem hn hp _ hin)
      _ (heckeCompletedRewritingSystem_lm_mem hn hp _ hout)
      ⟨ic.left, ic.right, ic.decomposition.symm⟩
  have hlen := congrArg List.length ic.decomposition
  rw [heq] at hlen
  simp only [List.length_append] at hlen
  exact ⟨List.eq_nil_of_length_eq_zero (by omega),
    List.eq_nil_of_length_eq_zero (by omega), heq⟩

/-! ## §4n  The quadratic self-overlap, for every `n`

`σᵢσᵢ` overlaps `σᵢσᵢ` in the single letter `σᵢ`, over the ambient word `σᵢσᵢσᵢ`.
By §4m that is the *only* way the quadratic family meets itself, and there is one
such composition per generator — four of the forty-five proper shapes at `n = 4`.

They resolve for the strongest available reason: the S-polynomial is identically
zero. `heckeRelation i` is a polynomial in the single generator `σᵢ`, so every
monomial of its relation commutes with `σᵢ` as a word, and the two halves of the
S-polynomial are that relation slid past the same letter
(`AlgElement.contextMul_gen_comm`). Nothing here is specific to `n = 4`. -/

/-- Every monomial of the quadratic relation commutes with `σᵢ`: they are `σᵢσᵢ`,
`σᵢ` and the empty word, all powers of the one generator. -/
theorem heckeRelation_coeff_comm {n : ℕ} (i : Fin n) (hp : HeckeParams)
    (w : Monomial (HeckeGen n)) (hw : (heckeRelation i hp).relation.coeff w ≠ 0) :
    w ++ [(⟨i⟩ : HeckeGen n)] = [(⟨i⟩ : HeckeGen n)] ++ w := by
  by_cases h1 : w = [(⟨i⟩ : HeckeGen n), ⟨i⟩]
  · rw [h1]; rfl
  · by_cases h2 : w = [(⟨i⟩ : HeckeGen n)]
    · rw [h2]
    · by_cases h3 : w = ([] : Monomial (HeckeGen n))
      · rw [h3]; rfl
      · exact absurd (by
          simp [heckeRelation, AlgElement.ofTerms_coeff, Ne.symm h1, Ne.symm h2,
            Ne.symm h3]) hw

/-- The composition of the quadratic rule with itself over `σᵢσᵢσᵢ`. -/
noncomputable def quadSelfOverlap {n : ℕ} (i : Fin n) (hp : HeckeParams) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := heckeRelation i hp
  rule₂ := heckeRelation i hp
  left := [⟨i⟩]
  overlap := [⟨i⟩]
  right := [⟨i⟩]
  lm₁_decomp := by rw [heckeRelation_lm]; rfl
  lm₂_decomp := by rw [heckeRelation_lm]; rfl
  overlap_nonempty := by simp

/-- **The quadratic self-overlap has S-polynomial identically zero** — for every
`n` and every generator. -/
theorem quadSelfOverlap_spoly_isZero {n : ℕ} (i : Fin n) (hp : HeckeParams) :
    (quadSelfOverlap i hp).spoly.isZero := by
  intro m
  show (heckeRelation i hp).lc (heckeOrder n)
      * (AlgElement.contextMul [] (heckeRelation i hp).relation [⟨i⟩]).coeff m
    - (heckeRelation i hp).lc (heckeOrder n)
      * (AlgElement.contextMul [⟨i⟩] (heckeRelation i hp).relation []).coeff m = 0
  rw [AlgElement.contextMul_gen_comm ⟨i⟩ _ (heckeRelation_coeff_comm i hp) m, sub_self]

theorem quadSelfOverlap_resolves {n : ℕ} (hn : 0 < n) (i : Fin n) (hp : HeckeParams) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (quadSelfOverlap i hp).spoly nf ∧ nf.isZero :=
  reducesToNF_self_of_isZero (quadSelfOverlap_spoly_isZero i hp)

/-! ## §4o  Bokut–Shiao against far-commutation — the family §4g does one case of

`refuting_overlap_resolves` (§4g) is one composition at `(i,j) = (3,1)`, proved by
`decide` on concrete words. It is not an isolated fact: it is the `n = 4`,
`j = i − 1` instance of a family that resolves for every `n` and for the same
reason, and this section proves the family.

**The shape.** `bsWord₁ i j` ends in `σᵢ`; the far-commutation rule `σᵢσ_{j₀}`
begins with `σᵢ`. They overlap in that single letter (§4m says every proper
overlap is one letter), over the ambient word `descWord i j ++ [σᵢ, σ_{j₀}]`. Take
`j₀` to be the index just below `j`, so that the far-commutation rule extends the
descending run by exactly one step.

**Why it resolves.** Write out the S-polynomial:

    lc₂ • (BS · σ_{j₀}) − lc₁ • (descWord i j · FC)
      = (bsWord₁ i j ++ [σ_{j₀}] − bsWord₂ i' i j ++ [σ_{j₀}])
        − (descWord i j ++ [σᵢ, σ_{j₀}] − descWord i j ++ [σ_{j₀}, σᵢ])

`bsWord₁ i j ++ [σ_{j₀}]` *is* `descWord i j ++ [σᵢ, σ_{j₀}]`, so those cancel
without any word-distinctness argument. What survives is
`descWord i j ++ [σ_{j₀}, σᵢ] − bsWord₂ i' i j ++ [σ_{j₀}]`, and `descWord_snoc`
turns both into the Bokut–Shiao words one index lower:

    descWord i j ++ [σ_{j₀}] ++ [σᵢ] = descWord i j₀ ++ [σᵢ] = bsWord₁ i j₀
    bsWord₂ i' i j ++ [σ_{j₀}]                                = bsWord₂ i' i j₀

So the S-polynomial **is** `bokutShiaoRelation i' i j₀`, and one application of
that rule in empty context annihilates it. The obstruction at depth `j` is
repaired by the rule at depth `j₀ = j − 1`: the family completes itself
downwards. -/

/-- The mirror of `filter_desc_cons` at the bottom end. `List.finRange n` is
`Pairwise (· < ·)`, so once the head is `j₀` every later index is at least
`j = j₀ + 1` and the two predicates agree on the tail; before the head is
reached both fail, because `a < j₀ < j`. -/
theorem filter_desc_snoc {n : ℕ} {i j j₀ : Fin n}
    (hj : j₀.val + 1 = j.val) (hij : j.val ≤ i.val) :
    ∀ l : List (Fin n), l.Pairwise (fun a b => a.val < b.val) → j₀ ∈ l →
      l.filter (fun k => decide (j₀.val ≤ k.val ∧ k.val ≤ i.val))
        = j₀ :: l.filter (fun k => decide (j.val ≤ k.val ∧ k.val ≤ i.val)) := by
  intro l
  induction l with
  | nil => intro _ hm; simp at hm
  | cons a t ih =>
    intro hp hm
    rw [List.pairwise_cons] at hp
    obtain ⟨halt, hpt⟩ := hp
    rcases List.mem_cons.mp hm with haj | hmt
    · -- the head is `j₀`; every later index is at least `j`, so the tails agree
      subst haj
      have htail : t.filter (fun k => decide (j₀.val ≤ k.val ∧ k.val ≤ i.val))
          = t.filter (fun k => decide (j.val ≤ k.val ∧ k.val ≤ i.val)) := by
        refine List.filter_congr (fun b hb => ?_)
        have := halt b hb
        simp only [decide_eq_decide]
        omega
      simp only [List.filter_cons, decide_eq_true_eq, htail]
      rw [if_pos (by omega : j₀.val ≤ j₀.val ∧ j₀.val ≤ i.val),
        if_neg (by omega : ¬ (j.val ≤ j₀.val ∧ j₀.val ≤ i.val))]
    · -- the head is below `j₀`, so both predicates fail on it
      have hlt : a.val < j₀.val := halt _ hmt
      simp only [List.filter_cons, decide_eq_true_eq]
      rw [if_neg (by omega : ¬ (j₀.val ≤ a.val ∧ a.val ≤ i.val)),
        if_neg (by omega : ¬ (j.val ≤ a.val ∧ a.val ≤ i.val))]
      exact ih hpt hmt

/-- **The snoc lemma**: extending the descending range one index lower appends
that letter. Dual to `descWord_cons`, and the only new word identity §4o needs. -/
theorem descWord_snoc {n : ℕ} {i j j₀ : Fin n}
    (hj : j₀.val + 1 = j.val) (hij : j.val ≤ i.val) :
    descWord i j₀ = descWord i j ++ [(⟨j₀⟩ : HeckeGen n)] := by
  simp only [descWord, filter_desc_snoc hj hij (List.finRange n)
    (List.pairwise_lt_finRange n) (List.mem_finRange j₀),
    List.reverse_cons, List.map_append, List.map_cons, List.map_nil]

/-! ### Leading coefficients, and membership -/

/-- The Bokut–Shiao rule is monic: deg-lex picks `bsWord₁`, which carries `+1`. -/
theorem bokutShiaoRelation_lc {n : ℕ} {i' i j : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) :
    (bokutShiaoRelation i' i j).lc (heckeOrder n) = 1 := by
  have hii' : i' ≠ i := fun hcon => absurd (congrArg Fin.val hcon) (by omega)
  have hne : bsWord₂ i' i j ≠ bsWord₁ i j := by
    rw [bsWord₁_cons hi hj, bsWord₂]
    simp [hii']
  show (bokutShiaoRelation i' i j).relation.coeff
    ((bokutShiaoRelation i' i j).lm (heckeOrder n)) = 1
  rw [bokutShiaoRelation_lm hi hj]
  simp [bokutShiaoRelation, AlgElement.ofTerms_coeff, hne]

/-- The far-commutation rule is monic. -/
theorem farCommRelation_lc {n : ℕ} (i j : Fin n) (hij : j.val < i.val) :
    (farCommRelation i j).lc (heckeOrder n) = 1 := by
  have hji : j ≠ i := fun hcon => absurd (congrArg Fin.val hcon) (by omega)
  show (farCommRelation i j).relation.coeff
    ((farCommRelation i j).lm (heckeOrder n)) = 1
  rw [farCommRelation_lm i j hij]
  simp [farCommRelation, AlgElement.ofTerms_coeff, hji]

/-- Every Bokut–Shiao rule really is a rule of the completed system. The `(3,1)`
instance is `Completion.bs31_mem`; this is it for all indices. -/
theorem bokutShiaoRelation_mem {n : ℕ} (hn : 0 < n) (hp : HeckeParams) {i' i j : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) :
    bokutShiaoRelation i' i j ∈ (heckeCompletedRewritingSystem n hn hp).rules := by
  refine List.mem_append_right _ ?_
  refine List.mem_flatMap.mpr ⟨i, List.mem_finRange i, ?_⟩
  refine List.mem_flatMap.mpr ⟨i', List.mem_finRange i', ?_⟩
  exact List.mem_filterMap.mpr ⟨j, List.mem_finRange j, by rw [if_pos ⟨hi, hj⟩]⟩

/-! ### The composition, and its S-polynomial -/

namespace BokutShiaoFarComm

variable {n : ℕ} {i' i j j₀ : Fin n}

/-- The composition of `bokutShiaoRelation i' i j` with `farCommRelation i j₀`,
overlapping in the single letter `σᵢ`. -/
noncomputable def oc (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val)
    (hj0 : j₀.val + 1 = j.val) : OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := bokutShiaoRelation i' i j
  rule₂ := farCommRelation i j₀
  left := descWord i j
  overlap := [⟨i⟩]
  right := [⟨j₀⟩]
  lm₁_decomp := by rw [bokutShiaoRelation_lm hi hj]; rfl
  lm₂_decomp := by rw [farCommRelation_lm i j₀ (by omega)]; rfl
  overlap_nonempty := by simp

/-- **The S-polynomial is the Bokut–Shiao relation one index lower.** Coefficient
by coefficient — the ambient word cancels identically, so no word-distinctness
argument is needed anywhere. -/
theorem oc_spoly_coeff (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val)
    (hj0 : j₀.val + 1 = j.val) (m : Monomial (HeckeGen n)) :
    (oc hi hj hj0).spoly.coeff m = (bokutShiaoRelation i' i j₀).relation.coeff m := by
  have wA : ([] ++ bsWord₁ i j ++ [(⟨j₀⟩ : HeckeGen n)])
      = descWord i j ++ [(⟨i⟩ : HeckeGen n), ⟨j₀⟩] := by
    simp [bsWord₁]
  have wB : ([] ++ bsWord₂ i' i j ++ [(⟨j₀⟩ : HeckeGen n)]) = bsWord₂ i' i j₀ := by
    rw [bsWord₂, bsWord₂, descWord_snoc hj0 hj]
    simp
  have vA : (descWord i j ++ [(⟨i⟩ : HeckeGen n), ⟨j₀⟩] ++ ([] : Monomial (HeckeGen n)))
      = descWord i j ++ [(⟨i⟩ : HeckeGen n), ⟨j₀⟩] := by simp
  have vB : (descWord i j ++ [(⟨j₀⟩ : HeckeGen n), ⟨i⟩] ++ ([] : Monomial (HeckeGen n)))
      = bsWord₁ i j₀ := by
    rw [bsWord₁, descWord_snoc hj0 (by omega : j.val ≤ i.val)]
    simp
  show (farCommRelation i j₀).lc (heckeOrder n)
      * (AlgElement.contextMul []
          (AlgElement.ofTerms [(bsWord₁ i j, (1 : ℝ)), (bsWord₂ i' i j, -1)])
          [⟨j₀⟩]).coeff m
    - (bokutShiaoRelation i' i j).lc (heckeOrder n)
      * (AlgElement.contextMul (descWord i j)
          (AlgElement.ofTerms
            [([(⟨i⟩ : HeckeGen n), ⟨j₀⟩], (1 : ℝ)), ([(⟨j₀⟩ : HeckeGen n), ⟨i⟩], -1)])
          []).coeff m
    = (AlgElement.ofTerms [(bsWord₁ i j₀, (1 : ℝ)), (bsWord₂ i' i j₀, -1)]).coeff m
  rw [farCommRelation_lc i j₀ (by omega), bokutShiaoRelation_lc hi hj, one_mul, one_mul,
    AlgElement.contextMul_ofTerms_pair_coeff, AlgElement.contextMul_ofTerms_pair_coeff,
    wA, wB, vA, vB, AlgElement.ofTerms_coeff, AlgElement.ofTerms_coeff,
    AlgElement.ofTerms_coeff]
  simp only [List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;> norm_num

/-- **One step, to zero** — the general form of `refuting_overlap_resolves`. -/
theorem oc_resolves (hn : 0 < n) (hp : HeckeParams) (hi : i'.val + 1 = i.val)
    (hj : j.val ≤ i'.val) (hj0 : j₀.val + 1 = j.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hi hj hj0).spoly AlgElement.zero := by
  have hj0i' : j₀.val ≤ i'.val := by omega
  have hlm : (bokutShiaoRelation i' i j₀).lm (heckeOrder n) = bsWord₁ i j₀ :=
    bokutShiaoRelation_lm hi hj0i'
  have hcoeff : (oc hi hj hj0).spoly.coeff ([] ++ bsWord₁ i j₀ ++ []) = 1 := by
    rw [show ([] ++ bsWord₁ i j₀ ++ [] : Monomial (HeckeGen n)) = bsWord₁ i j₀ by simp,
      oc_spoly_coeff hi hj hj0, ← hlm]
    exact bokutShiaoRelation_lc hi hj0i'
  refine ⟨bokutShiaoRelation i' i j₀, bokutShiaoRelation_mem hn hp hi hj0i', [], [], 1,
    ?_, ?_, ?_⟩
  · rw [hlm, hcoeff]; norm_num
  · rw [hlm, hcoeff, bokutShiaoRelation_lc hi hj0i']; norm_num
  · intro m
    show (0 : ℝ) = (oc hi hj hj0).spoly.coeff m
      - 1 * (AlgElement.contextMul [] (bokutShiaoRelation i' i j₀).relation []).coeff m
    rw [AlgElement.contextMul_nil_nil_coeff, oc_spoly_coeff hi hj hj0]
    ring

theorem oc_reduces_to_zero (hn : 0 < n) (hp : HeckeParams) (hi : i'.val + 1 = i.val)
    (hj : j.val ≤ i'.val) (hj0 : j₀.val + 1 = j.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hi hj hj0).spoly nf ∧ nf.isZero :=
  ⟨AlgElement.zero,
    ⟨MultiStepReduction.step (MultiStepReduction.refl _) (oc_resolves hn hp hi hj hj0),
      isNormalForm_of_isZero AlgElement.isZero_zero⟩,
    AlgElement.isZero_zero⟩

end BokutShiaoFarComm

/-! ### The Yang–Baxter rule against far-commutation

§4j puts `yangBaxterRelation i' i` and `bokutShiaoRelation i' i i'` on the same
leading monomial, so the completed system carries *two* rules that compose with
`farCommRelation i j₀` in the shape above, and both are obligations. The second
one is `BokutShiaoFarComm.oc` at `j = i − 1`; this is the first.

They differ by a sign and nothing else: the two relations are exact negatives and
their leading coefficients are `+1` and `−1`, so the S-polynomial here is the
negative of the one there, and the same rule annihilates it with coefficient `−1`
in place of `+1`. `Completion.refuting_overlap_resolves` — §4e's obstruction — is
this composition at `n = 4`, `(i', i, j₀) = (2, 3, 1)`. -/

namespace YangBaxterFarComm

variable {n : ℕ} {i' i j₀ : Fin n}

/-- `descWord i (i−1) = σᵢσᵢ₋₁`. -/
theorem descWord_at_pred (hi : i'.val + 1 = i.val) :
    descWord i i' = [(⟨i⟩ : HeckeGen n), ⟨i'⟩] := by
  rw [descWord_cons hi (le_refl _), descWord_self]

/-- The composition of `yangBaxterRelation i' i` with `farCommRelation i j₀`. -/
noncomputable def oc (hi : i'.val + 1 = i.val) (hj0 : j₀.val + 1 = i'.val) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := yangBaxterRelation i' i
  rule₂ := farCommRelation i j₀
  left := descWord i i'
  overlap := [⟨i⟩]
  right := [⟨j₀⟩]
  lm₁_decomp := by rw [yangBaxterRelation_lm i' i (by omega), descWord_at_pred hi]; rfl
  lm₂_decomp := by rw [farCommRelation_lm i j₀ (by omega)]; rfl
  overlap_nonempty := by simp

/-- **The S-polynomial is minus the Bokut–Shiao relation at `j₀`.** -/
theorem oc_spoly_coeff (hi : i'.val + 1 = i.val) (hj0 : j₀.val + 1 = i'.val)
    (m : Monomial (HeckeGen n)) :
    (oc hi hj0).spoly.coeff m = -((bokutShiaoRelation i' i j₀).relation.coeff m) := by
  have hdesc : descWord i j₀ = descWord i i' ++ [(⟨j₀⟩ : HeckeGen n)] :=
    descWord_snoc hj0 (by omega)
  have wA : ([] ++ [(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩] ++ [(⟨j₀⟩ : HeckeGen n)])
      = bsWord₂ i' i j₀ := by
    rw [bsWord₂, descWord_snoc hj0 (le_refl _), descWord_self]
    simp
  have wB : ([] ++ [(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩] ++ [(⟨j₀⟩ : HeckeGen n)])
      = descWord i i' ++ [(⟨i⟩ : HeckeGen n), ⟨j₀⟩] ++ ([] : Monomial (HeckeGen n)) := by
    rw [descWord_at_pred hi]; simp
  have vB : (descWord i i' ++ [(⟨j₀⟩ : HeckeGen n), ⟨i⟩] ++ ([] : Monomial (HeckeGen n)))
      = bsWord₁ i j₀ := by
    rw [bsWord₁, hdesc]; simp
  show (farCommRelation i j₀).lc (heckeOrder n)
      * (AlgElement.contextMul []
          (AlgElement.ofTerms [([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], (1 : ℝ)),
                               ([(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩], -1)]) [⟨j₀⟩]).coeff m
    - (yangBaxterRelation i' i).lc (heckeOrder n)
      * (AlgElement.contextMul (descWord i i')
          (AlgElement.ofTerms
            [([(⟨i⟩ : HeckeGen n), ⟨j₀⟩], (1 : ℝ)), ([(⟨j₀⟩ : HeckeGen n), ⟨i⟩], -1)])
          []).coeff m
    = -((AlgElement.ofTerms [(bsWord₁ i j₀, (1 : ℝ)), (bsWord₂ i' i j₀, -1)]).coeff m)
  rw [farCommRelation_lc i j₀ (by omega), DegenerateYbBs.yangBaxter_lc hi, one_mul,
    AlgElement.contextMul_ofTerms_pair_coeff, AlgElement.contextMul_ofTerms_pair_coeff,
    wA, wB, vB, AlgElement.ofTerms_coeff, AlgElement.ofTerms_coeff,
    AlgElement.ofTerms_coeff]
  simp only [List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;> norm_num

/-- **One step, to zero**, with coefficient `−1` where the Bokut–Shiao version
uses `+1`. -/
theorem oc_resolves (hn : 0 < n) (hp : HeckeParams) (hi : i'.val + 1 = i.val)
    (hj0 : j₀.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hi hj0).spoly AlgElement.zero := by
  have hj0i' : j₀.val ≤ i'.val := by omega
  have hlm : (bokutShiaoRelation i' i j₀).lm (heckeOrder n) = bsWord₁ i j₀ :=
    bokutShiaoRelation_lm hi hj0i'
  have hcoeff : (oc hi hj0).spoly.coeff ([] ++ bsWord₁ i j₀ ++ []) = -1 := by
    rw [show ([] ++ bsWord₁ i j₀ ++ [] : Monomial (HeckeGen n)) = bsWord₁ i j₀ by simp,
      oc_spoly_coeff hi hj0, ← hlm]
    exact congrArg Neg.neg (bokutShiaoRelation_lc hi hj0i')
  refine ⟨bokutShiaoRelation i' i j₀, bokutShiaoRelation_mem hn hp hi hj0i', [], [], -1,
    ?_, ?_, ?_⟩
  · rw [hlm, hcoeff]; norm_num
  · rw [hlm, hcoeff, bokutShiaoRelation_lc hi hj0i']; norm_num
  · intro m
    show (0 : ℝ) = (oc hi hj0).spoly.coeff m
      - (-1) * (AlgElement.contextMul [] (bokutShiaoRelation i' i j₀).relation []).coeff m
    rw [AlgElement.contextMul_nil_nil_coeff, oc_spoly_coeff hi hj0]
    ring

theorem oc_reduces_to_zero (hn : 0 < n) (hp : HeckeParams) (hi : i'.val + 1 = i.val)
    (hj0 : j₀.val + 1 = i'.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hi hj0).spoly nf ∧ nf.isZero :=
  ⟨AlgElement.zero,
    ⟨MultiStepReduction.step (MultiStepReduction.refl _) (oc_resolves hn hp hi hj0),
      isNormalForm_of_isZero AlgElement.isZero_zero⟩,
    AlgElement.isZero_zero⟩

end YangBaxterFarComm

/-! ## §4p  Any two-term rule against the quadratic rule — one family, three steps

§4n and §4o each resolve a composition in *no* steps or *one*. This is the first
family that needs a genuine reduction chain, and it is the largest single block
left: **twelve** of the `n = 4` shapes, and again general in `n`.

**The observation that makes it one family.** Every two-term rule of the
completed system has its two words in *cyclic* position — the leading monomial is
`u' ++ [σₓ]` and the other word is `σ_y :: u'`, the same `u'` in both:

    farCommRelation i j      u' = [σᵢ]              x = j    y = j
    yangBaxterRelation i' i  u' = [σᵢ, σᵢ₋₁]        x = i    y = i−1
    bokutShiaoRelation i' i j  u' = descWord i j    x = i    y = i−1

(the last because `descWord i j = σᵢ :: descWord i₋₁ j`, so
`bsWord₂ i' i j = σᵢ₋₁ :: descWord i j`.) Nothing else about the rule is used.

**The chain.** The leading monomial ends in `σₓ`, so it overlaps `σₓσₓ` in that
one letter, over `u' ++ [σₓ, σₓ]`. The ambient word cancels and

    spoly = −(σ_y :: u' ++ [σₓ]) + h·(u' ++ [σₓ]) + u'      (times `c`)

Then, in three steps:

1. `σ_y :: u' ++ [σₓ]` **is** `σ_y · (leading monomial)`, so `r` applies in the
   context `(σ_y, ε)` and turns it into `σ_y σ_y u'`;
2. which begins `σ_yσ_y`, so the quadratic rule at `y` applies — *a different
   generator from the one the composition is about*, which is why this needs a
   chain rather than a single annihilation — leaving `h·(σ_y :: u') + u'`;
3. what is left is `h` times `r`'s own relation, killed by `r` in empty context.

Step 3 needs `h ≠ 0`, and that is where `HeckeParams` finally earns its
`q > 0 ∧ q ≠ 1`: the composition does **not** resolve at `q = 1`. -/

/-- `h = q − q⁻¹ ≠ 0`. `q > 0` and `q ≠ 1` are exactly what rules out `q² = 1`. -/
theorem HeckeParams.h_ne_zero (hp : HeckeParams) : hp.q - hp.q⁻¹ ≠ 0 := by
  have hq : hp.q ≠ 0 := ne_of_gt hp.q_pos
  intro hzero
  have hqq : hp.q = hp.q⁻¹ := sub_eq_zero.mp hzero
  have hsq : hp.q * hp.q = 1 := by
    nth_rewrite 2 [hqq]
    exact mul_inv_cancel₀ hq
  have hfac : (hp.q - 1) * (hp.q + 1) = 0 := by
    have h2 : (hp.q - 1) * (hp.q + 1) = hp.q * hp.q - 1 := by ring
    rw [h2, hsq, sub_self]
  rcases mul_eq_zero.mp hfac with h | h
  · exact hp.q_ne_one (by linarith)
  · linarith [hp.q_pos]

/-- The quadratic rule is monic. -/
theorem heckeRelation_lc {n : ℕ} (i : Fin n) (hp : HeckeParams) :
    (heckeRelation i hp).lc (heckeOrder n) = 1 := by
  show (heckeRelation i hp).relation.coeff
    ((heckeRelation i hp).lm (heckeOrder n)) = 1
  rw [heckeRelation_lm]
  simp [heckeRelation, AlgElement.ofTerms_coeff]

/-- …and is a rule of the completed system. -/
theorem heckeRelation_mem {n : ℕ} (hn : 0 < n) (hp : HeckeParams) (i : Fin n) :
    heckeRelation i hp ∈ (heckeCompletedRewritingSystem n hn hp).rules :=
  List.mem_append_left _ (List.mem_append_left _ (List.mem_append_left _
    (List.mem_map.mpr ⟨i, List.mem_finRange i, rfl⟩)))

/-- The Yang–Baxter rule is a rule of the completed system. -/
theorem yangBaxterRelation_mem {n : ℕ} (hn : 0 < n) (hp : HeckeParams) {i' i : Fin n}
    (hi : i'.val + 1 = i.val) :
    yangBaxterRelation i' i ∈ (heckeCompletedRewritingSystem n hn hp).rules :=
  List.mem_append_left _ (List.mem_append_left _ (List.mem_append_right _
    (List.mem_flatMap.mpr ⟨i', List.mem_finRange i',
      List.mem_filterMap.mpr ⟨i, List.mem_finRange i, by rw [if_pos hi.symm]⟩⟩)))

/-- The far-commutation rule is a rule of the completed system. -/
theorem farCommRelation_mem {n : ℕ} (hn : 0 < n) (hp : HeckeParams) {i j : Fin n}
    (hij : j.val + 1 < i.val) :
    farCommRelation i j ∈ (heckeCompletedRewritingSystem n hn hp).rules :=
  List.mem_append_left _ (List.mem_append_right _
    (List.mem_flatMap.mpr ⟨i, List.mem_finRange i,
      List.mem_filterMap.mpr ⟨j, List.mem_finRange j, by rw [if_pos hij]⟩⟩))

namespace CyclicQuad

variable {n : ℕ}

/-- The composition of a two-term rule whose leading monomial ends in `σₓ` with
the quadratic rule at `σₓ`. -/
noncomputable def oc (hp : HeckeParams) (r : ReductionRule (HeckeGen n) ℝ)
    (u' : Monomial (HeckeGen n)) (x : Fin n)
    (hlm : r.lm (heckeOrder n) = u' ++ [(⟨x⟩ : HeckeGen n)]) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := r
  rule₂ := heckeRelation x hp
  left := u'
  overlap := [⟨x⟩]
  right := [⟨x⟩]
  lm₁_decomp := hlm
  lm₂_decomp := by rw [heckeRelation_lm]; rfl
  overlap_nonempty := by simp

variable (hp : HeckeParams) (r : ReductionRule (HeckeGen n) ℝ)
  (u' : Monomial (HeckeGen n)) (x y : Fin n) (c : ℝ)

/-- **The S-polynomial**, three terms, with the ambient word already cancelled. -/
theorem oc_spoly_coeff
    (hrel : ∀ w, r.relation.coeff w = (AlgElement.ofTerms
      [(u' ++ [(⟨x⟩ : HeckeGen n)], c), ((⟨y⟩ : HeckeGen n) :: u', -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = u' ++ [(⟨x⟩ : HeckeGen n)])
    (hlc : r.lc (heckeOrder n) = c) (m : Monomial (HeckeGen n)) :
    (oc hp r u' x hlm).spoly.coeff m
      = (AlgElement.ofTerms
          [((⟨y⟩ : HeckeGen n) :: (u' ++ [(⟨x⟩ : HeckeGen n)]), -c),
           (u' ++ [(⟨x⟩ : HeckeGen n)], c * (hp.q - hp.q⁻¹)),
           (u', c)]).coeff m := by
  show (heckeRelation x hp).lc (heckeOrder n)
      * (AlgElement.contextMul [] r.relation [⟨x⟩]).coeff m
    - r.lc (heckeOrder n)
      * (AlgElement.contextMul u' (heckeRelation x hp).relation []).coeff m
    = _
  rw [heckeRelation_lc, hlc, one_mul,
    AlgElement.contextMul_coeff_congr [] [(⟨x⟩ : HeckeGen n)] hrel m]
  simp only [heckeRelation, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
    List.map_nil, List.nil_append, List.append_nil, List.cons_append,
    List.append_assoc, AlgElement.ofTerms_coeff,
    List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- The leading monomial and the other word have the same length, so length
cannot separate them — but `lc = c ≠ 0` can: were they equal the two terms would
cancel and the leading coefficient would be `0`. -/
theorem word_ne (hrel : ∀ w, r.relation.coeff w = (AlgElement.ofTerms
      [(u' ++ [(⟨x⟩ : HeckeGen n)], c), ((⟨y⟩ : HeckeGen n) :: u', -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = u' ++ [(⟨x⟩ : HeckeGen n)])
    (hlc : r.lc (heckeOrder n) = c) (hc : c ≠ 0) :
    ((⟨y⟩ : HeckeGen n) :: u') ≠ u' ++ [(⟨x⟩ : HeckeGen n)] := by
  intro heq
  refine hc ?_
  rw [← hlc]
  show r.relation.coeff (r.lm (heckeOrder n)) = 0
  rw [hlm, hrel, ← heq]
  simp [AlgElement.ofTerms_coeff]

/-- **Three steps, to zero.**

Step 1 applies `r` in the context `(σ_y, ε)`, step 2 the quadratic rule at `y` in
the context `(ε, u')`, step 3 `r` again in empty context. Only the three
"the targeted coefficient is non-zero" conditions need any word distinguished
from another; every `CoeffEq` holds unconditionally, because the cancellations
are between *coefficients* and do not care whether the words happen to
coincide. -/
theorem oc_reduces_to_zero (hn : 0 < n)
    (hrel : ∀ w, r.relation.coeff w = (AlgElement.ofTerms
      [(u' ++ [(⟨x⟩ : HeckeGen n)], c), ((⟨y⟩ : HeckeGen n) :: u', -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = u' ++ [(⟨x⟩ : HeckeGen n)])
    (hlc : r.lc (heckeOrder n) = c) (hc : c ≠ 0)
    (hr : r ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hp r u' x hlm).spoly nf ∧ nf.isZero := by
  have hh := hp.h_ne_zero
  have hwne := word_ne r u' x y c hrel hlm hlc hc
  have hne₁₂ : (u' ++ [(⟨x⟩ : HeckeGen n)])
      ≠ (⟨y⟩ : HeckeGen n) :: (u' ++ [(⟨x⟩ : HeckeGen n)]) := by
    intro h; have := congrArg List.length h
    simp only [List.length_append, List.length_cons, List.length_nil] at this
    omega
  have hne₁₃ : u' ≠ (⟨y⟩ : HeckeGen n) :: (u' ++ [(⟨x⟩ : HeckeGen n)]) := by
    intro h; have := congrArg List.length h
    simp only [List.length_append, List.length_cons, List.length_nil] at this
    omega
  have hneV₂ : (u' ++ [(⟨x⟩ : HeckeGen n)])
      ≠ (⟨y⟩ : HeckeGen n) :: (⟨y⟩ : HeckeGen n) :: u' := by
    intro h; have := congrArg List.length h
    simp only [List.length_append, List.length_cons, List.length_nil] at this
    omega
  have hneV₃ : u' ≠ (⟨y⟩ : HeckeGen n) :: (⟨y⟩ : HeckeGen n) :: u' := by
    intro h; have := congrArg List.length h
    simp only [List.length_cons] at this
    omega
  have s₁ : SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hp r u' x hlm).spoly
      (AlgElement.ofTerms
        [((⟨y⟩ : HeckeGen n) :: (⟨y⟩ : HeckeGen n) :: u', -c),
         (u' ++ [(⟨x⟩ : HeckeGen n)], c * (hp.q - hp.q⁻¹)), (u', c)]) := by
    have hval : (oc hp r u' x hlm).spoly.coeff
        ([(⟨y⟩ : HeckeGen n)] ++ r.lm (heckeOrder n) ++ []) = -c := by
      rw [hlm, show ([(⟨y⟩ : HeckeGen n)] ++ (u' ++ [(⟨x⟩ : HeckeGen n)]) ++ [])
          = (⟨y⟩ : HeckeGen n) :: (u' ++ [(⟨x⟩ : HeckeGen n)]) by simp,
        oc_spoly_coeff hp r u' x y c hrel hlm hlc]
      simp [AlgElement.ofTerms_coeff, hne₁₂, hne₁₃]
    refine ⟨r, hr, [⟨y⟩], [], -1, ?_, ?_, ?_⟩
    · rw [hval]; simpa using hc
    · rw [hval, hlc]; ring
    · intro m
      show _ = (oc hp r u' x hlm).spoly.coeff m
        - (-1) * (AlgElement.contextMul [(⟨y⟩ : HeckeGen n)] r.relation []).coeff m
      rw [oc_spoly_coeff hp r u' x y c hrel hlm hlc,
        AlgElement.contextMul_coeff_congr [(⟨y⟩ : HeckeGen n)] [] hrel m,
        AlgElement.contextMul_ofTerms_coeff]
      simp only [List.map_cons, List.map_nil, List.nil_append, List.append_nil,
        List.cons_append, AlgElement.ofTerms_coeff,
        List.filter_cons, List.filter_nil, decide_eq_true_eq]
      split_ifs <;>
        simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring
  have s₂ : SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        [((⟨y⟩ : HeckeGen n) :: (⟨y⟩ : HeckeGen n) :: u', -c),
         (u' ++ [(⟨x⟩ : HeckeGen n)], c * (hp.q - hp.q⁻¹)), (u', c)])
      (AlgElement.ofTerms
        [(u' ++ [(⟨x⟩ : HeckeGen n)], c * (hp.q - hp.q⁻¹)),
         ((⟨y⟩ : HeckeGen n) :: u', -(c * (hp.q - hp.q⁻¹)))]) := by
    have hval : (AlgElement.ofTerms
        [((⟨y⟩ : HeckeGen n) :: (⟨y⟩ : HeckeGen n) :: u', -c),
         (u' ++ [(⟨x⟩ : HeckeGen n)], c * (hp.q - hp.q⁻¹)), (u', c)]).coeff
        ([] ++ (heckeRelation y hp).lm (heckeOrder n) ++ u') = -c := by
      rw [heckeRelation_lm, show (([] : Monomial (HeckeGen n)) ++ [⟨y⟩, ⟨y⟩] ++ u')
        = (⟨y⟩ : HeckeGen n) :: (⟨y⟩ : HeckeGen n) :: u' by simp]
      simp [AlgElement.ofTerms_coeff, hneV₂, hneV₃]
    refine ⟨heckeRelation y hp, heckeRelation_mem hn hp y, [], u', -c, ?_, ?_, ?_⟩
    · rw [hval]; simpa using hc
    · rw [hval, heckeRelation_lc]; ring
    · intro m
      show _ = _ - (-c) * (AlgElement.contextMul [] (heckeRelation y hp).relation u').coeff m
      simp only [heckeRelation, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
        List.map_nil, List.nil_append, List.cons_append,
        AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
      split_ifs <;>
        simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring
  have s₃ : SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        [(u' ++ [(⟨x⟩ : HeckeGen n)], c * (hp.q - hp.q⁻¹)),
         ((⟨y⟩ : HeckeGen n) :: u', -(c * (hp.q - hp.q⁻¹)))])
      AlgElement.zero := by
    have hval : (AlgElement.ofTerms
        [(u' ++ [(⟨x⟩ : HeckeGen n)], c * (hp.q - hp.q⁻¹)),
         ((⟨y⟩ : HeckeGen n) :: u', -(c * (hp.q - hp.q⁻¹)))]).coeff
        ([] ++ r.lm (heckeOrder n) ++ []) = c * (hp.q - hp.q⁻¹) := by
      rw [hlm, show (([] : Monomial (HeckeGen n)) ++ (u' ++ [⟨x⟩]) ++ [])
        = u' ++ [(⟨x⟩ : HeckeGen n)] by simp]
      simp [AlgElement.ofTerms_coeff, hwne]
    refine ⟨r, hr, [], [], hp.q - hp.q⁻¹, ?_, ?_, ?_⟩
    · rw [hval]; exact mul_ne_zero hc hh
    · rw [hval, hlc]; ring
    · intro m
      show (0 : ℝ) = _
        - (hp.q - hp.q⁻¹) * (AlgElement.contextMul [] r.relation []).coeff m
      rw [AlgElement.contextMul_coeff_congr [] [] hrel m,
        AlgElement.contextMul_ofTerms_coeff]
      simp only [List.map_cons, List.map_nil, List.nil_append, List.append_nil,
        AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
      split_ifs <;>
        simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring
  exact ⟨AlgElement.zero,
    ⟨(((MultiStepReduction.refl _).step s₁).step s₂).step s₃,
      isNormalForm_of_isZero AlgElement.isZero_zero⟩,
    AlgElement.isZero_zero⟩

/-! ### The three instances

Each is one application of `oc_reduces_to_zero`; all the work is exhibiting the
rule's two words in cyclic form. Nothing else about the rule enters, which is the
point of stating the family abstractly. -/

/-- Far-commutation: `u' = [σᵢ]`, `x = y = j`, `c = 1`. -/
theorem farComm_quad_resolves {n : ℕ} (hn : 0 < n) (hp : HeckeParams) {i j : Fin n}
    (hij : j.val + 1 < i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hp (farCommRelation i j) [(⟨i⟩ : HeckeGen n)] j
        (farCommRelation_lm i j (by omega))).spoly nf ∧ nf.isZero :=
  oc_reduces_to_zero hp (farCommRelation i j) [(⟨i⟩ : HeckeGen n)] j j 1 hn
    (fun _ => rfl) (farCommRelation_lm i j (by omega))
    (farCommRelation_lc i j (by omega)) one_ne_zero
    (farCommRelation_mem hn hp hij)

/-- Yang–Baxter: `u' = [σᵢ, σᵢ₋₁]`, `x = i`, `y = i−1`, `c = −1`. Its two terms
appear in the opposite order to the family's normal form, which is exactly why
`hrel` is stated coefficientwise. -/
theorem yangBaxter_quad_resolves {n : ℕ} (hn : 0 < n) (hp : HeckeParams) {i' i : Fin n}
    (hi : i'.val + 1 = i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hp (yangBaxterRelation i' i) [(⟨i⟩ : HeckeGen n), ⟨i'⟩] i
        (yangBaxterRelation_lm i' i (by omega))).spoly nf ∧ nf.isZero := by
  refine oc_reduces_to_zero hp (yangBaxterRelation i' i)
    [(⟨i⟩ : HeckeGen n), ⟨i'⟩] i i' (-1) hn ?_
    (yangBaxterRelation_lm i' i (by omega))
    (DegenerateYbBs.yangBaxter_lc hi) (by norm_num)
    (yangBaxterRelation_mem hn hp hi)
  intro w
  show (AlgElement.ofTerms [([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], (1 : ℝ)),
      ([(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩], -1)]).coeff w = _
  simp only [List.cons_append, List.nil_append, AlgElement.ofTerms_coeff,
    List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Bokut–Shiao: `u' = descWord i j`, `x = i`, `y = i−1`, `c = 1`. The cyclic form
is `descWord_cons` — `bsWord₂ i' i j = σᵢ₋₁ :: descWord i j`. -/
theorem bokutShiao_quad_resolves {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    {i' i j : Fin n} (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hp (bokutShiaoRelation i' i j) (descWord i j) i
        (bokutShiaoRelation_lm hi hj)).spoly nf ∧ nf.isZero := by
  refine oc_reduces_to_zero hp (bokutShiaoRelation i' i j) (descWord i j) i i' 1 hn ?_
    (bokutShiaoRelation_lm hi hj) (bokutShiaoRelation_lc hi hj) one_ne_zero
    (bokutShiaoRelation_mem hn hp hi hj)
  intro w
  have hcyc : bsWord₂ i' i j = (⟨i'⟩ : HeckeGen n) :: descWord i j := by
    rw [bsWord₂, descWord_cons hi hj]
  show (AlgElement.ofTerms [(bsWord₁ i j, (1 : ℝ)), (bsWord₂ i' i j, -1)]).coeff w = _
  rw [hcyc]; rfl

end CyclicQuad

/-! ## §4q  The quadratic rule on the **left** — the mirror of §4p, and not its corollary

§4p composes a two-term rule with the quadratic rule at the letter its leading
monomial *ends* with. This is the other side: the quadratic rule first, against a
rule whose leading monomial *begins* with `σₓ`. The two are not related by any
symmetry the presentation has — `mulNF₄`-style left and right actions are
different maps, and the cyclic-position hypothesis the chain needs is the
**other** one:

    §4p    lm r = u' ++ [σₓ]   and   the other word is   σ_y :: u'
    §4q    lm r = σₓ :: u''    and   the other word is   u'' ++ [σ_z]

Both hold for far-commutation and Yang–Baxter. Only §4p's holds for a general
Bokut–Shiao rule, because `bsWord₂ i' i j = σᵢ₋₁ :: descWord i j` puts the extra
letter on the *left*. §4q therefore reaches Bokut–Shiao only at `j = i − 1`,
where the rule is Yang–Baxter anyway — and that is exactly why `Q2 × B120` needs
eight steps rather than three.

**The chain.** The ambient word is `σₓσₓ ++ u''`, the leading terms cancel, and

    spoly = c · [ (σₓ :: u'') ++ [σ_z]  −  h · (σₓ :: u'')  −  u'' ]

1. `(σₓ :: u'') ++ [σ_z]` is `lm r` followed by one letter, so `r` applies in the
   context `(ε, σ_z)` and turns it into `u'' ++ [σ_z, σ_z]`;
2. which ends `σ_zσ_z`, so the quadratic rule **at `z`** applies in the context
   `(u'', ε)`, leaving `h · (u'' ++ [σ_z]) + u''`;
3. what is left is `−h` times `r`'s own relation, killed by `r` in empty context.

As in §4p, step 3 needs `h ≠ 0`, and every `CoeffEq` holds unconditionally —
only the three "targeted coefficient is non-zero" side conditions need words
distinguished, and only one of those is not a length argument. -/

namespace CyclicQuadLeft

variable {n : ℕ}

variable (hp : HeckeParams) (r : ReductionRule (HeckeGen n) ℝ)
  (u'' : Monomial (HeckeGen n)) (x z : Fin n) (c : ℝ)

/-- The composition of the quadratic rule at `σₓ` with a two-term rule whose
leading monomial begins with `σₓ`. -/
noncomputable def oc (hlm : r.lm (heckeOrder n) = (⟨x⟩ : HeckeGen n) :: u'') :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := heckeRelation x hp
  rule₂ := r
  left := [⟨x⟩]
  overlap := [⟨x⟩]
  right := u''
  lm₁_decomp := by rw [heckeRelation_lm]; rfl
  lm₂_decomp := hlm
  overlap_nonempty := by simp

/-- **The S-polynomial**, three terms, ambient word already cancelled. -/
theorem oc_spoly_coeff
    (hrel : ∀ w, r.relation.coeff w = (AlgElement.ofTerms
      [((⟨x⟩ : HeckeGen n) :: u'', c), (u'' ++ [(⟨z⟩ : HeckeGen n)], -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = (⟨x⟩ : HeckeGen n) :: u'')
    (hlc : r.lc (heckeOrder n) = c) (m : Monomial (HeckeGen n)) :
    (oc hp r u'' x hlm).spoly.coeff m
      = (AlgElement.ofTerms
          [(((⟨x⟩ : HeckeGen n) :: u'') ++ [(⟨z⟩ : HeckeGen n)], c),
           ((⟨x⟩ : HeckeGen n) :: u'', -(c * (hp.q - hp.q⁻¹))),
           (u'', -c)]).coeff m := by
  show r.lc (heckeOrder n)
      * (AlgElement.contextMul [] (heckeRelation x hp).relation u'').coeff m
    - (heckeRelation x hp).lc (heckeOrder n)
      * (AlgElement.contextMul [(⟨x⟩ : HeckeGen n)] r.relation []).coeff m
    = _
  rw [heckeRelation_lc, hlc, one_mul,
    AlgElement.contextMul_coeff_congr [(⟨x⟩ : HeckeGen n)] [] hrel m]
  simp only [heckeRelation, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
    List.map_nil, List.nil_append, List.append_nil, List.cons_append,
    AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- The leading monomial and the other word have the same length, so length
cannot separate them; `lc = c ≠ 0` can. -/
theorem word_ne
    (hrel : ∀ w, r.relation.coeff w = (AlgElement.ofTerms
      [((⟨x⟩ : HeckeGen n) :: u'', c), (u'' ++ [(⟨z⟩ : HeckeGen n)], -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = (⟨x⟩ : HeckeGen n) :: u'')
    (hlc : r.lc (heckeOrder n) = c) (hc : c ≠ 0) :
    (u'' ++ [(⟨z⟩ : HeckeGen n)]) ≠ (⟨x⟩ : HeckeGen n) :: u'' := by
  intro heq
  refine hc ?_
  rw [← hlc]
  show r.relation.coeff (r.lm (heckeOrder n)) = 0
  rw [hlm, hrel, ← heq]
  simp [AlgElement.ofTerms_coeff]

/-- **Three steps, to zero.** -/
theorem oc_reduces_to_zero (hn : 0 < n)
    (hrel : ∀ w, r.relation.coeff w = (AlgElement.ofTerms
      [((⟨x⟩ : HeckeGen n) :: u'', c), (u'' ++ [(⟨z⟩ : HeckeGen n)], -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = (⟨x⟩ : HeckeGen n) :: u'')
    (hlc : r.lc (heckeOrder n) = c) (hc : c ≠ 0)
    (hr : r ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hp r u'' x hlm).spoly nf ∧ nf.isZero := by
  have hh := hp.h_ne_zero
  have hwne := word_ne r u'' x z c hrel hlm hlc hc
  have hneL : ((⟨x⟩ : HeckeGen n) :: (u'' ++ [(⟨z⟩ : HeckeGen n)]))
      ≠ (⟨x⟩ : HeckeGen n) :: u'' := by
    intro h; have := congrArg List.length h
    simp only [List.length_append, List.length_cons] at this
    omega
  have hneL' : ((⟨x⟩ : HeckeGen n) :: (u'' ++ [(⟨z⟩ : HeckeGen n)])) ≠ u'' := by
    intro h; have := congrArg List.length h
    simp only [List.length_append, List.length_cons] at this
    omega
  have hneV : (u'' ++ [(⟨z⟩ : HeckeGen n), (⟨z⟩ : HeckeGen n)])
      ≠ (⟨x⟩ : HeckeGen n) :: u'' := by
    intro h; have := congrArg List.length h
    simp only [List.length_append, List.length_cons] at this
    omega
  have hneV' : (u'' ++ [(⟨z⟩ : HeckeGen n), (⟨z⟩ : HeckeGen n)]) ≠ u'' := by
    intro h; have := congrArg List.length h
    simp only [List.length_append, List.length_cons] at this
    omega
  have s₁ : SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hp r u'' x hlm).spoly
      (AlgElement.ofTerms
        [(u'' ++ [(⟨z⟩ : HeckeGen n), (⟨z⟩ : HeckeGen n)], c),
         ((⟨x⟩ : HeckeGen n) :: u'', -(c * (hp.q - hp.q⁻¹))), (u'', -c)]) := by
    have hval : (oc hp r u'' x hlm).spoly.coeff
        ([] ++ r.lm (heckeOrder n) ++ [(⟨z⟩ : HeckeGen n)]) = c := by
      rw [hlm, show (([] : Monomial (HeckeGen n)) ++ ((⟨x⟩ : HeckeGen n) :: u'')
            ++ [(⟨z⟩ : HeckeGen n)])
          = ((⟨x⟩ : HeckeGen n) :: u'') ++ [(⟨z⟩ : HeckeGen n)] by simp,
        oc_spoly_coeff hp r u'' x z c hrel hlm hlc]
      simp [AlgElement.ofTerms_coeff, Ne.symm hneL, Ne.symm hneL']
    refine ⟨r, hr, [], [⟨z⟩], 1, ?_, ?_, ?_⟩
    · rw [hval]; exact hc
    · rw [hval, hlc]; ring
    · intro m
      show _ = (oc hp r u'' x hlm).spoly.coeff m
        - 1 * (AlgElement.contextMul [] r.relation [(⟨z⟩ : HeckeGen n)]).coeff m
      rw [oc_spoly_coeff hp r u'' x z c hrel hlm hlc,
        AlgElement.contextMul_coeff_congr [] [(⟨z⟩ : HeckeGen n)] hrel m,
        AlgElement.contextMul_ofTerms_coeff]
      simp only [List.map_cons, List.map_nil, List.nil_append,
        List.cons_append, List.append_assoc,
        AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
      split_ifs <;>
        simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring
  have s₂ : SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        [(u'' ++ [(⟨z⟩ : HeckeGen n), (⟨z⟩ : HeckeGen n)], c),
         ((⟨x⟩ : HeckeGen n) :: u'', -(c * (hp.q - hp.q⁻¹))), (u'', -c)])
      (AlgElement.ofTerms
        [(u'' ++ [(⟨z⟩ : HeckeGen n)], c * (hp.q - hp.q⁻¹)),
         ((⟨x⟩ : HeckeGen n) :: u'', -(c * (hp.q - hp.q⁻¹)))]) := by
    have hval : (AlgElement.ofTerms
        [(u'' ++ [(⟨z⟩ : HeckeGen n), (⟨z⟩ : HeckeGen n)], c),
         ((⟨x⟩ : HeckeGen n) :: u'', -(c * (hp.q - hp.q⁻¹))), (u'', -c)]).coeff
        (u'' ++ (heckeRelation z hp).lm (heckeOrder n) ++ []) = c := by
      rw [heckeRelation_lm, show (u'' ++ [(⟨z⟩ : HeckeGen n), ⟨z⟩] ++ ([] : Monomial (HeckeGen n)))
        = u'' ++ [(⟨z⟩ : HeckeGen n), (⟨z⟩ : HeckeGen n)] by simp]
      simp [AlgElement.ofTerms_coeff, Ne.symm hneV, Ne.symm hneV']
    refine ⟨heckeRelation z hp, heckeRelation_mem hn hp z, u'', [], c, ?_, ?_, ?_⟩
    · rw [hval]; exact hc
    · rw [hval, heckeRelation_lc]; ring
    · intro m
      show _ = _ - c * (AlgElement.contextMul u'' (heckeRelation z hp).relation []).coeff m
      simp only [heckeRelation, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
        List.map_nil, List.append_nil,
        AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
      split_ifs <;>
        simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring
  have s₃ : SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        [(u'' ++ [(⟨z⟩ : HeckeGen n)], c * (hp.q - hp.q⁻¹)),
         ((⟨x⟩ : HeckeGen n) :: u'', -(c * (hp.q - hp.q⁻¹)))])
      AlgElement.zero := by
    have hval : (AlgElement.ofTerms
        [(u'' ++ [(⟨z⟩ : HeckeGen n)], c * (hp.q - hp.q⁻¹)),
         ((⟨x⟩ : HeckeGen n) :: u'', -(c * (hp.q - hp.q⁻¹)))]).coeff
        ([] ++ r.lm (heckeOrder n) ++ []) = -(c * (hp.q - hp.q⁻¹)) := by
      rw [hlm, show (([] : Monomial (HeckeGen n)) ++ ((⟨x⟩ : HeckeGen n) :: u'') ++ [])
        = (⟨x⟩ : HeckeGen n) :: u'' by simp]
      simp [AlgElement.ofTerms_coeff, hwne]
    refine ⟨r, hr, [], [], -(hp.q - hp.q⁻¹), ?_, ?_, ?_⟩
    · rw [hval]
      exact neg_ne_zero.mpr (mul_ne_zero hc hh)
    · rw [hval, hlc]; ring
    · intro m
      show (0 : ℝ) = _
        - (-(hp.q - hp.q⁻¹)) * (AlgElement.contextMul [] r.relation []).coeff m
      rw [AlgElement.contextMul_coeff_congr [] [] hrel m,
        AlgElement.contextMul_ofTerms_coeff]
      simp only [List.map_cons, List.map_nil, List.nil_append, List.append_nil,
        AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
      split_ifs <;>
        simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring
  exact ⟨AlgElement.zero,
    ⟨(((MultiStepReduction.refl _).step s₁).step s₂).step s₃,
      isNormalForm_of_isZero AlgElement.isZero_zero⟩,
    AlgElement.isZero_zero⟩

/-! ### The instances

Far-commutation and Yang–Baxter satisfy §4q's cyclic-position hypothesis, and
Bokut–Shiao does **only at `j = i − 1`**, where §4j identifies it with
Yang–Baxter. That is the asymmetry with §4p, and it is not cosmetic: it is why
the general Bokut–Shiao rule against the quadratic rule on the left is an
eight-step composition rather than a three-step one, and so is *not* covered
here. -/

/-- Far-commutation: `u'' = [σⱼ]`, `x = z = i`, `c = 1`. -/
theorem quad_farComm_resolves {n : ℕ} (hn : 0 < n) (hp : HeckeParams) {i j : Fin n}
    (hij : j.val + 1 < i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hp (farCommRelation i j) [(⟨j⟩ : HeckeGen n)] i
        (farCommRelation_lm i j (by omega))).spoly nf ∧ nf.isZero :=
  oc_reduces_to_zero hp (farCommRelation i j) [(⟨j⟩ : HeckeGen n)] i i 1 hn
    (fun _ => rfl) (farCommRelation_lm i j (by omega))
    (farCommRelation_lc i j (by omega)) one_ne_zero
    (farCommRelation_mem hn hp hij)

/-- Yang–Baxter: `u'' = [σᵢ₋₁, σᵢ]`, `x = i`, `z = i − 1`, `c = −1`. Terms in the
opposite order to the family's normal form again, hence the coefficientwise
`hrel`. -/
theorem quad_yangBaxter_resolves {n : ℕ} (hn : 0 < n) (hp : HeckeParams) {i' i : Fin n}
    (hi : i'.val + 1 = i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hp (yangBaxterRelation i' i) [(⟨i'⟩ : HeckeGen n), ⟨i⟩] i
        (yangBaxterRelation_lm i' i (by omega))).spoly nf ∧ nf.isZero := by
  refine oc_reduces_to_zero hp (yangBaxterRelation i' i)
    [(⟨i'⟩ : HeckeGen n), ⟨i⟩] i i' (-1) hn ?_
    (yangBaxterRelation_lm i' i (by omega))
    (DegenerateYbBs.yangBaxter_lc hi) (by norm_num)
    (yangBaxterRelation_mem hn hp hi)
  intro w
  show (AlgElement.ofTerms [([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], (1 : ℝ)),
      ([(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩], -1)]).coeff w = _
  simp only [List.cons_append, List.nil_append, AlgElement.ofTerms_coeff,
    List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Bokut–Shiao **at `j = i − 1` only**. `bsWord₂ i' i j = σᵢ₋₁ :: descWord i j`
puts the extra letter on the left, so for `j < i − 1` the other word is not
`u'' ++ [σ_z]` and this family does not reach it. -/
theorem quad_bokutShiao_resolves {n : ℕ} (hn : 0 < n) (hp : HeckeParams) {i' i : Fin n}
    (hi : i'.val + 1 = i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hp (bokutShiaoRelation i' i i') [(⟨i'⟩ : HeckeGen n), ⟨i⟩] i
        (by rw [bokutShiaoRelation_lm hi (le_refl _), bsWord₁_at_pred hi])).spoly nf
      ∧ nf.isZero := by
  refine oc_reduces_to_zero hp (bokutShiaoRelation i' i i')
    [(⟨i'⟩ : HeckeGen n), ⟨i⟩] i i' 1 hn ?_
    (by rw [bokutShiaoRelation_lm hi (le_refl _), bsWord₁_at_pred hi])
    (bokutShiaoRelation_lc hi (le_refl _)) one_ne_zero
    (bokutShiaoRelation_mem hn hp hi (le_refl _))
  intro w
  rw [bokutShiaoRelation_at_pred hi]; rfl

end CyclicQuadLeft

/-! ## §4r  The braid self-overlap `σᵢσᵢ₋₁σᵢσᵢ₋₁σᵢ`

The single largest block of what remains at `n = 4`: **twelve** of the forty
compositions, and the classical one — the braid relation overlapping itself.

Three words carry it (`σ₁σ₀σ₁σ₀σ₁`, `σ₂σ₁σ₂σ₁σ₂`, `σ₃σ₂σ₃σ₂σ₃`) and each carries
*two* rules with the same leading monomial (§4j: Yang–Baxter, and Bokut–Shiao at
`j = i − 1`), so four ordered rule-pairs per word. Stating the family for an
abstract pair `r₁, r₂` — each with leading monomial `σᵢσᵢ₋₁σᵢ` and relation
`c·σᵢσᵢ₋₁σᵢ − c·σᵢ₋₁σᵢσᵢ₋₁` — covers all twelve at once, and generally in `n`.

**The S-polynomial is two terms.** Both rules lead on the ambient word, so it
cancels and nothing about `c₁`, `c₂` survives except their product:

    spoly = c₁c₂ · ( σᵢσᵢ₋₁σᵢ₋₁σᵢσᵢ₋₁  −  σᵢ₋₁σᵢσᵢ₋₁σᵢ₋₁σᵢ )

**The chain is eight steps**, derived from the `n = 4` confluence engine and
recorded here because it is the specification the remaining proof has to meet.
Writing `I = σᵢ`, `J = σᵢ₋₁`, and `K = c₁c₂`:

| # | target | rule | context | coefficient |
|---|---|---|---|---|
| 1 | `IJJIJ` | `Q_{i-1}` | `(I ∣ IJ)` | `K` |
| 2 | `JIJJI` | `Q_{i-1}` | `(JI ∣ I)` | `−K` |
| 3 | `IJIJ` | `r₁` | `(ε ∣ J)` | `K·h·c₁` |
| 4 | `JIJI` | `r₁` | `(J ∣ ε)` | `−K·h·c₁` |
| 5 | `JIJJ` | `Q_{i-1}` | `(JI ∣ ε)` | `K·h` |
| 6 | `JJIJ` | `Q_{i-1}` | `(ε ∣ IJ)` | `−K·h` |
| 7 | `IIJ` | `Q_i` | `(ε ∣ J)` | `K` |
| 8 | `JII` | `Q_i` | `(J ∣ ε)` | `−K` |

Four applications of the quadratic rule at `i − 1`, two of the braid rule itself,
two of the quadratic rule at `i`. No intermediate exceeds **five** terms, and
`h²` appears in exactly one of them (`F₅`) before cancelling. Steps 3 and 4 need
`c₁ · c₁ = 1` — both instances have `c = ±1` — because the step coefficient must
satisfy `c₃ · lc(r₁) = K·h` and `lc(r₁) = c₁`.

`h ≠ 0` is needed for steps 3–6, as in §4p and §4q. -/

namespace BraidSelfOverlap

variable {n : ℕ} (hp : HeckeParams) (i' i : Fin n) (c₁ c₂ : ℝ)

/-- `σᵢσᵢ₋₁σᵢ` — the shared leading monomial. -/
def wHi : Monomial (HeckeGen n) := [⟨i⟩, ⟨i'⟩, ⟨i⟩]

/-- `σᵢ₋₁σᵢσᵢ₋₁` — the other word of both rules. -/
def wLo : Monomial (HeckeGen n) := [⟨i'⟩, ⟨i⟩, ⟨i'⟩]

/-- The composition of two rules that both lead on `σᵢσᵢ₋₁σᵢ`, overlapping in the
middle letter — the braid relation against itself. -/
noncomputable def oc (r₁ r₂ : ReductionRule (HeckeGen n) ℝ)
    (hlm₁ : r₁.lm (heckeOrder n) = wHi i' i)
    (hlm₂ : r₂.lm (heckeOrder n) = wHi i' i) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := r₁
  rule₂ := r₂
  left := [⟨i⟩, ⟨i'⟩]
  overlap := [⟨i⟩]
  right := [⟨i'⟩, ⟨i⟩]
  lm₁_decomp := hlm₁
  lm₂_decomp := hlm₂
  overlap_nonempty := by simp

/-- **The S-polynomial: two terms, and the leading coefficients enter only as
their product.** The ambient word `σᵢσᵢ₋₁σᵢσᵢ₋₁σᵢ` is reached from both sides and
cancels. -/
theorem oc_spoly_coeff (r₁ r₂ : ReductionRule (HeckeGen n) ℝ)
    (hrel₁ : ∀ w, r₁.relation.coeff w
      = (AlgElement.ofTerms [(wHi i' i, c₁), (wLo i' i, -c₁)]).coeff w)
    (hrel₂ : ∀ w, r₂.relation.coeff w
      = (AlgElement.ofTerms [(wHi i' i, c₂), (wLo i' i, -c₂)]).coeff w)
    (hlm₁ : r₁.lm (heckeOrder n) = wHi i' i) (hlm₂ : r₂.lm (heckeOrder n) = wHi i' i)
    (hlc₁ : r₁.lc (heckeOrder n) = c₁) (hlc₂ : r₂.lc (heckeOrder n) = c₂)
    (m : Monomial (HeckeGen n)) :
    (oc i' i r₁ r₂ hlm₁ hlm₂).spoly.coeff m
      = (AlgElement.ofTerms
          [([(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i'⟩, ⟨i⟩, ⟨i'⟩], c₁ * c₂),
           ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩, ⟨i'⟩, ⟨i⟩], -(c₁ * c₂))]).coeff m := by
  show r₂.lc (heckeOrder n)
      * (AlgElement.contextMul [] r₁.relation [(⟨i'⟩ : HeckeGen n), ⟨i⟩]).coeff m
    - r₁.lc (heckeOrder n)
      * (AlgElement.contextMul [(⟨i⟩ : HeckeGen n), ⟨i'⟩] r₂.relation []).coeff m
    = _
  rw [hlc₁, hlc₂,
    AlgElement.contextMul_coeff_congr [] [(⟨i'⟩ : HeckeGen n), ⟨i⟩] hrel₁ m,
    AlgElement.contextMul_coeff_congr [(⟨i⟩ : HeckeGen n), ⟨i'⟩] [] hrel₂ m,
    AlgElement.contextMul_ofTerms_coeff, AlgElement.contextMul_ofTerms_coeff]
  simp only [wHi, wLo, List.map_cons, List.map_nil, List.nil_append, List.append_nil,
    List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

end BraidSelfOverlap

end UGB.GrobnerShirshov.Hecke
