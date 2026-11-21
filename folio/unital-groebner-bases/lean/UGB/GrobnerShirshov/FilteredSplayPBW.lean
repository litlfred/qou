import UGB.GrobnerShirshov.BlockSplayPBW
import Mathlib.Algebra.MonoidAlgebra.Support

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

namespace UGB.GrobnerShirshov.BlockSplay

open UGB.GrobnerShirshov UGB.GrobnerShirshov.Diamond UGB.GrobnerShirshov.Quadratic AlgElement

universe u v w

variable {G : Type u} [DecidableEq G] {k : Type v} [CommRing k]

/-- The total weight of a word. -/
def wsum (wt : G → ℕ) (x : List G) : ℕ := (x.map wt).sum

@[simp] theorem wsum_nil (wt : G → ℕ) : wsum wt [] = 0 := rfl
@[simp] theorem wsum_cons (wt : G → ℕ) (a : G) (x : List G) :
    wsum wt (a :: x) = wt a + wsum wt x := by simp [wsum]
@[simp] theorem wsum_append (wt : G → ℕ) (x y : List G) :
    wsum wt (x ++ y) = wsum wt x + wsum wt y := by simp [wsum]

/-- **Filtered block-splay data** (the hypotheses of Thm. 1.9 of [leitner2006] on
    the presentation): a block splay whose order refines the weight, whose block
    products are associative and commutative, and whose `π` is strongly filtered. -/
structure FilteredData (G : Type u) [DecidableEq G] (k : Type v) [CommRing k]
    (ord : AdmissibleOrder G) (ι : Type w) [LinearOrder ι]
    extends BlockData G k ord ι where
  /-- Strictly lighter words are smaller. -/
  lt_of_wsum_lt : ∀ x y : List G, wsum wt x < wsum wt y → ord.lt x y
  /-- **Strong filtration**: every monomial of `π(a, b)` is lighter than `a b`. -/
  π_wt : ∀ a b, blk b < blk a → ∀ p ∈ (π a b).support,
    wsum wt (FreeMonoid.toList p) < wt a + wt b
  /-- Associativity of each block product. -/
  assoc : ∀ a b c, blk a = blk b → blk b = blk c →
    toBlockData.leftMul a (μ b c) = toBlockData.rightMul c (μ a b)
  /-- Commutativity of each block product. -/
  comm : ∀ a b, blk a = blk b → μ a b = μ b a

variable {ord : AdmissibleOrder G} {ι : Type w} [LinearOrder ι]

namespace FilteredData

variable (F : FilteredData G k ord ι)

/-- The same-block rules `a b ↦ μ(a, b)`: the presentation of the coordinate
    algebra `T' = TX / R` of Lemma 1.5. -/
noncomputable def same : QuadData G k ord where
  pairs := {p | F.blk p.1 = F.blk p.2}
  pairs_ne := by
    obtain ⟨a⟩ := F.inhabited
    exact ⟨(a, a), rfl⟩
  R := F.μ
  R_lt p hp w hw := by
    have := F.toBlockData.R_lt p (le_of_eq hp.symm) w
    rw [F.toBlockData.R_same hp] at this
    exact this hw

variable [Nontrivial k]

theorem same_rule_mem (p : F.same.pairs) : F.same.rule p ∈ F.quad.sys.rules := by
  refine ⟨⟨p.1, le_of_eq p.2.symm⟩, ?_⟩
  have e : F.quad.relMA p.1.1 p.1.2 = F.same.relMA p.1.1 p.1.2 := by
    show ofW _ - F.toBlockData.R _ _ = ofW _ - F.μ _ _
    rw [F.toBlockData.R_same p.2]
  unfold QuadData.rule
  congr 1
  rw [e]

theorem same_sub : ∀ r ∈ F.same.sys.rules, r ∈ F.quad.sys.rules := by
  rintro r ⟨p, rfl⟩; exact F.same_rule_mem p

/-- A same-block rule on a word of length two lies in `JM v` (same-block system)
    for any `v` of length three and no smaller weight. -/
theorem same_jm2 {v : Monomial G} (hv : v.length = 3) {a b : G} (h : F.blk a = F.blk b)
    (hw : F.wt a + F.wt b ≤ wsum F.wt v) :
    JM ord F.same.sys v (ofW [a, b] - F.μ a b) := by
  have := F.same.jm_rule (v := v) ⟨(a, b), h⟩ [] []
    (F.lt_of_wt _ _ (by simpa [wsum] using hw) (by simp [hv]))
  simpa [QuadData.relMA, same, ofW_nil] using this

