import UGB.GrobnerShirshov.NormalForms

/-!
# `UGB.GrobnerShirshov.QSerreCriticalPairs` — discharging the q-Serre GS obligation

`qSerre_is_gs_basis` was an axiom. Bean qou-18s7 verified it by an exact symbolic
critical-pair computation
(`computations/qserre_gs_basis_check.py`) but left it *verified, not formalised*.
This file formalises what can be formalised from the shape of the system alone,
and isolates exactly what is left. **Update 2026-11-21:** `QSerreGS.lean` closes
what is left and proves `qSerre_is_gs_basis` as a theorem, through the
composition lemma (`Diamond.isGrobnerShirshovBasis_iff_compositionsTrivial`)
rather than through the `MultiStepReduction` route sketched in §5 below.

## The structural observation everything here rests on

Every one of the seven q-Serre leading monomials is a **two-letter word**
(`qSerre_lm_length`), and the seven are **pairwise distinct**, so a rule of the
system is determined by its leading monomial (`qSerre_rule_eq_of_lm_eq`).

Those two facts collapse most of the obligation:

* **Inclusion compositions are entirely degenerate.** `outer.lm = left ++
  inner.lm ++ right` with both leading monomials of length 2 forces
  `left = right = []`, hence `outer.lm = inner.lm`, hence `outer = inner` — and
  then the S-polynomial is a difference of an element with itself.
  `qSerre_inclusion_resolves` discharges `inclusion_resolves` **outright**.

* **Overlap compositions split by overlap length.** `overlap ≠ []` together with
  the length-2 leading monomials leaves only `|overlap| ∈ {1, 2}`
  (`qSerre_overlap_shape`). The `|overlap| = 2` case is again degenerate —
  `left = right = []`, so `rule₁ = rule₂` and the S-polynomial vanishes
  (`qSerre_overlap_resolves_of_length_two`).

## What is left

Only the `|overlap| = 1` case: `lm₁ = [a,b]`, `lm₂ = [b,c]`, and the
S-polynomial reduces to `a·tail₂ − tail₁·c` (the ambient word `[a,b,c]` cancels
because the rules are monic — `qSerre_rules_monic`). Bean qou-18s7 found exactly
**8** such ambiguities among the seven rules and checked that all 8 resolve; each
needs an explicit two-step reduction chain, which is what remains to formalise.

So the axiom's remaining content is 8 concrete reduction chains, not an open
mathematical question — a materially smaller and better-understood gap than
"is this a Gröbner–Shirshov basis".
-/

namespace UGB.GrobnerShirshov

open SU2Gen

universe v

variable {k : Type v} [Field k]

/-! ## §1  The two structural facts -/

/-- **Every q-Serre leading monomial is a two-letter word.** -/
theorem qSerre_lm_length (qs : QSerreRelations k) :
    ∀ r ∈ (qSerreRewritingSystem k qs).rules, (r.lm degLexOrder).length = 2 := by
  intro r hr
  simp only [qSerreRewritingSystem, qSerreRules, List.mem_cons, List.not_mem_nil,
    or_false] at hr
  rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> simp

/-- **A rule of the system is determined by its leading monomial** — the seven
are pairwise distinct. -/
theorem qSerre_rule_eq_of_lm_eq (qs : QSerreRelations k)
    {r s : ReductionRule SU2Gen k}
    (hr : r ∈ (qSerreRewritingSystem k qs).rules)
    (hs : s ∈ (qSerreRewritingSystem k qs).rules)
    (h : r.lm degLexOrder = s.lm degLexOrder) : r = s := by
  simp only [qSerreRewritingSystem, qSerreRules, List.mem_cons, List.not_mem_nil,
    or_false] at hr hs
  rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
    rcases hs with rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
      first
        | rfl
        | (exfalso; simp at h)

/-! ## §2  Inclusion compositions are degenerate -/

/-- **`inclusion_resolves`, discharged.**

    Both leading monomials have length 2, and `outer.lm = left ++ inner.lm ++
    right`, so `left` and `right` are empty on length grounds alone. Then
    `outer.lm = inner.lm`, so `outer = inner` by §1, and the S-polynomial is a
    difference of an element with itself. -/
