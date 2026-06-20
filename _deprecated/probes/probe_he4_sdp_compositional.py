"""F1-SDP: ⁴He compositional probe via SDP active-set fingerprint.

Forward step from `2026-05-15-three-pr-integration.md` F1 prompt:
identify which compositional channels carry the ⁴He binding via the
LP/SDP shadow-price active set, *without* computing the full
12-strand braid τ_M.

## Compositional channels for ⁴He = (Z=2, N=2)

| channel | parts | $\sum \Delta_\mathrm{cat}$ (parts, MeV) |
|---------|-------|---:|
| D ⊕ D  | (1,1) + (1,1) | 4.052 |
| T ⊕ p  | (1,2) + (1,0) | 7.831 |
| ³He ⊕ n | (2,1) + (0,1) | 7.035 |

The empirical Δ_cat(⁴He) = 28.21 MeV. The "channel residual" is
the gap between the channel-sum-of-parts and the actual atom-level
Δ_cat — this measures how much *binding* a given channel
decomposition leaves on the table.

## SDP formulation

Use `solve_psd_operator_selection_sdp(t, G, n_target)` from
`lp_dual_solver.py` (AGENTS.md §LP/SDP duals — first-class infra).

- `t[i]` = channel-binding-residual for channel i:
  `t[i] = Δ_cat(⁴He) − sum-of-parts(i)`. Larger `t[i]` means the
  channel leaves more binding for the magic-shell coupling to
  explain.
- `G` = channel × channel Frobenius pairing, identity at leading
  order (channels are orthogonal in the cluster algebra).
- `n_target` = a normalization scale. We use the (2,2) anchor
  Δ_coupling = Δ_cat(⁴He) − 2·Δ_cat(³He) = 13.197 MeV (PR #645).

## Output

- `active_set`: which channels saturate the dual constraint.
  These are the **structurally-binding channels**.
- `y_star`: shadow prices — channel-by-channel receptivity.
- `duality_gap`: primal-dual closure check.

Cheap compute: O(seconds) for a 3-dim SDP.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import numpy as np
import mpmath as mp

from witness_base import WitnessBuilder
from lp_dual_solver import (
    solve_operator_selection_lp,
    solve_psd_operator_selection_sdp,
)


def _mpf_str(s: str) -> mp.mpf:
    return mp.mpf(s)


def main() -> int:
    msei = json.load(
        open(HERE / "magic-shell-empirical-instantiation.witness.json")
    )
    pad = msei["data"]["per_atom_delta_cat"]
    dc = {
        atom: _mpf_str(pad[atom]["delta_cat_MeV_50dps"])
        for atom in ("proton", "neutron", "deuteron", "tritium", "he3", "he4")
    }

    channels = [
        ("DD",   dc["deuteron"] + dc["deuteron"]),
        ("Tp",   dc["tritium"] + dc["proton"]),
        ("He3n", dc["he3"] + dc["neutron"]),
    ]
    he4_total = dc["he4"]
    t_residual = np.array(
        [float(he4_total - parts) for _, parts in channels],
        dtype=np.float64,
    )

    n_target = float(he4_total - 2 * dc["he3"])

    G = np.eye(len(channels), dtype=np.float64)

    print(f"=== F1-SDP: ⁴He compositional probe ===\n")
    print(f"Δ_cat(⁴He) = {float(he4_total):.6f} MeV")
    print(f"Channel residuals (binding left for magic-shell coupling):")
    for (name, parts), r in zip(channels, t_residual):
        print(f"  {name:8} parts={float(parts):>8.4f}  residual={r:>8.4f} MeV")
    print(f"\nn_target = Δ_coupling(2,2) = {n_target:.6f} MeV")

    # G is diagonal (channels orthogonal at leading order); per
    # AGENTS.md §LP/SDP duals the SDP reduces to LP for diagonal G.
    # Try SDP first (rigorous PSD), fall back to LP if cvxpy
    # unavailable — equivalent solution for this structure.
    solver_used = "sdp_cvxpy"
    try:
        sdp_result = solve_psd_operator_selection_sdp(
            t_residual, G, n_target,
        )
        res = sdp_result.to_dict()
    except ImportError as exc:
        print(f"  cvxpy unavailable ({exc}); falling back to LP "
              f"(equivalent for diagonal G).")
        lp_result = solve_operator_selection_lp(
            t_residual, G, n_target,
        )
        res = lp_result.to_dict()
        solver_used = "lp_scipy_linprog"
    print(f"\n=== SDP solution (solver = {solver_used}) ===")
    print(f"primal_obj      = {res['primal_obj']:.6f}")
    print(f"dual_obj        = {res['dual_obj']:.6f}")
    print(f"duality_gap     = {res['duality_gap']:.2e}")
    print(f"y0_star         = {res['y0_star']:.6f}")
    print(f"y_star          = {[round(v, 6) for v in res['y_star']]}")
    print(f"x_star (primal) = {[round(v, 6) for v in res['x_star']]}")
    active = res.get('active_set') or res.get('active_constraints', [])
    print(f"active_set      = {active}")
    print(f"\nInterpretation:")
    for i, (name, _) in enumerate(channels):
        weight = res['x_star'][i] if i < len(res['x_star']) else None
        price = res['y_star'][i] if i < len(res['y_star']) else None
        active_flag = "ACTIVE" if i in active else "      "
        print(f"  {name:8} x={weight:>9.4f}  y={price:>9.4f}  {active_flag}")

    builder = (
        WitnessBuilder(
            "he4-sdp-compositional-probe", engine="numpy+scipy",
        )
        .set_description(
            "⁴He compositional channel identification via SDP "
            "active-set fingerprint. Identifies which of the three "
            "primary channels (D⊕D, T⊕p, ³He⊕n) carry the magic-"
            "shell coupling without computing the full β_{⁴He} "
            "Markov trace. Forward step on F1 from the three-PR "
            "integration audit."
        )
        .set_content_block("prop:magic-shell-coupling-kappa")
        .add_parameter("channels", [name for name, _ in channels])
        .add_parameter("n_target", n_target)
        .add_data(
            "delta_cat_inputs",
            {atom: float(v) for atom, v in dc.items()},
        )
        .add_data(
            "channel_parts_sum",
            {name: float(p) for name, p in channels},
        )
        .add_data("t_residual_MeV", t_residual.tolist())
        .add_data("solver", solver_used)
        .add_data("sdp_full", res)
        .add_data(
            "active_channels",
            [channels[i][0] for i in active] if active else [],
        )
        .add_assertion(
            name="duality_gap_zero",
            computed=abs(res["duality_gap"]),
            expected=0.0,
            tolerance=1e-6,
            unit="dimensionless",
            source="strong duality for feasible LP/SDP",
        )
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
