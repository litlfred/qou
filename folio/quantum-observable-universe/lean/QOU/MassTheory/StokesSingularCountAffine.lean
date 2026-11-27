import Mathlib.Data.Int.Notation

/-!
# QOU.Mass.StokesSingularCountAffine — Euler's formula lower-bounds the cut locus of the canonical closure

Purely combinatorial: any cell decomposition of a surface with Euler characteristic `χ`, one vertex
and one face has at least `2 − χ` edges, and at the canonical closure's `χ = −9A + 1` that is
`9A + 1`. The three statements are over `ℤ` and closed by `omega`.

The asymptotic use of these bounds (that a singular count bounded below by an affine function of `A`
is not a `StokesSurfaceTerm` over the Seifert cell count) is a filter limit and lives behind the
transcendental boundary, in `QOU.Transcendental.MassTheory.StokesSingularCountAffineAnalytic`,
which keeps this namespace and the full discussion of hypothesis (H1).
-/

namespace QOU.Mass.StokesSingularCountAffine

/-! ## Euler's formula lower-bounds the cut locus -/

/-- **Any cell decomposition with a vertex and a face has at least `2 − χ` edges.** Pure Euler. -/
theorem edges_ge_two_sub_chi (V E F χ : ℤ) (hEuler : χ = V - E + F) (hV : 1 ≤ V) (hF : 1 ≤ F) :
    2 - χ ≤ E := by
  omega

/-- **At the canonical closure's `χ = −9A + 1`, every decomposition has `≥ 9A + 1` edges.** The
1-skeleton of any cell decomposition grows at least linearly in `A`. (Whether the connection's
singular locus contains it is hypothesis (H1) in the header of `StokesSingularCountAffineAnalytic`, not a consequence.) -/
theorem edges_ge_of_chi_canonical (A V E F : ℤ) (hEuler : -9 * A + 1 = V - E + F)
    (hV : 1 ≤ V) (hF : 1 ≤ F) : 9 * A + 1 ≤ E := by
  omega

/-- Euler's formula in the form `χ = 2 − 2g − μ` for a compact orientable surface of genus `g` with
`μ` boundary components, together with the corpus's `2g = 8A`, `μ = A + 1`, reproduces
`χ = −9A + 1` — the three measured invariants are mutually consistent. -/
theorem chi_of_genus_boundary (A g μ : ℤ) (hg : 2 * g = 8 * A) (hμ : μ = A + 1) :
    2 - 2 * g - μ = -9 * A + 1 := by
  omega

end QOU.Mass.StokesSingularCountAffine
