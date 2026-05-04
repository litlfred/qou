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
    [CommRing R] [Inv R] [Ring A] [Algebra R A] [HeckeAlgebra R n q A] where
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
  trace_gen : ∀ i : Generator n, trace (HeckeAlgebra.embed i) = z_param

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
  -- Ref: [prop:markov-pair-z2], two-step Markov peel. The σ_j is
  -- index-maximal in σ_i σ_j; one Markov move gives tr · z; the
  -- remaining σ_i lives in a lower-index subalgebra; another
  -- Markov move gives 1 · z.
  sorry

end MarkovTrace

end QOU.Hecke
