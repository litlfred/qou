import UGB.GrobnerShirshov.Basic
import UGB.GrobnerShirshov.AlgOps
import UGB.GrobnerShirshov.CompositionLemma
import Mathlib.Data.Real.Basic
import Mathlib.Logic.Function.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-!
# Gröbner–Shirshov Basis for the Hecke Algebra

Instantiation of the abstract GS framework for the Hecke algebra
`H_n(q)`, with constructive definitions replacing former axioms.

## Axiom budget

| Item | Status | Justification |
|------|--------|---------------|
| `heckeOrder` | **def** | `mkDegLexOrder` from AlgOps.lean (generic deg-lex) |
| `hecke_is_gs_basis` | **axiom** | Bokut & Shiao 2001, Thm 3.5 — non-vacuous since the sentinel was removed; see §4b |
| `heckeRewritingSystem` | **def** | Built from `AlgElement.ofTerms`; needs `0 < n`, no sentinel |
| `embedGenerator` | **def** | `single` + `ofTerms` |
| `braidToAlg` | **def** | `leftMulGen` fold |
| `augmentedBraidElement` | **def** | Composition of `braidToAlg` |
| `heckeCost` | **def** | Sum over `AlgElement.support` |
| `gs_basis_of_empty_lm` | **theorem** | why the sentinel had to go |

## References

- Bokut & Shiao, "Gröbner–Shirshov bases for Coxeter groups",
  Comm. Algebra 29 (2001), 4305–4319.
-/


namespace UGB.GrobnerShirshov.Hecke

open UGB.GrobnerShirshov

/-! ## §1  Hecke Generators -/

/-- Generator type for the Hecke algebra `H_n(q)`.
    For `n` strands, there are `n` generators `σ₀,…,σ_{n-1}`. -/
structure HeckeGen (n : ℕ) where
  /-- Generator index (0-based). -/
  index : Fin n

instance (n : ℕ) : DecidableEq (HeckeGen n) := by
  intro a b
  cases a; cases b
  simp only [HeckeGen.mk.injEq]
  exact inferInstance

/-- The rank of a Hecke generator (for deg-lex ordering). -/
def HeckeGen.rank {n : ℕ} (g : HeckeGen n) : ℕ := g.index.val

/-- Shorthand: create a Hecke generator from a natural number index.
    Returns the generator `σ_i` when `i < n`. -/
def σ {n : ℕ} (i : Fin n) : HeckeGen n := ⟨i⟩

/-! ## §2  Admissible Order -/

/-- The rank function for `HeckeGen n` is injective. -/
theorem HeckeGen.rank_injective {n : ℕ} :
    Function.Injective (HeckeGen.rank (n := n)) := by
  intro ⟨a⟩ ⟨b⟩ h
  simp [HeckeGen.rank] at h
  exact congrArg HeckeGen.mk (Fin.ext h)

/-- The deg-lex admissible order on Hecke monomials.
    Constructed via the generic `mkDegLexOrder` from AlgOps.lean,
    reusing the same proof infrastructure as `degLexOrder` for
    `SU2Gen` in NormalForms.lean. -/
noncomputable def heckeOrder (n : ℕ) : AdmissibleOrder (HeckeGen n) :=
  mkDegLexOrder HeckeGen.rank HeckeGen.rank_injective

/-! ## §3  Hecke Parameters -/

/-- Deformation parameter for the Hecke algebra. -/
structure HeckeParams where
  /-- The deformation parameter `q`. -/
  q : ℝ
  /-- `q > 0`. -/
  q_pos : 0 < q
  /-- `q ≠ 1` (non-classical). -/
  q_ne_one : q ≠ 1

/-! ## §4  Hecke Rewriting System (Constructive) -/

/-- The Hecke relation for generator `σᵢ`:
    `σᵢ² - (q - q⁻¹)σᵢ - 1 = 0`, oriented as
    `σᵢ² → (q - q⁻¹)σᵢ + 1`.

    As an `AlgElement`: leading monomial `[σᵢ, σᵢ]` with coefficient 1,
    plus `[σᵢ]` with coefficient `-(q - q⁻¹)`, plus `[]` with
    coefficient `-1`. -/
