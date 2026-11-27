import UGB.GrobnerShirshov.Basic
import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.Algebra.FreeMonoid.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NoncommRing

set_option linter.unusedSectionVars false

/-!
# The Diamond Lemma, proved (Bergman 1978, Theorem 1.2)

For a Gröbner–Shirshov basis with **unit leading coefficients** over a
**commutative** ring, every element has a unique normal form, up to `CoeffEq`
(`reductionUnique`). This replaces the axiom `local_confluence`, which was
stated with a structurally equal common reduct and is false as stated
(`LocalConfluenceSupportRefutation`).

## The argument

Bergman's, adapted to this file's single-step relation.

1. **Operators** (§1). A step `f → g` is the operator `op s f = f − (f_w·lc⁻¹)·(a·rel·b)`
   at a site `s = (rule, a, b)` with `f_w ≠ 0`; at `f_w = 0` the operator is the
   identity. Operators are additive and `k`-linear, fix normal forms, and every
   reduction run is a sequence of them.
2. **Additivity** (§2, Bergman's Lemma 1.1). If `f` and `g` are reduction-unique,
   then every normal form of `f + g` is `NF(f) + NF(g)`. The proof pushes one
   operator sequence through both summands.
3. **The ideal below a word** (§4–§5). `JM v` is the `k`-span of the `a·rel·b`
   with `a·lm·b < v`. Assuming everything below `v` is reduction-unique, each
   element of `JM v` reduces to zero.
4. **Two reductions of one word** (§6–§7). Two first steps from the monomial `v`
   differ by an element of `JM v`. There are three cases by the position of the
   two leading words: disjoint (pure algebra), overlap and inclusion (the
   S-polynomial, which the GS hypothesis reduces to zero).
5. **Induction** (§8). By well-founded induction on `v`, every element whose live
   monomials are `≤ v` is reduction-unique.

## Why commutative

The S-polynomials are `lc₂·rel₁·C − lc₁·A·rel₂` (overlap) and
`lc_in·outer − lc_out·(x·inner·y)` (inclusion). They are unit multiples of the
monic compositions `ρ₁C − Aρ₂` only when `lc₁·lc₂ = lc₂·lc₁`.

## No quasi-zeros

The hypothesis `NoQuasiZerosFree`, which `local_confluence` carried, is not
used.

## References

- G. M. Bergman, *The diamond lemma for ring theory*, Adv. Math. 29 (1978).
-/

namespace UGB.GrobnerShirshov.Diamond

open UGB.GrobnerShirshov AlgElement

universe u v

variable {G : Type u} [DecidableEq G] {k : Type v} [CommRing k]

/-! ## §1  Reduction sites and the reduction operators -/

/-- A reduction site: a rule and a two-sided context. -/
structure Site (G : Type u) (k : Type v) [Ring k] where
  r : ReductionRule G k
  a : Monomial G
  b : Monomial G

variable (ord : AdmissibleOrder G) (sys : RewritingSystem G k)

/-- The word a site rewrites. -/
noncomputable def Site.word (s : Site G k) : Monomial G := s.a ++ s.r.lm ord ++ s.b

/-- The reduction operator at a site: subtract the multiple of `a·rel·b` that
    kills the coefficient of the site's word. It is the identity when that
    coefficient is already zero. -/
noncomputable def op (s : Site G k) (f : AlgElement G k) : AlgElement G k :=
  sub f (smul (f.coeff (s.word ord) * Ring.inverse (s.r.lc ord))
    (contextMul s.a s.r.relation s.b))

theorem op_coeff (s : Site G k) (f : AlgElement G k) (m : Monomial G) :
    (op ord s f).coeff m = f.coeff m -
      (f.coeff (s.word ord) * Ring.inverse (s.r.lc ord)) *
        (contextMul s.a s.r.relation s.b).coeff m := by
  simp [op]

variable {ord}

theorem ceq_refl (f : AlgElement G k) : CoeffEq f f := fun _ => rfl
theorem ceq_symm {f g : AlgElement G k} (h : CoeffEq f g) : CoeffEq g f :=
  fun m => (h m).symm
theorem ceq_trans {f g h : AlgElement G k} (h₁ : CoeffEq f g) (h₂ : CoeffEq g h) :
    CoeffEq f h := fun m => (h₁ m).trans (h₂ m)

theorem op_congr (s : Site G k) {f f' : AlgElement G k} (h : CoeffEq f f') :
    CoeffEq (op ord s f) (op ord s f') := by
  intro m; rw [op_coeff, op_coeff, h m, h (s.word ord)]

theorem op_add (s : Site G k) (f g : AlgElement G k) :
    CoeffEq (op ord s (add f g)) (add (op ord s f) (op ord s g)) := by
  intro m; simp only [op_coeff, add_coeff]; ring

theorem op_smul (s : Site G k) (c : k) (f : AlgElement G k) :
    CoeffEq (op ord s (smul c f)) (smul c (op ord s f)) := by
  intro m; simp only [op_coeff, smul_coeff]; ring

theorem op_of_coeff_zero (s : Site G k) {f : AlgElement G k}
    (h : f.coeff (s.word ord) = 0) : CoeffEq (op ord s f) f := by
  intro m; rw [op_coeff, h]; ring

theorem op_step {s : Site G k} (hs : s.r ∈ sys.rules) (hu : IsUnit (s.r.lc ord))
    {f : AlgElement G k} (hne : f.coeff (s.word ord) ≠ 0) :
    SingleStepReduction ord sys f (op ord s f) := by
  refine ⟨⟨s.r, hs, s.a, s.b, f.coeff (s.word ord) * Ring.inverse (s.r.lc ord),
    hne, ?_, fun _ => rfl⟩⟩
  rw [mul_assoc, Ring.inverse_mul_cancel _ hu, mul_one]
  rfl

variable {sys}

theorem step_eq_op (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f g : AlgElement G k} (h : SingleStepReduction ord sys f g) :
    ∃ s : Site G k, s.r ∈ sys.rules ∧ f.coeff (s.word ord) ≠ 0 ∧
      CoeffEq g (op ord s f) := by
  obtain ⟨r, hr, a, b, c, hne, hc, heq⟩ := h.exists_witness
  refine ⟨⟨r, a, b⟩, hr, hne, ?_⟩
  have hc' : c = f.coeff (a ++ r.lm ord ++ b) * Ring.inverse (r.lc ord) := by
    rw [← hc, mul_assoc, Ring.mul_inverse_cancel _ (hlc r hr), mul_one]
  intro m
  rw [heq m, op_coeff, sub_coeff, smul_coeff, hc']
  rfl

theorem isNormalForm_congr {f g : AlgElement G k} (h : CoeffEq f g)
    (hf : isNormalForm ord sys f) : isNormalForm ord sys g := by
  intro r hr m hm
  exact hf r hr m (by rw [h m]; exact hm)

theorem op_of_isNormalForm {s : Site G k} (hs : s.r ∈ sys.rules)
    {f : AlgElement G k} (hf : isNormalForm ord sys f) : CoeffEq (op ord s f) f := by
  apply op_of_coeff_zero
  by_contra hne
  exact hf s.r hs (s.word ord) hne ⟨s.a, s.b, rfl⟩

/-! ### Sequences of operators -/

variable (ord) in
/-- Apply a list of operators, left to right. -/
noncomputable def opseq (L : List (Site G k)) (f : AlgElement G k) : AlgElement G k :=
  L.foldl (fun g s => op ord s g) f

@[simp] theorem opseq_nil (f : AlgElement G k) : opseq ord [] f = f := rfl
@[simp] theorem opseq_cons (s : Site G k) (L : List (Site G k)) (f : AlgElement G k) :
    opseq ord (s :: L) f = opseq ord L (op ord s f) := rfl
theorem opseq_append (L₁ L₂ : List (Site G k)) (f : AlgElement G k) :
    opseq ord (L₁ ++ L₂) f = opseq ord L₂ (opseq ord L₁ f) := by
  simp [opseq, List.foldl_append]

theorem opseq_congr (L : List (Site G k)) {f f' : AlgElement G k} (h : CoeffEq f f') :
    CoeffEq (opseq ord L f) (opseq ord L f') := by
  induction L generalizing f f' with
  | nil => exact h
  | cons s L ih => exact ih (op_congr s h)

theorem opseq_add (L : List (Site G k)) (f g : AlgElement G k) :
    CoeffEq (opseq ord L (add f g)) (add (opseq ord L f) (opseq ord L g)) := by
  induction L generalizing f g with
  | nil => exact ceq_refl _
  | cons s L ih => exact ceq_trans (opseq_congr L (op_add s f g)) (ih _ _)

theorem opseq_smul (L : List (Site G k)) (c : k) (f : AlgElement G k) :
    CoeffEq (opseq ord L (smul c f)) (smul c (opseq ord L f)) := by
  induction L generalizing f with
  | nil => exact ceq_refl _
  | cons s L ih => exact ceq_trans (opseq_congr L (op_smul s c f)) (ih _)

theorem opseq_of_isNormalForm {L : List (Site G k)} (hL : ∀ s ∈ L, s.r ∈ sys.rules)
    {f : AlgElement G k} (hf : isNormalForm ord sys f) : CoeffEq (opseq ord L f) f := by
  induction L generalizing f with
  | nil => exact ceq_refl _
  | cons s L ih =>
    have h1 := op_of_isNormalForm (hL s (by simp)) hf
    exact ceq_trans (ih (fun t ht => hL t (by simp [ht]))
      (isNormalForm_congr (ceq_symm h1) hf)) h1

variable (sys) in
theorem reach (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (L : List (Site G k)) (hL : ∀ s ∈ L, s.r ∈ sys.rules) (f : AlgElement G k) :
    ∃ h, MultiStepReduction ord sys f h ∧ CoeffEq h (opseq ord L f) := by
  induction L generalizing f with
  | nil => exact ⟨f, MultiStepReduction.refl f, ceq_refl _⟩
  | cons s L ih =>
    have hL' : ∀ t ∈ L, t.r ∈ sys.rules := fun t ht => hL t (by simp [ht])
    by_cases hz : f.coeff (s.word ord) = 0
    · obtain ⟨h, hm, hce⟩ := ih hL' f
      exact ⟨h, hm, ceq_trans hce (opseq_congr L (ceq_symm (op_of_coeff_zero s hz)))⟩
    · obtain ⟨h, hm, hce⟩ := ih hL' (op ord s f)
      exact ⟨h, MultiStepReduction.head (op_step sys (hL s (by simp))
        (hlc _ (hL s (by simp))) hz) hm, hce⟩

theorem toOps (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f g : AlgElement G k} (h : MultiStepReduction ord sys f g) :
    ∃ L : List (Site G k), (∀ s ∈ L, s.r ∈ sys.rules) ∧ CoeffEq g (opseq ord L f) := by
  induction h with
  | refl => exact ⟨[], by simp, ceq_refl _⟩
  | step _ hgh ih =>
    obtain ⟨L, hL, hg⟩ := ih
    obtain ⟨s, hs, -, hh⟩ := step_eq_op hlc hgh
    refine ⟨L ++ [s], ?_, ?_⟩
    · intro t ht
      rcases List.mem_append.mp ht with h | h
      · exact hL t h
      · simp at h; exact h ▸ hs
    · rw [opseq_append]
      exact ceq_trans hh (op_congr s hg)

/-! ## §2  Reduction-uniqueness, and why it is additive -/

variable (ord sys) in
/-- `f` is **reduction-unique**: all its normal forms agree coefficientwise. -/
def RU (f : AlgElement G k) : Prop :=
  ∀ n₁ n₂, ReducesToNF ord sys f n₁ → ReducesToNF ord sys f n₂ → CoeffEq n₁ n₂

theorem nf_of_congr (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f f' n : AlgElement G k} (hff : CoeffEq f f') (hn : ReducesToNF ord sys f' n) :
    ∃ n', ReducesToNF ord sys f n' ∧ CoeffEq n' n := by
  obtain ⟨L, hL, hnL⟩ := toOps hlc hn.reduces
  obtain ⟨h, hm, hh⟩ := reach sys hlc L hL f
  have hhn : CoeffEq h n := ceq_trans hh (ceq_trans (opseq_congr L hff) (ceq_symm hnL))
  exact ⟨h, ⟨hm, isNormalForm_congr (ceq_symm hhn) hn.is_normal⟩, hhn⟩

theorem RU_congr (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f f' : AlgElement G k} (hff : CoeffEq f f') (hf : RU ord sys f) : RU ord sys f' := by
  intro n₁ n₂ h₁ h₂
  obtain ⟨m₁, hm₁, e₁⟩ := nf_of_congr hlc hff h₁
  obtain ⟨m₂, hm₂, e₂⟩ := nf_of_congr hlc hff h₂
  exact ceq_trans (ceq_symm e₁) (ceq_trans (hf _ _ hm₁ hm₂) e₂)

theorem RU_of_isNormalForm {f : AlgElement G k} (hf : isNormalForm ord sys f) :
    RU ord sys f := by
  intro n₁ n₂ h₁ h₂
  rw [MultiStepReduction.eq_of_isNormalForm hf h₁.reduces,
    MultiStepReduction.eq_of_isNormalForm hf h₂.reduces]
  exact ceq_refl _

theorem isNormalForm_of_isZero {f : AlgElement G k} (hf : f.isZero) :
    isNormalForm ord sys f := fun _ _ m hm => absurd (hf m) hm

/-- **Bergman's Lemma 1.1, additive half.** Normal forms of reduction-unique
    elements add. -/
theorem nf_add (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f g n nf ng : AlgElement G k} (hf : RU ord sys f) (hg : RU ord sys g)
    (hn : ReducesToNF ord sys (add f g) n) (hnf : ReducesToNF ord sys f nf)
    (hng : ReducesToNF ord sys g ng) : CoeffEq n (add nf ng) := by
  obtain ⟨L, hL, hnL⟩ := toOps hlc hn.reduces
  obtain ⟨h₁, hm₁, hh₁⟩ := reach sys hlc L hL f
  obtain ⟨n₁, hn₁⟩ := normal_form_exists ord sys hlc h₁
  have e₁ : CoeffEq n₁ nf := hf _ _ ⟨hm₁.trans hn₁.reduces, hn₁.is_normal⟩ hnf
  obtain ⟨L₁, hL₁, hn₁L⟩ := toOps hlc hn₁.reduces
  have hLL₁ : ∀ s ∈ L ++ L₁, s.r ∈ sys.rules := by
    intro s hs; rcases List.mem_append.mp hs with h | h
    · exact hL s h
    · exact hL₁ s h
  obtain ⟨h₂, hm₂, hh₂⟩ := reach sys hlc (L ++ L₁) hLL₁ g
  obtain ⟨n₂, hn₂⟩ := normal_form_exists ord sys hlc h₂
  have e₂ : CoeffEq n₂ ng := hg _ _ ⟨hm₂.trans hn₂.reduces, hn₂.is_normal⟩ hng
  obtain ⟨L₂, hL₂, hn₂L⟩ := toOps hlc hn₂.reduces
  have hL₁₂ : ∀ s ∈ L₁ ++ L₂, s.r ∈ sys.rules := by
    intro s hs; rcases List.mem_append.mp hs with h | h
    · exact hL₁ s h
    · exact hL₂ s h
  -- `n` is fixed by the later operators
  have s0 : CoeffEq n (opseq ord (L₁ ++ L₂) n) :=
    ceq_symm (opseq_of_isNormalForm hL₁₂ hn.is_normal)
  have s1 : CoeffEq (opseq ord (L₁ ++ L₂) n)
      (opseq ord L₂ (opseq ord L₁ (opseq ord L (add f g)))) := by
    rw [← opseq_append]; exact opseq_congr _ hnL
  have s2 : CoeffEq (opseq ord L₂ (opseq ord L₁ (opseq ord L (add f g))))
      (add (opseq ord L₂ (opseq ord L₁ (opseq ord L f)))
        (opseq ord L₂ (opseq ord L₁ (opseq ord L g)))) := by
    have := opseq_add (ord := ord) (L ++ L₁ ++ L₂) f g
    simpa only [opseq_append] using this
  have s3 : CoeffEq (opseq ord L₂ (opseq ord L₁ (opseq ord L f))) nf := by
    refine ceq_trans (opseq_congr L₂ (opseq_congr L₁ (ceq_symm hh₁))) ?_
    refine ceq_trans (opseq_congr L₂ (ceq_symm hn₁L)) ?_
    exact ceq_trans (opseq_of_isNormalForm hL₂ hn₁.is_normal) e₁
  have s4 : CoeffEq (opseq ord L₂ (opseq ord L₁ (opseq ord L g))) ng := by
    rw [← opseq_append (ord := ord) L L₁ g]
    refine ceq_trans (opseq_congr L₂ (ceq_symm hh₂)) ?_
    exact ceq_trans (ceq_symm hn₂L) e₂
  intro m
  rw [s0 m, s1 m, s2 m, add_coeff, add_coeff, s3 m, s4 m]

/-- **Bergman's Lemma 1.1, scalar half.** -/
theorem nf_smul (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f n nf : AlgElement G k} (c : k) (hf : RU ord sys f)
    (hn : ReducesToNF ord sys (smul c f) n) (hnf : ReducesToNF ord sys f nf) :
    CoeffEq n (smul c nf) := by
  obtain ⟨L, hL, hnL⟩ := toOps hlc hn.reduces
  obtain ⟨h₁, hm₁, hh₁⟩ := reach sys hlc L hL f
  obtain ⟨n₁, hn₁⟩ := normal_form_exists ord sys hlc h₁
  have e₁ : CoeffEq n₁ nf := hf _ _ ⟨hm₁.trans hn₁.reduces, hn₁.is_normal⟩ hnf
  obtain ⟨L₁, hL₁, hn₁L⟩ := toOps hlc hn₁.reduces
  have s0 : CoeffEq n (opseq ord L₁ n) := ceq_symm (opseq_of_isNormalForm hL₁ hn.is_normal)
  have s1 : CoeffEq (opseq ord L₁ n) (smul c (opseq ord L₁ (opseq ord L f))) :=
    ceq_trans (opseq_congr L₁ hnL) (by
      rw [← opseq_append (ord := ord) L L₁ (smul c f), ← opseq_append (ord := ord) L L₁ f]
      exact opseq_smul _ _ _)
  have s2 : CoeffEq (opseq ord L₁ (opseq ord L f)) nf :=
    ceq_trans (opseq_congr L₁ (ceq_symm hh₁)) (ceq_trans (ceq_symm hn₁L) e₁)
  intro m
  rw [s0 m, s1 m, smul_coeff, smul_coeff, s2 m]

theorem RU_add (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f g : AlgElement G k} (hf : RU ord sys f) (hg : RU ord sys g) :
    RU ord sys (add f g) := by
  intro n₁ n₂ h₁ h₂
  obtain ⟨nf, hnf⟩ := normal_form_exists ord sys hlc f
  obtain ⟨ng, hng⟩ := normal_form_exists ord sys hlc g
  exact ceq_trans (nf_add hlc hf hg h₁ hnf hng) (ceq_symm (nf_add hlc hf hg h₂ hnf hng))

theorem RU_smul (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f : AlgElement G k} (c : k) (hf : RU ord sys f) : RU ord sys (smul c f) := by
  intro n₁ n₂ h₁ h₂
  obtain ⟨nf, hnf⟩ := normal_form_exists ord sys hlc f
  exact ceq_trans (nf_smul hlc c hf h₁ hnf) (ceq_symm (nf_smul hlc c hf h₂ hnf))

variable (ord sys) in
/-- `f` reduces to a normal form that is zero. -/
def ZeroNF (f : AlgElement G k) : Prop := ∃ n, ReducesToNF ord sys f n ∧ n.isZero

theorem zeroNF_of_isZero {f : AlgElement G k} (hf : f.isZero) : ZeroNF ord sys f :=
  ⟨f, ⟨MultiStepReduction.refl f, isNormalForm_of_isZero hf⟩, hf⟩

theorem zeroNF_congr (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f f' : AlgElement G k} (hff : CoeffEq f f') (h : ZeroNF ord sys f') :
    ZeroNF ord sys f := by
  obtain ⟨n, hn, hz⟩ := h
  obtain ⟨n', hn', e⟩ := nf_of_congr hlc hff hn
  exact ⟨n', hn', fun m => (e m).trans (hz m)⟩

theorem zeroNF_add (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f g : AlgElement G k} (hf : RU ord sys f) (hg : RU ord sys g)
    (hf0 : ZeroNF ord sys f) (hg0 : ZeroNF ord sys g) : ZeroNF ord sys (add f g) := by
  obtain ⟨nf, hnf, hzf⟩ := hf0
  obtain ⟨ng, hng, hzg⟩ := hg0
  obtain ⟨n, hn⟩ := normal_form_exists ord sys hlc (add f g)
  refine ⟨n, hn, fun m => ?_⟩
  rw [nf_add hlc hf hg hn hnf hng m, add_coeff, hzf m, hzg m, add_zero]

theorem zeroNF_smul (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {f : AlgElement G k} (c : k) (hf : RU ord sys f) (hf0 : ZeroNF ord sys f) :
    ZeroNF ord sys (smul c f) := by
  obtain ⟨nf, hnf, hzf⟩ := hf0
  obtain ⟨n, hn⟩ := normal_form_exists ord sys hlc (smul c f)
  refine ⟨n, hn, fun m => ?_⟩
  rw [nf_smul hlc c hf hn hnf m, smul_coeff, hzf m, mul_zero]

/-! ## §3  The free-algebra picture: `toMA` into `MonoidAlgebra k (FreeMonoid G)` -/

variable (G k) in
/-- The free algebra, as Mathlib's monoid algebra on the free monoid. -/
abbrev MA := MonoidAlgebra k (FreeMonoid G)

/-- The basis element of a word. -/
noncomputable def ofW (w : Monomial G) : MA G k :=
  MonoidAlgebra.single (FreeMonoid.ofList w) 1

theorem ofW_append (x y : Monomial G) : (ofW (x ++ y) : MA G k) = ofW x * ofW y := by
  simp [ofW, MonoidAlgebra.single_mul_single, FreeMonoid.ofList_append]

/-- Coefficient function of an element, as a monoid-algebra element. -/
noncomputable def toMA (f : AlgElement G k) : MA G k :=
  ∑ m ∈ f.support, MonoidAlgebra.single (FreeMonoid.ofList m) (f.coeff m)

theorem toMA_apply (f : AlgElement G k) (m : Monomial G) :
    toMA f (FreeMonoid.ofList m) = f.coeff m := by
  classical
  unfold toMA
  rw [Finsupp.finset_sum_apply]
  have : ∀ m' ∈ f.support, (MonoidAlgebra.single (FreeMonoid.ofList m') (f.coeff m'))
      (FreeMonoid.ofList m) = if m' = m then f.coeff m' else 0 := by
    intro m' _
    rw [MonoidAlgebra.single_apply]
    by_cases h : m' = m
    · subst h; simp
    · rw [if_neg (fun h' => h (FreeMonoid.ofList.injective h')), if_neg h]
  rw [Finset.sum_congr rfl this, Finset.sum_ite_eq']
  split_ifs with h
  · rfl
  · exact (f.support_spec m h).symm

theorem toMA_ext {F H : MA G k} (h : ∀ m : Monomial G, F (FreeMonoid.ofList m) = H (FreeMonoid.ofList m)) :
    F = H := by
  apply MonoidAlgebra.ext
  intro x
  rw [← FreeMonoid.ofList_toList x]
  exact h _

theorem toMA_eq_of_ceq {f g : AlgElement G k} (h : CoeffEq f g) : toMA f = toMA g :=
  toMA_ext (fun m => by rw [toMA_apply, toMA_apply, h m])

theorem ceq_of_toMA_eq {f g : AlgElement G k} (h : toMA f = toMA g) : CoeffEq f g := by
  intro m; rw [← toMA_apply, ← toMA_apply, h]

theorem toMA_add (f g : AlgElement G k) : toMA (add f g) = toMA f + toMA g :=
  toMA_ext (fun m => by simp [toMA_apply])

theorem toMA_smul (c : k) (f : AlgElement G k) : toMA (smul c f) = c • toMA f :=
  toMA_ext (fun m => by simp [toMA_apply])

theorem toMA_sub (f g : AlgElement G k) : toMA (sub f g) = toMA f - toMA g := by
  rw [eq_sub_iff_add_eq, ← toMA_add]
  apply toMA_eq_of_ceq
  intro m; simp

theorem ofW_apply (w m : Monomial G) :
    (ofW w : MA G k) (FreeMonoid.ofList m) = if w = m then 1 else 0 := by
  classical
  rw [ofW, MonoidAlgebra.single_apply]
  by_cases h : w = m
  · simp [h]
  · rw [if_neg (fun h' => h (FreeMonoid.ofList.injective h')), if_neg h]

/-- The support of `toMA f` sits inside `f.support`. -/
theorem toMA_eq_sum (f : AlgElement G k) :
    toMA f = ∑ m ∈ f.support, f.coeff m • (ofW m : MA G k) := by
  unfold toMA ofW
  refine Finset.sum_congr rfl (fun m _ => ?_)
  rw [MonoidAlgebra.smul_single', mul_one]

theorem toMA_contextMul (a b : Monomial G) (f : AlgElement G k) :
    toMA (contextMul a f b) = ofW a * toMA f * ofW b := by
  classical
  have hinj : Function.Injective (fun w : Monomial G => a ++ w ++ b) := by
    intro x y h; simpa using h
  rw [toMA_eq_sum (contextMul a f b), toMA_eq_sum f, Finset.mul_sum, Finset.sum_mul]
  show ∑ m ∈ f.support.image (fun w => a ++ w ++ b), _ = _
  rw [Finset.sum_image (fun x _ y _ h => hinj h)]
  refine Finset.sum_congr rfl (fun m _ => ?_)
  rw [contextMul_coeff_middle, mul_smul_comm, smul_mul_assoc, ← ofW_append, ← ofW_append]

/-- The element with a given monoid-algebra coefficient function. -/
noncomputable def ofMA (F : MA G k) : AlgElement G k where
  coeff := fun m => F (FreeMonoid.ofList m)
  support := F.support.image FreeMonoid.toList
  support_spec := by
    intro m hm
    by_contra h
    exact hm (Finset.mem_image.mpr ⟨FreeMonoid.ofList m, Finsupp.mem_support_iff.mpr h,
      FreeMonoid.toList_ofList m⟩)

theorem toMA_ofMA (F : MA G k) : toMA (ofMA F) = F :=
  toMA_ext (fun m => by rw [toMA_apply]; rfl)

theorem ceq_ofMA_toMA (f : AlgElement G k) : CoeffEq f (ofMA (toMA f)) := by
  intro m; show f.coeff m = toMA f (FreeMonoid.ofList m); rw [toMA_apply]

theorem ofMA_add (F H : MA G k) : CoeffEq (ofMA (F + H)) (add (ofMA F) (ofMA H)) :=
  ceq_of_toMA_eq (by rw [toMA_add, toMA_ofMA, toMA_ofMA, toMA_ofMA])

theorem ofMA_smul (c : k) (F : MA G k) : CoeffEq (ofMA (c • F)) (smul c (ofMA F)) :=
  ceq_of_toMA_eq (by rw [toMA_smul, toMA_ofMA, toMA_ofMA])

theorem ofMA_zero : (ofMA (0 : MA G k)).isZero := fun _ => rfl

theorem ofMA_ctx (a b : Monomial G) (f : AlgElement G k) :
    CoeffEq (ofMA (ofW a * toMA f * ofW b)) (contextMul a f b) :=
  ceq_of_toMA_eq (by rw [toMA_ofMA, toMA_contextMul])

/-! ## §4  The ideal below a word -/

variable (ord) in
/-- All live monomials of `f` lie strictly below `v`. -/
def Below (v : Monomial G) (f : AlgElement G k) : Prop :=
  ∀ m, f.coeff m ≠ 0 → ord.lt m v

theorem below_congr {v : Monomial G} {f g : AlgElement G k} (h : CoeffEq f g)
    (hf : Below ord v f) : Below ord v g := fun m hm => hf m (by rw [h m]; exact hm)

theorem compat (x y : Monomial G) {p q : Monomial G} (h : ord.lt p q) :
    ord.lt (x ++ p ++ y) (x ++ q ++ y) :=
  ord.right_compat _ _ y (ord.left_compat _ _ x h)

/-- Every live monomial of a rule's relation is at or below its leading monomial. -/
theorem le_lm (r : ReductionRule G k) {m : Monomial G} (hm : r.relation.coeff m ≠ 0) :
    m = r.lm ord ∨ ord.lt m (r.lm ord) := by
  by_cases h : m = r.lm ord
  · exact Or.inl h
  · exact Or.inr (lt_leadingMonomial_of_coeff_ne_zero ord r.relation r.nonzero hm h)

theorem ctx_le_word (s : Site G k) {m : Monomial G}
    (hm : (contextMul s.a s.r.relation s.b).coeff m ≠ 0) :
    m = s.word ord ∨ ord.lt m (s.word ord) := by
  obtain ⟨m', rfl, hm'⟩ := contextMul_shape hm
  rcases le_lm s.r hm' with h | h
  · left; rw [h]; rfl
  · exact Or.inr (compat s.a s.b h)

variable (ord sys) in
/-- The left `k`-span of the `a·rel·b` whose word lies strictly below `v`. -/
inductive JM (v : Monomial G) : MA G k → Prop
  | gen (s : Site G k) (hs : s.r ∈ sys.rules) (hlt : ord.lt (s.word ord) v) :
      JM v (ofW s.a * toMA s.r.relation * ofW s.b)
  | zero : JM v 0
  | add {F H : MA G k} : JM v F → JM v H → JM v (F + H)
  | smul (c : k) {F : MA G k} : JM v F → JM v (c • F)

theorem JM.neg {v : Monomial G} {F : MA G k} (h : JM ord sys v F) : JM ord sys v (-F) := by
  have := JM.smul (-1 : k) h; rwa [neg_one_smul] at this

theorem JM.sub {v : Monomial G} {F H : MA G k} (hF : JM ord sys v F) (hH : JM ord sys v H) :
    JM ord sys v (F - H) := by
  rw [sub_eq_add_neg]; exact JM.add hF hH.neg

theorem JM.sum {v : Monomial G} {ι : Type*} (s : Finset ι) (F : ι → MA G k)
    (h : ∀ i ∈ s, JM ord sys v (F i)) : JM ord sys v (∑ i ∈ s, F i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using (JM.zero : JM ord sys v 0)
  | insert i s hi ih =>
    rw [Finset.sum_insert hi]
    exact JM.add (h i (Finset.mem_insert_self _ _))
      (ih (fun j hj => h j (Finset.mem_insert_of_mem hj)))

theorem JM.isBelow {v : Monomial G} {F : MA G k} (h : JM ord sys v F) :
    Below ord v (ofMA F) := by
  induction h with
  | gen s _ hlt =>
    refine below_congr (ceq_symm (ofMA_ctx s.a s.b s.r.relation)) ?_
    intro m hm
    rcases ctx_le_word s hm with h | h
    · rw [h]; exact hlt
    · exact ord.lt_trans h hlt
  | zero => exact fun m hm => absurd (ofMA_zero m) hm
  | @add F H _ _ ihF ihH =>
    refine below_congr (ceq_symm (ofMA_add F H)) ?_
    intro m hm
    rw [add_coeff] at hm
    by_cases hF : (ofMA F).coeff m = 0
    · rw [hF, zero_add] at hm; exact ihH m hm
    · exact ihF m hF
  | smul c _ ih =>
    refine below_congr (ceq_symm (ofMA_smul _ _)) ?_
    intro m hm
    rw [smul_coeff] at hm
    exact ih m (fun h0 => hm (by rw [h0, mul_zero]))

theorem zeroNF_ctx (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) (s : Site G k)
    (hs : s.r ∈ sys.rules) : ZeroNF ord sys (contextMul s.a s.r.relation s.b) := by
  have hu := hlc s.r hs
  have hw : (contextMul s.a s.r.relation s.b).coeff (s.word ord) = s.r.lc ord :=
    contextMul_coeff_middle _ _ _ _
  by_cases h0 : s.r.lc ord = 0
  · have h10 : (1 : k) = 0 := by
      rw [← Ring.inverse_mul_cancel _ hu, h0, mul_zero]
    apply zeroNF_of_isZero
    intro m; rw [← mul_one ((contextMul _ _ _).coeff m), h10, mul_zero]
  · have hstep := op_step sys hs hu (f := contextMul s.a s.r.relation s.b) (by rw [hw]; exact h0)
    have hz : (op ord s (contextMul s.a s.r.relation s.b)).isZero := by
      intro m
      rw [op_coeff, hw, Ring.mul_inverse_cancel _ hu, one_mul, sub_self]
    exact ⟨_, ⟨MultiStepReduction.head hstep (MultiStepReduction.refl _),
      isNormalForm_of_isZero hz⟩, hz⟩

theorem JM.zeroNF (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) {v : Monomial G}
    (hbelow : ∀ f, Below ord v f → RU ord sys f) {F : MA G k} (h : JM ord sys v F) :
    ZeroNF ord sys (ofMA F) := by
  induction h with
  | gen s hs _ => exact zeroNF_congr hlc (ofMA_ctx _ _ _) (zeroNF_ctx hlc s hs)
  | zero => exact zeroNF_of_isZero ofMA_zero
  | add hF hH ihF ihH =>
    exact zeroNF_congr hlc (ofMA_add _ _)
      (zeroNF_add hlc (hbelow _ hF.isBelow) (hbelow _ hH.isBelow) ihF ihH)
  | smul c hF ih =>
    exact zeroNF_congr hlc (ofMA_smul _ _) (zeroNF_smul hlc c (hbelow _ hF.isBelow) ih)

/-! ## §5  Monic relations, and three ways to land in the ideal -/

variable (ord) in
/-- The monic form of a rule, `lc⁻¹ • rel`. -/
noncomputable def rho (r : ReductionRule G k) : MA G k :=
  Ring.inverse (r.lc ord) • toMA r.relation

variable (ord) in
/-- The tail of the monic form, `rho r − lm(r)`. -/
noncomputable def tail (r : ReductionRule G k) : MA G k := rho ord r - ofW (r.lm ord)

theorem ofW_nil : (ofW [] : MA G k) = 1 := rfl

theorem toMA_of_isZero {f : AlgElement G k} (hf : f.isZero) : toMA f = 0 :=
  toMA_ext (fun m => by rw [toMA_apply, hf m]; rfl)

theorem tail_support (r : ReductionRule G k) (hu : IsUnit (r.lc ord))
    {p : FreeMonoid G} (hp : p ∈ (tail ord r).support) :
    ord.lt (FreeMonoid.toList p) (r.lm ord) := by
  rw [Finsupp.mem_support_iff, ← FreeMonoid.ofList_toList p] at hp
  set q := FreeMonoid.toList p
  have hval : (tail ord r) (FreeMonoid.ofList q) =
      Ring.inverse (r.lc ord) * r.relation.coeff q - (if r.lm ord = q then 1 else 0) := by
    unfold tail rho
    rw [Finsupp.sub_apply, ofW_apply]
    simp [toMA_apply]
  rw [hval] at hp
  by_cases hq : r.lm ord = q
  · exfalso; apply hp
    rw [if_pos hq, ← hq]
    show Ring.inverse (r.lc ord) * r.lc ord - 1 = 0
    rw [Ring.inverse_mul_cancel _ hu, sub_self]
  · rw [if_neg hq, sub_zero] at hp
    rcases le_lm r (fun h0 => hp (by rw [h0, mul_zero])) with h | h
    · exact absurd h.symm hq
    · exact h

/-- Every element of the monoid algebra is the sum of its terms. -/
theorem ma_eq_sum (F : MA G k) :
    F = ∑ p ∈ F.support, F p • (ofW (FreeMonoid.toList p) : MA G k) := by
  conv_lhs => rw [← Finsupp.sum_single F]
  unfold Finsupp.sum ofW
  refine Finset.sum_congr rfl (fun p _ => ?_)
  rw [MonoidAlgebra.smul_single', mul_one, FreeMonoid.ofList_toList]

theorem JM_left {r : ReductionRule G k} (hr : r ∈ sys.rules) {v x m y : Monomial G} (F : MA G k)
    (hF : ∀ p ∈ F.support, ord.lt (x ++ FreeMonoid.toList p ++ m ++ r.lm ord ++ y) v) :
    JM ord sys v (ofW x * F * ofW m * rho ord r * ofW y) := by
  rw [ma_eq_sum F, Finset.mul_sum, Finset.sum_mul, Finset.sum_mul, Finset.sum_mul]
  refine JM.sum _ _ (fun p hp => ?_)
  have e : ofW x * (F p • (ofW (FreeMonoid.toList p) : MA G k)) * ofW m * rho ord r * ofW y
      = (F p * Ring.inverse (r.lc ord)) •
          (ofW (x ++ FreeMonoid.toList p ++ m) * toMA r.relation * ofW y) := by
    simp only [rho, mul_smul_comm, smul_mul_assoc, smul_smul, ofW_append, mul_assoc]
    rw [mul_comm (Ring.inverse _)]
  rw [e]
  refine JM.smul _ (JM.gen ⟨r, x ++ FreeMonoid.toList p ++ m, y⟩ hr ?_)
  simpa [Site.word, List.append_assoc] using hF p hp

theorem JM_right {r : ReductionRule G k} (hr : r ∈ sys.rules) {v x m y : Monomial G} (F : MA G k)
    (hF : ∀ p ∈ F.support, ord.lt (x ++ r.lm ord ++ m ++ FreeMonoid.toList p ++ y) v) :
    JM ord sys v (ofW x * rho ord r * ofW m * F * ofW y) := by
  rw [ma_eq_sum F, Finset.mul_sum, Finset.sum_mul]
  refine JM.sum _ _ (fun p hp => ?_)
  have e : ofW x * rho ord r * ofW m * (F p • (ofW (FreeMonoid.toList p) : MA G k)) * ofW y
      = (F p * Ring.inverse (r.lc ord)) •
          (ofW x * toMA r.relation * ofW (m ++ FreeMonoid.toList p ++ y)) := by
    simp only [rho, mul_smul_comm, smul_mul_assoc, smul_smul, ofW_append, mul_assoc]
  rw [e]
  refine JM.smul _ (JM.gen ⟨r, x, m ++ FreeMonoid.toList p ++ y⟩ hr ?_)
  simpa [Site.word, List.append_assoc] using hF p hp

/-- A step keeps everything strictly below `u`. -/
theorem below_step {u : Monomial G} {g h : AlgElement G k}
    (hstep : SingleStepReduction ord sys g h) (hg : Below ord u g) : Below ord u h := by
  obtain ⟨r, _, a, b, c, hne, _, heq⟩ := hstep.exists_witness
  have hw := hg _ hne
  intro m hm
  rw [heq m, sub_coeff, smul_coeff] at hm
  by_cases hgm : g.coeff m = 0
  · rw [hgm, zero_sub] at hm
    have hc : (contextMul a r.relation b).coeff m ≠ 0 := fun h0 => hm (by rw [h0, mul_zero, neg_zero])
    rcases ctx_le_word (ord := ord) ⟨r, a, b⟩ hc with h | h
    · rw [h]; exact hw
    · exact ord.lt_trans h hw
  · exact hg m hgm

/-- A reduction run, put in context, lands in the ideal below `v`. -/
theorem JM_of_multistep {u v : Monomial G} (a b : Monomial G)
    (hcomp : ∀ m, ord.lt m u → ord.lt (a ++ m ++ b) v) {f n : AlgElement G k}
    (h : MultiStepReduction ord sys f n) (hf : Below ord u f) :
    Below ord u n ∧ JM ord sys v (ofW a * (toMA f - toMA n) * ofW b) := by
  induction h with
  | refl => exact ⟨hf, by rw [sub_self, mul_zero, zero_mul]; exact JM.zero⟩
  | @step g h _ hgh ih =>
    obtain ⟨hbg, hJ⟩ := ih
    refine ⟨below_step hgh hbg, ?_⟩
    obtain ⟨r, hr, a', b', c, hne, _, heq⟩ := hgh.exists_witness
    have hh : toMA h = toMA g - c • (ofW a' * toMA r.relation * ofW b') := by
      rw [toMA_eq_of_ceq heq, toMA_sub, toMA_smul, toMA_contextMul]
    have e : ofW a * (toMA f - toMA h) * ofW b =
        ofW a * (toMA f - toMA g) * ofW b +
          c • (ofW (a ++ a') * toMA r.relation * ofW (b' ++ b)) := by
      rw [hh]
      simp only [ofW_append, mul_sub, sub_mul, mul_smul_comm,
        smul_mul_assoc, mul_assoc]
      abel
    rw [e]
    refine JM.add hJ (JM.smul c (JM.gen ⟨r, a ++ a', b' ++ b⟩ hr ?_))
    have := hcomp _ (hbg _ hne)
    simpa [Site.word, List.append_assoc] using this

/-! ## §6  Two reductions of one word differ by an element of the ideal below it -/

variable (ord) in
/-- The difference of the two monic reductions at `s₁` and `s₂`. -/
noncomputable def D (s₁ s₂ : Site G k) : MA G k :=
  ofW s₂.a * rho ord s₂.r * ofW s₂.b - ofW s₁.a * rho ord s₁.r * ofW s₁.b

theorem D_swap (s₁ s₂ : Site G k) : D ord s₂ s₁ = -D ord s₁ s₂ := by
  unfold D; abel

theorem toMA_spoly_ov (oc : OverlapComposition G k ord) :
    toMA oc.spoly = oc.rule₂.lc ord • (toMA oc.rule₁.relation * ofW oc.right) -
      oc.rule₁.lc ord • (ofW oc.left * toMA oc.rule₂.relation) := by
  simp only [OverlapComposition.spoly, toMA_sub, toMA_smul, toMA_contextMul, ofW_nil,
    one_mul, mul_one]

theorem toMA_spoly_inc (ic : InclusionComposition G k ord) :
    toMA ic.spoly = ic.inner.lc ord • toMA ic.outer.relation -
      ic.outer.lc ord • (ofW ic.left * toMA ic.inner.relation * ofW ic.right) := by
  simp only [InclusionComposition.spoly, toMA_sub, toMA_smul, toMA_contextMul]

theorem below_spoly_ov (oc : OverlapComposition G k ord) :
    Below ord oc.word oc.spoly := by
  intro m hm
  have hw₁ : ([] : Monomial G) ++ oc.rule₁.lm ord ++ oc.right = oc.word := by
    simp [OverlapComposition.word, oc.lm₁_decomp]
  have hw₂ : oc.left ++ oc.rule₂.lm ord ++ [] = oc.word := by
    simp [OverlapComposition.word, oc.lm₂_decomp, List.append_assoc]
  by_cases hmw : m = oc.word
  · exfalso; apply hm; rw [hmw, OverlapComposition.spoly_coeff_word, mul_comm, sub_self]
  simp only [OverlapComposition.spoly, sub_coeff, smul_coeff] at hm
  by_cases h₁ : (contextMul [] oc.rule₁.relation oc.right).coeff m = 0
  · rw [h₁, mul_zero, zero_sub] at hm
    have h₂ : (contextMul oc.left oc.rule₂.relation []).coeff m ≠ 0 :=
      fun h0 => hm (by rw [h0, mul_zero, neg_zero])
    rcases ctx_le_word (ord := ord) ⟨oc.rule₂, oc.left, []⟩ h₂ with h | h
    · exact absurd (h.trans hw₂) hmw
    · exact hw₂ ▸ h
  · rcases ctx_le_word (ord := ord) ⟨oc.rule₁, [], oc.right⟩ h₁ with h | h
    · exact absurd (h.trans hw₁) hmw
    · exact hw₁ ▸ h

theorem below_spoly_inc (ic : InclusionComposition G k ord) :
    Below ord (ic.outer.lm ord) ic.spoly := by
  intro m hm
  by_cases hmw : m = ic.outer.lm ord
  · exfalso; apply hm; rw [hmw, InclusionComposition.spoly_coeff_lm, mul_comm, sub_self]
  simp only [InclusionComposition.spoly, sub_coeff, smul_coeff] at hm
  by_cases h₁ : ic.outer.relation.coeff m = 0
  · rw [h₁, mul_zero, zero_sub] at hm
    have h₂ : (contextMul ic.left ic.inner.relation ic.right).coeff m ≠ 0 :=
      fun h0 => hm (by rw [h0, mul_zero, neg_zero])
    rcases ctx_le_word (ord := ord) ⟨ic.inner, ic.left, ic.right⟩ h₂ with h | h
    · exact absurd (h.trans ic.decomposition.symm) hmw
    · exact ic.decomposition ▸ h
  · rcases le_lm ic.outer h₁ with h | h
    · exact absurd h hmw
    · exact h

variable (ord sys) in
/-- **Compositions trivial modulo their word** (Shirshov's form of the
    composition condition). Every overlap S-polynomial lies in the `k`-span of
    the `a·rel·b` whose word is strictly below the ambient word of the overlap,
    and every inclusion S-polynomial in the span below the outer leading
    monomial.

    This is weaker-looking than `IsGrobnerShirshovBasis`, which asks for an
    explicit reduction of each S-polynomial to zero, and is the form a hand
    verification actually produces: one rewrites the S-polynomial with rules
    whose words lie below the composition word, in any order, without having to
    reach a normal form. `isGrobnerShirshovBasis_iff_compositionsTrivial` (end of
    file) shows the two conditions agree when every leading coefficient is a
    unit. Shirshov 1962; Bokut–Chen 2014, Theorem 2.3 (i) ⇔ (ii). -/
structure CompositionsTrivial : Prop where
  /-- Every overlap S-polynomial is trivial modulo the overlap word. -/
  overlap : ∀ oc : OverlapComposition G k ord, oc.rule₁ ∈ sys.rules →
    oc.rule₂ ∈ sys.rules → JM ord sys oc.word (toMA oc.spoly)
  /-- Every inclusion S-polynomial is trivial modulo the outer leading monomial. -/
  inclusion : ∀ ic : InclusionComposition G k ord, ic.inner ∈ sys.rules →
    ic.outer ∈ sys.rules → JM ord sys (ic.outer.lm ord) (toMA ic.spoly)

/-- A Gröbner–Shirshov basis has trivial compositions: the reduction of each
    S-polynomial to zero is itself the required expression below the word. -/
theorem CompositionsTrivial.of_isGrobnerShirshovBasis
    (hgs : IsGrobnerShirshovBasis G k ord sys) : CompositionsTrivial ord sys where
  overlap oc h₁ h₂ := by
    obtain ⟨nf, hred, hz⟩ := hgs.overlap_resolves oc h₁ h₂
    have hJ := (JM_of_multistep (ord := ord) (sys := sys) (u := oc.word) (v := oc.word)
      [] [] (fun m hm => by simpa using hm) hred.reduces (below_spoly_ov oc)).2
    rwa [toMA_of_isZero hz, sub_zero, ofW_nil, one_mul, mul_one] at hJ
  inclusion ic h₁ h₂ := by
    obtain ⟨nf, hred, hz⟩ := hgs.inclusion_resolves ic h₁ h₂
    have hJ := (JM_of_multistep (ord := ord) (sys := sys) (u := ic.outer.lm ord)
      (v := ic.outer.lm ord) [] [] (fun m hm => by simpa using hm) hred.reduces
      (below_spoly_inc ic)).2
    rwa [toMA_of_isZero hz, sub_zero, ofW_nil, one_mul, mul_one] at hJ

/-- `JM` is stable under two-sided context: if `F` lies in the span below `v`,
    then `a·F·b` lies in the span below `a·v·b`. -/
theorem JM.ctx {v : Monomial G} (a b : Monomial G) {F : MA G k} (h : JM ord sys v F) :
    JM ord sys (a ++ v ++ b) (ofW a * F * ofW b) := by
  induction h with
  | gen s hs hlt =>
    have e : ofW a * (ofW s.a * toMA s.r.relation * ofW s.b) * ofW b =
        ofW (a ++ s.a) * toMA s.r.relation * ofW (s.b ++ b) := by
      simp only [ofW_append, mul_assoc]
    rw [e]
    refine JM.gen ⟨s.r, a ++ s.a, s.b ++ b⟩ hs ?_
    have := compat (ord := ord) a b hlt
    simpa [Site.word, List.append_assoc] using this
  | zero => simpa using (JM.zero : JM ord sys (a ++ v ++ b) 0)
  | add _ _ ihF ihH => rw [mul_add, add_mul]; exact ihF.add ihH
  | smul c _ ih => rw [mul_smul_comm, smul_mul_assoc]; exact ih.smul c

/-- Disjoint occurrences. -/
theorem JM_disjoint {s₁ s₂ : Site G k} (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (hr₁ : s₁.r ∈ sys.rules) (hr₂ : s₂.r ∈ sys.rules) (m : Monomial G)
    (ha : s₂.a = s₁.a ++ s₁.r.lm ord ++ m) (hb : s₁.b = m ++ s₂.r.lm ord ++ s₂.b) :
    JM ord sys (s₁.word ord) (D ord s₁ s₂) := by
  have hX₁ : JM ord sys (s₁.word ord)
      (ofW s₁.a * tail ord s₁.r * ofW m * rho ord s₂.r * ofW s₂.b) := by
    refine JM_left hr₂ _ (fun p hp => ?_)
    have := compat (ord := ord) s₁.a (m ++ s₂.r.lm ord ++ s₂.b)
      (tail_support s₁.r (hlc _ hr₁) hp)
    simpa [Site.word, hb, List.append_assoc] using this
  have hX₂ : JM ord sys (s₁.word ord)
      (ofW s₁.a * rho ord s₁.r * ofW m * tail ord s₂.r * ofW s₂.b) := by
    refine JM_right hr₁ _ (fun p hp => ?_)
    have := compat (ord := ord) (s₁.a ++ s₁.r.lm ord ++ m) s₂.b
      (tail_support s₂.r (hlc _ hr₂) hp)
    simpa [Site.word, hb, List.append_assoc] using this
  have e : D ord s₁ s₂ = ofW s₁.a * rho ord s₁.r * ofW m * tail ord s₂.r * ofW s₂.b -
      ofW s₁.a * tail ord s₁.r * ofW m * rho ord s₂.r * ofW s₂.b := by
    unfold D tail
    rw [ha, hb, ofW_append, ofW_append, ofW_append, ofW_append]
    noncomm_ring
  rw [e]; exact JM.sub hX₂ hX₁

theorem inv_inv_lc_left {c₁ c₂ : k} (h₁ : IsUnit c₁) :
    Ring.inverse c₁ * Ring.inverse c₂ * c₁ = Ring.inverse c₂ := by
  rw [mul_comm (Ring.inverse c₁), mul_assoc, Ring.inverse_mul_cancel _ h₁, mul_one]

theorem inv_inv_lc_right {c₁ c₂ : k} (h₂ : IsUnit c₂) :
    Ring.inverse c₁ * Ring.inverse c₂ * c₂ = Ring.inverse c₁ := by
  rw [mul_assoc, Ring.inverse_mul_cancel _ h₂, mul_one]

/-- One occurrence inside the other (`lm₂` inside `lm₁`): an inclusion composition. -/
theorem JM_inclusion {s₁ s₂ : Site G k} (ht : CompositionsTrivial ord sys)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (hr₁ : s₁.r ∈ sys.rules) (hr₂ : s₂.r ∈ sys.rules) (x y : Monomial G)
    (hW : s₁.r.lm ord = x ++ s₂.r.lm ord ++ y) (ha : s₂.a = s₁.a ++ x)
    (hb : s₂.b = y ++ s₁.b) :
    JM ord sys (s₁.word ord) (D ord s₁ s₂) := by
  let ic : InclusionComposition G k ord := ⟨s₂.r, s₁.r, x, y, hW⟩
  have hJ : JM ord sys (s₁.word ord) (ofW s₁.a * toMA ic.spoly * ofW s₁.b) :=
    (ht.inclusion ic hr₂ hr₁).ctx s₁.a s₁.b
  have e : D ord s₁ s₂ = -((Ring.inverse (s₁.r.lc ord) * Ring.inverse (s₂.r.lc ord)) •
      (ofW s₁.a * toMA ic.spoly * ofW s₁.b)) := by
    rw [toMA_spoly_inc]
    show _ = -((Ring.inverse (s₁.r.lc ord) * Ring.inverse (s₂.r.lc ord)) •
      (ofW s₁.a * (s₂.r.lc ord • toMA s₁.r.relation -
        s₁.r.lc ord • (ofW x * toMA s₂.r.relation * ofW y)) * ofW s₁.b))
    simp only [mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc, smul_sub, smul_smul,
      inv_inv_lc_left (hlc _ hr₁), inv_inv_lc_right (c₁ := s₁.r.lc ord) (hlc _ hr₂)]
    unfold D rho
    rw [ha, hb, ofW_append, ofW_append]
    simp only [mul_smul_comm, smul_mul_assoc, mul_assoc]
    abel
  rw [e]; exact (JM.smul _ hJ).neg

/-- A proper overlap: an overlap composition. -/
theorem JM_overlap {s₁ s₂ : Site G k} (ht : CompositionsTrivial ord sys)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (hr₁ : s₁.r ∈ sys.rules) (hr₂ : s₂.r ∈ sys.rules) (A B C : Monomial G) (hB : B ≠ [])
    (h₁ : s₁.r.lm ord = A ++ B) (h₂ : s₂.r.lm ord = B ++ C) (ha : s₂.a = s₁.a ++ A)
    (hb : s₁.b = C ++ s₂.b) :
    JM ord sys (s₁.word ord) (D ord s₁ s₂) := by
  let oc : OverlapComposition G k ord := ⟨s₁.r, s₂.r, A, B, C, h₁, h₂, hB⟩
  have hv : s₁.word ord = s₁.a ++ oc.word ++ s₂.b := by
    simp [Site.word, OverlapComposition.word, oc, h₁, hb, List.append_assoc]
  have hJ : JM ord sys (s₁.word ord) (ofW s₁.a * toMA oc.spoly * ofW s₂.b) := by
    rw [hv]; exact (ht.overlap oc hr₁ hr₂).ctx s₁.a s₂.b
  have e : D ord s₁ s₂ = -((Ring.inverse (s₁.r.lc ord) * Ring.inverse (s₂.r.lc ord)) •
      (ofW s₁.a * toMA oc.spoly * ofW s₂.b)) := by
    rw [toMA_spoly_ov]
    show _ = -((Ring.inverse (s₁.r.lc ord) * Ring.inverse (s₂.r.lc ord)) •
      (ofW s₁.a * (s₂.r.lc ord • (toMA s₁.r.relation * ofW C) -
        s₁.r.lc ord • (ofW A * toMA s₂.r.relation)) * ofW s₂.b))
    simp only [mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc, smul_sub, smul_smul,
      inv_inv_lc_left (hlc _ hr₁), inv_inv_lc_right (c₁ := s₁.r.lc ord) (hlc _ hr₂)]
    unfold D rho
    rw [ha, hb, ofW_append, ofW_append]
    simp only [mul_smul_comm, smul_mul_assoc, mul_assoc]
    abel
  rw [e]; exact (JM.smul _ hJ).neg

/-! ## §7  Two occurrences of words in a word -/

/-- How two occurrences relate when the first starts no later than the second. -/
theorem word_half {a₁ W₁ b₁ a₂ W₂ b₂ a' : Monomial G} (ha : a₂ = a₁ ++ a')
    (h : W₁ ++ b₁ = a' ++ (W₂ ++ b₂)) :
    (∃ m, a₂ = a₁ ++ W₁ ++ m ∧ b₁ = m ++ W₂ ++ b₂) ∨
    (∃ x y, W₁ = x ++ W₂ ++ y ∧ a₂ = a₁ ++ x ∧ b₂ = y ++ b₁) ∨
    (∃ A B C, B ≠ [] ∧ W₁ = A ++ B ∧ W₂ = B ++ C ∧ a₂ = a₁ ++ A ∧ b₁ = C ++ b₂) := by
  rcases List.append_eq_append_iff.mp h with ⟨e, he, hb⟩ | ⟨e, hW, h'⟩
  · -- `a' = W₁ ++ e`: disjoint
    exact Or.inl ⟨e, by rw [ha, he, List.append_assoc], by rw [hb, List.append_assoc]⟩
  · -- `W₁ = a' ++ e` and `W₂ ++ b₂ = e ++ b₁`
    rcases List.append_eq_append_iff.mp h' with ⟨f, hf, hb₂⟩ | ⟨f, hW₂, hb₁⟩
    · -- `e = W₂ ++ f`: `W₂` inside `W₁`
      exact Or.inr (Or.inl ⟨a', f, by rw [hW, hf, List.append_assoc], ha, hb₂⟩)
    · -- `W₂ = e ++ f`, `b₁ = f ++ b₂`
      by_cases he : e = []
      · subst he
        simp only [List.append_nil] at hW
        simp only [List.nil_append] at hW₂
        exact Or.inl ⟨[], by rw [ha, hW]; simp, by rw [hb₁, hW₂]; simp⟩
      · exact Or.inr (Or.inr ⟨a', e, f, he, hW, hW₂, ha, hb₁⟩)

/-- Every two reductions of one word differ by an element of the ideal below it. -/
theorem JM_D (ht : CompositionsTrivial ord sys)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) {s₁ s₂ : Site G k}
    (hr₁ : s₁.r ∈ sys.rules) (hr₂ : s₂.r ∈ sys.rules)
    (hw : s₁.word ord = s₂.word ord) :
    JM ord sys (s₁.word ord) (D ord s₁ s₂) := by
  have h : s₁.a ++ (s₁.r.lm ord ++ s₁.b) = s₂.a ++ (s₂.r.lm ord ++ s₂.b) := by
    simpa [Site.word, List.append_assoc] using hw
  rcases List.append_eq_append_iff.mp h with ⟨a', ha, h'⟩ | ⟨c', ha, h'⟩
  · rcases word_half ha h' with ⟨m, ha₂, hb₁⟩ | ⟨x, y, hW, ha₂, hb₂⟩ |
        ⟨A, B, C, hB, h₁, h₂, ha₂, hb₁⟩
    · exact JM_disjoint hlc hr₁ hr₂ m ha₂ hb₁
    · exact JM_inclusion ht hlc hr₁ hr₂ x y hW ha₂ hb₂
    · exact JM_overlap ht hlc hr₁ hr₂ A B C hB h₁ h₂ ha₂ hb₁
  · have key : JM ord sys (s₂.word ord) (D ord s₂ s₁) := by
      rcases word_half ha h' with ⟨m, ha₂, hb₁⟩ | ⟨x, y, hW, ha₂, hb₂⟩ |
          ⟨A, B, C, hB, h₁, h₂, ha₂, hb₁⟩
      · exact JM_disjoint hlc hr₂ hr₁ m ha₂ hb₁
      · exact JM_inclusion ht hlc hr₂ hr₁ x y hW ha₂ hb₂
      · exact JM_overlap ht hlc hr₂ hr₁ A B C hB h₁ h₂ ha₂ hb₁
    rw [hw, ← neg_neg (D ord s₁ s₂), ← D_swap]
    exact key.neg

/-! ## §8  Every element is reduction-unique (Bergman 1978, Thm 1.2) -/

/-- A step from `single v 1` lands strictly below `v`, at a site whose word is `v`. -/
theorem single_step [DecidableEq k] (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    {v : Monomial G} {g : AlgElement G k}
    (h : SingleStepReduction ord sys (single v (1 : k)) g) :
    ∃ s : Site G k, s.r ∈ sys.rules ∧ s.word ord = v ∧ CoeffEq g (op ord s (single v 1)) ∧
      Below ord v g := by
  obtain ⟨s, hs, hne, hg⟩ := step_eq_op hlc h
  have hw : s.word ord = v := by
    by_contra hw; exact hne (single_coeff_of_ne _ hw)
  refine ⟨s, hs, hw, hg, below_congr (ceq_symm hg) ?_⟩
  intro m hm
  rw [op_coeff, hw, single_coeff_self, one_mul] at hm
  by_cases hmv : m = v
  · exfalso; apply hm
    rw [hmv, ← hw, single_coeff_self]
    show 1 - Ring.inverse (s.r.lc ord) *
      (contextMul s.a s.r.relation s.b).coeff (s.a ++ s.r.lm ord ++ s.b) = 0
    rw [contextMul_coeff_middle]
    show 1 - Ring.inverse (s.r.lc ord) * s.r.lc ord = 0
    rw [Ring.inverse_mul_cancel _ (hlc _ hs), sub_self]
  · rw [single_coeff_of_ne _ hmv, zero_sub] at hm
    have hc : (contextMul s.a s.r.relation s.b).coeff m ≠ 0 :=
      fun h0 => hm (by rw [h0, mul_zero, neg_zero])
    rcases ctx_le_word s hc with h | h
    · exact absurd (h.trans hw) hmv
    · exact hw ▸ h

theorem toMA_op_single [DecidableEq k] {v : Monomial G} (s : Site G k) (hw : s.word ord = v) :
    toMA (op ord s (single v (1 : k))) =
      toMA (single v (1 : k)) - ofW s.a * rho ord s.r * ofW s.b := by
  unfold op
  rw [toMA_sub, toMA_smul, toMA_contextMul, hw, single_coeff_self, one_mul]
  unfold rho
  rw [mul_smul_comm, smul_mul_assoc]

/-- **The crux.** If everything strictly below `v` is reduction-unique, so is the
    monomial `v`: two first steps from `v` differ by an element of the ideal
    below `v`, which reduces to zero. -/
theorem RU_single [DecidableEq k] (ht : CompositionsTrivial ord sys)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) {v : Monomial G}
    (hbelow : ∀ f, Below ord v f → RU ord sys f) : RU ord sys (single v (1 : k)) := by
  intro n₁ n₂ h₁ h₂
  by_cases hnorm : isNormalForm ord sys (single v (1 : k))
  · exact RU_of_isNormalForm hnorm n₁ n₂ h₁ h₂
  have first : ∀ n, ReducesToNF ord sys (single v (1 : k)) n →
      ∃ s : Site G k, ∃ g, s.r ∈ sys.rules ∧ s.word ord = v ∧
        CoeffEq g (op ord s (single v 1)) ∧ Below ord v g ∧ ReducesToNF ord sys g n := by
    intro n hn
    rcases MultiStepReduction.cases_head hn.reduces with heq | ⟨g, hstep, hrest⟩
    · exact absurd (heq ▸ hn.is_normal) hnorm
    · obtain ⟨s, hs, hw, hg, hb⟩ := single_step hlc hstep
      exact ⟨s, g, hs, hw, hg, hb, hrest, hn.is_normal⟩
  obtain ⟨s₁, g₁, hs₁, hw₁, hg₁, hb₁, hn₁⟩ := first n₁ h₁
  obtain ⟨s₂, g₂, hs₂, hw₂, hg₂, hb₂, hn₂⟩ := first n₂ h₂
  -- the difference of the two first reducts reduces to zero
  have hΔ : CoeffEq (sub g₁ g₂) (ofMA (D ord s₁ s₂)) := by
    apply ceq_of_toMA_eq
    rw [toMA_ofMA, toMA_sub, toMA_eq_of_ceq hg₁, toMA_eq_of_ceq hg₂,
      toMA_op_single s₁ hw₁, toMA_op_single s₂ hw₂]
    unfold D; abel
  have hJ := JM_D ht hlc hs₁ hs₂ (hw₁.trans hw₂.symm)
  rw [hw₁] at hJ
  obtain ⟨nΔ, hnΔ, hzΔ⟩ := zeroNF_congr hlc hΔ (hJ.zeroNF hlc hbelow)
  have hbΔ : Below ord v (sub g₁ g₂) := by
    intro m hm
    rw [sub_coeff] at hm
    by_cases h0 : g₁.coeff m = 0
    · exact hb₂ m (fun h' => hm (by rw [h0, h', sub_self]))
    · exact hb₁ m h0
  have hsum : CoeffEq (add g₂ (sub g₁ g₂)) g₁ := by
    intro m; rw [add_coeff, sub_coeff]; abel
  obtain ⟨n₁', hn₁', e₁⟩ := nf_of_congr hlc hsum hn₁
  have := nf_add hlc (hbelow _ hb₂) (hbelow _ hbΔ) hn₁' hn₂ hnΔ
  intro m
  rw [← e₁ m, this m, add_coeff, hzΔ m, add_zero]

variable (ord sys) in
/-- **Bergman's Diamond Lemma, triviality form.** If every composition is trivial
    modulo its word and every leading coefficient is a unit, every element has a
    unique normal form, up to `CoeffEq`. -/
theorem reductionUnique_of_trivial (ht : CompositionsTrivial ord sys)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) (f : AlgElement G k) : RU ord sys f := by
  classical
  have H : ∀ v : Monomial G, ∀ f : AlgElement G k,
      (∀ m, f.coeff m ≠ 0 → ord.lt m v ∨ m = v) → RU ord sys f := by
    intro v
    induction v using ord.wf.induction with
    | _ v IH =>
    have hbelow : ∀ f, Below ord v f → RU ord sys f := by
      intro f hf
      by_cases hz : ∀ m, f.coeff m = 0
      · exact RU_of_isNormalForm (isNormalForm_of_isZero hz)
      push_neg at hz
      obtain ⟨m₀, hm₀⟩ := hz
      have hne : (liveSupport f).Nonempty := ⟨m₀, (mem_liveSupport f m₀).mpr hm₀⟩
      obtain ⟨m₁, hm₁, hmax⟩ := ord.exists_max (liveSupport f) hne
      have hm₁' := (mem_liveSupport f m₁).mp hm₁
      refine IH m₁ (hf m₁ hm₁') f (fun m hm => ?_)
      rcases ord.trichotomy m m₁ with h | h | h
      · exact Or.inl h
      · exact Or.inr h
      · exact absurd h (hmax m ((mem_liveSupport f m).mpr hm))
    intro f hf
    have hrest : Below ord v (eraseCoeff f v) := by
      intro m hm
      by_cases hmv : m = v
      · exact absurd (by rw [hmv]; exact eraseCoeff_self f v) hm
      · rw [eraseCoeff_of_ne hmv] at hm
        rcases hf m hm with h | h
        · exact h
        · exact absurd h hmv
    have hce : CoeffEq (add (smul (f.coeff v) (single v (1 : k))) (eraseCoeff f v)) f := by
      intro m
      rw [add_coeff, smul_coeff]
      by_cases hmv : m = v
      · subst hmv; rw [single_coeff_self, eraseCoeff_self, mul_one, add_zero]
      · rw [single_coeff_of_ne _ hmv, eraseCoeff_of_ne hmv, mul_zero, zero_add]
    exact RU_congr hlc hce (RU_add hlc (RU_smul hlc _ (RU_single ht hlc hbelow))
      (hbelow _ hrest))
  by_cases hz : ∀ m, f.coeff m = 0
  · exact RU_of_isNormalForm (isNormalForm_of_isZero hz)
  push_neg at hz
  obtain ⟨m₀, hm₀⟩ := hz
  have hne : (liveSupport f).Nonempty := ⟨m₀, (mem_liveSupport f m₀).mpr hm₀⟩
  obtain ⟨m₁, _, hmax⟩ := ord.exists_max (liveSupport f) hne
  refine H m₁ f (fun m hm => ?_)
  rcases ord.trichotomy m m₁ with h | h | h
  · exact Or.inl h
  · exact Or.inr h
  · exact absurd h (hmax m ((mem_liveSupport f m).mpr hm))

variable (ord sys) in
/-- **Bergman's Diamond Lemma, in this framework.** For a Gröbner–Shirshov basis
    with unit leading coefficients over a commutative ring, every element has a
    unique normal form, up to `CoeffEq`. -/
theorem reductionUnique (hgs : IsGrobnerShirshovBasis G k ord sys)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) (f : AlgElement G k) : RU ord sys f :=
  reductionUnique_of_trivial ord sys (CompositionsTrivial.of_isGrobnerShirshovBasis hgs) hlc f

/-- **The converse.** Trivial compositions make every S-polynomial reduce to
    zero: an element of the span below a word reduces to zero once everything
    below that word is reduction-unique (`JM.zeroNF`), and here everything is. -/
theorem isGrobnerShirshovBasis_of_compositionsTrivial (ht : CompositionsTrivial ord sys)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) : IsGrobnerShirshovBasis G k ord sys where
  overlap_resolves oc h₁ h₂ :=
    zeroNF_congr hlc (ceq_ofMA_toMA oc.spoly)
      ((ht.overlap oc h₁ h₂).zeroNF hlc (fun f _ => reductionUnique_of_trivial ord sys ht hlc f))
  inclusion_resolves ic h₁ h₂ :=
    zeroNF_congr hlc (ceq_ofMA_toMA ic.spoly)
      ((ht.inclusion ic h₁ h₂).zeroNF hlc (fun f _ => reductionUnique_of_trivial ord sys ht hlc f))

/-- **Composition lemma, Shirshov's form.** With unit leading coefficients over a
    commutative ring, a rewriting system is a Gröbner–Shirshov basis exactly when
    every composition is trivial modulo its word. -/
theorem isGrobnerShirshovBasis_iff_compositionsTrivial
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) :
    IsGrobnerShirshovBasis G k ord sys ↔ CompositionsTrivial ord sys :=
  ⟨CompositionsTrivial.of_isGrobnerShirshovBasis,
    fun ht => isGrobnerShirshovBasis_of_compositionsTrivial ht hlc⟩

end UGB.GrobnerShirshov.Diamond
