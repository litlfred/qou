---
# qou-52ch
title: 'Vol(4_1) < Vol(5_2) reduces to an ALGEBRAIC angle inequality — no certified transcendental needed'
status: todo
type: task
priority: normal
created_at: 2026-08-30T08:45:00Z
updated_at: 2026-08-30T08:45:00Z
---

Follows `qou-f8lit` (#6084, #6138). **Correcting my own characterisation first:**
I closed #6138's report by calling this item *"blocked on method — certified Λ at
angles that are not rational multiples of π."* Measured, that was a claim about a
surface I had not walked. It is wrong twice over: the corpus already carries the
machinery, and the route does not need certified Λ at all.

## The reduction (MEASURED, not proved)

[`computations/knots/five_two_volume_chord_reduction_probe.py`](../computations/knots/five_two_volume_chord_reduction_probe.py)

Rivin concavity (`QOU.Knot.Rivin.strictConcaveOn_tetVolLine`, **proved**, lean-direct
exit 0, zero sorry warnings) makes the ideal-tetrahedron volume
`f(a) = Λ(a₁)+Λ(a₂)+Λ(a₃)` strictly concave along every line in the angle simplex.
Take the segment

    r = (π/3, π/3, π/3)        f(r) = Cl₂(π/3)     the regular tetrahedron
    → simplex BOUNDARY         f     = 0           degenerate: Λ(0)+Λ(b)+Λ(π−b) = 0

The 5₂ angle triple sits on that segment at fraction `t` from `r`, so concavity puts
`f` **above** the chord:

    VOL_5_2 = 3·f(a) ≥ 3(1−t)·Cl₂(π/3)        VOL_4_1 = 2·Cl₂(π/3)

**`Cl₂(π/3)` cancels.** The comparison is `3(1−t) > 2`, i.e. `t < 1/3`, and since the
boundary is reached first by the *smallest* angle, `t = 1 − 3·a_min/π`. So:

> **`VOL_4_1 < VOL_5_2`  ⟸  every dihedral angle of the 5₂ tetrahedron exceeds `2π/9`.**

No certified transcendental value appears on either side. That is the whole point:
the blocker I named — certifying Λ off `π/3` — is not on the path.

## Numbers (60 dps, mpmath, no float64)

    dihedral angles   1.0300194897   1.4077154426   0.7038577213
    2π/9              0.6981317008
    smallest margin   0.0057260205        (0.82 %)
    t                 0.3278653865   vs 1/3, slack 0.0054679468
    3(1−t)            2.0164038404   vs 2
    chord LB VOL_5_2  2.0465321530   vs VOL_4_1 = 2.0298832128   (clears by 0.82 %)
    VOL_5_2 actual    2.8281220883

**It is tight — 0.82 %.** That is the number to carry: any Lean bracket on the angles
must be good to well under a percent, which rules out coarse estimates but is
comfortable for rational brackets on an algebraic quantity.

## Why the inequality is algebraic

`a_min = arg((y₁−1)/y₁)` with `y₁` the non-real root of `X³−2X²+3X−1`, so

    a_min > 2π/9   ⟺   Im(z)/Re(z) > tan(2π/9),   z = (y₁−1)/y₁,  Re(z) > 0

and `tan(2π/9)` is algebraic: with `θ = 2π/9`, `3θ = 2π/3` and `tan(2π/3) = −√3`, the
triple-angle formula gives `τ³ − 3√3·τ² − 3τ + √3 = 0`. So **both** sides are roots of
cubics (one over `ℚ`, one over `ℚ(√3)`) and admit rational brackets — `nlinarith` with
`Real.sq_sqrt 3` territory, not special-function territory.

`QOU.Knot.FiveTwoShapeBounds` (landed #6084) already brackets `y₁`, and **the existing
bracket is already sufficient — no refinement needed.**

### CORRECTION — my first answer here said the opposite, and was wrong

I first interval-evaluated the condition over a rational **box** for `(Re y₁, Im y₁)`,
concluded the existing bounds fall short by `0.0176`, and wrote that denominators of
**200** were required (`156/200 < Re < 157/200`, `261/200 < Im < 262/200`), noting
pointedly that den=100 "still falls short". **All of that is an artefact of the
relaxation.** Re and Im are not independent — both are functions of the single real
root `t` of `X³−2X²+3X−1`:

    Re = (2 − t)/2            Im = √(3t² − 4t + 8)/2

so a box over `(Re, Im)` discards the constraint linking them, and here it discards
enough to **invert the answer**.

### The correct analysis

    Re² − Re + Im²  =  (4t² − 6t + 8)/4

    ratio(t)  =  Im / (Re² − Re + Im²)  =  2√(3t² − 4t + 8) / (4t² − 6t + 8)

`ratio` is strictly **increasing** across the bracket (`ratio′ ≈ 0.25–0.28` on
`[0.39, 0.46]`), so a **lower** bracket on `t` alone settles it:

    critical t (ratio = tan 2π/9)   0.3943107684
    EXISTING realRoot_gt : 2/5 < t  ratio(2/5) = 0.8406972467
    tan(2π/9)                       0.8390996312
    margin                          0.0015976155      SUFFICIENT

**Consequences for the Lean, all in the easier direction.** No new bracketing. The
*upper* bracket `realRoot_lt` and the separate `Re`/`Im` bounds are not needed for this
either — the whole angle condition rests on `2/5 < realRoot` plus monotonicity of a
rational-plus-one-square-root function.

### And it retroactively vindicates a docstring I was about to correct

`FiveTwoShapeBounds` §3 says *"the margins are deliberately loose … there is no reason
to chase digits."* I had this queued as a false claim to fix, on the strength of the
box analysis. Its stated **reason** is still wrong (it cites "34 % headroom" for a
consumer whose chord bound clears by 0.82 %), but its **advice** is right, and my
correction would have been the error. Fix the number, keep the conclusion.

## The Lean gap, stated so nobody reads this as done

Every ingredient exists, but the assembly has one identified hole:

* `strictConcaveOn_tetVolLine` is stated on `tetLineDomain`, and the chord's far
  endpoint is a **degenerate** tetrahedron *on the boundary*. Extending to the closed
  segment needs a continuity step — `QOU.Knot.continuous_Lob` exists — plus
  `FlatTetrahedra.BlochWigner_lob_eq_zero_of_im_eq_zero` for the endpoint value.
* The `a_min` identification needs all three angles bracketed (the reduction is
  cleaner as *"all three exceed 2π/9"*, which avoids proving which one is minimal).

**This is a measurement, not a proof.** Scope (a): the reduction holds numerically at
60 dps and the route is unobstructed as far as measured; it is not established in Lean.

## What it closes if it lands

`QOU.Encounter.FiveTwoVolumeBridge` deliberately states the 4₁/5₂ comparison as an
**equivalence** because the corpus does not prove the inequality — `MostowRigidity`'s
version discharged by `norm_num` on two truncated decimals, which proves nothing about
the exact constants (that was the #6084 finding). This would make it a real inequality.

## Gate status

Precision gates: the five REDs (`q0-anchor flip`, `q0-anchor refill ratchet`,
`float64-padding ratchet`, `q0-value drift ratchet`, `witness scriptFile provenance`)
are **byte-identically present on clean `main`** — measured by stashing this branch and
re-running the full gate, not inferred from "my diff has no witness". The probe itself
carries no `float()` and no numpy.

**Trap worth re-recording:** a `precision-gates.sh` run **writes 9 witness files** as a
side effect. Restore the whole `computations/` tree after any gate run, not the one file
you were looking at — otherwise a dirty tree reads as real work.

## 2026-08-30 — two Lean modules landed; and the remainder is NOT "just arithmetic"

### Landed (#6141, both `lean`-direct exit 0, `#print axioms` clean, guard-registered)

**`QOU/Archimedean/LobMonotonicity.lean`** (4 decls). `Λ′ < 0` exactly where
`2 sin t > 1`, hence `StrictAntiOn Λ (Icc (π/6) (5π/6))`, plus
`Lob_sub_Lob_add_pos` in the form the chord consumes. The corpus already proved
`Λ′ = −log(2 sin t)`; only the consequence was missing.

**`QOU/Knot/FiveTwoAngleSum.lean`** (5 decls). `VOL_5_2 = 3·(Λ a₁ + Λ a₂ + Λ a₃)`,
translating the Bloch–Wigner definition into the **angle functional** that
`strictConcaveOn_tetVolLine` is stated for.

### The boundary-continuity gap does not exist

Earlier entries called the chord's degenerate far endpoint the one genuinely new
Lean. It is not: `volChart` is the honest Λ-sum on all of `ℝ×ℝ`, and
`volChart_eq_zero_of_not_mem` proves it **exactly 0** on the boundary, sorry-free,
via `Lob_pi_sub` + `Lob_zero`. The far point can instead be taken strictly
INTERIOR at `s ≈ 3.02` (boundary is at `3.0500`), where only `f ≥ 0` is needed —
and that follows from the two lemmas above with no value of `Λ`.

### I nearly duplicated `fiveTwoTet`

It already exists in `FiveTwoVolumeConstant.lean`, with the triangulation and a
correction recording that the middle tetrahedron is `1/(1−y₁)`, not `y₁`, the
volume claim surviving via `rotate_angles`. Lean rejected the duplicate.
**My corpus-grep had been at topic level, not at DECLARATION level** — "does the
corpus bound VOL_5_2?" rather than "does `fiveTwoTet` exist?".

### CORRECTION — the remaining step is bigger than I said

I signed off the previous turn calling the remainder *"assembly, arithmetic
against `FiveTwoShapeBounds`, not new mathematics."* Measured, that is wrong.
`FiveTwoShapeBounds` brackets `Re` and `Im` of the **shape**; the chord needs
brackets on the **angles**, which are `arg` of derived complex numbers. The
corpus has **no** numeric `arg`/`arctan` bracketing at all — only qualitative
facts (`arg_nonneg_of_im_nonneg`, `arg_ne_pi_of_im_ne_zero`).

The route, with each prerequisite checked against Mathlib rather than assumed:

    arg z > 2π/9  ⟺  tan(arg z) > tan(2π/9)      [both in (0, π/2)]
                  ⟺  Im z / Re z > τ,  τ = tan(2π/9)

    Complex.tan_arg : Real.tan (arg x) = x.im / x.re        EXISTS
    strictMonoOn_tan, tan_lt_tan_of_nonneg_of_lt_pi_div_two EXISTS
    Real.tan_pi_div_three                                   EXISTS
    Real.tan_two_mul                                        EXISTS
    tan_three_mul                                           **DOES NOT EXIST**

So the one genuinely missing piece is a **triple-angle step for `tan`**, derived
from `tan_two_mul` + `tan_add`, used to pin `τ` by `τ³ − 3√3τ² − 3τ + √3 = 0`
(from `tan(3·2π/9) = tan(2π/3) = −√3`) and then bracket it rationally.

That is a real tranche, not arithmetic. Naming it precisely so the next attempt
starts from the gap rather than rediscovering it.

### Remaining checklist

1. `tan_three_mul` (derive) → the cubic for `τ = tan(2π/9)` → rational bracket.
2. Angle brackets for `a₁, a₂, a₃` via `Complex.tan_arg` + `FiveTwoShapeBounds`.
3. Domain membership of `0, 1, s₀` in `tetLineDomain` at `s₀ = 151/50`.
4. Far point `f(s₀) ≥ 0` — the two `LobMonotonicity` lemmas, already landed.
5. Chord from `strictConcaveOn_tetVolLine`; conclude via `VOL_5_2_eq_three_mul_lob_sum`.

Steps 4 and 5 are done or one-liners. **1 and 2 are the work.**