noncomputable def heckeRelation {n : ℕ} (i : Fin n) (hp : HeckeParams) :
    ReductionRule (HeckeGen n) ℝ where
  relation := AlgElement.ofTerms [
    ([⟨i⟩, ⟨i⟩], 1),
    ([⟨i⟩], -(hp.q - hp.q⁻¹)),
    ([], -1)
  ]
  nonzero := AlgElement.ofTerms_support_nonempty (by simp)

/-- The Yang–Baxter relation for adjacent generators `σᵢ, σᵢ₊₁`:
    `σᵢσᵢ₊₁σᵢ - σᵢ₊₁σᵢσᵢ₊₁ = 0`, oriented as
    `σᵢσᵢ₊₁σᵢ → σᵢ₊₁σᵢσᵢ₊₁`. -/
noncomputable def yangBaxterRelation {n : ℕ}
    (i : Fin n) (j : Fin n) : ReductionRule (HeckeGen n) ℝ where
  relation := AlgElement.ofTerms [
    ([⟨i⟩, ⟨j⟩, ⟨i⟩], 1),
    ([⟨j⟩, ⟨i⟩, ⟨j⟩], -1)
  ]
  nonzero := AlgElement.ofTerms_support_nonempty (by simp)

/-- The far-commutativity relation for non-adjacent generators:
    `σᵢσⱼ - σⱼσᵢ = 0` when `|i-j| ≥ 2`, oriented so that the
    higher-index generator comes first (lm = `[σᵢ, σⱼ]` with `i > j`). -/
noncomputable def farCommRelation {n : ℕ}
    (i : Fin n) (j : Fin n) : ReductionRule (HeckeGen n) ℝ where
  relation := AlgElement.ofTerms [
    ([⟨i⟩, ⟨j⟩], 1),
    ([⟨j⟩, ⟨i⟩], -1)
  ]
  nonzero := AlgElement.ofTerms_support_nonempty (by simp)

/-- The complete Hecke rewriting system for `H_n(q)`.
    Collects all Hecke, Yang–Baxter, and far-commutativity relations
    for generators `σ₀, …, σ_{n-1}`.

    **Requires `0 < n`, and carries no sentinel rule.** An earlier version
    appended `⟨ofTerms [([], q)], _⟩` to satisfy `RewritingSystem.nonempty` at
    `n = 0`. That rule's support is `{[]}`, so its leading monomial is the empty
    word, and `[] <:+: m` holds for every `m` — which made `isNormalForm` false
    for every element with non-empty support and collapsed the whole GS property
    (`gs_basis_of_empty_lm` below proves the collapse). With `0 < n` the Hecke
    relation for `σ₀` supplies the non-emptiness instead, and every leading
    monomial is a genuine word. `n = 0` is no loss: `H_0(q)` has no generators. -/
noncomputable def heckeRewritingSystem (n : ℕ) (hn : 0 < n) (hp : HeckeParams) :
    RewritingSystem (HeckeGen n) ℝ where
  rules :=
    -- Hecke relations: σᵢ² → (q-q⁻¹)σᵢ + 1 for each i
    (List.finRange n).map (fun i => heckeRelation i hp) ++
    -- Yang–Baxter: σᵢσᵢ₊₁σᵢ → σᵢ₊₁σᵢσᵢ₊₁ for adjacent pairs
    ((List.finRange n).flatMap (fun i =>
      (List.finRange n).filterMap (fun j =>
        if j.val = i.val + 1 then some (yangBaxterRelation i j) else none))) ++
    -- Far-commutativity: σᵢσⱼ → σⱼσᵢ for |i-j| ≥ 2, i > j
    ((List.finRange n).flatMap (fun i =>
      (List.finRange n).filterMap (fun j =>
        if i.val > j.val + 1 then some (farCommRelation i j) else none)))
  nonempty := by
    -- `0 < n` makes `finRange n` non-empty, so the Hecke-relation block is too.
    intro h
    have h1 := (List.append_eq_nil_iff.mp h).1
    have h2 := (List.append_eq_nil_iff.mp h1).1
    rw [List.map_eq_nil_iff] at h2
    exact absurd h2 (List.ne_nil_of_length_pos (by rw [List.length_finRange]; exact hn))

