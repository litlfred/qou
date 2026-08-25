---
# qou-4bq3
title: 'GAP: convention-c-triage DELIBERATE regex over-blocks 7 of 23 B3 verdicts'
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

## Measured, 2026-08-25

7 of 23 B3 verdicts (30%) rest ONLY on this collision. What actually matched:

| file | matched |
|---|---|
| `computations/audits/weight_factor_audit.py` | `__doc__`, `q_fac_n` |
| `computations/habiro/habiro_exact_mass_endomorphism.py` | `c_mp` |
| `computations/probes/m_pi_hecke_prediction_probe.py` | `c_Lminus`, `c_Lplus`, `c_e_minus`, `c_sigma1` |
| `computations/probes/pentagon_multipair_borromean_h4_probe.py` | `c_4` |
| `computations/probes/t6_tau_h5_embedding_probe.py` | `qfac_3` |
| `computations/t6_lepton_h3_3channel_convention.py` | `qfac_3` |
| `computations/t6_three_halves_factor_probes.py` | `qfac_3` |

None is a convention-C symbol. `c_k` coefficients and `q_fac`/`qfac`
quantum factorials are pervasive here, so the collision is systematic.
The other 16 B3s are sound — audit `deliberate` flag, or a real `z_C`/`pin_C`.

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

## Consequence for the sibling drain

3 of the 7 (`m_pi_hecke_prediction_probe`, `pentagon_multipair_borromean_h4_probe`,
the `t6_*` group) are in the sibling's scope and may be left as "deliberate
comparisons" on a verdict that does not hold.
