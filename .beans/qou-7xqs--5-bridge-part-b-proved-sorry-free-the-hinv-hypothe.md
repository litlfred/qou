---
# qou-7xqs
title: '5₂ bridge: part (B) proved sorry-free; the hinv hypothesis it replaced was FALSE'
status: in-progress
type: task
priority: normal
created_at: 2026-08-31T03:03:48Z
updated_at: 2026-08-31T03:04:12Z
---


Branch `claude/mt7r-archimedean-eval-2026-08-24`.

## What landed

`QOU/Archimedean/FiveTwoOhtsukiBridge.lean` has **no `sorry`**. The one that was
there — `ohtsuki_sum_im_eq_three_blochWigner`, part (B) — is proved, and the
bridge now consumes it instead of taking `hzeta`/`hvol` on faith.

Sorry-free (all `[propext, Classical.choice, Quot.sound]`, no `sorryAx`):

* `QOU.Archimedean.arg_ne_pi_of_im_ne_zero`, `arg_one_div_of_im_ne_zero`,
  `arg_conj_of_im_ne_zero`, `one_div_im_ne_zero`
* `QOU.Archimedean.BlochWigner_lob_inv` — `D(1/z) = −D(z)` for `z.im ≠ 0`
* `QOU.Archimedean.BlochWigner_lob_conj` — `D(z̄) = −D(z)`
* `QOU.Archimedean.BlochWigner_lob_conj_inv` — `D(conj (1/z)) = D(z)`
* bridge: `cubic_one_sub`, `eq_neg_one_sub_cube`, `xOf_mul_self`,
  `xOf_eq_one_div_sq`, `one_sub_one_div_xOf`, `one_sub_re_pos`,
  `ohtsuki_sum_im_eq_three_blochWigner` **(B)**,
  `two_pi_mul_re_of_div_two_pi_I`, `two_pi_re_zeta_eq_three_blochWigner`,
  `saddle_root_conj_inv`, `conj_inv_im_pos`, `conj_inv_is_five_two_shape`,
  `volume_conjecture_five_two_wired`

## ⚠ The hypothesis that was FALSE

The old (B) statement carried, as `_hinv`,

    ∀ z ≠ 0, Im Li₂(z) + Im Li₂(1/z) = −2·arg(1−z)·log‖z‖

described in the docstring as "the inversion formula". It is not. Euler's
inversion has imaginary part `−log‖z‖·arg(−z)`. Measured at 40 dps against
`mpmath.polylog`, the discharged form is off by `−2.97e-1` at `y₀`, `−9.17e-2`
at `x₀`, `−7.25e-3` at `x₀y₀`. It is also inconsistent with the sibling
hypothesis `_hbw`, which already pins `Im Li₂` completely — so the `sorry` was
guarding a hypothesis set no dilogarithm satisfies. **Removed, not replaced:**
the correct inversion is derivable from `_hbw` plus `D(1/z) = −D(z)`, so the
theorem now needs one identity where it claimed to need two.

## Two other wrong claims in the old docstrings

* "step 4 … using `D(x₀) = D(y₀)` and `D(x₀y₀) = D(y₀)/2`". The second is
  **not needed** — `D(x₀y₀)` cancels against itself between the `Li₂(x₀y₀)` and
  `Li₂(1/(x₀y₀))` terms. (It is true; measured to 50 dps. It is just not on the
  path.)
* `one_sub_one_div_xOf` (`1 − 1/x₀ = 1/(1−y)`) was drafted as needing the cubic
  in the form `w³ = w − 1`. It needs no cubic at all: it is
  `one_sub_inv_mobius`, the Möbius 3-cycle applied twice.

## The proof, for the next reader

Put `w = 1 − y`. The cubic says `w³ = w − 1`, and then every one of Ohtsuki's
five arguments is `±w^k`:

    x₀y₀ = −w      y₀ = −w³      x₀ = 1/w²      1 − 1/x₀ = 1/w

so each `log‖·‖` is an integer times `log‖w‖` and each `arg` an integer times
`arg w`. `D` gives `3·D(y₀)`; the `arg`·`log` corrections carry coefficients
`−1 − 3 + 6 − 2 = 0`.

