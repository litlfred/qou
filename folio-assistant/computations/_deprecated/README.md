# `_deprecated/`

Scripts and witness files in this directory are **superseded by the
canonical chain** (see `../README.md`). They are kept in git history
for reference but should not be imported by any active code.

## Quarantined as of 2026-04-27

| script / witness | reason | superseded by |
|---|---|---|
| `atom_mass_qou_calibration.py` | explicit "calibration" in name; fits to AME | `categorical_q_decay_ba_low_isotopes.py` |
| `atom_rt_fusion_v2.py` | exploratory v2 of an RT-fusion approach; not used in canonical chain | `mass_formula_6term.py` |
| `bw_lagrangian_prefactor_derivation_attempt.py` | explicit "attempt" in name; superseded | `bw_chirality_isotopes.py` |
| `comprehensive_low_isotope_table_v2.py` + witness | superseded by 4-tier canonical predictor | `categorical_q_decay_ba_low_isotopes.py` |
| `recursive_three_calibration.py` | explicit "calibration" in name; fits | derived from canonical 3-input scheme |
| `universal_three_calibration.py` | explicit "calibration" in name; fits | derived from canonical 3-input scheme |

## Policy

- **Do not import from `_deprecated/`.** If you need functionality
  here, the canonical replacement is in the table above.
- **Do not delete.** Git history is the audit trail; explicit
  quarantine signals "superseded but preserved" rather than
  "missing or accidentally lost".
- **Adding to this directory**: a script is deprecation-eligible if
  it (a) has explicit `_deprecated*`, `_v[0-9]+`, `_attempt`,
  `_calibration` markers in its filename AND (b) is not imported by
  any non-deprecated script (verified via `grep -l "from <name>"`).

## See also

- [`../README.md`](../README.md) — canonical-script index for
  `folio-assistant/computations/`
- [`../canonical-script-input-audit.witness.json`](../canonical-script-input-audit.witness.json) —
  full classification of all 524 scripts (524 → 518 after this
  quarantine round)
