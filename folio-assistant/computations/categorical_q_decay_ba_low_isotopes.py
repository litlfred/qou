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
                         SDP search at H_{3A} (currently census-assigned
                         knot id, structurally categorical).
  family 2 (⁴He):        magic-A formula 2·A·α, α = m_e · 8G.
  family 3 (⁸Be–⁴⁰Ca):    α-cluster recursion with c_αα.
  family 4 (⁶Li, ⁷Li, …): T_w not yet derived. Q-value cannot be
                          computed categorically until family-4 SDP
                          lands.

Decay rate (half-life) layer 3 is NOT computed: bottleneck is the
topological invariant N_v in the G_F decomposition (open).

Output: categorical-q-decay-ba-low-isotopes.witness.json
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────
# Categorical inputs
# ─────────────────────────────────────────────────────────────────────

# CODATA scaffold — to be replaced by joint-tower SDP at H_3 for {p, n, e}.
# Until then these are FLAGGED inputs, not categorical predictions.
M_E_MEV = 0.51099895   # joint-tower SDP at H_2 confirms ρ_e = 1, M(e) = 1 in ℚ(q)
M_P_MEV = 938.27208816  # SDP at H_3 verified PSD; absolute mass scale via m_e
M_N_MEV = 939.56542052  # SDP at H_3 verified PSD; absolute mass scale via m_e
Q_N_TO_P = M_N_MEV - M_P_MEV - M_E_MEV  # 0.7823321... MeV

# q_0 — substrate parameter (calibrated by m_e = 3·E_×·μ_0)
Q_0 = 1.1099785955541805

WITNESS_PATH = Path(__file__).parent / "mass-table-ppb.witness.json"


def load_layer1_bindings():
    """Pull categorical B-values from mass-table-ppb witness."""
    with open(WITNESS_PATH) as f:
        data = json.load(f)
    out = {}
    for row in data["rows"]:
        out[row["sym"]] = {
            "Z": row["Z"],
            "N": row["N"],
            "A": row["A"],
            "B_AME_MeV": row["B_AME_MeV"],
            "B_pred_MeV": row["B_pred_MeV"],
            "formula": row["formula"],
            "origin": row["origin"],
            "family": classify_family(row),
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
        }
    return out


def classify_family(row):
    """Family classification per PR #442 canonical chain."""
    sym = row["sym"]
    if sym in {"2H", "3H", "3He"}:
        return 1
    if sym == "4He":
        return 2
    if sym in {"8Be", "12C", "16O", "20Ne", "24Mg", "40Ca"}:
        return 3
    return 4


def categorical_q_beta_minus(parent, daughter, b):
    """Q_β⁻(X → Y) = Q_n→p + B_Y − B_X.

    Categorical IFF both B_p and B_d are categorical (families 1–3).
    Family 4 inputs => Q is undefined (open).
    """
    p = b.get(parent)
    d = b.get(daughter)
    if p is None or d is None:
        return None, "missing-atom"
    if p["B_pred_MeV"] is None or d["B_pred_MeV"] is None:
        return None, f"family-{max(p['family'], d['family'])}-open"
    Q = Q_N_TO_P + d["B_pred_MeV"] - p["B_pred_MeV"]
    return Q, f"family-{p['family']}/{d['family']}-categorical"


