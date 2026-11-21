import UGB.GrobnerShirshov.QuadraticPBW

set_option linter.unusedSectionVars false

/-!
# Block splays: Thm. 1.9 of [leitner2006] for basis-presented coordinate algebras

The generators are the basis letters of a family of commutative *coordinate
algebras* `Aᵢ`, indexed by a linearly ordered set `ι`; `blk a ∈ ι` is the block
of the letter `a`. The rules are

* **within a block** (`blk a = blk b`): `a b ↦ μ(a, b)`, the product in the
  coordinate algebra, a combination of the empty word (the unit) and single
  letters of the same block;
* **across blocks** (`blk b < blk a`): `a b ↦ b a + π(a, b)`, the commutation rule
  with the correction `π` of a strongly filtered Poisson structure.

The normal words are the **ordered monomials**: at most one letter per block,
blocks strictly increasing. This is the presentation of `U = T / J` in Thm. 1.9
of [leitner2006] when each coordinate algebra is presented by a basis, which is
the case used in Thm. 3.7 (the divided powers `δxⱼ^{(m)}` of a commutative
formal subgroup are a basis of its distribution algebra).

**What is proved here.** `overlapCondition_of` — the triple-overlap condition of
`QuadraticPBW.lean`, hence `normalFormBasis` (PBW), follows from four conditions,
one per ambiguity shape `a b c`:

* `AssocCondition` (all three letters in one block): the product of the block
  is associative, `a·μ(b,c) = μ(a,b)·c` after one more multiplication;
* `RightDerivCondition` (`blk a = blk b > blk c`, the ambiguity `S2` of the
  paper): `π(·, c)` is a derivation of the block product,
  `π(μ(a,b), c) = π(a,c) b + a π(b,c)`;
* `LeftDerivCondition` (`blk a > blk b = blk c`, the ambiguity `S1`): the mirror
  identity `π(a, μ(b,c)) = b π(a,c) + π(a,b) c`;
* `JacobiCondition` (`blk a > blk b > blk c`, the ambiguity `S3`): the Jacobi
  element of `SplayPBW.lean` (with `cf = 1`).

Each condition is stated modulo the span of the rules below `a b c`, which is
exactly what the paper's "`≡ 0`" means; the identities themselves are the
hypotheses of Thm. 1.9 (internal symmetry, `π` descends to each `Aᵢ`, Jacobi).

-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, Thm. 1.9 and its proof (S1, S2, S3).
-/

namespace UGB.GrobnerShirshov.BlockSplay

open UGB.GrobnerShirshov UGB.GrobnerShirshov.Diamond UGB.GrobnerShirshov.Quadratic AlgElement

universe u v w

variable {G : Type u} [DecidableEq G] {k : Type v} [CommRing k]

/-- A word of length at most one; its value under `e` (empty word) and `f` (a letter). -/
noncomputable def onShort (e : MA G k) (f : G → MA G k) : List G → MA G k
  | [] => e
  | [d] => f d
  | _ => 0

/-- Replace each term `F p • p` of `F` by `F p • Φ p`. -/
noncomputable def termSum (F : MA G k) (Φ : List G → MA G k) : MA G k :=
  ∑ p ∈ F.support, F p • Φ (FreeMonoid.toList p)

theorem termSum_ofW (F : MA G k) : termSum F ofW = F := (ma_eq_sum F).symm

theorem termSum_left (F : MA G k) (x : List G) :
    termSum F (fun w => ofW (x ++ w)) = ofW x * F := by
  conv_rhs => rw [← termSum_ofW F]
  simp only [termSum, Finset.mul_sum, mul_smul_comm, ofW_append]

theorem termSum_right (F : MA G k) (y : List G) :
    termSum F (fun w => ofW (w ++ y)) = F * ofW y := by
  conv_rhs => rw [← termSum_ofW F]
  simp only [termSum, Finset.sum_mul, smul_mul_assoc, ofW_append]

theorem termSum_sub (F : MA G k) (Φ Ψ : List G → MA G k) :
    termSum F Φ - termSum F Ψ = termSum F (fun w => Φ w - Ψ w) := by
  simp only [termSum, ← Finset.sum_sub_distrib, smul_sub]

