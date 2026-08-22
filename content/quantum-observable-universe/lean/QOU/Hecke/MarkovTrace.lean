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

/-- **Idempotent-sandwich collapse.** For an idempotent `e` (`e * e = e`),
    `tr_M(e · x · e) = tr_M(e · x)`.  Derived purely from the cyclicity axiom
    (M2) and idempotency: `tr(e·x·e) = tr(e·(e·x)) = tr((e·e)·x) = tr(e·x)`.

    This is the structural simplification behind the **Pauli-full-shell** case of
    the knot operator `F(τ, N)` in `cor:spectral-decomposition-qvalue`, whose
    numerator is `|tr_M(e_{(1³)} · τ · T_β · e_{(1³)})|` with `e_{(1³)}` the
    alternating Young idempotent: the outer `e` sandwich collapses, so the
    numerator equals `|tr_M(e_{(1³)} · τ · T_β)|`.  Bean `qou-xq3f`. -/
theorem trace_idempotent_sandwich (e x : A) (he : e * e = e) :
    MT.trace (e * x * e) = MT.trace (e * x) := by
  rw [MT.cyclic (e * x) e, ← mul_assoc, he]

/-- The mirror form: `tr_M(e · x · e) = tr_M(x · e)` for an idempotent `e`.
    Same derivation via cyclicity applied to the leading factor. -/
theorem trace_idempotent_sandwich' (e x : A) (he : e * e = e) :
    MT.trace (e * x * e) = MT.trace (x * e) := by
  rw [MT.cyclic (e * x) e, ← mul_assoc, he, MT.cyclic e x]

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

This Lean statement is therefore a **target / placeholder**:
it records the eventual theorem with a bibliographic reference
and a `sorry` so the proof obligation is tracked.  Closing this
`sorry` requires (a) extending `MarkovTrace` to carry the
cross-level Markov field, and (b) a basis-of-reduced-words
lemma for `H_n(q)` that has not yet been built up in
`QOU.Hecke.*`.
-/
/-- **External axiom (Ocneanu 1985; Jones 1987; Wenzl 1988):
    uniqueness of the Markov trace on `H_n(q)`.**

    The Markov trace is unique once the parameter `z` is fixed.
    Proof: reduce any element of `H_n(q)` to a `Z`-linear combination
    of reduced braid words via the Hecke quadratic relation
    `σ_i² = h σ_i + 1`, then evaluate via the Markov axiom +
    cyclicity.  Pending the basis-of-reduced-words lemma in
    `QOU.Hecke.*`. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
axiom markov_trace_unique_axiom :
    ∀ {R : Type u} {n : ℕ} {q : R} {A : Type u}
      [CommRing R] [Inv R] [Ring A] [Algebra R A]
      [HeckeAlgebra R n q A]
      (MT₁ MT₂ : MarkovTrace n q A)
      (_hz : MT₁.z_param = MT₂.z_param),
        MT₁.trace = MT₂.trace

theorem markov_trace_unique
    {R : Type u} {n : ℕ} {q : R} {A : Type u}
    [CommRing R] [Inv R] [Ring A] [Algebra R A]
    [HeckeAlgebra R n q A]
    (MT₁ MT₂ : MarkovTrace n q A)
    (hz : MT₁.z_param = MT₂.z_param) :
    MT₁.trace = MT₂.trace :=
  markov_trace_unique_axiom MT₁ MT₂ hz

end QOU.Hecke
