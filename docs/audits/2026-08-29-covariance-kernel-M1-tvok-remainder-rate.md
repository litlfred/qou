# Covariance-kernel epic (`qou-x631`) — M₁>0 machinery `qou-tvok` step 2: the remainder rate is θ⁻¹ (resolved), coefficient measured

**Date:** 2026-08-29 · **Branch:** `claude/m1-tvok-vA-leading-constant-2026-08-29` · **Tier:**
asymptotic measurement enabled by the exact leading constant · **Discipline:** no fit (exact `v_A`
subtracted; exponent/coefficient measured, closed-form candidate tested and *rejected*); nothing
wired; no `c_k`; L2 unchanged. **Epic:** `qou-h315`; gap `qou-k5r5`.

## Result

With the leading constant pinned exactly (`v_A = 8/π²`, step 1 / PR #5959), the remainder
`d(θ) := V_A(θ)/θ² − 8/π²` is now cleanly characterised:

- **Rate `θ^{−1}`.** Over 5 doublings `θ = 1000…32000`, the log-log slope of `|d|` is
  `p ∈ [0.95, 1.02]` — unambiguously `−1`.
- **Sign: `d(θ) < 0`** throughout — `V_A/θ²` approaches `8/π²` **from below**.
- **Coefficient `c_1 := lim θ·d(θ) ≈ −0.0678`** (Richardson over `θ` to 48000; a small residual
  oscillation is the Airy-edge signature). The clean-looking candidate `−2/(3π²) = −0.06755` is a
  **near-miss (off 2.2e-4) and is rejected** — no closed form for `c_1` identified.

So `V_A(θ)/θ² = 8/π² − c_1'/θ + (small oscillatory edge)`, `c_1' ≈ 0.0678`.

## Why this resolves what the #5939 retraction left open

PR #5939 retracted "rate `θ^{−1}`" because, at 6 points **with `v_A` unknown**, the exponent was
indeterminate (`θ^{−1/2}`/`θ^{−5/6}`/`θ^{−1}` all fit). That retraction was correct *given the
confound*: fitting `v_A` and the exponent simultaneously is ill-conditioned. **Step 1 removed the
confound** — `v_A = 8/π²` is now proved exactly — so subtracting it exposes the exponent directly, and
it is `θ^{−1}` across 5 clean doublings. This is the disciplined progression (pin the leading term,
then the remainder), not a flip-flop: the earlier claim was unfounded on the evidence then available;
this one rests on the exact `v_A` plus a five-doubling measurement.

## What this is / is not

- **Is:** the remainder rate (`θ^{−1}`, resolved), the sign (from below), the coefficient magnitude
  (`c_1 ≈ 0.0678`, measured, no clean form), and hence the **target** for the rigorous bound:
  `|V_A(θ)/θ² − 8/π²| ≤ C_A/θ` with `C_A ≈ 0.07–0.1` (bounds `|θ·d|` over the range incl. the edge
  oscillation).
- **Is not:** the rigorous bound itself. Proving `|d(θ)| ≤ C_A/θ` for all `θ ≥ θ₀` with an explicit
  `C_A` needs the actual analytic derivation — bulk Euler–Maclaurin (via `CompositeEulerMaclaurin`)
  plus the Airy-edge term (via the Gaussian bounds). **Not done here, not faked.** A *measured* `c_1`
  is not a *proved* `C_A`.

## Consequence for the closure

`v_A = 8/π²` (proved) + rate `θ^{−1}` (resolved) means the `V_A` ingredient of the (CS) margin
converges to its limit at `θ^{−1}` with a small constant — comfortably inside the `≥ θ^{−1/2}`,
30–300× headroom the closure needs. The remaining rigorous work is the explicit `C_A` bound (this
task's tail) and the analogous `V_W, P, V_D` (`qou-po72`), then ratio propagation (`qou-jh3m`).

## Compute

- [`wlambda_covariance_epic_M1_tvok_remainder_rate.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_tvok_remainder_rate.py)
  (exit 0; dps 50; exact Bessel sums; NO float64).

## Cross-references

- Leading constant `v_A = 8/π²`: [`2026-08-29-covariance-kernel-M1-tvok-leading-constant-vA.md`](2026-08-29-covariance-kernel-M1-tvok-leading-constant-vA.md)
- Exponent-indeterminacy retraction (now resolved): [`2026-08-29-covariance-kernel-M1-debye-kink-cancellation.md`](2026-08-29-covariance-kernel-M1-debye-kink-cancellation.md)
- Epic `qou-h315`; task `qou-tvok`; gap `qou-k5r5`.
