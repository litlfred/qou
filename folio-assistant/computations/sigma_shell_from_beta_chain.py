#!/usr/bin/env python3
# polynomial_q_not_applicable: pure data + arithmetic; no q-polynomial expansion involved.
"""σ_shell magnitude from compound β-decay chain (P8 from PR #564).

Implements the closed-form extraction of y_target(A_magic) per
`prop:sigma-shell-from-beta-chain-derivation`:

    y_target(A_magic) =
        (Q_β^net - Σ δρ^(k) · m_e · |tr_M(β_k)|) / (m_e · |tr_M(β_ref)|)

This script extracts y_target for the smallest two magic anchors
along the β-stability valley:

  * **A_magic = 2 (deuteron)** — single-link chain. The β-stability
    chain reaching A=2 is just the free-neutron β-decay
    n → p + e^- + ν̄_e, with the deuteron itself being the bound
    final state (binding 2.225 MeV). For this anchor we therefore
    use:
      - chain links: {n}  (one decay link, K=1)
      - reference braid β_ref: free neutron
      - Q_β = 0.78233341 MeV (free-neutron Q-value, AME 2020)
      - δρ^(0) = ρ_K(p) - ρ_K(n) (existing witness)
    See `atomic-mass-via-rho-k.witness.json` for the per-link ρ_K
    and |tr_M| inputs.

  * **A_magic = 8** — currently DEFERRED. Per the user directive
    the chain reaching ¹⁶O (Z=8 doubly-magic) requires per-link
    ρ_K extension to A ∈ {12..16} which is not yet wired in
    `atomic_mass_via_rho_k.py` (the existing table covers only
    p, n, D, T, ³He, ⁴He). AME 2020 Q-values for the candidate
    chains are recorded in this file's `_AME_2020_A8_CANDIDATES`
    block for the follow-up agent. We do NOT fabricate ρ_K values.

Inputs:
  * AME 2020 Q-values  — coded inline with sources
  * `atomic-mass-via-rho-k.witness.json` — for per-link ρ_K, |tr_M|

Output: `sigma-shell-from-beta-chain.witness.json`

References:
  * AME 2020 mass evaluation: M. Wang et al., Chinese Physics C 45,
    030003 (2021). https://www-nds.iaea.org/amdc/ame2020/
  * Free-neutron decay Q-value: PDG / AME 2020 derived value
    Q_β(n) = 0.78233341(50) MeV.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from decimal import Decimal, getcontext
from pathlib import Path

HERE = Path(__file__).parent

# Set high precision for all arithmetic.
getcontext().prec = 50

# CODATA / AME 2020 constants (MeV).
M_E_MEV = Decimal("0.51099895")
M_P_MEV = Decimal("938.27208816")
M_N_MEV = Decimal("939.56542052")
# Free-neutron β-decay Q-value: Q_β(n) = m_n - m_p - m_e = 0.78233341 MeV.
Q_BETA_NEUTRON_MEV = Decimal("0.78233341")

# Predicted target magnitude per HANDOVER-STATUS.md §3c.
# y_target(A_magic) ~ B(A_magic) / (A_magic · m_p).
B_DEUTERON_MEV = Decimal("2.224566110")  # AME 2020 binding energy of D


def _load_rho_k_table() -> dict[str, dict[str, Decimal]]:
    """Load ρ_K(β) and |tr_M(β)| for each atom from the existing witness."""
    src = HERE / "atomic-mass-via-rho-k.witness.json"
    if not src.exists():
        raise FileNotFoundError(f"Required upstream witness missing: {src}")
    data = json.loads(src.read_text())
    out: dict[str, dict[str, Decimal]] = {}
    for row in data["data"]["rows"]:
        out[row["atom"]] = {
            "rho_K": Decimal(row["rho_K_leading_order"]),
            "tr_M": Decimal(row["tr_M_at_q0"]),
            "M_codata_MeV": Decimal(row["M_codata_MeV"]),
            "M_pred_MeV": Decimal(row["M_pred_MeV"]),
        }
    return out


# AME 2020 Q-values for chains reaching A_magic = 8 (Z=8, ¹⁶O is doubly
# magic; the conventional A_magic = 8 anchor is the proton-magic shell
# closure at Z=8). Recorded here for the follow-up agent. Source for
# every Q-value: AME 2020 (Wang et al. 2021, Chinese Physics C 45,
# 030003). https://www-nds.iaea.org/amdc/ame2020/
#
# Standard β-stability chain reaching ¹⁶O along the valley
# (one nucleon flavor swap per step):
#
#   ¹⁶C  →  ¹⁶N  →  ¹⁶O   (β⁻ chain from neutron-rich side)
#
# Q-values (AME 2020 nuclear-data sheets):
#   ¹⁶C → ¹⁶N : Q_β⁻ = 8.010 MeV
#   ¹⁶N → ¹⁶O : Q_β⁻ = 10.420 MeV
#
# To extend coverage to a longer chain reaching ¹⁶O, additional links
# are: ¹⁶B → ¹⁶C (Q_β⁻ ≈ 22.7 MeV, very neutron-rich) — these are not
# required for the binding-energy benchmark but are recorded here.
_AME_2020_A8_CANDIDATES = {
    "chain_to_O16": {
        "links": [
            {"parent": "16C", "daughter": "16N", "Q_beta_MeV": "8.010",
             "source": "AME 2020 (Wang et al. 2021)"},
            {"parent": "16N", "daughter": "16O", "Q_beta_MeV": "10.420",
             "source": "AME 2020 (Wang et al. 2021)"},
        ],
        "terminus": {"atom": "16O", "Z": 8, "N": 8, "A": 16,
                     "binding_MeV": "127.619",
                     "source": "AME 2020 (Wang et al. 2021)"},
        "ref_braid_candidate": "16C",
        "blocker": (
            "Per-link ρ_K and |tr_M(β)| for atoms with A ∈ {12..16} are "
            "not yet computed. atomic_mass_via_rho_k.py covers only "
            "p, n, D, T, ³He, ⁴He. Extend the upstream pipeline first; "
            "do not fabricate ρ_K values for ¹⁶C/¹⁶N/¹⁶O."
        ),
    }
}


def compute_y_target_a2(rho_k_table: dict[str, dict[str, Decimal]]) -> dict:
    """Compute y_target(A_magic = 2) from the trivial deuteron chain.

    Closed form (per `prop:sigma-shell-from-beta-chain-derivation` §Step 4):

        y_target = (Q_β^net - Σ_k δρ^(k) · m_e · |tr_M(β_k)|)
                   / (m_e · |tr_M(β_ref)|)

    For A_magic = 2 (deuteron):
      - chain has K = 1 link: n → p + e^- + ν̄_e
      - δρ^(0) = ρ_K(p) - ρ_K(n)
      - β_0 = neutron (chain-link braid), β_ref = neutron
      - Q_β^net = Q_β(n) + K·m_e = Q_β(n) + m_e
        (electron-rest-mass correction per Step 4 of derivation)
    """
    p = rho_k_table["p"]
    n = rho_k_table["n"]

    # Step a: cumulative AME Q-value, with electron-emission correction.
    # K = 1 electron emitted, so Q_β^net = Q_β(n) + 1·m_e.
    Q_beta_net = Q_BETA_NEUTRON_MEV + Decimal(1) * M_E_MEV

    # Step b: constituent walk Σ δρ^(k) · m_e · |tr_M(β_k)|.
    # Single link; β_0 = n (chain origin braid).
    delta_rho_0 = p["rho_K"] - n["rho_K"]
    constituent_walk = delta_rho_0 * M_E_MEV * n["tr_M"]

    # Step c: divide by m_e · |tr_M(β_ref)|. β_ref = neutron.
    denom = M_E_MEV * n["tr_M"]
    numerator = Q_beta_net - constituent_walk
    y_target = numerator / denom

    # Predicted benchmark: B/(A · m_p).
    y_predicted = B_DEUTERON_MEV / (Decimal(2) * M_P_MEV)

    rel_disc = (y_target - y_predicted) / y_predicted

    return {
        "A_magic": 2,
        "compute_status": "computed",
        "chain_description": (
            "Trivial single-link chain: n → p + e^- + ν̄_e. "
            "Deuteron (Z=N=1) is the bound final state."
        ),
        "K_links": 1,
        "ref_braid": "n",
        "Q_beta_net_MeV": str(Q_beta_net),
        "Q_beta_net_formula": "Q_β(n) + K·m_e = 0.78233341 + 0.51099895",
        "delta_rho_0": str(delta_rho_0),
        "delta_rho_0_formula": "ρ_K(p) - ρ_K(n)",
        "constituent_walk_MeV": str(constituent_walk),
        "denominator_MeV": str(denom),
        "y_target_computed": str(y_target),
        "y_target_predicted_BoverAmp": str(y_predicted),
        "y_target_predicted_formula": "B(D) / (2·m_p) = 2.225 / 1876.54",
        "relative_discrepancy": str(rel_disc),
        "discrepancy_pct": str(rel_disc * Decimal(100)),
        "audit_note": (
            "If |relative_discrepancy| > 1, the derivation has a "
            "structural issue beyond a leading-order correction. "
            "Document but do NOT tune parameters at this layer."
        ),
        "inputs": {
            "Q_beta_neutron_MeV": str(Q_BETA_NEUTRON_MEV),
            "Q_beta_source": "AME 2020 / PDG free-neutron decay",
            "rho_K_p": str(p["rho_K"]),
            "rho_K_n": str(n["rho_K"]),
            "tr_M_n": str(n["tr_M"]),
            "tr_M_p": str(p["tr_M"]),
            "rho_K_source": "atomic-mass-via-rho-k.witness.json",
        },
    }


def main() -> int:
    print("=" * 80)
    print("  σ_shell magnitude from compound β-decay chain — P8")
    print("  Concrete extraction for A_magic ∈ {2, 8}")
    print("=" * 80)

    rho_k_table = _load_rho_k_table()
    print(f"\n  Loaded ρ_K table for atoms: {sorted(rho_k_table.keys())}")

    # A_magic = 2 (deuteron) — fully computed.
    print("\n" + "-" * 80)
    print("  A_magic = 2 (deuteron) — full compute")
    print("-" * 80)
    a2 = compute_y_target_a2(rho_k_table)
    print(f"  Q_β^net           = {a2['Q_beta_net_MeV']} MeV")
    print(f"  δρ^(0)            = {a2['delta_rho_0']}")
    print(f"  constituent walk  = {a2['constituent_walk_MeV']} MeV")
    print(f"  y_target computed = {a2['y_target_computed']}")
    print(f"  y_target predict  = {a2['y_target_predicted_BoverAmp']} (B/(2·m_p))")
    print(f"  rel. discrepancy  = {a2['discrepancy_pct']} %")

    # Audit flag if order of magnitude is off.
    y_computed = Decimal(a2["y_target_computed"])
    y_predicted = Decimal(a2["y_target_predicted_BoverAmp"])
    if y_computed == 0 or y_predicted == 0:
        ratio_log10 = None
    else:
        # Crude order-of-magnitude check: are computed and predicted within 1 dex?
        ratio = abs(y_computed) / abs(y_predicted)
        # log10 via ln(x)/ln(10)
        try:
            from math import log10
            ratio_log10 = log10(float(ratio))
        except Exception:
            ratio_log10 = None
    if ratio_log10 is not None and abs(ratio_log10) > 1.0:
        a2["audit_flag"] = (
            f"CANDIDATE AUDIT FLAG — formula needs refinement. "
            f"|computed/predicted| = 10^{ratio_log10:.2f}, off by more than "
            f"1 order of magnitude from B/(A·m_p) benchmark."
        )
        print(f"\n  ⚠ {a2['audit_flag']}")
    else:
        a2["audit_flag"] = None

    # A_magic = 8 (¹⁶O) — deferred with curated AME data.
    print("\n" + "-" * 80)
    print("  A_magic = 8 (¹⁶O, doubly-magic) — DEFERRED")
    print("-" * 80)
    print("  Per-link ρ_K not yet computed for A ∈ {12..16}.")
    print("  AME 2020 Q-values curated in witness for the follow-up agent.")

    a8 = {
        "A_magic": 8,
        "compute_status": "deferred",
        "blocker": _AME_2020_A8_CANDIDATES["chain_to_O16"]["blocker"],
        "ame_2020_curated_chain": _AME_2020_A8_CANDIDATES["chain_to_O16"],
        "next_step": (
            "Extend atomic_mass_via_rho_k.py to cover A ∈ {12..16} "
            "(¹⁶C, ¹⁶N, ¹⁶O at minimum), then re-run this script."
        ),
    }

    rows = [a2, a8]

    # Summary table.
    summary_table = [
        {
            "A_magic": 2,
            "y_target_computed": a2["y_target_computed"],
            "y_target_predicted": a2["y_target_predicted_BoverAmp"],
            "discrepancy_pct": a2["discrepancy_pct"],
            "status": "computed",
        },
        {
            "A_magic": 8,
            "y_target_computed": "deferred",
            "y_target_predicted": "deferred",
            "discrepancy_pct": "deferred",
            "status": "blocked on upstream ρ_K extension",
        },
    ]

    witness = {
        "computation": "sigma-shell-from-beta-chain",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Concrete extraction of y_target(A_magic) from compound β-decay "
            "chain Q-values per `prop:sigma-shell-from-beta-chain-derivation`. "
            "Closed form: y_target = (Q_β^net - Σ δρ^(k)·m_e·|tr_M(β_k)|) / "
            "(m_e·|tr_M(β_ref)|). A_magic = 2 (deuteron, trivial single-link "
            "n→p chain) is fully computed using existing ρ_K and |tr_M| data "
            "from atomic-mass-via-rho-k.witness.json. A_magic = 8 (¹⁶O) is "
            "DEFERRED: AME 2020 Q-values for the ¹⁶C → ¹⁶N → ¹⁶O chain are "
            "curated in this witness, but per-link ρ_K for A∈{12..16} is "
            "not yet wired in atomic_mass_via_rho_k.py. We do NOT fabricate "
            "ρ_K values. Discrepancy with the B/(A·m_p) benchmark is "
            "documented honestly per user directive — this is a candidate "
            "audit flag, not a fitting opportunity."
        ),
        "engine": "decimal",
        "scriptFile": "sigma_shell_from_beta_chain.py",
        "scriptHash": None,
        "parameters": {
            "magic_anchors": [2, 8, 20, 28, 50, 82, 126],
            "computed_anchors": [2],
            "deferred_anchors": [8, 20, 28, 50, 82, 126],
            "m_e_MeV": str(M_E_MEV),
            "m_p_MeV": str(M_P_MEV),
            "m_n_MeV": str(M_N_MEV),
            "Q_beta_neutron_MeV": str(Q_BETA_NEUTRON_MEV),
            "decimal_precision": 50,
        },
        "data": {
            "summary_table": summary_table,
            "rows": rows,
        },
        "audit_reference": "AUDIT-DEEP-2026-05.md §7 P8",
        "pr": "#564",
        "ame_data_provenance": (
            "AME 2020 mass evaluation, M. Wang, W.J. Huang, F.G. Kondev, "
            "G. Audi, S. Naimi, Chinese Physics C 45, 030003 (2021). "
            "https://www-nds.iaea.org/amdc/ame2020/"
        ),
        "follow_up": (
            "(1) Extend atomic_mass_via_rho_k.py to cover atoms in the "
            "¹⁶C → ¹⁶N → ¹⁶O chain. (2) Re-run this script to populate "
            "the A_magic = 8 row. (3) Repeat for A_magic ∈ {20, 28, 50, "
            "82, 126} as ρ_K coverage extends along the β-stability valley."
        ),
    }
    out = HERE / "sigma-shell-from-beta-chain.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  Wrote {out.name}")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    sys.exit(main())