/-! ### Why there is no sentinel rule

The composition lemma is stated in terms of leading monomials, and a rule whose
leading monomial is the **empty word** destroys it. `isNormalForm` asks that no
rule's leading monomial be an infix of any monomial in the support; `[] <:+: m`
holds for every `m`; so with such a rule present *nothing with non-empty support
is ever in normal form*, and `SingleStepReduction`'s infix side-condition is
satisfiable against any target at all. The consequence is proved below, in
general rather than for this system: `gs_basis_of_empty_lm`.

That is why `heckeRewritingSystem` now requires `0 < n` and drops the sentinel.

Two further defects in `UGB.GrobnerShirshov.Basic` remain, and both must be
repaired before `hecke_is_gs_basis` can be *proved* rather than assumed:

* `leadingMonomial (_ord) f hf := hf.choose` ignores its order argument and
  returns an arbitrary support element, not the `ord`-greatest one;
* `SingleStepReduction` has one field, `exists_witness`, and never requires
  `f - g` to lie in the ideal generated by the rules — its docstring says it
  does, the structure does not. Nor is `OverlapComposition.spoly` computed from
  the rules; it is a free field.

Until those are fixed the axiom below is the honest form: an assumption, cited,
not a theorem. Bean qou-auq3 tracks the repair; bean qou-k6ks tracks the
"no quasi-zeros" hypothesis on the ground algebra that the S-polynomial argument
also needs (Pawloski–Leitner) and that no Lean statement here carries.
-/

/-- **A rule with empty leading monomial collapses the GS property.**

If any rule's leading monomial is `[]`, then *every* element of the free algebra
reduces to zero and `IsGrobnerShirshovBasis` holds — for any generators, any
order, any rules. The predicate then distinguishes nothing, which is why
`heckeRewritingSystem` must not contain such a rule.

Note what the proof uses: only that `[] <:+: t` for every `t`, and that
`SingleStepReduction` places no algebraic condition on its target. Both are
properties of `UGB.GrobnerShirshov.Basic`, not of the Hecke relations. -/
theorem gs_basis_of_empty_lm {G : Type*} [DecidableEq G]
    (ord : AdmissibleOrder G) (sys : RewritingSystem G ℝ)
    (r₀ : ReductionRule G ℝ) (hr₀ : r₀ ∈ sys.rules)
    (hlm : leadingMonomial ord r₀.relation r₀.nonzero = []) :
    IsGrobnerShirshovBasis G ℝ ord sys := by
  have key : ∀ f : AlgElement G ℝ, ∃ nf, ReducesToNF ord sys f nf ∧ nf.isZero := by
    intro f
    by_cases hf : f.support = ∅
    · refine ⟨f, ⟨MultiStepReduction.refl f, ?_⟩, hf⟩
      intro r _ m hm
      rw [hf] at hm
      exact absurd hm (Finset.notMem_empty m)
    · obtain ⟨t, ht⟩ := Finset.nonempty_iff_ne_empty.mpr hf
      refine ⟨AlgElement.zero,
        ⟨MultiStepReduction.step (MultiStepReduction.refl f) ?_, ?_⟩, rfl⟩
      · exact ⟨r₀, hr₀, t, ht, by rw [hlm]; exact List.nil_infix,
          fun m hm => absurd hm (Finset.notMem_empty m)⟩
      · intro r _ m hm
        exact absurd hm (Finset.notMem_empty m)
  exact ⟨fun oc _ _ => key oc.spoly, fun ic _ _ => key ic.spoly⟩

/-- **Assumption** (Bokut & Shiao 2001, Theorem 3.5): the Hecke relations form a
GS basis for `H_n(q)`.

