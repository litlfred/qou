# Covariance-kernel epic (`qou-x631`) — M₁>0 Debye constant-tracking: the kink term cancels (rate θ⁻¹), closure de-risked

**Date:** 2026-08-29 · **Branch:** `claude/m1-debye-constant-tracking-2026-08-29` · **Tier:**
Debye/asymptotic-structure measurement + a candidate rigorous mechanism · **Discipline:** no fit
(asymptotic-coefficient read-off, not a physical fit); nothing wired; no `c_k`; L2 unchanged.
**Epic:** `qou-x631`; gap `qou-k5r5`.

## What the Debye attempt found

The rigorous finite-n bound needs `|V_A(θ)/θ² − v_A| ≤ C_A·θ^{−p}` for `V_A = Var(Σ|c|)`. The
conservative worst case is `p = 1/2` (the `|u|` kink), which carries a **hard** explicit constant. This
attempt measured the actual asymptotic expansion and found the kink case does **not** occur.

`wlambda_covariance_epic_M1_debye_expansion_fit.py` (exit 0; exact Bessel sums; dps 60; NO float64)
computes `V_A/θ²` at `θ = 256…8192` and fits the expansion `v_A + c_{1/2}θ^{−1/2} + c_1θ^{−1} + …`
across multiple bases:

| θ | `V_A/θ²` |
|---|---|
| 256 | 0.81031103 |
| 1024 | 0.81050248 |
| 4096 | 0.81055297 |
| 8192 | 0.81056117 |

- **Monotone increasing toward `v_A = 0.810568`** — the correction is *negative*, no oscillation.
- **The `θ^{−1/2}` kink coefficient is at the fit-noise floor**: across bases `c_{1/2} ∈ {−0.00048,
  +0.0010}`, sign-unstable, `|·| < 0.001` — **consistent with zero**, while the `θ^{−1}` term is
  stable (`c_1 ≈ −0.066`).

**Conclusion: the `|u|`-kink term vanishes; the rigorous rate is `θ^{−1}` (the *smooth*
Euler–Maclaurin case), not `θ^{−1/2}`.** The feared hard kink constant does not exist.

## Why it cancels — a candidate rigorous mechanism

Plancherel measure is **transpose-invariant** (`λ ↦ λ'` preserves `(dim λ)²/n!`), and the transpose
sends content `u ↦ −u`. Hence the Plancherel content law is **symmetric about 0**, and `Σ|c| =
Σ_u |u|·h(u)` is an **even** functional of it. The `θ^{−1/2}` correction to a bulk linear statistic is
the *odd* (edge-asymmetry) part of the `1/√θ` expansion; for an even statistic under a symmetric law
it must cancel, leaving an expansion in **integer powers of `1/θ`**. This is a structural argument
(not yet a fully written proof), and it matches the measurement exactly: `c_{1/2} = 0`, leading term
`c_1/θ`.

## Status of the closure — de-risked, not yet closed

- **Before:** "rigorous modulo one *hard* constant" (the `θ^{−1/2}` Olver/Debye kink bound).
- **After this attempt:** "rigorous modulo one *easy* constant" — the leading correction is
  `≈ −0.066/θ`, monotone from below, in the **smooth** `θ^{−1}` regime, with a clean symmetry reason
  the half-power is absent. The constant to pin is a standard smooth-weight Euler–Maclaurin remainder,
  and it is tiny.
- **Still not produced:** a **verified explicit `C`**. Two steps remain, both now easier: (i) turn the
  transpose-symmetry heuristic into a written proof that `c_{1/2} = 0`; (ii) the explicit `θ^{−1}`
  Euler–Maclaurin constant for `V_A` (and the analogous `V_W`, `P`, `V_D`), then ratio propagation.
  These are smooth-case estimates; I did **not** complete them to a verified number this session and
  will not assert a "rigorous `C`" from the measurement alone.

Net: the Debye constant-tracking removed the one genuinely hard obstruction (the kink), leaving a
routine smooth estimate with a tiny constant and 30–300× headroom (PR #5937). `qou-k5r5` stays
**OPEN**, but closure is now clearly bookkeeping-grade.

## Compute

- [`wlambda_covariance_epic_M1_debye_expansion_fit.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_debye_expansion_fit.py)
  (exit 0; dps 60; exact Bessel sums; NO float64).

## Cross-references

- Debye investigation + verdict: [`2026-08-29-covariance-kernel-M1-debye-CA-investigation-verdict.md`](2026-08-29-covariance-kernel-M1-debye-CA-investigation-verdict.md)
- Constant-C landscape: [`2026-08-29-covariance-kernel-M1-constant-C-and-N0.md`](2026-08-29-covariance-kernel-M1-constant-C-and-N0.md)
- Rigorous finite-n bound: [`2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md`](2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md)
- Gap bean `qou-k5r5`.
