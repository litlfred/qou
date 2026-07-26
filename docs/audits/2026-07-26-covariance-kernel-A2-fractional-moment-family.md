# Covariance-kernel epic (`qou-x631`) — A2 as the boundary of the fractional-moment family

**Date:** 2026-07-26 · **Branch:** `claude/covariance-a2-research-2026-07-26` · **Tier:** exact
reduction + new intermediate conjecture (exact-`Fraction` probe, `n ≤ 30`) · **Discipline:**
scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`, attack
`qou-ogrk` (A2), fractional-moment interpolation angle (parallel-attack per the overlap policy;
distinct from the even-moment and depoissonization routes).

## The family

For the covariance measure `ν_v = Cov_Planch(N_v, ω₃)` (mean-zero, `Σv²ν_v = n(n−1)(n−2)/3`,
even moments `M₂, M₄, M₆` proved positive), define the **fractional-moment family**

> `M_α(n) = Σ_v v^α · ν_v`,  `α > 0` real.

This interpolates the proved anchors (`α = 2, 4, 6`) and has **A2 as its `α → 0⁺` boundary**:

> **Bridge (exact, finite sums).** `Σ_v ν_v = 0` gives `M_α = Σ_v (v^α − 1)ν_v`, and
> `(v^α − 1)/α → ln v` as `α → 0⁺`, so `M_α/α → Σ_v ln(v)·ν_v` — i.e. `M(0) = 0`,
> `M′(0⁺) = Σ ln(v)ν_v`, and **A2 ⇔ `M′(0⁺) ≥ 0`**. In particular, if `M_α ≥ 0` on any right
> neighborhood of `0`, then A2 holds at that `n` (one-sided derivative at a boundary minimum).

## The intermediate conjecture (FMP) and the probe

> **(FMP)** `M_α(n) ≥ 0` for all real `α > 0` and all `n ≥ 3`.

Probe [`wlambda_covariance_epic_A2_fractional_moment_family_probe.py`](../../computations/deltalambda/wlambda_covariance_epic_A2_fractional_moment_family_probe.py)
(witness [`wlambda-covariance-epic-A2-fractional-moment-family.witness.json`](../../computations/deltalambda/wlambda-covariance-epic-A2-fractional-moment-family.witness.json)):
`ν_v` in exact `Fraction` arithmetic (zeroth moment `= 0` and `M₂ = n(n−1)(n−2)/3` **asserted
exactly per `n`**), `α`-scan over `[0.02, 6]` (110 grid points), `n ≤ 30`. Findings:

1. **FMP holds on the whole window — zero violations.** Every `M_α > 0`, every `n`.
2. **The minimum always sits at the left edge `α → 0⁺`** — the family is tightest exactly at the
   A2 boundary. The proved even anchors are the "easy" interior; the open content concentrates in
   the small-`α` limit, quantitatively confirming that A2 is the extremal member.
3. **FMP survives past the pointwise-falsification threshold** (`n = 29, 30` included). No
   contradiction with the falsified route: the failing weights `1 − e^{−sv}` are *bounded*
   increasing-concave and lie outside the power family `v^α`; mean-zero converts the falsified
   `Cov(H_s, ω₃) ≤ 0` into "`Σφν ≥ 0` for a *bounded* increasing `φ`", which FMP does not claim.
   The cone boundary is therefore between **unbounded power growth** (holds) and **bounded
   saturation** (fails) — a sharp structural datum for any eventual proof.
4. The small-`α` ratio `M_α/α` matches the log moment per `n` (bridge validated numerically on
   top of its finite-sum proof).

## Why this reframes the open problem

The synthesis map's "the proof must be global, not pointwise" now has a one-parameter
organization: prove `M_α ≥ 0` for `α ∈ (0, 2]` (the interval between the boundary and the first
proved anchor), or even just on `(0, ε)`. Candidate mechanisms, in order of appeal:

- **Interpolation/log-convexity:** if `α ↦ M_α`-type functionals inherit a log-convexity or
  total-positivity structure from the Plancherel weight (à la moment-problem Hankel positivity —
  note the proved `M₂M₆ ≥ ?M₄²`-type data is checkable exactly), positivity could propagate from
  the proved anchors down to `α → 0⁺`.
- **Mellin form:** `v^α` has the Mellin representation over the (sign-mixed) profile
  `Cov(H_s, ω₃)`; the α-family is exactly a one-parameter weighting of the Frullani cancellation
  the synthesis calls for — `Γ(−α)`-weighted instead of `1/s`-weighted.
- **Ivanov–Olshanski in `α`:** for integer `α` the moments are shifted-symmetric (polynomial in
  `n`); real-`α` interpolation of those polynomials (Newton over the integer anchors) may carry
  the positivity with effective control.

## Formalizability (next Lean rung, feasible now)

The bridge is the same `HasDerivAt`-at-`0` pattern already on the scaffold
(`hasDerivAt_tiltedMean_zero`): define `fracMoment k α = Σ_v exp(α·ln v)·ν_v` on
`YoungDiagramKernelPincer`; then `fracMoment k 0 = Σν_v = 0` (`sum_nuV_eq_zero`, proved),
`HasDerivAt (fracMoment k) (Σ ln(v)ν_v) 0` (term-by-term exp derivative), and the conditional
`(∀ α ∈ (0, ε), 0 ≤ fracMoment k α) → 0 ≤ Σ ln(v)ν_v (⇔ leg A2)` via the one-sided-derivative
argument — making **FMP ⇒ A2** a machine-checked implication with FMP as the new instance-less
target above `KernelPincerLegs.leg_A2`.

## Honest scope

FMP is a **conjecture** (numerically exact-verified `n ≤ 30`, `α`-grid `[0.02, 6]`) — a
*sharpening target*, not a proof of anything; A2 and the kernel remain open §3b conjectures. The
even-moment positivity (`M₂, M₄, M₆`) is the sibling's proved anchor set; nothing here overturns
any recorded route verdict. Float enters only in `v^α` evaluation on exact `ν` (sign margins
`~0.4` absolute at the binding minima vs `~1e-9` float noise); the zeroth/second moments are
asserted in exact rational arithmetic.
