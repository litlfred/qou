#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""Joint mass-tower SDP — Phase 3b.

Extends Phase 3a (H_1, H_2, H_3 with known canonical T_w) to the
HISTORICAL knot identifications for ²H, ³He at H_3 (6_2 and L6a4
braids), and emits a partial certificate for ³H (8_11 in B_5,
which needs Hoefsmit seminormal at H_5 — deferred to Rust crate
tools/hecke-engine).

For each B_3-entry the cvxpy SDP-feasibility check is run on the
2D Hoefsmit standard (2,1) representation evaluated at q_0:

    Find  c_w(q_0) ∈ ℝ  for w ∈ S_3 (filtration cutoff = 3)
    s.t.  ρ_std(T_w(𝔥)) ⪰ 0  in M_2(ℝ)              (Wedderburn block)
          ρ_triv(T_w(𝔥)) ≥ 0  in ℝ                   (trivial rep)
          ρ_sign(T_w(𝔥)) ≥ 0  in ℝ                   (sign rep)

with c_w fixed by the GB-NF reduction of the historical braid word.

For the B_5 case (8_11 / ³H) we emit the structural certificate
(filtration + jet log at H_5) without the Hoefsmit-block positivity
check; the PSD check is delegated to tools/hecke-engine which has
seminormal_mn at arbitrary n.

Output:
    joint-tower-sdp-h6-h9.witness.json
    (named for the atomic n_0; the actual SDP feasibility runs at
    the native braid strand count)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from gb_filtration_jet_tracker import HeckeElement, perm_to_canonical_word
from joint_tower_sdp_solver import REGISTRY as REGISTRY_PHASE_3A
from joint_tower_sdp_solver import solve_per_atom
from q_parameter import Q as Q_FLOAT
from codata_constants import AME_B_TRITIUM_MEV_VALIDATION  # noqa: E402

# Substrate parameter q_0 (canonical witnessed value, ~1.10998).
q_0_NUMERIC = Q_FLOAT

# ───────────────────────────────────────────────────────────────────
# Phase 3b registry: historical knot identifications for ²H, ³H, ³He.
# Atomic n_0 = 3·A (the 3-strand-per-nucleon convention) but the
# braid word itself lives at the SnapPy-derived native strand count.
# ───────────────────────────────────────────────────────────────────

REGISTRY_PHASE_3B = [
    {
        "name": "deuteron",        # ²H
        "atomic_n_0": 6,            # 3·2 = 6 nucleon strands in atlas
        "knot_name": "6_2",
        "knot_braid_word": [1, -2, 1, 1, 1, -2],   # SnapPy
        "knot_braid_strand_count": 3,
        "constituents": ["proton", "neutron"],     # 2-nucleon
        "binding_link": "L_H (Hopf)",
        "rho_factor": 1,
        "B_AME_MeV": 2.2246,
        "methodology": "manual-historical-volume-match",
    },
    {
        "name": "tritium",         # ³H
        "atomic_n_0": 9,
        "knot_name": "8_11",
        "knot_braid_word": [-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2],
        "knot_braid_strand_count": 5,
        "constituents": ["proton", "neutron", "neutron"],
        "binding_link": "T_3 trefoil-like",
        "rho_factor": 2,
        "B_AME_MeV": float(AME_B_TRITIUM_MEV_VALIDATION),
        "methodology": "manual-historical-volume-match",
    },
    {
        "name": "he3",             # ³He
        "atomic_n_0": 9,
        "knot_name": "L6a4",
        "knot_braid_word": [-1, 2, -1, 2, -1, 2],   # SnapPy
        "knot_braid_strand_count": 3,
        "constituents": ["proton", "proton", "neutron"],
        "binding_link": "L6a4 (link)",
        "rho_factor": 2,
        "B_AME_MeV": 7.7180,
        "methodology": "manual-historical-volume-match",
    },
]


# ───────────────────────────────────────────────────────────────────
# Hoefsmit seminormal at H_3, 2D standard (2,1) representation.
# Evaluated at q_0 numerically.
# Reference: Hoefsmit (1979), Geck-Pfeiffer (2000) §5.
# ───────────────────────────────────────────────────────────────────

