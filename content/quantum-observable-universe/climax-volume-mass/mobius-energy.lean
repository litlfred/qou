import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic


/-!
# QOU.Braiding.mobius_energy — Categorical Möbius energy

The categorical Möbius energy is defined via the Hopf comultiplication
and Frobenius form. In the classical limit q → 1, it recovers the
classical Möbius energy up to normalization.

LaTeX label: `prop:mobius-energy`

## References

- [freedman1994] https://doi.org/10.2307/2118583
- [manuscript] §4-path-integrals-and-braiding/mobius-energy

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation. The energy values themselves (which carry an
ordering `0 ≤ ·` and the rational normalisation `1/4`) live on the
archimedean side `ℝ` past the substrate→archimedean wall.
-/

namespace QOU.Braiding

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ

/-- The canonical indeterminate `q` of `R_q`. -/
def q_param : R_q := LaurentPolynomial.T 1

/-- The inverse indeterminate `q⁻¹` of `R_q`. -/
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Categorical Möbius energy data**.

    E_cat(γ) integrates the Hopf comultiplication Δ(γ(s)) ⊗ Δ(γ(t))
    off the diagonal in S¹ × S¹, weighted by the q-Hodge star.  The
    energy values are archimedean (real) quantities obtained after
    evaluating the categorical data at the substrate point `q₀`.

    Ref: [freedman1994], [manuscript] §4 -/
structure CategoricalMobiusEnergy where
  /-- The archimedean substrate parameter `q₀ > 0` (post-`τ` evaluation). -/
  q : ℝ
  /-- `q₀ > 0`. -/
  q_pos : 0 < q
  /-- The categorical Möbius energy. -/
  energy_cat : ℝ
  /-- The classical Möbius energy E(γ). -/
  energy_classical : ℝ
  /-- The topological normalisation constant. -/
  normConst : ℝ
  /-- The classical Möbius energy of an embedded curve is non-negative. -/
  energy_classical_nonneg : 0 ≤ energy_classical

/-- In the classical limit q → 1, the categorical Möbius energy
    reduces to ¼ E(γ) + const. -/
-- Ref: [freedman1994], [manuscript] §4
structure ClassicalLimit extends CategoricalMobiusEnergy where
  /-- Classical limit relation. -/
  classical_limit : energy_cat = (1 / 4 : ℝ) * energy_classical + normConst

/- **`mobius_energy_nonneg` was removed 2026-08-23.**

   It read

       theorem mobius_energy_nonneg (cme : CategoricalMobiusEnergy) :
           0 ≤ cme.energy_classical :=
         cme.energy_classical_nonneg

   — the conclusion is character-identical to the `energy_classical_nonneg`
   field, so the "theorem" re-exported a hypothesis as though it were derived.
   The vacuity audit flags it `proof-no-self-assuming-projection`
   (type-matched projection) and the review ledger carries an agent verdict of
   **genuine** with disposition `construct-witness-or-drop-pseudo-theorem`
   (2026-08-09, file_sha 2fbb52aa1f54 — still current). Nothing referenced it,
   so dropping it loses no content: consumers use the field
   `cme.energy_classical_nonneg` directly, which is honest about being an
   assumption.

   The `construct-witness` branch was not taken here. It needs
   `energy_classical` to be *defined* as the Möbius integral rather than
   carried as an opaque `ℝ`, which requires integration theory; a witness
   supplying a convenient value would be the `qou-6dzi` / `PUnit` defect.

   The genuine content now lives in
   [`QOU.Geometry.mobiusKernel_nonneg`](../lean/QOU/Geometry/MobiusKernel.lean):
   the Möbius integrand is pointwise non-negative, **derived** from chord ≤ arc
   (sorry-free; `#print axioms` = `[propext, Classical.choice, Quot.sound]`).
   Once `energy_classical` is defined as the integral of that kernel, its
   non-negativity follows and the field can be dropped too. -/

end

end QOU.Braiding
