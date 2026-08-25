# L4-1 feasibility pass: second-order log-sine expansion (bean qou-xzlt)

**Date**: 2026-08-11 · **Epic**: qou-u1b5 (vdV Lemma 4) · **Verdict**:
FEASIBLE, multi-session; decomposed into three sub-bricks (`qou-me9q`,
`qou-itg0`, `qou-q8lc`). Nothing lands until it lands sorry-free.

## The target

vdV's refined expansion (his §3, extending [Zheng, math/0508138] p. 7),
in the corpus convention `S(n) = Σ_{j≤n} log(2 sin(jπ/N))`:

    S(n) = −(N/π)·Λ(nπ/N) + ½·log( n·sin(rπ)/(rπ) ) + O(1/N),
    r = lim n/N ∈ (0, 5/6),

i.e. the E5c masterErr `O(1)` control sharpened to an identified
`½·log`-term plus `O(1/N)`. Lemma 2's Gaussian window estimates (L4-2)
consume exactly this.

## Route (vdV's own, checked line-by-line against the PDF)

1. **Exact cell-defect representation** (`qou-me9q`): the defect
   `S(n) + (N/π)Λ(nπ/N)` equals `Σ_{j≤n} (N/π)∫₀^{π/N}
   log( sin(jπ/N − u)/sin(jπ/N) ) du` — pure rearrangement of the
   integral against the grid, provable with the existing
   `intervalIntegrable_log_two_sin` / `integral_log_sin_window`
   machinery. **No estimates**; this is the honest first sub-brick.
2. **Stirling half-log** (`qou-itg0`): the `log|(x−u)/x|` part of the
   integrand sums to `−½·log n − ½·log 2π + o(1)` via
   `log n! − n·log(n) + n`-type asymptotics. Mathlib inventory: the
   `Stirling` file exists (`Mathlib/Analysis/SpecialFunctions/Stirling.lean`,
   19 theorems, `stirlingSeq` convergence to `√π`) — the needed
   `log`-form is derivable from it; no new deep analysis, but real
   glue work.
3. **Second-order remainder** (`qou-q8lc`): the `u`-linear Taylor term
   integrates to a Riemann sum converging to `½(log rπ − log sin rπ)`,
   and the `O(u²)` remainder needs a `cot`-derivative bound uniform for
   `x` in compacts of `(0, 5π/6]` — the genuinely new estimate; the
   masterErr toolkit gives the shape but at one order lower.

## What does NOT work

A naive Euler–Maclaurin appeal: Mathlib has no Euler–Maclaurin formula,
and the `log(2 sin)` endpoint singularity at `0` would defeat the
standard statement anyway — vdV's own route (cell defects + Stirling for
the singular part) avoids it, which is why the sub-bricks follow his
proof rather than a textbook summation formula.

## UPDATE (same day, after `qou-q8lc` was opened): Euler–Maclaurin is not needed at all

Building the third sub-brick surfaced a sharper decomposition than this
note anticipated, and it removes the summation-formula question entirely.
Split the cell integrand at the singularity:

    log(2 sin x_j) − log(2 sin u) = (log x_j − log u) + (φ(x_j) − φ(u)),
    φ(x) := log(2 sin x / x),   φ smooth at 0 (removable, φ(0⁺) = log 2).

* The **singular half telescopes EXACTLY** — no asymptotics, no
  hypothesis on `n`, every `h > 0`:
  `Σ_{j≤n} ( ∫_{(j−1)h}^{jh} log u du − h·log(jh) ) = h·(n·log n − n − log(n!))`
  (`log_cell_telescope`, `LogSineSingularPart.lean`, sorry-free). Mathlib's
  `integral_log` is **hypothesis-free** in the current version, so the first
  cell `[0, h]` passes through the singularity for free.
* Stirling (L4-1b) turns that right-hand side into
  `h·(½·log n + ½·log 2π + o(1))` — which is exactly why L4-1b was the right
  second brick.
* What remains is a **`C¹` Riemann-sum defect for the smooth `φ`** — a
  mean-value bound on `φ'`, not a summation formula.

So the owner's standing offer to build Euler–Maclaurin infrastructure is
**not needed for this front**; recorded here so a later agent does not
build it on this file's account. (It may of course be wanted elsewhere.)

## Order of attack

`qou-me9q` (exact, self-contained) → `qou-itg0` (Stirling glue) →
`qou-q8lc` (the estimate). Then L4-1 assembles the three; L4-2 consumes
it.

## RE-CORRECTION (2026-08-11, bean qou-shrp): E–M *is* needed — one step later

The §UPDATE above is right about the **singular** half and wrong to
generalise. Rewriting the smooth half exactly
(`smooth_defect_eq_riemann_defect`, `LogSineRiemannForm.lean`, sorry-free):

    Σ_{i<n} ∫_{cell_i} (φ(x_{i+1}) − φ(u)) du
      = h·Σ_{i<n} φ(x_{i+1}) − ∫_0^{nh} φ

— the smooth half **is** a right-endpoint Riemann-sum defect, whose leading
correction is the classical first Euler–Maclaurin term `(h/2)(φ(nh) − φ(0))`.
That is exactly van der Veen's missing `½`, and it matches the measured value
(`logsine_smooth_defect_constant.py`).

So the correct statement is:

* **singular half** — no summation formula needed; it telescopes exactly, and
  nothing touches the `log(2 sin)` endpoint singularity. (Unchanged.)
* **smooth half** — needs the first E–M correction, on the *regular* function
  `φ`. Mathlib has no Euler–Maclaurin formula, so this is a genuine infra gap.

Mathlib inventory for closing it: `Real.sinc` exists with
`Real.continuous_sinc` and `Real.sinc_zero`, but **no** differentiability or
analyticity — those plus the first E–M correction for `C¹` functions are what
`qou-shrp` must supply.

## CORRECTION (2026-08-19): the §RE-CORRECTION above sent an agent to rebuild
## infrastructure the corpus already had

§RE-CORRECTION closes with a "Mathlib inventory" for the missing
Euler–Maclaurin formula. That inventory is correct about **Mathlib** and does
not mention that **this corpus** has had a composite Euler–Maclaurin rule since
2026-08-10 —
[`QOU/MathlibExt/CompositeEulerMaclaurin.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/CompositeEulerMaclaurin.lean),
already applied to `logSinc` (which is `φ − log 2`) in
[`QOU/Knot/LogSincNearZero.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/LogSincNearZero.lean).

Acting on this file, PR #5297 rebuilt a weaker first-order version of it. The
corpus result identifies the `O(h)` coefficient as `(h/12)(g′(b) − g′(a))`
where #5297 only bounds it, by a factor of exactly 6.

**So: the smooth half of L4-1 is assembled from
`abs_sum_logSinc_sub_euler_maclaurin`, not from `phi_smooth_defect_sharp`.**
Full account, including the root cause (the corpus-grep checklist was not run
before declaring the gap):
[`2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md`](2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md).