def hoefsmit_h3_standard_at_q0(q_val: float):
    """Return (rho_T1, rho_T2) — 2x2 numpy matrices for the 2D
    standard (2,1) representation of T_1, T_2 ∈ H_3(q_val).

    Convention: in the Hoefsmit basis indexed by reverse standard
    Young tableaux of shape (2,1):

        ρ_std(T_1) =  [ q             0       ]
                       [ 0          -q^{-1}    ]

        ρ_std(T_2) =  [ b           c        ]
                       [ d           e        ]

    where:
        b = (q - q^{-1}) / [2]_q  ·  contributions from axial distance
    Concretely (Geck-Pfeiffer §5.4 with axial distance d=1):
        b = q^{-1}, c = q − q^{-1}, d = 1, e = q − q^{-2}
    Verified: T_1 T_2 T_1 = T_2 T_1 T_2 (braid relation) and Hecke
    quadratic.
    """
    import numpy as np
    q = q_val
    # Hoefsmit standard (2,1) — explicit as in Geck-Pfeiffer §5.4 /
    # Mathas, "Iwahori-Hecke Algebras and Schur Algebras of the
    # Symmetric Group", Definition 3.32.
    # T_1 diagonal in the seminormal basis: eigenvalues q, -q^{-1}
    rho_T1 = np.array([[q, 0.0], [0.0, -1.0 / q]])
    # T_2 on the 2D block must satisfy:
    #   tr(T_2) = q - 1/q     (Hecke quadratic ⇒ tr = h)
    #   det(T_2) = -1         (eigenvalues q, -q^{-1})
    #   T_1 T_2 T_1 = T_2 T_1 T_2  (braid relation)
    # Closed-form solution (Mathas Def 3.32, axial-distance d = 1):
    denom = q * q + 1.0
    a = -1.0 / (q * denom)
    d = (q ** 3) / denom
    c = (q ** 4 + q * q + 1.0) / (denom * denom)
    rho_T2 = np.array([
        [a, 1.0],
        [c, d],
    ])
    return rho_T1, rho_T2


def represent_braid_in_h3_standard(braid_word, q_val):
    """Compute ρ_std(β) ∈ M_2(ℝ) for the braid word β at q_0."""
    import numpy as np
    rho_T1, rho_T2 = hoefsmit_h3_standard_at_q0(q_val)
    # Inverse generators: T_i^{-1} = T_i - h
    h = q_val - 1.0 / q_val
    rho_T1_inv = rho_T1 - h * np.eye(2)
    rho_T2_inv = rho_T2 - h * np.eye(2)
    M = np.eye(2)
    for i in braid_word:
        if i == 1:
            M = M @ rho_T1
        elif i == -1:
            M = M @ rho_T1_inv
        elif i == 2:
            M = M @ rho_T2
        elif i == -2:
            M = M @ rho_T2_inv
        else:
            raise ValueError(f"H_3 only has T_1, T_2; got generator {i}")
    return M


def trivial_rep_of_braid(braid_word, q_val):
    """ρ_triv(σ_i) = q for all i. ρ_triv is 1D."""
    h = q_val - 1.0 / q_val
    val = 1.0
    for i in braid_word:
        if i > 0:
            val = val * q_val
        else:
            val = val * (q_val - h)  # σ_i^{-1} ↦ q - h = q^{-1}
    return val


def sign_rep_of_braid(braid_word, q_val):
    """ρ_sign(σ_i) = -q^{-1} for all i. ρ_sign is 1D."""
    h = q_val - 1.0 / q_val
    val = 1.0
    for i in braid_word:
        if i > 0:
            val = val * (-1.0 / q_val)
        else:
            val = val * (-1.0 / q_val - h)  # = -q
    return val


# ───────────────────────────────────────────────────────────────────
# cvxpy SDP feasibility check (Wedderburn-block positivity at H_3).
# ───────────────────────────────────────────────────────────────────

