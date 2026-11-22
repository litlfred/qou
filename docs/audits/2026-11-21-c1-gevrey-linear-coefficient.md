# The C1 q-Gevrey linear coefficient is `B = (1 − log_q(q − q⁻¹))/2`, not `8`

Bean `qou-z8me` (epic `qou-frzo`). Date 2026-11-21.

## 1. Pre-registration (written before the probe was run)

**Question.** For the C1 recurrence `[m+2]_q b_{m+2} = b_{m+1} + b_m` with the
symmetric q-integer `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`, a three-point fit at
`m ∈ {600,700,800}` gave `−log_q|b_m| ≈ m²/4 + B m + C` with `B = 8.00010424`
(`computations/qbeta/c3_w2_c1_qborel_singularity.py`). Is `B` exactly `8`?

**Hypothesis (from the Lean derivation, §2).** `B = (1 − log_q(q − q⁻¹))/2` for every
`q > 1` and every positive solution. It is a function of `q`; it is `8` only where
`log_q(q − q⁻¹) = −15`.

**Probe design.** `computations/probes/c1_gevrey_linear_coeff_probe.py`, mpmath at
300 dps, no float. For `q ∈ {6/5, 1.1099785827513808075916690956 (the probe's q), 3/2, 2}`
and initial data `(1,0)`, `(0,1)`, `(1,1)`:

1. **Window test** (the bean's task 2): the three-point quadratic fit on the disjoint
   windows `{200,300,400}` and `{600,700,800}`.
2. **Log-term test** (task 1): fit `A m² + B m + D·log m + C` on four points and
   report `D`.
3. **Prediction test** (task 3): compare against `B_pred = (1 − log_q(q − q⁻¹))/2`
   and the parity-free radius `log_q ξ_s = B_pred + 1/4`.

**Pass criteria, fixed now.**
- P1: for every `q` and every branch, the late-window fitted `B` agrees with
  `B_pred` to better than `1e-15` (the corrections are `O(q^{-m/2})`, about `1e-24` at `q = 6/5`, `m = 600`; the corrections are exponentially small in `m`, so
  a polynomial fit should be essentially exact once `m` is large).
- P2: the fitted `D` (coefficient of `log m`) is below `1e-15` in absolute value (four even points `{600,700,800,900}`).
- P3: at `q = 2`, `B_pred ≈ 0.2075` and the fit reproduces it, so `B` is not `8` (or
  any fixed integer) as a function of `q`.

**Fail criterion.** Any branch or `q` where the late-window `B` differs from `B_pred`
by more than `1e-10` refutes the derivation as stated.

## 2. Derivation (Lean, sorry-free)

`folio/quantum-observable-universe/lean/QOU/Mathlib/C1GevreyLinearCoeff.lean`,
namespace `QOU.Mathlib.C1GevreyLinearCoeff`.

- `ratio_two_step_le`: `r_{m+2} ≤ 1/[m+k+1]_q + q⁻¹ r_m`, `r_m = b_{m+1}/b_m`,
  because `[n]_q·q ≤ [n+1]_q` (`qInt_mul_le_succ`).
- `tendsto_ratio_zero`: `r_m → 0` (two-step contraction, `tendsto_zero_of_two_step_contraction`).
- `two_step_increment_tendsto`: `log_q b_m − log_q b_{m+2} − (m+k) → −log_q(q − q⁻¹)`.
- `linear_coeff_tendsto`: `(−log_q b_m − m²/4)/m → (k − 1 − log_q(q − q⁻¹))/2`.
- `c1_linear_coeff`, `c1_linear_coeff_of_nonneg_init`: the C1 case `k = 2`, including
  the three corpus branches.
- `quad_coeff_tendsto`: `−log_q b_m / m² → 1/4`.

Why the bean's "crude asymptotic gives 7.5" was wrong: the two-step increment is
`m + 2 + λ` with `λ = −log_q(q − q⁻¹)`; a profile `m²/4 + βm` has increment
`m + 1 + 2β`, so `β = (1 + λ)/2`. The 7.5 came from `β = λ/2`.

## 3. What it settles, and what it does not

- **Settled:** `B` is not an integer. The `8` is the value of a `q`-dependent closed
  form at one `q`, and the near-integer comes from `log_q(q − q⁻¹) ≈ −15.0002` at
  that `q`. The bean's numerology trap (the self-linking `8` of `T(2,9)`, `T(3,5)`)
  is therefore closed as a coincidence of evaluation, not a structural match.
- **Settled:** the parity-free q-Borel radius is `ξ_s = q^{B + 1/4} = q^{3/4}/√(q − q⁻¹)`,
  which is the `8.250104239…` that `c3_w2_c1_parity_artifact.py` measured.
- **Not settled:** sign-changing or complex initial data (not covered by the Lean);
  anything about Stokes data. `B` sets the radius, not the singularity structure.

Superseded-premise check (owner instruction 2026-11-21): the bean rests on none of
the superseded items (photon form, virtual photons, convention C, trace choice,
electron word, `c₂`, `χ₍₂,₁₎`, fitted constants). The C1 recurrence is a pure
q-difference object with `q` free.

## 4. Probe result (run after §1 was written; thresholds not changed)

`python3 -u computations/probes/c1_gevrey_linear_coeff_probe.py`, 300 dps, `N = 1000`,
witness `computations/probes/c1-gevrey-linear-coeff.witness.json`.

| q | B_pred | late fit − B_pred (m = 600..800) | early fit − B_pred (m = 200..400) | log-term D |
|---|---|---|---|---|
| 6/5 | 3.251463201901126 | −2.3e-24 | −7.3e-9 | −6.3e-21 |
| 1.10997858… (probe q) | 8.000104239513764 | −7.7e-14 | −4.2e-5 | −2.1e-10 |
| 3/2 | 0.724830143393396 | −5.5e-54 | −4.3e-19 | −1.5e-50 |
| 2 | 0.207518749639422 | −7.6e-92 | −5.7e-32 | −2.1e-88 |

(branch `(1,0)` shown for the early column; all three branches agree to the digits shown.)

**Verdicts against the pre-registered criteria.**

- **P3 passes.** At `q = 2`, `B = 0.20751874963942…`. `B` is not `8`, and not any fixed
  integer: it is the `q`-dependent closed form.
- **P1 and P2 FAIL at one `q`, the probe's own `q ≈ 1.11`** (late deviation `7.7e-14`
  against a `1e-15` threshold; log coefficient `2.1e-10` against `1e-15`). They pass at
  the other three `q`. The cause is my pre-registration, not the derivation: the
  threshold was sized from the correction `q^{−m/2}` at `q = 6/5` only, and at
  `q ≈ 1.11` that correction is `q^{−300} ≈ 2.5e-14` at `m = 600`, above the threshold.
  I have not moved the threshold after the fact; the failure stands as recorded.
- **The fail criterion is not met.** No deviation exceeds `1e-10`, so the derivation
  is not refuted.

**Diagnostic, added after the run and labelled as such.** The late deviation tracks
`q^{−300}` at every `q` (`1.8e-24`, `2.5e-14`, `1.5e-53`, `4.9e-91` against the measured
`2.3e-24`, `7.7e-14`, `5.5e-54`, `7.6e-92`), and the early/late ratio tracks `q^{200}`
(`6.9e15` vs `3.2e15` at `6/5`; `1.2e9` vs `5.4e8` at `1.11`). That is the
`O(q^{−m/2})` correction the Lean proof predicts (`r_m → 0` geometrically), and no
residual `log m` or constant offset in `B`.

The parity-free radius `log_q ξ_s = B + 1/4` is recorded per case in the witness.
