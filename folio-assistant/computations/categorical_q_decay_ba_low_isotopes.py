#!/usr/bin/env python3
"""Categorical Q / decay / B/A recomputation for low isotopes.

NO FITS. NO CALIBRATION. Pulls layer-1 categorical B-values from
the canonical chain (mass-table-ppb witness, derived per
prop:atom-knot-mass-derivation, PR #442 canonical chain) and
computes layer-2 categorical Q-values via

    Q_β⁻(X → Y) = Q_n→p + B_Y − B_X
    Q_n→p       = m_n − m_p − m_e   (currently CODATA — flagged "input")

Layer 1 (B/A) status per atom is family-aware:
  family 1 (D, T, ³He): ρ · m_e · Vol(K) with K from joint-tower
                         SDP search at H_{3A}. **Knot id is currently
                         volume-match (manual-historical), so layer-1
                         output is `partial`, not categorical.**
  family 2 (⁴He):        magic-A formula 2·A·α, α = m_e · 8G.
                         **categorical** (derived).
  family 3 (⁸Be–⁴⁰Ca):    α-cluster recursion with c_αα.
                         **partial** (c_αα coupling still empirical).
  family 4 (⁶Li, ⁷Li, …): T_w not yet derived. Q-value cannot be
                          computed categorically until family-4 SDP
                          lands.

Decay rate (half-life) layer 3 is NOT computed: bottleneck is the
topological invariant N_v in the G_F decomposition (open).

Output: categorical-q-decay-ba-low-isotopes.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from experimental_constants import (
    M_E_MEV,
    M_N_MEV,
    M_P_MEV,
    Q_NEUTRON_MEV,
    Q_NEUTRON_MEV_ERR,
    Q_TRITIUM_MEV,
    Q_TRITIUM_MEV_ERR,
)
from q_parameter import Q as Q_0
from q_parameter import Q_ERR as Q_0_ERR
from witness_base import WitnessBuilder

# ─────────────────────────────────────────────────────────────────────
# Module-level constants (review fix: was inside main())
# ─────────────────────────────────────────────────────────────────────

WITNESS_PATH = Path(__file__).parent / "mass-table-ppb.witness.json"

# Layer-2 reference Q-values (NNDC/ENSDF + branching-qvalues witness for
# decays not yet promoted to experimental_constants.py).
# TODO: promote ⁶He, ⁸Li to experimental_constants.py with explicit ± err.
Q_AME_REFERENCE = {
    "n → p":     (Q_NEUTRON_MEV,  Q_NEUTRON_MEV_ERR),
    "³H → ³He":  (Q_TRITIUM_MEV,  Q_TRITIUM_MEV_ERR),
    "⁶He → ⁶Li": (3.508,          0.001),    # NNDC; not yet in experimental_constants
    "¹⁴C → ¹⁴N": (0.15648,        0.00004),  # mirrors Q_C14_MEV
    "⁸Li → ⁸Be": (16.004,         0.001),    # NNDC; not yet in experimental_constants
}

DECAY_PAIRS = [
    ("n",    "p",    "n → p"),       # free neutron
    ("3H",   "3He",  "³H → ³He"),    # tritium β⁻
    ("6He",  "6Li",  "⁶He → ⁶Li"),   # blocked: ⁶He, ⁶Li are family 4
    ("14C",  "14N",  "¹⁴C → ¹⁴N"),   # blocked: ¹⁴C, ¹⁴N are family 4
    ("8Li",  "8Be",  "⁸Li → ⁸Be"),   # blocked: ⁸Li family 4
]

FAMILY_BY_SYM = {
    "2H": 1, "3H": 1, "3He": 1,
    "4He": 2,
    "8Be": 3, "12C": 3, "16O": 3, "20Ne": 3, "24Mg": 3, "40Ca": 3,
}

# Layer-1 categorical-status per family. Family 1 is "partial" because
# the knot id (6_2, 8_11, L6a4) comes from volume-match census, not yet
# from GB-NF derivation at H_{3A}. Family 3 is also "partial" because
# c_αα coupling is empirical. Only family 2 is fully derived today.
LAYER1_STATUS = {
    1: "partial-knot-id-via-vol-match",
    2: "categorical-derived",
    3: "partial-c-alpha-empirical",
    4: "open",
}

# Layer-2 categorical-status: a Q-value is categorical IFF both inputs
# (B_parent and B_daughter) are layer-1 categorical. If either is
# partial, propagate "partial". If either is open, Q is undefined.
LAYER2_STATUS_RULE = {
    ("categorical-derived",         "categorical-derived"):         "categorical",
    ("categorical-derived",         "partial-knot-id-via-vol-match"): "partial",
    ("partial-knot-id-via-vol-match", "categorical-derived"):         "partial",
    ("partial-knot-id-via-vol-match", "partial-knot-id-via-vol-match"): "partial",
    ("partial-c-alpha-empirical",   "partial-c-alpha-empirical"):   "partial",
    # any pairing involving "open" → undefined (handled in code)
}


def classify_family(sym: str) -> int:
    """Family classification per PR #442 canonical chain."""
    return FAMILY_BY_SYM.get(sym, 4)