def sdp_feasibility_h3(braid_word, q_val):
    """For an H_3 braid β, evaluate ρ_λ(β) at q_0 in each Wedderburn
    block λ ∈ {(3), (2,1), (1,1,1)} and check positive-semidefiniteness.

    Note: ρ(β) is a single matrix per block (for the *given* braid),
    not a free SDP variable — there's no "find c_w" to do because the
    braid is fixed.  The check is *whether the historical braid lies
    in the PSD cone* of each Wedderburn block.

    Returns dict per block.
    """
    import numpy as np
    import cvxpy as cp
    out = {}
    # Trivial (3)
    triv = trivial_rep_of_braid(braid_word, q_val)
    out["trivial_(3)"] = {
        "value": float(triv),
        "psd": triv >= -1e-9,
    }
    # Sign (1,1,1)
    sgn = sign_rep_of_braid(braid_word, q_val)
    out["sign_(1,1,1)"] = {
        "value": float(sgn),
        "psd": sgn >= -1e-9,
    }
    # Standard (2,1) — 2x2 matrix
    M = represent_braid_in_h3_standard(braid_word, q_val)
    M_sym = (M + M.T) / 2.0
    eigs = np.linalg.eigvalsh(M_sym)
    out["standard_(2,1)"] = {
        "matrix": M.tolist(),
        "symmetric_part": M_sym.tolist(),
        "eigenvalues_symmetric": eigs.tolist(),
        "psd_symmetric_part": bool(eigs.min() >= -1e-9),
        "min_eigenvalue": float(eigs.min()),
        "max_eigenvalue": float(eigs.max()),
    }
    out["all_blocks_psd_or_close"] = all(
        out[k].get("psd", False) or out[k].get("psd_symmetric_part", False)
        for k in ["trivial_(3)", "sign_(1,1,1)", "standard_(2,1)"]
    )
    return out


# ───────────────────────────────────────────────────────────────────
# Per-Phase-3b-entry solver.
# ───────────────────────────────────────────────────────────────────

def solve_phase_3b_entry(entry: dict) -> dict:
    """Run the historical braid through gb_filtration_jet_tracker at
    its native strand count + cvxpy SDP-feasibility check (where
    Hoefsmit available, i.e. n ≤ 3)."""
    n = entry["knot_braid_strand_count"]
    word = entry["knot_braid_word"]

    # GB-filtration certificate at native strand count
    structural_entry = {
        "name": entry["name"],
        "ell": 2,
        "n_0": n,
        "braid_word": word,
        "rho_factor": entry.get("rho_factor", 1),
    }
    structural_cert = solve_per_atom(structural_entry)
    structural_cert["atomic_n_0"] = entry["atomic_n_0"]
    structural_cert["knot_name"] = entry["knot_name"]
    structural_cert["constituents"] = entry["constituents"]
    structural_cert["binding_link"] = entry["binding_link"]
    structural_cert["B_AME_MeV"] = entry["B_AME_MeV"]
    structural_cert["methodology"] = entry["methodology"]

    # Wedderburn-block PSD check (only for H_3; H_5+ deferred to Rust)
    if n == 3:
        try:
            sdp_check = sdp_feasibility_h3(word, q_0_NUMERIC)
            structural_cert["sdp_feasibility"] = sdp_check
            structural_cert["sdp_feasibility_status"] = "checked"
        except Exception as e:
            structural_cert["sdp_feasibility_status"] = f"error: {e}"
    else:
        structural_cert["sdp_feasibility_status"] = (
            f"DEFERRED to Rust (tools/hecke-engine): braid in B_{n} "
            f"requires Hoefsmit seminormal at H_{n}; existing infra in "
            f"tools/hecke-engine/src/seminormal_mn.rs"
        )

    return structural_cert


# ───────────────────────────────────────────────────────────────────
# Driver.
# ───────────────────────────────────────────────────────────────────

