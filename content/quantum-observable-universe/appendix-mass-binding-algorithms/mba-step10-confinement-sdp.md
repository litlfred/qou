**Algorithm (Confinement SDP — canonical $T_w$).**
*Solve the LP/SDP that selects the canonical Hecke element $T_w$
realising confinement (or gluon attachment, electron attachment,
molecular bonding — the universal ILP of Algorithm
$\mathtt{def:universal-ilp-algorithm}$).*

### Input

- *Current state $x \in H_n(q)$ (Hecke normal form — Step 2).*
- *Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ computed once
  via Step 6.*
- *Markov-trace vector $t_i = \mathrm{tr}_M(b_i)$.*
- *Target net constraint $n_{\mathrm{target}} \in \mathbb{Z}_{\geq 0}$.*

### Output

- *Primal: optimal $x^* \in \mathbb{R}_{\geq 0}^{\mathrm{cols}(G)}$.*
- *Dual: shadow prices $y_0^*$ (net constraint) and
  $y^*_i \geq 0$ (Frobenius positivity).*
- *Active set: $\{i : y^*_i > 0\}$ — the "receptive sub-braids".*
- *`primal_obj`, `dual_obj`, `duality_gap = |primal_obj − dual_obj|`.*

### Algorithm

```
1. Build LP:
   minimize   Σ_i t_i x_i
   subject to net(x) = n_target,
              G x ≥ 0,
              x ≥ 0.
2. Solve via Clarabel (default) or a sibling SDP backend.
3. Recover dual variables y_0*, y*.
4. Emit the LP-dual witness (per CLAUDE.md "LP/SDP duals —
   first-class infra").
```

### Correctness conditions

*[`prop:operator-selection-lp`](#prop:operator-selection-lp)
specifies the LP and proves the canonical $T_w$ is its primal
optimum. Strong duality gives `primal_obj = dual_obj` (modulo
solver tolerance); the active dual variables identify the
binding-energy shadow prices that feed Step 9b.*

### Complexity

*Polynomial in $\dim H_n(q)$. Clarabel solves the proton-scale
LP in milliseconds.*

### Python API entry point

*Canonical compute is the script
[`computations/confinement-operator-selection.py`](../../../computations/confinement-operator-selection.py),
which solves the LP with primal + dual emission and writes
`confinement-operator-selection.witness.json`. The reusable
solver helpers are exposed as
`pyhecke.lp_dual_solver.solve_operator_selection_lp(t, G, n_target)`
(in [`tools/pyhecke/python/pyhecke/lp_dual_solver.py`](../../../tools/pyhecke/python/pyhecke/lp_dual_solver.py)).*

### Witness contract

*Canonical witness:
[`confinement-operator-selection.witness.json`](../../../computations/confinement-operator-selection.witness.json).
**Must emit all of** `y0_star`, `y_star`, `active_set`,
`primal_obj`, `dual_obj`, `duality_gap` — enforced in CI by
[`lp_dual_witness_validator.py`](../../../computations/lp_dual_witness_validator.py)
(see CLAUDE.md "LP/SDP duals — first-class infra").*

### Notes

*The active dual variables $y^*_i > 0$ name the "most receptive
sub-braids" — they are the structural identifiers of the
saturated Wedderburn blocks. Solving only the primal loses this
information; the dual emission is **required**, not optional.*