theorem jm_termSum' {s : RewritingSystem G k} {v : Monomial G} {B : ι} {n : ℕ} {X : MA G k}
    (hX : F.Short B n X) (Φ : List G → MA G k) (h0 : JM ord s v (Φ []))
    (h1 : ∀ d, F.blk d = B → F.wt d ≤ n → JM ord s v (Φ [d])) :
    JM ord s v (termSum X Φ) := by
  refine JM.sum _ _ (fun p hp => JM.smul _ ?_)
  rcases hX p hp with h | ⟨d, hd, hb, hw⟩
  · rw [h]; exact h0
  · rw [hd]; exact h1 d hb hw

/-- The same-block rules form a Gröbner–Shirshov basis (Lemma 1.5): the only
    ambiguities are within one block, and they resolve by associativity. -/
theorem same_trivial : CompositionsTrivial ord F.same.sys := by
  rw [F.same.compositionsTrivial_iff]
  intro a b c hab hbc
  change F.blk a = F.blk b at hab
  change F.blk b = F.blk c at hbc
  have h1 : JM ord F.same.sys [a, b, c]
      (ofW [a] * F.μ b c - F.toBlockData.leftMul a (F.μ b c)) := by
    rw [BlockData.leftMul, ← termSum_left, termSum_sub]
    refine F.jm_termSum' (F.toBlockData.short_μ hbc) _
      (by simpa [onShort] using JM.zero) (fun d hd hw => ?_)
    have := F.same_jm2 (v := [a, b, c]) rfl (a := a) (b := d) (hab.trans hd.symm)
      (by simp; omega)
    simpa [onShort] using this
  have h2 : JM ord F.same.sys [a, b, c]
      (F.μ a b * ofW [c] - F.toBlockData.rightMul c (F.μ a b)) := by
    rw [BlockData.rightMul, ← termSum_right, termSum_sub]
    refine F.jm_termSum' (F.toBlockData.short_μ hab) _
      (by simpa [onShort] using JM.zero) (fun d hd hw => ?_)
    have := F.same_jm2 (v := [a, b, c]) rfl (a := d) (b := c) (hd.trans (hab.trans hbc))
      (by simp; omega)
    simpa [onShort] using this
  have e : F.same.overlapElt a b c =
      (ofW [a] * F.μ b c - F.toBlockData.leftMul a (F.μ b c))
        - (F.μ a b * ofW [c] - F.toBlockData.rightMul c (F.μ a b)) := by
    rw [F.assoc a b c hab hbc]; simp only [QuadData.overlapElt, same]; abel
  rw [e]; exact h1.sub h2

end FilteredData

/-! ## Weight of the support -/

/-- Every monomial of `X` has weight `< n`. -/
def WtLt (wt : G → ℕ) (n : ℕ) (X : MA G k) : Prop :=
  ∀ p ∈ X.support, wsum wt (FreeMonoid.toList p) < n

/-- Every monomial of `X` has weight `≤ n`. -/
def WtLe (wt : G → ℕ) (n : ℕ) (X : MA G k) : Prop :=
  ∀ p ∈ X.support, wsum wt (FreeMonoid.toList p) ≤ n

section Wt

open scoped Pointwise

variable {wt : G → ℕ}

theorem WtLt.zero {n : ℕ} : WtLt wt n (0 : MA G k) := by simp [WtLt]

theorem WtLt.mono {n m : ℕ} {X : MA G k} (h : WtLt wt n X) (hnm : n ≤ m) : WtLt wt m X :=
  fun p hp => lt_of_lt_of_le (h p hp) hnm

theorem WtLt.add {n : ℕ} {X Y : MA G k} (hX : WtLt wt n X) (hY : WtLt wt n Y) :
    WtLt wt n (X + Y) := by
  classical
  intro p hp
  rcases Finset.mem_union.mp (Finsupp.support_add hp) with h | h
  · exact hX p h
  · exact hY p h

theorem WtLt.smul {n : ℕ} (c : k) {X : MA G k} (hX : WtLt wt n X) : WtLt wt n (c • X) :=
  fun p hp => hX p (Finsupp.support_smul hp)

theorem WtLt.neg {n : ℕ} {X : MA G k} (hX : WtLt wt n X) : WtLt wt n (-X) := by
  intro p hp; rw [Finsupp.support_neg] at hp; exact hX p hp

theorem WtLt.sub {n : ℕ} {X Y : MA G k} (hX : WtLt wt n X) (hY : WtLt wt n Y) :
    WtLt wt n (X - Y) := by
  rw [sub_eq_add_neg]; exact hX.add hY.neg

