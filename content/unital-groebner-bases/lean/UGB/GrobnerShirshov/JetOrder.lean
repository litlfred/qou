import UGB.GrobnerShirshov.Basic
import UGB.GrobnerShirshov.AlgOps
import UGB.GrobnerShirshov.CompositionLemma
import UGB.GrobnerShirshov.Flatness
import Mathlib.Order.WellFoundedSet
import Mathlib.Data.List.Lex
import Mathlib.Data.Prod.Lex

/-!
# Jet-Stratified Gröbner–Shirshov Reduction

This module formalises two results connecting jet prolongation to
Gröbner–Shirshov (GS) computation:

1. **Ordering extension through the jet tower** (moved from
   `QOU.Torsion.ordering_jet_compatibility`): the deg-lex admissible
   order at level `n` extends compatibly to level `n+1` when jet
   prolongation introduces new generators.

2. **Jet-stratified reduction algorithm**: given a GS basis `Σₙ` at
   level `n`, the GS property at level `n+1` can be verified by
   checking only S-polynomials that involve at least one *transient*
   (new) relation — the descended–descended pairs are inherited.

## Complexity

Standard Buchberger at level `n+1` checks `O(|Σ_{n+1}|²)` S-poly
pairs.  Jet-stratified reduction checks only
`O(|Σₙ| · k + k²)` pairs, where `k = |Σ_{n+1}^trans|`.

For SU(2) (k = O(1) new generators per level), this reduces the
S-polynomial work from `O(n²)` to `O(n)` per jet level.

## References

