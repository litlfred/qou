# Covariance-kernel epic (`qou-x631`) — M₁>0 sign attempt: honest wall

**Date:** 2026-08-22 · **Branch:** `claude/m1-deficit-rate-mechanism-2026-08-22` · **Tier:** honest
negative (records where the one-sided sign proof stalls) · **Discipline:** scope-(a); no fit; nothing
wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## Target

Close `M₁>0` all-n via the one-sided reduction: `M₁>0` ⟸ exact `M₁>0` (n≤12) ∧ `κ_n ≥ κ` for n≥13,
`κ = 128/(225π²)`. The remaining piece is the **sign of the correction** `κ_n − κ ≥ 0` (i.e.
`κ_n → κ` from above).

## Three diagnostics, one conclusion: the numerics cannot settle the sign, and it is not clean-bulk

1. **Deficit mechanism (`N` lags `P`).** `κ_n − κ = dN − dP` with `dP = P_lead − P_n/n^{5/2} ≥ 0`,
   `dN = N_lead − N_n/n^{5/2} ≥ 0`; `dN > dP` for all 13≤n≤42, `dN/dP` rising through 1 at n=13. But
   `dN − dP = κ_n − κ` **identically** — a re-description, not new logical content.
2. **Half-integer-power fit unstable.** Fitting `κ_n − κ = Σ_j a_j n^{-j/2}` on high-n windows gives
   `a₁` swinging wildly with the number of terms (`0.010 → 0.65 → −3.6`) and **mixed signs** across
   sliding windows. The correction is **not** a clean bulk `n^{-1/2}` series.
3. **Effective exponent not settled.** `κ_n − κ` **rises to a peak at n≈32** and only then declines
   slowly; the local exponent `β` of the decay is still unstable at n≤60 (`−1.18, −0.34, 0.04, 0.26`)
   — we are barely past the peak, **not** in the asymptotic regime. Combined with (2), the correction
   is plausibly **edge-sensitive** (Tracy–Widom, `~n^{-1/6..-1/3}` relative), not bulk `n^{-1/2}`.

## Honest conclusion

- **Empirically the sign holds:** `κ_n > κ` for every `13 ≤ n ≤ 60` (exact), so `M₁>0` is not in doubt.
- **The sign PROOF is out of numerical reach and is not a bulk second-order-CLT statement.** The
  asymptotic regime for `κ_n − κ` is not reached by n≤60, and the correction does not admit a clean
  `n^{-1/2}` expansion — it is likely governed by **edge (Tracy–Widom) asymptotics** of the
  Plancherel-random diagram, not just the bulk Kerov CLT. A rigorous `κ_n ≥ κ` (n≥13) therefore needs
  edge-sensitive second-order analysis (Tracy–Widom corrections to `Cov(Σh, ω₃)`), which is a
  substantially harder and separate research undertaking.
- **This is a genuine wall for the current toolkit**, recorded as an honest negative. It does NOT
  weaken the established results: `κ = 128/(225π²) > 0` (derived), `M₁ = Cov(Σh, ω₃)` with the `Λ*`
  route shown vacuous, and `M₁>0` exact to n≤60.

## State of `qou-k5r5` (for handoff)

- **Done:** `κ>0` derived; even moments proved positive (earlier); `M₁>0` exact n≤60; reduced to
  one-sided `κ_n≥κ` (crossing n₀=13); mechanism = "N lags P".
- **Open (the nub):** prove `κ_n ≥ κ` for n≥13. Now known to require **edge-sensitive** second-order
  asymptotics (not bulk `n^{-1/2}`), because the correction peaks at n≈32 and its decay is
  edge-flavoured. This is the precise, honest frontier.

## Compute

- Deficit mechanism: [`wlambda_covariance_epic_M1_deficit_rates.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_deficit_rates.py)
- Second-order fit (unstable → the finding): [`wlambda_covariance_epic_M1_secondorder_fit.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_secondorder_fit.py)

## Cross-references

- One-sided reframing: [`2026-08-22-covariance-kernel-M1-onesided-reframing.md`](2026-08-22-covariance-kernel-M1-onesided-reframing.md)
- κ derivation: [`2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md`](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)
- Sub-result (1) retraction: [`2026-08-22-covariance-kernel-M1-lambda-star-orthogonality.md`](2026-08-22-covariance-kernel-M1-lambda-star-orthogonality.md)
- Gap bean `qou-k5r5`.
