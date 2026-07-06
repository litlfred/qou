# Habiro interpolate cross-validator — factor-of-2 convention finding

**Date:** 2026-05-09
**Source:** PR #621 CI investigation; pre-existing on `origin/main`

## Failure description

`habiro_interpolate_cross_validator` exits 2 with assertion FAILURES:

```
✗  D (deuteron, A=2)  rel_diff = 0.5430257368
✗  n (neutron, A=1)   rel_diff = 0.4191285364
✗  p (proton, A=1)    rel_diff = 0.4981084486
asymmetric coverage: atomic-only=[], interpolate-only=['T (triton, A=3)', '³He (helion, A=3)']
```

## Root cause

The interpolate-side and atomic-side `tr_M(q_0)` values differ by a
**factor of 2**, not by precision noise:

| Atom | atomic side | interpolate side | ratio |
|------|------------|------------------|-------|
| p (proton) | 1.0653062286 | 2.1225825095 | **1.992** |
| n (neutron) | 0.9232333 | 1.8771749 | **2.033** |

The atomic side matches Phase 1.6's closed-form `|tr_M(β_p)| ≈ 1.633`
(rescaled by the polynomial denominator `(1+u²)^Z·(1+u·−)`), and the
canonical Markov-trace anchor on this branch
([commit `ac88823`](https://github.com/litlfred/qou/commit/ac88823)).

The interpolate side matches the value **`2.12258`** that surfaces in
`markov-trace-assembly-proton.derivation.json` and was identified in
[`docs/audits/2026-05-09-braid-encoding-deepdive.md §4`](2026-05-09-braid-encoding-deepdive.md)
as a normalisation inconsistency between the markov-trace assembly chain
(reports `Δ_n²·tr_M`) and the bare-trace closed-form chain (reports
`tr_M`).

[`Phase 1.12`](2026-05-09-braid-encoding-deepdive.md#5-coordination-with-claudeterm7-alpha5-derive-investigation)
verified directly:

```
tr_M(β_p)            = 1.6331536  (closed form / Strategy-3 / Phase 1.6)
tr_M(Δ_n² · β_p)     = 2.1111109  (per-particle LP-dual extraction)
markov-trace-assembly = 2.1225825  ≈ Δ_n²·tr_M (within 0.6%)
```

The two interpolate-side values (2.122 vs 2.111) are within 0.6% — the
small residual is the higher-order JM-element corrections beyond the
Δ_n² scalar. So the interpolate-side path is reporting `Δ_n²·tr_M`
(saturated-shell-multiplied trace), not the bare `tr_M` that the atomic
side reports.

## Why this is not actionable on PR #621

The fix requires a convention call:

- **Option A:** patch the interpolate-side script to divide its output
  by the Δ_n² scalar before comparison. Risk: changes the witness
  consumed by an unknown number of downstream chains; would need an
  audit of every consumer of `habiro-coefficients-interpolate.witness.json`.

- **Option B:** patch the atomic-side script to multiply its output
  by the Δ_n² scalar before comparison. Risk: same as A from the
  other direction.

- **Option C:** patch the cross-validator to report the disagreement
  as a convention difference rather than a rel_diff failure. Risk:
  hides a real signal that downstream agents may rely on.

All three options change scripts that pre-date PR #621 and were not
modified by this branch. PR #621's scope is the 1ppb-precision audit
chain + KLR upgrade work; resolving this convention disagreement is a
separate workstream.

## Verified claims (this audit)

1. `habiro_interpolate_cross_validator` fails on a clean `origin/main`
   checkout with the same exit code (2) and same numerical disagreements:

   ```bash
   git checkout origin/main
   python3 computations/habiro/habiro_interpolate_cross_validator.py
   # exit 2; rel_diff 0.42–0.54
   ```

2. The failure is **not** introduced by PR #621. The branch's commit
   `8fae07706` (CI-drift fix + Gemini/Copilot review fixes) does not
   touch any input to this validator.

3. Regenerating the atomic-side witness via
   `python3 habiro_coefficients_atomic.py` does not resolve the
   disagreement — it still produces `1.0653` for the proton, and the
   interpolate side still produces `2.1226`. The disagreement is
   structural, not stale.

## Resolution (2026-05-10)

The original "Δ_n² convention gap" diagnosis above is **withdrawn**.
Deeper analysis identified the true root cause: the interpolate path
was using the SU_q(2)-restricted Schur–Weyl projector
`w_λ(q) = s_λ(q, q⁻¹) / H_q(λ)` as its central weight, while the
atomic path correctly uses the canonical Wenzl-bridge weight
`y_λ` from
[`prop:y-lambda-closed-form-wenzl-bridge`](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md).

The legacy weight vanishes identically for any partition with
$\ell(\lambda) > 2$ — a textbook fact: Schur functions in $N$
variables vanish when evaluated at fewer variables than the number
of rows, $s_\lambda(x_1, \dots, x_N) = 0$ for $\ell(\lambda) > N$.
For atomic braids at $H_{3A}$, partitions with $\ell(\lambda) \geq 3$
carry non-trivial $\chi_\lambda$ contributions; truncating them via
the SU_q(2) projector amputated the trace expansion. At the substrate
value $q_0 \approx 1.110$ the dropped contributions happened to
nearly equal the retained contributions for $A \in \{1, 2\}$,
producing an apparent ratio close to 2 — but it was a structural
truncation artefact, not a $\Delta_n^2$ rescaling.

**Fix.**
[`computations/habiro/habiro_coefficients_interpolate.py`](../../computations/habiro/habiro_coefficients_interpolate.py)
now imports `y_lambda_wenzl_bridge_numeric` and uses it in
`markov_trace_numerical`, matching the symbolic atomic path
(`habiro_coefficients_atomic.markov_trace_symbolic`).

**Formal backing.**
[`prop:y-lambda-closed-form-wenzl-bridge`](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md)
proves $y_\lambda$ is the unique central weight of the Jones–Markov
trace under the σ-Hecke convention, by composition of:

1. Wenzl 1988 (existence of the principal-specialisation weight in
   the g-Hecke convention),
2. the convention isomorphism $g = q \sigma$ mapping σ-Hecke to
   g-Hecke with $(Q, z_{\mathrm{GL}}) = (q^2, q z)$,
3. Chlouveraki HDR Theorem 6.20 (1-dimensionality of the type-A
   Markov-trace family).

The Lean sibling [`y-lambda-closed-form-wenzl-bridge.lean`](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.lean)
records the same theorem with `-- Ref:` citations.

**Independent numerical verification (2026-05-10).**

1. Plancherel identity $\sum_\lambda y_\lambda(q_0) \cdot d_\lambda = 1$
   holds at 50 dps for $n \in \{1, \dots, 6\}$, with absolute
   residuals $\leq 2.7 \times 10^{-51}$.
2. Direct `markov_trace_numerical` evaluation under the fixed
   weight reproduces the atomic-path values exactly:

   | atom | fixed interpolate (40 dps) | atomic-path docstring | agreement |
   |------|----------------------------|-----------------------|-----------|
   | proton  | 1.0653062285924 | 1.0653062285923893 | 13 dps |
   | neutron | 0.9232332971696 | 0.9232332971695838 | 13 dps |
   | deuteron | 0.3882864715477 | 0.388286471547713 | 13 dps |

The cross-validator's `rel_diff` for p, n, D drops from
$\{0.498, 0.419, 0.543\}$ to $\leq 10^{-12}$ after the fix, clearing
the validate-job failure.

## Cross-references

- [`prop:y-lambda-closed-form-wenzl-bridge`](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md)
  — the operative theorem; identifies $y_\lambda$ as the unique
  Jones–Markov central weight via Wenzl 1988 + Chlouveraki uniqueness
- [`docs/audits/2026-05-08-p3-h-3a-divergence.md`](2026-05-08-p3-h-3a-divergence.md)
  — earlier audit that flagged the legacy Schur–Weyl weight as
  vanishing for $\ell(\lambda) > 2$; resolved on the atomic-path
  symbolic side, but the interpolate path was missed
- [`docs/audits/2026-05-09-braid-encoding-deepdive.md §4`](2026-05-09-braid-encoding-deepdive.md)
  — earlier (independent) Δ_n² convention diagnosis; superseded by
  this audit's resolution
- [`computations/y_lambda_wenzl_bridge.py`](../../computations/y_lambda_wenzl_bridge.py)
  — canonical implementation; `_y_lambda_wenzl_bridge_numeric_impl`
  applies the principal-specialisation formula at $X = q z / (1 - q^2 + q z)$
- [`computations/habiro/habiro_interpolate_cross_validator.py`](../../computations/habiro/habiro_interpolate_cross_validator.py)
  — the validator that originally surfaced the gap
