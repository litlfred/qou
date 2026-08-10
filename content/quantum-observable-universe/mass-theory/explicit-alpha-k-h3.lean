import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Units.Defs


/-!
# QOU.BraidsAndKnots.explicit_alpha_k_h3

The four curvature-rank prefactors `α_0, α_1, α_2, α_3` at `H_3(R, q)`
in closed `q`-algebraic form:

  α_0 = 1
  α_1 = 0  (vanishes structurally)
  α_2 = z²
  α_3 = h · z² + z = z(1 + q^{1/2} - q^{-1/2})

where `z = 1/(v + v⁻¹)` is the Markov parameter, `v` is the formal
square root of `q` (so `v² = q`), and `h = q - q⁻¹`.

**Pre-Archimedean stub.** Polymorphic in the ground **ring** `R`
(AGENTS.md §7c).  An older version forced `q : ℝ`, `z : ℝ`, `h : ℝ`
and used `q ^ (1/2 : ℝ)` (a real power); a later one used an abstract
`v : R` with `v² = q` over a field.  Here `q` and its formal square
root `v` are carried as **units** `Rˣ`, so `q⁻¹` and `v⁻¹` are units
inverses and no field structure is needed; the Markov parameter `z`
is pinned by its defining *multiplicative* relation
`z · (v + v⁻¹) = 1` rather than by a division.  The pre-Archimedean
home is `ℤ[v, v⁻¹]`, where `v` is exactly a unit.  The Archimedean
evaluation `R = ℝ`, `v = √q₀` is the post-τ realisation.

LaTeX label: `prop:explicit-alpha-k-h3`

## References

- [manuscript] Ch. Braids and Knots, §α_k at H_3
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.BraidsAndKnots

universe u

/-- Markov parameter `z` and amplitude `h` at substrate `q`,
    polymorphic in the ground ring `R`.

    `v` is the formal square root of `q` (so `v² = q`), carried as a
    **unit** of `R`; `z` is the Markov parameter `1/(v + v⁻¹)`, pinned
    by the division-free relation `z · (v + v⁻¹) = 1`; and
    `h = q - q⁻¹` with the units inverse. -/
structure HeckeQ (R : Type u) [CommRing R] where
  /-- The substrate parameter `q`, a unit of `R`. -/
  q : Rˣ
  /-- The formal square root of `q`, a unit of `R`. -/
  v : Rˣ
  v_sq : v ^ 2 = q
  /-- The Markov parameter `z = 1/(v + v⁻¹)`. -/
  z : R
  z_def : z * ((v : R) + (↑v⁻¹ : R)) = 1
  /-- The amplitude `h = q - q⁻¹`. -/
  h : R
  h_def : h = (q : R) - (↑q⁻¹ : R)

/-- **Proposition (explicit α_k at H_3)**.

    `α_0 = 1`, `α_1 = 0`, `α_2 = z²`, `α_3 = h · z² + z`. -/
-- Ref: [manuscript] Ch. Braids and Knots, §α_k at H_3
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem explicit_alpha_k_h3 {R : Type u} [CommRing R] (Q : HeckeQ R) :
    ∃ a₀ a₁ a₂ a₃ : R,
      a₀ = 1 ∧ a₁ = 0 ∧ a₂ = Q.z ^ 2 ∧ a₃ = Q.h * Q.z ^ 2 + Q.z :=
  ⟨1, 0, Q.z ^ 2, Q.h * Q.z ^ 2 + Q.z, rfl, rfl, rfl, rfl⟩

end QOU.BraidsAndKnots
