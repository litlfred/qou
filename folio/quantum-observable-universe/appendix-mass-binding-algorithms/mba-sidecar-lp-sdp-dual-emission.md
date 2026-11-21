**Algorithm (LP/SDP dual-emission contract).**
*Every LP / SDP / operator-selection compute must emit both
primal and dual variables in its witness JSON. This sidecar
documents the canonical contract.*

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

### Validation

The contract is checked mechanically by
[`computations/lp_dual_witness_validator.py`](../../../computations/lp_dual_witness_validator.py).
The validator scans every `*.witness.json` whose name or
`description` / `computation` field signals an LP / SDP /
operator-selection compute and verifies the dual fields are
present.

### Why this is mandatory

*The dual variables **are** the binding-energy shadow prices. Active demand channels (`y_star[i] > 0`) name the receptive sub-braids, identifying the Wedderburn blocks saturated by the bound state. Solving only the primal drops this structural information, a historical flaw (58 of 58 LP/SDP witnesses lacked the dual when this rule was introduced).*

### Correctness conditions

*[Knot operator selection as linear program with LP duality](#prop:operator-selection-lp) §
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

*Not every LP/SDP witness yet carries its dual. The number outstanding changes
as the computations are extended, so no figure for it is quoted here.*
