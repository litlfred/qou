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
triple-angle formula gives `τ³ + 3√3·τ² − 3τ − √3 = 0`. So **both** sides are roots of
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
from `tan_two_mul` + `tan_add`, used to pin `τ` by `τ³ + 3√3τ² − 3τ − √3 = 0`
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

## 2026-08-30 — the cubic I recorded for `tan(2π/9)` was WRONG BY TWO SIGNS

Corrected above, in two places, and in the #6141 body.

    RECORDED   τ³ − 3√3τ² − 3τ + √3   evaluates to  −3.85299750422
    CORRECT    τ³ + 3√3τ² − 3τ − √3   evaluates to  −6.9e−41   (i.e. exact)

From `tan(3θ) = (3t − t³)/(1 − 3t²) = tan(2π/3) = −√3`:

    3t − t³ = −√3(1 − 3t²) = −√3 + 3√3 t²   ⟹   t³ + 3√3 t² − 3t − √3 = 0

I dropped the sign when moving the terms across. **I asserted this in three
durable artifacts — this bean twice and the PR body — without ever evaluating
it**, which is the defect class this whole arc exists to document, and the
fourth instance of it today. A hand-derived identity is a claim; one line of
`mpmath` is the check.

### It also turns out not to be needed for the bound

Pinning `τ` by its cubic is one route. The chord only needs an UPPER bound on
`τ` beneath `Im(z)/Re(z)`, and there is rational room:

    τ = tan(2π/9)  = 0.8390996312
    21/25          = 0.84             ← any rational in between works
    Im(z)/Re(z)    = 0.8489044917

So `τ < 21/25 < Im/Re` suffices, and `21/25` has 0.6 % clearance on the left
and 0.6 % on the right. The cubic is still the natural way to *establish*
`τ < 21/25` in Lean (sign-check at a rational, as `FiveTwoShapeBounds` does for
`realRoot`) — but the target is now a single rational inequality rather than a
full bracket, which is strictly less work than the checklist above assumed.

## 2026-08-30 — the `z⁹` route replaces the whole tan/arctan plan

Found while starting the `tan_three_mul` derivation the checklist above calls
for. **That derivation is not needed, and neither is the cubic.**

`2π/9` is exactly one ninth of a full turn, so for `z` whose argument is pinned
to a window narrow enough to fix the branch,

    arg z > 2π/9   ⟺   9·arg z > 2π   ⟺   Im(z⁹) > 0

because `arg(z⁹) = 9·arg z (mod 2π)` and positive imaginary part is exactly
`arg ∈ (0, π)`. The branch window is `arg z ∈ (π/6, π/4)`, i.e.

    √3·Im(z) > Re(z)     and     Im(z) < Re(z)

both **algebraic**, and they put `9·arg z` in `(3π/2, 9π/4) ⊂ (π, 3π)`.

### What it replaces

| | tan route | `z⁹` route |
|---|---|---|
| Mathlib lemma | `tan_three_mul` — **does not exist** | `Complex.arg_pow_coe_angle` — **exists** |
| extra derivation | cubic `τ³ + 3√3τ² − 3τ − √3 = 0` for `tan(2π/9)` | none |
| numeric target | rational bracket `τ < 21/25`, 0.6 % clearance | polynomial sign check |
| robustness | ratio margin 0.0098 | sign of `Im(z⁹)` survives a **1e-3 box** on both coordinates of `z` |

### And it closes on the bracket already proved

    at t = 2/5 (QOU.Knot.FiveTwoShapeBounds.realRoot_gt):
      Im(z⁹) = 0.0022520546  > 0          ✓
      branch window                        ✓ both
    at the true root:
      Im(z⁹) = 0.0145327484
      arg(z⁹) = 0.0515341845 = 9·arg z − 2π   ✓ (branch confirmed)

Critical `t` is **0.3943107684** — the same value the tan analysis gave, as it
must be. So only a LOWER bracket on `realRoot` is needed, and `2/5` is it.

### Revised checklist (supersedes the one above)

1. ~~`tan_three_mul` → cubic for `τ` → rational bracket~~ **not needed**
2. Branch window `√3·Im(z) > Re(z)`, `Im(z) < Re(z)` from `FiveTwoShapeBounds`.
3. `Im(z⁹) > 0` — polynomial in `Re(z)`, `Im(z)`, from the same brackets.
4. `arg z > 2π/9` via `Complex.arg_pow_coe_angle` + `arg_nonneg_iff`.
5. Domain membership, far point, chord — **already done or one-liners**.

The `Real.Angle` bookkeeping in step 4 is the only fiddly part left, and it is
standard rather than missing.

