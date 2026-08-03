/-
# The 5₂ saddle sum rule — algebraic skeleton and the reflection reduction

Numerics (`computations/probes/qbeta_5two_saddle_sum_rule_and_provenance_probe.py`,
merged 2026-08-02) established to 80 dps that the three 5₂ saddle values satisfy

    Σⱼ Re(Vⱼ) = −3π²/2                                              (SUM)

with `Vⱼ = 3·Li₂(yⱼ) + (log yⱼ + bⱼ·πi)²` and `yⱼ` the roots of
`y³ − 2y² + 3y − 1`. That is strong evidence, **not a proof**.

## What this file does and does not prove

Mathlib carries **no polylogarithm** (no `Polylog`, no `dilog` — checked
2026-08-03), so (SUM) itself cannot be stated against a Mathlib `Li₂`, let
alone proved. Rather than fake it, this file:

* proves the **algebraic skeleton** sorry-free and over a generic `CommRing`
  (`cubic_iff_sq_eq_cube`);
* proves the **reflection reduction** sorry-free, with `Li` an *abstract*
  function carrying the reflection identity as an explicit hypothesis
  (`sum_reflection_of_branch`) — this is the analytic step of the paper
  derivation, and it is genuine content, not a placeholder;
* proves the two **bookkeeping consequences** that the prose asserts —
  that `π²/2` is the *unique* centering shift (`centering_constant_unique`)
  and that `V₃` is *determined* by `V₁` (`V_two_of_sum_rule`);
* records (SUM) itself as a **content-bearing conjecture carrier with no
  instance** (`FiveTwoSaddleSumRule`), which is the honest representation of
  an open statement.

The genuinely open input is isolated in `FiveTwoDilogLadder`: one further
relation between `Σ Li₂(yⱼ)` and `Σ Li₂(1−yⱼ)`. `sum_reflection_of_branch`
supplies one equation in those two unknowns; a second is needed, and the
identified route (Kubert/distribution relation on `Li₂(y²) = Li₂((1−y)³)`)
is not formalized here.

-- Ref: [manuscript] docs/coordination/1ppq-qbeta.md, 2026-08-02 row
-- Ref: [garoufalidis2020] https://arxiv.org/abs/2012.00062 eq (233)–(234)
-/
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Algebra.BigOperators.Fin

namespace QOU.QBeta.FiveTwo

open Complex

/-! ### Algebraic skeleton (generic commutative ring, §7c) -/

/-- The 5₂ saddle cubic **is** the branch equation `y² = (1−y)³`.

Both forms appear in the sources — GGM eq (233) at `x = 1` writes
`y² = (1−y)³`, GGMW eq (184) writes `(1−ξ)³ = ξ²`, and the corpus carries
`y³ − 2y² + 3y − 1`. They are the same equation, over any commutative ring:
no positivity, ordering, or archimedean structure is used. -/
theorem cubic_iff_sq_eq_cube {R : Type*} [CommRing R] (y : R) :
    y ^ 3 - 2 * y ^ 2 + 3 * y - 1 = 0 ↔ y ^ 2 = (1 - y) ^ 3 := by
  constructor <;> intro h <;> linear_combination h

/-! ### The reflection reduction

The analytic content of the partial derivation. `Li` is abstract: the only
thing assumed about it is the reflection identity, so this theorem is exactly
as strong as that identity and no stronger. -/

/-- **Summing the dilogarithm reflection identity over the three roots.**

Given the reflection identity `Li z + Li (1−z) = π²/6 − log z · log(1−z)` and
the branch data of the cubic — `2·log yⱼ − 3·log(1−yⱼ) = 2πi·εⱼ`, which is
what `y² = (1−y)³` gives after taking logarithms — the `Li` values at `1−yⱼ`
are eliminated in favour of log-squares:

    Σ Li(yⱼ) + Σ Li(1−yⱼ)
      = π²/2 − (2/3)·Σ(log yⱼ)² + (2πi/3)·Σ εⱼ·log yⱼ

This is **one equation in the two unknowns** `Σ Li(yⱼ)` and `Σ Li(1−yⱼ)`. It
does not close the sum rule; see `FiveTwoDilogLadder`. -/
theorem sum_reflection_of_branch
    (Li : ℂ → ℂ) (y ε : Fin 3 → ℂ)
    (hrefl : ∀ z : ℂ, Li z + Li (1 - z)
      = (Real.pi : ℂ) ^ 2 / 6 - Complex.log z * Complex.log (1 - z))
    (hbranch : ∀ j, 2 * Complex.log (y j) - 3 * Complex.log (1 - y j)
      = 2 * (Real.pi : ℂ) * I * ε j) :
    (∑ j, Li (y j)) + (∑ j, Li (1 - y j))
      = (Real.pi : ℂ) ^ 2 / 2 - (2 / 3) * ∑ j, Complex.log (y j) ^ 2
        + (2 * (Real.pi : ℂ) * I / 3) * ∑ j, ε j * Complex.log (y j) := by
  have per : ∀ j, Li (y j) + Li (1 - y j)
      = (Real.pi : ℂ) ^ 2 / 6 - (2 / 3) * Complex.log (y j) ^ 2
        + (2 * (Real.pi : ℂ) * I / 3) * (ε j * Complex.log (y j)) := by
    intro j
    have hk : Complex.log (1 - y j)
        = (2 * Complex.log (y j) - 2 * (Real.pi : ℂ) * I * ε j) / 3 := by
      linear_combination (-1 / 3 : ℂ) * hbranch j
    rw [hrefl (y j), hk]; ring
  simp only [Fin.sum_univ_three]
  linear_combination per 0 + per 1 + per 2