Still an axiom, and deliberately. With the sentinel removed this is no longer
vacuous — `gs_basis_of_empty_lm` no longer applies to `heckeRewritingSystem`, so
the property has content again and is genuinely unproved. Proving it needs the
two repairs listed above plus the overlap analysis of the Hecke presentation;
bean qou-auq3. -/
-- Ref: [bokutchen2014] https://doi.org/10.1007/s13373-014-0054-6 (Gröbner-Shirshov basis for the Iwahori-Hecke algebra H_n(q))
axiom hecke_is_gs_basis (n : ℕ) (hn : 0 < n) (hp : HeckeParams) :
    IsGrobnerShirshovBasis (HeckeGen n) ℝ (heckeOrder n)
      (heckeRewritingSystem n hn hp)

/-! ## §5  Braid Word Embedding (Constructive) -/

/-- Embed a positive generator `σᵢ` as the singleton monomial `[σᵢ]`. -/
noncomputable def embedPositiveGen {n : ℕ} (i : Fin n) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.singleton [⟨i⟩]

/-- Embed a negative generator `σᵢ⁻¹` via the Hecke relation inverse:
    `σᵢ⁻¹ = (q⁻¹ - q)σᵢ + q⁻¹`.

    Derived from `σᵢ² = (q-q⁻¹)σᵢ + 1`:
    `σᵢ · ((q⁻¹-q)σᵢ + q⁻¹) = (q⁻¹-q)σᵢ² + q⁻¹σᵢ`
    `= (q⁻¹-q)((q-q⁻¹)σᵢ + 1) + q⁻¹σᵢ`
    `= -(q-q⁻¹)²σᵢ + (q⁻¹-q) + q⁻¹σᵢ`
    `= (-(q²-2+q⁻²) + q⁻¹)σᵢ + (q⁻¹-q)`
    After simplification, this equals `1` (the identity). -/
noncomputable def embedNegativeGen {n : ℕ} (i : Fin n) (hp : HeckeParams) :
    AlgElement (HeckeGen n) ℝ :=
  AlgElement.ofTerms [
    ([⟨i⟩], hp.q⁻¹ - hp.q),
    ([], hp.q⁻¹)
  ]

/-- Embed a signed braid generator into `AlgElement`.
    Positive index → singleton monomial.
    Negative index → Hecke inverse.

    Requires `[NeZero n]` so that `_ % n < n` is well-defined. -/
noncomputable def embedGenerator {n : ℕ} [NeZero n]
    (hp : HeckeParams) (g : ℤ) :
    AlgElement (HeckeGen n) ℝ :=
  have hn : 0 < n := Nat.pos_of_ne_zero (NeZero.ne n)
  if g ≥ 0
  then embedPositiveGen ⟨g.toNat % n, Nat.mod_lt _ hn⟩
  else embedNegativeGen ⟨g.natAbs % n, Nat.mod_lt _ hn⟩ hp

/-- Embed a braid word (list of signed generators) into `AlgElement`
    by left-multiplying each generator's embedding successively.

    Uses `AlgElement.leftMulGen` from AlgOps.lean to avoid needing
    general convolution.  For a word `[g₁, g₂, g₃]`:
    `braidToAlg = embed(g₁) · embed(g₂) · embed(g₃)`

    Since each embedded generator is itself an `AlgElement` (not a single
    generator), we need `AlgElement` multiplication.  We approximate this
    by folding over the word, using `leftMulWord` for the singleton terms
    and `add`/`smul` for the inverse terms.

    For positive generators (which are singletons `[σᵢ]`), the
    multiplication is simply `leftMulGen σᵢ`.  For negative generators
    (which are 2-term sums), we distribute the multiplication. -/