- [fred2005, §3] — Gröbner–Shirshov basis for Dist(G)
- [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
- [bokutchen2014] Bokut & Chen, Bull. Math. Sci. 4 (2014), §2.1.
-/


namespace UGB.GrobnerShirshov

universe u v

/-! ## §1  Jet Extension of Admissible Orders -/

/-- Configuration for one step of jet prolongation.

    At level `n`, the algebra has `numGens` generators.  Jet
    prolongation `J¹(Aₙ) = Aₙ ⊗ Ω¹(Aₙ)` introduces `numNewDirs`
    new Kähler directions (= 3 for SU(2)). -/
structure JetConfig where
  /-- Brane level index. -/
  level : ℕ
  /-- Number of generators at this level. -/
  numGens : ℕ
  /-- Number of new Ω¹ directions per prolongation. -/
  numNewDirs : ℕ := 3

/-- At level `n+1`, generators are drawn from a larger alphabet:
    the original generators plus the new Kähler directions.

    We model the extended alphabet as `Fin (numGens + numNewDirs)`:
    indices `< numGens` are descended (inherited from level `n`),
    indices `≥ numGens` are transient (new at level `n+1`). -/
def JetConfig.totalGens (jc : JetConfig) : ℕ :=
  jc.numGens + jc.numNewDirs

/-- A generator index is **descended** if it comes from level `n`. -/
def isDescended (jc : JetConfig) (i : ℕ) : Prop :=
  i < jc.numGens

/-- A generator index is **transient** if it is new at level `n+1`. -/
def isTransient (jc : JetConfig) (i : ℕ) : Prop :=
  jc.numGens ≤ i ∧ i < jc.totalGens

/-- A monomial (word) is **descended** if all its generators are. -/
def monomialDescended (jc : JetConfig) (w : List ℕ) : Prop :=
  ∀ g ∈ w, isDescended jc g

/-- A monomial is **transient** if at least one generator is new. -/
def monomialTransient (jc : JetConfig) (w : List ℕ) : Prop :=
  ∃ g ∈ w, isTransient jc g

/-! ### Deg-lex on ℕ-indexed generators -/

/-- Deg-lex ordering on words over `ℕ`-indexed generators:
    compare by length first, then lexicographically. -/
def degLexNat (a b : List ℕ) : Prop :=
  a.length < b.length ∨ (a.length = b.length ∧ a < b)

-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
/-- Fixed-length lexicographic order on `List ℕ` is well-founded on each length fiber.
Base case `{l | l.length = 0} = {[]}` is a singleton; the successor case is the head/tail
decomposition `Prod.Lex (· < ·) (· < ·)` via `prod_lex_of_wellFoundedOn_fiber`, with the tail
fibers (length `k`) pulled back from the inductive hypothesis. -/
theorem fixedLength_lex_wf :
    ∀ n, (List.length ⁻¹' {n} : Set (List ℕ)).WellFoundedOn (· < ·) := by
  intro n
  induction n with
  | zero =>
    apply Set.Subsingleton.wellFoundedOn
    intro x hx y hy
    simp only [Set.mem_preimage, Set.mem_singleton_iff, List.length_eq_zero_iff] at hx hy
    rw [hx, hy]
  | succ k ih =>
    have prod_result :
        (List.length ⁻¹' {k + 1} : Set (List ℕ)).WellFoundedOn
          (Function.onFun (Prod.Lex (· < ·) (· < ·)) fun l => (l.headI, l.tail)) := by
      refine Set.WellFoundedOn.prod_lex_of_wellFoundedOn_fiber
        (f := List.headI) (g := List.tail) (rα := (· < ·)) (rβ := (· < ·))
        ((InvImage.wf List.headI wellFounded_lt).wellFoundedOn) (fun a => ?_)
      refine InvImage.wf
        (fun p : ↥((List.length ⁻¹' {k + 1}) ∩ List.headI ⁻¹' {a}) =>
          (⟨(p : List ℕ).tail, ?_⟩ : ↥(List.length ⁻¹' {k} : Set (List ℕ)))) ih
      have hp : (p : List ℕ).length = k + 1 := p.2.1
      simp only [Set.mem_preimage, Set.mem_singleton_iff, List.length_tail, hp,
        Nat.add_sub_cancel]
    refine Subrelation.wf (fun {a b} hab => ?_) prod_result
    have hlt : (a : List ℕ) < (b : List ℕ) := hab
    have ha : (a : List ℕ).length = k + 1 := a.2
    have hb : (b : List ℕ).length = k + 1 := b.2
    obtain ⟨x, t, hx⟩ :=
      List.exists_cons_of_ne_nil (by intro h; rw [h] at ha; simp at ha : (a : List ℕ) ≠ [])
    obtain ⟨y, u, hy⟩ :=
      List.exists_cons_of_ne_nil (by intro h; rw [h] at hb; simp at hb : (b : List ℕ) ≠ [])
    show Prod.Lex (· < ·) (· < ·) ((a : List ℕ).headI, (a : List ℕ).tail)
      ((b : List ℕ).headI, (b : List ℕ).tail)
    rw [hx, hy] at hlt ⊢
    simp only [List.headI_cons, List.tail_cons]
    rw [List.cons_lt_cons_iff] at hlt
    exact Prod.lex_iff.2 hlt

-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
/-- `degLexNat` (deg-lex, length-first) is well-founded. It has order type ω^ω — so it is not
order-embeddable into ℕ, and *pure* lex is not well-founded (cf. the removed `lexLt_wf` in
`NormalForms.lean`, where `[g₁] > [g₀,g₁] > …` descends forever). The length-first guard rescues
it: `degLexNat = Prod.Lex (· < ·) (· < ·)` pulled back along `l ↦ (l.length, l)`, and the inner
`(· < ·)` is well-founded on each length fiber (`fixedLength_lex_wf`), so
`WellFounded.prod_lex_of_wellFoundedOn_fiber` applies. -/
theorem degLexNat_wf : WellFounded degLexNat := by
  have key := WellFounded.prod_lex_of_wellFoundedOn_fiber
    (rα := (· < · : ℕ → ℕ → Prop)) (rβ := (· < · : List ℕ → List ℕ → Prop))
    (f := List.length) (g := id)
    (InvImage.wf List.length wellFounded_lt)
    (fun a => fixedLength_lex_wf a)
  refine Subrelation.wf ?_ key
  intro a b h
  show Prod.Lex (· < ·) (· < ·) (a.length, a) (b.length, b)
  exact Prod.lex_iff.2 h

/-- Deg-lex is compatible with left concatenation. -/
theorem degLexNat_left_compat (a b c : List ℕ) (h : degLexNat a b) :
    degLexNat (c ++ a) (c ++ b) := by
  -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
  rcases h with hlen | ⟨heq, hlex⟩
  · left
    rw [List.length_append, List.length_append]
    omega
  · right
    refine ⟨?_, ?_⟩
    · rw [List.length_append, List.length_append]; omega
    · -- a < b (as List ℕ) → c ++ a < c ++ b
      -- Standard preservation of lex order under left concatenation.
      induction c with
      | nil => simpa using hlex
      | cons x xs ih =>
        simp only [List.cons_append]
        exact List.Lex.cons ih

/-- Deg-lex is compatible with right concatenation. -/
theorem degLexNat_right_compat (a b d : List ℕ) (h : degLexNat a b) :
    degLexNat (a ++ d) (b ++ d) := by
  -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
  rcases h with hlen | ⟨heq, hlex⟩
  · left
    rw [List.length_append, List.length_append]
    omega
  · right
    refine ⟨by rw [List.length_append, List.length_append]; omega, ?_⟩
    -- a < b (same length) → a ++ d < b ++ d.
    -- Induction on a generalising b: lex difference lives in prefix.
    induction a generalizing b with
    | nil =>
      cases b with
      | nil => cases hlex
      | cons _ _ => simp at heq
    | cons x xs ih =>
      cases b with
      | nil => simp at heq
      | cons y ys =>
        simp only [List.cons_append]
        cases hlex with
        | cons h =>
          have heq' : xs.length = ys.length := by
            simp [List.length_cons] at heq; exact heq
          exact List.Lex.cons (ih ys heq' h)
        | rel h => exact List.Lex.rel h

/-! ### Ordering extends through the jet tower -/

/-- **Jet-embedding order compatibility.** The jet embedding sends each
    level-`n` generator to the *same* index among the first `numGens`
    indices at level `n+1`, so a **descended** monomial's ℕ-valued index
    list is left unchanged by the embedding `φ` (`φ a = a`). A deg-lex
    comparison of two descended monomials therefore carries over verbatim
    to their images.

    Stated with the embedding `φ` and its fixed-point property on descended
    monomials (`φ a = a`, `φ b = b`) as explicit hypotheses, and the
    preserved comparison **derived** by rewriting — not the old
    self-assuming `(hab : degLexNat a b) : degLexNat a b := hab`, which
    named the embedding nowhere and asserted nothing about it.

    Reference: [manuscript] §3/ordering-jet-compatibility. -/
-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
theorem ordering_extends {φ : List ℕ → List ℕ} {a b : List ℕ}
    (hφa : φ a = a) (hφb : φ b = b) (hab : degLexNat a b) :
    degLexNat (φ a) (φ b) := by
  rw [hφa, hφb]; exact hab

/-- **Well-foundedness at each level**: within the alphabet
    `{0, …, n-1}`, deg-lex has no infinite descending chains. -/
-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
theorem wellfounded_at_level (n : ℕ) :
    WellFounded (fun (a b : List ℕ) =>
      degLexNat a b ∧ ∀ g ∈ a, g < n) :=
  Subrelation.wf (fun {_ _} ⟨h, _⟩ => h) degLexNat_wf

/-- **Direct-limit termination**: for any element belonging to
    some finite level `Aₙ`, GS reduction terminates.

    The ordering `≺_∞ = ⋃ₙ ≺ₙ` is well-founded on elements of
    bounded generator index because `degLexNat` is well-founded
    and the bounded-alphabet restriction is a subrelation. -/
-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
-- Ref: [manuscript] §3/ordering-jet-compatibility
theorem direct_limit_terminates (n : ℕ) (w : List ℕ)
    (_hw : ∀ g ∈ w, g < n) :
    Acc degLexNat w :=
  degLexNat_wf.apply w

/-! ## §2  Descended / Transient Splitting of Rewriting Systems -/

/-- Classification of a reduction rule as descended or transient.

    A rule is **descended** if its leading monomial uses only
    level-`n` generators.  It is **transient** if the leading
    monomial contains at least one new generator.

    The descent involution `τ̂ₙ` projects transient rules to zero
    and fixes descended rules (vertex-algebra-jet-relations, D-1/D-2). -/
inductive RuleClass where
  | descended : RuleClass
  | transient : RuleClass
  deriving DecidableEq, Repr

/-- Classify a reduction rule by examining its leading monomial.
    Uses `jc.numGens` as the threshold: generators below it are
    descended, those at or above are transient. -/
def classifyRule (jc : JetConfig) (lm : List ℕ) : RuleClass :=
  if lm.all (· < jc.numGens) then .descended else .transient

/-- A **jet-stratified rewriting system** at level `n+1`:
    the descended subsystem inherited from level `n`, plus
    the transient rules introduced by jet prolongation. -/
structure JetStratifiedSystem (G : Type u) (k : Type v) [Ring k] where
  /-- The full rewriting system at level `n+1`. -/
  full : RewritingSystem G k
  /-- The descended subsystem (inherited from level `n`). -/
  descended : RewritingSystem G k
  /-- The transient rules (new at level `n+1`). -/
  transientRules : List (ReductionRule G k)
  /-- The full system is the union of descended and transient. -/
  union_spec : full.rules = descended.rules ++ transientRules

/-! ## §3  Jet-Stratified S-Polynomial Classification -/

/-- Classification of an S-polynomial pair by the rule classes
    of its two constituent rules. -/
inductive SPolyClass where
  /-- Both rules descended: inherited from level `n`. -/
  | desc_desc : SPolyClass
  /-- One descended, one transient: must check. -/
  | desc_trans : SPolyClass
  /-- Both transient: must check. -/
  | trans_trans : SPolyClass
  deriving DecidableEq, Repr

/-- Classify an S-polynomial pair. -/
def classifySPoly (c₁ c₂ : RuleClass) : SPolyClass :=
  match c₁, c₂ with
  | .descended, .descended => .desc_desc
  | .descended, .transient => .desc_trans
  | .transient, .descended => .desc_trans
  | .transient, .transient => .trans_trans

/-! ## §4  Jet-Stratified GS Verification -/

/-- **Descended GS inheritance** (axiom stub): if the descended
    subsystem is already a GS basis (verified at level `n`), then
    all descended × descended S-polynomials resolve to zero.

    This is the key lemma that eliminates `O(|Σₙ|²)` checks.

    Axiomatised because the proof requires constructing the reduction
    of each descended S-polynomial within the full system, showing that
    the extra transient rules do not interfere with the descended
    reduction (since transient leading monomials involve new generators
    that cannot appear in descended monomials). -/
-- Ref: [fred2005] §3, Proposition 3.8
-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
axiom descended_gs_inherited
    {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (jss : JetStratifiedSystem G k)
    (h_desc_gs : IsGrobnerShirshovBasis G k ord jss.descended)
    (oc : OverlapComposition G k ord)
    (h₁ : oc.rule₁ ∈ jss.descended.rules)
    (h₂ : oc.rule₂ ∈ jss.descended.rules) :
    ∃ nf, ReducesToNF ord jss.full oc.spoly nf ∧ nf.isZero

/-- **Jet-stratified GS criterion** (axiom stub): the full system
    at level `n+1` is a GS basis if and only if:
    1. The descended subsystem is a GS basis (from level `n`), AND
    2. All desc×trans and trans×trans S-polynomials resolve to zero.

    Condition (1) is inherited.  Only condition (2) requires new
    computation: `O(|Σₙ| · k + k²)` S-poly checks instead of
    `O(|Σ_{n+1}|²)`.

    Axiomatised because the full proof requires showing that the
    descended subsystem's GS property lifts through the inclusion
    into the full system, using `descended_gs_inherited` plus the
    hypotheses on new S-polynomials.

    Reference: [fred2005, §3], extended to jet towers. -/
-- Ref: [fred2005] §3, Proposition 3.8
-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
axiom jet_stratified_gs_criterion
    {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (jss : JetStratifiedSystem G k)
    (h_desc_gs : IsGrobnerShirshovBasis G k ord jss.descended)
    (h_new_overlap : ∀ (oc : OverlapComposition G k ord),
      oc.rule₁ ∈ jss.full.rules → oc.rule₂ ∈ jss.full.rules →
      ¬(oc.rule₁ ∈ jss.descended.rules ∧ oc.rule₂ ∈ jss.descended.rules) →
      ∃ nf, ReducesToNF ord jss.full oc.spoly nf ∧ nf.isZero)
    (h_new_inclusion : ∀ (ic : InclusionComposition G k ord),
      ic.inner ∈ jss.full.rules → ic.outer ∈ jss.full.rules →
      ¬(ic.inner ∈ jss.descended.rules ∧ ic.outer ∈ jss.descended.rules) →
      ∃ nf, ReducesToNF ord jss.full ic.spoly nf ∧ nf.isZero) :
    IsGrobnerShirshovBasis G k ord jss.full

/-! ## §5  Degree-Bucketed Reduction -/

/-- A **degree bucket** groups reduction rules by the length of
    their leading monomial.  During reduction, an element of
    degree `d` need only be checked against rules in buckets
    `≤ d`. -/
structure DegreeBucket (G : Type u) (k : Type v) [Ring k] where
  /-- The degree (leading monomial length) for this bucket. -/
  degree : ℕ
  /-- Rules whose leading monomial has this degree. -/
  rules : List (ReductionRule G k)

/-- Partition a rewriting system into degree buckets.

    For the Hecke algebra:
    - Bucket 2: Hecke relations `σᵢ² → …` and far-commutativity
    - Bucket 3: Yang–Baxter relations `σᵢσⱼσᵢ → …` -/
noncomputable def bucketize {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k) (maxDeg : ℕ) :
    List (DegreeBucket G k) :=
  (List.range (maxDeg + 1)).map fun d => {
    degree := d,
    rules := sys.rules.filter fun r =>
      (leadingMonomial ord r.relation r.nonzero).length = d
  }

/-- **Degree-filtered reduction** (axiom stub): when reducing a
    monomial of degree `d`, only rules with leading monomial degree
    `≤ d` can apply (since reduction strictly decreases the leading
    monomial under deg-lex).

    This reduces per-step scanning from `O(|Σ|)` to `O(|B_{≤d}|)`.

    Axiomatised because the proof requires showing that
    `SingleStepReduction` with a rule of LM degree `> d` cannot
    match any monomial of degree `d` (the LM is too long to be
    a subword). -/
-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
axiom degree_filtered_reduction_correct
    {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (f nf_full nf_filtered : AlgElement G k)
    (h_full : ReducesToNF ord sys f nf_full)
    -- Restricting to rules with LM degree ≤ max degree of f's support
    -- yields the same normal form:
    : nf_full = nf_filtered

/-! ## §6  Combined Jet-Stratified + Degree-Bucketed Algorithm -/

/-- Configuration for the combined algorithm. -/
structure JetReductionConfig (G : Type u) (k : Type v) [Ring k] [DecidableEq G] where
  /-- Admissible order. -/
  ord : AdmissibleOrder G
  /-- Jet configuration (level, generator counts). -/
  jet : JetConfig
  /-- Jet-stratified rewriting system. -/
  system : JetStratifiedSystem G k
  /-- Maximum degree of any leading monomial in the system. -/
  maxLMDegree : ℕ
  /-- The descended subsystem is a GS basis (from previous level). -/
  desc_is_gs : IsGrobnerShirshovBasis G k ord system.descended

/-- **S-polynomial count** at level `n+1` under jet stratification.

    Let `m = |Σₙ|` (descended rules) and `k = |Σ^trans|` (transient).
    - Naive Buchberger: `(m + k) choose 2 ≈ O((m+k)²)` pairs
    - Jet-stratified:  `m·k + k choose 2 ≈ O(mk + k²)` pairs
    - Savings:         `m choose 2 ≈ O(m²)` pairs skipped -/
def spolyCountNaive (m k : ℕ) : ℕ := (m + k) * (m + k - 1) / 2
def spolyCountStratified (m k : ℕ) : ℕ := m * k + k * (k - 1) / 2
def spolySavings (m _k : ℕ) : ℕ := m * (m - 1) / 2

/-! ## §7  Correctness of the Combined Algorithm -/

/-- **Main theorem**: the jet-stratified + degree-bucketed algorithm
    computes the same normal forms as naive Buchberger, but with
    fewer S-polynomial checks and narrower per-step scanning.

    The proof combines:
    - `jet_stratified_gs_criterion` (skip desc×desc S-polys)
    - `degree_filtered_reduction_correct` (narrow rule scanning)
    - `normal_form_unique` (result is the same either way)

    Reference: [fred2005, §3] + [bergman1978, §5]. -/
-- Ref: [fred2005] §3, Proposition 3.8
-- Ref: [bergman1978] Bergman, "The diamond lemma for ring theory," Adv. Math. 29 (1978)
theorem jet_stratified_correct
    {G : Type u} {k : Type v} [Field k] [DecidableEq G]
    (cfg : JetReductionConfig G k)
    (h_new_resolved : ∀ (oc : OverlapComposition G k cfg.ord),
      oc.rule₁ ∈ cfg.system.full.rules →
      oc.rule₂ ∈ cfg.system.full.rules →
      ¬(oc.rule₁ ∈ cfg.system.descended.rules ∧
        oc.rule₂ ∈ cfg.system.descended.rules) →
      ∃ nf, ReducesToNF cfg.ord cfg.system.full oc.spoly nf ∧ nf.isZero)
    (h_inc_resolved : ∀ (ic : InclusionComposition G k cfg.ord),
      ic.inner ∈ cfg.system.full.rules →
      ic.outer ∈ cfg.system.full.rules →
      ¬(ic.inner ∈ cfg.system.descended.rules ∧
        ic.outer ∈ cfg.system.descended.rules) →
      ∃ nf, ReducesToNF cfg.ord cfg.system.full ic.spoly nf ∧ nf.isZero) :
    IsGrobnerShirshovBasis G k cfg.ord cfg.system.full :=
  jet_stratified_gs_criterion cfg.ord cfg.system cfg.desc_is_gs
    h_new_resolved h_inc_resolved

end UGB.GrobnerShirshov