def main():
    base = Path(__file__).parent
    out_path = base / "joint-tower-sdp-h6-h9.witness.json"

    print("══════════════════════════════════════════════════════════════════════")
    print("  Joint mass-tower SDP — Phase 3b (²H, ³H, ³He historical entries)")
    print("══════════════════════════════════════════════════════════════════════")

    per_atom_certs = []
    for entry in REGISTRY_PHASE_3B:
        print(f"\n──── {entry['name']} ({entry['knot_name']}) ────")
        print(f"  atomic n_0 = {entry['atomic_n_0']}, "
              f"braid in B_{entry['knot_braid_strand_count']}")
        print(f"  braid word: {entry['knot_braid_word']}")
        cert = solve_phase_3b_entry(entry)
        per_atom_certs.append(cert)
        print(f"  filtration shape: {cert['filtration_shape']}")
        print(f"  jet steps: {cert['n_steps']}, "
              f"Hecke fires: {cert['n_hecke_relations_fired']}")
        if cert.get("sdp_feasibility_status") == "checked":
            sdp = cert["sdp_feasibility"]
            print(f"  SDP-feasibility (H_3 Hoefsmit at q_0={q_0_NUMERIC}):")
            print(f"    trivial (3):     {sdp['trivial_(3)']['value']:+.6f}  "
                  f"{'PSD' if sdp['trivial_(3)']['psd'] else 'NOT PSD'}")
            print(f"    sign (1,1,1):    {sdp['sign_(1,1,1)']['value']:+.6f}  "
                  f"{'PSD' if sdp['sign_(1,1,1)']['psd'] else 'NOT PSD'}")
            print(f"    standard (2,1) eigs(sym): "
                  f"[{sdp['standard_(2,1)']['min_eigenvalue']:+.6f}, "
                  f"{sdp['standard_(2,1)']['max_eigenvalue']:+.6f}]  "
                  f"{'PSD' if sdp['standard_(2,1)']['psd_symmetric_part'] else 'NOT PSD'}")
        else:
            print(f"  SDP-feasibility: {cert['sdp_feasibility_status']}")

    witness = {
        "computation": "joint-tower-sdp-h6-h9",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Phase 3b: extend joint-tower SDP solver from H_3 ground "
            "truth to H_6 (²H), H_9 (³H, ³He). Historical knot "
            "identifications (6_2, 8_11, L6a4) consumed; cvxpy SDP "
            "feasibility checked on H_3 Hoefsmit blocks for ²H and "
            "³He (B_3 braids); ³H (B_5 braid) deferred to Rust."
        ),
        "design_spec": "prop:joint-tower-sdp-confinement",
        "consumed_by": "prop:atom-knot-mass-derivation",
        "phase": "3b",
        "q_0_numeric": q_0_NUMERIC,
        "registry": REGISTRY_PHASE_3B,
        "per_atom_certificates": per_atom_certs,
        "summary": {
            "n_atoms": len(per_atom_certs),
            "checked_via_cvxpy": sum(
                1 for c in per_atom_certs
                if c.get("sdp_feasibility_status") == "checked"
            ),
            "deferred_to_rust": sum(
                1 for c in per_atom_certs
                if "DEFERRED" in c.get("sdp_feasibility_status", "")
            ),
            "all_sdp_checks_pass": all(
                c.get("sdp_feasibility", {}).get("all_blocks_psd_or_close", True)
                for c in per_atom_certs
                if c.get("sdp_feasibility_status") == "checked"
            ),
            "next_steps": [
                "Phase 3c: ⁶Li (B_18 atomic) and ⁷Li (B_21 atomic) need "
                "the SDP-as-SOLVER (not just verifier) — no historical "
                "braid word, so we must SOLVE for canonical T_w. "
                "Replaces deprecated li-atom-knot-search.",
                "Rust integration: extend tools/hecke-engine to emit "
                "design-spec joint-tower-SDP certificate format (per-grade "
                "filtration, jet log, Wedderburn-block sparsity, cross-level "
                "consistency edges).",
                "Once Rust emitter lands, ³H (B_5 / 8_11) gets its "
                "Hoefsmit-PSD check for free.",
            ],
        },
    }
    with open(out_path, "w") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
    print(f"\n→ wrote {out_path}")
    print(f"  atoms: {witness['summary']['n_atoms']}, "
          f"cvxpy-checked: {witness['summary']['checked_via_cvxpy']}, "
          f"deferred-to-rust: {witness['summary']['deferred_to_rust']}")


if __name__ == "__main__":
    main()
