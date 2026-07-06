# LP-dual backfill status

Date: 2026-05-07

Ran:

```bash
cd /home/runner/work/qou/qou/computations
python3 lp_dual_witness_validator.py
```

## Result

- witnesses scanned: `201`
- flagged as LP/SDP/operator-selection: `3`
- all flagged witnesses already include the required dual fields

## Notes

`ch-bond-writhe-lp.witness.json` exists, but the validator correctly does **not** flag it under the current heuristics because the sibling script does not import `linprog`, `cvxpy`, or `lp_dual_solver`.  No LP-dual backfill change was required in this retry.
