import UGB.GrobnerShirshov.BlockSplayPBW

set_option linter.unusedSectionVars false

/-!
# Filtered block splays: the four conditions of Thm. 1.9 from a Poisson bracket

`BlockSplayPBW.lean` reduces PBW for a block splay to four conditions, each stated
modulo the span of the rules below a word. This file discharges them from the
hypotheses of Thm. 1.9 of [leitner2006]:

* the block products are associative and commutative,
* `π` is a skew biderivation satisfying Jacobi on the coordinate algebra,
* `π` is strongly filtered: every monomial of `π(a, b)` has weight `< wt a + wt b`.

The bridge is an algebra map `q` from the free algebra onto the coordinate algebra
`T' = T X / R` (`R` the same-block rules), whose kernel is the two-sided ideal of
`R`. An element killed by `q` and lying below a word `v` is in the span below `v`,
because `R` is itself a Gröbner–Shirshov basis (associativity).

-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, Lemma 1.5, Lemma 1.7, Thm. 1.9.
-/

namespace UGB.GrobnerShirshov.Diamond

open UGB.GrobnerShirshov AlgElement

universe u v

variable {G : Type u} [DecidableEq G] {k : Type v} [CommRing k]

variable (sys : RewritingSystem G k) in
/-- The two-sided ideal of a rewriting system, as a predicate on the free algebra. -/
inductive InId : MA G k → Prop
  | gen (a b : Monomial G) (r : ReductionRule G k) (hr : r ∈ sys.rules) :
      InId (ofW a * toMA r.relation * ofW b)
  | zero : InId 0
  | add {F H : MA G k} : InId F → InId H → InId (F + H)
  | smul (c : k) {F : MA G k} : InId F → InId (c • F)

variable {ord : AdmissibleOrder G} {sys : RewritingSystem G k}

theorem InId.neg {F : MA G k} (h : InId sys F) : InId sys (-F) := by
  have := InId.smul (-1 : k) h; rwa [neg_one_smul] at this

theorem InId.sub {F H : MA G k} (hF : InId sys F) (hH : InId sys H) : InId sys (F - H) := by
  rw [sub_eq_add_neg]; exact hF.add hH.neg

theorem InId.sum {ι : Type*} (s : Finset ι) (F : ι → MA G k) (h : ∀ i ∈ s, InId sys (F i)) :
    InId sys (∑ i ∈ s, F i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using (InId.zero : InId sys 0)
  | insert i s hi ih =>
    rw [Finset.sum_insert hi]
    exact (h i (Finset.mem_insert_self _ _)).add (ih (fun j hj => h j (Finset.mem_insert_of_mem hj)))

theorem InId.ctx (a b : Monomial G) {F : MA G k} (h : InId sys F) :
    InId sys (ofW a * F * ofW b) := by
  induction h with
  | gen x y r hr =>
    have e : ofW a * (ofW x * toMA r.relation * ofW y) * ofW b =
        ofW (a ++ x) * toMA r.relation * ofW (y ++ b) := by
      simp only [ofW_append, mul_assoc]
    rw [e]; exact InId.gen _ _ r hr
  | zero => simpa using (InId.zero : InId sys 0)
  | add _ _ ihF ihH => rw [mul_add, add_mul]; exact ihF.add ihH
  | smul c _ ih => rw [mul_smul_comm, smul_mul_assoc]; exact ih.smul c

theorem InId.mul_left (X : MA G k) {F : MA G k} (h : InId sys F) : InId sys (X * F) := by
  rw [ma_eq_sum X, Finset.sum_mul]
  refine InId.sum _ _ (fun p _ => ?_)
  rw [smul_mul_assoc]
  have := h.ctx (FreeMonoid.toList p) []
  rw [ofW_nil, mul_one] at this
  exact this.smul _

theorem InId.mul_right (X : MA G k) {F : MA G k} (h : InId sys F) : InId sys (F * X) := by
  rw [ma_eq_sum X, Finset.mul_sum]
  refine InId.sum _ _ (fun p _ => ?_)
  rw [mul_smul_comm]
  have := h.ctx [] (FreeMonoid.toList p)
  rw [ofW_nil, one_mul] at this
  exact this.smul _

theorem InId.zeroNF (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (hru : ∀ f, RU ord sys f) {F : MA G k} (h : InId sys F) : ZeroNF ord sys (ofMA F) := by
  induction h with
  | gen a b r hr => exact zeroNF_congr hlc (ofMA_ctx _ _ _) (zeroNF_ctx hlc ⟨r, a, b⟩ hr)
  | zero => exact zeroNF_of_isZero ofMA_zero
  | add _ _ ihF ihH =>
    exact zeroNF_congr hlc (ofMA_add _ _) (zeroNF_add hlc (hru _) (hru _) ihF ihH)
  | smul c _ ih => exact zeroNF_congr hlc (ofMA_smul _ _) (zeroNF_smul hlc c (hru _) ih)

/-- **An ideal element below `v` is in the span below `v`**, for a system with
    trivial compositions and unit leading coefficients. -/
theorem jm_of_inId (ht : CompositionsTrivial ord sys) (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {v : Monomial G} {F : MA G k} (hF : InId sys F) (hb : Below ord v (ofMA F)) :
    JM ord sys v F := by
  obtain ⟨n, hn, hz⟩ := hF.zeroNF hlc (fun f => reductionUnique_of_trivial ord sys ht hlc f)
  have := (JM_of_multistep (u := v) [] [] (fun m h => by simpa using h) hn.reduces hb).2
  rwa [toMA_of_isZero hz, sub_zero, ofW_nil, one_mul, mul_one, toMA_ofMA] at this

/-- The span below `v` grows with the rule set. -/
theorem JM.mono {sys' : RewritingSystem G k} (hss : ∀ r ∈ sys.rules, r ∈ sys'.rules)
    {v : Monomial G} {F : MA G k} (h : JM ord sys v F) : JM ord sys' v F := by
  induction h with
  | gen s hs hlt => exact JM.gen s (hss _ hs) hlt
  | zero => exact JM.zero
  | add _ _ ihF ihH => exact ihF.add ihH
  | smul c _ ih => exact ih.smul c

end UGB.GrobnerShirshov.Diamond