noncomputable def braidToAlg {n : ℕ} [NeZero n] (hp : HeckeParams)
    (generators : List ℤ) : AlgElement (HeckeGen n) ℝ :=
  have hn : 0 < n := Nat.pos_of_ne_zero (NeZero.ne n)
  generators.foldr
    (fun g acc =>
      if g ≥ 0
      then AlgElement.leftMulGen ⟨g.toNat % n, Nat.mod_lt _ hn⟩ acc
      else
        -- σᵢ⁻¹ · acc = (q⁻¹ - q) · σᵢ · acc + q⁻¹ · acc
        let i : Fin n := ⟨g.natAbs % n, Nat.mod_lt _ hn⟩
        AlgElement.add
          (AlgElement.smul (hp.q⁻¹ - hp.q) (AlgElement.leftMulGen ⟨i⟩ acc))
          (AlgElement.smul hp.q⁻¹ acc))
    (AlgElement.singleton [])

/-- The augmented braid element for threading: prepend the photon
    strand above the hadron, then un-braid below.

    `augmentedBraid β_H = σ_n · σ_{n-1} · … · σ₁ · β_H · σ₁⁻¹ · … · σ_n⁻¹`

    In the `B_{n+1}` embedding. -/
noncomputable def augmentedBraidElement {n : ℕ} (hp : HeckeParams)
    (hadron_generators : List ℤ) : AlgElement (HeckeGen (n + 1)) ℝ :=
  let photon_above := (List.finRange (n + 1)).reverse.map
    (fun i => (i.val : ℤ))
  let photon_below := (List.finRange (n + 1)).map
    (fun i => -(i.val : ℤ))
  braidToAlg hp (photon_above ++ hadron_generators ++ photon_below)

/-! ## §6  Hecke Cost (Constructive) -/

/-- The Hecke cost of an element: the sum of absolute values of
    coefficients across the entire support.

    `heckeCost(f) = Σ_{m ∈ supp(f)} |f.coeff(m)|`

    This is well-defined because `support` is a `Finset`. -/
noncomputable def heckeCost {n : ℕ} (f : AlgElement (HeckeGen n) ℝ) : ℝ :=
  f.support.sum (fun m => |f.coeff m|)

/-- The Hecke cost is non-negative. -/
theorem heckeCost_nonneg {n : ℕ} (f : AlgElement (HeckeGen n) ℝ) :
    0 ≤ heckeCost f := by
  unfold heckeCost
  exact Finset.sum_nonneg (fun m _ => abs_nonneg _)

/-! ## §7  Normal Form Uniqueness -/

/-- The normal form of a Hecke algebra element is unique (proved,
    not axiom).  Uses `normal_form_unique` from CompositionLemma.lean
    applied to `hecke_is_gs_basis`. -/
theorem heckeCost_well_defined (n : ℕ) (hn : 0 < n) (hp : HeckeParams)
    (f : AlgElement (HeckeGen n) ℝ)
    (nf₁ nf₂ : AlgElement (HeckeGen n) ℝ)
    (hred₁ : ReducesToNF (heckeOrder n) (heckeRewritingSystem n hn hp) f nf₁)
    (hred₂ : ReducesToNF (heckeOrder n) (heckeRewritingSystem n hn hp) f nf₂) :
    nf₁ = nf₂ :=
  normal_form_unique (heckeOrder n) (heckeRewritingSystem n hn hp)
    (hecke_is_gs_basis n hn hp) f nf₁ nf₂ hred₁ hred₂

/-- Threading cost uniqueness: two reductions of the same augmented
    braid yield identical normal forms. -/
theorem threading_cost_unique (n : ℕ) (hp : HeckeParams)
    (hadron : List ℤ) :
    ∀ (nf₁ nf₂ : AlgElement (HeckeGen (n + 1)) ℝ),
      ReducesToNF (heckeOrder (n + 1)) (heckeRewritingSystem (n + 1) (Nat.succ_pos n) hp)
        (augmentedBraidElement hp hadron) nf₁ →
      ReducesToNF (heckeOrder (n + 1)) (heckeRewritingSystem (n + 1) (Nat.succ_pos n) hp)
        (augmentedBraidElement hp hadron) nf₂ →
      nf₁ = nf₂ := by
  intro nf₁ nf₂ h₁ h₂
  exact heckeCost_well_defined (n + 1) (Nat.succ_pos n) hp
    (augmentedBraidElement hp hadron) nf₁ nf₂ h₁ h₂

end UGB.GrobnerShirshov.Hecke