**Recorded because the previous checklist would have sent the next attempt
straight into deriving a Mathlib lemma that the problem does not require** —
and because I only looked for this route after the sign error forced me to
re-derive the cubic by hand. Checking a wrong answer found a better question.

## 2026-08-30 — CORRECTION: the `z⁹` route does NOT close on `2/5`, and the
## mod-cubic reduction gives the real answer

The entry above says *"the `z⁹` route closes on `2/5 < realRoot` ALONE."*
**Wrong.** It came from evaluating `Im(z⁹)` along `z(t) = 1 − 1/y(t)` at
`t = 2/5`, and `|y₁|² = 1/t` — the identity that makes that parametrisation
right — **holds only AT the root**, because it *is* the cubic in disguise
(`t·(t²−2t+3) = 1`). Away from the root, `z(t)` is not the shape of anything.

Same error shape as interval-evaluating `(Re, Im)` as independent variables,
one level down: **evaluating along a parametrisation that is not constrained
the way the actual object is.** Second instance on this item.

### Done correctly: reduce modulo the cubic

With `|y₁|² = 1/t` (valid at the root, i.e. exactly where we work):

    Re(z) = (t² − 2t + 2)/2          Im(z) = t·√(3t² − 4t + 8)/2

`Im(z⁹) = Im(z)·Q(Re², Im²)` with `Q(A,B) = 9A⁴ − 84A³B + 126A²B² − 36AB³ + B⁴`,
and `Re²`, `Im²` are polynomial in `t`. So `Im(z⁹) > 0` is a degree-15
polynomial condition — which, **reduced modulo the cubic, collapses to**

    Q(t) ≡ −3t² + 6t − 2

Exact at the root: both the degree-15 form and the quadratic give
`0.025846128265761922117`.

### The three conditions, and two of them are FREE

| condition | reduced mod cubic | needs |
|---|---|---|
| `Im(z) < Re(z)` (arg < π/4) | `−2t² + 2t = −2t(t−1)` | `0 < t < 1` — **`realRoot_pos` + `realRoot_lt_one`, already proved** |
| `√3·Im(z) > Re(z)` (arg > π/6) | `8t² − 8t + 4 = 8(t−½)² + 2` | **nothing — unconditional** |
| `Im(z⁹) > 0` | `−3t² + 6t − 2` | `t > (3−√3)/3 = 0.4226497` |

So the whole angle condition rests on **one** inequality, and the existing
`realRoot_gt : 2/5 < realRoot` fails it (`Q_red(2/5) = −0.08`).

### The bracket that is actually needed

    t > 2/5     g = -0.056        Q_red = -0.080   BAD
    t > 17/40   g = -0.0094844    Q_red = +0.0081  usable, tight
    t > 3/7     g = -0.0029155    Q_red = +0.0204  ← use this
    t > 43/100  g = -0.000293     Q_red = +0.0253  usable, g very tight

`3/7` balances both margins. It is proved exactly as `realRoot_gt` is —
`g(3/7) < 0` plus monotonicity — so this is a tighter constant in an existing
proof, not a new technique. Rate the earlier "no refinement needed" claim as
superseded: that was true for the *tan* route's ratio test and false for this one.

### Revised remaining Lean

1. `realRoot_gt' : 3/7 < realRoot` — same shape as `realRoot_gt`, tighter constant.
2. `−3t² + 6t − 2 > 0` from (1) — `nlinarith`.
3. The two free branch conditions — from `realRoot_pos` / `realRoot_lt_one` / nothing.
4. `arg z > 2π/9` via `Complex.arg_pow_coe_angle` + `arg_nonneg_iff`.
5. Chord, far point, conclusion — already done or one-liners.

Step 4's `Real.Angle` bookkeeping remains the only fiddly part.

## 2026-08-30 — PROVED: `2π/9 < fiveTwoTet.angle₃`

`QOU/Knot/FiveTwoNinthPower.lean`, **26 declarations**, `lean`-direct exit 0,
`#print axioms` clean on every one (no `sorryAx`), axiom guard 26/26.

The chain, and no step touches a value of a transcendental function:

    z := 1 − y₁⁻¹              arg z IS tetAngle₃ y₁  (zz_arg_eq_angle₃)
    z³ = z − 1                 Landen image of y₁'s cubic; z³−z+1 = (y³−2y²+3y−1)/y³
    z⁹ = −3z² + 4z − 2         one reduction — no degree-9 expansion
    Im(z⁹) = Im z · (4 − 6 Re z)
    ‖y₁‖²·t = 1                straight off `saddle.hprod`
    Re z = (t²−2t+2)/2         so `Re z < 2/3` IS the quadratic −3t²+6t−2 > 0
    arg z ∈ (π/6, π/4)         both from §2's reduced polynomials, by squaring
    arg(z⁹) ≡ 9·arg z (mod 2π) window forces winding number exactly 1
    ⟹ 2π/9 < arg z