/-- **Block-splay data.** -/
structure BlockData (G : Type u) [DecidableEq G] (k : Type v) [CommRing k]
    (ord : AdmissibleOrder G) (ι : Type w) [LinearOrder ι] where
  /-- The block of each letter. -/
  blk : G → ι
  /-- The product of two letters of one block. -/
  μ : G → G → MA G k
  /-- The commutation correction of two letters of different blocks. -/
  π : G → G → MA G k
  /-- A letter exists. -/
  inhabited : Nonempty G
  /-- The weight of each letter (the filtration degree). -/
  wt : G → ℕ
  /-- The product of two letters of a block is a combination of the unit and
      letters of that block, of weight at most the sum of the weights. -/
  μ_short : ∀ a b, blk a = blk b → ∀ p ∈ (μ a b).support,
    FreeMonoid.toList p = [] ∨
      ∃ d, FreeMonoid.toList p = [d] ∧ blk d = blk a ∧ wt d ≤ wt a + wt b
  /-- The order refines the weight filtration: a shorter word of no larger total
      weight is smaller. -/
  lt_of_wt : ∀ x y : List G, (x.map wt).sum ≤ (y.map wt).sum → x.length < y.length →
    ord.lt x y
  /-- Across blocks the swapped word is smaller (`x ≪ x'` for `blk x < blk x'`). -/
  swap_lt : ∀ a b, blk b < blk a → ord.lt [b, a] [a, b]
  /-- **Strong filtration**: every monomial of `π(a, b)` is below `a b`. -/
  π_lt : ∀ a b, blk b < blk a → ∀ p ∈ (π a b).support, ord.lt (FreeMonoid.toList p) [a, b]

variable {ord : AdmissibleOrder G} {ι : Type w} [LinearOrder ι]

namespace BlockData

variable (D : BlockData G k ord ι)

open Classical in
/-- The right-hand side of the rule for `a b`. -/
noncomputable def R (a b : G) : MA G k :=
  if D.blk b < D.blk a then ofW [b, a] + D.π a b else D.μ a b

theorem R_cross {a b : G} (h : D.blk b < D.blk a) : D.R a b = ofW [b, a] + D.π a b := by
  simp [R, h]

theorem R_same {a b : G} (h : D.blk a = D.blk b) : D.R a b = D.μ a b := by
  simp [R, h]

theorem R_lt (p : G × G) (hp : D.blk p.2 ≤ D.blk p.1) (w : FreeMonoid G)
    (hw : w ∈ (D.R p.1 p.2).support) : ord.lt (FreeMonoid.toList w) [p.1, p.2] := by
  classical
  rcases lt_or_eq_of_le hp with h | h
  · rw [D.R_cross h] at hw
    have hw' := Finsupp.support_add hw
    rcases Finset.mem_union.mp hw' with h1 | h1
    · have : w = FreeMonoid.ofList [p.2, p.1] := by
        rw [← FreeMonoid.ofList_toList w, Finsupp.mem_support_iff, ofW_apply] at h1
        by_contra hne
        rw [if_neg] at h1
        · exact h1 rfl
        · intro he; exact hne (by rw [he, FreeMonoid.ofList_toList])
      rw [this, FreeMonoid.toList_ofList]; exact D.swap_lt _ _ h
    · exact D.π_lt _ _ h w h1
  · rw [D.R_same h.symm] at hw
    rcases D.μ_short _ _ h.symm w hw with h0 | ⟨d, hd, -, hwd⟩
    · rw [h0]; exact D.lt_of_wt _ _ (by simp) (by simp)
    · rw [hd]; exact D.lt_of_wt _ _ (by simpa using hwd) (by simp)

/-- The quadratic data of a block splay: every pair `(a, b)` with `blk b ≤ blk a`
    carries a rule. -/
noncomputable def quad : QuadData G k ord where
  pairs := {p | D.blk p.2 ≤ D.blk p.1}
  pairs_ne := by
    obtain ⟨a⟩ := D.inhabited
    exact ⟨(a, a), le_refl _⟩
  R := D.R
  R_lt p hp := D.R_lt p hp

variable [Nontrivial k]

theorem relMA_eq (a b : G) : D.quad.relMA a b = ofW [a, b] - D.R a b := rfl

/-- A rule placed in context below `v` lies in `JM v`. -/
theorem jm {v : Monomial G} {a b : G} (h : D.blk b ≤ D.blk a) (x y : Monomial G)
    (hlt : ord.lt (x ++ [a, b] ++ y) v) :
    JM ord D.quad.sys v (ofW x * (ofW [a, b] - D.R a b) * ofW y) :=
  D.quad.jm_rule ⟨(a, b), h⟩ x y hlt

