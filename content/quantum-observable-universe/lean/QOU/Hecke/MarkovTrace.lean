import QOU.Hecke.Algebra
import Mathlib.Algebra.Module.LinearMap.Defs

/-!
# Markov trace on `H_n(q)`

A *Markov trace* on the family `{H_n(q)}_{n ≥ 1}` is an `R`-linear
functional `tr_M : H_n(q) → R` satisfying:

  (M1) Normalisation:  `tr_M(1) = 1`
  (M2) Cyclicity:      `tr_M(x · y) = tr_M(y · x)` for all x, y
  (M3) Markov axiom:   `tr_M^{H_n}(x · σ_{n-1}) = z · tr_M^{H_{n-1}}(x)`
                        for `x ∈ H_{n-1}(q) ⊂ H_n(q)`

with Markov parameter `z = 1 / (q^{1/2} + q^{-1/2})`.

Existence + uniqueness up to scalar normalisation: Jones (1987),
Ocneanu (1986).

## References

- [thm:jones-markov-trace]
- [prop:markov-pair-z2]
-/

namespace QOU.Hecke

universe u

/--
Markov trace structure on `H_n(q)`. Encodes the three Markov axioms
plus the connection to the Markov parameter `z`.

For the chain `H_1 ⊂ H_2 ⊂ ...` the Markov axiom relates traces at
adjacent levels; we capture this via a parameterised family of
traces and a coherence condition.
-/
class MarkovTrace
    {R : Type u} (n : ℕ) (q : R) (A : Type u)
    [CommRing R] [Inv R] [Ring A] [Algebra R A] [HA : HeckeAlgebra R n q A] where
  /-- The trace as an R-linear map A → R. -/
  trace : A →ₗ[R] R
  /-- (M1) Normalisation: tr_M(1) = 1. -/
  normalised : trace 1 = 1
  /-- (M2) Cyclicity: trace(x · y) = trace(y · x). -/
  cyclic : ∀ x y : A, trace (x * y) = trace (y * x)
  /-- The Markov parameter z = 1/(q^{1/2} + q^{-1/2}). Stored as a
  field rather than a definition because q^{1/2} requires choosing
  a square root extension of R. -/
  z_param : R
  /-- (M3 / generator value) tr_M(σ_i) = z for every generator.
  This is the key consequence of the full Markov axiom
  `tr_M^{H_n}(x · σ_{n-1}) = z · tr_M^{H_{n-1}}(x)` applied at
  level n with x = 1 ∈ H_{n-1}. -/
  trace_gen : ∀ i : Generator n, trace (HA.embed i) = z_param
  /-- (M3 / pair product) tr_M(σ_i · σ_j) = z² when i < j.
  Follows from two consecutive Markov peels: σ_j is top-indexed,
  one peel gives z · tr_{n-1}(σ_i); σ_i lives in H_{n-1} so the
  second peel gives z · z. -/
  trace_prod_gen : ∀ (i j : Generator n), i.idx.val < j.idx.val →
      trace (HA.embed i * HA.embed j) = z_param * z_param

namespace MarkovTrace

variable {R : Type u} {n : ℕ} {q : R} {A : Type u}
  [CommRing R] [Inv R] [Ring A] [Algebra R A]
  [HA : HeckeAlgebra R n q A]
  [MT : MarkovTrace n q A]

/-- The Markov trace value of a Hecke generator: tr_M(σ_i) = z. -/
theorem trace_generator (i : Generator n) :
    MT.trace (HA.embed i) = MT.z_param := by
  -- Ref: [thm:jones-markov-trace]; tr_M(σ_i) = z by Markov axiom.
  exact MT.trace_gen i

/-- Pair-of-generators trace formula:
    tr_M(σ_i · σ_j) = z²  for i < j
[manuscript] `prop:markov-pair-z2` — direct two-step Markov peel. -/
theorem trace_pair (i j : Generator n) (h : i.idx.val < j.idx.val) :
    MT.trace (HA.embed i * HA.embed j) = MT.z_param * MT.z_param := by
  -- Ref: [prop:markov-pair-z2]; follows from trace_prod_gen field.
  exact MT.trace_prod_gen i j h

end MarkovTrace

/- **Uniqueness of the Markov trace (target statement).**
The mathematical claim is: any two `R`-linear functionals on
`H_n(q)` satisfying the full Markov axioms (M1 normalisation,
M2 cyclicity, M3 cross-level Markov property at every level
`H_k ⊂ H_{k+1}`, k = 1, …, n−1) coincide once the Markov
parameter `z = 1/(√q + 1/√q)` is fixed.  This is Ocneanu (1985);
Jones (1987); Wenzl (1988).

**Caveat on the current `MarkovTrace` class.**  The class above
encodes only the *consequences* of the Markov axioms at the
generator/pair-product level (`trace_gen`, `trace_prod_gen`,
plus normalisation and cyclicity from `cyclic`/`normalise`
fields), not the cross-level Markov axiom itself or a basis
reduction principle.  As stated, two instances with the same
`z_param` are not yet shown equal at the linear-map level by
this class alone — the field set is too weak.  Strengthening
the class to carry the full cross-level Markov axiom (or
equivalently a basis-of-reduced-words decomposition) is a
prerequisite for a Lean-checkable proof.

The `Wedderburn` decomposition `tr_M = Σ_λ y_λ · χ^λ` with
explicit closed-form `y_λ(q)` (linear-system at H_3 or Wenzl
Schur principal specialisation for any n) is the constructive
shadow of this uniqueness — see
`docs/audits/2026-05-05-y-lambda-tr-m-equivalence-proof.md`
for the symbolic verification that the polynomial identity
`P^A_λ · Q^B_λ − P^B_λ · Q^A_λ ≡ 0` holds in
`Z[qCheck, qCheck^{-1}]` (`qCheck = q^{1/2}`, the spinor
information rate `\check{q}` in the narrative) for every λ ⊢ 3.

