**Algorithm (LP/SDP dual-emission contract).**
*Every LP / SDP / operator-selection compute must emit both
primal and dual variables in its witness JSON. This sidecar
documents the canonical contract enforced in CI.*

### Required witness fields

| Field | Meaning |
|-------|---------|
| `y0_star` | shadow price of the net constraint |
| `y_star` | shadow prices of Frobenius positivity constraints (≥ 0) |
| `active_set` (or `active_constraints` / `active_channels`) | indices $i$ with `y_star[i] > 0` |
| `primal_obj` | $\sum_i t_i x_i^*$ |
| `dual_obj` | $n_{\mathrm{target}} \cdot y_0^*$ (= `primal_obj` by strong duality) |
| `duality_gap` | $|\text{primal\_obj} - \text{dual\_obj}|$ |

### Canonical entry point

The shared solver helpers live at
[`tools/pyhecke/python/pyhecke/lp_dual_solver.py`](../../../tools/pyhecke/python/pyhecke/lp_dual_solver.py)
and expose `solve_operator_selection_lp(t, G, n_target)` and
`solve_psd_operator_selection_sdp(t, G, n_target)`. Both return a
result whose `.to_dict()` contains every required field. The
per-witness driver script is
[`confinement-operator-selection.py`](../../../computations/confinement-operator-selection.py).

### CI enforcement

[`computations/lp_dual_witness_validator.py`](../../../computations/lp_dual_witness_validator.py)
runs in `witness-pipeline.yml`:

- warn-only by default;
- `--strict` fails CI;
- `--strict-wired` enforces the wired subset only.

The validator scans every `*.witness.json` whose name or
`description` / `computation` field signals an LP / SDP /
operator-selection compute and verifies the dual fields are
present.

### Why this is mandatory

*The dual variables **are** the binding-energy shadow prices.
The active demand channels (`y_star[i] > 0`) name the most
receptive sub-braids — they identify which Wedderburn blocks the
bound state actually saturates. Solving only the primal loses
this structural information, which has been the historical
pattern (58 of 58 LP/SDP witnesses on `main` lacked the dual at
the time this rule was added).*

### Correctness conditions

*[`prop:operator-selection-lp`](#prop:operator-selection-lp) §
*dual program* establishes strong duality (`primal_obj = dual_obj`
to solver tolerance) and the interpretation of $y^*$ as the
binding-energy shadow prices.*

### Python API entry point

```python
from pyhecke.lp_dual_solver import (
    solve_operator_selection_lp,
    solve_psd_operator_selection_sdp,
)

result = solve_operator_selection_lp(t, G, n_target)
witness = result.to_dict()   # primal + dual + active_set + gap
```

### Notes

*Cross-reference: CLAUDE.md §"LP / SDP duals — first-class
infra". Active baseline of missing-dual witnesses: run the
validator for the current count — do not cite a dated baseline.*