theorem WtLt.sum {n : ℕ} {κ : Type*} (s : Finset κ) (X : κ → MA G k)
    (h : ∀ i ∈ s, WtLt wt n (X i)) : WtLt wt n (∑ i ∈ s, X i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using (WtLt.zero : WtLt wt n (0 : MA G k))
  | insert i s hi ih =>
    rw [Finset.sum_insert hi]
    exact (h i (Finset.mem_insert_self _ _)).add (ih (fun j hj => h j (Finset.mem_insert_of_mem hj)))

theorem WtLt.termSum {n : ℕ} (X : MA G k) (Φ : List G → MA G k)
    (h : ∀ p ∈ X.support, WtLt wt n (Φ (FreeMonoid.toList p))) : WtLt wt n (termSum X Φ) :=
  WtLt.sum _ _ (fun p hp => (h p hp).smul _)

theorem wsum_toList_mul (p q : FreeMonoid G) :
    wsum wt (FreeMonoid.toList (p * q)) = wsum wt (FreeMonoid.toList p) + wsum wt (FreeMonoid.toList q) := by
  rw [FreeMonoid.toList_mul, wsum_append]

theorem WtLt.mul {n m : ℕ} {X Y : MA G k} (hX : WtLt wt n X) (hY : WtLe wt m Y) :
    WtLt wt (n + m) (X * Y) := by
  classical
  intro p hp
  obtain ⟨x, hx, y, hy, rfl⟩ := Finset.mem_mul.mp (MonoidAlgebra.support_mul X Y hp)
  rw [wsum_toList_mul]; have := hX x hx; have := hY y hy; omega

theorem WtLt.mul' {n m : ℕ} {X Y : MA G k} (hX : WtLe wt n X) (hY : WtLt wt m Y) :
    WtLt wt (n + m) (X * Y) := by
  classical
  intro p hp
  obtain ⟨x, hx, y, hy, rfl⟩ := Finset.mem_mul.mp (MonoidAlgebra.support_mul X Y hp)
  rw [wsum_toList_mul]; have := hX x hx; have := hY y hy; omega

theorem wtLe_ofW (w : List G) : WtLe wt (wsum wt w) (ofW w : MA G k) := by
  intro p hp
  have : p = FreeMonoid.ofList w := by
    by_contra hne
    rw [Finsupp.mem_support_iff, ← FreeMonoid.ofList_toList p, ofW_apply] at hp
    rw [if_neg] at hp
    · exact hp rfl
    · intro he; exact hne (by rw [← FreeMonoid.ofList_toList p, he])
  rw [this, FreeMonoid.toList_ofList]

theorem wtLt_ofW {n : ℕ} {w : List G} (h : wsum wt w < n) : WtLt wt n (ofW w : MA G k) :=
  fun p hp => lt_of_le_of_lt (wtLe_ofW w p hp) h

end Wt

namespace FilteredData

variable (F : FilteredData G k ord ι)

/-- An element all of whose monomials are lighter than `v` lies below `v`. -/
theorem below_of_wtLt {v : Monomial G} {X : MA G k} (h : WtLt F.wt (wsum F.wt v) X) :
    Below ord v (ofMA X) := by
  intro m hm
  have := h (FreeMonoid.ofList m) (Finsupp.mem_support_iff.mpr hm)
  rw [FreeMonoid.toList_ofList] at this
  exact F.lt_of_wsum_lt _ _ this

theorem π_wtLt {a b : G} (h : F.blk b < F.blk a) : WtLt F.wt (F.wt a + F.wt b) (F.π a b) :=
  F.π_wt a b h

end FilteredData

/-! ## Moving a letter through a word: the derivation `D_x` -/

namespace FilteredData

variable (F : FilteredData G k ord ι)

theorem ofW_cons (y : G) (w : List G) : (ofW (y :: w) : MA G k) = ofW [y] * ofW w := by
  rw [← ofW_append]; rfl

/-- The commutator correction of two letters, for every pair: `π(x, y)` across
    blocks (extended skew), `0` within a block. -/
noncomputable def P (x y : G) : MA G k :=
  if F.blk y < F.blk x then F.π x y else if F.blk x < F.blk y then -F.π y x else 0

/-- `D_x` on a word: the derivation with `D_x(y) = P(x, y)`. -/
noncomputable def derivWord (x : G) : List G → MA G k
  | [] => 0
  | y :: w => F.P x y * ofW w + ofW [y] * derivWord x w

/-- `D_x` extended linearly. -/
noncomputable def deriv (x : G) (X : MA G k) : MA G k := termSum X (F.derivWord x)

variable [Nontrivial k]

/-- One commutation: `a (x y − y x − P(x, y)) b` lies in the span below `v`. -/
theorem comm_letter {v : Monomial G} (x y : G) (a b : List G)
    (hw : wsum F.wt (a ++ [x, y] ++ b) < wsum F.wt v) :
    JM ord F.quad.sys v (ofW a * (ofW [x, y] - ofW [y, x] - F.P x y) * ofW b) := by
  have hlt : ord.lt (a ++ [x, y] ++ b) v := F.lt_of_wsum_lt _ _ hw
  have hlt' : ord.lt (a ++ [y, x] ++ b) v :=
    F.lt_of_wsum_lt _ _ (by simp at hw ⊢; omega)
  rcases lt_trichotomy (F.blk y) (F.blk x) with h | h | h
  · have := F.toBlockData.jm h.le a b hlt
    rw [F.toBlockData.R_cross h] at this
    rw [P, if_pos h, sub_sub]; exact this
  · have g1 := F.toBlockData.jm (le_of_eq h) a b hlt
    have g2 := F.toBlockData.jm (le_of_eq h.symm) a b hlt'
    rw [F.toBlockData.R_same h.symm] at g1
    rw [F.toBlockData.R_same h] at g2
    rw [F.comm x y h.symm] at g1
    rw [P, if_neg (by rw [h]; exact lt_irrefl _), if_neg (by rw [h]; exact lt_irrefl _)]
    have e : ofW a * (ofW [x, y] - ofW [y, x] - 0) * ofW b =
        ofW a * (ofW [x, y] - F.μ y x) * ofW b - ofW a * (ofW [y, x] - F.μ y x) * ofW b := by
      noncomm_ring
    rw [e]; exact g1.sub g2
  · have := F.toBlockData.jm h.le a b hlt'
    rw [F.toBlockData.R_cross h] at this
    rw [P, if_neg (not_lt.mpr h.le), if_pos h]
    have e : ofW a * (ofW [x, y] - ofW [y, x] - -F.π y x) * ofW b =
        -(ofW a * (ofW [y, x] - (ofW [x, y] + F.π y x)) * ofW b) := by noncomm_ring
    rw [e]; exact this.neg

/-- **The commutator lemma** on a word: `a (x w − w x − D_x w) b` lies in the span
    below `v` once everything is lighter than `v`. -/
theorem comm_word {v : Monomial G} (x : G) (w : List G) : ∀ a b : List G,
    F.wt x + wsum F.wt (a ++ w ++ b) < wsum F.wt v →
    JM ord F.quad.sys v
      (ofW a * (ofW [x] * ofW w - ofW w * ofW [x] - F.derivWord x w) * ofW b) := by
  induction w with
  | nil => intro a b _; simpa [derivWord, ofW_nil] using (JM.zero : JM ord F.quad.sys v 0)
  | cons y w ih =>
    intro a b hw
    have h1 := F.comm_letter (v := v) x y a (w ++ b) (by simp at hw ⊢; omega)
    have h2 := ih (a ++ [y]) b (by simp at hw ⊢; omega)
    have e : ofW a * (ofW [x] * ofW (y :: w) - ofW (y :: w) * ofW [x] - F.derivWord x (y :: w))
        * ofW b =
        ofW a * (ofW [x, y] - ofW [y, x] - F.P x y) * ofW (w ++ b)
          + ofW (a ++ [y]) * (ofW [x] * ofW w - ofW w * ofW [x] - F.derivWord x w) * ofW b := by
      rw [derivWord, ofW_cons y w, ofW_append w b, ofW_append a [y],
        show (ofW [x, y] : MA G k) = ofW [x] * ofW [y] from by rw [← ofW_append]; rfl,
        show (ofW [y, x] : MA G k) = ofW [y] * ofW [x] from by rw [← ofW_append]; rfl]
      noncomm_ring
    rw [e]; exact h1.add h2

/-- **The commutator lemma**: `x X − X x − D_x X` lies in the span below `v` when
    every monomial of `X`, with `x`, is lighter than `v`. -/
theorem comm_elt {v : Monomial G} (x : G) {X : MA G k}
    (hX : ∀ p ∈ X.support, F.wt x + wsum F.wt (FreeMonoid.toList p) < wsum F.wt v) :
    JM ord F.quad.sys v (ofW [x] * X - X * ofW [x] - F.deriv x X) := by
  rw [deriv, ← termSum_left, ← termSum_right, termSum_sub, termSum_sub]
  refine JM.sum _ _ (fun p hp => JM.smul _ ?_)
  have := F.comm_word (v := v) x (FreeMonoid.toList p) [] [] (by simpa using hX p hp)
  simp only [ofW_nil, one_mul, mul_one] at this
  convert this using 2
  rw [ofW_append, ofW_append]

end FilteredData

end UGB.GrobnerShirshov.BlockSplay