/-- A rule on a word of length two lies in `JM v` for any `v` of length three and
    no smaller weight. -/
theorem jm2 {v : Monomial G} (hv : v.length = 3) {a b : G} (h : D.blk b ≤ D.blk a)
    (hw : D.wt a + D.wt b ≤ (v.map D.wt).sum) :
    JM ord D.quad.sys v (ofW [a, b] - D.R a b) := by
  have := D.jm (v := v) h [] [] (D.lt_of_wt _ _ (by simpa using hw) (by simp [hv]))
  simpa [ofW_nil] using this

/-! ## Moving a letter past an element of a block -/

/-- `F` is a combination of the unit and letters of the block `B` of weight at most `n`. -/
def Short (B : ι) (n : ℕ) (F : MA G k) : Prop :=
  ∀ p ∈ F.support, FreeMonoid.toList p = [] ∨
    ∃ d, FreeMonoid.toList p = [d] ∧ D.blk d = B ∧ D.wt d ≤ n

theorem jm_termSum {v : Monomial G} {B : ι} {n : ℕ} {F : MA G k} (hF : D.Short B n F)
    (Φ : List G → MA G k) (h0 : JM ord D.quad.sys v (Φ []))
    (h1 : ∀ d, D.blk d = B → D.wt d ≤ n → JM ord D.quad.sys v (Φ [d])) :
    JM ord D.quad.sys v (termSum F Φ) := by
  refine JM.sum _ _ (fun p hp => JM.smul _ ?_)
  rcases hF p hp with h | ⟨d, hd, hb, hw⟩
  · rw [h]; exact h0
  · rw [hd]; exact h1 d hb hw

/-- Left multiplication within a block: `a F ≡ M_a(F)`. -/
noncomputable def leftMul (a : G) (F : MA G k) : MA G k :=
  termSum F (onShort (ofW [a]) (D.μ a))

/-- Right multiplication within a block: `F c ≡ M'_c(F)`. -/
noncomputable def rightMul (c : G) (F : MA G k) : MA G k :=
  termSum F (onShort (ofW [c]) (fun d => D.μ d c))

/-- `π(·, c)` extended linearly to the unit and letters (`π(1, c) = 0`). -/
noncomputable def commR (c : G) (F : MA G k) : MA G k :=
  termSum F (onShort 0 (fun d => D.π d c))

/-- `π(a, ·)` extended linearly to the unit and letters (`π(a, 1) = 0`). -/
noncomputable def commL (a : G) (F : MA G k) : MA G k :=
  termSum F (onShort 0 (fun d => D.π a d))

theorem leftMul_jm {v : Monomial G} (hv : v.length = 3) {a : G} {n : ℕ} {F : MA G k}
    (hF : D.Short (D.blk a) n F) (hn : D.wt a + n ≤ (v.map D.wt).sum) :
    JM ord D.quad.sys v (ofW [a] * F - D.leftMul a F) := by
  rw [leftMul, ← termSum_left, termSum_sub]
  refine D.jm_termSum hF _ (by simpa [onShort] using JM.zero) (fun d hd hw => ?_)
  have := D.jm2 hv (a := a) (b := d) hd.le (by omega)
  simpa [onShort, D.R_same hd.symm] using this

theorem rightMul_jm {v : Monomial G} (hv : v.length = 3) {c : G} {n : ℕ} {F : MA G k}
    (hF : D.Short (D.blk c) n F) (hn : n + D.wt c ≤ (v.map D.wt).sum) :
    JM ord D.quad.sys v (F * ofW [c] - D.rightMul c F) := by
  rw [rightMul, ← termSum_right, termSum_sub]
  refine D.jm_termSum hF _ (by simpa [onShort] using JM.zero) (fun d hd hw => ?_)
  have := D.jm2 hv (a := d) (b := c) hd.ge (by omega)
  simpa [onShort, D.R_same hd] using this

theorem commR_jm {v : Monomial G} (hv : v.length = 3) {c : G} {B : ι} (hB : D.blk c < B)
    {n : ℕ} {F : MA G k} (hF : D.Short B n F) (hn : n + D.wt c ≤ (v.map D.wt).sum) :
    JM ord D.quad.sys v (F * ofW [c] - ofW [c] * F - D.commR c F) := by
  rw [commR, ← termSum_left, ← termSum_right, termSum_sub, termSum_sub]
  refine D.jm_termSum hF _ (by simpa [onShort] using JM.zero) (fun d hd hw => ?_)
  have hlt : D.blk c < D.blk d := hd ▸ hB
  have := D.jm2 hv (a := d) (b := c) hlt.le (by omega)
  rw [D.R_cross hlt] at this
  have e : ofW ([d] ++ [c]) - ofW ([c] ++ [d]) - onShort 0 (fun d => D.π d c) [d] =
      ofW [d, c] - (ofW [c, d] + D.π d c) := by simp [onShort]; abel
  simp only at e ⊢
  rw [e]; exact this

