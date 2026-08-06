/-
# Bridge: the complex dilogarithm agrees with QOU's real one

`QOU.MathlibExt.cLiTwo` is deliberately Mathlib-only so it stays upstreamable,
so it cannot mention `QOU.QPochhammer.LiTwo`. This file is the bridge, and it
is where the leverage is: QOU already carries ~20 sorry-free files of *real*
dilogarithm theory (`DilogReflection`, `DilogPartA*`, `DilogPartB*`), and a
single cast lemma makes all of it available to the complex side.

## Why this is the high-leverage brick

The remaining obstacle to the 5₂ saddle sum rule (bean `qou-0yqu`) is the
complex Euler reflection identity, needed at `y₁` with `|y₁| = 1.52 > 1`. The
standard route is analytic continuation from the real segment via the identity
theorem (`AnalyticOnNhd.eqOn_of_preconnected_of_frequently_eq`), which needs
the identity to hold on a set with an accumulation point.

`cLiTwo_reflection_ofReal` below supplies exactly that set — the real interval
`(0,1)` — by transporting the already-proved `LiTwo_reflection'`. It is the
input to the continuation argument, not the continuation itself.

## What is NOT here

The continuation argument itself, and hence the complex reflection identity at
non-real arguments. `cLiTwo` is only known to converge on the open unit disc
(`cLiTwo_summable`), so analyticity off the real axis is not yet established.
Nothing is stubbed: no `sorry`, no axiom. Tracked in `qou-gkco`.

-- Ref: [manuscript] beans qou-gkco, qou-ph1k
-/
import QOU.MathlibExt.ComplexDilogarithm
import QOU.Archimedean.DilogReflection

namespace QOU.Archimedean

-- `LiTwo` and its theory live in `QOU.QPochhammer` (in
-- `QOU/Archimedean/DilogarithmArchimedeanLimit.lean` — the namespace does not
-- follow the directory), so it must be opened explicitly.
open Complex QOU.MathlibExt QOU.QPochhammer

/-- **The bridge.** `cLiTwo` at a real argument is the real `LiTwo`.

Unconditional: both series are the same termwise after casting, and where
neither converges both `tsum`s are `0` by Mathlib's junk-value convention, so
no disc hypothesis is needed. -/
theorem cLiTwo_ofReal (x : ℝ) : cLiTwo (x : ℂ) = ((LiTwo x : ℝ) : ℂ) := by
  unfold cLiTwo LiTwo
  rw [Complex.ofReal_tsum]
  refine tsum_congr fun k => ?_
  push_cast
  ring

-- NOTE (2026-08-06): a `cLiTwo_one : cLiTwo 1 = π²/6` corollary follows in one
-- line from `QOU.QPochhammer.LiTwo_one` + `cLiTwo_ofReal`, but is NOT included
-- here because it could not be VERIFIED in this environment: the restored
-- `lake-cache/qou-v4-24-0` olean for `DilogarithmArchimedeanLimit` is stale —
-- it exports `LiTwo` but not `LiTwo_one` (unknown identifier even fully
-- qualified). Rather than ship an unverified lemma, it is left out; add it
-- once the cache branch is reseeded against current `main`.

/-- **The Euler reflection identity on the real segment, stated in ℂ.**

Transported from the sorry-free real `LiTwo_reflection'`. This is the set on
which the complex reflection identity is already known — the input to an
identity-theorem continuation, which is the remaining work (`qou-gkco`). -/
theorem cLiTwo_reflection_ofReal {x : ℝ} (hx0 : 0 < x) (hx1 : x < 1) :
    cLiTwo (x : ℂ) + cLiTwo (1 - (x : ℂ))
      = (Real.pi : ℂ) ^ 2 / 6
        - Complex.log (x : ℂ) * Complex.log (1 - (x : ℂ)) := by
  have hx1' : (0 : ℝ) ≤ 1 - x := by linarith
  have hsub : (1 : ℂ) - (x : ℂ) = ((1 - x : ℝ) : ℂ) := by push_cast; ring
  rw [hsub, cLiTwo_ofReal, cLiTwo_ofReal, ← Complex.ofReal_log hx0.le,
    ← Complex.ofReal_log hx1']
  have hr := LiTwo_reflection' x hx0 hx1
  have : ((LiTwo x + LiTwo (1 - x) : ℝ) : ℂ)
      = ((Real.pi ^ 2 / 6 - Real.log x * Real.log (1 - x) : ℝ) : ℂ) := by
    exact_mod_cast congrArg (fun r : ℝ => (r : ℂ)) hr
  push_cast at this ⊢
  linear_combination this

end QOU.Archimedean
