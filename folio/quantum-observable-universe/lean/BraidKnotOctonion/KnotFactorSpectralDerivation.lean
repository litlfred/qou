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
adjudication): the Gram pairing is *normalised* by `χ_λ(𝟙)² = d_λ²`,
where `d_λ = dim V_λ` is the classical dimension, an integer that is
not a unit of `ℤ[q^{±1}]`.  (This docstring previously said
`χ_λ(𝟙) = dim_q V_λ`; the character of the identity is the module's
dimension, `d_λ`.)  So the quotient leaves the Laurent ring and lands
in its fraction field — `R := ℚ(q)` is the intended base.

## What the narrative claims (corrected 2026-11-16)

`a_K := τ(π(β) β*)` with `π` the central projection and `τ` the
Markov trace, `τ(𝟙) = 1`.  Then
`a_K = Σ_λ w_λ χ_λ(β) χ_λ(β*) / d_λ²` with `w_λ = τ(e_λ) = y_λ d_λ`,
and `Σ_λ w_λ = 1`.  The structure below carries the character data
abstractly; `knotFactor_of_trivial` records the normalisation
consequence `a_𝟙 = Σ_λ w_λ`, which equals `1` exactly when the
weights come from a trace with `τ(𝟙) = 1`.  The
division is essential, not a restatable Laurent identity, and
`[Field R]` is the weakest §7c class admitting it.  `R := ℝ` remains
an instance for archimedean evaluation at the substrate anchor.

LaTeX label: `prop:knot-factor-spectral-form`

## References

- [leitner2026] §3/knot-factor-spectral-derivation
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

/-- Unfolding lemma for `knotFactor` (true by definition; it is the
    rewrite rule `KnotFactorAmphicheiral` uses).  The mathematical
    content of the narrative identity, the evaluation
    `τ(π(β) β*) = Σ_λ w_λ χ_λ(β) χ_λ(β*) / d_λ²`, is proved in the
    `.md` from orthogonality of the central idempotents; it is not
    encoded here, because `HeckeExpansion` carries no algebra. -/
-- Ref: [leitner2026] §3/knot-factor-spectral-derivation
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

/-- **Normalisation.**  If both expansions are those of the identity
    (`χ_λ(𝟙) = d_λ` on every block, `d_λ ≠ 0`), the knot factor is the
    total weight `Σ_λ w_λ`.  With `w_λ = τ(e_λ)` that total is
    `τ(𝟙) = 1`.  The old weights `dim_q² V_λ / [n]_q!` fail this, which
    is the defect the 2026-11-16 restatement removes. -/
theorem knotFactor_of_trivial {R : Type*} [Field R] (n : ℕ)
    (β β_mirror : HeckeExpansion R n)
    (hβ : ∀ lam ∈ β.partitions, β.c lam = β.trivial lam)
    (hβm : ∀ lam ∈ β.partitions, β_mirror.c lam = β.trivial lam)
    (hd : ∀ lam ∈ β.partitions, β.trivial lam ≠ 0) :
    knotFactor n β β_mirror = ∑ lam ∈ β.partitions, β.weight lam := by
  refine Finset.sum_congr rfl fun lam hlam => ?_
  rw [hβ lam hlam, hβm lam hlam, ← sq, mul_div_assoc, div_self (pow_ne_zero 2 (hd lam hlam)), mul_one]

end QOU.BraidKnot
