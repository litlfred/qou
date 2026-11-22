import Mathlib.Data.Real.Basic
import Mathlib.Data.Real.Archimedean
import Mathlib.Algebra.Order.Floor.Semiring

/-!
# QOU.FluidDynamics.yekutieli_obstruction_level — obstruction level = ⌊s⌋+1

The **Yekutieli obstruction level** and its identification with the terminal
Sobolev regularity, sharpening the categorical→classical bridge (Bridge B, B2)
of the q-NS classical-gap program
([`docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md`](../../../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md)).

**Scope discipline (owner directive 2026-07-24).** *Given a QOU*, `s(t)` is the
Sobolev regularity of the **QOU's own internal `q = 1` flow**, not of a classical
`ℝ³` Navier–Stokes solution. This file fixes the QOU-internal obstruction↔Sobolev
bookkeeping; it makes no claim about the external PDE.

## What this adds

`p3-blowup-yekutieli` (`blowup_yekutieli`) reformulates smoothness as lifting
through the whole brane tower: `v smooth ⟺ κ_n(v) = 0 ∀ n`, and blow-up as the
existence of a finite obstruction level `n*`. That block also records the
*mechanism* connecting the categorical obstruction to the Sobolev regularity
`s(t)` of the QOU-internal `q = 1` flow:

> at `q = 1` the `n`-th brane-tower class `κ_n(v)` is nonzero **iff** the `n`-th
> jet of `v` is undefined, i.e. **iff `n > s(t)`**; a finite-time singularity has
> terminal regularity `s* < ∞`, and the obstruction level is `n* = ⌊s*⌋ + 1`.

This file formalises that correspondence and **proves** `n* = ⌊s⌋ + 1` is exactly
the least level at which lifting fails:

* `yekutieli_obstruction_at_level` — the class κ_{n*} does not vanish;
* `yekutieli_no_obstruction_below` — every level below `n*` lifts cleanly;
* `yekutieli_obstruction_level_least` — `n*` is the minimal failing level.

This is the concrete realisation of Bridge (B)'s **B2** identification (the
categorical lift ⟺ classical `Hⁿ`-smoothness dictionary). It is still on the
categorical/definitional side of the wall — it does **not** prove that a
classical NS solution attains a finite `s*` (that existence statement is the
open Clay content, `conj:regularity-breakdown` R1/R2). It fixes the *bookkeeping*
between the two sides once a terminal `s` is given.

## Base ring (§7c)
Genuinely archimedean: `s : ℝ` is the (real) Sobolev exponent and the argument
uses the order structure and `Nat.floor`. `ℝ` is correct here — this block lives
on the archimedean side of the substrate wall.

## References
- [leitner2026] lifting-and-descent/p3-blowup-yekutieli (`prop:blowup-yekutieli`)
- [leitner2026] fluid-dynamics/ns-obstruction-tower, regularity-breakdown
- Yekutieli, *Nonabelian multiplicative integration on surfaces* / the lifting
  framework (DOI 10.1007/s00029-010-0029-8, `yekutieli2010`)
-/

namespace QOU.FluidDynamics

/-- Yekutieli obstruction–Sobolev correspondence at a fixed time.

    `sobolev` is the terminal Sobolev regularity `s = s(t)` of the QOU-internal
    `q = 1` flow's velocity
    (`0 ≤ s`, finite — the finite-time-blow-up regime); `obstruction n` is the
    proposition "`κ_n(v) ≠ 0`", i.e. lifting fails at brane-tower level `n`. The
    single field `obstruction_iff_exceeds` is the manuscript's mechanism
    (`p3-blowup-yekutieli`): the level-`n` class is nonzero exactly when `n`
    exceeds the Sobolev regularity, so the `n`-th jet is undefined. -/
class YekutieliObstructionLevel where
  /-- Terminal Sobolev regularity `s(t)` of the velocity field. -/
  sobolev : ℝ
  /-- Regularity is non-negative. -/
  sobolev_nonneg : 0 ≤ sobolev
  /-- "`κ_n(v) ≠ 0`": lifting fails at brane-tower level `n`. -/
  obstruction : ℕ → Prop
  /-- **Mechanism (`p3-blowup-yekutieli`):** the level-`n` obstruction class is
      nonzero iff `n` exceeds the Sobolev regularity. -/
  obstruction_iff_exceeds : ∀ n : ℕ, obstruction n ↔ sobolev < (n : ℝ)

/-- **The Yekutieli obstruction level** `n* = ⌊s⌋ + 1`. -/
noncomputable def obstructionLevel [ctx : YekutieliObstructionLevel] : ℕ :=
  ⌊ctx.sobolev⌋₊ + 1

/-- **Lifting fails at `n*`.** The obstruction class `κ_{n*}` does not vanish,
    because `s < ⌊s⌋ + 1 = n*`. -/
-- Ref: [leitner2026] lifting-and-descent/p3-blowup-yekutieli
theorem yekutieli_obstruction_at_level [ctx : YekutieliObstructionLevel] :
    ctx.obstruction obstructionLevel := by
  rw [ctx.obstruction_iff_exceeds]
  have h : ctx.sobolev < (⌊ctx.sobolev⌋₊ : ℝ) + 1 := Nat.lt_floor_add_one _
  simpa [obstructionLevel] using h

/-- **Every level below `n*` lifts cleanly.** For `n < n* = ⌊s⌋ + 1`, i.e.
    `n ≤ ⌊s⌋ ≤ s`, the obstruction class vanishes (`¬ (s < n)`). -/
-- Ref: [leitner2026] lifting-and-descent/p3-blowup-yekutieli
theorem yekutieli_no_obstruction_below [ctx : YekutieliObstructionLevel]
    (n : ℕ) (hn : n < obstructionLevel) : ¬ ctx.obstruction n := by
  rw [ctx.obstruction_iff_exceeds]
  -- n < ⌊s⌋ + 1  ⇒  n ≤ ⌊s⌋  ⇒  (n : ℝ) ≤ s  ⇒  ¬ (s < n)
  have hle : n ≤ ⌊ctx.sobolev⌋₊ := Nat.lt_succ_iff.mp hn
  have h1 : (n : ℝ) ≤ (⌊ctx.sobolev⌋₊ : ℝ) := by exact_mod_cast hle
  have h2 : (⌊ctx.sobolev⌋₊ : ℝ) ≤ ctx.sobolev := Nat.floor_le ctx.sobolev_nonneg
  exact not_lt.mpr (le_trans h1 h2)

/-- **`n*` is the least failing level.** It is nonzero at `n*` and vanishes at
    every smaller level — the manuscript's `n* = ⌊s*⌋ + 1` is exactly the
    minimal brane-tower level at which the classical velocity ceases to lift. -/
-- Ref: [leitner2026] lifting-and-descent/p3-blowup-yekutieli, regularity-breakdown
theorem yekutieli_obstruction_level_least [ctx : YekutieliObstructionLevel] :
    ctx.obstruction obstructionLevel ∧
      ∀ n : ℕ, n < obstructionLevel → ¬ ctx.obstruction n :=
  ⟨yekutieli_obstruction_at_level, yekutieli_no_obstruction_below⟩

end QOU.FluidDynamics
