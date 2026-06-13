import QOU.Torsion.MassGap
import QOU.AlgebraicSubstrate.qou_obstruction_reduction
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.IntervalCases

/-!
# QOU.BraidKnot.MassGapObstruction — Step 3, the mass-gap arm

Implements the **mass-gap arm of Step 3** of the three-step program
(`docs/workplans/2026-06-11-mass-gap-three-step-program.md` §3): tie
the mass-gap classical limit to the χ(A) = −6 Kummer obstruction of
`thm:qou-obstruction-reduction`, in §3b-cond conditional form.

The obstruction-reduction context class
(`QOU.AlgebraicSubstrate.QouObstructionReductionContext`) already
carries the three manuscript sub-claims — (a) one-dimensional
obstruction, (b) class = χ(A), (c) Kummer level-`n` vanishing ⟺
`n ∣ χ(A)` — and the NS corollaries are wired in
`QOU.FluidDynamics.ns_obstruction_*`.  What was missing is the
**mass-gap corollary**, landed here sorry-free:

- `kummer_vanishes_at_two` — at χ(A) = −6 the level-2 obstruction
  vanishes: the Kummer shadow of the μ₂-vanishing of the gap
  (`massGapBound_at_one`, the gap function vanishing on μ₂ ⊂ 𝔾ₘ).
- `kummer_persists_above_three` — at χ(A) = −6 the obstruction
  **persists at every prime > 3** (the workplan's headline claim,
  now an actual theorem: `p ∤ 6` for prime `p > 3`).
- `massgap_classical_limit_obstruction` — the combined Step-3
  statement: the categorical gap bound dies at the classical point
  (unconditional, from `QOU.Torsion.massGapBound_at_one`) AND the
  Kummer obstruction persists at all primes > 3 (conditional on the
  context).  Both phenomena reduce to the divisibility structure of
  χ(A) = −6, which is the workplan's "Route 1 executed honestly at
  the limit point computes the obstruction".

> **Universality caveat (mandatory per workplan §3).**  These
> theorems prove that *the QOU framework's* classical limit fails —
> NOT that standard q = 1 Yang–Mills (Wightman-axiomatized, on ℝ⁴)
> does not exist.  Promotion to a Millennium-relevant counterexample
> would additionally require a universality theorem ("any
> axiomatized YM with a gap yields a QOU-type structure"), which
> does not exist.  Every statement here is framework-conditional;
> publication, if any, is per-problem and conditional.
-/

namespace QOU.BraidKnot

open QOU.Torsion QOU.AlgebraicSubstrate

/-- **Kummer level-2 vanishing at χ(A) = −6** — the Kummer shadow of
    the μ₂-vanishing of the gap: `2 ∣ 6`, so the level-2 obstruction
    class vanishes, matching the (unconditional) vanishing of the
    categorical gap bound at the classical point. -/
-- Ref: [manuscript] models-of-qous/yang-mills-mass-gap.md §G_m-torsion
theorem kummer_vanishes_at_two [ctx : QouObstructionReductionContext]
    (hchi : ctx.chi_A = -6) : ctx.kappa_vanishes 2 :=
  (ctx.claim_c_kummer_vanishing 2 (by norm_num)).mpr (by rw [hchi]; decide)

/-- **Kummer persistence above 3 at χ(A) = −6** — the obstruction
    does NOT vanish at any prime `p > 3`: such a prime does not
    divide 6.  This is the workplan's "the classical-limit
    obstruction persists at all primes > 3" as a theorem. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §0
theorem kummer_persists_above_three [ctx : QouObstructionReductionContext]
    (hchi : ctx.chi_A = -6) {p : ℕ} (hp : Nat.Prime p) (hp3 : 3 < p) :
    ¬ ctx.kappa_vanishes p := by
  intro hvan
  have h := (ctx.claim_c_kummer_vanishing p (by omega)).mp hvan
  rw [hchi] at h
  have h6 : (p : ℤ) ∣ 6 := (dvd_neg).mp h
  have h6n : p ∣ 6 := by exact_mod_cast h6
  have hle : p ≤ 6 := Nat.le_of_dvd (by norm_num) h6n
  interval_cases p <;> revert h6n hp <;> decide

/-- **Step 3, mass-gap arm (combined statement).**  Conditional on the
    obstruction-reduction context with χ(A) = −6:

    1. the categorical gap bound vanishes at the classical point
       `q = 1` (unconditional — `QOU.Torsion.massGapBound_at_one`);
    2. the Kummer obstruction persists at every prime `p > 3`.

    Together: the mass-gap classical limit and the classical-limit
    obstruction both reduce to the divisibility structure of
    χ(A) = −6 in the Kummer tower — the gap's death at `q = 1` is the
    μ₂ face (`2 ∣ 6`, `kummer_vanishes_at_two`) of the same class
    whose primes-above-3 faces obstruct the classical limit.

    See the module docstring for the mandatory universality caveat:
    this is a statement about the QOU framework's classical limit,
    conditional on `QouObstructionReductionContext`. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §3
-- Ref: [jaffe2006] https://www.claymath.org/millennium/yang-mills-the-maths-gap/
theorem massgap_classical_limit_obstruction
    [ctx : QouObstructionReductionContext] (hchi : ctx.chi_A = -6) :
    massGapBound 1 = 0 ∧
    (∀ p : ℕ, Nat.Prime p → 3 < p → ¬ ctx.kappa_vanishes p) :=
  ⟨massGapBound_at_one,
   fun _ hp hp3 => kummer_persists_above_three hchi hp hp3⟩

end QOU.BraidKnot