theorem commL_jm {v : Monomial G} (hv : v.length = 3) {a : G} {B : ι} (hB : B < D.blk a)
    {n : ℕ} {F : MA G k} (hF : D.Short B n F) (hn : D.wt a + n ≤ (v.map D.wt).sum) :
    JM ord D.quad.sys v (ofW [a] * F - F * ofW [a] - D.commL a F) := by
  rw [commL, ← termSum_left, ← termSum_right, termSum_sub, termSum_sub]
  refine D.jm_termSum hF _ (by simpa [onShort] using JM.zero) (fun d hd hw => ?_)
  have hlt : D.blk d < D.blk a := hd ▸ hB
  have := D.jm2 hv (a := a) (b := d) hlt.le (by omega)
  rw [D.R_cross hlt] at this
  have e : ofW ([a] ++ [d]) - ofW ([d] ++ [a]) - onShort 0 (fun d => D.π a d) [d] =
      ofW [a, d] - (ofW [d, a] + D.π a d) := by simp [onShort]; abel
  simp only at e ⊢
  rw [e]; exact this

theorem short_μ {a b : G} (h : D.blk a = D.blk b) :
    D.Short (D.blk a) (D.wt a + D.wt b) (D.μ a b) :=
  D.μ_short a b h

/-! ## The four ambiguity shapes -/

/-- **Associativity** of each block product, modulo the span below `a b c`. -/
def AssocCondition : Prop :=
  ∀ a b c : G, D.blk a = D.blk b → D.blk b = D.blk c →
    JM ord D.quad.sys [a, b, c] (D.leftMul a (D.μ b c) - D.rightMul c (D.μ a b))

/-- **`π(·, c)` is a derivation of the block product** (ambiguity `S2`). -/
def RightDerivCondition : Prop :=
  ∀ a b c : G, D.blk a = D.blk b → D.blk c < D.blk b →
    JM ord D.quad.sys [a, b, c]
      (D.π a c * ofW [b] + ofW [a] * D.π b c - D.commR c (D.μ a b))

/-- **`π(a, ·)` is a derivation of the block product** (ambiguity `S1`). -/
def LeftDerivCondition : Prop :=
  ∀ a b c : G, D.blk b < D.blk a → D.blk b = D.blk c →
    JM ord D.quad.sys [a, b, c]
      (D.commL a (D.μ b c) - ofW [b] * D.π a c - D.π a b * ofW [c])

/-- The Jacobi element of a chain of three blocks (`cf = 1`). -/
noncomputable def jacobi (a b c : G) : MA G k :=
  ofW [a] * D.π b c - D.π b c * ofW [a] + ofW [c] * D.π a b - D.π a b * ofW [c]
    + D.π a c * ofW [b] - ofW [b] * D.π a c

/-- **The Jacobi condition** (ambiguity `S3`). -/
def JacobiCondition : Prop :=
  ∀ a b c : G, D.blk b < D.blk a → D.blk c < D.blk b →
    JM ord D.quad.sys [a, b, c] (D.jacobi a b c)

theorem overlap_same (a b c : G) (hab : D.blk a = D.blk b) (hbc : D.blk b = D.blk c) :
    JM ord D.quad.sys [a, b, c]
      (D.quad.overlapElt a b c - (D.leftMul a (D.μ b c) - D.rightMul c (D.μ a b))) := by
  have h1 := D.leftMul_jm (v := [a, b, c]) rfl (a := a) (F := D.μ b c)
    (by rw [hab]; exact D.short_μ hbc) (by simp)
  have h2 := D.rightMul_jm (v := [a, b, c]) rfl (c := c) (F := D.μ a b)
    (by rw [← hbc, ← hab]; exact D.short_μ hab) (by simp; omega)
  have e : D.quad.overlapElt a b c - (D.leftMul a (D.μ b c) - D.rightMul c (D.μ a b)) =
      (ofW [a] * D.μ b c - D.leftMul a (D.μ b c)) - (D.μ a b * ofW [c] - D.rightMul c (D.μ a b)) := by
    simp only [QuadData.overlapElt, quad, D.R_same hbc, D.R_same hab]; abel
  rw [e]; exact h1.sub h2