def main():
    bindings = load_layer1_bindings()

    # ─────────────────────────────────────────────────────────────────
    # Layer 1: B/A table (categorical predictions)
    # ─────────────────────────────────────────────────────────────────
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
            "categorical_status": (
                "categorical-derived" if b["family"] in (2, 3)
                else "categorical-knot-id-via-vol-match" if b["family"] == 1
                else "open"
            ),
        })

    # ─────────────────────────────────────────────────────────────────
    # Layer 2: Q-values for β⁻ decay (categorical via Q_n→p + B_d − B_p)
    # ─────────────────────────────────────────────────────────────────
    decays = [
        ("n",    "p",    "n → p"),       # free neutron
        ("3H",   "3He",  "³H → ³He"),    # tritium β⁻
        ("6He",  "6Li",  "⁶He → ⁶Li"),   # blocked: ⁶He, ⁶Li are family 4
        ("14C",  "14N",  "¹⁴C → ¹⁴N"),   # blocked: ¹⁴C, ¹⁴N are family 4
        ("8Li",  "8Be",  "⁸Li → ⁸Be"),   # blocked: ⁸Li family 4
    ]
    layer2_rows = []
    Q_AME = {
        "n → p":     0.7823334,
        "³H → ³He":  0.0186,
        "⁶He → ⁶Li": 3.508,
        "¹⁴C → ¹⁴N": 0.156,
        "⁸Li → ⁸Be": 16.004,
    }
    # n → p is special — direct from Q_N_TO_P input
    layer2_rows.append({
        "decay": "n → p",
        "Q_pred_MeV": Q_N_TO_P,
        "Q_AME_MeV": Q_AME["n → p"],
        "err_pct": 100 * (Q_N_TO_P - Q_AME["n → p"]) / Q_AME["n → p"],
        "categorical_status": (
            "input-from-codata-m_p-m_n-m_e "
            "(joint-tower SDP at H_3 verifies PSD, absolute scale "
            "via m_e — derived m_p, m_n still on TODO)"
        ),
        "formula": "Q_n→p = m_n − m_p − m_e",
    })
    for parent, daughter, label in decays[1:]:
        Q, status = categorical_q_beta_minus(parent, daughter, bindings)
        Q_ame = Q_AME.get(label, None)
        layer2_rows.append({
            "decay": label,
            "Q_pred_MeV": Q,
            "Q_AME_MeV": Q_ame,
            "err_pct": (
                100 * (Q - Q_ame) / Q_ame
                if Q is not None and Q_ame is not None and Q_ame != 0
                else None
            ),
            "categorical_status": status,
            "formula": "Q_n→p + B_daughter − B_parent",
        })

    # ─────────────────────────────────────────────────────────────────
    # Assemble witness
    # ─────────────────────────────────────────────────────────────────
    witness = {
        "computation": "categorical-q-decay-ba-low-isotopes",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Categorical recomputation of B/A and Q-values for low "
            "isotopes via the PR #442 canonical chain "
            "B(𝔥) = m_e · ρ · tr_M(T_w) | q = q_0. "
            "NO FITS. Layer 1 (B/A) pulls from mass-table-ppb "
            "(SDP-derived for families 2, 3; volume-match knot id "
            "for family 1; open for family 4). Layer 2 (Q-values) "
            "uses Q_β⁻ = Q_n→p + B_daughter − B_parent. Layer 3 "
            "(decay rates) is NOT computed: bottleneck N_v is open."
        ),
        "design_spec": "prop:atom-knot-mass-derivation",
        "consumed_by": "docs/audits/categorical-vs-fitted-q-decay-ba.md",
        "inputs": {
            "q_0": Q_0,
            "m_e_MeV": M_E_MEV,
            "Q_n_to_p_MeV": Q_N_TO_P,
            "Q_n_to_p_origin": (
                "m_n − m_p − m_e at CODATA values; SDP at H_3 verifies "
                "structural PSD but does not yet emit absolute mass values"
            ),
            "B_layer1_source": "folio-assistant/computations/mass-table-ppb.witness.json",
        },
        "layer1_b_over_a": layer1_rows,
        "layer2_q_values": layer2_rows,
        "layer3_decay_rates": {
            "status": "not-computed",
            "reason": (
                "G_F decomposition has open topological invariant "
                "N_v ≈ 1.4·10⁶ (effective crossing count of weak scale). "
                "See folio-assistant/computations/beta-decay-from-q.witness.json "
                "open_computations field. Layer 3 unblocks once N_v is "
                "derived from brane tower structure."
            ),
        },
        "fits_eliminated": [
            "branching-qvalues.witness.json (Frobenius-positivity filter)",
            "branching-qvalue-chain.witness.json (even/odd regime split)",
            "canonical-mass-table.witness.json (E_0 = 0.782 MeV fit)",
            "low-isotope-mass-table.witness.json (partial-shell f-interpolation)",
        ],
        "open_items": [
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
        ],
        "precision": "f64_numeric_fallback",
        "truncation_eps": 0.0,
    }

    out_path = Path(__file__).parent / "categorical-q-decay-ba-low-isotopes.witness.json"
    with open(out_path, "w") as f:
        json.dump(witness, f, indent=2)
    print(f"Wrote {out_path}")

    # Print human-readable summary tables.
    print("\n" + "=" * 78)
    print("LAYER 1 — Categorical B/A for low isotopes")
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
    print("LAYER 2 — Categorical Q-values (β⁻) via Q_n→p + B_d − B_p")
    print("=" * 78)
    print(f"{'decay':<14} {'Q_pred':>10} {'Q_AME':>10} {'err%':>8}  status")
    print("-" * 78)
    for r in layer2_rows:
        qp = f"{r['Q_pred_MeV']:>10.4f}" if r["Q_pred_MeV"] is not None else f"{'—':>10}"
        qa = f"{r['Q_AME_MeV']:>10.4f}" if r["Q_AME_MeV"] is not None else f"{'—':>10}"
        ep = f"{r['err_pct']:>+8.2f}" if r["err_pct"] is not None else f"{'—':>8}"
        print(f"{r['decay']:<14} {qp} {qa} {ep}  {r['categorical_status']}")

    print("\n" + "=" * 78)
    print("LAYER 3 — Decay rates: NOT COMPUTED (N_v open).")
    print("=" * 78)


if __name__ == "__main__":
    main()
