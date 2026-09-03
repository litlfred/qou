---
# qou-4bq3
title: 'GAP: convention-c-triage DELIBERATE regex over-blocks 8 of 24 B3 verdicts'
status: todo
type: task
created_at: 2026-08-25T01:09:17Z
updated_at: 2026-08-25T01:09:17Z
---


## Defect

`scripts/convention-c-producer-migrate.py:58`

    DELIBERATE = re.compile(r"(_c\b|_C\b|C_|_c_|zc$|z_c)", re.I)

The `C_` alternative is compiled with `re.I`, so it matches the substring
`c_` inside ordinary identifiers. `scripts/convention-c-triage.py` uses it
(via `_file_has_c_reference`) to class a site B3 "deliberate comparison —
leave it; it measures the excision", so a false positive tells an agent to
skip a real defect.

## SCOPE: this does NOT affect the audit's actionable count

Recorded first because it is the easy thing to get wrong. The regex lives in
`convention-c-producer-migrate.py` and is consumed by
`convention-c-triage.py`. It is **not** what produces the `deliberate` flag in
`convention-c-producer-audit.py`: that audit's `scan()` filters candidate
targets on `"z" in nm.lower()` (line 730), so a `c_`-style collision inside an
ordinary identifier can never reach it. Verified by reading the filter, not
inferred. All 15 of the audit's `deliberate` verdicts are genuine
`z_C`-family names.

So a before/after measured with `convention-c-producer-audit.py` is unaffected
by this bug. What moves is the **triage's B3 verdicts**, i.e. the advice an
agent is given about which sites to skip.

## Measured, 2026-08-25 (corrected)

**8 of 24 B3 verdicts (33%)** rest ONLY on this collision. An earlier version
of this bean said 7 of 23; that undercounted by one.

| file | matched | in scope of |
|---|---|---|
| `computations/audits/weight_factor_audit.py` | `__doc__`, `q_fac_n` | #5738 |
| `computations/canonical_lepton_braid_words.py` | `desc_tr_M` | #5738 |
| `computations/habiro/habiro_exact_mass_endomorphism.py` | `c_mp` | #5739 |
| `computations/probes/m_pi_hecke_prediction_probe.py` | `c_Lminus`, `c_Lplus`, `c_e_minus`, `c_sigma1` | #5739 |
| `computations/probes/pentagon_multipair_borromean_h4_probe.py` | `c_4` | #5739 |
| `computations/probes/t6_tau_h5_embedding_probe.py` | `qfac_3` | #5739 |
| `computations/t6_lepton_h3_3channel_convention.py` | `qfac_3` | #5739 |
| `computations/t6_three_halves_factor_probes.py` | `qfac_3` | #5739 |

The missed one is `canonical_lepton_braid_words.py`, matching on the `c_`
inside `desc_tr_M` (line 168) -- a local variable holding a Markov trace, as
un-convention-C a name as exists in this corpus. Systematic, as expected:
`c_k` coefficients, `q_fac`/`qfac` quantum factorials and now `desc_*` are all
pervasive here. The other 16 B3s are sound -- audit `deliberate` flag, or a
real `z_C`/`pin_C`.

Method, so the number is re-derivable: run `convention-c-triage.py`, take every
file with a B3 verdict, and ask whether `DELIBERATE` still matches under a
**case-sensitive** pattern. Six such files remain on PR #5738's branch, which
has already migrated the two `c_`/`desc_` cases out of B3; 6 + 2 = 8 of 24.

## Every one of the 8 was a real defect, and all 8 are now migrated

The verdict was wrong in all eight cases, not merely unreliable: #5738
migrated the first two and #5739 the other six, in each case by **reading the
site rather than trusting the verdict**. That is the practical lesson --
B3 is advice, not a finding.

## Confirmed true positive

`weight_factor_audit.py` `check_C8` was classed B3 and is a genuine defect:
it asserted `z_C` AS THE SPECIFICATION ("any consumer hardcoding a
different value would be a bug"). Migrated on PR #5738 by reading the site
rather than trusting the verdict. The `C8` is a check number, not convention C.

## Fix

Do NOT simply anchor as `\bC_`: `_` is a word character, so `\bc_` still
matches a name that STARTS with `c_` (`c_4`, `c_mp`). The C-convention
alternatives want to be case-SENSITIVE — `z_C`, `pin_C`, `Z_C` are
capitalised by convention; the lowercase `c_` prefix is the ambiguous one.
Split into a case-sensitive group for the C spellings, keep `re.I` only
where safe. Re-run the triage and confirm the 16 genuine B3s are unchanged.

## Not fixed on PR #5738

Deliberately: shared tooling a sibling agent was running concurrently
against the other half of the surface. Changing its verdicts mid-flight
would have been worse than the false positives.

## Consequence for the sibling drain -- resolved, recorded for the next reader

6 of the 8 were in PR #5739's scope and could have been left as "deliberate
comparisons" on a verdict that does not hold. They were not: #5739 migrated
all six. The risk this bean describes is therefore realised-and-survived
rather than hypothetical -- which is the argument for fixing the regex before
the next drain, when no one may check.
