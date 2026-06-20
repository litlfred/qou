# Bar-symmetric discipline tests — Option-E v9 + ⁴He ρ_F (2026-06-01)

**Date:** 2026-06-01
**PR:** TBD (claude/bar-symmetric-v9-and-he4-probes-2026-06-01)
**Status:** Two diagnostic probes, both with clean verdicts.
**Triggered by:** user 2026-06-01 "1 2" + "don't assume other agents
100% correct".

## TL;DR

Two probes applying PR #1643's bar-symmetrization discipline
(`prop:li2q-phiq-bar-symmetrization`: binding-context formulas must be
bar-symmetric under `q ↔ q⁻¹`):

**Probe 1 — Option-E v9 `(1+q)/2`:** FAILS bar-symmetrization. The v9
form is INHERENTLY bar-asymmetric. No bar-symmetric replacement comes
within 5% of the 0.11% empirical closure. **Confirms v9 was a
discipline-violating near-match, not a structural derivation.**

**Probe 2 — ⁴He ρ_F:** ALL truly bar-symmetric substrate candidates
miss ⁴He by `|err| ≥ 5.87%` (signed errors span −25.04% to +6.44%
across C1–C6, C8 — see Probe 2 table). Best near-match (C7:
2·cos(h/2)/q^(1/4)) at +2.58% is NOT bar-symmetric (q^(1/4) asymmetry).
**Confirms PR #1621's research direction: the +5.87% gap needs the
categorical multi-nucleon interface operator, NOT a substrate constant.**

## Probe 1 — Option-E v9 (1+q)/2 bar-symmetric test

| Candidate | Value at q_proton | err vs target |
|---|---|---|
| **C1: (1+q)/2 [bar-ASYMMETRIC, v9 original]** | 1.0550 | **-0.0958%** (v9 closure) |
| C2: (2 + [2]_q)/4 [bar-symmetric avg] | 1.0027 | -5.05% |
| C3: √((2+[2]_q)/4) [bar-modulus] | 1.0014 | -5.17% |
| C4: [2]_{q^(1/2)}/2 [bar-symmetric, half-q] | 1.0014 | -5.17% |
| C5: (2 + [2]_q)/2 | 2.0054 | +89.9% |
| C6: [2]_{q^(1/2)} | 2.0027 | +89.7% |

**Bar-symmetry verification:** (1+q)/2 at q_proton = 1.0550;
bar((1+q)/2) = (1+q⁻¹)/2 = 0.9505; **difference 0.1045 ≠ 0** ⟹
NOT bar-symmetric. Verified at 50 dps.

**Verdict:** the v9 (1+q)/2 form is inherently bar-asymmetric and
violates the framework's bar-symmetrization discipline
(`prop:li2q-phiq-bar-symmetrization`). No bar-symmetric replacement
preserves the 0.11% closure. The closure was an anchor-coincidence
of a discipline-violating form, NOT a categorical derivation.

This refutes the v9 closure as the path to Δ_λ for the A=3 mirror
pair. The `research-one-plus-q-over-two-derivation` queue item
should be closed as **REFUTED via bar-symmetry**.

## Probe 2 — ⁴He ρ_F bar-symmetric audit

Required ρ_F (from B_AME = 28.296 MeV): `B_AME / (m_e · A · 8G) = 1.8892`.
Production ρ_F = 2 gives B(⁴He) = 29.956 MeV (+5.87% off).