def load_layer1_bindings():
    """Pull categorical B-values from mass-table-ppb witness."""
    with open(WITNESS_PATH) as f:
        data = json.load(f)
    out = {}
    for row in data["rows"]:
        fam = classify_family(row["sym"])
        out[row["sym"]] = {
            "Z": row["Z"],
            "N": row["N"],
            "A": row["A"],
            "B_AME_MeV": row["B_AME_MeV"],
            "B_pred_MeV": row["B_pred_MeV"],
            "formula": row["formula"],
            "origin": row["origin"],
            "family": fam,
            "layer1_status": LAYER1_STATUS[fam],
        }
    # Family 4 — open
    for entry in data["atoms_no_assignment"]:
        sym, Z, N, A, B_ame = entry
        out[sym] = {
            "Z": Z, "N": N, "A": A,
            "B_AME_MeV": B_ame,
            "B_pred_MeV": None,
            "formula": None,
            "origin": "family-4-open",
            "family": 4,
            "layer1_status": LAYER1_STATUS[4],
        }
    return out


def categorical_q_beta_minus(parent: str, daughter: str, b: dict):
    """Q_β⁻(X → Y) = Q_n→p + B_Y − B_X.

    Categorical IFF both B_p and B_d are layer-1 categorical.
    Family 1, 3 → "partial" (knot id / c_αα still partial).
    Family 4   → "undefined" (open).
    """
    p = b.get(parent)
    d = b.get(daughter)
    if p is None or d is None:
        return None, "missing-atom"
    if p["B_pred_MeV"] is None or d["B_pred_MeV"] is None:
        return None, f"family-{max(p['family'], d['family'])}-open"
    Q = Q_NEUTRON_MEV + d["B_pred_MeV"] - p["B_pred_MeV"]
    p_status = p["layer1_status"]
    d_status = d["layer1_status"]
    if p_status == LAYER1_STATUS[4] or d_status == LAYER1_STATUS[4]:
        layer2 = "undefined"
    elif p_status == d_status == LAYER1_STATUS[2]:
        layer2 = "categorical"
    else:
        layer2 = "partial"
    return Q, f"layer2-{layer2} (parent={p_status}, daughter={d_status})"