/-! ### Bookkeeping consequences of the sum rule

Easy algebra — recorded because they are the two claims the prose makes, and
a claim worth asserting is worth checking. -/

/-- **`π²/2` is the *unique* shift that centers the saddle values.**

Given the sum rule, `Σⱼ (Vⱼ + c) = 0` holds for exactly one `c`, namely
`π²/2`. So the corpus's "extraction convention" — long treated as an
unexplained fudge absorbed by a fit — is forced, not chosen. -/
theorem centering_constant_unique (V : Fin 3 → ℝ) (c : ℝ)
    (hsum : ∑ j, V j = -3 * (Real.pi ^ 2 / 2)) :
    (∑ j, (V j + c)) = 0 ↔ c = Real.pi ^ 2 / 2 := by
  simp only [Fin.sum_univ_three] at hsum ⊢
  constructor <;> intro h <;> linarith

/-- **`V₃` is determined by `V₁`.**

With `V₂ = conj V₁` (hence equal real parts), the sum rule forces
`V₃ = −2·V₁ − 3π²/2`. Consequently `V₃` never needs to be carried as an
independent numerical literal — which is what let the corpus keep a wrong
one (`−2.7580990292`) unnoticed for months. -/
theorem V_two_of_sum_rule (V : Fin 3 → ℝ)
    (hsum : ∑ j, V j = -3 * (Real.pi ^ 2 / 2)) (hconj : V 1 = V 0) :
    V 2 = -2 * V 0 - 3 * (Real.pi ^ 2 / 2) := by
  simp only [Fin.sum_univ_three] at hsum
  linarith

/-! ### The open statements

Both carriers below are **primary conjectures**: their signatures take no
other conjecture class as a hypothesis. Neither is given an instance, which
is the honest representation of "numerically verified, not proved". -/

/-- **CONJECTURE (verified to 80 dps, unproved).** The 5₂ saddle sum rule.

`Vⱼ = 3·Li₂(yⱼ) + (log yⱼ + bⱼπi)²` over the three roots of the saddle cubic
satisfies `Σⱼ Re Vⱼ = −3π²/2`.

Numerical status: residual `3.4e-80` at 80 dps, and **specific to the 5₂
cubic** — five control cubics of the same shape, four sharing the `Πy = 1`
constraint, miss the target by 0.16 to 2.83. So this is an arithmetic
property of the 5₂ saddle cubic, not branch bookkeeping.

No instance is provided: the statement is open. -/
class FiveTwoSaddleSumRule (Li : ℂ → ℂ) (y b : Fin 3 → ℂ) : Prop where
  /-- `Σⱼ Re Vⱼ = −3π²/2`. -/
  sum_re_eq :
    (∑ j, (3 * Li (y j) + (Complex.log (y j) + b j * (Real.pi : ℂ) * I) ^ 2)).re
      = -3 * (Real.pi ^ 2 / 2)

/-- **CONJECTURE (unproved).** The missing second relation.

`sum_reflection_of_branch` gives one equation in `A = Σ Li₂(yⱼ)` and
`B = Σ Li₂(1−yⱼ)`. Numerically `A ≈ 0.9717306815` and `B ≈ 0.3514640301`,
neither with an evident closed form, so a second independent relation is
required to close the sum rule.

The identified route is the Kubert/distribution relation
`Li₂(zⁿ) = n·Σ_{k<n} Li₂(ζₙᵏ z)` applied to `Li₂(y²) = Li₂((1−y)³)`, which
supplies one at the cost of cube-root-of-unity arguments `ω(1−y)`. That
Bloch-group computation is not formalized here.

Stated as a linear dependence between the two sums with coefficients
`α, β, γ` to be identified; no instance is provided. -/
class FiveTwoDilogLadder (Li : ℂ → ℂ) (y : Fin 3 → ℂ) : Prop where
  /-- Some nontrivial linear relation over ℚ between `Σ Li(yⱼ)`,
  `Σ Li(1−yⱼ)` and `π²`, independent of the reflection identity. -/
  ladder : ∃ α β γ : ℚ, (α, β) ≠ (0, 0) ∧
    (α : ℂ) * (∑ j, Li (y j)) + (β : ℂ) * (∑ j, Li (1 - y j))
      = (γ : ℂ) * (Real.pi : ℂ) ^ 2

end QOU.QBeta.FiveTwo