### The plan's remaining "hard part" evaporated

The checklist expected the degree-15 polynomial and its reduction modulo the
cubic to be the work. **Both are unnecessary** — they were the shape of the
problem before noticing that `z` has its own cubic. Noticing it turned a
degree-15 identity into `(z−1)³`.

### The two numeric inputs, both small

* `realRoot_gt_three_sevenths` — `2/5` is genuinely not enough (the quadratic is
  negative there); `3/7` is, proved exactly as `realRoot_gt` is.
* The two branch inequalities lift from §2 by squaring, with exact cofactors:
  `(2Re)² − (2Im)² = (−2t²+2t) + (−2t−4)·cubic`, and
  `3(2Im)² − (2Re)² = (8t²−8t+4) + (8t+8)·cubic`.

### Corrected a stale header while landing this

`FiveTwoShapeBounds`'s module header asserted the route "needs interval
arithmetic on `sin` at irrational arguments — machinery the corpus does not
have, and its own project." **False, and it named the wrong obstruction**: no
`Λ` value is needed, because `Cl₂(π/3)` cancels from both sides of the chord.
Corrected in place, with the `2/5`-is-insufficient consequence recorded there.

### NOT proved

That `angle₃` is the **smallest** of the three angles. It is numerically
(`0.7039` against `1.0300` and `1.4077`), and the chord bound wants the minimum.
Either prove the ordering, or prove all three exceed `2π/9` — the latter is
probably easier, since the other two are nowhere near the bound.

That, plus assembling the chord itself, is what stands between here and
`VOL_4_1 < VOL_5_2`.

## 2026-08-30 — the "NOT proved" item is closed: ALL THREE angles exceed `2π/9`

The entry above left the ordering open — that `angle₃` is the smallest, which
the chord bound needs. **The ordering does not have to be proved.** Both other
angles clear the bound by a cheaper route: they exceed `π/4`, and
`π/4 > 2π/9` because `1/4 > 2/9`.

    angle₁ > π/4    ⟸ Im(y₁) > Re(y₁), which reduces to 2t² + 4 > 0 —
                      unconditional, given Re(y₁) > 0 (from t < 1)
    angle₁ < π/2    ⟸ Re(y₁) > 0
    angle₃ < π/4    already proved (zz_arg_lt_pi_div_four)
    angle₂ > π/4    ⟸ angle_sum minus the two above

`all_angles_gt_two_pi_div_nine` therefore holds, and the chord hypothesis is
satisfied for the minimum whichever it is.

Module now **32 declarations**, all `#print axioms` clean, guard 32/32.

**What actually remains for `VOL_4_1 < VOL_5_2`** is only the chord assembly
itself: instantiate `strictConcaveOn_tetVolLine` on the segment from the regular
point, discharge the far point at `s ≈ 3.02` with `LobMonotonicity` +
`Lob_nonneg_of_lt_pi_div_two`, and read off through
`VOL_5_2_eq_three_mul_lob_sum`. Every input to that is now proved.

## 2026-08-30 — the chord assembly, planned out: `s₀ = 3` EXACTLY, and one input missing

Worked the assembly while the merge was rate-limited. It lands on a pleasingly
tight configuration, and on exactly one gap.

### `s₀ = 3` is forced, and it is the right value

Chord from the regular point (`t = 0`) to a far point (`t = s₀`), with the 5₂
triple at `t = 1`:

    f(1) > (1 − 1/s₀)·f(0) + (1/s₀)·f(s₀)          [StrictConcaveOn]
    f(0) = 3Λ(π/3) = Cl₂(π/3)                      [three_Lob_pi_div_three]
    3·f(1) = VOL_5_2                               [VOL_5_2_eq_three_mul_lob_sum]
    VOL_4_1 = 2·Cl₂(π/3)

`3(1 − 1/s₀) ≥ 2 ⟺ s₀ ≥ 3`, so `s₀ = 3` is the smallest that works. And
domain membership at `s₀ = 3` — `π/3 + 3(a₃ − π/3) > 0` — is **exactly**
`3a₃ > 2π/3`, i.e. `a₃ > 2π/9`: the theorem just proved, with nothing to spare.
The two conditions meet at the same point.