The one non-algebraic input is `Re(1 − y₀) > 0` (`one_sub_re_pos`), which pins
`w` to the fourth quadrant so `arg w ∈ (−π/2, 0)`. Eliminating `Im` from
`w³ − w + 1 = 0` gives `8s³ − 2s − 1 = 0` for `s = Re w`, and that has no root
with `s ≤ 0` because `8r³ − 2r + 1 = 2r(2r−1)² + 8(r−¼)² + ½ > 0` for `r ≥ 0`.

## (D)

`hvol` is discharged. `FiveTwoTriangulation` lives at `y₊`, the upper root of
the **saddle** cubic; Ohtsuki's `y₀` is a root of the **reciprocal** cubic.
`y₊ = conj (1/y₀)` (checked to 40 dps, difference exactly 0), and
`BlochWigner_lob_conj_inv` gives `D(y₊) = D(y₀)`. `volume_conjecture_five_two_wired`
takes `[FiveTwoTriangulation (conj (1/y)) vol]`; `conj_inv_is_five_two_shape`
proves that shape satisfies both of the class's side conditions, so the instance
is asked only for the geometric content.

## Priority 3 — putting the two new MathlibExt bricks to work

**`ExponentialGrowthRate.tendsto_log_div_of_sandwich` — CONSUMED.**
`QOU/Knot/WhiteheadLinkScaffold.tendsto_log_norm_whiteheadLinkKashaev_of_majorant`
now calls it instead of hand-rolling the squeeze. The instantiation is
`m = majorant/N^p`, `S = ‖J_N‖`, `c = N^p`: `m ≤ S` is exactly
`VdVWhiteheadLemma4.phase_cost`, `S ≤ c·m` is exactly the sorry-free
`norm_whiteheadLinkKashaev_le`. Statement unchanged; still sorry-free; all five
downstream modules recompile. Note the direction: the lemma wants the *small*
side's rate and here the *large* side's is what is known, so the known side is
divided by `N^p` to land in the `m` slot — free, because `log(N^p)/N → 0` is
the same sub-exponentiality the `c` slot wants.

**`HalfPlaneNonCancellation.cos_mul_sum_norm_le_norm_sum` — NO CONSUMER; does
not fit.** Reported rather than forced.

* The only place in the corpus with `norm_sum_le` on a sum whose lower bound is
  open is `WhiteheadLinkScaffold:115`. Its outer Fresnel phase is
  `θ_n = −n(n+1−N)π/(2N)`, which sweeps `(N−1)²π/(8N) ≈ Nπ/8` radians —
  **unbounded**. Measured arc covered mod 2π: 135.0° (N=8), 303.8° (N=32),
  340.3° (N=128), 349.5° (N=256), i.e. → 360°. A half-plane hypothesis needs
  `α ≳ 175°`, where `cos α < 0` and the conclusion is vacuous.
* The *inner* sums, which the module's docstring claimed the lemma "settles
  outright", are already sums of real positive terms in the corpus's own
  transcription (`whiteheadTerm_pos`, `whiteheadLink_inner_pos`), so
  `‖Σ‖ = Σ‖·‖` on the nose and a `cos α` factor buys nothing.
* A conditional "phases half-plane-confined ⟹ VdVWhiteheadLemma4" was
  deliberately **not** written: its hypothesis is measured false, so it would
  be vacuous content dressed as progress.

The measurement is recorded in the module header instead — it closes the
elementary route, which is worth more than a bridge nobody can cross.

## Two stale docstring claims corrected

* `QOU/Knot/WhiteheadVolumeConjecture.lean` said (twice) that
  `whitehead_volume_conjecture` is "state-and-queued (`sorry` + Ref)" / "the one
  honest `sorry` here". **There is no `sorry` token in that file** — the proof
  is `exact hi.limit` from a §3b class carrier. A corpus `sorry`-audit reads the
  old wording as a hit and a reader hunting the gap looks in the wrong place.
* `QOU/MathlibExt/HalfPlaneNonCancellation.lean` claimed the lemma "settles the
  inner sums outright and isolates the outer one" — see above; neither half was
  a gain.
