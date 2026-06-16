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

| Audit | candidates | severity | nature |
|-------|-----------:|----------|--------|
| `validation_as_input` (I11) | 39 | **HIGH** | experimental anchor used as a derivation *input* → hidden calibration (violates three-cal discipline) |
| `float64_leak` (I8) | 16 | MEDIUM | `float()` cast on a derived `mpf` in a substrate-pure script (precision leak); all `fp_candidate=0` |
| `hardcoded_literal` (I9) | 248 | LOW | inline numeric literal matching a registry constant (P31: route through `codata_constants.py`) |

## I11 — validation-as-input (39, HIGH priority)

The I11 antipattern: a script imports a `*_VALIDATION` constant (an
experimental anchor — AME binding, CODATA mass) and uses it as a
**computation input**, not merely for a post-hoc comparison. That is a
*hidden fourth calibration* — exactly what `prop:three-calibration-inputs`
forbids. Flagged scripts include `applied_uniqueness_mass_table.py`,
`binding_K_direct.py`, `binding_canonical.py`,
`borromean_volume_propagation_to_m_p.py`,
`canonical_derivation_pipeline_compliance.py`, `audit_delta_S_chain.py`, …

**Remediation:** per-script review to confirm input-vs-comparison use.
True input uses must be re-derived or demoted to `auditOnly` comparison;
confirmed comparison-only uses get an acknowledgement marker so the audit
stops flagging them. This is the highest-value set — each is a potential
discipline breach, not a style nit.

## I8 — float64-leak (16, MEDIUM)

16 substrate-pure-banner scripts cast `float()` on a derived `mpf` (or
`==`-compare derived mpfs), with the audit's own `fp_candidate = 0` (i.e.
not the benign `mp.mpf(str(x))` re-entry). Examples:
`canonical_tr_m_via_branching.py` (5), `constit_factor_residual_phase5k.py`
(16), `canonical_mass_table_extended.py` (3), `closed_form_tau_M.py` (1).

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

1. **I11 (39)** — highest value: hidden-calibration breaches. Review +
   re-derive/demote, one cluster per PR.
2. **I8 (16)** — bounded precision fixes; aligns with #2355's no-float64
   work.
3. **I9 (248)** — codemod + acknowledge-marker; lowest severity.

Each is its own scoped follow-up; none is attempted in this PR (which
restores the audits' *scope* + regenerates their witnesses so the
violations are visible and trackable in the first place).