theorem qSerre_inclusion_resolves (qs : QSerreRelations k)
    (ic : InclusionComposition SU2Gen k degLexOrder)
    (h₁ : ic.inner ∈ (qSerreRewritingSystem k qs).rules)
    (h₂ : ic.outer ∈ (qSerreRewritingSystem k qs).rules) :
    ∃ nf, ReducesToNF degLexOrder (qSerreRewritingSystem k qs) ic.spoly nf ∧
      nf.isZero := by
  have hi := qSerre_lm_length qs _ h₁
  have ho := qSerre_lm_length qs _ h₂
  have hd := ic.decomposition
  have hl := congrArg List.length hd
  simp only [List.length_append, hi, ho] at hl
  have hleft : ic.left = [] := List.eq_nil_of_length_eq_zero (by omega)
  have hright : ic.right = [] := List.eq_nil_of_length_eq_zero (by omega)
  have hlm : ic.outer.lm degLexOrder = ic.inner.lm degLexOrder := by
    rw [hd, hleft, hright]; simp
  have hsame : ic.outer = ic.inner := qSerre_rule_eq_of_lm_eq qs h₂ h₁ hlm
  have hzero : ic.spoly.isZero := by
    intro m
    simp only [InclusionComposition.spoly, hleft, hright, hsame,
      AlgElement.sub_coeff, AlgElement.smul_coeff,
      AlgElement.contextMul_nil_nil_coeff]
    exact sub_self _
  exact ⟨ic.spoly, ⟨MultiStepReduction.refl _,
    fun r' _ m hm => absurd (hzero m) hm⟩, hzero⟩

/-! ## §3  Overlap compositions: the shape -/

/-- **Only two shapes are possible.** `overlap ≠ []` plus length-2 leading
    monomials leaves `|overlap| = 1` (the genuine critical pairs, with `left` and
    `right` single letters) or `|overlap| = 2` (degenerate: the two rules lead on
    the same word). -/
theorem qSerre_overlap_shape (qs : QSerreRelations k)
    (oc : OverlapComposition SU2Gen k degLexOrder)
    (h₁ : oc.rule₁ ∈ (qSerreRewritingSystem k qs).rules)
    (h₂ : oc.rule₂ ∈ (qSerreRewritingSystem k qs).rules) :
    (oc.overlap.length = 1 ∧ oc.left.length = 1 ∧ oc.right.length = 1) ∨
    (oc.overlap.length = 2 ∧ oc.left = [] ∧ oc.right = []) := by
  have h1 := qSerre_lm_length qs _ h₁
  have h2 := qSerre_lm_length qs _ h₂
  have e1 := congrArg List.length oc.lm₁_decomp
  have e2 := congrArg List.length oc.lm₂_decomp
  simp only [List.length_append, h1] at e1
  simp only [List.length_append, h2] at e2
  have hne : oc.overlap.length ≠ 0 := by
    simpa [List.length_eq_zero_iff] using oc.overlap_nonempty
  rcases Nat.lt_or_ge oc.overlap.length 2 with hlt | hge
  · left
    refine ⟨by omega, by omega, by omega⟩
  · right
    have hov : oc.overlap.length = 2 := by omega
    exact ⟨hov, List.eq_nil_of_length_eq_zero (by omega),
      List.eq_nil_of_length_eq_zero (by omega)⟩

/-- **The degenerate overlap case resolves.** When the overlap is the whole of
    both leading monomials the two rules coincide, and the S-polynomial is a
    difference of an element with itself. -/
