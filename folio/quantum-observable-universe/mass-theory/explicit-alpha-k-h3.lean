import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Units.Defs


/-!
# QOU.BraidsAndKnots.explicit_alpha_k_h3

The four curvature-rank prefactors `α_0, α_1, α_2, α_3` at `H_3(R, q)`
in closed `q`-algebraic form:

  α_0 = 1
  α_1 = 0  (vanishes structurally)
  α_2 = z²
  α_3 = h · z² + z = z · (1 + h·z)

where `z` is the Markov parameter and `h = q - q⁻¹`.

**MIGRATED TO CONVENTION D (2026-08-24).**  The 2026-08-15 owner ruling
makes `z_D = q³/(q²+1)` canonical and excises `z_C = √q/(q+1)`.  This
file was convention C, and the tell was the formal square root: the
relation `z · (v + v⁻¹) = 1` with `v² = q` *is* `z_C`.  Under D the
defining relation is

  z · (q + q⁻¹) = q²,

which needs **no square root at all** — `v` is gone, and with it the
`v_sq` field and the `ℤ[v, v⁻¹]` framing.  Evaluated:

  1 + h·z = (q⁴ + 1)/(q² + 1)          [C gave 1 + √q − 1/√q]
  α_2     = q⁶/(q² + 1)²
  α_3     = q³(q⁴ + 1)/(q² + 1)²

The numerator `q⁴ + 1 = Φ₈(q)` is cyclotomic, as under C it was not.

This is a migration of the *definition* of `z`, not a `z`-swap into a
C-derived conclusion — the move bean `qou-cds1` forbids.  The α_k are
stated in terms of an abstract `z` and are unchanged in form; only the
relation pinning `z`, and the closed-form gloss of `1 + h·z`, are
convention-dependent.

**Known defect, not introduced here and not fixed here.**  The theorem
below is a *vacuous existential*: `∃ a₀ a₁ a₂ a₃, a₀ = 1 ∧ … ∧ a₃ = …`
discharged by four `rfl`s asserts only that those four expressions
exist, which is true of any four expressions.  It states the α_k rather
than deriving them.  Making it falsifiable needs the α_k derived from
the `H_3` curvature-rank computation, which is not available here; it is
recorded as a bean rather than papered over.

**Pre-Archimedean stub.** Polymorphic in the ground **ring** `R`
(AGENTS.md §7c).  An older version forced `q : ℝ`, `z : ℝ`, `h : ℝ`
and used `q ^ (1/2 : ℝ)` (a real power); a later one used an abstract
`v : R` with `v² = q` over a field.  Here `q` is carried as a **unit**
`Rˣ`, so `q⁻¹` is a units inverse and no field structure is needed; the
Markov parameter `z` is pinned by its defining *multiplicative* relation
`z · (q + q⁻¹) = q²` rather than by a division.  Under convention D the
pre-Archimedean home is `ℤ[q, q⁻¹]` — no square root is adjoined.  The
Archimedean evaluation `R = ℝ`, `q = q₀` is the post-τ realisation.

LaTeX label: `conj:explicit-alpha-k-h3`

## References

- [leitner2026] Ch. Braids and Knots, §α_k at H_3
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.BraidsAndKnots

universe u

/-- Markov parameter `z` and amplitude `h` at substrate `q`,
    polymorphic in the ground ring `R`.

    `z` is the convention-D Markov parameter `q³/(q² + 1)`, pinned by
    the division-free relation `z · (q + q⁻¹) = q²`; and `h = q - q⁻¹`
    with the units inverse.  No square root is needed. -/
structure HeckeQ (R : Type u) [CommRing R] where
  /-- The substrate parameter `q`, a unit of `R`. -/
  q : Rˣ
  /-- The convention-D Markov parameter `z = q³/(q² + 1)`, pinned by the
      division-free relation `z · (q + q⁻¹) = q²`. -/
  z : R
  z_def : z * ((q : R) + (↑q⁻¹ : R)) = (q : R) ^ 2
  /-- The amplitude `h = q - q⁻¹`. -/
  h : R
  h_def : h = (q : R) - (↑q⁻¹ : R)

/-- **Proposition (explicit α_k at H_3)**.

    `α_0 = 1`, `α_1 = 0`, `α_2 = z²`, `α_3 = h · z² + z`. -/
-- Ref: [leitner2026] Ch. Braids and Knots, §α_k at H_3
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem explicit_alpha_k_h3 {R : Type u} [CommRing R] (Q : HeckeQ R) :
    ∃ a₀ a₁ a₂ a₃ : R,
      a₀ = 1 ∧ a₁ = 0 ∧ a₂ = Q.z ^ 2 ∧ a₃ = Q.h * Q.z ^ 2 + Q.z :=
  ⟨1, 0, Q.z ^ 2, Q.h * Q.z ^ 2 + Q.z, rfl, rfl, rfl, rfl⟩

end QOU.BraidsAndKnots