Strictness is free: `StrictConcaveOn` gives `>`, so `f(3) ≥ 0` suffices — no
need for `> 0`.

### The one missing input: `f(3) ≥ 0`

At `s = 3` the angles are `bᵢ = 3aᵢ − 2π/3`, numerically
`(0.9957, 2.1288, 0.01718)`, summing to π, with `f(3) = 0.0841`. Proving
`f(3) ≥ 0` needs one of:

* **General nonnegativity of the Λ-sum** — `Λα + Λβ + Λγ ≥ 0` for
  `α, β, γ > 0` summing to π. **Not in the corpus.** Grepped: only
  `volChart_regular_pos` (the regular point) and the max theorems. The natural
  proof uses the apparatus that *is* there — `volChart` continuous on the
  compact `closedSimplex`, `= 0` on its boundary
  (`volChart_eq_zero_of_not_mem`), concave inside — plus the fact that a
  concave function on a convex compact set attains its **minimum at an extreme
  point**, and the closed simplex's three vertices all sit on the boundary
  where the value is 0. That last step is the piece to find or build in Mathlib.

* **Or the specific route**, folding `b₂ > π/2` with `Lob_pi_sub` into
  `(Λb₁ − Λ(b₁+b₃)) + Λb₃` and using `LobMonotonicity` + the corpus's
  `Lob_nonneg_of_lt_pi_div_two`. That needs `b₁ > π/6`, i.e. **`a₁ > 5π/18`**
  (50°) — and the bound proved here is `a₁ > π/4` (45°), which is **not
  enough**. `5π/18` has no convenient tangent, so this route wants its own
  argument.

**The general lemma is the better target**: it is a real gap in the corpus
(ideal tetrahedra having non-negative volume is not currently stated), it is
reusable, and it avoids inventing a bound at 50°.

### Everything else is in place

Domain membership at `0` (trivial) and at `3` (the theorem above), the two
endpoint values, the angle-form bridge, and strictness. So the assembly is
**one lemma away**, and that lemma is about Λ in general, not about 5₂.

## 2026-08-30 — `lob_sum_nonneg` PROVED: the last missing input is in

`0 ≤ Λ a + Λ b + Λ c` for `a, b, c > 0` summing to `π` — the ideal
tetrahedron's volume is never negative. **The corpus did not have this**;
`volChart_regular_pos` bounds one point and the max theorems bound above,
nothing bounded the functional below.

The entry above proposed the extreme-point route (concave function on a convex
compact set attains its minimum at an extreme point). **Not needed** — an
elementary argument works:

    at most one angle exceeds π/2; if one does, Lob_pi_sub folds it and
    Λ is CONCAVE on [0, π/2] with Λ 0 = 0, hence SUBADDITIVE there

    Lob_pi_div_two               Λ(π/2) = 0, since Cl₂(π) = 0
    concaveOn_Lob                from `deriv_deriv_Lob_neg`, already in corpus
    Lob_nonneg_of_le_pi_div_two  concave + vanishing at both endpoints ⟹ ≥ 0
    Lob_add_le                   concave + Λ0 = 0 ⟹ subadditive
    lob_sum_nonneg               three-case split

`deriv_deriv_Lob_neg` (`Λ'' < 0` on `(0, π/2)`) was already proved — I had not
noticed it when writing `LobMonotonicity`'s first pass, which only used the
first derivative.

**`Lob_nonneg_of_le_pi_div_two` is derived, not imported.** The corpus's
`Lob_nonneg_of_lt_pi_div_two` sits in `QOU.Archimedean.HyperbolicVolume`
(`OrthoschemeWedgePair`), whose cone is the orthoscheme/measure-theory
development — far heavier than one line needs — and the derived version covers
the endpoint too.

Five declarations, `lean`-direct exit 0, `#print axioms` clean on all five,
guard 9/9 for the module.

### Every input to the chord is now proved

    f(0) = Cl₂(π/3)                three_Lob_pi_div_three
    3·f(1) = VOL_5_2               VOL_5_2_eq_three_mul_lob_sum
    0, 3 ∈ tetLineDomain           the second IS a₃ > 2π/9, proved
    f(3) ≥ 0                       lob_sum_nonneg  ← this entry
    strictness                     StrictConcaveOn
    s₀ = 3, 3(1 − 1/3) = 2         exact

What remains is assembling them: instantiate `strictConcaveOn_tetVolLine` with
`(u,v,w) = (a₁−π/3, a₂−π/3, a₃−π/3)`, apply the chord at `t = 1` between `0`
and `3`, and read off. No new mathematics.
