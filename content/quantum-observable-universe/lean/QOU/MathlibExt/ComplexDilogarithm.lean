/-
# The complex dilogarithm `Li₂ : ℂ → ℂ` — the Mathlib gap, filled on the disc

**Mathlib has no polylogarithm at all** (checked 2026-08-06: no `Polylog`, no
`dilog`, no `Real.dilog`). QOU already carries a *real* one —
`QOU.QPochhammer.LiTwo : ℝ → ℝ` with `LiTwo_reflection'` proved sorry-free on
`(0,1)` — but the 5₂ saddle sum rule needs `Li₂` at **complex** arguments, and
that is what this file starts.

## Why the complex case is needed

The three roots of the 5₂ saddle cubic `y³ − 2y² + 3y − 1` are

    y₃ = 0.4301597…          real, in (0,1)   — covered by the real `LiTwo`
    y₁ = 0.78492 + 1.30714i  complex, |y₁| = 1.52 > 1
    y₂ = conj y₁

so exactly one of the three is in reach of the existing real theory. See bean
`qou-ph1k`.

## Scope of THIS file — honest

Defines `cLiTwo` by its defining power series and proves exactly three things,
all sorry-free:

* `cLiTwo_zero` — the value at the origin;
* `cLiTwo_term_norm_le` — the term bound `‖zᵏ⁺¹/(k+1)²‖ ≤ ‖z‖ᵏ⁺¹`;
* `cLiTwo_summable` — convergence on the **open unit disc**.

That is the whole of it. This is a foundation, not a usable dilogarithm yet.

It does **not** provide:

* agreement with the real `QOU.QPochhammer.LiTwo` on ℝ (deliberately: that
  import would tie this file to QOU and defeat the upstreaming goal below);
* analytic continuation past `|z| = 1` — needed for `y₁` (`|y₁| = 1.52`);
* the complex Euler reflection `Li₂ z + Li₂ (1−z) = π²/6 − log z · log(1−z)`;
* the inversion formula `Li₂ z + Li₂ (1/z) = −π²/6 − ½·log(−z)²`, the standard
  route to `|z| > 1`.

**None of those is stubbed** — no `sorry`, no `True`-valued placeholder, no
axiom. The file asserts only what it proves. Remaining work: `qou-ph1k`.

In particular this does **not** yet discharge `hrefl` in
`QOU.QBeta.FiveTwo.sum_reflection_of_branch`; the reflection identity is the
next brick, and it needs the continuation first.

## Upstreaming

This is deliberately written in Mathlib style (series definition, `Summable`
lemmas, no QOU-specific dependencies beyond Mathlib itself) so it can be
offered upstream once the continuation and reflection land. Upstreaming is
premature until then and has no bean of its own; it is recorded as a follow-on
inside `qou-gkco`. (An earlier revision of this line cited a bean `qou-mlib`
that was never created — corrected 2026-08-06.)

-- Ref: [manuscript] bean qou-ph1k; docs/coordination/1ppq-qbeta.md 2026-08-02
-- Ref: [lewin1981] Polylogarithms and Associated Functions, L. Lewin
-/
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Analysis.SpecialFunctions.Complex.Log

namespace QOU.MathlibExt

open Complex

/-- The complex dilogarithm as its defining power series,
`Li₂ z = ∑_{k ≥ 0} z^(k+1)/(k+1)²`.

Indexed from `k = 0` with numerator `z^(k+1)` so the `k`-th term is
`z^(k+1)/(k+1)²`, matching `QOU.QPochhammer.LiTwo` term by term. Outside the
closed unit disc the `tsum` is `0` by Mathlib's junk-value convention; the
lemmas below are all guarded by a disc hypothesis. -/
noncomputable def cLiTwo (z : ℂ) : ℂ :=
  ∑' k : ℕ, z ^ (k + 1) / ((k : ℂ) + 1) ^ 2

@[simp] theorem cLiTwo_zero : cLiTwo 0 = 0 := by
  unfold cLiTwo
  simp

/-- Each term is dominated by `‖z‖^(k+1)`, since `1/(k+1)² ≤ 1`. -/
theorem cLiTwo_term_norm_le (z : ℂ) (k : ℕ) :
    ‖z ^ (k + 1) / ((k : ℂ) + 1) ^ 2‖ ≤ ‖z‖ ^ (k + 1) := by
  have hk : (1 : ℝ) ≤ ‖((k : ℂ) + 1) ^ 2‖ := by
    have : ((k : ℂ) + 1) = ((k + 1 : ℕ) : ℂ) := by push_cast; ring
    rw [this, ← Nat.cast_pow, Complex.norm_natCast]
    exact_mod_cast Nat.one_le_iff_ne_zero.mpr (by positivity)
  rw [norm_div, norm_pow]
  calc ‖z‖ ^ (k + 1) / ‖((k : ℂ) + 1) ^ 2‖
      ≤ ‖z‖ ^ (k + 1) / 1 := by gcongr
      _ = ‖z‖ ^ (k + 1) := by ring

/-- The defining series converges on the open unit disc. -/
theorem cLiTwo_summable {z : ℂ} (hz : ‖z‖ < 1) :
    Summable fun k : ℕ => z ^ (k + 1) / ((k : ℂ) + 1) ^ 2 := by
  refine Summable.of_norm_bounded (g := fun k : ℕ => ‖z‖ ^ (k + 1)) ?_ ?_
  · exact (summable_geometric_of_lt_one (norm_nonneg z) hz).mul_left ‖z‖ |>.congr
      fun k => by rw [pow_succ']
  · intro k
    exact cLiTwo_term_norm_le z k

end QOU.MathlibExt
