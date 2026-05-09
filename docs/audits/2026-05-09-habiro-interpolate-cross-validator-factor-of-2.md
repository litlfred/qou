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
   python3 folio-assistant/computations/habiro_interpolate_cross_validator.py
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

## Recommended next step

Open a separate issue (or audit doc) on `claude/term7-alpha5-derive-investigation`
or whichever branch owns the markov-trace-assembly conventions, to
align the two sides on a single trace normalisation
(`tr_M` vs `Δ_n²·tr_M`).

For PR #621: accept the validate-job failure as a pre-existing main
condition. The substantive content of PR #621 (Lean T1 closure +
audit chain + Gemini/Copilot review fixes) is independent of this
convention disagreement.

## Cross-references

- [`docs/audits/2026-05-09-braid-encoding-deepdive.md §4`](2026-05-09-braid-encoding-deepdive.md)
  — independent identification of the factor-of-2 normalisation gap
- [`folio-assistant/computations/delta-n2-lp-dual-extraction.witness.json`](../../folio-assistant/computations/delta-n2-lp-dual-extraction.witness.json)
  — Phase 1.12 per-particle LP-dual extraction giving
  `tr_M(Δ_n²·β_p) = 2.1111`
- [`folio-assistant/computations/habiro_interpolate_cross_validator.py`](../../folio-assistant/computations/habiro_interpolate_cross_validator.py)
  — the failing validator
