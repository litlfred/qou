# Covariance-kernel epic (`qou-x631`) — `mean_zero` discharged on the certified range, and step 3 of the (TAIL) first instance

**Date:** 2026-08-03 · **Branch:** `claude/covariance-meanzero-nu-n-2026-08-03` · **Tier:**
machine-checked (all statements sorry-free, lean-direct exit 0) · **Discipline:** scope-(a); no
fit; nothing wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`, attack `qou-ogrk` (A2).

## Finding 1 — a *provable* premise was sitting beside two open ones

The pincer scaffold carries its inputs in the instance-less class `KernelPincerLegs`:

| field | epistemic status |
|---|---|
| `mean_zero` — `E₂[ω₃] = 0` | **exact classical identity** — not conjectural |
| `leg_A2` — `Cov₂(ln f, ω₃) ≤ 0` | genuinely open |
| `leg_A3` — remainder bound | genuinely open |

Every downstream `[KernelPincerLegs k]` theorem therefore assumed a *provable* fact alongside the
two real conjectures — precisely the `conditional-proved ≠ premise-established` hazard (AGENTS.md,
STRICT). The ℤ-form of the identity, `secondMomentKernel k = Σ_λ (f^λ)²·ω₃(λ) = 0`, was already
`decide`-verified for `k ≤ 7` and *documented* as exact, but was never connected to the ℝ-side
class field — so the discharge had never actually happened.

**Now discharged on the certified range** (`YoungDiagramKernel`, `YoungDiagramKernelPincer`):

- `secondMomentKernel_eq_zero_of_le_twenty` — the ℤ-form extended `k ≤ 7` → `k ≤ 20`, matching the
  kernel base `kernelValue_nonpos_of_le_twenty`.
- `tilt_zero` — `tilt 0 f = f²` (no positivity needed; the exponent `0·log f` vanishes even at 0).
- `tiltOmega_zero_eq_secondMomentKernel` — the missing ℝ bridge `W(0) = secondMomentKernel k`, the
  `θ = 0` twin of the existing `tiltOmega_one_eq_kernelValue`.
- `tiltedMean_zero_of_secondMomentKernel_eq_zero` — vanishing numerator ⇒ `E₂[ω₃] = 0` (no
  non-degeneracy of the normalisation needed: `0 / Z = 0`).
- `tiltedMean_zero_of_le_twenty` — **for `3 ≤ k ≤ 20`, `mean_zero` is proved, not assumed.** On this
  range the pincer's premise set reduces to the two genuinely open legs.

**Honest scope.** The general-`k` statement is open *as Lean*, not as mathematics: the
character-orthogonality proof needs the Jucys–Murphy-eigenvalue ⇒ Plancherel-mean bridge (the
identity coefficient of `Σ_i X_i²` is `#{(i,j) : j < i} = C(k,2)`), which is Sₙ representation-theory
infrastructure the corpus does not yet carry (cf. the Sₙ rep-theory infra epic). What lands here is
a certified floor plus the ℝ-side plumbing that will consume the general proof unchanged when it
arrives.

## Finding 2 — step 3 of the (TAIL) first instance: the carrier confinement reaches the sum

Steps 1, 2 (carrier lemma + hook-shape data) and 4, 5 (moment sums + collapse) were already
machine-checked (PRs #4349, #4359, #4607). Step 3 — turning the *per-diagram* carrier statement
into a statement about the Plancherel sum — lands here:

- `hookShapes k` — the explicit `k`-element enumeration of hook shapes, with `hookShape_sum`,
  `hookShape_mem_partsOf` (via `mem_partsFuel`) and `hookShapes_nodup`.
- `eq_hookShape_of_rows_le_one` / `mem_hookShapes_of_rows_le_one` — the **converse** structural
  fact: a sorted positive list whose rows past the first are all `≤ 1` *is* one of the enumerated
  shapes. This makes the `getD`-level hook-shape condition and enumeration membership
  interchangeable, which is what the carrier lemma needs to bite on a sum.
- `sum_partsOf_eq_sum_hookShapes` — a weight vanishing off the hook shapes may be summed over the
  `k`-element family instead of the whole enumerator (`Finset.sum_subset` transported along
  `List.sum_toFinset`; both lists nodup).
- `hookCount_top_eq_zero_of_not_mem` / `hookCount_top_eq_one_mem` — carrier confinement in
  enumeration form.
- **`top_mixedMoment_eq_hookShapes_sum`** — the payoff: the `v = k` numerator of the ν-system is a
  sum over the `k` hook shapes alone.
- `six_mul_omega3_hookShape` — the **bracket-arithmetic hinge**
  `6·ω₃(a=i+1, c=k−1−i) = 2k·(3i² − 3(k−1)i + (k−1)(k−2))`, i.e. exactly the quadratic that
  `BinomialSquareSums.bracket_sum_collapse` consumes. Proved from `contentSq_hookShape` +
  `six_mul_sum_range_sq`; the arm/leg **cubic terms cancel identically**, now verified at the level
  of the diagram data rather than asserted.

## What remains for the fully machine-checked `ν_n ≥ 0`

One bridge: the **RSK normalisation** `Σ_λ (f^λ)² = k!` in the corpus' own `sytDim`/`partsOf`
形 (main carries `sum_numSYT_sq_eq_factorial` for `numSYT`; the corpus already has
`sytDim_eq_numSYTenum`, so this is a plumbing bridge, not new mathematics). With it, the chain

`top_mixedMoment_eq_hookShapes_sum` → `sytDim_hookShape` (`f = C(k−1,i)`) → `six_mul_omega3_hookShape`
→ `bracket_sum_collapse`

closes to `ν_n = n(n−2)(n−3)·C(2n−4, n−2)/(3·n!) ≥ 0`, the first (TAIL) instance in Lean.

## Honest scope (whole tranche)

Everything above is sorry-free and lean-direct verified; no `native_decide`. `mean_zero` is
discharged **only** on `3 ≤ k ≤ 20` (certified floor); (TAIL), FMP, A2, A3 and the kernel
conjecture itself all remain open. Nothing is wired to production; no witness, content block, or
compute changed; L2 unchanged (2/7). Per the [1ppq lever map](../coordination/2026-08-02-1ppq-lever-map-post-q0-gate.md)
this arc is formal-math infrastructure, **not** on the critical path to the `Δ_λ` *magnitude*
lever.
