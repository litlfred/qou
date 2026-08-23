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

/-- The two Bokut–Shiao words are distinct: they differ at their first letter,
`σᵢ` against `σᵢ₋₁`. `bokutShiaoRelation_lc` needs this to read the leading
coefficient off a two-term `ofTerms`, and `monicStep` needs it as `hLR`. -/
theorem bsWord₂_ne_bsWord₁ {n : ℕ} {i' i j : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) :
    bsWord₂ i' i j ≠ bsWord₁ i j := by
  have hii' : i' ≠ i := fun hcon => absurd (congrArg Fin.val hcon) (by omega)
  rw [bsWord₁_cons hi hj, bsWord₂]
  simp [hii']

/-- The Bokut–Shiao rule is monic: deg-lex picks `bsWord₁`, which carries `+1`. -/
theorem bokutShiaoRelation_lc {n : ℕ} {i' i j : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) :
    (bokutShiaoRelation i' i j).lc (heckeOrder n) = 1 := by
  have hne := bsWord₂_ne_bsWord₁ hi hj
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

/-! ### The chain

`F₀ … F₇` are the stages, `F₀` the S-polynomial. Named rather than inlined: each
appears three times — a step's source, its target, and its coefficient lemma —
and five-term elements written out three times over are unreadable.

Each step is its own theorem. Heartbeats are budgeted **per declaration**, and
eight steps against five-term elements do not fit one 200 000 budget; the same
splitting the H₄ generator tables needed. -/

/-- Stage `0` of the chain — the S-polynomial. -/
noncomputable def F0 (_hp : HeckeParams) (i' i : Fin n) (c₁ c₂ : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [([(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i'⟩, ⟨i⟩, ⟨i'⟩], c₁ * c₂),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩, ⟨i'⟩, ⟨i⟩], -(c₁ * c₂))]

/-- Stage `1` of the chain. -/
noncomputable def F1 (hp : HeckeParams) (i' i : Fin n) (c₁ c₂ : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [([(⟨i⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], c₁ * c₂),
     ([(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩, ⟨i'⟩], c₁ * c₂ * (hp.q - hp.q⁻¹)),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩, ⟨i'⟩, ⟨i⟩], -(c₁ * c₂))]

/-- Stage `2` of the chain. -/
noncomputable def F2 (hp : HeckeParams) (i' i : Fin n) (c₁ c₂ : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [([(⟨i⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], c₁ * c₂),
     ([(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩, ⟨i'⟩], c₁ * c₂ * (hp.q - hp.q⁻¹)),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i⟩], -(c₁ * c₂)),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩, ⟨i⟩], -(c₁ * c₂ * (hp.q - hp.q⁻¹)))]

/-- Stage `3` of the chain. -/
noncomputable def F3 (hp : HeckeParams) (i' i : Fin n) (c₁ c₂ : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [([(⟨i⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], c₁ * c₂),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i⟩], -(c₁ * c₂)),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩, ⟨i'⟩], c₁ * c₂ * (hp.q - hp.q⁻¹)),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩, ⟨i⟩], -(c₁ * c₂ * (hp.q - hp.q⁻¹)))]

/-- Stage `4` of the chain. -/
noncomputable def F4 (hp : HeckeParams) (i' i : Fin n) (c₁ c₂ : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [([(⟨i⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], c₁ * c₂),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i⟩], -(c₁ * c₂)),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩, ⟨i'⟩], c₁ * c₂ * (hp.q - hp.q⁻¹)),
     ([(⟨i'⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩, ⟨i'⟩], -(c₁ * c₂ * (hp.q - hp.q⁻¹)))]

/-- Stage `5` of the chain. -/
noncomputable def F5 (hp : HeckeParams) (i' i : Fin n) (c₁ c₂ : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [([(⟨i⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], c₁ * c₂),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i⟩], -(c₁ * c₂)),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩], c₁ * c₂ * (hp.q - hp.q⁻¹)),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], c₁ * c₂ * (hp.q - hp.q⁻¹) * (hp.q - hp.q⁻¹)),
     ([(⟨i'⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩, ⟨i'⟩], -(c₁ * c₂ * (hp.q - hp.q⁻¹)))]

/-- Stage `6` of the chain. -/
noncomputable def F6 (hp : HeckeParams) (i' i : Fin n) (c₁ c₂ : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [([(⟨i⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], c₁ * c₂),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i⟩], -(c₁ * c₂)),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩], c₁ * c₂ * (hp.q - hp.q⁻¹)),
     ([(⟨i⟩ : HeckeGen n), ⟨i'⟩], -(c₁ * c₂ * (hp.q - hp.q⁻¹)))]

/-- Stage `7` of the chain. -/
noncomputable def F7 (hp : HeckeParams) (i' i : Fin n) (c₁ c₂ : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i⟩], -(c₁ * c₂)),
     ([(⟨i'⟩ : HeckeGen n)], c₁ * c₂),
     ([(⟨i'⟩ : HeckeGen n), ⟨i⟩], c₁ * c₂ * (hp.q - hp.q⁻¹))]

theorem chainStep1 (hn : 0 < n) (hne : ((⟨i⟩ : HeckeGen n)) ≠ ⟨i'⟩) (hK : c₁ * c₂ ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F0 hp i' i c₁ c₂) (F1 hp i' i c₁ c₂) := by
  have hv : (F0 hp i' i c₁ c₂).coeff ([(⟨i⟩ : HeckeGen n)] ++ (heckeRelation i' hp).lm (heckeOrder n) ++ [(⟨i⟩ : HeckeGen n), ⟨i'⟩]) = c₁ * c₂ := by
    rw [heckeRelation_lm, show ([(⟨i⟩ : HeckeGen n)] ++ [(⟨i'⟩ : HeckeGen n), ⟨i'⟩] ++ [(⟨i⟩ : HeckeGen n), ⟨i'⟩] : Monomial (HeckeGen n)) = [(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i'⟩, ⟨i⟩, ⟨i'⟩] by simp]
    simp [F0, AlgElement.ofTerms_coeff, hne, hne.symm]
  refine ⟨heckeRelation i' hp, heckeRelation_mem hn hp i', [(⟨i⟩ : HeckeGen n)], [(⟨i⟩ : HeckeGen n), ⟨i'⟩], c₁ * c₂, ?_, ?_, ?_⟩
  · rw [hv]; exact hK
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (c₁ * c₂) * (AlgElement.contextMul [(⟨i⟩ : HeckeGen n)] (heckeRelation i' hp).relation [(⟨i⟩ : HeckeGen n), ⟨i'⟩]).coeff m
    simp only [F0, F1, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem chainStep2 (hn : 0 < n) (hne : ((⟨i⟩ : HeckeGen n)) ≠ ⟨i'⟩) (hK : c₁ * c₂ ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F1 hp i' i c₁ c₂) (F2 hp i' i c₁ c₂) := by
  have hv : (F1 hp i' i c₁ c₂).coeff ([(⟨i'⟩ : HeckeGen n), ⟨i⟩] ++ (heckeRelation i' hp).lm (heckeOrder n) ++ [(⟨i⟩ : HeckeGen n)]) = -(c₁ * c₂) := by
    rw [heckeRelation_lm, show ([(⟨i'⟩ : HeckeGen n), ⟨i⟩] ++ [(⟨i'⟩ : HeckeGen n), ⟨i'⟩] ++ [(⟨i⟩ : HeckeGen n)] : Monomial (HeckeGen n)) = [(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩, ⟨i'⟩, ⟨i⟩] by simp]
    simp [F1, AlgElement.ofTerms_coeff, hne, hne.symm]
  refine ⟨heckeRelation i' hp, heckeRelation_mem hn hp i', [(⟨i'⟩ : HeckeGen n), ⟨i⟩], [(⟨i⟩ : HeckeGen n)], -(c₁ * c₂), ?_, ?_, ?_⟩
  · rw [hv]; exact neg_ne_zero.mpr hK
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (-(c₁ * c₂)) * (AlgElement.contextMul [(⟨i'⟩ : HeckeGen n), ⟨i⟩] (heckeRelation i' hp).relation [(⟨i⟩ : HeckeGen n)]).coeff m
    simp only [F1, F2, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem chainStep3 (hn : 0 < n) (hne : ((⟨i⟩ : HeckeGen n)) ≠ ⟨i'⟩) (hK : c₁ * c₂ ≠ 0) (hh : (hp.q - hp.q⁻¹) ≠ 0)
    (r₁ : ReductionRule (HeckeGen n) ℝ)
    (hrel₁ : ∀ w, r₁.relation.coeff w
      = (AlgElement.ofTerms [(wHi i' i, c₁), (wLo i' i, -c₁)]).coeff w)
    (hlm₁ : r₁.lm (heckeOrder n) = wHi i' i) (hlc₁ : r₁.lc (heckeOrder n) = c₁)
    (hsq : c₁ * c₁ = 1) (hr₁ : r₁ ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F2 hp i' i c₁ c₂) (F3 hp i' i c₁ c₂) := by
  have hv : (F2 hp i' i c₁ c₂).coeff ([] ++ (r₁).lm (heckeOrder n) ++ [(⟨i'⟩ : HeckeGen n)]) = c₁ * c₂ * (hp.q - hp.q⁻¹) := by
    rw [hlm₁, show ([] ++ wHi i' i ++ [(⟨i'⟩ : HeckeGen n)] : Monomial (HeckeGen n)) = [(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩, ⟨i'⟩] by simp [wHi]]
    simp [F2, AlgElement.ofTerms_coeff, hne, hne.symm]
  have hc3 : c₁ ^ 3 = c₁ := by
    have h3 : c₁ ^ 3 = c₁ * (c₁ * c₁) := by ring
    rw [h3, hsq, mul_one]
  refine ⟨r₁, hr₁, [], [(⟨i'⟩ : HeckeGen n)], c₁ * c₂ * (hp.q - hp.q⁻¹) * c₁, ?_, ?_, ?_⟩
  · rw [hv]; exact mul_ne_zero hK hh
  · rw [hv, hlc₁]
    rw [mul_assoc, hsq, mul_one]
  · intro m
    show _ = _ - (c₁ * c₂ * (hp.q - hp.q⁻¹) * c₁) * (AlgElement.contextMul [] (r₁).relation [(⟨i'⟩ : HeckeGen n)]).coeff m
    rw [AlgElement.contextMul_coeff_congr [] [(⟨i'⟩ : HeckeGen n)] hrel₁ m,
      AlgElement.contextMul_ofTerms_coeff]
    simp only [F2, F3, wHi, wLo,
      List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;>
      ring_nf <;> (try simp only [hc3]) <;> (try ring)

theorem chainStep4 (hn : 0 < n) (hne : ((⟨i⟩ : HeckeGen n)) ≠ ⟨i'⟩) (hK : c₁ * c₂ ≠ 0) (hh : (hp.q - hp.q⁻¹) ≠ 0)
    (r₁ : ReductionRule (HeckeGen n) ℝ)
    (hrel₁ : ∀ w, r₁.relation.coeff w
      = (AlgElement.ofTerms [(wHi i' i, c₁), (wLo i' i, -c₁)]).coeff w)
    (hlm₁ : r₁.lm (heckeOrder n) = wHi i' i) (hlc₁ : r₁.lc (heckeOrder n) = c₁)
    (hsq : c₁ * c₁ = 1) (hr₁ : r₁ ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F3 hp i' i c₁ c₂) (F4 hp i' i c₁ c₂) := by
  have hv : (F3 hp i' i c₁ c₂).coeff ([(⟨i'⟩ : HeckeGen n)] ++ (r₁).lm (heckeOrder n) ++ []) = -(c₁ * c₂ * (hp.q - hp.q⁻¹)) := by
    rw [hlm₁, show ([(⟨i'⟩ : HeckeGen n)] ++ wHi i' i ++ [] : Monomial (HeckeGen n)) = [(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩, ⟨i⟩] by simp [wHi]]
    simp [F3, AlgElement.ofTerms_coeff, hne, hne.symm]
  have hc3 : c₁ ^ 3 = c₁ := by
    have h3 : c₁ ^ 3 = c₁ * (c₁ * c₁) := by ring
    rw [h3, hsq, mul_one]
  refine ⟨r₁, hr₁, [(⟨i'⟩ : HeckeGen n)], [], -(c₁ * c₂ * (hp.q - hp.q⁻¹) * c₁), ?_, ?_, ?_⟩
  · rw [hv]; exact neg_ne_zero.mpr (mul_ne_zero hK hh)
  · rw [hv, hlc₁]
    rw [neg_mul, mul_assoc, hsq, mul_one]
  · intro m
    show _ = _ - (-(c₁ * c₂ * (hp.q - hp.q⁻¹) * c₁)) * (AlgElement.contextMul [(⟨i'⟩ : HeckeGen n)] (r₁).relation []).coeff m
    rw [AlgElement.contextMul_coeff_congr [(⟨i'⟩ : HeckeGen n)] [] hrel₁ m,
      AlgElement.contextMul_ofTerms_coeff]
    simp only [F3, F4, wHi, wLo,
      List.map_cons, List.map_nil, List.nil_append, List.append_nil,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;>
      ring_nf <;> (try simp only [hc3]) <;> (try ring)

theorem chainStep5 (hn : 0 < n) (hne : ((⟨i⟩ : HeckeGen n)) ≠ ⟨i'⟩) (hK : c₁ * c₂ ≠ 0) (hh : (hp.q - hp.q⁻¹) ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F4 hp i' i c₁ c₂) (F5 hp i' i c₁ c₂) := by
  have hv : (F4 hp i' i c₁ c₂).coeff ([(⟨i'⟩ : HeckeGen n), ⟨i⟩] ++ (heckeRelation i' hp).lm (heckeOrder n) ++ []) = c₁ * c₂ * (hp.q - hp.q⁻¹) := by
    rw [heckeRelation_lm, show ([(⟨i'⟩ : HeckeGen n), ⟨i⟩] ++ [(⟨i'⟩ : HeckeGen n), ⟨i'⟩] ++ [] : Monomial (HeckeGen n)) = [(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩, ⟨i'⟩] by simp]
    simp [F4, AlgElement.ofTerms_coeff, hne, hne.symm]
  refine ⟨heckeRelation i' hp, heckeRelation_mem hn hp i', [(⟨i'⟩ : HeckeGen n), ⟨i⟩], [], c₁ * c₂ * (hp.q - hp.q⁻¹), ?_, ?_, ?_⟩
  · rw [hv]; exact mul_ne_zero hK hh
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (c₁ * c₂ * (hp.q - hp.q⁻¹)) * (AlgElement.contextMul [(⟨i'⟩ : HeckeGen n), ⟨i⟩] (heckeRelation i' hp).relation []).coeff m
    simp only [F4, F5, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append, List.append_nil,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem chainStep6 (hn : 0 < n) (hne : ((⟨i⟩ : HeckeGen n)) ≠ ⟨i'⟩) (hK : c₁ * c₂ ≠ 0) (hh : (hp.q - hp.q⁻¹) ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F5 hp i' i c₁ c₂) (F6 hp i' i c₁ c₂) := by
  have hv : (F5 hp i' i c₁ c₂).coeff ([] ++ (heckeRelation i' hp).lm (heckeOrder n) ++ [(⟨i⟩ : HeckeGen n), ⟨i'⟩]) = -(c₁ * c₂ * (hp.q - hp.q⁻¹)) := by
    rw [heckeRelation_lm, show ([] ++ [(⟨i'⟩ : HeckeGen n), ⟨i'⟩] ++ [(⟨i⟩ : HeckeGen n), ⟨i'⟩] : Monomial (HeckeGen n)) = [(⟨i'⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩, ⟨i'⟩] by simp]
    simp [F5, AlgElement.ofTerms_coeff, hne]
  refine ⟨heckeRelation i' hp, heckeRelation_mem hn hp i', [], [(⟨i⟩ : HeckeGen n), ⟨i'⟩], -(c₁ * c₂ * (hp.q - hp.q⁻¹)), ?_, ?_, ?_⟩
  · rw [hv]; exact neg_ne_zero.mpr (mul_ne_zero hK hh)
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (-(c₁ * c₂ * (hp.q - hp.q⁻¹))) * (AlgElement.contextMul [] (heckeRelation i' hp).relation [(⟨i⟩ : HeckeGen n), ⟨i'⟩]).coeff m
    simp only [F5, F6, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem chainStep7 (hn : 0 < n) (hne : ((⟨i⟩ : HeckeGen n)) ≠ ⟨i'⟩) (hK : c₁ * c₂ ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F6 hp i' i c₁ c₂) (F7 hp i' i c₁ c₂) := by
  have hv : (F6 hp i' i c₁ c₂).coeff ([] ++ (heckeRelation i hp).lm (heckeOrder n) ++ [(⟨i'⟩ : HeckeGen n)]) = c₁ * c₂ := by
    rw [heckeRelation_lm, show ([] ++ [(⟨i⟩ : HeckeGen n), ⟨i⟩] ++ [(⟨i'⟩ : HeckeGen n)] : Monomial (HeckeGen n)) = [(⟨i⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩] by simp]
    simp [F6, AlgElement.ofTerms_coeff, hne, hne.symm]
  refine ⟨heckeRelation i hp, heckeRelation_mem hn hp i, [], [(⟨i'⟩ : HeckeGen n)], c₁ * c₂, ?_, ?_, ?_⟩
  · rw [hv]; exact hK
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (c₁ * c₂) * (AlgElement.contextMul [] (heckeRelation i hp).relation [(⟨i'⟩ : HeckeGen n)]).coeff m
    simp only [F6, F7, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem chainStep8 (hn : 0 < n) (hK : c₁ * c₂ ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F7 hp i' i c₁ c₂) (AlgElement.zero) := by
  have hv : (F7 hp i' i c₁ c₂).coeff ([(⟨i'⟩ : HeckeGen n)] ++ (heckeRelation i hp).lm (heckeOrder n) ++ []) = -(c₁ * c₂) := by
    rw [heckeRelation_lm, show ([(⟨i'⟩ : HeckeGen n)] ++ [(⟨i⟩ : HeckeGen n), ⟨i⟩] ++ [] : Monomial (HeckeGen n)) = [(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i⟩] by simp]
    simp [F7, AlgElement.ofTerms_coeff]
  refine ⟨heckeRelation i hp, heckeRelation_mem hn hp i, [(⟨i'⟩ : HeckeGen n)], [], -(c₁ * c₂), ?_, ?_, ?_⟩
  · rw [hv]; exact neg_ne_zero.mpr hK
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (-(c₁ * c₂)) * (AlgElement.contextMul [(⟨i'⟩ : HeckeGen n)] (heckeRelation i hp).relation []).coeff m
    simp only [F7, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff,
      AlgElement.zero, List.map_cons, List.map_nil, List.nil_append, List.append_nil,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Eight steps, to zero.**

`reducesToZero_congr` (§6) makes the last join: the chain runs on `F₀`, and
`oc_spoly_coeff` says the S-polynomial is coefficientwise `F₀`. That congruence
was built for the negation transfer; this is where it first pays. -/
theorem oc_reduces_to_zero (hn : 0 < n) (r₁ r₂ : ReductionRule (HeckeGen n) ℝ)
    (hrel₁ : ∀ w, r₁.relation.coeff w
      = (AlgElement.ofTerms [(wHi i' i, c₁), (wLo i' i, -c₁)]).coeff w)
    (hrel₂ : ∀ w, r₂.relation.coeff w
      = (AlgElement.ofTerms [(wHi i' i, c₂), (wLo i' i, -c₂)]).coeff w)
    (hlm₁ : r₁.lm (heckeOrder n) = wHi i' i) (hlm₂ : r₂.lm (heckeOrder n) = wHi i' i)
    (hlc₁ : r₁.lc (heckeOrder n) = c₁) (hlc₂ : r₂.lc (heckeOrder n) = c₂)
    (hc₁ : c₁ ≠ 0) (hc₂ : c₂ ≠ 0) (hsq : c₁ * c₁ = 1) (hii : i'.val + 1 = i.val)
    (hr₁ : r₁ ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i' i r₁ r₂ hlm₁ hlm₂).spoly nf ∧ nf.isZero := by
  have hh := hp.h_ne_zero
  have hK : c₁ * c₂ ≠ 0 := mul_ne_zero hc₁ hc₂
  have hne : ((⟨i⟩ : HeckeGen n)) ≠ ⟨i'⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  refine reducesToZero_congr ⟨AlgElement.zero,
    ⟨(MultiStepReduction.refl _)
      |>.step (chainStep1 hp i' i c₁ c₂ hn hne hK)
      |>.step (chainStep2 hp i' i c₁ c₂ hn hne hK)
      |>.step (chainStep3 hp i' i c₁ c₂ hn hne hK hh r₁ hrel₁ hlm₁ hlc₁ hsq hr₁)
      |>.step (chainStep4 hp i' i c₁ c₂ hn hne hK hh r₁ hrel₁ hlm₁ hlc₁ hsq hr₁)
      |>.step (chainStep5 hp i' i c₁ c₂ hn hne hK hh)
      |>.step (chainStep6 hp i' i c₁ c₂ hn hne hK hh)
      |>.step (chainStep7 hp i' i c₁ c₂ hn hne hK)
      |>.step (chainStep8 hp i' i c₁ c₂ hn hK),
      isNormalForm_of_isZero AlgElement.isZero_zero⟩, AlgElement.isZero_zero⟩ ?_
  intro m
  exact oc_spoly_coeff i' i c₁ c₂ r₁ r₂ hrel₁ hrel₂ hlm₁ hlm₂ hlc₁ hlc₂ m

/-! ### The four instances

`wHi i' i` is the shared leading monomial of `yangBaxterRelation i' i` and
`bokutShiaoRelation i' i i'` (§4j), so each of `r₁`, `r₂` may be either — four
ordered pairs, and at `n = 4` three choices of `i`, giving the **twelve**
compositions this family exists for.

Only `r₁` needs `c₁ * c₁ = 1` and membership; `r₂` enters through its relation,
leading monomial and leading coefficient alone. -/

/-- The Yang–Baxter rule in the shape §4r wants, at `c = −1`. Its two terms are
listed in the opposite order, hence the coefficientwise statement. -/
theorem yb_hrel (_hi : i'.val + 1 = i.val) (w : Monomial (HeckeGen n)) :
    (yangBaxterRelation i' i).relation.coeff w
      = (AlgElement.ofTerms [(wHi i' i, (-1 : ℝ)), (wLo i' i, -(-1 : ℝ))]).coeff w := by
  show (AlgElement.ofTerms [([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], (1 : ℝ)),
      ([(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩], -1)]).coeff w = _
  simp only [wHi, wLo, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- The Bokut–Shiao rule at `j = i − 1`, at `c = 1`. Same terms, same order. -/
theorem bs_hrel (hi : i'.val + 1 = i.val) (w : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i' i i').relation.coeff w
      = (AlgElement.ofTerms [(wHi i' i, (1 : ℝ)), (wLo i' i, -(1 : ℝ))]).coeff w := by
  rw [bokutShiaoRelation_at_pred hi]; rfl

theorem yb_hlm (hi : i'.val + 1 = i.val) :
    (yangBaxterRelation i' i).lm (heckeOrder n) = wHi i' i :=
  yangBaxterRelation_lm i' i (by omega)

theorem bs_hlm (hi : i'.val + 1 = i.val) :
    (bokutShiaoRelation i' i i').lm (heckeOrder n) = wHi i' i := by
  rw [bokutShiaoRelation_lm hi (le_refl _), bsWord₁_at_pred hi]; rfl

/-- **Yang–Baxter against Yang–Baxter.** -/
theorem yb_yb_resolves (hn : 0 < n) (hi : i'.val + 1 = i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i' i (yangBaxterRelation i' i) (yangBaxterRelation i' i)
        (yb_hlm i' i hi) (yb_hlm i' i hi)).spoly nf ∧ nf.isZero :=
  oc_reduces_to_zero hp i' i (-1) (-1) hn _ _ (yb_hrel i' i hi) (yb_hrel i' i hi)
    (yb_hlm i' i hi) (yb_hlm i' i hi)
    (DegenerateYbBs.yangBaxter_lc hi) (DegenerateYbBs.yangBaxter_lc hi)
    (by norm_num) (by norm_num) (by norm_num) hi (yangBaxterRelation_mem hn hp hi)

/-- **Yang–Baxter against Bokut–Shiao.** -/
theorem yb_bs_resolves (hn : 0 < n) (hi : i'.val + 1 = i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i' i (yangBaxterRelation i' i) (bokutShiaoRelation i' i i')
        (yb_hlm i' i hi) (bs_hlm i' i hi)).spoly nf ∧ nf.isZero :=
  oc_reduces_to_zero hp i' i (-1) 1 hn _ _ (yb_hrel i' i hi) (bs_hrel i' i hi)
    (yb_hlm i' i hi) (bs_hlm i' i hi)
    (DegenerateYbBs.yangBaxter_lc hi) (bokutShiaoRelation_lc hi (le_refl _))
    (by norm_num) one_ne_zero (by norm_num) hi (yangBaxterRelation_mem hn hp hi)

/-- **Bokut–Shiao against Yang–Baxter.** -/
theorem bs_yb_resolves (hn : 0 < n) (hi : i'.val + 1 = i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i' i (bokutShiaoRelation i' i i') (yangBaxterRelation i' i)
        (bs_hlm i' i hi) (yb_hlm i' i hi)).spoly nf ∧ nf.isZero :=
  oc_reduces_to_zero hp i' i 1 (-1) hn _ _ (bs_hrel i' i hi) (yb_hrel i' i hi)
    (bs_hlm i' i hi) (yb_hlm i' i hi)
    (bokutShiaoRelation_lc hi (le_refl _)) (DegenerateYbBs.yangBaxter_lc hi)
    one_ne_zero (by norm_num) (by norm_num) hi
    (bokutShiaoRelation_mem hn hp hi (le_refl _))

/-- **Bokut–Shiao against Bokut–Shiao.** -/
theorem bs_bs_resolves (hn : 0 < n) (hi : i'.val + 1 = i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i' i (bokutShiaoRelation i' i i') (bokutShiaoRelation i' i i')
        (bs_hlm i' i hi) (bs_hlm i' i hi)).spoly nf ∧ nf.isZero :=
  oc_reduces_to_zero hp i' i 1 1 hn _ _ (bs_hrel i' i hi) (bs_hrel i' i hi)
    (bs_hlm i' i hi) (bs_hlm i' i hi)
    (bokutShiaoRelation_lc hi (le_refl _)) (bokutShiaoRelation_lc hi (le_refl _))
    one_ne_zero one_ne_zero (by norm_num) hi
    (bokutShiaoRelation_mem hn hp hi (le_refl _))

end BraidSelfOverlap

/-! ## §4s  Bokut–Shiao against far-commutation at the **same** index

§4o did `j₀ + 1 = j` — the far-commutation rule extending the descending run by
one step, which resolves in a single application. This is the neighbouring case
`j₀ = j`, where the two rules share their bottom index. It does not resolve in
one step: the shared index puts `σⱼσⱼ` at the end of both words, so the quadratic
rule fires twice before the Bokut–Shiao rules can.

Writing `jp` for `j + 1` and using `descWord_snoc` (§4o) —
`descWord i j = descWord i jp ++ [σⱼ]`, and hence
`bsWord₂ i' i j = bsWord₂ i' i jp ++ [σⱼ]` — the S-polynomial is

    (descWord i jp ++ [σⱼ, σⱼ, σᵢ])  −  (bsWord₂ i' i jp ++ [σⱼ, σⱼ])

and both terms end in `σⱼσⱼ`. Four steps:

| # | target | rule | context | coefficient |
|---|---|---|---|---|
| 1 | the first term | `Q_j` | `(descWord i jp ∣ σᵢ)` | `1` |
| 2 | the second | `Q_j` | `(bsWord₂ i' i jp ∣ ε)` | `−1` |
| 3 | `bsWord₁ i j` | Bokut–Shiao at `j` | `(ε ∣ ε)` | `h` |
| 4 | `bsWord₁ i jp` | Bokut–Shiao at `jp` | `(ε ∣ ε)` | `1` |

Steps 3 and 4 use the family's **own** rules at two adjacent depths — the `h`
term the two squares leave behind is the Bokut–Shiao relation at `j`, the
constant term is the one at `jp`. That is the same downward self-completion §4o
exhibited, arriving here through the quadratic rule rather than directly.

**Where the side condition comes from.** Step 4 needs `bokutShiaoRelation i' i jp`
to *be* a rule, that is `j + 1 ≤ i − 1` — which is exactly the condition for
`σᵢσⱼ` to be a far-commutation word in the first place, so nothing is left over.
At `j = i − 1` there is no composition to resolve: `σᵢσᵢ₋₁` is a braid word, not a
commuting pair, and that case is §4r's. At `n = 4` this family is **three**
compositions, `(i', i, j) ∈ {(1,2,0), (2,3,0), (2,3,1)}`.

Every word in the chain is `descWord i jp` prefixed or suffixed, and the single
fact that tells the two sides apart is the first letter — `σᵢ` on the `bsWord₁`
side (because `descWord i jp` begins with `σᵢ`), `σᵢ₋₁` on the `bsWord₂` side.
`head_ne` is that observation, and apart from one length count it is the only
word-distinctness the chain needs. -/

namespace BokutShiaoFarCommSame

variable {n : ℕ}

/-- The composition of `bokutShiaoRelation i' i j` with `farCommRelation i j`,
overlapping in the single letter `σᵢ` — the same shape as §4o, with the
far-commutation rule's bottom index moved up to `j`. -/
noncomputable def oc {i' i j : Fin n} (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := bokutShiaoRelation i' i j
  rule₂ := farCommRelation i j
  left := descWord i j
  overlap := [⟨i⟩]
  right := [⟨j⟩]
  lm₁_decomp := by rw [bokutShiaoRelation_lm hi hj]; rfl
  lm₂_decomp := by rw [farCommRelation_lm i j (by omega)]; rfl
  overlap_nonempty := by simp

/-- **The one word-distinctness fact the chain needs.** `descWord i jp` begins
with `σᵢ` (`descWord_cons`), and every `bsWord₂`-side word of the chain begins
with `σᵢ₋₁`; no length arithmetic and no knowledge of the tail is involved. -/
theorem head_ne {i' i jp : Fin n} (hi : i'.val + 1 = i.val) (hj : jp.val ≤ i'.val)
    (v w : Monomial (HeckeGen n)) :
    ((⟨i'⟩ : HeckeGen n) :: v) ≠ descWord i jp ++ w := by
  rw [descWord_cons hi hj, List.cons_append]
  intro hcon
  injection hcon with h1 _
  have := congrArg HeckeGen.rank h1
  simp only [HeckeGen.rank] at this
  omega

/-- `head_ne` the other way round; both directions occur, because the targeted
word is sometimes on the left of the comparison and sometimes on the right. -/
theorem head_ne' {i' i jp : Fin n} (hi : i'.val + 1 = i.val) (hj : jp.val ≤ i'.val)
    (v w : Monomial (HeckeGen n)) :
    descWord i jp ++ w ≠ (⟨i'⟩ : HeckeGen n) :: v :=
  fun hcon => head_ne hi hj v w hcon.symm

/-! ### The chain

`F₀ … F₃` are the stages, `F₀` the S-polynomial, and each step is its own
theorem — heartbeats are budgeted per declaration. -/

/-- Stage `0` — the S-polynomial. Both terms end in `σⱼσⱼ`. -/
noncomputable def F0 (_hp : HeckeParams) (i' i j jp : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(descWord i jp ++ [(⟨j⟩ : HeckeGen n), ⟨j⟩, ⟨i⟩], (1 : ℝ)),
     ((⟨i'⟩ : HeckeGen n) :: (descWord i jp ++ [(⟨j⟩ : HeckeGen n), ⟨j⟩]), -1)]

/-- Stage `1` — the square in the first term is out. -/
noncomputable def F1 (hp : HeckeParams) (i' i j jp : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(descWord i jp ++ [(⟨j⟩ : HeckeGen n), ⟨i⟩], hp.q - hp.q⁻¹),
     (descWord i jp ++ [(⟨i⟩ : HeckeGen n)], 1),
     ((⟨i'⟩ : HeckeGen n) :: (descWord i jp ++ [(⟨j⟩ : HeckeGen n), ⟨j⟩]), -1)]

/-- Stage `2` — both squares out. What is left is `h ·` the Bokut–Shiao relation
at `j`, plus the Bokut–Shiao relation at `jp`. -/
noncomputable def F2 (hp : HeckeParams) (i' i j jp : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(descWord i jp ++ [(⟨j⟩ : HeckeGen n), ⟨i⟩], hp.q - hp.q⁻¹),
     (descWord i jp ++ [(⟨i⟩ : HeckeGen n)], 1),
     ((⟨i'⟩ : HeckeGen n) :: (descWord i jp ++ [(⟨j⟩ : HeckeGen n)]), -(hp.q - hp.q⁻¹)),
     ((⟨i'⟩ : HeckeGen n) :: descWord i jp, -1)]

/-- Stage `3` — exactly the Bokut–Shiao relation at `jp`, which annihilates it. -/
noncomputable def F3 (_hp : HeckeParams) (i' i jp : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(descWord i jp ++ [(⟨i⟩ : HeckeGen n)], (1 : ℝ)),
     ((⟨i'⟩ : HeckeGen n) :: descWord i jp, -1)]

/-- **The S-polynomial.** The ambient word `descWord i j ++ [σᵢ, σⱼ]` is reached
from both sides and cancels identically; `descWord_snoc` then exhibits what
survives as `F₀`, with the square visible in both terms. -/
theorem oc_spoly_coeff (hp : HeckeParams) {i' i j jp : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) (hjp : j.val + 1 = jp.val)
    (hjpi : jp.val ≤ i'.val) (m : Monomial (HeckeGen n)) :
    (oc hi hj).spoly.coeff m = (F0 hp i' i j jp).coeff m := by
  have hDj : descWord i j = descWord i jp ++ [(⟨j⟩ : HeckeGen n)] :=
    descWord_snoc hjp (by omega : jp.val ≤ i.val)
  have hcyc : bsWord₂ i' i j = (⟨i'⟩ : HeckeGen n) :: descWord i j := by
    rw [bsWord₂, descWord_cons hi hj]
  show (farCommRelation i j).lc (heckeOrder n)
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i j).relation [⟨j⟩]).coeff m
    - (bokutShiaoRelation i' i j).lc (heckeOrder n)
      * (AlgElement.contextMul (descWord i j) (farCommRelation i j).relation []).coeff m
    = _
  rw [farCommRelation_lc i j (by omega), bokutShiaoRelation_lc hi hj, one_mul, one_mul]
  simp only [F0, bokutShiaoRelation, farCommRelation, bsWord₁, hcyc, hDj,
    AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
    List.append_nil, List.cons_append, List.append_assoc,
    AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 1 — the quadratic rule at `j`, in the context `(descWord i jp ∣ σᵢ)`. -/
theorem chainStep1 (hp : HeckeParams) (i' i j jp : Fin n) (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hjpi : jp.val ≤ i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F0 hp i' i j jp) (F1 hp i' i j jp) := by
  have hv : (F0 hp i' i j jp).coeff
      (descWord i jp ++ (heckeRelation j hp).lm (heckeOrder n) ++ [(⟨i⟩ : HeckeGen n)])
      = 1 := by
    rw [heckeRelation_lm,
      show (descWord i jp ++ [(⟨j⟩ : HeckeGen n), ⟨j⟩] ++ [(⟨i⟩ : HeckeGen n)])
        = descWord i jp ++ [(⟨j⟩ : HeckeGen n), ⟨j⟩, ⟨i⟩] by simp]
    simp [F0, AlgElement.ofTerms_coeff, head_ne hi hjpi]
  refine ⟨heckeRelation j hp, heckeRelation_mem hn hp j, descWord i jp,
    [(⟨i⟩ : HeckeGen n)], 1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (1 : ℝ) * (AlgElement.contextMul (descWord i jp)
      (heckeRelation j hp).relation [(⟨i⟩ : HeckeGen n)]).coeff m
    simp only [F0, F1, heckeRelation, AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, List.append_assoc,
      AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 2 — the quadratic rule at `j` again, now in the context
`(σᵢ₋₁ descWord i jp ∣ ε)`; that prefix *is* `bsWord₂ i' i jp`, by
`descWord_cons`. -/
theorem chainStep2 (hp : HeckeParams) (i' i j jp : Fin n) (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hjpi : jp.val ≤ i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F1 hp i' i j jp) (F2 hp i' i j jp) := by
  have hv : (F1 hp i' i j jp).coeff
      ((⟨i'⟩ : HeckeGen n) :: descWord i jp ++ (heckeRelation j hp).lm (heckeOrder n) ++ [])
      = -1 := by
    rw [heckeRelation_lm,
      show ((⟨i'⟩ : HeckeGen n) :: descWord i jp ++ [(⟨j⟩ : HeckeGen n), ⟨j⟩] ++ [])
        = (⟨i'⟩ : HeckeGen n) :: (descWord i jp ++ [(⟨j⟩ : HeckeGen n), ⟨j⟩]) by simp]
    simp [F1, AlgElement.ofTerms_coeff, head_ne' hi hjpi]
  refine ⟨heckeRelation j hp, heckeRelation_mem hn hp j,
    (⟨i'⟩ : HeckeGen n) :: descWord i jp, [], -1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (-1 : ℝ) * (AlgElement.contextMul ((⟨i'⟩ : HeckeGen n) :: descWord i jp)
      (heckeRelation j hp).relation []).coeff m
    simp only [F1, F2, heckeRelation, AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.append_nil,
      List.cons_append,
      AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 3 — the family's own rule at depth `j`, in empty context, clearing the
`h` term the two squares left. -/
theorem chainStep3 (hp : HeckeParams) (i' i j jp : Fin n) (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) (hjp : j.val + 1 = jp.val)
    (hjpi : jp.val ≤ i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F2 hp i' i j jp) (F3 hp i' i jp) := by
  have hh := hp.h_ne_zero
  have hDj : descWord i j = descWord i jp ++ [(⟨j⟩ : HeckeGen n)] :=
    descWord_snoc hjp (by omega : jp.val ≤ i.val)
  have hcyc : bsWord₂ i' i j = (⟨i'⟩ : HeckeGen n) :: descWord i j := by
    rw [bsWord₂, descWord_cons hi hj]
  have hlen : descWord i jp ++ [(⟨i⟩ : HeckeGen n)]
      ≠ descWord i jp ++ [(⟨j⟩ : HeckeGen n), ⟨i⟩] := by
    intro hcon
    have := congrArg List.length hcon
    simp only [List.length_append, List.length_cons, List.length_nil] at this
    omega
  have hw : ([] : Monomial (HeckeGen n))
      ++ (bokutShiaoRelation i' i j).lm (heckeOrder n) ++ []
      = descWord i jp ++ [(⟨j⟩ : HeckeGen n), ⟨i⟩] := by
    rw [bokutShiaoRelation_lm hi hj]
    simp only [bsWord₁, hDj]
    simp
  have hv : (F2 hp i' i j jp).coeff
      (([] : Monomial (HeckeGen n)) ++ (bokutShiaoRelation i' i j).lm (heckeOrder n) ++ [])
      = hp.q - hp.q⁻¹ := by
    rw [hw]
    simp [F2, AlgElement.ofTerms_coeff, head_ne hi hjpi, hlen]
  refine ⟨bokutShiaoRelation i' i j, bokutShiaoRelation_mem hn hp hi hj, [], [],
    hp.q - hp.q⁻¹, ?_, ?_, ?_⟩
  · rw [hv]; exact hh
  · rw [hv, bokutShiaoRelation_lc hi hj]; ring
  · intro m
    show _ = _ - (hp.q - hp.q⁻¹)
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i j).relation []).coeff m
    simp only [F2, F3, bokutShiaoRelation, bsWord₁, hcyc, hDj,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil,
      List.nil_append, List.append_nil, List.cons_append, List.append_assoc,
      AlgElement.ofTerms_coeff, List.filter_cons,
      List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 4 — the family's own rule at depth `jp`, in empty context. `F₃` *is*
that relation, so the step lands on zero. -/
theorem chainStep4 (hp : HeckeParams) (i' i jp : Fin n) (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hjpi : jp.val ≤ i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (F3 hp i' i jp) AlgElement.zero := by
  have hcyc : bsWord₂ i' i jp = (⟨i'⟩ : HeckeGen n) :: descWord i jp := by
    rw [bsWord₂, descWord_cons hi hjpi]
  have hw : ([] : Monomial (HeckeGen n))
      ++ (bokutShiaoRelation i' i jp).lm (heckeOrder n) ++ []
      = descWord i jp ++ [(⟨i⟩ : HeckeGen n)] := by
    rw [bokutShiaoRelation_lm hi hjpi]
    simp only [bsWord₁]
    simp
  have hv : (F3 hp i' i jp).coeff
      (([] : Monomial (HeckeGen n)) ++ (bokutShiaoRelation i' i jp).lm (heckeOrder n) ++ [])
      = 1 := by
    rw [hw]
    simp [F3, AlgElement.ofTerms_coeff, head_ne hi hjpi]
  refine ⟨bokutShiaoRelation i' i jp, bokutShiaoRelation_mem hn hp hi hjpi, [], [], 1,
    ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, bokutShiaoRelation_lc hi hjpi]; ring
  · intro m
    show _ = _ - (1 : ℝ)
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i jp).relation []).coeff m
    simp only [F3, bokutShiaoRelation, bsWord₁, hcyc, AlgElement.zero,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil,
      List.nil_append, List.append_nil,
      AlgElement.ofTerms_coeff, List.filter_cons,
      List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Four steps, to zero.** `reducesToZero_congr` (§6) joins the chain, which
runs on `F₀`, to the S-polynomial, which `oc_spoly_coeff` says is `F₀`
coefficientwise. -/
theorem oc_reduces_to_zero (hp : HeckeParams) {i' i j jp : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) (hjp : j.val + 1 = jp.val)
    (hjpi : jp.val ≤ i'.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hi hj).spoly nf ∧ nf.isZero := by
  refine reducesToZero_congr ⟨AlgElement.zero,
    ⟨(MultiStepReduction.refl _)
      |>.step (chainStep1 hp i' i j jp hn hi hjpi)
      |>.step (chainStep2 hp i' i j jp hn hi hjpi)
      |>.step (chainStep3 hp i' i j jp hn hi hj hjp hjpi)
      |>.step (chainStep4 hp i' i jp hn hi hjpi),
      isNormalForm_of_isZero AlgElement.isZero_zero⟩, AlgElement.isZero_zero⟩ ?_
  intro m
  exact oc_spoly_coeff hp hi hj hjp hjpi m

/-- **The family, in the form the enumeration meets it.** The hypothesis is the
far-commutation side condition `j + 1 < i` and nothing else: it is what makes
`σᵢσⱼ` a rule of the system, and simultaneously what makes `jp = j + 1` a legal
Bokut–Shiao depth for step 4. -/
theorem resolves (hp : HeckeParams) {i' i j : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) (hfar : j.val + 1 < i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc hi hj).spoly nf ∧ nf.isZero := by
  have hlt : j.val + 1 < n := Nat.lt_trans hfar i.isLt
  exact oc_reduces_to_zero hp hn hi hj (jp := ⟨j.val + 1, hlt⟩) rfl
    (show j.val + 1 ≤ i'.val by omega)

end BokutShiaoFarCommSame

/-! ## §4t  The quadratic rule against a **general** Bokut–Shiao rule

§4q covers the quadratic rule on the left against far-commutation, Yang–Baxter,
and Bokut–Shiao at `j = i − 1` — everything whose second word has the cyclic
shape `u'' ++ [σ_z]`. It says explicitly why the general Bokut–Shiao rule is not
among them: `bsWord₂ i' i j = σᵢ₋₁ :: descWord i j` puts the extra letter on the
**left**, so for `j < i − 1` no `σ_z` closes the cycle. This section is those
missing instances — three of the ninety-two at `n = 4`, and the first family in
this arc whose chain length is not constant.

**The shape.** With `v` for `descWord i−2 j`, so that
`descWord i' j = σᵢ₋₁ :: v`, the two words of the rule are

    bsWord₁ i j = σᵢ σᵢ₋₁ v σᵢ        bsWord₂ i' i j = σᵢ₋₁ σᵢ σᵢ₋₁ v

and the composition is `Q_i` against it over `σᵢ σᵢ σᵢ₋₁ v σᵢ`. The S-polynomial
is three terms,

    spoly = σᵢ σᵢ₋₁ σᵢ σᵢ₋₁ v  −  h · bsWord₁ i j  −  σᵢ₋₁ v σᵢ

**The chain is `3 + |v|` steps**, and only the first three are fixed:

| # | target | rule | context | coefficient |
|---|---|---|---|---|
| 1 | `σᵢσᵢ₋₁σᵢσᵢ₋₁v` | Yang–Baxter | `(ε ∣ σᵢ₋₁ v)` | `−1` |
| 2 | `σᵢ₋₁σᵢσᵢ₋₁σᵢ₋₁v` | `Q_{i−1}` | `(σᵢ₋₁σᵢ ∣ v)` | `1` |
| 3 | `bsWord₁ i j` | Bokut–Shiao at `j` | `(ε ∣ ε)` | `−h` |
| 4… | — | far-commutation | — | `1` |

Step 1 straightens the braid, step 2 squares out the `σᵢ₋₁σᵢ₋₁` that leaves, and
step 3 spends the `h` term against the rule's own relation. What remains is

    σᵢ₋₁ σᵢ v  −  σᵢ₋₁ v σᵢ

— one letter `σᵢ` on the wrong side of `v`, and every letter of `v` has index at
most `i − 2`, so each is a *far-commutation* letter for `σᵢ`. The rest of the
chain walks `σᵢ` across `v` one letter at a time and the two terms cancel. That
is `|v| = i − 1 − j` steps, giving `3 + (i−1−j)` in total — the `4, 4, 5` the
`n = 4` confluence engine reports for `Q2 × B120`, `Q3 × B231`, `Q3 × B230`.

**`farComm_transport` is the induction**, and it is stated for an arbitrary word
and an arbitrary left context rather than for `descWord`: transporting a
generator across a block of generators it commutes with is not special to this
composition, and the remaining `B × B` families will want it too. -/

/-- Every letter of `descWord i j` has index at most `i`. The bound the transport
needs: it is what makes each letter of `v` a far-commutation partner of `σᵢ`. -/
theorem descWord_index_le {n : ℕ} {i j : Fin n} {y : HeckeGen n}
    (hy : y ∈ descWord i j) : y.index.val ≤ i.val := by
  simp only [descWord, List.mem_map, List.mem_reverse, List.mem_filter,
    List.mem_finRange, true_and, decide_eq_true_eq] at hy
  obtain ⟨k, hk, hky⟩ := hy
  rw [← hky]
  exact hk.2

/-- **Far-commutation transport.** If every letter of `w` commutes far with `σₓ`,
then `c · (a σₓ w) − c · (a w σₓ)` reduces, in `|w|` steps, to an element that is
coefficientwise zero — one far-commutation application per letter, each in the
context accumulated so far.

Stated for an arbitrary `w` and an arbitrary left context `a`, because the
induction has to move `a` anyway: the letter just passed becomes part of the
context for the next step. -/
theorem farComm_transport {n : ℕ} (hn : 0 < n) (hp : HeckeParams) (x : Fin n)
    (c : ℝ) (hc : c ≠ 0) :
    ∀ (w a : Monomial (HeckeGen n)), (∀ y ∈ w, y.index.val + 1 < x.val) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms
          [(a ++ ((⟨x⟩ : HeckeGen n) :: w), c),
           (a ++ (w ++ [(⟨x⟩ : HeckeGen n)]), -c)])
        (AlgElement.ofTerms
          [(a ++ (w ++ [(⟨x⟩ : HeckeGen n)]), c),
           (a ++ (w ++ [(⟨x⟩ : HeckeGen n)]), -c)]) := by
  intro w
  induction w with
  | nil => intro a _; exact MultiStepReduction.refl _
  | cons y w ih =>
    intro a hw
    obtain ⟨yi⟩ := y
    have hy : yi.val + 1 < x.val := hw _ (by simp)
    have hyx : (⟨yi⟩ : HeckeGen n) ≠ ⟨x⟩ := by
      intro hcon
      have := congrArg HeckeGen.rank hcon
      simp only [HeckeGen.rank] at this
      omega
    have key := ih (a ++ [(⟨yi⟩ : HeckeGen n)]) (fun z hz => hw z (by simp [hz]))
    simp only [List.append_assoc, List.singleton_append] at key
    show MultiStepReduction _ _ (AlgElement.ofTerms
      [(a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w), c),
       (a ++ ((⟨yi⟩ : HeckeGen n) :: (w ++ [(⟨x⟩ : HeckeGen n)])), -c)]) _
    refine MultiStepReduction.head ?_ key
    have hne : a ++ ((⟨yi⟩ : HeckeGen n) :: (w ++ [(⟨x⟩ : HeckeGen n)]))
        ≠ a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w) := by
      intro hcon
      have h2 : ((⟨yi⟩ : HeckeGen n) :: (w ++ [(⟨x⟩ : HeckeGen n)]))
          = ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w) := by simpa using hcon
      injection h2 with h3 _
      exact hyx h3
    have hv : (AlgElement.ofTerms
        [(a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w), c),
         (a ++ ((⟨yi⟩ : HeckeGen n) :: (w ++ [(⟨x⟩ : HeckeGen n)])), -c)]).coeff
        (a ++ (farCommRelation x yi).lm (heckeOrder n) ++ w) = c := by
      rw [farCommRelation_lm x yi (by omega),
        show (a ++ [(⟨x⟩ : HeckeGen n), (⟨yi⟩ : HeckeGen n)] ++ w)
          = a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w) by simp]
      simp [AlgElement.ofTerms_coeff, hne]
    refine ⟨farCommRelation x yi, farCommRelation_mem hn hp hy, a, w, c, ?_, ?_, ?_⟩
    · rw [hv]; exact hc
    · rw [hv, farCommRelation_lc x yi (by omega)]; ring
    · intro m
      show _ = _ - c * (AlgElement.contextMul a (farCommRelation x yi).relation w).coeff m
      simp only [farCommRelation, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
        List.map_nil, List.cons_append, List.nil_append, List.append_assoc,
        AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
      split_ifs <;>
        simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

namespace QuadBokutShiao

variable {n : ℕ}

/-- The rule's leading monomial, in the form §4q's `oc` wants: it begins with
`σᵢ`, and the tail is `σᵢ₋₁ v σᵢ`. -/
theorem bs_lm {i' i j : Fin n} (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val)
    {v : Monomial (HeckeGen n)} (hv : descWord i' j = (⟨i'⟩ : HeckeGen n) :: v) :
    (bokutShiaoRelation i' i j).lm (heckeOrder n)
      = (⟨i⟩ : HeckeGen n) :: ((⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)])) := by
  rw [bokutShiaoRelation_lm hi hj, bsWord₁, descWord_cons hi hj, hv]
  rfl

/-- Stage `0` — the S-polynomial. The ambient word `σᵢσᵢσᵢ₋₁vσᵢ` cancels. -/
noncomputable def G0 (hp : HeckeParams) (i' i : Fin n) (v : Monomial (HeckeGen n)) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n)
        :: (⟨i'⟩ : HeckeGen n) :: v, (1 : ℝ)),
     ((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]),
        -(hp.q - hp.q⁻¹)),
     ((⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]), -1)]

/-- Stage `1` — the braid is straightened. -/
noncomputable def G1 (hp : HeckeParams) (i' i : Fin n) (v : Monomial (HeckeGen n)) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [((⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n)
        :: (⟨i'⟩ : HeckeGen n) :: v, (1 : ℝ)),
     ((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]),
        -(hp.q - hp.q⁻¹)),
     ((⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]), -1)]

/-- Stage `2` — the square is out; the `h` term it leaves is `bsWord₂`. -/
noncomputable def G2 (hp : HeckeParams) (i' i : Fin n) (v : Monomial (HeckeGen n)) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [((⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: v,
        hp.q - hp.q⁻¹),
     ((⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: v, 1),
     ((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]),
        -(hp.q - hp.q⁻¹)),
     ((⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]), -1)]

/-- Stage `3` — one generator on the wrong side of `v`, and nothing else. This is
exactly `farComm_transport`'s starting shape with `a = [σᵢ₋₁]`. -/
noncomputable def G3 (_hp : HeckeParams) (i' i : Fin n) (v : Monomial (HeckeGen n)) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [([(⟨i'⟩ : HeckeGen n)] ++ ((⟨i⟩ : HeckeGen n) :: v), (1 : ℝ)),
     ([(⟨i'⟩ : HeckeGen n)] ++ (v ++ [(⟨i⟩ : HeckeGen n)]), -1)]

/-- Stage `4` — what the transport lands on: two equal words with opposite
coefficients, coefficientwise zero. -/
noncomputable def G4 (_hp : HeckeParams) (i' i : Fin n) (v : Monomial (HeckeGen n)) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [([(⟨i'⟩ : HeckeGen n)] ++ (v ++ [(⟨i⟩ : HeckeGen n)]), (1 : ℝ)),
     ([(⟨i'⟩ : HeckeGen n)] ++ (v ++ [(⟨i⟩ : HeckeGen n)]), -1)]

theorem G4_isZero (hp : HeckeParams) (i' i : Fin n) (v : Monomial (HeckeGen n)) :
    (G4 hp i' i v).isZero := by
  intro m
  simp only [G4, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
  ring

/-- **The S-polynomial.** `Q_i`'s leading term and the rule's leading term are
both the ambient word `σᵢσᵢσᵢ₋₁vσᵢ`, so they cancel without any word-distinctness
argument; three terms survive. -/
theorem oc_spoly_coeff (hp : HeckeParams) {i' i j : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) {v : Monomial (HeckeGen n)}
    (hv : descWord i' j = (⟨i'⟩ : HeckeGen n) :: v) (m : Monomial (HeckeGen n)) :
    (CyclicQuadLeft.oc hp (bokutShiaoRelation i' i j)
      ((⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)])) i
      (bs_lm hi hj hv)).spoly.coeff m
      = (G0 hp i' i v).coeff m := by
  have hb₁ : bsWord₁ i j
      = (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]) := by
    rw [bsWord₁, descWord_cons hi hj, hv]; rfl
  have hb₂ : bsWord₂ i' i j
      = (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: v := by
    rw [bsWord₂, hv]
  show (bokutShiaoRelation i' i j).lc (heckeOrder n)
      * (AlgElement.contextMul [] (heckeRelation i hp).relation
          ((⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]))).coeff m
    - (heckeRelation i hp).lc (heckeOrder n)
      * (AlgElement.contextMul [(⟨i⟩ : HeckeGen n)]
          (bokutShiaoRelation i' i j).relation []).coeff m
    = _
  rw [heckeRelation_lc, bokutShiaoRelation_lc hi hj, one_mul, one_mul]
  simp only [G0, heckeRelation, bokutShiaoRelation, hb₁, hb₂,
    AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
    List.append_nil, List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons,
    List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 1 — Yang–Baxter, in the context `(ε ∣ σᵢ₋₁ v)`. Its leading coefficient
is `−1`, so the step coefficient is `−1` too. -/
theorem chainStep1 (hp : HeckeParams) (i' i : Fin n) (v : Monomial (HeckeGen n))
    (hn : 0 < n) (hi : i'.val + 1 = i.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (G0 hp i' i v) (G1 hp i' i v) := by
  have hv : (G0 hp i' i v).coeff
      ([] ++ (yangBaxterRelation i' i).lm (heckeOrder n)
        ++ ((⟨i'⟩ : HeckeGen n) :: v)) = 1 := by
    rw [yangBaxterRelation_lm i' i (by omega),
      show (([] : Monomial (HeckeGen n)) ++ [(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩]
          ++ ((⟨i'⟩ : HeckeGen n) :: v))
        = (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n)
            :: (⟨i'⟩ : HeckeGen n) :: v by simp]
    have h₂ : ((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]))
        ≠ (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n)
            :: (⟨i'⟩ : HeckeGen n) :: v := by
      intro hcon
      have := congrArg List.length hcon
      simp only [List.length_cons, List.length_append, List.length_nil] at this
      omega
    have h₃ : ((⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]))
        ≠ (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n)
            :: (⟨i'⟩ : HeckeGen n) :: v := by
      intro hcon
      have := congrArg List.length hcon
      simp only [List.length_cons, List.length_append, List.length_nil] at this
      omega
    simp [G0, AlgElement.ofTerms_coeff, h₂, h₃]
  refine ⟨yangBaxterRelation i' i, yangBaxterRelation_mem hn hp hi, [],
    (⟨i'⟩ : HeckeGen n) :: v, -1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, DegenerateYbBs.yangBaxter_lc hi]; ring
  · intro m
    show _ = _ - (-1 : ℝ) * (AlgElement.contextMul [] (yangBaxterRelation i' i).relation
      ((⟨i'⟩ : HeckeGen n) :: v)).coeff m
    simp only [G0, G1, yangBaxterRelation, AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append, List.cons_append,
      AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 2 — the quadratic rule at `i − 1`, on the `σᵢ₋₁σᵢ₋₁` the braid step
left, in the context `(σᵢ₋₁σᵢ ∣ v)`. -/
theorem chainStep2 (hp : HeckeParams) (i' i : Fin n) (v : Monomial (HeckeGen n))
    (hn : 0 < n) (_hi : i'.val + 1 = i.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (G1 hp i' i v) (G2 hp i' i v) := by
  have hv : (G1 hp i' i v).coeff
      ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
        ++ (heckeRelation i' hp).lm (heckeOrder n) ++ v) = 1 := by
    rw [heckeRelation_lm,
      show ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
          ++ [(⟨i'⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] ++ v)
        = (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n)
            :: (⟨i'⟩ : HeckeGen n) :: v by simp]
    have h₂ : ((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]))
        ≠ (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n)
            :: (⟨i'⟩ : HeckeGen n) :: v := by
      intro hcon
      have := congrArg List.length hcon
      simp only [List.length_cons, List.length_append, List.length_nil] at this
      omega
    have h₃ : ((⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]))
        ≠ (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n)
            :: (⟨i'⟩ : HeckeGen n) :: v := by
      intro hcon
      have := congrArg List.length hcon
      simp only [List.length_cons, List.length_append, List.length_nil] at this
      omega
    simp [G1, AlgElement.ofTerms_coeff, h₂, h₃]
  refine ⟨heckeRelation i' hp, heckeRelation_mem hn hp i',
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)], v, 1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (1 : ℝ) * (AlgElement.contextMul
      [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] (heckeRelation i' hp).relation v).coeff m
    simp only [G1, G2, heckeRelation, AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append, List.cons_append,
      AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 3 — the rule's own relation in empty context, spending the `h` term.
The only distinctness here that is not a length count: `bsWord₁` and `bsWord₂`
have the same length and are separated by their first letter. -/
theorem chainStep3 (hp : HeckeParams) {i' i j : Fin n} (v : Monomial (HeckeGen n))
    (hn : 0 < n) (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val)
    (hvd : descWord i' j = (⟨i'⟩ : HeckeGen n) :: v) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (G2 hp i' i v) (G3 hp i' i v) := by
  have hh := hp.h_ne_zero
  have hii' : (⟨i⟩ : HeckeGen n) ≠ ⟨i'⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  have hb₁ : bsWord₁ i j
      = (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]) := by
    rw [bsWord₁, descWord_cons hi hj, hvd]; rfl
  have hb₂ : bsWord₂ i' i j
      = (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: v := by
    rw [bsWord₂, hvd]
  have hw : ([] : Monomial (HeckeGen n))
      ++ (bokutShiaoRelation i' i j).lm (heckeOrder n) ++ []
      = (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]) := by
    rw [bokutShiaoRelation_lm hi hj, hb₁]; simp
  have hv : (G2 hp i' i v).coeff
      (([] : Monomial (HeckeGen n)) ++ (bokutShiaoRelation i' i j).lm (heckeOrder n) ++ [])
      = -(hp.q - hp.q⁻¹) := by
    rw [hw]
    have h₁ : ((⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: v)
        ≠ (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]) := by
      intro hcon
      injection hcon with h _
      exact hii' h.symm
    have h₂ : ((⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: v)
        ≠ (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]) := by
      intro hcon
      have := congrArg List.length hcon
      simp only [List.length_cons, List.length_append, List.length_nil] at this
      omega
    have h₄ : ((⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]))
        ≠ (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)]) := by
      intro hcon
      have := congrArg List.length hcon
      simp only [List.length_cons, List.length_append, List.length_nil] at this
      omega
    simp [G2, AlgElement.ofTerms_coeff, h₁, h₂, h₄]
  refine ⟨bokutShiaoRelation i' i j, bokutShiaoRelation_mem hn hp hi hj, [], [],
    -(hp.q - hp.q⁻¹), ?_, ?_, ?_⟩
  · rw [hv]; exact neg_ne_zero.mpr hh
  · rw [hv, bokutShiaoRelation_lc hi hj]; ring
  · intro m
    show _ = _ - (-(hp.q - hp.q⁻¹))
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i j).relation []).coeff m
    simp only [G2, G3, bokutShiaoRelation, hb₁, hb₂,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil,
      List.nil_append, List.append_nil, List.cons_append,
      AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Three fixed steps, then `|v|` far-commutation steps, to zero.** -/
theorem oc_reduces_to_zero (hp : HeckeParams) {i' i j : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) {v : Monomial (HeckeGen n)}
    (hvd : descWord i' j = (⟨i'⟩ : HeckeGen n) :: v)
    (hvfar : ∀ y ∈ v, y.index.val + 1 < i.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (CyclicQuadLeft.oc hp (bokutShiaoRelation i' i j)
        ((⟨i'⟩ : HeckeGen n) :: (v ++ [(⟨i⟩ : HeckeGen n)])) i
        (bs_lm hi hj hvd)).spoly nf ∧ nf.isZero := by
  refine reducesToZero_congr ⟨G4 hp i' i v,
    ⟨((MultiStepReduction.refl (G0 hp i' i v))
      |>.step (chainStep1 hp i' i v hn hi)
      |>.step (chainStep2 hp i' i v hn hi)
      |>.step (chainStep3 hp v hn hi hj hvd)).trans
        (farComm_transport hn hp i 1 one_ne_zero v [(⟨i'⟩ : HeckeGen n)] hvfar),
      isNormalForm_of_isZero (G4_isZero hp i' i v)⟩, G4_isZero hp i' i v⟩ ?_
  intro m
  exact oc_spoly_coeff hp hi hj hvd m

/-- **The family, in the form the enumeration meets it.** `v` is `descWord i−2 j`,
which exists exactly when `j < i − 1` — the condition §4q's cyclic hypothesis
fails under, so this covers precisely what §4q leaves open. -/
theorem resolves (hp : HeckeParams) {i'' i' i j : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) (hj : j.val ≤ i''.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (CyclicQuadLeft.oc hp (bokutShiaoRelation i' i j)
        ((⟨i'⟩ : HeckeGen n) :: (descWord i'' j ++ [(⟨i⟩ : HeckeGen n)])) i
        (bs_lm hi (by omega) (descWord_cons hi'' hj))).spoly nf ∧ nf.isZero :=
  oc_reduces_to_zero hp hn hi (by omega) (descWord_cons hi'' hj)
    (fun _ hy => by have := descWord_index_le hy; omega)

end QuadBokutShiao

/-! ## §4u  Far-commutation on the **left**, against Bokut–Shiao or Yang–Baxter

§4o, §4s and §4t all have the far-commutation rule on the right of the
composition. This is the other side: `farCommRelation x m` leads on `σₓσ_m`, a
Bokut–Shiao or Yang–Baxter rule leads on a word *beginning* with `σ_m`, and the
two overlap in that single letter.

**The shape.** Write the second rule as `c · (σ_m :: u'') − c · w₂` — leading
monomial `σ_m :: u''`, other word `w₂`, monic up to `c`. Both Bokut–Shiao and
Yang–Baxter are of this form, and at `j = i − 1` both rules sit on the same
leading monomial (§4j), which is why this section proves two instances rather
than one. The ambient word `σₓ σ_m u''` cancels and

    spoly = c · (σₓ :: w₂)  −  c · (σ_m :: σₓ :: u'')

**Why it resolves, and why it is a transport.** `σₓ` commutes far with *every*
letter of the second rule, because `m + 1 < x` is the far-commutation side
condition and every letter of `w₂` and of `u''` has index at most `m`. So `σₓ` is
a passenger in both terms, and the chain simply walks it to the right end of
each:

| phase | term | steps |
|---|---|---|
| 1 | `σₓ :: w₂` → `w₂ ++ [σₓ]` | `\|w₂\|` |
| 2 | `σ_m :: σₓ :: u''` → `σ_m :: (u'' ++ [σₓ])` | `\|u''\|` |
| 3 | the rule itself, in the context `(ε ∣ σₓ)` | `1` |

After phase 2 the second term is `(σ_m :: u'') ++ [σₓ]` — the rule's leading
monomial with `σₓ` appended — so one application of the rule in the context
`(ε ∣ σₓ)` turns it into `w₂ ++ [σₓ]` and the two terms cancel. Total
`|w₂| + |u''| + 1`, which is `6` for both `n = 4` instances.

**Why the transport needs a passenger.** `farComm_transport` (§4t) moves a
generator across a word in an element whose *other* term is the transport's own
destination, so the two cancel at the end. Here the other term is a bystander: it
has to be carried along untouched, and the step's "targeted coefficient is
non-zero" condition needs it distinguished from every intermediate word. Hence
`farComm_transport_snd` and `farComm_transport_fst` — the same induction with the
bystander in the second and the first list slot. Both slots are genuinely needed:
each phase transports a different term, so whichever slot phase 1 leaves the
moving term in, phase 2 needs the other one. -/

/-- **Transport with a bystander, moving term first.** The collision hypothesis
is stated over every splitting `u ++ v = w`, because that enumerates exactly the
intermediate words the run passes through: `σₓ` sits after `u` and before `v`. -/
theorem farComm_transport_snd {n : ℕ} (hn : 0 < n) (hp : HeckeParams) (x : Fin n)
    (c d : ℝ) (hc : c ≠ 0) (p : Monomial (HeckeGen n)) :
    ∀ (w a : Monomial (HeckeGen n)), (∀ y ∈ w, y.index.val + 1 < x.val) →
      (∀ u v : Monomial (HeckeGen n), u ++ v = w →
          p ≠ a ++ (u ++ ((⟨x⟩ : HeckeGen n) :: v))) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms [(a ++ ((⟨x⟩ : HeckeGen n) :: w), c), (p, d)])
        (AlgElement.ofTerms [(a ++ (w ++ [(⟨x⟩ : HeckeGen n)]), c), (p, d)]) := by
  intro w
  induction w with
  | nil => intro a _ _; exact MultiStepReduction.refl _
  | cons y w ih =>
    intro a hw hpw
    obtain ⟨yi⟩ := y
    have hy : yi.val + 1 < x.val := hw _ (by simp)
    have hyx : (⟨yi⟩ : HeckeGen n) ≠ ⟨x⟩ := by
      intro hcon
      have := congrArg HeckeGen.rank hcon
      simp only [HeckeGen.rank] at this
      omega
    have key := ih (a ++ [(⟨yi⟩ : HeckeGen n)]) (fun z hz => hw z (by simp [hz]))
      (fun u v huv => by
        have := hpw ((⟨yi⟩ : HeckeGen n) :: u) v (by rw [List.cons_append, huv])
        simpa only [List.append_assoc, List.singleton_append, List.cons_append] using this)
    simp only [List.append_assoc, List.singleton_append] at key
    show MultiStepReduction _ _ (AlgElement.ofTerms
      [(a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w), c), (p, d)]) _
    refine MultiStepReduction.head ?_ key
    have hne : p ≠ a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w) :=
      hpw [] ((⟨yi⟩ : HeckeGen n) :: w) rfl
    have hv : (AlgElement.ofTerms
        [(a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w), c), (p, d)]).coeff
        (a ++ (farCommRelation x yi).lm (heckeOrder n) ++ w) = c := by
      rw [farCommRelation_lm x yi (by omega),
        show (a ++ [(⟨x⟩ : HeckeGen n), (⟨yi⟩ : HeckeGen n)] ++ w)
          = a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w) by simp]
      simp [AlgElement.ofTerms_coeff, hne]
    refine ⟨farCommRelation x yi, farCommRelation_mem hn hp hy, a, w, c, ?_, ?_, ?_⟩
    · rw [hv]; exact hc
    · rw [hv, farCommRelation_lc x yi (by omega)]; ring
    · intro m
      show _ = _ - c * (AlgElement.contextMul a (farCommRelation x yi).relation w).coeff m
      simp only [farCommRelation, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
        List.map_nil, List.cons_append, List.nil_append, List.append_assoc,
        AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
      split_ifs <;>
        simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Transport with a bystander, moving term second.** The mirror of
`farComm_transport_snd` in the list slot, not in the direction of travel. -/
theorem farComm_transport_fst {n : ℕ} (hn : 0 < n) (hp : HeckeParams) (x : Fin n)
    (c d : ℝ) (hc : c ≠ 0) (p : Monomial (HeckeGen n)) :
    ∀ (w a : Monomial (HeckeGen n)), (∀ y ∈ w, y.index.val + 1 < x.val) →
      (∀ u v : Monomial (HeckeGen n), u ++ v = w →
          p ≠ a ++ (u ++ ((⟨x⟩ : HeckeGen n) :: v))) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms [(p, d), (a ++ ((⟨x⟩ : HeckeGen n) :: w), c)])
        (AlgElement.ofTerms [(p, d), (a ++ (w ++ [(⟨x⟩ : HeckeGen n)]), c)]) := by
  intro w
  induction w with
  | nil => intro a _ _; exact MultiStepReduction.refl _
  | cons y w ih =>
    intro a hw hpw
    obtain ⟨yi⟩ := y
    have hy : yi.val + 1 < x.val := hw _ (by simp)
    have hyx : (⟨yi⟩ : HeckeGen n) ≠ ⟨x⟩ := by
      intro hcon
      have := congrArg HeckeGen.rank hcon
      simp only [HeckeGen.rank] at this
      omega
    have key := ih (a ++ [(⟨yi⟩ : HeckeGen n)]) (fun z hz => hw z (by simp [hz]))
      (fun u v huv => by
        have := hpw ((⟨yi⟩ : HeckeGen n) :: u) v (by rw [List.cons_append, huv])
        simpa only [List.append_assoc, List.singleton_append, List.cons_append] using this)
    simp only [List.append_assoc, List.singleton_append] at key
    show MultiStepReduction _ _ (AlgElement.ofTerms
      [(p, d), (a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w), c)]) _
    refine MultiStepReduction.head ?_ key
    have hne : p ≠ a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w) :=
      hpw [] ((⟨yi⟩ : HeckeGen n) :: w) rfl
    have hv : (AlgElement.ofTerms
        [(p, d), (a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w), c)]).coeff
        (a ++ (farCommRelation x yi).lm (heckeOrder n) ++ w) = c := by
      rw [farCommRelation_lm x yi (by omega),
        show (a ++ [(⟨x⟩ : HeckeGen n), (⟨yi⟩ : HeckeGen n)] ++ w)
          = a ++ ((⟨x⟩ : HeckeGen n) :: (⟨yi⟩ : HeckeGen n) :: w) by simp]
      simp [AlgElement.ofTerms_coeff, hne]
    refine ⟨farCommRelation x yi, farCommRelation_mem hn hp hy, a, w, c, ?_, ?_, ?_⟩
    · rw [hv]; exact hc
    · rw [hv, farCommRelation_lc x yi (by omega)]; ring
    · intro m
      show _ = _ - c * (AlgElement.contextMul a (farCommRelation x yi).relation w).coeff m
      simp only [farCommRelation, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
        List.map_nil, List.cons_append, List.nil_append, List.append_assoc,
        AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
      split_ifs <;>
        simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

namespace FarCommCyclic

variable {n : ℕ}

/-- The composition of `farCommRelation x m` with a rule whose leading monomial
begins with `σ_m`, overlapping in that letter. -/
noncomputable def oc (r : ReductionRule (HeckeGen n) ℝ) (x m : Fin n)
    (u'' : Monomial (HeckeGen n))
    (hlm : r.lm (heckeOrder n) = (⟨m⟩ : HeckeGen n) :: u'')
    (hmx : m.val + 1 < x.val) : OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := farCommRelation x m
  rule₂ := r
  left := [⟨x⟩]
  overlap := [⟨m⟩]
  right := u''
  lm₁_decomp := by rw [farCommRelation_lm x m (by omega)]; rfl
  lm₂_decomp := hlm
  overlap_nonempty := by simp

/-- Stage `0` — the S-polynomial, two terms; the ambient word `σₓ σ_m u''` is
reached from both sides and cancels. -/
noncomputable def E0 (x m : Fin n) (q : HeckeGen n)
    (t u'' : Monomial (HeckeGen n)) (c : ℝ) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [((⟨x⟩ : HeckeGen n) :: (q :: t), c),
     ((⟨m⟩ : HeckeGen n) :: ((⟨x⟩ : HeckeGen n) :: u''), -c)]

/-- Stage `1` — `σₓ` has crossed `w₂`. -/
noncomputable def E1 (x m : Fin n) (q : HeckeGen n)
    (t u'' : Monomial (HeckeGen n)) (c : ℝ) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [((q :: t) ++ [(⟨x⟩ : HeckeGen n)], c),
     ((⟨m⟩ : HeckeGen n) :: ((⟨x⟩ : HeckeGen n) :: u''), -c)]

/-- Stage `2` — `σₓ` has crossed `u''` too, so the second term is the rule's
leading monomial with `σₓ` appended. -/
noncomputable def E2 (x m : Fin n) (q : HeckeGen n)
    (t u'' : Monomial (HeckeGen n)) (c : ℝ) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [((q :: t) ++ [(⟨x⟩ : HeckeGen n)], c),
     ((⟨m⟩ : HeckeGen n) :: (u'' ++ [(⟨x⟩ : HeckeGen n)]), -c)]

/-- **The S-polynomial.** -/
theorem oc_spoly_coeff (r : ReductionRule (HeckeGen n) ℝ) (x m : Fin n)
    {q : HeckeGen n} {t u'' : Monomial (HeckeGen n)} {c : ℝ}
    (hrel : ∀ w, r.relation.coeff w
      = (AlgElement.ofTerms [((⟨m⟩ : HeckeGen n) :: u'', c), (q :: t, -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = (⟨m⟩ : HeckeGen n) :: u'')
    (hlc : r.lc (heckeOrder n) = c) (hmx : m.val + 1 < x.val)
    (w : Monomial (HeckeGen n)) :
    (oc r x m u'' hlm hmx).spoly.coeff w = (E0 x m q t u'' c).coeff w := by
  show r.lc (heckeOrder n)
      * (AlgElement.contextMul [] (farCommRelation x m).relation u'').coeff w
    - (farCommRelation x m).lc (heckeOrder n)
      * (AlgElement.contextMul [(⟨x⟩ : HeckeGen n)] r.relation []).coeff w
    = _
  rw [hlc, farCommRelation_lc x m (by omega), one_mul,
    AlgElement.contextMul_coeff_congr [(⟨x⟩ : HeckeGen n)] [] hrel w]
  simp only [E0, farCommRelation, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
    List.map_nil, List.nil_append, List.append_nil, List.cons_append,
    AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Phase 3 — the rule itself, in the context `(ε ∣ σₓ)`, landing on zero. -/
theorem chainStep3 (hp : HeckeParams) (r : ReductionRule (HeckeGen n) ℝ) (x m : Fin n)
    {q : HeckeGen n} {t u'' : Monomial (HeckeGen n)} {c : ℝ} (hn : 0 < n)
    (hrel : ∀ w, r.relation.coeff w
      = (AlgElement.ofTerms [((⟨m⟩ : HeckeGen n) :: u'', c), (q :: t, -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = (⟨m⟩ : HeckeGen n) :: u'')
    (hlc : r.lc (heckeOrder n) = c) (hc : c ≠ 0) (hqm : q ≠ (⟨m⟩ : HeckeGen n))
    (hr : r ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (E2 x m q t u'' c) AlgElement.zero := by
  have hne : (q :: (t ++ [(⟨x⟩ : HeckeGen n)]))
      ≠ (⟨m⟩ : HeckeGen n) :: (u'' ++ [(⟨x⟩ : HeckeGen n)]) := by
    intro hcon
    injection hcon with h1 _
    exact hqm h1
  have hv : (E2 x m q t u'' c).coeff
      (([] : Monomial (HeckeGen n)) ++ r.lm (heckeOrder n)
        ++ [(⟨x⟩ : HeckeGen n)]) = -c := by
    rw [hlm, show (([] : Monomial (HeckeGen n)) ++ ((⟨m⟩ : HeckeGen n) :: u'')
        ++ [(⟨x⟩ : HeckeGen n)])
      = (⟨m⟩ : HeckeGen n) :: (u'' ++ [(⟨x⟩ : HeckeGen n)]) by simp]
    simp [E2, AlgElement.ofTerms_coeff, hne]
  refine ⟨r, hr, [], [(⟨x⟩ : HeckeGen n)], -1, ?_, ?_, ?_⟩
  · rw [hv]; exact neg_ne_zero.mpr hc
  · rw [hv, hlc]; ring
  · intro m'
    show _ = _ - (-1 : ℝ)
      * (AlgElement.contextMul [] r.relation [(⟨x⟩ : HeckeGen n)]).coeff m'
    rw [AlgElement.contextMul_coeff_congr [] [(⟨x⟩ : HeckeGen n)] hrel m']
    simp only [E2, AlgElement.zero, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
      List.map_nil, List.nil_append, List.cons_append,
      AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Two transports and one rule application, to zero.**

`hfar₂` and `hfaru` are the two far-commutation blanket conditions: every letter
of the rule's other word, and of the tail of its leading monomial, is far below
`σₓ`. For both instances they follow from `m + 1 < x` and the fact that no letter
of either word has index above `m`. -/
theorem oc_reduces_to_zero (hp : HeckeParams) (r : ReductionRule (HeckeGen n) ℝ)
    (x m : Fin n) {q : HeckeGen n} {t u'' : Monomial (HeckeGen n)} {c : ℝ} (hn : 0 < n)
    (hrel : ∀ w, r.relation.coeff w
      = (AlgElement.ofTerms [((⟨m⟩ : HeckeGen n) :: u'', c), (q :: t, -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = (⟨m⟩ : HeckeGen n) :: u'')
    (hlc : r.lc (heckeOrder n) = c) (hc : c ≠ 0) (hmx : m.val + 1 < x.val)
    (hqm : q ≠ (⟨m⟩ : HeckeGen n))
    (hfar₂ : ∀ y ∈ q :: t, y.index.val + 1 < x.val)
    (hfaru : ∀ y ∈ u'', y.index.val + 1 < x.val)
    (hr : r ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc r x m u'' hlm hmx).spoly nf ∧ nf.isZero := by
  have hmxg : (⟨m⟩ : HeckeGen n) ≠ ⟨x⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  -- phase 1: `σₓ` crosses `w₂ = q :: t`, with the second term a bystander
  have ph1 : MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (E0 x m q t u'' c) (E1 x m q t u'' c) :=
    farComm_transport_snd hn hp x c (-c) hc
      ((⟨m⟩ : HeckeGen n) :: ((⟨x⟩ : HeckeGen n) :: u'')) (q :: t) [] hfar₂
      (by
        intro u v huv
        cases u with
        | nil =>
          simp only [List.nil_append] at huv ⊢
          intro hcon
          injection hcon with h1 _
          exact hmxg h1
        | cons b u' =>
          rw [List.cons_append] at huv
          injection huv with hb _
          subst hb
          simp only [List.nil_append, List.cons_append]
          intro hcon
          injection hcon with h1 _
          exact hqm h1.symm)
  -- phase 2: `σₓ` crosses `u''`, with the first term a bystander
  have ph2 : MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (E1 x m q t u'' c) (E2 x m q t u'' c) :=
    farComm_transport_fst hn hp x (-c) c (neg_ne_zero.mpr hc)
      ((q :: t) ++ [(⟨x⟩ : HeckeGen n)]) u'' [(⟨m⟩ : HeckeGen n)] hfaru
      (by
        intro u v _
        simp only [List.cons_append]
        intro hcon
        injection hcon with h1 _
        exact hqm h1)
  refine reducesToZero_congr ⟨AlgElement.zero,
    ⟨(ph1.trans ph2).step (chainStep3 hp r x m hn hrel hlm hlc hc hqm hr),
      isNormalForm_of_isZero AlgElement.isZero_zero⟩, AlgElement.isZero_zero⟩ ?_
  intro w
  exact oc_spoly_coeff r x m hrel hlm hlc hmx w

/-! ### The two instances

At `j = m − 1` the Bokut–Shiao and Yang–Baxter rules lead on the same word (§4j),
so the composition exists with either as `rule₂` — the same doubling §4r has, and
the two `n = 4` members of this family, `F31 × B010` and `F31 × Y01`. -/

/-- Every letter of `bsWord₂ m' m j` has index at most `m`. -/
theorem bsWord₂_index_le {m' m j : Fin n} (hm : m'.val + 1 = m.val)
    {y : HeckeGen n} (hy : y ∈ bsWord₂ m' m j) : y.index.val ≤ m.val := by
  rcases List.mem_cons.mp hy with rfl | hy
  · show m'.val ≤ m.val
    omega
  rcases List.mem_cons.mp hy with rfl | hy
  · show m.val ≤ m.val
    omega
  have := descWord_index_le hy
  omega

/-- **Bokut–Shiao**: `u'' = descWord m−1 j ++ [σ_m]`, `w₂ = bsWord₂`, `c = 1`. -/
theorem bokutShiao_resolves (hp : HeckeParams) {x m' m j : Fin n} (hn : 0 < n)
    (hm : m'.val + 1 = m.val) (hj : j.val ≤ m'.val) (hmx : m.val + 1 < x.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc (bokutShiaoRelation m' m j) x m (descWord m' j ++ [(⟨m⟩ : HeckeGen n)])
        (by rw [bokutShiaoRelation_lm hm hj, bsWord₁_cons hm hj]) hmx).spoly nf
      ∧ nf.isZero := by
  have hqm : (⟨m'⟩ : HeckeGen n) ≠ ⟨m⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  refine oc_reduces_to_zero hp (bokutShiaoRelation m' m j) x m
    (q := (⟨m'⟩ : HeckeGen n)) (t := (⟨m⟩ : HeckeGen n) :: descWord m' j) hn ?_
    (by rw [bokutShiaoRelation_lm hm hj, bsWord₁_cons hm hj])
    (bokutShiaoRelation_lc hm hj) one_ne_zero hmx hqm ?_ ?_
    (bokutShiaoRelation_mem hn hp hm hj)
  · intro w
    show (AlgElement.ofTerms [(bsWord₁ m j, (1 : ℝ)), (bsWord₂ m' m j, -1)]).coeff w = _
    rw [bsWord₁_cons hm hj, bsWord₂]
  · intro y hy
    have := bsWord₂_index_le hm (show y ∈ bsWord₂ m' m j from hy)
    omega
  · intro y hy
    rcases List.mem_append.mp hy with hy | hy
    · have := descWord_index_le hy
      omega
    · have hym : y = (⟨m⟩ : HeckeGen n) := List.mem_singleton.mp hy
      subst hym
      show m.val + 1 < x.val
      omega

/-- **Yang–Baxter**: `u'' = [σ_{m−1}, σ_m]`, `w₂ = σ_{m−1}σ_mσ_{m−1}`, `c = −1`.
Its two terms are listed in the opposite order, hence the coefficientwise
`hrel`. -/
theorem yangBaxter_resolves (hp : HeckeParams) {x m' m : Fin n} (hn : 0 < n)
    (hm : m'.val + 1 = m.val) (hmx : m.val + 1 < x.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc (yangBaxterRelation m' m) x m [(⟨m'⟩ : HeckeGen n), (⟨m⟩ : HeckeGen n)]
        (by rw [yangBaxterRelation_lm m' m (by omega)]) hmx).spoly nf
      ∧ nf.isZero := by
  have hqm : (⟨m'⟩ : HeckeGen n) ≠ ⟨m⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  refine oc_reduces_to_zero hp (yangBaxterRelation m' m) x m
    (q := (⟨m'⟩ : HeckeGen n)) (t := [(⟨m⟩ : HeckeGen n), (⟨m'⟩ : HeckeGen n)]) hn ?_
    (by rw [yangBaxterRelation_lm m' m (by omega)])
    (DegenerateYbBs.yangBaxter_lc hm) (by norm_num) hmx hqm ?_ ?_
    (yangBaxterRelation_mem hn hp hm)
  · intro w
    show (AlgElement.ofTerms [([(⟨m'⟩ : HeckeGen n), ⟨m⟩, ⟨m'⟩], (1 : ℝ)),
        ([(⟨m⟩ : HeckeGen n), ⟨m'⟩, ⟨m⟩], -1)]).coeff w = _
    simp only [AlgElement.ofTerms_coeff,
      List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring
  · intro y hy
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hy
    rcases hy with rfl | rfl | rfl
    · show m'.val + 1 < x.val
      omega
    · show m.val + 1 < x.val
      omega
    · show m'.val + 1 < x.val
      omega
  · intro y hy
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hy
    rcases hy with rfl | rfl
    · show m'.val + 1 < x.val
      omega
    · show m.val + 1 < x.val
      omega

end FarCommCyclic

/-! ## §4v  Bokut–Shiao or Yang–Baxter against far-commutation **below** the run

The third and last regime of `BS/YB × farCommRelation i j₀`. §4o is `j₀ + 1 = j`
(one step: the S-polynomial *is* the Bokut–Shiao rule one index lower) and §4s is
`j₀ = j` (four steps: a square at each end). This is `j₀ + 1 < j`, where `σ_{j₀}`
sits strictly below the whole descending run and therefore commutes past *all* of
it. The S-polynomial is

    spoly = c · (descWord i j ++ [σ_{j₀}, σᵢ])  −  c · (w₂ ++ [σ_{j₀}])

writing the first rule as `c · bsWord₁ i j − c · w₂`, and both terms have a
stray `σ_{j₀}` that wants to be at the front:

| phase | term | steps |
|---|---|---|
| 1 | `descWord i j σ_{j₀} σᵢ` → `σ_{j₀} descWord i j σᵢ` | `\|descWord i j\|` |
| 2 | `w₂ σ_{j₀}` → `σ_{j₀} w₂` | `\|w₂\|` |
| 3 | the rule, in the context `(σ_{j₀} ∣ ε)` | `1` |

After phase 1 the first term is `σ_{j₀} :: bsWord₁ i j`, so one application of
the rule in the context `(σ_{j₀} ∣ ε)` turns it into `σ_{j₀} :: w₂` and the terms
cancel. Six steps for both `n = 4` instances.

**This is the mirror transport, and it is a different lemma.** §4t and §4u move a
*big* generator rightwards through small ones; here a *small* generator moves
leftwards through big ones. Same rule `σ_aσ_b → σ_bσ_a`, opposite role in it: the
moving letter is the second factor of the leading monomial rather than the first,
so the induction recurses at the other end of the word and needs a **right**
context, which neither earlier transport carries.

`farComm_transport_left` is therefore stated once, in a form that also removes
the list-slot duplication §4u had to live with: the moving term sits at an
arbitrary position `L₁ ++ (·) :: L₂` of the `ofTerms` list, so one lemma serves
both phases. `ofTerms_coeff_mid` is what makes that work — the coefficient of a
singled-out term, given that no other term carries its word.

**Where the last regime went.** `j < j₀` (the `n = 4` composition `B230 × F31`)
is *not* this: `σ_{j₀}` lands inside the run's index range, so it does not commute
past `σ_{j₀±1}`, and the chain instead fires the Bokut–Shiao rule at the inner
index `j₀` first. That one is left. -/

/-- Every letter of `descWord i j` has index at least `j` — the lower bound to
`descWord_index_le`, and what makes each letter a far-commutation partner of a
generator strictly below `j`. -/
theorem descWord_index_ge {n : ℕ} {i j : Fin n} {y : HeckeGen n}
    (hy : y ∈ descWord i j) : j.val ≤ y.index.val := by
  simp only [descWord, List.mem_map, List.mem_reverse, List.mem_filter,
    List.mem_finRange, true_and, decide_eq_true_eq] at hy
  obtain ⟨k, hk, hky⟩ := hy
  rw [← hky]
  exact hk.1

/-- The coefficient of one singled-out term of an `ofTerms` list, when no other
term carries the same word. Stating the transport for a term at an arbitrary
position needs exactly this. -/
theorem ofTerms_coeff_mid {n : ℕ} (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (W : Monomial (HeckeGen n)) (c : ℝ)
    (h : ∀ r ∈ (L₁ ++ L₂).map Prod.fst, r ≠ W) :
    (AlgElement.ofTerms (L₁ ++ (W, c) :: L₂)).coeff W = c := by
  have hnil : ∀ L : List (Monomial (HeckeGen n) × ℝ),
      (∀ r ∈ L.map Prod.fst, r ≠ W) → L.filter (fun p => decide (p.1 = W)) = [] := by
    intro L hL
    refine List.filter_eq_nil_iff.mpr ?_
    intro a ha
    simp only [decide_eq_true_eq]
    exact hL a.1 (List.mem_map.mpr ⟨a, ha, rfl⟩)
  have h₁ := hnil L₁ (fun r hr => h r (by rw [List.map_append]; exact List.mem_append_left _ hr))
  have h₂ := hnil L₂ (fun r hr => h r (by rw [List.map_append]; exact List.mem_append_right _ hr))
  simp [AlgElement.ofTerms_coeff, List.filter_append, h₁, h₂]

/-! ### §4ak  A cancelling pair drops out

The `a ≤ b` chain's term list is not fixed-shape. `hecke_chain_cancellation.py`
measures its profile: the two quadratic steps each add a term (peak four), and
then **two** later steps remove two at once — which no rewrite can do, since a
far-commutation takes one term to one term. Each is a pair reconverging on a
single word with opposite coefficients and annihilating. Worked at `a = 4`,
`b = 6`, step 24 rewrites `h · σ_i σ_{i−4} ⋯` into precisely the word already
carried by `−h`, and the two vanish.

The first such event is mid-prefix; the second **is the final step**, so the
chain does not terminate by a separate mechanism — reaching zero is itself a
cancellation. That is why the lemma below is needed twice, and why the second
use is what will deliver "reduces to zero".

`MultiStepReduction` is stated through `CoeffEq`, so the cancellation is *sound*
with no help at all (§6 already carries the congruences). What is missing is the
**shape** bridge: without it every lemma downstream of a cancellation would have
to be stated against a list whose first two entries are dead weight. -/

set_option linter.unnecessarySeqFocus false in
/-- **Two terms on one word with opposite coefficients contribute nothing, even
with other terms between them.**

The adjacent case is what §4ak's cancellations need at the top level; the
`a ≤ b` closing phase needs the split one. There the four-term element is
`[(Vh, h), (V1, 1), (Uh, −h), (U1, −1)]`, and the two terms that reconverge are
the two `h`-weighted ones — with `(V1, 1)` sitting between them. That ordering
is not a choice: `trio` emits its `h`-weighted word immediately before its plain
one, in place, so the two lineages interleave as `V, V, U, U`.

`ofTerms_cancel_pair` is this at `M = []`. -/
theorem ofTerms_cancel_split {n : ℕ} (w : Monomial (HeckeGen n)) (c : ℝ)
    (L₁ M L₂ : List (Monomial (HeckeGen n) × ℝ)) :
    AlgElement.CoeffEq
      (AlgElement.ofTerms (L₁ ++ (w, c) :: (M ++ (w, -c) :: L₂)))
      (AlgElement.ofTerms (L₁ ++ (M ++ L₂))) := by
  intro m
  simp only [AlgElement.ofTerms_coeff, List.filter_append, List.filter_cons,
    List.map_append, List.sum_append, decide_eq_true_eq]
  -- The append normalisation has to run AGAIN after `split_ifs`: resolving the
  -- inner `if` leaves `(w, -c) :: filter L₂` sitting inside `filter M ++ …`,
  -- which `map_append` had already passed over. And `simp only` closes some
  -- branches outright while making no progress on others -- "no progress" being
  -- an ERROR rather than a no-op -- so both it and `ring` are guarded. Same
  -- hazard the adjacent-pair proof below documents from the other side.
  split_ifs <;>
    (try simp only [List.map_append, List.sum_append, List.map_cons,
      List.sum_cons]) <;>
    (try ring)

set_option linter.unnecessarySeqFocus false in
/-- **Two terms on one word with opposite coefficients contribute nothing.**
The bridge between the chain's term list before and after a cancellation. -/
theorem ofTerms_cancel_pair {n : ℕ} (w : Monomial (HeckeGen n)) (c : ℝ)
    (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ)) :
    AlgElement.CoeffEq
      (AlgElement.ofTerms (L₁ ++ (w, c) :: (w, -c) :: L₂))
      (AlgElement.ofTerms (L₁ ++ L₂)) := by
  intro m
  simp only [AlgElement.ofTerms_coeff, List.filter_append, List.filter_cons,
    List.map_append, List.sum_append, decide_eq_true_eq]
  -- `linter.unnecessarySeqFocus` proposes `(simp only …; ring)` here. That is
  -- WRONG: `simp only` already closes several of the `split_ifs` branches, so
  -- the sequenced `ring` fails with "no goals to be solved". The option is
  -- disabled for this declaration rather than the suggestion taken.
  split_ifs <;> simp only [List.map_cons, List.sum_cons] <;> ring

/-- **Far-commutation transport, leftwards.** If every letter of `w` is strictly
more than one above `σ_z`, then `σ_z` may be walked from the right end of `w` to
its left end, one far-commutation application per letter, inside any contexts
`a`, `b` and at any position of the term list.

The induction recurses on the *head* of `w` and appends its step at the end,
which is the opposite end from `farComm_transport`: there the moving letter
leads, here it trails. The collision hypothesis enumerates the intermediate words
by splitting `w`, exactly as in §4u.

That enumeration includes the split `u = []`, which names the transport's *final*
word — and the proof never uses it: `hcol` is applied only with a cons-headed
first argument, and the `nil` case discards it outright. So `u ≠ []` suffices,
and it matters. In the corner chain of §4af the bystanding term *is* the final
word, so the unrestricted hypothesis is false exactly where the transport is
needed. `farComm_transport_left` below is this with the stronger hypothesis,
kept because §4v's callers already supply it. -/
theorem farComm_transport_left_sources {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    (z : Fin n)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ)) :
    ∀ (w a b : Monomial (HeckeGen n)), (∀ y ∈ w, z.val + 1 < y.index.val) →
      (∀ u v : Monomial (HeckeGen n), u ++ v = w → u ≠ [] →
          ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
            r ≠ a ++ (u ++ ((⟨z⟩ : HeckeGen n) :: (v ++ b)))) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms
          (L₁ ++ (a ++ (w ++ ((⟨z⟩ : HeckeGen n) :: b)), c) :: L₂))
        (AlgElement.ofTerms
          (L₁ ++ (a ++ ((⟨z⟩ : HeckeGen n) :: (w ++ b)), c) :: L₂)) := by
  intro w
  induction w with
  | nil => intro a b _ _; exact MultiStepReduction.refl _
  | cons y w ih =>
    intro a b hw hcol
    obtain ⟨yi⟩ := y
    have hy : z.val + 1 < yi.val := hw _ (by simp)
    have hyz : (⟨yi⟩ : HeckeGen n) ≠ ⟨z⟩ := by
      intro hcon
      have := congrArg HeckeGen.rank hcon
      simp only [HeckeGen.rank] at this
      omega
    have key := ih (a ++ [(⟨yi⟩ : HeckeGen n)]) b (fun t ht => hw t (by simp [ht]))
      (fun u v huv _ => by
        have := hcol ((⟨yi⟩ : HeckeGen n) :: u) v (by rw [List.cons_append, huv])
          (by simp)
        simpa only [List.append_assoc, List.singleton_append, List.cons_append] using this)
    simp only [List.append_assoc, List.singleton_append] at key
    show MultiStepReduction _ _ (AlgElement.ofTerms
      (L₁ ++ (a ++ ((⟨yi⟩ : HeckeGen n) :: (w ++ ((⟨z⟩ : HeckeGen n) :: b))), c) :: L₂)) _
    refine MultiStepReduction.step key ?_
    have hv : (AlgElement.ofTerms
        (L₁ ++ (a ++ ((⟨yi⟩ : HeckeGen n) :: ((⟨z⟩ : HeckeGen n) :: (w ++ b))), c) :: L₂)).coeff
        (a ++ (farCommRelation yi z).lm (heckeOrder n) ++ (w ++ b)) = c := by
      rw [farCommRelation_lm yi z (by omega),
        show (a ++ [(⟨yi⟩ : HeckeGen n), (⟨z⟩ : HeckeGen n)] ++ (w ++ b))
          = a ++ ((⟨yi⟩ : HeckeGen n) :: ((⟨z⟩ : HeckeGen n) :: (w ++ b))) by simp]
      refine ofTerms_coeff_mid L₁ L₂ _ c (fun r hr => ?_)
      have := hcol [(⟨yi⟩ : HeckeGen n)] w rfl (by simp) r hr
      simpa only [List.singleton_append, List.cons_append] using this
    refine ⟨farCommRelation yi z, farCommRelation_mem hn hp hy, a, w ++ b, c, ?_, ?_, ?_⟩
    · rw [hv]; exact hc
    · rw [hv, farCommRelation_lc yi z (by omega)]; ring
    · intro m
      show _ = _ - c
        * (AlgElement.contextMul a (farCommRelation yi z).relation (w ++ b)).coeff m
      simp only [farCommRelation, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
        List.map_nil, List.cons_append, List.nil_append, List.append_assoc,
        AlgElement.ofTerms_coeff, List.filter_append, List.filter_cons, List.filter_nil,
        List.map_append, List.sum_append, decide_eq_true_eq]
      split_ifs <;>
        simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- The transport with the unrestricted collision hypothesis — every split of `w`,
including the one naming the final word. Weaker than
`farComm_transport_left_sources` and kept for §4v's callers. -/
theorem farComm_transport_left {n : ℕ} (hn : 0 < n) (hp : HeckeParams) (z : Fin n)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ)) :
    ∀ (w a b : Monomial (HeckeGen n)), (∀ y ∈ w, z.val + 1 < y.index.val) →
      (∀ u v : Monomial (HeckeGen n), u ++ v = w →
          ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
            r ≠ a ++ (u ++ ((⟨z⟩ : HeckeGen n) :: (v ++ b)))) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms
          (L₁ ++ (a ++ (w ++ ((⟨z⟩ : HeckeGen n) :: b)), c) :: L₂))
        (AlgElement.ofTerms
          (L₁ ++ (a ++ ((⟨z⟩ : HeckeGen n) :: (w ++ b)), c) :: L₂)) :=
  fun w a b hw hcol =>
    farComm_transport_left_sources hn hp z c hc L₁ L₂ w a b hw
      (fun u v huv _ => hcol u v huv)

namespace CyclicFarCommLow

variable {n : ℕ}

/-- The composition of a rule leading on `σᵢ D' σᵢ` with the far-commutation rule
`σᵢ σ_{j₀}`, overlapping in the trailing `σᵢ`. -/
noncomputable def oc (r : ReductionRule (HeckeGen n) ℝ) (i j₀ : Fin n)
    (D' : Monomial (HeckeGen n))
    (hlm : r.lm (heckeOrder n)
      = ((⟨i⟩ : HeckeGen n) :: D') ++ [(⟨i⟩ : HeckeGen n)])
    (hij : j₀.val + 1 < i.val) : OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := r
  rule₂ := farCommRelation i j₀
  left := (⟨i⟩ : HeckeGen n) :: D'
  overlap := [⟨i⟩]
  right := [⟨j₀⟩]
  lm₁_decomp := hlm
  lm₂_decomp := by rw [farCommRelation_lm i j₀ (by omega)]; rfl
  overlap_nonempty := by simp

/-- Stage `0` — the S-polynomial. The ambient word cancels; each surviving term
carries a stray `σ_{j₀}`. -/
noncomputable def E0 (i j₀ : Fin n) (q : HeckeGen n) (D' s : Monomial (HeckeGen n))
    (c : ℝ) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(((⟨i⟩ : HeckeGen n) :: D') ++ ((⟨j₀⟩ : HeckeGen n) :: [(⟨i⟩ : HeckeGen n)]), c),
     ((q :: s) ++ [(⟨j₀⟩ : HeckeGen n)], -c)]

/-- Stage `1` — `σ_{j₀}` has crossed the descending run. -/
noncomputable def E1 (i j₀ : Fin n) (q : HeckeGen n) (D' s : Monomial (HeckeGen n))
    (c : ℝ) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [((⟨j₀⟩ : HeckeGen n) :: (((⟨i⟩ : HeckeGen n) :: D') ++ [(⟨i⟩ : HeckeGen n)]), c),
     ((q :: s) ++ [(⟨j₀⟩ : HeckeGen n)], -c)]

/-- Stage `2` — and the rule's other word too, so the first term is now the
leading monomial in the context `(σ_{j₀} ∣ ε)`. -/
noncomputable def E2 (i j₀ : Fin n) (q : HeckeGen n) (D' s : Monomial (HeckeGen n))
    (c : ℝ) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [((⟨j₀⟩ : HeckeGen n) :: (((⟨i⟩ : HeckeGen n) :: D') ++ [(⟨i⟩ : HeckeGen n)]), c),
     ((⟨j₀⟩ : HeckeGen n) :: ((q :: s) ++ ([] : Monomial (HeckeGen n))), -c)]

/-- **The S-polynomial.** -/
theorem oc_spoly_coeff (r : ReductionRule (HeckeGen n) ℝ) (i j₀ : Fin n)
    {q : HeckeGen n} {D' s : Monomial (HeckeGen n)} {c : ℝ}
    (hrel : ∀ w, r.relation.coeff w
      = (AlgElement.ofTerms
          [(((⟨i⟩ : HeckeGen n) :: D') ++ [(⟨i⟩ : HeckeGen n)], c), (q :: s, -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = ((⟨i⟩ : HeckeGen n) :: D') ++ [(⟨i⟩ : HeckeGen n)])
    (hlc : r.lc (heckeOrder n) = c) (hij : j₀.val + 1 < i.val)
    (w : Monomial (HeckeGen n)) :
    (oc r i j₀ D' hlm hij).spoly.coeff w = (E0 i j₀ q D' s c).coeff w := by
  show (farCommRelation i j₀).lc (heckeOrder n)
      * (AlgElement.contextMul [] r.relation [⟨j₀⟩]).coeff w
    - r.lc (heckeOrder n)
      * (AlgElement.contextMul ((⟨i⟩ : HeckeGen n) :: D')
          (farCommRelation i j₀).relation []).coeff w
    = _
  rw [hlc, farCommRelation_lc i j₀ (by omega), one_mul,
    AlgElement.contextMul_coeff_congr [] [(⟨j₀⟩ : HeckeGen n)] hrel w]
  simp only [E0, farCommRelation, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
    List.map_nil, List.nil_append, List.append_nil, List.cons_append, List.append_assoc,
    AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Phase 3 — the rule itself, in the context `(σ_{j₀} ∣ ε)`, landing on zero.
The one distinctness needed is the first letter: the rule's other word begins
with `q`, its leading monomial with `σᵢ`. -/
theorem chainStep3 (hp : HeckeParams) (r : ReductionRule (HeckeGen n) ℝ) (i j₀ : Fin n)
    {q : HeckeGen n} {D' s : Monomial (HeckeGen n)} {c : ℝ} (hn : 0 < n)
    (hrel : ∀ w, r.relation.coeff w
      = (AlgElement.ofTerms
          [(((⟨i⟩ : HeckeGen n) :: D') ++ [(⟨i⟩ : HeckeGen n)], c), (q :: s, -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = ((⟨i⟩ : HeckeGen n) :: D') ++ [(⟨i⟩ : HeckeGen n)])
    (hlc : r.lc (heckeOrder n) = c) (hc : c ≠ 0) (hqi : q ≠ (⟨i⟩ : HeckeGen n))
    (hr : r ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (E2 i j₀ q D' s c) AlgElement.zero := by
  have hne : ((⟨j₀⟩ : HeckeGen n) :: (q :: s))
      ≠ (⟨j₀⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n) :: (D' ++ [(⟨i⟩ : HeckeGen n)])) := by
    intro hcon
    injection hcon with _ h2
    injection h2 with h3 _
    exact hqi h3
  have hv : (E2 i j₀ q D' s c).coeff
      ([(⟨j₀⟩ : HeckeGen n)] ++ r.lm (heckeOrder n) ++ []) = c := by
    rw [hlm, show ([(⟨j₀⟩ : HeckeGen n)] ++ (((⟨i⟩ : HeckeGen n) :: D')
        ++ [(⟨i⟩ : HeckeGen n)]) ++ [])
      = (⟨j₀⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n) :: (D' ++ [(⟨i⟩ : HeckeGen n)]))
      by simp]
    simp [E2, AlgElement.ofTerms_coeff, hne]
  refine ⟨r, hr, [(⟨j₀⟩ : HeckeGen n)], [], 1, ?_, ?_, ?_⟩
  · rw [hv]; exact hc
  · rw [hv, hlc]; ring
  · intro m
    show _ = _ - (1 : ℝ)
      * (AlgElement.contextMul [(⟨j₀⟩ : HeckeGen n)] r.relation []).coeff m
    rw [AlgElement.contextMul_coeff_congr [(⟨j₀⟩ : HeckeGen n)] [] hrel m]
    simp only [E2, AlgElement.zero, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
      List.map_nil, List.nil_append, List.append_nil, List.cons_append,
      AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Two leftward transports and one rule application, to zero.**

Every side condition reduces to the two letter inequalities `q ≠ σᵢ` and
`q ≠ σ_{j₀}`: the rule's other word begins with a letter that is neither the top
of the run nor the travelling generator, which is what keeps it distinguishable
from every intermediate word of both transports. -/
theorem oc_reduces_to_zero (hp : HeckeParams) (r : ReductionRule (HeckeGen n) ℝ)
    (i j₀ : Fin n) {q : HeckeGen n} {D' s : Monomial (HeckeGen n)} {c : ℝ} (hn : 0 < n)
    (hrel : ∀ w, r.relation.coeff w
      = (AlgElement.ofTerms
          [(((⟨i⟩ : HeckeGen n) :: D') ++ [(⟨i⟩ : HeckeGen n)], c), (q :: s, -c)]).coeff w)
    (hlm : r.lm (heckeOrder n) = ((⟨i⟩ : HeckeGen n) :: D') ++ [(⟨i⟩ : HeckeGen n)])
    (hlc : r.lc (heckeOrder n) = c) (hc : c ≠ 0) (hij : j₀.val + 1 < i.val)
    (hqi : q ≠ (⟨i⟩ : HeckeGen n)) (hqj : q ≠ (⟨j₀⟩ : HeckeGen n))
    (hfarD : ∀ y ∈ (⟨i⟩ : HeckeGen n) :: D', j₀.val + 1 < y.index.val)
    (hfar₂ : ∀ y ∈ q :: s, j₀.val + 1 < y.index.val)
    (hr : r ∈ (heckeCompletedRewritingSystem n hn hp).rules) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc r i j₀ D' hlm hij).spoly nf ∧ nf.isZero := by
  -- phase 1: `σ_{j₀}` crosses the descending run, the other term a bystander
  have ph1 : MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (E0 i j₀ q D' s c) (E1 i j₀ q D' s c) :=
    farComm_transport_left hn hp j₀ c hc [] [((q :: s) ++ [(⟨j₀⟩ : HeckeGen n)], -c)]
      ((⟨i⟩ : HeckeGen n) :: D') [] [(⟨i⟩ : HeckeGen n)] hfarD
      (by
        intro u v huv r' hr'
        simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
          List.not_mem_nil, or_false] at hr'
        subst hr'
        cases u with
        | nil =>
          simp only [List.nil_append, List.cons_append]
          intro hcon
          injection hcon with h1 _
          exact hqj h1
        | cons a u' =>
          rw [List.cons_append] at huv
          injection huv with ha _
          subst ha
          simp only [List.cons_append]
          intro hcon
          injection hcon with h1 _
          exact hqi h1)
  -- phase 2: and across the rule's other word, the first term a bystander
  have ph2 : MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (E1 i j₀ q D' s c) (E2 i j₀ q D' s c) :=
    farComm_transport_left hn hp j₀ (-c) (neg_ne_zero.mpr hc)
      [((⟨j₀⟩ : HeckeGen n) :: (((⟨i⟩ : HeckeGen n) :: D') ++ [(⟨i⟩ : HeckeGen n)]), c)] []
      (q :: s) [] [] hfar₂
      (by
        intro u v huv r' hr'
        simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
          List.not_mem_nil, or_false] at hr'
        subst hr'
        cases u with
        | nil =>
          simp only [List.nil_append] at huv
          subst huv
          simp only [List.nil_append, List.append_nil, List.cons_append]
          intro hcon
          injection hcon with _ h2
          injection h2 with h3 _
          exact hqi h3.symm
        | cons a u' =>
          rw [List.cons_append] at huv
          injection huv with ha _
          subst ha
          simp only [List.nil_append, List.append_nil, List.cons_append]
          intro hcon
          injection hcon with h1 _
          exact hqj h1.symm)
  refine reducesToZero_congr ⟨AlgElement.zero,
    ⟨(ph1.trans ph2).step (chainStep3 hp r i j₀ hn hrel hlm hlc hc hqi hr),
      isNormalForm_of_isZero AlgElement.isZero_zero⟩, AlgElement.isZero_zero⟩ ?_
  intro w
  exact oc_spoly_coeff r i j₀ hrel hlm hlc hij w

/-! ### The two instances

As in §4r and §4u, at `j = i − 1` the Bokut–Shiao and Yang–Baxter rules lead on
the same word, so both must be discharged. Those are the `n = 4` members
`B232 × F30` and `Y23 × F30`. -/

/-- Every letter of `bsWord₂ i' i j` has index at least `j`. -/
theorem bsWord₂_index_ge {i' i j : Fin n} (hi : i'.val + 1 = i.val)
    (hj : j.val ≤ i'.val) {y : HeckeGen n} (hy : y ∈ bsWord₂ i' i j) :
    j.val ≤ y.index.val := by
  rcases List.mem_cons.mp hy with rfl | hy
  · show j.val ≤ i'.val
    omega
  rcases List.mem_cons.mp hy with rfl | hy
  · show j.val ≤ i.val
    omega
  exact descWord_index_ge hy

/-- **Bokut–Shiao**, at any `j` with `j₀ + 1 < j`. -/
theorem bokutShiao_resolves (hp : HeckeParams) {i' i j j₀ : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val) (hj₀ : j₀.val + 1 < j.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc (bokutShiaoRelation i' i j) i j₀ (descWord i' j)
        (by rw [bokutShiaoRelation_lm hi hj, bsWord₁, descWord_cons hi hj])
        (by omega)).spoly nf ∧ nf.isZero := by
  have hqi : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  have hqj : (⟨i'⟩ : HeckeGen n) ≠ ⟨j₀⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  refine oc_reduces_to_zero hp (bokutShiaoRelation i' i j) i j₀
    (q := (⟨i'⟩ : HeckeGen n)) (s := (⟨i⟩ : HeckeGen n) :: descWord i' j) hn ?_
    (by rw [bokutShiaoRelation_lm hi hj, bsWord₁, descWord_cons hi hj])
    (bokutShiaoRelation_lc hi hj) one_ne_zero (by omega) hqi hqj ?_ ?_
    (bokutShiaoRelation_mem hn hp hi hj)
  · intro w
    show (AlgElement.ofTerms [(bsWord₁ i j, (1 : ℝ)), (bsWord₂ i' i j, -1)]).coeff w = _
    rw [bsWord₁, descWord_cons hi hj, bsWord₂]
  · intro y hy
    rw [← descWord_cons hi hj] at hy
    have := descWord_index_ge hy
    omega
  · intro y hy
    have := bsWord₂_index_ge hi hj (show y ∈ bsWord₂ i' i j from hy)
    omega

/-- **Yang–Baxter**, which exists only at `j = i − 1`. -/
theorem yangBaxter_resolves (hp : HeckeParams) {i' i j₀ : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hj₀ : j₀.val + 1 < i'.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc (yangBaxterRelation i' i) i j₀ [(⟨i'⟩ : HeckeGen n)]
        (by rw [yangBaxterRelation_lm i' i (by omega)]; rfl)
        (by omega)).spoly nf ∧ nf.isZero := by
  have hqi : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  have hqj : (⟨i'⟩ : HeckeGen n) ≠ ⟨j₀⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  refine oc_reduces_to_zero hp (yangBaxterRelation i' i) i j₀
    (q := (⟨i'⟩ : HeckeGen n)) (s := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]) hn ?_
    (by rw [yangBaxterRelation_lm i' i (by omega)]; rfl)
    (DegenerateYbBs.yangBaxter_lc hi) (by norm_num) (by omega) hqi hqj ?_ ?_
    (yangBaxterRelation_mem hn hp hi)
  · intro w
    show (AlgElement.ofTerms [([(⟨i'⟩ : HeckeGen n), ⟨i⟩, ⟨i'⟩], (1 : ℝ)),
        ([(⟨i⟩ : HeckeGen n), ⟨i'⟩, ⟨i⟩], -1)]).coeff w = _
    simp only [AlgElement.ofTerms_coeff, List.cons_append, List.nil_append,
      List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring
  · intro y hy
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hy
    rcases hy with rfl | rfl
    · show j₀.val + 1 < i.val
      omega
    · show j₀.val + 1 < i'.val
      omega
  · intro y hy
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hy
    rcases hy with rfl | rfl | rfl
    · show j₀.val + 1 < i'.val
      omega
    · show j₀.val + 1 < i.val
      omega
    · show j₀.val + 1 < i'.val
      omega

end CyclicFarCommLow

/-! ## §4w  Far-commutation **inside** the descending run — the last regime

The fourth and last position `j₀` can take relative to `descWord i j`, and the
one that is not a transport. §4o (`j₀ + 1 = j`), §4s (`j₀ = j`) and §4v
(`j₀ + 1 < j`) all have `σ_{j₀}` at or below the bottom of the run. Here
`j < j₀`, so `σ_{j₀}` is a letter the run already contains, and it does *not*
commute past its own neighbours `σ_{j₀±1}`.

**What happens instead.** Split the run at `j₀`:

    descWord i j = descWord i jup ++ (σ_{j₀} :: descWord j₀' j)

writing `jup` for `j₀ + 1` and `j₀'` for `j₀ − 1`. Then the first term of the
S-polynomial ends in

    descWord j₀ j ++ [σ_{j₀}]  =  bsWord₁ j₀ j

— the Bokut–Shiao word at the **inner** index `j₀`. So the inner rule fires
first, and what it leaves is `σ_{j₀'} :: σ_{j₀} :: descWord j₀' j`, whose leading
`σ_{j₀'}` is *now* below everything above it and can be transported to the front.
The same thing happens in the second term. Five stages:

| # | target | rule | context |
|---|---|---|---|
| 1 | `bsWord₁ j₀ j` in term 1 | Bokut–Shiao at `j₀` | `(σᵢ descWord i' jup ∣ σᵢ)` |
| 2… | `σ_{j₀'}` to the front | far-commutation | `\|descWord i jup\|` steps |
| 3 | `bsWord₁ j₀ j` in term 2 | Bokut–Shiao at `j₀` | `(σᵢ₋₁σᵢ descWord i' jup ∣ ε)` |
| 4… | `σ_{j₀'}` to the front | far-commutation | `\|descWord i' jup\| + 2` steps |
| 5 | `bsWord₁ i j` | Bokut–Shiao at `j` | `(σ_{j₀'} ∣ ε)` |

After stage 2 the first term is `σ_{j₀'} :: bsWord₁ i j` and after stage 4 the
second is `σ_{j₀'} :: bsWord₂ i' i j`, so the outer rule in the context
`(σ_{j₀'} ∣ ε)` closes the gap. Eight steps at `n = 4`, matching `B230 × F31`.

**Only Bokut–Shiao occurs here.** `j < j₀` and `j₀ + 1 < i` force
`j < j₀ ≤ i − 2 < i − 1`, so `j ≠ i − 1` and the Yang–Baxter rule never leads on
`bsWord₁ i j`. Unlike §4r, §4u and §4v there is no second instance to discharge —
the regime that creates the nesting also rules out the doubling.

The composition is §4v's, so `CyclicFarCommLow.oc` and its S-polynomial are
reused verbatim; only the chain is new. What is new besides the chain is
`descWord_split`, and that is a word identity the `B × B` block will want too. -/

/-- **The descending run splits at any interior index.** Proved by walking the
bottom index down with `descWord_snoc`, so the induction is on the gap
`k' − j` rather than on `List.finRange`. -/
theorem descWord_split_aux {n : ℕ} {i k k' : Fin n} (hk : k'.val + 1 = k.val)
    (hki : k.val ≤ i.val) :
    ∀ (d : ℕ) (j : Fin n), k'.val = j.val + d →
      descWord i j = descWord i k ++ descWord k' j := by
  intro d
  induction d with
  | zero =>
    intro j hj
    have hjk : j = k' := Fin.ext (by omega)
    subst hjk
    rw [descWord_snoc hk hki, descWord_self]
  | succ d ih =>
    intro j hj
    have hk' := k'.isLt
    have hlt : j.val + 1 < n := by omega
    have h1 : descWord i j
        = descWord i ⟨j.val + 1, hlt⟩ ++ [(⟨j⟩ : HeckeGen n)] :=
      descWord_snoc rfl (show j.val + 1 ≤ i.val by omega)
    have h2 : descWord k' j
        = descWord k' ⟨j.val + 1, hlt⟩ ++ [(⟨j⟩ : HeckeGen n)] :=
      descWord_snoc rfl (show j.val + 1 ≤ k'.val by omega)
    rw [h1, h2, ih ⟨j.val + 1, hlt⟩ (show k'.val = j.val + 1 + d by omega),
      List.append_assoc]

/-- `descWord i j = descWord i k ++ descWord k' j` whenever `k' + 1 = k` and the
split point lies inside the run. -/
theorem descWord_split {n : ℕ} {i j k k' : Fin n} (hk : k'.val + 1 = k.val)
    (hj : j.val ≤ k'.val) (hki : k.val ≤ i.val) :
    descWord i j = descWord i k ++ descWord k' j :=
  descWord_split_aux hk hki (k'.val - j.val) j (by omega)

namespace CyclicFarCommInner

variable {n : ℕ}

/-- Stage `1` — the inner Bokut–Shiao rule has fired in the first term. -/
noncomputable def T1 (i' i j₀' j₀ : Fin n) (A' B : Monomial (HeckeGen n)) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(((⟨i⟩ : HeckeGen n) :: A') ++ ((⟨j₀'⟩ : HeckeGen n)
        :: ((⟨j₀⟩ : HeckeGen n) :: (B ++ [(⟨i⟩ : HeckeGen n)]))), (1 : ℝ)),
     (((⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n) :: (A' ++ ((⟨j₀⟩ : HeckeGen n) :: B))))
        ++ [(⟨j₀⟩ : HeckeGen n)], -1)]

/-- Stage `2` — `σ_{j₀'}` has crossed the upper run, so the first term is
`σ_{j₀'} :: bsWord₁ i j`. -/
noncomputable def T2 (i' i j₀' j₀ : Fin n) (A' B : Monomial (HeckeGen n)) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [((⟨j₀'⟩ : HeckeGen n) :: (((⟨i⟩ : HeckeGen n) :: A')
        ++ ((⟨j₀⟩ : HeckeGen n) :: (B ++ [(⟨i⟩ : HeckeGen n)]))), (1 : ℝ)),
     (((⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n) :: (A' ++ ((⟨j₀⟩ : HeckeGen n) :: B))))
        ++ [(⟨j₀⟩ : HeckeGen n)], -1)]

/-- Stage `3` — the inner rule has fired in the second term too. -/
noncomputable def T3 (i' i j₀' j₀ : Fin n) (A' B : Monomial (HeckeGen n)) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [((⟨j₀'⟩ : HeckeGen n) :: (((⟨i⟩ : HeckeGen n) :: A')
        ++ ((⟨j₀⟩ : HeckeGen n) :: (B ++ [(⟨i⟩ : HeckeGen n)]))), (1 : ℝ)),
     (([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ A') ++ ((⟨j₀'⟩ : HeckeGen n)
        :: ((⟨j₀⟩ : HeckeGen n) :: B)), -1)]

/-- Stage `4` — both terms now begin with `σ_{j₀'}`, and what follows is the
outer rule's two words. -/
noncomputable def T4 (i' i j₀' j₀ : Fin n) (A' B : Monomial (HeckeGen n)) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [((⟨j₀'⟩ : HeckeGen n) :: (((⟨i⟩ : HeckeGen n) :: A')
        ++ ((⟨j₀⟩ : HeckeGen n) :: (B ++ [(⟨i⟩ : HeckeGen n)]))), (1 : ℝ)),
     ((⟨j₀'⟩ : HeckeGen n) :: (([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ A')
        ++ ((⟨j₀⟩ : HeckeGen n) :: B)), -1)]

section

variable (hp : HeckeParams) {i' i j₀' j₀ j : Fin n} {A' B : Monomial (HeckeGen n)}

/-- Step 1 — the inner Bokut–Shiao rule, in the context `(σᵢ A' ∣ σᵢ)`. -/
theorem chainStep1 (hn : 0 < n) (hjj : j₀'.val + 1 = j₀.val) (hjle : j.val ≤ j₀'.val)
    (hii' : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩)
    (hB : descWord j₀' j = B) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (CyclicFarCommLow.E0 i j₀ (⟨i'⟩ : HeckeGen n)
        (A' ++ ((⟨j₀⟩ : HeckeGen n) :: B))
        ((⟨i⟩ : HeckeGen n) :: (A' ++ ((⟨j₀⟩ : HeckeGen n) :: B))) 1)
      (T1 i' i j₀' j₀ A' B) := by
  have hlm : (bokutShiaoRelation j₀' j₀ j).lm (heckeOrder n)
      = ((⟨j₀⟩ : HeckeGen n) :: B) ++ [(⟨j₀⟩ : HeckeGen n)] := by
    rw [bokutShiaoRelation_lm hjj hjle, bsWord₁, descWord_cons hjj hjle, hB]
  have hrel : ∀ w, (bokutShiaoRelation j₀' j₀ j).relation.coeff w
      = (AlgElement.ofTerms
          [(((⟨j₀⟩ : HeckeGen n) :: B) ++ [(⟨j₀⟩ : HeckeGen n)], (1 : ℝ)),
           ((⟨j₀'⟩ : HeckeGen n) :: ((⟨j₀⟩ : HeckeGen n) :: B), -1)]).coeff w := by
    intro w
    show (AlgElement.ofTerms [(bsWord₁ j₀ j, (1 : ℝ)), (bsWord₂ j₀' j₀ j, -1)]).coeff w = _
    rw [bsWord₁, descWord_cons hjj hjle, hB, bsWord₂, hB]
  have hne : ((⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n)
        :: (A' ++ ((⟨j₀⟩ : HeckeGen n) :: (B ++ [(⟨j₀⟩ : HeckeGen n)])))))
      ≠ (⟨i⟩ : HeckeGen n) :: (A' ++ ((⟨j₀⟩ : HeckeGen n)
          :: (B ++ [(⟨j₀⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]))) := by
    intro hcon
    injection hcon with h1 _
    exact hii' h1
  have hv : (CyclicFarCommLow.E0 i j₀ (⟨i'⟩ : HeckeGen n)
      (A' ++ ((⟨j₀⟩ : HeckeGen n) :: B))
      ((⟨i⟩ : HeckeGen n) :: (A' ++ ((⟨j₀⟩ : HeckeGen n) :: B))) 1).coeff
      (((⟨i⟩ : HeckeGen n) :: A') ++ (bokutShiaoRelation j₀' j₀ j).lm (heckeOrder n)
        ++ [(⟨i⟩ : HeckeGen n)]) = 1 := by
    rw [hlm, show (((⟨i⟩ : HeckeGen n) :: A') ++ (((⟨j₀⟩ : HeckeGen n) :: B)
        ++ [(⟨j₀⟩ : HeckeGen n)]) ++ [(⟨i⟩ : HeckeGen n)])
      = (⟨i⟩ : HeckeGen n) :: (A' ++ ((⟨j₀⟩ : HeckeGen n)
          :: (B ++ [(⟨j₀⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]))) by simp]
    simp [CyclicFarCommLow.E0, AlgElement.ofTerms_coeff, hne]
  refine ⟨bokutShiaoRelation j₀' j₀ j, bokutShiaoRelation_mem hn hp hjj hjle,
    (⟨i⟩ : HeckeGen n) :: A', [(⟨i⟩ : HeckeGen n)], 1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, bokutShiaoRelation_lc hjj hjle]; ring
  · intro m
    show _ = _ - (1 : ℝ) * (AlgElement.contextMul ((⟨i⟩ : HeckeGen n) :: A')
      (bokutShiaoRelation j₀' j₀ j).relation [(⟨i⟩ : HeckeGen n)]).coeff m
    rw [AlgElement.contextMul_coeff_congr ((⟨i⟩ : HeckeGen n) :: A')
      [(⟨i⟩ : HeckeGen n)] hrel m]
    simp only [CyclicFarCommLow.E0, T1, AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append, List.cons_append,
      List.append_assoc, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 3 — the inner rule again, now in the second term. -/
theorem chainStep3 (hn : 0 < n) (hjj : j₀'.val + 1 = j₀.val) (hjle : j.val ≤ j₀'.val)
    (hjq : (⟨j₀'⟩ : HeckeGen n) ≠ ⟨i'⟩)
    (hB : descWord j₀' j = B) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T2 i' i j₀' j₀ A' B) (T3 i' i j₀' j₀ A' B) := by
  have hlm : (bokutShiaoRelation j₀' j₀ j).lm (heckeOrder n)
      = ((⟨j₀⟩ : HeckeGen n) :: B) ++ [(⟨j₀⟩ : HeckeGen n)] := by
    rw [bokutShiaoRelation_lm hjj hjle, bsWord₁, descWord_cons hjj hjle, hB]
  have hrel : ∀ w, (bokutShiaoRelation j₀' j₀ j).relation.coeff w
      = (AlgElement.ofTerms
          [(((⟨j₀⟩ : HeckeGen n) :: B) ++ [(⟨j₀⟩ : HeckeGen n)], (1 : ℝ)),
           ((⟨j₀'⟩ : HeckeGen n) :: ((⟨j₀⟩ : HeckeGen n) :: B), -1)]).coeff w := by
    intro w
    show (AlgElement.ofTerms [(bsWord₁ j₀ j, (1 : ℝ)), (bsWord₂ j₀' j₀ j, -1)]).coeff w = _
    rw [bsWord₁, descWord_cons hjj hjle, hB, bsWord₂, hB]
  have hne : ((⟨j₀'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n)
        :: (A' ++ ((⟨j₀⟩ : HeckeGen n) :: (B ++ [(⟨i⟩ : HeckeGen n)])))))
      ≠ (⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n) :: (A' ++ ((⟨j₀⟩ : HeckeGen n)
          :: (B ++ [(⟨j₀⟩ : HeckeGen n)])))) := by
    intro hcon
    injection hcon with h1 _
    exact hjq h1
  have hv : (T2 i' i j₀' j₀ A' B).coeff
      (([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ A')
        ++ (bokutShiaoRelation j₀' j₀ j).lm (heckeOrder n) ++ []) = -1 := by
    rw [hlm, show (([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ A')
        ++ (((⟨j₀⟩ : HeckeGen n) :: B) ++ [(⟨j₀⟩ : HeckeGen n)]) ++ [])
      = (⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n) :: (A' ++ ((⟨j₀⟩ : HeckeGen n)
          :: (B ++ [(⟨j₀⟩ : HeckeGen n)])))) by simp]
    simp [T2, AlgElement.ofTerms_coeff, hne]
  refine ⟨bokutShiaoRelation j₀' j₀ j, bokutShiaoRelation_mem hn hp hjj hjle,
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ A', [], -1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, bokutShiaoRelation_lc hjj hjle]; ring
  · intro m
    show _ = _ - (-1 : ℝ) * (AlgElement.contextMul
      ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ A')
      (bokutShiaoRelation j₀' j₀ j).relation []).coeff m
    rw [AlgElement.contextMul_coeff_congr
      ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ A') [] hrel m]
    simp only [T2, T3, AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append, List.append_nil, List.cons_append,
      List.append_assoc, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 5 — the outer rule, in the context `(σ_{j₀'} ∣ ε)`, landing on zero. -/
theorem chainStep5 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val)
    (hii' : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩)
    (hsplit : descWord i j = ((⟨i⟩ : HeckeGen n) :: A') ++ ((⟨j₀⟩ : HeckeGen n) :: B))
    (hsplit' : descWord i' j = A' ++ ((⟨j₀⟩ : HeckeGen n) :: B)) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T4 i' i j₀' j₀ A' B) AlgElement.zero := by
  have hlm : (bokutShiaoRelation i' i j).lm (heckeOrder n)
      = ((⟨i⟩ : HeckeGen n) :: A') ++ ((⟨j₀⟩ : HeckeGen n) :: (B ++ [(⟨i⟩ : HeckeGen n)])) := by
    rw [bokutShiaoRelation_lm hi hj, bsWord₁, hsplit]
    simp
  have hrel : ∀ w, (bokutShiaoRelation i' i j).relation.coeff w
      = (AlgElement.ofTerms
          [(((⟨i⟩ : HeckeGen n) :: A') ++ ((⟨j₀⟩ : HeckeGen n)
              :: (B ++ [(⟨i⟩ : HeckeGen n)])), (1 : ℝ)),
           ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ A'
              ++ ((⟨j₀⟩ : HeckeGen n) :: B), -1)]).coeff w := by
    intro w
    show (AlgElement.ofTerms [(bsWord₁ i j, (1 : ℝ)), (bsWord₂ i' i j, -1)]).coeff w = _
    rw [bsWord₁, hsplit, bsWord₂, hsplit']
    simp only [List.cons_append, List.nil_append, List.append_assoc]
  have hne : ((⟨j₀'⟩ : HeckeGen n) :: ((⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n)
        :: (A' ++ ((⟨j₀⟩ : HeckeGen n) :: B)))))
      ≠ (⟨j₀'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n) :: (A' ++ ((⟨j₀⟩ : HeckeGen n)
          :: (B ++ [(⟨i⟩ : HeckeGen n)])))) := by
    intro hcon
    injection hcon with _ h2
    injection h2 with h3 _
    exact hii' h3
  have hv : (T4 i' i j₀' j₀ A' B).coeff
      ([(⟨j₀'⟩ : HeckeGen n)] ++ (bokutShiaoRelation i' i j).lm (heckeOrder n) ++ [])
      = 1 := by
    rw [hlm, show ([(⟨j₀'⟩ : HeckeGen n)] ++ (((⟨i⟩ : HeckeGen n) :: A')
        ++ ((⟨j₀⟩ : HeckeGen n) :: (B ++ [(⟨i⟩ : HeckeGen n)]))) ++ [])
      = (⟨j₀'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n) :: (A' ++ ((⟨j₀⟩ : HeckeGen n)
          :: (B ++ [(⟨i⟩ : HeckeGen n)])))) by simp]
    simp [T4, AlgElement.ofTerms_coeff, hne]
  refine ⟨bokutShiaoRelation i' i j, bokutShiaoRelation_mem hn hp hi hj,
    [(⟨j₀'⟩ : HeckeGen n)], [], 1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, bokutShiaoRelation_lc hi hj]; ring
  · intro m
    show _ = _ - (1 : ℝ) * (AlgElement.contextMul [(⟨j₀'⟩ : HeckeGen n)]
      (bokutShiaoRelation i' i j).relation []).coeff m
    rw [AlgElement.contextMul_coeff_congr [(⟨j₀'⟩ : HeckeGen n)] [] hrel m]
    simp only [T4, AlgElement.zero, AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append, List.append_nil, List.cons_append,
      AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

end

/-- **Five stages, to zero.** -/
theorem oc_reduces_to_zero (hp : HeckeParams) {i' i j₀' j₀ j : Fin n}
    {A' B : Monomial (HeckeGen n)} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hjj : j₀'.val + 1 = j₀.val)
    (hji : j₀.val + 1 ≤ i'.val) (hjle : j.val ≤ j₀'.val)
    (hsplit : descWord i j = ((⟨i⟩ : HeckeGen n) :: A') ++ ((⟨j₀⟩ : HeckeGen n) :: B))
    (hsplit' : descWord i' j = A' ++ ((⟨j₀⟩ : HeckeGen n) :: B))
    (hB : descWord j₀' j = B)
    (hfarA : ∀ y ∈ A', j₀'.val + 1 < y.index.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (CyclicFarCommLow.oc (bokutShiaoRelation i' i j) i j₀
        (A' ++ ((⟨j₀⟩ : HeckeGen n) :: B))
        (by rw [bokutShiaoRelation_lm hi (by omega), bsWord₁, hsplit]; rfl)
        (by omega)).spoly nf ∧ nf.isZero := by
  have hii' : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  have hjq : (⟨j₀'⟩ : HeckeGen n) ≠ ⟨i'⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  have hqi : (⟨i'⟩ : HeckeGen n) ≠ ⟨j₀'⟩ := fun h => hjq h.symm
  have hfar1 : ∀ y ∈ (⟨i⟩ : HeckeGen n) :: A', j₀'.val + 1 < y.index.val := by
    intro y hy
    rcases List.mem_cons.mp hy with rfl | hy
    · show j₀'.val + 1 < i.val
      omega
    · exact hfarA y hy
  have hfar2 : ∀ y ∈ [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ A',
      j₀'.val + 1 < y.index.val := by
    intro y hy
    rcases List.mem_append.mp hy with hy | hy
    · simp only [List.mem_cons, List.not_mem_nil, or_false] at hy
      rcases hy with rfl | rfl
      · show j₀'.val + 1 < i'.val
        omega
      · show j₀'.val + 1 < i.val
        omega
    · exact hfarA y hy
  -- stage 2: `σ_{j₀'}` crosses the upper run in the first term
  have ph1 : MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T1 i' i j₀' j₀ A' B) (T2 i' i j₀' j₀ A' B) :=
    farComm_transport_left hn hp j₀' 1 one_ne_zero []
      [(((⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n)
          :: (A' ++ ((⟨j₀⟩ : HeckeGen n) :: B)))) ++ [(⟨j₀⟩ : HeckeGen n)], (-1 : ℝ))]
      ((⟨i⟩ : HeckeGen n) :: A') [] ((⟨j₀⟩ : HeckeGen n) :: (B ++ [(⟨i⟩ : HeckeGen n)]))
      hfar1
      (by
        intro u v huv r hr
        simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
          List.not_mem_nil, or_false] at hr
        subst hr
        cases u with
        | nil =>
          simp only [List.nil_append, List.cons_append]
          intro hcon
          injection hcon with h1 _
          exact hqi h1
        | cons a u' =>
          rw [List.cons_append] at huv
          injection huv with ha _
          subst ha
          simp only [List.cons_append]
          intro hcon
          injection hcon with h1 _
          exact hii' h1)
  -- stage 4: and in the second term, across `σᵢ₋₁ σᵢ A'`
  have ph2 : MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T3 i' i j₀' j₀ A' B) (T4 i' i j₀' j₀ A' B) :=
    farComm_transport_left hn hp j₀' (-1) (by norm_num)
      [((⟨j₀'⟩ : HeckeGen n) :: (((⟨i⟩ : HeckeGen n) :: A')
          ++ ((⟨j₀⟩ : HeckeGen n) :: (B ++ [(⟨i⟩ : HeckeGen n)]))), (1 : ℝ))] []
      ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ A') [] ((⟨j₀⟩ : HeckeGen n) :: B)
      hfar2
      (by
        intro u v huv r hr
        simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
          List.not_mem_nil, or_false] at hr
        subst hr
        cases u with
        | nil =>
          simp only [List.nil_append] at huv
          subst huv
          simp only [List.nil_append, List.cons_append]
          intro hcon
          injection hcon with _ h2
          injection h2 with h3 _
          exact hii' h3.symm
        | cons a u' =>
          simp only [List.cons_append, List.nil_append] at huv
          injection huv with ha _
          subst ha
          simp only [List.nil_append, List.cons_append]
          intro hcon
          injection hcon with h1 _
          exact hjq h1)
  refine reducesToZero_congr ⟨AlgElement.zero,
    ⟨((((MultiStepReduction.refl _).step
        (chainStep1 hp hn hjj hjle hii' hB)).trans ph1).step
        (chainStep3 hp hn hjj hjle hjq hB)).trans ph2
      |>.step (chainStep5 hp hn hi (by omega) hii' hsplit hsplit'),
      isNormalForm_of_isZero AlgElement.isZero_zero⟩, AlgElement.isZero_zero⟩ ?_
  intro w
  refine CyclicFarCommLow.oc_spoly_coeff (bokutShiaoRelation i' i j) i j₀ ?_
    (by rw [bokutShiaoRelation_lm hi (by omega), bsWord₁, hsplit]; rfl)
    (bokutShiaoRelation_lc hi (by omega)) (by omega) w
  intro w'
  show (AlgElement.ofTerms [(bsWord₁ i j, (1 : ℝ)), (bsWord₂ i' i j, -1)]).coeff w' = _
  rw [bsWord₁, hsplit, bsWord₂, hsplit']
  rfl

/-- **The family, at the indices the enumeration presents it with.** `jup` names
`j₀ + 1`; the two splits of the descending run come from `descWord_split`, and
`A'` is the piece above `j₀`. -/
theorem resolves (hp : HeckeParams) {i' i j₀' j₀ jup j : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hjj : j₀'.val + 1 = j₀.val) (hjp : j₀.val + 1 = jup.val)
    (hji : jup.val ≤ i'.val) (hjle : j.val ≤ j₀'.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (CyclicFarCommLow.oc (bokutShiaoRelation i' i j) i j₀
        (descWord i' jup ++ ((⟨j₀⟩ : HeckeGen n) :: descWord j₀' j))
        (by rw [bokutShiaoRelation_lm hi (by omega), bsWord₁,
              descWord_split hjp (by omega) (by omega), descWord_cons hjj hjle,
              descWord_cons hi (by omega)]; rfl)
        (by omega)).spoly nf ∧ nf.isZero := by
  refine oc_reduces_to_zero hp hn hi hjj (by omega) hjle ?_ ?_ rfl ?_
  · rw [descWord_split hjp (by omega) (by omega), descWord_cons hjj hjle,
      descWord_cons hi (by omega)]
  · rw [descWord_split hjp (by omega) (by omega), descWord_cons hjj hjle]
  · intro y hy
    have := descWord_index_ge hy
    omega

end CyclicFarCommInner

/-! ## §4x  Bokut–Shiao against the braid word — the first `B × B` sub-family

`B × B` is the last shape, seventeen compositions at `n = 4` with chains of nine
to twenty-five steps. It is not one family: writing `a = i − j₁` and
`b = i − j₂` for the two depths, the engine's chain lengths depend only on
`(a, b)` and split it up as

    (1,1) → 8    §4r, the braid self-overlap
    (a,1) → 9    this section
    (1,2) → 10       (1,3) → 12
    (a,2) → 15       (2,3) → 19       (3,3) → 25

This section is the column `b = 1`, i.e. `j₂ = i − 1`, where the second rule
leads on the braid word `σᵢσᵢ₋₁σᵢ` — six of the seventeen, and the one whose
chain is uniform in `a`.

**The S-polynomial, in the shape that makes the chain visible.** Both rules lead
on a word ending in `σᵢ`, they overlap in that letter, and the ambient word
cancels. With `E = descWord i−1 j₁`, so that `descWord i j₁ = σᵢ :: E`:

    spoly = c₂ · ( σᵢ E σᵢ₋₁ σᵢ σᵢ₋₁  −  σᵢ₋₁ σᵢ E σᵢ₋₁ σᵢ )

`c₂` is the second rule's leading coefficient — `1` for Bokut–Shiao at
`j = i − 1`, `−1` for Yang–Baxter, the two rules §4j puts on that word. The first
rule cannot be Yang–Baxter: `j₁ ≤ i − 2` here, so it leads on a longer word.

**Both terms reduce to `σᵢ₋₂ σᵢ₋₁ σᵢ₋₂ σᵢ E`**, and every step is one of three
rules — Bokut–Shiao at `(i−2, i−1, j₁)`, far-commutation `σᵢσᵢ₋₂`, and the outer
rule itself:

| | term 1 | | term 2 |
|---|---|---|---|
| 1 | `BS(i−2,i−1,j₁)` at `(σᵢ ∣ σᵢσᵢ₋₁)` | 6 | `BS(i−2,i−1,j₁)` at `(σᵢ₋₁σᵢ ∣ σᵢ)` |
| 2 | `σᵢσᵢ₋₂` at `(ε ∣ E σᵢ σᵢ₋₁)` | 7 | `σᵢσᵢ₋₂` at `(σᵢ₋₁ ∣ E σᵢ)` |
| 3 | `BS(i−1,i,j₁)` at `(σᵢ₋₂ ∣ σᵢ₋₁)` | 8 | `BS(i−1,i,j₁)` at `(σᵢ₋₁σᵢ₋₂ ∣ ε)` |
| 4 | `BS(i−2,i−1,j₁)` at `(σᵢ₋₂σᵢ₋₁σᵢ ∣ ε)` | 9 | `BS(i−2,i−1,i−2)` at `(ε ∣ σᵢ E)` |
| 5 | `σᵢσᵢ₋₂` at `(σᵢ₋₂σᵢ₋₁ ∣ E)` | | |

Five steps for the first term, four for the second, nine in all — independent of
`a`, which is why this column is flat where the others grow. The two branches
differ only in their last step: term 1 finishes by commuting `σᵢ` past `σᵢ₋₂`,
term 2 by straightening the braid `σᵢ₋₁σᵢ₋₂σᵢ₋₁`.

**Every intermediate is told apart by its first letter.** The nine stages begin
with `σᵢ`, `σᵢ`, `σᵢ₋₂`, `σᵢ₋₂`, `σᵢ₋₂` and `σᵢ₋₁`, `σᵢ₋₁`, `σᵢ₋₁`, `σᵢ₋₁`
against a passenger beginning with `σᵢ₋₁` and then `σᵢ₋₂` — so no length count
and no word-uniqueness argument is needed anywhere in the section.

`monicStep` is the other thing that keeps this short: every rule the chain
applies is monic, every stage is two terms, and the step is always "rewrite the
first term, carry the second" — so one lemma discharges all nine. -/

/-- **One step of a two-term chain, by a monic two-word rule.** The stage words
are arbitrary and tied to the rule's by equations, so consecutive steps compose
without the decompositions having to agree syntactically. -/
theorem monicStep {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    (r : ReductionRule (HeckeGen n) ℝ)
    (hr : r ∈ (heckeCompletedRewritingSystem n hn hp).rules)
    {L R : Monomial (HeckeGen n)}
    (hrel : ∀ w, r.relation.coeff w
      = (AlgElement.ofTerms [(L, (1 : ℝ)), (R, -1)]).coeff w)
    (hlm : r.lm (heckeOrder n) = L) (hLR : R ≠ L)
    (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (a b W W' : Monomial (HeckeGen n)) (c : ℝ) (hc : c ≠ 0)
    (hW : W = a ++ L ++ b) (hW' : W' = a ++ R ++ b)
    (hne : ∀ q ∈ (L₁ ++ L₂).map Prod.fst, q ≠ W) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++ (W, c) :: L₂))
      (AlgElement.ofTerms (L₁ ++ (W', c) :: L₂)) := by
  have hlc : r.lc (heckeOrder n) = 1 := by
    show r.relation.coeff (r.lm (heckeOrder n)) = 1
    rw [hlm, hrel]
    simp [AlgElement.ofTerms_coeff, hLR]
  have hv : (AlgElement.ofTerms (L₁ ++ (W, c) :: L₂)).coeff
      (a ++ r.lm (heckeOrder n) ++ b) = c := by
    rw [hlm, ← hW]
    exact ofTerms_coeff_mid L₁ L₂ W c hne
  refine ⟨r, hr, a, b, c, ?_, ?_, ?_⟩
  · rw [hv]; exact hc
  · rw [hv, hlc]; ring
  · intro m
    show _ = _ - c * (AlgElement.contextMul a r.relation b).coeff m
    rw [AlgElement.contextMul_coeff_congr a b hrel m,
      AlgElement.contextMul_ofTerms_coeff]
    subst hW
    subst hW'
    simp only [List.map_cons, List.map_nil, AlgElement.ofTerms_coeff,
      List.filter_append, List.filter_cons, List.filter_nil,
      List.map_append, List.sum_append, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-! ### §4ah  The same, for the quadratic rule

`monicStep` above asks the rule to be monic with **two** words, `L − R`, so that
a step is a substitution: one term in, one term out. The quadratic rule
`σ_z² − h·σ_z − 1` has **three**, so a step by it is not a substitution — the
term `(a σ_z² b, c)` becomes the *pair* `(a σ_z b, h·c)` and `(a b, c)`. That is
the whole reason `monicStep` does not reach the corner's two quadratic steps,
and the eight-step chain of §4y writes five of its steps out by hand.

`quadStep` is the missing companion. It is `monicStep`'s statement with the
one-term output replaced by the two-term one, and its proof is the same shape:
the coefficient at the targeted word is read off by `ofTerms_coeff_mid`, and the
`CoeffEq` obligation is a `split_ifs <;> ring` once both sides are unfolded.

**One lemma covers both occurrences.** `hecke_quad_pair_shape.py` measured the
two quadratic steps of the `a ≤ b` regime and found they apply the *same* rule,
`heckeRelation j₁`, after the *same* Yang–Baxter step, differing only in their
contexts — the second has `σ_{i−2}` prepended on the left and lacks a trailing
`σ_i` on the right. Since the contexts here are parameters, that difference
costs nothing: the assembly supplies them and the step lemma never sees it. -/

/-- **One step of a chain, by the quadratic rule.** Unlike `monicStep` the
output has one more term than the input: the quadratic rule has three words, so
the targeted term is replaced by two, with coefficients `c·(q − q⁻¹)` and `c`.

The contexts `a`, `b` and the surrounding terms `L₁`, `L₂` are arbitrary, and
`W` is tied to the rule's leading word by an equation rather than being it on
the nose, so consecutive steps compose without their decompositions having to
agree syntactically — the same reason `monicStep` is stated that way. -/
theorem quadStep {n : ℕ} (hn : 0 < n) (hp : HeckeParams) (z : Fin n)
    (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (a b W : Monomial (HeckeGen n)) (c : ℝ) (hc : c ≠ 0)
    (hW : W = a ++ [(⟨z⟩ : HeckeGen n), ⟨z⟩] ++ b)
    (hne : ∀ w ∈ (L₁ ++ L₂).map Prod.fst, w ≠ W) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++ (W, c) :: L₂))
      (AlgElement.ofTerms (L₁ ++ (a ++ [(⟨z⟩ : HeckeGen n)] ++ b,
          c * (hp.q - hp.q⁻¹)) :: (a ++ b, c) :: L₂)) := by
  have hv : (AlgElement.ofTerms (L₁ ++ (W, c) :: L₂)).coeff
      (a ++ (heckeRelation z hp).lm (heckeOrder n) ++ b) = c := by
    rw [heckeRelation_lm, ← hW]
    exact ofTerms_coeff_mid L₁ L₂ W c hne
  refine ⟨heckeRelation z hp, heckeRelation_mem hn hp z, a, b, c, ?_, ?_, ?_⟩
  · rw [hv]; exact hc
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - c * (AlgElement.contextMul a (heckeRelation z hp).relation b).coeff m
    subst hW
    simp only [heckeRelation, AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.append_nil,
      AlgElement.ofTerms_coeff, List.filter_append,
      List.filter_cons, List.filter_nil, List.map_append, List.sum_append,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

namespace BokutShiaoBraid

variable {n : ℕ}

/-- The composition of `bokutShiaoRelation i' i j₁` with a rule leading on the
braid word `σᵢσᵢ₋₁σᵢ`, overlapping in the trailing `σᵢ`. -/
noncomputable def oc (r₂ : ReductionRule (HeckeGen n) ℝ) {i' i j₁ : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j₁.val ≤ i'.val)
    (hlm₂ : r₂.lm (heckeOrder n) = BraidSelfOverlap.wHi i' i) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := bokutShiaoRelation i' i j₁
  rule₂ := r₂
  left := descWord i j₁
  overlap := [⟨i⟩]
  right := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
  lm₁_decomp := by rw [bokutShiaoRelation_lm hi hj]; rfl
  lm₂_decomp := hlm₂
  overlap_nonempty := by simp

/-! ### The nine stages

`A₀ … A₅` are the first term as it reduces, `B₀ … B₃` the second; the chain runs
`A₀ → A₅` with `B₀` a passenger, then `B₀ → B₃` with `A₅` a passenger, and `B₃`
lands on `A₅`. -/

/-- Stage words of the first term. -/
def A0 (i' i : Fin n) (E : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i⟩ : HeckeGen n) :: (E ++ [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)])

/-- After the first Bokut–Shiao application. -/
def A1 (i'' i' i : Fin n) (E : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i⟩ : HeckeGen n) :: ((⟨i''⟩ : HeckeGen n)
    :: (E ++ [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]))

/-- After commuting `σᵢ` past `σᵢ₋₂`. -/
def A2 (i'' i' i : Fin n) (E : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i''⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n)
    :: (E ++ [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]))

/-- After the outer rule. -/
def A3 (i'' i' i : Fin n) (E : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i''⟩ : HeckeGen n) :: ((⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n)
    :: (E ++ [(⟨i'⟩ : HeckeGen n)])))

/-- After the second Bokut–Shiao application. -/
def A4 (i'' i' i : Fin n) (E : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i''⟩ : HeckeGen n) :: ((⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n)
    :: ((⟨i''⟩ : HeckeGen n) :: E)))

/-- **The common endpoint of both branches.** -/
def A5 (i'' i' i : Fin n) (E : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i''⟩ : HeckeGen n) :: ((⟨i'⟩ : HeckeGen n) :: ((⟨i''⟩ : HeckeGen n)
    :: ((⟨i⟩ : HeckeGen n) :: E)))

/-- Stage words of the second term. -/
def B0 (i' i : Fin n) (E : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n)
    :: (E ++ [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]))

/-- After the first Bokut–Shiao application. -/
def B1 (i'' i' i : Fin n) (E : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n) :: ((⟨i''⟩ : HeckeGen n)
    :: (E ++ [(⟨i⟩ : HeckeGen n)])))

/-- After commuting `σᵢ` past `σᵢ₋₂`. -/
def B2 (i'' i' i : Fin n) (E : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: ((⟨i''⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n)
    :: (E ++ [(⟨i⟩ : HeckeGen n)])))

/-- After the outer rule; one braid straightening from `A₅`. -/
def B3 (i'' i' i : Fin n) (E : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: ((⟨i''⟩ : HeckeGen n) :: ((⟨i'⟩ : HeckeGen n)
    :: ((⟨i⟩ : HeckeGen n) :: E)))

/-- Stage `k` of the chain: the live term, the passenger, and the coefficient. -/
noncomputable def stage (W P : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(W, c), (P, -c)]

section

variable {i'' i' i j₁ : Fin n} {E : Monomial (HeckeGen n)}

/-- The lower Bokut–Shiao rule, in the two-word form `monicStep` wants. -/
theorem lower_hrel (hi'' : i''.val + 1 = i'.val) (hj : j₁.val ≤ i''.val)
    (hE : descWord i' j₁ = E) (w : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i'' i' j₁).relation.coeff w
      = (AlgElement.ofTerms
          [(E ++ [(⟨i'⟩ : HeckeGen n)], (1 : ℝ)), ((⟨i''⟩ : HeckeGen n) :: E, -1)]).coeff w := by
  show (AlgElement.ofTerms [(bsWord₁ i' j₁, (1 : ℝ)), (bsWord₂ i'' i' j₁, -1)]).coeff w = _
  rw [bsWord₁, hE, bsWord₂, ← hE, descWord_cons hi'' hj]

theorem lower_hlm (hi'' : i''.val + 1 = i'.val) (hj : j₁.val ≤ i''.val)
    (hE : descWord i' j₁ = E) :
    (bokutShiaoRelation i'' i' j₁).lm (heckeOrder n) = E ++ [(⟨i'⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm hi'' hj, bsWord₁, hE]

/-- The outer Bokut–Shiao rule, in the same form. -/
theorem outer_hrel (hi : i'.val + 1 = i.val) (hj : j₁.val ≤ i'.val)
    (hE : descWord i' j₁ = E) (w : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i' i j₁).relation.coeff w
      = (AlgElement.ofTerms
          [((⟨i⟩ : HeckeGen n) :: (E ++ [(⟨i⟩ : HeckeGen n)]), (1 : ℝ)),
           ((⟨i'⟩ : HeckeGen n) :: ((⟨i⟩ : HeckeGen n) :: E), -1)]).coeff w := by
  show (AlgElement.ofTerms [(bsWord₁ i j₁, (1 : ℝ)), (bsWord₂ i' i j₁, -1)]).coeff w = _
  rw [bsWord₁, descWord_cons hi hj, hE, bsWord₂, hE]
  rfl

theorem outer_hlm (hi : i'.val + 1 = i.val) (hj : j₁.val ≤ i'.val)
    (hE : descWord i' j₁ = E) :
    (bokutShiaoRelation i' i j₁).lm (heckeOrder n)
      = (⟨i⟩ : HeckeGen n) :: (E ++ [(⟨i⟩ : HeckeGen n)]) := by
  rw [bokutShiaoRelation_lm hi hj, bsWord₁, descWord_cons hi hj, hE]
  rfl

/-- Far-commutation between the top generator and the one two below it. -/
theorem far_hrel (i'' i : Fin n) (w : Monomial (HeckeGen n)) :
    (farCommRelation i i'').relation.coeff w
      = (AlgElement.ofTerms
          [([(⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)], -1)]).coeff w := rfl

/-- The braid rule at the lower level, which is the Bokut–Shiao rule at
`j = i − 2`. -/
theorem braid_hrel (hi'' : i''.val + 1 = i'.val) (w : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i'' i' i'').relation.coeff w
      = (AlgElement.ofTerms
          [([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)], -1)]).coeff w := by
  show (AlgElement.ofTerms [(bsWord₁ i' i'', (1 : ℝ)), (bsWord₂ i'' i' i'', -1)]).coeff w = _
  rw [bsWord₁_at_pred hi'', bsWord₂_at_pred i'' i']

theorem braid_hlm (hi'' : i''.val + 1 = i'.val) :
    (bokutShiaoRelation i'' i' i'').lm (heckeOrder n)
      = [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm hi'' (le_refl _), bsWord₁_at_pred hi'']

end

/-! ### The chain

Nine applications of `monicStep`. Steps 1–5 move the first term with the second
as passenger (`L₁ = []`), steps 6–9 the other way round (`L₂ = []`); the
list-position-general form of `monicStep` is what lets one lemma do both. -/

section

variable (hp : HeckeParams) {i'' i' i j₁ : Fin n} {E F : Monomial (HeckeGen n)} {c : ℝ}

/-- The three generators in play are pairwise distinct, which is the only
word-distinctness the whole section needs. -/
theorem gen_ne (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    (⟨i⟩ : HeckeGen n) ≠ ⟨i'⟩ ∧ (⟨i⟩ : HeckeGen n) ≠ ⟨i''⟩
      ∧ (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩ := by
  refine ⟨?_, ?_, ?_⟩ <;>
    · intro hcon
      have := congrArg HeckeGen.rank hcon
      simp only [HeckeGen.rank] at this
      omega

theorem chain1 (hn : 0 < n) (hi'' : i''.val + 1 = i'.val) (hj : j₁.val ≤ i''.val)
    (hE : descWord i' j₁ = E) (hEF : E = (⟨i'⟩ : HeckeGen n) :: F)
    (hne : (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩) (hni : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩)
    (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (stage (A0 i' i E) (B0 i' i E) c) (stage (A1 i'' i' i E) (B0 i' i E) c) :=
  monicStep hn hp _ (bokutShiaoRelation_mem hn hp hi'' hj) (lower_hrel hi'' hj hE)
    (lower_hlm hi'' hj hE)
    (by rw [hEF]; intro hcon; injection hcon with h1 _; exact hne h1.symm)
    [] [(B0 i' i E, -c)] [(⟨i⟩ : HeckeGen n)]
    [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] _ _ c hc
    (by simp [A0]) (by simp [A1])
    (by
      intro q hq
      simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      simp only [A0, B0]
      intro hcon
      injection hcon with h1 _
      exact hni h1)

theorem chain2 (hn : 0 < n) (hi'' : i''.val + 1 = i'.val) (hij : i''.val + 1 < i.val)
    (hne : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩) (hnc : (⟨i''⟩ : HeckeGen n) ≠ ⟨i⟩) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (stage (A1 i'' i' i E) (B0 i' i E) c) (stage (A2 i'' i' i E) (B0 i' i E) c) :=
  monicStep hn hp _ (farCommRelation_mem hn hp hij) (far_hrel i'' i)
    (farCommRelation_lm i i'' (by omega))
    (by intro hcon; injection hcon with h1 _; exact hnc h1)
    [] [(B0 i' i E, -c)] [] (E ++ [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]) _ _ c hc
    (by simp [A1]) (by simp [A2])
    (by
      intro q hq
      simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      simp only [A1, B0]
      intro hcon
      injection hcon with h1 _
      exact hne h1)

theorem chain3 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hj : j₁.val ≤ i'.val)
    (hE : descWord i' j₁ = E) (hne : (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩)
    (hni : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (stage (A2 i'' i' i E) (B0 i' i E) c) (stage (A3 i'' i' i E) (B0 i' i E) c) :=
  monicStep hn hp _ (bokutShiaoRelation_mem hn hp hi hj) (outer_hrel hi hj hE)
    (outer_hlm hi hj hE)
    (by intro hcon; injection hcon with h1 _; exact hni h1)
    [] [(B0 i' i E, -c)] [(⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n)] _ _ c hc
    (by simp [A2]) (by simp [A3])
    (by
      intro q hq
      simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      simp only [A2, B0]
      intro hcon
      injection hcon with h1 _
      exact hne h1)

theorem chain4 (hn : 0 < n) (hi'' : i''.val + 1 = i'.val) (hj : j₁.val ≤ i''.val)
    (hE : descWord i' j₁ = E) (hEF : E = (⟨i'⟩ : HeckeGen n) :: F)
    (hne : (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (stage (A3 i'' i' i E) (B0 i' i E) c) (stage (A4 i'' i' i E) (B0 i' i E) c) :=
  monicStep hn hp _ (bokutShiaoRelation_mem hn hp hi'' hj) (lower_hrel hi'' hj hE)
    (lower_hlm hi'' hj hE)
    (by rw [hEF]; intro hcon; injection hcon with h1 _; exact hne h1.symm)
    [] [(B0 i' i E, -c)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] [] _ _ c hc
    (by simp [A3]) (by simp [A4])
    (by
      intro q hq
      simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      simp only [A3, B0]
      intro hcon
      injection hcon with h1 _
      exact hne h1)

theorem chain5 (hn : 0 < n) (hij : i''.val + 1 < i.val)
    (hne : (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩) (hnc : (⟨i''⟩ : HeckeGen n) ≠ ⟨i⟩) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (stage (A4 i'' i' i E) (B0 i' i E) c) (stage (A5 i'' i' i E) (B0 i' i E) c) :=
  monicStep hn hp _ (farCommRelation_mem hn hp hij) (far_hrel i'' i)
    (farCommRelation_lm i i'' (by omega))
    (by intro hcon; injection hcon with h1 _; exact hnc h1)
    [] [(B0 i' i E, -c)] [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] E _ _ c hc
    (by simp [A4]) (by simp [A5])
    (by
      intro q hq
      simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      simp only [A4, B0]
      intro hcon
      injection hcon with h1 _
      exact hne h1)

theorem chain6 (hn : 0 < n) (hi'' : i''.val + 1 = i'.val) (hj : j₁.val ≤ i''.val)
    (hE : descWord i' j₁ = E) (hEF : E = (⟨i'⟩ : HeckeGen n) :: F)
    (hne : (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (stage (A5 i'' i' i E) (B0 i' i E) c) (stage (A5 i'' i' i E) (B1 i'' i' i E) c) :=
  monicStep hn hp _ (bokutShiaoRelation_mem hn hp hi'' hj) (lower_hrel hi'' hj hE)
    (lower_hlm hi'' hj hE)
    (by rw [hEF]; intro hcon; injection hcon with h1 _; exact hne h1.symm)
    [(A5 i'' i' i E, c)] [] [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
    [(⟨i⟩ : HeckeGen n)] _ _ (-c) (neg_ne_zero.mpr hc)
    (by simp [B0]) (by simp [B1])
    (by
      intro q hq
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      simp only [A5, B0]
      intro hcon
      injection hcon with h1 _
      exact hne h1.symm)

theorem chain7 (hn : 0 < n) (hij : i''.val + 1 < i.val)
    (hne : (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩) (hnc : (⟨i''⟩ : HeckeGen n) ≠ ⟨i⟩) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (stage (A5 i'' i' i E) (B1 i'' i' i E) c) (stage (A5 i'' i' i E) (B2 i'' i' i E) c) :=
  monicStep hn hp _ (farCommRelation_mem hn hp hij) (far_hrel i'' i)
    (farCommRelation_lm i i'' (by omega))
    (by intro hcon; injection hcon with h1 _; exact hnc h1)
    [(A5 i'' i' i E, c)] [] [(⟨i'⟩ : HeckeGen n)] (E ++ [(⟨i⟩ : HeckeGen n)]) _ _ (-c)
    (neg_ne_zero.mpr hc)
    (by simp [B1]) (by simp [B2])
    (by
      intro q hq
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      simp only [A5, B1]
      intro hcon
      injection hcon with h1 _
      exact hne h1.symm)

theorem chain8 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hj : j₁.val ≤ i'.val)
    (hE : descWord i' j₁ = E) (hne : (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩)
    (hni : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (stage (A5 i'' i' i E) (B2 i'' i' i E) c) (stage (A5 i'' i' i E) (B3 i'' i' i E) c) :=
  monicStep hn hp _ (bokutShiaoRelation_mem hn hp hi hj) (outer_hrel hi hj hE)
    (outer_hlm hi hj hE)
    (by intro hcon; injection hcon with h1 _; exact hni h1)
    [(A5 i'' i' i E, c)] [] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [] _ _ (-c)
    (neg_ne_zero.mpr hc)
    (by simp [B2]) (by simp [B3])
    (by
      intro q hq
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      simp only [A5, B2]
      intro hcon
      injection hcon with h1 _
      exact hne h1.symm)

theorem chain9 (hn : 0 < n) (hi'' : i''.val + 1 = i'.val)
    (hne : (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (stage (A5 i'' i' i E) (B3 i'' i' i E) c) (stage (A5 i'' i' i E) (A5 i'' i' i E) c) :=
  monicStep hn hp _ (bokutShiaoRelation_mem hn hp hi'' (le_refl _)) (braid_hrel hi'')
    (braid_hlm hi'')
    (by intro hcon; injection hcon with h1 _; exact hne h1.symm)
    [(A5 i'' i' i E, c)] [] [] ((⟨i⟩ : HeckeGen n) :: E) _ _ (-c) (neg_ne_zero.mpr hc)
    (by simp [B3]) (by simp [A5])
    (by
      intro q hq
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      simp only [A5, B3]
      intro hcon
      injection hcon with h1 _
      exact hne h1.symm)

end

/-- The chain's endpoint is coefficientwise zero: the same word with opposite
coefficients. -/
theorem stage_self_isZero (W : Monomial (HeckeGen n)) (c : ℝ) :
    (stage W W c).isZero := by
  intro m
  simp only [stage, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
  ring

/-- **The S-polynomial**, in the two-term shape the chain starts from. -/
theorem oc_spoly_coeff (r₂ : ReductionRule (HeckeGen n) ℝ) {i' i j₁ : Fin n}
    {E : Monomial (HeckeGen n)} {c₂ : ℝ}
    (hi : i'.val + 1 = i.val) (hj : j₁.val ≤ i'.val)
    (hlm₂ : r₂.lm (heckeOrder n) = BraidSelfOverlap.wHi i' i)
    (hlc₂ : r₂.lc (heckeOrder n) = c₂)
    (hrel₂ : ∀ w, r₂.relation.coeff w
      = (AlgElement.ofTerms
          [(BraidSelfOverlap.wHi i' i, c₂), (BraidSelfOverlap.wLo i' i, -c₂)]).coeff w)
    (hE : descWord i' j₁ = E) (m : Monomial (HeckeGen n)) :
    (oc r₂ hi hj hlm₂).spoly.coeff m = (stage (A0 i' i E) (B0 i' i E) c₂).coeff m := by
  show r₂.lc (heckeOrder n)
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i j₁).relation
          [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]).coeff m
    - (bokutShiaoRelation i' i j₁).lc (heckeOrder n)
      * (AlgElement.contextMul (descWord i j₁) r₂.relation []).coeff m
    = _
  rw [hlc₂, bokutShiaoRelation_lc hi hj, one_mul,
    AlgElement.contextMul_coeff_congr [] [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
      (outer_hrel hi hj hE) m,
    AlgElement.contextMul_coeff_congr (descWord i j₁) [] hrel₂ m,
    descWord_cons hi hj, hE]
  simp only [stage, A0, B0, BraidSelfOverlap.wHi, BraidSelfOverlap.wLo,
    AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
    List.append_nil, List.cons_append, List.append_assoc, AlgElement.ofTerms_coeff,
    List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Nine steps, to zero.** -/
theorem oc_reduces_to_zero (hp : HeckeParams) (r₂ : ReductionRule (HeckeGen n) ℝ)
    {i'' i' i j₁ : Fin n} {c₂ : ℝ} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) (hj : j₁.val ≤ i''.val)
    (hlm₂ : r₂.lm (heckeOrder n) = BraidSelfOverlap.wHi i' i)
    (hlc₂ : r₂.lc (heckeOrder n) = c₂)
    (hrel₂ : ∀ w, r₂.relation.coeff w
      = (AlgElement.ofTerms
          [(BraidSelfOverlap.wHi i' i, c₂), (BraidSelfOverlap.wLo i' i, -c₂)]).coeff w)
    (hc₂ : c₂ ≠ 0) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc r₂ (j₁ := j₁) hi (by omega) hlm₂).spoly nf ∧ nf.isZero := by
  obtain ⟨hii', hii'', hi'i''⟩ := gen_ne (i := i) (i' := i') (i'' := i'') hi hi''
  have hE : descWord i' j₁ = descWord i' j₁ := rfl
  have hEF : descWord i' j₁ = (⟨i'⟩ : HeckeGen n) :: descWord i'' j₁ :=
    descWord_cons hi'' hj
  have hij : i''.val + 1 < i.val := by omega
  have hj' : j₁.val ≤ i'.val := by omega
  refine reducesToZero_congr ⟨stage (A5 i'' i' i (descWord i' j₁))
      (A5 i'' i' i (descWord i' j₁)) c₂,
    ⟨(MultiStepReduction.refl _)
      |>.step (chain1 hp hn hi'' hj hE hEF hi'i'' hii'.symm hc₂)
      |>.step (chain2 hp hn hi'' hij hii'.symm hii''.symm hc₂)
      |>.step (chain3 hp hn hi hj' hE hi'i'' hii'.symm hc₂)
      |>.step (chain4 hp hn hi'' hj hE hEF hi'i'' hc₂)
      |>.step (chain5 hp hn hij hi'i'' hii''.symm hc₂)
      |>.step (chain6 hp hn hi'' hj hE hEF hi'i'' hc₂)
      |>.step (chain7 hp hn hij hi'i'' hii''.symm hc₂)
      |>.step (chain8 hp hn hi hj' hE hi'i'' hii'.symm hc₂)
      |>.step (chain9 hp hn hi'' hi'i'' hc₂),
      isNormalForm_of_isZero (stage_self_isZero _ _)⟩, stage_self_isZero _ _⟩ ?_
  intro m
  exact oc_spoly_coeff r₂ hi hj' hlm₂ hlc₂ hrel₂ hE m

/-! ### The two instances

`wHi i' i` carries both `yangBaxterRelation i' i` and `bokutShiaoRelation i' i i'`
(§4j), so the composition exists with either as `rule₂` — the six `n = 4` members
of this family. `rule₁` cannot double: `j₁ ≤ i − 2` puts its leading monomial
strictly longer than the braid word. -/

/-- **Against Yang–Baxter.** -/
theorem yangBaxter_resolves (hp : HeckeParams) {i'' i' i j₁ : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) (hj : j₁.val ≤ i''.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc (yangBaxterRelation i' i) (j₁ := j₁) hi (by omega)
        (BraidSelfOverlap.yb_hlm i' i hi)).spoly nf ∧ nf.isZero :=
  oc_reduces_to_zero hp (yangBaxterRelation i' i) hn hi hi'' hj
    (BraidSelfOverlap.yb_hlm i' i hi) (DegenerateYbBs.yangBaxter_lc hi)
    (BraidSelfOverlap.yb_hrel i' i hi) (by norm_num)

/-- **Against Bokut–Shiao at `j = i − 1`.** -/
theorem bokutShiao_resolves (hp : HeckeParams) {i'' i' i j₁ : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) (hj : j₁.val ≤ i''.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc (bokutShiaoRelation i' i i') (j₁ := j₁) hi (by omega)
        (BraidSelfOverlap.bs_hlm i' i hi)).spoly nf ∧ nf.isZero :=
  oc_reduces_to_zero hp (bokutShiaoRelation i' i i') hn hi hi'' hj
    (BraidSelfOverlap.bs_hlm i' i hi) (bokutShiaoRelation_lc hi (le_refl _))
    (BraidSelfOverlap.bs_hrel i' i hi) one_ne_zero

end BokutShiaoBraid

/-! ## §4y  Preparation for the `a = 1` row of `B × B`: transport at any position

`farComm_transport` (§4t) moves a generator rightwards but only in an element
whose other term is the transport's own destination; `farComm_transport_snd` /
`_fst` (§4u) add a single bystander. The `a = 1` row of `B × B` needs it with
*two* bystanders and `h`-weighted coefficients, so here is the rightward
transport in the same `L₁ ++ (·) :: L₂` form `farComm_transport_left` (§4v) and
`monicStep` (§4x) already use — the moving term at an arbitrary position of the
term list, everything else carried untouched.

With this, all four transports in the file are instances of two lemmas
(`farComm_transport_left`, `farComm_transport_right`) at arbitrary list
positions, and the earlier special cases are only kept because they are already
used. -/

/-- **Far-commutation transport, rightwards, at any list position.** The mirror
of `farComm_transport_left_sources`: there a generator below the block moves
left, here a generator above it moves right. The induction recurses on the head
of `w` and prepends its step, the opposite end from the leftward version.

As on the left, the collision hypothesis enumerates the intermediate words by
splitting `w`, and one of those splits names the transport's own *final* word,
which the proof never needs. **On this side that split is `v = []`, not
`u = []`** — the two ends swap with the direction of travel, since here the
moving letter starts at the left of `w` and finishes at its right. Concretely
`hcol` is used at `u = []` with `v = y :: w` for the single step, which is
non-empty, and the recursion passes `v` through untouched.

The distinction matters because the bystanding term of the corner chain *is*
the transport's final word, so the unrestricted hypothesis is false exactly
where the transport is needed — the same trap §4v hit on the left, and it would
be hit again here by mirroring the wrong end. `farComm_transport_right` below is
this with the stronger hypothesis, kept because §4y's callers already supply
it. -/
theorem farComm_transport_right_sources {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    (x : Fin n)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ)) :
    ∀ (w a b : Monomial (HeckeGen n)), (∀ y ∈ w, y.index.val + 1 < x.val) →
      (∀ u v : Monomial (HeckeGen n), u ++ v = w → v ≠ [] →
          ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
            r ≠ a ++ (u ++ ((⟨x⟩ : HeckeGen n) :: (v ++ b)))) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms
          (L₁ ++ (a ++ ((⟨x⟩ : HeckeGen n) :: (w ++ b)), c) :: L₂))
        (AlgElement.ofTerms
          (L₁ ++ (a ++ (w ++ ((⟨x⟩ : HeckeGen n) :: b)), c) :: L₂)) := by
  intro w
  induction w with
  | nil => intro a b _ _; exact MultiStepReduction.refl _
  | cons y w ih =>
    intro a b hw hcol
    obtain ⟨yi⟩ := y
    have hy : yi.val + 1 < x.val := hw _ (by simp)
    have hyx : (⟨yi⟩ : HeckeGen n) ≠ ⟨x⟩ := by
      intro hcon
      have := congrArg HeckeGen.rank hcon
      simp only [HeckeGen.rank] at this
      omega
    have key := ih (a ++ [(⟨yi⟩ : HeckeGen n)]) b (fun t ht => hw t (by simp [ht]))
      (fun u v huv hv => by
        have := hcol ((⟨yi⟩ : HeckeGen n) :: u) v (by rw [List.cons_append, huv]) hv
        simpa only [List.append_assoc, List.singleton_append, List.cons_append] using this)
    simp only [List.append_assoc, List.singleton_append] at key
    show MultiStepReduction _ _ (AlgElement.ofTerms
      (L₁ ++ (a ++ ((⟨x⟩ : HeckeGen n) :: ((⟨yi⟩ : HeckeGen n) :: (w ++ b))), c) :: L₂)) _
    refine MultiStepReduction.head ?_ key
    have hv : (AlgElement.ofTerms
        (L₁ ++ (a ++ ((⟨x⟩ : HeckeGen n) :: ((⟨yi⟩ : HeckeGen n) :: (w ++ b))), c) :: L₂)).coeff
        (a ++ (farCommRelation x yi).lm (heckeOrder n) ++ (w ++ b)) = c := by
      rw [farCommRelation_lm x yi (by omega),
        show (a ++ [(⟨x⟩ : HeckeGen n), (⟨yi⟩ : HeckeGen n)] ++ (w ++ b))
          = a ++ ((⟨x⟩ : HeckeGen n) :: ((⟨yi⟩ : HeckeGen n) :: (w ++ b))) by simp]
      refine ofTerms_coeff_mid L₁ L₂ _ c (fun r hr => ?_)
      have := hcol [] ((⟨yi⟩ : HeckeGen n) :: w) rfl (by simp) r hr
      simpa only [List.nil_append, List.cons_append] using this
    refine ⟨farCommRelation x yi, farCommRelation_mem hn hp hy, a, w ++ b, c, ?_, ?_, ?_⟩
    · rw [hv]; exact hc
    · rw [hv, farCommRelation_lc x yi (by omega)]; ring
    · intro m
      show _ = _ - c
        * (AlgElement.contextMul a (farCommRelation x yi).relation (w ++ b)).coeff m
      simp only [farCommRelation, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
        List.map_nil, List.cons_append, List.nil_append, List.append_assoc,
        AlgElement.ofTerms_coeff, List.filter_append, List.filter_cons, List.filter_nil,
        List.map_append, List.sum_append, decide_eq_true_eq]
      split_ifs <;>
        simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- The rightward transport with the unrestricted collision hypothesis — every
split of `w`, including the one naming the final word. Weaker than
`farComm_transport_right_sources` and kept for §4y's callers, exactly as
`farComm_transport_left` is kept for §4v's. -/
theorem farComm_transport_right {n : ℕ} (hn : 0 < n) (hp : HeckeParams) (x : Fin n)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ)) :
    ∀ (w a b : Monomial (HeckeGen n)), (∀ y ∈ w, y.index.val + 1 < x.val) →
      (∀ u v : Monomial (HeckeGen n), u ++ v = w →
          ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
            r ≠ a ++ (u ++ ((⟨x⟩ : HeckeGen n) :: (v ++ b)))) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms
          (L₁ ++ (a ++ ((⟨x⟩ : HeckeGen n) :: (w ++ b)), c) :: L₂))
        (AlgElement.ofTerms
          (L₁ ++ (a ++ (w ++ ((⟨x⟩ : HeckeGen n) :: b)), c) :: L₂)) :=
  fun w a b hw hcol =>
    farComm_transport_right_sources hn hp x c hc L₁ L₂ w a b hw
      (fun u v huv _ => hcol u v huv)

/-! ### §4ai  A whole block transported past a run

The `a ≤ b` regime's blocks are `a` levels (or `a − 1` on the diagonal), each
one letter transported rightwards past a run of far-commutations, and
`hecke_block_transport_shape.py` measures the level lengths as
`min(b−a−1+k, b−a+2)` off the diagonal and `min(k, 2)` on it. The consequence
worth acting on is that the number of *short* levels is **fixed** — two, or one
on the diagonal — so every remaining level passes the *same* run
`descWord (j₁+1) j₂`. The block is therefore a fixed prologue followed by a
uniform loop, not a nested loop with a growing inner run.

`blockTransportRight` is that uniform part, and stating it needs no reference to
the block at all: it is "carry a whole word `X` rightwards past a whole word
`W`", by induction peeling `X` from its right end. Each peel is one
`farComm_transport_right_sources`, and the letter just moved joins `B`, which is
exactly the transition the measurement shows between consecutive levels.

**The parked-term hypothesis is `loopTwoGen`'s, and for the same reason.**
Enumerating the intermediate words here would mean splitting `X` *and* `W`
simultaneously, which is unusable in practice. But every word any step of this
induction rewrites has the form `A ++ z` — the accumulator only ever grows to
the right of `A` — so the single hypothesis "no parked term begins with `A`"
discharges every collision obligation at once. In the corner it holds because
the two terms start with different letters. -/

/-- **A whole block carried rightwards past a run, with the source-only
collision hypothesis.** `X` and `W` swap, provided every letter of `X` is at
least two above every letter of `W`, inside any context and at any position of
the term list.

The induction peels `X` from the **right**: its last letter transports across
`W` first and then joins `B`, so the recursion re-enters with `X` one shorter
and `B` one longer. Peeling from the left would not compose — the head of `X`
is separated from `W` by the rest of `X`, so no single transport applies.

`hpark` below — no other term extends `A` — is *sufficient* but not necessary,
and `hecke_prefix_head_separation.py` measures where the difference bites: at
`2a` steps of the corner's closing phase no choice of left context satisfies
`hpark`, while **every source in the chain is unique**, so the precise condition
holds throughout.

What the transport actually needs is that no other term equal a word it
*rewrites*. Peeling `X` from the right, those are exactly

    A ++ P ++ u ++ (x :: (v ++ (S ++ B)))    for  P ++ (x :: S) = X,
                                                   u ++ v = W,  v ≠ []

— one per letter of `X` and per interior split of `W`. The `v ≠ []` exclusion is
`farComm_transport_right_sources`'s own (§4ah): it drops the split naming each
transport's final word, which is produced and never rewritten. This lemma
threads that family through the recursion instead of over-approximating it. -/
theorem blockTransportRightSources {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (A W : Monomial (HeckeGen n)) :
    ∀ (X B : Monomial (HeckeGen n)),
      (∀ x ∈ X, ∀ y ∈ W, y.index.val + 1 < x.index.val) →
      (∀ (P S u v : Monomial (HeckeGen n)) (x : HeckeGen n),
          P ++ (x :: S) = X → u ++ v = W → v ≠ [] →
          ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
            r ≠ A ++ (P ++ (u ++ (x :: (v ++ (S ++ B)))))) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms (L₁ ++ (A ++ (X ++ (W ++ B)), c) :: L₂))
        (AlgElement.ofTerms (L₁ ++ (A ++ (W ++ (X ++ B)), c) :: L₂)) := by
  intro X
  induction X using List.reverseRecOn with
  | nil =>
      intro B _ _
      simp only [List.nil_append]
      exact MultiStepReduction.refl _
  | append_singleton X' xg ih =>
      intro B hfar hcol
      obtain ⟨xi⟩ := xg
      have hstep := farComm_transport_right_sources hn hp xi c hc L₁ L₂ W (A ++ X') B
        (fun y hy => hfar ⟨xi⟩ (by simp) y hy)
        (fun u v huv hv r hr => by
          have := hcol X' [] u v ⟨xi⟩ (by simp) huv hv r hr
          simpa only [List.append_assoc, List.nil_append] using this)
      have hrec := ih ((⟨xi⟩ : HeckeGen n) :: B)
        (fun x hx => hfar x (List.mem_append_left _ hx))
        (fun P S u v x hPS huv hv r hr => by
          have := hcol P (S ++ [(⟨xi⟩ : HeckeGen n)]) u v x
            (by rw [← hPS]; simp) huv hv r hr
          simpa only [List.append_assoc, List.cons_append,
            List.singleton_append] using this)
      simp only [List.append_assoc, List.cons_append] at hstep hrec ⊢
      exact MultiStepReduction.trans hstep hrec

/-- The block transport with the unrestricted hypothesis — `hpark` supplies
every case of the source family at once. Kept because §4aj's callers already
supply it, exactly as `farComm_transport_right` is kept for §4y's. -/
theorem blockTransportRight {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (A : Monomial (HeckeGen n))
    (hpark : ∀ r ∈ (L₁ ++ L₂).map Prod.fst, ∀ z : Monomial (HeckeGen n), r ≠ A ++ z)
    (W : Monomial (HeckeGen n)) :
    ∀ (X B : Monomial (HeckeGen n)),
      (∀ x ∈ X, ∀ y ∈ W, y.index.val + 1 < x.index.val) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms (L₁ ++ (A ++ (X ++ (W ++ B)), c) :: L₂))
        (AlgElement.ofTerms (L₁ ++ (A ++ (W ++ (X ++ B)), c) :: L₂)) :=
  fun X B hfar =>
    blockTransportRightSources hn hp c hc L₁ L₂ A W X B hfar
      (fun _ _ _ _ _ _ _ _ r hr => hpark r hr _)

/-! ### §4aj  The whole block, in three steps

With `blockTransportRight` in hand the block closes. The per-level blueprint —
measured over 102 levels in `hecke_block_transport_shape.py`, uniform on and off
the diagonal — says the level with high letter `σ_h` passes
`descWord (min(h−2, j₁+1)) j₂` and carries `descWord (h−1) (j₁+1) ++ [σ_i]` on
its right. Only two levels sit below the cap, so the block is

    h = j₁+1   one transport across `descWord (j₁−1) j₂`
    h = j₁+2   one transport across `descWord j₁ j₂`
    h ≥ j₁+3   one `blockTransportRight`, `X = descWord i (j₁+3)`

and the two short levels need no lemma of their own — they are
`farComm_transport_right_sources` applications, with the blueprint supplying
their arguments.

**What makes the three compose is the left contexts, and they are forced.**
Writing `A` for the block transport's context, the earlier steps must run at

    A₂ = A ++ descWord i (j₁+3) ++ [σ_{j₁+1}]
    A₁ = A₂ ++ [σ_{j₁+2}, σ_{j₁}]

and then each step's target is the next one's source *on the nose*, because
`descWord j₁ j₂ = σ_{j₁} :: descWord (j₁−1) j₂` and
`descWord (j₁+1) j₂ = σ_{j₁+1} :: descWord j₁ j₂` peel exactly the letters the
contexts carry. Those two `descWord_cons` peelings and
`descWord (j₁+2) (j₁+1) = [σ_{j₁+2}, σ_{j₁+1}]` are the whole of the gluing.

**No bound relating `j₁+3` to `i` is needed.** The obvious hypothesis
`j₁+3 ≤ i` is *not* required and is not taken: if it fails, `descWord i (j₁+3)`
is empty and the middle step is vacuous, which is exactly the degenerate
short-block case. Stating it would have narrowed the lemma for nothing.

**Two corrections to the first version of this section, both about scope.**

*The diagonal was excluded.* `blockPass` originally carried
`hj₂ : j₂ ≤ j₁ − 1`, and `b = a` means `j₂ = j₁`, so it could not be
instantiated there at all — yet `a ≤ b` includes the diagonal, and the diagonal
block is real (`a − 1` levels rather than `a`, starting one level higher). The
first level is simply absent there, so the fix is to name the rest:
`blockPassFromTwo` asks only `j₂ ≤ j₁` and covers the diagonal, with
`blockPass` = one leading transport + it.

*The trailing word was hardcoded.* Both versions ended `… ++ [σ_i]`. That is
right for the top-level block, but the *same* block shape occurs inside the
prefix as `small(a)`, where what sits to the right is `descWord j₁ j₂` instead.
Measured over 131 levels, top-level and `small(a)` obey one blueprint,

    W = descWord (min(h−2, j₁+1)) j_eff        B = descWord (h−1) (j₁+1) ++ T

differing only in `j_eff` and the tail `T`. Making `T` a parameter is what lets
one lemma serve both — and `small(a)` is where the prefix's own
`block · two steps · block` self-similarity stops being an observation and
becomes literal reuse. -/

/-- **The block from its second level on, with the source-only collision
hypothesis.** Two families, one per underlying transport: the `σ_jpp` step
across `descWord j₁ j₂`, and the block carried across `descWord jp j₂`. See
`blockTransportRightSources` (§4ai) for why `hpark` is stronger than needed. -/
theorem blockPassFromTwoSources {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    {i j₂ j₁ jp jpp jppp : Fin n}
    (hjp : j₁.val + 1 = jp.val) (hjpp : jp.val + 1 = jpp.val)
    (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ j₁.val)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (A T : Monomial (HeckeGen n))
    (hcol₁ : ∀ u v : Monomial (HeckeGen n), u ++ v = descWord j₁ j₂ → v ≠ [] →
      ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
        r ≠ A ++ (descWord i jppp ++ ([(⟨jp⟩ : HeckeGen n)] ++
          (u ++ ((⟨jpp⟩ : HeckeGen n) :: (v ++ ([(⟨jp⟩ : HeckeGen n)] ++ T)))))))
    (hcol₂ : ∀ (P S u v : Monomial (HeckeGen n)) (x : HeckeGen n),
      P ++ (x :: S) = descWord i jppp → u ++ v = descWord jp j₂ → v ≠ [] →
      ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
        r ≠ A ++ (P ++ (u ++ (x :: (v ++ (S ++ (descWord jpp jp ++ T))))))) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++
        (A ++ (descWord i jppp ++ ([(⟨jp⟩ : HeckeGen n)] ++
          ((⟨jpp⟩ : HeckeGen n) :: (descWord j₁ j₂ ++ ([(⟨jp⟩ : HeckeGen n)] ++ T))))), c)
          :: L₂))
      (AlgElement.ofTerms (L₁ ++
        (A ++ (descWord jp j₂ ++ (descWord i jppp ++ (descWord jpp jp ++ T))), c) :: L₂)) := by
  have hd2 : descWord jp j₂ = (⟨jp⟩ : HeckeGen n) :: descWord j₁ j₂ :=
    descWord_cons hjp hj₂
  have hd3 : descWord jpp jp = [(⟨jpp⟩ : HeckeGen n), ⟨jp⟩] := by
    rw [descWord_cons hjpp (le_refl _), descWord_self]
  have s2 := farComm_transport_right_sources hn hp jpp c hc L₁ L₂
    (descWord j₁ j₂)
    (A ++ (descWord i jppp ++ [(⟨jp⟩ : HeckeGen n)]))
    ([(⟨jp⟩ : HeckeGen n)] ++ T)
    (fun y hy => by have := descWord_index_le hy; omega)
    (fun u v huv hv r hr => by
      have := hcol₁ u v huv hv r hr
      simpa only [List.append_assoc] using this)
  have s3 := blockTransportRightSources hn hp c hc L₁ L₂ A (descWord jp j₂)
    (descWord i jppp) (descWord jpp jp ++ T)
    (fun x hx y hy => by
      have hx' := descWord_index_ge hx
      have hy' := descWord_index_le hy
      omega)
    hcol₂
  rw [hd2, hd3] at s3 ⊢
  simp only [List.append_assoc, List.cons_append, List.nil_append] at s2 s3 ⊢
  exact MultiStepReduction.trans s2 s3

/-- **The block from its second level on.** The two levels below the cap are
`h = j₁+1` and `h = j₁+2`; this covers the second and everything above it, which
is all of the block when the first level is absent.

It asks only `j₂ ≤ j₁`, **not** `j₂ < j₁`, and that is the point: at `b = a` the
two coincide, so a lemma demanding the strict inequality cannot be instantiated
on the diagonal at all. The trailing word `T` is a parameter for the same
reason — see §4aj. -/
theorem blockPassFromTwo {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    {i j₂ j₁ jp jpp jppp : Fin n}
    (hjp : j₁.val + 1 = jp.val) (hjpp : jp.val + 1 = jpp.val)
    (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ j₁.val)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (A T : Monomial (HeckeGen n))
    (hpark : ∀ r ∈ (L₁ ++ L₂).map Prod.fst, ∀ z : Monomial (HeckeGen n), r ≠ A ++ z) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++
        (A ++ (descWord i jppp ++ ([(⟨jp⟩ : HeckeGen n)] ++
          ((⟨jpp⟩ : HeckeGen n) :: (descWord j₁ j₂ ++ ([(⟨jp⟩ : HeckeGen n)] ++ T))))), c)
          :: L₂))
      (AlgElement.ofTerms (L₁ ++
        (A ++ (descWord jp j₂ ++ (descWord i jppp ++ (descWord jpp jp ++ T))), c) :: L₂)) :=
  blockPassFromTwoSources hn hp hjp hjpp hjppp hj₂ c hc L₁ L₂ A T
    (fun _ _ _ _ r hr => hpark r hr _)
    (fun _ _ _ _ _ _ _ _ r hr => hpark r hr _)

/-- **The block off the diagonal, with the source-only collision hypothesis.**
Three families: the leading `σ_jp` transport across `descWord jm j₂`, plus the
two `blockPassFromTwoSources` asks. -/
theorem blockPassSources {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    {i j₂ jm j₁ jp jpp jppp : Fin n}
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ jm.val)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (A T : Monomial (HeckeGen n))
    (hcol₀ : ∀ u v : Monomial (HeckeGen n), u ++ v = descWord jm j₂ → v ≠ [] →
      ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
        r ≠ A ++ (descWord i jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩] ++
          (u ++ ((⟨jp⟩ : HeckeGen n) :: (v ++ T))))))
    (hcol₁ : ∀ u v : Monomial (HeckeGen n), u ++ v = descWord j₁ j₂ → v ≠ [] →
      ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
        r ≠ A ++ (descWord i jppp ++ ([(⟨jp⟩ : HeckeGen n)] ++
          (u ++ ((⟨jpp⟩ : HeckeGen n) :: (v ++ ([(⟨jp⟩ : HeckeGen n)] ++ T)))))))
    (hcol₂ : ∀ (P S u v : Monomial (HeckeGen n)) (x : HeckeGen n),
      P ++ (x :: S) = descWord i jppp → u ++ v = descWord jp j₂ → v ≠ [] →
      ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
        r ≠ A ++ (P ++ (u ++ (x :: (v ++ (S ++ (descWord jpp jp ++ T))))))) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++
        (A ++ (descWord i jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩] ++
          ((⟨jp⟩ : HeckeGen n) :: (descWord jm j₂ ++ T)))), c) :: L₂))
      (AlgElement.ofTerms (L₁ ++
        (A ++ (descWord jp j₂ ++ (descWord i jppp ++ (descWord jpp jp ++ T))), c) :: L₂)) := by
  have hd1 : descWord j₁ j₂ = (⟨j₁⟩ : HeckeGen n) :: descWord jm j₂ :=
    descWord_cons hjm hj₂
  have s1 := farComm_transport_right_sources hn hp jp c hc L₁ L₂
    (descWord jm j₂)
    (A ++ (descWord i jppp ++ [(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩])) T
    (fun y hy => by have := descWord_index_le hy; omega)
    (fun u v huv hv r hr => by
      have := hcol₀ u v huv hv r hr
      simpa only [List.append_assoc] using this)
  have hj₂' : j₂.val ≤ j₁.val := by omega
  have s23 := blockPassFromTwoSources (i := i) (j₂ := j₂) (j₁ := j₁) (jp := jp)
    (jpp := jpp) (jppp := jppp) hn hp hjp hjpp hjppp hj₂' c hc L₁ L₂ A T
    hcol₁ hcol₂
  rw [hd1] at s23
  simp only [List.append_assoc, List.cons_append, List.nil_append] at s1 s23 ⊢
  exact MultiStepReduction.trans s1 s23

/-- **The block, at general depth, off the diagonal.** One pass of the `a ≤ b`
regime's far-commutation block when `j₂ < j₁`: the first level below the cap,
then `blockPassFromTwo` for the rest.

The left context `A` and the trailing word `T` are both arbitrary — the block
never has to know what the prefix left on either side of it. -/
theorem blockPass {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    {i j₂ jm j₁ jp jpp jppp : Fin n}
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ jm.val)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (A T : Monomial (HeckeGen n))
    (hpark : ∀ r ∈ (L₁ ++ L₂).map Prod.fst, ∀ z : Monomial (HeckeGen n), r ≠ A ++ z) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++
        (A ++ (descWord i jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩] ++
          ((⟨jp⟩ : HeckeGen n) :: (descWord jm j₂ ++ T)))), c) :: L₂))
      (AlgElement.ofTerms (L₁ ++
        (A ++ (descWord jp j₂ ++ (descWord i jppp ++ (descWord jpp jp ++ T))), c) :: L₂)) :=
  blockPassSources hn hp hjm hjp hjpp hjppp hj₂ c hc L₁ L₂ A T
    (fun _ _ _ _ r hr => hpark r hr _)
    (fun _ _ _ _ r hr => hpark r hr _)
    (fun _ _ _ _ _ _ _ _ r hr => hpark r hr _)

/-! ### §4al  The quadratic pair, at general depth

The prefix uses the quadratic rule exactly twice, and each time the step before
it is a Yang–Baxter. `hecke_quad_pair_shape.py` measured both occurrences and
they differ only in their surrounding words, so one lemma covers them — but the
mechanism is worth stating, because it is what makes the pair a *pair* rather
than two unrelated steps:

    L ++ [σ_{j₁+1}, σ_{j₁}, σ_{j₁+1}] ++ (σ_{j₁} :: R)
      Y →   L ++ [σ_{j₁}, σ_{j₁+1}] ++ [σ_{j₁}, σ_{j₁}] ++ R
      Q →   (L ++ [σ_{j₁}, σ_{j₁+1}, σ_{j₁}] ++ R,  c·h)
            (L ++ [σ_{j₁}, σ_{j₁+1}] ++ R,          c)

The Yang–Baxter step ends by emitting a `σ_{j₁}`, and `R` already *begins* with
one. The two land adjacent, and that is the quadratic redex. Neither step
creates it alone.

**The Yang–Baxter step does not go through `yangBaxterRelation`.** That rule
carries `−1` at its own leading word, so it is not monic and `monicStep` cannot
take it. The route is `bokutShiaoRelation j₁ (j₁+1) j₁`, which is the same
relation at `j = i − 1` (§4j) but monic and with the leading word the right way
round — `braid_hrel` / `braid_hlm` are exactly that repackaging. -/

/-- **The Yang–Baxter step and the quadratic step it sets up.** One term in, two
out, with the `h`-weighted one first. `L` and `R` are arbitrary: the pair occurs
twice in the prefix and the two occurrences differ only in them. -/
theorem quadPair {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    {j₁ jp : Fin n} (hjp : j₁.val + 1 = jp.val)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (L R : Monomial (HeckeGen n))
    (hpark : ∀ r ∈ (L₁ ++ L₂).map Prod.fst, ∀ z : Monomial (HeckeGen n), r ≠ L ++ z) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++
        (L ++ ([(⟨jp⟩ : HeckeGen n), ⟨j₁⟩, ⟨jp⟩] ++ ((⟨j₁⟩ : HeckeGen n) :: R)), c) :: L₂))
      (AlgElement.ofTerms (L₁ ++
        (L ++ ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ ((⟨j₁⟩ : HeckeGen n) :: R)),
            c * (hp.q - hp.q⁻¹))
          :: (L ++ ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ R), c) :: L₂)) := by
  have hne : (⟨j₁⟩ : HeckeGen n) ≠ ⟨jp⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  -- the Yang-Baxter step, taken through the Bokut-Shiao rule at j = i-1,
  -- which is the same relation but monic (4j)
  have s1 := monicStep hn hp _
    (bokutShiaoRelation_mem hn hp hjp (le_refl _))
    (BokutShiaoBraid.braid_hrel hjp) (BokutShiaoBraid.braid_hlm hjp)
    (by simp [hne]) L₁ L₂ L ((⟨j₁⟩ : HeckeGen n) :: R) _ _ c hc rfl rfl
    (fun q hq => by
      have := hpark q hq ([(⟨jp⟩ : HeckeGen n), ⟨j₁⟩, ⟨jp⟩] ++ ((⟨j₁⟩ : HeckeGen n) :: R))
      simpa using this)
  -- the quadratic step: Y's output puts a second σ_{j₁} against R's head
  have s2 := quadStep hn hp j₁ L₁ L₂ (L ++ [(⟨j₁⟩ : HeckeGen n), ⟨jp⟩]) R _ c hc rfl
    (fun q hq => by
      have := hpark q hq ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ ([(⟨j₁⟩ : HeckeGen n), ⟨j₁⟩] ++ R))
      simpa only [List.append_assoc, List.cons_append, List.nil_append] using this)
  simp only [List.append_assoc, List.cons_append, List.nil_append] at s1 s2 ⊢
  exact MultiStepReduction.head s1 (MultiStepReduction.head s2 (MultiStepReduction.refl _))

/-- **The descending run begins with its top index**, whenever it is non-empty.
Splits on `j = i` (`descWord_self`) and `j < i` (`descWord_cons` at `i − 1`). -/
theorem descWord_head {n : ℕ} {i j : Fin n} (hj : j.val ≤ i.val) :
    ∃ t, descWord i j = (⟨i⟩ : HeckeGen n) :: t := by
  rcases Nat.eq_or_lt_of_le hj with heq | hlt
  · have hji : j = i := Fin.ext heq
    subst hji
    exact ⟨[], descWord_self j⟩
  · have hi1 : i.val - 1 < n := by omega
    refine ⟨descWord ⟨i.val - 1, hi1⟩ j, ?_⟩
    exact descWord_cons (i' := ⟨i.val - 1, hi1⟩)
      (show i.val - 1 + 1 = i.val by omega) (show j.val ≤ i.val - 1 by omega)

namespace BraidBokutShiao

variable {n : ℕ}

/-! ### The words

Thirteen of them, all over the common tail `T = descWord i−2 j₂`. Their lengths
are what separates them at almost every step: `t+5, t+4, t+3, t+2, t+1` with only
three collisions, resolved by a first or fourth letter. -/

/-- `σᵢ σᵢ₋₁ σᵢ₋₁ σᵢ σᵢ₋₁ T` — the first term of the S-polynomial. -/
def w1 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n)
    :: (⟨i'⟩ : HeckeGen n) :: T

/-- `σᵢ₋₁ σᵢ σᵢ₋₁ σᵢ₋₁ T σᵢ` — the second. -/
def w2 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n)
    :: (T ++ [(⟨i⟩ : HeckeGen n)])

def v1 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T

def v2 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T

def v3 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n)
    :: (T ++ [(⟨i⟩ : HeckeGen n)])

def v4 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (T ++ [(⟨i⟩ : HeckeGen n)])

def v5 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T

def v6 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T

def v7 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: T

def v8 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T

def v9 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T

def v10 (i' : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: T

def v11 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: (T ++ [(⟨i⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)])

def v12 (i' i : Fin n) (T : Monomial (HeckeGen n)) : Monomial (HeckeGen n) :=
  (⟨i'⟩ : HeckeGen n) :: (T ++ [(⟨i⟩ : HeckeGen n)])

/-! ### The eleven stages -/

noncomputable def S0 (_hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(w1 i' i T, c), (w2 i' i T, -c)]

noncomputable def S1 (hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(v1 i' i T, c * (hp.q - hp.q⁻¹)), (v2 i' i T, c), (w2 i' i T, -c)]

noncomputable def S2 (hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(v1 i' i T, c * (hp.q - hp.q⁻¹)), (v2 i' i T, c),
     (v3 i' i T, -(c * (hp.q - hp.q⁻¹))), (v4 i' i T, -c)]

noncomputable def S3 (hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(v5 i' i T, c * (hp.q - hp.q⁻¹)), (v2 i' i T, c),
     (v3 i' i T, -(c * (hp.q - hp.q⁻¹))), (v4 i' i T, -c)]

noncomputable def S4 (hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(v6 i' i T, c * (hp.q - hp.q⁻¹) * (hp.q - hp.q⁻¹)), (v7 i' i T, c * (hp.q - hp.q⁻¹)),
     (v2 i' i T, c), (v3 i' i T, -(c * (hp.q - hp.q⁻¹))), (v4 i' i T, -c)]

noncomputable def S5 (hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(v6 i' i T, c * (hp.q - hp.q⁻¹) * (hp.q - hp.q⁻¹)), (v7 i' i T, c * (hp.q - hp.q⁻¹)),
     (v2 i' i T, c), (v8 i' i T, -(c * (hp.q - hp.q⁻¹))), (v4 i' i T, -c)]

noncomputable def S6 (hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(v7 i' i T, c * (hp.q - hp.q⁻¹)), (v2 i' i T, c),
     (v9 i' i T, -(c * (hp.q - hp.q⁻¹))), (v4 i' i T, -c)]

noncomputable def S7 (hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(v7 i' i T, c * (hp.q - hp.q⁻¹)), (v10 i' T, c), (v4 i' i T, -c)]

noncomputable def S8 (hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(v7 i' i T, c * (hp.q - hp.q⁻¹)), (v10 i' T, c), (v11 i' i T, -c)]

noncomputable def S9 (hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(v7 i' i T, c * (hp.q - hp.q⁻¹)), (v12 i' i T, -(c * (hp.q - hp.q⁻¹)))]

noncomputable def S10 (hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(v12 i' i T, c * (hp.q - hp.q⁻¹)), (v12 i' i T, -(c * (hp.q - hp.q⁻¹)))]

theorem S10_isZero (hp : HeckeParams) (i' i : Fin n) (T : Monomial (HeckeGen n)) (c : ℝ) :
    (S10 hp i' i T c).isZero := by
  intro m
  simp only [S10, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
  ring

/-- The composition of a rule leading on the braid word `σᵢσᵢ₋₁σᵢ` with
`bokutShiaoRelation i' i j₂`, overlapping in the trailing `σᵢ`. -/
noncomputable def oc (r₁ : ReductionRule (HeckeGen n) ℝ) {i' i j₂ : Fin n}
    {T : Monomial (HeckeGen n)}
    (hlm₁ : r₁.lm (heckeOrder n) = BraidSelfOverlap.wHi i' i)
    (hi : i'.val + 1 = i.val) (hj : j₂.val ≤ i'.val)
    (hT : descWord i' j₂ = (⟨i'⟩ : HeckeGen n) :: T) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := r₁
  rule₂ := bokutShiaoRelation i' i j₂
  left := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
  overlap := [⟨i⟩]
  right := (⟨i'⟩ : HeckeGen n) :: (T ++ [(⟨i⟩ : HeckeGen n)])
  lm₁_decomp := hlm₁
  lm₂_decomp := by
    rw [bokutShiaoRelation_lm hi hj, bsWord₁, descWord_cons hi hj, hT]
    rfl
  overlap_nonempty := by simp

/-- The outer Bokut–Shiao rule in two-word form over `T`. -/
theorem rule₂_hrel {i' i j₂ : Fin n} {T : Monomial (HeckeGen n)}
    (hi : i'.val + 1 = i.val) (hj : j₂.val ≤ i'.val)
    (hT : descWord i' j₂ = (⟨i'⟩ : HeckeGen n) :: T) (w : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i' i j₂).relation.coeff w
      = (AlgElement.ofTerms
          [((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (T ++ [(⟨i⟩ : HeckeGen n)]), (1 : ℝ)),
           (v6 i' i T, -1)]).coeff w := by
  show (AlgElement.ofTerms [(bsWord₁ i j₂, (1 : ℝ)), (bsWord₂ i' i j₂, -1)]).coeff w = _
  rw [bsWord₁, descWord_cons hi hj, hT, bsWord₂, hT, v6]
  rfl

theorem rule₂_hlm {i' i j₂ : Fin n} {T : Monomial (HeckeGen n)}
    (hi : i'.val + 1 = i.val) (hj : j₂.val ≤ i'.val)
    (hT : descWord i' j₂ = (⟨i'⟩ : HeckeGen n) :: T) :
    (bokutShiaoRelation i' i j₂).lm (heckeOrder n)
      = (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (T ++ [(⟨i⟩ : HeckeGen n)]) := by
  rw [bokutShiaoRelation_lm hi hj, bsWord₁, descWord_cons hi hj, hT]
  rfl

/-- **The S-polynomial.** The ambient word `σᵢσᵢ₋₁σᵢσᵢ₋₁Tσᵢ` is reached from both
sides and cancels; each surviving term carries a square `σᵢ₋₁σᵢ₋₁`. -/
theorem oc_spoly_coeff (r₁ : ReductionRule (HeckeGen n) ℝ) {i' i j₂ : Fin n}
    {T : Monomial (HeckeGen n)} {c : ℝ}
    (hlm₁ : r₁.lm (heckeOrder n) = BraidSelfOverlap.wHi i' i)
    (hlc₁ : r₁.lc (heckeOrder n) = c)
    (hrel₁ : ∀ w, r₁.relation.coeff w
      = (AlgElement.ofTerms
          [(BraidSelfOverlap.wHi i' i, c), (BraidSelfOverlap.wLo i' i, -c)]).coeff w)
    (hi : i'.val + 1 = i.val) (hj : j₂.val ≤ i'.val)
    (hT : descWord i' j₂ = (⟨i'⟩ : HeckeGen n) :: T) (hp : HeckeParams)
    (m : Monomial (HeckeGen n)) :
    (oc r₁ hlm₁ hi hj hT).spoly.coeff m = (S0 hp i' i T c).coeff m := by
  show (bokutShiaoRelation i' i j₂).lc (heckeOrder n)
      * (AlgElement.contextMul [] r₁.relation
          ((⟨i'⟩ : HeckeGen n) :: (T ++ [(⟨i⟩ : HeckeGen n)]))).coeff m
    - r₁.lc (heckeOrder n)
      * (AlgElement.contextMul [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
          (bokutShiaoRelation i' i j₂).relation []).coeff m
    = _
  rw [hlc₁, bokutShiaoRelation_lc hi hj, one_mul,
    AlgElement.contextMul_coeff_congr [] ((⟨i'⟩ : HeckeGen n) :: (T ++ [(⟨i⟩ : HeckeGen n)]))
      hrel₁ m,
    AlgElement.contextMul_coeff_congr [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] []
      (rule₂_hrel hi hj hT) m]
  simp only [S0, w1, w2, v6, BraidSelfOverlap.wHi, BraidSelfOverlap.wLo,
    AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
    List.append_nil, List.cons_append, AlgElement.ofTerms_coeff,
    List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-! ### The eight fixed steps

Five of them apply the quadratic rule, which has three words, so `monicStep`
(§4x) does not reach them and each is written out. The distinctness obligations
are lengths — `t+5, t+4, t+3, t+2, t+1` over the shared tail — with three
exceptions resolved by a first letter and one (step 4) by a fourth. -/

section

variable (hp : HeckeParams) {i'' i' i j₂ : Fin n} {T T' : Monomial (HeckeGen n)} {c : ℝ}

theorem chainA1 (hn : 0 < n) (hii' : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S0 hp i' i T c) (S1 hp i' i T c) := by
  have hv : (S0 hp i' i T c).coeff
      ([(⟨i⟩ : HeckeGen n)] ++ (heckeRelation i' hp).lm (heckeOrder n)
        ++ ((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T)) = c := by
    rw [heckeRelation_lm, show ([(⟨i⟩ : HeckeGen n)] ++ [(⟨i'⟩ : HeckeGen n), ⟨i'⟩]
        ++ ((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T)) = w1 i' i T by simp [w1]]
    have h2 : w2 i' i T ≠ w1 i' i T := by
      simp only [w1, w2]
      intro hcon
      injection hcon with h1 _
      exact hii' h1
    simp [S0, AlgElement.ofTerms_coeff, h2]
  refine ⟨heckeRelation i' hp, heckeRelation_mem hn hp i', [(⟨i⟩ : HeckeGen n)],
    (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T, c, ?_, ?_, ?_⟩
  · rw [hv]; exact hc
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - c * (AlgElement.contextMul [(⟨i⟩ : HeckeGen n)]
      (heckeRelation i' hp).relation
      ((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T)).coeff m
    simp only [S0, S1, w1, w2, v1, v2, heckeRelation, AlgElement.contextMul_ofTerms_coeff,
      List.map_cons, List.map_nil, List.nil_append, List.cons_append,
      AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
      decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem chainA2 (hn : 0 < n) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S1 hp i' i T c) (S2 hp i' i T c) := by
  have hlen : ∀ W : Monomial (HeckeGen n), W.length ≠ (w2 i' i T).length → W ≠ w2 i' i T :=
    fun W h hcon => h (by rw [hcon])
  have hv : (S1 hp i' i T c).coeff
      ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ (heckeRelation i' hp).lm (heckeOrder n)
        ++ (T ++ [(⟨i⟩ : HeckeGen n)])) = -c := by
    rw [heckeRelation_lm, show ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
        ++ [(⟨i'⟩ : HeckeGen n), ⟨i'⟩] ++ (T ++ [(⟨i⟩ : HeckeGen n)])) = w2 i' i T
      by simp [w2]]
    have h1 : v1 i' i T ≠ w2 i' i T := by
      refine hlen _ ?_
      simp only [v1, w2, List.length_cons, List.length_append, List.length_nil]
      omega
    have h2 : v2 i' i T ≠ w2 i' i T := by
      refine hlen _ ?_
      simp only [v2, w2, List.length_cons, List.length_append, List.length_nil]
      omega
    simp [S1, AlgElement.ofTerms_coeff, h1, h2]
  refine ⟨heckeRelation i' hp, heckeRelation_mem hn hp i',
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)], T ++ [(⟨i⟩ : HeckeGen n)], -c, ?_, ?_, ?_⟩
  · rw [hv]; exact neg_ne_zero.mpr hc
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (-c) * (AlgElement.contextMul
      [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] (heckeRelation i' hp).relation
      (T ++ [(⟨i⟩ : HeckeGen n)])).coeff m
    simp only [S1, S2, w2, v1, v2, v3, v4, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff,
      List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem chainA3 (hn : 0 < n) (hi : i'.val + 1 = i.val)
    (hii' : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩) (hc : c ≠ 0) (hh : hp.q - hp.q⁻¹ ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S2 hp i' i T c) (S3 hp i' i T c) := by
  have hlen : ∀ W : Monomial (HeckeGen n), W.length ≠ (v1 i' i T).length → W ≠ v1 i' i T :=
    fun W h hcon => h (by rw [hcon])
  have hv : (S2 hp i' i T c).coeff
      ([] ++ (bokutShiaoRelation i' i i').lm (heckeOrder n)
        ++ ((⟨i'⟩ : HeckeGen n) :: T)) = c * (hp.q - hp.q⁻¹) := by
    rw [BraidSelfOverlap.bs_hlm i' i hi,
      show (([] : Monomial (HeckeGen n)) ++ BraidSelfOverlap.wHi i' i
        ++ ((⟨i'⟩ : HeckeGen n) :: T)) = v1 i' i T by simp [BraidSelfOverlap.wHi, v1]]
    have h2 : v2 i' i T ≠ v1 i' i T := by
      refine hlen _ ?_
      simp only [v1, v2, List.length_cons]
      omega
    have h3 : v3 i' i T ≠ v1 i' i T := by
      simp only [v1, v3]
      intro hcon
      injection hcon with h1 _
      exact hii' h1
    have h4 : v4 i' i T ≠ v1 i' i T := by
      refine hlen _ ?_
      simp only [v1, v4, List.length_cons, List.length_append, List.length_nil]
      omega
    simp [S2, AlgElement.ofTerms_coeff, h2, h3, h4]
  refine ⟨bokutShiaoRelation i' i i', bokutShiaoRelation_mem hn hp hi (le_refl _), [],
    (⟨i'⟩ : HeckeGen n) :: T, c * (hp.q - hp.q⁻¹), ?_, ?_, ?_⟩
  · rw [hv]; exact mul_ne_zero hc hh
  · rw [hv, bokutShiaoRelation_lc hi (le_refl _)]; ring
  · intro m
    show _ = _ - (c * (hp.q - hp.q⁻¹)) * (AlgElement.contextMul []
      (bokutShiaoRelation i' i i').relation ((⟨i'⟩ : HeckeGen n) :: T)).coeff m
    rw [AlgElement.contextMul_coeff_congr [] ((⟨i'⟩ : HeckeGen n) :: T)
      (BraidSelfOverlap.bs_hrel i' i hi) m]
    simp only [S2, S3, v1, v2, v3, v4, v5, BraidSelfOverlap.wHi, BraidSelfOverlap.wLo,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff,
      List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem chainA4 (hn : 0 < n) (hT : T = (⟨i''⟩ : HeckeGen n) :: T')
    (hi'i'' : (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩) (hc : c ≠ 0) (hh : hp.q - hp.q⁻¹ ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S3 hp i' i T c) (S4 hp i' i T c) := by
  have hlen : ∀ W : Monomial (HeckeGen n), W.length ≠ (v5 i' i T).length → W ≠ v5 i' i T :=
    fun W h hcon => h (by rw [hcon])
  have hv : (S3 hp i' i T c).coeff
      ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] ++ (heckeRelation i' hp).lm (heckeOrder n)
        ++ T) = c * (hp.q - hp.q⁻¹) := by
    rw [heckeRelation_lm, show ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
        ++ [(⟨i'⟩ : HeckeGen n), ⟨i'⟩] ++ T) = v5 i' i T by simp [v5]]
    have h2 : v2 i' i T ≠ v5 i' i T := by
      refine hlen _ ?_
      simp only [v2, v5, List.length_cons]
      omega
    have h3 : v3 i' i T ≠ v5 i' i T := by
      simp only [v3, v5, hT]
      intro hcon
      injection hcon with _ h2'
      injection h2' with _ h3'
      injection h3' with _ h4'
      injection h4' with h5' _
      exact hi'i'' h5'.symm
    have h4 : v4 i' i T ≠ v5 i' i T := by
      refine hlen _ ?_
      simp only [v4, v5, List.length_cons, List.length_append, List.length_nil]
      omega
    simp [S3, AlgElement.ofTerms_coeff, h2, h3, h4]
  refine ⟨heckeRelation i' hp, heckeRelation_mem hn hp i',
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)], T, c * (hp.q - hp.q⁻¹), ?_, ?_, ?_⟩
  · rw [hv]; exact mul_ne_zero hc hh
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (c * (hp.q - hp.q⁻¹)) * (AlgElement.contextMul
      [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] (heckeRelation i' hp).relation T).coeff m
    simp only [S3, S4, v2, v3, v4, v5, v6, v7, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff,
      List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

end

section

variable (hp : HeckeParams) {i'' i' i j₂ : Fin n} {T T' : Monomial (HeckeGen n)} {c : ℝ}

theorem chainA5 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hj : j₂.val ≤ i'.val)
    (hT : descWord i' j₂ = (⟨i'⟩ : HeckeGen n) :: T) (hc : c ≠ 0)
    (hh : hp.q - hp.q⁻¹ ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S4 hp i' i T c) (S5 hp i' i T c) := by
  have hlen : ∀ W : Monomial (HeckeGen n), W.length ≠ (v3 i' i T).length → W ≠ v3 i' i T :=
    fun W h hcon => h (by rw [hcon])
  have hv : (S4 hp i' i T c).coeff
      ([(⟨i'⟩ : HeckeGen n)] ++ (bokutShiaoRelation i' i j₂).lm (heckeOrder n) ++ [])
      = -(c * (hp.q - hp.q⁻¹)) := by
    rw [rule₂_hlm hi hj hT, show ([(⟨i'⟩ : HeckeGen n)] ++ ((⟨i⟩ : HeckeGen n)
        :: (⟨i'⟩ : HeckeGen n) :: (T ++ [(⟨i⟩ : HeckeGen n)])) ++ []) = v3 i' i T
      by simp [v3]]
    have h6 : v6 i' i T ≠ v3 i' i T := by
      refine hlen _ ?_
      simp only [v3, v6, List.length_cons, List.length_append, List.length_nil]; omega
    have h7 : v7 i' i T ≠ v3 i' i T := by
      refine hlen _ ?_
      simp only [v3, v7, List.length_cons, List.length_append, List.length_nil]; omega
    have h2 : v2 i' i T ≠ v3 i' i T := by
      refine hlen _ ?_
      simp only [v2, v3, List.length_cons, List.length_append, List.length_nil]; omega
    have h4 : v4 i' i T ≠ v3 i' i T := by
      refine hlen _ ?_
      simp only [v3, v4, List.length_cons, List.length_append, List.length_nil]; omega
    simp [S4, AlgElement.ofTerms_coeff, h6, h7, h2, h4]
  refine ⟨bokutShiaoRelation i' i j₂, bokutShiaoRelation_mem hn hp hi hj,
    [(⟨i'⟩ : HeckeGen n)], [], -(c * (hp.q - hp.q⁻¹)), ?_, ?_, ?_⟩
  · rw [hv]; exact neg_ne_zero.mpr (mul_ne_zero hc hh)
  · rw [hv, bokutShiaoRelation_lc hi hj]; ring
  · intro m
    show _ = _ - (-(c * (hp.q - hp.q⁻¹))) * (AlgElement.contextMul [(⟨i'⟩ : HeckeGen n)]
      (bokutShiaoRelation i' i j₂).relation []).coeff m
    rw [AlgElement.contextMul_coeff_congr [(⟨i'⟩ : HeckeGen n)] []
      (rule₂_hrel hi hj hT) m]
    simp only [S4, S5, v2, v3, v4, v6, v7, v8,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.append_nil, List.cons_append, AlgElement.ofTerms_coeff,
      List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem chainA6 (hn : 0 < n) (hc : c ≠ 0) (hh : hp.q - hp.q⁻¹ ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S5 hp i' i T c) (S6 hp i' i T c) := by
  have hlen : ∀ W : Monomial (HeckeGen n), W.length ≠ (v8 i' i T).length → W ≠ v8 i' i T :=
    fun W h hcon => h (by rw [hcon])
  have hv : (S5 hp i' i T c).coeff
      ([] ++ (heckeRelation i' hp).lm (heckeOrder n)
        ++ ((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T))
      = -(c * (hp.q - hp.q⁻¹)) := by
    rw [heckeRelation_lm, show (([] : Monomial (HeckeGen n)) ++ [(⟨i'⟩ : HeckeGen n), ⟨i'⟩]
        ++ ((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T)) = v8 i' i T by simp [v8]]
    have h6 : v6 i' i T ≠ v8 i' i T := by
      refine hlen _ ?_; simp only [v6, v8, List.length_cons]; omega
    have h7 : v7 i' i T ≠ v8 i' i T := by
      refine hlen _ ?_; simp only [v7, v8, List.length_cons]; omega
    have h2 : v2 i' i T ≠ v8 i' i T := by
      refine hlen _ ?_; simp only [v2, v8, List.length_cons]; omega
    have h4 : v4 i' i T ≠ v8 i' i T := by
      refine hlen _ ?_
      simp only [v4, v8, List.length_cons, List.length_append, List.length_nil]; omega
    simp [S5, AlgElement.ofTerms_coeff, h6, h7, h2, h4]
  refine ⟨heckeRelation i' hp, heckeRelation_mem hn hp i', [],
    (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T, -(c * (hp.q - hp.q⁻¹)), ?_, ?_, ?_⟩
  · rw [hv]; exact neg_ne_zero.mpr (mul_ne_zero hc hh)
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (-(c * (hp.q - hp.q⁻¹))) * (AlgElement.contextMul []
      (heckeRelation i' hp).relation
      ((⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: T)).coeff m
    simp only [S5, S6, v2, v4, v6, v7, v8, v9, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff,
      List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem chainA7 (hn : 0 < n) (hii' : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S6 hp i' i T c) (S7 hp i' i T c) := by
  have hlen : ∀ W : Monomial (HeckeGen n), W.length ≠ (v2 i' i T).length → W ≠ v2 i' i T :=
    fun W h hcon => h (by rw [hcon])
  have hv : (S6 hp i' i T c).coeff
      ([] ++ (heckeRelation i hp).lm (heckeOrder n) ++ ((⟨i'⟩ : HeckeGen n) :: T)) = c := by
    rw [heckeRelation_lm, show (([] : Monomial (HeckeGen n)) ++ [(⟨i⟩ : HeckeGen n), ⟨i⟩]
        ++ ((⟨i'⟩ : HeckeGen n) :: T)) = v2 i' i T by simp [v2]]
    have h7 : v7 i' i T ≠ v2 i' i T := by
      refine hlen _ ?_; simp only [v2, v7, List.length_cons]; omega
    have h9 : v9 i' i T ≠ v2 i' i T := by
      refine hlen _ ?_; simp only [v2, v9, List.length_cons]; omega
    have h4 : v4 i' i T ≠ v2 i' i T := by
      simp only [v2, v4]
      intro hcon
      injection hcon with h1 _
      exact hii' h1
    simp [S6, AlgElement.ofTerms_coeff, h7, h9, h4]
  refine ⟨heckeRelation i hp, heckeRelation_mem hn hp i, [],
    (⟨i'⟩ : HeckeGen n) :: T, c, ?_, ?_, ?_⟩
  · rw [hv]; exact hc
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - c * (AlgElement.contextMul [] (heckeRelation i hp).relation
      ((⟨i'⟩ : HeckeGen n) :: T)).coeff m
    simp only [S6, S7, v2, v4, v7, v9, v10, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff,
      List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

theorem chainA8 (hn : 0 < n) (hc : c ≠ 0) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S8 hp i' i T c) (S9 hp i' i T c) := by
  have hlen : ∀ W : Monomial (HeckeGen n), W.length ≠ (v11 i' i T).length → W ≠ v11 i' i T :=
    fun W h hcon => h (by rw [hcon])
  have hv : (S8 hp i' i T c).coeff
      (((⟨i'⟩ : HeckeGen n) :: T) ++ (heckeRelation i hp).lm (heckeOrder n) ++ []) = -c := by
    rw [heckeRelation_lm, show (((⟨i'⟩ : HeckeGen n) :: T) ++ [(⟨i⟩ : HeckeGen n), ⟨i⟩] ++ [])
      = v11 i' i T by simp [v11]]
    have h7 : v7 i' i T ≠ v11 i' i T := by
      refine hlen _ ?_
      simp only [v7, v11, List.length_cons, List.length_append, List.length_nil]; omega
    have h10 : v10 i' T ≠ v11 i' i T := by
      refine hlen _ ?_
      simp only [v10, v11, List.length_cons, List.length_append, List.length_nil]; omega
    simp [S8, AlgElement.ofTerms_coeff, h7, h10]
  refine ⟨heckeRelation i hp, heckeRelation_mem hn hp i, (⟨i'⟩ : HeckeGen n) :: T, [],
    -c, ?_, ?_, ?_⟩
  · rw [hv]; exact neg_ne_zero.mpr hc
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (-c) * (AlgElement.contextMul ((⟨i'⟩ : HeckeGen n) :: T)
      (heckeRelation i hp).relation []).coeff m
    simp only [S8, S9, v7, v10, v11, v12, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil,
      List.append_nil, List.cons_append, AlgElement.ofTerms_coeff,
      List.filter_cons, List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

end

/-- **Eight steps and two transports, to zero.** -/
theorem oc_reduces_to_zero (hp : HeckeParams) (r₁ : ReductionRule (HeckeGen n) ℝ)
    {i'' i' i j₂ : Fin n} {c : ℝ} (hn : 0 < n)
    (hlm₁ : r₁.lm (heckeOrder n) = BraidSelfOverlap.wHi i' i)
    (hlc₁ : r₁.lc (heckeOrder n) = c)
    (hrel₁ : ∀ w, r₁.relation.coeff w
      = (AlgElement.ofTerms
          [(BraidSelfOverlap.wHi i' i, c), (BraidSelfOverlap.wLo i' i, -c)]).coeff w)
    (hc : c ≠ 0) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hj : j₂.val ≤ i''.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc r₁ hlm₁ hi (by omega) (descWord_cons hi'' hj)).spoly nf ∧ nf.isZero := by
  have hh := hp.h_ne_zero
  have hii' : (⟨i'⟩ : HeckeGen n) ≠ ⟨i⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  have hi'i'' : (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  obtain ⟨T', hT'⟩ := descWord_head (i := i'') (j := j₂) hj
  have hT : descWord i' j₂ = (⟨i'⟩ : HeckeGen n) :: descWord i'' j₂ :=
    descWord_cons hi'' hj
  have hfar : ∀ y ∈ descWord i'' j₂, y.index.val + 1 < i.val := by
    intro y hy
    have := descWord_index_le hy
    omega
  -- the first transport: the trailing generator crosses `T`, two terms carried
  have ph1 : MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S7 hp i' i (descWord i'' j₂) c) (S8 hp i' i (descWord i'' j₂) c) :=
    farComm_transport_right hn hp i (-c) (neg_ne_zero.mpr hc)
      [(v7 i' i (descWord i'' j₂), c * (hp.q - hp.q⁻¹)),
       (v10 i' (descWord i'' j₂), c)] []
      (descWord i'' j₂) [(⟨i'⟩ : HeckeGen n)] [(⟨i⟩ : HeckeGen n)] hfar
      (by
        intro u v huv r hr
        have hlen := congrArg List.length huv
        simp only [List.length_append] at hlen
        simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
          List.not_mem_nil, or_false] at hr
        rcases hr with rfl | rfl
        · simp only [v7]
          intro hcon
          have := congrArg List.length hcon
          simp only [List.length_cons, List.length_append, List.length_nil,
            List.singleton_append] at this
          omega
        · simp only [v10]
          intro hcon
          have := congrArg List.length hcon
          simp only [List.length_cons, List.length_append, List.length_nil,
            List.singleton_append] at this
          omega)
  -- the second: what is left is the cancelling form of §4t
  have ph2 : MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S9 hp i' i (descWord i'' j₂) c) (S10 hp i' i (descWord i'' j₂) c) :=
    farComm_transport hn hp i (c * (hp.q - hp.q⁻¹)) (mul_ne_zero hc hh)
      (descWord i'' j₂) [(⟨i'⟩ : HeckeGen n)] hfar
  refine reducesToZero_congr ⟨S10 hp i' i (descWord i'' j₂) c,
    ⟨((((MultiStepReduction.refl (S0 hp i' i (descWord i'' j₂) c))
      |>.step (chainA1 hp hn hii' hc)
      |>.step (chainA2 hp hn hc)
      |>.step (chainA3 hp hn hi hii' hc hh)
      |>.step (chainA4 hp hn hT' hi'i'' hc hh)
      |>.step (chainA5 hp hn hi (by omega) hT hc hh)
      |>.step (chainA6 hp hn hc hh)
      |>.step (chainA7 hp hn hii' hc)).trans ph1).step (chainA8 hp hn hc)).trans ph2,
      isNormalForm_of_isZero (S10_isZero hp i' i (descWord i'' j₂) c)⟩,
    S10_isZero hp i' i (descWord i'' j₂) c⟩ ?_
  intro m
  exact oc_spoly_coeff r₁ hlm₁ hlc₁ hrel₁ hi (by omega) hT hp m

/-! ### The two instances

`rule₁` leads on the braid word, so it doubles (§4j); `rule₂` cannot, because
`j₂ ≤ i − 2` puts its leading monomial strictly longer. Those are the six `n = 4`
members of the `a = 1` row. -/

/-- **Yang–Baxter against the outer Bokut–Shiao rule.** -/
theorem yangBaxter_resolves (hp : HeckeParams) {i'' i' i j₂ : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) (hj : j₂.val ≤ i''.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc (yangBaxterRelation i' i) (BraidSelfOverlap.yb_hlm i' i hi) hi (by omega)
        (descWord_cons hi'' hj)).spoly nf ∧ nf.isZero :=
  oc_reduces_to_zero hp (yangBaxterRelation i' i) hn (BraidSelfOverlap.yb_hlm i' i hi)
    (DegenerateYbBs.yangBaxter_lc hi) (BraidSelfOverlap.yb_hrel i' i hi) (by norm_num)
    hi hi'' hj

/-- **Bokut–Shiao at `j = i − 1` against it.** -/
theorem bokutShiao_resolves (hp : HeckeParams) {i'' i' i j₂ : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) (hj : j₂.val ≤ i''.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc (bokutShiaoRelation i' i i') (BraidSelfOverlap.bs_hlm i' i hi) hi (by omega)
        (descWord_cons hi'' hj)).spoly nf ∧ nf.isZero :=
  oc_reduces_to_zero hp (bokutShiaoRelation i' i i') hn (BraidSelfOverlap.bs_hlm i' i hi)
    (bokutShiaoRelation_lc hi (le_refl _)) (BraidSelfOverlap.bs_hrel i' i hi) one_ne_zero
    hi hi'' hj

end BraidBokutShiao

/-! ## §4z  Both depths at `i − 2` — the first corner case of `B × B`

The five that remain after §4x and §4y all have `a, b ≥ 2`: both rules at general
depth, neither on the braid word. This is the corner `a = b = 2`, i.e.
`j₁ = j₂ = i − 2`, where the composition is a Bokut–Shiao rule **against
itself** at a proper overlap — the analogue of §4r one level down.

Because `a, b ≥ 2` puts both leading monomials strictly longer than the braid
word, neither rule can be Yang–Baxter: there is no §4j doubling here, and the
family is one composition per `i` rather than four. At `n = 4` that is
`B120 × B120` and `B231 × B231`.

**Everything is explicit.** With `x = σᵢ`, `y = σᵢ₋₁`, `z = σᵢ₋₂`, both depths
pinned at `i − 2` make `descWord i j₁ = xyz` and `descWord i−1 j₂ = yz`, so every
word in the chain is a literal five-, six- or seven-letter list in three
generators. The S-polynomial is

    spoly = x y z y x y z  −  y x y z y z x

and the chain is fifteen steps. **Thirteen of them apply a two-word monic rule**
— the braid rule at `(i−2, i−1)`, the braid rule at `(i−1, i)`, far-commutation
`σᵢσᵢ₋₂`, and the rule itself — so `monicStep` (§4x) discharges each in a few
lines. Only steps 4 and 7 are quadratic, and those are written out.

The two quadratic steps are where `h` enters, and it leaves again at step 11:
`z y x z y z` and `z y z x y z` both carry `h` there with opposite signs and
cancel, taking the element from four live terms back to two. The `h`-weighted
pair is kept in the term list rather than merged, because `monicStep` produces
the unmerged list and a merge would need its own step; carrying it costs nothing
since the surviving stages are still told apart by length or third letter.

**No transports.** Unlike §4y this corner needs none: with both depths at
`i − 2` there is no run left to cross, which is exactly why it is the corner to
do first. The remaining three — `(3,2)`, `(2,3)`, `(3,3)` at 15, 19 and 25 steps
— reintroduce the runs and with them the transports. -/

namespace BokutShiaoCorner

variable {n : ℕ}

/-- The three generators in play are pairwise distinct. -/
theorem gen3_ne {i'' i' i : Fin n} (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    (⟨i⟩ : HeckeGen n) ≠ ⟨i'⟩ ∧ (⟨i⟩ : HeckeGen n) ≠ ⟨i''⟩
      ∧ (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩ := by
  refine ⟨?_, ?_, ?_⟩ <;>
    · intro hcon
      have := congrArg HeckeGen.rank hcon
      simp only [HeckeGen.rank] at this
      omega

/-- `descWord i−1 (i−2) = σᵢ₋₁σᵢ₋₂`. -/
theorem descWord2 {i'' i' : Fin n} (hi'' : i''.val + 1 = i'.val) :
    descWord i' i'' = [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] := by
  rw [descWord_cons hi'' (le_refl _), descWord_self]

/-- `descWord i (i−2) = σᵢσᵢ₋₁σᵢ₋₂`. -/
theorem descWord3 {i'' i' i : Fin n} (hi : i'.val + 1 = i.val)
    (hi'' : i''.val + 1 = i'.val) :
    descWord i i'' = [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] := by
  rw [descWord_cons hi (by omega), descWord2 hi'']

section

variable (hp : HeckeParams) {i'' i' i : Fin n}

/-- The rule of the composition, in two-word form. -/
theorem outer_hrel (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (w : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i' i i'').relation.coeff w
      = (AlgElement.ofTerms
          [([(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
              (⟨i⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n),
              (⟨i''⟩ : HeckeGen n)], -1)]).coeff w := by
  show (AlgElement.ofTerms
    [(bsWord₁ i i'', (1 : ℝ)), (bsWord₂ i' i i'', -1)]).coeff w = _
  rw [bsWord₁, descWord3 hi hi'', bsWord₂, descWord2 hi'']
  rfl

theorem outer_hlm (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    (bokutShiaoRelation i' i i'').lm (heckeOrder n)
      = [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
         (⟨i⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm hi (by omega), bsWord₁, descWord3 hi hi'']
  rfl

end

def p0 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def p1 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def p2 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def q0 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def q1 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def q2 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def q3 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def p3 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def p4 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def p5 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def p6 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
def q4 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def q5 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def q6 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def q7 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def q8 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
def q9 (i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]

noncomputable def U0 (_hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(p0 i'' i' i, 1),
     (q0 i'' i' i, -1)]
noncomputable def U1 (_hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(p1 i'' i' i, 1),
     (q0 i'' i' i, -1)]
noncomputable def U2 (_hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(p2 i'' i' i, 1),
     (q0 i'' i' i, -1)]
noncomputable def U3 (_hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(p2 i'' i' i, 1),
     (q1 i'' i' i, -1)]
noncomputable def U4 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(p2 i'' i' i, 1),
     (q2 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q3 i'' i' i, -1)]
noncomputable def U5 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(p3 i'' i' i, 1),
     (q2 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q3 i'' i' i, -1)]
noncomputable def U6 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(p4 i'' i' i, 1),
     (q2 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q3 i'' i' i, -1)]
noncomputable def U7 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(p5 i'' i' i, hp.q - hp.q⁻¹),
     (p6 i'' i' i, 1),
     (q2 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q3 i'' i' i, -1)]
noncomputable def U8 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(p5 i'' i' i, hp.q - hp.q⁻¹),
     (p6 i'' i' i, 1),
     (q4 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q3 i'' i' i, -1)]
noncomputable def U9 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(p5 i'' i' i, hp.q - hp.q⁻¹),
     (p6 i'' i' i, 1),
     (q5 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q3 i'' i' i, -1)]
noncomputable def U10 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(p5 i'' i' i, hp.q - hp.q⁻¹),
     (p6 i'' i' i, 1),
     (q6 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q3 i'' i' i, -1)]
noncomputable def U11 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(q6 i'' i' i, hp.q - hp.q⁻¹),
     (p6 i'' i' i, 1),
     (q6 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q3 i'' i' i, -1)]
noncomputable def U12 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(q6 i'' i' i, hp.q - hp.q⁻¹),
     (p6 i'' i' i, 1),
     (q6 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q7 i'' i' i, -1)]
noncomputable def U13 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(q6 i'' i' i, hp.q - hp.q⁻¹),
     (p6 i'' i' i, 1),
     (q6 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q8 i'' i' i, -1)]
noncomputable def U14 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(q6 i'' i' i, hp.q - hp.q⁻¹),
     (p6 i'' i' i, 1),
     (q6 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q9 i'' i' i, -1)]
noncomputable def U15 (hp : HeckeParams) (i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(q6 i'' i' i, hp.q - hp.q⁻¹),
     (q9 i'' i' i, 1),
     (q6 i'' i' i, -(hp.q - hp.q⁻¹)),
     (q9 i'' i' i, -1)]

section

variable (hp : HeckeParams) {i'' i' i : Fin n}

theorem z1 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U0 hp i'' i' i) (U1 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i'') (bokutShiaoRelation_mem hn hp hi'' (le_refl _))
    (BraidSelfOverlap.bs_hrel i'' i' hi'') (BraidSelfOverlap.bs_hlm i'' i' hi'')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [] [(q0 i'' i' i, -1)]
    [(⟨i⟩ : HeckeGen n)] [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [p0, q0, *])

theorem z2 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U1 hp i'' i' i) (U2 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [] [(q0 i'' i' i, -1)]
    [] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [p1, q0, *])

theorem z3 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U2 hp i'' i' i) (U3 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i'') (bokutShiaoRelation_mem hn hp hi'' (le_refl _))
    (BraidSelfOverlap.bs_hrel i'' i' hi'') (BraidSelfOverlap.bs_hlm i'' i' hi'')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [(p2 i'' i' i, 1)] []
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [q0, p2, *])

theorem z5 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U4 hp i'' i' i) (U5 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  exact monicStep hn hp (bokutShiaoRelation i' i i'') (bokutShiaoRelation_mem hn hp hi (by omega))
    (outer_hrel hi hi'') (outer_hlm hi hi'')
    (by simp [*])
    [] [(q2 i'' i' i, -(hp.q - hp.q⁻¹)), (q3 i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [p2, q2, q3, *])

theorem z6 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U5 hp i'' i' i) (U6 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i'') (bokutShiaoRelation_mem hn hp hi'' (le_refl _))
    (BraidSelfOverlap.bs_hrel i'' i' hi'') (BraidSelfOverlap.bs_hlm i'' i' hi'')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [] [(q2 i'' i' i, -(hp.q - hp.q⁻¹)), (q3 i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [p3, q2, q3, *])

theorem z8 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U7 hp i'' i' i) (U8 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [(p5 i'' i' i, hp.q - hp.q⁻¹), (p6 i'' i' i, 1)] [(q3 i'' i' i, -1)]
    [(⟨i'⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hh) (by rfl) (by rfl)
    (by simp [q2, p5, p6, q3, *])

theorem z9 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U8 hp i'' i' i) (U9 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (bokutShiaoRelation i' i i'') (bokutShiaoRelation_mem hn hp hi (by omega))
    (outer_hrel hi hi'') (outer_hlm hi hi'')
    (by simp [*])
    [(p5 i'' i' i, hp.q - hp.q⁻¹), (p6 i'' i' i, 1)] [(q3 i'' i' i, -1)]
    [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [] _ _ (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hh) (by rfl) (by rfl)
    (by simp [q4, p5, p6, q3, *])

theorem z10 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U9 hp i'' i' i) (U10 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (bokutShiaoRelation i'' i' i'') (bokutShiaoRelation_mem hn hp hi'' (le_refl _))
    (BraidSelfOverlap.bs_hrel i'' i' hi'') (BraidSelfOverlap.bs_hlm i'' i' hi'')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [(p5 i'' i' i, hp.q - hp.q⁻¹), (p6 i'' i' i, 1)] [(q3 i'' i' i, -1)]
    [] [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] _ _ (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hh) (by rfl) (by rfl)
    (by simp [q5, p5, p6, q3, *])

theorem z11 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U10 hp i'' i' i) (U11 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [] [(p6 i'' i' i, 1), (q6 i'' i' i, -(hp.q - hp.q⁻¹)), (q3 i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] _ _ (hp.q - hp.q⁻¹) hh (by rfl) (by rfl)
    (by simp [p5, p6, q6, q3, *])

theorem z12 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U11 hp i'' i' i) (U12 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [(q6 i'' i' i, hp.q - hp.q⁻¹), (p6 i'' i' i, 1), (q6 i'' i' i, -(hp.q - hp.q⁻¹))] []
    [(⟨i'⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [q3, q6, p6, *])

theorem z13 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U12 hp i'' i' i) (U13 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  exact monicStep hn hp (bokutShiaoRelation i' i i') (bokutShiaoRelation_mem hn hp hi (le_refl _))
    (BraidSelfOverlap.bs_hrel i' i hi) (BraidSelfOverlap.bs_hlm i' i hi)
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [(q6 i'' i' i, hp.q - hp.q⁻¹), (p6 i'' i' i, 1), (q6 i'' i' i, -(hp.q - hp.q⁻¹))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [q7, q6, p6, *])

theorem z14 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U13 hp i'' i' i) (U14 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i'') (bokutShiaoRelation_mem hn hp hi'' (le_refl _))
    (BraidSelfOverlap.bs_hrel i'' i' hi'') (BraidSelfOverlap.bs_hlm i'' i' hi'')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [(q6 i'' i' i, hp.q - hp.q⁻¹), (p6 i'' i' i, 1), (q6 i'' i' i, -(hp.q - hp.q⁻¹))] []
    [] [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [q8, q6, p6, *])

theorem z15 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U14 hp i'' i' i) (U15 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hzy := hyz.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [(q6 i'' i' i, hp.q - hp.q⁻¹)] [(q6 i'' i' i, -(hp.q - hp.q⁻¹)), (q9 i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [p6, q6, q9, *])
end

section

variable (hp : HeckeParams) {i'' i' i : Fin n}

/-- Step 4 — the quadratic rule at `i − 2`, on the square the braid step left. -/
theorem z4 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U3 hp i'' i' i) (U4 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm; have hzx := hxz.symm; have hzy := hyz.symm
  have hv : (U3 hp i'' i' i).coeff
      ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
        ++ (heckeRelation i'' hp).lm (heckeOrder n) ++ [(⟨i⟩ : HeckeGen n)]) = -1 := by
    rw [heckeRelation_lm, show ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
        (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] ++ [(⟨i''⟩ : HeckeGen n), ⟨i''⟩]
        ++ [(⟨i⟩ : HeckeGen n)]) = q1 i'' i' i from rfl]
    simp [U3, p2, q1, AlgElement.ofTerms_coeff, *]
  refine ⟨heckeRelation i'' hp, heckeRelation_mem hn hp i'',
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)],
    [(⟨i⟩ : HeckeGen n)], -1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (-1 : ℝ) * (AlgElement.contextMul
      [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
      (heckeRelation i'' hp).relation [(⟨i⟩ : HeckeGen n)]).coeff m
    simp only [U3, U4, p2, q1, q2, q3, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons,
      List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 7 — the quadratic rule at `i − 2` again, on the trailing square. -/
theorem z7 (hn : 0 < n) (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (U6 hp i'' i' i) (U7 hp i'' i' i) := by
  obtain ⟨hxy, hxz, hyz⟩ := gen3_ne hi hi''
  have hyx := hxy.symm; have hzx := hxz.symm; have hzy := hyz.symm
  have hv : (U6 hp i'' i' i).coeff
      ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
        (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
        ++ (heckeRelation i'' hp).lm (heckeOrder n) ++ []) = 1 := by
    rw [heckeRelation_lm, show ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n),
        (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
        ++ [(⟨i''⟩ : HeckeGen n), ⟨i''⟩] ++ []) = p4 i'' i' i from rfl]
    simp [U6, p4, q2, q3, AlgElement.ofTerms_coeff, *]
  refine ⟨heckeRelation i'' hp, heckeRelation_mem hn hp i'',
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
     (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)], [], 1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (1 : ℝ) * (AlgElement.contextMul
      [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
       (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
      (heckeRelation i'' hp).relation []).coeff m
    simp only [U6, U7, p4, p5, p6, q2, q3, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.append_nil, List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons,
      List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

end

theorem U15_isZero (hp : HeckeParams) (i'' i' i : Fin n) : (U15 hp i'' i' i).isZero := by
  intro m
  simp only [U15, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- The composition of `bokutShiaoRelation i' i i''` with itself, overlapping in
the trailing `σᵢ`. -/
noncomputable def oc (i'' i' i : Fin n) (hi : i'.val + 1 = i.val)
    (hi'' : i''.val + 1 = i'.val) : OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := bokutShiaoRelation i' i i''
  rule₂ := bokutShiaoRelation i' i i''
  left := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
  overlap := [⟨i⟩]
  right := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
  lm₁_decomp := by rw [outer_hlm hi hi'']; rfl
  lm₂_decomp := by rw [outer_hlm hi hi'']; rfl
  overlap_nonempty := by simp

/-- **The S-polynomial.** -/
theorem oc_spoly_coeff (hp : HeckeParams) {i'' i' i : Fin n} (hi : i'.val + 1 = i.val)
    (hi'' : i''.val + 1 = i'.val) (m : Monomial (HeckeGen n)) :
    (oc i'' i' i hi hi'').spoly.coeff m = (U0 hp i'' i' i).coeff m := by
  show (bokutShiaoRelation i' i i'').lc (heckeOrder n)
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i i'').relation
          [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]).coeff m
    - (bokutShiaoRelation i' i i'').lc (heckeOrder n)
      * (AlgElement.contextMul
          [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
          (bokutShiaoRelation i' i i'').relation []).coeff m
    = _
  rw [bokutShiaoRelation_lc hi (by omega), one_mul, one_mul,
    AlgElement.contextMul_coeff_congr []
      [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
      (outer_hrel hi hi'') m,
    AlgElement.contextMul_coeff_congr
      [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] []
      (outer_hrel hi hi'') m]
  simp only [U0, p0, q0, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
    List.map_nil, List.nil_append, List.append_nil, List.cons_append,
    AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Fifteen steps, to zero.** -/
theorem resolves (hp : HeckeParams) {i'' i' i : Fin n} (hn : 0 < n)
    (hi : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i'' i' i hi hi'').spoly nf ∧ nf.isZero := by
  refine reducesToZero_congr ⟨U15 hp i'' i' i,
    ⟨(MultiStepReduction.refl (U0 hp i'' i' i))
      |>.step (z1 hp hn hi hi'') |>.step (z2 hp hn hi hi'') |>.step (z3 hp hn hi hi'')
      |>.step (z4 hp hn hi hi'') |>.step (z5 hp hn hi hi'') |>.step (z6 hp hn hi hi'')
      |>.step (z7 hp hn hi hi'') |>.step (z8 hp hn hi hi'') |>.step (z9 hp hn hi hi'')
      |>.step (z10 hp hn hi hi'') |>.step (z11 hp hn hi hi'') |>.step (z12 hp hn hi hi'')
      |>.step (z13 hp hn hi hi'') |>.step (z14 hp hn hi hi'') |>.step (z15 hp hn hi hi''),
      isNormalForm_of_isZero (U15_isZero hp i'' i' i)⟩, U15_isZero hp i'' i' i⟩ ?_
  intro m
  exact oc_spoly_coeff hp hi hi'' m

end BokutShiaoCorner

/-! ## §4aa  Depths `i−3` and `i−2` — the unequal corner, and the cheapest of the three

Of the three that remain after §4z this is the one to take next, because
**nothing in it is quadratic**: all fifteen steps apply a two-word monic rule and
every stage has exactly two terms, so `monicStep` discharges the whole chain and
`h` never appears. `(a, b) = (3, 2)`, i.e. `j₁ = i − 3` and `j₂ = i − 2`.

Writing `x = σᵢ`, `y = σᵢ₋₁`, `z = σᵢ₋₂`, `w = σᵢ₋₃`, both depths are pinned, so
`descWord i j₁ = xyzw` and `descWord i−1 j₂ = yz` and every word is an explicit
eight-letter list in four generators:

    spoly = x y z w y x y z  −  y x y z w y z x

Seven steps take the second term to `z y z w x y z w`, eight take the first to
the same word, and they cancel. Six rules occur — the Bokut–Shiao rule at
`(i−2,i−1,i−3)`, the braid rule at `(i−3,i−2)`, the three far-commutations
`σᵢσᵢ₋₂`, `σᵢσᵢ₋₃`, `σᵢ₋₁σᵢ₋₃`, and the composition's own first rule.

**Why the count is 15 and not less.** Reducing the two terms *separately* to
normal form takes 8 and 7 steps, and 8 + 7 = 15 — the chain is exactly the two
reductions, with no shared intermediate to cut. That holds for all four corner
cases (`(2,2)`: 7+8=15, `(2,3)`: 9+10=19, `(3,3)`: 12+13=25), so there is no
shorter route to be found by looking for a common midpoint; an earlier guess that
one existed was wrong.

Every distinctness is a first, second, third or fourth letter among four
generators. -/

namespace BokutShiaoCornerUneq

variable {n : ℕ}

/-- The four generators in play are pairwise distinct. -/
theorem gen4_ne {i''' i'' i' i : Fin n} (hi' : i'.val + 1 = i.val)
    (hi'' : i''.val + 1 = i'.val) (hi''' : i'''.val + 1 = i''.val) :
    (⟨i⟩ : HeckeGen n) ≠ ⟨i'⟩ ∧ (⟨i⟩ : HeckeGen n) ≠ ⟨i''⟩
      ∧ (⟨i⟩ : HeckeGen n) ≠ ⟨i'''⟩ ∧ (⟨i'⟩ : HeckeGen n) ≠ ⟨i''⟩
      ∧ (⟨i'⟩ : HeckeGen n) ≠ ⟨i'''⟩ ∧ (⟨i''⟩ : HeckeGen n) ≠ ⟨i'''⟩ := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    · intro hcon
      have := congrArg HeckeGen.rank hcon
      simp only [HeckeGen.rank] at this
      omega

section

variable {i''' i'' i' i : Fin n}

theorem dw_zw (hi''' : i'''.val + 1 = i''.val) :
    descWord i'' i''' = [(⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] := by
  rw [descWord_cons hi''' (le_refl _), descWord_self]

theorem dw_yzw (hi'' : i''.val + 1 = i'.val) (hi''' : i'''.val + 1 = i''.val) :
    descWord i' i''' = [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] := by
  rw [descWord_cons hi'' (by omega), dw_zw hi''']

theorem dw_xyzw (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    descWord i i''' = [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
      (⟨i'''⟩ : HeckeGen n)] := by
  rw [descWord_cons hi' (by omega), dw_yzw hi'' hi''']

theorem dw_yz (hi'' : i''.val + 1 = i'.val) :
    descWord i' i'' = [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] := by
  rw [descWord_cons hi'' (le_refl _), descWord_self]

/-- The Bokut–Shiao rule with top index `i−1` and bottom `i−3`. -/
theorem bs_yw_hrel (hi'' : i''.val + 1 = i'.val) (hi''' : i'''.val + 1 = i''.val)
    (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i'' i' i''').relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
              (⟨i'⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
              (⟨i'''⟩ : HeckeGen n)], -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i' i''', (1 : ℝ)), (bsWord₂ i'' i' i''', -1)]).coeff v = _
  rw [bsWord₁, dw_yzw hi'' hi''', bsWord₂, dw_zw hi''']
  rfl

theorem bs_yw_hlm (hi'' : i''.val + 1 = i'.val) (hi''' : i'''.val + 1 = i''.val) :
    (bokutShiaoRelation i'' i' i''').lm (heckeOrder n)
      = [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
         (⟨i'⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm hi'' (by omega), bsWord₁, dw_yzw hi'' hi''']
  rfl

/-- The composition's first rule: top `i`, bottom `i−3`. -/
theorem bs_xw_hrel (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i' i i''').relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
              (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n),
              (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)], -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i i''', (1 : ℝ)), (bsWord₂ i' i i''', -1)]).coeff v = _
  rw [bsWord₁, dw_xyzw hi' hi'' hi''', bsWord₂, dw_yzw hi'' hi''']
  rfl

theorem bs_xw_hlm (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    (bokutShiaoRelation i' i i''').lm (heckeOrder n)
      = [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
         (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm hi' (by omega), bsWord₁, dw_xyzw hi' hi'' hi''']
  rfl

/-- The composition's second rule: top `i`, bottom `i−2`. -/
theorem bs_xz_hrel (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i' i i'').relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
              (⟨i⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n),
              (⟨i''⟩ : HeckeGen n)], -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i i'', (1 : ℝ)), (bsWord₂ i' i i'', -1)]).coeff v = _
  rw [bsWord₁, descWord_cons hi' (by omega), dw_yz hi'', bsWord₂, dw_yz hi'']
  rfl

theorem bs_xz_hlm (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val) :
    (bokutShiaoRelation i' i i'').lm (heckeOrder n)
      = [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
         (⟨i⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm hi' (by omega), bsWord₁, descWord_cons hi' (by omega),
    dw_yz hi'']
  rfl

end

def V0 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def V1 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def V2 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def V3 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def V4 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def V5 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def V6 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def V7 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def V8 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def U0 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def U1 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def U2 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def U3 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def U4 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def U5 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def U6 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def U7 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]

noncomputable def T0 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V0 i''' i'' i' i, (1 : ℝ)), (U0 i''' i'' i' i, -1)]

noncomputable def T1 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V1 i''' i'' i' i, (1 : ℝ)), (U0 i''' i'' i' i, -1)]

noncomputable def T2 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i, (1 : ℝ)), (U0 i''' i'' i' i, -1)]

noncomputable def T3 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i, (1 : ℝ)), (U1 i''' i'' i' i, -1)]

noncomputable def T4 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i, (1 : ℝ)), (U2 i''' i'' i' i, -1)]

noncomputable def T5 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i, (1 : ℝ)), (U3 i''' i'' i' i, -1)]

noncomputable def T6 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i, (1 : ℝ)), (U4 i''' i'' i' i, -1)]

noncomputable def T7 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i, (1 : ℝ)), (U5 i''' i'' i' i, -1)]

noncomputable def T8 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i, (1 : ℝ)), (U6 i''' i'' i' i, -1)]

noncomputable def T9 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i, (1 : ℝ)), (U7 i''' i'' i' i, -1)]

noncomputable def T10 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V3 i''' i'' i' i, (1 : ℝ)), (U7 i''' i'' i' i, -1)]

noncomputable def T11 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V4 i''' i'' i' i, (1 : ℝ)), (U7 i''' i'' i' i, -1)]

noncomputable def T12 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V5 i''' i'' i' i, (1 : ℝ)), (U7 i''' i'' i' i, -1)]

noncomputable def T13 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V6 i''' i'' i' i, (1 : ℝ)), (U7 i''' i'' i' i, -1)]

noncomputable def T14 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V7 i''' i'' i' i, (1 : ℝ)), (U7 i''' i'' i' i, -1)]

noncomputable def T15 (i''' i'' i' i : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V8 i''' i'' i' i, (1 : ℝ)), (U7 i''' i'' i' i, -1)]

section

variable (hp : HeckeParams) {i''' i'' i' i : Fin n}

theorem s1 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T0 i''' i'' i' i) (T1 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i''') (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (bs_yw_hrel hi'' hi''') (bs_yw_hlm hi'' hi''')
    (by simp [*])
    [] [(U0 i''' i'' i' i, -1)]
    [(⟨i⟩ : HeckeGen n)] [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [V0, U0, *])

theorem s2 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T1 i''' i'' i' i) (T2 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [] [(U0 i''' i'' i' i, -1)]
    [] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [V1, U0, *])

theorem s3 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T2 i''' i'' i' i) (T3 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i''') (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (bs_yw_hrel hi'' hi''') (bs_yw_hlm hi'' hi''')
    (by simp [*])
    [(V2 i''' i'' i' i, (1 : ℝ))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [U0, V2, *])

theorem s4 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T3 i''' i'' i' i) (T4 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i''' i'' i''') (bokutShiaoRelation_mem hn hp hi''' (le_refl _))
    (BraidSelfOverlap.bs_hrel i''' i'' hi''') (BraidSelfOverlap.bs_hlm i''' i'' hi''')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [(V2 i''' i'' i' i, (1 : ℝ))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] [(⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [U1, V2, *])

theorem s5 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T4 i''' i'' i' i) (T5 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i' i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i') (farCommRelation_lm i' i''' (by omega))
    (by simp [*])
    [(V2 i''' i'' i' i, (1 : ℝ))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [U2, V2, *])

theorem s6 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T5 i''' i'' i' i) (T6 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [(V2 i''' i'' i' i, (1 : ℝ))] []
    [(⟨i'⟩ : HeckeGen n)] [(⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [U3, V2, *])

theorem s7 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T6 i''' i'' i' i) (T7 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i) (farCommRelation_lm i i''' (by omega))
    (by simp [*])
    [(V2 i''' i'' i' i, (1 : ℝ))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [U4, V2, *])

theorem s8 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T7 i''' i'' i' i) (T8 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i' i i''') (bokutShiaoRelation_mem hn hp hi' (by omega))
    (bs_xw_hrel hi' hi'' hi''') (bs_xw_hlm hi' hi'' hi''')
    (by simp [*])
    [(V2 i''' i'' i' i, (1 : ℝ))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] [] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [U5, V2, *])

theorem s9 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T8 i''' i'' i' i) (T9 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i''') (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (bs_yw_hrel hi'' hi''') (bs_yw_hlm hi'' hi''')
    (by simp [*])
    [(V2 i''' i'' i' i, (1 : ℝ))] []
    [] [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [U6, V2, *])

theorem s10 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T9 i''' i'' i' i) (T10 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i' i i''') (bokutShiaoRelation_mem hn hp hi' (by omega))
    (bs_xw_hrel hi' hi'' hi''') (bs_xw_hlm hi' hi'' hi''')
    (by simp [*])
    [] [(U7 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [V2, U7, *])

theorem s11 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T10 i''' i'' i' i) (T11 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i''') (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (bs_yw_hrel hi'' hi''') (bs_yw_hlm hi'' hi''')
    (by simp [*])
    [] [(U7 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [V3, U7, *])

theorem s12 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T11 i''' i'' i' i) (T12 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i''' i'' i''') (bokutShiaoRelation_mem hn hp hi''' (le_refl _))
    (BraidSelfOverlap.bs_hrel i''' i'' hi''') (BraidSelfOverlap.bs_hlm i''' i'' hi''')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [] [(U7 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] [] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [V4, U7, *])

theorem s13 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T12 i''' i'' i' i) (T13 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i' i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i') (farCommRelation_lm i' i''' (by omega))
    (by simp [*])
    [] [(U7 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [V5, U7, *])

theorem s14 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T13 i''' i'' i' i) (T14 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [] [(U7 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] [(⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [V6, U7, *])

theorem s15 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T14 i''' i'' i' i) (T15 i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i) (farCommRelation_lm i i''' (by omega))
    (by simp [*])
    [] [(U7 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [V7, U7, *])
end

theorem T15_isZero (i''' i'' i' i : Fin n) : (T15 i''' i'' i' i).isZero := by
  intro m
  simp only [T15, V8, U7, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
  ring

/-- The composition of the rule at depth `i−3` with the rule at depth `i−2`,
overlapping in the trailing `σᵢ`. -/
noncomputable def oc (i''' i'' i' i : Fin n) (hi' : i'.val + 1 = i.val)
    (hi'' : i''.val + 1 = i'.val) (hi''' : i'''.val + 1 = i''.val) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := bokutShiaoRelation i' i i'''
  rule₂ := bokutShiaoRelation i' i i''
  left := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
           (⟨i'''⟩ : HeckeGen n)]
  overlap := [⟨i⟩]
  right := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
  lm₁_decomp := by rw [bs_xw_hlm hi' hi'' hi''']; rfl
  lm₂_decomp := by rw [bs_xz_hlm hi' hi'']; rfl
  overlap_nonempty := by simp

/-- **The S-polynomial.** -/
theorem oc_spoly_coeff {i''' i'' i' i : Fin n} (hi' : i'.val + 1 = i.val)
    (hi'' : i''.val + 1 = i'.val) (hi''' : i'''.val + 1 = i''.val)
    (m : Monomial (HeckeGen n)) :
    (oc i''' i'' i' i hi' hi'' hi''').spoly.coeff m = (T0 i''' i'' i' i).coeff m := by
  show (bokutShiaoRelation i' i i'').lc (heckeOrder n)
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i i''').relation
          [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]).coeff m
    - (bokutShiaoRelation i' i i''').lc (heckeOrder n)
      * (AlgElement.contextMul
          [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
           (⟨i'''⟩ : HeckeGen n)]
          (bokutShiaoRelation i' i i'').relation []).coeff m
    = _
  rw [bokutShiaoRelation_lc hi' (by omega), bokutShiaoRelation_lc hi' (by omega),
    one_mul, one_mul,
    AlgElement.contextMul_coeff_congr []
      [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
      (bs_xw_hrel hi' hi'' hi''') m,
    AlgElement.contextMul_coeff_congr
      [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
       (⟨i'''⟩ : HeckeGen n)] [] (bs_xz_hrel hi' hi'') m]
  simp only [T0, V0, U0, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
    List.map_nil, List.nil_append, List.append_nil, List.cons_append,
    AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Fifteen steps, to zero, with no quadratic rule anywhere.** -/
theorem resolves (hp : HeckeParams) {i''' i'' i' i : Fin n} (hn : 0 < n)
    (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i''' i'' i' i hi' hi'' hi''').spoly nf ∧ nf.isZero := by
  refine reducesToZero_congr ⟨T15 i''' i'' i' i,
    ⟨(MultiStepReduction.refl (T0 i''' i'' i' i))
      |>.step (s1 hp hn hi' hi'' hi''') |>.step (s2 hp hn hi' hi'' hi''')
      |>.step (s3 hp hn hi' hi'' hi''') |>.step (s4 hp hn hi' hi'' hi''')
      |>.step (s5 hp hn hi' hi'' hi''') |>.step (s6 hp hn hi' hi'' hi''')
      |>.step (s7 hp hn hi' hi'' hi''') |>.step (s8 hp hn hi' hi'' hi''')
      |>.step (s9 hp hn hi' hi'' hi''') |>.step (s10 hp hn hi' hi'' hi''')
      |>.step (s11 hp hn hi' hi'' hi''') |>.step (s12 hp hn hi' hi'' hi''')
      |>.step (s13 hp hn hi' hi'' hi''') |>.step (s14 hp hn hi' hi'' hi''')
      |>.step (s15 hp hn hi' hi'' hi'''),
      isNormalForm_of_isZero (T15_isZero i''' i'' i' i)⟩, T15_isZero i''' i'' i' i⟩ ?_
  intro m
  exact oc_spoly_coeff hi' hi'' hi''' m

end BokutShiaoCornerUneq

/-! ## §4ab  Depths `i−2` and `i−3` — the mirror of §4aa, and not its mirror image

`(a, b) = (2, 3)`: the depths of §4aa the other way round. That does **not**
transpose the chain — §4aa needs no quadratic rule at all and runs in fifteen
steps, this one needs two and runs in nineteen. The asymmetry is real: the two
depths enter the S-polynomial in different positions,

    spoly = D₁ σᵢ₋₁ σᵢ E₂  −  σᵢ₋₁ D₁ E₂ σᵢ

so swapping them is not a symmetry of the problem.

With `x = σᵢ`, `y = σᵢ₋₁`, `z = σᵢ₋₂`, `w = σᵢ₋₃`, here `D₁ = xyz` and
`E₂ = yzw`:

    spoly = x y z y x y z w  −  y x y z y z w x

Seventeen of the nineteen steps apply a two-word monic rule and go through
`monicStep`; the two quadratic ones, at steps 4 and 7, are written out and are
where `h` enters. It leaves at step 11, where `z y x z y z w` and `z y z x y z w`
carry `h` with opposite signs — the same cancellation shape as §4z, and again the
pair is carried unmerged rather than costing a step.

Nine rules occur: the braid rule at each of the three adjacent pairs, all three
far-commutations, the Bokut–Shiao rule at `(i−2,i−1,i−3)`, and the composition's
own two rules. Every helper they need was already proved in §4aa. -/

namespace BokutShiaoCornerLow

variable {n : ℕ}

def A0 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def A1 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def A2 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def A3 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def A4 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def A5 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def A6 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def A7 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
def A8 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
def B0 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def B1 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def B2 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def B3 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def B4 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def B5 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def B6 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def B7 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def B8 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def B9 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def B10 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
def B11 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]

noncomputable def S0 (_hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(A0 i''' i'' i' i, (1 : ℝ)),
     (B0 i''' i'' i' i, -1)]

noncomputable def S1 (_hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(A1 i''' i'' i' i, (1 : ℝ)),
     (B0 i''' i'' i' i, -1)]

noncomputable def S2 (_hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(A2 i''' i'' i' i, (1 : ℝ)),
     (B0 i''' i'' i' i, -1)]

noncomputable def S3 (_hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(A2 i''' i'' i' i, (1 : ℝ)),
     (B1 i''' i'' i' i, -1)]

noncomputable def S4 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(A2 i''' i'' i' i, (1 : ℝ)),
     (B2 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B3 i''' i'' i' i, -1)]

noncomputable def S5 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(A3 i''' i'' i' i, (1 : ℝ)),
     (B2 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B3 i''' i'' i' i, -1)]

noncomputable def S6 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(A4 i''' i'' i' i, (1 : ℝ)),
     (B2 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B3 i''' i'' i' i, -1)]

noncomputable def S7 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(A5 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A6 i''' i'' i' i, 1),
     (B2 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B3 i''' i'' i' i, -1)]

noncomputable def S8 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(A5 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A6 i''' i'' i' i, 1),
     (B4 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B3 i''' i'' i' i, -1)]

noncomputable def S9 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(A5 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A6 i''' i'' i' i, 1),
     (B5 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B3 i''' i'' i' i, -1)]

noncomputable def S10 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(A5 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A6 i''' i'' i' i, 1),
     (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B3 i''' i'' i' i, -1)]

noncomputable def S11 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A6 i''' i'' i' i, 1),
     (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B3 i''' i'' i' i, -1)]

noncomputable def S12 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A6 i''' i'' i' i, 1),
     (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B7 i''' i'' i' i, -1)]

noncomputable def S13 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A6 i''' i'' i' i, 1),
     (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B8 i''' i'' i' i, -1)]

noncomputable def S14 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A6 i''' i'' i' i, 1),
     (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B9 i''' i'' i' i, -1)]

noncomputable def S15 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A6 i''' i'' i' i, 1),
     (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B10 i''' i'' i' i, -1)]

noncomputable def S16 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A6 i''' i'' i' i, 1),
     (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B11 i''' i'' i' i, -1)]

noncomputable def S17 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A7 i''' i'' i' i, 1),
     (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B11 i''' i'' i' i, -1)]

noncomputable def S18 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (A8 i''' i'' i' i, 1),
     (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B11 i''' i'' i' i, -1)]

noncomputable def S19 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (B11 i''' i'' i' i, 1),
     (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (B11 i''' i'' i' i, -1)]

section

variable (hp : HeckeParams) {i''' i'' i' i : Fin n}

theorem c1 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S0 hp i''' i'' i' i) (S1 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i'') (bokutShiaoRelation_mem hn hp hi'' (le_refl _))
    (BraidSelfOverlap.bs_hrel i'' i' hi'') (BraidSelfOverlap.bs_hlm i'' i' hi'')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [] [(B0 i''' i'' i' i, -1)]
    [(⟨i⟩ : HeckeGen n)] [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (1 : ℝ) one_ne_zero (by rfl) (by rfl)
    (by simp [A0, B0, *])

theorem c2 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S1 hp i''' i'' i' i) (S2 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [] [(B0 i''' i'' i' i, -1)]
    [] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (1 : ℝ) one_ne_zero (by rfl) (by rfl)
    (by simp [A1, B0, *])

theorem c3 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S2 hp i''' i'' i' i) (S3 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i'') (bokutShiaoRelation_mem hn hp hi'' (le_refl _))
    (BraidSelfOverlap.bs_hrel i'' i' hi'') (BraidSelfOverlap.bs_hlm i'' i' hi'')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [(A2 i''' i'' i' i, (1 : ℝ))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [B0, A2, *])

theorem c5 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S4 hp i''' i'' i' i) (S5 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i' i i'') (bokutShiaoRelation_mem hn hp hi' (by omega))
    (BokutShiaoCornerUneq.bs_xz_hrel hi' hi'') (BokutShiaoCornerUneq.bs_xz_hlm hi' hi'')
    (by simp [*])
    [] [(B2 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (B3 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (1 : ℝ) one_ne_zero (by rfl) (by rfl)
    (by simp [A2, B2, B3, *])

theorem c6 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S5 hp i''' i'' i' i) (S6 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i'') (bokutShiaoRelation_mem hn hp hi'' (le_refl _))
    (BraidSelfOverlap.bs_hrel i'' i' hi'') (BraidSelfOverlap.bs_hlm i'' i' hi'')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [] [(B2 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (B3 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (1 : ℝ) one_ne_zero (by rfl) (by rfl)
    (by simp [A3, B2, B3, *])

theorem c8 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S7 hp i''' i'' i' i) (S8 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [(A5 i''' i'' i' i, hp.q - hp.q⁻¹), (A6 i''' i'' i' i, 1)] [(B3 i''' i'' i' i, -1)]
    [(⟨i'⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hh) (by rfl) (by rfl)
    (by simp [B2, A5, A6, B3, *])

theorem c9 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S8 hp i''' i'' i' i) (S9 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (bokutShiaoRelation i' i i''') (bokutShiaoRelation_mem hn hp hi' (by omega))
    (BokutShiaoCornerUneq.bs_xw_hrel hi' hi'' hi''') (BokutShiaoCornerUneq.bs_xw_hlm hi' hi'' hi''')
    (by simp [*])
    [(A5 i''' i'' i' i, hp.q - hp.q⁻¹), (A6 i''' i'' i' i, 1)] [(B3 i''' i'' i' i, -1)]
    [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [] _ _ (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hh) (by rfl) (by rfl)
    (by simp [B4, A5, A6, B3, *])

theorem c10 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S9 hp i''' i'' i' i) (S10 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (bokutShiaoRelation i'' i' i'') (bokutShiaoRelation_mem hn hp hi'' (le_refl _))
    (BraidSelfOverlap.bs_hrel i'' i' hi'') (BraidSelfOverlap.bs_hlm i'' i' hi'')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [(A5 i''' i'' i' i, hp.q - hp.q⁻¹), (A6 i''' i'' i' i, 1)] [(B3 i''' i'' i' i, -1)]
    [] [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hh) (by rfl) (by rfl)
    (by simp [B5, A5, A6, B3, *])

theorem c11 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S10 hp i''' i'' i' i) (S11 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [] [(A6 i''' i'' i' i, 1), (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (B3 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (hp.q - hp.q⁻¹) hh (by rfl) (by rfl)
    (by simp [A5, A6, B3, B6, *])

theorem c12 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S11 hp i''' i'' i' i) (S12 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i' i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i') (farCommRelation_lm i' i''' (by omega))
    (by simp [*])
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹), (A6 i''' i'' i' i, 1), (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [B3, A6, B6, *])

theorem c13 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S12 hp i''' i'' i' i) (S13 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹), (A6 i''' i'' i' i, 1), (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹))] []
    [(⟨i'⟩ : HeckeGen n)] [(⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [B7, A6, B6, *])

theorem c14 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S13 hp i''' i'' i' i) (S14 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i) (farCommRelation_lm i i''' (by omega))
    (by simp [*])
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹), (A6 i''' i'' i' i, 1), (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [B8, A6, B6, *])

theorem c15 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S14 hp i''' i'' i' i) (S15 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i' i i') (bokutShiaoRelation_mem hn hp hi' (le_refl _))
    (BraidSelfOverlap.bs_hrel i' i hi') (BraidSelfOverlap.bs_hlm i' i hi')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹), (A6 i''' i'' i' i, 1), (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] [] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [B9, A6, B6, *])

theorem c16 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S15 hp i''' i'' i' i) (S16 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i''') (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (BokutShiaoCornerUneq.bs_yw_hrel hi'' hi''') (BokutShiaoCornerUneq.bs_yw_hlm hi'' hi''')
    (by simp [*])
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹), (A6 i''' i'' i' i, 1), (B6 i''' i'' i' i, -(hp.q - hp.q⁻¹))] []
    [] [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [B10, A6, B6, *])

theorem c17 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S16 hp i''' i'' i' i) (S17 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i' i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i') (farCommRelation_lm i' i''' (by omega))
    (by simp [*])
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹)] [(B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (B11 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [A6, B11, B6, *])

theorem c18 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S17 hp i''' i'' i' i) (S18 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹)] [(B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (B11 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] [(⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [A7, B11, B6, *])

theorem c19 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S18 hp i''' i'' i' i) (S19 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i) (farCommRelation_lm i i''' (by omega))
    (by simp [*])
    [(B6 i''' i'' i' i, hp.q - hp.q⁻¹)] [(B6 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (B11 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [A8, B11, B6, *])
end

section

variable (hp : HeckeParams) {i''' i'' i' i : Fin n}

/-- Step 4 — the quadratic rule at `i−2`, on the square the braid step left. -/
theorem c4 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S3 hp i''' i'' i' i) (S4 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzy := hyz.symm
  have hv : (S3 hp i''' i'' i' i).coeff
      ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
        ++ (heckeRelation i'' hp).lm (heckeOrder n)
        ++ [(⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]) = -1 := by
    rw [heckeRelation_lm, show ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
        (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] ++ [(⟨i''⟩ : HeckeGen n), ⟨i''⟩]
        ++ [(⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]) = B1 i''' i'' i' i from rfl]
    simp [S3, A2, B1, AlgElement.ofTerms_coeff, *]
  refine ⟨heckeRelation i'' hp, heckeRelation_mem hn hp i'',
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)],
    [(⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)], -1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (-1 : ℝ) * (AlgElement.contextMul
      [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
      (heckeRelation i'' hp).relation
      [(⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]).coeff m
    simp only [S3, S4, A2, B1, B2, B3, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons,
      List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 7 — the quadratic rule at `i−2` again, on the other square. -/
theorem c7 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (S6 hp i''' i'' i' i) (S7 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzy := hyz.symm
  have hv : (S6 hp i''' i'' i' i).coeff
      ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
        (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
        ++ (heckeRelation i'' hp).lm (heckeOrder n) ++ [(⟨i'''⟩ : HeckeGen n)]) = 1 := by
    rw [heckeRelation_lm, show ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n),
        (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
        ++ [(⟨i''⟩ : HeckeGen n), ⟨i''⟩] ++ [(⟨i'''⟩ : HeckeGen n)]) = A4 i''' i'' i' i
      from rfl]
    simp [S6, A4, B2, B3, AlgElement.ofTerms_coeff, *]
  refine ⟨heckeRelation i'' hp, heckeRelation_mem hn hp i'',
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
     (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)], [(⟨i'''⟩ : HeckeGen n)], 1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (1 : ℝ) * (AlgElement.contextMul
      [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
       (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]
      (heckeRelation i'' hp).relation [(⟨i'''⟩ : HeckeGen n)]).coeff m
    simp only [S6, S7, A4, A5, A6, B2, B3, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons,
      List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

end

theorem S19_isZero (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    (S19 hp i''' i'' i' i).isZero := by
  intro m
  simp only [S19, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- The composition of the rule at depth `i−2` with the rule at depth `i−3`. -/
noncomputable def oc (i''' i'' i' i : Fin n) (hi' : i'.val + 1 = i.val)
    (hi'' : i''.val + 1 = i'.val) (hi''' : i'''.val + 1 = i''.val) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := bokutShiaoRelation i' i i''
  rule₂ := bokutShiaoRelation i' i i'''
  left := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
  overlap := [⟨i⟩]
  right := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
            (⟨i⟩ : HeckeGen n)]
  lm₁_decomp := by rw [BokutShiaoCornerUneq.bs_xz_hlm hi' hi'']; rfl
  lm₂_decomp := by rw [BokutShiaoCornerUneq.bs_xw_hlm hi' hi'' hi''']; rfl
  overlap_nonempty := by simp

/-- **The S-polynomial.** -/
theorem oc_spoly_coeff (hp : HeckeParams) {i''' i'' i' i : Fin n}
    (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (m : Monomial (HeckeGen n)) :
    (oc i''' i'' i' i hi' hi'' hi''').spoly.coeff m = (S0 hp i''' i'' i' i).coeff m := by
  show (bokutShiaoRelation i' i i''').lc (heckeOrder n)
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i i'').relation
          [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
           (⟨i⟩ : HeckeGen n)]).coeff m
    - (bokutShiaoRelation i' i i'').lc (heckeOrder n)
      * (AlgElement.contextMul
          [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
          (bokutShiaoRelation i' i i''').relation []).coeff m
    = _
  rw [bokutShiaoRelation_lc hi' (by omega), bokutShiaoRelation_lc hi' (by omega),
    one_mul, one_mul,
    AlgElement.contextMul_coeff_congr []
      [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
       (⟨i⟩ : HeckeGen n)] (BokutShiaoCornerUneq.bs_xz_hrel hi' hi'') m,
    AlgElement.contextMul_coeff_congr
      [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] []
      (BokutShiaoCornerUneq.bs_xw_hrel hi' hi'' hi''') m]
  simp only [S0, A0, B0, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
    List.map_nil, List.nil_append, List.append_nil, List.cons_append,
    AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Nineteen steps, to zero.** -/
theorem resolves (hp : HeckeParams) {i''' i'' i' i : Fin n} (hn : 0 < n)
    (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i''' i'' i' i hi' hi'' hi''').spoly nf ∧ nf.isZero := by
  refine reducesToZero_congr ⟨S19 hp i''' i'' i' i,
    ⟨(MultiStepReduction.refl (S0 hp i''' i'' i' i))
      |>.step (c1 hp hn hi' hi'' hi''') |>.step (c2 hp hn hi' hi'' hi''')
      |>.step (c3 hp hn hi' hi'' hi''') |>.step (c4 hp hn hi' hi'' hi''')
      |>.step (c5 hp hn hi' hi'' hi''') |>.step (c6 hp hn hi' hi'' hi''')
      |>.step (c7 hp hn hi' hi'' hi''') |>.step (c8 hp hn hi' hi'' hi''')
      |>.step (c9 hp hn hi' hi'' hi''') |>.step (c10 hp hn hi' hi'' hi''')
      |>.step (c11 hp hn hi' hi'' hi''') |>.step (c12 hp hn hi' hi'' hi''')
      |>.step (c13 hp hn hi' hi'' hi''') |>.step (c14 hp hn hi' hi'' hi''')
      |>.step (c15 hp hn hi' hi'' hi''') |>.step (c16 hp hn hi' hi'' hi''')
      |>.step (c17 hp hn hi' hi'' hi''') |>.step (c18 hp hn hi' hi'' hi''')
      |>.step (c19 hp hn hi' hi'' hi'''),
      isNormalForm_of_isZero (S19_isZero hp i''' i'' i' i)⟩, S19_isZero hp i''' i'' i' i⟩ ?_
  intro m
  exact oc_spoly_coeff hp hi' hi'' hi''' m

end BokutShiaoCornerLow

/-! ## §4ac  Both depths at `i−3` — the last composition, and the longest

`(a, b) = (3, 3)`, twenty-five steps: the largest single obligation in the arc,
and the one that closes the `n = 4` enumeration. Structurally it is §4z at one
more level of depth — the Bokut–Shiao rule against itself, both depths pinned at
`i − 3` — and it inherits §4z's shape exactly: two quadratic steps, an `h` that
enters there and cancels in the middle, and everything else a two-word monic
rule.

With `x = σᵢ`, `y = σᵢ₋₁`, `z = σᵢ₋₂`, `w = σᵢ₋₃`, `descWord i j₁ = xyzw` and
`descWord i−1 j₂ = yzw`:

    spoly = x y z w y x y z w  −  y x y z w y z w x

Twenty-three of the twenty-five steps go through `monicStep`; the two quadratic
ones are at steps 5 and 9, both at `σᵢ₋₃`, and `h` cancels at step 17 where
`z y z x w y z w` and `z y z w x y z w` meet with opposite signs.

Its length is not a sign of extra difficulty — reducing the two terms separately
takes 12 and 13 steps, and 12 + 13 = 25. Every corner case is exactly the sum of
its two reductions; this one just has the longest pair. -/

namespace BokutShiaoCornerDeep

variable {n : ℕ}

def C0 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def C1 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def C2 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def C3 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def C4 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def C5 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def C6 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def C7 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def C8 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def C9 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def C10 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def C11 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def D0 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def D1 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def D2 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def D3 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def D4 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def D5 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def D6 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def D7 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def D8 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def D9 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]
def D10 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def D11 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def D12 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def D13 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def D14 (i''' i'' i' i : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]

noncomputable def T0 (_hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C0 i''' i'' i' i, (1 : ℝ)),
     (D0 i''' i'' i' i, -1)]

noncomputable def T1 (_hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C1 i''' i'' i' i, (1 : ℝ)),
     (D0 i''' i'' i' i, -1)]

noncomputable def T2 (_hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C2 i''' i'' i' i, (1 : ℝ)),
     (D0 i''' i'' i' i, -1)]

noncomputable def T3 (_hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C2 i''' i'' i' i, (1 : ℝ)),
     (D1 i''' i'' i' i, -1)]

noncomputable def T4 (_hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C2 i''' i'' i' i, (1 : ℝ)),
     (D2 i''' i'' i' i, -1)]

noncomputable def T5 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C2 i''' i'' i' i, (1 : ℝ)),
     (D3 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T6 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C3 i''' i'' i' i, (1 : ℝ)),
     (D3 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T7 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C4 i''' i'' i' i, (1 : ℝ)),
     (D3 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T8 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C5 i''' i'' i' i, (1 : ℝ)),
     (D3 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T9 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D3 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T10 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D5 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T11 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D6 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T12 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D7 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T13 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D8 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T14 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C6 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T15 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C8 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T16 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(C9 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T17 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D4 i''' i'' i' i, -1)]

noncomputable def T18 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D10 i''' i'' i' i, -1)]

noncomputable def T19 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D11 i''' i'' i' i, -1)]

noncomputable def T20 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D12 i''' i'' i' i, -1)]

noncomputable def T21 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D13 i''' i'' i' i, -1)]

noncomputable def T22 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C7 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D14 i''' i'' i' i, -1)]

noncomputable def T23 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C10 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D14 i''' i'' i' i, -1)]

noncomputable def T24 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹),
     (C11 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D14 i''' i'' i' i, -1)]

noncomputable def T25 (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹),
     (D14 i''' i'' i' i, 1),
     (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)),
     (D14 i''' i'' i' i, -1)]

section

variable (hp : HeckeParams) {i''' i'' i' i : Fin n}

theorem d1 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T0 hp i''' i'' i' i) (T1 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i''') (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (BokutShiaoCornerUneq.bs_yw_hrel hi'' hi''') (BokutShiaoCornerUneq.bs_yw_hlm hi'' hi''')
    (by simp [*])
    [] [(D0 i''' i'' i' i, -1)]
    [(⟨i⟩ : HeckeGen n)] [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (1 : ℝ) one_ne_zero (by rfl) (by rfl)
    (by simp [C0, D0, *])

theorem d2 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T1 hp i''' i'' i' i) (T2 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [] [(D0 i''' i'' i' i, -1)]
    [] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (1 : ℝ) one_ne_zero (by rfl) (by rfl)
    (by simp [C1, D0, *])

theorem d3 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T2 hp i''' i'' i' i) (T3 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i''') (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (BokutShiaoCornerUneq.bs_yw_hrel hi'' hi''') (BokutShiaoCornerUneq.bs_yw_hlm hi'' hi''')
    (by simp [*])
    [(C2 i''' i'' i' i, (1 : ℝ))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [D0, C2, *])

theorem d4 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T3 hp i''' i'' i' i) (T4 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i''' i'' i''') (bokutShiaoRelation_mem hn hp hi''' (le_refl _))
    (BraidSelfOverlap.bs_hrel i''' i'' hi''') (BraidSelfOverlap.bs_hlm i''' i'' hi''')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [(C2 i''' i'' i' i, (1 : ℝ))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] [(⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [D1, C2, *])

theorem d6 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T5 hp i''' i'' i' i) (T6 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i' i i''') (bokutShiaoRelation_mem hn hp hi' (by omega))
    (BokutShiaoCornerUneq.bs_xw_hrel hi' hi'' hi''') (BokutShiaoCornerUneq.bs_xw_hlm hi' hi'' hi''')
    (by simp [*])
    [] [(D3 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (D4 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (1 : ℝ) one_ne_zero (by rfl) (by rfl)
    (by simp [C2, D3, D4, *])

theorem d7 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T6 hp i''' i'' i' i) (T7 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i''') (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (BokutShiaoCornerUneq.bs_yw_hrel hi'' hi''') (BokutShiaoCornerUneq.bs_yw_hlm hi'' hi''')
    (by simp [*])
    [] [(D3 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (D4 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (1 : ℝ) one_ne_zero (by rfl) (by rfl)
    (by simp [C3, D3, D4, *])

theorem d8 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T7 hp i''' i'' i' i) (T8 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i''' i'' i''') (bokutShiaoRelation_mem hn hp hi''' (le_refl _))
    (BraidSelfOverlap.bs_hrel i''' i'' hi''') (BraidSelfOverlap.bs_hlm i''' i'' hi''')
    (by simp [BraidSelfOverlap.wHi, BraidSelfOverlap.wLo, *])
    [] [(D3 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (D4 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] [(⟨i'''⟩ : HeckeGen n)] _ _ (1 : ℝ) one_ne_zero (by rfl) (by rfl)
    (by simp [C4, D3, D4, *])

theorem d10 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T9 hp i''' i'' i' i) (T10 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (farCommRelation i' i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i') (farCommRelation_lm i' i''' (by omega))
    (by simp [*])
    [(C6 i''' i'' i' i, hp.q - hp.q⁻¹), (C7 i''' i'' i' i, 1)] [(D4 i''' i'' i' i, -1)]
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hh) (by rfl) (by rfl)
    (by simp [D3, C6, C7, D4, *])

theorem d11 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T10 hp i''' i'' i' i) (T11 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [(C6 i''' i'' i' i, hp.q - hp.q⁻¹), (C7 i''' i'' i' i, 1)] [(D4 i''' i'' i' i, -1)]
    [(⟨i'⟩ : HeckeGen n)] [(⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hh) (by rfl) (by rfl)
    (by simp [D5, C6, C7, D4, *])

theorem d12 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T11 hp i''' i'' i' i) (T12 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (farCommRelation i i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i) (farCommRelation_lm i i''' (by omega))
    (by simp [*])
    [(C6 i''' i'' i' i, hp.q - hp.q⁻¹), (C7 i''' i'' i' i, 1)] [(D4 i''' i'' i' i, -1)]
    [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hh) (by rfl) (by rfl)
    (by simp [D6, C6, C7, D4, *])

theorem d13 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T12 hp i''' i'' i' i) (T13 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (bokutShiaoRelation i' i i''') (bokutShiaoRelation_mem hn hp hi' (by omega))
    (BokutShiaoCornerUneq.bs_xw_hrel hi' hi'' hi''') (BokutShiaoCornerUneq.bs_xw_hlm hi' hi'' hi''')
    (by simp [*])
    [(C6 i''' i'' i' i, hp.q - hp.q⁻¹), (C7 i''' i'' i' i, 1)] [(D4 i''' i'' i' i, -1)]
    [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] [] _ _ (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hh) (by rfl) (by rfl)
    (by simp [D7, C6, C7, D4, *])

theorem d14 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T13 hp i''' i'' i' i) (T14 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (bokutShiaoRelation i'' i' i''') (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (BokutShiaoCornerUneq.bs_yw_hrel hi'' hi''') (BokutShiaoCornerUneq.bs_yw_hlm hi'' hi''')
    (by simp [*])
    [(C6 i''' i'' i' i, hp.q - hp.q⁻¹), (C7 i''' i'' i' i, 1)] [(D4 i''' i'' i' i, -1)]
    [] [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hh) (by rfl) (by rfl)
    (by simp [D8, C6, C7, D4, *])

theorem d15 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T14 hp i''' i'' i' i) (T15 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (farCommRelation i' i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i') (farCommRelation_lm i' i''' (by omega))
    (by simp [*])
    [] [(C7 i''' i'' i' i, 1), (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (D4 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (hp.q - hp.q⁻¹) hh (by rfl) (by rfl)
    (by simp [C6, C7, D4, D9, *])

theorem d16 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T15 hp i''' i'' i' i) (T16 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [] [(C7 i''' i'' i' i, 1), (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (D4 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] [(⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (hp.q - hp.q⁻¹) hh (by rfl) (by rfl)
    (by simp [C8, C7, D4, D9, *])

theorem d17 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T16 hp i''' i'' i' i) (T17 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  have hh := hp.h_ne_zero
  exact monicStep hn hp (farCommRelation i i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i) (farCommRelation_lm i i''' (by omega))
    (by simp [*])
    [] [(C7 i''' i'' i' i, 1), (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (D4 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] _ _ (hp.q - hp.q⁻¹) hh (by rfl) (by rfl)
    (by simp [C9, C7, D4, D9, *])

theorem d18 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T17 hp i''' i'' i' i) (T18 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i' i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i') (farCommRelation_lm i' i''' (by omega))
    (by simp [*])
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹), (C7 i''' i'' i' i, 1), (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [D4, C7, D9, *])

theorem d19 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T18 hp i''' i'' i' i) (T19 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹), (C7 i''' i'' i' i, 1), (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹))] []
    [(⟨i'⟩ : HeckeGen n)] [(⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [D10, C7, D9, *])

theorem d20 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T19 hp i''' i'' i' i) (T20 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i) (farCommRelation_lm i i''' (by omega))
    (by simp [*])
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹), (C7 i''' i'' i' i, 1), (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [D11, C7, D9, *])

theorem d21 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T20 hp i''' i'' i' i) (T21 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i' i i'') (bokutShiaoRelation_mem hn hp hi' (by omega))
    (BokutShiaoCornerUneq.bs_xz_hrel hi' hi'') (BokutShiaoCornerUneq.bs_xz_hlm hi' hi'')
    (by simp [*])
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹), (C7 i''' i'' i' i, 1), (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹))] []
    [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)] [] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [D12, C7, D9, *])

theorem d22 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T21 hp i''' i'' i' i) (T22 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i''') (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (BokutShiaoCornerUneq.bs_yw_hrel hi'' hi''') (BokutShiaoCornerUneq.bs_yw_hlm hi'' hi''')
    (by simp [*])
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹), (C7 i''' i'' i' i, 1), (D9 i''' i'' i' i, -(hp.q - hp.q⁻¹))] []
    [] [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] _ _ (-1) (neg_ne_zero.mpr one_ne_zero) (by rfl) (by rfl)
    (by simp [D13, C7, D9, *])

theorem d23 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T22 hp i''' i'' i' i) (T23 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i' i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i') (farCommRelation_lm i' i''' (by omega))
    (by simp [*])
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹)] [(D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (D14 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [C7, D14, D9, *])

theorem d24 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T23 hp i''' i'' i' i) (T24 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹)] [(D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (D14 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)] [(⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [C10, D14, D9, *])

theorem d25 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T24 hp i''' i'' i' i) (T25 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i) (farCommRelation_lm i i''' (by omega))
    (by simp [*])
    [(D9 i''' i'' i' i, hp.q - hp.q⁻¹)] [(D9 i''' i'' i' i, -(hp.q - hp.q⁻¹)), (D14 i''' i'' i' i, -1)]
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] _ _ 1 one_ne_zero (by rfl) (by rfl)
    (by simp [C11, D14, D9, *])
end

section

variable (hp : HeckeParams) {i''' i'' i' i : Fin n}

/-- Step 5 — the quadratic rule at `i−3`. -/
theorem d5 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T4 hp i''' i'' i' i) (T5 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzy := hyz.symm
  have hv : (T4 hp i''' i'' i' i).coeff
      ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
        (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
        ++ (heckeRelation i''' hp).lm (heckeOrder n) ++ [(⟨i⟩ : HeckeGen n)]) = -1 := by
    rw [heckeRelation_lm, show ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
        (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
        (⟨i''⟩ : HeckeGen n)] ++ [(⟨i'''⟩ : HeckeGen n), ⟨i'''⟩]
        ++ [(⟨i⟩ : HeckeGen n)]) = D2 i''' i'' i' i from rfl]
    simp [T4, C2, D2, AlgElement.ofTerms_coeff, *]
  refine ⟨heckeRelation i''' hp, heckeRelation_mem hn hp i''',
    [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
     (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)],
    [(⟨i⟩ : HeckeGen n)], -1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (-1 : ℝ) * (AlgElement.contextMul
      [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
       (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
      (heckeRelation i''' hp).relation [(⟨i⟩ : HeckeGen n)]).coeff m
    simp only [T4, T5, C2, D2, D3, D4, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons,
      List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- Step 9 — the quadratic rule at `i−3` again. -/
theorem d9 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T8 hp i''' i'' i' i) (T9 hp i''' i'' i' i) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ := BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzy := hyz.symm
  have hv : (T8 hp i''' i'' i' i).coeff
      ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
        (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
        (⟨i''⟩ : HeckeGen n)]
        ++ (heckeRelation i''' hp).lm (heckeOrder n) ++ []) = 1 := by
    rw [heckeRelation_lm, show ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n),
        (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n),
        (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
        ++ [(⟨i'''⟩ : HeckeGen n), ⟨i'''⟩] ++ []) = C5 i''' i'' i' i from rfl]
    simp [T8, C5, D3, D4, AlgElement.ofTerms_coeff, *]
  refine ⟨heckeRelation i''' hp, heckeRelation_mem hn hp i''',
    [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
     (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
     (⟨i''⟩ : HeckeGen n)], [], 1, ?_, ?_, ?_⟩
  · rw [hv]; norm_num
  · rw [hv, heckeRelation_lc]; ring
  · intro m
    show _ = _ - (1 : ℝ) * (AlgElement.contextMul
      [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n),
       (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
       (⟨i''⟩ : HeckeGen n)] (heckeRelation i''' hp).relation []).coeff m
    simp only [T8, T9, C5, C6, C7, D3, D4, heckeRelation,
      AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil, List.nil_append,
      List.append_nil, List.cons_append, AlgElement.ofTerms_coeff, List.filter_cons,
      List.filter_nil, decide_eq_true_eq]
    split_ifs <;>
      simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

end

theorem T25_isZero (hp : HeckeParams) (i''' i'' i' i : Fin n) :
    (T25 hp i''' i'' i' i).isZero := by
  intro m
  simp only [T25, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- The rule at depth `i−3` against itself. -/
noncomputable def oc (i''' i'' i' i : Fin n) (hi' : i'.val + 1 = i.val)
    (hi'' : i''.val + 1 = i'.val) (hi''' : i'''.val + 1 = i''.val) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := bokutShiaoRelation i' i i'''
  rule₂ := bokutShiaoRelation i' i i'''
  left := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
           (⟨i'''⟩ : HeckeGen n)]
  overlap := [⟨i⟩]
  right := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
            (⟨i⟩ : HeckeGen n)]
  lm₁_decomp := by rw [BokutShiaoCornerUneq.bs_xw_hlm hi' hi'' hi''']; rfl
  lm₂_decomp := by rw [BokutShiaoCornerUneq.bs_xw_hlm hi' hi'' hi''']; rfl
  overlap_nonempty := by simp

/-- **The S-polynomial.** -/
theorem oc_spoly_coeff (hp : HeckeParams) {i''' i'' i' i : Fin n}
    (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (m : Monomial (HeckeGen n)) :
    (oc i''' i'' i' i hi' hi'' hi''').spoly.coeff m = (T0 hp i''' i'' i' i).coeff m := by
  show (bokutShiaoRelation i' i i''').lc (heckeOrder n)
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i i''').relation
          [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
           (⟨i⟩ : HeckeGen n)]).coeff m
    - (bokutShiaoRelation i' i i''').lc (heckeOrder n)
      * (AlgElement.contextMul
          [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
           (⟨i'''⟩ : HeckeGen n)]
          (bokutShiaoRelation i' i i''').relation []).coeff m
    = _
  rw [bokutShiaoRelation_lc hi' (by omega), one_mul, one_mul,
    AlgElement.contextMul_coeff_congr []
      [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n),
       (⟨i⟩ : HeckeGen n)] (BokutShiaoCornerUneq.bs_xw_hrel hi' hi'' hi''') m,
    AlgElement.contextMul_coeff_congr
      [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n),
       (⟨i'''⟩ : HeckeGen n)] [] (BokutShiaoCornerUneq.bs_xw_hrel hi' hi'' hi''') m]
  simp only [T0, C0, D0, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
    List.map_nil, List.nil_append, List.append_nil, List.cons_append,
    AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Twenty-five steps, to zero** — the last composition of the `n = 4`
enumeration. -/
theorem resolves (hp : HeckeParams) {i''' i'' i' i : Fin n} (hn : 0 < n)
    (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i''' i'' i' i hi' hi'' hi''').spoly nf ∧ nf.isZero := by
  refine reducesToZero_congr ⟨T25 hp i''' i'' i' i,
    ⟨(MultiStepReduction.refl (T0 hp i''' i'' i' i))
      |>.step (d1 hp hn hi' hi'' hi''') |>.step (d2 hp hn hi' hi'' hi''')
      |>.step (d3 hp hn hi' hi'' hi''') |>.step (d4 hp hn hi' hi'' hi''')
      |>.step (d5 hp hn hi' hi'' hi''') |>.step (d6 hp hn hi' hi'' hi''')
      |>.step (d7 hp hn hi' hi'' hi''') |>.step (d8 hp hn hi' hi'' hi''')
      |>.step (d9 hp hn hi' hi'' hi''') |>.step (d10 hp hn hi' hi'' hi''')
      |>.step (d11 hp hn hi' hi'' hi''') |>.step (d12 hp hn hi' hi'' hi''')
      |>.step (d13 hp hn hi' hi'' hi''') |>.step (d14 hp hn hi' hi'' hi''')
      |>.step (d15 hp hn hi' hi'' hi''') |>.step (d16 hp hn hi' hi'' hi''')
      |>.step (d17 hp hn hi' hi'' hi''') |>.step (d18 hp hn hi' hi'' hi''')
      |>.step (d19 hp hn hi' hi'' hi''') |>.step (d20 hp hn hi' hi'' hi''')
      |>.step (d21 hp hn hi' hi'' hi''') |>.step (d22 hp hn hi' hi'' hi''')
      |>.step (d23 hp hn hi' hi'' hi''') |>.step (d24 hp hn hi' hi'' hi''')
      |>.step (d25 hp hn hi' hi'' hi'''),
      isNormalForm_of_isZero (T25_isZero hp i''' i'' i' i)⟩, T25_isZero hp i''' i'' i' i⟩ ?_
  intro m
  exact oc_spoly_coeff hp hi' hi'' hi''' m

end BokutShiaoCornerDeep

/-! ## §4ad  `B × B` at general depth: the whole `b = 2` column

§4z–§4ac closed the Bokut–Shiao-against-Bokut–Shiao corner at four fixed depths,
`(a, b) ∈ {(2,2), (3,2), (2,3), (3,3)}`, writing `a = i − j₁` and `b = i − j₂`.
Those are cases, not a family. The chain length is *quadratic* in the depths —
`2ab − a² + 5a + 1` steps when `a ≤ b`, `b² + 3b + 5` when `a > b` — so no fixed
script covers the corner, and the general statement needs an induction on both.

This section takes the first genuinely general slice: **`b = 2`, and `a`
arbitrary**. It is the tractable half, because in the `a > b` regime the length
does not depend on `a` at all — the extra depth rides along inertly rather than
contributing work. That is precisely what the proof exhibits. Writing

    x = σᵢ,   y = σᵢ₋₁,   z = σᵢ₋₂,   u = σᵢ₋₃,   E = descWord (i−3) j

so that `descWord i j = x y z E`, every one of the seventeen words in the chain
has the shape

    (explicit prefix) ++ E ++ (explicit suffix)

and `E` is never inspected — not by a rule, not by a distinctness obligation.
The chain is fifteen steps at every depth, all of them monic, so `monicStep`
(§4x) discharges the lot and the deformation parameter `h` never appears.

The only hypothesis on the depth is `j ≤ i − 3`, so this **subsumes §4aa**, which
is the case `j = i − 3` (there `E = [σᵢ₋₃]`). §4aa is kept rather than replaced
because its chain is the one the confluence engine produces at that depth: when
`j = i − 3` the rule used at steps 5 and 13 degenerates to the braid word, and
the engine picks the Yang–Baxter rule sharing that leading monomial — a rule of
leading coefficient `−1`, which is why §4aa reads differently step for step.
Both rules are in the completed system and both chains are valid.

Six rules occur. Three are Bokut–Shiao at the general bottom `j`, with tops `i`,
`i−1` and `i−2`; one is the fixed-depth Bokut–Shiao at `(i−2, i−1, i−3)` (§4aa's,
reused); and three are far-commutations, `σᵢσᵢ₋₂`, `σᵢσᵢ₋₃` and `σᵢ₋₁σᵢ₋₃`.
Every distinctness obligation is settled by a first, second, third or fourth
letter among the four generators, which is what leaves the depth free.

**Why fifteen.** Reducing the two terms of the S-polynomial separately takes 8
and 7 steps, and 8 + 7 = 15: as in every other corner case, the chain is exactly
the two independent reductions with no shared intermediate to cut. Here that
split is visible in the stage list — `V0 ⋯ V8` is the first term's reduction,
`U0 ⋯ U7` the second's, and they meet at `V8 = U7`. -/

namespace BokutShiaoCornerDepth

variable {n : ℕ}

section

variable {i''' i'' i' i j : Fin n}

/-- The run with its top letter split off. -/
theorem dw_y (hi'' : i''.val + 1 = i'.val) (hi''' : i'''.val + 1 = i''.val)
    (hj : j.val ≤ i'''.val) :
    descWord i' j = (⟨i'⟩ : HeckeGen n) :: (⟨i''⟩ : HeckeGen n) :: descWord i''' j := by
  rw [descWord_cons hi'' (by omega), descWord_cons hi''' hj]

/-- The run with its top two letters split off. -/
theorem dw_x (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    descWord i j = (⟨i⟩ : HeckeGen n) :: (⟨i'⟩ : HeckeGen n) :: (⟨i''⟩ : HeckeGen n) :: descWord i''' j := by
  rw [descWord_cons hi' (by omega), dw_y hi'' hi''' hj]

/-- The Bokut–Shiao rule with top `i` and the general bottom `j`. -/
theorem bs_x_hrel (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val)
    (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i' i j).relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j, -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i j, (1 : ℝ)), (bsWord₂ i' i j, -1)]).coeff v = _
  rw [bsWord₁, dw_x hi' hi'' hi''' hj, bsWord₂, dw_y hi'' hi''' hj]
  rfl

theorem bs_x_hlm (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    (bokutShiaoRelation i' i j).lm (heckeOrder n)
      = [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm hi' (by omega), bsWord₁, dw_x hi' hi'' hi''' hj]
  rfl

/-- The Bokut–Shiao rule with top `i−1` and the general bottom `j`. -/
theorem bs_y_hrel (hi'' : i''.val + 1 = i'.val) (hi''' : i'''.val + 1 = i''.val)
    (hj : j.val ≤ i'''.val)
    (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i'' i' j).relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i'⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j, -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i' j, (1 : ℝ)), (bsWord₂ i'' i' j, -1)]).coeff v = _
  rw [bsWord₁, dw_y hi'' hi''' hj, bsWord₂, descWord_cons hi''' hj]
  rfl

theorem bs_y_hlm (hi'' : i''.val + 1 = i'.val) (hi''' : i'''.val + 1 = i''.val)
    (hj : j.val ≤ i'''.val) :
    (bokutShiaoRelation i'' i' j).lm (heckeOrder n)
      = [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i'⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm hi'' (by omega), bsWord₁, dw_y hi'' hi''' hj]
  rfl

/-- The Bokut–Shiao rule with top `i−2` and the general bottom `j`. -/
theorem bs_z_hrel (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val)
    (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i''' i'' j).relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i''⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j, -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i'' j, (1 : ℝ)), (bsWord₂ i''' i'' j, -1)]).coeff v = _
  rw [bsWord₁, descWord_cons hi''' hj, bsWord₂]
  rfl

theorem bs_z_hlm (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    (bokutShiaoRelation i''' i'' j).lm (heckeOrder n)
      = [(⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i''⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm hi''' hj, bsWord₁, descWord_cons hi''' hj]
  rfl

end

def V0 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def V1 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def V2 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def V3 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]
def V4 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i''⟩ : HeckeGen n)]
def V5 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i''⟩ : HeckeGen n)]
def V6 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j
def V7 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j
def V8 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j
def U0 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def U1 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def U2 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
def U3 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i⟩ : HeckeGen n)]
def U4 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i⟩ : HeckeGen n)]
def U5 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i⟩ : HeckeGen n)]
def U6 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j
def U7 (i''' i'' i' i j : Fin n) : Monomial (HeckeGen n) := [(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j

noncomputable def T0 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V0 i''' i'' i' i j, (1 : ℝ)), (U0 i''' i'' i' i j, -1)]

noncomputable def T1 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V1 i''' i'' i' i j, (1 : ℝ)), (U0 i''' i'' i' i j, -1)]

noncomputable def T2 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i j, (1 : ℝ)), (U0 i''' i'' i' i j, -1)]

noncomputable def T3 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i j, (1 : ℝ)), (U1 i''' i'' i' i j, -1)]

noncomputable def T4 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i j, (1 : ℝ)), (U2 i''' i'' i' i j, -1)]

noncomputable def T5 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i j, (1 : ℝ)), (U3 i''' i'' i' i j, -1)]

noncomputable def T6 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i j, (1 : ℝ)), (U4 i''' i'' i' i j, -1)]

noncomputable def T7 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i j, (1 : ℝ)), (U5 i''' i'' i' i j, -1)]

noncomputable def T8 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i j, (1 : ℝ)), (U6 i''' i'' i' i j, -1)]

noncomputable def T9 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i''' i'' i' i j, (1 : ℝ)), (U7 i''' i'' i' i j, -1)]

noncomputable def T10 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V3 i''' i'' i' i j, (1 : ℝ)), (U7 i''' i'' i' i j, -1)]

noncomputable def T11 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V4 i''' i'' i' i j, (1 : ℝ)), (U7 i''' i'' i' i j, -1)]

noncomputable def T12 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V5 i''' i'' i' i j, (1 : ℝ)), (U7 i''' i'' i' i j, -1)]

noncomputable def T13 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V6 i''' i'' i' i j, (1 : ℝ)), (U7 i''' i'' i' i j, -1)]

noncomputable def T14 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V7 i''' i'' i' i j, (1 : ℝ)), (U7 i''' i'' i' i j, -1)]

noncomputable def T15 (i''' i'' i' i j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V8 i''' i'' i' i j, (1 : ℝ)), (U7 i''' i'' i' i j, -1)]

section

variable (hp : HeckeParams) {i''' i'' i' i j : Fin n}

theorem s1 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T0 i''' i'' i' i j) (T1 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' j) (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (bs_y_hrel hi'' hi''' hj) (bs_y_hlm hi'' hi''' hj)
    (by simp [*])
    [] [(U0 i''' i'' i' i j, -1)]
    ([(⟨i⟩ : HeckeGen n)]) ([(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V0]) (by simp [V1])
    (by simp [V0, U0, *])

theorem s2 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (_hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T1 i''' i'' i' i j) (T2 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [] [(U0 i''' i'' i' i j, -1)]
    ([]) ([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V1]) (by simp [V2])
    (by simp [V1, U0, *])

theorem s3 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T2 i''' i'' i' i j) (T3 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' j) (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (bs_y_hrel hi'' hi''' hj) (bs_y_hlm hi'' hi''' hj)
    (by simp [*])
    [(V2 i''' i'' i' i j, (1 : ℝ))] []
    ([(⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]) ([(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U0]) (by simp [U1])
    (by simp [U0, V2, *])

theorem s4 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (_hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T3 i''' i'' i' i j) (T4 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [(V2 i''' i'' i' i j, (1 : ℝ))] []
    ([(⟨i'⟩ : HeckeGen n)]) ([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U1]) (by simp [U2])
    (by simp [U1, V2, *])

theorem s5 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T4 i''' i'' i' i j) (T5 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i''' i'' j) (bokutShiaoRelation_mem hn hp hi''' hj)
    (bs_z_hrel hi''' hj) (bs_z_hlm hi''' hj)
    (by simp [*])
    [(V2 i''' i'' i' i j, (1 : ℝ))] []
    ([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]) ([(⟨i⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U2]) (by simp [U3])
    (by simp [U2, V2, *])

theorem s6 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (_hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T5 i''' i'' i' i j) (T6 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i' i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i') (farCommRelation_lm i' i''' (by omega))
    (by simp [*])
    [(V2 i''' i'' i' i j, (1 : ℝ))] []
    ([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]) ([(⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U3]) (by simp [U4])
    (by simp [U3, V2, *])

theorem s7 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (_hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T6 i''' i'' i' i j) (T7 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i) (farCommRelation_lm i i''' (by omega))
    (by simp [*])
    [(V2 i''' i'' i' i j, (1 : ℝ))] []
    ([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]) ([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U4]) (by simp [U5])
    (by simp [U4, V2, *])

theorem s8 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T7 i''' i'' i' i j) (T8 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i' i j) (bokutShiaoRelation_mem hn hp hi' (by omega))
    (bs_x_hrel hi' hi'' hi''' hj) (bs_x_hlm hi' hi'' hi''' hj)
    (by simp [*])
    [(V2 i''' i'' i' i j, (1 : ℝ))] []
    ([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i'''⟩ : HeckeGen n)]) ([]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U5]) (by simp [U6])
    (by simp [U5, V2, *])

theorem s9 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (_hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T8 i''' i'' i' i j) (T9 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' i''') (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (BokutShiaoCornerUneq.bs_yw_hrel hi'' hi''') (BokutShiaoCornerUneq.bs_yw_hlm hi'' hi''')
    (by simp [*])
    [(V2 i''' i'' i' i j, (1 : ℝ))] []
    ([]) ([(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U6]) (by simp [U7])
    (by simp [U6, V2, *])

theorem s10 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T9 i''' i'' i' i j) (T10 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i' i j) (bokutShiaoRelation_mem hn hp hi' (by omega))
    (bs_x_hrel hi' hi'' hi''' hj) (bs_x_hlm hi' hi'' hi''' hj)
    (by simp [*])
    [] [(U7 i''' i'' i' i j, -1)]
    ([(⟨i''⟩ : HeckeGen n)]) ([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V2]) (by simp [V3])
    (by simp [V2, U7, *])

theorem s11 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T10 i''' i'' i' i j) (T11 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i'' i' j) (bokutShiaoRelation_mem hn hp hi'' (by omega))
    (bs_y_hrel hi'' hi''' hj) (bs_y_hlm hi'' hi''' hj)
    (by simp [*])
    [] [(U7 i''' i'' i' i j, -1)]
    ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]) ([(⟨i''⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V3]) (by simp [V4])
    (by simp [V3, U7, *])

theorem s12 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (_hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T11 i''' i'' i' i j) (T12 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i'') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i'' i) (farCommRelation_lm i i'' (by omega))
    (by simp [*])
    [] [(U7 i''' i'' i' i j, -1)]
    ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]) ([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j ++ [(⟨i''⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V4]) (by simp [V5])
    (by simp [V4, U7, *])

theorem s13 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T12 i''' i'' i' i j) (T13 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (bokutShiaoRelation i''' i'' j) (bokutShiaoRelation_mem hn hp hi''' hj)
    (bs_z_hrel hi''' hj) (bs_z_hlm hi''' hj)
    (by simp [*])
    [] [(U7 i''' i'' i' i j, -1)]
    ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n)]) ([]) _ _ 1 one_ne_zero
    (by simp [V5]) (by simp [V6])
    (by simp [V5, U7, *])

theorem s14 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (_hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T13 i''' i'' i' i j) (T14 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i' i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i') (farCommRelation_lm i' i''' (by omega))
    (by simp [*])
    [] [(U7 i''' i'' i' i j, -1)]
    ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]) ([(⟨i''⟩ : HeckeGen n)] ++ descWord i''' j) _ _ 1 one_ne_zero
    (by simp [V6]) (by simp [V7])
    (by simp [V6, U7, *])

theorem s15 (hn : 0 < n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (_hj : j.val ≤ i'''.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T14 i''' i'' i' i j) (T15 i''' i'' i' i j) := by
  obtain ⟨hxy, hxz, hxw, hyz, hyw, hzw⟩ :=
    BokutShiaoCornerUneq.gen4_ne hi' hi'' hi'''
  have hyx := hxy.symm
  have hzx := hxz.symm
  have hwx := hxw.symm
  have hzy := hyz.symm
  have hwy := hyw.symm
  have hwz := hzw.symm
  exact monicStep hn hp (farCommRelation i i''') (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i''' i) (farCommRelation_lm i i''' (by omega))
    (by simp [*])
    [] [(U7 i''' i'' i' i j, -1)]
    ([(⟨i''⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)]) ([(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j) _ _ 1 one_ne_zero
    (by simp [V7]) (by simp [V8])
    (by simp [V7, U7, *])

end

theorem T15_isZero (i''' i'' i' i j : Fin n) : (T15 i''' i'' i' i j).isZero := by
  intro m
  simp only [T15, V8, U7, AlgElement.ofTerms_coeff, List.filter_cons,
    List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
  ring

/-- The composition of the rule at the general depth `j` with the rule at
depth `i−2`, overlapping in the trailing `σᵢ`. -/
noncomputable def oc (i''' i'' i' i j : Fin n) (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := bokutShiaoRelation i' i j
  rule₂ := bokutShiaoRelation i' i i''
  left := [(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j
  overlap := [(⟨i⟩ : HeckeGen n)]
  right := [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
  lm₁_decomp := by rw [bs_x_hlm hi' hi'' hi''' hj]
  lm₂_decomp := by rw [BokutShiaoCornerUneq.bs_xz_hlm hi' hi'']; rfl
  overlap_nonempty := by simp

/-- **The S-polynomial.** -/
theorem oc_spoly_coeff {i''' i'' i' i j : Fin n} (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val)
    (m : Monomial (HeckeGen n)) :
    (oc i''' i'' i' i j hi' hi'' hi''' hj).spoly.coeff m = (T0 i''' i'' i' i j).coeff m := by
  show (bokutShiaoRelation i' i i'').lc (heckeOrder n)
      * (AlgElement.contextMul [] (bokutShiaoRelation i' i j).relation
          [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]).coeff m
    - (bokutShiaoRelation i' i j).lc (heckeOrder n)
      * (AlgElement.contextMul ([(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j)
          (bokutShiaoRelation i' i i'').relation []).coeff m
    = _
  rw [bokutShiaoRelation_lc hi' (by omega), bokutShiaoRelation_lc hi' (by omega),
    one_mul, one_mul,
    AlgElement.contextMul_coeff_congr [] [(⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n), (⟨i⟩ : HeckeGen n)]
      (bs_x_hrel hi' hi'' hi''' hj) m,
    AlgElement.contextMul_coeff_congr ([(⟨i⟩ : HeckeGen n), (⟨i'⟩ : HeckeGen n), (⟨i''⟩ : HeckeGen n)] ++ descWord i''' j) []
      (BokutShiaoCornerUneq.bs_xz_hrel hi' hi'') m]
  simp only [T0, V0, U0, AlgElement.contextMul_ofTerms_coeff, List.map_cons,
    List.map_nil, List.nil_append, List.append_nil, List.cons_append,
    List.append_assoc, AlgElement.ofTerms_coeff, List.filter_cons,
    List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **Fifteen steps, to zero, at every depth `j ≤ i − 3`.** -/
theorem resolves (hp : HeckeParams) {i''' i'' i' i j : Fin n} (hn : 0 < n)
    (hi' : i'.val + 1 = i.val) (hi'' : i''.val + 1 = i'.val)
    (hi''' : i'''.val + 1 = i''.val) (hj : j.val ≤ i'''.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i''' i'' i' i j hi' hi'' hi''' hj).spoly nf ∧ nf.isZero := by
  refine reducesToZero_congr ⟨T15 i''' i'' i' i j,
    ⟨(MultiStepReduction.refl (T0 i''' i'' i' i j))
      |>.step (s1 hp hn hi' hi'' hi''' hj)
      |>.step (s2 hp hn hi' hi'' hi''' hj)
      |>.step (s3 hp hn hi' hi'' hi''' hj)
      |>.step (s4 hp hn hi' hi'' hi''' hj)
      |>.step (s5 hp hn hi' hi'' hi''' hj)
      |>.step (s6 hp hn hi' hi'' hi''' hj)
      |>.step (s7 hp hn hi' hi'' hi''' hj)
      |>.step (s8 hp hn hi' hi'' hi''' hj)
      |>.step (s9 hp hn hi' hi'' hi''' hj)
      |>.step (s10 hp hn hi' hi'' hi''' hj)
      |>.step (s11 hp hn hi' hi'' hi''' hj)
      |>.step (s12 hp hn hi' hi'' hi''' hj)
      |>.step (s13 hp hn hi' hi'' hi''' hj)
      |>.step (s14 hp hn hi' hi'' hi''' hj)
      |>.step (s15 hp hn hi' hi'' hi''' hj),
      isNormalForm_of_isZero (T15_isZero i''' i'' i' i j)⟩, T15_isZero i''' i'' i' i j⟩ ?_
  intro m
  exact oc_spoly_coeff hi' hi'' hi''' hj m

end BokutShiaoCornerDepth

/-! ## §4ae  The corner's `b = 3` column

§4ad closed the corner's `b = 2` column for every depth `a`. This is the same
statement one level down: `b = 3`, and `a` arbitrary. Naming the generators by
distance below the top index — `i₀ = σᵢ`, `i₁ = σᵢ₋₁`, … — and writing
`E = descWord i₄ j` for the part of the descending run that grows with `a`, every
word is again `(explicit prefix) ++ E ++ (explicit suffix)` with `E` never
inspected. Twenty-three steps, all monic, `h` never appears, and the only
hypothesis on the depth is `j ≤ i − 4`.

**What the extra level costs, exactly.** Setting the two columns side by side
with rules named relatively, the `b = 3` chain is the `b = 2` chain with one
block inserted twice — once into each term's reduction:

    b = 2:  B₂₁ F₀₂ │ B₂₁ F₀₂ B₃₂ F₁₃ F₀₃                    │ B₁₀ B₂₁⁽ᵛ⁾ │ B₁₀ B₂₁ F₀₂ B₃₂ F₁₃ F₀₃
    b = 3:  B₂₁ F₀₂ │ B₂₁ F₀₂ B₃₂ F₁₃ F₀₃ ⟨B₄₃ F₂₄ F₁₄ F₀₄⟩  │ B₁₀ B₂₁⁽ᵛ⁾ │ B₁₀ B₂₁ F₀₂ B₃₂ F₁₃ F₀₃ ⟨B₄₃ F₂₄ F₁₄ F₀₄⟩

The inserted block is one Bokut–Shiao step at the next generator down, then a run
of far-commutations carrying the newly exposed letter leftwards past the prefix.
Its length is `b + 1`, so `steps(b) = steps(b−1) + 2(b + 1)` from `steps(2) = 15`,
which is the `b² + 3b + 5` the rank sweep fitted: 15, 23, 33, …

That far-commutation run is not new work in disguise — it is exactly
`farComm_transport_left` (§4v), a low generator moving left past a run of
generators that all far-commute with it, whose side condition `descWord_index_ge`
already supplies. Writing the column out step by step, as here, is the honest
thing to do while `b` is fixed; the transport lemma is what an induction *on* `b`
would have to use instead, because there the block's length is not a constant.

Both this section and §4ad are emitted from the confluence engine's own trace
rather than transcribed: the generator was checked by re-deriving §4ad's
seventeen words and fifteen rules and finding them identical.

**Why twenty-three.** Reducing the two terms of the S-polynomial separately takes
12 and 11 steps, and 12 + 11 = 23. The first term runs `V0 ⋯ V11` and then one
further step onto the second term's endpoint, which is why the section has no
`V12`: that word is `U11`, reached from the other side. As in every corner case
the chain is exactly the two independent reductions, with no shared intermediate
to cut. -/

namespace BokutShiaoCornerDepth3

variable {n : ℕ}

section

variable {i₀ i₁ i₂ i₃ i₄ j : Fin n}

/-- The 5 generators in play are pairwise distinct. -/
theorem gen_ne (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) :
    (⟨i₀⟩ : HeckeGen n) ≠ (⟨i₁⟩ : HeckeGen n)
      ∧ (⟨i₀⟩ : HeckeGen n) ≠ (⟨i₂⟩ : HeckeGen n)
      ∧ (⟨i₀⟩ : HeckeGen n) ≠ (⟨i₃⟩ : HeckeGen n)
      ∧ (⟨i₀⟩ : HeckeGen n) ≠ (⟨i₄⟩ : HeckeGen n)
      ∧ (⟨i₁⟩ : HeckeGen n) ≠ (⟨i₂⟩ : HeckeGen n)
      ∧ (⟨i₁⟩ : HeckeGen n) ≠ (⟨i₃⟩ : HeckeGen n)
      ∧ (⟨i₁⟩ : HeckeGen n) ≠ (⟨i₄⟩ : HeckeGen n)
      ∧ (⟨i₂⟩ : HeckeGen n) ≠ (⟨i₃⟩ : HeckeGen n)
      ∧ (⟨i₂⟩ : HeckeGen n) ≠ (⟨i₄⟩ : HeckeGen n)
      ∧ (⟨i₃⟩ : HeckeGen n) ≠ (⟨i₄⟩ : HeckeGen n) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    · intro hcon
      have := congrArg HeckeGen.rank hcon
      simp only [HeckeGen.rank] at this
      omega

/-- The run from `i₃` with its explicit head split off. -/
theorem dw3 (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    descWord i₃ j = [(⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j := by
  rw [descWord_cons h₄ hj]
  rfl

/-- The run from `i₂` with its explicit head split off. -/
theorem dw2 (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    descWord i₂ j = [(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j := by
  rw [descWord_cons h₃ (by omega), dw3 h₄ hj]
  rfl

/-- The run from `i₁` with its explicit head split off. -/
theorem dw1 (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    descWord i₁ j = [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j := by
  rw [descWord_cons h₂ (by omega), dw2 h₃ h₄ hj]
  rfl

/-- The run from `i₀` with its explicit head split off. -/
theorem dw0 (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    descWord i₀ j = [(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j := by
  rw [descWord_cons h₁ (by omega), dw1 h₂ h₃ h₄ hj]
  rfl

theorem dwLit3_3 :
    descWord i₃ i₃ = [(⟨i₃⟩ : HeckeGen n)] := by
  rw [descWord_self]

theorem dwLit2_3 (h₃ : i₃.val + 1 = i₂.val) :
    descWord i₂ i₃ = [(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] := by
  rw [descWord_cons h₃ (by omega), dwLit3_3]

theorem dwLit1_3 (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) :
    descWord i₁ i₃ = [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] := by
  rw [descWord_cons h₂ (by omega), dwLit2_3 h₃]

theorem dwLit0_3 (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) :
    descWord i₀ i₃ = [(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] := by
  rw [descWord_cons h₁ (by omega), dwLit1_3 h₂ h₃]

theorem dwLit4_4 :
    descWord i₄ i₄ = [(⟨i₄⟩ : HeckeGen n)] := by
  rw [descWord_self]

theorem dwLit3_4 (h₄ : i₄.val + 1 = i₃.val) :
    descWord i₃ i₄ = [(⟨i₃⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n)] := by
  rw [descWord_cons h₄ (by omega), dwLit4_4]

theorem dwLit2_4 (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) :
    descWord i₂ i₄ = [(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n)] := by
  rw [descWord_cons h₃ (by omega), dwLit3_4 h₄]

theorem dwLit1_4 (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) :
    descWord i₁ i₄ = [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n)] := by
  rw [descWord_cons h₂ (by omega), dwLit2_4 h₃ h₄]

theorem dwLit0_4 (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) :
    descWord i₀ i₄ = [(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n)] := by
  rw [descWord_cons h₁ (by omega), dwLit1_4 h₂ h₃ h₄]

theorem bsJ1_hrel (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val)
    (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i₂ i₁ j).relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₁⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j, -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i₁ j, (1 : ℝ)), (bsWord₂ i₂ i₁ j, -1)]).coeff v = _
  rw [bsWord₁, dw1 h₂ h₃ h₄ hj, bsWord₂, dw2 h₃ h₄ hj]
  rfl

theorem bsJ1_hlm (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    (bokutShiaoRelation i₂ i₁ j).lm (heckeOrder n)
      = [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₁⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm h₂ (by omega), bsWord₁, dw1 h₂ h₃ h₄ hj]

theorem bsJ2_hrel (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val)
    (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i₃ i₂ j).relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₂⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i₃⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j, -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i₂ j, (1 : ℝ)), (bsWord₂ i₃ i₂ j, -1)]).coeff v = _
  rw [bsWord₁, dw2 h₃ h₄ hj, bsWord₂, dw3 h₄ hj]
  rfl

theorem bsJ2_hlm (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    (bokutShiaoRelation i₃ i₂ j).lm (heckeOrder n)
      = [(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₂⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm h₃ (by omega), bsWord₁, dw2 h₃ h₄ hj]

theorem bsJ3_hrel (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val)
    (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i₄ i₃ j).relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i₄⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j, -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i₃ j, (1 : ℝ)), (bsWord₂ i₄ i₃ j, -1)]).coeff v = _
  rw [bsWord₁, dw3 h₄ hj, bsWord₂]
  rfl

theorem bsJ3_hlm (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    (bokutShiaoRelation i₄ i₃ j).lm (heckeOrder n)
      = [(⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm h₄ (by omega), bsWord₁, dw3 h₄ hj]

theorem bsJ0_hrel (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val)
    (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i₁ i₀ j).relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i₁⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j, -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i₀ j, (1 : ℝ)), (bsWord₂ i₁ i₀ j, -1)]).coeff v = _
  rw [bsWord₁, dw0 h₁ h₂ h₃ h₄ hj, bsWord₂, dw1 h₂ h₃ h₄ hj]
  rfl

theorem bsJ0_hlm (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    (bokutShiaoRelation i₁ i₀ j).lm (heckeOrder n)
      = [(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm h₁ (by omega), bsWord₁, dw0 h₁ h₂ h₃ h₄ hj]

theorem bsF2_1_4_hrel (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val)
    (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i₂ i₁ i₄).relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n)], -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i₁ i₄, (1 : ℝ)), (bsWord₂ i₂ i₁ i₄, -1)]).coeff v = _
  rw [bsWord₁, dwLit1_4 h₂ h₃ h₄, bsWord₂, dwLit2_4 h₃ h₄]
  rfl

theorem bsF2_1_4_hlm (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) :
    (bokutShiaoRelation i₂ i₁ i₄).lm (heckeOrder n)
      = [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm h₂ (by omega), bsWord₁, dwLit1_4 h₂ h₃ h₄]
  rfl

theorem bsF1_0_3_hrel (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val)
    (v : Monomial (HeckeGen n)) :
    (bokutShiaoRelation i₁ i₀ i₃).relation.coeff v
      = (AlgElement.ofTerms
          [([(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)], (1 : ℝ)),
           ([(⟨i₁⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)], -1)]).coeff v := by
  show (AlgElement.ofTerms
    [(bsWord₁ i₀ i₃, (1 : ℝ)), (bsWord₂ i₁ i₀ i₃, -1)]).coeff v = _
  rw [bsWord₁, dwLit0_3 h₁ h₂ h₃, bsWord₂, dwLit1_3 h₂ h₃]
  rfl

theorem bsF1_0_3_hlm (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) :
    (bokutShiaoRelation i₁ i₀ i₃).lm (heckeOrder n)
      = [(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)] := by
  rw [bokutShiaoRelation_lm h₁ (by omega), bsWord₁, dwLit0_3 h₁ h₂ h₃]
  rfl

end

def V0 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₁⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]
def U0 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₁⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]
def V1 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₀⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]
def V2 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₂⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]
def U1 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₁⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]
def U2 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]
def U3 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]
def U4 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]
def U5 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]
def U6 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n)]
def U7 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n)]
def U8 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n)]
def U9 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n)]
def U10 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j
def U11 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j
def V3 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]
def V4 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]
def V5 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]
def V6 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n)]
def V7 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n)]
def V8 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n)]
def V9 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j
def V10 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j
def V11 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : Monomial (HeckeGen n) := [(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j

noncomputable def T0 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V0 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U0 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T1 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V1 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U0 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T2 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U0 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T3 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U1 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T4 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U2 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T5 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U3 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T6 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U4 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T7 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U5 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T8 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U6 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T9 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U7 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T10 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U8 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T11 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U9 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T12 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U10 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T13 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U11 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T14 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V3 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U11 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T15 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V4 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U11 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T16 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V5 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U11 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T17 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V6 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U11 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T18 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V7 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U11 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T19 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V8 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U11 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T20 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V9 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U11 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T21 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V10 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U11 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T22 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V11 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U11 i₀ i₁ i₂ i₃ i₄ j, -1)]

noncomputable def T23 (i₀ i₁ i₂ i₃ i₄ j : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(U11 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ)), (U11 i₀ i₁ i₂ i₃ i₄ j, -1)]

section

variable (hp : HeckeParams) {i₀ i₁ i₂ i₃ i₄ j : Fin n}

theorem s1 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T0 i₀ i₁ i₂ i₃ i₄ j) (T1 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (bokutShiaoRelation i₂ i₁ j) (bokutShiaoRelation_mem hn hp h₂ (by omega))
    (bsJ1_hrel h₂ h₃ h₄ hj) (bsJ1_hlm h₂ h₃ h₄ hj)
    (by simp [*])
    [] [(U0 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([(⟨i₀⟩ : HeckeGen n)]) ([(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V0]) (by simp [V1])
    (by simp [V0, U0, *])

theorem s2 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T1 i₀ i₁ i₂ i₃ i₄ j) (T2 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₀ i₂) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₂ i₀) (farCommRelation_lm i₀ i₂ (by omega))
    (by simp [*])
    [] [(U0 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([]) ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V1]) (by simp [V2])
    (by simp [V1, U0, *])

theorem s3 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T2 i₀ i₁ i₂ i₃ i₄ j) (T3 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (bokutShiaoRelation i₂ i₁ j) (bokutShiaoRelation_mem hn hp h₂ (by omega))
    (bsJ1_hrel h₂ h₃ h₄ hj) (bsJ1_hlm h₂ h₃ h₄ hj)
    (by simp [*])
    [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ))] []
    ([(⟨i₁⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]) ([(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U0]) (by simp [U1])
    (by simp [U0, V2, *])

theorem s4 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T3 i₀ i₁ i₂ i₃ i₄ j) (T4 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₀ i₂) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₂ i₀) (farCommRelation_lm i₀ i₂ (by omega))
    (by simp [*])
    [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ))] []
    ([(⟨i₁⟩ : HeckeGen n)]) ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U1]) (by simp [U2])
    (by simp [U1, V2, *])

theorem s5 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T4 i₀ i₁ i₂ i₃ i₄ j) (T5 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (bokutShiaoRelation i₃ i₂ j) (bokutShiaoRelation_mem hn hp h₃ (by omega))
    (bsJ2_hrel h₃ h₄ hj) (bsJ2_hlm h₃ h₄ hj)
    (by simp [*])
    [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ))] []
    ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n)]) ([(⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U2]) (by simp [U3])
    (by simp [U2, V2, *])

theorem s6 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T5 i₀ i₁ i₂ i₃ i₄ j) (T6 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₁ i₃) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₃ i₁) (farCommRelation_lm i₁ i₃ (by omega))
    (by simp [*])
    [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ))] []
    ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]) ([(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U3]) (by simp [U4])
    (by simp [U3, V2, *])

theorem s7 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T6 i₀ i₁ i₂ i₃ i₄ j) (T7 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₀ i₃) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₃ i₀) (farCommRelation_lm i₀ i₃ (by omega))
    (by simp [*])
    [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ))] []
    ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n)]) ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U4]) (by simp [U5])
    (by simp [U4, V2, *])

theorem s8 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T7 i₀ i₁ i₂ i₃ i₄ j) (T8 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (bokutShiaoRelation i₄ i₃ j) (bokutShiaoRelation_mem hn hp h₄ (by omega))
    (bsJ3_hrel h₄ hj) (bsJ3_hlm h₄ hj)
    (by simp [*])
    [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ))] []
    ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n)]) ([(⟨i₀⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U5]) (by simp [U6])
    (by simp [U5, V2, *])

theorem s9 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T8 i₀ i₁ i₂ i₃ i₄ j) (T9 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₂ i₄) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₄ i₂) (farCommRelation_lm i₂ i₄ (by omega))
    (by simp [*])
    [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ))] []
    ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n)]) ([(⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U6]) (by simp [U7])
    (by simp [U6, V2, *])

theorem s10 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T9 i₀ i₁ i₂ i₃ i₄ j) (T10 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₁ i₄) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₄ i₁) (farCommRelation_lm i₁ i₄ (by omega))
    (by simp [*])
    [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ))] []
    ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]) ([(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U7]) (by simp [U8])
    (by simp [U7, V2, *])

theorem s11 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T10 i₀ i₁ i₂ i₃ i₄ j) (T11 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₀ i₄) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₄ i₀) (farCommRelation_lm i₀ i₄ (by omega))
    (by simp [*])
    [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ))] []
    ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]) ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₀⟩ : HeckeGen n)]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U8]) (by simp [U9])
    (by simp [U8, V2, *])

theorem s12 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T11 i₀ i₁ i₂ i₃ i₄ j) (T12 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (bokutShiaoRelation i₁ i₀ j) (bokutShiaoRelation_mem hn hp h₁ (by omega))
    (bsJ0_hrel h₁ h₂ h₃ h₄ hj) (bsJ0_hlm h₁ h₂ h₃ h₄ hj)
    (by simp [*])
    [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ))] []
    ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₄⟩ : HeckeGen n)]) ([]) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U9]) (by simp [U10])
    (by simp [U9, V2, *])

theorem s13 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T12 i₀ i₁ i₂ i₃ i₄ j) (T13 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (bokutShiaoRelation i₂ i₁ i₄) (bokutShiaoRelation_mem hn hp h₂ (by omega))
    (bsF2_1_4_hrel h₂ h₃ h₄) (bsF2_1_4_hlm h₂ h₃ h₄)
    (by simp [*])
    [(V2 i₀ i₁ i₂ i₃ i₄ j, (1 : ℝ))] []
    ([]) ([(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by simp [U10]) (by simp [U11])
    (by simp [U10, V2, *])

theorem s14 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T13 i₀ i₁ i₂ i₃ i₄ j) (T14 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (bokutShiaoRelation i₁ i₀ j) (bokutShiaoRelation_mem hn hp h₁ (by omega))
    (bsJ0_hrel h₁ h₂ h₃ h₄ hj) (bsJ0_hlm h₁ h₂ h₃ h₄ hj)
    (by simp [*])
    [] [(U11 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([(⟨i₂⟩ : HeckeGen n)]) ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V2]) (by simp [V3])
    (by simp [V2, U11, *])

theorem s15 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T14 i₀ i₁ i₂ i₃ i₄ j) (T15 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (bokutShiaoRelation i₂ i₁ j) (bokutShiaoRelation_mem hn hp h₂ (by omega))
    (bsJ1_hrel h₂ h₃ h₄ hj) (bsJ1_hlm h₂ h₃ h₄ hj)
    (by simp [*])
    [] [(U11 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]) ([(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V3]) (by simp [V4])
    (by simp [V3, U11, *])

theorem s16 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T15 i₀ i₁ i₂ i₃ i₄ j) (T16 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₀ i₂) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₂ i₀) (farCommRelation_lm i₀ i₂ (by omega))
    (by simp [*])
    [] [(U11 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n)]) ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V4]) (by simp [V5])
    (by simp [V4, U11, *])

theorem s17 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T16 i₀ i₁ i₂ i₃ i₄ j) (T17 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (bokutShiaoRelation i₃ i₂ j) (bokutShiaoRelation_mem hn hp h₃ (by omega))
    (bsJ2_hrel h₃ h₄ hj) (bsJ2_hlm h₃ h₄ hj)
    (by simp [*])
    [] [(U11 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n)]) ([(⟨i₃⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V5]) (by simp [V6])
    (by simp [V5, U11, *])

theorem s18 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T17 i₀ i₁ i₂ i₃ i₄ j) (T18 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₁ i₃) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₃ i₁) (farCommRelation_lm i₁ i₃ (by omega))
    (by simp [*])
    [] [(U11 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]) ([(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V6]) (by simp [V7])
    (by simp [V6, U11, *])

theorem s19 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T18 i₀ i₁ i₂ i₃ i₄ j) (T19 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₀ i₃) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₃ i₀) (farCommRelation_lm i₀ i₃ (by omega))
    (by simp [*])
    [] [(U11 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n)]) ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j ++ [(⟨i₃⟩ : HeckeGen n)]) _ _ 1 one_ne_zero
    (by simp [V7]) (by simp [V8])
    (by simp [V7, U11, *])

theorem s20 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T19 i₀ i₁ i₂ i₃ i₄ j) (T20 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (bokutShiaoRelation i₄ i₃ j) (bokutShiaoRelation_mem hn hp h₄ (by omega))
    (bsJ3_hrel h₄ hj) (bsJ3_hlm h₄ hj)
    (by simp [*])
    [] [(U11 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n)]) ([]) _ _ 1 one_ne_zero
    (by simp [V8]) (by simp [V9])
    (by simp [V8, U11, *])

theorem s21 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T20 i₀ i₁ i₂ i₃ i₄ j) (T21 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₂ i₄) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₄ i₂) (farCommRelation_lm i₂ i₄ (by omega))
    (by simp [*])
    [] [(U11 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n)]) ([(⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j) _ _ 1 one_ne_zero
    (by simp [V9]) (by simp [V10])
    (by simp [V9, U11, *])

theorem s22 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T21 i₀ i₁ i₂ i₃ i₄ j) (T22 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₁ i₄) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₄ i₁) (farCommRelation_lm i₁ i₄ (by omega))
    (by simp [*])
    [] [(U11 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]) ([(⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j) _ _ 1 one_ne_zero
    (by simp [V10]) (by simp [V11])
    (by simp [V10, U11, *])

theorem s23 (hn : 0 < n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (_hj : j.val ≤ i₄.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T22 i₀ i₁ i₂ i₃ i₄ j) (T23 i₀ i₁ i₂ i₃ i₄ j) := by
  obtain ⟨g01, g02, g03, g04, g12, g13, g14, g23, g24, g34⟩ := gen_ne h₁ h₂ h₃ h₄
  have g10 := g01.symm
  have g20 := g02.symm
  have g30 := g03.symm
  have g40 := g04.symm
  have g21 := g12.symm
  have g31 := g13.symm
  have g41 := g14.symm
  have g32 := g23.symm
  have g42 := g24.symm
  have g43 := g34.symm
  exact monicStep hn hp (farCommRelation i₀ i₄) (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₄ i₀) (farCommRelation_lm i₀ i₄ (by omega))
    (by simp [*])
    [] [(U11 i₀ i₁ i₂ i₃ i₄ j, -1)]
    ([(⟨i₂⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)]) ([(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j) _ _ 1 one_ne_zero
    (by simp [V11]) (by simp [U11])
    (by simp [V11, U11, *])

end

theorem T23_isZero (i₀ i₁ i₂ i₃ i₄ j : Fin n) : (T23 i₀ i₁ i₂ i₃ i₄ j).isZero := by
  intro m
  simp only [T23, U11, U11,
    AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
  ring

/-- The composition of the rule at the general depth `j` with the rule at
depth `3`, overlapping in the trailing `σᵢ`. -/
noncomputable def oc (i₀ i₁ i₂ i₃ i₄ j : Fin n) (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := bokutShiaoRelation i₁ i₀ j
  rule₂ := bokutShiaoRelation i₁ i₀ i₃
  left := [(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j
  overlap := [(⟨i₀⟩ : HeckeGen n)]
  right := [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]
  lm₁_decomp := by rw [bsJ0_hlm h₁ h₂ h₃ h₄ hj]
  lm₂_decomp := by rw [bsF1_0_3_hlm h₁ h₂ h₃]; rfl
  overlap_nonempty := by simp

/-- **The S-polynomial.** -/
theorem oc_spoly_coeff {i₀ i₁ i₂ i₃ i₄ j : Fin n} (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val)
    (m : Monomial (HeckeGen n)) :
    (oc i₀ i₁ i₂ i₃ i₄ j h₁ h₂ h₃ h₄ hj).spoly.coeff m = (T0 i₀ i₁ i₂ i₃ i₄ j).coeff m := by
  show (bokutShiaoRelation i₁ i₀ i₃).lc (heckeOrder n)
      * (AlgElement.contextMul [] (bokutShiaoRelation i₁ i₀ j).relation
          [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]).coeff m
    - (bokutShiaoRelation i₁ i₀ j).lc (heckeOrder n)
      * (AlgElement.contextMul ([(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j)
          (bokutShiaoRelation i₁ i₀ i₃).relation []).coeff m
    = _
  rw [bokutShiaoRelation_lc h₁ (by omega), bokutShiaoRelation_lc h₁ (by omega),
    one_mul, one_mul,
    AlgElement.contextMul_coeff_congr [] [(⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n), (⟨i₀⟩ : HeckeGen n)]
      (bsJ0_hrel h₁ h₂ h₃ h₄ hj) m,
    AlgElement.contextMul_coeff_congr ([(⟨i₀⟩ : HeckeGen n), (⟨i₁⟩ : HeckeGen n), (⟨i₂⟩ : HeckeGen n), (⟨i₃⟩ : HeckeGen n)] ++ descWord i₄ j) []
      (bsF1_0_3_hrel h₁ h₂ h₃) m]
  simp only [T0, V0, U0,
    AlgElement.contextMul_ofTerms_coeff, List.map_cons,
    List.map_nil, List.nil_append, List.append_nil, List.cons_append,
    List.append_assoc, AlgElement.ofTerms_coeff, List.filter_cons,
    List.filter_nil, decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **23 steps, to zero, at every depth `j ≤ i − 4`.** -/
theorem resolves (hp : HeckeParams) {i₀ i₁ i₂ i₃ i₄ j : Fin n} (hn : 0 < n)
    (h₁ : i₁.val + 1 = i₀.val) (h₂ : i₂.val + 1 = i₁.val) (h₃ : i₃.val + 1 = i₂.val) (h₄ : i₄.val + 1 = i₃.val) (hj : j.val ≤ i₄.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i₀ i₁ i₂ i₃ i₄ j h₁ h₂ h₃ h₄ hj).spoly nf ∧ nf.isZero := by
  refine reducesToZero_congr ⟨T23 i₀ i₁ i₂ i₃ i₄ j,
    ⟨(MultiStepReduction.refl (T0 i₀ i₁ i₂ i₃ i₄ j))
      |>.step (s1 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s2 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s3 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s4 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s5 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s6 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s7 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s8 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s9 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s10 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s11 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s12 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s13 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s14 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s15 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s16 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s17 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s18 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s19 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s20 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s21 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s22 hp hn h₁ h₂ h₃ h₄ hj)
      |>.step (s23 hp hn h₁ h₂ h₃ h₄ hj),
      isNormalForm_of_isZero (T23_isZero i₀ i₁ i₂ i₃ i₄ j)⟩, T23_isZero i₀ i₁ i₂ i₃ i₄ j⟩ ?_
  intro m
  exact oc_spoly_coeff h₁ h₂ h₃ h₄ hj m

end BokutShiaoCornerDepth3

/-! ## §4af  The block that drives the whole `a > b` corner

§4ad and §4ae close the corner's `b = 2` and `b = 3` columns by writing their
fifteen and twenty-three steps out one at a time. That does not scale: the chain
is `b² + 3b + 5` steps long, so column `b` needs a longer script than column
`b − 1` and no fixed script covers them all.

It does not have to. Setting the two columns side by side shows the chain is not
a flat list of steps but **a loop over a single index**, and this section proves
the body of that loop once and for all.

Write `D = descWord i j₁` for the long run and `j₂` for the short one. The claim
is that both terms of the S-polynomial march down through the invariants

    V side:   R ++ D ++ descWord k j₂                →  (R ++ [σ_{k−1}]) ++ D ++ descWord (k−1) j₂
    U side:   Q ++ D ++ descWord k j₂ ++ [σᵢ]        →  (Q ++ [σ_{k−1}]) ++ D ++ descWord (k−1) j₂ ++ [σᵢ]

as `k` runs from `i` down past `j₂`, and that each pass is the same two moves:

* one **Bokut–Shiao step at top `k`**, which is available because the letter `σ_k`
  ending `descWord k j₁` inside `D` is immediately followed by the `σ_k` that
  heads `descWord k j₂` — the two runs meet exactly there, which is what makes
  the redex `bsWord₁ k j₁`; and
* one **leftward transport** of the newly exposed `σ_{k−1}` across the letters of
  `D` lying above `k`, which is `farComm_transport_left` (§4v), its side
  condition supplied by `descWord_index_ge` (every letter of a descending run
  from `i` down to `k+1` has index `> (k−1) + 1`).

`blockStep` below is that pass. The part of `D` above `k` enters as an abstract
`Y` rather than as `descWord i (k+1)`, which costs nothing and avoids naming
`k + 1` — needed, since the first pass has `k = i` and no such index exists.

The counts this predicts are exactly the measured ones. The `V` side runs the
loop for `k = i` down to `j₂`, preceded by two setup steps; the `U` side runs it
for `k = i−1` down to `j₂` and is followed by two closing steps. Each pass at
depth `d = i − k` costs `1 + d`, so

    V = 2 + (b+1) + b(b+1)/2,   U = b + b(b+1)/2 + 2,   V + U = b² + 3b + 5

matching the confluence engine at every `b` from 2 to 7 and every `a > b`,
including `a = b + 1`, where the engine's own deg-lex strategy interleaves the
passes differently but the chain built from these blocks is still a legal
reduction — a `SingleStepReduction` may rewrite any redex, not only the largest.
-/

/-- A descending run from below its own floor is empty. -/
theorem descWord_of_lt {n : ℕ} {i j : Fin n} (hij : i.val < j.val) :
    descWord i j = [] := by
  simp only [descWord, List.map_eq_nil_iff, List.reverse_eq_nil_iff,
    List.filter_eq_nil_iff, decide_eq_true_eq]
  intro k _
  omega

/-- `descWord_cons` at the boundary. The original needs the floor to lie at or
below `i − 1`; this needs it only at or below `i`, the extra case being `j = i`,
where the tail is empty rather than a shorter run. The corner loop's last pass
is exactly that case, so it cannot use the original. -/
theorem descWord_cons_le {n : ℕ} {i' i j : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i.val) :
    descWord i j = (⟨i⟩ : HeckeGen n) :: descWord i' j := by
  rcases le_or_gt j.val i'.val with h | h
  · exact descWord_cons hi h
  · have hji : j = i := Fin.ext (by omega)
    subst hji
    rw [descWord_self, descWord_of_lt h]

namespace CornerBlock

variable {n : ℕ}

/-- **One pass of the corner loop**: a Bokut–Shiao step at top `k`, then the
newly exposed `σ_{k−1}` carried left across `Y`.

`Y` is the part of the long run `descWord i j₁` lying above `k`; `R` is whatever
has already accumulated to the left, `S` whatever trails on the right (empty on
the `V` side, `[σᵢ]` on the `U` side). The two collision hypotheses are the ones
`monicStep` and `farComm_transport_left` ask for: the other terms of the element
must miss the word being rewritten, and must miss every word the transport passes
through. -/
theorem blockStep (hn : 0 < n) (hp : HeckeParams) {i j₁ j₂ k kd : Fin n}
    (hk : kd.val + 1 = k.val) (hj₁ : j₁.val ≤ kd.val) (hj₂ : j₂.val ≤ k.val)
    (Y R S : Monomial (HeckeGen n))
    (hY : ∀ y ∈ Y, kd.val + 1 < y.index.val)
    (hD : descWord i j₁ = Y ++ ((⟨k⟩ : HeckeGen n) :: descWord kd j₁))
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (hne : ∀ q ∈ (L₁ ++ L₂).map Prod.fst,
      q ≠ R ++ (descWord i j₁ ++ (descWord k j₂ ++ S)))
    (hcol : ∀ u v : Monomial (HeckeGen n), u ++ v = Y → u ≠ [] →
      ∀ q ∈ (L₁ ++ L₂).map Prod.fst,
        q ≠ R ++ (u ++ ((⟨kd⟩ : HeckeGen n) ::
          (v ++ (((⟨k⟩ : HeckeGen n) :: descWord kd j₁) ++ (descWord kd j₂ ++ S)))))) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        (L₁ ++ (R ++ (descWord i j₁ ++ (descWord k j₂ ++ S)), c) :: L₂))
      (AlgElement.ofTerms
        (L₁ ++ (R ++ ((⟨kd⟩ : HeckeGen n)
          :: (descWord i j₁ ++ (descWord kd j₂ ++ S))), c) :: L₂)) := by
  have hkdk : (⟨kd⟩ : HeckeGen n) ≠ ⟨k⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  have hdk : descWord k j₂ = (⟨k⟩ : HeckeGen n) :: descWord kd j₂ :=
    descWord_cons_le hk hj₂
  have hLR : bsWord₂ kd k j₁ ≠ bsWord₁ k j₁ := by
    rw [bsWord₁_cons hk hj₁, bsWord₂]
    simp [hkdk]
  -- the word after the Bokut–Shiao step, before anything is transported
  refine MultiStepReduction.head
    (g := AlgElement.ofTerms (L₁ ++ (R ++ (Y ++ ((⟨kd⟩ : HeckeGen n) ::
      (((⟨k⟩ : HeckeGen n) :: descWord kd j₁) ++ (descWord kd j₂ ++ S)))), c) :: L₂))
    ?_ ?_
  · exact monicStep hn hp (bokutShiaoRelation kd k j₁)
      (bokutShiaoRelation_mem hn hp hk hj₁)
      (fun v => rfl) (bokutShiaoRelation_lm hk hj₁) hLR
      L₁ L₂ (R ++ Y) (descWord kd j₂ ++ S) _ _ c hc
      (by rw [hD, hdk, bsWord₁, descWord_cons hk hj₁]; simp)
      (by rw [bsWord₂]; simp)
      (by simpa using hne)
  · have := farComm_transport_left_sources hn hp kd c hc L₁ L₂ Y R
      (((⟨k⟩ : HeckeGen n) :: descWord kd j₁) ++ (descWord kd j₂ ++ S)) hY hcol
    rw [hD]
    simpa using this

/-- **The loop's first pass**, where `k = i` and nothing lies above it: `Y` is
empty and the transport is the identity, so the pass is the Bokut–Shiao step
alone. Only two non-collision facts are needed, one per endpoint — with `Y` empty
the transport passes through no intermediate word. -/
theorem blockStep_top (hn : 0 < n) (hp : HeckeParams) {i j₁ j₂ kd : Fin n}
    (hk : kd.val + 1 = i.val) (hj₁ : j₁.val ≤ kd.val) (hj₂ : j₂.val ≤ kd.val)
    (R S : Monomial (HeckeGen n)) (c : ℝ) (hc : c ≠ 0)
    (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (hne : ∀ q ∈ (L₁ ++ L₂).map Prod.fst,
      q ≠ R ++ (descWord i j₁ ++ (descWord i j₂ ++ S)))
    :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        (L₁ ++ (R ++ (descWord i j₁ ++ (descWord i j₂ ++ S)), c) :: L₂))
      (AlgElement.ofTerms
        (L₁ ++ (R ++ ((⟨kd⟩ : HeckeGen n)
          :: (descWord i j₁ ++ (descWord kd j₂ ++ S))), c) :: L₂)) := by
  refine blockStep hn hp hk hj₁ (by omega) [] R S (by simp)
    (by rw [descWord_cons hk hj₁]; rfl) c hc L₁ L₂ hne ?_
  intro u v huv hu
  exact absurd (List.append_eq_nil_iff.mp huv).1 hu

/-- **The loop.** `blockStep` iterated: `k` walks down from its starting value to
`e`, one pass per index, and what those passes leave behind is the descending run
`descWord kd ed` accumulated in front.

The induction is on the number of passes still to come. It carries `Y` — the part
of the long run lying above `k` — as a parameter rather than as `descWord i (k+1)`,
so each pass hands the next one `Y ++ [σ_k]` and no index above `k` is ever named.

Stated for a single term, where the collision hypotheses of `blockStep` are
vacuous. That is the whole combinatorial content of the `a > b` corner: what
remains for the two-term S-polynomial is bookkeeping about which words the
bystanding term must avoid, not further rewriting. -/
theorem loop (hn : 0 < n) (hp : HeckeParams) {i j₁ j₂ e ed : Fin n}
    (hed : ed.val + 1 = e.val) (hj₁ : j₁.val ≤ ed.val) (hj₂ : j₂.val ≤ e.val)
    (S : Monomial (HeckeGen n)) (c : ℝ) (hc : c ≠ 0) :
    ∀ (m : ℕ) (k kd : Fin n) (A Y : Monomial (HeckeGen n)),
      kd.val + 1 = k.val → k.val = e.val + m →
      (∀ y ∈ Y, kd.val + 1 < y.index.val) →
      descWord i j₁ = Y ++ ((⟨k⟩ : HeckeGen n) :: descWord kd j₁) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms [(A ++ (descWord i j₁ ++ (descWord k j₂ ++ S)), c)])
        (AlgElement.ofTerms
          [(A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c)]) := by
  intro m
  induction m with
  | zero =>
    intro k kd A Y hk hke hY hD
    have hke' : k.val = e.val := by omega
    have hj₂k : j₂.val ≤ k.val := by omega
    have hkde : kd = ed := Fin.ext (by omega)
    subst hkde
    have hstep := blockStep hn hp hk hj₁ hj₂k Y A S hY hD c hc [] []
      (by simp) (by simp)
    rw [descWord_self]
    simpa using hstep
  | succ m ih =>
    intro k kd A Y hk hke hY hD
    have hkdlt : kd.val < n := kd.isLt
    have hkdlow : ed.val ≤ kd.val := by omega
    have hkdpos : 0 < kd.val := by omega
    have hj₁kd : j₁.val ≤ kd.val := by omega
    have hj₂k : j₂.val ≤ k.val := by omega
    refine MultiStepReduction.trans
      (blockStep hn hp hk hj₁kd hj₂k Y A S hY hD c hc [] [] (by simp) (by simp)) ?_
    obtain ⟨kdd, hkdd⟩ : ∃ kdd : Fin n, kdd.val + 1 = kd.val :=
      ⟨⟨kd.val - 1, by omega⟩, by show kd.val - 1 + 1 = kd.val; omega⟩
    have hsplit : descWord kd j₁ = (⟨kd⟩ : HeckeGen n) :: descWord kdd j₁ :=
      descWord_cons_le hkdd (by omega)
    have hrun : descWord kd ed = (⟨kd⟩ : HeckeGen n) :: descWord kdd ed :=
      descWord_cons_le hkdd (by omega)
    have hnext := ih kd kdd (A ++ [(⟨kd⟩ : HeckeGen n)]) (Y ++ [(⟨k⟩ : HeckeGen n)])
      hkdd (by omega)
      (by
        intro y hy
        rcases List.mem_append.mp hy with hy | hy
        · have := hY y hy
          omega
        · have hyk : y = (⟨k⟩ : HeckeGen n) := by simpa using hy
          subst hyk
          show kdd.val + 1 < k.val
          omega)
      (by rw [hD, hsplit]; simp)
    rw [hrun]
    simpa using hnext

/-- **The loop, entered at the top.** The first pass has `k = i`, so nothing of
the long run lies above it and `Y` is empty; `m` is the number of passes less one.
This is the form the corner's two terms are actually reduced by, and it witnesses
that `loop`'s hypotheses are satisfiable. -/
theorem loopFromTop (hn : 0 < n) (hp : HeckeParams) {i j₁ j₂ e ed idd : Fin n}
    (m : ℕ) (hed : ed.val + 1 = e.val) (hj₁ : j₁.val ≤ ed.val)
    (hj₂ : j₂.val ≤ e.val) (hid : idd.val + 1 = i.val) (hm : i.val = e.val + m)
    (A S : Monomial (HeckeGen n)) (c : ℝ) (hc : c ≠ 0) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms [(A ++ (descWord i j₁ ++ (descWord i j₂ ++ S)), c)])
      (AlgElement.ofTerms
        [(A ++ (descWord idd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c)]) :=
  loop hn hp hed hj₁ hj₂ S c hc m i idd A [] hid hm (by simp)
    (by rw [descWord_cons_le hid (by omega)]; simp)

/-! ### Carrying a bystanding term through the loop

The corner's S-polynomial has two terms, so each pass of the loop rewrites one
while the other sits by, and `blockStep` must be told the bystander is not the
word being rewritten. Two facts make that uniform.

First, **the bystander does not move**. At pass `k` it is
`A ++ descWord kd ed ++ ⋯`, and after the pass `A` has grown by `σ_kd` while the
run has shortened to `descWord kdd ed` — so `A ++ [σ_kd] ++ descWord kdd ed` is
again `A ++ descWord kd ed`. It is literally the same word at every pass.

Second, **every word a pass rewrites begins, after `A`, with `σ_i`**, the head of
the long run: the pass's own source is `A ++ (descWord i j₁ ++ ⋯)`, and each word
the transport visits is `A ++ (u ++ ⋯)` with `u` a non-empty prefix of the part of
the long run above `k`. The bystander instead begins with `σ_kd`, and `kd < i`.
So one letter separates the bystander from everything in sight. -/

/-- Two words with a common prefix differ as soon as the next letter does. -/
theorem append_cons_ne {n : ℕ} {A B C : Monomial (HeckeGen n)} {x y : HeckeGen n}
    (hxy : x ≠ y) : A ++ (x :: B) ≠ A ++ (y :: C) := by
  intro hcon
  have h := List.append_cancel_left hcon
  injection h with h1 _
  exact hxy h1

/-- The bystander is not the word the pass rewrites. -/
theorem pass_hne {n : ℕ} {i j₁ j₂ k kd ed : Fin n} (hji : j₁.val ≤ i.val)
    (hedkd : ed.val ≤ kd.val) (hkdi : kd.val < i.val)
    (A S : Monomial (HeckeGen n)) (c' : ℝ) :
    ∀ q ∈ (([] : List (Monomial (HeckeGen n) × ℝ)) ++
        [(A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c')]).map
        Prod.fst,
      q ≠ A ++ (descWord i j₁ ++ (descWord k j₂ ++ S)) := by
  intro q hq
  simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
    List.not_mem_nil, or_false] at hq
  subst hq
  obtain ⟨T, hT⟩ := descWord_head hedkd
  obtain ⟨Dt, hDt⟩ := descWord_head hji
  have hgen : (⟨kd⟩ : HeckeGen n) ≠ ⟨i⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  rw [hT, hDt]
  simp only [List.cons_append]
  exact append_cons_ne hgen

/-- The bystander is not any word the pass's transport visits. Each such word
starts, after `A`, with a letter of the run above `k`, and every one of those is
more than one above `σ_kd`. -/
theorem pass_hcol {n : ℕ} {i j₁ j₂ k kd ed : Fin n} (hedkd : ed.val ≤ kd.val)
    (A S Y : Monomial (HeckeGen n)) (c' : ℝ)
    (hY : ∀ y ∈ Y, kd.val + 1 < y.index.val) :
    ∀ u v : Monomial (HeckeGen n), u ++ v = Y → u ≠ [] →
      ∀ q ∈ (([] : List (Monomial (HeckeGen n) × ℝ)) ++
          [(A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c')]).map
          Prod.fst,
        q ≠ A ++ (u ++ ((⟨kd⟩ : HeckeGen n) ::
          (v ++ (((⟨k⟩ : HeckeGen n) :: descWord kd j₁) ++ (descWord kd j₂ ++ S))))) := by
  intro u v huv hu q hq
  simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
    List.not_mem_nil, or_false] at hq
  subst hq
  obtain ⟨y₀, u', rfl⟩ := List.exists_cons_of_ne_nil hu
  have hy₀ : y₀ ∈ Y := by rw [← huv]; simp
  have hlt := hY y₀ hy₀
  have hgen : (⟨kd⟩ : HeckeGen n) ≠ y₀ := by
    intro hcon
    have h2 : y₀.index = kd := by rw [← hcon]
    rw [h2] at hlt
    omega
  obtain ⟨T, hT⟩ := descWord_head hedkd
  rw [hT]
  simp only [List.cons_append]
  exact append_cons_ne hgen

/-- **The loop, with the S-polynomial's other term riding along.** Same walk as
`loop`, but the element carries a second term throughout — the word the loop is
heading for, which is what the corner's two reductions meet at. Because the
bystander does not move (see above), it is one fixed word and the two
distinctness obligations of each pass are discharged uniformly by `pass_hne` and
`pass_hcol`. -/
theorem loopTwo (hn : 0 < n) (hp : HeckeParams) {i j₁ j₂ e ed : Fin n}
    (hed : ed.val + 1 = e.val) (hj₁ : j₁.val ≤ ed.val) (hj₂ : j₂.val ≤ e.val)
    (hji : j₁.val ≤ i.val) (S : Monomial (HeckeGen n)) (c c' : ℝ) (hc : c ≠ 0) :
    ∀ (m : ℕ) (k kd : Fin n) (A Y : Monomial (HeckeGen n)),
      kd.val + 1 = k.val → k.val = e.val + m → k.val ≤ i.val →
      (∀ y ∈ Y, kd.val + 1 < y.index.val) →
      descWord i j₁ = Y ++ ((⟨k⟩ : HeckeGen n) :: descWord kd j₁) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms
          [(A ++ (descWord i j₁ ++ (descWord k j₂ ++ S)), c),
           (A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c')])
        (AlgElement.ofTerms
          [(A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c),
           (A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c')]) := by
  intro m
  induction m with
  | zero =>
    intro k kd A Y hk hke hki hY hD
    have hj₂k : j₂.val ≤ k.val := by omega
    have hkdi : kd.val < i.val := by omega
    have hkde : kd = ed := Fin.ext (by omega)
    subst hkde
    have hstep := blockStep hn hp hk hj₁ hj₂k Y A S hY hD c hc []
      [(A ++ (descWord kd kd ++ (descWord i j₁ ++ (descWord kd j₂ ++ S))), c')]
      (pass_hne hji (le_refl _) hkdi A S c')
      (pass_hcol (le_refl _) A S Y c' hY)
    simpa [descWord_self] using hstep
  | succ m ih =>
    intro k kd A Y hk hke hki hY hD
    have hkdlt : kd.val < n := kd.isLt
    have hkdlow : ed.val ≤ kd.val := by omega
    have hkdpos : 0 < kd.val := by omega
    have hj₁kd : j₁.val ≤ kd.val := by omega
    have hj₂k : j₂.val ≤ k.val := by omega
    have hkdi : kd.val < i.val := by omega
    refine MultiStepReduction.trans
      (blockStep hn hp hk hj₁kd hj₂k Y A S hY hD c hc []
        [(A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c')]
        (pass_hne hji hkdlow hkdi A S c')
        (pass_hcol hkdlow A S Y c' hY)) ?_
    obtain ⟨kdd, hkdd⟩ : ∃ kdd : Fin n, kdd.val + 1 = kd.val :=
      ⟨⟨kd.val - 1, by omega⟩, by show kd.val - 1 + 1 = kd.val; omega⟩
    have hsplit : descWord kd j₁ = (⟨kd⟩ : HeckeGen n) :: descWord kdd j₁ :=
      descWord_cons_le hkdd (by omega)
    have hrun : descWord kd ed = (⟨kd⟩ : HeckeGen n) :: descWord kdd ed :=
      descWord_cons_le hkdd (by omega)
    have hnext := ih kd kdd (A ++ [(⟨kd⟩ : HeckeGen n)]) (Y ++ [(⟨k⟩ : HeckeGen n)])
      hkdd (by omega) (by omega)
      (by
        intro y hy
        rcases List.mem_append.mp hy with hy | hy
        · have := hY y hy
          omega
        · have hyk : y = (⟨k⟩ : HeckeGen n) := by simpa using hy
          subst hyk
          show kdd.val + 1 < k.val
          omega)
      (by rw [hD, hsplit]; simp)
    rw [hrun]
    simpa using hnext

/-- `loopTwo` entered at the top, where `Y` is empty. This is the shape in which
each of the corner's two terms is actually reduced: `A` is what already sits to
the left of the long run, `S` what trails it (empty for the first term, `[σᵢ]` for
the second), and the second listed term is the word they meet at. -/
theorem loopTwoFromTop (hn : 0 < n) (hp : HeckeParams) {i j₁ j₂ e ed idd : Fin n}
    (m : ℕ) (hed : ed.val + 1 = e.val) (hj₁ : j₁.val ≤ ed.val)
    (hj₂ : j₂.val ≤ e.val) (hid : idd.val + 1 = i.val) (hm : i.val = e.val + m)
    (A S : Monomial (HeckeGen n)) (c c' : ℝ) (hc : c ≠ 0) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        [(A ++ (descWord i j₁ ++ (descWord i j₂ ++ S)), c),
         (A ++ (descWord idd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c')])
      (AlgElement.ofTerms
        [(A ++ (descWord idd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c),
         (A ++ (descWord idd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c')]) :=
  loopTwo hn hp hed hj₁ hj₂ (by omega) S c c' hc m i idd A [] hid hm (le_refl _)
    (by simp) (by rw [descWord_cons_le hid (by omega)]; simp)

/-- **The loop against an arbitrary term list, with the source-only collision
hypothesis.**

Two generalisations of `loopTwo` at once, both forced by the corner.

**Source-only collisions.** `loopTwoGen` below asks that the parked word `P` be
no extension of `A` at all. That is sufficient — every word any pass rewrites
does have the form `A ++ z` — but not necessary, and
`hecke_prefix_head_separation.py` measures where the difference bites: at `2a`
steps of the corner's closing phase no choice of left context satisfies it, while
**every source in the chain is unique**, so the precise condition holds
throughout.

What the loop actually needs is that each parked word differ from the two
families `blockStep` asks about, at every level. The accumulator only ever grows
on the right of `A`, so quantifying over that growth `D` makes the hypothesis
closed under the recursion: descending a level replaces `D` by `σ_kd :: D`.

**An arbitrary term list.** `blockStep` has taken general `L₁`/`L₂` all along;
`loopTwo` and its descendants fixed them to `[(P, c')]` and `[]`, which puts the
parked term *first*. `ofTerms` is a representation rather than a normal form, so
that choice is not free: a chain ending at `[(P, c'), (w, c)]` does not compose
with one starting at `[(w, c), (P, c')]`, even though the two are the same
element. Carrying `L₁` and `L₂` through the induction removes the choice, and
`loopTwoGenSources` / `loopTwoGenRightSources` are the two slots. The corner's
opening phase needs both: the U-side loop parks V and the V-side loop parks U. -/
theorem loopListSources (hn : 0 < n) (hp : HeckeParams) {i j₁ j₂ e ed : Fin n}
    (hed : ed.val + 1 = e.val) (hj₁ : j₁.val ≤ ed.val) (hj₂ : j₂.val ≤ e.val)
    (S : Monomial (HeckeGen n)) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (c : ℝ) (hc : c ≠ 0) :
    ∀ (m : ℕ) (k kd : Fin n) (A Y : Monomial (HeckeGen n)),
      kd.val + 1 = k.val → k.val = e.val + m →
      (∀ P ∈ (L₁ ++ L₂).map Prod.fst,
        ∀ (D Y' : Monomial (HeckeGen n)) (k' kd' : Fin n),
        (P ≠ A ++ (D ++ (descWord i j₁ ++ (descWord k' j₂ ++ S)))) ∧
        (∀ u v : Monomial (HeckeGen n), u ++ v = Y' → u ≠ [] →
          P ≠ A ++ (D ++ (u ++ ((⟨kd'⟩ : HeckeGen n) ::
            (v ++ (((⟨k'⟩ : HeckeGen n) :: descWord kd' j₁) ++
              (descWord kd' j₂ ++ S)))))))) →
      (∀ y ∈ Y, kd.val + 1 < y.index.val) →
      descWord i j₁ = Y ++ ((⟨k⟩ : HeckeGen n) :: descWord kd j₁) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms
          (L₁ ++ (A ++ (descWord i j₁ ++ (descWord k j₂ ++ S)), c) :: L₂))
        (AlgElement.ofTerms
          (L₁ ++
            (A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c)
              :: L₂)) := by
  intro m
  induction m with
  | zero =>
    intro k kd A Y hk hke hP hY hD
    have hj₂k : j₂.val ≤ k.val := by omega
    have hkde : kd = ed := Fin.ext (by omega)
    subst hkde
    have hstep := blockStep hn hp hk hj₁ hj₂k Y A S hY hD c hc L₁ L₂
      (fun q hq => by simpa only [List.nil_append] using (hP q hq [] Y k kd).1)
      (fun u v huv hu q hq => by
        simpa only [List.nil_append] using (hP q hq [] Y k kd).2 u v huv hu)
    simpa [descWord_self] using hstep
  | succ m ih =>
    intro k kd A Y hk hke hP hY hD
    have hkdlt : kd.val < n := kd.isLt
    have hkdlow : ed.val ≤ kd.val := by omega
    have hkdpos : 0 < kd.val := by omega
    have hj₁kd : j₁.val ≤ kd.val := by omega
    have hj₂k : j₂.val ≤ k.val := by omega
    refine MultiStepReduction.trans
      (blockStep hn hp hk hj₁kd hj₂k Y A S hY hD c hc L₁ L₂
        (fun q hq => by simpa only [List.nil_append] using (hP q hq [] Y k kd).1)
        (fun u v huv hu q hq => by
          simpa only [List.nil_append] using (hP q hq [] Y k kd).2 u v huv hu)) ?_
    obtain ⟨kdd, hkdd⟩ : ∃ kdd : Fin n, kdd.val + 1 = kd.val :=
      ⟨⟨kd.val - 1, by omega⟩, by show kd.val - 1 + 1 = kd.val; omega⟩
    have hsplit : descWord kd j₁ = (⟨kd⟩ : HeckeGen n) :: descWord kdd j₁ :=
      descWord_cons_le hkdd (by omega)
    have hrun : descWord kd ed = (⟨kd⟩ : HeckeGen n) :: descWord kdd ed :=
      descWord_cons_le hkdd (by omega)
    have hnext := ih kd kdd (A ++ [(⟨kd⟩ : HeckeGen n)]) (Y ++ [(⟨k⟩ : HeckeGen n)])
      hkdd (by omega)
      (fun q hq D Y' k' kd' => by
        constructor
        · have := (hP q hq ([(⟨kd⟩ : HeckeGen n)] ++ D) Y' k' kd').1
          simpa only [List.append_assoc] using this
        · intro u v huv hu
          have := (hP q hq ([(⟨kd⟩ : HeckeGen n)] ++ D) Y' k' kd').2 u v huv hu
          simpa only [List.append_assoc] using this)
      (by
        intro y hy
        rcases List.mem_append.mp hy with hy | hy
        · have := hY y hy
          omega
        · have hyk : y = (⟨k⟩ : HeckeGen n) := by simpa using hy
          subst hyk
          show kdd.val + 1 < k.val
          omega)
      (by rw [hD, hsplit]; simp)
    rw [hrun]
    simpa using hnext

/-- **The loop with the parked term listed first**, the shape `loopTwoGen` and the
`a > b` corner use. `loopListSources` at `L₁ = [(P, c')]`, `L₂ = []`. -/
theorem loopTwoGenSources (hn : 0 < n) (hp : HeckeParams) {i j₁ j₂ e ed : Fin n}
    (hed : ed.val + 1 = e.val) (hj₁ : j₁.val ≤ ed.val) (hj₂ : j₂.val ≤ e.val)
    (S P : Monomial (HeckeGen n)) (c c' : ℝ) (hc : c ≠ 0) :
    ∀ (m : ℕ) (k kd : Fin n) (A Y : Monomial (HeckeGen n)),
      kd.val + 1 = k.val → k.val = e.val + m →
      (∀ (D Y' : Monomial (HeckeGen n)) (k' kd' : Fin n),
        (P ≠ A ++ (D ++ (descWord i j₁ ++ (descWord k' j₂ ++ S)))) ∧
        (∀ u v : Monomial (HeckeGen n), u ++ v = Y' → u ≠ [] →
          P ≠ A ++ (D ++ (u ++ ((⟨kd'⟩ : HeckeGen n) ::
            (v ++ (((⟨k'⟩ : HeckeGen n) :: descWord kd' j₁) ++
              (descWord kd' j₂ ++ S)))))))) →
      (∀ y ∈ Y, kd.val + 1 < y.index.val) →
      descWord i j₁ = Y ++ ((⟨k⟩ : HeckeGen n) :: descWord kd j₁) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms
          [(P, c'), (A ++ (descWord i j₁ ++ (descWord k j₂ ++ S)), c)])
        (AlgElement.ofTerms
          [(P, c'),
           (A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c)]) :=
  fun m k kd A Y hk hke hP hY hD =>
    loopListSources hn hp hed hj₁ hj₂ S [(P, c')] [] c hc m k kd A Y hk hke
      (fun q hq => by
        simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
          List.not_mem_nil, or_false] at hq
        subst hq
        exact hP)
      hY hD

/-- **The loop with the parked term listed second.** `loopListSources` at
`L₁ = []`, `L₂ = [(P, c')]`.

`AlgElement.ofTerms` is a *representation*, not a normal form: the same element
with its two terms in the other order is a different value, so this does not
follow from `loopTwoGenSources` by rearrangement — it has to be the same
induction against the other slot of `blockStep`'s term list, which is what
`loopListSources` supplies.

The corner's opening phase needs exactly this. `loopTwoGen` forces the parked
term first, so the U-side loop ends at `[(V2, 1), (U0L, −1)]`; the V-side loop
that follows then has the *V* term active with the U term parked, and its source
must therefore list the U term first. Without this variant the two loops do not
compose without a change-of-representation argument. -/
theorem loopTwoGenRightSources (hn : 0 < n) (hp : HeckeParams) {i j₁ j₂ e ed : Fin n}
    (hed : ed.val + 1 = e.val) (hj₁ : j₁.val ≤ ed.val) (hj₂ : j₂.val ≤ e.val)
    (S P : Monomial (HeckeGen n)) (c c' : ℝ) (hc : c ≠ 0) :
    ∀ (m : ℕ) (k kd : Fin n) (A Y : Monomial (HeckeGen n)),
      kd.val + 1 = k.val → k.val = e.val + m →
      (∀ (D Y' : Monomial (HeckeGen n)) (k' kd' : Fin n),
        (P ≠ A ++ (D ++ (descWord i j₁ ++ (descWord k' j₂ ++ S)))) ∧
        (∀ u v : Monomial (HeckeGen n), u ++ v = Y' → u ≠ [] →
          P ≠ A ++ (D ++ (u ++ ((⟨kd'⟩ : HeckeGen n) ::
            (v ++ (((⟨k'⟩ : HeckeGen n) :: descWord kd' j₁) ++
              (descWord kd' j₂ ++ S)))))))) →
      (∀ y ∈ Y, kd.val + 1 < y.index.val) →
      descWord i j₁ = Y ++ ((⟨k⟩ : HeckeGen n) :: descWord kd j₁) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms
          [(A ++ (descWord i j₁ ++ (descWord k j₂ ++ S)), c), (P, c')])
        (AlgElement.ofTerms
          [(A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c),
           (P, c')]) :=
  fun m k kd A Y hk hke hP hY hD =>
    loopListSources hn hp hed hj₁ hj₂ S [] [(P, c')] c hc m k kd A Y hk hke
      (fun q hq => by
        simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
          List.not_mem_nil, or_false] at hq
        subst hq
        exact hP)
      hY hD

/-- `loopTwoGenRightSources` with the sufficient collision hypothesis, matching
`loopTwoGen`. -/
theorem loopTwoGenRight (hn : 0 < n) (hp : HeckeParams) {i j₁ j₂ e ed : Fin n}
    (hed : ed.val + 1 = e.val) (hj₁ : j₁.val ≤ ed.val) (hj₂ : j₂.val ≤ e.val)
    (S P : Monomial (HeckeGen n)) (c c' : ℝ) (hc : c ≠ 0) :
    ∀ (m : ℕ) (k kd : Fin n) (A Y : Monomial (HeckeGen n)),
      kd.val + 1 = k.val → k.val = e.val + m →
      (∀ z : Monomial (HeckeGen n), P ≠ A ++ z) →
      (∀ y ∈ Y, kd.val + 1 < y.index.val) →
      descWord i j₁ = Y ++ ((⟨k⟩ : HeckeGen n) :: descWord kd j₁) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms
          [(A ++ (descWord i j₁ ++ (descWord k j₂ ++ S)), c), (P, c')])
        (AlgElement.ofTerms
          [(A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c),
           (P, c')]) :=
  fun m k kd A Y hk hke hpark hY hD =>
    loopTwoGenRightSources hn hp hed hj₁ hj₂ S P c c' hc m k kd A Y hk hke
      (fun _ _ _ _ => ⟨hpark _, fun _ _ _ _ => hpark _⟩) hY hD

/-- **The loop with a parked term that is not its endpoint.**

`loopTwo` carries the word the loop is heading for. The corner needs the other
arrangement too: while one term of the S-polynomial runs its loop, the other sits
parked at a word of its own. Every word any pass rewrites has the form
`A ++ z` — the accumulator only ever grows on the right of `A` — so a single
hypothesis, that the parked word is not of that form, discharges every
obligation of every pass at once. In the corner it holds for the cheapest of
reasons: the two terms start with different letters. -/
theorem loopTwoGen (hn : 0 < n) (hp : HeckeParams) {i j₁ j₂ e ed : Fin n}
    (hed : ed.val + 1 = e.val) (hj₁ : j₁.val ≤ ed.val) (hj₂ : j₂.val ≤ e.val)
    (S P : Monomial (HeckeGen n)) (c c' : ℝ) (hc : c ≠ 0) :
    ∀ (m : ℕ) (k kd : Fin n) (A Y : Monomial (HeckeGen n)),
      kd.val + 1 = k.val → k.val = e.val + m →
      (∀ z : Monomial (HeckeGen n), P ≠ A ++ z) →
      (∀ y ∈ Y, kd.val + 1 < y.index.val) →
      descWord i j₁ = Y ++ ((⟨k⟩ : HeckeGen n) :: descWord kd j₁) →
      MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
        (AlgElement.ofTerms
          [(P, c'), (A ++ (descWord i j₁ ++ (descWord k j₂ ++ S)), c)])
        (AlgElement.ofTerms
          [(P, c'),
           (A ++ (descWord kd ed ++ (descWord i j₁ ++ (descWord ed j₂ ++ S))), c)]) :=
  fun m k kd A Y hk hke hpark hY hD =>
    loopTwoGenSources hn hp hed hj₁ hj₂ S P c c' hc m k kd A Y hk hke
      (fun _ _ _ _ => ⟨hpark _, fun _ _ _ _ => hpark _⟩) hY hD

end CornerBlock

/-! ## §4ag  The `a > b` corner at every pair of depths

§4ad and §4ae close the columns `b = 2` and `b = 3` one at a time. §4af replaces
the quadratic middle of any such column by a loop. What is left is the ends, and
they are the same four steps whatever the depths are. This section assembles
them.

The chain runs in three phases, in the order the confluence engine takes them:

* **two setup steps** carry the first term from the S-polynomial to the loop's
  entry shape, with the second term parked at `U0`;
* **the second term's whole reduction** — its loop, then a Bokut–Shiao step at
  top `i` and the fixed-depth one at `(i−2, i−1, j₂−1)` — with the first term
  parked at `V2`;
* **the first term's loop**, with the second parked at the word they meet at.

Only the middle of each phase depends on the depths, and that is exactly what
§4af's loop absorbs. Writing `ed` for `j₂ − 1`, the meeting word is
`σᵢ₋₂ ++ descWord (i−1) ed ++ descWord i j₁`. -/

namespace CornerGeneral

variable {n : ℕ}

section

variable {i i₁ i₂ j₁ j₂ ed : Fin n}

/-- The S-polynomial's first term. -/
def V0 (i i₁ j₁ j₂ : Fin n) : Monomial (HeckeGen n) :=
  descWord i j₁ ++ ((⟨i₁⟩ : HeckeGen n) :: descWord i j₂)

/-- After the Bokut–Shiao step at top `i−1`. -/
def V1 (i i₁ i₂ j₁ j₂ : Fin n) : Monomial (HeckeGen n) :=
  [(⟨i⟩ : HeckeGen n)] ++ ((⟨i₂⟩ : HeckeGen n) :: (⟨i₁⟩ : HeckeGen n) :: descWord i₂ j₁)
    ++ descWord i j₂

/-- The first term parked at the loop's entry shape. -/
def V2 (i i₂ j₁ j₂ : Fin n) : Monomial (HeckeGen n) :=
  [(⟨i₂⟩ : HeckeGen n)] ++ (descWord i j₁ ++ (descWord i j₂ ++ []))

/-- The S-polynomial's second term. -/
def U0 (i i₁ j₁ j₂ : Fin n) : Monomial (HeckeGen n) :=
  [(⟨i₁⟩ : HeckeGen n)] ++ (descWord i j₁ ++ (descWord i₁ j₂ ++ [(⟨i⟩ : HeckeGen n)]))

/-- The second term begins with `σᵢ₋₁`, the first with `σᵢ`: that is all the
setup steps need in order to tell them apart. -/
theorem U0_ne_cons (h₁ : i₁.val + 1 = i.val) (X : Monomial (HeckeGen n)) :
    U0 i i₁ j₁ j₂ ≠ (⟨i⟩ : HeckeGen n) :: X := by
  have hgen : (⟨i₁⟩ : HeckeGen n) ≠ ⟨i⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  intro hcon
  simp only [U0, List.singleton_append] at hcon
  injection hcon with h _
  exact hgen h

/-- **Setup step one**: the Bokut–Shiao rule at top `i−1` and the general bottom,
inside `σᵢ · − · descWord i j₂`. -/
theorem s1 (hn : 0 < n) (hp : HeckeParams) (h₁ : i₁.val + 1 = i.val)
    (h₂ : i₂.val + 1 = i₁.val) (hj₁ : j₁.val ≤ i₂.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms [(V0 i i₁ j₁ j₂, (1 : ℝ)), (U0 i i₁ j₁ j₂, -1)])
      (AlgElement.ofTerms [(V1 i i₁ i₂ j₁ j₂, (1 : ℝ)), (U0 i i₁ j₁ j₂, -1)]) := by
  have hgen : (⟨i₂⟩ : HeckeGen n) ≠ ⟨i₁⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  have hLR : bsWord₂ i₂ i₁ j₁ ≠ bsWord₁ i₁ j₁ := by
    rw [bsWord₁_cons h₂ hj₁, bsWord₂]
    simp [hgen]
  exact monicStep hn hp (bokutShiaoRelation i₂ i₁ j₁)
    (bokutShiaoRelation_mem hn hp h₂ hj₁)
    (fun v => rfl) (bokutShiaoRelation_lm h₂ hj₁) hLR
    [] [(U0 i i₁ j₁ j₂, -1)]
    [(⟨i⟩ : HeckeGen n)] (descWord i j₂) _ _ 1 one_ne_zero
    (by simp [V0, bsWord₁, descWord_cons h₁ (show j₁.val ≤ i₁.val by omega)])
    (by simp [V1, bsWord₂])
    (by
      intro q hq
      simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      rw [V0, descWord_cons h₁ (show j₁.val ≤ i₁.val by omega)]
      simpa using U0_ne_cons h₁ _)

/-- **Setup step two**: `σᵢσᵢ₋₂ → σᵢ₋₂σᵢ`, which puts the first term into the
shape the loop is entered in. -/
theorem s2 (hn : 0 < n) (hp : HeckeParams) (h₁ : i₁.val + 1 = i.val)
    (h₂ : i₂.val + 1 = i₁.val) (hj₁ : j₁.val ≤ i₂.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms [(V1 i i₁ i₂ j₁ j₂, (1 : ℝ)), (U0 i i₁ j₁ j₂, -1)])
      (AlgElement.ofTerms [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U0 i i₁ j₁ j₂, -1)]) := by
  have hgen : (⟨i₂⟩ : HeckeGen n) ≠ ⟨i⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  exact monicStep hn hp (farCommRelation i i₂)
    (farCommRelation_mem hn hp (by omega))
    (BokutShiaoBraid.far_hrel i₂ i) (farCommRelation_lm i i₂ (by omega))
    (by simp [hgen])
    [] [(U0 i i₁ j₁ j₂, -1)]
    [] (((⟨i₁⟩ : HeckeGen n) :: descWord i₂ j₁) ++ descWord i j₂) _ _ 1 one_ne_zero
    (by simp [V1])
    (by
      simp [V2, descWord_cons h₁ (show j₁.val ≤ i₁.val by omega),
        descWord_cons h₂ hj₁])
    (by
      intro q hq
      simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      rw [V1]
      simpa using U0_ne_cons h₁ _)

/-- The second term after its loop. -/
def U1 (i i₁ i₂ j₁ j₂ ed : Fin n) : Monomial (HeckeGen n) :=
  [(⟨i₁⟩ : HeckeGen n)] ++ (descWord i₂ ed ++
    (descWord i j₁ ++ (descWord ed j₂ ++ [(⟨i⟩ : HeckeGen n)])))

/-- The second term after the Bokut–Shiao step at top `i`. -/
def U2 (i i₁ i₂ j₁ ed : Fin n) : Monomial (HeckeGen n) :=
  ([(⟨i₁⟩ : HeckeGen n)] ++ descWord i₂ ed)
    ++ ((⟨i₁⟩ : HeckeGen n) :: (⟨i⟩ : HeckeGen n) :: descWord i₁ j₁)

/-- The word the two reductions meet at. -/
def W (i i₁ i₂ j₁ j₂ ed : Fin n) : Monomial (HeckeGen n) :=
  [(⟨i₂⟩ : HeckeGen n)] ++ (descWord i₁ ed ++
    (descWord i j₁ ++ (descWord ed j₂ ++ [])))

/-- The parked first term begins with `σᵢ₋₂`, the second with `σᵢ₋₁`. -/
theorem V2_ne_cons (h₂ : i₂.val + 1 = i₁.val) (X : Monomial (HeckeGen n)) :
    V2 i i₂ j₁ j₂ ≠ (⟨i₁⟩ : HeckeGen n) :: X := by
  have hgen : (⟨i₂⟩ : HeckeGen n) ≠ ⟨i₁⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  intro hcon
  simp only [V2, List.singleton_append] at hcon
  injection hcon with h _
  exact hgen h

/-- **Closing step one**: the Bokut–Shiao rule at top `i`, at the tail. -/
theorem s3 (hn : 0 < n) (hp : HeckeParams) (h₁ : i₁.val + 1 = i.val)
    (h₂ : i₂.val + 1 = i₁.val) (hed : ed.val + 1 = j₂.val)
    (hj₁ : j₁.val ≤ ed.val) (hj₂ : j₂.val ≤ i₂.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U1 i i₁ i₂ j₁ j₂ ed, -1)])
      (AlgElement.ofTerms
        [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U2 i i₁ i₂ j₁ ed, -1)]) := by
  have hedj : descWord ed j₂ = [] := descWord_of_lt (by omega)
  have hgen : (⟨i₁⟩ : HeckeGen n) ≠ ⟨i⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  have hLR : bsWord₂ i₁ i j₁ ≠ bsWord₁ i j₁ := by
    rw [bsWord₁_cons h₁ (show j₁.val ≤ i₁.val by omega), bsWord₂]
    simp [hgen]
  exact monicStep hn hp (bokutShiaoRelation i₁ i j₁)
    (bokutShiaoRelation_mem hn hp h₁ (show j₁.val ≤ i₁.val by omega))
    (fun v => rfl) (bokutShiaoRelation_lm h₁ (show j₁.val ≤ i₁.val by omega)) hLR
    [(V2 i i₂ j₁ j₂, (1 : ℝ))] []
    ([(⟨i₁⟩ : HeckeGen n)] ++ descWord i₂ ed) [] _ _ (-1)
    (neg_ne_zero.mpr one_ne_zero)
    (by simp [U1, bsWord₁, hedj])
    (by simp [U2, bsWord₂])
    (by
      intro q hq
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      rw [U1]
      simpa using V2_ne_cons h₂ _)

/-- **Closing step two**: the fixed-depth Bokut–Shiao rule at `(i−2, i−1, j₂−1)`,
at the head. This lands on the word the first term's loop is heading for. -/
theorem s4 (hn : 0 < n) (hp : HeckeParams) (h₁ : i₁.val + 1 = i.val)
    (h₂ : i₂.val + 1 = i₁.val) (hed : ed.val + 1 = j₂.val)
    (hj₁ : j₁.val ≤ ed.val) (hj₂ : j₂.val ≤ i₂.val) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U2 i i₁ i₂ j₁ ed, -1)])
      (AlgElement.ofTerms
        [(V2 i i₂ j₁ j₂, (1 : ℝ)), (W i i₁ i₂ j₁ j₂ ed, -1)]) := by
  have hedj : descWord ed j₂ = [] := descWord_of_lt (by omega)
  have hedi₂ : ed.val ≤ i₂.val := by omega
  have hgen : (⟨i₂⟩ : HeckeGen n) ≠ ⟨i₁⟩ := by
    intro hcon
    have := congrArg HeckeGen.rank hcon
    simp only [HeckeGen.rank] at this
    omega
  have hLR : bsWord₂ i₂ i₁ ed ≠ bsWord₁ i₁ ed := by
    rw [bsWord₁_cons h₂ hedi₂, bsWord₂]
    simp [hgen]
  exact monicStep hn hp (bokutShiaoRelation i₂ i₁ ed)
    (bokutShiaoRelation_mem hn hp h₂ hedi₂)
    (fun v => rfl) (bokutShiaoRelation_lm h₂ hedi₂) hLR
    [(V2 i i₂ j₁ j₂, (1 : ℝ))] []
    [] (descWord i j₁) _ _ (-1) (neg_ne_zero.mpr one_ne_zero)
    (by
      simp [U2, bsWord₁, descWord_cons h₂ hedi₂,
        descWord_cons h₁ (show j₁.val ≤ i₁.val by omega)])
    (by simp [W, bsWord₂, hedj, descWord_cons h₂ hedi₂])
    (by
      intro q hq
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      rw [U2]
      simpa using V2_ne_cons h₂ _)

end

noncomputable def T0 (i i₁ j₁ j₂ : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V0 i i₁ j₁ j₂, (1 : ℝ)), (U0 i i₁ j₁ j₂, -1)]

noncomputable def T1 (i i₁ i₂ j₁ j₂ : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V1 i i₁ i₂ j₁ j₂, (1 : ℝ)), (U0 i i₁ j₁ j₂, -1)]

noncomputable def T2 (i i₁ i₂ j₁ j₂ : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U0 i i₁ j₁ j₂, -1)]

noncomputable def T3 (i i₁ i₂ j₁ j₂ ed : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U1 i i₁ i₂ j₁ j₂ ed, -1)]

noncomputable def T4 (i i₁ i₂ j₁ j₂ ed : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U2 i i₁ i₂ j₁ ed, -1)]

noncomputable def T5 (i i₁ i₂ j₁ j₂ ed : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [(V2 i i₂ j₁ j₂, (1 : ℝ)), (W i i₁ i₂ j₁ j₂ ed, -1)]

noncomputable def T6 (i i₁ i₂ j₁ j₂ ed : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(W i i₁ i₂ j₁ j₂ ed, (1 : ℝ)), (W i i₁ i₂ j₁ j₂ ed, -1)]

theorem T6_isZero (i i₁ i₂ j₁ j₂ ed : Fin n) : (T6 i i₁ i₂ j₁ j₂ ed).isZero := by
  intro m
  simp only [T6, AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]
  ring

section

variable {i i₁ i₂ j₁ j₂ ed : Fin n}

/-- **The whole chain.** Two setup steps, the second term's loop, its two closing
steps, then the first term's loop — and the two terms coincide. -/
theorem chain (hn : 0 < n) (hp : HeckeParams) (h₁ : i₁.val + 1 = i.val)
    (h₂ : i₂.val + 1 = i₁.val) (hed : ed.val + 1 = j₂.val)
    (hj₁ : j₁.val ≤ ed.val) (hj₂ : j₂.val ≤ i₂.val) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T0 i i₁ j₁ j₂) (T6 i i₁ i₂ j₁ j₂ ed) := by
  have hsetup : MultiStepReduction (heckeOrder n)
      (heckeCompletedRewritingSystem n hn hp) (T0 i i₁ j₁ j₂) (T2 i i₁ i₂ j₁ j₂) :=
    ((MultiStepReduction.refl _).step (s1 hn hp h₁ h₂ (by omega))).step
      (s2 hn hp h₁ h₂ (by omega))
  have hloopU : MultiStepReduction (heckeOrder n)
      (heckeCompletedRewritingSystem n hn hp) (T2 i i₁ i₂ j₁ j₂)
      (T3 i i₁ i₂ j₁ j₂ ed) :=
    CornerBlock.loopTwoGen hn hp hed hj₁ (le_refl _) [(⟨i⟩ : HeckeGen n)] (V2 i i₂ j₁ j₂)
      (-1) 1 (neg_ne_zero.mpr one_ne_zero)
      (i₁.val - j₂.val) i₁ i₂ [(⟨i₁⟩ : HeckeGen n)] [(⟨i⟩ : HeckeGen n)]
      h₂ (by omega)
      (fun z => by simpa using V2_ne_cons h₂ z)
      (by
        intro y hy
        have hyi : y = (⟨i⟩ : HeckeGen n) := by simpa using hy
        subst hyi
        show i₂.val + 1 < i.val
        omega)
      (by
        rw [descWord_cons h₁ (show j₁.val ≤ i₁.val by omega),
          descWord_cons h₂ (show j₁.val ≤ i₂.val by omega)]
        simp)
  have hclose : MultiStepReduction (heckeOrder n)
      (heckeCompletedRewritingSystem n hn hp) (T3 i i₁ i₂ j₁ j₂ ed)
      (T5 i i₁ i₂ j₁ j₂ ed) :=
    ((MultiStepReduction.refl _).step (s3 hn hp h₁ h₂ hed hj₁ hj₂)).step
      (s4 hn hp h₁ h₂ hed hj₁ hj₂)
  have hloopV : MultiStepReduction (heckeOrder n)
      (heckeCompletedRewritingSystem n hn hp) (T5 i i₁ i₂ j₁ j₂ ed)
      (T6 i i₁ i₂ j₁ j₂ ed) :=
    CornerBlock.loopTwoFromTop hn hp (i.val - j₂.val) hed hj₁ (le_refl _) h₁ (by omega)
      [(⟨i₂⟩ : HeckeGen n)] [] 1 (-1) one_ne_zero
  exact (hsetup.trans hloopU).trans (hclose.trans hloopV)

end

/-- The composition: the Bokut–Shiao rule at the deeper bottom `j₁` against the
one at `j₂`, overlapping in the trailing `σᵢ`. -/
noncomputable def oc (i i₁ j₁ j₂ : Fin n) (h₁ : i₁.val + 1 = i.val)
    (hj₁ : j₁.val ≤ i₁.val) (hj₂ : j₂.val ≤ i₁.val) :
    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where
  rule₁ := bokutShiaoRelation i₁ i j₁
  rule₂ := bokutShiaoRelation i₁ i j₂
  left := descWord i j₁
  overlap := [(⟨i⟩ : HeckeGen n)]
  right := descWord i₁ j₂ ++ [(⟨i⟩ : HeckeGen n)]
  lm₁_decomp := by rw [bokutShiaoRelation_lm h₁ hj₁]; rfl
  lm₂_decomp := by
    rw [bokutShiaoRelation_lm h₁ hj₂, bsWord₁, descWord_cons h₁ hj₂]
    simp
  overlap_nonempty := by simp

/-- **The S-polynomial** is `V0 − U0`. The two leading words cancel because the
short run splits as `descWord i j₂ = σᵢ :: descWord (i−1) j₂`, which is exactly
the overlap.

**This is regime-independent, and that is worth stating.** Neither `oc` nor this
identity relates `j₁` to `j₂` — both ask only `j₁ ≤ i₁` and `j₂ ≤ i₁`. So the
overlap composition and its S-polynomial are *already* established for the
`a ≤ b` regime (`j₂ ≤ j₁`), diagonal `j₂ = j₁` included, and not only for the
`a > b` regime this namespace's `chain` and `resolves` go on to close. What is
regime-specific is the reduction chain from `T0` to zero, nothing before it.

Recorded because the `a ≤ b` arc (bean `qou-auq3`) had been carrying
"`OverlapComposition` + `spoly`" on its open list, which was wrong: both were in
the corpus, generic in both depths, the whole time. Verified by instantiating
this lemma at `j₂ ≤ j₁` and at `j₂ = j₁`. -/
theorem oc_spoly_coeff {i i₁ j₁ j₂ : Fin n} (h₁ : i₁.val + 1 = i.val)
    (hj₁ : j₁.val ≤ i₁.val) (hj₂ : j₂.val ≤ i₁.val) (m : Monomial (HeckeGen n)) :
    (oc i i₁ j₁ j₂ h₁ hj₁ hj₂).spoly.coeff m = (T0 i i₁ j₁ j₂).coeff m := by
  show (bokutShiaoRelation i₁ i j₂).lc (heckeOrder n)
      * (AlgElement.contextMul [] (bokutShiaoRelation i₁ i j₁).relation
          (descWord i₁ j₂ ++ [(⟨i⟩ : HeckeGen n)])).coeff m
    - (bokutShiaoRelation i₁ i j₁).lc (heckeOrder n)
      * (AlgElement.contextMul (descWord i j₁)
          (bokutShiaoRelation i₁ i j₂).relation []).coeff m
    = _
  rw [bokutShiaoRelation_lc h₁ hj₂, bokutShiaoRelation_lc h₁ hj₁, one_mul, one_mul]
  simp only [T0, V0, U0, bokutShiaoRelation, bsWord₁, bsWord₂,
    descWord_cons h₁ hj₂, descWord_cons h₁ hj₁,
    AlgElement.contextMul_ofTerms_coeff, List.map_cons, List.map_nil,
    List.nil_append, List.append_nil, List.cons_append, List.append_assoc,
    AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,
    decide_eq_true_eq]
  split_ifs <;>
    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring

/-- **The `a > b` corner, at every pair of depths.** The Bokut–Shiao rule at
bottom `j₁` composed with the one at bottom `j₂`, whenever `j₁ < j₂ ≤ i − 2`,
reduces to zero. No bound on either depth, and the chain's length — quadratic in
them — is carried entirely by §4af's loop. -/
theorem resolves (hp : HeckeParams) {i i₁ i₂ j₁ j₂ ed : Fin n} (hn : 0 < n)
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hed : ed.val + 1 = j₂.val) (hj₁ : j₁.val ≤ ed.val) (hj₂ : j₂.val ≤ i₂.val) :
    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (oc i i₁ j₁ j₂ h₁ (by omega) (by omega)).spoly nf ∧ nf.isZero := by
  refine reducesToZero_congr ⟨T6 i i₁ i₂ j₁ j₂ ed,
    ⟨chain hn hp h₁ h₂ hed hj₁ hj₂,
      isNormalForm_of_isZero (T6_isZero i i₁ i₂ j₁ j₂ ed)⟩,
    T6_isZero i i₁ i₂ j₁ j₂ ed⟩ ?_
  intro m
  exact oc_spoly_coeff h₁ (by omega) (by omega) m

end CornerGeneral

/-! ### §4am  The `a ≤ b` tail, assembled — and why the order is not the engine's

Everything the tail needs has been in the file since §4al: two `blockPass`
applications, two Bokut–Shiao steps, and the two `descWord` splittings that make
the terms meet. What was missing is the *schedule*, and it is not the engine's.

`hecke_tail_collision_check.py` measured `blockPass`'s collision hypothesis
`hpark` — no other term is any extension of the block's left context — at both
applications, under the order the confluence engine produces (block 1, the two
Bokut–Shiao steps, block 2). It **holds at the first and fails at the second**,
8/8 off the diagonal. It fails for one reason: that block's last step emits the
bystander, and that emission is the cancellation which ends the chain.

The reflex is to weaken `hpark` — to propagate down the source-only relaxation
`farComm_transport_right_sources` already carries, since `SingleStepReduction`
reads `f.coeff (a ++ lm ++ b)` off the **source** side and a collision on a word
the block only ever *produces* costs nothing. That is three lemmas restated, and
the relaxed proof would then owe an argument that a block's destination differs
from each of its own intermediate sources.

**None of it is needed.** The tail's two blocks act on *different terms*, so
their steps commute, and `MultiStepReduction` fixes no order beyond each step's
redex being present. Deg-lex runs block 1 first; that is the engine's scheduling
accident, not a constraint on the Lean. Run block 2 first and its bystander is
term 1 in its *pre*-block form, which does not extend `σ_{i−2} :: A` at all —
and by the time term 1 moves, term 2 sits at a word beginning `σ_{i−2}`, which
does not extend `A`. `hecke_tail_reorder_check.py` measures both, together with
every source being unique and the chain still reaching zero, 8/8.

The last step lands on the bystander, and that is legal: `monicStep` constrains
its **source** (`hne`), never its target. The landing *is* the cancellation, and
the two terms then differ only in sign — the `a > b` regime's own ending, where
`chain` stops at `T6` and `T6_isZero` finishes the job.

The two words meet because of two splittings of one descending run, nothing more:

    descWord id j₂ = descWord id jpp ++ descWord jp j₂
    descWord i  jp = descWord i jppp ++ descWord jpp jp

both instances of `descWord_split`. -/


theorem bsStep {n : ℕ} (hn : 0 < n) (hp : HeckeParams) {i' i j : Fin n}
    (hi : i'.val + 1 = i.val) (hj : j.val ≤ i'.val)
    (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (a b W W' : Monomial (HeckeGen n)) (c : ℝ) (hc : c ≠ 0)
    (hW : W = a ++ bsWord₁ i j ++ b) (hW' : W' = a ++ bsWord₂ i' i j ++ b)
    (hne : ∀ q ∈ (L₁ ++ L₂).map Prod.fst, q ≠ W) :
    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++ (W, c) :: L₂))
      (AlgElement.ofTerms (L₁ ++ (W', c) :: L₂)) :=
  monicStep hn hp (bokutShiaoRelation i' i j) (bokutShiaoRelation_mem hn hp hi hj)
    (fun _ => rfl) (bokutShiaoRelation_lm hi hj) (bsWord₂_ne_bsWord₁ hi hj)
    L₁ L₂ a b W W' c hc hW hW' hne

theorem heckeGen_ne_of_val_ne {n : ℕ} {x y : Fin n} (h : x.val ≠ y.val) :
    (⟨x⟩ : HeckeGen n) ≠ ⟨y⟩ := by
  intro hcon
  have := congrArg HeckeGen.rank hcon
  simp only [HeckeGen.rank] at this
  omega

theorem tailChain {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    {i id idd j₂ jm j₁ jp jpp jppp : Fin n}
    (hid : id.val + 1 = i.val) (hidd : idd.val + 1 = id.val)
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ jm.val) (hjppid : jpp.val ≤ id.val)
    (c : ℝ) (hc : c ≠ 0) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        [((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord i jppp ++
            ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩] ++
              ((⟨jp⟩ : HeckeGen n) :: descWord jm j₂)))), c),
         (descWord id jpp ++ (descWord i jppp ++
            ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩] ++
              ((⟨jp⟩ : HeckeGen n) :: (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)])))), -c)])
      (AlgElement.ofTerms
        [((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
            (descWord i jppp ++ descWord jpp jp))), c),
         ((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
            (descWord i jppp ++ descWord jpp jp))), -c)]) := by
  have hcn : -c ≠ 0 := neg_ne_zero.mpr hc
  have hAcons : descWord id jpp = (⟨id⟩ : HeckeGen n) :: descWord idd jpp :=
    descWord_cons_le hidd hjppid
  have hDcons : descWord id j₂ = (⟨id⟩ : HeckeGen n) :: descWord idd j₂ :=
    descWord_cons_le hidd (by omega)
  have hidd_ne : (⟨idd⟩ : HeckeGen n) ≠ ⟨id⟩ := heckeGen_ne_of_val_ne (by omega)
  -- the two splittings that make the two terms meet
  have hsplitA : descWord id j₂ = descWord id jpp ++ descWord jp j₂ :=
    descWord_split hjpp (by omega) hjppid
  have hsplitI : descWord i jp = descWord i jppp ++ descWord jpp jp :=
    descWord_split hjppp (by omega) (by omega)
  have hicons : descWord i jp = (⟨i⟩ : HeckeGen n) :: descWord id jp :=
    descWord_cons hid (by omega)
  -- STEP 1 -- the block on the SECOND term, run first: its bystander is the
  -- first term in its PRE-block form, which does not extend `⟨idd⟩ :: A`.
  have s1 := blockPass (i := i) hn hp hjm hjp hjpp hjppp hj₂ c hc
    ([] : List (Monomial (HeckeGen n) × ℝ))
    [(descWord id jpp ++ (descWord i jppp ++
        ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩] ++
          ((⟨jp⟩ : HeckeGen n) :: (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)])))), -c)]
    ((⟨idd⟩ : HeckeGen n) :: descWord id jpp) []
    (fun r hr z => by
      simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hr
      subst hr
      intro hcon
      rw [hAcons] at hcon
      simp only [List.cons_append] at hcon
      exact hidd_ne (List.cons.inj hcon).1.symm)
  -- STEP 2 -- the block on the FIRST term, whose bystander is now term 2 at
  -- its destination -- which starts `⟨idd⟩` and so does not extend `A`.
  have s2 := blockPass (i := i) hn hp hjm hjp hjpp hjppp hj₂ (-c) hcn
    [((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
        (descWord i jppp ++ (descWord jpp jp ++ [])))), c)]
    ([] : List (Monomial (HeckeGen n) × ℝ))
    (descWord id jpp) [(⟨i⟩ : HeckeGen n)]
    (fun r hr z => by
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hr
      subst hr
      intro hcon
      rw [hAcons] at hcon
      simp only [List.cons_append] at hcon
      exact hidd_ne (List.cons.inj hcon).1)
  -- STEP 3 -- the first of the two closing Bokut-Shiao steps, at bottom `jp`.
  have s3 := bsStep (i' := id) (i := i) (j := jp) hn hp hid (by omega)
    [((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
        (descWord i jppp ++ (descWord jpp jp ++ [])))), c)]
    ([] : List (Monomial (HeckeGen n) × ℝ))
    (descWord id j₂) []
    (descWord id jpp ++ (descWord jp j₂ ++ (descWord i jppp ++
      (descWord jpp jp ++ [(⟨i⟩ : HeckeGen n)]))))
    (descWord id j₂ ++ bsWord₂ id i jp ++ [])
    (-c) hcn
    (by simp only [bsWord₁, hsplitA, hsplitI, List.append_assoc, List.append_nil])
    rfl
    (fun q hq => by
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      intro hcon
      rw [hAcons] at hcon
      simp only [List.cons_append] at hcon
      exact hidd_ne (List.cons.inj hcon).1)
  -- STEP 4 -- the second, at bottom `j₂`, one level lower. Its target is the
  -- OTHER term's word: `monicStep` constrains the source only, so landing on
  -- the bystander is legal, and that landing IS the cancellation.
  have s4 := bsStep (i' := idd) (i := id) (j := j₂) hn hp hidd (by omega)
    [((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
        (descWord i jppp ++ (descWord jpp jp ++ [])))), c)]
    ([] : List (Monomial (HeckeGen n) × ℝ))
    [] ((⟨i⟩ : HeckeGen n) :: descWord id jp)
    (descWord id j₂ ++ bsWord₂ id i jp ++ [])
    ((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
      (descWord i jppp ++ descWord jpp jp))))
    (-c) hcn
    (by simp only [bsWord₁, bsWord₂, List.nil_append, List.append_nil,
      List.append_assoc, List.cons_append])
    (by simp only [bsWord₂, List.nil_append, List.cons_append, ← hDcons,
      ← hicons, hsplitA, hsplitI, List.append_assoc])
    (fun q hq => by
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      intro hcon
      rw [hDcons] at hcon
      simp only [List.cons_append] at hcon
      exact hidd_ne (List.cons.inj hcon).1)
  simp only [List.nil_append, List.cons_append, List.append_nil]
    at s1 s2 s3 s4 ⊢
  exact ((s1.trans s2).step s3).step s4

/-- The tail's index hypotheses are satisfiable, so `tailChain` is not vacuous.
These are `a = 4`, `b = 6` at `n = 13` — the case the probes measure. -/
theorem tailChain_indices_nonvacuous :
    ∃ (i id idd j₂ jm j₁ jp jpp jppp : Fin 13),
      id.val + 1 = i.val ∧ idd.val + 1 = id.val ∧ jm.val + 1 = j₁.val ∧
      j₁.val + 1 = jp.val ∧ jp.val + 1 = jpp.val ∧ jpp.val + 1 = jppp.val ∧
      j₂.val ≤ jm.val ∧ jpp.val ≤ id.val :=
  ⟨11, 10, 9, 5, 6, 7, 8, 9, 10, by decide⟩


/-- **The tail from the block's second level on — the diagonal included.**

`tailChain` above asks `j₂ ≤ jm`, so it is off-diagonal only. This asks
`j₂ ≤ j₁`, and at `b = a` the two coincide: the same relation `blockPass` and
`blockPassFromTwo` stand in, one level up.

Neither statement subsumes the other, because their *sources* differ. On the
diagonal the block is one level shorter and `blockPassFromTwo`'s source word is
not `blockPass`'s — the trailing `σ_jp` sits on the other side of the descending
run, one transport later. So this is not `tailChain` with a weakened hypothesis;
it is the same four-step argument starting from the later word.

Everything after the two blocks is *identical* to `tailChain`'s, and measurement
says so rather than inspection: `hecke_tail_diagonal_check.py` finds the
diagonal's two Bokut–Shiao steps and its endpoint word to be the same as the
off-diagonal's, with only the block source differing — and finds the same
collision pattern, `hpark` failing under the engine's order at the second block
and holding under the reordered one, 4/4 at `a = b = 3..6`. -/
theorem tailChainFromTwo {n : ℕ} (hn : 0 < n) (hp : HeckeParams)
    {i id idd j₂ j₁ jp jpp jppp : Fin n}
    (hid : id.val + 1 = i.val) (hidd : idd.val + 1 = id.val)
    (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ j₁.val) (hjppid : jpp.val ≤ id.val)
    (c : ℝ) (hc : c ≠ 0) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        [((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord i jppp ++
            ([(⟨jp⟩ : HeckeGen n)] ++ ((⟨jpp⟩ : HeckeGen n) ::
              (descWord j₁ j₂ ++ [(⟨jp⟩ : HeckeGen n)]))))), c),
         (descWord id jpp ++ (descWord i jppp ++
            ([(⟨jp⟩ : HeckeGen n)] ++ ((⟨jpp⟩ : HeckeGen n) ::
              (descWord j₁ j₂ ++ ([(⟨jp⟩ : HeckeGen n)] ++
                [(⟨i⟩ : HeckeGen n)]))))), -c)])
      (AlgElement.ofTerms
        [((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
            (descWord i jppp ++ descWord jpp jp))), c),
         ((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
            (descWord i jppp ++ descWord jpp jp))), -c)]) := by
  have hcn : -c ≠ 0 := neg_ne_zero.mpr hc
  have hAcons : descWord id jpp = (⟨id⟩ : HeckeGen n) :: descWord idd jpp :=
    descWord_cons_le hidd hjppid
  have hDcons : descWord id j₂ = (⟨id⟩ : HeckeGen n) :: descWord idd j₂ :=
    descWord_cons_le hidd (by omega)
  have hidd_ne : (⟨idd⟩ : HeckeGen n) ≠ ⟨id⟩ := heckeGen_ne_of_val_ne (by omega)
  have hsplitA : descWord id j₂ = descWord id jpp ++ descWord jp j₂ :=
    descWord_split hjpp (by omega) hjppid
  have hsplitI : descWord i jp = descWord i jppp ++ descWord jpp jp :=
    descWord_split hjppp (by omega) (by omega)
  have hicons : descWord i jp = (⟨i⟩ : HeckeGen n) :: descWord id jp :=
    descWord_cons hid (by omega)
  have s1 := blockPassFromTwo (i := i) hn hp hjp hjpp hjppp hj₂ c hc
    ([] : List (Monomial (HeckeGen n) × ℝ))
    [(descWord id jpp ++ (descWord i jppp ++
        ([(⟨jp⟩ : HeckeGen n)] ++ ((⟨jpp⟩ : HeckeGen n) ::
          (descWord j₁ j₂ ++ ([(⟨jp⟩ : HeckeGen n)] ++
            [(⟨i⟩ : HeckeGen n)]))))), -c)]
    ((⟨idd⟩ : HeckeGen n) :: descWord id jpp) []
    (fun r hr z => by
      simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hr
      subst hr
      intro hcon
      rw [hAcons] at hcon
      simp only [List.cons_append] at hcon
      exact hidd_ne (List.cons.inj hcon).1.symm)
  have s2 := blockPassFromTwo (i := i) hn hp hjp hjpp hjppp hj₂ (-c) hcn
    [((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
        (descWord i jppp ++ (descWord jpp jp ++ [])))), c)]
    ([] : List (Monomial (HeckeGen n) × ℝ))
    (descWord id jpp) [(⟨i⟩ : HeckeGen n)]
    (fun r hr z => by
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hr
      subst hr
      intro hcon
      rw [hAcons] at hcon
      simp only [List.cons_append] at hcon
      exact hidd_ne (List.cons.inj hcon).1)
  have s3 := bsStep (i' := id) (i := i) (j := jp) hn hp hid (by omega)
    [((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
        (descWord i jppp ++ (descWord jpp jp ++ [])))), c)]
    ([] : List (Monomial (HeckeGen n) × ℝ))
    (descWord id j₂) []
    (descWord id jpp ++ (descWord jp j₂ ++ (descWord i jppp ++
      (descWord jpp jp ++ [(⟨i⟩ : HeckeGen n)]))))
    (descWord id j₂ ++ bsWord₂ id i jp ++ [])
    (-c) hcn
    (by simp only [bsWord₁, hsplitA, hsplitI, List.append_assoc, List.append_nil])
    rfl
    (fun q hq => by
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      intro hcon
      rw [hAcons] at hcon
      simp only [List.cons_append] at hcon
      exact hidd_ne (List.cons.inj hcon).1)
  have s4 := bsStep (i' := idd) (i := id) (j := j₂) hn hp hidd (by omega)
    [((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
        (descWord i jppp ++ (descWord jpp jp ++ [])))), c)]
    ([] : List (Monomial (HeckeGen n) × ℝ))
    [] ((⟨i⟩ : HeckeGen n) :: descWord id jp)
    (descWord id j₂ ++ bsWord₂ id i jp ++ [])
    ((⟨idd⟩ : HeckeGen n) :: (descWord id jpp ++ (descWord jp j₂ ++
      (descWord i jppp ++ descWord jpp jp))))
    (-c) hcn
    (by simp only [bsWord₁, bsWord₂, List.nil_append, List.append_nil,
      List.append_assoc, List.cons_append])
    (by simp only [bsWord₂, List.nil_append, List.cons_append, ← hDcons,
      ← hicons, hsplitA, hsplitI, List.append_assoc])
    (fun q hq => by
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hq
      subst hq
      intro hcon
      rw [hDcons] at hcon
      simp only [List.cons_append] at hcon
      exact hidd_ne (List.cons.inj hcon).1)
  simp only [List.nil_append, List.cons_append, List.append_nil]
    at s1 s2 s3 s4 ⊢
  exact ((s1.trans s2).step s3).step s4

/-- The diagonal `b = a` is inside `tailChainFromTwo`'s reach: `j₂ = j₁`. -/
theorem tailChainFromTwo_covers_diagonal :
    ∃ (i id idd j₂ j₁ jp jpp jppp : Fin 11),
      id.val + 1 = i.val ∧ idd.val + 1 = id.val ∧ j₁.val + 1 = jp.val ∧
      jp.val + 1 = jpp.val ∧ jpp.val + 1 = jppp.val ∧
      j₂.val = j₁.val ∧ jpp.val ≤ id.val :=
  ⟨9, 8, 7, 5, 5, 6, 7, 8, by decide⟩


/-! ### §4an  The `a ≤ b` chain's opening — most of it was already proved

Two facts about `CornerGeneral`, both established by instantiation rather than
by reading a signature, and both of which shrink the `a ≤ b` arc's open list.

**The overlap and the S-polynomial were never regime-specific.** Neither
`CornerGeneral.oc` nor `oc_spoly_coeff` relates `j₁` to `j₂` — see the note on
that lemma. So the `a ≤ b` corner starts from the *same* `T0`, diagonal
included, and `hecke_prefix_loop_fit.py`'s companion measurement confirms it
against the engine: the start element is exactly `ofTerms [(V0, 1), (U0, −1)]`.

**The first two steps were not either.** `s1` and `s2` ask only `i₁+1 = i`,
`i₂+1 = i₁` and `j₁ ≤ i₂` — Lean's unused-variable linter reports `j₂` unused
when they are instantiated, which is the sharpest possible statement of it. So
they carry the `a ≤ b` chain to `ofTerms [(V2, 1), (U0, −1)]` unchanged, and
that is exactly where the engine's own replay puts it after two steps.

What this namespace adds is the *second* term's head, which the `a > b` regime
does not share: there `s3`/`s4` need `hed : ed+1 = j₂` with `j₁ ≤ ed`, i.e.
`j₁ < j₂`, and cannot be instantiated here at all.

`uHead` is that head — and it is **`loopTwoGen` at `m = 0`**, not new work.
I first proved it by hand before checking; the instantiation is `k = i₁`,
`kd = ed = i₂`, `A = [σᵢ₋₁]`, `S = [σᵢ]`, `Y = [σᵢ]`, and the hypothesis
`descWord i j₁ = Y ++ (σ_k :: descWord kd j₁)` is just the run's first two
letters peeled off. Recorded because the consequence matters for the assembly:
if one level is `loopTwoGen` at `m = 0`, the **whole** U-side loop is
`loopTwoGen` at general `m`, so the opening phase's second lineage is a single
application rather than a chain.

It is the **same two-rule motif** as `s1`/`s2` — a Bokut–Shiao step then a
far-commutation — displaced one letter right, because `U0` carries a leading
`σᵢ₋₁` that `V0` does not:

    U0  = σᵢ₋₁ · σᵢ · (descWord i₁ j₁ ++ [σᵢ₋₁]) · descWord i₂ j₂ · σᵢ
      B →  σᵢ₋₁ · σᵢ · (σᵢ₋₂ σᵢ₋₁ descWord i₂ j₁) · descWord i₂ j₂ · σᵢ
      F →  σᵢ₋₁ · σᵢ₋₂ · σᵢ · σᵢ₋₁ · descWord i₂ j₁ · descWord i₂ j₂ · σᵢ

The Bokut–Shiao redex straddles the two descending runs — it is
`descWord i₁ j₁ ++ [σᵢ₋₁]`, whose last letter is `descWord i₁ j₂`'s first — and
the far-commutation then moves `σᵢ` right past `σᵢ₋₂`, which is legal because
`i₂ + 1 < i`. Both collision hypotheses are discharged by one letter: the
bystander `V2` opens `σᵢ₋₂` and every word here opens `σᵢ₋₁`. That is the
opening phase's head separation, which
`hecke_prefix_head_separation.py` measures to hold for the first `a²−3a+9`
steps and to fail thereafter. -/

namespace CornerLe
open CornerGeneral

variable {n : ℕ}

/-- The second term after its own two-step head. -/
def U0' (i i₁ i₂ j₁ j₂ : Fin n) : Monomial (HeckeGen n) :=
  [(⟨i₁⟩ : HeckeGen n), ⟨i₂⟩] ++
    (descWord i j₁ ++ (descWord i₂ j₂ ++ [(⟨i⟩ : HeckeGen n)]))

/-- The second term after its whole loop, at general depth. -/
def U0L (i i₁ i₂ j₁ j₂ jpp : Fin n) : Monomial (HeckeGen n) :=
  [(⟨i₁⟩ : HeckeGen n)] ++ (descWord i₂ jpp ++
    (descWord i j₁ ++ (descWord jpp j₂ ++ [(⟨i⟩ : HeckeGen n)])))

/-- **The second term's whole loop, at general depth.** `loopTwoGen` at
`m = i₁ − jppp`, which `hecke_opening_coverage.py` measures as the U side's
entire contribution to the opening phase — `2`, `5`, `9` steps at `a = 4, 5, 6`.

`uHead` below is this at `jppp = i₁`, i.e. `m = 0`, i.e. `a = 4`. That the
general case is the same lemma at a larger `m` is why the opening phase's second
lineage is one application rather than a chain of levels. -/
theorem uLoop (hn : 0 < n) (hp : HeckeParams) {i i₁ i₂ j₁ j₂ jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjpp : jpp.val + 1 = jppp.val) (hj₁ : j₁.val ≤ jpp.val)
    (hj₂ : j₂.val ≤ jppp.val) (htop : jppp.val ≤ i₁.val) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U0 i i₁ j₁ j₂, -1)])
      (AlgElement.ofTerms
        [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U0L i i₁ i₂ j₁ j₂ jpp, -1)]) := by
  have hne2 : (⟨i₂⟩ : HeckeGen n) ≠ ⟨i₁⟩ := heckeGen_ne_of_val_ne (by omega)
  have key := CornerBlock.loopTwoGen (i := i) (j₁ := j₁) (j₂ := j₂)
    (e := jppp) (ed := jpp)
    hn hp hjpp hj₁ hj₂ [(⟨i⟩ : HeckeGen n)] (V2 i i₂ j₁ j₂)
    (-1) 1 (by norm_num)
    (i₁.val - jppp.val) i₁ i₂ [(⟨i₁⟩ : HeckeGen n)] [(⟨i⟩ : HeckeGen n)]
    h₂ (by omega)
    (fun z => by
      rw [V2]
      simp only [List.cons_append]
      intro hcon
      exact hne2 (List.cons.inj hcon).1)
    (by
      intro y hy
      simp only [List.mem_singleton] at hy
      subst hy
      show i₂.val + 1 < i.val
      omega)
    (by rw [descWord_cons h₁ (by omega), descWord_cons h₂ (by omega)]; simp)
  simpa [U0L, U0] using key

/-- The first term after its own loop, at general depth. -/
def V2L (i i₁ i₂ j₁ j₂ jpp : Fin n) : Monomial (HeckeGen n) :=
  [(⟨i₂⟩ : HeckeGen n)] ++ (descWord i₁ jpp ++
    (descWord i j₁ ++ (descWord jpp j₂ ++ [])))

/-- **The first term's whole loop, at general depth**, with the second parked at
the word its own loop left it on.

`V2` is already in the loop's entry shape on the nose —
`[σᵢ₋₂] ++ (descWord i j₁ ++ (descWord i j₂ ++ []))` — so this is
`loopTwoGenRight` at `A = [σᵢ₋₂]`, `k = i`, `S = []`, and `m = i − jppp`. That is
one more than `uLoop`'s `m = i₁ − jppp`, which is why
`hecke_opening_coverage.py` measures the two lineages at `L` and `L + 1` steps
for the same bottom `jppp`.

The two loops compose without any change of representation, and that is what
`loopTwoGenRight` bought: `uLoop` runs `loopTwoGen`, which lists the parked term
first, so it ends at `[(V2, 1), (U0L, −1)]` — V parked, U active. Here V is the
active one and U the parked one, so the source must list V first, which is the
same list. The collision hypothesis is one letter: `U0L` opens `σᵢ₋₁`, and every
word this loop touches extends `[σᵢ₋₂]`. -/
theorem vLoop (hn : 0 < n) (hp : HeckeParams) {i i₁ i₂ j₁ j₂ jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjpp : jpp.val + 1 = jppp.val) (hj₁ : j₁.val ≤ jpp.val)
    (hj₂ : j₂.val ≤ jppp.val) (htop : jppp.val ≤ i.val) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U0L i i₁ i₂ j₁ j₂ jpp, -1)])
      (AlgElement.ofTerms
        [(V2L i i₁ i₂ j₁ j₂ jpp, (1 : ℝ)), (U0L i i₁ i₂ j₁ j₂ jpp, -1)]) := by
  have hne1 : (⟨i₁⟩ : HeckeGen n) ≠ ⟨i₂⟩ := heckeGen_ne_of_val_ne (by omega)
  have key := CornerBlock.loopTwoGenRight (i := i) (j₁ := j₁) (j₂ := j₂)
    (e := jppp) (ed := jpp)
    hn hp hjpp hj₁ hj₂ [] (U0L i i₁ i₂ j₁ j₂ jpp)
    1 (-1) one_ne_zero
    (i.val - jppp.val) i i₁ [(⟨i₂⟩ : HeckeGen n)] []
    h₁ (by omega)
    (fun z => by
      rw [U0L]
      simp only [List.cons_append]
      intro hcon
      exact hne1 (List.cons.inj hcon).1)
    (by simp)
    (by rw [descWord_cons h₁ (by omega)]; simp)
  simpa [V2, V2L] using key

/-- **The trio**: one Bokut–Shiao step then `quadPair`, in the shape both
lineages of the opening phase use.

`hecke_opening_trio_shape.py` measures the six steps after `TL` as
`B(jp,jpp,j₁)`, `Y(j₁,jp)`, `Q(j₁)` twice, 6/6 — and the two occurrences differ
only in `A` and `T`, so this is one lemma applied twice rather than a U trio and
a V trio:

| | `A` | `T` |
|---|---|---|
| U | `[σᵢ₋₁] ++ descWord i₂ jpp ++ descWord i jppp` | `[σᵢ]` |
| V | `[σᵢ₋₂] ++ descWord i₁ jpp ++ descWord i jppp` | `[]` |

The Bokut–Shiao redex straddles the two descending runs: `descWord i j₁` splits
at `jppp`, leaving `descWord jpp j₁`, and `descWord jpp j₂` opens with `σ_jpp` —
so `descWord jpp j₁ ++ [σ_jpp]` is `bsWord₁ jpp j₁`, sitting on the join. Its
image `bsWord₂ jp jpp j₁ = [σ_jp, σ_jpp, σ_jp, σ_j₁]` then meets `descWord jp j₂`,
whose first two letters are `σ_jp, σ_j₁` — and `σ_jp σ_j₁ σ_jp` followed by
`σ_j₁` is exactly `quadPair`'s redex. Neither step creates it alone, which is
the same mechanism §4al describes one level down.

**`hj₂ : j₂ ≤ j₁` is the regime.** It is what makes `descWord jp j₂` open with
those two letters, and it is `b ≥ a` — so this lemma does not instantiate in the
`a > b` corner at all. The diagonal `b = a` is included: there `descWord j₁ j₂`
is the single letter `σ_j₁` and `descWord jm j₂` is empty.

One collision hypothesis serves both steps: no bystander extends `A`.
`quadPair` asks about `A ++ [σ_jp, σ_jpp]`, which is an extension of `A`, and
`bsStep` asks about a source that begins with `A`. At both call sites it is
discharged by a single letter — the U trio's `A` opens `σᵢ₋₁` against the parked
`V2L`'s `σᵢ₋₂`, and the V trio's the other way round. -/
theorem trio (hn : 0 < n) (hp : HeckeParams) {j₂ jm j₁ jp jpp : Fin n}
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hj₂ : j₂.val ≤ j₁.val)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (A T : Monomial (HeckeGen n))
    (hpark : ∀ r ∈ (L₁ ++ L₂).map Prod.fst, ∀ z : Monomial (HeckeGen n),
      r ≠ A ++ z) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++
        (A ++ (bsWord₁ jpp j₁ ++ (descWord jp j₂ ++ T)), c) :: L₂))
      (AlgElement.ofTerms (L₁ ++
        (A ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
          ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
            ((⟨j₁⟩ : HeckeGen n) :: (descWord jm j₂ ++ T)))),
          c * (hp.q - hp.q⁻¹))
        :: (A ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
              ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ (descWord jm j₂ ++ T))), c)
        :: L₂)) := by
  -- `descWord jp j₂` opens `σ_jp, σ_j₁` — this is where `j₂ ≤ j₁` is used
  have hsplit : descWord jp j₂ =
      (⟨jp⟩ : HeckeGen n) :: ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂) := by
    rw [descWord_cons_le hjp (by omega), descWord_cons_le hjm hj₂]
  -- state the Bokut-Shiao step's TARGET already in `quadPair`'s source shape,
  -- so the two compose with no rewriting between them
  have hmid : (A ++ [(⟨jp⟩ : HeckeGen n), ⟨jpp⟩]) ++
        ([(⟨jp⟩ : HeckeGen n), ⟨j₁⟩, ⟨jp⟩] ++
          ((⟨j₁⟩ : HeckeGen n) :: (descWord jm j₂ ++ T)))
      = A ++ bsWord₂ jp jpp j₁ ++ (descWord jp j₂ ++ T) := by
    rw [bsWord₂, hsplit,
      descWord_cons_le (i' := j₁) (i := jp) (j := j₁) hjp (by omega),
      descWord_self]
    simp only [List.cons_append, List.append_assoc, List.nil_append]
  have hbs := bsStep (i' := jp) (i := jpp) (j := j₁) hn hp hjpp (by omega)
    L₁ L₂ A (descWord jp j₂ ++ T)
    (A ++ (bsWord₁ jpp j₁ ++ (descWord jp j₂ ++ T)))
    ((A ++ [(⟨jp⟩ : HeckeGen n), ⟨jpp⟩]) ++
      ([(⟨jp⟩ : HeckeGen n), ⟨j₁⟩, ⟨jp⟩] ++
        ((⟨j₁⟩ : HeckeGen n) :: (descWord jm j₂ ++ T))))
    c hc
    (by simp only [List.append_assoc])
    hmid
    (fun q hq => by
      have := hpark q hq (bsWord₁ jpp j₁ ++ (descWord jp j₂ ++ T))
      simpa only [List.append_assoc] using this)
  have hq := quadPair (j₁ := j₁) (jp := jp) hn hp hjp c hc L₁ L₂
    (A ++ [(⟨jp⟩ : HeckeGen n), ⟨jpp⟩]) (descWord jm j₂ ++ T)
    (fun r hr z => by
      have := hpark r hr ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++ z)
      simpa only [List.append_assoc] using this)
  have hchain := ((MultiStepReduction.refl _).step hbs).trans hq
  simpa only [List.append_assoc, List.cons_append, List.singleton_append,
    List.nil_append] using hchain

/-- The chain after both loops, before either trio. -/
noncomputable def TL (i i₁ i₂ j₁ j₂ jpp : Fin n) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(V2L i i₁ i₂ j₁ j₂ jpp, (1 : ℝ)), (U0L i i₁ i₂ j₁ j₂ jpp, -1)]

/-- **The `a ≤ b` chain's opening phase, loops included** — the two setup steps
and both loops, in the one order in which they compose.

`hecke_opening_coverage.py` decomposes the opening's `a² − 3a + 9` steps into
five stretches: the two setup steps, the U loop (`L` steps), a trio, the V loop
(`L + 1` steps), and a second trio. This lemma is the first three of those five —
`2 + L + (L + 1) = 2L + 3` steps — because **both loops must precede both
trios**, and that ordering is a constraint, not a preference.

`L = (a² − 3a)/2`: measured `2, 5, 9` at `a = 4, 5, 6`, so `2L + 9` recovers the
phase length `13, 19, 27`. It is **not** `jpp − j₁`, which this docstring said
until `hecke_opening_trio_shape.py` measured it — that difference is `2` for
every `a`, and agrees only at `a = 4`. The loop's *level* parameter `m = a − 4`
is the thing that is linear in `a`; its step count is not, because each level
descends by a pass whose own length grows.

The probe measures why. `loopTwoGenRight` (like every loop lemma here) is stated
for a *two-term* element, while `quadPair`, which the trios use, takes general
`L₁`/`L₂`. Under the order the confluence engine itself produces, the U trio's
quadratic step **splits U into two terms** before the V loop has run — at step
6, 9 and 13 for `a = 4, 5, 6`, against V-loop completion at 9, 15 and 23 — so a
V loop scheduled after the U trio would face three terms and no loop lemma
applies. Running both loops first keeps the element at two terms throughout, and
the trios then run against the general-list `quadPair`.

That the reordering is *legal* is the same argument §4am makes for the tail: the
two lineages act on different terms, so their steps commute, and
`MultiStepReduction` fixes no order beyond each step's redex being present. Deg-lex
picks one; the Lean is not obliged to. -/
theorem openingLoops (hn : 0 < n) (hp : HeckeParams) {i i₁ i₂ j₁ j₂ jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjpp : jpp.val + 1 = jppp.val) (hj₁ : j₁.val ≤ jpp.val)
    (hj₂ : j₂.val ≤ jppp.val) (htop : jppp.val ≤ i₁.val) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T0 i i₁ j₁ j₂) (TL i i₁ i₂ j₁ j₂ jpp) := by
  have hj₁i₂ : j₁.val ≤ i₂.val := by omega
  have hsetup : MultiStepReduction (heckeOrder n)
      (heckeCompletedRewritingSystem n hn hp) (T0 i i₁ j₁ j₂) (T2 i i₁ i₂ j₁ j₂) :=
    ((MultiStepReduction.refl _).step (s1 hn hp h₁ h₂ hj₁i₂)).step
      (s2 hn hp h₁ h₂ hj₁i₂)
  have hU := uLoop hn hp h₁ h₂ hjpp hj₁ hj₂ htop
  -- `vLoop` asks only `jppp ≤ i`, which `jppp ≤ i₁ < i` gives. The distinction
  -- is not cosmetic: at `a = 3` the FIRST holds and the second does not.
  have hV := vLoop hn hp h₁ h₂ hjpp hj₁ hj₂ (by omega)
  rw [T0, TL] at *
  rw [T2] at hsetup
  exact (hsetup.trans hU).trans hV

/-- The trio's `A`, for a lineage whose leading letter is `x` and whose second
run starts at `y`. `U` takes `(x, y) = (i₁, i₂)`, `V` takes `(i₂, i₁)`. -/
def trioLeft (i x y jpp jppp : Fin n) : Monomial (HeckeGen n) :=
  [(⟨x⟩ : HeckeGen n)] ++ (descWord y jpp ++ descWord i jppp)

/-- **Both lineage words open on the trio's redex.** `descWord i j₁` splits at
`jppp`, and `descWord jpp j₂` opens with `σ_jpp`; the two halves meet as
`bsWord₁ jpp j₁`. This is the one rewriting that turns `U0L` and `V2L` into
`trio`'s source shape, and it is the same for both. -/
theorem lineage_eq_trio_source {n : ℕ} {i x y j₁ j₂ jp jpp jppp : Fin n}
    (hjpp : jp.val + 1 = jpp.val)
    (hjppp : jpp.val + 1 = jppp.val) (hj₁ : j₁.val ≤ jpp.val)
    (hj₂ : j₂.val ≤ jpp.val) (htop : jppp.val ≤ i.val)
    (T : Monomial (HeckeGen n)) :
    [(⟨x⟩ : HeckeGen n)] ++ (descWord y jpp ++
        (descWord i j₁ ++ (descWord jpp j₂ ++ T)))
      = trioLeft i x y jpp jppp ++
          (bsWord₁ jpp j₁ ++ (descWord jp j₂ ++ T)) := by
  rw [trioLeft, bsWord₁,
    descWord_split (k := jppp) (k' := jpp) hjppp hj₁ htop,
    descWord_cons_le (i' := jp) (i := jpp) (j := j₂) hjpp (by omega)]
  simp only [List.cons_append, List.append_assoc, List.nil_append]

/-- The chain after both trios: four terms, two per lineage. -/
noncomputable def TOpen (i i₁ i₂ j₁ j₂ jm jp jpp jppp : Fin n)
    (h : ℝ) : AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
          ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂))), h),
     (trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ descWord jm j₂)), 1),
     (trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
          ((⟨j₁⟩ : HeckeGen n) :: (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)])))),
        -h),
     (trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
          (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))), -1)]

/-- **The `a ≤ b` chain's opening phase, whole** — `a² − 3a + 9` steps, from the
S-polynomial `T0` to the four-term `TOpen`.

Five stretches, in the one order in which the lemmas compose: `s1`, `s2`, the U
loop, the V loop, then `trio` twice. `hecke_opening_trio_shape.py` measures
`2 + L + (L+1) + 6 = 2L + 9` steps and `2L + 9 = a² − 3a + 9`, so this is the
whole phase and nothing is left over.

The two trios run U before V, which is deg-lex's order and also the one the term
list forces: `openingLoops` ends at `[(V2L, 1), (U0L, −1)]`, so U is the second
entry and V the parked one; after U's quadratic step splits it in two, V is the
first entry of three. Each trio's collision hypothesis is one letter — `U`'s
left context opens `σᵢ₋₁` against the parked `V2L`'s `σᵢ₋₂`, and `V`'s the other
way round against both of U's outputs, which share U's prefix. -/
theorem openingPhase_of_loops (hn : 0 < n) (hp : HeckeParams)
    {i i₁ i₂ j₁ j₂ jm jp jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ j₁.val) (htopi : jppp.val ≤ i.val)
    (hloops : MultiStepReduction (heckeOrder n)
      (heckeCompletedRewritingSystem n hn hp)
      (T0 i i₁ j₁ j₂) (TL i i₁ i₂ j₁ j₂ jpp)) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T0 i i₁ j₁ j₂) (TOpen i i₁ i₂ j₁ j₂ jm jp jpp jppp (hp.q - hp.q⁻¹)) := by
  have hj₁ : j₁.val ≤ jpp.val := by omega
  have hne : (⟨i₁⟩ : HeckeGen n) ≠ ⟨i₂⟩ := heckeGen_ne_of_val_ne (by omega)
  -- every index pinned by name: these are bare `have`s with no expected type,
  -- so an implicit the hypotheses do not determine stays a metavariable and
  -- the `by omega` beside it has nothing to prove about
  -- both lineage words, rewritten into `trio`'s source shape
  have hUeq := lineage_eq_trio_source (i := i) (x := i₁) (y := i₂) (j₁ := j₁)
    (j₂ := j₂) (jp := jp) (jpp := jpp) (jppp := jppp)
    hjpp hjppp hj₁ (by omega) (by omega) [(⟨i⟩ : HeckeGen n)]
  have hVeq := lineage_eq_trio_source (i := i) (x := i₂) (y := i₁) (j₁ := j₁)
    (j₂ := j₂) (jp := jp) (jpp := jpp) (jppp := jppp)
    hjpp hjppp hj₁ (by omega) (by omega) ([] : Monomial (HeckeGen n))
  have hU := trio hn hp hjm hjp hjpp hj₂ (-1) (by norm_num)
    [(V2L i i₁ i₂ j₁ j₂ jpp, (1 : ℝ))] [] (trioLeft i i₁ i₂ jpp jppp)
    [(⟨i⟩ : HeckeGen n)]
    (fun r hr z => by
      simp only [List.append_nil, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hr
      subst hr
      rw [V2L, trioLeft]
      simp only [List.cons_append]
      intro hcon
      exact hne (List.cons.inj hcon).1.symm)
  have hV := trio hn hp hjm hjp hjpp hj₂ (1 : ℝ) one_ne_zero []
    [(trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
          ((⟨j₁⟩ : HeckeGen n) :: (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)])))),
        -1 * (hp.q - hp.q⁻¹)),
     (trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
          (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))), -1)]
    (trioLeft i i₂ i₁ jpp jppp) ([] : Monomial (HeckeGen n))
    (fun r hr z => by
      simp only [List.nil_append, List.map_cons, List.map_nil, List.mem_cons,
        List.not_mem_nil, or_false] at hr
      rw [trioLeft] at *
      rcases hr with hr | hr <;> subst hr <;>
        · simp only [List.cons_append]
          intro hcon
          exact hne (List.cons.inj hcon).1
      )
  -- Put every endpoint in `trio`'s source shape. `hUeq`/`hVeq` are the only
  -- rewriting the composition needs; the three chains then meet syntactically.
  rw [TL, V2L, U0L, hUeq, hVeq] at hloops
  rw [V2L, hVeq] at hU
  rw [T0, TOpen]
  simp only [List.nil_append, List.append_nil, List.cons_append,
    one_mul, neg_one_mul] at hloops hU hV ⊢
  exact (hloops.trans hU).trans hV

/-! #### The closing phase's F-run

`hecke_closing_from_topen.py` measures the `4(a−1)` steps after `TOpen` as one
shape, uniform in `a` and `b`: an F-run of `2a−3` steps, two Bokut–Shiao steps,
the **same** F-run again, then the cancellation. Machine-checked — exactly two
adjacent `B` steps, the two runs literally equal.

The engine interleaves two letters through the run, but they are on one term, so
the order is free and the run **sequences into three lemma calls**. The first is
the bare far-commutation `σ_jpp σ_j₁ → σ_j₁ σ_jpp`, which makes `σ_jp` and
`σ_j₁` adjacent; the pair then transports left past `descWord i jppp` — first
`σ_jp`, whose every obstacle is `≥ jppp = jp + 1`… no: `≥ jppp`, and
`jp + 1 = jpp < jppp`, so all far-commute; then `σ_j₁`, for which they are
`≥ jppp = j₁ + 3`. That is `2(a−2)` engine steps replaced by two inductions.

**The `A`-prefix collision hypothesis is unavailable here, and this is the `2a`
hard core.** The two terms of one lineage share their whole left context —
`quadPair` splits a word into two that differ only in an interior `σ_j₁` — so
"no other term extends `A`" is false at exactly the `2a` steps
`hecke_prefix_head_separation.py` counted. Measured again at `TOpen`: `U1`
extends `Uh`'s `A`. What the steps actually need is `monicStep`'s `hne` and the
transports' split-indexed source condition, which this arc's `_sources`
relaxations supply — so the hypotheses below are stated in that form and not
collapsed. -/

/-- **The closing phase's F-run**, as three lemma calls rather than `2a−3`
steps. `S` is whatever trails the block: `σ_j₁ :: R` for the `h`-weighted term
of a lineage and `R` for the plain one, which is the only difference between
them. -/
theorem fRun (hn : 0 < n) (hp : HeckeParams) {i j₁ jp jpp jppp : Fin n}
    (hjp : j₁.val + 1 = jp.val) (hjpp : jp.val + 1 = jpp.val)
    (hjppp : jpp.val + 1 = jppp.val) (htop : jppp.val ≤ i.val)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (A S : Monomial (HeckeGen n))
    (hne : ∀ q ∈ (L₁ ++ L₂).map Prod.fst,
      q ≠ A ++ (descWord i jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩, ⟨jp⟩]
        ++ S)))
    (hcol₁ : ∀ u v : Monomial (HeckeGen n), u ++ v = descWord i jppp → u ≠ [] →
      ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
        r ≠ A ++ (u ++ ((⟨jp⟩ : HeckeGen n) ::
          (v ++ ([(⟨j₁⟩ : HeckeGen n), ⟨jpp⟩, ⟨jp⟩] ++ S)))))
    (hcol₂ : ∀ u v : Monomial (HeckeGen n), u ++ v = descWord i jppp → u ≠ [] →
      ∀ r ∈ (L₁ ++ L₂).map Prod.fst,
        r ≠ (A ++ [(⟨jp⟩ : HeckeGen n)]) ++ (u ++ ((⟨j₁⟩ : HeckeGen n) ::
          (v ++ ([(⟨jpp⟩ : HeckeGen n), ⟨jp⟩] ++ S))))) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++
        (A ++ (descWord i jppp ++
          ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩, ⟨jp⟩] ++ S)), c) :: L₂))
      (AlgElement.ofTerms (L₁ ++
        (A ++ ([(⟨jp⟩ : HeckeGen n), ⟨j₁⟩] ++ (descWord i jp ++ S)), c)
          :: L₂)) := by
  have hjpj₁ : j₁.val + 1 < jpp.val := by omega
  have hgen : (⟨j₁⟩ : HeckeGen n) ≠ ⟨jpp⟩ := heckeGen_ne_of_val_ne (by omega)
  -- stage 1: the bare far-commutation, making σ_jp and σ_j₁ adjacent
  have hswap := monicStep hn hp (farCommRelation jpp j₁)
    (farCommRelation_mem hn hp hjpj₁)
    (BokutShiaoBraid.far_hrel j₁ jpp)
    (farCommRelation_lm jpp j₁ (by omega))
    (by simp [hgen])
    L₁ L₂ (A ++ (descWord i jppp ++ [(⟨jp⟩ : HeckeGen n)]))
    ((⟨jp⟩ : HeckeGen n) :: S)
    -- both words named: a bare `have` pins no implicit, and `_` here left
    -- `monicStep`'s W and W' open (the same failure as `openingPhase`'s).
    -- W' is written in stage 2's SOURCE shape so the two compose directly.
    (A ++ (descWord i jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩, ⟨jp⟩] ++ S)))
    (A ++ (descWord i jppp ++ ((⟨jp⟩ : HeckeGen n) ::
      ([(⟨j₁⟩ : HeckeGen n), ⟨jpp⟩, ⟨jp⟩] ++ S))))
    c hc
    (by simp only [List.append_assoc, List.cons_append, List.nil_append])
    (by simp only [List.append_assoc, List.cons_append, List.nil_append])
    (fun q hq => by
      have := hne q hq
      simpa only [List.append_assoc, List.cons_append, List.singleton_append,
        List.nil_append] using this)
  -- stage 2: σ_jp leftwards past the run; every obstacle is at least jppp
  have hstep2 := farComm_transport_left_sources hn hp jp c hc L₁ L₂
    (descWord i jppp) A ([(⟨j₁⟩ : HeckeGen n), ⟨jpp⟩, ⟨jp⟩] ++ S)
    (fun y hy => by have := descWord_index_ge hy; omega) hcol₁
  -- stage 3: σ_j₁ leftwards past the same run, now behind σ_jp
  have hstep3 := farComm_transport_left_sources hn hp j₁ c hc L₁ L₂
    (descWord i jppp) (A ++ [(⟨jp⟩ : HeckeGen n)])
    ([(⟨jpp⟩ : HeckeGen n), ⟨jp⟩] ++ S)
    (fun y hy => by have := descWord_index_ge hy; omega) hcol₂
  -- `descWord i jppp ++ [σ_jpp, σ_jp]` closes back up into `descWord i jp`
  have hclose : descWord i jppp ++ [(⟨jpp⟩ : HeckeGen n), ⟨jp⟩]
      = descWord i jp := by
    rw [descWord_split (k := jppp) (k' := jpp) (i := i) (j := jp) hjppp
      (by omega) htop,
      descWord_cons_le (i' := jp) (i := jpp) (j := jp) hjpp (by omega),
      descWord_self]
  -- normalise the three endpoints BEFORE composing: `MultiStepReduction.trans`
  -- needs them equal on the nose, and the three lemmas bracket their appends
  -- differently
  simp only [List.append_assoc, List.cons_append,
    List.nil_append] at hswap hstep2 hstep3
  have hchain := (((MultiStepReduction.refl _).step hswap).trans
    hstep2).trans hstep3
  rw [← hclose]
  simpa only [List.append_assoc, List.cons_append, List.singleton_append,
    List.nil_append] using hchain

/-- **The two Bokut–Shiao steps between the closing phase's two F-runs.**

After `fRun` the moved term reads `descWord i₁ j₁ ++ bsWord₁ i j₂`, because its
two halves close up: the left context `[σᵢ₋₁] ++ descWord i₂ jpp ++ [σ_jp, σ_j₁]`
*is* `descWord i₁ j₁`, and `descWord i j₁ ++ descWord jm j₂` is `descWord i j₂`.
Both are `descWord_split`, one at each end.

**The two steps sit at different bottoms, and that is invisible on the
diagonal.** The first is at `j₂`, the second at `j₁`. When `b = a` they coincide
and any check run only there would pass; at `b = a+1` the first redex is
`bsWord₁ i j₂`, three letters longer. Read off the trace at `a = 6, b = 7`, not
derived. -/
theorem closingBs (hn : 0 < n) (hp : HeckeParams) {i i₁ i₂ j₁ j₂ : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hj₂ : j₂.val ≤ j₁.val) (hj₁ : j₁.val ≤ i₂.val)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (hne₀ : ∀ q ∈ (L₁ ++ L₂).map Prod.fst,
      q ≠ descWord i₁ j₁ ++ bsWord₁ i j₂)
    (hne₁ : ∀ q ∈ (L₁ ++ L₂).map Prod.fst,
      q ≠ bsWord₁ i₁ j₁ ++ ((⟨i⟩ : HeckeGen n) :: descWord i₁ j₂)) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++ (descWord i₁ j₁ ++ bsWord₁ i j₂, c) :: L₂))
      (AlgElement.ofTerms (L₁ ++
        (bsWord₂ i₂ i₁ j₁ ++ ((⟨i⟩ : HeckeGen n) :: descWord i₁ j₂), c)
          :: L₂)) := by
  have hb₀ := bsStep (i' := i₁) (i := i) (j := j₂) hn hp h₁ (by omega)
    L₁ L₂ (descWord i₁ j₁) []
    (descWord i₁ j₁ ++ bsWord₁ i j₂)
    -- the target is written in the SECOND step's source shape, so the two
    -- compose with no rewriting between them
    (bsWord₁ i₁ j₁ ++ ((⟨i⟩ : HeckeGen n) :: descWord i₁ j₂))
    c hc
    (by simp only [List.append_nil])
    (by simp only [bsWord₁, bsWord₂, List.append_nil, List.append_assoc,
      List.cons_append, List.nil_append])
    hne₀
  have hb₁ := bsStep (i' := i₂) (i := i₁) (j := j₁) hn hp h₂ hj₁
    L₁ L₂ [] ((⟨i⟩ : HeckeGen n) :: descWord i₁ j₂)
    (bsWord₁ i₁ j₁ ++ ((⟨i⟩ : HeckeGen n) :: descWord i₁ j₂))
    (bsWord₂ i₂ i₁ j₁ ++ ((⟨i⟩ : HeckeGen n) :: descWord i₁ j₂))
    c hc
    (by simp only [List.nil_append])
    (by simp only [List.nil_append])
    hne₁
  exact ((MultiStepReduction.refl _).step hb₀).step hb₁

/-! #### Bridging `TOpen` to `fRun` and `fRun` to `closingBs`

Two list identities, each shared by both lineages. Neither is a step; they are
what lets the closing phase's four lemma calls meet on the nose. -/

/-- **A `TOpen` word is an `fRun` source.** Pure associativity once `trioLeft`
is unfolded — `fRun`'s left context is `trioLeft` without its trailing run. -/
theorem trio_out_eq_fRun_source {n : ℕ} (i x y j₁ jp jpp jppp : Fin n)
    (S : Monomial (HeckeGen n)) :
    trioLeft i x y jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ S))
      = ([(⟨x⟩ : HeckeGen n)] ++ descWord y jpp) ++
          (descWord i jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩, ⟨jp⟩] ++ S)) := by
  rw [trioLeft]
  simp only [List.append_assoc, List.cons_append, List.nil_append]

/-- **An `fRun` target closes up into two descending runs.** Both ends rejoin:
`descWord y jpp ++ [σ_jp, σ_j₁]` is `descWord y j₁`, and
`descWord i jp ++ (σ_j₁ :: descWord jm j₂)` is `descWord i j₂`. Both are
`descWord_split`; `hj₂ : j₂ ≤ j₁` is the regime, entering here as it does in
`trio`. -/
theorem fRun_target_eq {n : ℕ} {i x y j₂ jm j₁ jp jpp : Fin n}
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hj₂ : j₂.val ≤ j₁.val)
    (hy : jpp.val ≤ y.val) (hi : jp.val ≤ i.val)
    (T : Monomial (HeckeGen n)) :
    ([(⟨x⟩ : HeckeGen n)] ++ descWord y jpp) ++
        ([(⟨jp⟩ : HeckeGen n), ⟨j₁⟩] ++
          (descWord i jp ++ ((⟨j₁⟩ : HeckeGen n) :: (descWord jm j₂ ++ T))))
      = [(⟨x⟩ : HeckeGen n)] ++ (descWord y j₁ ++ (descWord i j₂ ++ T)) := by
  have hleft : descWord y j₁ = descWord y jpp ++ [(⟨jp⟩ : HeckeGen n), ⟨j₁⟩] := by
    rw [descWord_split (k := jpp) (k' := jp) (i := y) (j := j₁) hjpp
      (by omega) hy,
      descWord_cons_le (i' := j₁) (i := jp) (j := j₁) hjp (by omega),
      descWord_self]
  have hright : descWord i j₂
      = descWord i jp ++ ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂) := by
    rw [descWord_split (k := jp) (k' := j₁) (i := i) (j := j₂) hjp
      (by omega) hi,
      descWord_cons_le (i' := jm) (i := j₁) (j := j₂) hjm hj₂]
  rw [hleft, hright]
  simp only [List.append_assoc, List.cons_append, List.nil_append]

/-- The word both lineages converge on: `closingBs`'s target, and the V run's. -/
def WStar (i i₁ i₂ j₁ j₂ : Fin n) : Monomial (HeckeGen n) :=
  bsWord₂ i₂ i₁ j₁ ++ ((⟨i⟩ : HeckeGen n) :: descWord i₁ j₂)

/-- **The U lineage's whole closing run**: `fRun` then `closingBs`, carrying the
bystanders throughout, from a `TOpen` word to `WStar`.

**One hypothesis covers all five obligations.** Every word this run touches has
the form `A ++ X` for the *same* left context `A = [σᵢ₋₁] ++ descWord i₂ jpp` and
an `X` of the *same* length — because both rules involved are length-preserving.
Far-commutation swaps two adjacent letters; Bokut–Shiao takes
`descWord i j ++ [σᵢ]` to `σᵢ₋₁ :: σᵢ :: descWord (i−1) j`, and
`|descWord i j| = |descWord (i−1) j| + 1`. So `hsep` — no bystander equals `A`
followed by anything of that length — is exactly what is needed, and it is
*discharged* differently per bystander, which is the point:

* a word opening `σᵢ₋₂` fails at the first letter;
* `U1`, which opens `σᵢ₋₁` and shares the whole context, fails on **length**: it
  is `A ++ X₀` with `|X₀|` one short, so `List.append_cancel_left` reduces the
  question to `|X₀| ≠ |X|`.

No length *formula* appears: the same `descWord`s occur on both sides, so `omega`
closes each obligation with their lengths opaque.

An earlier version of this lemma packaged the hypothesis as "every bystander
opens `σᵢ₋₂`". That is **false at the call site** — the U run acts on `TOpen`'s
third entry, so `U1` is a bystander and opens `σᵢ₋₁` — and the lemma, though
true and sorry-free, could not be applied. Sorry-freeness does not check
instantiability. -/
theorem closingU (hn : 0 < n) (hp : HeckeParams)
    {i i₁ i₂ j₁ j₂ jm jp jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ j₁.val) (htop : jppp.val ≤ i₁.val)
    (c : ℝ) (hc : c ≠ 0) (L₁ L₂ : List (Monomial (HeckeGen n) × ℝ))
    (hsep : ∀ r ∈ (L₁ ++ L₂).map Prod.fst, ∀ X : Monomial (HeckeGen n),
      X.length = (descWord i jppp).length + (descWord jm j₂).length + 6 →
      r ≠ ([(⟨i₁⟩ : HeckeGen n)] ++ descWord i₂ jpp) ++ X) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms (L₁ ++
        (trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
          ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
            ((⟨j₁⟩ : HeckeGen n) :: (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)])))),
          c) :: L₂))
      (AlgElement.ofTerms (L₁ ++ (WStar i i₁ i₂ j₁ j₂, c) :: L₂)) := by
  -- the three `descWord` length relations the obligations need; each is
  -- `congrArg List.length` on a split or a cons, never a closed formula
  have hDsplit : (descWord i j₂).length
      = (descWord i jppp).length + (descWord jpp j₂).length := by
    have := congrArg List.length (descWord_split (k := jppp) (k' := jpp)
      (i := i) (j := j₂) hjppp (by omega) (by omega))
    simpa only [List.length_append] using this
  have hDjpp : (descWord jpp j₂).length = (descWord jm j₂).length + 3 := by
    rw [descWord_cons_le (i' := jp) (i := jpp) (j := j₂) hjpp (by omega),
      descWord_cons_le (i' := j₁) (i := jp) (j := j₂) hjp (by omega),
      descWord_cons_le (i' := jm) (i := j₁) (j := j₂) hjm hj₂]
    simp
  have hDi₁ : (descWord i j₂).length = (descWord i₁ j₂).length + 1 := by
    rw [descWord_cons_le (i' := i₁) (i := i) (j := j₂) h₁ (by omega)]
    simp
  have hAsplit : descWord i₁ j₁
      = ([(⟨i₁⟩ : HeckeGen n)] ++ descWord i₂ jpp) ++ descWord jp j₁ := by
    rw [descWord_cons_le (i' := i₂) (i := i₁) (j := j₁) h₂ (by omega),
      descWord_split (k := jpp) (k' := jp) (i := i₂) (j := j₁) hjpp
        (by omega) (by omega)]
    simp
  have hjpj₁ : descWord jp j₁ = [(⟨jp⟩ : HeckeGen n), ⟨j₁⟩] := by
    rw [descWord_cons_le (i' := j₁) (i := jp) (j := j₁) hjp (by omega),
      descWord_self]
  have hfr := fRun (i := i) (j₁ := j₁) (jp := jp) (jpp := jpp) (jppp := jppp)
    hn hp hjp hjpp hjppp (by omega) c hc L₁ L₂
    ([(⟨i₁⟩ : HeckeGen n)] ++ descWord i₂ jpp)
    ((⟨j₁⟩ : HeckeGen n) :: (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))
    (fun q hq => by
      refine hsep q hq _ ?_
      simp only [List.length_append, List.length_cons, List.length_nil]
      omega)
    (fun u v huv _ r hr => by
      have hl := congrArg List.length huv
      simp only [List.length_append] at hl
      have := hsep r hr (u ++ ((⟨jp⟩ : HeckeGen n) ::
        (v ++ ([(⟨j₁⟩ : HeckeGen n), ⟨jpp⟩, ⟨jp⟩] ++
          ((⟨j₁⟩ : HeckeGen n) :: (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))))))
        (by
          simp only [List.length_append, List.length_cons,
            List.length_nil]
          omega)
      simpa only [List.append_assoc] using this)
    (fun u v huv _ r hr => by
      have hl := congrArg List.length huv
      simp only [List.length_append] at hl
      have := hsep r hr ([(⟨jp⟩ : HeckeGen n)] ++ (u ++ ((⟨j₁⟩ : HeckeGen n) ::
        (v ++ ([(⟨jpp⟩ : HeckeGen n), ⟨jp⟩] ++
          ((⟨j₁⟩ : HeckeGen n) :: (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)])))))))
        (by
          simp only [List.length_append, List.length_cons,
            List.length_nil]
          omega)
      simpa only [List.append_assoc] using this)
  have hbs := closingBs (i := i) (i₁ := i₁) (i₂ := i₂) (j₁ := j₁) (j₂ := j₂)
    hn hp h₁ h₂ hj₂ (by omega) c hc L₁ L₂
    (fun q hq => by
      have := hsep q hq (descWord jp j₁ ++ bsWord₁ i j₂)
        (by
          rw [hjpj₁, bsWord₁]
          simp only [List.length_append, List.length_cons,
            List.length_nil]
          omega)
      rw [hAsplit]
      simpa only [List.append_assoc] using this)
    (fun q hq => by
      have := hsep q hq (descWord jp j₁ ++ ([(⟨i₁⟩ : HeckeGen n)] ++
        ((⟨i⟩ : HeckeGen n) :: descWord i₁ j₂)))
        (by
          rw [hjpj₁]
          simp only [List.length_append, List.length_cons,
            List.length_nil]
          omega)
      rw [bsWord₁, hAsplit]
      simpa only [List.append_assoc] using this)
  rw [trio_out_eq_fRun_source] at *
  rw [fRun_target_eq (x := i₁) (y := i₂) hjm hjp hjpp hj₂ (by omega)
    (by omega) [(⟨i⟩ : HeckeGen n)]] at hfr
  have hUeq : [(⟨i₁⟩ : HeckeGen n)] ++
      (descWord i₂ j₁ ++ (descWord i j₂ ++ [(⟨i⟩ : HeckeGen n)]))
      = descWord i₁ j₁ ++ bsWord₁ i j₂ := by
    rw [bsWord₁, descWord_cons_le (i' := i₂) (i := i₁) (j := j₁) h₂ (by omega)]
    simp only [List.cons_append, List.nil_append]
  rw [hUeq] at hfr
  rw [WStar]
  exact hfr.trans hbs

/-- **`closingU` instantiated at `TOpen`** — the U lineage's run, in place, with
the real three bystanders.

This exists to *check that `closingU`'s hypothesis is reachable*, which the
previous version's was not. The discharge is the measured one: `Vh` and `V1`
open `σᵢ₋₂` and fail at the first letter; `U1` opens `σᵢ₋₁` and shares the whole
left context, so it fails on length — it is `A ++ X₀` with `|X₀|` exactly one
short of what `hsep` quantifies over, and taking `List.length` of both sides is
the whole argument. -/
theorem closingU_at_TOpen (hn : 0 < n) (hp : HeckeParams)
    {i i₁ i₂ j₁ j₂ jm jp jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ j₁.val) (htop : jppp.val ≤ i₁.val) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (TOpen i i₁ i₂ j₁ j₂ jm jp jpp jppp (hp.q - hp.q⁻¹))
      (AlgElement.ofTerms
        [(trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
              ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂))), hp.q - hp.q⁻¹),
         (trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ descWord jm j₂)), 1),
         (WStar i i₁ i₂ j₁ j₂, -(hp.q - hp.q⁻¹)),
         (trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
              (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))), -1)]) := by
  have hne : (⟨i₂⟩ : HeckeGen n) ≠ ⟨i₁⟩ := heckeGen_ne_of_val_ne (by omega)
  have key := closingU (i := i) (i₁ := i₁) (i₂ := i₂) (j₁ := j₁) (j₂ := j₂)
    (jm := jm) (jp := jp) (jpp := jpp) (jppp := jppp)
    hn hp h₁ h₂ hjm hjp hjpp hjppp hj₂ htop
    (-(hp.q - hp.q⁻¹)) (neg_ne_zero.mpr hp.h_ne_zero)
    [(trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
          ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂))), hp.q - hp.q⁻¹),
     (trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ descWord jm j₂)), 1)]
    [(trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
          (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))), -1)]
    (by
      intro r hr X hX hcon
      simp only [List.map_cons, List.map_nil, List.cons_append, List.nil_append,
        List.mem_cons, List.not_mem_nil, or_false] at hr
      rcases hr with hr | hr | hr <;> subst hr
      -- Vh and V1 open σᵢ₋₂; the run's words open σᵢ₋₁
      case _ | _ =>
        · rw [trioLeft] at hcon
          simp only [List.cons_append] at hcon
          exact hne (List.cons.inj hcon).1
      -- U1 shares the context; it is one letter short
      case _ =>
        · have hlen := congrArg List.length hcon
          rw [trioLeft] at hlen
          simp only [List.length_append, List.length_cons, List.length_nil,
            hX] at hlen
          omega)
  exact key

/-- `WStar` split at the V run's left context. Both ends of `descWord i₂ j₁`
are needed: `[σᵢ₋₂] ++ descWord i₁ jpp` is `σᵢ₋₂ :: σᵢ₋₁ :: descWord i₂ jpp`, and
`descWord i₂ j₁` continues past `jpp` by exactly `[σ_jp, σ_j₁]`. -/
theorem WStar_split {n : ℕ} {i i₁ i₂ j₁ j₂ jp jpp : Fin n}
    (h₂ : i₂.val + 1 = i₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppi : jpp.val ≤ i₂.val) :
    WStar i i₁ i₂ j₁ j₂
      = ([(⟨i₂⟩ : HeckeGen n)] ++ descWord i₁ jpp) ++
          ([(⟨jp⟩ : HeckeGen n), ⟨j₁⟩] ++
            ((⟨i⟩ : HeckeGen n) :: descWord i₁ j₂)) := by
  rw [WStar, bsWord₂,
    descWord_split (k := jpp) (k' := jp) (i := i₂) (j := j₁) hjpp
      (by omega) hjppi,
    descWord_cons_le (i' := j₁) (i := jp) (j := j₁) hjp (by omega),
    descWord_self,
    descWord_cons_le (i' := i₂) (i := i₁) (j := jpp) h₂ (by omega)]
  simp

/-- **The V lineage's closing run, in place** — `fRun` alone: the V side does not
run `closingBs`, because its final step *is* the cancellation. It lands on
`WStar`, the word the U side reached two steps earlier.

All three bystanders are separated, and by three different arguments — measured
uniform across `a = 4,5,6` and `b ∈ {a, a+1}`, for each of `fRun`'s three
hypothesis families:

* `U1` opens `σᵢ₋₁` while every word here opens `σᵢ₋₂` — **head**;
* `V1` shares the head and is one letter short — **length**;
* `WStar` shares head *and* length — **peel**. After cancelling the common left
  context, every family word continues `σᵢ` (families 1 and 2) or `σ_jp, σᵢ`
  (family 3), where `WStar` continues `σ_jp, σ_j₁`. So the discriminator is
  `σᵢ ≠ σ_jp` or `σᵢ ≠ σ_j₁`, one letter in from the split.

`WStar` is the reason the packaged `hsep` of `closingU` does not transfer: it is
the one bystander neither head nor length reaches. -/
theorem closingV_at_TOpen (hn : 0 < n) (hp : HeckeParams)
    {i i₁ i₂ j₁ j₂ jm jp jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ j₁.val) (htop : jppp.val ≤ i₁.val) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms
        [(trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
              ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂))), hp.q - hp.q⁻¹),
         (trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ descWord jm j₂)), 1),
         (WStar i i₁ i₂ j₁ j₂, -(hp.q - hp.q⁻¹)),
         (trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
              (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))), -1)])
      (AlgElement.ofTerms
        [(WStar i i₁ i₂ j₁ j₂, hp.q - hp.q⁻¹),
         (trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ descWord jm j₂)), 1),
         (WStar i i₁ i₂ j₁ j₂, -(hp.q - hp.q⁻¹)),
         (trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
              (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))), -1)]) := by
  have hne : (⟨i₁⟩ : HeckeGen n) ≠ ⟨i₂⟩ := heckeGen_ne_of_val_ne (by omega)
  have hnei : (⟨i⟩ : HeckeGen n) ≠ ⟨jp⟩ := heckeGen_ne_of_val_ne (by omega)
  have hnej : (⟨i⟩ : HeckeGen n) ≠ ⟨j₁⟩ := heckeGen_ne_of_val_ne (by omega)
  have hWs := WStar_split (i := i) (i₁ := i₁) (i₂ := i₂) (j₁ := j₁) (j₂ := j₂)
    (jp := jp) (jpp := jpp) h₂ hjp hjpp (by omega)
  have hDi₁ : (descWord i j₂).length = (descWord i₁ j₂).length + 1 := by
    rw [descWord_cons_le (i' := i₁) (i := i) (j := j₂) h₁ (by omega)]
    simp
  have hDsplit : (descWord i j₂).length
      = (descWord i jppp).length + (descWord jpp j₂).length := by
    have := congrArg List.length (descWord_split (k := jppp) (k' := jpp)
      (i := i) (j := j₂) hjppp (by omega) (by omega))
    simpa only [List.length_append] using this
  have hDjpp : (descWord jpp j₂).length = (descWord jm j₂).length + 3 := by
    rw [descWord_cons_le (i' := jp) (i := jpp) (j := j₂) hjpp (by omega),
      descWord_cons_le (i' := j₁) (i := jp) (j := j₂) hjp (by omega),
      descWord_cons_le (i' := jm) (i := j₁) (j := j₂) hjm hj₂]
    simp
  -- one bystander-separation fact, applied at all three families
  have hsep : ∀ r ∈ ([(trioLeft i i₂ i₁ jpp jppp ++
          ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ descWord jm j₂)), (1 : ℝ)),
        (WStar i i₁ i₂ j₁ j₂, -(hp.q - hp.q⁻¹)),
        (trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
          ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
            (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))), -1)] : List _).map Prod.fst,
      ∀ Y : Monomial (HeckeGen n),
        Y.length = (descWord i jppp).length + (descWord jm j₂).length + 5 →
        (∃ Z : Monomial (HeckeGen n), Y = (⟨i⟩ : HeckeGen n) :: Z) ∨
          (∃ Z : Monomial (HeckeGen n), Y = (⟨jp⟩ : HeckeGen n) ::
            ((⟨i⟩ : HeckeGen n) :: Z)) →
        r ≠ ([(⟨i₂⟩ : HeckeGen n)] ++ descWord i₁ jpp) ++ Y := by
    intro r hr Y hY hshape hcon
    simp only [List.map_cons, List.map_nil, List.mem_cons, List.not_mem_nil,
      or_false] at hr
    rcases hr with hr | hr | hr <;> subst hr
    · -- V1: shares the head, one letter short
      have hlen := congrArg List.length hcon
      rw [trioLeft] at hlen
      simp only [List.length_append, List.length_cons, List.length_nil,
        hY] at hlen
      omega
    · -- WStar: shares head AND length; peel the context, compare one letter in
      rw [hWs] at hcon
      have hZ := List.append_cancel_left hcon
      rcases hshape with ⟨Z, hZ'⟩ | ⟨Z, hZ'⟩ <;> rw [hZ'] at hZ
      · exact hnei (List.cons.inj hZ).1.symm
      · exact hnej (List.cons.inj (List.cons.inj hZ).2).1.symm
    · -- U1: opens σᵢ₋₁ where every word here opens σᵢ₋₂
      rw [trioLeft] at hcon
      simp only [List.cons_append] at hcon
      exact hne (List.cons.inj hcon).1
  have key := fRun (i := i) (j₁ := j₁) (jp := jp) (jpp := jpp) (jppp := jppp)
    hn hp hjp hjpp hjppp (by omega) (hp.q - hp.q⁻¹) hp.h_ne_zero
    ([] : List (Monomial (HeckeGen n) × ℝ))
    [(trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ descWord jm j₂)), (1 : ℝ)),
     (WStar i i₁ i₂ j₁ j₂, -(hp.q - hp.q⁻¹)),
     (trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
          (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))), -1)]
    ([(⟨i₂⟩ : HeckeGen n)] ++ descWord i₁ jpp)
    ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂)
    (fun q hq => by
      have := hsep q (by simpa using hq)
        (descWord i jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩, ⟨jp⟩] ++
          ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂)))
        (by
          simp only [List.length_append, List.length_cons, List.length_nil]
          omega)
        (Or.inl ⟨descWord i₁ jppp ++
            ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩, ⟨j₁⟩, ⟨jp⟩] ++
              ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂)), by
          rw [descWord_cons_le (i' := i₁) (i := i) (j := jppp) h₁ (by omega)]
          simp⟩)
      simpa only [List.append_assoc] using this)
    (fun u v huv hu r hr => by
      have hl := congrArg List.length huv
      simp only [List.length_append] at hl
      obtain ⟨y, u', hu'⟩ : ∃ (y : HeckeGen n) (u' : Monomial (HeckeGen n)),
          u = y :: u' := by
        cases u with
        | nil => exact absurd rfl hu
        | cons y u' => exact ⟨y, u', rfl⟩
      have hy : y = (⟨i⟩ : HeckeGen n) := by
        have := huv
        rw [hu', descWord_cons_le (i' := i₁) (i := i) (j := jppp) h₁
          (by omega)] at this
        exact (List.cons.inj this).1
      have := hsep r (by simpa using hr)
        (u ++ ((⟨jp⟩ : HeckeGen n) :: (v ++
          ([(⟨j₁⟩ : HeckeGen n), ⟨jpp⟩, ⟨jp⟩] ++
            ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂)))))
        (by
          simp only [List.length_append, List.length_cons, List.length_nil]
          omega)
        (Or.inl ⟨u' ++ ((⟨jp⟩ : HeckeGen n) :: (v ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jpp⟩, ⟨jp⟩] ++
              ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂)))), by
          rw [hu', hy]; simp⟩)
      simpa only [List.append_assoc] using this)
    (fun u v huv hu r hr => by
      have hl := congrArg List.length huv
      simp only [List.length_append] at hl
      obtain ⟨y, u', hu'⟩ : ∃ (y : HeckeGen n) (u' : Monomial (HeckeGen n)),
          u = y :: u' := by
        cases u with
        | nil => exact absurd rfl hu
        | cons y u' => exact ⟨y, u', rfl⟩
      have hy : y = (⟨i⟩ : HeckeGen n) := by
        have := huv
        rw [hu', descWord_cons_le (i' := i₁) (i := i) (j := jppp) h₁
          (by omega)] at this
        exact (List.cons.inj this).1
      have := hsep r (by simpa using hr)
        ([(⟨jp⟩ : HeckeGen n)] ++ (u ++ ((⟨j₁⟩ : HeckeGen n) ::
          (v ++ ([(⟨jpp⟩ : HeckeGen n), ⟨jp⟩] ++
            ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂))))))
        (by
          simp only [List.length_append, List.length_cons, List.length_nil]
          omega)
        (Or.inr ⟨u' ++ ((⟨j₁⟩ : HeckeGen n) :: (v ++
            ([(⟨jpp⟩ : HeckeGen n), ⟨jp⟩] ++
              ((⟨j₁⟩ : HeckeGen n) :: descWord jm j₂)))), by
          rw [hu', hy]; simp⟩)
      simpa only [List.append_assoc] using this)
  -- `T = []` leaves `descWord jm j₂ ++ []` in the equation but not in `key`,
  -- so the rewrite has to be normalised before it will match
  have hteq := fRun_target_eq (i := i) (x := i₂) (y := i₁) (j₂ := j₂) (jm := jm)
    (j₁ := j₁) (jp := jp) (jpp := jpp) hjm hjp hjpp hj₂ (by omega)
    (by omega) ([] : Monomial (HeckeGen n))
  simp only [List.append_nil] at hteq
  rw [hteq] at key
  have hVeq : [(⟨i₂⟩ : HeckeGen n)] ++
      (descWord i₁ j₁ ++ descWord i j₂) = WStar i i₁ i₂ j₁ j₂ := by
    rw [WStar, bsWord₂,
      descWord_cons_le (i' := i₂) (i := i₁) (j := j₁) h₂ (by omega),
      descWord_cons_le (i' := i₁) (i := i) (j := j₂) h₁ (by omega)]
    simp
  rw [hVeq] at key
  -- normalise BOTH sides the same way; `rw ... at *` hit the hypotheses too and
  -- left the two associations different
  simp only [trio_out_eq_fRun_source, List.nil_append,
    List.append_assoc] at key ⊢
  exact key

/-- **`a ≥ 4`**: the loop stretch is `openingLoops`. -/
theorem openingPhase (hn : 0 < n) (hp : HeckeParams)
    {i i₁ i₂ j₁ j₂ jm jp jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ j₁.val) (htop : jppp.val ≤ i₁.val) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T0 i i₁ j₁ j₂) (TOpen i i₁ i₂ j₁ j₂ jm jp jpp jppp (hp.q - hp.q⁻¹)) :=
  openingPhase_of_loops hn hp h₁ h₂ hjm hjp hjpp hjppp hj₂ (by omega)
    (openingLoops (i := i) (i₁ := i₁) (i₂ := i₂) (j₁ := j₁) (j₂ := j₂)
      (jpp := jpp) (jppp := jppp) hn hp h₁ h₂ hjppp (by omega) (by omega) htop)

/-! #### `a = 3`: the same construction, with the U loop as the identity

`hecke_closing_from_topen.py`'s small-`a` sweep measures `a = 3` at
`s1, s2` = 2 steps, U loop = **0**, V loop = **1**, two trios = 6 — the same
`a² − 3a + 9 = 9` the general case gives, and the same five stretches.

The U loop is zero-length for a structural reason, not by accident: at `a = 3`,
`jpp = i₁`, so `descWord i₂ jpp` is empty and **`U0L` and `U0` are the same
word**. `uLoop` is not *absent* here, it is the identity — which is exactly what
its parameter `m = i₁ − jppp = −1` cannot express.

`vLoop` runs one pass, and needs only `jppp ≤ i`, which at `a = 3` holds with
equality. That weakening (three commits back) is what makes this case reachable
at all. -/

/-- `a = 3` collapses the U loop: `jpp = i₁` empties `descWord i₂ jpp`. -/
theorem U0L_eq_U0 {n : ℕ} {i i₁ i₂ j₁ j₂ jpp : Fin n}
    (h₂ : i₂.val + 1 = i₁.val) (hjppi : jpp = i₁) :
    U0L i i₁ i₂ j₁ j₂ jpp = U0 i i₁ j₁ j₂ := by
  subst hjppi
  rw [U0L, U0, descWord_of_lt (by omega)]
  simp

/-- **`a = 3`'s loop stretch**: `s1`, `s2`, then the V loop alone. -/
theorem openingLoops₃ (hn : 0 < n) (hp : HeckeParams)
    {i i₁ i₂ j₁ j₂ jp jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjp : j₁.val + 1 = jp.val) (hjpplow : jp.val + 1 = jpp.val)
    (hjpp : jpp.val + 1 = jppp.val) (hj₁ : j₁.val ≤ jpp.val)
    (hj₂ : j₂.val ≤ jppp.val) (hjppi : jpp = i₁) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T0 i i₁ j₁ j₂) (TL i i₁ i₂ j₁ j₂ jpp) := by
  have hjppv : jpp.val = i₁.val := congrArg Fin.val hjppi
  have hj₁i₂ : j₁.val ≤ i₂.val := by omega
  have hsetup : MultiStepReduction (heckeOrder n)
      (heckeCompletedRewritingSystem n hn hp) (T0 i i₁ j₁ j₂)
      (T2 i i₁ i₂ j₁ j₂) :=
    ((MultiStepReduction.refl _).step (s1 hn hp h₁ h₂ hj₁i₂)).step
      (s2 hn hp h₁ h₂ hj₁i₂)
  have hV := vLoop (i := i) (i₁ := i₁) (i₂ := i₂) (j₁ := j₁) (j₂ := j₂)
    (jpp := jpp) (jppp := jppp) hn hp h₁ h₂ hjpp hj₁ hj₂ (by omega)
  have hUU := U0L_eq_U0 (i := i) (i₁ := i₁) (i₂ := i₂) (j₁ := j₁) (j₂ := j₂)
    (jpp := jpp) h₂ hjppi
  -- rewrite `U0L → U0` in `hV` and in the GOAL. Doing it in `hsetup` instead
  -- hits its SOURCE too, which is `T0` and must stay `U0`.
  rw [T0, TL, hUU]
  rw [T2] at hsetup
  rw [hUU] at hV
  exact hsetup.trans hV

/-- **`a = 3`**: the loop stretch is `openingLoops₃`. Same `TOpen`, same trios. -/
theorem openingPhase₃ (hn : 0 < n) (hp : HeckeParams)
    {i i₁ i₂ j₁ j₂ jm jp jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ j₁.val) (hjppi : jpp = i₁) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T0 i i₁ j₁ j₂) (TOpen i i₁ i₂ j₁ j₂ jm jp jpp jppp (hp.q - hp.q⁻¹)) :=
  have hjppv : jpp.val = i₁.val := congrArg Fin.val hjppi
  openingPhase_of_loops hn hp h₁ h₂ hjm hjp hjpp hjppp hj₂ (by omega)
    (openingLoops₃ (i := i) (i₁ := i₁) (i₂ := i₂) (j₁ := j₁) (j₂ := j₂)
      (jp := jp) (jpp := jpp) (jppp := jppp) hn hp h₁ h₂ hjp hjpp hjppp
      (by omega) (by omega) hjppi)

/-- The chain at the prefix's first cancellation: four terms, two of them the
same word with opposite coefficients. -/
noncomputable def TCancel (i i₁ i₂ j₁ j₂ jm jp jpp jppp : Fin n) (h : ℝ) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms
    [(WStar i i₁ i₂ j₁ j₂, h),
     (trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ descWord jm j₂)), 1),
     (WStar i i₁ i₂ j₁ j₂, -h),
     (trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
          (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))), -1)]

/-- **The `a ≤ b` chain's closing phase** — `4(a−1)` steps, `TOpen` to `TCancel`.

The U lineage's `fRun` and two Bokut–Shiao steps, then the V lineage's `fRun`,
whose last step lands on the word the U side already reached. The two halves
compose on the nose: `closingV_at_TOpen`'s source *is* `closingU_at_TOpen`'s
target, because both were stated against the same four-term list. -/
theorem closingPhase (hn : 0 < n) (hp : HeckeParams)
    {i i₁ i₂ j₁ j₂ jm jp jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ j₁.val) (htop : jppp.val ≤ i₁.val) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (TOpen i i₁ i₂ j₁ j₂ jm jp jpp jppp (hp.q - hp.q⁻¹))
      (TCancel i i₁ i₂ j₁ j₂ jm jp jpp jppp (hp.q - hp.q⁻¹)) := by
  rw [TCancel]
  exact (closingU_at_TOpen hn hp h₁ h₂ hjm hjp hjpp hjppp hj₂ htop).trans
    (closingV_at_TOpen hn hp h₁ h₂ hjm hjp hjpp hjppp hj₂ htop)

/-- **The cancellation.** `TCancel`'s two `WStar` entries carry `h` and `−h`, so
they contribute nothing; what survives is the two plain words. They are not
adjacent — `trio` emits each lineage's `h`-weighted word immediately before its
plain one — which is why this is `ofTerms_cancel_split` and not
`ofTerms_cancel_pair`. -/
theorem TCancel_coeffEq {n : ℕ} (i i₁ i₂ j₁ j₂ jm jp jpp jppp : Fin n) (h : ℝ) :
    AlgElement.CoeffEq (TCancel i i₁ i₂ j₁ j₂ jm jp jpp jppp h)
      (AlgElement.ofTerms
        [(trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ descWord jm j₂)), (1 : ℝ)),
         (trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
            ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
              (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))), -1)]) := by
  have := ofTerms_cancel_split (WStar i i₁ i₂ j₁ j₂) h
    ([] : List (Monomial (HeckeGen n) × ℝ))
    [(trioLeft i i₂ i₁ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++ descWord jm j₂)), (1 : ℝ))]
    [(trioLeft i i₁ i₂ jpp jppp ++ ([(⟨jp⟩ : HeckeGen n), ⟨jpp⟩] ++
        ([(⟨j₁⟩ : HeckeGen n), ⟨jp⟩] ++
          (descWord jm j₂ ++ [(⟨i⟩ : HeckeGen n)]))), -1)]
  rw [TCancel]
  simpa only [List.nil_append, List.cons_append, List.singleton_append] using this

/-- **The whole `a ≤ b` prefix** — all `a² + a + 5` steps, from the
S-polynomial to the first cancellation.

`openingPhase` is `a² − 3a + 9` of them and `closingPhase` the remaining
`4(a − 1)`; `hecke_closing_from_topen.py` measures the two against the prefix
length and they close exactly, 6/6 at `a = 4, 5, 6` and `b ∈ {a, a+1}` — the
diagonal `b = a` included.

`a = 3` is **not** covered: its loop parameter would be `m = −1`, so there is no
loop pass at all and the opening phase's shape does not arise. It needs its own
treatment. -/
theorem prefixChain (hn : 0 < n) (hp : HeckeParams)
    {i i₁ i₂ j₁ j₂ jm jp jpp jppp : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hjm : jm.val + 1 = j₁.val) (hjp : j₁.val + 1 = jp.val)
    (hjpp : jp.val + 1 = jpp.val) (hjppp : jpp.val + 1 = jppp.val)
    (hj₂ : j₂.val ≤ j₁.val) (htop : jppp.val ≤ i₁.val) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (T0 i i₁ j₁ j₂)
      (TCancel i i₁ i₂ j₁ j₂ jm jp jpp jppp (hp.q - hp.q⁻¹)) :=
  (openingPhase hn hp h₁ h₂ hjm hjp hjpp hjppp hj₂ htop).trans
    (closingPhase hn hp h₁ h₂ hjm hjp hjpp hjppp hj₂ htop)

theorem uHead (hn : 0 < n) (hp : HeckeParams) {i i₁ i₂ j₁ j₂ : Fin n}
    (h₁ : i₁.val + 1 = i.val) (h₂ : i₂.val + 1 = i₁.val)
    (hj₁ : j₁.val ≤ i₂.val) (hj₂ : j₂.val ≤ i₂.val) :
    MultiStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)
      (AlgElement.ofTerms [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U0 i i₁ j₁ j₂, -1)])
      (AlgElement.ofTerms [(V2 i i₂ j₁ j₂, (1 : ℝ)), (U0' i i₁ i₂ j₁ j₂, -1)]) := by
  have h := uLoop (i := i) (i₁ := i₁) (i₂ := i₂) (j₁ := j₁) (j₂ := j₂)
    (jpp := i₂) (jppp := i₁) hn hp h₁ h₂ h₂ (by omega) (by omega) (le_refl _)
  simpa [U0L, U0', descWord_self] using h

end CornerLe

end UGB.GrobnerShirshov.Hecke
