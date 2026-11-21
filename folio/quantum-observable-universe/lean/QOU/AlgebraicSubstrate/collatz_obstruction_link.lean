import QOU.AlgebraicSubstrate.qou_obstruction_reduction

/-!
# q-Collatz Kummer removability via the universal χ(A) obstruction (Tier C, C9)

The q-Collatz map's **even branch** divides by `[2]_q`; the obstruction to that
division being globally removable is the level-2 residue `κ_C` of the universal
`χ(A)` class (`thm:qou-obstruction-reduction`,
`QOU.AlgebraicSubstrate.QouObstructionReductionContext`). This file supplies the
**C9 Lean-link**: conditional on the obstruction context, the even-branch `[2]_q`
Kummer obstruction vanishes — the divisor is removable — **iff** `2 ∣ χ(A)`,
specialising the universal `kappa_vanishes_iff_chi` to the q-Collatz-relevant
level `n = 2`.

## Honest scope (anti-laundering)

This is the **Kummer-removability leg only**, *not* the full q-Collatz
conjecture. Removability of the `[2]_q` divisor is *necessary* for the map to be
well-behaved on its even branch, but convergence (`reaches_cycle`) additionally
requires the descent measure `μ` — the open wall documented in the
2026-07-18 audit. So this file links `κ_C = 0` to a **divisibility fact about
χ(A)**, and does **not** claim `κ_C = 0 ⟺ [q-Collatz holds]`.

`χ(A) = −6` is **Descartes-universe-specific** (Bring's surface `Σ₄`, genus 4),
not a general-QOU fact; the `_of_chi_neg_six` corollary is therefore stated with
`χ(A) = −6` as an explicit hypothesis, matching the scoping of the q-Collatz
contact-boundary block (`prop:collatz-contact-boundary`, scoped to "QOU with
`2 ∣ χ(A)`").

-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/collatz-contact-boundary.md
-/

namespace QOU.AlgebraicSubstrate

/-- **C9 — q-Collatz even-branch Kummer removability ⟺ `2 ∣ χ(A)`.** Conditional
    on the universal obstruction context, the level-2 residue `κ_C` of the `χ(A)`
    class vanishes — the q-Collatz `[2]_q` divisor is removable — iff `2 ∣ χ(A)`.
    The q-Collatz specialisation (`n = 2`) of `kappa_vanishes_iff_chi`. -/
theorem qcollatz_kummer_removable_iff_two_dvd_chi
    [ctx : QouObstructionReductionContext] :
    ctx.kappa_vanishes 2 ↔ (2 : ℤ) ∣ ctx.chi_A := by
  simpa using kappa_vanishes_iff_chi (ctx := ctx) 2

/-- **Descartes instance.** In a Descartes universe `χ(A) = −6`, so `2 ∣ χ(A)` and
    the q-Collatz even-branch `[2]_q` obstruction vanishes — the Kummer divisor is
    removable. Stated with `χ(A) = −6` as an explicit hypothesis, since that value
    is Descartes-specific, not general-QOU. -/
theorem qcollatz_kummer_removable_of_chi_neg_six
    [ctx : QouObstructionReductionContext] (h : ctx.chi_A = -6) :
    ctx.kappa_vanishes 2 := by
  rw [qcollatz_kummer_removable_iff_two_dvd_chi, h]
  decide

end QOU.AlgebraicSubstrate
