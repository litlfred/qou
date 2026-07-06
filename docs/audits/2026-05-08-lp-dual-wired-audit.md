# LP-dual wired witness audit (2026-05-08)

This follow-up extends `lp_dual_witness_validator.py` with wired-aware modes so we can separate high-priority production failures from audit-only probes.

## New validator modes

- `--list-wired`  
  Prints every LP/SDP-flagged witness with `[wired]` vs `[audit/orphan]` status and the trigger reason.
- `--strict-wired`  
  Enforces LP-dual completeness only for flagged **wired** witnesses (exit 1 on missing dual fields).
- Existing `--strict` is unchanged (enforces all flagged witnesses).

## Diagnostic improvements

Failure output now includes:

- match reason (filename/description hint + solver marker),
- sibling producer script name (when found),
- missing dual fields list.

## Usage

```bash
python3 computations/lp_dual_witness_validator.py --list-wired
python3 computations/lp_dual_witness_validator.py --strict-wired
python3 computations/lp_dual_witness_validator.py --strict
```

This keeps CI policy explicit: enforce wired production outputs first, while still allowing broader audit scans when needed.
