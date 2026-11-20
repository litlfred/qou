import UGB.GrobnerShirshov.Basic

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
(bean qou-lzoo). The axiom is stated purely in `Basic`'s vocabulary, and
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

/-! ## §2  Local Confluence from S-Polynomial Resolution -/

/-- **Local confluence**: if all S-polynomials reduce to zero (i.e., the
    system is a GS basis), then whenever `f → g₁` and `f → g₂` by
    single-step reductions, there exists `h` with `g₁ →* h` and `g₂ →* h`.

    Axiomatised because the three-case proof (disjoint / overlap / inclusion)
    requires `AlgElement` subtraction to form the S-polynomial `g₁ - g₂`,
    which is not available at the abstract level.  The argument is:
    - **Disjoint sites**: both reductions commute; apply each to the other's result.
    - **Overlap**: `g₁ - g₂` is an overlap S-polynomial, which reduces to zero
      by `hgs.overlap_resolves`.
    - **Inclusion**: `g₁ - g₂` is an inclusion S-polynomial, which reduces to zero
      by `hgs.inclusion_resolves`.

    Reference: Bergman 1978, §3, proof of Theorem 1.2 (the Diamond Lemma).

    **`hlc` added 2026-11-15.** Without unit leading coefficients the
    statement is false: `LocalConfluenceRefutation.local_confluence_false`
    gives a one-rule GS basis over `ℤ` (relation `2K + 1`) and an element
    `2·K E₊ K` whose two reducts `−E₊K` and `−K E₊` are both stuck. Bergman's
    theorem is for monic (unit-lc) rules, which is what `hlc` records. -/
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5 §3 Thm 1.2 (local confluence from S-polynomial resolution)
axiom local_confluence
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (hnqz : NoQuasiZerosFree G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (f g₁ g₂ : AlgElement G k)
    (h₁ : SingleStepReduction ord sys f g₁)
    (h₂ : SingleStepReduction ord sys f g₂) :
    ∃ (h : AlgElement G k),
      MultiStepReduction ord sys g₁ h ∧
      MultiStepReduction ord sys g₂ h

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

/-- **Confluence**: any two multi-step reducts of the same element have a common
    reduct.

    Was an axiom. It is not one: it is `newman` applied to `local_confluence`
    (§2, still an axiom) and `reduction_well_founded` (a theorem since
    2026-11-20, `Basic.lean`), and those two are the only inputs it ever
    needed. The previous docstring's reason for
    axiomatising — that an explicit derivation-height measure on
    `MultiStepReduction` was missing — is not in fact what the argument induct
    on; it inducts on the accessibility of the *source*, which §1 already
    supplies. `MultiStepReduction.cases_head` is the one piece that was missing,
    and it is three lines. -/
theorem confluence
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (hnqz : NoQuasiZerosFree G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (f g₁ g₂ : AlgElement G k)
    (h₁ : MultiStepReduction ord sys f g₁)
    (h₂ : MultiStepReduction ord sys f g₂) :
    ∃ (h : AlgElement G k),
      MultiStepReduction ord sys g₁ h ∧
      MultiStepReduction ord sys g₂ h :=
  newman ord sys (fun _ _ _ s₁ s₂ => local_confluence ord sys hgs hnqz hlc _ _ _ s₁ s₂)
    f (reduction_well_founded ord sys f) g₁ g₂ h₁ h₂

/-! ## §4  Uniqueness of Normal Forms -/

/-- **Uniqueness of normal forms**: if `f →* nf₁` and `f →* nf₂`
    where both `nf₁` and `nf₂` are in normal form, then `nf₁ = nf₂`.

    Proof: by confluence, `nf₁` and `nf₂` have a common reduct `h`.
    Since both are in normal form (no reduction applies), `h = nf₁`
    and `h = nf₂`, hence `nf₁ = nf₂`.

    Was an axiom. Its own docstring gave the two-line proof and then listed as
    the reason for axiomatising exactly the two things that are available:
    confluence (§3, now a theorem) and irreducibility of normal forms
    (`MultiStepReduction.eq_of_isNormalForm`, proved in `Basic.lean` since the
    reduction relation was repaired).

    Justified by Bergman 1978, Theorem 1.2. -/
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5 Thm 1.2 (uniqueness of normal forms from confluence)
theorem normal_form_unique
    {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (hnqz : NoQuasiZerosFree G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord))
    (f nf₁ nf₂ : AlgElement G k)
    (hred₁ : ReducesToNF ord sys f nf₁)
    (hred₂ : ReducesToNF ord sys f nf₂)
    : nf₁ = nf₂ := by
  obtain ⟨h, hh₁, hh₂⟩ :=
    confluence ord sys hgs hnqz hlc f nf₁ nf₂ hred₁.reduces hred₂.reduces
  exact (MultiStepReduction.eq_of_isNormalForm hred₁.is_normal hh₁).symm.trans
    (MultiStepReduction.eq_of_isNormalForm hred₂.is_normal hh₂)

/-! ## §5  The Composition Lemma (Main Theorem) -/

/-- **The Composition Lemma** (Shirshov 1962, Bokut 1976, Bergman 1978):

    The reduction map is **idempotent**: `reduce (reduce f) = reduce f`.

    This encodes the forward direction of the diamond lemma: a GS basis
    (all S-polynomials reduce to zero) implies that normal-form monomials
    form a `k`-basis of the quotient `k⟨G⟩ / (Σ)`.

    Proof: `reduce f` is in normal form (by `reduce_is_normal`), so it
    reduces to itself in zero steps.  By `normal_form_unique`, the
    chosen normal form of `reduce f` must equal `reduce f`.

    Carries `hlc` (unit leading coefficients) since `reduce` does — see
    `Basic.lean` §6. Both hypotheses are load-bearing and for different reasons:
    `hlc` is what makes `reduce` defined at all, `hgs` is what makes its value
    canonical. -/
theorem composition_lemma
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (hnqz : NoQuasiZerosFree G k)
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
  -- By uniqueness: nf' = nf
  exact normal_form_unique ord sys hgs hnqz hlc nf nf' nf h_nf'_red h_nf_self

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
