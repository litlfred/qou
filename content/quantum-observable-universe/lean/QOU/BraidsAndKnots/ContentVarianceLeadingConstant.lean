import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.BraidsAndKnots.ContentVarianceLeadingConstant — the partial-fraction step of `v_A = 8/π²`

The leading constant of the descent-DPP variance of `Σ|c|` is `v_A = 8/π²`
(`docs/audits/2026-08-29-covariance-kernel-M1-tvok-leading-constant-vA.md`, machinery task
`qou-tvok`, epic `qou-h315`). Its derivation reduces — via the IO Kerov CLT and the elementary
closed form `Â_{2m+1} = 8(−1)^{m+1}/(π((2m+1)²−4))` — to the rational-series identity

    Σ_{n odd ≥ 1} 1/[n(n²−4)²] = 1/8,

which is proved by **partial fractions + telescoping** (both the divergent `Σ1/odd` linear tail and
the `π²/8` quadratic tail cancel exactly, leaving `1/16 + 1/16`).

This file formalizes the **algebraic heart** of that step — the partial-fraction identity itself, a
sorry-free `field_simp; ring` fact over any field. It is deliberately scoped: it proves the *summand
decomposition*, **not** the infinite sum (`= 1/8`, a `tsum` telescoping) and **not** `v_A = 8/π²`
(which also invokes the cited IO CLT). Stated over a generic characteristic-zero field (§7c — no `ℝ`;
the identity is purely algebraic, needing only `char ≠ 2` so that `16, 32 ≠ 0`); the reals instantiate
it at use. -/

namespace QOU.BraidsAndKnots.ContentVarianceLeadingConstant

/-- **Partial-fraction decomposition of the `v_A` summand (sorry-free).**

For `x ≠ 0, 2, −2` in any field,

    1/(x(x²−4)²) = 1/(16x) − 1/(32(x−2)) − 1/(32(x+2)) + 1/(32(x−2)²) − 1/(32(x+2)²).

This is the elementary identity underlying `Σ_{n odd} 1/[n(n²−4)²] = 1/8`: summed over odd `n`, the
`1/(16x)`, `1/(x∓2)` linear parts telescope (the divergent tail cancels, coefficient
`1/16 − 1/32 − 1/32 = 0`) and the `1/(x∓2)²` quadratic parts telescope (the `π²/8` tail cancels),
leaving the rational value `1/8`. Here only the per-term algebra is asserted. -/
theorem vA_summand_partial_fractions {K : Type*} [Field K] [CharZero K] (x : K)
    (hx : x ≠ 0) (h2 : x - 2 ≠ 0) (h2' : x + 2 ≠ 0) :
    1 / (x * (x ^ 2 - 4) ^ 2)
      = 1 / (16 * x) - 1 / (32 * (x - 2)) - 1 / (32 * (x + 2))
        + 1 / (32 * (x - 2) ^ 2) - 1 / (32 * (x + 2) ^ 2) := by
  have hx2 : x ^ 2 - 4 = (x - 2) * (x + 2) := by ring
  rw [hx2]
  field_simp
  ring

end QOU.BraidsAndKnots.ContentVarianceLeadingConstant
