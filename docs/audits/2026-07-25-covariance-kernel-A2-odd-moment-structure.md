# Covariance-kernel epic (`qou-x631`) — ODD hook-power moment structure

**Date:** 2026-07-25 · **Branch:** `claude/even-moment-positivity-proof-qvxk1b` · **Tier:** structural
characterization (exact `Fraction`, `n = 3..14`) · **Discipline:** scope-(a); no fit; nothing wired;
no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`, attack `qou-ogrk` (A2).

## Result

Companion to the [proved even-moment positivity](2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md).
The moments of the covariance measure

> `M_k = Σ_v v^k ν_v = Cov_Planch(Σ_□ h^k, Σ_□ h²)`   (with `ν_v = Cov_Planch(N_v, ω₃)`)

split by parity. For EVEN `k` both weights are shifted-symmetric, `M_{2j}` is an exact polynomial in
`n`, and positivity is **proved** (Lean `YoungDiagramKernel.{threeM4_pos, M6_pos}`). For ODD `k` the
weight `Σ_□ h^{2j+1}` is **not** shifted-symmetric, so `M_{2j+1}` is non-polynomial and the even-`k`
argument does not apply. This audit characterizes the odd-`k` structure exactly.

## Findings

| # | property | status |
|---|---|---|
| 1 | **Non-polynomial.** A degree-`d` Lagrange interpolation of `M_1, M_3, M_5` from small `n` mispredicts at larger `n` (an exact polynomial would not). | confirmed `n ≤ 14` |
| 2 | **Log-convex ⇒ not a positive-measure moment sequence.** `M_{k+1}² > M_k·M_{k+2}` uniformly, i.e. every `2×2` Hankel minor `M_i M_{i+2} − M_{i+1}² < 0`. A positive measure's moments satisfy the *reverse* (Cauchy–Schwarz) inequality, so `{M_k}` is **not** the moment sequence of any positive measure. | confirmed `n ∈ {6,10,14}` |
| 3 | **Transpose identity (exact).** `M_1(n) = 2·Cov_Planch(n_λ, Σ_□ c(□)²)`, where `n_λ = Σ_i i·λ_i`. | confirmed `n = 3..14` |
| 4 | **Signs.** `M_1, M_3, M_5, M_7 > 0` for all tested `n`. | empirical `n ≤ 14` |

### What each finding rules in / out

- **(2) kills the positive-measure route.** The natural way to prove `M_k > 0` for all `k` at once
  would be to exhibit a positive measure `ν ≥ 0` with `M_k = ∫ v^k dν`. Finding 2 shows no such `ν`
  exists (the Hankel matrix is not PSD — its leading `2×2` minors are already negative). Log-convexity
  is the exact reformulation: `M_i M_{i+2} − M_{i+1}² < 0 ⟺ M_{i+1}² > M_i M_{i+2}`.
- **(3) locates `M_1` in the same difficulty class as the kernel.** From `Σ_□ h = n_λ + n_λ' + |λ|` and
  the transpose-invariance of Plancherel measure, the first odd moment reduces to a row-content /
  content-spread covariance `Cov_Planch(n_λ, Σc²)` — structurally a sibling of the open kernel
  `Cov_Planch(f^λ, Σc²) ≤ 0`, **not** an easier object. So `M_1 > 0` is not a low-hanging fruit.
- **(4) is not bootstrapped by (2) + even positivity.** One might hope: even moments `M_{2j}, M_{2j+2}`
  are proved `> 0`, and log-convexity gives `M_{2j+1}² > M_{2j} M_{2j+2} > 0` — but a square being
  positive says nothing about the **sign** of `M_{2j+1}`. So odd-moment positivity is **genuinely
  open**; it does not follow from the even result plus the sequence's log-convexity.

## Scope and honesty

A structural characterization — *which routes are and are not available* for the odd moments — not a
proof of odd positivity, A2, or the kernel. The even/odd split does not by itself prove A2 (whose
weight `ln(v)` is concave, hence not a positive combination of powers — a global argument is still
required, per the [pointwise-route correction](2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md)).

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_A2_odd_moment_structure.py`](../../computations/deltalambda/wlambda_covariance_epic_A2_odd_moment_structure.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-A2-odd-moment-structure.witness.json`

## Cross-references

- Even-moment positivity (proved): [`2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md`](2026-07-25-covariance-kernel-A2-even-moment-positivity-proved.md)
- Moment skeleton (the lead): [`2026-07-25-covariance-kernel-A2-moment-skeleton.md`](2026-07-25-covariance-kernel-A2-moment-skeleton.md)
- Pointwise-route correction: [`2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md`](2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md)
- Attack plan: bean `qou-v8t7`; A2 `qou-ogrk`. Ivanov–Olshanski `math/0304010`.
