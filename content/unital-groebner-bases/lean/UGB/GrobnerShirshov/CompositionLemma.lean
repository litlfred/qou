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

/-! ## §1  Termination -/

/-- Every sequence of single-step reductions is finite: the reduction
    relation is well-founded.

    Each `SingleStepReduction` strictly decreases the multiset of
    monomials in the support under the Dershowitz–Manna ordering,
    which inherits well-foundedness from `ord.wf`.

    Axiomatised because the proof requires:
    1. A `Multiset (Monomial G)` representation of `AlgElement` support
    2. A proof that `SingleStepReduction` strictly decreases this multiset
       under `ord.lt`
    3. The Dershowitz–Manna theorem (`Multiset.wellFoundedLT`) lifting
       element well-foundedness to multiset well-foundedness

    These components require `AlgElement` subtraction and support extraction
    operations that are not available at the abstract level.

    Reference: Bergman 1978, §2, proof of Theorem 1.1 (termination). -/
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5 §2 Thm 1.1 (reduction is well-founded / terminating)
axiom reduction_well_founded
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k) :
    ∀ (f : AlgElement G k), Acc (fun g h => SingleStepReduction ord sys h g) f

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

    Reference: Bergman 1978, §3, proof of Theorem 1.2 (the Diamond Lemma). -/
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5 §3 Thm 1.2 (local confluence from S-polynomial resolution)
axiom local_confluence
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (f g₁ g₂ : AlgElement G k)
    (h₁ : SingleStepReduction ord sys f g₁)
    (h₂ : SingleStepReduction ord sys f g₂) :
    ∃ (h : AlgElement G k),
      MultiStepReduction ord sys g₁ h ∧
      MultiStepReduction ord sys g₂ h

/-! ## §3  Confluence (Newman's Lemma) -/

/-- **Newman's lemma**: a terminating, locally confluent rewriting
    system is confluent.

    Since our reduction terminates (§1) and is locally confluent when
    all S-polynomials resolve (§2), any two multi-step reducts of the
    same element have a common reduct.

    Axiomatised because the full proof requires well-founded induction
    on `MultiStepReduction` derivation height, composing local confluence
    at each fork.  The argument is entirely standard (Newman 1942) and
    has been verified in Lean's `Mathlib.Order.WellFounded` for abstract
    relations; instantiating it here requires an explicit derivation-height
    measure on `MultiStepReduction` that we do not carry.

    Reference: Newman (1942); Bergman 1978, Corollary to Theorem 1.2. -/
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5 Cor. to Thm 1.2 (Newman's lemma: termination + local confluence ⟹ confluence)
axiom confluence
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (f g₁ g₂ : AlgElement G k)
    (h₁ : MultiStepReduction ord sys f g₁)
    (h₂ : MultiStepReduction ord sys f g₂) :
    ∃ (h : AlgElement G k),
      MultiStepReduction ord sys g₁ h ∧
      MultiStepReduction ord sys g₂ h

/-! ## §4  Uniqueness of Normal Forms -/

/-- **Uniqueness of normal forms**: if `f →* nf₁` and `f →* nf₂`
    where both `nf₁` and `nf₂` are in normal form, then `nf₁ = nf₂`.

    Proof: by confluence, `nf₁` and `nf₂` have a common reduct `h`.
    Since both are in normal form (no reduction applies), `h = nf₁`
    and `h = nf₂`, hence `nf₁ = nf₂`.

    Axiomatised because the full proof requires:
    1. Confluence (which depends on algebra operations for S-poly reduction).
    2. The fact that normal forms are irreducible under →.

    Justified by Bergman 1978, Theorem 1.2. -/
-- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5 Thm 1.2 (uniqueness of normal forms from confluence)
axiom normal_form_unique
    {G : Type u} {k : Type v} [Ring k] [DecidableEq G]
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (f nf₁ nf₂ : AlgElement G k)
    (hred₁ : ReducesToNF ord sys f nf₁)
    (hred₂ : ReducesToNF ord sys f nf₂)
    : nf₁ = nf₂

/-! ## §5  The Composition Lemma (Main Theorem) -/

/-- **The Composition Lemma** (Shirshov 1962, Bokut 1976, Bergman 1978):

    The reduction map is **idempotent**: `reduce (reduce f) = reduce f`.

    This encodes the forward direction of the diamond lemma: a GS basis
    (all S-polynomials reduce to zero) implies that normal-form monomials
    form a `k`-basis of the quotient `k⟨G⟩ / (Σ)`.

    Proof: `reduce f` is in normal form (by `reduce_is_normal`), so it
    reduces to itself in zero steps.  By `normal_form_unique`, the
    chosen normal form of `reduce f` must equal `reduce f`. -/
theorem composition_lemma
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys) :
    ∀ (f : AlgElement G k),
      reduce ord sys hgs (reduce ord sys hgs f) = reduce ord sys hgs f := by
  intro f
  set nf := reduce ord sys hgs f
  set nf' := reduce ord sys hgs nf
  -- nf is in normal form
  have h_nf_normal := reduce_is_normal ord sys hgs f
  -- nf' is in normal form
  have h_nf'_normal := reduce_is_normal ord sys hgs nf
  -- nf reduces to itself (zero steps, already normal)
  have h_nf_self : ReducesToNF ord sys nf nf :=
    ⟨MultiStepReduction.refl nf, h_nf_normal⟩
  -- nf' is a normal form of nf (via reduce)
  have h_nf'_red : ReducesToNF ord sys nf nf' :=
    ⟨reduce_reduces ord sys hgs nf, h_nf'_normal⟩
  -- By uniqueness: nf' = nf
  exact normal_form_unique ord sys hgs nf nf' nf h_nf'_red h_nf_self

/-! ## §6  Retraction Property (Bridge to FormalGroups.lean) -/

/-- The retraction property `reduce ∘ embed ∘ reduce = reduce`
    needed by `FormalGroups.GrobnerShirshovBasis.composition_lemma`.

    If `embed` is the identity on reduced elements, then the property
    follows from idempotency of `reduce`. -/
theorem retraction_property
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (embed : AlgElement G k → AlgElement G k)
    (h_embed : ∀ f, embed (reduce ord sys hgs f) = reduce ord sys hgs f) :
    ∀ (f : AlgElement G k),
      reduce ord sys hgs (embed (reduce ord sys hgs f)) =
      reduce ord sys hgs f := by
  intro f
  rw [h_embed]
  exact composition_lemma ord sys hgs f

end UGB.GrobnerShirshov