theorem overlap_right (a b c : G) (hab : D.blk a = D.blk b) (hcb : D.blk c < D.blk b) :
    JM ord D.quad.sys [a, b, c]
      (D.quad.overlapElt a b c - (D.π a c * ofW [b] + ofW [a] * D.π b c - D.commR c (D.μ a b))) := by
  have hca : D.blk c < D.blk a := hab ▸ hcb
  have g1 := D.jm (v := [a, b, c]) hca.le [] [b]
    (by simpa using compat (ord := ord) [a] [] (D.swap_lt _ _ hcb))
  have g2 := D.jm (v := [a, b, c]) hab.ge [c] []
    (ord.lt_trans (by simpa using compat (ord := ord) [] [b] (D.swap_lt _ _ hca))
      (by simpa using compat (ord := ord) [a] [] (D.swap_lt _ _ hcb)))
  have g3 := D.commR_jm (v := [a, b, c]) rfl (c := c) (B := D.blk a) hca (D.short_μ hab)
    (by simp; omega)
  rw [D.R_cross hca] at g1
  rw [D.R_same hab] at g2
  simp only [ofW_nil, one_mul, mul_one] at g1 g2
  have e : D.quad.overlapElt a b c - (D.π a c * ofW [b] + ofW [a] * D.π b c - D.commR c (D.μ a b)) =
      (ofW [a, c] - (ofW [c, a] + D.π a c)) * ofW [b] + ofW [c] * (ofW [a, b] - D.μ a b)
        - (D.μ a b * ofW [c] - ofW [c] * D.μ a b - D.commR c (D.μ a b)) := by
    simp only [QuadData.overlapElt, quad, D.R_cross hcb, D.R_same hab, mul_add, add_mul,
      sub_mul, mul_sub, ← ofW_append, List.cons_append, List.nil_append]
    abel
  rw [e]; exact (g1.add g2).sub g3

theorem overlap_left (a b c : G) (hba : D.blk b < D.blk a) (hbc : D.blk b = D.blk c) :
    JM ord D.quad.sys [a, b, c]
      (D.quad.overlapElt a b c - (D.commL a (D.μ b c) - ofW [b] * D.π a c - D.π a b * ofW [c])) := by
  have hca : D.blk c < D.blk a := hbc ▸ hba
  have h1 : ord.lt [b, a, c] [a, b, c] := by
    simpa using compat (ord := ord) [] [c] (D.swap_lt _ _ hba)
  have g1 := D.jm (v := [a, b, c]) hca.le [b] [] (by simpa using h1)
  have g2 := D.jm (v := [a, b, c]) hbc.ge [] [a]
    (ord.lt_trans (by simpa using compat (ord := ord) [b] [] (D.swap_lt _ _ hca)) h1)
  have g3 := D.commL_jm (v := [a, b, c]) rfl (a := a) (B := D.blk b) hba (D.short_μ hbc)
    (by simp)
  rw [D.R_cross hca] at g1
  rw [D.R_same hbc] at g2
  simp only [ofW_nil, one_mul, mul_one] at g1 g2
  have e : D.quad.overlapElt a b c - (D.commL a (D.μ b c) - ofW [b] * D.π a c - D.π a b * ofW [c]) =
      ofW [a] * D.μ b c - D.μ b c * ofW [a] - D.commL a (D.μ b c)
        - ofW [b] * (ofW [a, c] - (ofW [c, a] + D.π a c)) - (ofW [b, c] - D.μ b c) * ofW [a] := by
    simp only [QuadData.overlapElt, quad, D.R_cross hba, D.R_same hbc, mul_add, add_mul,
      sub_mul, mul_sub, ← ofW_append, List.cons_append, List.nil_append]
    abel
  rw [e]; exact (g3.sub g1).sub g2

