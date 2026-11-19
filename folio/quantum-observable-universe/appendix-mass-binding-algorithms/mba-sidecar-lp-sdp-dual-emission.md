**Algorithm (LP/SDP dual-emission contract).**
*Every LP / SDP / operator-selection compute must emit both
primal and dual variables in its witness JSON. This sidecar
documents the canonical contract.*

### Required witness fields

```json
{
  "y0_star":     "<float: shadow price of the net constraint>",
  "y_star":      ["<float >= 0: shadow prices of Frobenius positivity constraints>"],
  "active_set":  ["<int: indices i with y_star[i] > 0 (aliases: active_constraints, active_channels)>"],
  "primal_obj":  "<float: sum_i t_i x_i*>",
  "dual_obj":    "<float: n_target * y_0* (= primal_obj by strong duality)>",
  "duality_gap": "<float: |primal_obj - dual_obj|>"
}
```

| Quantity | Meaning |
|-------|---------|
| $y_0^*$ | shadow price of the net constraint |
| $y^*$ | shadow prices of Frobenius positivity constraints ($\geq 0$) |
| $\{i : y_i^* > 0\}$ | active constraint indices |
| $p^*$ | primal objective $\sum_i t_i x_i^*$ |
| $d^*$ | dual objective $n_{\mathrm{target}} \cdot y_0^*$ ($= p^*$ by strong duality) |
| $|p^* - d^*|$ | duality gap |

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
[`lp_dual_witness_validator.py`](../../../computations/lp_dual_witness_validator.py).
The validator scans every `*.witness.json` whose name or
`description` / `computation` field signals an LP / SDP /
operator-selection compute and verifies the dual fields are
present.

### Why this is mandatory

*The dual variables **are** the binding-energy shadow prices. Active demand channels ($y_i^* > 0$) name the receptive sub-braids, identifying the Wedderburn blocks saturated by the bound state. Solving only the primal drops this structural information.*

### Correctness conditions

*[The operator-selection LP proposition](#prop:operator-selection-lp) §
*dual program* establishes strong duality ($p^* = d^*$
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
