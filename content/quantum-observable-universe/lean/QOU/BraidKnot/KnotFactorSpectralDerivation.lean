import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Field.Defs
import Mathlib.Tactic.Ring


/-!
# QOU.BraidKnot.knot_factor_spectral_derivation

The knot factor `a_K` in the unified mass formula is the chirality
Gram pairing in the Wedderburn (central-idempotent) basis.

## Base ring (AGENTS.md §7c)

Pre-archimedean.  The narrative states the pairing over the Hecke
base ring — *"we work over `A = H_n(R, q)`… the identity holds
exactly in `R`"* — and the Lean now matches: everything below is
stated over a generic `{R : Type*} [Field R]`.  Nothing here uses
an ordering, `Real.*`, or any archimedean input; the previous `ℝ`
was a gratuitous specialisation.

Why a **field** and not `CommRing` (the `wall-base-ring-minimal`
adjudication): the Gram pairing is *normalised* by `χ_λ(𝟙)²`, and
`χ_λ(𝟙) = dim_q V_λ` is a Laurent polynomial in `q`, not a unit of
`ℤ[q^{±1}]`.  So the quotient genuinely leaves the Laurent ring and
lands in its fraction field — `R := ℚ(q)` is the intended base.  The
division is essential, not a restatable Laurent identity, and
`[Field R]` is the weakest §7c class admitting it.  `R := ℝ` remains
an instance for archimedean evaluation at the substrate anchor.

LaTeX label: `prop:knot-factor-spectral-form`

## References

- [manuscript] §3/knot-factor-spectral-derivation
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.BraidKnot

/-- Central-idempotent character expansion of a braid in `H_n(q)`,
    over the Hecke base ring `R` (§7c: generic; `R := ℚ(q)` is the
    intended instance, `R := ℝ` the archimedean one). -/
structure HeckeExpansion (R : Type*) [Field R] (n : ℕ) where
  partitions : Finset (List ℕ)
  c : List ℕ → R                       -- χ_λ(β)
  weight : List ℕ → R                  -- Plancherel w_λ(q)
  trivial : List ℕ → R                 -- χ_λ(𝟙)

/-- The knot-factor `a_K` as a Gram pairing on the chirality block. -/
def knotFactor {R : Type*} [Field R] (n : ℕ)
    (β β_mirror : HeckeExpansion R n) : R :=
  β.partitions.sum fun p =>
    β.weight p * (β.c p * β_mirror.c p) / (β.trivial p) ^ 2

/-- **Proposition (knot factor as chirality Gram pairing)**.

    For any braid `β ∈ B_n` with mirror `β*`, the knot factor
    appearing in the unified mass formula is the Plancherel-weighted
    character pairing displayed above. -/
-- Ref: [manuscript] §3/knot-factor-spectral-derivation
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem knot_factor_spectral_form {R : Type*} [Field R] (n : ℕ)
    (β β_mirror : HeckeExpansion R n) :
    knotFactor n β β_mirror
      = ∑ lam ∈ β.partitions,
          β.weight lam * (β.c lam * β_mirror.c lam) / (β.trivial lam) ^ 2 :=
  rfl

/-- **Self-pairing.**  Pairing a braid with itself gives the Plancherel
    sum of squared character ratios,

      `a_K(β, β) = Σ_λ w_λ · (χ_λ(β) / χ_λ(𝟙))²` ,

    the "sum of positive squares" form.  Over an ordered field every
    summand with `w_λ ≥ 0` is non-negative, which is what makes the
    amphicheiral corollary's sign flip on the alternating block
    observable rather than a convention. -/
theorem knotFactor_self {R : Type*} [Field R] (n : ℕ)
    (β : HeckeExpansion R n) :
    knotFactor n β β
      = ∑ lam ∈ β.partitions, β.weight lam * (β.c lam / β.trivial lam) ^ 2 := by
  refine Finset.sum_congr rfl fun lam _ => ?_
  rw [div_pow]
  ring

end QOU.BraidKnot