theorem qSerre_overlap_resolves_of_length_two (qs : QSerreRelations k)
    (oc : OverlapComposition SU2Gen k degLexOrder)
    (h₁ : oc.rule₁ ∈ (qSerreRewritingSystem k qs).rules)
    (h₂ : oc.rule₂ ∈ (qSerreRewritingSystem k qs).rules)
    (hleft : oc.left = []) (hright : oc.right = []) :
    ∃ nf, ReducesToNF degLexOrder (qSerreRewritingSystem k qs) oc.spoly nf ∧
      nf.isZero := by
  have hlm : oc.rule₁.lm degLexOrder = oc.rule₂.lm degLexOrder := by
    rw [oc.lm₁_decomp, oc.lm₂_decomp, hleft, hright]; simp
  have hsame : oc.rule₁ = oc.rule₂ := qSerre_rule_eq_of_lm_eq qs h₁ h₂ hlm
  have hzero := oc.spoly_isZero_of_self hsame hleft hright
  exact ⟨oc.spoly, ⟨MultiStepReduction.refl _,
    fun r' _ m hm => absurd (hzero m) hm⟩, hzero⟩

/-! ## §4  The axiom, reduced to exactly the genuine critical pairs -/

/-- **`qSerre_is_gs_basis` follows from the length-1 critical pairs alone.**

    This is the point of the file. `IsGrobnerShirshovBasis` quantifies over
    *every* overlap and inclusion composition, which is an unbounded-looking
    obligation; §§2–3 show that all of it is degenerate except the overlaps whose
    overlap is a single letter. So the axiom's entire content is the hypothesis
    `hcp` below — and bean qou-18s7's computation says there are exactly **8**
    such ambiguities and all 8 resolve.

    Discharging `hcp` therefore discharges `qSerre_is_gs_basis` outright, and
    `hcp` is 8 explicit two-step reduction chains rather than an open question
    about the algebra. -/
theorem qSerre_is_gs_basis_of_critical_pairs (qs : QSerreRelations k)
    (hcp : ∀ oc : OverlapComposition SU2Gen k degLexOrder,
      oc.rule₁ ∈ (qSerreRewritingSystem k qs).rules →
      oc.rule₂ ∈ (qSerreRewritingSystem k qs).rules →
      oc.overlap.length = 1 →
      ∃ nf, ReducesToNF degLexOrder (qSerreRewritingSystem k qs) oc.spoly nf ∧
        nf.isZero) :
    IsGrobnerShirshovBasis SU2Gen k degLexOrder (qSerreRewritingSystem k qs) := by
  constructor
  · intro oc h₁ h₂
    rcases qSerre_overlap_shape qs oc h₁ h₂ with ⟨hov, -, -⟩ | ⟨-, hleft, hright⟩
    · exact hcp oc h₁ h₂ hov
    · exact qSerre_overlap_resolves_of_length_two qs oc h₁ h₂ hleft hright
  · intro ic h₁ h₂
    exact qSerre_inclusion_resolves qs ic h₁ h₂

/-! ## §5  The eight critical pairs, enumerated in Lean -/

set_option maxHeartbeats 4000000 in
/-- **Exactly eight ordered rule pairs admit a length-1 overlap, and here they
are.**

Of the 49 ordered pairs, 41 admit none: a length-1 overlap forces
`lm₁ = [a,b]` and `lm₂ = [b,c]` sharing the letter `b`, and for those 41 the
second letter of `lm₁` differs from the first of `lm₂`, so the decomposition
equations are contradictory.

