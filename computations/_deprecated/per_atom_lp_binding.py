"""
Per-atom LP binding via shadow prices — H_6 probe for 4He (and beyond).

Per `prop:operator-selection-lp` and the user's directive, replace
the hand-picked per-braid hybrid with an LP-driven mass formula.
For each atom (Z, N), build:
  - reduced NF basis (H_3 active set lifted to H_{3A} via tensor)
  - Markov traces t_i on that basis
  - Frobenius Gram G_{ij}
  - target n_target (= AME / m_e)
Solve the operator-selection LP via `lp_dual_solver` — get
primal Φ* and dual y_0*, y_i*. The dual y_0* IS the categorical
mass per unit target; its strong-duality value should match AME/m_e
WITHOUT scheme selection.

H_3 case: starts from confinement-lp.witness.json (NF basis +
Gram). H_6 case: lifts the H_3 active set ({σ₀, L_-} per
lp-duality-check.witness.json) via tensor product to build a small
reduced basis for H_6.

This is the FIRST per-atom LP binding script using the new
lp_dual_solver infra. Witnesses include the full primal+dual per
the §3b LP-dual contract (lp_dual_witness_validator enforces).
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from lp_dual_solver import solve_operator_selection_lp


# H_3 NF basis + Markov traces from existing witness.
def load_h3_data() -> dict:
    """Load NF basis + Markov traces + Gram matrix from H_3 witness."""
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


# ───────────────────────────────────────────────────────────────────
# Phase 1: H_3 LP — proton/neutron via shadow prices.
# ───────────────────────────────────────────────────────────────────

# Targets per `operator-selection-lp.md` table (line 179):
#   proton  ≈ 0.999
#   neutron ≈ 0.811
# These are the categorical-mass targets at H_3.
H3_TARGETS = {
    "proton":  0.9991,
    "neutron": 0.8108,
}


def lp_at_h3(target_name: str, h3: dict) -> dict:
    """Run operator-selection LP at H_3 for a named target (proton/neutron)."""
    n_target = H3_TARGETS[target_name]
    res = solve_operator_selection_lp(h3["t"], h3["G"], n_target)
    out = res.to_dict()
    out["target"] = target_name
    out["n_target"] = n_target
    out["basis_names"] = h3["names"]
    out["active_basis"] = [h3["names"][i] for i in res.active_set]
    return out


# ───────────────────────────────────────────────────────────────────
# Phase 2: H_6 LP — 4He from H_3 active-set tensor lift.
# ───────────────────────────────────────────────────────────────────
# Reduced basis for H_6: tensor products of H_3 active-set elements
# with themselves. This is the principled iterative reduction:
# the LP's active set at level n = 3 identifies the basis elements
# that survive at level n = 6.

def lift_h3_active_to_h6_basis(h3_lp_result: dict, h3: dict) -> dict:
    """Tensor-lift H_3 active set to a reduced H_6 basis.

    Reduced basis at H_6: {b_i ⊗ b_j : i, j ∈ active_h3} plus the
    H_3 active set acting on the first 3 strands only (γ ⊗ b_i and
    b_i ⊗ γ as identity-padded versions).

    Returns dict with names + Markov traces + Gram for the small
    (~4-9 element) H_6 reduced basis. Markov traces of tensor
    products use the multiplicativity tr_M(a ⊗ b) = tr_M(a) · tr_M(b)
    (Jones–Markov factorization; see thm:markov-trace-factorization).
    """
    active = h3_lp_result["active_set"]
    if not active:
        # Fallback: use top-2 absolute primal coefficients as active proxy
        x = np.abs(np.asarray(h3_lp_result["x_star"]))
        active = list(np.argsort(-x)[:2])
    # Build reduced H_6 basis: tensor pairs of active H_3 elements.
    h3_names = h3["names"]
    h3_t = h3["t"]
    h3_G = h3["G"]

    h6_names = []
    h6_t = []
    # We approximate the H_6 Gram diagonal by tr_M(b_i⊗b_j · b_i⊗b_j)
    # = tr_M(b_i²) · tr_M(b_j²) = G[i,i] · G[j,j].  Off-diagonals via
    # tr_M((b_i⊗b_j)(b_k⊗b_l)) = G[i,k] · G[j,l] (multiplicativity on
    # disjoint strand groups).
    pair_idx = []
    for i in active:
        for j in active:
            h6_names.append(f"{h3_names[i]}⊗{h3_names[j]}")
            h6_t.append(float(h3_t[i] * h3_t[j]))
            pair_idx.append((i, j))
    d6 = len(h6_names)
    G6 = np.zeros((d6, d6))
    for a, (i, j) in enumerate(pair_idx):
        for b, (k, l) in enumerate(pair_idx):
            G6[a, b] = h3_G[i, k] * h3_G[j, l]
    return {
        "names": h6_names,
        "t": np.asarray(h6_t),
        "G": G6,
        "pair_idx": pair_idx,
        "active_h3": active,
    }


def lp_at_h6_for_4he(h6: dict) -> dict:
    """LP at H_6 reduced basis for 4He (Z=N=2).

    Target: n_target = AME(4He) / m_e in dimensionless units.
    """
    AME_4HE = 3727.37909409  # MeV
    M_E_MEV = 0.51099895
    n_target = AME_4HE / M_E_MEV  # ≈ 7294.30

    res = solve_operator_selection_lp(h6["t"], h6["G"], n_target)
    out = res.to_dict()
    out["target_atom"] = "4He"
    out["n_target"] = n_target
    out["basis_names"] = h6["names"]
    out["active_basis"] = [h6["names"][i] for i in res.active_set]
    return out


def main():
    h3 = load_h3_data()
    print("=" * 88)
    print("Per-atom LP binding via shadow prices — H_3 + H_6 probe")
    print("=" * 88)

    # Phase 1: H_3 LP for proton / neutron
    print()
    print("─── Phase 1: H_3 LP for proton + neutron ───")
    h3_results = {}
    for target_name in ("proton", "neutron"):
        r = lp_at_h3(target_name, h3)
        h3_results[target_name] = r
        print(f"  {target_name}:  n_target = {r['n_target']:.4f}")
        print(f"    primal_obj = {r['primal_obj']:.6f}")
        print(f"    dual_obj   = {r['dual_obj']:.6f}")
        print(f"    duality_gap = {r['duality_gap']:.2e}")
        print(f"    y_0* (shadow price) = {r['y0_star']:.6f}")
        print(f"    active basis: {r['active_basis']}")

    # Phase 2: H_6 LP for 4He via lifted basis
    print()
    print("─── Phase 2: H_6 LP for 4He (lifted from proton active set) ───")
    h6 = lift_h3_active_to_h6_basis(h3_results["proton"], h3)
    print(f"  Reduced H_6 basis ({len(h6['names'])} elements):")
    for nm in h6["names"]:
        print(f"    {nm}")
    r6 = lp_at_h6_for_4he(h6)
    print()
    print(f"  4He LP:  n_target = AME/m_e = {r6['n_target']:.4f}")
    print(f"    primal_obj = {r6['primal_obj']:.6f}")
    print(f"    dual_obj   = {r6['dual_obj']:.6f}")
    print(f"    duality_gap = {r6['duality_gap']:.2e}")
    print(f"    y_0* (shadow price) = {r6['y0_star']:.6f}")
    print(f"    active basis: {r6['active_basis']}")
    print()
    if r6["feasible"]:
        # cal/m_e: how close is y_0* to 1?  Per strong duality,
        # y_0* IS the binding-energy density per unit target mass.
        print(f"    y_0* / 1 (binding density vs unit) = {r6['y0_star']:.6f}")
    else:
        print("    LP infeasible — basis too restrictive at this n_target.")

    # Witness output (includes full LP duals per §3b LP-dual contract)
    out = {
        "computation": "per-atom LP binding via shadow prices",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "h3_results": h3_results,
        "h6_basis": {
            "names": h6["names"],
            "size": len(h6["names"]),
        },
        "h6_4He_result": r6,
        "lp_dual_contract": "per §3b LP-dual: includes y0_star, y_star, "
                            "active_set, primal_obj, dual_obj, duality_gap",
    }
    out_path = Path(__file__).parent / "per-atom-lp-binding.witness.json"
    out_path.write_text(json.dumps(out, indent=2, default=str))
    print()
    print(f"Witness: {out_path.relative_to(Path(__file__).parent.parent.parent)}")


if __name__ == "__main__":
    main()
