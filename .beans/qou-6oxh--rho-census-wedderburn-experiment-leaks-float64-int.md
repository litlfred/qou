---
# qou-6oxh
title: rho-census-wedderburn-experiment leaks float64 into every downstream relay
status: todo
type: bug
created_at: 2026-08-30T10:19:49Z
updated_at: 2026-08-30T10:19:49Z
---

`b_over_a_v5_unified.py` reads `rho-census-wedderburn-experiment.witness.json` and relays four fields verbatim into its own `plan_h_diagnostic` block:

    true_rho, delta_rho, rho_handpick, M_err_ppm_predicted

They arrive as raw float64 and are re-emitted as raw float64, so
`b-over-a-v5-unified.witness.json` carries 12 raw-float64 fields it did not
author. Converting them on relay would be fake precision -- they are already
float64 at their source -- so the fix belongs to the upstream producer:
carry mpmath.mpf and serialize with `_precision.fmt`.

Surfaced 2026-08-30 during the AME drain. The committed
`b-over-a-v5-unified.witness.json` predates the `plan_h_diagnostic` feature
entirely, so the leak was invisible until the witness was regenerated. Running
origin/main's own source in the same container also yields 12, confirming none
of it comes from the drain.

## Todo
- [ ] Carry the four fields as mpf in rho_census_wedderburn_experiment
- [ ] Regenerate rho-census-wedderburn-experiment.witness.json
- [ ] Regenerate b-over-a-v5-unified.witness.json and confirm the ratchet drains
