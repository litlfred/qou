import UGB.GrobnerShirshov.DiamondLemma

/-!
# Gröbner–Shirshov Composition Lemma (Diamond Lemma)

The **Composition Lemma** (also known as the **Diamond Lemma** for ring
theory, Bergman 1978) is the central result of Gröbner–Shirshov theory:

> A rewriting system `Σ` is confluent (hence yields unique normal forms)
> **if and only if** every S-polynomial of `Σ` reduces to zero.

This module states the lemma and its corollaries using the proper
reduction relations defined in `Basic.lean`:

1. **Termination** — well-founded induction on the admissible order.
2. **Local confluence** — from S-polynomial resolution.
3. **Confluence** — Newman's lemma (termination + local confluence).
4. **Uniqueness of normal forms** — from confluence.
5. **Idempotency of reduce** — the composition lemma itself.
6. **Retraction property** — bridge to `FormalGroups.lean`.

## References

- Bergman, *The diamond lemma for ring theory*, Adv. Math. 29 (1978).
- Bokut, *Imbeddings into simple associative algebras*, Algebra i Logika 15 (1976).
- [fred2005, §3, Proposition 3.8].
-/


namespace UGB.GrobnerShirshov

universe u v

variable {G : Type u} {k : Type v} [Ring k] [DecidableEq G]

/-! ## §1  Termination

`reduction_well_founded` and `normal_form_exists` **moved to `Basic.lean` §6**
(bean qou-lzoo). The termination result (an axiom until 2026-11-20, now a theorem) is stated purely in `Basic`'s vocabulary, and
`normal_form_exists` — now a theorem carrying `∀ r ∈ sys.rules, IsUnit (r.lc ord)`
— needs it in order for `reduce` to be defined there rather than from the false
axiom it replaced. Both remain in the `UGB.GrobnerShirshov` namespace, so uses
elsewhere in this file are unqualified as before. -/

/-- Compatibility alias for the name this theorem carried while it lived here.

    It is now `Basic.normal_form_exists`: once the false axiom of that name was
    removed, the repaired statement could take the plain name, and the `_of_unit_lc`
    suffix stopped earning its keep. Retained so the migration does not break
    references. -/
@[deprecated normal_form_exists (since := "2026-08-10")]
theorem normal_form_exists_of_unit_lc
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (f : AlgElement G k) :
    ∃ nf, ReducesToNF ord sys f nf :=
  normal_form_exists ord sys hlc f

/-! ## §2  Local Confluence from S-Polynomial Resolution

**`local_confluence` was an axiom, and it was false as stated** (bean
`qou-lc7q`). It promised a *structurally equal* common reduct, but a step fixes
its target only up to `CoeffEq` (`support` is a free superset), and
`LocalConfluenceSupportRefutation.local_confluence_structural_false` exhibits
two normal reducts of one element that differ only in `support`. With every
hypothesis satisfiable, the axiom proved `False`.

It is now a **theorem**, up to `CoeffEq`, over a commutative ring, from
`Diamond.reductionUnique` (Bergman 1978, Theorem 1.2, proved in
`DiamondLemma.lean`). `hnqz` is kept in the signature for its callers and is not
used. -/

/-- **Local confluence, up to `CoeffEq`.** Two single steps from `f` lead to
    multi-step reducts that agree coefficientwise. -/