This reproduces, inside Lean, the enumeration
`computations/qserre_gs_basis_check.py` arrived at symbolically — the two agree
that there are 8, and on which 8. Bean qou-18s7 verified that all 8 resolve;
the reduction chains witnessing that are what remains (§6). -/
theorem qSerre_overlap_enumeration (qs : QSerreRelations k)
    (oc : OverlapComposition SU2Gen k degLexOrder)
    (h₁ : oc.rule₁ ∈ (qSerreRewritingSystem k qs).rules)
    (h₂ : oc.rule₂ ∈ (qSerreRewritingSystem k qs).rules)
    (hov : oc.overlap.length = 1) :
    (oc.rule₁ = qSerreRule1 ∧ oc.rule₂ = qSerreRule2 ∧
       oc.left = [K] ∧ oc.overlap = [K_inv] ∧ oc.right = [K]) ∨
    (oc.rule₁ = qSerreRule1 ∧ oc.rule₂ = qSerreRule6 qs ∧
       oc.left = [K] ∧ oc.overlap = [K_inv] ∧ oc.right = [E_plus]) ∨
    (oc.rule₁ = qSerreRule1 ∧ oc.rule₂ = qSerreRule7 qs ∧
       oc.left = [K] ∧ oc.overlap = [K_inv] ∧ oc.right = [E_minus]) ∨
    (oc.rule₁ = qSerreRule2 ∧ oc.rule₂ = qSerreRule1 ∧
       oc.left = [K_inv] ∧ oc.overlap = [K] ∧ oc.right = [K_inv]) ∨
    (oc.rule₁ = qSerreRule2 ∧ oc.rule₂ = qSerreRule3 qs ∧
       oc.left = [K_inv] ∧ oc.overlap = [K] ∧ oc.right = [E_plus]) ∨
    (oc.rule₁ = qSerreRule2 ∧ oc.rule₂ = qSerreRule4 qs ∧
       oc.left = [K_inv] ∧ oc.overlap = [K] ∧ oc.right = [E_minus]) ∨
    (oc.rule₁ = qSerreRule3 qs ∧ oc.rule₂ = qSerreRule5 qs ∧
       oc.left = [K] ∧ oc.overlap = [E_plus] ∧ oc.right = [E_minus]) ∨
    (oc.rule₁ = qSerreRule6 qs ∧ oc.rule₂ = qSerreRule5 qs ∧
       oc.left = [K_inv] ∧ oc.overlap = [E_plus] ∧ oc.right = [E_minus]) := by
  obtain ⟨hov1, hl1, hr1⟩ | ⟨hov2, -, -⟩ := qSerre_overlap_shape qs oc h₁ h₂
  · obtain ⟨a, ha⟩ := List.length_eq_one_iff.mp hl1
    obtain ⟨b, hb⟩ := List.length_eq_one_iff.mp hov1
    obtain ⟨c, hc⟩ := List.length_eq_one_iff.mp hr1
    have e1 : oc.rule₁.lm degLexOrder = [a, b] := by
      rw [oc.lm₁_decomp, ha, hb]; rfl
    have e2 : oc.rule₂.lm degLexOrder = [b, c] := by
      rw [oc.lm₂_decomp, hb, hc]; rfl
    have m1 := h₁; have m2 := h₂
    simp only [qSerreRewritingSystem, qSerreRules, List.mem_cons,
      List.not_mem_nil, or_false] at m1 m2
    rcases m1 with h1|h1|h1|h1|h1|h1|h1 <;> rcases m2 with h2|h2|h2|h2|h2|h2|h2 <;>
      rw [h1] at e1 <;> rw [h2] at e2 <;>
      simp only [qSerre_lm_1, qSerre_lm_2, qSerre_lm_3, qSerre_lm_4, qSerre_lm_5,
        qSerre_lm_6, qSerre_lm_7, List.cons.injEq, and_true] at e1 e2 <;>
      obtain ⟨rfl, rfl⟩ := e1 <;> simp_all
  · omega

/-! ## §7  What remains

The `|overlap| = 1` case. By §3 that means `left = [a]`, `overlap = [b]`,
`right = [c]` with `lm₁ = [a,b]` and `lm₂ = [b,c]`, and since every rule is monic
(`qSerre_rules_monic`) the S-polynomial simplifies: the ambient word `[a,b,c]`
appears with coefficient `1` in both halves and cancels, leaving

  `spoly = a · tail₂  −  tail₁ · c`

where `tailᵢ` is the right-hand side of rule `i`. Bean qou-18s7 enumerated the
ambiguities of this shape — there are **8** — and verified by exact computation
over `ℚ(q)` that every one reduces to zero, each in two steps.

Formalising those 8 chains is the whole of the remaining gap in
`qSerre_is_gs_basis`. Each needs an explicit `MultiStepReduction`, and the cost
per chain is dominated by the `CoeffEq` obligation in `SingleStepReduction`,
which is an equality of coefficient functions at every monomial. -/

/-! ## §6  Bridge: `contextMul` of an explicit element is an explicit element

