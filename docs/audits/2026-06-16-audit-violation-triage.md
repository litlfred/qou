# Audit-violation triage — post-scan-root-restoration

**Date:** 2026-06-16
**Branch:** `claude/audit-scanroot-followup-2026-06-16` (PR #2374)
**Context:** #2355 restored the scan roots of the `computations/audits/`
discipline audits (they were vacuously scanning only `audits/` after the
reorg). With full tree scope back, they now surface the violations that
were hidden. This doc triages those violations — they are **largely real
candidates, not noise** — and recommends a remediation order. It does NOT
attempt mass-remediation (300+ candidates across 3 audits is a multi-PR
program, not one fix).

## Summary

| Audit | flagged | severity | nature |
|-------|--------:|----------|--------|
| `validation_as_input` (I11) | 39 | **audit over-flags** | ≥13 pure FP (witness recordings / comparisons); most rest are two-step comparisons. Refine the heuristic first; true hidden-cal subset is small. |
| `float64_leak` (I8) | 16 | MEDIUM | `float()` cast on a derived `mpf` in a substrate-pure script (precision leak); all `fp_candidate=0` |
| `hardcoded_literal` (I9) | 248 | LOW | inline numeric literal matching a registry constant (P31: route through `codata_constants.py`) |

## I11 — validation-as-input (39 flagged; audit OVER-FLAGS — see review below)

The I11 antipattern: a script imports a `*_VALIDATION` constant (an
experimental anchor — AME binding, CODATA mass) and uses it as a
**computation input**, not merely for a post-hoc comparison. A true such
use is a *hidden fourth calibration* — what `prop:three-calibration-inputs`
forbids.

**Review finding (2026-06-16) — the audit's flat count of 39 substantially
over-flags.** Reading the flagged lines:

- **≥ 13 / 39 are pure false-positives** — every flagged line is either an
  `add_parameter("m_p_MeV", str(M_P_MEV_VALIDATION))` **witness-provenance
  recording** (e.g. `binding_K_direct.py:209-210`) or an `err = pred −
  M_X_VALIDATION` **comparison** the heuristic's "final-line" check missed.
- **Most of the remaining 26 are two-step comparisons** — `m_p =
  mp.mpf(str(M_P_MEV_VALIDATION))` assigns the anchor to a local, which is
  then used in `err = pred − m_p` (e.g. `audit_delta_S_chain.py`,
  `m_p_borromean_verification_50dps.py`). That is comparison-reference, not
  a derivation input.
- The **genuine hidden-calibration subset** (anchor actually feeding a
  predicted quantity) is plausibly small and needs per-line confirmation.

**Recommendation (corrects the earlier "HIGH, 39 breaches" framing):** the
highest-value action is to **refine the I11 audit heuristic first** so it
stops counting (a) `add_parameter` / witness-recording uses and (b)
two-step `local = anchor; … pred − local` comparisons. That collapses 39
to the true-candidate subset; only then review that (much smaller) set for
real hidden calibration. Do **not** mass-edit 39 scripts — most are not
violations.

## I8 — float64-leak (16, MEDIUM)

16 substrate-pure-banner scripts cast `float()` on a derived `mpf` (or
`==`-compare derived mpfs), with the audit's own `fp_candidate = 0` (i.e.
not the benign `mp.mpf(str(x))` re-entry). Examples:
`canonical_tr_m_via_branching.py` (5), `constit_factor_residual_phase5k.py`
(16), `canonical_mass_table_extended.py` (3), `closed_form_tau_M.py` (1).

**Update (audit refined, PR #i8-float64-leak-fixes):** like I11, the I8 audit over-flagged. Two safe exclusions added — `float(` inside triple-quoted docstrings, and dict-value serialization `"key": float(x)` (witness/JSON output, not a compute input). Result: **i8_violation 16 → 11**. The remaining 11 are a mix of by-design f64-mode paths (`knot_volumes._F64` constants, `markov_trace` f64 mode) and ~2 genuine candidates (`h_val = float(Q0-1/Q0)` feeding `marshal_to_chi_lambda_braid` in `closed_form_tau_M` / `rho_constit`). The genuine ones are RISKY to auto-fix — the marshaller is typed `h_val: float` and changing to mpf would shift validated trace results — so they need careful per-script review + regeneration, not a blind edit.

**Remediation:** per-script — replace the f64 cast with a 50-dps path
(`mpmath` throughout, decimal-string round-trips), or, if the value is
display-only, move the cast to the print/serialise boundary. Concrete and
bounded (16 scripts); aligns with the no-float64 theme of #2355.

## I9 — hardcoded-literal (248, LOW but widespread)

248/263 scanned scripts inline a numeric literal that exactly matches a
registry constant (e.g. `2.22456612` = `AME_B_DEUTERON_MEV_VALIDATION`,
`938.27208816` = `M_P_MEV_VALIDATION`, `0.51099895069` = `M_E_MEV`). These
are **real** P31 discipline gaps (route experimental/CODATA values through
`codata_constants.py`), not false positives — but mostly low-severity
(many in display/comparison/docstring contexts).

**Remediation:** a **bulk codemod** is the right tool — replace exact
registry-value literals with the named import where the literal is used in
a computation; leave display/docstring literals (or acknowledge them).
Manual per-script fixing of 248 is not warranted; a codemod + an
acknowledge-marker convention is.

## Recommended order

1. **I11 — refine the audit first** (not mass-edit). Exclude `add_parameter`
   recordings + two-step `local = anchor; pred − local` comparisons; the 39
   collapses to the true hidden-cal subset, then review that.
2. **I8 (16)** — bounded precision fixes; aligns with #2355's no-float64
   work; the concrete, real set.
3. **I9 (248)** — codemod + acknowledge-marker; lowest severity.

The I11 over-flagging is itself the main review finding: a flat violation
count is misleading until the heuristic excludes provenance recordings and
two-step comparisons.

Each is its own scoped follow-up; none is attempted in this PR (which
restores the audits' *scope* + regenerates their witnesses so the
violations are visible and trackable in the first place).