theorem overlap_chain (a b c : G) (hba : D.blk b < D.blk a) (hcb : D.blk c < D.blk b) :
    JM ord D.quad.sys [a, b, c] (D.quad.overlapElt a b c - D.jacobi a b c) := by
  have hca : D.blk c < D.blk a := hcb.trans hba
  have h1 : ord.lt [b, a, c] [a, b, c] := by
    simpa using compat (ord := ord) [] [c] (D.swap_lt _ _ hba)
  have h2 : ord.lt [a, c, b] [a, b, c] := by
    simpa using compat (ord := ord) [a] [] (D.swap_lt _ _ hcb)
  have h3 : ord.lt [b, c, a] [a, b, c] :=
    ord.lt_trans (by simpa using compat (ord := ord) [b] [] (D.swap_lt _ _ hca)) h1
  have h4 : ord.lt [c, a, b] [a, b, c] :=
    ord.lt_trans (by simpa using compat (ord := ord) [] [b] (D.swap_lt _ _ hca)) h2
  have g1 := D.jm (v := [a, b, c]) hca.le [b] [] (by simpa using h1)
  have g2 := D.jm (v := [a, b, c]) hcb.le [] [a] (by simpa using h3)
  have g3 := D.jm (v := [a, b, c]) hca.le [] [b] (by simpa using h2)
  have g4 := D.jm (v := [a, b, c]) hba.le [c] [] (by simpa using h4)
  rw [D.R_cross hca] at g1 g3
  rw [D.R_cross hcb] at g2
  rw [D.R_cross hba] at g4
  simp only [ofW_nil, one_mul, mul_one] at g1 g2 g3 g4
  have e : D.quad.overlapElt a b c - D.jacobi a b c =
      -(ofW [b] * (ofW [a, c] - (ofW [c, a] + D.π a c)))
        - (ofW [b, c] - (ofW [c, b] + D.π b c)) * ofW [a]
        + (ofW [a, c] - (ofW [c, a] + D.π a c)) * ofW [b]
        + ofW [c] * (ofW [a, b] - (ofW [b, a] + D.π a b)) := by
    simp only [QuadData.overlapElt, quad, jacobi, D.R_cross hba, D.R_cross hcb, mul_add,
      add_mul, sub_mul, mul_sub, ← ofW_append, List.cons_append, List.nil_append]
    abel
  rw [e]; exact ((g1.neg.sub g2).add g3).add g4

/-- **Thm. 1.9, composition step.** The four conditions give the triple-overlap
    condition of the block splay. -/
theorem overlapCondition_of (hA : D.AssocCondition) (hR : D.RightDerivCondition)
    (hL : D.LeftDerivCondition) (hJ : D.JacobiCondition) : D.quad.OverlapCondition := by
  intro a b c hab hbc
  change D.blk b ≤ D.blk a at hab
  change D.blk c ≤ D.blk b at hbc
  rcases lt_or_eq_of_le hab with hab' | hab' <;> rcases lt_or_eq_of_le hbc with hbc' | hbc'
  · have := (D.overlap_chain a b c hab' hbc').add (hJ a b c hab' hbc')
    rwa [sub_add_cancel] at this
  · have := (D.overlap_left a b c hab' hbc'.symm).add (hL a b c hab' hbc'.symm)
    rwa [sub_add_cancel] at this
  · have := (D.overlap_right a b c hab'.symm hbc').add (hR a b c hab'.symm hbc')
    rwa [sub_add_cancel] at this
  · have := (D.overlap_same a b c hab'.symm hbc'.symm).add (hA a b c hab'.symm hbc'.symm)
    rwa [sub_add_cancel] at this

/-- The normal words of a block splay are the **ordered monomials**: no two
    adjacent letters `a b` with `blk b ≤ blk a`, i.e. the blocks strictly increase. -/
theorem normalFormMonomial_iff (m : Monomial G) :
    NormalFormMonomial ord D.quad.sys m ↔
      ∀ a b : G, D.blk b ≤ D.blk a → ¬ [a, b] <:+: m := by
  rw [D.quad.normalFormMonomial_iff]
  exact ⟨fun h a b hab => h (a, b) hab, fun h p hp => h p.1 p.2 hp⟩

/-- **Thm. 1.9 of [leitner2006] (basis-presented coordinate algebras).** Under
    associativity of the block products, the two derivation conditions and the
    Jacobi condition, the ordered monomials form a `k`-basis of `U = T / J`. -/
theorem normalFormBasis [DecidableEq k] (hA : D.AssocCondition) (hR : D.RightDerivCondition)
    (hL : D.LeftDerivCondition) (hJ : D.JacobiCondition) : NormalFormBasis ord D.quad.sys :=
  D.quad.normalFormBasis (D.overlapCondition_of hA hR hL hJ)

end BlockData

end UGB.GrobnerShirshov.BlockSplay
