import Mathlib.FieldTheory.Minpoly.Field
import Mathlib.Tactic

/-!
# QOU.Mass.IrreducibleCubicNoQuadraticRoot — a cubic acquires no root among elements
of degree at most two

**Statement.** Let `F` be a field, `L` an `F`-algebra which is a nontrivial ring, and
`a : L`. If `a` is a root of *some* nonzero `g : F[X]` of degree `≤ 2`, then `a` is not
a root of any irreducible `p : F[X]` of degree `3`. Reason: the minimal polynomial of
`a` would have degree `3` (being `p` up to a unit) and at the same time degree `≤ 2`
(being minimal among annihilators, `g` included).

The hypothesis "`a` is annihilated by a nonzero polynomial of degree `≤ 2`" is the
usable form of "`a` lies in a quadratic extension of `F`": in `L = F⟮b⟯` with
`b² ∈ F` every element satisfies such a `g`. Taking it as the hypothesis keeps this
file free of the `IntermediateField` tower machinery while proving exactly the
obstruction the application needs.

## Why this is here (bean `qou-7fnr`, follows `qou-1z28` / #6695)

#6695 pruned the first route of wall W1 (`qou-d8de`): a q-connection on the base
`z`-line with coefficients in `ℂ(z)` cannot have the colour sheets as flat sections.
The chain is — the colour cubic is irreducible over `K(z)`
(`QOU.Mass.ColorCubicIrreducible`), so no sheet is a rational function of `z`; each
sheet is algebraic, hence D-finite; a rational q-difference system would make a sheet
q-holonomic; and D-finite together with q-holonomic forces rationality (Bézivin;
Ramis; Schäfke–Singer). Contradiction.

That PR then asserted that the **local** q-dilation `t ↦ μt` at a ramification point
`z = z_c + t²` escapes the same exclusion, on the grounds that a power series always
satisfies a first-order q-equation with a *power-series* coefficient. The theorem is
about *rational* coefficients, so that reason does not support the claim — and the
claim is false. This file supplies the missing step.

In the local coordinate the sheets are power series in `t`, algebraic over `K(t)` and
therefore D-finite there, so the identical argument applies as soon as no sheet is
*rational in `t`*. Now `t² = z − z_c`, so every element of `K(t)` satisfies a
polynomial of degree `≤ 2` over `K(z)`; the colour cubic is irreducible over `K(z)`;
so by this lemma it has no root in `K(t)`. Every hypothesis of the rationality theorem
is then met in the local chart exactly as on the base, and the local rational
q-dilation is excluded too.

The concrete instance for this curve is checked exactly in
[`w1_local_qdilation_branchpoint_probe.py`](../../../../../computations/probes/w1_local_qdilation_branchpoint_probe.py),
which also verifies directly that the local cubic has no root in `K[t]` at any degree
— a leading-term bound for degree `≥ 3`, and a Gröbner basis `[1]` over
`ℚ[c₀,c₁,c₂,z_c]` modulo the branch sextic for degree `≤ 2`. What this file carries is
the general obstruction, which is the part that was missing and is reusable.

Ground field is a generic `[Field F]`; no characteristic assumption and nothing
archimedean (§7c).
-/

namespace QOU.Mass.IrreducibleCubicNoQuadraticRoot

open Polynomial

variable {F L : Type*} [Field F] [Ring L] [Algebra F L] [Nontrivial L]

/-- **The minimal polynomial of a root of an irreducible `p` has `p`'s degree.** -/
theorem degree_minpoly_eq_of_irreducible {p : F[X]} (hp : Irreducible p) {a : L}
    (ha : aeval a p = 0) : (minpoly F a).degree = p.degree := by
  rw [← minpoly.eq_of_irreducible hp ha]
  exact degree_mul_leadingCoeff_inv p hp.ne_zero

/-- **An irreducible cubic has no root of degree at most two.** If `a` is annihilated
by a nonzero polynomial of degree `≤ 2` over `F` — which is what membership of a
quadratic extension of `F` supplies — then `a` is not a root of an irreducible cubic
over `F`.

This is the step that carries the #6695 exclusion from the base coordinate `z` to the
local coordinate `t` at a ramification point, where `K(t) / K(z)` is quadratic. -/
theorem no_root_of_irreducible_cubic
    {p : F[X]} (hp : Irreducible p) (hp3 : p.degree = 3)
    {a : L} {g : F[X]} (hg0 : g ≠ 0) (hg2 : g.degree ≤ 2) (hga : aeval a g = 0) :
    aeval a p ≠ 0 := by
  intro ha
  have h3 : (minpoly F a).degree = 3 := by
    rw [degree_minpoly_eq_of_irreducible hp ha, hp3]
  have hle : (minpoly F a).degree ≤ 2 :=
    le_trans (minpoly.degree_le_of_ne_zero F a hg0 hga) hg2
  rw [h3] at hle
  norm_num at hle

/-- **Contrapositive, in the shape the prune uses.** No element annihilated by a
nonzero quadratic is a root of the irreducible cubic — so the sheets of an
irreducible cubic curve are not elements of a quadratic extension of the base
rational function field. -/
theorem not_isRoot_of_irreducible_cubic
    {p : F[X]} (hp : Irreducible p) (hp3 : p.degree = 3)
    {a : L} {g : F[X]} (hg0 : g ≠ 0) (hg2 : g.degree ≤ 2) (hga : aeval a g = 0) :
    ¬ (p.map (algebraMap F L)).IsRoot a := by
  intro hroot
  exact no_root_of_irreducible_cubic hp hp3 hg0 hg2 hga
    (by simpa [aeval_def, eval_map] using hroot)

/-- **Specialisation to linear annihilators (`degree ≤ 1`, `qou-3f7a`).**
If `a : L` is annihilated by a nonzero polynomial `g : F[X]` of degree `≤ 1`,
then `a` is not a root of any irreducible cubic `p : F[X]` (`p.degree = 3`). -/
theorem no_root_of_irreducible_cubic_degree_le_one
    {p : F[X]} (hp : Irreducible p) (hp3 : p.degree = 3)
    {a : L} {g : F[X]} (hg0 : g ≠ 0) (hg1 : g.degree ≤ 1) (hga : aeval a g = 0) :
    aeval a p ≠ 0 := by
  have hg2 : g.degree ≤ 2 := le_trans hg1 (by decide)
  exact no_root_of_irreducible_cubic hp hp3 hg0 hg2 hga

end QOU.Mass.IrreducibleCubicNoQuadraticRoot