theorem local_confluence {k : Type v} [CommRing k]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (_hnqz : NoQuasiZerosFree G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (f g₁ g₂ : AlgElement G k)
    (h₁ : SingleStepReduction ord sys f g₁)
    (h₂ : SingleStepReduction ord sys f g₂) :
    ∃ (h₁' h₂' : AlgElement G k),
      MultiStepReduction ord sys g₁ h₁' ∧
      MultiStepReduction ord sys g₂ h₂' ∧ AlgElement.CoeffEq h₁' h₂' := by
  obtain ⟨n₁, hn₁⟩ := normal_form_exists ord sys hlc g₁
  obtain ⟨n₂, hn₂⟩ := normal_form_exists ord sys hlc g₂
  exact ⟨n₁, n₂, hn₁.reduces, hn₂.reduces,
    Diamond.reductionUnique ord sys hgs hlc f n₁ n₂
      ⟨MultiStepReduction.head h₁ hn₁.reduces, hn₁.is_normal⟩
      ⟨MultiStepReduction.head h₂ hn₂.reduces, hn₂.is_normal⟩⟩

/-! ## §3  Confluence (Newman's Lemma) -/

/-- **Newman's lemma**, in the form the induction actually needs: local
    confluence plus accessibility of `f` under reduction gives confluence at `f`.

    The hypothesis is taken as a plain function rather than as
    `IsGrobnerShirshovBasis`, because nothing in the argument looks at *why* the
    system is locally confluent — this is the abstract rewriting content, and
    keeping it separate is what makes `confluence` below a one-line instantiation.

    The proof is the standard tiling argument. Given `x →* g₁` and `x →* g₂`,
    expose the first step of each (`MultiStepReduction.cases_head`); if either run
    is empty the other is the common reduct. Otherwise `x → a →* g₁` and
    `x → b →* g₂`, and:

    * local confluence at the fork `a ← x → b` gives `c` with `a →* c`, `b →* c`;
    * the induction hypothesis at `a` — legitimate because `x → a` — applied to
      `a →* g₁` and `a →* c` gives `d` with `g₁ →* d` and `c →* d`;
    * the induction hypothesis at `b`, applied to `b →* g₂` and `b →* c →* d`,
      gives `e` with `g₂ →* e` and `d →* e`.

    Then `e` is the common reduct: `g₁ →* d →* e` and `g₂ →* e`. Note that the
    two induction steps are *not* symmetric — the second consumes the output of
    the first — which is why local confluence alone does not suffice and
    termination is doing real work.

    Reference: Newman (1942); Bergman 1978, Corollary to Theorem 1.2. -/
theorem newman
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hlc : ∀ f g₁ g₂ : AlgElement G k,
      SingleStepReduction ord sys f g₁ → SingleStepReduction ord sys f g₂ →
      ∃ h, MultiStepReduction ord sys g₁ h ∧ MultiStepReduction ord sys g₂ h)
    (f : AlgElement G k)
    (hacc : Acc (fun g h => SingleStepReduction ord sys h g) f) :
    ∀ g₁ g₂ : AlgElement G k,
      MultiStepReduction ord sys f g₁ → MultiStepReduction ord sys f g₂ →
      ∃ h, MultiStepReduction ord sys g₁ h ∧ MultiStepReduction ord sys g₂ h := by
  induction hacc with
  | intro x _ ih =>
    intro g₁ g₂ h₁ h₂
    rcases h₁.cases_head with rfl | ⟨a, hxa, hag₁⟩
    · exact ⟨g₂, h₂, MultiStepReduction.refl _⟩
    rcases h₂.cases_head with rfl | ⟨b, hxb, hbg₂⟩
    · exact ⟨g₁, MultiStepReduction.refl _, MultiStepReduction.head hxa hag₁⟩
    obtain ⟨c, hac, hbc⟩ := hlc _ a b hxa hxb
    obtain ⟨d, hg₁d, hcd⟩ := ih a hxa g₁ c hag₁ hac
    obtain ⟨e, hg₂e, hde⟩ := ih b hxb g₂ d hbg₂ (hbc.trans hcd)
    exact ⟨e, hg₁d.trans hde, hg₂e⟩

/-- **Confluence, up to `CoeffEq`**: any two multi-step reducts of the same
    element have multi-step reducts that agree coefficientwise.

    Restated 2026-11-20 (bean `qou-lc7q`). It used to promise a structurally
    equal common reduct, via `newman` from the false structural
    `local_confluence`; that form is false for the same reason. It now follows
    directly from `Diamond.reductionUnique`: normal forms of `g₁` and `g₂` are
    normal forms of `f`. `newman` above is kept: it is correct, and it is the
    abstract rewriting fact. -/
