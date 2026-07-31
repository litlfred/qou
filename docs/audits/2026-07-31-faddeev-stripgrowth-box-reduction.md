# Strip-growth reduces to a fundamental-domain bound (2026-07-31)

**Branch:** `claude/faddeev-stripgrowth-box-reduction-2026-07-31`. **Front 2** of the
A_ω work (owner-reassigned from the stalled `qou-7xvy`). **Reduction, not closure.**

## The gap

The Faddeev–Volkov A_ω uniqueness leg (`FaddeevPhiFullUniqueness.faddeevPhi_uniqueUpToScalar`)
is conditional on the class `FaddeevPhiPhysical`, whose one genuine open field is
`instStripGrowth` (`FaddeevPhiStripGrowth`): that a *second* Faddeev shift solution `Φ` is
**comparable in modulus** to `phiBProd` (`∃ C > 0, ∀ z, ‖Φ z‖ ≤ C‖phiBProd z‖ ∧
‖phiBProd z‖ ≤ C‖Φ z‖`). The shift equations alone do **not** give this — the
elliptic-freedom obstruction shows solutions exist that violate it — so it is the
physical Faddeev–Kashaev asymptotic content, a genuine analytic input, not a Lean
technicality.

## The reduction (this brick)

`QOU/QBeta/FaddeevStripGrowthBoxReduction.lean` (sorry-free, `lean`-direct exit 0) makes
that global analytic axiom **local**:

- **`norm_le_of_periodic_ballBound`** — a function `r : ℂ → ℂ` periodic under both vectors
  of an `ℝ`-basis of `ℂ`, bounded by `C` on the closed ball of radius `‖bas 0‖+‖bas 1‖`,
  is bounded by `C` **everywhere**. (Reduce the two `ℝ`-coordinates of `z` mod 1 via
  `Int.fract`; the lattice translation is invisible to `r`.)
- **`comparable_of_periodic_ballBound`** — the two-sided form: if the ratio is
  doubly-periodic and both `‖r‖ ≤ C` and `1/C ≤ ‖r‖` hold on the fundamental ball, they
  hold globally — the `FaddeevPhiStripGrowth.comparable` shape.

The point: the ratio `Φ/phiBProd` **is** doubly-periodic — the FaddeevPhi shift prefactors
cancel (`CyclicDilogPentagon.ratio_ib_periodic`/`ratio_ibinv_periodic`, on main). So the
*global* comparability bound reduces to a bound on **one compact fundamental
parallelogram**, where the Faddeev asymptotic is a finite, checkable estimate rather than
a global one.

This is the **non-holomorphic** companion to `DoublyPeriodicLiouville.const_of_doublyPeriodic`
(which needs analyticity to conclude *constancy*): here only periodicity is used, to
propagate a **modulus bound** — which is exactly what `comparable` is (a norm inequality,
not a holomorphic statement). Same `Int.fract`/`periodic_zsmul` lattice machinery.

## Scope (STRICT)

Reduction, **not** closure. It converts the *global* strip-growth axiom into a
*fundamental-domain* one — the standard, tractable form. It does **not** prove that bound
for a second solution: that remains the physical Faddeev asymptotic on the compact
domain, plus divisor matching at `phiBProd`'s zeros (the separate same-divisor input,
where the ratio-norm approach does not directly apply). No fit; nothing wired; uses only
on-main `DoublyPeriodicLiouville`. The residual physical input is now a compact-domain
estimate, which is where the `qou-ja69` toolbox note (4₁ saddle product-growth mechanics)
applies.
