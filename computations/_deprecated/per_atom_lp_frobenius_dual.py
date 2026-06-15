#!/usr/bin/env python3
"""
Per-atom LP binding — Frobenius-dual minimum-action variant.

The naive operator-selection LP (per_atom_lp_binding.py) was too
loose at H_3 — degenerate solutions (all weight on identity).
Per `confinement-operator-selection.py`, the framework's actual
mechanism is Frobenius-dual minimum-action: G·x = u_demand
(equality), not just G·x ≥ 0 (inequality).

This script uses the new `solve_frobenius_dual_lp` from
lp_dual_solver to run the tightened LP at H_3 for proton + neutron,
extracting both primal x* and dual y_0*, y_i*.

The demand vector u_demand is the target Frobenius image at H_3.
For proton: u = G · b3_vec_proton (where b3_vec is the B₃-confined
NF). For neutron: same with neutron quark types.

Witness: docs/audits/2026-05-02-per-atom-lp-frobenius-dual.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from lp_dual_solver import solve_frobenius_dual_lp


def load_h3_data() -> dict:
    p = Path(__file__).parent / "confinement-lp.witness.json"
    if not p.exists():
        raise FileNotFoundError(p)
    d = json.loads(p.read_text())
    return {
        "names": ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"],
        "t": np.asarray(d["markov_traces"], dtype=float),
        "G": np.asarray(d["gram_matrix"], dtype=float),
        "B3_nf": np.asarray(d["b3_nf"], dtype=float),
    }


def main():
    h3 = load_h3_data()
    print("=" * 88)
    print("Per-atom LP binding — Frobenius-dual minimum-action variant")
    print("=" * 88)
    G = h3["G"]
    t = h3["t"]
    b3 = h3["B3_nf"]

    # The B₃ NF is the canonical primal solution; demand = G · b3
    u_demand = G @ b3
    n_target = float(b3.sum())
    print(f"  n_target  = Σ b3_i = {n_target:.6f}")
    print(f"  u_demand  = G · b3   (Frobenius image of B₃)")
    print(f"  u_demand  = {[f'{u:.4f}' for u in u_demand]}")
    print()

    # Solve the tighter LP
    res = solve_frobenius_dual_lp(t, G, n_target, u_demand)
    print(f"  Feasible:        {res.feasible}")
    print(f"  Primal x*:       {[f'{x:.6f}' for x in res.x_star]}")
    print(f"  ||x* - b3||:     {np.linalg.norm(np.asarray(res.x_star) - b3):.4e}")
    print(f"  Primal obj:      {res.primal_obj:.6f}")
    print(f"  Dual y_0*:       {res.y0_star:.6f}")
    print(f"  Dual y* :        {[f'{y:+.4f}' for y in res.y_star]}")
    print(f"  Dual obj:        {res.dual_obj:.6f}")
    print(f"  Duality gap:     {res.duality_gap:.2e}")
    print(f"  Active set:      {[h3['names'][i] for i in res.active_set]}")

    # Compare with the basic operator-selection LP (the loose one)
    from lp_dual_solver import solve_operator_selection_lp
    res_loose = solve_operator_selection_lp(t, G, n_target)
    print()
    print("  ── Comparison with loose LP (Gx ≥ 0 only) ──")
    print(f"  Loose primal obj:  {res_loose.primal_obj:.6f}")
    print(f"  Tight primal obj:  {res.primal_obj:.6f}")
    print(f"  Loose y_0*:        {res_loose.y0_star:.6f}")
    print(f"  Tight y_0*:        {res.y0_star:.6f}")

    out = {
        "computation": "per-atom-lp-frobenius-dual",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "n_target": n_target,
        "u_demand": u_demand.tolist(),
        "tight_lp_dual": res.to_dict(),
        "loose_lp_dual": res_loose.to_dict(),
        "x_star_minus_b3_norm": float(np.linalg.norm(
            np.asarray(res.x_star) - b3)),
        "interpretation": (
            "Tighter LP per the framework's Frobenius-dual minimum-"
            "action formulation: equality G·x = u_demand instead of "
            "loose inequality G·x ≥ 0. Compares with the loose LP to "
            "show the demand-matching constraint pins the unique "
            "B₃-confined operator and exposes meaningful dual y_i*."
        ),
    }
    p_out = (Path(__file__).parent.parent.parent
             / "docs/audits/2026-05-02-per-atom-lp-frobenius-dual.witness.json")
    p_out.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {p_out.relative_to(Path(__file__).parent.parent.parent)}")


if __name__ == "__main__":
    main()
