/-
  Bar-parity exclusion (GAP-A-4 formalize-first invariant I-2).

  Companion to
    docs/scope/2026-07-02-gap-a4-perknot-density-rule-scoping.md  §I-2
    computations/he3_tritium_cosh_asymmetry_diagnosis.py
    computations/binding_bar_even_odd_probe.py
    QOU/Interactions/qbeta_channel_split.lean  (the concrete barEven/barOdd h-scalars)

  Context.  Under the bar-involution `q ↦ q⁻¹` (equivalently `h ↦ −h` for
  `h = q − q⁻¹`), the per-knot Markov traces split into a bar-EVEN (cosh) and a
  bar-ODD (sinh) channel.  The compute (`he3_tritium_cosh_asymmetry_diagnosis`)
  shows the intra-nucleon proton/neutron distinction is exactly `+h` per nucleon
  — a single linear-in-`h` term, i.e. **bar-ODD**.  So the p≠n binding split
  lives in the bar-odd channel, and the absolute scale in the bar-even channel.

  I-2 is the structural consequence used to prune candidate ρ(K)/Δ_λ rules
  *before* any scan: a **bar-even** candidate cannot supply a nonzero bar-odd
  split.  `qbeta_channel_split.lean` gives `barEven_invariant` / `barOdd_anti`
  for the concrete `h`-scalars; this file states the general **exclusion** those
  specialise to — the missing (b)-grade invariant.

  Base ring (§7c): generic `[Field R] [NeZero (2 : R)]` — purely algebraic; the
  only requirement is `2 ≠ 0` (the substrate is not characteristic 2), which is
  strictly weaker than `CharZero` (admits finite fields of characteristic
  `p > 2`). No q₀, no archimedean construct.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.LinearCombination

namespace QOU.MassTheory

variable {R : Type*} [Field R] [NeZero (2 : R)]

/-- A function that is simultaneously bar-EVEN (`f(−h) = f h`) and bar-ODD
(`f(−h) = −f h`) is identically zero. The two parity conditions force
`f h = −f h`, hence `2·f h = 0`, hence `f h = 0` since `2 ≠ 0`. -/
theorem barEven_and_barOdd_forces_zero
    (f : R → R) (heven : ∀ h, f (-h) = f h) (hodd : ∀ h, f (-h) = -f h) :
    ∀ h, f h = 0 := by
  intro h
  have h1 : f h = -f h := (heven h).symm.trans (hodd h)
  have h2 : (2 : R) * f h = 0 := by linear_combination h1
  exact (mul_eq_zero.mp h2).resolve_left (NeZero.ne (2 : R))

/-- **I-2 exclusion.** If the proton−neutron trace difference `d` is bar-ODD and
nonzero at some point, then no bar-EVEN candidate `c` equals it: a bar-even
correction cannot carry the p≠n binding split. (Compute: the intra-nucleon p/n
distinction is `+h` per nucleon — bar-odd — per `he3_tritium_cosh_asymmetry_diagnosis`.) -/
theorem barEven_cannot_carry_barOdd_split
    (c d : R → R) (hc_even : ∀ h, c (-h) = c h) (hd_odd : ∀ h, d (-h) = -d h)
    {h₀ : R} (hd_ne : d h₀ ≠ 0) : c ≠ d := by
  intro hcd
  refine hd_ne ?_
  have hd_even : ∀ h, d (-h) = d h := fun h => by rw [← hcd]; exact hc_even h
  exact barEven_and_barOdd_forces_zero d hd_even hd_odd h₀

end QOU.MassTheory