The cost driver in every critical-pair chain is `contextMul` at a *general*
monomial: its coefficient is stated through `excise`, so `contextMul_coeff_middle`
(which matches only the literal shape `a ++ w ++ b`) does not fire. These two
lemmas evaluate it once and for all, turning `a · (explicit element) · b` back
into an explicit element, after which a chain step is ordinary arithmetic. -/

section Bridge

open AlgElement

/-- Cancelling a common context on both sides. -/
theorem context_cancel {a b w u : Monomial SU2Gen} :
    a ++ w ++ b = a ++ u ++ b ↔ w = u := by
  constructor
  · intro h; exact List.append_cancel_left (List.append_cancel_right h)
  · intro h; rw [h]

/-- `a · (c₁·m₁ + c₂·m₂) · b = c₁·(a m₁ b) + c₂·(a m₂ b)`. -/
theorem contextMul_two_coeffEq (a b m₁ m₂ : Monomial SU2Gen) (c₁ c₂ : k) :
    CoeffEq (contextMul a (two m₁ c₁ m₂ c₂ : AlgElement SU2Gen k) b)
      (two (a ++ m₁ ++ b) c₁ (a ++ m₂ ++ b) c₂) := by
  intro m
  show (if a ++ excise a m b ++ b = m then
          (two m₁ c₁ m₂ c₂ : AlgElement SU2Gen k).coeff (excise a m b) else 0)
      = (if m = a ++ m₁ ++ b then c₁ else if m = a ++ m₂ ++ b then c₂ else 0)
  by_cases hs : a ++ excise a m b ++ b = m
  · have hm : m = a ++ excise a m b ++ b := hs.symm
    have e : ∀ u : Monomial SU2Gen, (m = a ++ u ++ b) ↔ (excise a m b = u) := by
      intro u
      constructor
      · intro h; rw [h, excise_middle]
      · intro h; rw [hm, h]
    rw [if_pos hs]
    show (if excise a m b = m₁ then c₁ else if excise a m b = m₂ then c₂ else 0) = _
    simp only [e]
  · rw [if_neg hs, if_neg, if_neg]
    · intro h; exact hs (by rw [h, excise_middle])
    · intro h; exact hs (by rw [h, excise_middle])

/-- The four-term counterpart. -/
theorem contextMul_four_coeffEq (a b m₁ m₂ m₃ m₄ : Monomial SU2Gen)
    (c₁ c₂ c₃ c₄ : k) :
    CoeffEq (contextMul a (four m₁ c₁ m₂ c₂ m₃ c₃ m₄ c₄ : AlgElement SU2Gen k) b)
      (four (a ++ m₁ ++ b) c₁ (a ++ m₂ ++ b) c₂
            (a ++ m₃ ++ b) c₃ (a ++ m₄ ++ b) c₄) := by
  intro m
  show (if a ++ excise a m b ++ b = m then
          (four m₁ c₁ m₂ c₂ m₃ c₃ m₄ c₄ : AlgElement SU2Gen k).coeff
            (excise a m b) else 0)
      = (if m = a ++ m₁ ++ b then c₁ else if m = a ++ m₂ ++ b then c₂ else
         if m = a ++ m₃ ++ b then c₃ else if m = a ++ m₄ ++ b then c₄ else 0)
  by_cases hs : a ++ excise a m b ++ b = m
  · have hm : m = a ++ excise a m b ++ b := hs.symm
    have e : ∀ u : Monomial SU2Gen, (m = a ++ u ++ b) ↔ (excise a m b = u) := by
      intro u
      constructor
      · intro h; rw [h, excise_middle]
      · intro h; rw [hm, h]
    rw [if_pos hs]
    show (if excise a m b = m₁ then c₁ else if excise a m b = m₂ then c₂ else
          if excise a m b = m₃ then c₃ else if excise a m b = m₄ then c₄ else 0) = _
    simp only [e]
  · rw [if_neg hs, if_neg, if_neg, if_neg, if_neg]
    · intro h; exact hs (by rw [h, excise_middle])
    · intro h; exact hs (by rw [h, excise_middle])
    · intro h; exact hs (by rw [h, excise_middle])
    · intro h; exact hs (by rw [h, excise_middle])

end Bridge

end UGB.GrobnerShirshov