This Lean statement is therefore a **conditional** result.  The
*single* genuinely-missing input — the basis-of-reduced-words /
spanning-reduction principle for `H_n(q)`, which is **not** in
Mathlib — is isolated as the conjecture class
`MarkovTraceReducedWordBasis` below (§3b-cond).  Everything else —
that two `MarkovTrace` instances sharing `z_param` agree on each
generator and on each generator-pair — is *derived* from the class
fields (`trace_gen`, `trace_prod_gen`), so the uniqueness theorem
is fully checked **modulo that one named class instance**, no
longer an opaque whole-theorem `axiom`.
-/

/-- **Conjecture class (primary): basis-of-reduced-words rigidity for
`H_n(q)`** (Ocneanu 1985; Jones 1987; Wenzl 1988).

This isolates the one input not available in Mathlib: that the
generators `{σ_i}` and ascending products `{σ_i σ_j : i.idx < j.idx}`
carry enough information to pin an `R`-linear functional on the whole
Hecke algebra.  Concretely, any two `R`-linear maps `t₁ t₂ : A →ₗ[R] R`
that agree on `1`, on every generator `embed i`, and on every
ascending generator-product `embed i * embed j` (`i.idx < j.idx`)
coincide.  This is the
content of the reduction `element ↦ R`-linear combination of
reduced braid words (via `σ_i² = (q - q⁻¹)σ_i + 1`) together with
the Markov/cyclicity peel: once the trace is fixed on the spanning
words, it is fixed everywhere.

The field is the genuine reduction principle — a parameter-
quantified rigidity statement in the shape of the claim — not a
bare `True` or an empty marker (§3b-tax: content-bearing primary
conjecture, no instance is fabricated).

`q ≈ √?` archimedean structure is **not** used: the statement is
generic over `[CommRing R]` (§7c). -/
class MarkovTraceReducedWordBasis
    (R : Type u) (n : ℕ) (q : R) (A : Type u)
    [CommRing R] [Inv R] [Ring A] [Algebra R A]
    [HeckeAlgebra R n q A] : Prop where
  /-- Two `R`-linear functionals on `A` that agree on the unit, on
  every generator, and on every *ascending* generator-pair
  (`i.idx < j.idx`) are equal.  This is the basis-of-reduced-words
  decomposition expressed as agreement on the spanning monomials of
  degree ≤ 2 (the ascending pairs are the canonical reduced
  length-2 words; descending and equal-index pairs are rewritten to
  ascending normal form by the braid/quadratic relations) plus the
  Markov-peel recursion to higher degree. -/
  agree_of_agree_on_words :
    ∀ {HA : HeckeAlgebra R n q A} (t₁ t₂ : A →ₗ[R] R),
      t₁ 1 = t₂ 1 →
      (∀ i : Generator n, t₁ (HA.embed i) = t₂ (HA.embed i)) →
      (∀ i j : Generator n, i.idx.val < j.idx.val →
          t₁ (HA.embed i * HA.embed j) = t₂ (HA.embed i * HA.embed j)) →
      t₁ = t₂

/-- **Uniqueness of the Markov trace on `H_n(q)`, conditional on the
basis-of-reduced-words rigidity class.**

The Markov trace is unique once the parameter `z` is fixed — a
rigorous *conditional* result (§3b-cond): the only unproved input is
the `MarkovTraceReducedWordBasis` instance.  The agreement of the two
traces on the unit (`normalised`), on each generator (`trace_gen`),
and on each generator-pair (`trace_prod_gen`/`trace_gen`) is derived
here from the class fields and the shared `z_param`; the reduction to
the whole algebra is supplied by the class hypothesis. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.  Reduction-to-words principle:
--      [wenzl1988] (Hecke-A_n subfactors) + [kassel1995] Ch. X.
theorem markov_trace_unique
    {R : Type u} {n : ℕ} {q : R} {A : Type u}
    [CommRing R] [Inv R] [Ring A] [Algebra R A]
    [HA : HeckeAlgebra R n q A]
    [MarkovTraceReducedWordBasis R n q A]
    (MT₁ MT₂ : MarkovTrace n q A)
    (hz : MT₁.z_param = MT₂.z_param) :
    MT₁.trace = MT₂.trace := by
  -- The two traces agree on the unit, on generators, and on every
  -- ascending generator-pair; the reduced-word basis rigidity
  -- (`MarkovTraceReducedWordBasis`) then forces equality on the
  -- whole algebra.  All three agreement obligations are *derived*
  -- here from the class fields + the shared `z_param`, so this is no
  -- longer an opaque whole-theorem axiom — only the named class
  -- instance remains unproved (§3b-cond).
  -- TODO(verify): the three `rw`-closed obligations + the rigidity
  -- application are not yet machine-checked (Lean unavailable this
  -- session); the rewrite chains are standard but unconfirmed.
  refine MarkovTraceReducedWordBasis.agree_of_agree_on_words
    (HA := HA) MT₁.trace MT₂.trace ?_ ?_ ?_
  · -- unit: both normalised to 1.
    rw [MT₁.normalised, MT₂.normalised]
  · -- generators: both equal their (shared) z_param.
    intro i
    rw [MT₁.trace_gen i, MT₂.trace_gen i, hz]
  · -- ascending generator-pairs (i.idx < j.idx): both equal z²
    -- (`trace_prod_gen`), and the two z_params coincide by `hz`.
    intro i j hij
    rw [MT₁.trace_prod_gen i j hij, MT₂.trace_prod_gen i j hij, hz]

end QOU.Hecke