theorem confluence {k : Type v} [CommRing k]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (_hnqz : NoQuasiZerosFree G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (f g₁ g₂ : AlgElement G k)
    (h₁ : MultiStepReduction ord sys f g₁)
    (h₂ : MultiStepReduction ord sys f g₂) :
    ∃ (h₁' h₂' : AlgElement G k),
      MultiStepReduction ord sys g₁ h₁' ∧
      MultiStepReduction ord sys g₂ h₂' ∧ AlgElement.CoeffEq h₁' h₂' := by
  obtain ⟨n₁, hn₁⟩ := normal_form_exists ord sys hlc g₁
  obtain ⟨n₂, hn₂⟩ := normal_form_exists ord sys hlc g₂
  exact ⟨n₁, n₂, hn₁.reduces, hn₂.reduces,
    Diamond.reductionUnique ord sys hgs hlc f n₁ n₂
      ⟨h₁.trans hn₁.reduces, hn₁.is_normal⟩ ⟨h₂.trans hn₂.reduces, hn₂.is_normal⟩⟩

/-! ## §4  Uniqueness of Normal Forms -/

/-- **Uniqueness of normal forms, up to `CoeffEq`**: if `f →* nf₁` and
    `f →* nf₂` with both normal, then `nf₁` and `nf₂` agree coefficientwise.

    Restated 2026-11-20 (bean `qou-lc7q`). It concluded `nf₁ = nf₂`, which is
    false: a normal form is fixed only up to its `support` field
    (`LocalConfluenceSupportRefutation`). `CoeffEq` is equality of the elements
    of the free algebra, which is what the mathematics says.

    Justified by Bergman 1978, Theorem 1.2, proved in `DiamondLemma.lean`. -/
theorem normal_form_unique
    {G : Type u} {k : Type v} [CommRing k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (_hnqz : NoQuasiZerosFree G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (f nf₁ nf₂ : AlgElement G k)
    (hred₁ : ReducesToNF ord sys f nf₁)
    (hred₂ : ReducesToNF ord sys f nf₂)
    : AlgElement.CoeffEq nf₁ nf₂ :=
  Diamond.reductionUnique ord sys hgs hlc f nf₁ nf₂ hred₁ hred₂

/-! ## §5  The Composition Lemma (Main Theorem) -/

/-- **The Composition Lemma** (Shirshov 1962, Bokut 1976, Bergman 1978):

    The reduction map is **idempotent**: `reduce (reduce f) = reduce f`.

    Proof: `reduce f` is in normal form (by `reduce_is_normal`), and a normal
    form admits no step, so the only reduct of `reduce f` is itself
    (`MultiStepReduction.eq_of_isNormalForm`).

    **Corrected 2026-11-20 (bean `qou-lc7q`).** This used to route through
    `normal_form_unique` and said `hgs` makes the value canonical. Idempotency
    needs no uniqueness theorem and no GS hypothesis: `_hgs` and `_hnqz` are
    unused and kept only for callers. What the GS hypothesis buys is
    `normal_form_unique` (normal forms agree up to `CoeffEq`), which is the
    basis statement, not this one. `hlc` is still what makes `reduce` defined. -/
theorem composition_lemma
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (_hgs : IsGrobnerShirshovBasis G k ord sys)
    (_hnqz : NoQuasiZerosFree G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) :
    ∀ (f : AlgElement G k),
      reduce ord sys hlc (reduce ord sys hlc f) = reduce ord sys hlc f := by
  intro f
  set nf := reduce ord sys hlc f
  set nf' := reduce ord sys hlc nf
  -- nf is in normal form
  have h_nf_normal := reduce_is_normal ord sys hlc f
  -- nf' is in normal form
  have h_nf'_normal := reduce_is_normal ord sys hlc nf
  -- nf reduces to itself (zero steps, already normal)
  have h_nf_self : ReducesToNF ord sys nf nf :=
    ⟨MultiStepReduction.refl nf, h_nf_normal⟩
  -- nf' is a normal form of nf (via reduce)
  have h_nf'_red : ReducesToNF ord sys nf nf' :=
    ⟨reduce_reduces ord sys hlc nf, h_nf'_normal⟩
  -- `nf` is normal, so its only reduct is itself (no uniqueness theorem needed)
  exact MultiStepReduction.eq_of_isNormalForm h_nf_normal h_nf'_red.reduces

/-! ## §6  Retraction Property (Bridge to FormalGroups.lean) -/

/-- The retraction property `reduce ∘ embed ∘ reduce = reduce`
    needed by `FormalGroups.GrobnerShirshovBasis.composition_lemma`.

    If `embed` is the identity on reduced elements, then the property
    follows from idempotency of `reduce`. -/
theorem retraction_property
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (hnqz : NoQuasiZerosFree G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (embed : AlgElement G k → AlgElement G k)
    (h_embed : ∀ f, embed (reduce ord sys hlc f) = reduce ord sys hlc f) :
    ∀ (f : AlgElement G k),
      reduce ord sys hlc (embed (reduce ord sys hlc f)) =
      reduce ord sys hlc f := by
  intro f
  rw [h_embed]
  exact composition_lemma ord sys hgs hnqz hlc f

end UGB.GrobnerShirshov