| Candidate | Value | B_pred MeV | err % |
|---|---|---|---|
| C1: 2 [production] | 2.0000 | 29.956 | +5.87% |
| C2: [2]_q | 2.0109 | 30.119 | +6.44% |
| C3: [2]_{q^(1/2)} (PR #1621) | 2.0027 | 29.996 | +6.01% |
| C4: [2]_q/2 + 1 | 2.0054 | 30.037 | +6.16% |
| C5: √(([2]_q+2)/2) [bar-modulus] | 1.4161 | 21.211 | -25.04% |
| C6: 1 + b² (Hoefsmit) | 1.7527 | 26.252 | -7.22% |
| **C7: 2·cos(h/2)/q^(1/4)** | 1.9379 | 29.025 | **+2.58%** |
| C8: ([2]_q)²/(2·[2]_q−2) | 2.0001 | 29.957 | +5.87% |

**Best candidate C7 is NOT bar-symmetric.** Under q ↔ q⁻¹:
2·cos(h/2)/q^(1/4) → 2·cos(h/2)·q^(1/4) ≠ self. So C7's +2.58% match
is a discipline violation — anchor coincidence at q_proton.

**Strictly bar-symmetric candidates (C1–C6, C8) all miss by ≥ 5.87%.**

**Verdict:** ⁴He's +5.87% gap cannot be closed by a bar-symmetric
substrate constant. Confirms PR #1621's recommendation: the gap
needs the **categorical interface operator** H_3⊗H_3⊗H_3⊗H_3 → H_12
respecting (4,4,4) Wedderburn PSD dominance (per PR #1289).

## Skeptical note on prior findings (per user 2026-06-01)

Per user "don't assume other agents 100% correct", flagging prior
audits / conclusions that warrant re-examination:

| Prior finding | Status | Re-examination warranted? |
|---|---|---|
| PR #1642 — "Wenzl → Q_β NEGATIVE" | merged | **Partial.** The NEGATIVE conclusion is about ONE specific mapping (ζ_8 Wenzl truncation → Q_β Habiro coefficients). It does NOT refute the broader Wenzl-positivity-implies-substrate-positivity framework. The bar-involution discipline (PR #1643 / this PR) still uses Wenzl as the positivity engine. |
| PR #1621 — ⁴He +5.87% miss; ρ_F=2 postulated; interface operator open | merged | **Confirmed by Probe 2 here.** Bar-symmetric ρ_F candidates all fail; structural-operator direction stands. |
| 2026-05-30 KLR dialog assessment "0/6 candidate proofs shorten with KLR" | citation in AGENTS.md §7b | **Stands.** This is authoring guidance, not a positivity claim. PR #1643's KLR/Wenzl audit clarifies the distinction. |
| Option-E v9 "0.11% closure" empirical near-match | various probes | **Refuted by Probe 1 here** as discipline-violating bar-asymmetric near-match. Was already known as "selected from substrate candidates, not derived" per PR #1594 master ledger; this probe shows WHY it can't be derived. |
| 6 ruled-out mechanisms per `b502b9b83` for Q_β c_3 | audit | **Stands.** Independent of bar-discipline. |

## Implications

1. **Option-E v9 thread**: close `research-one-plus-q-over-two-derivation`
   as REFUTED-by-bar-symmetry. The +0.11% closure was anchor-coincidental.
   Don't search for a derivation of (1+q)/2 — there isn't one.

2. **⁴He multi-nucleon interface**: confirm Probe 2 finding ratifies
   PR #1621. Bar-symmetric substrate constants are exhausted; the
   categorical interface operator approach is the only remaining
   structural path.

3. **Bar-discipline as falsification tool**: this session demonstrates
   that PR #1643's bar-symmetrization can FALSIFY near-match candidates
   that violated the discipline. Use it routinely as a first-pass
   filter on new c_k or Δ_λ candidates.

## Anti-pattern guards

- ❌ Do NOT propose a NEW substrate constant (bar-symmetric or not)
  to close ⁴He without categorical justification — 8th-ansatz trap
- ❌ Do NOT try to "fix" the v9 (1+q)/2 by adding a small bar-symmetric
  correction term — that's the 7th-ansatz trap
- ❌ Do NOT cite PR #1642's NEGATIVE finding as refuting all Wenzl
  approaches; the NEGATIVE was on ONE specific ζ_8 Habiro mapping
- ✓ DO use bar-symmetry as a first-pass falsification filter on new
  c_k / Δ_λ candidates

## Files

- `computations/probes/option_e_v9_bar_symmetric_test_probe.py`
- `computations/probes/option-e-v9-bar-symmetric-test-probe.witness.json`
- `computations/probes/he4_rho_f_bar_symmetric_audit_probe.py`
- `computations/probes/he4-rho-f-bar-symmetric-audit-probe.witness.json`
- `docs/audits/2026-06-01-bar-symmetric-discipline-tests.md` (this file)

## Cross-refs

- PR #1643 — paper |...| audit + refactor + KLR/Wenzl positivity (the
  bar-symmetrization discipline is from this PR)
- PR #1641 — Φ_q signed-vs-|...| 92% sensitivity
- PR #1621 — ⁴He +5.87% miss; ρ_F=2 postulated; multi-nucleon interface
- PR #1594 — Option-E master ledger (v9 (1+q)/2 "anchor-selected")
- PR #1642 — Wenzl → Q_β NEGATIVE (skeptically referenced above)
- `prop:li2q-phiq-bar-symmetrization`
- `prop:magic-A-binding-formula` (⁴He formula)
- `prop:operator-selection-lp` (SDP T_w selection)
- `conj:wenzl-positivity-implies-substrate-positivity`