def main():
    bindings = load_layer1_bindings()

    # Layer 1: B/A table
    layer1_rows = []
    for sym, b in bindings.items():
        layer1_rows.append({
            "sym": sym,
            "Z": b["Z"], "N": b["N"], "A": b["A"],
            "family": b["family"],
            "B_AME_MeV": b["B_AME_MeV"],
            "B_pred_MeV": b["B_pred_MeV"],
            "B_per_A_AME_MeV": b["B_AME_MeV"] / b["A"] if b["A"] > 0 else None,
            "B_per_A_pred_MeV": (
                b["B_pred_MeV"] / b["A"] if b["B_pred_MeV"] is not None else None
            ),
            "err_pct": (
                100 * (b["B_pred_MeV"] - b["B_AME_MeV"]) / b["B_AME_MeV"]
                if b["B_pred_MeV"] is not None and b["B_AME_MeV"] > 0 else None
            ),
            "formula": b["formula"],
            "origin": b["origin"],
            "categorical_status": b["layer1_status"],
        })

    # Layer 2: Q-values for β⁻ decay
    layer2_rows = []
    # n → p — direct from CODATA Q_NEUTRON_MEV scaffold
    q_ame_n, q_ame_n_err = Q_AME_REFERENCE["n → p"]
    layer2_rows.append({
        "decay": "n → p",
        "Q_pred_MeV": Q_NEUTRON_MEV,
        "Q_pred_MeV_err": Q_NEUTRON_MEV_ERR,
        "Q_AME_MeV": q_ame_n,
        "Q_AME_MeV_err": q_ame_n_err,
        "err_pct": 100 * (Q_NEUTRON_MEV - q_ame_n) / q_ame_n,
        "categorical_status": (
            "scaffold-from-codata-m_p-m_n-m_e "
            "(joint-tower SDP at H_3 verifies PSD; absolute m_p, m_n "
            "still on TODO via μ_0 calibration)"
        ),
        "formula": "Q_n→p = m_n − m_p − m_e",
    })
    for parent, daughter, label in DECAY_PAIRS[1:]:
        Q, status = categorical_q_beta_minus(parent, daughter, bindings)
        q_ame, q_ame_err = Q_AME_REFERENCE.get(label, (None, None))
        layer2_rows.append({
            "decay": label,
            "Q_pred_MeV": Q,
            "Q_AME_MeV": q_ame,
            "Q_AME_MeV_err": q_ame_err,
            "err_pct": (
                100 * (Q - q_ame) / q_ame
                if Q is not None and q_ame is not None and q_ame != 0
                else None
            ),
            "categorical_status": status,
            "formula": "Q_n→p + B_daughter − B_parent",
        })

    # Build witness via canonical infrastructure (review fix: was manual JSON)
    w = (
        WitnessBuilder(
            "categorical-q-decay-ba-low-isotopes",
            engine="python",
        )
        .set_description(
            "Categorical recomputation of B/A and Q-values for low "
            "isotopes via the PR #442 canonical chain "
            "B(𝔥) = m_e · ρ · tr_M(T_w) | q = q_0. "
            "NO FITS. Layer 1 (B/A) pulls from mass-table-ppb "
            "(SDP-derived for family 2; partial for families 1, 3; "
            "open for family 4). Layer 2 (Q-values) uses "
            "Q_β⁻ = Q_n→p + B_daughter − B_parent. Layer 3 "
            "(decay rates) is NOT computed: bottleneck N_v is open."
        )
        .set_content_block("prop:atom-knot-mass-derivation")
        .add_parameter("q_0", Q_0)
        .add_parameter("q_0_err", Q_0_ERR)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("m_p_MeV", M_P_MEV)
        .add_parameter("m_n_MeV", M_N_MEV)
        .add_parameter("Q_n_to_p_MeV", Q_NEUTRON_MEV)
        .add_parameter("Q_n_to_p_MeV_err", Q_NEUTRON_MEV_ERR)
        .add_data("Q_n_to_p_origin", (
            "m_n − m_p − m_e at CODATA values; SDP at H_3 verifies "
            "structural PSD but does not yet emit absolute mass values"
        ))
        .add_data("B_layer1_source",
                  "folio-assistant/computations/mass-table-ppb.witness.json")
        .add_data("layer1_b_over_a", layer1_rows)
        .add_data("layer2_q_values", layer2_rows)
        .add_data("layer3_decay_rates", {
            "status": "not-computed",
            "reason": (
                "G_F decomposition has open topological invariant "
                "N_v ≈ 1.4·10⁶ (effective crossing count of weak scale). "
                "See folio-assistant/computations/beta-decay-from-q.witness.json "
                "open_computations field. Layer 3 unblocks once N_v is "
                "derived from brane tower structure."
            ),
        })
        .add_data("fits_eliminated", [
            "branching-qvalues.witness.json (Frobenius-positivity filter)",
            "branching-qvalue-chain.witness.json (even/odd regime split)",
            "canonical-mass-table.witness.json (E_0 = 0.782 MeV fit)",
            "low-isotope-mass-table.witness.json (partial-shell f-interpolation)",
        ])
        .add_data("open_items", [
            "GAP 1: replace volume-match knot id (D=6_2, T=8_11, ³He=L6a4) "
            "with GB-NF derivation from H_n SDP — blocked on Clarabel-rs H_5 bug.",
            "GAP 2: derive m_p, m_n absolute scale from joint-tower SDP "
            "(currently only m_e absolute via μ_0 calibration).",
            "GAP 3: family-4 T_w (⁶Li, ⁷Li, ⁹Be, ¹¹B, ¹⁴N, ¹⁹F) — "
            "blocks Q for ⁶He → ⁶Li, ¹⁴C → ¹⁴N, etc.",
            "GAP 4: derive c_αα coupling categorically (currently empirical "
            "2.43 MeV/pair residual in mass-table-ppb).",
            "GAP 5: derive N_v topological invariant — opens layer 3 "
            "(β-decay half-lives).",
        ])
        .add_caveat(
            "Family-1 atoms (D, T, ³He) currently use volume-match knot id "
            "(manual-historical), so layer-1 output is partial, not "
            "categorical. Layer-2 Q-values inherit this status — the "
            "³H → ³He Q-value error is dominated by the ³He B-error "
            "(~0.22 MeV → sign-flips a 0.019 MeV Q)."
        )
        .add_caveat(
            "Family 3 (⁸Be–⁴⁰Ca) c_αα coupling = 2.43 MeV/pair is empirical "
            "(extracted from mass-table-ppb); replace with H_8 SDP derivation."
        )
        .add_caveat(
            "Layer 3 (decay rates) NOT computed — N_v open. Do not infer "
            "half-lives from this witness."
        )
    )
    out_path = w.save()

    # Print human-readable summary tables.
    print("\n" + "=" * 78)
    print("LAYER 1 — B/A for low isotopes (family-aware status)")
    print("=" * 78)
    print(f"{'sym':<6} {'A':>3} {'fam':>4} {'B_AME':>10} {'B_pred':>10} "
          f"{'B/A_pred':>9} {'err%':>7}  status")
    print("-" * 78)
    for r in layer1_rows:
        bp = f"{r['B_pred_MeV']:>10.4f}" if r["B_pred_MeV"] is not None else f"{'—':>10}"
        bpa = (f"{r['B_per_A_pred_MeV']:>9.4f}"
               if r["B_per_A_pred_MeV"] is not None else f"{'—':>9}")
        ep = f"{r['err_pct']:>+7.2f}" if r["err_pct"] is not None else f"{'—':>7}"
        print(f"{r['sym']:<6} {r['A']:>3} {r['family']:>4} "
              f"{r['B_AME_MeV']:>10.4f} {bp} {bpa} {ep}  {r['categorical_status']}")

    print("\n" + "=" * 78)
    print("LAYER 2 — Q-values (β⁻) via Q_n→p + B_d − B_p")
    print("=" * 78)
    print(f"{'decay':<14} {'Q_pred':>10} {'Q_AME':>10} {'err%':>8}  status")
    print("-" * 78)
    for r in layer2_rows:
        qp = f"{r['Q_pred_MeV']:>10.4f}" if r["Q_pred_MeV"] is not None else f"{'—':>10}"
        qa = f"{r['Q_AME_MeV']:>10.4f}" if r["Q_AME_MeV"] is not None else f"{'—':>10}"
        ep = f"{r['err_pct']:>+8.2f}" if r["err_pct"] is not None else f"{'—':>8}"
        print(f"{r['decay']:<14} {qp} {qa} {ep}  {r['categorical_status']}")

    print("\n" + "=" * 78)
    print(f"LAYER 3 — Decay rates: NOT COMPUTED (N_v open).  → {out_path.name}")
    print("=" * 78)


if __name__ == "__main__":
    main()
